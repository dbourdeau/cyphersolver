import fetch,tempfile,os,re,html,sys,json
src,outf=sys.argv[1],sys.argv[2]
ids=list(json.load(open(src,encoding='utf-8')))
res=json.load(open(outf,encoding='utf-8')) if os.path.exists(outf) else {}
for i in ids:
    if i in res: continue
    jar=tempfile.mktemp(); p=os.path.join(fetch.SCR,'d_%s.html'%i)
    fetch.curl(fetch.B+'catalogo/description/'+i,p,jar)
    h=open(p,encoding='utf-8',errors='replace').read()
    t=re.sub(r'<script.*?</script>|<style.*?</style>','',h,flags=re.S); t=html.unescape(re.sub(r'<[^>]+>',' ',t)); t=re.sub(r'\s+',' ',t)
    sig=re.search(r'Signatura: (\S+)',t); k=t.find('Alcance y Contenido'); k2=t.find('Condiciones de Acceso')
    vol=re.search(r'Soporte y Volumen (.*?) Contexto',t)
    res[i]={'sig':sig.group(1) if sig else '', 'vol':vol.group(1) if vol else '', 'desc':t[k:k2][:700] if k>0 else ''}
    json.dump(res,open(outf,'w',encoding='utf-8'),ensure_ascii=False,indent=0)
print('done',len(res))
