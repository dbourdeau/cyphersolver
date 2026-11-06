"""Build docs/archives.html: the requests a volunteer can take to an archive or a library, from ../archive_requests.json.

The ledger is seeded by tools/seed_archive_requests.py from two places and kept by hand after that (status, history,
volunteer):
  - the "blocker: needs-physical-access" gaps in targets/*/NOTES.md (a reading already under way that stops at the archive);
  - every open catalogue.json entry with access "archive" (the ciphertext or the key is not online yet).
The page groups the requests by archive, since people volunteer for the archive they live near or travel to, and gives
each one an "I can do this" link that opens the archive-visit issue form with the request filled in.

Called from _build_site.py before the pages are processed, like further.html, so it gets the nav and footer.
"""
import html, json, pathlib, re
from urllib.parse import urlencode

HERE = pathlib.Path(__file__).parent
LEDGER = HERE.parent / 'archive_requests.json'
REPO = 'https://github.com/dbourdeau/cyphersolver'
KIND = {'visit': ('reading room', 'Go to the reading room and look at, or photograph, the original.'),
        'order': ('order', 'Ask the archive for a scan or a reproduction: an email or an order form, sometimes a fee.'),
        'library': ('library', 'A printed book or a database behind a login: a university library card or a subscription is enough.')}
STATUS = {'open': 'open', 'claimed': 'taken', 'requested': 'asked the archive', 'received': 'images in hand',
          'closed': 'gap closed', 'unavailable': 'not available'}
LIVE = ('open', 'claimed', 'requested')
OPEN_FIRST = 3          # archives shown unfolded; the rest fold until a search or filter touches them


# the map: each request at the town of its archive. The ledger's city when it names a place the atlas gazetteer knows,
# else the first of these patterns found in the archive name or the shelfmark (a few ledger archives are shelfmarks).
# A request that matches nothing (a library or database, an archive not yet identified, a printed calendar) stays off the map
# and is listed under "not on the map".
WHERE = [(r'Bogot', 'Bogotá'), (r'AGN M[eé]xico|Mexicali', 'Mexico City'), (r'\bNAA\b|Australian War Memorial', 'Canberra'),
         (r'Chile', 'Santiago de Chile'), (r'\bASF\b|Firenze|Dieci di Bal|^Signori$', 'Florence'), (r'Napoli', 'Naples'),
         (r'Venezia', 'Venice'), (r'Milano|Trivulziana', 'Milan'), (r'Angelo Mai', 'Bergamo'), (r'Vatican', 'Vatican City'),
         (r'FHKA Wien|\bHHStA\b|Wien', 'Vienna'), (r'AHNOB|^OSUNA$|^FRIAS$|^FUENRUBIA$', 'Toledo'), (r'Lope de Soria|Real Academia de la Historia', 'Madrid'),
         (r'GLA Karlsruhe|Generallandesarchiv Karlsruhe', 'Karlsruhe'), (r'Stuttgart', 'Stuttgart'), (r'Ludwigsburg', 'Ludwigsburg'),
         (r'Neuenstein', 'Neuenstein'), (r'Dresden|Sächsisch', 'Dresden'), (r'Leipzig', 'Leipzig'), (r'StAN\b|Nürnberg', 'Nuremberg'),
         (r'StAWü|Würzburg', 'Würzburg'), (r'StABa|Bamberg', 'Bamberg'), (r'LASH|Schleswig', 'Schleswig'), (r'Sachsen-Anhalt', 'Magdeburg'),
         (r'NRW (?:Abt\. )?Rheinland', 'Duisburg'), (r'NRW Westfalen', 'Münster'), (r'Ostwestfalen', 'Detmold'), (r'NLA Wolfenb', 'Wolfenbüttel'),
         (r'NLA Hannover|Hannover', 'Hanover'), (r'Stade', 'Stade'), (r'Oldenburg', 'Oldenburg'), (r'Hildesheim', 'Hildesheim'),
         (r'HStA Marburg|Marburg', 'Marburg'), (r'HStAD\b|Darmstadt', 'Darmstadt'), (r'Wiesbaden', 'Wiesbaden'), (r'Gotha', 'Gotha'),
         (r'Konstanz', 'Konstanz'), (r'Viersen', 'Viersen'), (r'Schwerin', 'Schwerin'), (r'Zofingen', 'Zofingen'),
         (r'Institut de France|Mazarine|Sorbonne', 'Paris'), (r'Affaires [eé]trang|Courneuve', 'La Courneuve'), (r'Service historique de la D', 'Vincennes'),
         (r'Montpellier', 'Montpellier'), (r'Besan[cç]on', 'Besançon'), (r'Chantilly', 'Chantilly'), (r'Charente-Maritime', 'La Rochelle'),
         (r'Seine-et-Marne', 'Melun'), (r'Dordogne', 'Périgueux'), (r'Archives d.Alsace', 'Strasbourg'), (r'FR-FRAD073', 'Chambéry'),
         (r'Ch[aâ]lons', 'Châlons'), (r'NL-UtHUA', 'Utrecht'), (r'NL-MtRHCL', 'Maastricht'), (r'Belgian State', 'Brussels'),
         (r'Slovak National', 'Pozsony'), (r'APESP', 'São Paulo'), (r'Lublin', 'Lublin'), (r'Portugal', 'Lisbon'),
         (r'\bNLS\b|\bNRS\b', 'Edinburgh'), (r'PRONI', 'Belfast'), (r'Kresen Kernow', 'Redruth'), (r'Devon', 'Exeter'), (r'Stafford', 'Stafford'),
         (r'Hatfield', 'Hatfield'), (r'Pepys', 'Cambridge'), (r'Lambeth|Senate House|Kew', 'London'),
         (r'Morgan Library|New York Public|New-York Hist', 'New York'), (r'Folger|College Park|Washington Library', 'Washington'),
         (r'Newberry|Chicago', 'Chicago'), (r'Houghton', 'Cambridge, Massachusetts'), (r'Lilly Library', 'Bloomington'),
         (r'UNC Southern', 'Chapel Hill'), (r'University of Virginia', 'Charlottesville'), (r'William & Mary', 'Williamsburg'),
         (r'Library of Virginia', 'Richmond, Virginia'), (r'Virginia Tech', 'Blacksburg'), (r'West Virginia', 'Morgantown'),
         (r'Brigham Young', 'Provo'), (r'Connecticut Historical', 'Hartford'), (r'Kentucky Historical', 'Frankfort'),
         (r'Archives of Michigan', 'Lansing'), (r'Ohio History', 'Columbus'), (r'Detroit', 'Detroit'), (r'Lincoln Presidential', 'Springfield'),
         (r'Rutgers', 'New Brunswick'), (r'Middlebury', 'Middlebury'), (r'Cornell', 'Ithaca'), (r'Iowa', 'Des Moines'),
         (r'Temple University|Philadelphia|Haverford', 'Philadelphia'), (r'Duke', 'Durham'), (r'South Carolina', 'Columbia'),
         (r'Henry Ford', 'Dearborn'), (r'Army Heritage', 'Carlisle'), (r'Stanford', 'Stanford'), (r'Lehigh', 'Bethlehem'),
         (r'Friedman Collection|Marshall Foundation', 'Lexington')]
# towns the atlas gazetteer does not have, [lat, lon]
TOWNS = {'Bogotá': [4.71, -74.07], 'Canberra': [-35.28, 149.13], 'Santiago de Chile': [-33.45, -70.67], 'Bergamo': [45.70, 9.67],
         'Vatican City': [41.904, 12.453], 'Karlsruhe': [49.01, 8.40], 'Stuttgart': [48.78, 9.18], 'Ludwigsburg': [48.90, 9.19],
         'Neuenstein': [49.20, 9.58], 'Leipzig': [51.34, 12.37], 'Nuremberg': [49.45, 11.08], 'Würzburg': [49.79, 9.95],
         'Bamberg': [49.89, 10.89], 'Schleswig': [54.52, 9.57], 'Magdeburg': [52.13, 11.63], 'Duisburg': [51.43, 6.76],
         'Detmold': [51.94, 8.88], 'Stade': [53.60, 9.48], 'Oldenburg': [53.14, 8.21], 'Hildesheim': [52.15, 9.95],
         'Marburg': [50.81, 8.77], 'Wiesbaden': [50.08, 8.24], 'Gotha': [50.95, 10.70], 'Konstanz': [47.66, 9.18],
         'Viersen': [51.26, 6.39], 'Schwerin': [53.63, 11.41], 'Zofingen': [47.29, 7.95], 'La Courneuve': [48.93, 2.40],
         'Vincennes': [48.84, 2.44], 'Montpellier': [43.61, 3.88], 'Besançon': [47.24, 6.02], 'Chantilly': [49.19, 2.47],
         'Melun': [48.54, 2.66], 'Périgueux': [45.18, 0.72], 'Chambéry': [45.57, 5.92], 'Utrecht': [52.09, 5.12],
         'Maastricht': [50.85, 5.69], 'Belfast': [54.60, -5.93], 'Redruth': [50.23, -5.23], 'Exeter': [50.72, -3.53],
         'Stafford': [52.81, -2.12], 'Hatfield': [51.76, -0.22], 'Cambridge': [52.21, 0.12], 'Dublin': [53.35, -6.26],
         'Budapest': [47.50, 19.04], 'Aix-en-Provence': [43.53, 5.45], 'Modena': [44.65, 10.93], 'Simancas': [41.59, -4.83],
         'Heraklion': [35.34, 25.13], 'Klášter u Nepomuka': [49.47, 13.58], 'New Haven': [41.31, -72.93], 'Ann Arbor': [42.28, -83.74],
         'Porto Alegre': [-30.03, -51.23], 'São Paulo': [-23.55, -46.63], 'San Marino, California': [34.12, -118.11], 'Boston': [42.36, -71.06],
         'Cambridge, Massachusetts': [42.37, -71.11], 'Bloomington': [39.17, -86.53], 'Chapel Hill': [35.91, -79.05],
         'Charlottesville': [38.03, -78.48], 'Williamsburg': [37.27, -76.71], 'Blacksburg': [37.23, -80.41], 'Morgantown': [39.63, -79.96],
         'Provo': [40.23, -111.66], 'Hartford': [41.76, -72.69], 'Frankfort': [38.20, -84.87], 'Lansing': [42.73, -84.55],
         'Columbus': [39.96, -83.00], 'Detroit': [42.33, -83.05], 'Springfield': [39.80, -89.64], 'New Brunswick': [40.50, -74.45],
         'Middlebury': [44.01, -73.17], 'Ithaca': [42.44, -76.50], 'Des Moines': [41.59, -93.62], 'Durham': [35.99, -78.90],
         'Columbia': [34.00, -81.03], 'Dearborn': [42.32, -83.18], 'Carlisle': [40.20, -77.19], 'Stanford': [37.43, -122.17],
         'Bethlehem': [40.61, -75.37], 'Lexington': [37.78, -79.44], 'Sigmaringen': [48.09, 9.22], 'Wertheim': [49.76, 9.52],
         'Montevideo': [-34.90, -56.19], 'Brno': [49.19, 16.61], 'Kostelec nad Orlicí': [50.12, 16.21], 'Mount Vernon': [38.71, -77.09], 'Châlons-en-Champagne': [48.96, 4.36]}


def gazetteer():
    import sys
    sys.path.insert(0, str(HERE.parent / 'tools'))
    import atlas_places as AP
    names = {**AP.gazetteer(json.loads((HERE / 'atlas.json').read_text(encoding='utf-8'))), **TOWNS}
    return names, lambda t: AP.place_in(t, names)


def place_of(r, find):
    """The town of a request's archive, or '' when it cannot be placed."""
    if r.get('city'):
        p = find(r['city'])
        if p: return p
    text = f'{r["archive"]} | {r.get("shelfmark") or ""}'
    for pat, p in WHERE:
        if re.search(pat, text): return p
    if r['archive'] in ('A library or database', 'unknown'): return ''
    return find(r['archive']) or ''


def esc(t):
    return html.escape(str(t or ''), quote=False)


def attr(t):
    return html.escape(str(t or ''), quote=True)


def load():
    return json.loads(LEDGER.read_text(encoding='utf-8'))['requests'] if LEDGER.is_file() else []


def pages_by_folder(pages):
    out = {}
    for p in pages:
        for f in p.get('folders') or []: out.setdefault(f, p)
    return out


def issue_url(r):
    q = {'template': 'archive-visit.yml', 'title': f'Archive request: {r["id"]} ({r["archive"]})', 'request': r['id'],
         'archive': ', '.join(x for x in (r['archive'], r.get('shelfmark')) if x and x != 'unknown')}
    return f'{REPO}/issues/new?' + urlencode(q)


def who(r):
    v = r.get('volunteer') or {}
    if not v.get('name'): return ''
    return f' · {esc(v["name"])}{(", " + esc(v["month"])) if v.get("month") else ""}'


def is_cat(r):
    """A catalogue item (no reading under way), as against a gap in a reading already written up."""
    return bool(r.get('catalogue')) and not r.get('target')


def pri(r):
    """Order inside an archive: a gap stalling a reading first, then catalogue items by importance x solvability."""
    return (r.get('imp') or 0) * (r.get('solv') or 0) if is_cat(r) else 100


def target_link(r, bypage):
    t = r.get('target')
    if is_cat(r):
        bits = ' · '.join(x for x in (f'cat. {r["catalogue"]}', str(r.get('year') or ''), f'class {r["cls"]}' if r.get('cls') else '') if x)
        import _catalogue_page as C     # an open entry, or a number that left and keeps a notice: both have a page
        known = r['catalogue'] in C.SOLVED or any(e['id'] == r['catalogue'] for e in C.DATA['entries'])
        return f'<a class="tgt" href="solve/{r["catalogue"]}.html">{bits}</a>' if known else f'<span class="tgt">{bits}</span>'
    if not t: return '<span class="tgt">general</span>'
    p = bypage.get(t)
    if p: return f'<a class="tgt" href="{p["slug"]}.html">{re.sub(r"<[^>]+>", "", p["label"] or p["slug"])}</a>'
    return f'<a class="tgt" href="{REPO}/tree/main/targets/{t}" rel="noopener">{esc(t)}</a>'


def row(r, bypage):
    k = r['kind']
    issue = f' · <a href="{REPO}/issues/{r["issue"]}" rel="noopener">issue #{r["issue"]}</a>' if r.get('issue') else ''
    act = (f'<a class="take" href="{attr(issue_url(r))}" rel="noopener">I can do this</a>' if r['status'] == 'open' else
           f'<span class="st st-{r["status"]}">{STATUS.get(r["status"], r["status"])}</span>')
    why = f'<span class="why2">{esc(r["why"])}</span>' if r.get('why') else ''
    shelf = f'<span class="sm">{esc(r["shelfmark"])}</span>' if r.get('shelfmark') else ''
    src = 'cat' if is_cat(r) else 'gap'
    flag = '<span class="gapflag" title="A reading is already under way; this gap is what stops it">reading stalled here</span>' if src == 'gap' else ''
    text = ' '.join(x for x in (r['id'], r.get('target') or '', str(r.get('catalogue') or ''), r['archive'], r.get('city', ''),
                                r.get('shelfmark', ''), r['need'], r.get('why', ''), r.get('region') or '', KIND[k][0])).lower()
    cid = f' id="c{r["catalogue"]}"' if is_cat(r) else ''
    return (f'<li class="rq"{cid} data-kind="{k}" data-src="{src}" data-status="{r["status"]}" data-pl="{attr(r.get("_pl"))}" data-q="{attr(text)}">'
            f'<div class="hd"><span class="id">{r["id"]}</span><span class="kd kd-{k}">{KIND[k][0]}</span>{target_link(r, bypage)}{flag}</div>'
            f'<p class="nd">{esc(r["need"])}</p>{shelf}{why}'
            f'<div class="ft">{act}{who(r)}{issue}</div></li>')


def groups(reqs):
    g = {}
    for r in reqs: g.setdefault((r['archive'], r.get('city') or ''), []).append(r)
    last = ('A library or database', 'unknown')
    return sorted(g.items(), key=lambda kv: (kv[0][0] in last, -len(kv[1]), kv[0][0]))


def gid(name):
    return 'a-' + re.sub(r'[^a-z0-9]+', '-', name.lower()).strip('-')


def mix(rs):
    return ''.join(f'<span class="kd kd-{k}" title="{KIND[k][0]}">{m}</span>'
                   for k in KIND if (m := sum(r['kind'] == k for r in rs)))


def build_html(pages):
    reqs = load()
    bypage = pages_by_folder(pages)
    live = [r for r in reqs if r['status'] in LIVE]
    names, find = gazetteer()
    for r in live: r['_pl'] = place_of(r, find)
    towns = {p: names[p] for p in sorted({r['_pl'] for r in live} - {''})}
    unplaced = sum(not r['_pl'] for r in live)
    n = {s: sum(r['status'] == s for r in reqs) for s in STATUS}
    nk = {k: sum(r['kind'] == k for r in live) for k in KIND}
    ncat = sum(is_cat(r) for r in live)
    ngap = len(live) - ncat
    G = groups(live)
    places = len({a for (a, _), _ in G if a not in ('A library or database', 'unknown')})
    toc = ''.join(f'<li><a href="#{gid(a)}">{esc(a)}</a>{f" <span>{esc(c)}</span>" if c else ""} <b>{len(rs)}</b></li>' for (a, c), rs in G)
    secs = ''.join(
        f'<details class="arch" id="{gid(a)}"{" open" if i < OPEN_FIRST else ""}><summary>'
        f'<h3>{esc("Archive not yet identified" if a == "unknown" else a)}{f" <span class=city>{esc(c)}</span>" if c else ""}</h3>'
        f'<span class="mix">{mix(rs)}</span><span class="n">{len(rs)}</span></summary>'
        f'<ul class="rqs">{"".join(row(r, bypage) for r in sorted(rs, key=lambda r: (r["status"] != "open", -pri(r), r["id"])))}</ul></details>'
        for i, ((a, c), rs) in enumerate(G))
    done = [r for r in reqs if r['status'] not in LIVE]
    done_html = (f'<ul class="rqs done">{"".join(row(r, bypage) for r in sorted(done, key=lambda r: r["history"][-1]["date"], reverse=True))}</ul>'
                 if done else '<p class="none">None yet. The first photograph that closes a gap will be listed here, with its volunteer.</p>')
    kinds = ''.join(f'<li><button type="button" class="kc" data-k="{k}" aria-pressed="false"><b>{nk[k]}</b>'
                    f'<span class="kd kd-{k}">{lab}</span><small>{desc}</small></button></li>' for k, (lab, desc) in KIND.items())
    page = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>To the Archive — {len(live)} open requests</title>
<meta name="description" content="{len(live)} pieces of historical ciphers that only an archive or a library can supply: leaves to photograph, scans to order, books to look up. {ngap} stall a reading already under way; {ncat} are catalogue items not online. Take one on.">
<link rel="stylesheet" href="style.css">
</head>
<body id="top" class="nojs">
<!-- site:nav -->

<section class="hero">
  <div class="ahero-grid"><div class="ahero-lead">
  <p class="kicker">{len(live)} open requests · {places} archives · {n["claimed"] + n["requested"]} under way · {n["received"] + n["closed"]} done</p>
  <h1>To the <span class="stk">Archive<a class="sticker arc" href="#list" title="Pick a request below"><span><b>Go<br>Look!</b><small>pick a request</small></span></a></span></h1>
  <p class="sub">Some readings stop where the scans stop: a line lost in the binding, a leaf nobody photographed, a decipherment filed in a volume that was never digitised, a book behind a login. Other ciphers are catalogued but were never imaged at all. Each request below is one of those gaps. If you live near the archive, travel past it, or have a library card that reaches the book, you can close it.</p>
  </div>
  <figure class="ahero"><img src="archives_indias.jpg" width="1200" height="800" decoding="async" fetchpriority="high" alt="A long vaulted gallery of the Archivo General de Indias in Seville: walnut shelves of document bundles on both sides, portraits on the walls, a coffered ceiling and a polished marble floor">
    <figcaption>Archivo General de Indias, Seville. <span class="credit">Photo: <a href="https://commons.wikimedia.org/wiki/File:Archivo_General_de_Indias._Sevilla.jpg">Jos&eacute; L. Filpo</a>, <a href="https://creativecommons.org/licenses/by/3.0/">CC BY 3.0</a>, via Wikimedia Commons.</span></figcaption></figure>
  </div>
  <ol class="steps"><li><b>1</b>find an archive you can reach</li><li><b>2</b>click &ldquo;I can do this&rdquo;</li><li><b>3</b>look, photograph or order</li><li><b>4</b>send the images; you are credited</li></ol>
</section>

<main>
<ul class="kinds" aria-label="Filter by kind of request">{kinds}</ul>

<h2 id="map">The map</h2>
<p class="am-lede">Every open request, at the town of the archive that holds the piece: {len(live) - unplaced} of the {len(live)} in {len(towns)} towns. A ring grows with the requests there and follows the filters below; click one to list only its requests. The other {unplaced} need a library or a database rather than a place, or an archive not yet identified. The <a href="atlas.html">atlas</a> draws the same unread letters where they were written.</p>
<div class="amap-wrap jsonly">
  <div class="amap" id="amap">
    <span class="am-count" id="amapn"></span>
    <button type="button" class="am-world" id="amworld" hidden></button>
    <div class="am-zoom" role="group" aria-label="Zoom the map"><button type="button" id="amzin" aria-label="Zoom in">+</button><button type="button" id="amzout" aria-label="Zoom out">&minus;</button><button type="button" id="amzreset" aria-label="Reset the map">&#8634;</button></div>
  </div>
  <aside class="am-side" id="amapside" aria-live="polite"></aside>
</div>
<script type="application/json" id="amapdata">{json.dumps({"towns": towns}, ensure_ascii=False)}</script>

<div class="qbar jsonly" id="list">
  <input type="search" id="q" placeholder="Search: archive, city, shelfmark, cipher, region…" aria-label="Search the requests">
  <span class="kf" role="group" aria-label="Kind"><button type="button" data-k="" aria-pressed="true">all kinds</button><button type="button" data-k="visit" aria-pressed="false">reading room</button><button type="button" data-k="order" aria-pressed="false">order</button><button type="button" data-k="library" aria-pressed="false">library</button></span>
  <span class="kf" role="group" aria-label="Source"><button type="button" data-s="" aria-pressed="true">everything</button><button type="button" data-s="gap" aria-pressed="false">readings stalled ({ngap})</button><button type="button" data-s="cat" aria-pressed="false">catalogue items ({ncat})</button></span>
  <span class="plchip" id="plchip" hidden><span></span><button type="button" aria-label="Show every place">&times;</button></span>
  <span class="count" id="count" aria-live="polite"></span>
  <span class="fold"><button type="button" id="openall">expand all</button><button type="button" id="closeall">collapse all</button></span>
</div>
<details class="toc"><summary>Jump to an archive ({len(G)})</summary><ul>{toc}</ul></details>
{secs}

<h2 id="done">Done</h2>
{done_html}

<h2>How it works</h2>
<p>Click <b>I can do this</b> on a request. It opens a short form on GitHub with the request filled in: say how you will do it (visit, order, library) and roughly when, by month. The request is then marked as taken on this page, so two people do not go for the same leaf. When you have the images or the text, send them on the same issue, or by <a href="contribute.html#email">email</a> if you do not use GitHub. Say whether the images may be shown on the site; they are always credited to you and to the archive.</p>
<p>Before photographing, check the archive&rsquo;s rules: most reading rooms allow it without flash, some ask for a form or a fee. A phone photograph of the whole page, flat, with the folio number visible, is enough for most requests; for a line in the gutter, one more of the page edge. Do not cut or mark anything to see better: say what you could not see and that closes the request too.</p>
<p>Something not listed? Use the same form to propose a request. Each one here comes either from a write-up&rsquo;s notes (its &ldquo;Remaining gaps&rdquo;, where the gap is marked as needing the archive) or from the <a href="catalogue.html">catalogue</a>, for every open item tagged &ldquo;needs archive scans&rdquo;; the list is rebuilt with the site. The ledger is <a href="{REPO}/blob/main/archive_requests.json" rel="noopener">archive_requests.json</a>. Credit works as for every contribution: <a href="contribute.html">contribute</a>.</p>
</main>
<!-- site:footer -->
<script>
(function(){{
document.body.classList.remove('nojs');
var rows=[].slice.call(document.querySelectorAll('li.rq')).filter(function(r){{return !r.closest('.done');}}),
 secs=[].slice.call(document.querySelectorAll('details.arch')),q=document.getElementById('q'),c=document.getElementById('count'),
 kb=[].slice.call(document.querySelectorAll('.kf button[data-k]')),sb=[].slice.call(document.querySelectorAll('.kf button[data-s]')),
 cards=[].slice.call(document.querySelectorAll('.kc')),k='',sr='',pl=null,t=rows.length,keep=secs.map(function(x){{return x.open;}}),
 chip=document.getElementById('plchip');
function press(list,a,v){{list.forEach(function(x){{x.setAttribute('aria-pressed',x.dataset[a]===v?'true':'false');}});}}
// pl: the town picked on the map (null: every place; '': the requests not on the map)
function others(r,s){{return (!s||r.dataset.q.indexOf(s)>=0)&&(!k||r.dataset.kind===k)&&(!sr||r.dataset.src===sr);}}
function render(){{
 var s=q.value.trim().toLowerCase(),n=0,f=!!(s||k||sr||pl!==null);
 rows.forEach(function(r){{var ok=others(r,s)&&(pl===null||r.dataset.pl===pl);r.hidden=!ok;if(ok)n++;}});
 secs.forEach(function(x,i){{var any=!!x.querySelector('li.rq:not([hidden])');x.hidden=!any;x.open=f?any:keep[i];}});
 c.textContent=f?n+' of '+t+' requests':t+' requests';
 chip.hidden=pl===null;chip.firstChild.textContent=pl===''?'not on the map':pl||'';
 if(window.archList.onchange)window.archList.onchange();
}}
// what the map reads: the requests per town under the other filters, and the town picked
window.archList={{place:function(){{return pl;}},
 counts:function(){{var s=q.value.trim().toLowerCase(),o={{}};rows.forEach(function(r){{if(others(r,s))o[r.dataset.pl]=(o[r.dataset.pl]||0)+1;}});return o;}},
 archives:function(){{return secs.filter(function(x){{return !x.hidden;}}).map(function(x){{return {{id:x.id,name:x.querySelector('h3').textContent,n:x.querySelectorAll('li.rq:not([hidden])').length}};}});}},
 pick:function(v){{pl=v;render();}},onchange:null}};
chip.querySelector('button').addEventListener('click',function(){{pl=null;render();}});
function setK(v){{k=v;press(kb,'k',v);press(cards,'k',v);render();}}
kb.forEach(function(b){{b.addEventListener('click',function(){{setK(b.dataset.k);}});}});
cards.forEach(function(b){{b.addEventListener('click',function(){{setK(k===b.dataset.k?'':b.dataset.k);}});}});
sb.forEach(function(b){{b.addEventListener('click',function(){{sr=b.dataset.s;press(sb,'s',sr);render();}});}});
q.addEventListener('input',render);
document.getElementById('openall').addEventListener('click',function(){{secs.forEach(function(x){{if(!x.hidden)x.open=true;}});}});
document.getElementById('closeall').addEventListener('click',function(){{secs.forEach(function(x){{x.open=false;}});}});
[].forEach.call(document.querySelectorAll('details.toc a'),function(a){{a.addEventListener('click',function(){{var d=document.querySelector(a.getAttribute('href'));if(d){{d.hidden=false;d.open=true;}}}});}});
render();
function hit(){{
 var hm=/^#(c\\d+)$/.exec(location.hash),he=hm&&document.getElementById(hm[1]);if(!he)return;
 if(he.hidden){{q.value='';k='';sr='';pl=null;press(kb,'k','');press(cards,'k','');press(sb,'s','');render();}}
 var hd=he.closest('details.arch');if(hd){{hd.hidden=false;hd.open=true;}}
 [].forEach.call(document.querySelectorAll('li.rq.hit'),function(x){{x.classList.remove('hit');}});he.classList.add('hit');he.scrollIntoView();
}}
hit();addEventListener('hashchange',hit);
}})();
</script>
<script src="https://cdn.jsdelivr.net/npm/d3@7.9.0/dist/d3.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/topojson-client@3.1.0/dist/topojson-client.min.js"></script>
<script src="archmap.js" defer></script>
</body>
</html>
'''
    (HERE / 'archives.html').write_text(page, encoding='utf-8')
    return len(live)


def requests_for(folder):
    """Open requests of one target, for the link from its further page."""
    return [r for r in load() if r.get('target') == folder and r['status'] in LIVE]
