"""Count cipher words, read words and holes per letter from reading_marked.tsv, and check that every unmarked word
is what decryption.tsv gives (letters only). Usage (from targets/argumedo1921/beling/round2/): python3 -I scripts/count_words.py"""
import csv, re
from pathlib import Path
dec = {}
for r in csv.DictReader(open('decryption.tsv', encoding='utf-8'), delimiter='\t'):
    dec[(r['doc'], r['run'])] = re.sub(r'[^A-ZÑ]', '', r['decode'])
tot = {}; bad = 0
lines = [l for l in Path('reading_marked.tsv').read_text(encoding='utf-8').splitlines() if l.startswith('DCXXI')]
for l in lines:
    doc, run, words, note = (l.split('\t') + [''])[:4]
    ws = words.split()
    # reconstruct the key's output from the marks and compare with the decryption
    got = ''.join(re.sub(r'\{([^/]*)/[^}]*\}', lambda m: '' if m.group(1) in '-' else m.group(1), w).replace('*', '') for w in ws)
    want = dec[(doc, run)].replace('?', '')
    got = re.sub(r'\d+|\?', '', got)
    if got != want:
        bad += 1; print('MISMATCH', doc, run, got, want)
    t = tot.setdefault(doc, [0, 0, 0])
    for w in ws:
        t[0] += 1
        if '{' in w: t[2] += 1
        else: t[1] += 1
G = [0, 0, 0]
print('letter\tcipher_words\tread\tholes\tshare')
for d, (n, r, h) in sorted(tot.items()):
    print(f'{d}\t{n}\t{r}\t{h}\t{r/n:.3f}'); G = [G[0]+n, G[1]+r, G[2]+h]
print(f'ALL\t{G[0]}\t{G[1]}\t{G[2]}\t{G[1]/G[0]:.3f}')
print('marks consistent with decryption.tsv' if not bad else f'{bad} mismatches')
