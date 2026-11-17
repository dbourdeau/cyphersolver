"""Independent check by the project (16 Nov 2026) of Brice Dudout's identification (PR #690).
Check the numeral lines of Trinity College O.4.22 f. 248v against the Paschal full moon (nomikon phaska) of the
Julian computus, indexed by the Byzantine cycle of the moon. Reads pairs.tsv, writes nothing.

Paschal full moon of year AD Y (Julian calendar): 21 March + ((19 * (Y mod 19) + 15) mod 30) days.
Byzantine cycle of the moon of that year: (Y + 5508) mod 19, with 0 written 19.
"""
import pathlib

def full_moon(y):
    d = 21 + (19 * (y % 19) + 15) % 30          # day counted in March
    return ('March', d) if d <= 31 else ('April', d - 31)

table = {}
for y in range(1000, 1019):                     # any 19 consecutive years
    table[(y + 5508) % 19 or 19] = full_moon(y)

rows = [l.split('\t') for l in pathlib.Path(__file__).with_name('pairs.tsv').read_text(encoding='utf8').splitlines()
        if l and not l.startswith('#')]
ok = 0
for r in rows:
    n, v = int(r[0]), int(r[3])
    month, day = table[n]
    hit = v == day
    ok += hit
    print(f'{n:2d}  {r[1]:>2} {r[2]:>3}  value {v:2d}  full moon {day:2d} {month:5s}  {"match" if hit else "DIFFERENT"}')
print(f'{ok} of {len(rows)} values equal the day of the Paschal full moon; counts run 1..{len(rows)}:',
      [int(r[0]) for r in rows] == list(range(1, len(rows) + 1)))
