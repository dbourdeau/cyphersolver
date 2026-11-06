"""Decode a transcription (t252.tsv, t142.tsv, t170.tsv) with key.tsv: one line of output per manuscript line.

    python decode.py t252.tsv          cipher words in CAPITALS, clear words in lower case, numerals as [n]
    python decode.py t252.tsv --alt    also show each sign's second value where the key has one
"""
import csv, sys
KEY = 'key_refined.tsv' if __import__('os').path.exists('key_refined.tsv') else 'key.tsv'
from build_key import merge

key, alt = {}, {}
for r in csv.DictReader(open(KEY, encoding='utf-8'), delimiter='\t'):
    key[r['token']] = '' if r['value'] == '(null)' else r['value']
    a = [x.split(':')[0] for x in r.get('alternatives', '').split()]
    alt[r['token']] = [x for x in a if x not in ('0',)][:1]


def word(toks, show_alt=False):
    out = []
    for t in merge(toks):
        v = key.get(t, '?')
        if show_alt and alt.get(t):
            v = f'{v}/{alt[t][0]}'
        out.append(v)
    return ''.join(out) if not show_alt else '|'.join(out)


if __name__ == '__main__':
    path = sys.argv[1]
    rows = list(csv.DictReader(open(path, encoding='utf-8'), delimiter='\t'))
    col = 'text' if 'text' in rows[0] else 'cipher'
    lines = {}
    for r in rows:
        if r['kind'] == 'C':
            w = word(r[col].split(), '--alt' in sys.argv).upper()
        elif r['kind'] == 'N':
            w = f'[{r[col]}]'
        else:
            w = r[col].lower()
        lines.setdefault(r['line'], []).append(w)
    for ln, ws in lines.items():
        print(f'{ln:>3}  {" ".join(ws)}')
