import json,unicodedata,sys
t=open(sys.argv[1]).read().strip().replace('(*)','*')
s=[c for c in t if not c.isspace()]
print('len',len(s))
def base(c): return unicodedata.normalize('NFD',c)[0].lower()
gl=json.load(open(__import__('os').path.join(__import__('os').path.dirname(__import__('os').path.abspath(__file__)),'..','tests','test1','key_full.json')))['key']
mis=sorted((int(k),v,s[int(k)-1] if int(k)<=len(s) else None) for k,v in gl.items() if int(k)>len(s) or base(s[int(k)-1])!=v.lower())
print(len(gl),'glossed; mismatches',len(mis)); print(mis[:40])
ends=[57,114,168,223,278,335,394,445,499,555,612,666,682]
for e in ends: print(e, ''.join(s[max(0,e-10):e]),'|',''.join(s[e:e+3]))
