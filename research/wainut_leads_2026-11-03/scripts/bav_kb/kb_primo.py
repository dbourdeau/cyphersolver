import fetch,json,sys,urllib.parse as u
S="out"  # raw hit files; not kept in the repo
def q(term,offset=0):
    url=("https://soeg.kb.dk/primaws/rest/pub/pnxs?blendFacetsSeparately=false&disableCache=false&getMore=0&inst=45KBDK_KGL&lang=da"
         f"&limit=50&newspapersActive=false&offset={offset}&pcAvailability=false&q=any,contains,{u.quote(term)}&qExclude=&qInclude=facet_rtype,exact,manuscripts&rapido=false"
         "&refEntryActive=false&rtaLinks=true&scope=MyInstitution&skipDelivery=Y&sort=rank&tab=LibraryCatalog&vid=45KBDK_KGL:KGL")
    s,b=fetch.get(url,"application/json")
    return s,(json.loads(b) if s==200 else {"err":b[:300]})
out={}
for t in sys.argv[1:]:
    s,d=q(t)
    if s!=200: print('##',t,s,d); continue
    n=d['info']['total']; print('##',t,n)
    docs=d['docs']
    off=50
    while off<min(n,200):
        s2,d2=q(t,off); docs+=d2.get('docs',[]); off+=50
    for x in docs:
        p=x['pnx']; disp=p.get('display',{}); ctl=p.get('control',{})
        rid=ctl.get('recordid',[''])[0]
        rec={'title':disp.get('title',[''])[0],'type':disp.get('type',[''])[0],'date':disp.get('creationdate',[''])[0],'desc':' | '.join(disp.get('description',[]))[:500],'creator':'; '.join(disp.get('creator',[])+disp.get('contributor',[]))[:200],'subject':'; '.join(disp.get('subject',[]))[:200],'id':rid,'term':t}
        out[rid]=rec
        print('  -',rec['type'],'|',rec['date'],'|',rec['title'][:90],'|',rec['id'])
json.dump(out,open(f"{S}/kb_primo_{'_'.join(a[:6] for a in sys.argv[1:3])}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
