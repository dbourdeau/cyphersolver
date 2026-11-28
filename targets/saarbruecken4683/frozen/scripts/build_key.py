# Construit K selon PREREG (majorité par nombre ; égalité -> '?'; codes >=200 -> mot de glose)
import sys, os, re, json, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from norm import norm
A=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','apprentissage')
votes=collections.defaultdict(collections.Counter); codes=collections.defaultdict(collections.Counter)
stats=collections.Counter()
for f in ['T1.tsv','T2.tsv','T3.tsv','T4.tsv']:
    for line in open(os.path.join(A,f),encoding='utf-8'):
        c=line.rstrip('\n').split('\t')
        if len(c)<4 or not re.match(r'^\d',c[1].strip() or 'x'): continue
        fol,nums,gl,typ=c[0],c[1].split(),c[2],c[3].strip().upper()
        if re.match(r'29[6-8]',fol): stats['exclu_test']+=1; continue
        if '?' in gl: stats['glose_douteuse']+=1; continue
        if typ=='C' or (len(nums)==1 and nums[0].rstrip('?').isdigit() and int(nums[0].rstrip('?'))>=200):
            if len(nums)==1 and '?' not in nums[0] and int(nums[0])>=200:
                codes[int(nums[0])][norm(gl)]+=1; stats['codes']+=1
            continue
        g=norm(gl)
        if len(nums)!=len(g): stats['longueur_differente']+=1; continue
        for n,ch in zip(nums,g):
            if '?' in n or not n.isdigit(): stats['nombre_douteux']+=1; continue
            n=int(n)
            if n>=200: stats['code_dans_groupe']+=1; continue
            votes[n][ch]+=1; stats['paires']+=1
K={}
for n,c in sorted(votes.items()):
    mc=c.most_common()
    K[n]= '?' if len(mc)>1 and mc[0][1]==mc[1][1] else mc[0][0]
C={}
for n,c in sorted(codes.items()):
    mc=c.most_common(); C[n]='?' if len(mc)>1 and mc[0][1]==mc[1][1] else mc[0][0]
json.dump({'lettres':{str(k):v for k,v in K.items()},'codes':{str(k):v for k,v in C.items()},
           'votes':{str(k):dict(v) for k,v in sorted(votes.items())},'stats':dict(stats)},
          open(os.path.join(A,'..','CLE-K.json'),'w'),ensure_ascii=False,indent=1)
print(dict(stats)); print('nombres couverts',len(K),'codes',len(C))
