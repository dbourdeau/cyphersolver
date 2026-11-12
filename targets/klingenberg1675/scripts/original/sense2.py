# sense2.py table.json words.json tx gloss.tsv : strict/lenient sense over ALL cipher tokens (b47 sense.py rules; kt2 tokens + SIGN2 + word map).
# strict: decode(span)==gloss exactly (lower-case); lenient: Levenshtein<=1 (<=2 if gloss>=9). Tokens not in any gloss span count as failures.
import sys,json,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from kt2 import tokens,SIGN2
t=json.load(open(sys.argv[1])); w={k:v for k,v in json.load(open(sys.argv[2])).items() if not k.startswith('_')}
T=[(k,x) for k,x in tokens(sys.argv[3]) if k!='C']
dec=[(t[x] if x in t else w.get(x,'['+x+']')) if k=='N' else SIGN2.get(x,'?') for k,x in T]
def lev(a,b):
    p=list(range(len(b)+1))
    for i,ca in enumerate(a,1):
        c=[i]
        for j,cb in enumerate(b,1): c.append(min(p[j]+1,c[j-1]+1,p[j-1]+(ca!=cb)))
        p=c
    return p[-1]
st=le=0; used=set(); quiet='-q' in sys.argv
for l in open(sys.argv[4],encoding='utf-8'):
    if not l.strip() or l.startswith('#'): continue
    a,b,g=l.split(); a,b=int(a),int(b); assert not (set(range(a,b+1))&used); used|=set(range(a,b+1))
    d=''.join(dec[a:b+1]).lower(); n=b-a+1; L=lev(d,g)
    s=(d==g); le_=L<=(2 if len(g)>=9 else 1); st+=n*s; le+=n*le_
    if not quiet: print(f'{a:>3}-{b:<3} {d:<18} {g:<16} {"STRICT" if s else ("lenient" if le_ else "no")}')
N=len(T); print(f'TOTAL cipher tokens {N}: strict {st}/{N} = {100*st/N:.1f}%  lenient {le}/{N} = {100*le/N:.1f}%  (glossed tokens {len(used)})')
