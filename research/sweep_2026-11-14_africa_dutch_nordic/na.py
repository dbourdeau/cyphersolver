"""Nationaal Archief zvt API: for each term, archive-level hits in Africa-related archives; item-level hits dumped.
usage: na.py term [...]   writes na_<term>.json"""
import json,sys,time,urllib.parse,urllib.request
BASE='https://zvt.nationaalarchief.nl/api/search'
def get(path,**p):
    url=f'{BASE}/{path}?'+urllib.parse.urlencode(p)
    for a in range(4):
        try:
            with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0 (research)'}),timeout=60) as r:
                time.sleep(2.5); return json.load(r)
        except Exception as e:
            print('retry',url,e,file=sys.stderr); time.sleep(4*(a+1))
    return {}
def archives(t):
    out=[];pg=1
    while True:
        d=get('eads',q=t,page=pg,rows=50); r=d.get('results') or []; out+=r
        if pg>=(d.get('pages') or 0) or not r: return out
        pg+=1
def items(ead,t):
    out=[];pg=1
    while True:
        d=get('eads/'+urllib.parse.quote(ead),q=t,page=pg,rows=100); r=d.get('results') or []; out+=r
        if pg>=(d.get('pages') or 0) or not r: return out
        pg+=1
if __name__=='__main__':
    for t in sys.argv[1:]:
        a=archives(t)
        json.dump(a,open(f'na_arch_{t.replace(" ","_")}.json','w'),ensure_ascii=False)
        print(t,len(a),'archives')
