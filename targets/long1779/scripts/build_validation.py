"""Build validation.tsv (input to docs/_validate.py) from reconciled_transcription.tsv.

System A words read with confidence (H) only; signs are the key's encoding of the reading. One sign per line; '?'
marks a break where words were unread, plain, probable, doubtful or in the second alphabet.
Usage (from targets/long1779): python scripts/build_validation.py [transcription] [out]
"""
import csv, json, sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent.parent
src = sys.argv[1] if len(sys.argv) > 1 else HERE / 'reconciled_transcription.tsv'
out = sys.argv[2] if len(sys.argv) > 2 else HERE / 'validation.tsv'
key = json.load(open(HERE / 'key_systemA_frozen.json', encoding='utf-8'))['key']
lines = ['# model: en-modern',
         '# source: reconciled_transcription.tsv (System A words, confidence H, signs = key encoding of the reading)',
         '# note: one sign per line; ? marks a break where words were unread, plain or doubtful']
brk = True
for r in csv.DictReader(open(src, encoding='utf-8'), delimiter='\t'):
    ok = r['alphabet'] == 'A' and r['confidence'] == 'H'
    if ok:
        sig = r['reconciled_signs'].replace("'", '')
        if any(c not in key for c in sig):
            ok = False
    if not ok:
        if r['confidence'] == 'plain' and r['alphabet'] == '-':
            continue
        if not brk:
            lines.append('?\t?'); brk = True
        continue
    for c in sig:
        lines.append('%s\t%s' % (c, key[c]))
    brk = False
open(out, 'w', encoding='utf-8').write('\n'.join(lines) + '\n')
print('signs', sum(1 for l in lines if not l.startswith('#') and not l.startswith('?')))
