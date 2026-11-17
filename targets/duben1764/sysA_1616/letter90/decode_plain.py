import json,re,sys
k={a:(b[0] if b else '') for a,b in json.load(open(sys.argv[1])).items()}
for l in open(sys.argv[2]):
  if l.startswith('#') or not l.strip(): continue
  lab,_,b=l.strip().partition(' ')
  out=[]
  for g in re.split(r'[.|\s]+',b):
    g=re.sub(r'[^0-9]','',g)
    if not g: continue
    if int(g)<100: continue
    v=k.get(str(int(g)))
    out.append(v if v else '<'+g+'>')
  print(lab,' '.join(out))
