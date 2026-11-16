import re,sys
def parse(fn):
    words=[]  # list of (col, [groups])
    for line in open(fn):
        if line.startswith('#') or ':' not in line: continue
        col,rest=line.split(':',1)
        for w in rest.split('|'):
            g=w.split()
            if g: words.append((col.strip(),g))
    return words
def expand(g):
    # doubled groups 2-99 etc -> two letters same cell
    out=[]
    for x in g:
        x=x.rstrip('?')
        if x.startswith('['): out.append(x); continue
        r,c=x.split('-')
        if len(c)==2 and c[0]==c[1] and x in ('2-99','6-77','15-55','2-77'):
            out += [r+'-'+c[0]]*2
        else: out.append(x)
    return out
