"""Phrase-level search: a character 5-gram (lang en-modern) scores the whole phrase, not word by word.

search.py ranks word sequences by unigram frequency, so it cannot tell sense from word salad (its line 23 reading is
"with doubt portion from gift first mending she of chairs seven mariner"). Here the plaintext is generated letter by
letter under the shared English 5-gram, each word must lie in the vocabulary (vocab.tsv, count >= 4), and every cipher
letter must be consumed in order from its stream (A = 8 May, B = 20 May); a letter in neither stream costs OMIT.

Usage: python beam.py 23 [9 26 29 ...]   (line numbers as in ads.PAIRS)
"""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
from lang import lm
from ads import PAIRS

OMIT = 2.3
MAX_WORD_OMIT = 3
BEAM = int(os.environ.get('BEAM', 4000))
HERE = os.path.dirname(os.path.abspath(__file__))


def vocab(min_count=4):
    V = {}
    for line in open(os.path.join(HERE, 'vocab.tsv'), encoding='utf-8'):
        w, c = line.split('\t'); c = int(c)
        if c >= min_count and w.isalpha() and (len(w) > 1 or w in ('a', 'i')):
            V[w] = c
    for w in ('conington', 'jowett', 'shirley', 'hertford', 'balliol', 'oxford', 'satirs', 'lecsurs', 'qui', 'fit',
              'horace', 'motto', 'scholarship', 'examination', 'tutor', 'dean', 'proctor', 'master', 'pupil'):
        V.setdefault(w, 5)
    return V


def prefixes(V):
    P = set()
    for w in V:
        for k in range(1, len(w) + 1): P.add(w[:k])
    return P


def search(A, B, M, V, P, K=15):
    o = M.order; Al = M.alpha; idx = M.index; sp = idx[' ']
    lp = M.lp.reshape(-1, M.A)
    nctx = M.A ** (o - 1)
    letters = [c for c in Al if c != ' ']
    # state: (i, j, ctx, word, wom) -> (score, text, omitted)
    ctx0 = 0
    for _ in range(o - 1): ctx0 = (ctx0 * M.A + sp) % nctx
    beam = {(0, 0, ctx0, '', 0): (0.0, '', 0)}
    done = []
    a, b = len(A), len(B)
    max_steps = (a + b) * 2 + 20
    for _ in range(max_steps):
        nb = {}
        for (i, j, ctx, w, wom), (s, t, om) in beam.items():
            row = lp[ctx]
            # finish
            if i == a and j == b and w in V:
                done.append((s + float(row[sp]) - 0, t, om))
            cands = []
            if i < a: cands.append((A[i], i + 1, j, 0))
            if j < b: cands.append((B[j], i, j + 1, 0))
            if wom < MAX_WORD_OMIT:
                for c in letters: cands.append((c, i, j, 1))
            for c, ni, nj, isom in cands:
                nw = w + c
                if nw not in P: continue
                ci = idx[c]
                ns = s + float(row[ci]) - (OMIT if isom else 0)
                key = (ni, nj, (ctx * M.A + ci) % nctx, nw, wom + isom)
                if key not in nb or nb[key][0] < ns:
                    nb[key] = (ns, t + c, om + isom)
            if w in V:   # word boundary
                ns = s + float(row[sp])
                key = (i, j, (ctx * M.A + sp) % nctx, '', 0)
                if key not in nb or nb[key][0] < ns:
                    nb[key] = (ns, t + ' ', om)
        if not nb: break
        # prune: rank by score plus a progress bonus so long-consuming paths are not starved
        items = sorted(nb.items(), key=lambda kv: kv[1][0] + 1.2 * (kv[0][0] + kv[0][1]), reverse=True)[:BEAM]
        beam = dict(items)
    done.sort(reverse=True)
    seen, out = set(), []
    for s, t, om in done:
        if t in seen: continue
        seen.add(t); out.append((s, t, om))
        if len(out) >= K: break
    return out


if __name__ == '__main__':
    M = lm.load('en-modern')
    V = vocab(); P = prefixes(V)
    for ln in map(int, sys.argv[1:]):
        A, B = PAIRS[ln - 1]
        print('line %d  %s / %s' % (ln, A, B))
        for s, t, om in search(A, B, M, V, P):
            print('  %8.1f  %5.2f/ch  om=%d  %s' % (s, M.per_char(' ' + t + ' '), om, t))
        sys.stdout.flush()
