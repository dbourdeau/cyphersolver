"""Decode the frozen blind Niccolini transcriptions ONCE with the milan1494 key (upstream main, sha256 in FREEZE.txt).
Usage: python3 -I decode_once.py <blind_dir> > decode_once.txt
Rendering per sign: single value -> the letter(s); several values -> {a|b}; null ('') -> nothing; '?' value or
unknown label -> '_'; doubtful label 'S12?' -> its value (doubt kept in the token list); '??' / NEWn -> '_'.
Runs are joined by ' / ' so the judge sees where clear words stood (given in the note column)."""
import csv, json, sys, os
B = sys.argv[1]
k = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../aaymeloglu/key.json')))['signs']
m = dict(r for r in csv.reader(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../sheet_to_key.tsv')), delimiter='\t'))
m.pop('label', None)

def val(tok):
    t = tok.rstrip('?')
    if t not in m:
        return '_'
    v = k[m[t]]['values']
    if v == ['']:
        return ''
    if v == ['?']:
        return '_'
    if len(v) == 1:
        return v[0]
    return '{' + '|'.join(x if x else '0' for x in v) + '}'

for doc in ('d42', 'd49', 'd81', 'd90'):
    f = os.path.join(B, f'BLIND_{doc}.tsv')
    rows = [r for r in csv.DictReader(open(f, encoding='utf-8'), delimiter='\t')]
    print(f'## {doc}')
    for r in rows:
        toks = r['labels'].split()
        print(f"{doc}\tL{r['line']}.{r['run']}\t{''.join(val(t) for t in toks)}\t{r.get('note','')}")
    print()
