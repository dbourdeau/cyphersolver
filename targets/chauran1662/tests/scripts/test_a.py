#!/usr/bin/env python3
"""Test A (see TEST_PLAN.md). One run."""
import sys, collections
sys.path.insert(0,'scripts')
from testlib import *
T,tier=load_table()
ITEMS=[('f264','t264/f264_pass1.txt',1),('f294','t294/f294_pass1.txt',0),('f187 opening','t187/f187_pass1.txt',1),('f243 opening','t243a/f243_p1-2_pass1.txt',0)]
def lines_for(path,off):
    out=[]
    for sec,recs in sections(path).items():
        gl=[gloss_clean('' if (r['gloss'] or '').startswith('(none') else r['gloss']) for r in recs]
        idx=[k for k,r in enumerate(recs) if r['groups']]
        for k in idx:
            j=k-off
            own=gl[j] if 0<=j<len(gl) else ''
            if len(own)<10: continue
            prev=gl[j-1][-15:] if j-1>=0 else ''
            nxt=gl[j+1][:15] if j+1<len(gl) else ''
            groups=[gid(g) for g in recs[k]['groups'] if not g['struck'] and g['num'] is not None]
            out.append((sec,recs[k]['line'],groups,prev+own+nxt))
    return out
def best_hits(groups,w,Tn):
    m=len(w); NEG=-1
    cur=[0]*(m+1)   # free start
    for g in groups:
        nxt=[NEG]*(m+1)
        v=Tn.get(g)
        # miss / unscored: cover 0..12 letters
        run=NEG
        # nxt[j]=max(cur[j-L]) for L in 0..12
        for j in range(m+1):
            b=NEG
            for L in range(0,13):
                if j-L<0: break
                if cur[j-L]>b: b=cur[j-L]
            nxt[j]=b
        if v:
            L=len(v)
            for j in range(0,m-L+1):
                if cur[j]>=0 and w[j:j+L]==v and cur[j]+1>nxt[j+L]: nxt[j+L]=cur[j]+1
        cur=nxt
    return max(cur)
def hits_by_group(groups,w,Tn):
    # traceback version to attribute hits to groups (for tier breakdown), real table only
    m=len(w); n=len(groups); NEG=-1
    best=[[NEG]*(m+1) for _ in range(n+1)]; bk=[[None]*(m+1) for _ in range(n+1)]
    best[0]=[0]*(m+1)
    for i,g in enumerate(groups,1):
        v=Tn.get(g)
        for j in range(m+1):
            for L in range(0,13):
                if j-L<0: break
                if best[i-1][j-L]>best[i][j]: best[i][j]=best[i-1][j-L]; bk[i][j]=(L,False)
        if v:
            L=len(v)
            for j in range(0,m-L+1):
                if best[i-1][j]>=0 and w[j:j+L]==v and best[i-1][j]+1>best[i][j+L]: best[i][j+L]=best[i-1][j]+1; bk[i][j+L]=(L,True)
    j=max(range(m+1),key=lambda x:best[n][x]); res=[]
    for i in range(n,0,-1):
        L,h=bk[i][j]; res.append(h); j-=L
    return res[::-1]
out=open('tests/test_a_result.txt','w')
def P(*a):
    s=' '.join(str(x) for x in a); print(s); out.write(s+'\n')
data={name:lines_for(path,off) for name,path,off in ITEMS}
def run(Tb):
    Tn={g:norm(v) for g,v in Tb.items()}
    res={}
    for name,L in data.items():
        cov=tot=h=0
        for sec,ln,groups,w in L:
            tot+=len(groups); cov+=sum(1 for g in groups if g in Tn); h+=best_hits(groups,w,Tn)
        res[name]=(tot,cov,h)
    return res
real=run(T)
P('Test A, table_v1 sha256',SHA)
allt=allc=allh=0
for name,(tot,cov,h) in real.items():
    P('%-14s glossed lines %3d  groups %4d  in table %4d (coverage %.1f%%)  hits %4d  hit rate %.1f%%'%(name,len(data[name]),tot,cov,100*cov/tot,h,100*h/cov))
    allt+=tot;allc+=cov;allh+=h
P('%-14s groups %4d  in table %4d (coverage %.1f%%)  hits %4d  hit rate %.1f%%'%('OVERALL',allt,allc,100*allc/allt,allh,100*allh/allc))
# tier breakdown
Tn={g:norm(v) for g,v in T.items()}
tb=collections.Counter(); th=collections.Counter(); misses=collections.Counter()
for name,L in data.items():
    for sec,ln,groups,w in L:
        hb=hits_by_group(groups,w,Tn)
        for g,hh in zip(groups,hb):
            if g in Tn:
                tb[tier[g]]+=1; th[tier[g]]+=hh
                if not hh: misses[g]+=1
for t in ('firm','mixed','single'): P('tier %-6s scored %4d hits %4d (%.1f%%)'%(t,tb[t],th[t],100*th[t]/max(1,tb[t])))
P('most-missed groups:',', '.join('%s=%s×%d'%(g,T[g],c) for g,c in misses.most_common(25)))
sh=[]
per={n:[] for n in data}
for seed in range(1,201):
    r=run(shuffled(T,seed)); c=sum(v[1] for v in r.values()); h=sum(v[2] for v in r.values()); sh.append(h/c)
    for n,(tot,cov,hh) in r.items(): per[n].append(hh/cov)
P('200 shuffled tables: overall hit rate mean %.1f%%, max %.1f%%'%(100*sum(sh)/len(sh),100*max(sh)))
for n in data: P('  %-14s shuffled mean %.1f%% max %.1f%%'%(n,100*sum(per[n])/200,100*max(per[n])))
ov=allh/allc
ok=ov>=0.70 and ov>max(sh) and real['f264'][2]/real['f264'][1]>=0.60 and real['f294'][2]/real['f294'][1]>=0.60
P('PASS MARK (overall >=70%% and above shuffled max; f264 and f294 each >=60%%): %s'%('PASS' if ok else 'MISS'))
