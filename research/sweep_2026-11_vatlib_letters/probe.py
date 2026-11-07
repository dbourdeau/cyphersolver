import sys,urllib.request,time,json,urllib.error
UA='Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/130.0'
def head(sm):
    r=urllib.request.Request(f'https://digi.vatlib.it/iiif/MSS_{sm}/manifest.json',headers={'User-Agent':UA},method='GET')
    try:
        resp=urllib.request.urlopen(r,timeout=90); d=resp.read(); return (resp.status,len(json.loads(d)['sequences'][0]['canvases']),json.loads(d).get('label','')[:60])
    except urllib.error.HTTPError as e: return e.code
    except Exception as e: return str(e)[:40]
if __name__=='__main__':
    for sm in sys.argv[1:]:
        print(sm,head(sm),flush=True); time.sleep(3)
