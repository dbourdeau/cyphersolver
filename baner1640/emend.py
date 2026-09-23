"""Search misread figures in an unread stretch: every token may be replaced by a visually confusable value (one or two
digit confusions of this hand), at most N substitutions per stretch; decodings ranked by the de-1640s model in context.

    python emend.py S5 61 74 [--subs 2] [--ctx 12] [--top 25]
"""
import argparse, itertools, json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..'))
from lang import lm

CONF = {'0': '68', '1': '74', '2': '7', '3': '58', '4': '9', '5': '38', '6': '80', '7': '12', '8': '360', '9': '4'}


def alts(t, key):
    out = set()
    for i, d in enumerate(t):
        for c in CONF.get(d, ''):
            v = t[:i] + c + t[i + 1:]
            if v in key: out.add(v)
    return sorted(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('seg'); ap.add_argument('a', type=int); ap.add_argument('b', type=int)
    ap.add_argument('--subs', type=int, default=2); ap.add_argument('--ctx', type=int, default=12)
    ap.add_argument('--top', type=int, default=25)
    ap.add_argument('--free', default='', help='comma-separated values treated as unknown (any letter)')
    a = ap.parse_args()
    key = json.load(open(os.path.join(HERE, 'key.json'), encoding='utf-8'))
    free = set(x for x in a.free.split(',') if x)
    m = lm.load('de-1640s', order=5, spaces=False)
    toks = [l.split()[1:] for l in open(os.path.join(HERE, 'ct_neal.txt')) if l.startswith(a.seg + ' ')][0]
    dec = lambda t: key.get(t, '') if len(t) < 3 else ''
    left = ''.join(dec(t) for t in toks[max(0, a.a - a.ctx):a.a])
    right = ''.join(dec(t) for t in toks[a.b + 1:a.b + 1 + a.ctx])
    span = toks[a.a:a.b + 1]
    res = []
    idx = range(len(span))
    for n in range(a.subs + 1):
        for pos in itertools.combinations(idx, n):
            choices = [alts(span[i], key) if i in pos else [span[i]] for i in idx]
            for combo in itertools.product(*choices):
                letters = [key.get(t, '?') for t in combo]
                frees = [i for i, t in enumerate(combo) if t in free]
                for fill in itertools.product(*[m.alpha for _ in frees]) if frees else [()]:
                    L = list(letters)
                    for i, c in zip(frees, fill): L[i] = c
                    s = left + ''.join(L) + right
                    res.append((m.score(s) - 0.0 * n, n, ''.join(L), ' '.join(combo)))
    res.sort(reverse=True)
    seen = set()
    for sc, n, txt, combo in res:
        if txt in seen: continue
        seen.add(txt)
        print(f'{sc:8.2f} subs={n} {left}|{txt}|{right}   {combo}')
        if len(seen) >= a.top: break


if __name__ == '__main__':
    main()
