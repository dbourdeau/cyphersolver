import sys,json,urllib.request,time,os
import pymupdf as fitz
def get(n):
    p=f'dl/fs/{n}.pdf'
    if not os.path.exists(p) or os.path.getsize(p)<2000:
        a=json.load(urllib.request.urlopen(f'http://archive.org/wayback/available?url=lwl.org/westfaelische-geschichte/txt/fs-{n}.pdf',timeout=60))
        s=a.get('archived_snapshots',{}).get('closest')
        if not s: return None
        u=s['url'].replace('/https://','id_/https://',1).replace('http://web.archive.org','https://web.archive.org')
        data=urllib.request.urlopen(u,timeout=120).read(); open(p,'wb').write(data); time.sleep(1)
    return fitz.open(p)
for n in sys.argv[1:]:
    try:
        d=get(n)
        if d is None: print(n,'none'); continue
        t=d[0].get_text().replace('\n',' | ')
        print(n,d.page_count,t[:260])
    except Exception as e: print(n,'ERR',e)
