"""No. 29, second round (PLAN2.md): recount the words of ../no29_reading.md on the agreed groups only.

python no29_recount.py > no29_recount.txt

The reading's sentences (the '> ' lines) are aligned with align.py, unchanged, over no29_agreed.txt (the groups the
two blind readings agree on; 0 = not agreed), using the M97 key sheet alone
(../../../morris1813/beling/key/codebook_M97_13_transcription.csv, reading column). A word counts as read only when
it carries no hole mark in the reading ([?..], supplied letters, [...]) AND every one of its letters is placed on an
agreed group whose sheet value the alignment confirms; manuscript clear words are left out. Python standard library only.
"""
import csv, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(os.path.dirname(HERE)))
import align as A  # noqa: E402

tab = {}
for r in csv.DictReader(open(os.path.join(HERE, '..', '..', '..', 'morris1813', 'beling', 'key', 'codebook_M97_13_transcription.csv'), encoding='utf8')):
    v = A.norm(r['reading'] or '')
    if v:
        tab.setdefault(int(r['code_number']), {})[v] = 'H'
toks = ' '.join(l for l in open(os.path.join(HERE, 'no29_agreed.txt'), encoding='utf8') if not l.startswith('#')).split()
text = ' '.join(l[2:].strip() for l in open(os.path.join(HERE, '..', 'no29_reading.md'), encoding='utf8') if l.startswith('> '))
words = text.split()
holes_marked = [bool(re.search(r'\[', w)) for w in words]
clear = [bool(re.fullmatch(r'\W*\*[^*]+\*\W*', w)) for w in words]
plain = ' '.join(re.sub(r'\[\.\.\.(?: \d+)?\]', ' ', w).replace('[?', '').replace('[', '').replace(']', '').replace('*', '') for w in words)
out, _ = A.align(toks, plain, tab)
status = []
for how, tok, letters in out:
    status += ['K' if how == 'known' else 'C' if how == 'word' else 'H'] * len(letters)
P = A.norm(plain)
status += ['H'] * (len(P) - len(status))
pos = 0; n = read = marked = 0
for w, hm, cl in zip(words, holes_marked, clear):
    cw = A.norm(re.sub(r'\[\.\.\.(?: \d+)?\]', '', w).replace('[?', '').replace('[', '').replace(']', ''))
    seg = status[pos:pos + len(cw)]; pos += len(cw)
    if cl:
        continue
    n += 1
    if hm:
        marked += 1
        continue
    if seg and all(s in 'KC' for s in seg):
        read += 1
agreed = sum(1 for t in toks if t != '0' and t[0].isdigit()); total = sum(1 for t in toks if t[0].isdigit())
print(f'No. 29: {total} group positions, {agreed} agreed by the two blind readings ({agreed / total:.3f})')
print(f'words of no29_reading.md (manuscript clear words left out): {n}; marked as holes in the reading: {marked}')
print(f'words read on agreed groups with the sheet value confirmed: {read} = {read / n:.3f}')
print(f'(round 1 count in the reading, on either transcription: 695 of 772 = 0.900)')
