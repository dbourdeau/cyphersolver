"""Word-lattice reading aid for the third pass: which dictionary words can the digits of a stretch spell under k2d?

  python wordfit.py 64v.10 36 64v.11 4      lattice over 64v.10 pos 36 .. 64v.11 pos 4
  python wordfit.py 64v.12                  the whole line
  python wordfit.py --slip 65r.1            allow one wrong digit per word (shown as word<12>16=di>)

Words come from ../vatican5/it_words.json (30,000 sixteenth-century word forms) plus their degeminated spellings
(the clerk writes tuto, fato, Ingiltera). Each word is walked through a trie from every start position over the
key's code options (probe.options: k2d plus dotted codes where a dot is seen; '*' = dotted code with no dot seen,
penalised). 11 is a free null. The best path maximises word log-frequency; a digit left out costs UNK.
Prints the best path and, per start position, the longest words that fit.
"""
import sys, json, math, re
import probe

UNK, STAR, NULL = -14.0, -5.0, -1.0


def load_words():
    raw = json.load(open('../vatican5/it_words.json', encoding='utf-8'))
    tot = sum(c for _, c in raw)
    W = {}
    for w, c in raw:
        s = math.log(c / tot)
        for v in {w, re.sub(r'([b-df-hj-np-tv-z])\1', r'\1', w)}:
            if v and (v not in W or W[v] < s):
                W[v] = s
    for w in ('ns', 'smta', 'cesarea', 'turco', 'imperatore', 'imperator'):
        W.setdefault(w, math.log(50 / tot))
    return W


def trie_of(W):
    T = {}
    for w in W:
        node = T
        for ch in w:
            node = node.setdefault(ch, {})
        node['$'] = w
    return T


SLIP = -6.0


def fits(i0, i1, T, W, slips=0):
    """[(start, end, word, score, path)] for every dictionary word spelled by FLAT[start:end] inside [i0, i1);
    with slips=1, at most one code per word may be one digit off (probe.slip_options, cost SLIP, marked '!')."""
    res = []
    for s in range(i0, i1):
        stack = [(s, T, 0.0, [], 0)]
        while stack:
            i, node, pen, path, ns = stack.pop()
            if '$' in node and i > s:
                res.append((s, i, node['$'], W[node['$']] + pen, path))
            if i >= i1:
                continue
            opts = probe.options(i) + (probe.slip_options(i) if ns < slips else [])
            for n, c, o, f in opts:
                if c == '_':
                    for ch in 'aeiou':
                        if ch in node:
                            stack.append((i + 1, node[ch], pen - 3, path + [f'_={ch}'], ns))
                    continue
                if not o or i + n > i1:
                    continue
                nd = node
                for ch in o:
                    nd = nd.get(ch) if nd else None
                if nd:
                    stack.append((i + n, nd, pen + (SLIP if f == '!' else STAR if f else 0), path + [f'{c}={o}{f}'],
                                  ns + (f == '!')))
    return res


def main():
    a = [x for x in sys.argv[1:] if x != '--slip']
    slips = 1 if '--slip' in sys.argv else 0
    lab0 = a[0]
    if len(a) == 1:
        i0, i1 = probe.span(lab0)
    else:
        i0 = probe.span(lab0, int(a[1]), int(a[1]))[0]
        i1 = probe.span(a[2], int(a[3]), int(a[3]))[1] if len(a) > 3 else probe.span(lab0)[1]
    W = load_words()
    T = trie_of(W)
    F = fits(i0, i1, T, W, slips)
    by_s = {}
    for f in F:
        by_s.setdefault(f[0], []).append(f)
    best = {i0: (0.0, [])}
    for i in range(i0, i1):
        if i not in best:
            continue
        sc, path = best[i]
        def upd(j, v, p):
            if j <= i1 and (j not in best or best[j][0] < v):
                best[j] = (v, p)
        upd(i + 1, sc + UNK, path + [f'<{probe.tok(probe.FLAT[i])}>'])
        if i + 1 < i1 and probe.FLAT[i][2] == 1 and probe.FLAT[i + 1][2] == 1:
            upd(i + 2, sc + NULL, path + ['|'])
        for s, e, w, v, p in by_s.get(i, []):
            bad = [x for x in p if x.endswith('!')]
            upd(e, sc + v, path + [w + (f'<{bad[0][:-1]}>' if bad else '')])
    print('best:', ' '.join(best[i1][1]), f'({best[i1][0]:.1f})')
    print()
    for s in range(i0, i1):
        ws = sorted(by_s.get(s, []), key=lambda f: (-(f[1] - f[0]), -f[3]))[:8]
        t = probe.FLAT[s]
        print(f'{t[0]}:{t[1]:<3} {probe.tok(t):4}', ', '.join(f'{w}({e - s})' for _, e, w, _, _ in ws))


if __name__ == '__main__':
    main()
