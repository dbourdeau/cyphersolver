import sys, os, numpy as np, multiprocessing as mp, json
sys.path.insert(0, '.')
from parse1890 import toks
W = float(os.environ.get('W', '1')); IT = int(os.environ.get('IT', '4000000'))
def clean(t):
    t = t.replace('?', '').replace('_.', '').replace('.', '')
    m = {'l/z': 'l', 'l/zp': ['l', 'p'], 'l/z6': ['l', '6'], 'pla/u': 'pla', 'ple/i': 'ple', 'c/1o/0': ['c', 'o'], 'g^a': ['g', 'a']}
    if t in m: v = m[t]; return v if isinstance(v, list) else [v]
    return [t]
seq_t = []
for t in toks:
    if t == '|': seq_t.append('|'); continue
    if t in '/()': continue
    seq_t += clean(t)
syms = sorted(set(x for x in seq_t if x != '|'))
sid = {s: i for i, s in enumerate(syms)}
seq = np.array([-1 if x == '|' else sid[x] for x in seq_t], np.int64)
def job(seed):
    import hsolve
    fixed = -np.ones(len(syms), np.int64); init = fixed.copy()
    if os.environ.get('VOW'):
        for i, t in enumerate(syms):
            v = [c for c in t if c in 'aeiou']
            if len(t) > 1 and not t.isdigit() and len(v) == 1:
                fixed[i] = hsolve.ALPHA.index(v[0])
    b, k = hsolve.anneal(seq, len(syms), hsolve.LP, hsolve.A, hsolve.ORDER, IT, 20.0, 0.0, 0.0, fixed, init, seed, hsolve.FREQ, W)
    return b, k.tolist()
if __name__ == '__main__':
    import hsolve
    print(len(seq), len(syms))
    with mp.Pool(20) as p:
        res = p.map(job, range(int(os.environ.get("NR","16"))))
    res.sort(key=lambda r: -r[0])
    for b, k in res[:5]:
        print(round(b, 1), hsolve.decode(seq, np.array(k))[:240])
    json.dump({'syms': syms, 'res': res}, open('res1890_W%s.json' % W, 'w'))
