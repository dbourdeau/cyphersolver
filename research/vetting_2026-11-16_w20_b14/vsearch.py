import json,subprocess,sys,time,urllib.parse
q=sys.argv[1]; out=sys.argv[2]
allr=[]
for page in range(1,20):
    u=f"https://www.vestigia.hu/api/search?search={urllib.parse.quote(q)}&page={page}"
    r=subprocess.run(['curl','-sL','-A','Mozilla/5.0',u],capture_output=True,text=True,encoding='utf8').stdout
    try: d=json.loads(r)['documents']
    except Exception as e:
        print('fail',page,r[:200]); break
    allr+=d['data']
    if page>=d.get('last_page',1): break
    time.sleep(1.5)
json.dump(allr,open(out,'w',encoding='utf8'),ensure_ascii=False,indent=0)
print(len(allr))
