import json,subprocess,sys,time
out={}
for df in sys.argv[1].split(','):
    for suf in ['-a','-1','-b']:
        q=df+suf
        r=subprocess.run(['curl','-sL','-A','Mozilla/5.0','https://www.vestigia.hu/api/search?search='+q],capture_output=True,text=True,encoding='utf8').stdout
        try: d=json.loads(r)['documents']['data']
        except Exception: print(q,'fail'); continue
        hit=[it for it in d if (it.get('df') or '').replace('DF ','')==q]
        for it in hit:
            ir=it.get('import_raw') or {}
            out[q]=it
            print(q,it['vestigia_id'],it['date_from'],it['archive_ref'],'|',ir.get('fennmaradasi_forma'),'|',ir.get('nyelv'),'| pp',ir.get('terjedelem'),'|',ir.get('megjegyzesek'),'|',(ir.get('eleje') or '')[:80])
        time.sleep(1.1)
json.dump(out,open('img/v_sub.json','w',encoding='utf8'),ensure_ascii=False,indent=0)
