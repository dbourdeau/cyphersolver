# decode_adjudicated.py: one decode of the frozen adjudicated transcription with key_B.txt, labelled by the rule in
# transcriptions/adjudication_rule.md. Checks the freeze file first. Writes decryptions/adjudicated.txt.
import os,hashlib,collections
R=os.path.dirname(os.path.dirname(os.path.abspath(__file__))); P=lambda *a: os.path.join(R,*a)
for l in open(P('transcriptions','ADJUDICATION_FROZEN.md5')):
    p=l.split()
    if len(p)==2 and len(p[0])==32:
        assert hashlib.md5(open(P(p[1]),'rb').read()).hexdigest()==p[0],('changed since freeze',p[1])
key={}
for l in open(P('key_B.txt')):
    if l.startswith('#'): continue
    for x in l.split(): a,b=x.split('='); key[a]=b
SF=set(l.split('\t')[0] for l in open(P('transcriptions','s_forms.txt'),encoding='utf-8') if not l.startswith('#'))
rows=[l.rstrip('\n').split('\t') for l in open(P('transcriptions','adjudicated.tsv'),encoding='utf-8') if not l.startswith('#')]
def dec(u): return ''.join(key.get(c,'?') for c in u)
def lab(u):
    if u.isdigit(): return u,'E'
    d=dec(u)
    if '?' in d: return d,'N'
    return d,('S' if d in SF else 'E')
res={}
with open(P('decryptions','adjudicated.txt'),'w',encoding='utf-8') as f:
    f.write('# Decode of transcriptions/adjudicated.tsv with key_B.txt, run once; labels by transcriptions/adjudication_rule.md\n# line\treader1 unit\tmajority\tdecode\tlabel\tunanimous\tdecode\tlabel\n')
    for col in (2,3): res[col]=collections.Counter()
    for r in rows:
        dm,lm=lab(r[2]); du,lu=lab(r[3]); res[2][lm]+=1; res[3][lu]+=1
        f.write('\t'.join([r[0],r[1],r[2],dm,lm,r[3],du,lu])+'\n')
for col,name in ((2,'majority (>=2 of 3)'),(3,'unanimous (all 3)')):
    c=res[col]; n=c['S']+c['E']+c['N']
    print('%s: S %d + E %d + N %d = %d; strict S/(S+E+N) = %d/%d = %.2f%%'%(name,c['S'],c['E'],c['N'],n,c['S'],n,100*c['S']/n))
