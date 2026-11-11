"""Abhilekh Patal item pages -> ap_details.jsonl (public metadata block; notes whether a preview/thumbnail is offered).
usage: python ap_details.py <itemId> ..."""
import sys, json, re, html, time, os
import ap
done=set()
if os.path.exists('ap_details.jsonl'):
    done={json.loads(l)['itemId'] for l in open('ap_details.jsonl')}
f=open('ap_details.jsonl','a',encoding='utf8')
for iid in sys.argv[1:]:
    if iid in done: continue
    t=ap.get('https://www.abhilekh-patal.in/Category/ItemDetails/ItemDetails?itemId='+iid)
    raw=re.sub(r'data:image[^"]+','',t)
    x=html.unescape(raw)
    x=re.sub(r'<script.*?</script>|<style.*?</style>','',x,flags=re.S)
    x=re.sub(r'<[^>]+>',' ',x); x=re.sub(r'\s+',' ',x)
    m=re.search(r'detailed feedback survey Yes No (.*?) Held by:',x)
    d={'itemId':iid,'meta':m.group(1) if m else x[:1500],
       'readcontent_login': 'ReadContent' in raw, 'has_inline_image': 'data:image' in t and len(t)-len(raw)>20000,
       'abstract': bool(re.search(r'(?i)abstract|description',m.group(1) if m else ''))}
    f.write(json.dumps(d,ensure_ascii=False)+'\n'); f.flush()
    print(iid,d['meta'][:700],d['readcontent_login'],d['has_inline_image'],len(t),flush=True)
    time.sleep(5)
