"""Mechanical decryption for catalogue 2534. Standard library only.
    python scripts/decrypt.py <transcription.txt> <key.tsv>
Output, one line per transcription line ('Lxx.y: ...'):
  «word»        clear word of the letter
  abc           letters from letter groups (a run of letter groups is printed as one run; word breaks are not encoded)
  [value]       word or name group from the key (spaces as _)
  [#478]        group not in the key
"""
import sys
sys.stdout.reconfigure(encoding='utf-8')
tr, keyf = sys.argv[1:3]
key = {}
for line in open(keyf, encoding='utf-8'):
    if line.startswith('#') or not line.strip():
        continue
    g, v, t = line.rstrip('\n').split('\t')[:3]
    key[g] = (v, t)
for line in open(tr, encoding='utf-8'):
    if line.startswith('#') or not line.strip():
        continue
    lid, *toks = line.split()
    out, run = [], ''
    for t in toks:
        if t.startswith('='):
            if run: out.append(run); run = ''
            out.append('«' + t[1:] + '»')
        elif t in key and key[t][1] == 'letter':
            run += key[t][0]
        else:
            if run: out.append(run); run = ''
            out.append('[' + key[t][0].replace(' ', '_') + ']' if t in key else f'[#{t}]')
    if run: out.append(run)
    print(f'L{lid}: ' + ' '.join(out))
