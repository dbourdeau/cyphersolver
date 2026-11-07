import openpyxl,re,collections,json,sys
d="data/"
wb=openpyxl.load_workbook(d+"Repertoire2_ChiffreNouveau.xlsx",read_only=True,data_only=True)
r2=collections.defaultdict(list)
for r in wb.worksheets[0].iter_rows(values_only=True):
    try: k=int(str(r[0]).strip())
    except: continue
    if r[1] is not None: r2[k].append(str(r[1]).strip())
wb=openpyxl.load_workbook(d+"Dossiers individuels/701218 - Message Chaudordy_ADECHIFFRER/Texte_Chaudordy.xlsx",read_only=True,data_only=True)
rows=[]
for r in wb.worksheets[0].iter_rows(values_only=True):
    row=[str(v).strip() for v in r if v is not None]
    if row: rows.append(row)
for i,row in enumerate(rows):
    o=[]
    for t in row:
        m=re.match(r"^\??(\d+)\??$",t)
        if m:
            n=int(m.group(1)); w=r2.get(n)
            o.append("/".join(w)[:12] if w else "<%d>"%n)
        else:o.append("{"+t+"}")
    print(i+1," ".join(o))
