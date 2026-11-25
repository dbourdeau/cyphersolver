"""Score the C4/C5 variants. Unchanged words keep the separate judge's central call (parsed from JUDGE_P3_RESULT.md);
changed words take the calls in CHANGED (this session's, by judge/BRIEF.txt), or N under 'strict'. Own code, python3 -I.
usage: score_variant.py <basel_p2 folder> <variant folder>"""
import sys,re
R,V=sys.argv[1].rstrip('/')+'/',sys.argv[2].rstrip('/')+'/'
J={}
for ln in open(R+'JUDGE_P3_RESULT.md',encoding='utf-8'):
    m=re.match(r'\| ((?:H1r|H4|S2) \S+) \| (\S+) \| (\d+) \| ([SEN]) \| ([SEN]) \| ([SEN]) \|',ln)
    if m: J[(m.group(1),m.group(2))]=(m.group(4),int(m.group(3)))
assert len(J)==34,len(J)
CHANGED={'iristiana':('N','christiana: ch written i = one wrong letter and one missing, two slips'),
         'pa[?]te':('S','parte with [?] for r: recognisable with no further slip (BRIEF rule for [?])'),
         'i~ri':('E','chri~ with i for ch: the bar marks an abbreviation, one slip')}
def L(w): return len(re.sub('[^a-z]','',w.replace('[?]','')))
def rows(path):
    r=[]
    for ln in open(path,encoding='utf-8'):
        if ln.startswith('#') or '\t' not in ln: continue
        u,t=ln.rstrip('\n').split('\t'); r.append((u,t.split()))
    return r
def score(path,strict,basewords):
    tot={}; line={}; used=set(); notes=[]
    for (u,ws),(u0,ws0) in zip(rows(path),basewords):
        assert u==u0 and len(ws)==len(ws0),u
        sec=u.split()[0]
        for w,w0 in zip(ws,ws0):
            n=L(w)
            if w!=w0:
                tag=('N' if strict else CHANGED[w][0]); notes.append((u,w0,w,n,tag))
            elif (u,w) in J:
                tag,jl=J[(u,w)]; used.add((u,w))
                if w=='t[?]=': n=jl
                assert jl==n,(u,w,jl,n)
            else: tag='S'
            if n==0: continue
            s,e,x=(n,0,0) if tag=='S' else ((n-1,1,0) if tag=='E' else (0,0,n))
            for k in (sec,u):
                a=tot.setdefault(k,[0,0,0]); a[0]+=s;a[1]+=e;a[2]+=x
    assert used==set(J),set(J)-used
    return tot,notes
base=rows(R+'DECODE_P3.txt'); out=[]
t0,_=score(R+'DECODE_P3.txt',False,base)
out.append('# check: the judged pass 3 decode re-added from the judge\'s word table')
for k in ('H1r','H4','S2'):
    s,e,n=t0[k]; out.append('judged, C4+C5 on\t%s\tS %d E %d N %d\t%d/(%d+%d+%d) = %d/%d = %.1f%%'%(k,s,e,n,s,s,e,n,s,s+e+n,100*s/(s+e+n)))
assert (t0['H1r'],t0['H4'],t0['S2'])==([399,6,0],[389,9,17],[486,10,25])
for mode in ('noC4','noC5','noC4C5'):
    for strict in (False,True):
        t,notes=score(V+'DECODE_P3_%s.txt'%mode,strict,base)
        lab='%s, %s'%(mode,'strict (every changed word N)' if strict else 'as called')
        for k in ('H1r','H4','S2'):
            s,e,n=t[k]; out.append('%s\t%s\tS %d E %d N %d\t%d/(%d+%d+%d) = %d/%d = %.1f%%'%(lab,k,s,e,n,s,s,e,n,s,s+e+n,100*s/(s+e+n)))
        if mode=='noC4C5':
            for k in sorted(t):
                if ' ' in k and t[k]!=t0[k]:
                    s,e,n=t[k]; s0,e0,n0=t0[k]; out.append('%s\t%s\tS %d E %d N %d\t%d/%d = %.1f%% (judged %d/%d = %.1f%%)'%(lab,k,s,e,n,s,s+e+n,100*s/(s+e+n),s0,s0+e0+n0,100*s0/(s0+e0+n0)))
    out.append('# %s changed words: '%mode+'; '.join('%s %s -> %s (%d letters)'%(u,a,b,n) for u,a,b,n,_ in notes))
out.append('# calls on changed words (this session, NOT the separate judge): '+'; '.join('%s = %s, %s'%(k,v[0],v[1]) for k,v in CHANGED.items()))
out.append('# H4: no word of H4 uses C4 or C5; the variant decode of H4 is letter for letter the judged decode.')
open(V+'SCORE_VARIANT.tsv','w').write('\n'.join(out)+'\n'); print('\n'.join(out))
