import re, sys, difflib, collections
sys.path.insert(0, sys.argv[3])
from pass2_check import norm
dec=[]
for l in open(sys.argv[2], encoding='utf-8'):
    if l.startswith('#') or l.startswith('f.'): continue
    l=re.sub(r'<[^>]*>','',l); l=re.sub(r'^\d+\s','',l).replace('v. mad.','vuestra magestad').replace('v. ma.','vuestra magestad').replace('v.mad.','vuestra magestad').replace('^','')
    dec += [norm(w) for w in re.findall(r"[A-Za-zÁÉÍÓÚáéíóúñÑçÇ]+", l)]
dec=[w for w in dec if w]
ours=[]
for l in open(sys.argv[1], encoding='utf-8'):
    if l.startswith('#') or not l.strip(): continue
    txt=l.split(' ',1)[1]; txt=re.sub(r'«[^»]*»',' ',txt)
    for m in re.finditer(r'\{[^}]*\}|\[[^\]]*\]|<[^>]*>|[^\s{}\[\]<>]+', txt):
        w=m.group(0)
        if w.endswith('-'): continue
        k='P+' if w.startswith('{') and '†' in w else 'P' if w.startswith('{') else 'R' if w.startswith('[') else 'I' if w.startswith('<') else 'S'
        ours.append((k, norm(w.strip('{}[]<>†'))))
# join split words already counted on ending line: approximate
a=[w for k,w in ours]; sm=difflib.SequenceMatcher(None,a,dec,autojunk=False)
hit=set()
for blk in sm.get_matching_blocks():
    for i in range(blk.size): hit.add(blk.a+i)
c=collections.Counter(); h=collections.Counter()
for i,(k,w) in enumerate(ours):
    c[k]+=1; h[k]+= i in hit
for k in ['S','P','P+','I','R']:
    if c[k]: print(k, c[k], 'aligned-equal', h[k], '%.1f %%'%(100*h[k]/c[k]))
print('decipherment words', len(dec), 'our words', len(ours))
near=collections.Counter(); ex=[]
for op,i1,i2,j1,j2 in sm.get_opcodes():
    if op!='replace': continue
    for i in range(i1,i2):
        best=max((difflib.SequenceMatcher(None,a[i],dec[j]).ratio(),dec[j]) for j in range(j1,j2))
        if best[0]>=0.75: near[ours[i][0]]+=1
        elif ours[i][0]=='S': ex.append((a[i],' '.join(dec[j1:j2])[:40]))
for k in ['S','P','P+']: print(k,'equal+near', h[k]+near[k], '%.1f %%'%(100*(h[k]+near[k])/c[k]))
print(ex[:40])
