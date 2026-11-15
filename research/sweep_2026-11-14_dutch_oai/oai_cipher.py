"""Harvest archieven.nl OAI-PMH oai_ead records (open-data sets) and keep components whose title/scope note mentions cipher.
usage: oai_cipher.py out.jsonl SET [SET...]   (resumes per set via out.progress.json)"""
import sys, re, json, time, html, os, requests
S = requests.Session(); S.headers['User-Agent'] = 'Mozilla/5.0'
B = 'https://harvest.archieven.nl/OAI/OAIHandler'
out = sys.argv[1]; prog_f = out + '.progress.json'
prog = json.load(open(prog_f)) if os.path.exists(prog_f) else {}
RX = re.compile(r'cijfer(?:schrift|code|brief|sleutel|tabel|alfabet|letter)|in (?:het |de )?cijfer|in cijfers? (?:geschreven|opgesteld)|geheimschrift|chiffr|cypher|cipher|cyfer|\bin code\b|codeschrift|geheimtaal|figuurcode|letterschrift|cifra|cifrad|dechiffr|ontcijfer|gecodeerd|gecijferd|cijfers?leutel|secreet\s*schrift|chiffres|en chiffre|cifrat|cifr', re.I)
TOK = re.compile(r'<(c\d\d)[ >][^>]*>|</(c\d\d)>|<unittitle[^>]*>(.*?)</unittitle>|<unitid>([^<]*)</unitid>|<scopecontent>(.*?)</scopecontent>|<unitdate[^>]*>([^<]*)</unitdate>|<odd[^>]*>(.*?)</odd>', re.S)
f = open(out, 'a', encoding='utf-8')
def clean(s): return html.unescape(re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', s))).strip()
def process(rec, setn):
    head = re.search(r'<archdesc.*?<unittitle[^>]*>([^<]*)', rec, re.S)
    code = re.search(r'<archdesc.*?<unitid[^>]*>([^<]*)', rec, re.S)
    guid = re.search(r'<identifier>([^<]*)</identifier>', rec)
    fond = clean(head.group(1)) if head else ''
    stack = []; hits = 0
    for m in TOK.finditer(rec):
        if m.group(1):
            stack.append({'t': '', 'id': '', 'sc': '', 'd': '', 'odd': ''})
        elif m.group(2):
            c = stack.pop() if stack else None
            if c and RX.search(c['t'] + ' ' + c['sc'] + ' ' + c['odd']):
                f.write(json.dumps({'set': setn, 'fond': fond, 'fond_code': code.group(1) if code else '', 'guid': guid.group(1) if guid else '',
                                    'parents': [x['t'][:80] for x in stack][-3:], 'id': c['id'], 'title': c['t'], 'date': c['d'], 'scope': c['sc'][:600], 'odd': c['odd'][:200]}, ensure_ascii=False) + '\n'); hits += 1
        elif stack:
            c = stack[-1]
            if m.group(3) is not None and not c['t']: c['t'] = clean(m.group(3))
            elif m.group(4) is not None and not c['id']: c['id'] = m.group(4).strip()
            elif m.group(5) is not None: c['sc'] += ' ' + clean(m.group(5))
            elif m.group(6) is not None and not c['d']: c['d'] = m.group(6).strip()
            elif m.group(7) is not None: c['odd'] += ' ' + clean(m.group(7))
    f.flush(); return hits
for setn in sys.argv[2:]:
    if prog.get(setn) == 'done': continue
    url = B + '?verb=ListRecords&metadataPrefix=oai_ead&set=' + setn
    if isinstance(prog.get(setn), str) and prog[setn] != 'done': url = B + '?verb=ListRecords&resumptionToken=' + requests.utils.quote(prog[setn])
    nrec = 0; nh = 0
    while True:
        try: r = S.get(url, timeout=300)
        except Exception as e: print('ERR', setn, e); time.sleep(10); continue
        if r.status_code in (403, 429): print('STOP', r.status_code, setn); sys.exit(1)
        x = r.text
        if 'noRecordsMatch' in x: break
        for m in re.finditer(r'<record>(.*?)</record>', x, re.S):
            if '<header status="deleted"' in m.group(1): continue
            nrec += 1; nh += process(m.group(1), setn)
        tok = re.search(r'<resumptionToken[^>]*>([^<]+)', x)
        print(setn, nrec, nh, flush=True)
        if not tok: break
        prog[setn] = tok.group(1); json.dump(prog, open(prog_f, 'w'))
        url = B + '?verb=ListRecords&resumptionToken=' + requests.utils.quote(tok.group(1))
        time.sleep(2.5)
    prog[setn] = 'done'; json.dump(prog, open(prog_f, 'w'))
