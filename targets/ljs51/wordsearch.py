"""Word-level search for LJS 51 f. 106v: every cipher word is matched against the vocabulary of the classical
Arabic poetry corpus (lang/corpora/ar-classical-poetry.txt), keeping one consistent one-to-one sign -> letter key.

Beam search over the words, the most constrained first. A word may stay unmatched at a fixed penalty.
Score = sum of log frequencies of the matched words. Prints the best keys and their decodings.

    python targets/ljs51/wordsearch.py --fix H=ا N=و Y=م K=ث M=ل P=ي X=ض [--beam 4000] [--unk -22]
"""
import argparse, collections, math, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, ROOT)
sys.path.insert(0, HERE)
from lang import lm
from solve import read_words


def vocab(minc=2):
    c = collections.Counter()
    with open(os.path.join(ROOT, 'lang', 'corpora', 'ar-classical-poetry.txt'), encoding='utf-8') as fh:
        for line in fh:
            c.update(lm.norm(line, 'arabic28').split())
    tot = sum(c.values())
    return {w: math.log(n / tot) for w, n in c.items() if n >= minc}


def pattern(seq):
    seen = {}
    return tuple(seen.setdefault(x, len(seen)) for x in seq)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--fix', nargs='*', default=[])
    ap.add_argument('--beam', type=int, default=3000)
    ap.add_argument('--unk', type=float, default=-22.0)
    ap.add_argument('--top', type=int, default=8)
    ap.add_argument('--dir', default='rtl')
    a = ap.parse_args()
    words = read_words(os.path.join(HERE, 'transcription.txt'))
    if a.dir == 'ltr':
        words = [w[::-1] for w in words[::-1]]
    fixed = dict(f.split('=') for f in a.fix)
    V = vocab()
    bylen = collections.defaultdict(list)
    for w, lp in V.items():
        bylen[(len(w), pattern(w))].append((w, lp))
    cands = []
    for w in words:
        lst = []
        for pw, lp in bylen.get((len(w), pattern(w)), []):
            if all(fixed.get(s, pw[i]) == pw[i] for i, s in enumerate(w)) and \
               all(pw[i] not in fixed.values() or fixed.get(s) == pw[i] for i, s in enumerate(w)):
                lst.append((pw, lp))
        lst.sort(key=lambda x: -x[1])
        cands.append(lst[:4000])
    order = sorted(range(len(words)), key=lambda i: len(cands[i]))
    beam = [(0.0, dict(fixed), {})]
    for i in order:
        w, nb = words[i], []
        for sc, mp, out in beam:
            inv = {v: k for k, v in mp.items()}
            hit = False
            for pw, lp in cands[i]:
                ok, new = True, None
                for s, ch in zip(w, pw):
                    m = mp.get(s) if new is None else new.get(s)
                    if m is None:
                        owner = (inv if new is None else {v: k for k, v in new.items()}).get(ch)
                        if owner is not None and owner != s:
                            ok = False; break
                        if new is None: new = dict(mp)
                        new[s] = ch
                    elif m != ch:
                        ok = False; break
                if ok:
                    o2 = dict(out); o2[i] = pw
                    nb.append((sc + lp, new if new is not None else mp, o2)); hit = True
            o2 = dict(out); o2[i] = None
            nb.append((sc + a.unk, mp, o2))
        nb.sort(key=lambda x: -x[0])
        seen, beam = set(), []
        for x in nb:
            key = tuple(sorted(x[1].items()))
            if key in seen: continue
            seen.add(key); beam.append(x)
            if len(beam) >= a.beam: break
        print(f'word {i:2d} ({len(cands[i])} cands)  best {beam[0][0]:.1f}', file=sys.stderr)
    for sc, mp, out in beam[:a.top]:
        txt = ' '.join(out[i] if out.get(i) else '[' + ''.join(mp.get(s, '?') for s in words[i]) + ']' for i in range(len(words)))
        print(f'{sc:8.1f}  {txt}')
        print('          ' + ' '.join(f'{k}={v}' for k, v in sorted(mp.items()) if k not in fixed))


if __name__ == '__main__':
    main()
