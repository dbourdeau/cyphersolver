"""Rebuild transcription.txt, decryption.txt, reading_sv.txt from the word-level pairs and key.tsv, and print the counts.
Run from the target folder after scripts/make_key.py."""
import unicodedata
key = {l.split('\t')[0]: l.rstrip('\n').split('\t') for l in open('key.tsv', encoding='utf-8') if l[0] != '#'}
tot = K = X = dig = 0; read = []; dec = []; tr = []
for fn in ('wordpairs_322_323.tsv', 'wordpairs_324_325.tsv', 'wordpairs_326_327.tsv'):
    cur = None
    for l in open(fn, encoding='utf-8'):
        if l[0] == '#': continue
        f = (l.rstrip('\n').split('\t') + [''] * 7)[:7]
        if f[0] != cur:
            cur = f[0]
            for a in (read, dec, tr): a.append(f'\n\n[image {cur}]\n')
        if f[2] == 'C': read.append(f[4]); dec.append('{' + f[4] + '}'); continue
        gs = f[3].split(); tot += len(gs); tr.append(f[3]); dig += sum('?' in g for g in gs)
        if f[2] == 'K': K += len(gs); read.append(f[4])
        else: X += len(gs); read.append('[' + f[4] + ' ?]')
        dec.append('-'.join((key[g][1] if key[g][4] != 'single' else key[g][1].upper()) if g in key else '[' + g + ']' for g in gs))
print(f'groups {tot}; in confident words {K} ({K/tot:.1%}); in doubtful words {X}; doubtful digits {dig}')
open('transcription.txt', 'w', encoding='utf-8').write('# Groups in reading order, per image (from the word-level pairs; ? = doubtful digit).' + ' '.join(tr) + '\n')
open('decryption.txt', 'w', encoding='utf-8').write('# Decoded with key.tsv, word by word; {clear text}; UPPER = value seen once; [1234] = not in the key.' + ' '.join(dec) + '\n')
open('reading_sv.txt', 'w', encoding='utf-8').write('# The contemporary Swedish decipherment with the clear text, in order. [word ?] = doubtful (see the note column of the pairs).' + ' '.join(read) + '\n')
