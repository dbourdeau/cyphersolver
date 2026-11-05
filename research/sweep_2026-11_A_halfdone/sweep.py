"""PARES description sweep for cipher items (Oct 2026 archive sweep).

    python research/pares_ags/sweep.py "en cifra" [maxpages] [anio1 anio2]

Searches one term in its own PARES session and appends each hit (id, signatura, dates, title, has_images, term,
and the year range when one is given) to research/pares_ags/hits.jsonl, deduplicated by id within the term (and
year range). Raw pages go to the scratch dir given by PARES_RAW (not the repo).

How PARES pages (worked out from the saved pages and tested live on 27 Oct 2026):
  1. GET  catalogo/find?nm=&texto=<term>[&anio1=<y>&anio2=<y>]  starts the search in a new session (cookie
     JSESSIONID); it always renders 25 rows, whatever `tambloque` / `pagina` say.
  2. POST catalogo/SearchController.do?nm=.  with the fields of the form `formBusqueda` (tambloque=100,
     orderBy=PARES_ORDER, default 8) re-renders the same search in the session with 100 rows a page.
  3. Page n is the displaytag link in the `pagelinks` div:
     SearchController.do;jsessionid=<s>?texto=...&d-2677838-p=<n>&nm=  (followed with the same cookie jar).
A resume at page n repeats steps 1-2 and then asks for page n with the same link pattern.
The order is not stable between pages (orderBy=8 and orderBy=0 both repeat a few rows on the next page and skip as
many), so a term with fewer unique hits than PARES's total needs a second pass in another order: PARES_ORDER=0
(title) has its own progress entry `<term>#order0`. orderBy=7 (signatura) gave the PARES error page.

Politeness (27 Oct 2026): one request at a time, at least PARES_DELAY seconds (default 20) plus up to 10 s jitter
between any two requests, also across processes (the time of the last request is kept in the file PARES_STAMP);
the run stops at the first 429 (exit 2) instead of retrying into the block; PARES_MAXREQ (default 50) caps the
requests of one run; hits_progress.json keeps the last page done per term, so a restart resumes after it; a page
whose rows all appeared on earlier pages, or the PARES error page, ends the term.
"""
import datetime, html, http.cookiejar, json, os, random, re, sys, tempfile, time
import urllib.error, urllib.parse, urllib.request

BASE = 'https://pares.cultura.gob.es/ParesBusquedas20/catalogo'
UA = 'Mozilla/5.0 (research; cyphersolver archive sweep)'
PER_PAGE = 100
ORDER = int(os.environ.get('PARES_ORDER', '8'))   # formBusqueda orderBy: 8 nivel, 4 relevancia, 0 titulo, 1 fecha,
                                                  # 2 archivo, 3 digitalizado, 7 signatura
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'hits.jsonl')
PROGRESS = os.path.join(HERE, 'hits_progress.json')
RAW = os.environ.get('PARES_RAW')
DELAY = float(os.environ.get('PARES_DELAY', '20'))
MAXREQ = int(os.environ.get('PARES_MAXREQ', '50'))
STAMP = os.environ.get('PARES_STAMP', os.path.join(tempfile.gettempdir(), 'pares_last_request'))  # spacing
PAUSE_EVERY = 0      # run_batch.py sets these: a long pause after every PAUSE_EVERY requests
PAUSE_SECS = 0
NREQ = 0
LOG = []             # (UTC time, method, status) of every live request of this run
_last = 0.0


class Blocked(Exception):
    pass


def opener():
    op = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar()))
    op.addheaders = [('User-Agent', UA)]
    return op


def utc():
    return datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S')


def fetch(op, url, data=None, referer=None):
    """The only place that talks to PARES: one request at a time, spaced, capped, stop on 429."""
    global NREQ, _last
    if NREQ >= MAXREQ:
        raise Blocked('request cap reached (%d)' % MAXREQ)
    if PAUSE_EVERY and NREQ and NREQ % PAUSE_EVERY == 0:
        print(f'pause {PAUSE_SECS} s after {NREQ} requests', file=sys.stderr)
        time.sleep(PAUSE_SECS)
    last = _last
    try:                                # the last request of an earlier process counts too
        last = max(last, os.path.getmtime(STAMP))
    except OSError:
        pass
    wait = last + DELAY + random.uniform(0, 10) - time.time()
    if last and wait > 0:
        time.sleep(wait)
    NREQ += 1
    req = urllib.request.Request(url, data=urllib.parse.urlencode(data).encode('ascii') if data else None)
    if referer:
        req.add_header('Referer', referer)
    try:
        r = op.open(req, timeout=90)
        body = r.read()
        LOG.append((utc(), 'POST' if data else 'GET', r.status))
        return body.decode('utf-8', 'replace')
    except urllib.error.HTTPError as e:
        LOG.append((utc(), 'POST' if data else 'GET', e.code))
        if e.code == 429:
            raise Blocked('429, retry-after %s' % e.headers.get('Retry-After'))
        raise
    finally:
        _last = time.time()
        try:
            open(STAMP, 'w').close()
            os.utime(STAMP, (_last, _last))
        except OSError:
            pass


def load_progress():
    return json.load(open(PROGRESS, encoding='utf-8')) if os.path.exists(PROGRESS) else {}


def save_progress(pr):
    with open(PROGRESS, 'w', encoding='utf-8', newline='\n') as fh:
        json.dump(pr, fh, ensure_ascii=False, indent=1)
        fh.write('\n')


def parse(h):
    """One dict per result row (<tr class="odd|even">). The thumbnail link to catalogo/show/<id> sits in the row's
    first cell, before the title link, so has_images must be read per row."""
    out = []
    for row in re.findall(r'(?s)<tr class="(?:odd|even)">(.*?)</tr>', h):
        m = re.search(r'href="/ParesBusquedas20/catalogo/description/(\d+)\?nm"[^>]*>(.*?)</a>', row, re.S)
        if not m:
            continue
        txt = lambda x: re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]*>', ' ', x))).strip()
        full = re.search(r"title='([^']*)'", row)
        dates = re.search(r'Fechas?: </em>(.*?)</p>', row, re.S)
        sig = re.search(r'Signatura: </em>(.*?)</p>', row, re.S)
        sig = re.sub(r'\s*\[ Signaturas anteriores \]', '', txt(sig.group(1))) if sig else '?'
        out.append({'id': m.group(1), 'sig': sig, 'date': txt(dates.group(1)) if dates else '?',
                    'title': txt(full.group(1) if full else m.group(2)),
                    'images': f'catalogo/show/{m.group(1)}' in row})
    return out


def banner(h):
    """(first row, last row, total) from 'Resultados 1 - 100 de 488', or from 'Resultados 58' when all rows fit
    on one page; None when there is no banner."""
    m = re.search(r'Resultados <span class="azul">([\d.]+)</span> - <span class="azul">([\d.]+)</span> de '
                  r'<span class="azul">([\d.]+)</span>', h)
    if m:
        return tuple(int(x.replace('.', '')) for x in m.groups())
    m = re.search(r'Resultados <span class="azul">([\d.]+)</span>\s*</div>', h)
    if m:
        t = int(m.group(1).replace('.', ''))
        return (1, t, t)
    return None


def page_link(h, n):
    """URL of results page n, built from any displaytag link in the pagelinks div (same session)."""
    m = re.search(r'<div class="pagelinks">(.*?)</div>', h, re.S)
    links = re.findall(r'href="([^"]*d-2677838-p=\d+[^"]*)"', m.group(1)) if m else []
    if not links:
        return None
    u = re.sub(r'd-2677838-p=\d+', f'd-2677838-p={n}', html.unescape(links[0]))
    return urllib.parse.urljoin(BASE + '/', u)


def is_error(h):
    return 'id="error_mensaje"' in h or 'Problema encontrado al realizar la b' in h


def key_of(term, anio1=None, anio2=None, facet=None):
    k = term if anio1 is None and anio2 is None else f'{term}|{anio1 or ""}-{anio2 or ""}'
    return k if not facet else f'{k}&{facet}'


def save_raw(key, label, h):
    if RAW:
        name = f's{PER_PAGE}_{re.sub(r"[^0-9A-Za-z]+", "_", key)}_{label}.html'
        with open(os.path.join(RAW, name), 'w', encoding='utf-8', newline='\n') as fh:
            fh.write(h)


def open_search(op, rawkey, term, anio1=None, anio2=None, facet=None):
    """Steps 1-2: start the search in a new session and switch it to PER_PAGE rows. Returns page 1.

    facet: a PARES facet filter from the left column of the result page, e.g. 'idFI=16' (start date in the
    16th century), 'idFI=0' (no date), 'idD=S' (digitised). anio1/anio2 are NOT applied by PARES (28 Oct 2026:
    'cifrada' with anio1=1450&anio2=1499 still reports 1,282 rows); the facets are the working date filter."""
    q = {'nm': '', 'texto': term}
    if anio1 is not None:
        q['anio1'] = anio1
    if anio2 is not None:
        q['anio2'] = anio2
    if facet:
        q.update(urllib.parse.parse_qsl(facet))
    url = f'{BASE}/find?' + urllib.parse.urlencode(q, encoding='latin-1')
    h0 = fetch(op, url)
    save_raw(rawkey, 'find', h0)
    b0 = banner(h0)
    if not b0 or is_error(h0):
        return h0, b0
    if b0[1] >= b0[2]:          # everything already on the 25-row page
        return h0, b0
    h = fetch(op, f'{BASE}/SearchController.do?nm=.', {'tambloque': PER_PAGE, 'orderBy': ORDER}, referer=url)
    save_raw(rawkey, 'p1', h)
    return h, banner(h)


def run(term, maxpages=20, anio1=None, anio2=None, facet=None):
    key = key_of(term, anio1, anio2, facet)
    seen = set()
    if os.path.exists(OUT):
        for line in open(OUT, encoding='utf-8'):
            r = json.loads(line)
            if key_of(r['term'], r.get('anio1'), r.get('anio2'), r.get('facet')) == key:
                seen.add(r['id'])
    pkey = key if ORDER == 8 else f'{key}#order{ORDER}'   # a second pass in another order has its own progress
    pr = load_progress()
    st = pr.get(pkey, {})
    if st.get('done'):
        return 0
    start = st.get('last_page', 0) + 1 if st.get('per_page') == PER_PAGE else 1
    op = opener()
    req0 = NREQ
    try:
        n = _pages(op, key, pkey, term, anio1, anio2, start, maxpages, seen, pr, facet)
    finally:                                # count this run's requests even when it stops on 429 or the cap
        if NREQ > req0:
            pr = load_progress()
            st = pr.setdefault(pkey, {})
            st['requests'] = st.get('requests', 0) + (NREQ - req0)
            save_progress(pr)
    return n


def _pages(op, key, pkey, term, anio1, anio2, p, maxpages, seen, pr, facet=None):
    n, prev, h, b, shown = 0, None, None, None, set()   # shown: ids on earlier pages of this session
    while p <= maxpages:
        if h is None:                       # new session: page 1 of the search
            h, b = open_search(op, pkey, term, anio1, anio2, facet)
            if p > 1:
                url = page_link(h, p)
                if not url:
                    break
                h = fetch(op, url)
                save_raw(pkey, f'p{p}', h)
                b = banner(h)
        if is_error(h) or not b:
            print(f'{key!r} page {p}: PARES error page or no result banner; term left open', file=sys.stderr)
            pr.setdefault(pkey, {})['note'] = 'stopped on PARES error page at page %d, %s UTC' % (p, utc())
            save_progress(pr)
            break
        rows = parse(h)
        ids = [r['id'] for r in rows]
        new = 0
        with open(OUT, 'a', encoding='utf-8', newline='\n') as fh:
            for r in rows:
                if r['id'] in seen:
                    continue
                seen.add(r['id'])
                r['term'] = term
                if anio1 is not None or anio2 is not None:
                    r['anio1'], r['anio2'] = anio1, anio2
                if facet:
                    r['facet'] = facet
                fh.write(json.dumps(r, ensure_ascii=False) + '\n')
                new += 1
        n += new
        print(f'{key!r} page {p}: rows {b[0]}-{b[1]} of {b[2]}, {len(rows)} parsed, {new} new', file=sys.stderr)
        repeat = ids == prev or (bool(shown) and bool(rows) and set(ids) <= shown)   # rows must differ page to page
        shown.update(ids)
        last = not rows or b[1] >= b[2] or repeat
        prev = ids
        pp = (b[0] - 1) // (p - 1) if p > 1 else (b[1] - b[0] + 1 if b[1] < b[2] else PER_PAGE)
        if pp != PER_PAGE:
            print(f'{key!r}: PARES served {pp} rows a page, not {PER_PAGE}', file=sys.stderr)
        st = {'last_page': p, 'per_page': pp, 'done': last and not repeat,
              'date': datetime.date.today().isoformat(), 'unique_hits': len(seen), 'total': b[2],
              'requests': pr.get(pkey, {}).get('requests', 0)}
        if ORDER != 8:
            st['order'] = ORDER
        if repeat:
            st['note'] = 'page %d repeated page %d; paging broken again, term left open' % (p, p - 1)
        pr[pkey] = st
        save_progress(pr)
        if last:
            break
        p += 1
        url = page_link(h, p)
        if not url:
            break
        h = fetch(op, url)
        save_raw(pkey, f'p{p}', h)
        b = banner(h)
    return n


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    a = sys.argv[1:]
    try:
        print(run(a[0], int(a[1]) if len(a) > 1 else 20,
                  int(a[2]) if len(a) > 2 else None, int(a[3]) if len(a) > 3 else None), 'new hits')
    except Blocked as e:
        print('stopped:', e, file=sys.stderr)
        sys.exit(2)
    finally:
        for t, m, s in LOG:
            print(t, 'UTC', m, s, file=sys.stderr)
