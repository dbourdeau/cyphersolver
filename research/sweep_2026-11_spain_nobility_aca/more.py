import fetch,tempfile,os,sys
i,db=sys.argv[1],sys.argv[2]
jar=tempfile.mktemp(); fetch.curl(fetch.B+'catalogo/show/'+i,os.path.join(fetch.SCR,'x.html'),jar)
for k in map(int,sys.argv[3:]):
    u=fetch.B+'ViewImage.do?accion=42&txt_descarga=1&dbCode=%s&txt_id_imagen=%d&txt_zoom=10&txt_contraste=0&txt_polarizado=&txt_brillo=10.0&txt_contrast=1.0'%(db,k)
    out=os.path.join(fetch.SCR,'%s_%d.jpg'%(i,k)); print(fetch.curl(u,out,jar),k,os.path.getsize(out),flush=True)
