import sys,re,itertools
key={};cnt={}
for l in open(sys.argv[1],encoding='utf-8'):
    if l.startswith('#'):continue
    p=l.rstrip('\n').split('\t')
    if len(p)>=2 and p[1] not in ('','?'):
        key[p[0]]=p[1]
        try: cnt[p[0]]=int(p[2].split('/')[0])
        except: cnt[p[0]]=0
def look(g):
    g=g.rstrip('?')
    base=re.sub('[abc]$','',g)
    cands=[]
    for form in (g,base):
        n=form.count('X')
        for combo in itertools.product('08',repeat=n):
            f=form
            for c in combo: f=f.replace('X',c,1)
            if f in key: cands.append((cnt.get(f,0),f))
        if cands: break
    if not cands: return None,None
    c=max(cands); return c[1],key[c[1]]
def run(fn,show=True):
    n=k=0; rows=[]
    for line in open(fn,encoding='utf-8'):
        if line.startswith('#') or not line.strip(): continue
        loc,*gs=line.split(); out=[]
        for g in gs:
            n+=1
            gg=re.sub('[abc?]$','',g.rstrip('?'))
            f,v=look(g)
            vars_=[gg.replace('X','0'),gg.replace('X','8')] if 'X' in gg else [gg]
            if v is None and any(x.isdigit() and 1775<=int(x)<=1788 for x in vars_):
                k+=1; out.append('·'); continue
            if v is not None: k+=1; out.append(v)
            else: out.append('‹'+g+'›')
        rows.append((loc,out))
        if show: print(loc,' '.join(out))
    if show: print(f'# groups {n}, with a key value {k} ({k/n:.1%})')
    return rows
if __name__=='__main__': run(sys.argv[2])
