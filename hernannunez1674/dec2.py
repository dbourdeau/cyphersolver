"""Second pass (22 Sept 2026): dec.py plus the image-checked values of the 118 groups dec.py left unread.

fix_R1012.tsv and fix_R1013-15.tsv give, for every token dec.py could not value, what the image shows and its
value (misread by DECODE, new code group fixed by the margin, null, or illegible), graded H/C/M/I. Key changes the
image pass found and applies everywhere: 167 = Suecia (in NOTES, missing from dec.py), 13 = e (not a null in this
hand: 13 8 = el, 13 ef = esse), N (underlined) = V.S.

Run from hernannunez1674/:  python dec2.py  ->  read2/R*.txt and a count per letter.
"""
import json, sys, csv
sys.stdout.reconfigure(encoding='utf-8')
K = json.load(open('../balbases1677/key.json', encoding='utf8'))
K.update({'d': 'que', 'N': 'V.S.', 'N_': 'V.S.', '30': 'p', '6+': 'o', '4': 't', '161': 'resolucion', 'os': 'para',
          'a': '', '>': '', '167': 'Suecia', '13': 'e'})
FIX = {}
for f in ('fix_R1012.tsv', 'fix_R1013-15.tsv'):
    for r in csv.DictReader(open(f, encoding='utf8'), delimiter='\t'):
        FIX[(r['record'], int(r['token_no']))] = r
tot = {'tokens': 0, 'unread': 0, 'M': 0}
for rec in ('R1012', 'R1013', 'R1014', 'R1015'):
    C, M = [], []
    for line in open(f'tx/{rec}.txt', encoding='utf8'):
        if line.startswith('C:'): C += line[2:].split()
        elif line.startswith('M:'): M.append(line[2:].strip())
    out, un, m = [], 0, 0
    for i, t in enumerate(C):
        fx = FIX.get((rec, i))
        if fx:
            if fx['kind'] == 'illegible': out.append('[?]'); un += 1; continue
            if fx['grade'] == 'M': m += 1
            out.append(f"{{{fx['value']}}}" if fx['kind'] != 'null' else '')
            continue
        v = K.get(t.strip('()=').rstrip('?'))
        if v is None: out.append('[' + t + ']'); un += 1
        else: out.append(v)
    tot['tokens'] += len(C); tot['unread'] += un; tot['M'] += m
    with open(f'read2/{rec}.txt', 'w', encoding='utf8') as w:
        w.write(f'===== {rec}: {len(C)} tokens, unread {un}, image-pass values graded M {m}; '
                '{..} = value from the image pass, [..] = unread\n')
        w.write(''.join(out) + '\n--- margin:\n' + ' '.join(M) + '\n')
    print(rec, len(C), 'tokens, unread', un, ', M', m)
print('total', tot, 'read', round(1 - tot['unread'] / tot['tokens'], 4),
      'read excluding M', round(1 - (tot['unread'] + tot['M']) / tot['tokens'], 4))
