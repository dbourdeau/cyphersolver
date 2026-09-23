"""Keep only lines whose signs field is really signs; strip unknown tokens."""
import sys,re
KNOWN=set('Gm L 7 X Xo psi w wT w0 wf f G n U Usq o u B b dd d Oi phi q E E3 Eb # H ne F T Pi PiG sh hg cy y c I II III J Br + Tn Om tr ti tl V v bx eq R , Tu rho'.split())
DOTS={':','.','..',':2',':3',':4','::','.:.',':.'}
out=[]
for fn in sys.argv[1:]:
    for line in open(fn,encoding='utf-8',errors='replace'):
        if line.startswith('#') or '|' not in line:
            continue
        p=[x.strip() for x in line.rstrip('\n').split('|')]
        if len(p)<3: continue
        newfields=list(p)
        ok=tot=0
        for i in range(2,len(p),2):
            toks=[]
            for t in p[i].replace('/',' ').split():
                b=t.rstrip('?')
                tot+=1
                if b in KNOWN or b in DOTS or b.startswith('#') and b[1:].isdigit():
                    toks.append(t); ok+=1
            newfields[i]=' '+' '.join(toks)+' '
        if tot and ok/tot>=0.75 and ok>=3:
            out.append('|'.join(newfields))
print('\n'.join(out))
