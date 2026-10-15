"""Key-rebuild attempt for F22b: give values to the two-figure codes Lasry's reconstruction leaves empty.

Lasry's ~70 values are kept fixed. Each empty two-figure code (11, 13, 24, 27, ...) gets the syllable or letter,
from those his key lacks, that most improves the decoder's language-model score (coordinate ascent, several
sweeps, the order of codes shuffled per restart). Adding a value can only raise the best score, so every code is
always assigned and only the choice among values is scored; a value is kept only when it beats the code's best
"neutral" use by a margin (MARGIN nats), otherwise the code is left empty.

Held-out check: fit on one record, then score the other record's text with and without the new values
(sense measure of measure_sense.py, on a word split made by the same splitter).
usage: python rebuild.py fit R53|R54|both [restarts]
"""
import json
import os
import random
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'morosini1588'))
import decrypt as D  # noqa: E402

FILES = {'R53': 'decode/DOC_R53_D1717_1717.txt', 'R54': 'decode/DOC_R54_D1825_1825.txt'}
DOCS = {r: [it for _, it in D.parse(os.path.join(HERE, f), dot_first=True)] for r, f in FILES.items()}
BASE = {c: list(v) for c, v in D.CODES_B.items()}
HAVE = {pt for v in BASE.values() for pt, _ in v}
EMPTY = [f'{a}{b}' for a in range(1, 10) for b in range(10) if f'{a}{b}' not in BASE]
SYL = [c + v for c in 'bcdfglmnprstvz' for v in 'aeiou'] + ['ha', 'he', 'hi', 'ho', 'qui', 'quo', 'ua', 'ue', 'ui', 'uo',
       'gli', 'gn', 'ch', 'b', 'c', 'f', 'q', 'v', 'z', 'x', 'et', 'con', 'per', 'non', 'ss', 'tt', 'll']
CAND = [s for s in SYL if s not in HAVE]
MARGIN = 3.0


def score(codes, recs):
    tot = 0.0
    for r in recs:
        for items in DOCS[r]:
            _, per = D.decode(items, beam=150, codes=codes, nom=D.NOM_B, nulls=False)
            tot += per * len(items)
    return tot


def with_values(vals):
    codes = {c: list(v) for c, v in BASE.items()}
    for c, pt in vals.items():
        if pt:
            codes[c] = [(pt, 0.0)]
    return codes


def fit(recs, restarts=3, sweeps=3, seed=1):
    best_vals, best = None, -1e18
    for k in range(restarts):
        rnd = random.Random(seed + k)
        vals = {c: None for c in EMPTY}
        cur = score(with_values(vals), recs)
        for s in range(sweeps):
            order = EMPTY[:]
            rnd.shuffle(order)
            changed = 0
            for c in order:
                old = vals[c]
                trial = {}
                for pt in [None] + CAND:
                    vals[c] = pt
                    trial[pt] = score(with_values(vals), recs)
                top = max(trial, key=trial.get)
                pick = top if top is not None and trial[top] - trial[None] >= MARGIN else None
                vals[c] = pick
                changed += pick != old
                cur = trial[pick]
            print(f'restart {k} sweep {s}: score {cur:.1f}, changed {changed}', flush=True)
            if not changed:
                break
        if cur > best:
            best, best_vals = cur, dict(vals)
    return best_vals, best


def main():
    mode, which = sys.argv[1], sys.argv[2]
    restarts = int(sys.argv[3]) if len(sys.argv) > 3 else 3
    recs = ['R53', 'R54'] if which == 'both' else [which]
    base = score(with_values({}), recs)
    vals, sc = fit(recs, restarts)
    got = {c: v for c, v in vals.items() if v}
    print(f'base {base:.1f} -> {sc:.1f}; {len(got)} codes given values: {got}')
    out = os.path.join(HERE, f'rebuild_{which}.json')
    json.dump({'fitted_on': recs, 'base_score': base, 'score': sc, 'margin': MARGIN, 'values': got},
              open(out, 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
    for r in ('R53', 'R54'):
        for items in DOCS[r]:
            txt, per = D.decode(items, beam=400, codes=with_values(got), nom=D.NOM_B, nulls=False)
            print(f'== {r} ({per:.2f}/item)\n{txt}\n')


if __name__ == '__main__':
    main()
