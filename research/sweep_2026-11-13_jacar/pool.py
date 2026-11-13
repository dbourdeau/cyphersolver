import json,glob,re
Z=str.maketrans("０１２３４５６７８９","0123456789")
seen={}
for fn in glob.glob('hits/*.jsonl'):
    for l in open(fn,encoding='utf8'):
        h=json.loads(l); seen[h['id']]=h
def year(h):
    d=h.get('資料作成年月日','')
    m=re.search(r"(明治|大正|昭和)([０-９0-9]+)",d)
    if not m: 
        m2=re.search(r'(\d{4})',d.translate(Z)); return int(m2.group(1)) if m2 else None
    n=int(m.group(2).translate(Z)); return {"明治":1867,"大正":1911,"昭和":1925}[m.group(1)]+n
out=[]
for h in seen.values():
    y=year(h); h['y']=y
    if y and y>1950: continue
    t=h['title']+' '+h.get('内容','')
    t=t.translate(Z)
    if h['id'][:3] in ('A01','A02'): continue
    score=0
    if re.search(r'(?<!\d)\d{4,5}(?!\d)[ 、,]+\d{4,5}[ 、,]+\d{4,5}',t): score+=3
    if re.search(r'解読不能|不明ノ暗号|意味不明|未解読|判読不能ノ暗号|解読出来|不明',t) and '暗号' in t: score+=2
    if re.search(r'露国|ソ連|蘇|露西亜|支那|清国|朝鮮|鮮人|英国|米国|独逸|仏国|伊太利|波斯|土耳古',t): score+=1
    if re.search(r'傍受|押収|差押|入手|密書|写|訳文|検閲',t): score+=1
    if re.search(r'暗号書|暗号表|乱数表|電信暗号法|暗号符号|暗号方式',h['title']) and score<5: score-=2
    if score>=4: out.append((score,h))
out.sort(key=lambda x:-x[0])
print(len(seen),len(out))
for s,h in out: print(s,h['ref'],h['y'],h['title'][:60],'|',h.get('内容','')[:110].replace('\n',' '))
