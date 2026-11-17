import requests,sys,json,time,urllib.parse
sys.stdout.reconfigure(encoding='utf-8')
H={'User-Agent':'Mozilla/5.0'}
B='https://cdm21054.contentdm.oclc.org/digital/api/search/collection/%s/searchterm/%s/field/all/mode/all/conn/and/order/nosort/ad/asc/maxRecords/100/page/%d'
def get(u):
    for i in range(4):
        try: return requests.get(u,headers=H,timeout=60).json()
        except Exception: time.sleep(3)
    return {}
def run(coll,term,maxpages=60):
    out={}
    for p in range(1,maxpages+1):
        r=get(B%(coll,urllib.parse.quote(term),p)); its=r.get('items',[])
        if p==1: tot=r.get('totalResults')
        for it in its: out[it['itemId']+'|'+it['collectionAlias']]=it
        if len(its)<100: break
        time.sleep(.4)
    return tot,out
if __name__=='__main__':
    allitems={}
    for coll,term in [('HPBK','1'),('HPBK','Hilmi'),('HPBK','telgraf'),('MHC','şifre'),('MHC','telgraf'),('MHC','1337'),('HTA','şifre'),('ABK','şifre')]:
        tot,o=run(coll,term); print(coll,term,tot,len(o)); allitems.update(o)
    json.dump(allitems,open('hpbk_all.json','w',encoding='utf-8'),ensure_ascii=False)
