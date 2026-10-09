"""R1890 family hypothesis: the extra symbols come in vowel series (AEIOU). Each family F has one consonant
string C_F and an orientation (C+v or v+C); member with vowel v = C_F+v or v+C_F. Families:
 numbers 40-44, 45-49, 50-54 (vowel by units digit 0..4 -> a e i o u), pl?, ?p, c?, h?, t?s, ?n, ?u, m?, g?, ?t.
Other unknown symbols are free (letters/bigrams). R1889 key fixed. Anneal with the `la` model."""
import sys, os, json, collections, numpy as np, multiprocessing as mp
sys.path.insert(0, '.'); sys.path.insert(0, r'C:\Users\dbour\cypher')
import io, contextlib
with contextlib.redirect_stdout(io.StringIO()):
    from dec1890 import lines, key as KEY

V = 'aeiou'
FAM = {}
for i in range(15):
    FAM[str(40 + i)] = ('N%d' % (i // 5), V[i % 5])
for v in V:
    FAM['pl' + v] = ('pl', v); FAM[v + 'p'] = ('p', v); FAM['c' + v] = ('c', v); FAM['h' + v] = ('h', v)
    FAM['t' + v + 's'] = ('ts', v); FAM[v + 'n'] = ('n', v); FAM[v + 'u'] = ('u', v); FAM['m' + v] = ('m', v)
    FAM['g' + v] = ('g', v); FAM[v + 't'] = ('t', v)
CONS = ['', 'b', 'c', 'd', 'f', 'g', 'h', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'x', 'qu', 'st', 'tr', 'pr', 'cr',
        'gr', 'br', 'nt', 'ns', 'nd', 'rt', 'sc', 'sp', 'ct', 'ss', 'mp', 'bl', 'pl', 'cl', 'fr', 'dr', 'ph', 'rr', 'll']
FREE = list('abcdefghilmnopqrstux') + ['qu', 'que', 'us', 'um', 'em', 'is', 'am', 'it', 'er', 'en', 'in', 'es', 'ae', 'ue',
                                       'st', 'nt', 'tu', 'ti', 'ta', 'te', 're', 'ri', 'ra', 'li', 'ni', 'di', 'si', 'ci']

def job(args):
    seed, iters = args
    from lang import lm
    M = lm.load('la', order=5, spaces=False)
    rng = np.random.default_rng(seed)
    toks = [t for L in lines for t in L]
    unknown = sorted(set(t for t in toks if t not in KEY))
    fams = sorted(set(FAM[t][0] for t in unknown if t in FAM))
    free = [t for t in unknown if t not in FAM]
    st = {f: (CONS[rng.integers(len(CONS))], int(rng.integers(2))) for f in fams}
    fv = {t: FREE[rng.integers(len(FREE))] for t in free}
    def val(t):
        if t in KEY: return KEY[t]
        if t in FAM:
            f, v = FAM[t]; c, o = st[f]
            return c + v if o == 0 else v + c
        return fv[t]
    def sc():
        return M.score(''.join(val(t) for t in toks))
    cur = sc(); best = (cur, dict(st), dict(fv))
    for it in range(iters):
        T = 6.0 * (1 - it / iters) + 0.2
        if rng.random() < 0.5:
            f = fams[rng.integers(len(fams))]; old = st[f]
            st[f] = (CONS[rng.integers(len(CONS))], int(rng.integers(2))) if rng.random() < .7 else (old[0], 1 - old[1])
            new = sc(); d = new - cur
            if d > 0 or rng.random() < np.exp(d / T): cur = new
            else: st[f] = old
        else:
            t = free[rng.integers(len(free))]; old = fv[t]; fv[t] = FREE[rng.integers(len(FREE))]
            new = sc(); d = new - cur
            if d > 0 or rng.random() < np.exp(d / T): cur = new
            else: fv[t] = old
        if cur > best[0]: best = (cur, dict(st), dict(fv))
    st, fv = best[1], best[2]
    return best[0], {f: (c + 'v' if o == 0 else 'v' + c) for f, (c, o) in st.items()}, fv, ''.join(val(t) for t in toks)[:400]

if __name__ == '__main__':
    it = int(os.environ.get('IT', '60000')); nr = int(os.environ.get('NR', '20'))
    with mp.Pool(20) as p:
        res = p.map(job, [(s, it) for s in range(nr)])
    res.sort(key=lambda r: -r[0])
    json.dump(res, open('fam1890_res.json', 'w'), indent=0)
    for r in res[:6]:
        print(round(r[0]), r[1]); print('   ', r[2]); print('   ', r[3][:300])
