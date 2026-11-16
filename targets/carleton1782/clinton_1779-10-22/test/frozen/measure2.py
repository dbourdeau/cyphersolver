# Mesure unique PREREG_2026-11-16 : key2_armylist.tsv sur v.760 + P.S.
import sys,re,random,difflib,collections
sys.path.insert(0,'.')
from parse import parse,expand
key={}
for l in open('key2_armylist.tsv'):
    if l.startswith('#'): continue
    k,v=l.split('\t')[:2]; key[k]=v
w=parse('transcription_760.txt')
H=[x for c,g in w for x in expand(g)]
clear=open('clair_epoque_p134-135.txt').read().split('\n',2)[2]
a=clear.index('no alternative left'); b=clear.index('Chesapeak')+len('Chesapeak')
ref=re.sub('[^a-z]','',(clear[a:b]+' I have received your Dispatches by the Defiance').lower())
def score(k):
    dec=''.join(k.get(x,'?') if k.get(x,'?')!='?' else '?' for x in H)
    m=sum(bl.size for bl in difflib.SequenceMatcher(None,dec,ref,autojunk=False).get_matching_blocks())
    return m/len(H),dec
s,dec=score(key)
byline=collections.defaultdict(list)
for k in key: byline[k.split('-')[0]].append(k)
best=0
for seed in range(1,201):
    r=random.Random(seed); K={}
    for ln,cells in byline.items():
        L=[key[c] for c in cells]; r.shuffle(L); K.update(zip(cells,L))
    best=max(best,score(K)[0])
print('H groupes',len(H),'ref lettres',len(ref))
print('DEC',dec); print('REF',ref)
print('ACCORD %.3f  meilleur temoin %.3f  marge %.3f'%(s,best,s-best))
print('verdict','VALIDEE' if s>=0.85 and s>=best+0.30 else ('PARTIEL' if s>=0.5 and s>=best+0.30 else 'ECHEC'))
print('mots',' '.join(''.join(key.get(x,'?') for x in expand(g)) for c,g in w))
