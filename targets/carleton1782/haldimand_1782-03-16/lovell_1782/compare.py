"""Compare James Lovell's 1782 table of Army List cells (lovell_table.tsv) with our key, cell by cell.

    python targets/carleton1782/haldimand_1782-03-16/lovell_1782/compare.py

For every cell Lovell wrote with a letter: does it equal our key (key/armylist_titlepage_1778.txt, letters counted
from the left, & counted, no spaces or punctuation)? And is the cell used in the 16 March letter (either cipher copy,
alignment.tsv)? Writes comparison.tsv.
"""
import csv, re
from pathlib import Path

H = Path(__file__).resolve().parent
T = H.parents[1]

key = {}
for l in (T / 'key/armylist_titlepage_1778.txt').read_text(encoding='utf-8').splitlines():
    if '\t' in l and not l.startswith('#'):
        n, text = l.split('\t', 1)
        letters = [c for c in text if c.isalpha() or c == '&']
        key[int(n)] = [c.lower() for c in letters]

used = set()
for r in csv.DictReader((H.parent / 'alignment.tsv').open(encoding='utf-8'), delimiter='\t'):
    for col in ('p227_cipher', 'p737_cipher'):
        for tok in (r.get(col) or '').split():
            m = re.match(r'^(\d+)\.(\d+)$', tok)
            if m:
                used.add((int(m.group(1)), int(m.group(2))))

rows = [r for r in csv.DictReader((x for x in (H / 'lovell_table.tsv').open(encoding='utf-8') if not x.startswith('#')),
                                  delimiter='\t')]
out, stat = [], {}
for r in rows:
    ln, pl, le = int(r['line']), int(r['place']), r['letter'].strip()
    ours = key.get(ln, [])
    our = ours[pl - 1] if 0 < pl <= len(ours) else ''
    u = (ln, pl) in used
    verdict = 'blank' if not le else ('agree' if le == our else 'differs')
    stat.setdefault((verdict, u), 0)
    stat[(verdict, u)] += 1
    out.append((ln, pl, le, our, 'yes' if u else 'no', verdict, r['doubt']))
with (H / 'comparison.tsv').open('w', encoding='utf-8') as f:
    f.write('line\tplace\tlovell\tours\tused_in_16_march_letter\tverdict\tdoubt\n')
    for o in out:
        f.write('\t'.join(map(str, o)) + '\n')
lov_cells = {(int(r['line']), int(r['place'])) for r in rows if r['letter'].strip()}
print(f'Lovell cells with a letter: {sum(1 for o in out if o[5] != "blank")}; blank places: {sum(1 for o in out if o[5] == "blank")}')
for u in (True, False):
    a, d = stat.get(('agree', u), 0), stat.get(('differs', u), 0)
    print(f'  cells {"used" if u else "not used"} in the letter: {a} agree, {d} differ')
print(f'cells used in the letter (both copies): {len(used)}; given a letter by Lovell: {len(used & lov_cells)}; '
      f'missing from his table: {sorted(used - lov_cells)}')
print('differences:', [(o[0], o[1], o[2], o[3], o[4]) for o in out if o[5] == 'differs'])
