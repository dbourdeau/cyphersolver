"""Registered held-out test (PLAN.md). usage: VIND_LANG=la heldout.py
Key from lines 1-6 by the solver (seed 1, 30 restarts); applied unchanged to lines 7-12.
Word rate = share of held-out cipher words whose decode is a lexicon word (any frequency).
Controls: 1000 shuffles of the key's plain values among its signs (seed 20261126), 4-gram score per letter on lines 7-12."""
import sys, os, random, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import read_lines, lexicon, model, score, LANG
from solve import solve, decode

lex = lexicon(); m, floor = model(lex)
allw = read_lines()
train = [w for ln, w in allw if ln <= 6]
test = [w for ln, w in allw if ln >= 7]
sc, key = solve(train, m, floor, random.Random(1), restarts=30)
# signs that occur only in the held-out lines get no value (counted as not decoded)
dec = [''.join(key.get(c, '?') for c in w) for w in test]
hits = [d for d in dec if d in lex]
n = sum(len(w) for w in test)
true = score(' '.join(dec), m, floor) / n
rng = random.Random(20261126); vals = list(key.values()); signs = list(key)
ge = 0; best = -1e9
for _ in range(1000):
    rng.shuffle(vals); k2 = dict(zip(signs, vals))
    s = score(' '.join(''.join(k2.get(c, '?') for c in w) for w in test), m, floor) / n
    best = max(best, s); ge += s >= true
res = {'lang': LANG, 'train_lines': '1-6', 'test_lines': '7-12', 'key': key, 'test_words': len(test),
       'test_words_in_lexicon': len(hits), 'word_rate': round(len(hits) / len(test), 4),
       'score_per_letter': round(true, 4), 'best_control': round(best, 4), 'controls_at_or_above': ge,
       'pass': len(hits) / len(test) >= 0.8 and ge == 0}
print(json.dumps(res, sort_keys=True, ensure_ascii=False))
print(' '.join(dec))
