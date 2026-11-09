import subprocess,re,sys,html,time,json,urllib.parse
def get(u):
    return subprocess.run(['curl','-s','-m','60','-L','-A','Mozilla/5.0',u],capture_output=True).stdout.decode('utf8','ignore')
def txt(s): return re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]+>',' ',s))).strip()
def search(base,n,term):
    out=[];page=1
    while True:
        u=f"{base}/archive/recherche/transversale/n:{n}?RECH_libre={urllib.parse.quote(term)}"
        if page>1: u=f"{base}/archive/resultats/transversale/n:{n}/page:{page}?RECH_libre={urllib.parse.quote(term)}&type=transversale"
        h=get(u); time.sleep(2.5)
        m=re.search(r'<table id="resultats".*?</table>',h,re.S)
        if not m: break
        rows=re.findall(r'<tr class="(?:pair|impair)">(.*?)</tr>',m.group(0),re.S)
        for r in rows:
            tds=re.findall(r'<td[^>]*>(.*?)</td>',r,re.S)
            link=re.search(r'href="(/archive/fonds/[^"]*)"',r)
            out.append([txt(t) for t in tds[:4]]+[base+link.group(1) if link else ''])
        if 'page:%d'%(page+1) not in h or page>=8: break
        page+=1
    return out
if __name__=='__main__':
    base,n=sys.argv[1],sys.argv[2]
    res={}
    for t in sys.argv[3:]:
        r=search(base,n,t); res[t]=r
        print(t,len(r))
        for x in r[:40]: print('  ',x[:4])
    json.dump(res,open('lig_'+re.sub(r'\W','_',base)+'.json','w'),ensure_ascii=False)
