# Build the French model and code vocabulary from Turner 1904 (ministers to the US, 1791-97), French paragraphs only.
import re,unicodedata,collections as C,sys,pickle,math
import numpy as np
W=r'C:/Users/dbour/cypher/.work/delacroix1797/'
T=open(W+'turner.txt',encoding='utf8',errors='replace').read()
SW=set('le la les de des du et que qui dans pour par une un en est au aux sur ne pas je vous nous il elle ce cette a'.split())
EN=set('the of and to in that is was for with by from this have his be as on'.split())
paras=re.split(r'\n\s*\n',T)
def norm(s):
    s=unicodedata.normalize('NFD',s); s=''.join(c for c in s if not unicodedata.combining(c)).lower()
    s=s.replace('1\'',"l'").replace('œ','oe')
    s=re.sub(r"-\s+",'',s)
    s=re.sub(r"[^a-z]+",' ',s)
    return s.strip()
keep=[]
for p in paras:
    n=norm(p).split()
    if len(n)<25: continue
    a=sum(w in SW for w in n);b=sum(w in EN for w in n)
    if a>0.2*len(n) and b<0.03*len(n): keep.append(' '.join(n))
txt=' '.join(keep)
print('french chars',len(txt),'paras',len(keep))
open(W+'turner_fr.txt','w',encoding='utf8').write(txt)
words=txt.split()
wc=C.Counter(words)
print('types',len(wc),[w for w,_ in wc.most_common(40)])
pickle.dump(wc,open(W+'wc.pkl','wb'))
# char 5-gram with spaces; alphabet a-z + space = 27
A={c:i for i,c in enumerate('abcdefghijklmnopqrstuvwxyz ')}
x=np.array([A[c] for c in txt],dtype=np.int64)
ORD=5
idx=np.zeros(len(x)-ORD+1,dtype=np.int64)
for k in range(ORD): idx=idx*27+x[k:len(x)-ORD+1+k]
cnt5=np.bincount(idx,minlength=27**5).astype(np.float64)
cnt4=cnt5.reshape(-1,27).sum(1)
cnt3=cnt4.reshape(-1,27).sum(1)
cnt2=cnt3.reshape(-1,27).sum(1)
cnt1=cnt2.reshape(-1,27).sum(1)
# interpolated conditional log P(c5|c1..c4)
p1=(cnt1+1)/(cnt1.sum()+27)
p2=(cnt2.reshape(27,27)+27*p1[None,:]*0.5)/(cnt1[:,None]+13.5)
p3=(cnt3.reshape(729,27)+5*np.tile(p2,(27,1)))/(cnt2[:,None]+5)
p4=(cnt4.reshape(19683,27)+3*np.tile(p3,(27,1)))/(cnt3[:,None]+3)
p5=(cnt5.reshape(531441,27)+2*np.tile(p4,(27,1)))/(cnt4[:,None]+2)
np.save(W+'lm5.npy',np.log(p5).astype(np.float32))
ent=-np.mean(np.log(p5[idx//27,x[ORD-1:]]))
print('in-sample nats/char',ent)
