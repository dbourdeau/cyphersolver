import re,sys,math,collections
sys.path.insert(0,'.')
import ws
raw=open('../dl/q_2.dat',encoding='utf8').read()
def norm(w):
    w=re.sub('[ً-ْـٰ]','',w)
    for a,b in (('أ','ا'),('إ','ا'),('آ','ا'),('ٱ','ا'),('ى','ي'),('ة','ه'),('ؤ','و'),('ئ','ي'),('ء','')): w=w.replace(a,b)
    return w
AR="ابجدهوزحطيكلمنسعفصقرشتثخذضظغ"
cnt=collections.Counter(w for w in norm(raw).split() if w and not set(w)-set(AR))
for ws_ in ws.lex.values():
    for w in ws_: cnt[norm(w)]+=30
tot=sum(cnt.values())
ORD={'abjad':AR,'hija':"ابتثجحخدذرزسشصضطظعغفقكلمنهوي"}
S="71589217218921518421924"
res=[]
for on,o in ORD.items():
  for k in range(28):
    for mode in ('red','root'):
      # letter at index i (0-based) after shift k -> value index j=(i+k)%28 ; red: digit=(j%9)+1 ; same thing for abjad; root for hija = digital root of (j+1)
      code={c:str(((i+k)%28)%9+1) for i,c in enumerate(o)}
      if mode=='root':
          if k%9==0 and k: pass
          code={c:str((((i+k)%28+1)-1)%9+1) for i,c in enumerate(o)}
          if on=='abjad': continue
      bycode=collections.defaultdict(list)
      for w,c in cnt.items():
          if len(w)>=2 or w=='و': bycode[''.join(code[x] for x in w)].append((c,w))
      for d,s in (('ltr',S),('rtl',S[::-1])):
          n=len(s);best=[(-1e9,[])]*(n+1);best[0]=(0,[])
          for i in range(n):
              if best[i][0]<-1e8: continue
              for L in range(1,9):
                  if i+L>n: break
                  cands=bycode.get(s[i:i+L])
                  if cands:
                      c,w=max(cands)
                      sc=best[i][0]+math.log10(c/tot)-1.5+0.9*L
                      if sc>best[i+L][0]: best[i+L]=(sc,best[i][1]+[w])
          res.append((best[n][0],on,k,mode,d,' '.join(best[n][1])))
res.sort(reverse=True)
for r in res[:40]: print(r)
