"""Parse the Badator 'cifra' CSV export (Exportar Busqueda) into badator_rows.json: one row per record, order kept,
companion ('Texto descifrado') rows linked to the original they follow. Usage: python -I badator_parse.py export.csv"""
import csv, json, re, sys
rows = list(csv.DictReader(open(sys.argv[1], encoding='utf-8-sig'), delimiter=';'))
out = []
for i, x in enumerate(rows):
    d = x['Título/Descripción'].replace('\n', ' | ')
    out.append({'i': i, 'date': x['Fecha'], 'sig': x['Signatura'], 'desc': d,
                'comp': bool(re.match(r'\s*Texto descifrado|\s*Descifrado|\s*Traducci', d, re.I))})
for k, r in enumerate(out):
    r['decipherment_filed'] = False
for k, r in enumerate(out):
    if r['comp']:
        j = k - 1
        while j >= 0 and out[j]['comp']: j -= 1
        if j >= 0: out[j]['decipherment_filed'] = True; r['of'] = j
json.dump(out, open('badator_rows.json', 'w', encoding='utf-8'), ensure_ascii=False)
print(len(out), sum(r['comp'] for r in out), sum(r['decipherment_filed'] for r in out))
