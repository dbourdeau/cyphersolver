import sys,random,re,subprocess,os
sys.path.insert(0,'.')
from lang import lm
src=open('lang/corpora/'+sorted(f for f in os.listdir('lang/corpora') if 'nevers' in f.lower() or 'henri' in f.lower())[0],encoding='utf8',errors='ignore').read()
t=lm.norm(src[200000:260000],'early')
t=re.sub(r'\s+',' ',re.sub('[^a-z ]',' ',t)).strip()
N=int(sys.argv[1]); noise=float(sys.argv[2])
w=t.split(); s=' '.join(w[:N//5])[:N]
random.seed(1)
signs=list('abcdefghiklmnopqrstuvxyzGS3')
letters=sorted(set(s)-{' '})
key={}; pool=signs[:]; random.shuffle(pool)
for i,c in enumerate(letters): key[c]=[pool[i%len(pool)]]
for c in 'eaisn': key[c].append(pool.pop())  if pool else None
ct=''.join(' ' if c==' ' else (random.choice(signs) if random.random()<noise else random.choice(key[c])) for c in s)
open('vieuville1587/ctrl_ct.txt','w').write('x '+ct+'\n')
print('plain:',s[:150])
