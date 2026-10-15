"""Write docs/reveal/morosini1589.json: a stretch of R53 decoded sign by sign with Lasry's F22b key.

Uses the decoder of ../morosini1588/decrypt.py (same beam search, F22b values), keeping each segment's figures.
usage: python reveal.py START N    (START = index of the first decoded segment, N = number of segments)
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'morosini1588'))
import decrypt as D  # noqa: E402


def segments(items, beam=400):
    """decrypt.decode with the F22b key, returning [(figures, text)] instead of the joined text."""
    codes, nom = D.CODES_B, D.NOM_B
    start = 0
    for x in D.enc('ente'):
        start = (start * D.A + x) % (D.A ** (D.K - 1))
    n = len(items)
    states = [dict() for _ in range(n + 1)]
    states[0][start] = (0.0, None)
    for p in range(n):
        if not states[p]:
            continue
        best = sorted(states[p].items(), key=lambda kv: -kv[1][0])[:beam]
        for ctx, (sc, _) in best:
            it = items[p]
            moves = []
            if isinstance(it, tuple):
                pt = nom.get(it[1])
                moves.append((1, '[' + pt.upper() + ']' if pt else '[' + it[1] + '?]', D.enc(pt) if pt else [], 0.0 if pt else -6.0))
            else:
                for L in (1, 2, 3):
                    seg = items[p:p + L]
                    if len(seg) < L or not all(isinstance(x, str) for x in seg):
                        break
                    for pt, pen in codes.get(''.join(seg), []):
                        moves.append((L, pt, D.enc(pt), pen))
                if not moves:
                    moves.append((1, '?', [], -12.0))
            for L, txt, chars, pen in moves:
                nctx, s = D.step(ctx, chars)
                ns = sc + s + pen
                old = states[p + L].get(nctx)
                if old is None or ns > old[0]:
                    states[p + L][nctx] = (ns, (p, ctx, txt))
    q, ctx = n, max(states[n].items(), key=lambda kv: kv[1][0])[0]
    out = []
    while states[q][ctx][1] is not None:
        p, pctx, txt = states[q][ctx][1]
        fig = items[p:q]
        g = ''.join(x[1] + '̇' if isinstance(x, tuple) else x for x in fig)
        if fig and isinstance(fig[0], tuple):
            g = fig[0][1][0] + '̇' + fig[0][1][1:]
        out.append((g, txt))
        q, ctx = p, pctx
    return out[::-1]


def main():
    start, num = int(sys.argv[1]), int(sys.argv[2])
    f = os.path.join(HERE, 'decode', 'DOC_R53_D1717_1717.txt')
    (img, items), = D.parse(f, dot_first=True)
    segs = segments(items)[start:start + num]
    toks = []
    for g, t in segs:
        if t.startswith('['):
            toks.append({'g': g, 'p': t.strip('[]').lower(), 'cls': 'unk' if t.endswith('?]') else 'code'})
        elif t == '?':
            toks.append({'g': g, 'p': '?', 'cls': 'unk'})
        else:
            toks.append({'g': g, 'p': t})
    out = {
        'slug': 'morosini1589',
        'anchor': 'r53-tours-spring-1589',
        'title': "Tours, spring 1589: 'heretics and Catholics' at court",
        'caption': "A stretch of R53 (Francia 22/32, image 499v) decoded with George Lasry's partial F22b key by the "
                   "segmenting decoder; the division into units is the language model's choice, and stretches the "
                   "partial key does not cover come out as near-words.",
        'unit': 'figures',
        'key_note': "Lasry's F22b reconstruction (DECODE R53 D3187, 2020), one- and two-figure syllables, no nulls; "
                    "a dot on the first figure marks a nomenclator code.",
        'tokens': toks,
    }
    path = os.path.join(HERE, '..', '..', 'docs', 'reveal', 'morosini1589.json')
    json.dump(out, open(path, 'w', encoding='utf-8', newline='\n'), indent=1, ensure_ascii=False)
    print(''.join(t['p'] if t.get('cls') != 'code' else '[' + t['p'] + ']' for t in toks))
    print(len(toks), 'tokens ->', path)


if __name__ == '__main__':
    main()
