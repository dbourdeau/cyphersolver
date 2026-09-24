import re,collections,sys
def items(path,sections):
    txt=open(path,encoding='utf-8').read()
    cur="D" if path.endswith("letter_D_1706.txt") else None; out=[]
    for line in txt.splitlines():
        m=re.match(r'## ([A-D])\.',line)
        if m: cur=m.group(1)
        if path.endswith('letter_D_1706.txt'): cur='D'
        if cur is None or cur not in sections or line.startswith('#'): continue
        for g,gl in re.findall(r'\[([0-9.?]+) = ([^\]]*)\]',line):
            out.append((cur,g.split('.'),gl.strip()))
    return out
A=items('letters_1697_1706.txt','A')
B=items('letters_1697_1706.txt','BC')+items('letter_D_1706.txt','D')
for name,its in (('code A',A),('code B',B)):
    single=collections.defaultdict(list); multi=collections.defaultdict(list)
    ntok=0; unglossed=0
    for let,gs,gl in its:
        ntok+=len(gs)
        if gl=='---': unglossed+=len(gs)
        if len(gs)==1: single[gs[0]].append(let+':'+gl)
        else:
            for g in gs: multi[g].append(let+':'+'.'.join(gs)+'='+gl)
    print('==',name,'tokens',ntok,'distinct',len(set(g for _,gs,_ in its for g in gs)),'unglossed tokens',unglossed)
    for g in sorted(set(single)|set(multi),key=lambda x:int(re.sub(r'\D','',x) or 0)):
        s=single.get(g,[]); m=multi.get(g,[])
        if len(s)+len(m)>1: print(' ',g,'|',s,'|',m[:4])
