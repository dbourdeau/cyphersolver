import sys,json
K=json.loads(sys.argv[1])
for l in open('cipher_tokens.txt',encoding='utf8'):
  if not l.startswith('L'): continue
  T=l.split(':',1)[1].split(); U=[];i=0
  while i<len(T):
    if T[i]=='1' and i+1<len(T) and T[i+1]=='2': U.append('12');i+=2
    else: U.append(T[i]);i+=1
  o=''
  for t in U:
    if t=='/': o+=' '
    elif t=='M' and 'M' not in K: o+=o[-1]
    else: o+=K.get(t,'['+t+']')
  print(l[:3],o)
