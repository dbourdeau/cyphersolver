"""Write validation.tsv for docs/_validate.py: one cipher group per line with the value the frozen key gives it
(the mechanical decryption; marked repairs are not applied). Groups with an unread figure, or not in the key,
are written '?' (unread). usage: python scripts/validation_pairs.py TRANSCRIPTION [KEY_TSV]"""
import sys, os, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from decrypt import key, segs
T = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
k = key(sys.argv[2] if len(sys.argv) > 2 else None)
out = ['# source: ' + os.path.basename(sys.argv[1]) + ' with ' + (os.path.basename(sys.argv[2]) if len(sys.argv) > 2 else 'key_frozen.tsv'),
       '# note: mechanical values of the frozen key, one group per line; marked repairs not applied; unread groups ?']
n = r = 0
for sid, pre, gr, post in segs(sys.argv[1]):
    for g in gr:
        n += 1
        if re.fullmatch(r'\d\d', g) and g in k:
            out.append(f'{g}\t{k[g]}'); r += 1
        else:
            out.append(f'{g}\t?')
open(os.path.join(T, 'validation.tsv'), 'w', encoding='utf8', newline='\n').write('\n'.join(out) + '\n')
print(f'{n} groups, {r} with a value -> validation.tsv')
