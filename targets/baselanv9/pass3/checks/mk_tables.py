"""Per-unit table for NOTES 'Pass 3' from the pass 3 files (own code, python3 -I). usage: mk_tables.py <basel_p2>"""
import sys,re
R=sys.argv[1].rstrip('/')+'/'
dec={};own={};jud={};ctl={}
for ln in open(R+'DECODE_P3.txt'):
    if '\t' in ln and not ln.startswith('#'): u,t=ln.rstrip('\n').split('\t'); dec[u]=t
for ln in open(R+'SCORE_P3.tsv'):
    p=ln.rstrip('\n').split('\t')
    if len(p)>=6 and p[1].isdigit(): own[p[0].replace('TOTAL ','')]=(int(p[1]),int(p[2]),int(p[3]))
sec=None
for ln in open(R+'JUDGE_P3_RESULT.md'):
    m=re.match(r'## (H1r|H4|S2)$',ln.strip())
    if m: sec=m.group(1)
    if ln.startswith('## Every word'): sec=None
    m=re.match(r'\| (L\d\d|S2-\d\d) \| (\d+) \| (\d+) \| (\d+) \| (\d+) \|',ln)
    if m and sec: jud[sec+' '+m.group(1)]=tuple(int(m.group(i)) for i in (2,3,4))
    m=re.match(r'central: S (\d+), E (\d+), N (\d+)',ln)
    if m and sec: jud[sec]=tuple(int(m.group(i)) for i in (1,2,3))
for ln in open(R+'CONTROL_P3.txt'):
    p=ln.rstrip('\n').split('\t')
    if len(p)==6: ctl.setdefault(p[1],[]).append((p[4].replace('z ',''),p[5].replace('shuffles>=real ','')))
def f(t): s,e,n=t; return '%d/%d/%d'%(s,e,n),'%d/%d = %.1f%%'%(s,s+e+n,100*s/(s+e+n))
o=['| unit | decode (no emendation) | judge S/E/N | judge S/(S+E+N) | solver\'s own S/E/N | solver\'s own share | controls, seeds 20261112 / 7 |','|---|---|---|---|---|---|---|']
for u in dec:
    sec,l=u.split(); j=f(jud[u]); w=f(own[u])
    c=ctl.get(l); cs='%s, %s (z %s / %s)'%(c[0][1],c[1][1],c[0][0],c[1][0]) if c else 'section only'
    under=' **under**' if 100*jud[u][0]/sum(jud[u])<65 else ''
    o.append('| %s | %s | %s | %s%s | %s | %s | %s |'%(u,dec[u],j[0],j[1],under,w[0],w[1],cs))
    last=[k for k in dec if k.startswith(sec+' ')][-1]
    if u==last:
        j=f(jud[sec]); w=f(own[sec]); c=ctl[sec]
        assert tuple(sum(jud[k][i] for k in dec if k.startswith(sec+' ')) for i in range(3))==jud[sec]
        assert tuple(sum(own[k][i] for k in dec if k.startswith(sec+' ')) for i in range(3))==own[sec]
        o.append('| **%s, all** | | **%s** | **%s** | %s | %s | %s, %s (z %s / %s) |'%(sec,j[0],j[1],w[0],w[1],c[0][1],c[1][1],c[0][0],c[1][0]))
print('\n'.join(o))
