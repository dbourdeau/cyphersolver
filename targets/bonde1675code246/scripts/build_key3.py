# Draft-key builder as run on 14 Nov 2026 (pass 3: METHODE-CLE.md + ADDENDUM-3), with the file paths changed to this
# folder. Run from the target folder: python3 scripts/build_key3.py .  It writes key/key_draft.rebuilt.json and prints
# the resubstitution figures (0.6534 with the ADDENDUM-3 metric, 0.6309 with the earlier one) and the two decodes.
# Clé passe 3 : METHODE-CLE.md inchangée + ADDENDUM-3 (S1/S2 passe 3 ; T normalisée (b)1 ; métrique (b)2-3)
import sys,re,collections,json
B=sys.argv[1]; sys.path.insert(0,B+'/scripts')
from data import load
ABBR=[(r'\bMaij?:\s*t?t[zs]\b','maiestets'),(r'\bMaij?:\s*(tt|t|~)?','maiestet'),(r'\bM:\s*tt?\b','maiestet'),
      (r'\bKongl[:.]','kongelig'),(r'\bförbe[mn]:\s*~?|\bförb:\s*te\b','förbenämnde'),(r'\bd\.(?=\s*\d)','den'),
      (r'&','och'),(r'\bExc(ell)?[:.]','excellens')]
def pre(s):
    s=re.sub(r'‹[^›]*›',' ',s); s=re.sub(r'\{([^|}]*)[^}]*\}',r'\1',s); s=re.sub(r'[\[\]]','',s)
    return s
def abbr(s):
    for p,r in ABBR: s=re.sub(p,r,s,flags=re.I)
    return s
def nw(w):
    w=w.lower().replace('w','v').replace('j','i'); return re.sub(r'[^a-zåäö#]','',w)
def words(raw):  # list of normalised words
    return [x for x in (nw(w) for w in abbr(pre(raw)).split()) if x]
fab=[l.rstrip('\n').split('\t') for l in open(B+'/gloss/113R_G01-G20_fable.tsv',encoding='utf-8')][1:]
hg={'H'+f[0][1:]:f[1] for f in (l.rstrip('\n').split('\t') for l in open(B+'/gloss/113R_G19-G33_subagents.tsv',encoding='utf-8'))}  # gloss only (was column 3 of the held-out file)
G114=load(B+'/transcriptions/114L_G01-G32_pass3_final.tsv'); L=load(B+'/transcriptions/113R_L01-L18_pass3_final.tsv')
G114A=load(B+'/transcriptions/114L_G01-G32_pass1.tsv')
raw=' '.join(r[1] for r in fab)+' '+' '.join(hg['H%02d'%k] for k in range(21,34))+' '+' '.join(r[2] for r in G114A[:5])
TW=words(raw); T=''.join(TW)
S1=[g for r in L for g in r[1]]; S2=[g for r in G114 for g in r[1]]
key={}
for l in open(B+'/key/key_start_draft.tsv'):
    if l.startswith('#') or not l.strip(): continue
    n,v=l.split()[:2]; key[n]=v
def align(a,b):   # align() d'origine (build_key.py), pour le vote
    n,m=len(a),len(b); D=[[0]*(m+1) for _ in range(n+1)]
    for i in range(1,n+1): D[i][0]=i
    for i in range(1,n+1):
        ai=a[i-1]; p=D[i-1]; c=D[i]
        for j in range(1,m+1):
            c[j]=min(p[j]+1,c[j-1]+1,p[j-1]+(0 if (ai==b[j-1] and ai!='?') else 1))
    j=min(range(m+1),key=lambda j:D[n][j]); dist=D[n][j]; i=n; pairs=[]
    while i>0 and j>0:
        if D[i][j]==D[i-1][j-1]+(0 if (a[i-1]==b[j-1] and a[i-1]!='?') else 1): pairs.append((i-1,j-1)); i-=1; j-=1
        elif D[i][j]==D[i-1][j]+1: i-=1
        else: j-=1
    return dist,pairs[::-1]
def cost3(a,W):   # métrique ADDENDUM-3 (b)2 : semi-globale, saut de mot entier de référence = 1
    b=''.join(W); m=len(b); starts={}; pos=0
    for w in W: starts[pos+len(w)]=pos; pos+=len(w)   # end -> start
    INF=10**9; prev=[0.0]*(m+1)
    for i in range(1,len(a)+1):
        ai=a[i-1]; cur=[prev[0]+1]+[0.0]*m
        for j in range(1,m+1):
            v=min(prev[j]+1,cur[j-1]+1,prev[j-1]+(0 if (ai==b[j-1] and ai!='?' and ai!='#') else 1))
            s=starts.get(j)
            if s is not None: v=min(v,cur[s]+1)
            cur[j]=v
        prev=cur
    return min(prev)
dec=lambda S:''.join(key.get(g,'?') for g in S)
if __name__=='__main__':
    for it in range(13):
        d1,p1=align(dec(S1),T); d2,p2=align(dec(S2),T)
        print(it,'A_train(ancienne)=%.4f'%(1-(d1+d2)/(len(S1)+len(S2))),flush=True)
        if it==12: break
        votes=collections.defaultdict(collections.Counter)
        for S,P in((S1,p1),(S2,p2)):
            for i,j in P: votes[S[i]][T[j]]+=1
        cnt=collections.Counter(S1+S2); new=dict(key)
        for n,c in votes.items():
            l,k=c.most_common(1)[0]
            if k>=2 or cnt[n]==1: new[n]=l
        if new==key: print('converged'); break
        key=new
    used=set(S1+S2); key={n:v for n,v in key.items() if n in used}
    json.dump(key,open(B+'/key/key_draft.rebuilt.json','w'),indent=0,sort_keys=True)
    d1,_=align(dec(S1),T); d2,_=align(dec(S2),T)
    c1=cost3(dec(S1),TW); c2=cost3(dec(S2),TW)
    print('|S1|',len(S1),'|S2|',len(S2),'|T|',len(T),'nkey',len(key))
    print('ANCIENNE metrique A_train=%.4f (S1 %.3f S2 %.3f)'%(1-(d1+d2)/(len(S1)+len(S2)),1-d1/len(S1),1-d2/len(S2)))
    print('ADDENDUM-3 metrique A_train=%.4f (S1 %.3f S2 %.3f)'%(1-(c1+c2)/(len(S1)+len(S2)),1-c1/len(S1),1-c2/len(S2)))
    print(dec(S1)); print(dec(S2))
