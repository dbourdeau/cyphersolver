# Align pass A and pass B tokens by coordinates (greedy nearest within R px); write merged TSV + stats.
import csv, sys, math, os
D=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
R=float(os.environ.get('R','70'))
def load(p):
    with open(p,encoding='utf-8') as f: return list(csv.DictReader(f,delimiter='\t'))
def norm(g):
    g=(g or '').strip().replace('ي','ی').replace('ى','ی').replace('ک','ك').replace('ة','ه').replace('ۀ','ه')
    return g
for sid in sys.argv[1:]:
    A=load(f'{D}/transcription/passA/{sid}.tsv'); B=load(f'{D}/transcription/passB/{sid}.tsv')
    pairs=[]
    for i,a in enumerate(A):
        for j,b in enumerate(B):
            try: d=math.hypot(float(a['x'])-float(b['x']),float(a['y'])-float(b['y']))
            except: continue
            if d<=R: pairs.append((d,i,j))
    pairs.sort(); ua=set(); ub=set(); m=[]
    for d,i,j in pairs:
        if i in ua or j in ub: continue
        ua.add(i); ub.add(j); m.append((i,j))
    out=open(f'{D}/transcription/merged_{sid}.tsv','w',encoding='utf-8')
    out.write('seqA\tseqB\tx\ty\ttype\tnumA\tnumB\tglossA\tglossB\tnum_agree\tgloss_agree\tnoteA\tnoteB\n')
    na=ng=n=0
    for i,j in sorted(m,key=lambda t:int(A[t[0]]['seq'])):
        a,b=A[i],B[j]; n+=1
        nu=a['num']==b['num']; gl=norm(a['gloss'])==norm(b['gloss'])
        na+=nu; ng+=gl
        out.write('\t'.join([a['seq'],b['seq'],a['x'],a['y'],a['type'],a['num'],b['num'],a['gloss'],b['gloss'],str(int(nu)),str(int(gl)),a['note'],b['note']])+'\n')
    for i in sorted(set(range(len(A)))-ua): out.write('\t'.join([A[i]['seq'],'',A[i]['x'],A[i]['y'],A[i]['type'],A[i]['num'],'',A[i]['gloss'],'','0','0',A[i]['note'],'ONLY_A'])+'\n')
    for j in sorted(set(range(len(B)))-ub): out.write('\t'.join(['',B[j]['seq'],B[j]['x'],B[j]['y'],B[j]['type'],'',B[j]['num'],'',B[j]['gloss'],'0','0','ONLY_B',B[j]['note']])+'\n')
    print(sid,'A',len(A),'B',len(B),'matched',n,'num agree',na,'gloss agree',ng,'onlyA',len(A)-n,'onlyB',len(B)-n)
