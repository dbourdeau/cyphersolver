# Two-fold cross-validation on the training lines only (17 Nov 2026), to estimate what a key of this code would score
# on held-out lines before spending the held-out portion (113 right L19-L33, not in this folder, never decoded).
# Run from the target folder: python3 scripts/cv_estimate.py .
# Fold a: key fitted on 113R L01-L09 + 114L, scored on 113R L10-L18; fold b: the reverse. Same voting and same metric
# (ADDENDUM-3) as build_key3.py, pass 4 numbers. The starting draft key was itself fitted on all training lines, so the
# figures are optimistic. "+table" fills values unseen in the fold from Fable's proposal (key/fable_lot14_proposal.json).
import sys,collections,json,random
B=sys.argv[1]; sys.path.insert(0,B+'/scripts')
import build_key3 as bk
from data import load
L=load(B+'/transcriptions/113R_L01-L18_pass4_final.tsv'); G=load(B+'/transcriptions/114L_G01-G32_pass3_final.tsv')
T,TW=bk.T,bk.TW; start=dict(bk.key); fab=json.load(open(B+'/key/fable_lot14_proposal.json'))
flat=lambda rows:[g for r in rows for g in r[1]]
def train(seqs,key):
    key=dict(key)
    for it in range(12):
        votes=collections.defaultdict(collections.Counter)
        for S in seqs:
            _,P=bk.align(''.join(key.get(g,'?') for g in S),T)
            for i,j in P: votes[S[i]][T[j]]+=1
        cnt=collections.Counter(g for S in seqs for g in S); new=dict(key)
        for n,c in votes.items():
            l,k=c.most_common(1)[0]
            if k>=2 or cnt[n]==1: new[n]=l
        if new==key: break
        key=new
    used={g for S in seqs for g in S}; return {n:v for n,v in key.items() if n in used}
def score(S,key):
    d=''.join(key.get(g,'?') for g in S); return 1-bk.cost3(d,TW)/len(d)
def best_witness(S,key,n=50,seed=1676000):
    ks,vs=list(key),list(key.values()); b=0
    for s in range(n):
        v=vs[:]; random.Random(seed+s).shuffle(v); b=max(b,score(S,dict(zip(ks,v))))
    return b
for name,tr,te in (('a: test L10-L18',L[:9],L[9:18]),('b: test L01-L09',L[9:18],L[:9])):
    k=train([flat(tr),flat(G)],start); kt=dict(fab); kt.update(k); Ste=flat(te)
    print('%s |test| %d unseen %d A_test %.3f A_test+table %.3f best of 50 witnesses %.3f'%(
        name,len(Ste),sum(g not in k for g in Ste),score(Ste,k),score(Ste,kt),best_witness(Ste,k)))
k=train([flat(L),flat(G)],start); print('resubstitution, all training lines: 113R %.3f 114L %.3f'%(score(flat(L),k),score(flat(G),k)))
