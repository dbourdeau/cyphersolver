"""R7524: homophonic annealing that uses the writer's word division (r7524-words.txt).

Each cipher run between clear words is scored as ' w1 w2 ... ' with the shared pl-modern order-5 spaced model,
so word starts and ends constrain the key. Optional fixed values: --fix 15=i,20=e
"""
import sys, re, random, math, json
sys.path.insert(0, __file__.rsplit('targets', 1)[0])
import numpy as np
from lang import lm

HERE = __file__.rsplit('\\', 1)[0] if '\\' in __file__ else __file__.rsplit('/', 1)[0]


def load_runs(path=HERE + '/r7524-words.txt'):
    runs, cur = [], []
    for line in open(path, encoding='utf8'):
        if line.startswith('#'):
            continue
        for tok in re.findall(r'\[[^\]]*\]|\S+', line):
            if tok.startswith('['):
                if cur:
                    runs.append(cur); cur = []
            else:
                cur.append([int(x) for x in tok.split('.')])
    if cur:
        runs.append(cur)
    return runs


def main():
    args = sys.argv[1:]
    fix = {}
    if '--fix' in args:
        s = args[args.index('--fix') + 1]
        fix = {int(a): b for a, b in (p.split('=') for p in s.split(','))}
    restarts = int(args[args.index('--restarts') + 1]) if '--restarts' in args else 20
    iters = int(args[args.index('--iters') + 1]) if '--iters' in args else 40000
    seed = int(args[args.index('--seed') + 1]) if '--seed' in args else 1
    if '--model' in args:   # a DenseLM saved with .save(path): path.npy + path.json
        mp = args[args.index('--model') + 1]
        meta = json.load(open(mp + '.json'))
        m = lm.DenseLM(np.load(mp + '.npy'), meta['order'], meta['alpha'], meta)
    else:
        m = lm.load('pl-modern', order=5, spaces=True)
    alpha = m.alpha
    sp = m.index[' ']
    letters = [i for i, c in enumerate(alpha) if c != ' ' and c not in 'qvxj']
    runs = load_runs()
    signs = sorted({s for r in runs for w in r for s in w})
    sid = {s: i for i, s in enumerate(signs)}
    # build index template: per run, a list of sign indices with -1 for space
    tmpl = []
    for r in runs:
        t = [-1]
        for w in r:
            t += [sid[s] for s in w] + [-1]
        tmpl.append(np.array(t))
    fixed = {sid[k]: m.index[v] for k, v in fix.items() if k in sid}
    rng = random.Random(seed)

    def score(key):
        tot = 0.0
        for t in tmpl:
            x = np.where(t < 0, sp, key[np.maximum(t, 0)])
            tot += m.score_idx(np.concatenate(([sp] * 4, x)))
        return tot

    best_all = None
    for r in range(restarts):
        key = np.array([rng.choice(letters) for _ in signs])
        for k, v in fixed.items():
            key[k] = v
        cur = score(key); best = (cur, key.copy())
        free = [i for i in range(len(signs)) if i not in fixed]
        T0 = 3.0
        for it in range(iters):
            T = T0 * (1 - it / iters) + 0.05
            i = rng.choice(free)
            old = key[i]
            key[i] = rng.choice(letters)
            new = score(key)
            if new >= cur or rng.random() < math.exp((new - cur) / T):
                cur = new
                if cur > best[0]:
                    best = (cur, key.copy())
            else:
                key[i] = old
        key = best[1]
        text = ' | '.join(' '.join(''.join(alpha[key[sid[s]]] for s in w) for w in run) for run in runs)
        print(f'{best[0]:.1f}  {text}', flush=True)
        if best_all is None or best[0] > best_all[0]:
            best_all = (best[0], {s: alpha[key[sid[s]]] for s in signs}, text)
    print('BEST', best_all[0]); print(best_all[2]); print(json.dumps(best_all[1]))


if __name__ == '__main__':
    main()
