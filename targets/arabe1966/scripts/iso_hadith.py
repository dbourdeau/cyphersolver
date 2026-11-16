import re,sys,json,glob,collections
def norm(w):
    w=re.sub('[ً-ْـٰ]','',w)
    for a,b in (('أ','ا'),('إ','ا'),('آ','ا'),('ٱ','ا'),('ى','ي'),('ة','ه'),('ؤ','و'),('ئ','ي'),('ء','')): w=w.replace(a,b)
    return w
parts=[]
for f in glob.glob('../dl/h/*.json'):
    d=json.load(open(f,encoding='utf8'))
    for h in d['hadiths']: parts.append(h.get('arabic','') or '')
txt=norm(' '.join(parts)); txt=re.sub('[^ابجدهوزحطيكلمنسعفصقرشتثخذضظغ ]',' ',txt); txt=re.sub(' +',' ',txt)
letters=txt.replace(' ','');pos=[i for i,c in enumerate(txt) if c!=' ']
print(len(letters))
def pat(t):
    d={};return tuple(d.setdefault(c,len(d)) for c in t)
toks={'17':"4 2 9 12 4 8 15 12 9 8 12 7 12 9 8 5 17".split(),'16':"7 15 8 9 21 7 21 8 9 21 5 18 4 21 9 24".split(),'23':list("71589217218921518421924")}
for name,t in toks.items():
  for d,tt in (('fwd',t),('rev',t[::-1])):
    for n in (len(tt),len(tt)-2,len(tt)-4):
      for off in range(len(tt)-n+1):
        sub=tt[off:off+n];p=pat(sub)
        # index by hashing windows
        seen=collections.Counter()
        for i in range(len(letters)-n):
            w=letters[i:i+n]
            if w[0]==w[1]: continue
            if pat(w)==p: seen[txt[pos[i]:pos[i+n-1]+1]]+=1
        print(name,d,n,off,sum(seen.values()),seen.most_common(4))
