import sys,os,json,glob
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__))+'/..')
mp=json.load(open(sys.argv[1]))
lo=int(sys.argv[2]); hi=int(sys.argv[3])
n=0
for fn in sorted(glob.glob('ct_p*.txt')):
    for line in open(fn,encoding='utf-8'):
        if line.startswith('#') or '|' not in line: continue
        p=[x.strip() for x in line.split('|')]
        if len(p)<3: continue
        seg=[]
        for t in ' : '.join(p[2::2]).replace('/',' ').split():
            t=t.rstrip('?')
            if not t or t==':' or t.startswith('#') or t in ('.','..','-'):
                if seg:
                    if lo<=n<hi: print(f'[{n}] {p[0]} <{p[1]}> {"".join(mp.get(s,"?") for s in seg)} <{p[-1][:40]}>')
                    n+=1; seg=[]
                continue
            seg.append(t.split('/')[0])
        if seg:
            if lo<=n<hi: print(f'[{n}] {p[0]} <{p[1]}> {"".join(mp.get(s,"?") for s in seg)} <{p[-1][:40]}>')
            n+=1
