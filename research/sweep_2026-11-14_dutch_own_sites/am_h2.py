import am_search as a, json, time, re
rows={}
for t in ['chijffer*','chyffer*','ciffer*','cifer*','cijfferschrift*','cyfferschrift','geheymschrift*','geheime? brieven','"in cijffer"','"in cyffer"','gedecijfferd','ontcijffer*','ontcyffer*','gecijffert','chiffer*','chifre*','zifra','cifra','sleutel*']:
    for ty in ['File','Series','Fonds']:
        page=1
        while page<=3:
            d=a.q(t,ty,page=page,per=100)
            for r in d['rows']:
                s=((r['data'].get('date') or {}).get('start') or '')[:4]
                if s and s>'1900': continue
                rows[r['id']]=dict(t=t,title=r['title'][:300],date=s,par=(r['data']['parents'][0]['title'][:60] if r['data']['parents'] else ''),media=bool(r.get('media')))
            if page*100>=d['total']: break
            page+=1; time.sleep(.3)
    print(t,len(rows),flush=True)
json.dump(rows,open('am_hits2.json','w',encoding='utf8'),ensure_ascii=False)
rx=re.compile(r'chijffer|chyffer|cijffer|cyffer|ciffer|cifer|ontcijffer|ontcyffer|chiffer|chifre|zifra|cifra|geheym|geheime? brieven|sleutel',re.I)
for k,v in rows.items():
    if v['t']!='sleutel*' and rx.search(v['title']) or (v['t']=='sleutel*' and re.search(r'sleutel.*(cijf|cyf|chif|geheim|code)|(cijf|cyf|chif|geheim|code).*sleutel',v['title'],re.I)):
        print(v['date'],'|',v['title'][:200],'|',v['par'],'|',v['media'])
