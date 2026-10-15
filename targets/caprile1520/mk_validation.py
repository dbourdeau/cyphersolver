"""Build validation.tsv for caprile1519: the V1921 cipher runs from read_v1921.py (SIGN=value per token, the project's
reading of that letter; '' = null, '?' = unread). R1139/R1136 are claimed only as phrases over beam output (regrade21.py),
with no token-level alignment, and are left out; the 1519 two-tier cipher and R1137 are unread."""
import os, pathlib, sys
HERE = pathlib.Path(__file__).resolve().parent; os.chdir(HERE); sys.path.insert(0, str(HERE))
import read_v1921 as R
out = ['# model: it-cinquecento', '# source: read_v1921.py RUNS (V1921, 25 Feb 1521, 1520-21 sign cipher, key21 + V1921 values), mk_validation.py',
       '# note: V1921 only; R1139 and R1136 are read as phrases over beam output (no token alignment), left out; Italian 1521']
for run in R.RUNS:
    for item in run[3].split():
        if item == '|': continue
        sign, _, v = item.partition('=')
        v = v.rstrip('*')
        out.append(f'{sign}\t{"-" if v == "" else v}')
pathlib.Path('validation.tsv').write_text('\n'.join(out) + '\n', encoding='utf-8')
print(len(out) - 3)
