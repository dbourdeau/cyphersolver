"""measure_o4.py (PREREG-O4.md, 25 Nov 2026) = measure_o2.py (bc5d71cd...) with three additions, the measure itself unchanged:
(1) namespace guard: every token must be a key name, NIL, or a transcriber name starting with 't' (struck 'X_' -> NIL);
    anything else aborts BEFORE decoding (no value is shown). (2) z = (M - mean(controls)) / sd(controls), printed for
    information only, not a criterion. (3) JSON summary on stdout last line.
Original docstring: ONE measure of WAINUT's stmauris1548 table.
usage: python3 measure_o2.py TRANSCRIPTION KEY_TSV CORPUS [seed]
TRANSCRIPTION: blind sign names (SIGNS.md), rows '1r L01: ...' (parsed by WAINUT's compare.load: quotes, '.', '/', '(' dropped,
'?' stripped). KEY_TSV: sign<TAB>value ('-' = null), comment lines start with '# '. Signs absent from the key give no letter
and break word coverage. M = share of decoded letters covered by a max-coverage segmentation into lexicon words of 3-15
letters; lexicon = word types of CORPUS (fr-1520s-diplomatic), normalised like the decode (accents off, j->i, v->u, k->c,
w dropped). Controls: 200 tables with the values permuted among the signs of the key (as WAINUT's heldout.py).
PASS iff decoded letters >= 300 AND M >= 0.85 AND M >= max(controls) + 0.30."""
import sys, os, re, random, unicodedata, json, statistics
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'o2-2311', 'wainut-scripts'))
from compare import load
def norm(s):
    s = unicodedata.normalize('NFD', s.lower()); s = ''.join(c for c in s if not unicodedata.combining(c))
    return re.sub('[^a-z]', '', s.replace('j', 'i').replace('v', 'u').replace('k', 'c').replace('w', ''))
def lexicon(path):
    t = open(path, encoding='utf-8', errors='ignore').read()
    return {w for w in (norm(x) for x in re.findall(r"[^\W\d_]+", t)) if 3 <= len(w) <= 15}
def key(path):
    K = {}
    for l in open(path, encoding='utf-8'):
        if not l.strip() or l.startswith('# '): continue
        p = l.rstrip('\n').split('\t')
        if len(p) >= 2: K[p[0]] = '' if p[1] == '-' else norm(p[1])
    return K
def decode(toks, K):
    return ''.join(K[t] if t in K else '|' for t in toks)
def coverage(s, lex):
    tot = 0; cov = 0
    for seg in s.split('|'):
        n = len(seg); tot += n
        if not n: continue
        best = [0] * (n + 1)
        for i in range(1, n + 1):
            b = best[i - 1]
            for L in range(3, min(15, i) + 1):
                if seg[i - L:i] in lex and best[i - L] + L > b: b = best[i - L] + L
            best[i] = b
        cov += best[n]
    return (cov / tot if tot else 0.0), tot
def main():
    tr, kp, cp = sys.argv[1:4]; seed = int(sys.argv[4]) if len(sys.argv) > 4 else 1547
    rows = load(tr); K = key(kp)
    assert not any(k.startswith('t') or k == 'NIL' for k in K), 'key uses the transcriber namespace'
    bad = sorted({t for r in rows.values() for t in r if not (t in K or t == 'NIL' or t.startswith('t') or t.endswith('_'))})
    if bad: sys.exit('ABORT before decoding: names outside key / t-namespace / NIL: ' + ' '.join(bad))
    rows = {k: [('NIL' if t.endswith('_') else t) for t in r] for k, r in rows.items()}
    toks = [t for r in rows.values() for t in r]; lex = lexicon(cp)
    s = decode(toks, K); M, n = coverage(s, lex)
    signs = sorted(K); vals = [K[x] for x in signs]; rng = random.Random(seed); ctrl = []
    for _ in range(200):
        v = vals[:]; rng.shuffle(v); ctrl.append(coverage(decode(toks, dict(zip(signs, v))), lex)[0])
    known = sum(1 for t in toks if t in K)
    print('rows %d tokens %d with a key value %d (%.1f%%) decoded letters %d lexicon %d types' % (len(rows), len(toks), known, 100*known/max(1, len(toks)), n, len(lex)))
    mu = sum(ctrl)/200; sd = statistics.pstdev(ctrl); z = (M - mu) / sd if sd else float('inf')
    print('M %.4f  controls n=200 max %.4f mean %.4f sd %.4f  margin %.4f  z %.2f (information only)' % (M, max(ctrl), mu, sd, M - max(ctrl), z))
    ok = n >= 300 and M >= 0.85 and M >= max(ctrl) + 0.30
    print('VERDICT', 'PASS' if ok else ('NOT MEASURABLE (<300 letters)' if n < 300 else 'FAIL'))
    for k, r in rows.items(): print('%s %s: %s' % (k[0], k[1], ''.join(K.get(t, '?') for t in r)))
    print(json.dumps({'rows': len(rows), 'tokens': len(toks), 'with_value': known, 'letters': n, 'M': round(M, 4),
        'ctrl_max': round(max(ctrl), 4), 'ctrl_mean': round(mu, 4), 'ctrl_sd': round(sd, 4), 'z': round(z, 2), 'seed': seed,
        'verdict': 'PASS' if ok else ('NOT MEASURABLE' if n < 300 else 'FAIL')}))
if __name__ == '__main__': main()
