"""C04 — alignement groupe ↔ clair 127-128 (APRÈS la mesure). Valeurs connues (key_c03 + ajouts) : coût 0 si la chaîne
correspond, sinon émission libre coût 4 ; valeurs inconnues : émission 0..7 lettres coût 1+0.2k ; lettres du clair sautées : 1,5 chacune.
Sortie : chemin (page.ligne, groupe, lettres) et tableau valeur -> chaînes."""
import sys,json,re,collections
sys.path.insert(0,'/Users/bdudout/Documents/Veille cyber/dechiffrements-europe/lovisa-ulrika-1764/cryptanalysis/c04/scripts')
from measure_clair import B,ORDER,norm
K=json.load(open(B+'c03/construction/key_c03.json')); K.update(json.load(open(B+'c03/construction/c03b_ajouts.json')))
G=[]
pages={p:[] for p in ORDER}
for l in open(B+'c03/transcr/lecture_121-124L.txt'):
    if l.startswith('#') or not l.strip(): continue
    lab,rest=l.split(' ',1); rest=re.sub(r'\[del:[^\]]*\]','',rest)
    for t in rest.split():
        g=re.sub(r"[?'`]",'',t)
        if g.isdigit(): pages[lab.split('.')[0]].append((g,lab))
G=[x for p in ORDER for x in pages[p]]
R=open(B+'c04/clair/127-128_norm.txt').read().strip()
N,M=len(G),len(R); INF=1e9; BAND=260
def cen(i): return i*M/N
D=[dict() for _ in range(N+1)]; D[0][0]=(0.0,None,None)
# clear skips at start allowed
for j in range(1,40): D[0][j]=(1.5*j,(0,j-1),'skip')
for i in range(N):
    g=G[i][0]; s=K.get(g); ks=None if s is None else norm(s)
    items=sorted(D[i].items())
    for j,(c,_,_) in items:
        opts=[]
        if ks is not None:
            if R[j:j+len(ks)]==ks: opts.append((len(ks),0.0))
            for k in range(0,7): opts.append((k,4.0+0.3*k))
        else:
            for k in range(0,8): opts.append((k,1.0+0.2*k))
        for k,cost in opts:
            jj=j+k
            if jj>M or abs(jj-cen(i+1))>BAND: continue
            v=c+cost
            if jj not in D[i+1] or D[i+1][jj][0]>v: D[i+1][jj]=(v,(i,j),R[j:jj])
    # clear-letter skips within row i+1
    row=D[i+1]
    for jj in sorted(row):
        v=row[jj][0]
        for d in (1,2,3):
            t=jj+d
            if t>M or abs(t-cen(i+1))>BAND: break
            nv=v+1.5*d
            if t not in row or row[t][0]>nv: row[t]=(nv,(i+1,jj),'skip')
end=min(D[N],key=lambda j:D[N][j][0]+1.5*(M-j))
path=[];i,j=N,end
while (i,j)!=(0,0) and D[i][j][1] is not None:
    _,(pi,pj),lab=D[i][j]
    if lab!='skip': path.append((G[i-1][1],G[i-1][0],lab,K.get(G[i-1][0])))
    i,j=pi,pj
path=path[::-1]
tab=collections.defaultdict(collections.Counter)
for lab,g,s,k in path: tab[g][s]+=1
json.dump({'path':path,'table':{g:dict(c) for g,c in tab.items()}},open(B+'c04/align_clair.json','w'),ensure_ascii=False,indent=0)
print('cost',round(D[N][end][0],1),'end',end,'of',M)
