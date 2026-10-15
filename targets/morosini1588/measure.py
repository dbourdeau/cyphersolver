"""Share of decoded units with a value, Meister no. 40 records only (14 Oct 2026 split).

Units = plaintext letters (one per decoded cipher element) + one per bracketed nomenclator group.
Unread = '?' letters and bracketed groups ending in '?' (off-list dotted codes, unknown elements).
Counts decrypt_raw.txt (Francia 22, Meister records; R53/R54 are F22b, now targets/morosini1589/, skipped)
and R17_decryption.txt (Francia 18/3, moved here from bergamo1585). Single-letter slips that decode to a
wrong letter are not caught by this count (1-3 per hundred letters by eye, see NOTES).
usage: python measure.py
"""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
SKIP = {'R53', 'R54'}


def count(path):
    per = {}
    rec = None
    for line in open(path, encoding='utf-8'):
        line = line.rstrip('\n')
        m = re.match(r'== (R\d+)', line)
        if m:
            rec = m.group(1)
            continue
        if not line or rec is None or rec in SKIP:
            continue
        codes = re.findall(r'\[[^\]]*\]', line)
        letters = re.sub(r'\[[^\]]*\]', '', line)
        tot = len(codes) + len(letters)
        bad = sum(1 for c in codes if c.endswith('?]')) + letters.count('?')
        t, b = per.get(rec, (0, 0))
        per[rec] = (t + tot, b + bad)
    return per


per = count(os.path.join(HERE, 'decrypt_raw.txt'))
per.update(count(os.path.join(HERE, 'R17_decryption.txt')))
T = sum(t for t, b in per.values())
B = sum(b for t, b in per.values())
for r in sorted(per, key=lambda x: int(x[1:])):
    t, b = per[r]
    print(f'{r}\t{t}\t{b}\t{1 - b / t:.4f}')
print(f'records {len(per)}  units {T}  unread {B}  read {1 - B / T:.4f}')
