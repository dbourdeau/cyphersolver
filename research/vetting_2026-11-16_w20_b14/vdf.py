import json,subprocess,sys,time
dfs=sys.argv[1].split(',')
res={}
for df in dfs:
    u=f"https://www.vestigia.hu/api/search?search={df}"
    r=subprocess.run(['curl','-sL','-A','Mozilla/5.0',u],capture_output=True,text=True,encoding='utf8').stdout
    try: d=json.loads(r)['documents']['data']
    except Exception: print(df,'fail'); continue
    hit=[it for it in d if (it.get('df') or '').replace('DF ','').split('-')[0]==df]
    for it in hit:
        ir=it.get('import_raw') or {}
        res[df]=it
        print(df,it['vestigia_id'],it['date_from'],it['archive_ref'],'|',ir.get('kiadas_helye'),'->',ir.get('cimzettkedvezmenyezett'),'|',ir.get('nyelv'),'|',ir.get('fennmaradasi_forma'),'| pp',ir.get('terjedelem'),'| pub:',ir.get('publikaciok'),'| megj:',(ir.get('megjegyzesek') or '')[:150])
    if not hit: print(df,'nohit')
    time.sleep(1.2)
json.dump(res,open('img/v_dfs.json','w',encoding='utf8'),ensure_ascii=False,indent=0)
