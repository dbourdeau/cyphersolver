"""Held-out test of a frozen key. Standard library only.

    python scripts/heldout.py <key_frozen.tsv> <transcription.txt> <reading.md> <label> [<label> ...]

For the named lines: every cipher letter is decrypted with the frozen key and compared with the letter of the final
reading at the same place (the reading lines used must carry no marks). A two-valued key letter (a|b) counts as right
when the reading letter is one of its values. Letters not in the frozen key count as wrong. Clear =words= are skipped.
"""
import re, sys, unicodedata
sys.stdout.reconfigure(encoding='utf-8')
def norm(s):
    s = unicodedata.normalize('NFD', s)
    return re.sub('[^a-z]', '', ''.join(c for c in s if not unicodedata.combining(c)).lower())
key = {}
for l in open(sys.argv[1], encoding='utf-8'):
    if l.strip() and not l.startswith('#'):
        c, v = l.rstrip('\n').split('\t')[:2]; key[c] = set(v.split('|'))
tr = {l.split('\t')[0]: l.rstrip('\n').split('\t')[1] for l in open(sys.argv[2], encoding='utf-8') if '\t' in l and not l.startswith('#')}
md = open(sys.argv[3], encoding='utf-8').read().split('```marked')[1].split('```')[0]
rd = {l.split('|')[0].strip(): l.split('|', 1)[1] for l in md.strip().splitlines() if '|' in l}
right = wrong = miss = 0; words_ok = words = 0
for lab in sys.argv[4:]:
    assert '{' not in rd[lab] and '«' not in rd[lab], lab + ' carries marks'
    toks = tr[lab].split()
    reading = norm(rd[lab])
    pos = 0
    for t in toks:
        if t.startswith('='):
            pos += len(norm(t.strip('='))); continue
        ok = True
        for ch in t:
            r = reading[pos]; pos += 1
            if ch not in key: miss += 1; ok = False
            elif r in key[ch]: right += 1
            else: wrong += 1; ok = False
        words += 1; words_ok += ok
    assert pos == len(reading), (lab, pos, len(reading))
n = right + wrong + miss
print(f'held-out lines {" ".join(sys.argv[4:])}: {n} cipher letters, right {right} ({100*right/n:.1f}%), '
      f'wrong {wrong}, not in frozen key {miss}; cipher groups wholly right {words_ok}/{words}')
