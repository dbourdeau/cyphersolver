"""Held-out test: apply key_frozen.tsv (built from L01-L10) to L11-L17 and compare, sign by sign,
with the value each sign has in the alignment with c. 42r. Points are not counted."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from common import read_align, read_key, HERE
key = read_key(os.path.join(HERE, 'key_frozen.tsv')); al = read_align()
ok = bad = unk = 0; rows = []
for lab in sorted(al):
    if lab <= 'L10': continue
    for w in al[lab]:
        for tok, val in w:
            if val == '_': continue
            k = key.get(tok)
            if k is None: unk += 1; rows.append((lab, tok, val, '(not in frozen key)'))
            elif k == val: ok += 1
            else: bad += 1; rows.append((lab, tok, val, k))
n = ok + bad + unk
print(f'held-out signs L11-L17: {n}; frozen key right {ok} ({ok/n:.1%}); wrong {bad}; sign not in frozen key {unk}')
print(f'of the signs the frozen key knows: {ok}/{ok+bad} = {ok/(ok+bad):.1%}')
for r in rows: print('\t'.join(r))

# Lenient count: a known sign counts as right when the frozen value and the read value begin with the same
# letter (same consonant family; the vowel marks of this syllabary are small and were not all separated).
len_ok = ok + sum(1 for r in rows if not r[3].startswith('(') and r[3][:1] == r[2][:1])
print(f'lenient (same consonant): {len_ok}/{ok+bad} = {len_ok/(ok+bad):.1%} of known signs; {len_ok}/{n} = {len_ok/n:.1%} of all held-out signs')
