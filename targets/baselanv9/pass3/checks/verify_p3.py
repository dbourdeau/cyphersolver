"""Checks for the pass 3 follow-up (own code, python3 -I). usage: verify_p3.py <basel_p2> <repo target folder>"""
import sys,re,difflib
R,W=sys.argv[1].rstrip('/')+'/',sys.argv[2].rstrip('/')+'/'
def tsv(p):
    r=[]
    for ln in open(p,encoding='utf-8'):
        if ln.startswith('#') or not ln.strip(): continue
        r.append(ln.rstrip('\n').split('\t'))
    return r
k3={r[0]:r[1] for r in tsv(R+'KEY_V3.tsv')[1:]}
kl=tsv(W+'keyleaf/KEY_LEAF.tsv'); hdr=kl[0]; print('KEY_LEAF header',hdr)
kd={}
for r in kl[1:]:
    kd.setdefault(r[0],[]).append(r)
same=[t for t in k3 if t in kd and any(k3[t]==x[1] for x in kd[t])]
print('KEY_V3 tokens',len(k3),'| in KEY_LEAF with the same value',len(same),'| differing or absent',[(t,k3[t],[x[1] for x in kd.get(t,[])]) for t in k3 if t not in same])
print('KEY_LEAF rows not in KEY_V3:',[(r[0],r[1]) for r in kl[1:] if r[0] not in k3])
print('shape_match counts:',{v:[r[3] for r in tsv(R+'KEY_V3.tsv')[1:]].count(v) for v in ('exact','probable')})
def lines(p):
    return {r[0]:[w.split() for w in r[1].split(' / ')] for r in tsv(p) if len(r)==2}
a=lines(W+'keyleaf/tx2/f015r.txt'); b=lines(R+'tx/f015r_p3.txt')
tw=cw=0
for l in sorted(b):
    A=[' '.join(w) for w in a.get(l,[])]; B=[' '.join(w) for w in b[l]]
    ch=sum(1 for w in B if w not in A); tw+=len(B); cw+=ch
    print(l,'pass-2 words',len(A),'pass-3 words',len(B),'pass-3 words not in the pass-2 line',ch)
print('H1 re-read: %d of %d pass-3 cipher words differ from pass 2 (tx2/f015r.txt)'%(cw,tw))
dec=open(R+'DECODE_P3.txt').read()
print('ch~ri count: H1r',sum(l.count('ch~ri') for l in dec.split('\n') if l.startswith('H1r')),'S2',sum(l.count('ch~ri') for l in dec.split('\n') if l.startswith('S2')))
clear=''.join(l for l in open(W+'score/CLEAR_H1_f109v.txt') if not l.startswith('#')).lower()
clear=re.sub(r'[\[\]]','',clear); clear=re.sub('[^a-z]','',clear.replace('v','u').replace('j','i'))
for name,p in [('pass 3',R+'DECODE_P3.txt'),('noC4C5',R+'pr_prep/variant/DECODE_P3_noC4C5.txt')]:
    d=''.join(l.split('\t')[1] for l in open(p) if l.startswith('H1r')); d=re.sub('[^a-z]','',d.replace('[?]',''))
    m=sum(x.size for x in difflib.SequenceMatcher(None,d,clear,autojunk=False).get_matching_blocks())
    print('H1r %s against clear f.109v: matched %d of %d clear letters = %.1f%%; decode letters %d'%(name,m,len(clear),100*m/len(clear),len(d)))
