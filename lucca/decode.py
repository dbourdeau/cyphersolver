# Polyphonic decode of R2159: each symbol has 1-2 candidate letters; Viterbi over the Italian 5-gram picks per occurrence.
import numpy as np,itertools
lp=np.load('it5.npy')
ct=[int(x) for x in open('ct.txt').read().split()]
key={1:'e',2:'g',3:'a',4:'b',5:'f',6:'c',7:'e',8:'d',9:'a',10:'h',11:'l',12:'m',13:'o',14:'n',15:'i',17:'i',18:'o',19:'ts',21:'r',22:'t',23:'u',25:'u',26:'p',32:'r'}
def lp5(a,b,c,d,e): return float(lp[a*456976+b*17576+c*676+d*26+e])
def viterbi(ct,key):
    cands=[[ord(ch)-97 for ch in key[c]] for c in ct]
    # state = last 4 letters; do beam search (exact is fine: at most 2 options/step)
    beams={():0.0}
    back=[]
    for i,opts in enumerate(cands):
        nb={}
        for hist,sc in beams.items():
            for o in opts:
                h=hist+(o,)
                s=sc
                if len(h)>=5: s+=lp5(*h[-5:])
                elif len(h)>=1: s+=0
                k=h[-4:]
                if k not in nb or nb[k][0]<s: nb[k]=(s,hist,o)
        back.append(nb); beams={k:v[0] for k,v in nb.items()}
    # backtrack
    k=max(beams,key=beams.get); out=[]
    for i in range(len(cands)-1,-1,-1):
        s,hist,o=back[i][k]; out.append(o); k=hist[-4:] if len(hist)>=4 else hist
    return ''.join(chr(97+x) for x in reversed(out))
if __name__=='__main__':
    txt=viterbi(ct,key); print(txt)
    open('plaintext_raw.txt','w').write(txt)
    print(' '.join(f'{c}={l}' for c,l in zip(ct,txt)))
