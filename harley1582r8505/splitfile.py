import sys,os,json,collections,glob
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__))+'/..')
import word as W
LET=W.LET; key=json.load(open(sys.argv[1])); target=sys.argv[2:]
def runs_with_file():
    out=[]
    for fn in sorted(glob.glob('ct_p*.txt')):
        for line in open(fn,encoding='utf-8'):
            if line.startswith('#') or '|' not in line: continue
            p=[x.strip() for x in line.split('|')]
            if len(p)<3: continue
            seg=[]
            for t in ' : '.join(p[2::2]).replace('/',' ').split():
                t=t.rstrip('?')
                if not t or t==':' or t.startswith('#') or t in ('.','..','-'):
                    if seg: out.append((fn,seg)); seg=[]
                    continue
                seg.append(t.split('/')[0])
            if seg: out.append((fn,seg))
    return out
st=collections.defaultdict(collections.Counter)
for fn,r in runs_with_file():
    if len(r)<3: continue
    base=[key.get(s,'e') for s in r]
    for i,s in enumerate(r):
        if target and s not in target: continue
        best=None
        for c in LET:
            t=''.join(base[:i]+[c]+base[i+1:])
            v=W.seg_score(t)+W.CH.score(t)
            if best is None or v>best[0]: best=(v,c)
        st[(s,fn)][best[1]]+=1
for (s,fn),c in sorted(st.items()):
    print(f'{s:4s} {fn}  ' + ' '.join(f'{ch}:{n}' for ch,n in c.most_common(4)))
