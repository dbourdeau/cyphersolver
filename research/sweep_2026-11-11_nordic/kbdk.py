import requests,json,time,sys
H={'User-Agent':'Mozilla/5.0'}
URL='https://soeg.kb.dk/primaws/rest/pub/pnxs'
def run(q,scope='MyInst_and_CI',tab='Everything',limit=50,maxn=500):
    out=[];off=0
    while off<maxn:
        p=dict(blendFacetsSeparately='false',disableCache='false',getMore='0',inst='45KBDK_KGL',lang='da',limit=limit,newspapersActive='false',newspapersSearch='false',offset=off,pcAvailability='false',q='any,contains,'+q,qExclude='',qInclude='',rapido='false',refEntryActive='false',rtaLinks='true',scope=scope,skipDelivery='Y',sort='rank',tab=tab,**{'vid':'45KBDK_KGL:KGL'})
        r=requests.get(URL,params=p,headers=H,timeout=60)
        try:j=r.json()
        except Exception: print('err',r.status_code,r.text[:200]);break
        docs=j.get('docs',[])
        for d in docs:
            px=d['pnx']
            g=lambda a,b:(px.get(a,{}).get(b) or [''])
            out.append(dict(id=px['control']['recordid'][0],title=g('display','title')[0],date=g('display','creationdate')[0],type=g('display','type')[0],creator=g('display','creator')[0],source=g('display','source')[0] if px.get('display',{}).get('source') else '',desc=g('display','description')[0][:300],ispartof=g('display','ispartof')[0],lds=g('display','lds01')[0] if px.get('display',{}).get('lds01') else ''))
        tot=j['info']['totalResultsLocal'] if scope!='MyInst_and_CI' else j['info']['total']
        off+=limit
        time.sleep(2.5)
        if not docs or off>=j['info']['total']:break
    return out
if __name__=='__main__':
    q=sys.argv[1];scope=sys.argv[2] if len(sys.argv)>2 else 'MyInst_and_CI'
    o=run(q,scope)
    print(len(o))
    for x in o: print(x['id'],x['type'],x['date'],'|',x['title'][:80],'|',x['creator'][:30],'|',x['desc'][:100].replace('\n',' '))
