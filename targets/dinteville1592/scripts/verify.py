"""Verification tests for the f. 130 reading.
1. Null test: decode f. 130 with the real key vs keys whose values are shuffled among signs; score = French
   lexicon segmentation log-prob per letter and fraction of letters inside dictionary words (len >= 3).
2. Held-out test: decode f. 130 with ONLY the key as fixed on f. 128 (key128.tsv); signs first valued on f. 130 -> '?'.
"""
import random, re, sys, decode, segment
def lines(path='../f130_signs.txt'):
    return [(n, s.split()) for n, s in (l.rstrip('\n').split('\t') for l in open(path) if l.strip() and not l.startswith('# ')) if not n.endswith('.clear')]
def score(text):
    sc, ws = segment.seg(text)
    L = len(segment.parse(text))
    inw = sum(len(w) for w in ws if not w.startswith('[') and len(w) >= 3)
    return sc / max(1, L), inw / max(1, L)
def total(key, data):
    a = b = n = 0
    for _, S in data:
        t = decode.dec(S, key).replace('[', '').replace(']', '')
        t = re.sub(r'[^a-z()/]', '', t)
        if not t: continue
        s1, s2 = score(t); L = len(segment.parse(t)); a += s1 * L; b += s2 * L; n += L
    return a / n, b / n
if __name__ == '__main__':
    data = lines(); k = decode.key('../key.tsv')
    real = total(k, data); print(f'REAL key           logp/letter {real[0]:.2f}  in-word {real[1]:.0%}')
    k128 = decode.key('../key_f128.tsv'); held = total(k128, data); print(f'f.128-only key     logp/letter {held[0]:.2f}  in-word {held[1]:.0%}')
    rng = random.Random(1); vals = [k[s] for s in k]; nulls = []
    for i in range(int(sys.argv[1]) if len(sys.argv) > 1 else 30):
        v = vals[:]; rng.shuffle(v); kk = dict(zip(k.keys(), v)); nulls.append(total(kk, data))
    nulls.sort()
    print(f'shuffled keys (n={len(nulls)}): logp/letter best {max(x[0] for x in nulls):.2f} median {nulls[len(nulls)//2][0]:.2f};'
          f' in-word best {max(x[1] for x in nulls):.0%} median {sorted(x[1] for x in nulls)[len(nulls)//2]:.0%}')
