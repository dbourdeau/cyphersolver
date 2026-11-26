# 18th-c. Russian char n-gram model (pre-reform PSZ texts from ru.wikisource, 1700-1749 documents)
import re,html,glob,math,collections,pickle,os
W='/home/claude/keyless/ostermann1737/'
ALPHA='абвгдежзиклмнопрстуфхцчшщъыьѣюя'
TR=str.maketrans({'й':'и','і':'и','э':'е','ё':'е','ѳ':'ф','ѵ':'и','ї':'и'})
def norm(s):
    s=s.lower().translate(TR)
    return re.sub(r'\s+',' ',re.sub('[^'+ALPHA+']+',' ',s)).strip()
def corpus():
    out=[]
    for f in sorted(glob.glob(W+'lmsrc/html/*.html')):
        s=open(f,encoding='utf8').read()
        s=re.sub(r'<(script|style)[^>]*>.*?</\1>',' ',s,flags=re.S); s=re.sub(r'<[^>]+>',' ',s); s=re.sub(r'\s+',' ',html.unescape(s))
        i=s.find(' → ',s.find(' → ')+1) if s.count(' → ')>=2 else 0
        j=len(s)
        for m in ('См. также','Источник —','Примѣчанія','Примечания [ править'):
            k=s.find(m,i)
            if k>0: j=min(j,k)
        out.append(norm(s[i:j]))
    return out
class LM:
    def __init__(self,texts,order=5):
        self.n=order; self.c=[collections.Counter() for _ in range(order+1)]
        for t in texts:
            t=' '+t+' '
            for k in range(1,order+1):
                for i in range(len(t)-k+1): self.c[k][t[i:i+k]]+=1
        self.N=sum(self.c[1].values()); self.cache={}
    def lp(self,g):
        v=self.cache.get(g)
        if v is not None: return v
        k=len(g); pen=0.0; h=g
        while k>1:
            a=self.c[k].get(h,0)
            if a>0:
                v=math.log(a/self.c[k-1][h[:-1]])+pen; break
            h=h[1:]; k-=1; pen+=math.log(0.3)
        else:
            v=math.log((self.c[1].get(h,0)+0.5)/(self.N+16))+pen
        self.cache[g]=v; return v
    def score(self,text):
        t=' '+text+' '; n=self.n; s=0.0
        for i in range(1,len(t)):
            s+=self.lp(t[max(0,i-n+1):i+1])
        return s
def get(order=5):
    p=W+'lmsrc/rulm%d.pkl'%order
    if os.path.exists(p): return pickle.load(open(p,'rb'))
    m=LM(corpus(),order); m.cache={}; pickle.dump(m,open(p,'wb')); return m
if __name__=='__main__':
    c=corpus(); print(len(c),sum(map(len,c))); print(c[3][:400])
    m=LM(c,5); t='понеже хотя по генеральному регламенту и велѣно всѣ дѣла'
    print(m.score(t)/len(t)); import random
    l=list(t); random.shuffle(l); print(m.score(''.join(l))/len(t))
