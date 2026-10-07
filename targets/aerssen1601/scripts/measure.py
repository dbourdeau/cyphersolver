"""measure.py <key.tsv> <reading.md> [--control N]
key.tsv: token<TAB>value(s, '/'-separated alternatives; '@' prefix = code word)<TAB>grade(H/C/M/I)<TAB>evidence
reading.md blocks:
  ## <id> ...
  TOK: t1 t2 ...            (cipher tokens, notation of CONVENTIONS.md; [n] markers ignored)
  SEG: t1 t2 => mot | t3 => mot2 | t4 => ?  (every token exactly once, same order)
A token counts as READ when its group's word is not '?' and the concatenation of key values of the group
(some alternative combination) equals the word after normalisation (case, accents, u/v, i/j/y; '@' code
words compared as whole words). Grade of a read token = its key grade. Unread = '?' group, key-missing,
or mismatch. Prints per-passage and total shares, by grade. --control: shuffles TOK within each passage,
decodes with the most likely value of each token and reports French coverage vs. the real order."""
import sys, re, random, itertools
sys.path.insert(0, __import__('os').path.dirname(__file__))
from frscore import norm, coverage
def load_key(fn):
    K={}
    for ln in open(fn):
        if not ln.strip() or ln.startswith('#'): continue
        p=ln.rstrip('\n').split('\t')
        K[p[0]]=(p[1].split('/'), p[2] if len(p)>2 else 'M')
    return K
def clean(t): return t.rstrip('?')
def look(K,t):
    t=clean(t)
    if t in K: return t
    if t.rstrip("'") in K: return t.rstrip("'")
    return None
def blocks(fn):
    B=[];cur=None
    for ln in open(fn):
        if ln.startswith('## '): cur={'id':ln[3:].split('|')[0].strip()}; B.append(cur)
        elif cur is not None and ln.startswith('TOK:'): cur['tok']=[t for t in ln[4:].split() if not re.fullmatch(r'\[\w+\]',t)]
        elif cur is not None and ln.startswith('SEG:'): cur['seg']=ln[4:].strip()
    return [b for b in B if 'tok' in b]
def group_ok(toks,word,K):
    if word.strip()=='?' : return None
    alts=[]
    for t in toks:
        k=look(K,t)
        if k is None: return None
        alts.append(K[k][0])
    w=norm(word)
    for combo in itertools.product(*alts):
        if norm(''.join(v.lstrip('@') for v in combo))==w: return combo
    return None
def tgrade(K,t,v):
    k=look(K,t); g=K[k][1]
    if g!='I' and v!=K[k][0][0]: g='M'   # minority homophone value used
    return g
def main():
    a=sys.argv[1:]; K=load_key(a[0]); B=blocks(a[1])
    ctrl=int(a[a.index('--control')+1]) if '--control' in a else 0
    tot={'n':0,'read':0,'H':0,'C':0,'M':0,'I':0}
    for b in B:
        n=len(b['tok']); read=0; g={'H':0,'C':0,'M':0,'I':0}
        if 'seg' in b:
            flat=[]
            for grp in b['seg'].split('|'):
                if '=>' not in grp: continue
                l,r=grp.split('=>',1); toks=l.split(); flat+=toks
                combo=group_ok(toks,r,K)
                if combo is not None:
                    read+=len(toks)
                    for t,v in zip(toks,combo): gg=tgrade(K,t,v); g[gg]=g.get(gg,0)+1
            if [clean(x) for x in flat]!=[clean(x) for x in b['tok']]:
                print('  !! SEG/TOK mismatch in',b['id'],len(flat),n)
        tot['n']+=n; tot['read']+=read
        for k in g: tot[k]=tot.get(k,0)+g[k]
        print(f"{b['id']:10s} tokens {n:4d} read {read:4d} ({100*read/max(n,1):5.1f}%)  H{g['H']} C{g['C']} M{g['M']} I{g['I']}")
    print(f"TOTAL tokens {tot['n']} read {tot['read']} = {100*tot['read']/max(tot['n'],1):.1f}%  by grade H{tot['H']} C{tot['C']} M{tot['M']} I{tot['I']}")
    nk=tot['read']-tot['I']
    print(f"  read from glossed key values only (H+C+M, excluding I = context-only): {nk} = {100*nk/max(tot['n'],1):.1f}%")
    if ctrl:
        rnd=random.Random(1)
        def dec(ts): return ''.join(K[look(K,t)][0][0].lstrip('@') if look(K,t) and K[look(K,t)][1]!='I' else '' for t in ts)
        real=[coverage(dec(b['tok'])) for b in B]
        allt=[t for b in B for t in b['tok']]
        realall=coverage(dec(allt))
        sh=[]
        for i in range(ctrl):
            s=[]
            for b in B:
                x=b['tok'][:]; rnd.shuffle(x); s+=x
            sh.append(coverage(dec(s)))
        sh.sort()
        print(f"CONTROL French coverage (words>=4 letters): real order {realall:.3f}; shuffled mean {sum(sh)/len(sh):.3f}, max {sh[-1]:.3f}, 95th pct {sh[int(.95*len(sh))-1]:.3f} (n={ctrl})")
        print(f"  real > all shuffles: {all(realall>x for x in sh)}")
if __name__=='__main__': main()
