import json, re, sys, html
H = json.load(open('_dl/hits.json', encoding='utf8'))
D = {}
for l in open('_dl/detail.jsonl', encoding='utf8'):
    try: j = json.loads(l); D[j['id']] = j['text']
    except Exception: pass
KW = re.compile(r'(?i)(?<![a-z])(de|di)?c?[sz]?ifr\w*|zifr\w*|crittogra\w*|nomenclator\w*|segni convenzional\w*|caratteri convenzional\w*|scrittura segreta|alfabeto segreto')
CIPH = re.compile(r'(?i)\b(in cifra|cifrat\w+|decifr\w+|discifr\w+|cifrario|cifrari|zifra|zifre|ziffr\w+|crittogr\w+|cifre? (segret|diplomatic)\w*|cifra (di|da|per|del|della|dei)\b|con cifra|a cifra|cifrate|senza cifra|in zifra|in cifre)\b')
NUMER = re.compile(r'(?i)(cifre? (arabe|romane|arabiche|numeric\w*|decimal\w*|rosse|nere)|numeri e cifre|in cifre (arabe|romane)|cifre? (di|dei) (data|anno))')
STRICT = re.compile(r'(?i)(\bin cifra\b|\bcifrat\w+|\bde?scifr\w+|\bdiscifr\w+|\bdecifr\w+|\bcifrari\w*|\bz[i]?ifr\w+|\bcrittogr\w+|\bnomenclator\w*|\bcifra\b(?=[^|]{0,60}(lettere|lettera|dispacci|corrisp|carteggi|scritt|segret|chiave|alfabet|nunzi|ambasc))|(lettere|lettera|dispacci|corrisp|carteggi|scritt\w+|segret\w*|chiave|alfabet\w+)\W{1,5}(\w+\W+){0,3}cifre?\b(?!\s+(arabe|romane))|\bcifre\b(?=[^|]{0,40}(lettere|dispacci|segret|diplomat)))')
def clean(t):
    segs = []; seen = set()
    for s in t.split(' || '):
        s = html.unescape(s).replace('<br />', ' ').strip()
        if s and s not in seen and s not in ('_blank','XML'): seen.add(s); segs.append(s)
    return ' | '.join(segs)
def ctx(t, rx, w=130, maxn=4):
    out = []; last = -1
    for m in rx.finditer(t):
        if m.start() < last: continue
        out.append(t[max(0, m.start()-w): m.end()+w].replace('\n', ' ')); last = m.end() + w
        if len(out) >= maxn: break
    return out
if __name__ == '__main__':
    sel = sys.argv[1] if len(sys.argv) > 1 else 'all'
    res = []
    for k, t in D.items():
        c = clean(t)
        cs = ctx(c, STRICT)
        if cs: res.append((k, H[k]['title'], c, cs))
    print(len(D), 'fetched;', len(res), 'with cipher-context')
    json.dump([{'id': k, 'title': ti, 'ctx': cs} for k, ti, c, cs in res], open('_dl/screen.json', 'w', encoding='utf8'), ensure_ascii=False, indent=0)
