"""Hill-climb a simple substitution on the given words. usage: solve.py LINES(e.g. 1-6 or 1-12) SEED RESTARTS [perm]"""
import sys, random, json, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import read_lines, lexicon, model, score
ALPH = 'abcdefghiklmnopqrstuxyz' if os.environ.get('VIND_LANG', 'la') == 'la' else 'abcdefghijklmnopqrstuvwxyz'

def decode(words, key):
    return ' '.join(''.join(key[c] for c in w) for w in words)

def solve(words, m, floor, rng, restarts=30, iters=6000):
    signs = sorted(set(''.join(words)))
    best = None
    for r in range(restarts):
        letters = list(ALPH); rng.shuffle(letters)
        key = {s: letters[i % len(letters)] for i, s in enumerate(signs)}
        cur = score(decode(words, key), m, floor)
        stale = 0
        while stale < iters:
            # move: swap the values of two signs, or give one sign a letter no sign has
            a = rng.choice(signs)
            unused = [c for c in ALPH if c not in key.values()]
            if unused and rng.random() < 0.2:
                old = key[a]; key[a] = rng.choice(unused); undo = lambda: key.__setitem__(a, old)
            else:
                b = rng.choice(signs); key[a], key[b] = key[b], key[a]; undo = lambda: key.update({a: key[b], b: key[a]})
            sc = score(decode(words, key), m, floor)
            if sc > cur: cur = sc; stale = 0
            else: undo(); stale += 1
        if best is None or cur > best[0]:
            best = (cur, dict(key))
    return best

if __name__ == '__main__':
    lo, hi = map(int, sys.argv[1].split('-'))
    seed = int(sys.argv[2]); restarts = int(sys.argv[3])
    rng = random.Random(seed)
    words = [w for (ln, w) in read_lines() if lo <= ln <= hi]
    if len(sys.argv) > 4 and sys.argv[4] == 'perm':
        letters = list(''.join(words)); rng.shuffle(letters); out = []; i = 0
        for w in words: out.append(''.join(letters[i:i + len(w)])); i += len(w)
        words = out
    lex = lexicon(); m, floor = model(lex)
    sc, key = solve(words, m, floor, rng, restarts)
    n = sum(len(w) for w in words)
    print(json.dumps({'lines': sys.argv[1], 'seed': seed, 'score_per_letter': round(sc / n, 4), 'key': key}, sort_keys=True))
    print(decode(words, key))
