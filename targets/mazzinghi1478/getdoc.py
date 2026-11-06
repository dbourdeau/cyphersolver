# usage: getdoc.py FILZA DOC [DOC...] -> native-size images of MAP docs into img/
import re,sys,os,urllib.request,time
UA={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36'}
B='https://archiviodistatofirenze.cultura.gov.it'
D=os.path.dirname(os.path.abspath(__file__))
def get(u):
    for k in range(3):
        try: return urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=90).read()
        except Exception as e: err=e; time.sleep(3)
    raise err
f=sys.argv[1]
cache=f'{D}/pages/f{f}.html'
if os.path.exists(cache): t=open(cache,encoding='utf8').read()
else:
    t=get(f'{B}/map/ricerca/ricerca-su-filza/?f={f}&d={sys.argv[2]}&c=').decode('utf8','replace'); open(cache,'w',encoding='utf8').write(t)
items=re.findall(r'<li id="rip_(\d+)"[^>]*><a [^>]*>([^<]+?)\s*<i',t)
img=re.findall(r'"image":"([^"]+)"',t)[0]; cur=re.findall(r'class="slim-current"><a href="[^"]*id=(\d+)',t)[0]
pos=int(re.findall(r'</span> <span>(\d+)</span> di',t)[0])
base=int(cur)-pos+1; dirp=img.rsplit('/',1)[0]
for d in sys.argv[2:]:
    sel=[(i,l) for i,l in items if re.match(rf'doc\. {d}\b',l)]
    for i,l in sel:
        n=int(i)-base+1; p=f'{dirp}/A{n:07d}.ptif'
        url=f'{B}/iipsrv/iipsrv.fcgi?IIIF={p}/full/full/0/default.jpg'
        fn=f'{D}/img/f{f}_{l.replace("doc. ","d").replace(" ","_").replace(",","")}.jpg'
        if not os.path.exists(fn): open(fn,'wb').write(get(url)); time.sleep(1)
        print(i,l,'|',url,'|',os.path.basename(fn))
print('items in filza',len(items))
