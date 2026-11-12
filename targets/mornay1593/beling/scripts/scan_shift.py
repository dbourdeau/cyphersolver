"""Exploratory (PREREG.md, 'Not tested here'): the folded 1593 key with every number shifted by c = 1-100, on part A.
A search over 100 keys: its best result is a lead, not a pass. Usage from beling/:
  python3 -I scripts/scan_shift.py <path to mmoiresetcorre06morn_djvu.txt>   -> results/scan_shift.txt
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import test_folded as t

lm = t.Tri(Path(sys.argv[1]).read_text(encoding='utf-8', errors='replace'))
key = t.read_key('key/key_dudout.tsv')
A = (t.repo_passages('transcription/repo/lomenie1595.txt', 2, lambda i: i[0] in 'LD')
     + t.repo_passages('transcription/repo/duplessis1597.txt', 2, lambda i: i[0] in 'CW'))
rows = []
for c in range(0, 101):
    k2 = {str(int(f) + c): v for f, v in key.items()}
    n, ok, pieces, _ = t.run(A, k2, 'folded')
    L, nl = t.lang_score(lm, pieces)
    rows.append((c, ok / n, L, nl))
out = ['# c\tcoverage\tlang_score\tletters  (c = 0 is the frozen key)']
out += [f'{c}\t{cov:.3f}\t{L:.3f}\t{nl}' for c, cov, L, nl in rows]
best_cov = max(rows[1:], key=lambda r: r[1])
best_L = max((r for r in rows[1:] if r[3] >= 40), key=lambda r: r[2])
out.append(f'# best coverage, c>0: c={best_cov[0]} {best_cov[1]:.3f}; best language (>=40 letters), c>0: c={best_L[0]} {best_L[2]:.3f}')
(t.HERE / 'results/scan_shift.txt').write_text('\n'.join(out) + '\n', encoding='utf-8')
print(out[0]); print('\n'.join(out[1:6])); print(out[-1])
