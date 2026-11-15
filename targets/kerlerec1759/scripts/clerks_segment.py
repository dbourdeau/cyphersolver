"""Cut the clerks' running decipherments into one piece per code group WITHOUT Pusch's table where possible.

Usage:
  python3 -I clerks_segment.py <outdir> <seed key_manuscript.tsv | none> [--pusch <table.tsv>] <glossed transcriptions...>

Method (a), clerks' evidence alone. Start from a dictionary D of values already established from the clerks'
glosses (the seed: key/key_manuscript.tsv, the 164 codes of nos. 194 and 228). Align each despatch's code stream
with the clerk's running plaintext using D only (kcommon-style dynamic programme; codes not in D take a free slice).
A code not in D is FORCED when both neighbouring groups matched a D value and the clerk's text between them is
exactly the free slice it took: the pieces must tile the clerk's word, so that slice is its value. Forced values are
collected over all despatches; a code is added to D when its forced readings agree (one reading, or a strict
majority). Repeat until nothing changes. Every pair whose code ends up in D and whose group matched its D value is
basis 'a'.

Method (b), with Pusch's table as dictionary. Codes still outside D are aligned with Pusch 2008 Table 2 as the
dictionary (local file, not in this folder); a group whose clerk's slice equals Pusch's value is basis 'b'. The
plaintext of every pair is still the clerk's.

Also: leave-one-out on the seed. Each seed code is removed from D in turn (with D otherwise final) and the
alignment rerun; if the code is then forced to its seed value from the new pages, its seed value is re-derived
from clerks' evidence alone ('seed_rederived').

Writes: pairs_more.tsv (one row per group), clerks_values.tsv (code, value, basis, n pairs, locations),
segment_log.txt.
"""
import os, sys
from collections import Counter, defaultdict
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kcommon import parse, norm, load_table

INF = 1e18


def align_pos(groups, text, table, free_cost=3.0, skip_cost=1.6, empty_cost=3.5, maxlen=12):
    """As kcommon.align, but returns (group_index, j0, j1, how) with text positions."""
    n, m = len(groups), len(text)
    dp = [[INF] * (m + 1) for _ in range(n + 1)]
    bk = [[None] * (m + 1) for _ in range(n + 1)]
    dp[0][0] = 0.0
    for i in range(n + 1):
        row = dp[i]
        for j in range(m + 1):
            c = row[j]
            if c >= INF:
                continue
            if j < m and c + skip_cost < dp[i][j + 1]:
                dp[i][j + 1] = c + skip_cost
                bk[i][j + 1] = ('skip', i, j)
            if i == n:
                continue
            g = groups[i]
            cands = []
            if g['kind'] == 'code' and g['code'] in table:
                for v in table[g['code']]:
                    if v and text.startswith(v, j):
                        cands.append((len(v), 0.0, 'match'))
                for L in range(1, min(maxlen, m - j) + 1):
                    cands.append((L, free_cost + 2.0 + 0.15 * L, 'conflict'))
            elif g['kind'] in ('num', 'clear'):
                v = norm(g['text'])
                if v and text.startswith(v, j):
                    cands.append((len(v), 0.0, 'match'))
                cands.append((0, 0.5, 'empty'))
            else:
                for L in range(1, min(maxlen, m - j) + 1):
                    cands.append((L, free_cost + 0.15 * L, 'free'))
            cands.append((0, empty_cost, 'empty'))
            for L, cost, how in cands:
                if c + cost < dp[i + 1][j + L]:
                    dp[i + 1][j + L] = c + cost
                    bk[i + 1][j + L] = (how, i, j)
    i, j = n, m
    out = []
    while (i, j) != (0, 0):
        how, pi, pj = bk[i][j]
        if how != 'skip':
            out.append((pi, pj, j, how))
        i, j = pi, pj
    out.reverse()
    return out


def load_docs(paths):
    docs = []
    for path in paths:
        desp = os.path.basename(path).replace('glossed_', '').replace('.txt', '')
        groups, locs, text = [], [], ''
        for p in parse(path):
            for L in p['lines']:
                text += norm(L['gloss'])
                for k, g in enumerate(L['codes']):
                    groups.append(g)
                    locs.append((p['page'], p['folio'], L['n'], k + 1))
        docs.append((desp, groups, locs, text))
    return docs


def forced_candidates(docs, D):
    """Return {code: Counter(value)} of forced slices, and the alignments."""
    cand = defaultdict(Counter)
    where = defaultdict(list)
    for desp, groups, locs, text in docs:
        out = align_pos(groups, text, D)
        by_g = {gi: (j0, j1, how) for gi, j0, j1, how in out}
        for gi, g in enumerate(groups):
            if g['kind'] != 'code' or g['code'] in D or gi not in by_g:
                continue
            j0, j1, how = by_g[gi]
            if how != 'free':
                continue
            prv, nxt = by_g.get(gi - 1), by_g.get(gi + 1)
            if not prv or not nxt or prv[2] != 'match' or nxt[2] != 'match':
                continue
            if prv[1] != j0 or nxt[0] != j1:      # chars skipped inside the gap: not forced
                continue
            v = text[j0:j1]
            if 1 <= len(v) <= 12:
                cand[g['code']][v] += 1
                where[(g['code'], v)].append('%s %s l.%s g.%s' % ((desp[:5],) + locs[gi][1:]))
                if g['top']:
                    cand[g['top']][v] += 1
                    where[(g['top'], v)].append('%s %s l.%s g.%s (upper)' % ((desp[:5],) + locs[gi][1:]))
    return cand, where


def accept(cnt):
    vals = cnt.most_common()
    if len(vals) == 1 or vals[0][1] > sum(c for _, c in vals[1:]):
        return vals[0][0]
    return None


def main():
    outdir = sys.argv[1]
    seedp = sys.argv[2]
    rest = sys.argv[3:]
    pusch = None
    if rest and rest[0] == '--pusch':
        pusch = load_table(rest[1]); rest = rest[2:]
        pusch[208] = ['cu']            # OCR slip in our extraction of his table; his prose gives cu (p. 469)
    docs = load_docs(rest)
    log = []
    D = {}
    seed = {}
    if seedp != 'none':
        for l in list(open(seedp, encoding='utf-8')):
            if l.startswith('#') or l.startswith('code\t') or not l.strip():
                continue
            f = l.rstrip('\n').split('\t')
            vals = {norm(f[1])}
            try:
                vals |= {norm(k) for k in eval(f[3], {}, {}).keys()}
            except Exception:
                pass
            seed[int(f[0])] = sorted(vals, key=lambda v: (v != norm(f[1]), v))
        D = {c: v[:] for c, v in seed.items()}
    basis = {c: 'seed' for c in D}
    first = {}
    it = 0
    contested = {}
    while True:
        while True:
            it += 1
            cand, where = forced_candidates(docs, D)
            new = {}
            for c, cnt in cand.items():
                v = accept(cnt)
                if v is not None and c not in D and c not in contested:
                    new[c] = v
            log.append('iteration %d: %d codes forced' % (it, len(new)))
            if not new or it > 40:
                break
            for c, v in new.items():
                D[c] = [v]; basis[c] = 'a'; first[c] = (cand[c], where[(c, v)][:3])
        # consistency: a forced value must hold at the code's other occurrences. Where the clerk's text at the
        # code's occurrences conflicts with the forced value at least as often as it matches, withdraw the value
        # (contested) and redo the forcing without it.
        mc = defaultdict(Counter)
        for desp, groups, locs, text in docs:
            for gi, j0, j1, how in align_pos(groups, text, D):
                g = groups[gi]
                if g['kind'] == 'code' and basis.get(g['code']) == 'a':
                    mc[g['code']][how] += 1
        drop = [c for c in mc if mc[c]['conflict'] >= max(1, mc[c]['match'])]
        log.append('consistency pass: %d forced values withdrawn %s' % (
            len(drop), ['%d=%s (%d match, %d conflict)' % (c, D[c][0], mc[c]['match'], mc[c]['conflict']) for c in drop]))
        if not drop:
            break
        for c in drop:
            contested[c] = (D[c][0], dict(mc[c]))
            del D[c]; del basis[c]
    # leave-one-out on the seed, in windows of 12 groups either side of each occurrence (cut at the positions
    # of the final alignment with D), so that each test is a local realignment
    rederived = {}
    finals = [align_pos(groups, text, D) for desp, groups, locs, text in docs]
    occ = defaultdict(list)
    for di, (desp, groups, locs, text) in enumerate(docs):
        for gi, g in enumerate(groups):
            if g['kind'] == 'code':
                occ[g['code']].append((di, gi))
                if g['top']:
                    occ[g['top']].append((di, gi))
    for c in sorted(seed):
        D2 = {k: v for k, v in D.items() if k != c}
        wdocs = []
        for di, gi in occ.get(c, []):
            desp, groups, locs, text = docs[di]
            pos = {g2: (j0, j1) for g2, j0, j1, how in finals[di]}
            a, b = max(0, gi - 12), min(len(groups), gi + 13)
            while a > 0 and a not in pos: a -= 1
            while b < len(groups) and (b - 1) not in pos: b += 1
            j0 = pos[a][0] if a in pos else 0
            j1 = pos[b - 1][1] if (b - 1) in pos else len(text)
            wdocs.append((desp, groups[a:b], locs[a:b], text[j0:j1]))
        cand, where = forced_candidates(wdocs, D2)
        if c in cand:
            v = accept(cand[c])
            rederived[c] = (v, dict(cand[c]), v in seed[c] if v else False)
    # final alignment with D (basis a) and, if given, Pusch for the codes outside D (basis b)
    dict_b = dict(D)
    if pusch:
        for c, v in pusch.items():
            if c not in dict_b:
                dict_b[c] = v
    rows = []
    for desp, groups, locs, text in docs:
        out = align_pos(groups, text, dict_b)
        for gi, j0, j1, how in out:
            g = groups[gi]
            pg, fo, ln, pos = locs[gi]
            sl = text[j0:j1]
            if g['kind'] != 'code':
                b = '-'
            elif g['code'] in D:
                b = ('a' if basis[g['code']] == 'a' else 'seed') if how == 'match' else '-'
            elif how == 'match':
                b = 'b'
            else:
                b = '-'
            rows.append((desp, pg, fo, ln, pos, g['raw'], g['code'] if g['code'] is not None else '', g['top'] or '',
                         sl, how, b))
    with open(os.path.join(outdir, 'pairs_more.tsv'), 'w', encoding='utf-8') as f:
        f.write('# One row per code group of the further glossed despatches. clerk_plain = the clerk\'s text cut to this\n')
        f.write('# group. basis: seed = code already in key/key_manuscript.tsv and the clerk\'s piece equals that value;\n')
        f.write('# a = value forced by the tiling of the clerk\'s text between two known groups (clerks\' evidence alone);\n')
        f.write('# b = piece cut with Pusch 2008 Table 2 as dictionary (the plaintext is still the clerk\'s);\n')
        f.write('# - = no pair (lost, numeral, conflict with the key, or not assignable).\n')
        f.write('despatch\timage\tfolio\tline\tpos\traw\tcode\ttop\tclerk_plain\thow\tbasis\n')
        for r in rows:
            f.write('\t'.join(str(x) for x in r) + '\n')
    # values table
    per = defaultdict(Counter); locs_by = defaultdict(list)
    for r in rows:
        if r[10] in ('a', 'b', 'seed') and r[6] != '':
            for c in [r[6]] + ([r[7]] if r[7] else []):
                per[(int(c), r[10] if r[10] != 'seed' else 'seed')][r[8]] += 1
                locs_by[int(c)].append('%s %s l.%s g.%s' % (r[0][:5], r[2], r[3], r[4]))
    with open(os.path.join(outdir, 'clerks_values.tsv'), 'w', encoding='utf-8') as f:
        f.write('code\tvalue\tbasis\tn_pairs_new\treadings\tfirst_locations\n')
        for c in sorted(set(D) | {k[0] for k in per}):
            if c in D:
                bs = basis[c]
                cnt = per.get((c, 'a' if bs == 'a' else 'seed'), Counter())
                v = D[c][0]
            else:
                bs = 'b'
                cnt = per.get((c, 'b'), Counter())
                if not cnt:
                    continue
                v = cnt.most_common(1)[0][0]
            f.write('%d\t%s\t%s\t%d\t%s\t%s\n' % (c, v, bs, sum(cnt.values()), dict(cnt), '; '.join(locs_by[c][:3])))
    with open(os.path.join(outdir, 'seed_rederived.tsv'), 'w', encoding='utf-8') as f:
        f.write('# Leave-one-out: each seed code removed from the dictionary, the new pages realigned; forced value.\n')
        f.write('code\tseed_value\tforced_value\tforced_readings\tsame\n')
        for c, (v, cnt, same) in sorted(rederived.items()):
            f.write('%d\t%s\t%s\t%s\t%s\n' % (c, seed[c][0], v, cnt, same))
    na = sum(1 for c in basis if basis[c] == 'a')
    log.append('seed codes %d; codes added from clerks alone (a) %d; codes with a (b) pair only %d' % (
        len(seed), na, len({k[0] for k in per if k[1] == 'b'})))
    log.append('seed codes re-derived by leave-one-out with the same value: %d of %d tested (%d forced at all)' % (
        sum(1 for v in rederived.values() if v[2]), len(seed), len(rederived)))
    c = Counter(r[10] for r in rows if r[6] != '')
    log.append('group rows by basis: %s' % dict(c))
    log.append('contested (withdrawn) forced values: %s' % contested)
    open(os.path.join(outdir, 'segment_log.txt'), 'w').write('\n'.join(log) + '\n')
    print('\n'.join(log))


if __name__ == '__main__':
    main()
