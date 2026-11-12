# shuffle_words.py table.json words.json tx gloss.tsv n seed : strict sense with real word map vs n random permutations of the
# word-map values over the same codes (table fixed). Reports mean, sd, max, count >= real.
import sys,json,os,random,statistics
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from kt2 import tokens,SIGN2
t=json.load(open(sys.argv[1])); w={k:v for k,v in json.load(open(sys.argv[2])).items() if not k.startswith('_')}
T=[(k,x) for k,x in tokens(sys.argv[3]) if k!='C']
G=[]
for l in open(sys.argv[4],encoding='utf-8'):
    if l.strip() and not l.startswith('#'):
        a,b,g=l.split(); G.append((int(a),int(b),g))
n=int(sys.argv[5]); rnd=random.Random(int(sys.argv[6]))
def strict(wm):
    dec=[(t[x] if x in t else wm.get(x,'['+x+']')) if k=='N' else SIGN2.get(x,'?') for k,x in T]
    return sum(b-a+1 for a,b,g in G if ''.join(dec[a:b+1]).lower()==g)
real=strict(w); keys=list(w); X=[]
for i in range(n):
    v=[w[k] for k in keys]; rnd.shuffle(v); X.append(strict(dict(zip(keys,v))))
mu=statistics.mean(X); sd=statistics.pstdev(X); N=len(T)
print(f'N={N} real strict {real} ({100*real/N:.1f}%); shuffled mean {mu:.1f} ({100*mu/N:.1f}%) sd {sd:.2f} max {max(X)} ({100*max(X)/N:.1f}%); z {(real-mu)/sd:.1f}; shuffles>=real {sum(x>=real for x in X)}/{n}')
