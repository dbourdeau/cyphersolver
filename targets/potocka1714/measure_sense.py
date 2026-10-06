"""Word-level sense measure for potocka1714 (5 Oct 2026).

`coverage.json` 'valued' is key coverage: a figure counts once the key gives it a letter, whether or not the
letters make a word. 'conservative_coherent' drops whole segments whose reading note contains a hedge word.
Neither measures sense. Here every segment reading in reading.md was checked word by word: a valued token counts
as sense when its word reads as a word of the passage in the writer's spelling (slips that the context forces,
e.g. connedere = confedere, morcowide = moscovite, Krodyznski = Kroszynski, are sense; names whose letters
are firm count). The words below do not read and are excluded. Unvalued figures (codes, 73, R7524) never count.
Run: python targets/potocka1714/measure_sense.py
"""
import csv, json, os
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
# (record, segment) -> token positions (1-based) that do not read as sense, with the reason
NOT_SENSE = {
    ('7534', '43'): (range(1, 7), 'zaia[73]d: 73 unvalued, word not established'),
    ('7536', '70'): (range(10, 17), 'a Kinnik: no word or identified place'),
    ('7527', '89'): (range(1, 5), 'tegn: not a French word; tienne needs other figures'),
    ('7527', '94'): (range(5, 7), 'tombap: tombe reads, the final 52 78 (a p) do not'),
}


def main():
    rows = list(csv.DictReader(open(os.path.join(HERE, 'reading-tokens.tsv'), encoding='utf8'), delimiter='\t'))
    per = defaultdict(lambda: [0, 0])
    for r in rows:
        key = (r['record'], r['segment'])
        bad = key in NOT_SENSE and int(r['position']) in NOT_SENSE[key][0]
        ok = r['plain'] != '?' and not bad
        per[r['record']][0] += 1
        per[r['record']][1] += ok
    tot = sum(v[0] for v in per.values()); sense = sum(v[1] for v in per.values())
    pot = [(k, v) for k, v in per.items() if k != '7524']
    ptot = sum(v[0] for k, v in pot); psense = sum(v[1] for k, v in pot)
    out = dict(documents={k: dict(tokens=v[0], sense=v[1], fraction=round(v[1] / v[0], 4)) for k, v in sorted(per.items())},
               total=tot, sense=sense, fraction_sense=sense / tot,
               potocka_total=ptot, potocka_sense=psense, potocka_fraction=psense / ptot,
               excluded={f'{a}/{b}': c[1] for (a, b), c in NOT_SENSE.items()})
    json.dump(out, open(os.path.join(HERE, 'sense.json'), 'w', encoding='utf8'), indent=1, ensure_ascii=False)
    for k, v in out['documents'].items():
        print(k, v)
    print(f"all: {sense}/{tot} = {sense / tot:.4f};  Potocka letters: {psense}/{ptot} = {psense / ptot:.4f}")


if __name__ == '__main__':
    main()
