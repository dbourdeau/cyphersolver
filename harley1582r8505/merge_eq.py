"""Merge (t-sign + dot-group) into the single sign eq = f, where the word model clearly prefers it.
The f.263v reading showed eq is one sign (a short vertical with a small dot cluster at its upper
right) that the first pass split into a t-sign plus a dot group. Every change is logged."""
import sys,os,json
os.environ.setdefault('LAM','1.0'); sys.path.insert(0,os.path.dirname(os.path.abspath(__file__))+'/..')
import word as W
key=json.load(open(sys.argv[1])); MARGIN=float(os.environ.get('MARGIN','8'))
DOTS=(':','.','..',':2',':3',':4','::')
TSIGN=('I','Eb','B','wf','i')
log=[]
for fn in sys.argv[2:]:
    out=[]
    for line in open(fn,encoding='utf-8',errors='replace').read().split('\n'):
        if line.startswith('#') or '|' not in line: out.append(line); continue
        p=[x.strip() for x in line.split('|')]
        if len(p)<3: out.append(line); continue
        for fi in range(2,len(p),2):
            toks=p[fi].split()
            changed=True
            while changed:
                changed=False
                idx=[i for i,t in enumerate(toks) if not t.startswith('#') and t not in ('/','-')]
                def dec(tk):
                    s=''
                    for i in [j for j,t in enumerate(tk) if not t.startswith('#') and t not in ('/','-')]:
                        t=tk[i].rstrip('?')
                        s += 'm' if t in DOTS else key.get(t,'?')
                    return s
                base=dec(toks); bs=W.seg_score(base)+W.CH.score(base)
                for a,b in zip(idx,idx[1:]):
                    ta,tb=toks[a].rstrip('?'),toks[b].rstrip('?')
                    if ta in TSIGN and tb in DOTS:
                        tk=[t for i,t in enumerate(toks) if i!=b]; tk[a]='eq'
                        s=dec(tk); v=W.seg_score(s)+W.CH.score(s)
                        if v>bs+MARGIN:
                            log.append(f'{fn} {p[0]}: {ta}+{tb} -> eq (+{v-bs:.1f})')
                            toks=tk; changed=True; break
            p[fi]=' '+' '.join(toks)+' '
        out.append('|'.join(p))
    open(fn.replace('.txt','_eq.txt'),'w',encoding='utf-8').write('\n'.join(out))
open('merges.txt','a',encoding='utf-8').write('\n'.join(log)+'\n')
print(len(log),'merges')
