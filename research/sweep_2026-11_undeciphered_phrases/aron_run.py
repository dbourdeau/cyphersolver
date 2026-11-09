import sys,json,time
sys.path.insert(0,'../sweep_2026-11_czech_slovak')
import aron
bases=['https://www.mza.cz/aron','https://aron.soaplzen.cz','https://aron.vychodoceskearchivy.cz','https://aron.soapraha.cz','https://portal.nacr.cz/aron']
terms=sys.argv[1:]
out=open('aron_hits.jsonl','a',encoding='utf-8')
for b in bases:
    for t in terms:
        try:
            j=aron.search(b,t,50,0)
        except Exception as e:
            print(b,t,'ERR',str(e)[:80]);time.sleep(3);continue
        print(b,t,j['count'])
        for i in j['items']:
            out.write(json.dumps({'base':b,'term':t,'id':i['id'],'name':i.get('name'),'desc':(i.get('description') or '')[:500]},ensure_ascii=False)+'\n')
            if j['count']<=12: print('   ',i['id'][:8],(i.get('name') or '')[:110],'|',(i.get('description') or '')[:150])
        out.flush();time.sleep(2.5)
