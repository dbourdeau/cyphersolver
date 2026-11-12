import collections,re,sys
B=sys.argv[1]
D={}
for l in open(B+'/transcription_fuerstenberg1659_pass1.txt',encoding='utf8'):
  if '\t' in l and not l.startswith('#'):
    a,b=l.strip().split('\t'); D[a]=re.sub(r'[^a-z]','',b)
P=[D['85.1']+D['85.2'],D['85.3']+D['85.4']+D['85.5'],D['85.6']+D['85.7']+D['85.8']+D['85.9']+D['85.10'],D['86.1']+D['86.2'],D['86.3']+D['86.4']+D['86.5']]
pairs=[]
for p in P:
  pr=[p[i:i+2] for i in range(0,len(p)-1,2)]; pairs+=pr
  print(' '.join(pr))
c=collections.Counter(pairs); print(len(pairs),len(c)); print(c.most_common(40))
f=collections.Counter(x[0] for x in pairs); s=collections.Counter(x[1] for x in pairs)
print('first',f.most_common()); print('second',s.most_common())
