import sys,json,time,urllib.request,os
os.makedirs('src',exist_ok=True)
def get(id):
    fn=f'src/{id}.json'
    if os.path.exists(fn): return json.load(open(fn,encoding='utf8'))
    r=urllib.request.Request(f'https://discovery.nationalarchives.gov.uk/API/records/v1/details/{id}',headers={'Accept':'application/json','User-Agent':'Mozilla/5.0'})
    d=json.load(urllib.request.urlopen(r,timeout=30)); time.sleep(1)
    json.dump(d,open(fn,'w',encoding='utf8'),ensure_ascii=False); return d
def show(id):
    d=get(id)
    print(id,d.get('citableReference'),d.get('coveringDates'),'dig=',d.get('digitised'))
    for k in ('scopeContent','note','physicalDescription','arrangement'):
        v=d.get(k)
        if isinstance(v,dict): v=v.get('description')
        if v: print(' ',k,':',str(v)[:1500])
    return d
if __name__=='__main__':
    for a in sys.argv[1:]: show(a)
