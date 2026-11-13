# build_check.py rows_dir out.json : merge one-row JSON files into candidates.json and check them against the
# vetting gate as summarised in b169 VETTING_RULES.md (own re-implementation; no repo script run)
import json,sys,glob,datetime
REQ=['year','date','title','correspondents','place','language','region','period','shelfmark','folio_note','cls','status','why','importance','solvability','difficulty','score_note','verify','links','seen','source','prior_art','needs_archive_scan','access_note']
REG="England, France, Italy, Spain, Portugal, Low Countries, Central Europe, Germany, Scandinavia, Poland-Lithuania, Papacy, Americas, Other".split(', ')
PER="15th century, 1497-1559, 1560-1589, 1589-1598, 1598-1610, 1611-1650, 1651-1700, 1701-1800, 1801-1900, 1901-1950, unknown".split(', ')
ok=lambda v:isinstance(v,str) and len(v.strip())>=12
rows=[json.load(open(f)) for f in sorted(glob.glob(sys.argv[1]+'/*.json'))]
bad=0; texts={}
for i,e in enumerate(rows):
    p=[k for k in REQ if k not in e]
    if 'id' in e: p.append('has id')
    if e.get('region') not in REG: p.append('region')
    if e.get('period') not in PER: p.append('period')
    if e.get('cls') not in ('A','B','C'): p.append('cls')
    for k in ('importance','solvability','difficulty'):
        if not isinstance(e.get(k),int) or not 1<=e[k]<=5: p.append(k)
    if not isinstance(e.get('year'),int): p.append('year')
    v=e.get('vetting',{})
    try: datetime.date.fromisoformat(v.get('date',''))
    except Exception: p.append('v.date')
    s=v.get('seen',{})
    if s.get('kind') not in ('scan','facsimile','transcription','not online'): p.append('seen.kind')
    p+=['seen.'+k for k in ('where','extent','cipher') if not ok(s.get(k))]
    p+=['pa.'+k for k in ('decode','tomokiyo','lasry','edition','literature') if not ok(v.get('prior_art',{}).get(k))]
    p+=[k for k in ('key_check','duplicates','by') if not ok(v.get(k))]
    if v.get('verdict')!='open': p.append('verdict')
    if len(v.get('searches') or [])<3: p.append('searches<3')
    for k in ('decode','tomokiyo','lasry','edition','literature'):
        texts.setdefault((k,v.get('prior_art',{}).get(k)),[]).append(i)
    for l in e['links']:
        if not l['href'].startswith('https://'): p.append('link')
    print(i,e['cls'],'OK' if not p else p,e['title'][:80]); bad+=bool(p)
dup=[(k[0],ix) for k,ix in texts.items() if len(ix)>1]
print('rows',len(rows),'identical prior_art texts across rows:',dup)
print('result:','pass' if not bad and not dup else 'fail')
json.dump(rows,open(sys.argv[2],'w'),ensure_ascii=False,indent=1)
