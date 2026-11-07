import sys,re,json,time,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from opac import get, clean
ids=json.load(open(sys.argv[1],encoding='utf8'))
done=set()
if os.path.exists('itemdet.jsonl'):
    done={json.loads(l)['id'] for l in open('itemdet.jsonl',encoding='utf8')}
out=open('itemdet.jsonl','a',encoding='utf-8')
for i,(sm,t) in ids.items():
    if i in done: continue
    h=get('https://opac.vatlib.it/mss/detail/'+i); time.sleep(1.0)
    h=re.sub(r'<script.*?</script>','',h,flags=re.S)
    s=clean(h)
    a=s.find('General Information'); b=s.find('Back to Top')
    out.write(json.dumps({'id':i,'sm':sm,'text':s[a:b]},ensure_ascii=False)+'\n'); out.flush()
print('done')
