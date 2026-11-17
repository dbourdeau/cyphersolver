import csv, json, glob, re, sys
sys.stdout.reconfigure(encoding='utf8')
old=json.load(open('../sweep_2026-11-15_chrome_wave10/badator_rows.json',encoding='utf8'))
seen={(r['sig'].strip(),r['date'].strip()) for r in old}
allrows={}
for p in sorted(glob.glob('csv/*.csv')):
    rows=list(csv.DictReader(open(p,encoding='utf-8-sig'),delimiter=';'))
    new=0;sal=0
    for x in rows:
        k=(x['Signatura'].strip(),x['Fecha'].strip())
        isSal='Salazar y Castro' in x['Fondo']
        sal+=isSal
        if k in seen: continue
        if (p,k) in allrows: continue
        allrows[k]=dict(src=p,fondo=x['Fondo'],arch=x['Archivo'],**{a:x[a] for a in ('Fecha','Signatura','Título/Descripción','Tipo')})
        new+=1
    print(p,len(rows),'salazar',sal,'new vs wave10',new)
json.dump(list(allrows.values()),open('newrows.json','w',encoding='utf8'),ensure_ascii=False,indent=0)
sal=[v for v in allrows.values() if 'Salazar y Castro' in v['fondo']]
print('new Salazar rows',len(sal))
for v in sal[:400]:
    d=v['Título/Descripción'].replace('\n',' | ')
    print(v['Fecha'][:11],'|',v['Signatura'][:28],'|',d[:200])
