# Compte règle de Daniel sur un fichier de lecture balisé (cf. en-tête de lecture/R22-lecture.txt).
import sys, re, collections
C = collections.Counter(); R = collections.defaultdict(list)
for l in open(sys.argv[1], encoding='utf-8'):
    if not l.startswith('@'): continue
    t = l.split(':', 1)[1]
    t = re.sub(r'«[^»]*»', ' ', t); t = re.sub(r'∅\d+', ' ', t).replace('|', ' ')
    for w in t.split():
        if '‹' in w: k = 'irresolus'
        elif '[' in w: k = 'restitues'
        elif '{' in w: k = 'probables'
        else: k = 'surs'
        C[k] += 1; R[k].append(w)
n = sum(C.values())
print(dict(C), 'mots', n)
print('surs+probables = %.1f %%' % (100*(C['surs']+C['probables'])/n))
for k in ('restitues', 'irresolus'): print(k, ' '.join(R[k]))
