import sys
runs=[]
for l in open(sys.argv[1]):
    if l.startswith('#'): continue
    s,p,n=l.rstrip('\n').split('\t')
    if p!='T': continue
    runs.append((s,n.replace('58|5.8','58').replace('5|4','5').replace('18|13','18').split('.')))
words=sys.argv[2].split(',')
strict = len(sys.argv)>3  # injective too
for w in words:
    for s,r in runs:
        for i in range(len(r)-len(w)+1):
            seg=r[i:i+len(w)]
            if '70' in seg: continue
            m={};ok=True;inv={}
            for c,x in zip(w,seg):
                if m.setdefault(x,c)!=c: ok=False;break
                if strict and inv.setdefault(c,x)!=x: ok=False;break
            if ok and len(set(w))<len(w): print(w,s,i,' '.join(seg))
