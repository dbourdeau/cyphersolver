"""Group the Badator rows by sender/key and print the stats used for the leads (writes badator_groups.json)."""
import json, re, sys
rows = json.load(open('badator_rows.json', encoding='utf-8'))
NEG = r'(sin que|sin |no se halla|no figura|no sigue|no existe|no conste|no se encuentra|cuyo texto descifrado no|pendiente de descifrar)'
POS = re.compile(r'descifrad[oa]s?\s+(al margen|entre\s+(renglones|l[ií]neas)|a continuaci[oó]n|en el f)|descifrad[oa]s? en|descrifrad|descifrada entre|entre l[ií]neas', re.I)
def year(x):
    m = re.match(r'(\d{4})', x['date']); return int(m.group(1)) if m else 0
def filed(x):
    d = x['desc']
    if x['decipherment_filed']: return True
    for m in POS.finditer(d):
        pre = d[max(0, m.start()-60):m.start()+len(m.group(0))+10]
        if re.search(NEG, pre, re.I): continue
        return True
    return False
def folio(x):
    m = re.search(r'f[ºo°]\s*([0-9][0-9 ,ayv\.]*)', x['sig']); vol = re.match(r'([A-Z]-\d+)', x['sig'])
    return (vol.group(1) if vol else '?') + ' f.' + (m.group(1).strip(' .,').replace(' a ', '-').replace(' y ', '+') if m else '?')
G = {
 'perez': (r'Juan P[eé]rez, secretario|secretario Juan P[eé]rez', 1524, 1530),
 'caracciolo': (r'Marino Caracciolo', 1524, 1530),
 'herrera': (r'Miguel de Herrera', 1524, 1530),
 'lannoy': (r'Carta de Carlos de Lannoy', 1522, 1528),
 'colonna': (r'Carta de Pr[oó]spero Colonna', 1522, 1524),
 'adorno': (r'Adorno', 1522, 1524),
 'adrian': (r'Carta del papa Adriano VI', 1522, 1524),
 'nino': (r'Rodrigo Ni[nñ]o', 1522, 1523),
 'roca': (r'conde de la Roca', 1643, 1645),
 'tribulcio': (r'Tribulcis', 1652, 1655),
 'leopoldo': (r'Carta de Leopoldo Guillermo', 1650, 1657),
 'medici1521': (r'Rafael de M[eé]dicis', 1521, 1522),
}
out = {}
for k, (rx, y0, y1) in G.items():
    sel = [x for x in rows if not x['comp'] and re.search(rx, x['desc']) and y0 <= year(x) <= y1 and re.search(r'cifra|cifrad', x['desc'] + x['sig'], re.I)]
    # a row whose own description has no cipher mention (cipher wording only in the part cut off) is kept: desc is complete here
    def body(x):
        d = re.sub(r'^.*?(Ejemplar (duplicado|triplicado)[^:]*:|Copia[^:]*:)\s*\|?\s*', '', x['desc'], flags=re.I)
        d = d.split(' | ')[0] if d.startswith(('Carta', 'Cap')) else d
        return re.sub(r'\W+', ' ', d.lower())[:90]
    fb = {(x['date'][:10], body(x)) for x in sel if filed(x) and len(body(x)) > 50}
    dup_of_filed = lambda x: (x['date'][:10], body(x)) in fb and len(body(x)) > 50
    unf = [x for x in sel if not filed(x) and not dup_of_filed(x)]
    out[k] = dict(n=len(sel), n_filed=len(sel)-len(unf), years=sorted({year(x) for x in sel}),
                  unfiled=[(x['date'][:10], folio(x), x['i']) for x in unf],
                  filed=[(x['date'][:10], folio(x), x['i']) for x in sel if filed(x)])
    print(k, out[k]['n'], 'filed', out[k]['n_filed'], 'years', out[k]['years'])
json.dump(out, open('badator_groups.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
