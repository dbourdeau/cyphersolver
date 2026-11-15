"""PARES show pages -> description text + image count. python desc.py id1 id2 ...  (4 s apart, stop on 429)"""
import subprocess,re,sys,time,os,tempfile,html,json
B='https://pares.cultura.gob.es/ParesBusquedas20/'
HERE=os.path.dirname(os.path.abspath(__file__)); RAW=os.path.join(HERE,'raw')
OUT=os.path.join(HERE,'descs.jsonl')
done={json.loads(l)['id'] for l in open(OUT,encoding='utf8')} if os.path.exists(OUT) else set()
for i in sys.argv[1:]:
    if i in done: continue
    jar=tempfile.mktemp(); sh=os.path.join(RAW,'show_%s.html'%i)
    c=subprocess.run(['curl','-s','-m','40','-A','Mozilla/5.0 (research)','-c',jar,'-b',jar,'-o',sh,'-w','%{http_code}',B+'catalogo/show/'+i],capture_output=True,text=True).stdout
    if c=='429': print('429 STOP'); break
    h=open(sh,encoding='utf-8',errors='replace').read()
    t=re.sub(r'<script.*?</script>|<style.*?</style>','',h,flags=re.S); t=html.unescape(re.sub(r'<[^>]+>',' ',t)); t=re.sub(r'\s+',' ',t)
    k=t.find('Signatura'); m=re.search(r'dbCode=(\d+)',h)
    r={'id':i,'code':c,'db':m.group(1) if m else None,'nimg':len(set(re.findall(r'txt_id_imagen=(\d+)',h))),'text':t[max(0,k-150):k+2200]}
    open(OUT,'a',encoding='utf8').write(json.dumps(r,ensure_ascii=False)+'\n'); print(i,c,r['nimg'],flush=True)
    time.sleep(4)
