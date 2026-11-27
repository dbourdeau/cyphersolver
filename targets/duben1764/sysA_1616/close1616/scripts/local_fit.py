"""Which value does the alignment of the two letters with their decipherments impose on a group?

usage (from targets/duben1764/):
  python3 -I sysA_1616/close1616/scripts/local_fit.py <key_c01.json> <align_1764.json> <align_1765.json> > fits.jsonl

Input: the two --json outputs of strict_align.py with key_c01 alone (key_c01 is not changed).
For every group type that has no value in key_c01, or whose key_c01 value equals its witness letters at none of its
occurrences in the two letters:
1. each occurrence gets a window: from the nearest group before it, at least two places back, that key_c01 gives
   exactly, to the same after it; the window's witness letters are fixed by those two anchors;
2. candidate values are the strings of 1-9 letters found in the windows of *every* occurrence;
3. for each candidate the window is re-aligned (same costs as strict_align.py) with the candidate put in, and the
   candidate is kept if the group then takes exactly the candidate's letters at every occurrence;
4. among kept candidates the one with the lowest total window cost wins; a tie, or no kept candidate, is reported.
A window that cannot be anchored (no exact group near) is reported and the group is not fitted.
"""
import json, sys
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from strict_align import align  # noqa: E402


def windows(d, g):
    gs = d['groups']
    out = []
    for i, x in enumerate(gs):
        if x['g'] != g:
            continue
        a = i - 2
        while a >= 0 and gs[a]['kind'] != 'exact':
            a -= 1
        b = i + 2
        while b < len(gs) and gs[b]['kind'] != 'exact':
            b += 1
        if a < 0 or b >= len(gs) or b - a > 14:
            out.append(None)
            continue
        out.append((a, b, i))
    return out


def run(clear, d, win, gval):
    a, b, i = win
    gs = d['groups']
    j0, j1 = gs[a]['j1'], gs[b]['j0']
    seg = clear[j0:j1]
    vals = []
    for k in range(a + 1, b):
        vals.append(gval if k == i else (gs[k]['value'] if gs[k]['value'] else None))
    try:
        spans, owner, end, cost = align(vals, seg, False)
    except TypeError:  # no monotone path (a candidate too long for the window)
        return '', 'none', float('inf'), seg
    s = spans[i - a - 1]
    return seg[s[0]:s[1]], s[2], cost, seg


def main():
    key = {g: (v[0] if v else '') for g, v in json.load(open(sys.argv[1])).items()}
    D = [json.load(open(p)) for p in sys.argv[2:4]]
    exact = set()
    types = {}
    for d in D:
        for x in d['groups']:
            if x['kind'] == 'exact':
                exact.add(x['g'])
            types.setdefault(x['g'], 0)
            types[x['g']] += 1
    for g in sorted(types, key=lambda t: int(t) if t.isdigit() else 9999):
        if g == '???' or (key.get(g) and g in exact):
            continue
        occ = []
        for di, d in enumerate(D):
            for w in windows(d, g):
                occ.append((di, w))
        rec = {'group': g, 'key_c01': key.get(g) or None, 'n_occ': len(occ)}
        if any(w is None for _, w in occ) or not occ:
            rec['result'] = 'not anchored'
            print(json.dumps(rec, ensure_ascii=False)); continue
        # candidate strings present in every window
        cands = None
        for di, w in occ:
            _, _, _, seg = run(W[di], D[di], w, None)
            subs = {seg[p:p + L] for L in range(1, 10) for p in range(0, max(0, len(seg) - L + 1))}
            cands = subs if cands is None else cands & subs
        kept = []
        for c in sorted(cands):
            tot, ok, hits = 0.0, True, []
            for di, w in occ:
                got, kind, cost, _ = run(W[di], D[di], w, c)
                if not (kind == 'exact' and got == c):
                    ok = False; break
                tot += cost
            if ok:
                kept.append((round(tot, 2), c))
        kept.sort()
        base = sum(run(W[di], D[di], w, key.get(g) or None)[2] for di, w in occ)
        rec['base_cost'] = round(base, 2)
        rec['kept'] = kept[:5]
        if not kept:
            rec['result'] = 'no value fits every occurrence'
        elif len(kept) > 1 and kept[0][0] == kept[1][0]:
            rec['result'] = 'tie'
        else:
            rec['result'] = 'fit'
            rec['value'] = kept[0][1]
            rec['gain'] = round(base - kept[0][0], 2)
        rec['where'] = ['%s %s' % (D[di]['summary']['letter'], D[di]['groups'][w[2]]['line']) for di, w in occ]
        print(json.dumps(rec, ensure_ascii=False))


if __name__ == '__main__':
    W = []
    import strict_align as sa
    # witness strings, rebuilt exactly as strict_align.py builds them
    for letter in ('1764-03-06', '1765-11-15'):
        words = sa.clear_words_1764('tx/p1764-03-06.txt') if letter == '1764-03-06' else sa.clear_words_1765('tx/g1765-11-15.txt')
        W.append(''.join(sa.norm(w['w']) for w in words))
    main()
