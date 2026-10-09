"""R1890: R1889 key fixed; anneal the unknown symbols over candidate values (letters, Latin bigrams/trigrams,
null) with the shared `la` model. Output: best assignments over restarts, for context checking by eye."""
import sys, os, json, re, collections, numpy as np, multiprocessing as mp
sys.path.insert(0, '.'); sys.path.insert(0, r'C:\Users\dbour\cypher')
from dec1890 import lines, key as KEY  # noqa  (prints the current decode on import)

ORDER = 5
def cands():
    from lang import lm
    txt = lm.norm(open(r'C:\Users\dbour\cypher\lang\corpora\la-gutenberg.txt', encoding='latin-1').read()[:4000000], 'latin', spaces=True)
    bi = collections.Counter(); tri = collections.Counter()
    for w in txt.split():
        for i in range(len(w) - 1): bi[w[i:i+2]] += 1
        for i in range(len(w) - 2): tri[w[i:i+3]] += 1
    alpha = 'abcdefghilmnopqrstux'
    return list(alpha) + [b for b, _ in bi.most_common(160)] + [t for t, _ in tri.most_common(120)] + ([''] if os.environ.get('NULLS') else [])

def job(args):
    seed, iters, fixed_extra = args
    from lang import lm
    M = lm.load('la', order=ORDER, spaces=False)
    C = cands(); rng = np.random.default_rng(seed)
    toks = [t for L in lines for t in L]
    unknown = sorted(set(t for t in toks if t not in KEY and t not in fixed_extra))
    val = {t: KEY[t] for t in KEY}; val.update(fixed_extra)
    for t in unknown: val[t] = C[rng.integers(len(C))]
    def sc():
        s = ''.join(val[t] for t in toks)
        return M.score(s) - float(os.environ.get('NP','6')) * sum(len(val[t]) == 0 for t in unknown)
    cur = sc(); best = (cur, dict(val))
    for it in range(iters):
        T = 8.0 * (1 - it / iters) + 0.2
        t = unknown[rng.integers(len(unknown))]
        old = val[t]; val[t] = C[rng.integers(len(C))]
        new = sc(); d = new - cur
        if d > 0 or rng.random() < np.exp(d / T): cur = new
        else: val[t] = old
        if cur > best[0]: best = (cur, dict(val))
    return best[0], {t: best[1][t] for t in unknown}

if __name__ == '__main__':
    iters = int(os.environ.get('IT', '60000')); nr = int(os.environ.get('NR', '20'))
    fx = json.load(open('key1890_extra.json')) if os.path.exists('key1890_extra.json') else {}
    with mp.Pool(20) as p:
        res = p.map(job, [(s, iters, fx) for s in range(nr)])
    res.sort(key=lambda r: -r[0])
    json.dump(res, open('syl1890_res.json', 'w'), indent=0)
    syms = sorted(res[0][1])
    for t in syms:
        c = collections.Counter(r[1][t] for r in res[:10])
        print(t, c.most_common(4))
    print([round(r[0]) for r in res])
