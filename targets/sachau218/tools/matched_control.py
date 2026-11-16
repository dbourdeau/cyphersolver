"""Matched control for the one test of Sachau 218 f. 231r (added 16 Nov 2026, after the frozen measure).

Question: at this length and with this design, would the frozen test (tools/measure.py) pick out the TRUE key?
Each trial takes a held-out run of Arabic words (the last 15% of the corpus, not used to train the bigram model),
cut into 13 groups of about 59 letters as on the leaf, reduced to the same 22-letter alphabet. The letters that
K1 values (alif, ba, jim, dal, ha, ha', ta') are given K1's sign classes (dal to E or F at random); every other
letter becomes an unknown sign, as on the leaf. The true key is scored exactly as measure.py scores K1, against
the same kind of null (200 keys giving the 8 classes 8 random letters), and its rank among 201 is recorded.
No red-dot rule (there is no dot in a synthetic text). It also counts the groups of two or more letters
that the true key decodes entirely (the frozen sense rule asks for three whole words).

  python3 tools/matched_control.py <corpus.txt>      (corpus: Tanzil 'simple-clean', lines 'sura|aya|text')
"""
import sys, math, random, collections

A22 = 'ابجدهوزحطيكلمنسعفصقرشت'
NORM = {'ث': 'ت', 'خ': 'ك', 'ذ': 'د', 'ض': 'ص', 'ظ': 'ط', 'غ': 'ع', 'ة': 'ه', 'ى': 'ي',
        'أ': 'ا', 'إ': 'ا', 'آ': 'ا', 'ء': 'ا', 'ؤ': 'و', 'ئ': 'ي'}
K1 = {'I': 'ا', 'R': 'ب', 'W': 'ج', 'E': 'د', 'F': 'د', 'O': 'ه', 'L': 'ح', 'N9': 'ط'}
INV = {}
for s, c in K1.items():
    INV.setdefault(c, []).append(s)

words = []
for line in open(sys.argv[1], encoding='utf8'):
    for w in line.split('|')[-1].split():
        w = ''.join(NORM.get(c, c) for c in w)
        w = ''.join(c for c in w if c in A22)
        if w:
            words.append(w)
cut = int(len(words) * 0.85)
train, held = words[:cut], words[cut:]
big, uni = collections.Counter(), collections.Counter()
for w in train:
    for a, b in zip(w, w[1:]):
        big[a + b] += 1; uni[a] += 1
V = len(A22)
lp = lambda a, b: math.log((big[a + b] + 1) / (uni[a] + V))

def score(groups, key):
    t = n = 0
    for g in groups:
        d = [key.get(x) for x in g]
        for a, b in zip(d, d[1:]):
            if a and b:
                t += lp(a, b); n += 1
    return t / n if n else float('-inf')

rnd = random.Random(20261116)
ranks, firsts, whole = [], 0, []
TRIALS = 200
for trial in range(TRIALS):
    while True:                                   # 13 consecutive held-out words, 55-63 letters
        i = rnd.randrange(len(held) - 13)
        run = held[i:i + 13]
        if 55 <= sum(map(len, run)) <= 63:
            break
    unknown = {}
    groups = []
    for w in run:
        g = []
        for c in w:
            if c in INV:
                g.append(rnd.choice(INV[c]))
            else:
                g.append(unknown.setdefault(c, 'U%d' % len(unknown)))
        groups.append(g)
    s_true = score(groups, K1)
    nulls = [score(groups, dict(zip(K1, rnd.sample(A22, 8)))) for _ in range(200)]
    rank = 1 + sum(x > s_true for x in nulls)
    ranks.append(rank); firsts += (rank == 1)
    whole.append(sum(all(x in K1 for x in g) and len(g) > 1 for g in groups))
ranks.sort()
print('trials', TRIALS, '| true key ranked 1st of 201 (the frozen pass rule):', firsts,
      '| median rank', ranks[TRIALS // 2], '| 90th percentile rank', ranks[int(TRIALS * 0.9)],
      '| worst', ranks[-1])
print('share of trials where the true key ranks 12th or worse (K1 on the leaf ranked 12th):',
      round(sum(r >= 12 for r in ranks) / TRIALS, 3))
print('groups of 2+ letters decoded entirely by the true key: mean', round(sum(whole) / TRIALS, 2),
      '| trials with 3 or more (the frozen sense rule needs 3 whole words):', sum(w >= 3 for w in whole))
