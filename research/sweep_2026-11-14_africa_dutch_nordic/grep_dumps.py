"""wide regex over dumped EAD listings: python3 grep_dumps.py dumps/*.jsonl"""
import json,re,sys
R=re.compile(r'cijf|cijff|chif|chiff|ciph|cyph|cifra|geheim|secre[et]|sleutel|\bcode|codes\b|teken|ontcijfer|hiërogl|sign[ae]|vercijfer|onleesbaar',re.I)
for f in sys.argv[1:]:
    seen=set(); n=0; hits=[]
    for l in open(f,encoding='utf8'):
        r=json.loads(l); k=(r.get('id'),r.get('unitid'))
        if k in seen: continue
        seen.add(k); n+=1
        s=json.dumps(r,ensure_ascii=False)
        t=' '.join(str(r.get(x) or '') for x in ('title','scopecontent','physdesc'))
        m=R.findall(re.sub('<[^>]+>','',t))
        if m: hits.append((r.get('id'),r.get('unitid'),r.get('unitdate'),re.sub('<[^>]+>','',str(r.get('title')))[:140],sorted(set(x.lower() for x in m))))
    print('##',f,'unique',n,'hits',len(hits))
    for h in hits[:60]: print('  ',h)
