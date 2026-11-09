import json,sys,time,urllib.parse,urllib.request
sys.stdout.reconfigure(encoding='utf-8')
B='https://api.deutsche-digitale-bibliothek.de/2/search/index/search/select'
def get(p):
    u=B+'?'+urllib.parse.urlencode(p)
    for i in range(3):
        try: return json.load(urllib.request.urlopen(u,timeout=60))
        except Exception as e: print('retry',e,file=sys.stderr);time.sleep(4)
C='(Chiffre OR Chiffren OR chiffriert* OR Ziffern OR Ziffernschrift OR Geheimschrift OR Zifferschrift OR verschlüsselt* OR Chiffrierung OR cifra OR chiffré* OR Schlüssel)'
NEG=['unentziffert','unentziffert*','"nicht aufgelöst"','"ohne Auflösung"','"ungelöst"','"nicht entschlüsselt"','"nicht entziffert"','unaufgelöst','"ohne Entzifferung"','"ohne Dechiffrierung"','undechiffriert','"nicht dechiffriert"','"nicht aufgeschlüsselt"','"ohne Schlüssel"','"Schlüssel fehlt"','unlesbar','"nicht lesbar"','"nicht gelöst"','"Auflösung fehlt"','"ohne Lösung"','"nicht entzifferbar"','"nicht chiffriert"']
seen={}
out=open('ddb_hits.jsonl','a',encoding='utf-8')
for n in NEG:
    q=f'{n} AND {C}'
    d=get({'q':q,'rows':100,'start':0,'wt':'json','sort':'id asc'})
    r=d['response'];print('##',n,r['numFound'])
    for doc in r['docs']:
        rid=doc['id']
        if rid in seen: continue
        seen[rid]=1
        doc.pop('preview_store',None)
        doc['_neg']=n
        out.write(json.dumps(doc,ensure_ascii=False)+'\n')
        t=doc.get('label') or doc.get('title') or ''
        print('  ',rid[:12],'|',(doc.get('begin_time') or doc.get('time_fct') or ''),'|',(doc.get('provider') or doc.get('provider_fct') or '' ),'|',str(t)[:150])
    time.sleep(1.5)
