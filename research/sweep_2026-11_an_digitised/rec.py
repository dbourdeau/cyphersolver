import an,json,re,sys,html
store=json.load(open("units.json",encoding="utf8"))
def fetch(i):
    r=store.get(i) or {}
    url=r.get("route") or "https://archivinazionali.cultura.gov.it/it/unita-archivistica/-/ua/view/"+i
    t=an.get(url)
    man=re.findall(r'data-uuid-manifest="([^"]*)"',t)
    txt=re.sub(r'<script.*?</script>|<style.*?</style>','',t,flags=re.S)
    txt=html.unescape(re.sub(r'<[^>]+>',' ',txt)); txt=re.sub(r'\s+',' ',txt)
    return url,man,txt
if __name__=="__main__":
    for i in sys.argv[1:]:
        url,man,txt=fetch(i)
        ms=[m.start() for m in re.finditer(r'(?i)cifr|segret|zifr|chiffr',txt)]
        print("==",i,url,"manifest:",man[:2],len(txt))
        seen=-999
        for s in ms:
            if s-seen>300:
                print("  ...",txt[max(0,s-250):s+350]); seen=s
