"""Held-out test of Code No. 15 key v1 on document A (Jefferson to Pinckney, 1 Jan 1793), as fixed in
plan/PROTOCOL_code15_heldout.md. Run once, after the FreeTSA timestamp of plan/MANIFEST.txt has been verified:
python3 scripts/heldout_test.py   (from output/code15_1793_2026-11-28). Writes test/heldout_result.json and
test/heldout_alignment.tsv."""
import csv, json, random, re, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from code15lib import load_groups, parse, words_of, matches

key = {r['group']: r['value'] for r in csv.DictReader(open('key/code15_key_v1.tsv', encoding='utf-8'), delimiter='\t')}
groups = [parse(g)[:2] for (_, _, g) in load_groups('transcription/code15_groups.tsv')['A']]
crib = [l for l in open('plaintext/heldout_crib.txt', encoding='utf-8') if not l.startswith('#')][0]
words = words_of(crib)
DRY = os.environ.get('CODE15_DRYRUN')  # plumbing check only: empty key, 3 shuffles, nothing written
if DRY: key = {'99999': 'x'}

# positions: (word index, char index); pieces may be part of a word, a whole word, or two whole words
starts = [(wi, ci) for wi, w in enumerate(words) for ci in range(len(w))] + [(len(words), 0)]
idx = {p: i for i, p in enumerate(starts)}
moves = []
for (wi, ci) in starts[:-1]:
    w = words[wi]; m = []
    for cj in range(ci + 1, len(w) + 1):
        m.append((w[ci:cj], idx[(wi + 1, 0)] if cj == len(w) else idx[(wi, cj)]))
    if ci == 0 and wi + 1 < len(words):
        m.append((w + ' ' + words[wi + 1], idx[(wi + 2, 0)]))
    moves.append(m)

def run(k):
    G, P = len(groups), len(starts) - 1
    NEG = -10**9
    best = [[NEG] * (P + 1) for _ in range(G + 1)]; back = [[None] * (P + 1) for _ in range(G + 1)]
    best[0][0] = 0
    for gi in range(G):
        num, mark = groups[gi]; v = k.get(num) if num else None
        row, nrow, nback = best[gi], best[gi + 1], back[gi + 1]
        for p in range(P):
            if row[p] == NEG: continue
            for piece, q in moves[p]:
                s = row[p] + (1 if (v is not None and matches(v, mark, piece)) else 0)
                if s > nrow[q]: nrow[q] = s; nback[q] = (p, piece)
    if best[G][P] == NEG: return None, []
    al = []; q = P
    for gi in range(G, 0, -1):
        p, piece = back[gi][q]; al.append(piece); q = p
    return best[G][P], al[::-1]

k_real, al = run(key)
n = sum(1 for num, _ in groups if num and num in key)
rng = random.Random(1793); vals = list(key.values()); nums = list(key.keys()); ge = 0; dist = []
for _ in range(3 if DRY else 1000):
    rng.shuffle(vals); s, _ = run(dict(zip(nums, vals))); dist.append(s); ge += (s >= k_real)
res = {'groups': len(groups), 'with_key_value': n, 'matches': k_real, 'precision': round(k_real / n, 3) if n else 0,
       'coverage': round(k_real / len(groups), 3), 'shuffled_max': max(dist), 'shuffled_mean': round(sum(dist) / len(dist), 2),
       'p': round((1 + ge) / 1001, 4)}
res['pass'] = res['precision'] >= 0.80 and res['p'] <= 0.01
if DRY: print('dry run', res, len(al)); sys.exit()
json.dump(res, open('test/heldout_result.json', 'w'), indent=1)
with open('test/heldout_alignment.tsv', 'w', encoding='utf-8') as f:
    f.write('pos\tgroup\tkey_value\tcrib_piece\tmatch\n')
    for i, ((num, mark), piece) in enumerate(zip(groups, al)):
        v = key.get(num) if num else None
        f.write(f'{i+1}\t{num or "?"}{mark}\t{v or ""}\t{piece}\t{int(bool(v and matches(v, mark, piece)))}\n')
print(json.dumps(res))
