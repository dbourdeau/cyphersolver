# ledger.py words.json tx seg.txt out.tsv : full per-word-unit ledger (no sampling, no grep). Classes:
# S = decode of the unit equals the intended word exactly (strict); E = glossed but decode differs, or unit holds an unmapped code / unread run (?n);
# N = unit is only a damaged/doubtful mark (BLOT, EDGE, 'A?' mark) with no code to judge. Each seg item = one word unit.
import sys,os,json
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from kt2 import tokens,SIGN2
here=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
t=json.load(open(os.path.join(here,'frozen/table_M3.json')))
w={k:v for k,v in json.load(open(sys.argv[1])).items() if not k.startswith('_')}
raw=[x for x in open(sys.argv[2],encoding='utf-8').read().split('\n',1)[1].replace('\n',' ').split(' ')]
T=[(k,x) for k,x in tokens(sys.argv[2]) if k!='C']
dec=[((t[x] if x in t else w.get(x,'['+x+']')) if k=='N' else SIGN2.get(x,'<'+x+'>')).lower() for k,x in T]
segs=[s for l in open(sys.argv[3],encoding='utf-8') if not l.startswith('#') for s in l.split()]
i=0; rows=[]
for s in segs:
    if s.startswith('?'):
        n=int(s[1:]); d=''.join(dec[i:i+n]); toks=[x for k,x in T[i:i+n]]
        cls='N' if all(x in('BLOT','EDGE','A') and k=='L' for k,x in T[i:i+n]) and (toks!=['A'] or i==250) else 'E'
        rows.append((i,i+n-1,n,cls,d,'-')); i+=n; continue
    if ':' in s:
        g,n=s.split(':'); n=int(n); d=''.join(dec[i:i+n]); assert d!=g,(i,d,g); rows.append((i,i+n-1,n,'E',d,g)); i+=n; continue
    j=i; acc=''
    while j<len(dec) and len(acc)<len(s): acc+=dec[j]; j+=1
    assert acc==s,(i,acc,s); rows.append((i,j-1,j-i,'S',acc,s)); i=j
assert i==len(dec)
open(sys.argv[4],'w',encoding='utf-8').write('first\tlast\ttokens\tclass\tdecode\tintended\n'+''.join('\t'.join(map(str,r))+'\n' for r in rows))
for c in 'SEN':
    R=[r for r in rows if r[3]==c]; print(f'{c}: word units {len(R)}; tokens {sum(r[2] for r in R)}')
print('units',len(rows),'tokens',sum(r[2] for r in rows),'of',len(dec))
E=[r for r in rows if r[3]=='E']
print(' E glossed-but-wrong:',' + '.join(f'{r[5]} {r[2]}' for r in E if r[5]!='-'),'=',sum(r[2] for r in E if r[5]!='-'))
print(' E unread/unmapped:',' + '.join(f'{r[4]} {r[2]}' for r in E if r[5]=='-'),'=',sum(r[2] for r in E if r[5]=='-'))
print(' N:',' + '.join(f'{r[4]} {r[2]}' for r in rows if r[3]=='N'))
import collections
C=collections.Counter(len and r[2] for r in rows if r[3]=='S'); print(' S units by token length:',' + '.join(f'{C[k]}x{k}' for k in sorted(C)),'=',sum(k*C[k] for k in C),'tokens in',sum(C.values()),'units')
