import re,sys,math,collections,json,glob
sys.path.insert(0,'.')
import ws
def norm(w):
    w=re.sub('[ً-ْـٰ]','',w)
    for a,b in (('أ','ا'),('إ','ا'),('آ','ا'),('ٱ','ا'),('ى','ي'),('ة','ه'),('ؤ','و'),('ئ','ي'),('ء','')): w=w.replace(a,b)
    return w
AR="ابجدهوزحطيكلمنسعفصقرشتثخذضظغ"
cnt=collections.Counter(w for w in norm(open('../dl/q_2.dat',encoding='utf8').read()).split() if w and not set(w)-set(AR))
d=json.load(open('../dl/h/bukhari.json',encoding='utf8'))
for h in d['hadiths']:
    for w in norm(h.get('arabic','') or '').split():
        w=re.sub('[^'+AR+']','',w)
        if w: cnt[w]+=1
for l in ws.lex.values():
    for w in l: cnt[norm(w)]+=50
tot=sum(cnt.values())
W={w:math.log10(c/tot) for w,c in cnt.items() if c>=2 and (len(w)>1 or w=='و')}
def seg(t):
    n=len(t);best=[-1e9]*(n+1);bk=[None]*(n+1);best[0]=0
    for i in range(n):
        if best[i]<-1e8: continue
        for L in range(1,9):
            w=t[i:i+L]
            if len(w)<L: break
            sc=best[i]+(W[w]-1.0 if w in W else -6.0*L-1)
            if sc>best[i+L]: best[i+L]=sc;bk[i+L]=i
    out=[];i=n
    while i>0: out.append(t[bk[i]:i]);i=bk[i]
    return best[n],' '.join(out[::-1])
S="71589217218921518421924"
val={v:c for c,v in zip(AR,[1,2,3,4,5,6,7,8,9,10,20,30,40,50,60,70,80,90,100,200,300,400,500,600,700,800,900,1000])}
res=[]
for dname,s in (('ltr',S),('rtl',S[::-1])):
  for conv in ('dm','md'):
    for base in (0,1):  # marker m means 10^(m-base) : base0: m=1 tens,2 hundreds,3 thousands ; base1: m=2 tens,3 hundreds,4 thousands
      outs=set()
      def rec(i,acc):
        if i==len(s): outs.add(''.join(acc));return
        dgt=int(s[i]); 
        if dgt in val: rec(i+1,acc+[val[dgt]])
        if i+1<len(s):
            a,b=int(s[i]),int(s[i+1])
            dg,m=(a,b) if conv=='dm' else (b,a)
            e=m-base
            if 1<=e<=3:
                v=dg*10**e
                if v in val: rec(i+2,acc+[val[v]])
      rec(0,[])
      for t in outs:
          for tt,o in ((t,'f'),(t[::-1],'r')):
              sc,sg=seg(tt); res.append((sc/len(tt),dname,conv,base,o,sg))
res.sort(reverse=True)
print(len(res))
for r in res[:25]: print(r)
