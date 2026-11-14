import re,sys,collections,json
def parse(path):
    words=[]  # list of (clear_prefix, [cells])
    lead=None
    for line in open(path):
        line=line.rstrip('\n')
        if not line or line.startswith('#'): continue
        clear=re.findall(r'"([^"]*)"',line)
        rest=re.sub(r'"[^"]*"\??','',line)
        cells=[]
        mo=re.search(r'\{lead=(\d+)\}',rest)
        if mo: lead=int(mo.group(1)); rest=rest.replace(mo.group(0),'')
        for tok in rest.split():
            if tok=='@': cells.append('@'); continue
            if tok=='[blot]': cells.append('?'); continue
            m=re.match(r'^(\d+)?\.(\d+)$',tok)
            if m:
                if m.group(1): lead=int(m.group(1))
                cells.append((lead,int(m.group(2))))
        words.append((clear,cells))
    return words
if __name__=='__main__':
    w=parse(sys.argv[1])
    allc=[c for _,cs in w for c in cs if isinstance(c,tuple)]
    print('words',len(w),'cells',len(allc),'distinct',len(set(allc)))
    cnt=collections.Counter(allc)
    print(sorted(cnt.items(),key=lambda x:-x[1])[:40])
    byline=collections.defaultdict(set)
    for l,p in allc: byline[l].add(p)
    for l in sorted(byline): print(l,sorted(byline[l]))
