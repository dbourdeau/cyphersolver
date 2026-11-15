"""Held-out test (see ../PREREGISTRATION.md).
Step 1: on the training segments (A1-A9) only, score every set of three shifts and take the best -> frozen key.
Step 2: write the frozen key (as an explicit table cipher letter -> allowed plain letters) to ../keys/frozen_key.json
        and print its sha256.
Step 3: decode the held-out segments (A10-B2) with the frozen key; score = mean quadgram log10 prob per letter.
Step 4: 200 control keys = the frozen key's value-sets permuted at random among the cipher letters; same decoding.
Usage: python3 -I heldout.py [freeze|test]
"""
import sys, os, json, hashlib, itertools, random
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import poly, multishift as ms
A = ms.A
segs, labels = poly.read_ct(os.path.join(HERE, '..', 'transcription', 'pass1.txt'))
train = [(l, s) for l, s in zip(labels, segs) if l.split('.')[0] in {f'A{i}' for i in range(1, 10)}]
test = [(l, s) for l, s in zip(labels, segs) if (l, s) not in train]
KEYF = os.path.join(HERE, '..', 'keys', 'frozen_key.json')

def score_key(key, part):
    tot = 0.0; n = 0; outs = []
    for l, s in part:
        s2 = ms.prep(s)
        sc, txt = poly.best_reading(s2, key)
        tot += sc; n += max(1, len(s2) - 3); outs.append((l, txt))
    return tot / n, outs

if __name__ == '__main__':
    mode = sys.argv[1] if len(sys.argv) > 1 else 'test'
    print('train letters', sum(len(s) for _, s in train), 'test letters', sum(len(s) for _, s in test))
    if mode == 'freeze':
        res = sorted(((ms.run([s for _, s in train], t)[0], t) for t in itertools.combinations(range(24), 3)), reverse=True)
        print('training top 5:', [(round(s, 3), t) for s, t in res[:5]])
        best = res[0][1]
        key = {c: sorted(set(A[(A.index(c) + k) % 24] for k in best)) for c in A}
        json.dump({'shifts': list(best), 'alphabet': A, 'printed_v_is': 'u', 'printed_u_is': 'n', 'key': key},
                  open(KEYF, 'w'), indent=1, sort_keys=True)
        print('frozen', best, 'sha256', hashlib.sha256(open(KEYF, 'rb').read()).hexdigest())
    else:
        d = json.load(open(KEYF)); print('using', d['shifts'], 'sha256', hashlib.sha256(open(KEYF, 'rb').read()).hexdigest())
        key = {c: tuple(v) for c, v in d['key'].items()}
        real, outs = score_key(key, test)
        rng = random.Random(2026); ctrl = []
        letters = sorted(key); vals = [key[c] for c in letters]
        for i in range(200):
            v2 = vals[:]; rng.shuffle(v2)
            ctrl.append(score_key(dict(zip(letters, v2)), test)[0])
        ctrl.sort()
        print(f'held-out score {real:.4f}; controls: max {ctrl[-1]:.4f} median {ctrl[100]:.4f} min {ctrl[0]:.4f}; '
              f'controls >= real: {sum(c >= real for c in ctrl)} of 200')
        for l, t in outs: print(l, t)
