import csv,glob,json,re,sys
sys.stdout.reconfigure(encoding='utf8')
rows={}
for r in json.load(open('../sweep_2026-11-15_chrome_wave10/badator_rows.json',encoding='utf8')):
    rows[(r['date'].strip(),r['sig'].strip(),r['desc'][:60])]=(r['date'],r['sig'],r['desc'])
for p in sorted(glob.glob('csv/*.csv')):
    for x in csv.DictReader(open(p,encoding='utf-8-sig'),delimiter=';'):
        if 'Salazar y Castro' in x['Fondo']:
            d=x['Título/Descripción'].replace('\n',' | ')
            rows.setdefault((x['Fecha'].strip(),x['Signatura'].strip(),d[:60]),(x['Fecha'],x['Signatura'],d))
def vol(s):
    m=re.match(r'(A-\d+)',s); return m.group(1) if m else 'App' if s.startswith('Ap') else '?'
def fol(s):
    m=re.search(r'f[ºo°]\s*([0-9][0-9 ,ayv\.]*)',s); return (m.group(1).strip(' .,').replace(' a ','-').replace(' y ','+') if m else '?')
POS=re.compile(r'descifrad[oa]s?\s+(al margen|entre|a continuaci|en el f|en otro)|descifrados?,? en|descifrado a continuaci|con el texto descifrado|texto descifrado en|nº \d+|n[uú]mero',re.I)
M=[r for r in rows.values() if re.search(r'Mar[ií]n, abad de N',r[2])]
comp={(r[0][:10],vol(r[1])) for r in M if re.match(r'\s*(Texto\s+descifrado|Traducci|Descifrado)',r[2],re.I)}
let=[r for r in M if not re.match(r'\s*(Texto\s+descifrado|Traducci|Descifrado)',r[2],re.I) and re.search(r'cifra|cifrad',r[2],re.I)]
unf=[]
for r in let:
    d=r[2]; own=bool(re.search(r'descifrad|traducci',d,re.I)) and not re.search(r'sin que|no consta|no figura',d,re.I)
    dup=bool(re.match(r'\s*Ejemplar (duplicado|triplicado)',d))
    k=(r[0][:10],vol(r[1]))
    if own or k in comp: continue
    unf.append((r[0][:10],vol(r[1]),fol(r[1]),'dup' if dup else '',re.search(r'\| ([^|]*cifr[^|]*)$',d).group(1)[:60] if re.search(r'\| ([^|]*cifr[^|]*)$',d) else ''))
print(len(M),len(let),len(unf))
for u in sorted(unf): print(u)
json.dump(sorted(unf),open('marin_unfiled.json','w',encoding='utf8'),ensure_ascii=False)
