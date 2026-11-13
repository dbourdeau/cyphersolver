import sys,re,math,random,hashlib,json
sys.path.insert(0,'/home/claude/en/trackB/b198_magdeburg_blind/scripts')
from decode import words,K
B='/home/claude/en/trackB/b198_magdeburg_blind/'
raw=open(B+'corpus/pg5323.txt','rb').read()
md5=hashlib.md5(raw).hexdigest(); assert md5=='e966df334531570ffaaf4b4466ce2494'
t=raw.decode('utf-8')
a=t.find('*** START'); b=t.find('*** END'); t=t[t.find('\n',a):b].lower()
for x,y in (('ä','a'),('ö','o'),('ü','u'),('ß','ss')): t=t.replace(x,y)
t=re.sub(r'[^a-z]+',' ',t)
tw=t.split(); frac=sum(w in('und','der','die','das','nicht') for w in tw)/len(tw); assert frac>0.07, frac
A='abcdefghijklmnopqrstuvwxyz '
from collections import Counter
c4=Counter(t[i:i+4] for i in range(len(t)-3)); c3=Counter(t[i:i+3] for i in range(len(t)-2))
V=len(A)
def lp(s):
    return sum(math.log((c4[s[i:i+4]]+0.1)/(c3[s[i:i+3]]+0.1*V)) for i in range(len(s)-3))
res={'corpus_md5':md5,'corpus_chars':len(t),'german_function_word_share':round(frac,4)}
L='abcdefghijklmnopqrstuvwxyz'
full={ch:K.get(ch,ch) for ch in L}
for f in ('f102','f104','f204'):
    ct=' '+' '.join(re.sub('[^a-z]','',c.lower()) for _,_,c in words(B+'tx/%s.txt'%f))+' '
    true=lp(''.join(full.get(ch,ch) for ch in ct))
    res[f]={'chars':len(ct),'true_logp':round(true,2)}
    for seed in (20261112,7):
        rnd=random.Random(seed); ge=0; best=-1e18; tot=0.0
        for _ in range(5000):
            p=list(L); rnd.shuffle(p); m=dict(zip(L,p))
            sc=lp(''.join(m.get(ch,ch) for ch in ct)); ge+=sc>=true; best=max(best,sc); tot+=sc
        res[f]['seed_%d'%seed]={'n':5000,'at_or_above_true':ge,'best_shuffle':round(best,2),'mean_shuffle':round(tot/5000,2)}
json.dump(res,open(B+'dec/shuffle.json','w'),indent=1); print(json.dumps(res,indent=1))
