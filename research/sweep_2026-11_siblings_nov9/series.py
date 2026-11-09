"""List the children of a PARES series via catalogo/contiene/<id> + displaytag pages. Usage: series.py <seriesid> <out.json>"""
import fetch,tempfile,os,re,html,sys,json
sid,outf=sys.argv[1],sys.argv[2]
jar=tempfile.mktemp()
fetch.curl(fetch.B+'catalogo/description/'+sid,os.path.join(fetch.SCR,'x.html'),jar)
rows={}
def parse(h):
    for m in re.finditer(r'name="sel" value="(\d+)">(.*?)(?=name="sel" value=|</table>|$)',h,flags=re.S):
        t=html.unescape(re.sub(r'<[^>]+>',' ',m.group(2))); t=re.sub(r'\s+',' ',t)
        sig=re.search(r'Signatura:\s*(.*?)(?:$|\s{2,})',t)
        rows[m.group(1)]=t[:400]
p=os.path.join(fetch.SCR,'ct_%s_1.html'%sid)
fetch.curl(fetch.B+'catalogo/contiene/'+sid,p,jar); h=open(p,encoding='utf-8',errors='replace').read()
parse(h); tot=re.search(r'Todos los resultados \((\d+)\)',h); tot=int(tot.group(1)) if tot else 0
print('total',tot)
n=2
while len(rows)<tot and n<60:
    p=os.path.join(fetch.SCR,'ct_%s_%d.html'%(sid,n))
    fetch.curl(fetch.B+'catalogo/SearchController.do?d-2677838-p=%d'%n,p,jar); parse(open(p,encoding='utf-8',errors='replace').read()); n+=1
json.dump(rows,open(outf,'w',encoding='utf-8'),ensure_ascii=False,indent=0)
print(len(rows))
