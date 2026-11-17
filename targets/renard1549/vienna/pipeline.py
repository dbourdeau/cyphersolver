#!/usr/bin/env python3
"""renard1549 Vienna original: alignment of frozen CIPHER.tsv with frozen FR_CLEAR.txt, key build, hold-out test, shuffle control.
Run: python3 -I pipeline.py   (reads only CIPHER.tsv, FR_CLEAR.txt, SIGNS.tsv, seed_init.json in this folder)"""
import re,math,sys,collections,json,random,hashlib,os
W=os.path.dirname(os.path.abspath(__file__))+'/'
MAXL=5
LENP={0:0.04,1:0.60,2:0.25,3:0.06,4:0.03,5:0.02}
def load_plain():
    out=[]
    for ln in open(W+'FR_CLEAR.txt',encoding='utf-8'):
        if ln.startswith('#') or not ln.strip(): continue
        lid,txt=ln.rstrip('\n').split('\t')
        if lid.split('.')[1][0] not in 'TMB': continue      # decipherer's zones only
        txt=txt.replace('[?]','').replace('&','et')
        txt=re.sub(r'[\[\]]','',txt).lower()
        out.append((lid,re.sub(r'[^a-z]','',txt)))
    return out
def load_cipher():
    out=[]
    for ln in open(W+'CIPHER.tsv',encoding='utf-8'):
        if ln.startswith('#'): continue
        fol,l,pos,s=ln.rstrip('\n').split('\t')
        out.append((fol+'.'+l,s.rstrip('?')))
    return out
def viterbi(toks,text,logp,ratio,band=260,free_end=False):
    T=len(toks);L=len(text);NEG=-1e18
    best=[[NEG]*(L+1) for _ in range(T+1)]; bk=[[0]*(L+1) for _ in range(T+1)]
    best[0][0]=0.0
    for t in range(T):
        bt=best[t]; bn=best[t+1]; bkn=bk[t+1]; c=int(t*ratio); tok=toks[t]
        for i in range(max(0,c-band),min(L,c+band)+1):
            b=bt[i]
            if b<=NEG/2: continue
            for k in range(0,MAXL+1):
                if i+k>L: break
                v=b+logp(tok,text[i:i+k])
                if v>bn[i+k]: bn[i+k]=v; bkn[i+k]=k
    end=max(range(L+1),key=lambda i:best[T][i]) if free_end else L
    seg=[];i=end
    for t in range(T,0,-1):
        k=bk[t][i]; seg.append(text[i-k:i]); i-=k
    seg.reverse()
    return best[T][end],seg,end
def em(toks,text,seed,ratio,free_end=False,iters=14,seed_iters=5,strength=15):
    counts=collections.defaultdict(collections.Counter)
    for g,v in seed.items(): counts[g][v]+=strength
    seg=None;end=None
    for it in range(iters):
        tot={t:sum(c.values()) for t,c in counts.items()}
        def logp(tok,sub,counts=counts,tot=tot):
            return math.log((counts.get(tok,{}).get(sub,0)+0.3*LENP[len(sub)])/(tot.get(tok,0)+0.3))
        sc,seg,end=viterbi(toks,text,logp,ratio,free_end=free_end)
        counts=collections.defaultdict(collections.Counter)
        if it<seed_iters-1:
            for g,v in seed.items(): counts[g][v]+=strength
        for t,s in zip(toks,seg): counts[t][s]+=1
    return counts,seg,end
def key_from(counts):
    key={}
    for t,c in counts.items():
        (v,n),=c.most_common(1)
        key[t]=(v,n,sum(c.values()))
    return key
def decode(toks,key): return ''.join(key[t][0] if t in key else '?' for t in toks)
def lev(a,b):
    # Myers bit-parallel edit distance
    if not a: return len(b)
    pe=collections.defaultdict(int)
    for i,ch in enumerate(a): pe[ch]|=1<<i
    m=len(a); mask=(1<<m)-1; pv=mask; mv=0; sc=m; hb=1<<(m-1)
    for ch in b:
        eq=pe.get(ch,0); xv=eq|mv; xh=(((eq&pv)+pv)^pv)|eq
        ph=mv|~(xh|pv); mh=pv&xh
        if ph&hb: sc+=1
        elif mh&hb: sc-=1
        ph=((ph<<1)|1)&mask; mh=(mh<<1)&mask
        pv=(mh|~(xv|ph))&mask; mv=ph&xv
    return sc
def acc(dec,truth): return 1-lev(dec,truth)/max(len(dec),len(truth))
if __name__=='__main__':
    P=load_plain();C=load_cipher()
    text=''.join(t for _,t in P); toks=[s for _,s in C]
    seed=json.load(open(W+(sys.argv[2] if len(sys.argv)>2 else 'seed_init.json')))
    ratio=len(text)/len(toks)
    mode=sys.argv[1] if len(sys.argv)>1 else 'full'
    lines=list(collections.OrderedDict((l,1) for l,_ in C))
    if mode=='full':
        counts,seg,end=em(toks,text,seed,ratio)
        key=key_from(counts)
        with open(W+'key_renard1549_vienna.tsv','w',encoding='utf-8') as f:
            f.write('# key_renard1549_vienna.tsv  key recovered based on adjacent plaintext (contemporary marginal decipherment), HHStA Frankreich Dipl.Korr. 17, Konv. Juli 1549, fol. 13-14\n')
            f.write('# sign = neutral label of CIPHER.tsv / SIGNS.tsv; value = majority value in the alignment; n_value = times aligned to that value; n_total = occurrences; other = other aligned values with counts (- = aligned to nothing)\n')
            f.write('# sign\tvalue\tn_value\tn_total\tother\n')
            for t in sorted(key,key=lambda t:(-key[t][2],t)):
                v,n,tt=key[t]; oth=' '.join('%s:%d'%(k or '-',c) for k,c in counts[t].most_common() if k!=v)
                f.write('%s\t%s\t%d\t%d\t%s\n'%(t,v or '-',n,tt,oth))
        with open(W+'ALIGNMENT.tsv','w',encoding='utf-8') as f:
            f.write('# line\tpos\tsign\taligned_plaintext\tkey_value\n')
            pos=collections.Counter()
            for (l,t),s in zip(C,seg):
                pos[l]+=1; f.write('%s\t%d\t%s\t%s\t%s\n'%(l,pos[l],t,s or '-',key[t][0] or '-'))
        with open(W+'DECODE_fullkey.txt','w',encoding='utf-8') as f:
            f.write('# each cipher line decoded with the full key (majority values), then the plaintext the alignment gave that line\n')
            by=collections.OrderedDict()
            for (l,t),s in zip(C,seg): by.setdefault(l,[]).append((t,s))
            for l,x in by.items():
                f.write('%s\tKEY\t%s\n%s\tFR \t%s\n'%(l,' '.join(key[t][0] or '-' for t,_ in x),l,' '.join(s or '-' for _,s in x)))
        d=decode(toks,key); print('full-key self-decode accuracy (in-sample, not a test): %.4f  tokens %d letters %d signs %d'%(acc(d,text),len(toks),len(text),len(key)))
    else:
        ntrain=round(len(lines)*0.8); trl=set(lines[:ntrain]); hol=lines[ntrain:]
        tr=[s for l,s in C if l in trl]; ho=[s for l,s in C if l not in trl]
        counts,seg,end=em(tr,text,seed,ratio,free_end=True)
        key=key_from(counts); truth=text[end:]
        dec=decode(ho,key); a=acc(dec,truth)
        unseen=sum(1 for t in ho if t not in key)
        print('lines total %d train %d (%s..%s) held-out %d (%s..%s)'%(len(lines),ntrain,lines[0],lines[ntrain-1],len(hol),hol[0],hol[-1]))
        print('train tokens %d, held-out tokens %d (unseen signs %d), plaintext boundary at letter %d of %d, held-out letters %d'%(len(tr),len(ho),unseen,end,len(text),len(truth)))
        print('HELD-OUT DECODE :',dec); print('HELD-OUT TRUTH  :',truth)
        print('held-out letter accuracy (1 - Levenshtein/max len), no emendation: %.4f  (edit distance %d, decoded %d, truth %d)'%(a,lev(dec,truth),len(dec),len(truth)))
        signs=sorted(key); vals=[key[t][0] for t in signs]
        for sd in (20261112,7):
            rng=random.Random(sd); best=0;tot=0;ge=0;N=5000
            for _ in range(N):
                v=vals[:]; rng.shuffle(v); k=dict(zip(signs,v))
                s=acc(''.join(k.get(t,'?') for t in ho),truth); tot+=s; best=max(best,s); ge+=(s>=a)
            print('control seed %d: %d shuffles of key values over the %d signs: mean %.4f max %.4f, shuffles >= real: %d'%(sd,N,len(signs),tot/N,best,ge))
