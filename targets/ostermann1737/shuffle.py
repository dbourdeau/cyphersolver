# 5,000 shuffled keys per seed (letter values permuted among the letter signs), same language model
import sys,random,re
sys.path.insert(0,'/home/claude/keyless/ostermann1737/scripts')
import rulm
from common import *
from solve import text_words, render
m=rulm.LM(rulm.corpus(),5)
key={}
for l in open(W+'KEY.tsv').read().split('\n')[1:]:
    if l:
        f=l.split('\t')
        if f[3]=='letter': key[f[1]]=f[2]
for name,lines in (('full (lines 1-20)',TRAIN|HELD),('held-out (lines 17-20)',HELD),('training (lines 1-16)',TRAIN)):
    ws=text_words(lines); n=sum(map(len,ws))
    real=m.score(render(ws,key))
    print('%s: %d letter signs, real score %.1f (%.3f per sign)'%(name,n,real,real/n))
    for seed in (20261112,7):
        rnd=random.Random(seed); ks=list(key); vs=[key[k] for k in ks]; sc=[]
        for i in range(5000):
            v=vs[:]; rnd.shuffle(v); sc.append(m.score(render(ws,dict(zip(ks,v)))))
        mu=sum(sc)/len(sc); sd=(sum((x-mu)**2 for x in sc)/len(sc))**.5
        print('  seed %d: shuffles mean %.1f sd %.1f best %.1f; shuffles >= real: %d of 5000; z = %.1f'%(seed,mu,sd,max(sc),sum(x>=real for x in sc),(real-mu)/sd))
