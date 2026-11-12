"""validation_pairs_1741.py: writes validation.tsv (cipher group TAB reading) for docs/_validate.py from the two bare documents
of 1741 (the Castellane letter and the reply, transcription_*_oct1741.txt) and key_1741.tsv. The reading of a group is its value in
the key (word codes as the French word: grefwen = comte ...); a group that is not in the key is '?'. Run from this folder."""
import re
FR = {'grefwen': 'comte', 'storviziren': 'grandvizir', 'ottporten': 'porte', 'hof': 'cour', 'swerige': 'suede',
      'ryssland': 'russie', 'frankrike': 'france', 'fred': 'paix', 'tractat': 'traite', 'konglmajt': 'roi', 'ambassadeur': 'ambassadeur'}
K = {}
for l in open('key_1741.tsv', encoding='utf-8'):
    if l[0] == '#' or not l.strip():
        continue
    f = l.rstrip('\r\n').split('\t'); K[f[0]] = f[1]
out = ['# model: fr-1600-letters', '# source: transcription_castellane_oct1741.txt and transcription_reply_oct1741.txt with key_1741.tsv',
       '# note: the bare pages of 1741 only; groups not in the key are ?; doubtful digits as read; clear sentences left out']
for fn in ('transcription_castellane_oct1741.txt', 'transcription_reply_oct1741.txt'):
    for l in open(fn, encoding='utf-8'):
        if l[0] == '#' or not l.strip():
            continue
        l = l.split(' ', 1)[1]
        l = re.sub(r'\[clear:[^\]]*\]', ' ', l)
        for t in l.split():
            if t in ',.;':
                continue
            g = re.sub(r"[?']", '', t)
            v = K.get(g)
            v = '?' if v is None else FR.get(v, v)
            out.append('%s\t%s' % (g, v))
open('validation.tsv', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print(len(out) - 3, 'tokens')
