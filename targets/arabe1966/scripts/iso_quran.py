import re,sys
raw=open(sys.argv[1],encoding='utf8').read()
lines=[l.split('|',2)[2] for l in raw.splitlines() if l.count('|')>=2]
def norm(w):
    w=re.sub('[ً-ْـٰ]','',w)
    for a,b in (('أ','ا'),('إ','ا'),('آ','ا'),('ٱ','ا'),('ى','ي'),('ة','ه'),('ؤ','و'),('ئ','ي'),('ء','')): w=w.replace(a,b)
    return w
txt=norm(' '.join(lines)); txt=re.sub('[^ابجدهوزحطيكلمنسعفصقرشتثخذضظغ ]','',txt)
letters=txt.replace(' ','')
# map letter index->position in spaced text
pos=[i for i,c in enumerate(txt) if c!=' ']
def pat(t):
    d={};return tuple(d.setdefault(c,len(d)) for c in t)
toks={'17rtl':"4 2 9 12 4 8 15 12 9 8 12 7 12 9 8 5 17".split(),'16ltr':"7 15 8 9 21 7 21 8 9 21 5 18 4 21 9 24".split(),'23':list("71589217218921518421924")}
for name,t in toks.items():
  for d,tt in (('fwd',t),('rev',t[::-1])):
    p=pat(tt);n=len(tt);hits=0
    for i in range(len(letters)-n):
        if pat(letters[i:i+n])==p:
            hits+=1
            if hits<=15: print(name,d,txt[pos[i]:pos[i+n-1]+1])
    print(name,d,'hits',hits)
