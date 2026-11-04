"""One-part code test: code numbers should rise with the plaintext alphabet. Prints every value of key.tsv (status
both/n63/solms) whose initial letter breaks the order against its neighbours. Normalisations: C/K and Ch/K are not merged;
'Hertzog in X', 'König in X', 'Graf von X' sort by their first word (as in the code book's own entries).
Exit 1 if more than 5% of values break the order."""
import pathlib, sys
ROOT = pathlib.Path(__file__).resolve().parent.parent
rows = []
for l in (ROOT / 'key.tsv').read_text(encoding='utf8').splitlines():
    if l.startswith(('#', 'group')): continue
    g, v, s, src = l.split('\t')
    if s == 'doubt' or int(g) < 100: continue
    rows.append((int(g), v, v.lstrip('[?').upper().replace('Ä', 'A').replace('Ö', 'O').replace('Ü', 'U')[:1]))
bad = []
for i, (g, v, c) in enumerate(rows):
    prev = [x[2] for x in rows[max(0, i - 3):i]]; nxt = [x[2] for x in rows[i + 1:i + 4]]
    if (prev and c < max(prev[-1:])) and (nxt and c > min(nxt[:1])):
        bad.append((g, v))
    elif prev and nxt and c < prev[-1] and c < min(nxt):
        bad.append((g, v))
print(f'{len(rows)} values; out of alphabetical order: {len(bad)}')
for b in bad: print('  ', *b)
sys.exit(1 if len(bad) > 0.05 * len(rows) else 0)
