import sys,itertools
V='''sale sal armoniaco armoniacho ammoniaco argento vivo solfere solfore solfo zolfo arsenico arsenicho orpimento oropimento salnitro nitro gemma commune comune alkali alcali alume allume rocha roccha zucharino scagliola piuma vetriolo vitriolo romano borace borax tutia tuzia marchasita marcasita magnesia antimonio verderame verde rame cinabrio cinabro litargirio calcina viva tartaro gripola gomma dragante minio biacca cerusa piombo stagno ferro oro argento acqua aqua forte vita aceto urina orina sangue tincar tinchar atincar cristallo calamina squama croco feccia vino sublimato solimato realgar risigallo bianco citrino cipro oglio olio mele miele cera sapone calce vetro fiel lume ovo ovi chiara rosso bianco negro giallo verde
una uno doi due tre quatro quattro cinque sei sette otto nove diece meza mezo onza onze oncia once dramma drama dramme drame libra libre lira scropolo scropoli carati parte parti
et e de del di a al in con cioe poi ana tanto quanto ogni per sopra
sol sole luna saturno giove iove marte venere mercurio
ariete tauro gemini cancer leo leone virgo libra scorpio sagitario capricorno aquario pisce pissis'''.split()
V=sorted(set(V))
def pat(s):
    d={};return tuple(d.setdefault(c,len(d)) for c in s)
def ok(m,inv,c,p):
    m=dict(m);inv=dict(inv)
    for a,b in zip(c,p):
        if m.get(a,b)!=b or inv.get(b,a)!=a: return None
        m[a]=b;inv[b]=a
    return m,inv
toks=sys.argv[1].split()
# candidates per token: single word or two-word split
cand={}
for t in set(toks):
    cs=[(w,) for w in V if len(w)==len(t) and pat(w)==pat(t)]
    for i in range(2,len(t)-1):
        a,b=t[:i],t[i:]
        for w1 in V:
            if len(w1)==i:
                for w2 in V:
                    if len(w2)==len(b) and pat(w1+w2)==pat(t): cs.append((w1,w2))
    cand[t]=cs
order=sorted(set(toks),key=lambda t:len(cand[t]))
best=[0,None]
def rec(i,m,inv,sol,cov):
    if cov+sum(len(t) for t in order[i:])<=best[0]: return
    if i==len(order):
        best[0]=cov;best[1]=dict(sol);return
    t=order[i]
    for c in cand[t]:
        r=ok(m,inv,t,''.join(c))
        if r: sol[t]=c; rec(i+1,r[0],r[1],sol,cov+len(t)); del sol[t]
    rec(i+1,m,inv,sol,cov)
rec(0,{},{},{},0)
print('covered',best[0],'of',sum(len(t) for t in set(toks)))
for t in toks: print(t,best[1].get(t) if best[1] else None)
