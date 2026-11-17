import sys,json,time,urllib.request,os,re
def kids(pid):
    fn=f'src/kids_{pid}.json'
    if os.path.exists(fn): return json.load(open(fn,encoding='utf8'))
    a=[];seen=set();start=None
    while True:
        u=f'https://discovery.nationalarchives.gov.uk/API/records/v1/children/{pid}?limit=500'+(f'&batchStartRecordId={start}' if start else '')
        r=urllib.request.Request(u,headers={'Accept':'application/json','User-Agent':'Mozilla/5.0'})
        d=json.load(urllib.request.urlopen(r,timeout=60)); time.sleep(1)
        new=[x for x in d['assets'] if x['id'] not in seen]
        for x in new: seen.add(x['id']); a.append(x)
        if not d.get('hasMoreAfterLast') or not new: break
        start=a[-1]['id']
    json.dump(a,open(fn,'w',encoding='utf8'),ensure_ascii=False); print('n',len(a),file=sys.stderr); return a
def txt(x):
    s=(x.get('scopeContent') or {}).get('description') or ''
    return re.sub(r'<[^>]+>',' ',s)
if __name__=='__main__':
    pid=sys.argv[1]; pat=sys.argv[2] if len(sys.argv)>2 else None
    for x in kids(pid):
        t=txt(x)
        if pat is None or re.search(pat,t,re.I):
            print(x['citableReference'],x['id'],x['coveringDates'],'|',re.sub(r'\s+',' ',t)[:400])
