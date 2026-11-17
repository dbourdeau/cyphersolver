"""Ciphertext-only attack on LJS 51 f. 106v: simple substitution of invented signs for Arabic letters, word divisions
kept, lam and alif written with one sign (the compiler: "wajadtuhu ja'ala al-lam alif").

Score = character 5-gram log-probability (lang model ar-classical-poetry, with spaces) + a word bonus from the same
corpus's vocabulary. The shared sign (default H) is read per word as alif or lam, whichever scores better.
Simulated annealing over sign -> letter maps, many restarts; prints the best decodings.

    python targets/ljs51/solve.py [--restarts 40] [--iters 60000] [--shared H] [--fix N=و ...]
"""
import argparse, collections, math, os, random, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, ROOT)
from lang import lm

LETTERS = lm.AR_LETTERS


def read_words(path, join_lines=((4, 5),)):
    lines = {}
    for ln in open(path, encoding='utf-8'):
        m = re.match(r'L(\d+):\s*(.*)', ln)
        if m:
            lines[int(m.group(1))] = m.group(2)
    words, cur = [], []
    for n in sorted(lines):
        toks = lines[n].split()
        for t in toks:
            if t == '|':
                if cur: words.append(cur); cur = []
            else:
                cur.append(t)
        if cur and not any(n == a for a, b in join_lines):
            words.append(cur); cur = []
    if cur: words.append(cur)
    return words


def vocab():
    path = os.path.join(ROOT, 'lang', 'corpora', 'ar-classical-poetry.txt')
    c = collections.Counter()
    with open(path, encoding='utf-8') as fh:
        for i, line in enumerate(fh):
            c.update(lm.norm(line, 'arabic28').split())
            if i > 400000: break
    tot = sum(c.values())
    return {w: math.log(n / tot) for w, n in c.items() if n >= 2}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--restarts', type=int, default=30)
    ap.add_argument('--iters', type=int, default=40000)
    ap.add_argument('--shared', default='H')
    ap.add_argument('--wbonus', type=float, default=1.0)
    ap.add_argument('--fix', nargs='*', default=[])
    ap.add_argument('--seed', type=int, default=1)
    ap.add_argument('--dir', default='rtl', choices=['rtl', 'ltr'])
    ap.add_argument('--lamalif', action='store_true', help='one sign may stand for the ligature lam-alif')
    ap.add_argument('--text', default='transcription.txt', help='transcription file in this folder')
    ap.add_argument('--nodiv', action='store_true', help='ignore the dividers: score each bayt as one string without spaces')
    ap.add_argument('--homophones', type=float, default=None,
                    help='allow two signs for one letter, at this score penalty per extra sign (default: one-to-one key)')
    a = ap.parse_args()
    random.seed(a.seed)
    words = read_words(os.path.join(HERE, a.text), ((3, 4), (4, 5)) if 'divshift' in a.text else ((4, 5),))
    if a.dir == 'ltr':                      # written left to right: reverse the signs in each word and the word order
        words = [w[::-1] for w in words[::-1]]
    signs = sorted({s for w in words for s in w if s != a.shared})
    model = lm.load('ar-classical-poetry', spaces=not a.nodiv)
    if a.nodiv:                              # two bayts: words 0-11 and 12-21
        words = [sum(words[:12], []), sum(words[12:], [])]
        a.wbonus = 0.0
    V = vocab()
    unk = min(V.values()) - 4
    fixed = dict(f.split('=') for f in a.fix)
    pool = list(LETTERS) if (a.shared == 'none' or a.homophones is not None) else [c for c in LETTERS if c not in 'ال']
    if a.lamalif:
        pool.append('لا')
    wcache = {}

    def word_score(w, mp):
        # best over alif/lam choices for each shared sign
        slots = [i for i, s in enumerate(w) if s == a.shared]
        base = [mp.get(s, '?') for s in w]
        best = -1e9, ''
        for k in range(1 << len(slots)):
            t = base[:]
            for j, i in enumerate(slots):
                t[i] = 'ل' if k >> j & 1 else 'ا'
            s = ''.join(t)
            if s in wcache:
                sc = wcache[s]
            else:
                sc = (model.score(s) if a.nodiv else model.score(' ' + s + ' ')) + a.wbonus * V.get(s, unk)
                wcache[s] = sc
            if sc > best[0]:
                best = sc, s
        return best

    def total(mp):
        sc, out = 0.0, []
        if a.homophones is not None:
            sc -= a.homophones * (len(mp) - len(set(mp.values())))
        for w in words:
            s, t = word_score(w, mp)
            sc += s; out.append(t)
        return sc, ' '.join(out)

    results = []
    for r in range(a.restarts):
        free = [s for s in signs if s not in fixed]
        letters = [c for c in pool if c not in fixed.values()]
        random.shuffle(letters)
        mp = dict(fixed); mp.update(zip(free, letters))
        cur, txt = total(mp)
        best = (cur, txt, dict(mp))
        T0 = 8.0
        for it in range(a.iters):
            T = T0 * (1 - it / a.iters) + 0.05
            s1 = random.choice(free)
            new = dict(mp)
            if random.random() < 0.5:
                s2 = random.choice(free)
                new[s1], new[s2] = mp[s2], mp[s1]
            else:
                choices = pool if a.homophones is not None else [c for c in letters if c not in mp.values()]
                if not choices: continue
                new[s1] = random.choice(choices)
            sc, t = total(new)
            if sc > cur or random.random() < math.exp((sc - cur) / T):
                mp, cur, txt = new, sc, t
                if cur > best[0]:
                    best = (cur, txt, dict(mp))
        results.append(best)
        print(f'{r:3d} {best[0]:9.1f}  {best[1]}', flush=True)
    results.sort(key=lambda x: -x[0])
    print('\nBEST')
    for sc, txt, mp in results[:5]:
        print(f'{sc:9.1f}  {txt}')
        print('          ' + ' '.join(f'{k}={v}' for k, v in sorted(mp.items())))


if __name__ == '__main__':
    main()
