"""Word-level refinement: score a key by the best word segmentation of its decrypt.

Vocabulary and word unigrams from the lang/ French corpora (normalised 'early', no accents).
Score of a run = Viterbi segmentation log-prob, with a character-LM fallback for unknown stretches.
Anneal/hill-climb the key on that objective, starting from a given key, with optional pins.

usage: FIX=fix.json python word.py <start key.json> <rounds> <iters>
"""
import sys, os, json, math, random, collections
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from lang import lm
import numpy as np
from solve import load_runs

HERE = os.path.dirname(os.path.abspath(__file__))
CH = lm.load('fr-1530-despatches', order=5, spaces=False)
LET = 'abcdefghilmnopqrstuxy'


def build_vocab():
    cache = os.path.join(HERE, 'vocab.json')
    if os.path.exists(cache):
        return json.load(open(cache))
    cnt = collections.Counter()
    for name in ('fr-1520s-diplomatic.txt', 'fr-henri4.txt', 'fr-gutenberg.txt'):
        p = os.path.join(HERE, '..', 'lang', 'corpora', name)
        if not os.path.exists(p): continue
        txt = lm.norm(open(p, encoding='utf-8', errors='replace').read(), 'early')
        cnt.update(w for w in txt.split() if 1 <= len(w) <= 18)
    tot = sum(cnt.values())
    import re
    roman = re.compile(r'^[ixvlcdm]+$')
    keep_short = {'a','y','o','en','et','de','le','la','du','au','ne','se','ce','il','on','si','je','me','te','qu','ou','un','sa','ses','les','des','est'}
    voc = {w: math.log(c / tot) for w, c in cnt.items()
           if c >= 3 and not (roman.match(w) and w not in keep_short) and (len(w) >= 3 or w in keep_short)}
    json.dump(voc, open(cache, 'w'), ensure_ascii=False)
    return voc


VOC = build_vocab()
MAXW = 16
UNK = float(os.environ.get('UNK','-9.0'))
BCOST = float(os.environ.get('BCOST','2.5'))


def seg_score(s):
    """best log-prob segmentation of s into vocabulary words (unknown chunks charged UNK/char)."""
    n = len(s)
    best = [-1e18] * (n + 1); best[0] = 0.0
    for i in range(1, n + 1):
        b = best[i - 1] + UNK          # one unknown character
        for j in range(max(0, i - MAXW), i):
            if best[j] <= -1e17: continue
            w = s[j:i]
            lp = VOC.get(w)
            if lp is not None:
                v = best[j] + lp - BCOST
                if v > b: b = v
        best[i] = b
    return best[n]


def main():
    start = json.load(open(sys.argv[1]))
    ROUNDS = int(sys.argv[2]); IT = int(sys.argv[3])
    FIX = json.load(open(os.environ['FIX'])) if os.environ.get('FIX') else {}
    runs = [r for r in load_runs() if len(r) >= 3]
    signs = sorted({s for r in runs for s in r})
    si = {s: i for i, s in enumerate(signs)}
    seq = [[si[s] for s in r] for r in runs]
    occ = [[j for j, r in enumerate(seq) if i in r] for i in range(len(signs))]
    free = [i for i, s in enumerate(signs) if s not in FIX]
    idx2ch = {i: c for i, c in enumerate(LET)}
    ch2idx = {c: i for i, c in idx2ch.items()}
    key = [ch2idx.get(FIX.get(s, start.get(s, 'e')), 0) for s in signs]
    LAM = float(os.environ.get('LAM', '1.0'))

    def text(k, r):
        return ''.join(idx2ch[k[i]] for i in r)

    def sc(k, r):
        t = text(k, r)
        return LAM * seg_score(t) + CH.score(t)

    rsc = [sc(key, r) for r in seq]
    cur = sum(rsc); best = (cur, list(key))
    print('start', round(cur, 1), file=sys.stderr)
    for rd in range(ROUNDS):
        key = list(best[1])
        for _ in range(random.randint(0, 4)):
            key[random.choice(free)] = random.randrange(len(LET))
        rsc = [sc(key, r) for r in seq]; cur = sum(rsc)
        loc = (cur, list(key))
        for it in range(IT):
            T = 30.0 * (1 - it / IT) + 0.5
            i = random.choice(free); old = key[i]; nv = random.randrange(len(LET))
            if nv == old: continue
            key[i] = nv; js = occ[i]
            ns = [sc(key, seq[j]) for j in js]
            new = cur - sum(rsc[j] for j in js) + sum(ns)
            if new >= cur or random.random() < math.exp((new - cur) / T):
                cur = new
                for j, v in zip(js, ns): rsc[j] = v
                if cur > loc[0]: loc = (cur, list(key))
            else:
                key[i] = old
        if loc[0] > best[0]:
            best = loc; print('round', rd, round(best[0], 1), file=sys.stderr)
    key = best[1]
    mp = {s: idx2ch[key[i]] for i, s in enumerate(signs)}
    print(json.dumps(mp, sort_keys=True))
    tot = cov = 0
    for r in seq:
        t = text(key, r)
        tot += len(t)
    print('score', round(best[0], 1))
    for r in seq:
        print(text(key, r))


if __name__ == '__main__':
    main()
