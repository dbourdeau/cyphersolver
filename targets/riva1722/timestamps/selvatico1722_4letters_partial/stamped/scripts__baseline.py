"""baseline.py KEY TX N SEED -- shuffled-key baseline. Score = mean Italian quadgram log-prob (wave14 quad.pkl; v->u) over runs of
keyed units (SYL/WORD only; a code, unkeyed, illegible or struck unit or clear text breaks the run). Shuffle = random permutation of
the key values over the distinct keyed canonical tokens present in TX. No optimisation of the shuffled keys."""
import sys,random,pickle,re,importlib.util
spec=importlib.util.spec_from_file_location('dec','/home/claude/en/trackB/b70_selvatico_read/scripts/dec.py');dec=importlib.util.module_from_spec(spec);spec.loader.exec_module(dec)
Q=pickle.load(open('/home/claude/en/trackB/wave14_cosimo/quad.pkl','rb'));q=Q['q'];fl=Q['floor']
key=dec.loadkey(sys.argv[1]); N=int(sys.argv[3]); random.seed(int(sys.argv[4]))
seq=[]
for lid,items in dec.run(sys.argv[1],sys.argv[2]):
    for k,o in items:
        seq.append(o['canon'] if k=='unit' and o['cls'] in('SYL','WORD') else None)
types=sorted({t for t in seq if t})
real={t:key[t].lower().replace('v','u') for t in types}
def score(m):
    s=n=0;cur=''
    for t in seq+[None]:
        if t is None:
            for i in range(len(cur)-3): s+=q.get(cur[i:i+4],fl); n+=1
            cur=''
        else: cur+=m[t]
    return s/n
R=score(real);vals=[real[t] for t in types];best=-99;ge=0;tot=0
for i in range(N):
    random.shuffle(vals);s=score(dict(zip(types,vals)));tot+=s;best=max(best,s);ge+=s>=R
print(f"{sys.argv[1].split('/')[-1]} on {sys.argv[2].split('/')[-1]}: keyed units {sum(1 for t in seq if t)}, types {len(types)}; real {R:.3f}; shuffled mean {tot/N:.3f}, max {best:.3f}; shuffles >= real {ge}/{N} (seed {sys.argv[4]})")
