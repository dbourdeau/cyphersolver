"""Held-out test of the candidate keys, catalogue 1500. Standard library only.

    python scripts/heldout.py <path to Dan's lang/lexicons/es.json.gz>

Held out: every letter run except R05 (the crib). Lone numbers, PHI and the group 98 (not in the letter table)
are left out. Each run is decrypted (parts joined across line breaks) and scored two ways against the repo's
Spanish lexicon (lang/lexicons/es.json.gz; words of 1-2 letters only if among the 40 commonest):
  whole-run: the run is exactly one lexicon word, or exactly two or three of them; score = groups in such runs;
  letter-level: share of groups that fall inside lexicon words in the best cut (weak: a 30,000-word list covers
  much random text, so it is printed only for comparison). Control: 1,000 random keys that keep the seven crib values and shuffle the
other letters over the other values (seed 1500).
Proper names (Olinda, Paulino) and 'ministerial' are not in the lexicon, so the score is a floor.
"""
import gzip, json, pathlib, random, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import build_keys, decrypt
sys.stdout.reconfigure(encoding='utf-8')
ROOT = pathlib.Path(__file__).resolve().parent.parent
lex = json.load(gzip.open(sys.argv[1]))
short = set(sorted((w for w in lex if len(w) <= 2), key=lambda w: -lex[w])[:40])
words = {w for w in lex if len(w) >= 3} | short

held = []
for rid, where, run, ctx in decrypt.runs(ROOT / 'transcription_varela1850.txt'):
    if rid.startswith('R') and rid != 'R05':
        gs = [int(g) for part in run.split(' / ') for g in part.split('.') if g.strip().isdigit() and int(g) != 98]
        held.append((rid, gs))


def covered(letters):
    n = len(letters)
    best = [0] * (n + 1)
    for i in range(1, n + 1):
        best[i] = best[i - 1]
        for j in range(max(0, i - 14), i):
            if ''.join(letters[j:i]) in words:
                best[i] = max(best[i], best[j] + (i - j))
    return best[n]


def whole(letters, maxw=3):
    n = len(letters)
    best = [99] * (n + 1); best[0] = 0
    for i in range(1, n + 1):
        for j in range(max(0, i - 14), i):
            if best[j] < 99 and ''.join(letters[j:i]) in words:
                best[i] = min(best[i], best[j] + 1)
    return best[n] <= maxw


def score(k, show=False, mode='whole'):
    tot = cov = 0
    for rid, gs in held:
        letters = [k.get(g, '?') for g in gs]
        c = (len(gs) if whole(letters) else 0) if mode == 'whole' else covered(letters)
        tot += len(gs); cov += c
        if show:
            print(f'  {rid}	{"".join(letters)}	{c}/{len(gs)}')
    return cov, tot


for mode in ('whole', 'letter'):
    print(f'== {mode} ==')
    for v in 'ABC':
        c, t = score(build_keys.key(v), show=(mode == 'whole'), mode=mode)
        print(f'candidate {v}: {c}/{t} held-out groups ({100 * c / t:.1f}%)')
    rng = random.Random(1500)
    base = build_keys.key('A')
    free_vals = [v for v in base if v not in build_keys.CRIB]
    free_letters = [base[v] for v in free_vals]
    res = []
    for _ in range(1000):
        rng.shuffle(free_letters)
        k = dict(build_keys.CRIB); k.update(zip(free_vals, free_letters))
        res.append(score(k, mode=mode)[0])
    a, t = score(base, mode=mode)
    print(f'control (1,000 shuffles of the non-crib values): mean {100 * sum(res) / len(res) / t:.1f}%, '
          f'max {100 * max(res) / t:.1f}%, shuffles at or above candidate A: {sum(r >= a for r in res)}')
