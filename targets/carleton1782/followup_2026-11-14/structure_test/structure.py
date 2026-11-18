"""What the two numbers of a word code are: tests on the 174 known codes (post-test material, 14 Nov 2026).

    python targets/carleton1782/followup_2026-11-14/structure_test/structure.py

Reads key/word_codes.tsv only. Prints:
  1. how many codes have a reading whose first letter sits at place b of the 24-letter alphabet (a-y, i=j, u and v apart),
     with a permutation control (b shuffled among codes, 2000 draws, seed 1782);
  2. the codes that do not fit;
  3. Spearman's rho between the first number a and the alphabetical rank of the word, over all codes and inside each
     letter column (a dictionary page-line code would give rho near +1 overall and inside each letter);
  4. the range of a and b, and the a values per letter column.
"""
import csv, random
from pathlib import Path

T = Path(__file__).resolve().parents[2]
AL = 'abcdefghiklmnopqrstuvwxy'
IDX = {c: i + 1 for i, c in enumerate(AL)}
IDX['j'] = 9

rows = list(csv.DictReader((T / 'key/word_codes.tsv').open(encoding='utf-8'), delimiter='\t'))
codes = []
for r in rows:
    a, b = map(int, r['code'].split('-'))
    reads = [x.split(' (')[0].strip().lower() for x in r['readings'].split(' / ')]
    codes.append((a, b, reads))

def fits(b, reads):
    return any(IDX.get(w[0]) == b for w in reads)

n = len(codes)
k = sum(fits(b, rd) for a, b, rd in codes)
rng = random.Random(1782)
bs = [b for _, b, _ in codes]
ctrl = []
for _ in range(2000):
    rng.shuffle(bs)
    ctrl.append(sum(fits(b, rd) for b, (_, _, rd) in zip(bs, codes)))
print(f'1. second number = place of first letter: {k} of {n} codes; shuffled control mean {sum(ctrl)/len(ctrl):.1f}, max {max(ctrl)}')
print('2. codes that do not fit:')
for a, b, rd in codes:
    if not fits(b, rd):
        print(f'   {a}-{b}  {" / ".join(rd)}')

def rank(xs):
    s = sorted(range(len(xs)), key=lambda i: xs[i])
    r = [0] * len(xs)
    for pos, i in enumerate(s):
        r[i] = pos
    return r

def spearman(x, y):
    if len(x) < 3:
        return None
    rx, ry = rank(x), rank(y)
    m = len(x)
    mx, my = sum(rx) / m, sum(ry) / m
    num = sum((p - mx) * (q - my) for p, q in zip(rx, ry))
    den = (sum((p - mx) ** 2 for p in rx) * sum((q - my) ** 2 for q in ry)) ** .5
    return num / den if den else None

first = [(a, rd[0]) for a, b, rd in codes]
print(f'3. Spearman rho, first number against alphabetical order of the word, all codes: '
      f'{spearman([a for a, _ in first], [w for _, w in first]):+.2f}')
cols = {}
for a, b, rd in codes:
    if fits(b, rd):
        cols.setdefault(b, []).append((a, [w for w in rd if IDX.get(w[0]) == b][0]))
tot, wsum = 0, 0.0
for b in sorted(cols):
    v = sorted(cols[b])
    rho = spearman([a for a, _ in v], [w for _, w in v])
    if rho is not None:
        tot += len(v); wsum += rho * len(v)
    print(f'   column {b:2d} ({AL[b-1]}): {len(v):2d} codes, rho {"" if rho is None else f"{rho:+.2f}"}  ' +
          ' '.join(f'{a}:{w}' for a, w in v))
print(f'   weighted mean rho inside the letter columns: {wsum/tot:+.2f}')
print(f'4. range: first number {min(a for a,_,_ in codes)}-{max(a for a,_,_ in codes)}, '
      f'second number {min(b for _,b,_ in codes)}-{max(b for _,b,_ in codes)}; '
      f'second numbers above 24: {sorted({f"{a}-{b}" for a,b,_ in codes if b > 24})}')
