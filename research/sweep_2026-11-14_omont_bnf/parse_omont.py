"""Parse the OCR of the BnF Ancien-fonds / Ancien-Supplement catalogue volumes (archive.org *_djvu.txt) for
items described 'avec chiffre' / 'en chiffre' without a decipherment. Output: omont_items.json.
usage: python parse_omont.py <dir with the djvu txt files> <out.json>"""
import re, sys, glob, json, os
D = sys.argv[1]; OUT = sys.argv[2]
cip = re.compile(r'(?:avec\s+c[hli]{1,3}if?fres?|en\s+c[hli]{1,3}if?fres?\b|chiffr[ée]e?s?\b|chiffre\s*\.\s*\(Fol|c[hl]i{1,3}ffre)', re.I)
dec = re.compile(r'd[ée]-?\s*c[hl]i{1,3}ff?r|dechiff|interlin|traduction|explication|déchiffr|et\s+d[ée]ch', re.I)
skip = re.compile(r"au\s+chiffre\s+d|aux?\s+armes\s+et\s+chiffre|chiffre\s+du\s+(?:roi|maréchal)|armes\s+et\s+chiffre|chiffre\s+de\s+(?:Louis|Napol|Charles X|Henri IV|Saint)", re.I)
head = re.compile(r'\n\s*(\d{1,5})\.\s*\n')
rows = []
for f in sorted(glob.glob(os.path.join(D, '*.txt'))):
    t = open(f, encoding='utf8', errors='ignore').read()
    if t.lstrip().startswith('<'): continue
    t = re.sub(r'[ \t]+', ' ', t)
    hs = [(m.start(), int(m.group(1))) for m in head.finditer(t)]
    for i, (off, num) in enumerate(hs):
        end = hs[i+1][0] if i+1 < len(hs) else len(t)
        body = t[off:end]
        if len(body) < 80 or len(body) > 400000: continue
        title = re.sub(r'\s+', ' ', body[:700]).strip()
        # items: split on lines beginning with number-dot
        its = re.split(r'\n\s*(?=\d{1,3}\.\s+\S)', body)
        hits = []
        for it in its:
            it1 = re.sub(r'\s+', ' ', it).strip()
            if cip.search(it1) and not skip.search(it1):
                hits.append({'dec': bool(dec.search(it1)), 'text': it1[:420]})
        flat = re.sub(r'\s+', ' ', body)
        avec = re.findall(r'avec\s+c[hl][il1]{1,3}[a-z]{1,3}[ei]?\s*,?\s*(et\s+d[eé])?', flat, re.I)
        n_avec = len(avec); n_dec = sum(1 for a in avec if a)
        n_en = len(re.findall(r"(?:en|ec)\s+chiffres?", flat, re.I))
        if n_avec or n_en:
            hits = hits or [{'dec': False, 'text': ''}]
        if hits:
            rows.append({'n_avec': n_avec, 'n_avec_dec': n_dec, 'n_en': n_en, 'vol': os.path.basename(f)[:-4], 'num': num, 'off': off, 'title': title[:500], 'items': hits})
json.dump(rows, open(OUT, 'w', encoding='utf8'), ensure_ascii=False, indent=0)
print(len(rows), sum(len(r['items']) for r in rows), sum(1 for r in rows for x in r['items'] if not x['dec']))
