"""Fetch archived inventory PDFs of blocked Italian state-archive sites from the Wayback Machine (if_ raw mode),
convert with pdftotext, grep for cipher terms. Cache in _dl/wb/. Polite: one request per 6 s, back off on 429.
Usage: python wb_grep.py <cdx_key> [maxsize_bytes]"""
import json, sys, os, re, time, urllib.parse, urllib.request, subprocess, hashlib
HERE = os.path.dirname(os.path.abspath(__file__))
D = os.path.join(HERE, '_dl', 'wb'); os.makedirs(D, exist_ok=True)
key = sys.argv[1]; maxsize = int(sys.argv[2]) if len(sys.argv) > 2 else 4_000_000
INC = re.compile(sys.argv[3], re.I) if len(sys.argv) > 3 else None
lists = json.load(open(os.path.join(HERE, '_dl', 'cdx_lists.json')))
rows = [r for r in lists[key][1:] if r[0].lower().endswith('.pdf')]
EXC = re.compile(r'Distretto|Rubrica|RuoMat|Avviso|CV_|Cv_|Convenzione|Bando|bando|DPCM|Decreto|DDG|Conferimento|All\._|Allegato|obblighi|Modulo|Modello|determina|Piano_|Regolamento|domanda|Carta_dei|Condizioni|Contratto|Circ|circ_|DM_|uso_bbcc|Struttura|Rubrica|Notai|notai|Martinoli|Olgiati|Gambi|Orlandi|Filangieri|DECRETI|Prot__|51536116|52913484|58905485|60950441|5_-_com|cap0|^Stato_civile|StatoCivile|Matricole|Leve|Sanit|Zecca|Bagni|Criminale|Rota', re.I)
PAT = re.compile(r'cifr|cifre|decifr|chiffr|ciphe|cypher|zifra|in cifra|scrittura segreta|alfabeto segreto', re.I)
log = open(os.path.join(HERE, '_dl', f'wb_{key}.log'), 'a', encoding='utf8')
hits_out = os.path.join(HERE, '_dl', f'wb_{key}_hits.jsonl')
def fetch(url, ts):
    u = f'http://web.archive.org/web/{ts}if_/{url}'
    for a in range(6):
        try:
            r = urllib.request.urlopen(urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'}), timeout=180)
            return r.read()
        except urllib.error.HTTPError as e:
            if e.code in (429, 503, 504):
                time.sleep(45 * (a + 1)); continue
            if e.code in (404, 403): return None
            time.sleep(10)
        except Exception as e:
            time.sleep(15)
    return None
for orig, ts, mt, ln in rows:
    name = urllib.parse.unquote(orig).split('/')[-1]
    if EXC.search(name): continue
    if INC and not INC.search(name): continue
    if int(ln or 0) > maxsize: 
        log.write(f'SKIP big {name} {ln}\n'); log.flush(); continue
    fn = os.path.join(D, key + '__' + hashlib.md5(orig.encode()).hexdigest()[:8] + '.txt')
    if not os.path.exists(fn):
        data = fetch(orig, ts)
        time.sleep(6)
        if not data:
            log.write(f'FAIL {name}\n'); log.flush(); continue
        pdf = fn.replace('.txt', '.pdf')
        open(pdf, 'wb').write(data)
        subprocess.run(['pdftotext', '-layout', pdf, fn], capture_output=True)
        try: os.remove(pdf)
        except Exception: pass
    if not os.path.exists(fn):
        log.write(f'NOTEXT {name}'+chr(10)); log.flush(); continue
    txt = open(fn, encoding='utf8', errors='replace').read()
    n = 0
    for m in PAT.finditer(txt):
        a, b = max(0, m.start() - 160), min(len(txt), m.end() + 160)
        open(hits_out, 'a', encoding='utf8').write(json.dumps({'file': name, 'orig': orig, 'ts': ts, 'ctx': re.sub(r'\s+', ' ', txt[a:b])}, ensure_ascii=False) + '\n')
        n += 1
    log.write(f'OK {name} {len(txt)} chars, {n} hits\n'); log.flush()
log.write('DONE\n'); log.flush()
