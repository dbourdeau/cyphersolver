# 16/11/2026 : ajustement de la page de titre Army List 1778 (cle carleton1782) sur v.758 SEULEMENT (apprentissage).
import sys,re,collections
sys.path.insert(0,'.')
from parse import parse,expand
lines={}
for l in open('armylist_titlepage_1778.txt'):
    if l.startswith('#') or not l.strip(): continue
    n,t=l.rstrip('\n').split('\t'); lines[int(n)]=re.sub('[^a-z&]','',t.lower())
def cell(k,L=lines):
    r,c=map(int,k.split('-'))
    s=L.get(r,'')
    return s[c-1] if 1<=c<=len(s) else '?'
w=parse('transcription_758.txt')
clear=open('clair_epoque_p134-135.txt').read().split('\n',2)[2]
clear=clear.replace('19th July','').replace('with us, disappointed','with us, I am disappointed')
cw=[re.sub('[^a-z]','',x.lower()) for x in clear.replace('-',' ').split()]; cw=[x for x in cw if x]
i=0; pairs=[]; skips=[]
for col,g in w:
    if g[0].startswith('['): continue
    e=expand(g)
    if i<len(cw) and len(e)==len(cw[i]): pw=cw[i]; i+=1
    elif i+1<len(cw) and len(e)==len(cw[i])+len(cw[i+1]): pw=cw[i]+cw[i+1]; i+=2
    else: skips.append((col,' '.join(g),cw[i])); i+=1; continue
    pairs+=list(zip(e,pw))
if __name__=='__main__':
    print('pairs',len(pairs),'skips',len(skips),skips[:8],'next',cw[i:i+3])
    ok=sum(cell(a)==b for a,b in pairs); print('Army List 1778 tel quel : %d/%d = %.3f'%(ok,len(pairs),ok/len(pairs)))
    bad=collections.Counter((a,cell(a),b) for a,b in pairs if cell(a)!=b)
    for (a,k,b),n in sorted(bad.items(),key=lambda x:tuple(map(int,x[0][0].split('-')))): print(a,'1778=',k,'clair=',b,n)
