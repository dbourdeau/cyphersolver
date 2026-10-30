"""Write validation.tsv for docs/_validate.py: one cipher unit per line with what the key (key.json + the extended
values of the 30 Oct 2026 retry, measure.py) gives it at that place.

Units are the decoder's units (scripts/data/alignment.json): a pair unit (Ho, oH, nq, LL, Ga, Gp, ve, Om) is one
token. A polyphonic sign carries the value of its set that the alignment chose; a code sign its word(s); a null '-';
a lost sign or a sign with no value at that place '?'.

    python scripts/make_validation.py
"""
import importlib.util, pathlib

H = pathlib.Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('measure', H / 'measure.py')
M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)

out = ['# model: la-letters',
       '# source: scripts/data/alignment.json units decoded by measure.emit (key.json + EXTENDED/EXT_CODE)',
       '# note: pair units are one token; code signs read as their words; damage and unvalued places are ?']
n = 0
for p in M.P:
    if p['type'] == 'skip': continue
    e = M.emit(p)
    if e in ('_', '#') or '#' in e or '_' in e: v = '?'
    elif e == '': v = '-'
    else: v = e.strip('{}')
    out.append(f"{p['sign']}\t{v}"); n += 1
(H / 'validation.tsv').write_text('\n'.join(out) + '\n', encoding='utf-8')
print(n, 'units')
