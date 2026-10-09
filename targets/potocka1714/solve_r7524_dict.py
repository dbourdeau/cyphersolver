"""R7524: word-level homophonic annealing with a period Polish dictionary.

Each cipher word scores log P(word) from a word-frequency list when the candidate is a dictionary word, else
the char-model log-prob of ' word ' minus an OOV penalty. Signs map to letters; homophones allowed.
Usage: python solve_r7524_dict.py MODELPATH WORDCOUNTS.pkl [--fix 15=i,..] [--restarts N] [--iters N] [--oov X]
"""
import sys, math, random, json, pickle
sys.path.insert(0, __file__.rsplit('targets', 1)[0])
import numpy as np
from lang import lm
from solve_r7524_words import load_runs


def main():
    a = sys.argv[1:]
    mp, wp = a[0], a[1]
    opt = lambda k, d: type(d)(a[a.index(k) + 1]) if k in a else d
    restarts, iters, oov, seed = opt('--restarts', 10), opt('--iters', 30000), opt('--oov', 4.0), opt('--seed', 1)
    fix = {int(x): y for x, y in (p.split('=') for p in opt('--fix', '').split(',') if p)}
    meta = json.load(open(mp + '.json'))
    m = lm.DenseLM(np.load(mp + '.npy'), meta['order'], meta['alpha'], meta)
    wc = pickle.load(open(wp, 'rb'))
    tot = sum(wc.values())
    logp = {w: math.log(c / tot) for w, c in wc.items() if c >= 2 or len(w) > 6}
    runs = load_runs()
    words = [w for r in runs for w in r]
    signs = sorted({s for w in words for s in w})
    sid = {s: i for i, s in enumerate(signs)}
    W = [[sid[s] for s in w] for w in words]
    occ = {i: [j for j, w in enumerate(W) if i in w] for i in range(len(signs))}
    letters = list('abcdefghiklmnoprstuwyz')
    rng = random.Random(seed)
    memo = {}

    def wscore(s):
        v = memo.get(s)
        if v is None:
            lp = m.score(' ' * 4 + s + ' ')
            if s in logp:
                v = max(logp[s] + 2.0, lp)   # dictionary words get a small bonus
            else:
                v = lp - oov * (1 + len(s) / 4)
            memo[s] = v
        return v

    best_all = None
    for r in range(restarts):
        key = [rng.choice(letters) for _ in signs]
        for k, v in fix.items():
            key[sid[k]] = v
        free = [i for i in range(len(signs)) if signs[i] not in fix]
        ws = [wscore(''.join(key[i] for i in w)) for w in W]
        cur = sum(ws); best = (cur, key[:])
        for it in range(iters):
            T = 4.0 * (1 - it / iters) + 0.1
            i = rng.choice(free)
            old = key[i]; key[i] = rng.choice(letters)
            new_ws = {j: wscore(''.join(key[x] for x in W[j])) for j in occ[i]}
            d = sum(new_ws[j] - ws[j] for j in occ[i])
            if d >= 0 or rng.random() < math.exp(d / T):
                for j, v in new_ws.items():
                    ws[j] = v
                cur += d
                if cur > best[0]:
                    best = (cur, key[:])
            else:
                key[i] = old
        key = best[1]
        text = ' '.join(''.join(key[i] for i in w) for w in W)
        indict = sum(''.join(key[i] for i in w) in logp for w in W)
        print(f'{best[0]:.1f} dict={indict}/{len(W)}  {text}', flush=True)
        if best_all is None or best[0] > best_all[0]:
            best_all = (best[0], dict(zip(signs, key)), text)
    print('BEST', best_all[0]); print(best_all[2]); print(json.dumps(best_all[1]))


if __name__ == '__main__':
    main()
