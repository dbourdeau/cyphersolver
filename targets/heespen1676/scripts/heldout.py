"""Held-out glossed checks (own code, standard library). usage: python3 -I heldout.py <folder>
Pages 342R (tested with KEY_HB_v1) and 413 (tested with KEY_HB_v2); neither page was used to build the key it tests.
For each glossed group: tokens, valued tokens (by the key file), and two judgements:
 (1) FILED rule: every valued token agrees unless heldout/judgements.tsv lists it as a contradiction; listed allowances
     (spelling) count as agreement, and a second figure counts them against;
 (2) MECHANICAL rule (added here, stricter): after folding case, umlauts and ß, the decoded values must spell the gloss
     exactly, each unvalued token standing for 1-4 letters; the script finds the fewest valued tokens that must be freed
     (treated as unvalued) for the group to spell the gloss. Every freed token is a mechanical contradiction.
Dan Bourdeau's rule (holes count): agreeing tokens over ALL tokens of the glossed groups, valued or not."""
import sys, re, pathlib, functools
F = pathlib.Path(sys.argv[1])
def key(p):
    K = {}
    for l in open(p, encoding='utf-8'):
        q = l.rstrip('\n').split('\t')
        if q[0] == 'tok': K[q[1]] = q[2]
    return K
def fold(s):
    s = s.lower()
    for a, b in (('ä', 'a'), ('ö', 'o'), ('ü', 'u'), ('ß', 'ss'), ('ſ', 's')): s = s.replace(a, b)
    return re.sub('[^a-z]', '', s)
def mech(tk, K, gloss):
    g = fold(gloss); vals = [fold(K[t]) if t in K else None for t in tk]
    @functools.lru_cache(None)
    def f(i, j):
        if i == len(tk): return (0, ()) if j == len(g) else None
        best = None
        v = vals[i]
        if v is not None and g.startswith(v, j):
            r = f(i + 1, j + len(v)); best = r
        for w in range(1, 5):
            if j + w > len(g): break
            r = f(i + 1, j + w)
            if r is None: continue
            c = (r[0] + (v is not None), r[1] + ((tk[i],) if v is not None else ()))
            if best is None or c[0] < best[0]: best = c
        return best
    return f(0, 0)
J = [l.rstrip('\n').split('\t') for l in open(F / 'heldout/judgements.tsv', encoding='utf-8') if not l.startswith('#')]
def groups(page):
    p = F / ('heldout/342R_glosses.tsv' if page == '342R' else 'heldout/413_transcription_glosses.tsv')
    return [l.rstrip('\n').split('\t') for l in open(p, encoding='utf-8') if l.strip() and not l.startswith('#')]
for page, kf in (('342R', 'gloss/KEY_HB_v1.tsv'), ('413', 'gloss/KEY_HB_v2.tsv')):
    K = key(F / kf); G = groups(page)
    con = {(r[1], r[2]) for r in J if r[0] == page and r[3] == 'contradiction'}
    alw = {(r[1], r[2]) for r in J if r[0] == page and r[3] == 'allowance'}
    print('== %s with %s: %d glossed groups' % (page, kf.split('/')[-1], len(G)))
    T = V = C = A = M = 0; mlist = []; vlist = []
    for toks, gl in G:
        tk = toks.split(); v = [t for t in tk if t in K]
        c = sum((gl, t) in con for t in v); a = sum((gl, t) in alw for t in v)
        m = mech(tk, K, gl)
        T += len(tk); V += len(v); C += c; A += a; vlist.append(len(v))
        ms = 'not alignable' if m is None else ('%d (%s)' % (m[0], ' '.join(m[1])) if m[0] else '0')
        if m is None: M += len(v); mlist.append(gl + ': not alignable')
        elif m[0]: M += m[0]; mlist.append('%s: %s' % (gl, ' '.join('%s=%s' % (t, K[t]) for t in m[1])))
        print('  %-14s %-28s -> %-32s tokens %2d valued %2d filed-contra %d allowance %d mechanical-contra %s' % (gl, toks, ' '.join(K.get(t, '[' + t + ']') for t in tk), len(tk), len(v), c, a, ms))
    print('  valued per group: %s = %d; tokens %d (unvalued %d)' % (' + '.join(map(str, vlist)), V, T, T - V))
    print('  FILED rule: agree %d - %d = %d of %d valued = %.2f%%; allowances counted against: %d/%d = %.2f%%' % (V, C, V - C, V, 100 * (V - C) / V, V - C - A, V, 100 * (V - C - A) / V))
    print("  Dan's rule (unvalued tokens are holes): %d/%d = %.2f%% (allowances against: %d/%d = %.2f%%)" % (V - C, T, 100 * (V - C) / T, V - C - A, T, 100 * (V - C - A) / T))
    print('  MECHANICAL rule: %d contradictions -> %d/%d = %.2f%%; %s' % (M, V - M, V, 100 * (V - M) / V, '; '.join(mlist) or 'none'))
