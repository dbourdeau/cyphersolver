import re,sys,collections,math
B=sys.argv[1]
D={}
for l in open(B+'/transcription_fuerstenberg1659_pass1.txt',encoding='utf8'):
  if '\t' in l and not l.startswith('#'):
    a,b=l.strip().split('\t'); D[a]=re.sub(r'[^a-z]','',b)
P=[D['85.1']+D['85.2'],D['85.3']+D['85.4']+D['85.5'],D['85.6']+D['85.7']+D['85.8']+D['85.9']+D['85.10'],D['86.1']+D['86.2'],D['86.3']+D['86.4']+D['86.5']]
G=dict(zip('abcdefghijklmnopqrstuvwxyz',[6.5,1.9,3.0,5.1,17.4,1.7,3.0,4.8,7.6,0.3,1.2,3.4,2.5,9.8,2.5,0.8,0.02,7.0,7.3,6.2,4.4,0.7,1.9,0.03,0.04,1.1]))
for alpha in ['abcdefghijklmnopqrstuvwxyz','abcdefghiklmnopqrstuwxyz','abcdefghiklmnopqrstuxyz']:
  n=len(alpha)
  for col in (0,1):
    s=''.join(p[col::2] for p in P)
    c=collections.Counter(s)
    res=[]
    for k in range(n):
      sc=sum(c[ch]*math.log(G.get(alpha[(alpha.index(ch)-k)%n],0.01)+0.01) for ch in s if ch in alpha)
      res.append((round(sc,1),k))
    res.sort(reverse=True); print(n,col,res[:3])
