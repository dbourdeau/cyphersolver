"""Rule #728 count: segment decoded target lines into words (group-level DP over a lexicon);
a word is SURE iff all its groups are S-status codes with an agreed/arbiter-sure transcription and the
decoded string equals a lexicon word exactly. Everything else = holes. Non-lexicon stretches: one hole-word
per started 5 letters (at least one per stretch)."""
import sys,json,re
sys.path.insert(0,sys.argv[1]); from vlib import *
D=sys.argv[2]
K={};ST={}
for l in open(D+"/key/KEY-K2-frozen.tsv").read().split('\n')[1:]:
    if not l: continue
    c,v,n,a,cu,st=l.split('\t'); K[c]='' if v=='-' else v; ST[c]=st
lex=set()
for ln in open(f"{T}/gloss_careful.txt"):
    if re.match(r'L\d+ G:',ln): lex|=set(nz(w) for w in re.split(r"[\s'’,;.]+",ln.split(':',1)[1]) if nz(w))
for f in ['passA_targets.txt']:
    for ln in open(f"{T}/{f}"):
        for m in re.findall(r'«([^»]*)»',ln)+([ln.split(':',1)[1]] if ' T:' in ln else []):
            lex|=set(nz(w) for w in re.split(r"[\s'’,;.()]+",m) if nz(w))
lex|=set(nz(w) for w in open(sys.argv[4]).read().split())
lex.discard('')
TWO={'le','la','de','du','et','en','au','un','ce','il','ne','se','sa','me','ma','on','ou','si','y','a','nu','ie','lu','eu','ni','qu'}
lex={w for w in lex if len(w)>2 or w in TWO}
lex-={'qu','nu','lu','ni'}
M=json.load(open(f"{T}/merged_cipher.json"))
res={}
detail=[]
for name,pages in [('T1','0060S,0061L,0061R,0062L'),('T2','0092S,0093L,0093R,0094L,0094R,0095L,0095R,0096L')]:
    sure=0;holes=0;groups=0
    for pg in pages.split(','):
        lines={}
        for (l,t,s) in M[pg]: lines.setdefault(l,[]).append((t,s))
        A=parse(f"{T}/passA_targets.txt")[pg]
        gut={no for no,k,p in A if k=='C' and '[G]' in p}
        for l in sorted(lines):
            g=lines[l]; groups+=len(g)
            vals=[];ok=[]
            for t,s in g:
                c=cc(t); v=K.get(c)
                vals.append(nz(v) if v is not None else None)
                ok.append(v is not None and ST.get(c)=='S' and s in('agree','arb-sure'))
            n=len(g); INF=10**9
            # dp[i] = (holes, -sure) best; words: j..i groups
            best=[(INF,0,None)]*(n+1); best[0]=(0,0,None)
            for i in range(1,n+1):
                for j in range(max(0,i-8),i):
                    if best[j][0]>=INF: continue
                    seg=vals[j:i]
                    if None not in seg and ''.join(seg) in lex and ''.join(seg):
                        s_ok=all(ok[j:i]); h=0 if s_ok else 1; sc=(best[j][0]+h,best[j][1]-(1 if s_ok else 0),(j,'w' if s_ok else 'p'))
                    else:
                        L=sum(len(x) if x else 3 for x in seg)
                        h=max(1,-(-L//5)); sc=(best[j][0]+h,best[j][1],(j,'x'))
                    if (sc[0],sc[1])<(best[i][0],best[i][1]) : best[i]=sc
            i=n; segs=[]
            while i>0:
                j,kind=best[i][2]; segs.append((j,i,kind)); i=j
            segs.reverse()
            words=[]
            for j,i,kind in segs:
                txt=''.join(x if x is not None else '*' for x in vals[j:i])
                if kind=='w': sure+=1; words.append(txt)
                elif kind=='p': holes+=1; words.append('{'+txt+'}')
                else:
                    L=sum(len(x) if x else 3 for x in vals[j:i]); h=max(1,-(-L//5)); holes+=h; words.append('‹'+txt+'›')
            if l in gut: holes+=1; words.append('‹[G]›')
            detail.append(f"{name} {pg} L{l:02d}: "+' '.join(words))
    res[name]=dict(cipher_groups=groups,sure_words=sure,hole_words=holes,cipher_words=sure+holes,read_fraction=round(sure/(sure+holes),3))
print(json.dumps(res,indent=1))
open(sys.argv[3],'w').write('\n'.join(detail)+'\n')
