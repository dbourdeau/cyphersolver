"""Compare the two transcriptions of the Argumedo runs pair by pair, per document (no decoding).
Usage: python3 scripts/compare_t1_t2.py   (run from targets/argumedo1921/beling/)"""
import re, difflib, csv
from pathlib import Path

def pairs(s):
    s = s.replace('÷', '.').replace('=', '.').replace(':', '.')
    s = re.sub(r'\[([^\]|]*)\|[^\]]*\]', lambda m: m.group(1), s)  # first alternative
    s = s.replace('?', 'X')
    toks = re.findall(r'[0-9XQ]+', s)
    out = []
    for t in toks:
        if len(t) % 2 == 0:
            out += [t[i:i+2] for i in range(0, len(t), 2)]
        else:
            out.append(t)  # odd-length token kept whole (e.g. a lone 1)
    return out

def load_t1(p):
    d = {}
    for line in Path(p).read_text(encoding='utf-8').splitlines():
        if not line.startswith('DCXXI'): continue
        f = line.split('\t')
        d.setdefault(f[0], []).extend(pairs(f[3]))
    return d

def load_t2(p):
    d = {}
    with open(p, newline='', encoding='utf-8') as fh:
        for r in csv.DictReader(fh, delimiter='\t'):
            d.setdefault(r['doc'], []).extend(pairs(r['run']))
    return d

t1 = load_t1('transcription_T1.txt'); t2 = load_t2('transcription_T2_blind.tsv')
tot = agree = 0
for doc in sorted(set(t1) | set(t2)):
    a, b = t1.get(doc, []), t2.get(doc, [])
    sm = difflib.SequenceMatcher(a=a, b=b, autojunk=False)
    m = sum(x.size for x in sm.get_matching_blocks())
    tot += max(len(a), len(b)); agree += m
    print(f'{doc}: T1 {len(a)} pairs, T2 {len(b)} pairs, matching {m}')
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op != 'equal':
            ctx = '-'.join(a[max(0,i1-3):i1])
            print(f'   {op}: T1 {"-".join(a[i1:i2]) or "(none)"}  T2 {"-".join(b[j1:j2]) or "(none)"}   after ...{ctx}')
print(f'ALL: {agree} of {tot} pair places agree')
