"""archieven.nl OAI-PMH: ListIdentifiers per set (cached), then GetRecord (oai_ead) with a few workers; keep components
whose title/scope/odd matches cipher words. usage: oai_get.py out.jsonl SET[:skip] ...   (resumes via out.done.txt)"""
import sys, re, json, time, html, os, threading, requests
from concurrent.futures import ThreadPoolExecutor
B = 'https://harvest.archieven.nl/OAI/OAIHandler'
out = sys.argv[1]; done_f = out + '.done.txt'; W = int(os.environ.get('W', '4'))
done = set(open(done_f).read().split()) if os.path.exists(done_f) else set()
RX = re.compile(r'cijfer(?:schrift|code|brie|sleutel|tabel|alfabet|letter|telegram)|in (?:het |de )?cijfer|in cijfers? (?:geschreven|opgesteld|gesteld)|geheim\s?schrift|geheime? (?:code|schrift|taal|teken)|chiffr|cypher|cipher|cyfer|\bin code\b|code(?:schrift|brie|telegram|boek|sleutel|-)|geheimtaal|figuurcode|letterschrift|cifr|ontcijfer|gecodeerd|gecijferd|secreet\s*schrift|nomenclat|cryptogra|kryptogra|sleutel (?:van|voor|tot) (?:het|de|een) (?:cijfer|code|geheim)', re.I)
TOK = re.compile(r'<(c\d\d|c)[ >][^>]*>|</(c\d\d|c)>|<unittitle[^>]*>(.*?)</unittitle>|<unitid[^>]*>([^<]*)</unitid>|<scopecontent[^>]*>(.*?)</scopecontent>|<unitdate[^>]*>([^<]*)</unitdate>|<odd[^>]*>(.*?)</odd>|<(dao)[ >]', re.S)
lock = threading.Lock(); f = open(out, 'a', encoding='utf-8'); df = open(done_f, 'a'); log = open(out + '.fonds.tsv', 'a', encoding='utf-8')
def clean(s): return html.unescape(re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', s))).strip()
def process(rec, setn, guid):
    head = re.search(r'<archdesc.*?<unittitle[^>]*>(.*?)</unittitle>', rec, re.S)
    code = re.search(r'<archdesc.*?<unitid[^>]*>([^<]*)', rec, re.S)
    fond = clean(head.group(1)) if head else ''; fc = code.group(1) if code else ''
    stack = []; rows = []; n = 0
    for m in TOK.finditer(rec):
        if m.group(1):
            stack.append({'t': '', 'id': '', 'sc': '', 'd': '', 'odd': '', 'dao': 0}); n += 1
        elif m.group(2):
            c = stack.pop() if stack else None
            if c and RX.search(c['t'] + ' ' + c['sc'] + ' ' + c['odd']):
                rows.append({'set': setn, 'fond': fond, 'fond_code': fc, 'guid': guid, 'parents': [x['t'][:100] for x in stack][-3:], 'id': c['id'], 'title': c['t'], 'date': c['d'], 'scope': c['sc'][:800], 'odd': c['odd'][:300], 'dao': c['dao']})
        elif stack:
            c = stack[-1]
            if m.group(3) is not None and not c['t']: c['t'] = clean(m.group(3))
            elif m.group(4) is not None and not c['id']: c['id'] = m.group(4).strip()
            elif m.group(5) is not None: c['sc'] += ' ' + clean(m.group(5))
            elif m.group(6) is not None and not c['d']: c['d'] = m.group(6).strip()
            elif m.group(7) is not None: c['odd'] += ' ' + clean(m.group(7))
            elif m.group(8): c['dao'] = 1
    with lock:
        for r in rows: f.write(json.dumps(r, ensure_ascii=False) + '\n')
        f.flush(); log.write('\t'.join([setn, guid, fc, fond[:120], str(n), str(len(rec)), str(len(rows))]) + '\n'); log.flush()
        df.write(guid + '\n'); df.flush()
    return len(rows)
tl = threading.local()
def sess():
    if not hasattr(tl, 's'): tl.s = requests.Session(); tl.s.headers['User-Agent'] = 'Mozilla/5.0'
    return tl.s
STOP = threading.Event()
def get(a):
    setn, guid = a
    if STOP.is_set(): return 0
    for k in range(4):
        try:
            r = sess().get(B, params={'verb': 'GetRecord', 'metadataPrefix': 'oai_ead', 'identifier': guid}, timeout=600)
            if r.status_code in (403, 429): STOP.set(); print('STOP', r.status_code, flush=True); return 0
            if r.status_code != 200: time.sleep(10); continue
            r.encoding = 'utf-8'; h = process(r.text, setn, guid); time.sleep(1.0); return h
        except Exception as e:
            print('ERR', guid, repr(e)[:100], flush=True); time.sleep(15)
    return 0
def ids(setn):
    cf = out + '.ids.' + setn + '.txt'
    if os.path.exists(cf): return open(cf).read().split()
    res = []; p = {'verb': 'ListIdentifiers', 'metadataPrefix': 'oai_ead', 'set': setn}
    while True:
        try: x = sess().get(B, params=p, timeout=300).text
        except Exception as e: print('ERR ids', e); time.sleep(10); continue
        res += [m.group(2) for m in re.finditer(r'<header( status="deleted")?>\s*<identifier>([^<]*)', x) if not m.group(1)]
        t = re.search(r'<resumptionToken[^>]*>([^<]+)', x)
        if not t: break
        p = {'verb': 'ListIdentifiers', 'resumptionToken': t.group(1)}; time.sleep(1)
    open(cf, 'w').write('\n'.join(res)); return res
for a in sys.argv[2:]:
    setn, _, skip = a.partition(':'); L = ids(setn)[int(skip or 0):]
    todo = [(setn, g) for g in L if g not in done]
    print(setn, 'ids', len(L), 'todo', len(todo), flush=True)
    with ThreadPoolExecutor(W) as ex:
        tot = 0
        for i, h in enumerate(ex.map(get, todo)):
            tot += h
            if i % 50 == 0: print(setn, i, tot, flush=True)
    if STOP.is_set(): sys.exit(1)
    print(setn, 'done', flush=True)
