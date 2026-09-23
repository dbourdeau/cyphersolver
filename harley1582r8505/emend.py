"""Conservative emendation of the two pages not re-read from the images.

Only swaps a token between members of a shape-pair that the second reading of ff.263v/264v
showed to be confusable (documented in signs.md), and only when the word-model score improves
by a clear margin. Every change is logged to emendations.txt for audit.
"""
import sys,os,json,glob,collections
os.environ.setdefault('LAM','1.0'); sys.path.insert(0,os.path.dirname(os.path.abspath(__file__))+'/..')
import word as W
PAIRS={'DOT':['eq'],':':['eq'],'..':['eq'],':2':['eq'],'.2':['eq'],':3':['eq'],':4':['eq'],'.':['eq'],'...':['eq'],
       'eq':['I'],'E':['E3'],'E3':['E'],'X':['hg'],'Xo':['hg'],'hg':['X','Xo'],'b':['T'],'T':['b'],
       'phi':['f'],'f':['phi'],'I':['eq'],'H':['#','ne'],'#':['H','ne'],'ne':['H','#'],
       'Pi':['Br','Usq'],'PiG':['Br','Usq'],'sh':['Br','Usq'],'Br':['Pi','sh'],'Usq':['Pi','sh'],
       'b':['o','T'],'o':['b','T'],'T':['b','o','f'],'q':['f','T'],'f':['q','T','phi']}
key=json.load(open(sys.argv[1])); MARGIN=float(os.environ.get('MARGIN','8'))
log=[]
for fn in sys.argv[2:]:
    lines=open(fn,encoding='utf-8',errors='replace').read().split('\n')
    out=[]
    for ln,line in enumerate(lines):
        if line.startswith('#') or '|' not in line:
            out.append(line); continue
        p=[x.strip() for x in line.split('|')]
        if len(p)<3: out.append(line); continue
        for fi in range(2,len(p),2):
            toks=p[fi].split()
            # build the decode of this field as a flat list with token indices
            idx=[i for i,t in enumerate(toks) if t.rstrip('?') not in ('/','-') and not t.startswith('#')]
            def dec(tk):
                s=''
                for i in idx:
                    t=tk[i].rstrip('?')
                    s+= 'm' if t in (':','.','..',':2',':3',':4') else key.get(t,'?')
                return s
            base=dec(toks); bs=W.seg_score(base)+W.CH.score(base)
            for i in idx:
                t=toks[i].rstrip('?')
                if t not in PAIRS: continue
                for alt in PAIRS[t]:
                    tk=list(toks); tk[i]=alt
                    s=dec(tk); v=W.seg_score(s)+W.CH.score(s)
                    if v>bs+MARGIN:
                        log.append(f'{fn} {p[0]} pos{i}: {t} -> {alt}  (+{v-bs:.1f})')
                        toks[i]=alt; base=s; bs=v; break
            p[fi]=' '+' '.join(toks)+' '
        out.append('|'.join(p))
    open(fn.replace('.txt','_em.txt'),'w',encoding='utf-8').write('\n'.join(out))
open('emendations.txt','w',encoding='utf-8').write('\n'.join(log)+'\n')
print(len(log),'emendations')
