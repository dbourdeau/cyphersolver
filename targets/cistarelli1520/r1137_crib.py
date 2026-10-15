# R1137 (Cistarelli, Eger 25 Jul 1520): ciphertext-only homophonic anneal with cribs and a word-level rerank, 2 Oct 2026.
# 1. Unconstrained anneal (fastanneal, it-cinquecento, ORDER env, many restarts) -> base key.
# 2. Cribs from the 1520-21 Caprile letters (custode, agria, alfonso, debito, buda, episcopato) and control words of the
#    same lengths that should not occur (pentola, zucchero, ...): each crib is tried at every position where it is
#    consistent (a repeated token may not take two letters), ranked by agreement with the base decryption; the top
#    windows are re-annealed with the crib fixed. A crib that is really in the text should give a larger gain than
#    the controls.
# 3. Word-level rerank: best segmentation of each candidate into words of the it-cinquecento corpora (unigram
#    log-probabilities), as mean log-prob per character.
# Run: ORDER=5 python r1137_crib.py [restarts] [top]
import os, sys, math, random, collections, re
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')
sys.path.insert(0, ROOT)
from lang import lm, corpora
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'caprile1519'))   # shared anneal.py / fastanneal.py (split 14 Oct 2026)
import anneal, fastanneal
import numpy as np

CRIBS = ['custode', 'agria', 'alfonso', 'debito', 'buda', 'episcopato']
CONTROLS = ['pentola', 'zucca', 'tamburo', 'uendemmia', 'cipolla', 'farfalla']

def words_model():
    txt = lm.norm(corpora.text(['it-renaissance', 'it-nunziature']), 'early', True)
    c = collections.Counter(txt.split())
    n = sum(c.values())
    return {w: math.log(k / n) for w, k in c.items() if k >= 2 and len(w) <= 14}, math.log(0.5 / n)

def segment_score(s, W, unk):
    best = [0.0] + [-1e18] * len(s)
    for i in range(1, len(s) + 1):
        for j in range(max(0, i - 14), i):
            w = s[j:i]
            lp = W.get(w, unk * len(w) if len(w) <= 2 else -1e18 if len(w) > 3 else unk * 2)
            if best[j] + lp > best[i]: best[i] = best[j] + lp
    return best[-1] / max(1, len(s))

def decrypt(seqs, key, toks):
    ti = {t: i for i, t in enumerate(toks)}
    return [''.join(fastanneal.M.alpha[key[ti[t]]] for t in s) for s in seqs]

def main():
    R = int(sys.argv[1]) if len(sys.argv) > 1 else 20
    TOP = int(sys.argv[2]) if len(sys.argv) > 2 else 8
    seqs = anneal.runs(os.path.join(HERE, 'r1137_transcription.txt'))
    flat = [t for s in seqs for t in s]
    (s0, k0), toks = fastanneal.run(seqs, 80000, R, seed=11)
    base = ''.join(decrypt(seqs, k0, toks))
    W, unk = words_model()
    print('base score', round(s0, 1), 'per token', round(s0 / len(flat), 3), 'word', round(segment_score(base, W, unk), 3))
    print('base', base[:300])
    results = []
    for w0 in CRIBS + CONTROLS:
        w = lm.norm(w0, 'early', False)
        cands = []
        for p in range(len(flat) - len(w) + 1):
            win = flat[p:p + len(w)]
            m = {}
            ok = all(m.setdefault(t, c) == c for t, c in zip(win, w))
            if not ok: continue
            agree = sum(base[p + i] == c for i, c in enumerate(w))
            cands.append((agree, p, m))
        cands.sort(key=lambda x: -x[0])
        best = None
        for agree, p, m in cands[:TOP]:
            (s1, k1), _ = fastanneal.run(seqs, int(os.environ.get('CITERS', '80000')), 3, seed=p, fixed=m)
            if best is None or s1 > best[0]: best = (s1, p, agree, k1)
        s1, p, agree, k1 = best
        d = ''.join(decrypt(seqs, k1, toks))
        ws = segment_score(d, W, unk)
        tag = 'crib' if w0 in CRIBS else 'control'
        results.append((tag, w, len(cands), round(s1 - s0, 1), round(ws, 3), p, d[max(0, p - 25):p + len(w) + 25]))
        print(tag, w, 'positions', len(cands), 'gain', round(s1 - s0, 1), 'word', round(ws, 3), 'at', p, d[max(0, p - 25):p + len(w) + 25], flush=True)
    print('\nsummary (gain = anneal score with the crib fixed minus the unconstrained score; word = segmentation score)')
    for r in results: print(*r[:6])

if __name__ == '__main__':
    main()
