"""Fill the free sign values by annealing against a French 5-gram model, holding fixed values.

Each label maps to one letter, or to nothing when listed in NULLS. Clear words inside a block ([word] in the
transcription) are kept as plaintext. Prints the best decodes of several restarts so the free values can be
compared with the gloss, and the per-label agreement across restarts."""
import sys, json, random, math
import numpy as np

A = 'abcdefghilmnopqrstuxyz'


def load(fn):
    out = {}
    for l in open(fn):
        if l.startswith('#') or ':' not in l: continue
        k, v = l.split(':', 1)
        out[k.strip()] = v.split()
    return out


def main():
    tr = load(sys.argv[1]); cfg = json.load(open(sys.argv[2])); lp = np.load(sys.argv[3])
    seed = int(sys.argv[4]) if len(sys.argv) > 4 else 1
    rng = random.Random(seed)
    fixed = {k: ('0' if v == '0' else v.lower().replace('v', 'u').replace('j', 'i')) for k, v in cfg['fixed'].items()}
    nulls = set(cfg.get('nulls', []))
    seqs = []
    for b in cfg['blocks']:
        s = []
        for l in b['lines']:
            for t in tr[l]:
                if t.startswith('['): s += [('clear', c) for c in t.strip('[]').lower().replace('v', 'u').replace('j', 'i')]
                elif t in nulls: continue
                else: s.append(('sign', t))
        seqs.append(s)
    labels = sorted({t for s in seqs for k, t in s if k == 'sign'})
    free = [t for t in labels if t not in fixed]

    def decode(key):
        return [''.join(t if k == 'clear' else ('' if key[t] == '0' else key[t]) for k, t in s) for s in seqs]

    def score(key):
        tot = 0.0
        for txt in decode(key):
            x = [A.index(c) for c in txt]
            for i in range(4, len(x)): tot += lp[x[i - 4], x[i - 3], x[i - 2], x[i - 1], x[i]]
        return tot

    results = []
    for run in range(cfg.get('runs', 10)):
        key = {t: fixed.get(t, rng.choice(A)) for t in labels}
        cur = score(key); T = 4.0
        for it in range(cfg.get('iters', 20000)):
            t = rng.choice(free); old = key[t]; key[t] = rng.choice(A)
            c = score(key)
            if c >= cur or rng.random() < math.exp((c - cur) / T): cur = c
            else: key[t] = old
            T = max(0.2, T * 0.9997)
        results.append((cur, dict(key)))
    results.sort(key=lambda r: -r[0])
    n = sum(len(s) for s in seqs)
    for cur, key in results[:4]:
        print(f'{cur / n:.3f}', ' | '.join(decode(key)))
    print('\nagreement of free labels across runs (best first):')
    for t in free:
        vals = [k[t] for _, k in results]
        print(f'  {t:5}', ' '.join(vals))
    if len(sys.argv) > 5:
        json.dump(results[0][1], open(sys.argv[5], 'w'))


if __name__ == '__main__':
    main()
