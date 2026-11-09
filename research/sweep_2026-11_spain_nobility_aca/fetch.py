"""PARES: description text + first N images for given ids. 4 s between requests, stop on 429."""
import subprocess,re,sys,time,os,tempfile,html
B='https://pares.cultura.gob.es/ParesBusquedas20/'
SCR=r'C:\Users\dbour\AppData\Local\Temp\claude\C--Users-dbour-cypher\75de5c3e-f515-4461-8587-8e578d7e5174\scratchpad'
os.makedirs(SCR,exist_ok=True)
def curl(url,out,jar):
    r=subprocess.run(['curl','-s','-m','40','-A','Mozilla/5.0','-c',jar,'-b',jar,'-o',out,'-w','%{http_code}',url],capture_output=True,text=True).stdout
    if r=='429': print('429 STOP'); sys.exit(1)
    time.sleep(4); return r
def run(i,maxn):
    jar=tempfile.mktemp()
    sh=os.path.join(SCR,'show_%s.html'%i)
    print(i,curl(B+'catalogo/show/'+i,sh,jar))
    h=open(sh,encoding='utf-8',errors='replace').read()
    t=re.sub(r'<script.*?</script>|<style.*?</style>','',h,flags=re.S); t=html.unescape(re.sub(r'<[^>]+>',' ',t)); t=re.sub(r'\s+',' ',t)
    k=t.find('Signatura'); print(t[max(0,k-100):k+1800])
    m=re.search(r'dbCode=(\d+)',h); db=m.group(1) if m else None
    n=re.findall(r'txt_id_imagen=(\d+)',h)
    print(' db',db,'imgs',len(set(n)))
    if db:
        for k in range(1,maxn+1):
            u=B+'ViewImage.do?accion=42&txt_descarga=1&dbCode=%s&txt_id_imagen=%d&txt_zoom=10&txt_contraste=0&txt_polarizado=&txt_brillo=10.0&txt_contrast=1.0'%(db,k)
            out=os.path.join(SCR,'%s_%d.jpg'%(i,k)); c=curl(u,out,jar); print(' img',k,c,os.path.getsize(out))
if __name__=='__main__':
    maxn=int(sys.argv[1])
    for i in sys.argv[2:]: run(i,maxn)
