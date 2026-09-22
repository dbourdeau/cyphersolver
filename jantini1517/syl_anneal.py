"""Anneal the 1517-19 Ferrarese two-tier cipher as a syllabary.

Model (from the R1130/4c pairing in caprile1519/pairX): a column upper/base gives C(upper) + V(base);
a bracket-L sign [x] gives a free short string S(x) (a CV syllable). Score = LM log-prob + BONUS per char
(offsets the preference of total log-prob for short output).
usage: python syl_anneal.py t1126.txt [restarts] [iters] [seed-json]
"""
import json, os, random, re, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
import numpy as np
from lang import lm

M = lm.load('it-cinquecento', order=5, spaces=False)
BONUS = 2.3
LAM = 1.0
_ref = np.bincount(M.encode(lm.norm(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'lang', 'corpora', 'it-renaissance.txt'), encoding='utf8').read()[:2000000], 'early', spaces=False)), minlength=M.A) + 1.0
REF = np.log(_ref / _ref.sum())
CONS = list('bcdfglmnpqrstuz') + ['', 'a', 'e', 'i', 'o', 'ch', 'gh', 'qu', 'gn', 'h', 'x']
VOW = ['', 'a', 'e', 'i', 'o', 'u']
SYL = [c + v for c in list('bcdfglmnpqrstuz') + ['ch', 'qu', 'gn', 'gl'] for v in 'aeiou'] + list('aeiou') + \
      [c + v + 'r' for c in 'ptd' for v in 'aeo'] + ['per', 'con', 'in', 'non', 'et', 'de', 'il', 'la', 'che']


def load(path):
    segs, cur = [], []
    for line in open(path, encoding='utf8'):
        if not re.match(r'R11\d\d P\d L|R11\d\d L', line):
            continue
        s = re.sub(r'\{struck:[^}]*\}', ' ', line.split(':', 1)[1])
        s = re.sub(r'\[clear:[^\]]*\]', ' ', s)
        for c in s.split():
            c = c.replace('?', '')
            if '#' in c or '/' not in c:
                if cur: segs.append(cur); cur = []
                continue
            up, base = c.split('/', 1)
            if base.startswith('['):
                cur.append(('B', base.strip('[]')))
            else:
                cur.append(('C', up, base))
    if cur: segs.append(cur)
    return segs


def render(segs, K):
    out = []
    for seg in segs:
        t = []
        for tok in seg:
            if tok[0] == 'B':
                t.append(K['B'][tok[1]])
            else:
                t.append(K['U'][tok[1]] + K['V'][tok[2]])
        out.append(t)
    return out


def score(segs, K):
    tot, allx = 0.0, []
    for t in render(segs, K):
        x = M.encode(''.join(t))
        allx.append(x)
        tot += M.score_idx(x) + BONUS * len(x)
    x = np.concatenate(allx)
    c = np.bincount(x, minlength=M.A) + 0.5
    q = c / c.sum()
    kl = float((q * (np.log(q) - REF)).sum())
    return tot - LAM * len(x) * kl * 5


def main():
    path = sys.argv[1]
    R = int(sys.argv[2]) if len(sys.argv) > 2 else 4
    N = int(sys.argv[3]) if len(sys.argv) > 3 else 40000
    seed = json.load(open(sys.argv[4])) if len(sys.argv) > 4 else {}
    segs = load(path)
    ups = sorted({t[1] for s in segs for t in s if t[0] == 'C'} - {'-'})
    bases = sorted({t[2] for s in segs for t in s if t[0] == 'C'})
    brs = sorted({t[1] for s in segs for t in s if t[0] == 'B'})
    print(len(segs), 'segments', sum(map(len, segs)), 'tokens;', len(ups), 'uppers', len(bases), 'bases', len(brs), 'brackets')
    best = None
    for r in range(R):
        rnd = random.Random(r)
        K = {'U': {u: rnd.choice(CONS) for u in ups}, 'V': {b: rnd.choice(VOW) for b in bases},
             'B': {b: rnd.choice(SYL) for b in brs}}
        K['U']['-'] = ''
        for part in ('U', 'V', 'B'):
            K[part].update(seed.get(part, {}))
        fixed = {(p, k) for p in seed for k in seed[p]}
        cur = score(segs, K)
        T0 = float(os.environ.get("T0", "20"))
        for i in range(N):
            T = T0 * (1 - i / N) + 0.5
            part = rnd.choice('UUUVBB')
            keys = [k for k in K[part] if (part, k) not in fixed and not (part == 'U' and k == '-')]
            k = rnd.choice(keys)
            old = K[part][k]
            K[part][k] = rnd.choice({'U': CONS, 'V': VOW, 'B': SYL}[part])
            new = score(segs, K)
            if new >= cur or rnd.random() < np.exp((new - cur) / T):
                cur = new
            else:
                K[part][k] = old
        txt = '|'.join(''.join(t) for t in render(segs, K))
        n = len(M.encode(txt.replace('|', '')))
        print(f'restart {r}: score {cur:.0f} chars {n} per-char {(cur - BONUS * n) / n:.3f}')
        print(txt[:600])
        if best is None or cur > best[0]:
            best = (cur, json.loads(json.dumps(K)), txt)
    out = os.path.splitext(path)[0] + '_syl_best.json'
    json.dump({'score': best[0], 'key': best[1], 'text': best[2]}, open(out, 'w', encoding='utf8'), ensure_ascii=False, indent=1)
    print('saved', out)


if __name__ == '__main__':
    main()
