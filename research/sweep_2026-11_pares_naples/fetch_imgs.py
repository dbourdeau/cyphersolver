"""Fetch PARES page images (zoom 10) for the Naples/Sicily viceroy items. One record at a time, fresh cookie jar, 4 s pause."""
import subprocess,re,sys,time,os,tempfile
B='https://pares.cultura.gob.es/ParesBusquedas20/'
ids={'3641220':2,'3641224':2}
os.makedirs('img',exist_ok=True)
def curl(url,out,jar):
    return subprocess.run(['curl','-s','-m','40','-A','Mozilla/5.0','-c',jar,'-b',jar,'-o',out,'-w','%{http_code}',url],capture_output=True,text=True).stdout
for i,n in ids.items():
    jar=tempfile.mktemp(); 
    curl(B+'catalogo/show/'+i,'show_%s.html'%i,jar)
    h=open('show_%s.html'%i,encoding='utf-8',errors='replace').read()
    m=re.search(r'dbCode=(\d+)',h); db=m.group(1) if m else None
    print(i,'dbCode',db,flush=True)
    if not db: continue
    for k in range(1,n+1):
        u=B+'ViewImage.do?accion=42&txt_descarga=1&dbCode=%s&txt_id_imagen=%d&txt_zoom=10&txt_contraste=0&txt_polarizado=&txt_brillo=10.0&txt_contrast=1.0'%(db,k)
        c=curl(u,'img/%s_%d.jpg'%(i,k),jar); print(' ',k,c,os.path.getsize('img/%s_%d.jpg'%(i,k)),flush=True); time.sleep(4)
    time.sleep(4)
