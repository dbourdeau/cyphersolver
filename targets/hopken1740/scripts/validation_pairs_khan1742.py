"""validation_pairs_khan1742.py: writes validation_khan1742.tsv (cipher group TAB reading) for docs/_validate.py from the Khan's letter
(transcription_khan1742.txt, pass 3) and the FROZEN key key_1741.tsv (not fitted to
these pages). The reading of a group is its value in the frozen key (word codes as the French word: ottporten = porte ...);
a group that is not in the frozen key is '?', so the 21 values taken from this document's gloss are left out. Doubtful
digits as read; clear words left out. Run from this folder (targets/hopken1740)."""
import re
FR = {'grefwen': 'comte', 'storviziren': 'grandvizir', 'ottporten': 'porte', 'hof': 'cour', 'swerige': 'suede',
      'ryssland': 'russie', 'frankrike': 'france', 'fred': 'paix', 'tractat': 'traite', 'konglmajt': 'roi',
      'ambassadeur': 'ambassadeur', 'minister': 'ministre'}
K = {}
for l in open('key_1741.tsv', encoding='utf-8'):
    if l[0] == '#' or not l.strip():
        continue
    f = l.rstrip('\r\n').split('\t'); K[f[0]] = f[1]
out = ['# model: fr-1600-letters', '# source: transcription_khan1742.txt (pass 3) with key_1741.tsv',
       '# note: groups not in the frozen key are ?; doubtful digits as read; clear words left out']
for l in open('transcription_khan1742.txt', encoding='utf-8'):
    if l[0] == '#' or not l.strip():
        continue
    l = l.split(' ', 1)[1]
    l = re.sub(r'\[clear:[^\]]*\]', ' ', l)
    for t in l.split():
        if t in ',.;:':
            continue
        g = re.sub(r"[?']", '', t)
        v = K.get(g)
        v = '?' if v is None else FR.get(v, v)
        out.append('%s\t%s' % (g, v))
open('validation_khan1742.tsv', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print(len(out) - 3, 'tokens')
