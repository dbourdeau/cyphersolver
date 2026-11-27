# Decode the 1643 letter with KEY_v2 once; DP word segmentation per METHOD_1643.md; key-shuffle and ciphertext-shuffle controls.
# Usage: python3 -I run_1643.py <transcription> <outprefix>
import sys, random, re
sys.path.insert(0,'/home/claude/hunts40/G3/M4/trackB/scripts')
import score as S
T=sys.argv[1]; OUT=sys.argv[2]
W,C=S.wordlist(); key=S.load_key('/home/claude/hunts40/G3/M4/trackB/keyv2/KEY_v2.tsv')
S2={'en','de','te','in','op','is','al','of','na','om','ia','er','so','ie','uu','nu'}  # norm('uw')='uu'
def parse(path):
    runs=[]; cur=[]; page=None
    for l in open(path,encoding='utf-8'):
        if l.startswith('#') or '|' not in l: continue
        lab,c=[x.strip() for x in l.split('|',1)]
        pg=lab.split('.')[0]
        c=re.sub(r'\[[^\]]*\]',' , ',c); c=re.sub(r'<[^>]*>',' , ',c)
        for t in c.replace(',',' , ').split():
            if t==',':
                if cur: runs.append((page,cur)); cur=[]
            else:
                if not cur: page=pg
                cur.append(int(t))
    if cur: runs.append((page,cur))
    return runs
def seg(s):
    n=len(s); best=[(0,0,None)]*(n+1)  # (covered, -pieces, back)
    best=[None]*(n+1); best[0]=(0,0,-1,False)
    for i in range(1,n+1):
        cand=[]
        p=best[i-1]; cand.append((p[0],p[1]-1,i-1,False))
        for j in range(max(0,i-20),i-1):
            pc=s[j:i]; L=i-j
            if '?' in pc: continue
            nm=S.norm(pc)
            ok=(L>=3 and nm in W) or (L==2 and nm in S2)
            if ok:
                q=best[j]; cand.append((q[0]+L,q[1]-1,j,True))
        best[i]=max(cand,key=lambda x:(x[0],x[1],-x[2]))
    out=[]; i=n
    while i>0:
        c,_,j,w=best[i]; out.append((s[j:i],w)); i=j
    return best[n][0], out[::-1]
def total(runs,k):
    return sum(seg(''.join(k.get(x,'?') for x in g))[0] for _,g in runs)
runs=parse(T); groups=[x for _,g in runs for x in g]; N=len(groups)
lines=[]; P=lambda *a: lines.append(' '.join(str(x) for x in a))
cov=sum(1 for x in groups if x in key)
P(f'runs {len(runs)}; groups {N}; keyed {cov}; coverage {cov}/{N} = {100*cov/N:.2f}%')
unk=sorted({x for x in groups if x not in key}); P('numbers not in KEY_v2:',unk,'occurrences',N-cov)
real=0; full=0; perpage={}
rows=[]
for pg,g in runs:
    d=''.join(key.get(x,'?') for x in g); c,sg=seg(d); real+=c; full+=(c==len(g))
    a=perpage.setdefault(pg,[0,0]); a[0]+=c; a[1]+=len(g)
    shown=' '.join(p.upper() if w else p for p,w in sg)
    rows.append((pg,' '.join(map(str,g)),d,shown,c,len(g)))
    P(f'{pg} | {" ".join(map(str,g))} | {d} | {shown} | {c}/{len(g)}')
for pg,(a,b) in sorted(perpage.items()): P(f'page {pg}: covered {a}/{b} = {100*a/b:.2f}%')
P(f'FIGURE OF RECORD: covered {real}/{N} = {100*real/N:.2f}%; runs fully covered {full}/{len(runs)}')
open(OUT+'_firstpass.tsv','w').write('page\tgroups\tdecode\tsegmentation(WORDS upper)\tcovered\tlen\n'+''.join('\t'.join(map(str,r))+'\n' for r in rows))
nums=sorted(key); vals=[key[n] for n in nums]
for seed in (20261112,7):
    rng=random.Random(seed); ge=0; mx=0; tot=0
    for _ in range(5000):
        v=vals[:]; rng.shuffle(v); s=total(runs,dict(zip(nums,v))); tot+=s; mx=max(mx,s); ge+=(s>=real)
    P(f'key shuffle seed {seed}: >= real {ge}/5000; max {mx} ({100*mx/N:.2f}%); mean {tot/5000:.2f} ({100*tot/5000/N:.2f}%)')
lens=[len(g) for _,g in runs]
for seed in (20261112,7):
    rng=random.Random(seed); ge=0; mx=0; tot=0
    for _ in range(5000):
        gg=groups[:]; rng.shuffle(gg); rr=[]; i=0
        for L in lens: rr.append((None,gg[i:i+L])); i+=L
        s=total(rr,key); tot+=s; mx=max(mx,s); ge+=(s>=real)
    P(f'matched control (ciphertext shuffle) seed {seed}: >= real {ge}/5000 (rank of real: {ge+1} of 5001); max {mx} ({100*mx/N:.2f}%); mean {tot/5000:.2f} ({100*tot/5000/N:.2f}%)')
open(OUT+'_output.txt','w').write('\n'.join(lines)+'\n'); print('\n'.join(lines))
