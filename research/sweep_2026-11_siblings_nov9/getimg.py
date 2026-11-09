"""getimg.py <pares id> <dbCode> n1 n2 ... : download page images (zoom 10), 4 s apart, stop on 429"""
import sys, os, tempfile
import fetch
i, db = sys.argv[1], sys.argv[2]
jar = tempfile.mktemp()
fetch.curl(fetch.B + 'catalogo/show/' + i, os.path.join(fetch.SCR, 'show_%s.html' % i), jar)
for k in map(int, sys.argv[3:]):
    out = os.path.join(fetch.SCR, '%s_%d.jpg' % (i, k))
    if os.path.exists(out) and os.path.getsize(out) > 5000: continue
    u = fetch.B + 'ViewImage.do?accion=42&txt_descarga=1&dbCode=%s&txt_id_imagen=%d&txt_zoom=10&txt_contraste=0&txt_polarizado=&txt_brillo=10.0&txt_contrast=1.0' % (db, k)
    print(k, fetch.curl(u, out, jar), os.path.getsize(out))
