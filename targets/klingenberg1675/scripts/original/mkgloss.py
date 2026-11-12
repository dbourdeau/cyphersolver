# mkgloss.py words.json tx seg.txt out.tsv : build index gloss from a judge's word sequence.
# seg tokens: word (must equal the decode of the next k tokens exactly, k found greedily) | word:n (intended word over next n tokens,
# decode may differ = failure) | ?n (n tokens left unglossed = failure). Lines starting with # ignored. Asserts all cipher tokens are consumed.
import sys,os,json
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from kt2 import tokens,SIGN2
here=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
t=json.load(open(os.path.join(here,'frozen/table_M3.json')))
w={k:v for k,v in json.load(open(sys.argv[1])).items() if not k.startswith('_')}
T=[(k,x) for k,x in tokens(sys.argv[2]) if k!='C']
dec=[((t[x] if x in t else w.get(x,'['+x+']')) if k=='N' else SIGN2.get(x,'?')).lower() for k,x in T]
segs=[s for l in open(sys.argv[3],encoding='utf-8') if not l.startswith('#') for s in l.split()]
i=0; out=[]
for s in segs:
    if s.startswith('?'): i+=int(s[1:]); continue
    if ':' in s:
        g,n=s.split(':'); n=int(n); out.append((i,i+n-1,g)); i+=n; continue
    j=i; acc=''
    while j<len(dec) and len(acc)<len(s): acc+=dec[j]; j+=1
    if acc!=s: sys.exit(f'MISMATCH at token {i}: want {s!r} got {acc!r}; next decode: {dec[i:i+10]}')
    out.append((i,j-1,s)); i=j
if i!=len(dec): sys.exit(f'consumed {i} of {len(dec)}; next decode {dec[i:i+12]}')
open(sys.argv[4],'w',encoding='utf-8').write(''.join(f'{a} {b} {g}\n' for a,b,g in out)); print('gloss spans',len(out),'tokens',len(dec))
