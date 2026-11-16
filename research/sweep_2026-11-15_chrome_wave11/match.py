import json, re, sys, glob
sys.stdout.reconfigure(encoding='utf8')
E=[]
for p in glob.glob('csp2_*.json'): E+=json.load(open(p,encoding='utf8'))['entries']
def nums(s):
    out=set()
    for a,b in re.findall(r'(\d+)\s*-\s*(\d+)',s):
        a,b=int(a),int(b)
        if 0<b-a<30: out|=set(range(a,b+1))
    out|={int(x) for x in re.findall(r'\d+',s)}
    return out
idx={}
for e in E: idx.setdefault(e['vol'],[]).append((nums(e['fol']),e))
L=json.load(open('../../research/leads.json',encoding='utf8')); L=L if isinstance(L,list) else L['leads']
res={}
for lid in [2867,2868,2869,2870,2871,2872,2873,2874,2875]:
    ld=[x for x in L if x['id']==lid][0]
    fn=ld['folio_note']
    items=re.findall(r'(\d{4}-\d\d-\d\d) (A-\d+) f\.([\d\-+, ]+)',fn)
    tot=0;hit=0;dec=0;rows=[]
    for date,vol,fol in items:
        v=int(vol[2:]); ns=nums(fol.replace('+',','))
        m=[e for s,e in idx.get(v,[]) if s&ns]
        tot+=1
        if m:
            hit+=1
            d=any(e['deciph'] for e in m)
            dec+=d
            rows.append((date,vol,fol,'CAL',('DECIPH' if d else 'cipher-only'),m[0]['page'],m[0]['tail'][-200:] if d else ''))
        else: rows.append((date,vol,fol,'nocal','',''))
    res[lid]=rows
    print(lid,'unfiled',tot,'in calendar',hit,'with deciphering',dec)
json.dump(res,open('match_result.json','w',encoding='utf8'),ensure_ascii=False,indent=1)
