import re,collections
def load(norm=True):
    toks=[];pos=[]
    for p in (1,2,3,4):
        for li,l in enumerate(open(f'D107_p{p}.txt')):
            if l.startswith('#'): continue
            for j,t in enumerate(l.split()):
                raw=t
                t=t.split('/')[0].replace("'","")
                toks.append(t); pos.append((p,li,j+1,raw))
    return toks,pos
