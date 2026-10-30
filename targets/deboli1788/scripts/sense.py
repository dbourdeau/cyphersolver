"""Share of cipher groups read as sense on a pair with a known clear text (see NOTES.md). usage: sense.py KEY cipher clear [n_controls]"""
import sys,random,re
from learn import groups,align,norm,lev,val
def ok(t,v,s):
    if t=='P': return True
    if t!='K': return False
    if '|' in v: return any(ok(t,x,s) for x in v.split('|'))
    if v==s: return True
    if v and s and (v.startswith(s) or s.startswith(v)) and abs(len(v)-len(s))<=2: return True
    if len(v)>=4 and lev(v,s)<=1: return True
    return False
def rate(gs,C):
    res=align(gs,C); n=sum(1 for g,_,_ in res if not g.startswith('='))
    return sum(ok(t,v,s) for g,(t,v),s in res if not g.startswith('='))/n, res
if __name__=='__main__':
    gs=groups(sys.argv[2]); C=norm(''.join(l for l in open(sys.argv[3],encoding='utf-8') if not l.startswith('#')))
    r,res=rate(gs,C); print(f'read as sense: {r:.3f} ({len(gs)} groups)')
    if len(sys.argv)>4:
        random.seed(7); T=[]
        for i in range(int(sys.argv[4])):
            g=gs[:]; random.shuffle(g); T.append(rate(g,C)[0])
        T.sort(); print(f'controls ({len(T)}) : max {T[-1]:.3f} p50 {T[len(T)//2]:.3f}')
    bad=[(g,v,s) for g,(t,v),s in res if not ok(t,v,s)]
    print('unread:',' '.join(f'{g}:{v}->{s}' for g,v,s in bad))
