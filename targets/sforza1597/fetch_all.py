import json,os,re,sys,time
sys.path.insert(0,'C:/Users/dbour/cypher/research/venice_milan_decode')
import api
T='C:/Users/dbour/cypher/targets/sforza1597/'
ks=json.load(open(T+'list1597.json'))
os.makedirs(T+'rec',exist_ok=True); os.makedirs(T+'pdf',exist_ok=True)
for r in sorted(ks,key=lambda r:int(r['id'])):
    i=r['id']; hp=T+f'rec/{i}.htm'
    if not os.path.exists(hp):
        open(hp,'w',encoding='utf-8').write(api.get(api.BASE+'RecordsView/'+i)); time.sleep(0.4)
    h=open(hp,encoding='utf-8').read()
    names=sorted(set(re.findall(r'(?<![A-Z]_)IMG_R%s_I\d+_P\d*\.pdf'%i,h)))
    if not names: names=sorted(set(re.findall(r'IMG_R%s_I\d+_P\d*\.(?:png|jpg)'%i,h)))
    for n in names:
        fp=T+'pdf/'+n
        if os.path.exists(fp): continue
        try:
            b=api.op.open(api.urllib.request.Request('https://de-crypt.org/decrypt-custom/filesrv/?file='+n,headers={'User-Agent':api.UA,'Cookie':api.cookie()}),timeout=120).read()
            open(fp,'wb').write(b)
        except Exception as e: print('ERR',n,e)
        time.sleep(0.4)
    print(i,r['record_type'],names,flush=True)
