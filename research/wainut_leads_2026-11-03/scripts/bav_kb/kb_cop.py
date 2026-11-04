import fetch,re,html,sys,json,urllib.parse as u
BASE="https://www.kb.dk/cop/syndication/{coll}/?query={q}&format=rss&itemsPerPage=100"
def search(coll,q):
    s,b=fetch.get(BASE.format(coll=coll,q=u.quote(q)))
    tot=re.search(r'totalResults[^>]*>(\d+)<',b)
    items=[]
    for it in re.findall(r'<item>(.*?)</item>',b,re.S):
        t=re.search(r'<title>(.*?)</title>',it,re.S); l=re.search(r'<link>(.*?)</link>',it,re.S)
        d=re.search(r'<description>(.*?)</description>',it,re.S)
        items.append({'title':html.unescape(t.group(1)).strip() if t else '', 'link':l.group(1).strip() if l else '', 'desc':re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]+>',' ',html.unescape(d.group(1))))).strip()[:400] if d else ''})
    return s,int(tot.group(1)) if tot else None,items
if __name__=="__main__":
    coll=sys.argv[1]
    for q in sys.argv[2:]:
        s,n,its=search(coll,q); print('##',coll,q,s,n)
        for i in its[:100]: print('  -',i['title'][:100],'|',i['link'],'|',i['desc'][:200])
