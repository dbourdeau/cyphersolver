"""Site builder: one manifest drives the navigation, footers, tables of contents and index cards of every page.

Run  python _build_site.py  from docs/ after editing any page. It is idempotent.

Per page it: replaces the first <nav class="nav">...</nav> (or the <!-- site:nav --> marker) with the generated
header; replaces the last <footer>...</footer> (or <!-- site:footer -->) with the generated footer, including
previous / next links in chronological order; inserts an "On this page" contents strip after <main> when the page
has three or more h2 sections with ids; stamps the stylesheet and script versions; and removes inline <style>
blocks whose rules now live in style.css. On index.html it also regenerates the featured cards between
<!-- cards:start --> and <!-- cards:end -->, the ways to help and the routes into the write-ups. Every finding lives on
findings.html (add new entries at the top of its list and rebuild); index.html mirrors the newest RECENT_VISIBLE.

It also stamps the dates: the hero dateline, the head meta tags, the index cards, the list rows and each line
of findings.html all carry the day the finding landed, from _dates.json, which this script maintains.
"""
import os, re, sys, pathlib, html, json, hashlib, datetime
import _images as IMG
HERE = pathlib.Path(__file__).parent
ICONS = ('<link rel="icon" href="favicon.svg" type="image/svg+xml">\n<link rel="icon" href="favicon-32.png" sizes="32x32" type="image/png">\n'
         '<link rel="apple-touch-icon" href="apple-touch-icon.png">\n')
# stamped on the stylesheet and scripts: a hash of their content, so an edit reaches browsers without a bump and a
# rebuild with no CSS or JS change rewrites no page
VERSION = hashlib.sha1(b''.join((HERE / f).read_bytes().replace(b'\r\n', b'\n') for f in ('style.css', 'site.js', 'zoom.js', 'solve-replay.js', 'home.js'))).hexdigest()[:8]
SITE = 'Cyphersolver'
REPO = 'https://github.com/dbourdeau/cyphersolver'

# ---------------------------------------------------------------------------
# Datestamps.  _dates.json records, per page, the day the finding first landed
# in the repository and the day its text last really changed.  "Really" means
# the page body: nav, footer, contents strip, lead figure, the dateline itself
# and the version stamps are all generated here, so normalise() removes them
# before hashing.  A rebuild that only reshuffles that furniture therefore does
# not move the date.  Findings on findings.html are dated the same way, keyed by
# the bold lead-in of each entry, so a hand-added line dates itself on the next
# build.  Seed the file with _seed_dates.py; after that it maintains itself.
DATES_PATH = HERE / '_dates.json'
TODAY = datetime.date.today().isoformat()
# 'posted' (UTC, to the second) is when a write-up was submitted: stamped the first time a build sees the page,
# backfilled for older pages from the commit that first added them (tools/backfill_posted.py). It orders the
# Latest list in the Write-ups menu; 'first' alone would leave every page of one day tied.
NOW = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
MONTHS = ('January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December')
SHORT = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec')
# what the first date means, by status class
VERB = {'solved': 'solved', 'found': 'resolved', 'partial': 'read in part', 'stuck': 'attempted'}
def verb_of(p):
    """Byline verb. st 'solved' covers both outcomes that meet the read bar: 'solved' (key broken here) and
    'read' (an existing key or decipherment); the badge text says which, and the verb follows it."""
    if p.get('method'): return 'posted'      # the outcome line under the dateline carries method and extent
    plain_stt = re.sub(r'<[^>]+>|&[a-z]+;', '', p['stt']).strip()
    if p['st'] == 'solved' and not plain_stt.startswith('solved'): return 'read'
    if p['st'] == 'partial' and plain_stt.startswith('solved'): return 'solved in part'
    return VERB.get(p['st'], 'posted')
VERB_SHORT = {'partial': 'part read'}      # the card and list stamps have less room

def fmt_date(iso, short=False):
    y, m, d = (int(x) for x in iso.split('-'))
    return f'{d} {(SHORT if short else MONTHS)[m-1]} {y}'

FINDINGS_REGION = re.compile(r'<h2 id="recent">.*?(?=\n<h2|\n<!-- |\Z)', re.S)
GENERATED = [
    r'<header class="nav">.*?</header>', r'<div class="search" id="search".*?</div>\n</div>', r'<nav class="nav">.*?</nav>', r'<footer.*?</footer>',
    r'<nav class="toc".*?</nav>', r'<figure class="lead">.*?</figure>',
    r'<!-- cards:start -->.*?<!-- cards:end -->', r'<!-- site:(?:nav|footer) -->',
    r'<script src="site\.js[^"]*"></script>',
    r'\n?<div class="seal [a-z]+" aria-hidden="true">.*?</div>',
    r'\n?<div class="parties">.*?</div><!-- /parties -->',
    r'<!-- replay:start -->.*?<!-- replay:end -->\n?', r'<script src="solve-replay\.js[^"]*" defer></script>\n?',
    r'<script src="zoom\.js[^"]*" defer></script>\n?',
    r'<!-- live:start -->.*?<!-- live:end -->\n?', r'<script src="home\.js[^"]*" defer></script>\n?',
    r'<meta name="(?:date|last-modified)"[^>]*>', r'<link rel="(?:icon|apple-touch-icon)"[^>]*>',
    r'\n?<!-- bnx -->.*?<!-- /bnx -->', r' data-bnx="1"', r'<span class="fth">.*?</span><!-- /fth -->',
    r'<!-- cattop:start -->.*?<!-- cattop:end -->\n?',
    r'<!-- help:start -->.*?<!-- help:end -->\n?', r'<!-- browse:start -->.*?<!-- browse:end -->\n?', r' data-mirror',
    r'<!-- lasry:start -->.*?<!-- lasry:end -->\n?',
    r'\n?<p class="outcome">.*?</p><!-- /outcome -->',
    r'\n?<p class="credits">.*?</p><!-- /credits -->', r'<!-- contrib:start -->.*?<!-- contrib:end -->\n?',
    r'<link rel="stylesheet" href="pg-[a-z]+\.css[^"]*">\n?', r'\n?<p class="readjump">.*?</p><!-- /readjump -->',r'<!-- cite:start -->.*?<!-- cite:end -->\n?', r'<!-- social:start -->.*?<!-- social:end -->\n?',
]

def normalise(s):
    """The page as content: everything this script generates removed, whitespace flattened."""
    def fold(m):        # the findings list is re-split on every build; compare the entries alone
        r = m.group(0)
        r = re.sub(r'</?ul class="findings">|</ul>|<div class="more" hidden>|</div>|'
                   r'<button class="showmore".*?</button>', ' ', r, flags=re.S)
        return r
    s = FINDINGS_REGION.sub(fold, s)
    s = re.sub(r'<time class="fdate"[^>]*>.*?</time>', '', s, flags=re.S)   # inserted flush, remove flush
    s = re.sub(r'<p class="meta">.*?</p>', ' ', s, count=1, flags=re.S)     # the hero dateline only: some pages
                                                                           # use .meta again in the body for notes
    s = re.sub(r'(?<![\w-])(?:targets|research)/', '', s)   # repo paths gained these prefixes on 26 Sept 2026; a move is not an edit
    s = re.sub(r'\?v=\w+', '', s)      # version stamps vanish without a trace, so a newly stamped src hashes as before
    s = s.replace(' translate="no"', '')       # added by protect_text(); not an edit
    s = re.sub(r' ?<span class="credit">[^<]*</span>| data-credit="[^"]*"', '', s)   # figure credits, added flush
    s = IMG.ADDED.sub('', s)                   # image sizes and srcset (_images.py), added flush
    s = re.sub(r'(<meta name="description" content=")[^"]*" data-full="([^"]*)">', r'\1\2">', s)   # the hand-written description is the content
    for pat in GENERATED: s = re.sub(pat, ' ', s, flags=re.S)
    return re.sub(r'\s+', ' ', s).strip()

def content_hash(s):
    return hashlib.sha1(normalise(s).encode('utf-8')).hexdigest()[:12]

def load_dates():
    try: return json.loads(DATES_PATH.read_text(encoding='utf-8'))
    except FileNotFoundError: return {'pages': {}, 'findings': {}}

def save_dates(d):
    DATES_PATH.write_text(json.dumps(d, indent=1, sort_keys=True, ensure_ascii=False) + '\n', encoding='utf-8')

DATES = load_dates()

def page_dates(slug, s):
    """Record and return {'first', 'updated'} for a page, moving 'updated' when the body changed."""
    h = content_hash(s)
    rec = DATES['pages'].get(slug)
    if rec is None: rec = DATES['pages'][slug] = {'first': TODAY, 'updated': TODAY, 'hash': h, 'posted': NOW}
    elif rec.get('hash') != h: rec['updated'], rec['hash'] = TODAY, h
    return rec

DATEISH = re.compile(r'^(?:solved(?: in part)?|resolved|attempted|posted|read(?: in part)?|published|first published|updated)?'
                     r'\s*(?:\d{1,2}\s+)?(?:' + '|'.join(MONTHS) + r'|Sept?)?\s*\d{4}$', re.I)

SHARED_PAGES = ('index', 'findings', 'contributors', 'contribute')      # pages of the ledger as a whole, not of one write-up
def meta_html(p, rec, old, slug=None):
    """Rebuild the hero dateline, keeping whatever else the page put on that line."""
    author = (p.get('author') if p else None) or ('Daniel Bourdeau and contributors' if slug in SHARED_PAGES else 'Daniel Bourdeau')
    keep = []
    for part in re.split(r'\s*(?:&middot;|·)\s*', old or '')[1:]:
        flat = re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', '', part))).strip()
        if flat and not DATEISH.match(flat): keep.append(part.strip())
    verb = verb_of(p) if p else 'posted'
    if p and p['slug'] in SURVEYS: verb = 'posted'
    bits = [author, f'{verb} <time datetime="{rec["first"]}">{fmt_date(rec["first"])}</time>']
    if rec['updated'] != rec['first']:
        bits.append(f'updated <time datetime="{rec["updated"]}">{fmt_date(rec["updated"])}</time>')
    return '<p class="meta">' + ' &middot; '.join(bits + keep) + '</p>'

def finding_key(li):
    """A findings entry is identified by its bold lead-in, which does not change when the text is edited."""
    m = re.search(r'<b>(.*?)</b>', li, re.S)
    text = re.sub(r'<[^>]+>', '', m.group(1) if m else li[:160])
    return re.sub(r'\s+', ' ', html.unescape(text)).strip().lower()[:80]

def stamp_finding(li):
    li = re.sub(r'<time class="fdate"[^>]*>.*?</time>\s*', '', li, flags=re.S)
    key = finding_key(li)
    iso = DATES['findings'].setdefault(key, TODAY)
    stamp = f'<time class="fdate" datetime="{iso}">{fmt_date(iso, short=True)}</time>'
    li = re.sub(r'<span class="fth">.*?</span><!-- /fth -->', '', li, flags=re.S)
    slugs = [x for x in re.findall(r'href="([a-z0-9]+)\.html', li) if any(q['slug'] == x for q in PAGES)]
    th = mini_thumb(slugs[-1], 'fth') if slugs else ''
    if th: stamp = th + '<!-- /fth -->' + stamp
    return li.replace('<li>', '<li>' + stamp, 1)

# The manifest (PAGES, one entry per write-up; IMAGES, the lead figures) is data and lives in _manifest.py.
from _manifest import PAGES, IMAGES

SURVEYS = ('solved', 'highlights', 'top25')
# Outcome method (George Lasry's categories, _methods.py): a page whose target has a profile with outcome.method
# takes its badge, colour, seal and byline verb from the profile, so the hand-typed st/stt above only stand for
# surveys, famous targets and pages without a classified profile.  p['method'] / p['extent'] drive the filters.
import _methods as M
PROFILE_SLUG = {'bordeaux': 'bordeaux1653'}      # profile folder -> page slug, where they differ beyond case
def attach_methods():
    paths = M.profile_paths()
    by_slug = {PROFILE_SLUG.get(k, k): v for k, v in paths.items()}
    for p in PAGES:
        p['method'] = p['extent'] = p['frac'] = None
        p['parts'] = []                                  # (label, method, extent) when a page reports several targets
        if p['slug'] in SURVEYS: continue
        cls = None
        if p['slug'] in M.PAGE_PROFILES:
            profs = [(f, M.load(paths[f])) for f in M.PAGE_PROFILES[p['slug']] if f in paths]
            parts = [(f, pr['outcome']['method'], M.extent(pr)) for f, pr in profs if pr and pr.get('outcome', {}).get('method') in M.METHODS]
            if not parts: continue
            p['parts'] = parts
            p['method'], p['extent'] = min(parts, key=lambda t: M.METHODS.index(t[1]))[1:]
            if any(e == 'partial' for _, _, e in parts): p['extent'] = 'partial'
        elif p['slug'] in M.PAGE_METHOD:
            p['method'], p['extent'], _ = M.PAGE_METHOD[p['slug']]
        else:
            prof = M.load(by_slug[p['slug']]) if p['slug'] in by_slug else None
            out = (prof or {}).get('outcome') or {}
            if out.get('method') not in M.METHODS: continue
            p['method'], p['extent'], cls = out['method'], M.extent(prof), out.get('class')
            if len(out.get('parts') or []) > 1:           # a split entry: each part has its own method (README Conventions)
                p['parts'] = [(x['label'], x['method'], x['extent']) for x in out['parts']]
            p['frac'] = out.get('fraction_coherent') if isinstance(out.get('fraction_coherent'), (int, float)) else                         out.get('fraction_read') if isinstance(out.get('fraction_read'), (int, float)) else None
        p['stt_hand'] = p['stt']
        p['st'] = M.status_class(p['method'], p['extent'])
        p['stt'] = M.badge(p['method'], p['extent'], cls)


def outcome_html(p):
    """The hero's outcome line: method linked to its glossary entry, and extent."""
    m = p.get('method')
    if not m: return ''
    ext = {'complete': 'complete', 'partial': 'partial', 'none': 'text not obtained', 'n/a': ''}[p['extent']]
    if p['extent'] == 'partial' and p.get('frac'):
        pct = 100 * p['frac']
        # a partial reading must not round up to the bar or to 100% (94.7% shown as 95%, 99.5% as 100%)
        shown = f'{pct:.1f}' if round(pct) != int(pct) and (round(pct) >= 95 > pct or round(pct) == 100 > pct) else str(round(pct))
        ext += f' ({shown}% of the cipher)'
    if M.key_only(m, p['extent']): ext = 'none (key obtained, text not read)'   # George Lasry, 24 Oct 2026
    if p.get('parts') and len({x[1] for x in p['parts']}) > 1:      # several targets, several methods
        bits = [f'{f}: <a href="glossary.html#{M.KEY[pm]}">{pm}</a> ({pe})' for f, pm, pe in p['parts']]
        return '<p class="outcome">Method &middot; ' + ' &middot; '.join(bits) + '</p><!-- /outcome -->'
    bits = [f'Method: <a href="glossary.html#{M.KEY[m]}">{m if m != M.NA else plain(p["stt"])}</a>']
    if ext: bits.append(f'Extent: {ext}')
    return '<p class="outcome">' + ' &middot; '.join(bits) + '</p><!-- /outcome -->'

attach_methods()

# Credits (_credits.py): who besides the project contributed to each page's target(s), from profile outcome.credits.
import _credits as CR
CONTRIB = CR.registry()
PROFILES = CR.load_all()
def attach_credits():
    by_slug = {}
    for folder in PROFILES: by_slug.setdefault(PROFILE_SLUG.get(folder, folder), []).append(folder)
    for slug, folders in M.PAGE_PROFILES.items(): by_slug[slug] = folders
    for p in PAGES:
        p['folders'] = [f for f in by_slug.get(p['slug'], []) if f in PROFILES]
        p['credits'] = [c for f in p['folders'] for c in CR.credits_of(PROFILES[f])]
        provs = {CR.provenance_of(PROFILES[f]) for f in p['folders']}
        p['provenance'] = 'contributed' if provs == {'contributed'} else 'mixed' if provs & {'contributed', 'mixed'} else 'project'
attach_credits()
FOLDER_PAGE = {f: p for p in PAGES for f in p['folders']}

# Full texts (George Lasry, 22 Oct 2026): a reading shows the transcription and decryption of every document it reports
# on, and the key when the project changed it, from profile outcome.texts / outcome.key_file (_texts.py).
import _texts as TX
REPO_BLOB = 'https://github.com/dbourdeau/cyphersolver/blob/main/'
TEXT_INLINE_MAX = 16000          # bytes: shorter files are shown on the page, longer ones linked
def texts_html(page):
    paths = M.profile_paths()
    out = []
    for f in page.get('folders') or []:
        prof = PROFILES.get(f) or {}
        o = prof.get('outcome') or {}
        if not o.get('texts') and not o.get('key_file'): continue
        base = paths[f].parent
        rel = base.resolve().relative_to(HERE.resolve().parent).as_posix()
        docs = {d.get('id'): d for d in prof.get('documents') or []}
        def link(p):
            return p if str(p).startswith('http') else REPO_BLOB + rel + '/' + str(p)
        def show(kind, p):
            name = html.escape(pathlib.PurePosixPath(str(p)).name)
            if str(p).startswith('lasry/report/'):     # shown in full in George Lasry's report at the top of the page
                return (f'<p class="ftext">{kind}: in full above, in <a href="#lasry-report">George Lasry&rsquo;s decipherment</a> '
                        f'(<a href="{link(p)}">{name}</a>)</p>')
            fp = None if str(p).startswith('http') else base / p
            # size with LF line ends, so a Windows (CRLF) checkout and the Linux CI build make the same page
            if fp and fp.is_file() and fp.suffix.lower() in ('.txt', '.md', '.tsv', '') and len(fp.read_bytes().replace(b'\r\n', b'\n')) <= TEXT_INLINE_MAX:
                body = html.escape(fp.read_text(encoding='utf-8', errors='replace').rstrip())
                return (f'<details class="ftext"><summary>{kind}</summary><p class="muted"><a href="{link(p)}">{name}</a></p>'
                        f'<pre>{body}</pre></details>')
            return f'<p class="ftext">{kind}: <a href="{link(p)}">{name}</a></p>'
        for t in o.get('texts') or []:
            ids = TX.listify(t.get('doc'))
            labels = []
            for i in ids:
                d = docs.get(i) or {}
                bits = [b for b in (d.get('shelfmark'), d.get('date')) if b]
                labels.append(html.escape(i if i != 'all' else 'All documents') + (f' <span class="muted">({html.escape(", ".join(map(str, bits)))})</span>' if bits else ''))
            head = html.escape(t['label']) if t.get('label') else ('; '.join(labels) or 'Texts')
            # a mechanical decode that does not yet build sentences is shown for checking, labelled as such (Lasry, 22 Oct 2026)
            state = TX.entry_state(t)
            tag = {'decoded, not read': ' <span class="st stuck">decoded, not read</span>',
                   'read in part': ' <span class="st partial">read in part</span>',
                   'not prose': ' <span class="st found">not prose</span>'}.get(state, '')
            out.append(f'<h3>{head}{tag}</h3>')
            if t.get('summary'): out.append(f'<p>{html.escape(t["summary"])}</p>')
            if state == 'read in part':
                rs = t.get('read_share')
                out.append('<p class="muted">Builds coherent sentences, but ' + ('its word share is at or above the 95% read bar, and it stays read in part for another reason stated on this page' if isinstance(t.get('read_share'), (int, float)) and t['read_share'] >= 0.95 else 'under the read bar of 95% of words read as sense')
                           + (f' ({rs * 100:.1f}% here)' if isinstance(rs, (int, float)) and 0.945 <= rs < 0.95 else f' ({rs * 100:.0f}% here)' if isinstance(rs, (int, float)) else '') + '; the holes are marked in the reading.</p>')
            if state == 'decoded, not read':
                out.append('<p class="muted">A mechanical decode with holes in most sentences: shown so that the transcription '
                           'and the key can be checked and improved, not as a reading.</p>')
            if t.get('transcription_missing') and not t.get('transcription'):
                out.append(f'<p class="ftext">Transcription: none of the cipher. {html.escape(t["transcription_missing"])}</p>')
            for kind, key in (('Transcription', 'transcription'), ('Decipherment of the time', 'contemporary'), ('Decryption', 'decryption'),
                              ('Reading', 'reading'), ('Translation', 'translation')):
                for p in TX.listify(t.get(key)): out.append(show(kind, p))
        keys = TX.listify(o.get('key_file'))
        if keys:
            out.append('<p class="ftext">Key: ' + ', '.join(f'<a href="{link(k)}">{html.escape(pathlib.PurePosixPath(str(k)).name)}</a>' for k in keys) + '</p>')
    if not out: return ''
    return ('<!-- texts:start -->\n<h2 id="texts">Full texts</h2>\n<p>The transcription and the decryption of every document on '
            'this page, so that the reading can be used and checked. Short files are shown here; all are in the repository.</p>\n'
            + '\n'.join(out) + '\n<!-- texts:end -->\n')

# George Lasry's report (24 Oct 2026): "Make sure the decryption and translation are on the relevant page, immediately
# visible, and not buried under a link ... Same for the reconstructed key. ... the closer the page to the format in the
# PDF, the better." A target with targets/<folder>/lasry/report/ (research/reading_audit/lasry_pdf_extract.py) gets his
# report at the top of the page body, in the PDF's order and wording: the summary, the key, Excerpt and Translation side
# by side, the full Readable text, inline. The page's own sections (Verification, Other contributions, Sources) follow.
LR_START, LR_END = '<!-- lasry:start -->', '<!-- lasry:end -->'
LR_MAXW = 1600         # px: report images are copied to docs/lasry/<folder>/ at most this wide

def lr_inline(s):
    s = html.escape(s, quote=False)
    s = re.sub(r'\*\*(.+?)\*\*', r'<b class="dec">\1</b>', s)
    s = re.sub(r'&lt;(https?://[^&\s]+)&gt;', r'<a href="\1" rel="noopener">\1</a>', s)
    return s

def lr_copy(src, dst):
    """Copy a report image into docs/ as a JPEG scaled down to LR_MAXW; returns (width, height) as published.
    The copy is redone only when the source's content changes (sha1 in docs/lasry/<folder>/sources.json), not on file
    times: a fresh checkout gives every file a new mtime, and comparing them rewrote all the copies on each build."""
    import hashlib
    man_f = dst.parent / 'sources.json'
    man = json.loads(man_f.read_text(encoding='utf-8')) if man_f.is_file() else {}
    sha = hashlib.sha1(src.read_bytes()).hexdigest()
    try:
        from PIL import Image
        if dst.exists() and man.get(dst.name) == sha:
            return Image.open(dst).size
        im = Image.open(src)
        w, h = im.size
        dst.parent.mkdir(parents=True, exist_ok=True)
        if w > LR_MAXW:
            im = im.resize((LR_MAXW, round(h * LR_MAXW / w)), Image.LANCZOS); w, h = im.size
        im.convert('RGB').save(dst, quality=85, optimize=True)
    except ImportError:
        if dst.exists() and man.get(dst.name) == sha: return None, None
        dst.parent.mkdir(parents=True, exist_ok=True); dst.write_bytes(src.read_bytes()); w = h = None
    man[dst.name] = sha
    man_f.write_text(json.dumps(man, indent=1, sort_keys=True) + '\n', encoding='utf-8')
    return w, h

def lasry_report_html(page):
    out = []
    for f in page.get('folders') or []:
        paths = M.profile_paths()
        base = paths[f].parent if f in paths else HERE.parent / 'targets' / f
        rd = base / 'lasry' / 'report'
        if not (rd / 'report.json').is_file(): continue
        r = json.loads((rd / 'report.json').read_text(encoding='utf-8'))
        rel = rd.resolve().relative_to(HERE.resolve().parent).as_posix()
        shelf = re.split(r' [—–-] |, ', r['title'])[0].strip()
        bnf = f'Biblioth&egrave;que nationale de France, {html.escape(shelf)}'
        gal = {g['label']: g['url'] for g in r.get('gallica') or [] if g.get('label')}
        def fig(rec, credit, cap, cls=''):
            src = rd / rec['file']
            name = f'lasry/{f}/{pathlib.PurePosixPath(rec["file"]).stem}.jpg'
            w, h = lr_copy(src, HERE / name)
            wh = f' width="{w}" height="{h}"' if w else ''
            alt = html.escape(html.unescape(re.sub(r'<[^>]+>', '', cap)))
            return (f'<figure{cls} data-credit="{credit}"><img src="{name}" alt="{alt}"{wh} loading="lazy">'
                    f'<figcaption>{cap}</figcaption></figure>')
        def leaf_credit(folio):
            fo = re.match(r'(f\d+[rv]|p\d+)', folio or '')
            return (f'{bnf}' + (f', {fo.group(1)}' if fo else '') + ', via Gallica'
                    + '; crop from George Lasry&rsquo;s report')
        pdf = f'{REPO_BLOB}{rel}/{r["pdf"]}'
        out.append(f'<p class="lr-src">George Lasry&rsquo;s report on this item, as he sent it on {fmt_date(r["received"])} '
                   f'(<a href="{pdf}">PDF</a>), in its own order and wording. The decipherment, the translation and the '
                   'reconstruction of the key are his, made with ChatGPT Astra 6 and Anthropic Opus 5.5. This project&rsquo;s '
                   'own checks follow under <a href="#verification">Verification</a>.</p>')
        # the summary page
        s = [f'<div class="lr-summary"><h3>{html.escape(r["title"])}</h3>']
        if r.get('contents'): s.append(f'<p><b>Contents:</b> {lr_inline(r["contents"])}</p>')
        if r.get('status'): s.append(f'<p class="lr-status">{lr_inline(r["status"])}</p>')
        if r.get('fields'):
            s.append('<dl>' + ''.join(f'<dt>{html.escape(k)}:</dt><dd>{lr_inline(v)}</dd>' for k, v in r['fields']) + '</dl>')
        for x in r.get('extra') or []: s.append(f'<p>{lr_inline(x)}</p>')
        if r.get('gallica'):
            s.append('<p class="lr-links">' + ' &middot; '.join(
                f'<a href="{html.escape(g["url"])}" rel="noopener">Gallica {html.escape(g["label"])}</a>' for g in r['gallica']) + '</p>')
        s.append('</div>')
        out.append('\n'.join(s))
        for rec in [i for i in r.get('images') or [] if i['kind'] == 'key']:
            out.append(fig(rec, f'key reconstructed by George Lasry (report, {fmt_date(r["received"])}); sign images: {bnf}, via Gallica',
                           'The reconstructed key, from George Lasry&rsquo;s report.', ' class="keytab"'))
        # Excerpt and Translation
        if r.get('excerpts'):
            out.append('<h3 id="lasry-excerpt">Excerpt and Translation</h3>')
            for e in r['excerpts']:
                if e.get('folio'): out.append(f'<p class="exwhere">{html.escape(e["folio"])}</p>')
                for im in e.get('images') or []:
                    rec = next((i for i in r['images'] if i['file'] == im), None)
                    fo = re.match(r'(f\d+[rv]|p\d+)', e.get('folio') or '')
                    url = gal.get(fo.group(1)) if fo else None
                    see = f' <a href="{html.escape(url)}" rel="noopener">Gallica {fo.group(1)}</a>.' if url else ''
                    if rec: out.append(fig(rec, leaf_credit(e.get('folio')), f'The manuscript lines of the excerpt ({html.escape(e.get("folio") or "")}).{see}'))
                ex = ''.join(f'<p>{lr_inline(x)}</p>' for x in e.get('excerpt') or [])
                tr = ''.join(f'<p>{lr_inline(x)}</p>' for x in e.get('translation') or [])
                out.append(f'<div class="lr-pair"><div class="lr-excerpt"><h4>Excerpt</h4>{ex}</div>' + (f'<div><h4>Translation</h4>{tr}</div>' if tr else '') + '</div>')
        # Readable text, in full
        rt = (rd / 'readable.md').read_text(encoding='utf-8')
        body = ['<h3 id="lasry-readable">Readable text</h3>',
                '<p class="muted">The full text, folio by folio, as in the report. Bold marks the passages deciphered from the '
                'cipher; the rest is the clear text of the letter. Question marks are the report&rsquo;s: [?] or a bare ? for a sign or group left unread, a ? after a word for a doubtful reading.</p>', '<div class="lr-readable">']
        for blk in re.split(r'\n\s*\n', rt):
            blk = blk.strip()
            if not blk or blk.startswith('<!--'): continue
            if blk.startswith('# '): body.append(f'<p class="lr-doc">{lr_inline(blk[2:])}</p>'); continue
            if blk.startswith('## '): body.append(f'<h4>{lr_inline(blk[3:])}</h4>'); continue
            m = re.match(r'!\[([^\]]*)\]\(([^)]+)\)$', blk)
            if m:
                rec = next((i for i in r['images'] if i['file'] == m.group(2)), None)
                if rec: body.append(fig(rec, f'as reproduced in George Lasry&rsquo;s report ({html.escape(rec.get("caption") or "")})', html.escape(rec.get('caption') or 'From the report.')))
                continue
            body.append('<p>' + lr_inline(blk).replace('\n', '<br>') + '</p>')
        body.append('</div>')
        out.extend(body)
        if (rd / 'key.md').is_file():
            k = (rd / 'key.md').read_text(encoding='utf-8').split('\n', 2)[-1]
            out.append(f'<h3 id="lasry-key">Reconstructed key</h3>\n<pre class="lr-key">{html.escape(k.strip())}</pre>')
    if not out: return ''
    return (f'{LR_START}\n<section class="lreport">\n<h2 id="lasry-report">George Lasry&rsquo;s decipherment</h2>\n'
            + '\n'.join(out) + f'\n</section>\n{LR_END}\n')

def credits_html(p):
    """The hero's credits line: everyone credited on the page's target(s), grouped by person, linked to contributors.html."""
    cs = [c for c in p.get('credits') or [] if c.get('who') in CONTRIB]
    if not cs: return ''
    people = {}
    for c in cs:
        roles = people.setdefault(c['who'], [])
        label = 'unpublished earlier solution' if c['role'] == 'prior solution' and c.get('published') is False else CR.ROLE_LABEL[c['role']]
        if label not in roles: roles.append(label)
    order = sorted(people, key=lambda w: (CONTRIB[w]['kind'] != 'person', min(CR.ROLES.index(c['role']) for c in cs if c['who'] == w)))
    bit = lambda w: f'<a href="contributors.html#{w}">{html.escape(CONTRIB[w]["name"])}</a> ({", ".join(people[w])})'
    # a contributed or mixed result names its contributors first, then everyone else credited
    outside = [w for w in order if p.get('provenance') in ('contributed', 'mixed') and CONTRIB[w]['kind'] == 'person'
               and any(c['who'] == w and c['role'] not in ('pointer', 'prior solution') for c in cs)]
    rest = [w for w in order if w not in outside]
    parts = []
    if outside: parts.append(('Contributed by ' if p['provenance'] == 'contributed' else 'With ') + ' and '.join(bit(w) for w in outside))
    if rest: parts.append(('Also credited' if outside else 'Credits') + ' &middot; ' + ' &middot; '.join(bit(w) for w in rest))
    return '<p class="credits">' + ' &middot; '.join(parts) + '</p><!-- /credits -->'

# chip value on writeups.html, menu label, badge class, predicate
GROUPS = [(M.KEY[m], M.LABEL[m][0].upper() + M.LABEL[m][1:], M.status_class(m, 'complete'), (lambda m: lambda p: p.get('method') == m)(m))
          for m in M.METHODS] + [
          ('other', 'Not yet classified', 'todo', lambda p: not p.get('method') and p['slug'] not in SURVEYS),
          ('survey', 'Surveys', 'todo', lambda p: p['slug'] in SURVEYS)]
# the Explore menu: the pages that are not write-ups (slug, label, one line)
EXPLORE = [('highlights', 'Highlights', 'Thirty favourites: the funny, the historic, the ingenious'),
           ('glossary', 'Glossary', 'How each cipher was solved, and the terms used'),
           ('top25', 'Top 25 unsolved ciphers', 'Twenty-five ciphers with no accepted reading, ranked'),
           ('atlas', 'Atlas', 'Every letter drawn on the map, five centuries of it'),
           ('keys', 'Key web', 'Which key opened which letter'),
           ('secret', 'Secret letter', 'Seal a message in a real historical cipher')]
CHEVRON = ('<svg width="10" height="7" viewBox="0 0 10 7" aria-hidden="true"><path d="M1 1l4 4 4-4" fill="none" '
           'stroke="currentColor" stroke-width="1.6"/></svg>')
# the same groups named in a word or two, for the two-column outcome grid in the phone menu
NAV_SHORT = {'ct': 'Ciphertext-only', 'extpt': 'Ext. plaintext', 'adjpt': 'Adj. plaintext', 'extkey': 'External key',
             'known': 'Known key', 'deciph': 'Existing reading', 'notsolved': 'Not solved', 'na': 'Not applicable',
             'other': 'Unclassified', 'survey': 'Surveys'}
NAV_LATEST = 6          # write-ups shown in the menu; the rest are one click away on writeups.html

def kind_of(p): return 'survey' if p['slug'] in SURVEYS else M.KEY[p['method']] if p.get('method') else 'other'

def posted_at(slug):
    """Submission time of a write-up for the Latest list: 'posted', else the first day at midnight."""
    rec = DATES['pages'].get(slug, {})
    return rec.get('posted') or (rec.get('first', TODAY) + 'T00:00:00Z')

def write_menu():
    """menu.json: the two changing groups of the Write-ups menu, fetched by site.js."""
    latest = sorted([p for p in PAGES if p['slug'] not in SURVEYS],
                    key=lambda p: posted_at(p['slug']), reverse=True)[:NAV_LATEST]
    # each row: a coloured dot for the outcome, the label, the year; the method under it in plain text, not a pill
    lis = ''.join(f'<li><a href="{p["slug"]}.html"><i class="dot {p["st"]}" aria-hidden="true"></i>'
                  f'<b>{p["label"]}</b><span class="yr">{p["year"]}</span><span class="m">{p["stt"]}</span></a></li>' for p in latest)
    groups = ''.join(f'<li><a href="writeups.html#kind={key}"><i class="dot {cls}" aria-hidden="true"></i>'
                     f'<b>{name}</b><b class="sh">{NAV_SHORT.get(key, name)}</b><span class="n">{n}</span></a></li>' for key, name, cls, pred in GROUPS if (n := sum(1 for p in PAGES if pred(p))))
    menu = dict(groups=f'<div class="grp latest"><h4>Latest</h4><ul>{lis}</ul></div><div class="grp outc"><h4>By outcome</h4><ul>{groups}</ul></div>',
                all=f'All {len(PAGES)} write-ups, with filters \u2192')
    (HERE / 'menu.json').write_text(json.dumps(menu, ensure_ascii=False, separators=(',', ':')), encoding='utf-8')

def nav_html(current):
    """The Write-ups menu. It stopped listing every page when the count passed forty: it now shows the newest few,
    the counts by outcome (each a link into the filtered index) and the way to the full list on writeups.html."""
    cur = lambda slug: ' aria-current="page"' if slug == current else ''
    in_explore = any(slug == current for slug, _, _ in EXPLORE)
    on = ' class="active"' if not in_explore and (current == 'writeups' or any(p['slug'] == current for p in PAGES)) else ''
    # Latest and By outcome change with every new write-up, so they live in menu.json (site.js fills them in) and a new
    # write-up no longer rewrites every page; without JavaScript the menu still has these links
    panel = (f'<div class="foot"><a class="all" href="writeups.html"{cur("writeups")}>All write-ups, with filters &rarr;</a>'
             f'<a href="findings.html"{cur("findings")}>All findings, newest first</a>'
             f'<a href="writeups.html#src=notes">Results only in the notes</a></div>')
    explore = (''.join(f'<li><a href="{slug}.html"{cur(slug)}><b>{name}</b><span class="d">{desc}</span></a></li>'
                       for slug, name, desc in EXPLORE).join(('<ul>', '</ul>'))
               + f'<div class="foot"><a href="{REPO}" rel="noopener">The code and the working notes on GitHub &#8599;</a></div>')
    return (
        f'<header class="nav"><a class="skip" href="#content">Skip to content</a><div class="in">\n'
        f'  <a class="brand" href="index.html"><span class="glyph">972</span><span>{SITE}</span></a>\n'
        f'  <button class="navtoggle" type="button" aria-expanded="false" aria-controls="sitemenu"><span></span><span></span><span></span><i>Menu</i></button>\n'
        f'  <nav id="sitemenu" class="links" aria-label="Site">\n'
        f'    <details class="menu"><summary{on}>Write-ups {CHEVRON}</summary>\n'
        f'      <div class="panel wp">{panel}</div></details>\n'
        f'    <details class="menu"><summary{" class=\"active\"" if in_explore else ""}>Explore {CHEVRON}</summary>\n'
        f'      <div class="panel ex">{explore}</div></details>\n'
        f'    <a class="navcat" href="catalogue.html"{cur("catalogue")}>Catalogue<span class="sticker" aria-hidden="true"><span><b>Help<br>Solve!</b></span></span></a>\n'
        f'    <a class="navcat" href="further.html"{cur("further")}>Read further<span class="sticker alt" aria-hidden="true"><span><b>Finish<br>It!</b></span></span></a>\n'
        f'    <a class="navcat" href="archives.html"{cur("archives")}>To the archive<span class="sticker arc" aria-hidden="true"><span><b>Go<br>Look!</b></span></span></a>\n'
        f'    <a href="contributors.html"{cur("contributors")}>Contributors</a>\n'
        f'    <button class="searchbtn" type="button" aria-label="Search the site" aria-keyshortcuts="/ Control+K"><svg width="14" height="14" viewBox="0 0 16 16" aria-hidden="true"><circle cx="6.8" cy="6.8" r="5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M10.5 10.5L15 15" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg><span>Search</span><kbd>/</kbd></button>\n'
        f'    <button class="theme" type="button" aria-label="Switch between dark and light" title="Dark / light"><svg width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><circle cx="8" cy="8" r="6.2" fill="none" stroke="currentColor" stroke-width="1.5"/><path d="M8 1.8a6.2 6.2 0 0 1 0 12.4z" fill="currentColor"/></svg></button>\n'
        f'  </nav>\n</div><span id="content" tabindex="-1"></span></header>\n' + SEARCH_HTML)

SEARCH_HTML = (
    '<div class="search" id="search" hidden>\n'
    '  <div class="sbox" role="dialog" aria-modal="true" aria-label="Search the site">\n'
    '    <form class="sform" role="search" onsubmit="return false">\n'
    '      <svg width="18" height="18" viewBox="0 0 16 16" aria-hidden="true"><circle cx="6.8" cy="6.8" r="5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M10.5 10.5L15 15" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>\n'
    '      <input type="search" id="sq" placeholder="Search names, places, shelfmarks, words of the cipher&hellip;" autocomplete="off" spellcheck="false" aria-label="Search" aria-controls="sres">\n'
    '      <button type="button" class="sclose" aria-label="Close search">Esc</button>\n'
    '    </form>\n'
    '    <div class="sres" id="sres" role="listbox" aria-label="Results"></div>\n'
    '    <div class="shint"><span><kbd>&uarr;</kbd><kbd>&darr;</kbd> move</span><span><kbd>&crarr;</kbd> open</span><span><kbd>Esc</kbd> close</span><span class="sn" id="sn"></span></div>\n'
    '  </div>\n</div>')

# ---------------------------------------------------------------------------
# writeups.html: every write-up, filterable, followed by the results that exist only as notes in the repository.
# The second list is read from ../README.md, whose Results tables are the ledger every session keeps: a row whose
# "Where" column links to a site page is a write-up (checked against PAGES), any other row is notes only.
# century keys are the ones the catalogue.html Century facet uses, so a #century=1600s link works on both pages
CENTURIES = [('early', 'before 1400')] + [(f'{c}00s', f'{c}00s') for c in range(14, 20)] + [('undated', 'undated')]
KINDS = [(M.KEY[m], M.LABEL[m]) for m in M.METHODS] + [('active', 'in progress'), ('other', 'not yet classified'), ('survey', 'survey')]
EXTENTS = [('complete', 'complete'), ('partial', 'partial'), ('none', 'text not obtained')]
# README section heading, status class, badge text
README_SECTIONS = [(M.SECTION[m], M.status_class(m, 'complete'), M.LABEL[m]) for m in M.METHODS] + \
                  [('### In progress', 'partial', 'in progress')]

def century_of(y):
    if not y or y >= 2000: return 'undated'           # surveys carry 9999, undatable notes 0
    return 'early' if y < 1400 else f'{int(y) // 100}00s'

# the writeups.html Language facet: plaintext languages from profile documents[].language, matched by the first words
# ('Latin with Catalan and Castilian phrases' counts as Latin, 'French and German' as both); the rest is 'other'
LANGS = ['French', 'Italian', 'English', 'Spanish', 'German', 'Latin', 'Dutch', 'Hungarian', 'Polish', 'Swedish',
         'Portuguese', 'Chinese', 'Japanese']
LANG_ALIAS = {'castilian': 'Spanish', 'scots': 'English'}

def langs_of(folders):
    """Space-separated language keys of a page's or note's target folders, for data-lang."""
    out = set()
    for f in folders:
        prof = PROFILES.get(f.lower())
        for d in (prof or {}).get('documents') or []:
            v = str(d.get('language') or '')
            if not v or v.startswith(('unknown', 'none')): continue
            head = re.split(r'[(;,]| with ', v)[0]
            found = {LANG_ALIAS.get(w.lower(), w.capitalize()) for w in re.findall(r'[A-Za-z]+', head)} & set(LANGS)
            out |= found or {'other'}
    return ' '.join(sorted(l.lower() for l in out)) or 'unknown'

def repo_url(link):
    if link.startswith('http'): return link
    link = link.lstrip('./')
    return f'{REPO}/{"tree" if link.endswith("/") else "blob"}/main/{link}'

def md_inline(s):
    """The little Markdown the README cells use: links, bold, italic, code."""
    s = html.escape(s, quote=False)
    s = re.sub(r'\[([^\]]+)\]\(([^)\s]+)\)', lambda m: f'<a href="{repo_url(m.group(2))}" rel="noopener">{m.group(1)}</a>', s)
    s = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', s)
    s = re.sub(r'(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])', r'<i>\1</i>', s)
    s = re.sub(r'`([^`]+)`', r'<code>\1</code>', s)
    return s

def plain(s):
    return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', '', s))).strip()

def year_of(date):
    m = re.search(r'(\d{4})', date)
    if m: return int(m.group(1))
    m = re.search(r'(\d{2})th c', date)
    return int(m.group(1)) * 100 - 50 if m else 0

def readme_notes():
    """Rows of the README results tables that have no site page: target, date, result, link, status."""
    try: text = (HERE.parent / 'README.md').read_text(encoding='utf-8')
    except FileNotFoundError: return []
    slugs = {p['slug'] for p in PAGES}
    PATHS = M.profile_paths()
    notes, seen_pages, st = [], set(), None
    for line in text.splitlines():
        if line.startswith('## '): st = None
        if line.startswith('### '):
            st = next(((k, t) for h, k, t in README_SECTIONS if line.startswith(h)), None); continue
        if not st or not line.startswith('| ') or line.startswith('| Target') or line.startswith('|---'): continue
        cells = [c.strip() for c in line.strip().strip('|').split('|')]
        if len(cells) < 4: continue
        target, date, result, where = cells[0], cells[1], cells[-2], cells[-1]
        pages = re.findall(r'cyphersolver/([a-z0-9]+)\.html', where)
        if pages:
            for slug in pages:
                if slug in slugs: seen_pages.add(slug)
                else: print(f'  note: README links {slug}.html, which is not in the manifest')
            continue
        links = re.findall(r'\]\(([^)\s]+)\)', where)
        if not links: continue
        notes.append(dict(target=md_inline(target), date=html.escape(date, quote=False), y=year_of(date),
                          result=md_inline(result), url=repo_url(links[0]), st=st[0], stt=st[1], kind='active' if st[1] == 'in progress' else 'other', extent=''))
        folder = re.sub(r'^targets/', '', links[0].lstrip('./')).split('/')[0].lower()
        notes[-1]['lang'] = langs_of([folder])
        prof = M.load(PATHS[folder]) if folder in PATHS else None
        out = (prof or {}).get('outcome') or {}
        if out.get('method') not in M.METHODS and folder in M.PAGE_METHOD:      # famous targets keep no profile
            out, prof = {'method': M.PAGE_METHOD[folder][0]}, {'outcome': {'method': M.PAGE_METHOD[folder][0]}}
        if out.get('method') in M.METHODS:
            ext = M.extent(prof)
            notes[-1].update(kind=M.KEY[out['method']], extent=ext, st=M.status_class(out['method'], ext),
                             stt=M.badge(out['method'], ext, out.get('class')))
    for slug in sorted(slugs - seen_pages - set(SURVEYS)):
        print(f'  note: {slug}.html has no README row')
    return notes

def readme_glance():
    """Rewrite the "At a glance" counts in ../README.md from its own Results tables and ../catalogue.json."""
    p = HERE.parent / 'README.md'
    text = p.read_text(encoding='utf-8')
    if '<!-- glance:start -->' not in text: return None
    counts, sec, in_results = [], None, False
    for line in text.splitlines():
        if line.startswith('## '): in_results = line.strip() == '## Results'; sec = None; continue
        if in_results and line.startswith('### '):
            sec = line[4:].strip()
            if sec == 'Surveys': sec = None
            else: counts.append([sec, 0, 0])
            continue
        if sec and line.startswith('| ') and not line.startswith('| Target') and not line.startswith('|---'):
            cells = [c.strip() for c in line.strip().strip('|').split('|')]
            counts[-1][1] += 1
            counts[-1][2] += len(cells) > 3 and cells[3].startswith('complete')
    import _catalogue_page as C
    open_n = sum(1 for e in C.DATA['entries'] if C.is_open(e))
    pages = sum(1 for p_ in PAGES if p_['slug'] not in SURVEYS)
    anchor = lambda h: re.sub(r'[^\w\- ]', '', h.lower()).replace(' ', '-')
    rows = '\n'.join(f'| [{s}](#{anchor(s)}) | {n} | {c if s not in ("Not solved", "Not applicable", "In progress") else "&mdash;"} |'
                     for s, n, c in counts)
    block = ('<!-- glance:start -->\n'
             f'{sum(n for s, n, _ in counts if s not in ("Not solved", "Not applicable", "In progress"))} rows record a '
             f'reading of some kind; the site has {pages} write-up pages and {open_n} catalogue targets are open. Counts are '
             'rows of the tables below (a row can cover a group of letters), regenerated by `docs/_build_site.py`.\n\n'
             '| Outcome | Rows | Complete |\n|---|---|---|\n' + rows + '\n<!-- glance:end -->')
    new = re.sub(r'<!-- glance:start -->.*?<!-- glance:end -->', lambda m: block, text, flags=re.S)
    if new != text: p.write_text(new, encoding='utf-8')
    return len(counts)

def writeups_html():
    def q(*parts): return html.escape(plain(' '.join(parts)).lower(), quote=True)
    rows = []
    for p in sorted(PAGES, key=lambda p: p['y']):
        by = ' '.join(sorted({c['who'] for c in p.get('credits') or [] if c.get('who') in CONTRIB}))
        rows.append(f'<li data-kind="{kind_of(p)}" data-extent="{p.get("extent") or ""}" data-century="{century_of(p["y"])}" data-src="page" data-by="{by}" '
                    f'data-lang="{langs_of(p.get("folders") or [])}" '
                    f'data-q="{q(p["label"], p["title"], p["place"], p["year"], p["blurb"], p["stt"])}">'
                    f'<a href="{p["slug"]}.html"><span class="st {p["st"]}">{p["stt"]}</span>'
                    f'<span class="t">{avatars_html(p["slug"])}{p["title"]}</span>{when_html(p, cls="dt")}<span class="yr">{p["year"]}</span>'
                    f'<span class="b">{p["blurb"]}</span></a></li>')
    notes = readme_notes()
    nrows = []
    for n in sorted(notes, key=lambda n: n['y']):
        nrows.append(f'<li data-kind="{n["kind"]}" data-extent="{n["extent"]}" data-century="{century_of(n["y"])}" data-src="notes" data-lang="{n.get("lang", "")}" '
                     f'data-q="{q(n["target"], n["result"], n["date"], n["stt"])}">'
                     f'<a href="{n["url"]}" rel="noopener"><span class="st {n["st"]}">{n["stt"]}</span>'
                     f'<span class="t">{n["target"]}</span><span class="dt">notes &#8599;</span><span class="yr">{n["date"]}</span>'
                     f'<span class="b">{n["result"]}</span></a></li>')
    # chips only for values some entry has; site.js fills in each chip's live count
    have = {}
    for li in rows + nrows:
        for k, v in re.findall(r' data-(kind|extent|century|src|lang)="([^"]*)"', li.split('>', 1)[0]):
            n = have.setdefault(k, {})
            for x in v.split(): n[x] = n.get(x, 0) + 1
    def facet(name, label, vals, extra=''):
        opts = ''.join(f'<button type="button" class="chip" data-facet="{name}" data-val="{k}" aria-pressed="false">{l}<span class="n"></span></button>'
                       for k, l in vals if k in have.get(name, {}))
        return f'<div class="facet" role="group" aria-label="{label}"><span class="flabel">{label}</span><span class="opts">{opts}</span>{extra}</div>'
    def dropdown(label, body, name):
        return (f'<details class="dd" data-dd="{name}"><summary><span class="dl">{label}</span><span class="dv"></span></summary>'
                f'<div class="pop">{body}</div></details>')
    nl = have.get('lang', {})
    langs = [(l, l if l in ('other', 'unknown') else l.capitalize()) for l in sorted(nl, key=lambda l: (l in ('other', 'unknown'), l == 'unknown', -nl[l], l))]
    total = len(rows) + len(nrows)
    return (
        '<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
        f'<title>All write-ups &mdash; {len(rows)} ciphers by outcome and date, and {len(nrows)} results still in the notes</title>\n'
        f'<meta name="description" content="Every write-up on the site, filterable by method, extent, language, century and text, followed by the '
        f'results that exist only as notes in the repository: read, explained, attempted or waiting on an archive.">\n'
        f'<link rel="stylesheet" href="style.css?v={VERSION}">\n</head>\n<body id="top">\n<!-- site:nav -->\n\n'
        '<section class="hero">\n'
        f'  <p class="kicker">Index &middot; {len(rows)} write-ups &middot; {len(nrows)} results only in the notes</p>\n'
        '  <h1>Every write-up</h1>\n'
        '  <p class="sub">Each cipher this site has worked on, in date order, with its outcome. Filter by method, extent, language or century, or search '
        'the titles and summaries. The second list is work that exists only as notes in the repository: results not yet written up, '
        'attempts closed from the evidence, and items waiting on an archive.</p>\n'
        '  <div class="jump"><a href="#pages">Write-ups</a><a href="#notes">Only in the notes</a><a href="catalogue.html">Catalogue</a></div>\n'
        '  <p class="meta">Daniel Bourdeau</p>\n</section>\n\n<main>\n\n'
        '<div class="cfilters" role="search">\n'
        '  <input id="wq" type="search" placeholder="Search: titles, places, summaries&hellip;" aria-label="Search the write-ups">\n'
        f'  {dropdown("Method", facet("kind", "Method", KINDS, '<a class="gl" href="glossary.html">what these mean</a>'), "kind")}\n'
        f'  {dropdown("Extent", facet("extent", "Extent", EXTENTS), "extent")}\n'
        f'  {dropdown("Language", facet("lang", "Language", langs), "lang")}\n'
        f'  {dropdown("Century", facet("century", "Century", CENTURIES), "century")}\n'
        f'  {dropdown("Where", facet("src", "Where", [("page", "site page"), ("notes", "notes only")]), "src")}\n'
        f'  <span class="count" id="wcount" aria-live="polite" data-names="{html.escape(json.dumps({k: c["name"] for k, c in CONTRIB.items()}, ensure_ascii=False), quote=True)}">All {total} entries</span>\n'
        '  <button type="button" class="chip clear" id="wreset" hidden>clear filters</button>\n</div>\n\n'
        '<section class="wsec" id="pages">\n<h2 id="write-ups"><span class="num">01</span> Write-ups</h2>\n'
        '<ul class="list wl wi">\n' + '\n'.join(rows) + '\n</ul>\n</section>\n\n'
        '<section class="wsec" id="notes">\n<h2 id="only-in-the-notes"><span class="num">02</span> Only in the notes</h2>\n'
        f'<p>Results recorded in the repository <a href="{REPO}#results" rel="noopener">README</a> that have no page here yet. '
        'Each row links to the folder with the notes, transcriptions and code. The rows are read from the README at build time, '
        'so a result lands here as soon as it is logged there.</p>\n'
        '<ul class="list wl wi">\n' + '\n'.join(nrows) + '\n</ul>\n</section>\n\n</main>\n<!-- site:footer -->\n</body>\n</html>\n')

# glossary.html: the outcome methods (with a count of write-ups under each, linked into the filtered index) and the
# cryptologic terms the write-ups use.  Generated from _methods.py, the same vocabulary the badges and checkers use.
def glossary_html():
    counts = {m: sum(1 for p in PAGES if p.get('method') == m) for m in M.METHODS}
    meth = ''.join(
        f'<dt id="{M.KEY[m]}"><span class="st {M.status_class(m, "complete")}">{M.LABEL[m]}</span> {m[0].upper() + m[1:]}</dt>\n'
        f'<dd>{html.escape(M.DEFINE[m])} <a href="writeups.html#kind={M.KEY[m]}">{counts[m]} write-up{"s" if counts[m] != 1 else ""} &rarr;</a></dd>\n'
        for m in M.METHODS)
    terms = ''.join(f'<dt id="{a}">{html.escape(t)}</dt>\n<dd>{html.escape(d)}</dd>\n' for a, t, d in M.TERMS)
    return (
        '<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
        '<title>Glossary &mdash; how each cipher was solved, and the terms used</title>\n'
        '<meta name="description" content="The outcome categories used on every write-up (how the key or text was obtained, and how '
        'much of it) and the cryptologic terms the write-ups use.">\n'
        f'<link rel="stylesheet" href="style.css?v={VERSION}">\n</head>\n<body id="top">\n<!-- site:nav -->\n\n'
        '<section class="hero">\n  <p class="kicker">Reference &middot; outcome methods &middot; terms</p>\n'
        '  <h1>Glossary</h1>\n'
        '  <p class="sub">Every write-up states two things about its outcome. The <b>method</b> says how the key or the text was '
        'obtained. The <b>extent</b> says how much of the text was obtained: complete or partial. The methods follow the '
        'categories proposed by George Lasry, with one addition for items that already had a full decipherment.</p>\n'
        '  <p class="meta">Daniel Bourdeau</p>\n</section>\n\n<main>\n\n'
        '<h2 id="methods">Methods</h2>\n<p>The first three are cryptanalysis: the key was recovered here. The next three '
        'applied a key or decipherment that already existed; the work was transcription and decipherment. Whether someone had '
        'solved an item before, and when that was found, is stated on each write-up.</p>\n'
        f'<dl class="gloss">\n{meth}</dl>\n\n'
        '<h2 id="extent-complete-or-partial">Extent</h2>\n<p><b>Complete</b>: at least 95% of the cipher symbols give sense, '
        'every document is covered, and what stays open is scattered code groups or pieces blocked from outside. '
        '<b>Partial</b>: anything less; the write-up lists what is open and why.</p>\n\n'
        f'<h2 id="terms">Terms</h2>\n<dl class="gloss">\n{terms}</dl>\n\n</main>\n<!-- site:footer -->\n</body>\n</html>\n')


def footer_html(current):
    order = sorted([p for p in PAGES if p['slug'] not in ('solved', 'top25')], key=lambda p: p['y'])
    prev = nxt = None
    for i, p in enumerate(order):
        if p['slug'] == current:
            prev = order[i-1] if i > 0 else None; nxt = order[i+1] if i+1 < len(order) else None
    cur = next((p for p in PAGES if p['slug'] == current), None)
    rights = f' &middot; {cur["rights"]}' if cur and cur.get('rights') else ''
    links = ['<a href="index.html">Overview</a>']
    if prev: links.append(f'<a href="{prev["slug"]}.html" rel="prev">&larr; {prev["label"]} {prev["year"]}</a>')
    if nxt: links.append(f'<a href="{nxt["slug"]}.html" rel="next">{nxt["label"]} {nxt["year"]} &rarr;</a>')
    links.append(f'<a href="{REPO}" rel="noopener">Code &#8599;</a>')
    links.append('<a href="contribute.html#email">Contact &#9993;</a>')
    links.append('<a href="feed.xml">Feed</a>')
    links.append('<a href="#top">Top &uarr;</a>')
    author = cur.get('author', 'Daniel Bourdeau') if cur else 'Daniel Bourdeau and contributors' if current in SHARED_PAGES else 'Daniel Bourdeau'
    footer_date = cur.get('footer_date', 'September 2026') if cur else 'September 2026'
    return (f'<footer><div class="in">\n  <span>{author}, {footer_date} &middot; Text released under CC BY 4.0{rights}</span>\n'
            f'  <nav aria-label="Footer">{"".join(links)}</nav>\n</div></footer>')

# the write-ups with letters on the Atlas, for the "On the map" link in their outcome line
ATLAS_SLUGS = {l['slug'] for l in json.loads((HERE / 'atlas.json').read_text(encoding='utf-8'))['letters']}

def toc_html(s):
    heads = re.findall(r'<h2 id="([^"]+)">(.*?)</h2>', s, re.S)
    if len(heads) < 3: return ''
    links = []
    for hid, inner in heads:
        text = re.sub(r'<span class="num">.*?</span>', '', inner); text = re.sub(r'<[^>]+>', '', text)
        text = re.sub(r'\s+', ' ', html.unescape(text)).strip()
        text = text.split(' &mdash; ')[0]
        if len(text) > 48: text = text[:48].rsplit(' ', 1)[0].rstrip(' ,;:') + '\u2026'     # at a word, not in the middle of one
        links.append(f'<a href="#{hid}">{html.escape(text)}</a>')
    return '<nav class="toc" aria-label="On this page"><span>On this page</span>' + ''.join(links) + '</nav>\n'

def when_html(p, cls='when'):
    """The short datestamp shown on the index cards and list rows."""
    rec = DATES['pages'].get(p['slug'])
    if not rec: return ''
    verb = 'posted' if p['slug'] in ('solved', 'top25') else verb_of(p)
    return (f'<time class="{cls}" datetime="{rec["first"]}" '
            f'title="{verb} {fmt_date(rec["first"])}, updated {fmt_date(rec["updated"])}">'
            f'{verb if p.get("method") else VERB_SHORT.get(p["st"], verb)} {fmt_date(rec["first"], short=True)}</time>')

def avatars_html(slug):
    """The correspondents' portraits as a small overlapping pair, for cards and list rows."""
    people = sorted(PICTURED.get(slug, []), key=lambda p: p['role'] != 'sender')
    if not people: return ''
    tip = html.escape(' → '.join(p['name'] for p in people), quote=True)
    return (f'<span class="avs" title="{tip}">' +
            ''.join(f'<img src="{p["img"]}" alt="" loading="lazy">' for p in people) + '</span>')

def mini_thumb(slug, cls):
    """A small square for list rows and findings: a crop of the script when there is one, the correspondent's
    portrait tucked into its corner; the portrait alone when there is no script image; '' when there is neither."""
    im = IMAGES.get(slug)
    people = sorted(PICTURED.get(slug, []), key=lambda p: p['role'] != 'sender')
    if not im and not people: return ''
    inner = f'<img class="sc" src="{im[0]}" alt="" loading="lazy">' if im else f'<img class="pt" src="{people[0]["img"]}" alt="" loading="lazy">'
    if im and people: inner += f'<img class="pc" src="{people[0]["img"]}" alt="" loading="lazy">'
    return f'<span class="{cls}">{inner}</span>'

def reveal_run(slug, n=9):
    """The opening run of a reveal passage, for the slides on the index: n cipher tokens with their readings."""
    f = HERE / 'reveal' / f'{slug}.json'
    if not f.exists(): return None
    d = json.loads(f.read_text(encoding='utf-8'))
    toks = [t for t in d.get('tokens', []) if t.get('g') and t.get('p') and t.get('cls') not in ('plain', 'null', 'unk') and t['p'] != '?']
    if len(toks) < 4: return None
    return d, toks[:n]

def catintro_html():
    """The catalogue section's opening paragraph, counted from catalogue.json so it never goes stale."""
    import _catalogue_page as C
    es = json.loads((HERE.parent / 'catalogue.json').read_text(encoding='utf-8'))['entries']
    op = [e for e in es if C.is_open(e)]
    ys = [e['year'] for e in op if isinstance(e.get('year'), int)]
    seen = sum(1 for e in op if 'image' in str(e.get('seen')) or e.get('seen') == 'viewed')
    return (f'<!-- catintro:start -->\n<p>{len(op):,} undeciphered letters and series from {min(ys)} to {max(ys)}. Each carries its shelfmark, the prior art '
            f'checked, a difficulty class and the check that would confirm it is genuinely open; {seen} have been looked at on the image.</p>\n<!-- catintro:end -->')


def cattop_html(n=6):
    """The highest-priority open entries of the Unsolved Catalogue, for the index."""
    import _catalogue_page as C
    top = sorted([e for e in C.DATA['entries'] if e['counted'] and C.is_open(e)], key=lambda e: (-C.priority(e), e['id']))[:n]
    li = ''.join(f'  <li><a href="solve/{e["id"]}.html">{C.people_html(e) or C.blank_html(e)}<span class="t">{C.esc(e["title"])}</span>'
                 f'<span class="pr"><small>priority</small> {C.priority(e):.1f}</span><span class="yr">{C.esc(e["date"])}</span></a></li>\n' for e in top)
    return f'<!-- cattop:start -->\n<h3 class="listhead">Top of the queue</h3>\n<ul class="list cattop">\n{li}</ul>\n<!-- cattop:end -->\n'

def card_html(p):
    im = IMAGES.get(p['slug'])
    thumb = f'    <img class="thumb" src="{im[0]}" alt="" loading="lazy">\n' if im else ''
    return (f'  <a class="card{" hasthumb" if im else ""}" href="{p["slug"]}.html">\n' + thumb +
            f'    <div class="eyebrow"><span>{p["place"]} &middot; {p["year"]}</span><span class="st {p["st"]}">{p["stt"]}</span></div>\n'
            f'    <h3>{p["title"]}</h3>\n    <p>{p["blurb"]}</p>\n    <p class="quote">{p["quote"]}</p>\n    {avatars_html(p["slug"])}<span class="go">read &rarr;</span>\n  </a>\n')

PORTRAITS = json.loads((HERE / '_portraits.json').read_text(encoding='utf-8')) if (HERE / '_portraits.json').exists() else {}
# entries with no image are names only: the atlas shows them as a lettered circle, the pages and cards leave them out
PICTURED = {k: [p for p in v if p.get('img')] for k, v in PORTRAITS.items() if any(p.get('img') for p in v)}

def parties_html(people):
    """Sender and recipient portraits, sender first, an arrow between them when both are known."""
    order = sorted(people, key=lambda p: p['role'] != 'sender')
    def one(p):
        tip = html.escape(f"{p['name']}: {p['what']}. {p['credit']}.", quote=True)
        return (f'<figure class="party {p["role"]}"><img src="{p["img"]}" alt="{html.escape(p["name"], quote=True)}" title="{tip}" loading="lazy">'
                f'<figcaption><span class="role">{"from" if p["role"] == "sender" else "to"}</span>{p["name"]}</figcaption></figure>')
    sep = '<span class="arrow" aria-hidden="true">&rarr;</span>'
    # a page covering letters to two people lists both recipients side by side, the arrow only after the sender
    senders = ''.join(one(p) for p in order if p['role'] == 'sender')
    recipients = ''.join(one(p) for p in order if p['role'] != 'sender')
    return '\n<div class="parties">' + senders + (sep if senders and recipients else '') + recipients + '</div><!-- /parties -->'

RECENT_VISIBLE = 5      # "Latest findings" on index.html mirrors this many entries of findings.html
FINDINGS_PAGE = HERE / 'findings.html'
FINDINGS_LIST = re.compile(r'(<h2 id="recent">.*?</h2>\n(?:<p>.*?</p>\n)?)(<ul class="findings">.*?)(?=\n<h2|\n<!-- |\Z)', re.S)

def absorb_findings():
    """findings.html holds every finding and index.html mirrors the newest (<li data-mirror>). A plain <li> on index.html
    was added there by hand or by a branch older than findings.html: it moves to the top of findings.html, once."""
    index, page = (HERE / 'index.html').read_text(encoding='utf-8'), FINDINGS_PAGE.read_text(encoding='utf-8')
    region, held = FINDINGS_REGION.search(index), FINDINGS_LIST.search(page)
    if not region or not held: return 0
    have = {finding_key(li) for li in re.findall(r'<li>.*?</li>', held.group(2), re.S)}
    new = [li for li in re.findall(r'<li>.*?</li>', region.group(0), re.S) if finding_key(li) not in have]
    if new:
        at = held.start(2) + len('<ul class="findings">\n')
        FINDINGS_PAGE.write_text(page[:at] + '\n'.join(new) + '\n' + page[at:], encoding='utf-8')
    return len(new)

def findings_items(s):
    """The entries of a findings list, in order, each once, dated."""
    m = FINDINGS_LIST.search(s)
    if not m: return None
    items = re.findall(r'<li>.*?</li>', m.group(2), re.S)
    # Navigation entries have been accidentally pasted here during publication
    # merges. Do not date and promote menu links as research findings.
    if any(re.search(r'<span class="st [^"]+">|<i class="dot [^"]+"', li) for li in items):
        raise ValueError('Recent findings contains navigation status badges. '
                         'Restore the editorial findings; do not copy menu <li> entries.')
    # Concurrent publications can insert the same finding twice. Compare the
    # editorial content without generated dates or thumbnails; keep the first.
    seen = set()
    unique = []
    for li in items:
        key = normalise(li)
        if key not in seen:
            seen.add(key)
            unique.append(stamp_finding(li))
    return unique

def list_findings(s):
    """findings.html: every entry, stamped."""
    m, items = FINDINGS_LIST.search(s), findings_items(s)
    if not items: return s
    return s[:m.start(2)] + '<ul class="findings">\n' + '\n'.join(items) + '\n</ul>' + s[m.end(2):]

def mirror_findings(s, n=RECENT_VISIBLE):
    """index.html: the newest n entries of findings.html, then the way to all the write-ups."""
    m, items = FINDINGS_LIST.search(s), findings_items(FINDINGS_PAGE.read_text(encoding='utf-8'))
    if not m or not items: return s
    head = ('<ul class="findings">\n' + '\n'.join(li.replace('<li>', '<li data-mirror>', 1) for li in items[:n]) + '\n</ul>\n'
            f'<p class="allws"><a href="writeups.html">All {len(PAGES)} write-ups &rarr;</a></p>')
    return s[:m.start(2)] + head + s[m.end(2):]

FEATURED = ['voynich', 'lucca', 'armstrong', 'sunyatsen', 'feuquieres', 'ormonde']
BROWSE_LANGS = 6        # languages listed under "Browse the write-ups"; the filter on writeups.html has the rest

def browse_html():
    """The routes from the home page into writeups.html: its own filters, each with what it would show."""
    from collections import Counter
    shown = [p for p in PAGES if p['slug'] not in SURVEYS]
    def col(title, rows):
        lis = ''.join(f'<li><a href="writeups.html#{k}={v}&amp;src=page">{l}<span class="n">{n}</span></a></li>' for k, v, l, n in rows if n)
        return f'<div class="br-col"><h3>{title}</h3><ul>{lis}</ul></div>'
    kinds = Counter(kind_of(p) for p in shown)
    cents = Counter(century_of(p['y']) for p in shown)
    langs = Counter(x for p in shown for x in langs_of(p.get('folders') or []).split())
    top = [l for l, _ in langs.most_common() if l not in ('other', 'unknown')][:BROWSE_LANGS]
    return ('<!-- browse:start -->\n<section class="browse" aria-labelledby="writeups">\n<h2 id="writeups">Browse the write-ups</h2>\n<div class="br-grid">'
            + col('By how the text was obtained', [('kind', k, l[0].upper() + l[1:], kinds[k]) for k, l in KINDS if k not in ('active', 'other', 'survey')])
            + col('By century', [('century', k, l, cents[k]) for k, l in CENTURIES if k != 'undated'])
            + col('By language', [('lang', l, l.capitalize(), langs[l]) for l in top])
            + f'</div>\n<p class="allws"><a href="writeups.html">All {len(PAGES)} write-ups, with filters and search &rarr;</a> &middot; '
              '<a href="atlas.html">the atlas</a> &middot; <a href="keys.html">the key web</a> &middot; <a href="glossary.html">what the methods mean</a></p>\n</section>\n<!-- browse:end -->')

# The larger of them keep their rules in a sheet of their own, docs/pg-<slug>.css, linked after style.css on that page
# alone (slug -> a hash of the file); the rest, and pg-solve, stay in style.css.
PAGE_CSS = {f.stem[3:]: hashlib.sha1(f.read_bytes().replace(b'\r\n', b'\n')).hexdigest()[:8] for f in sorted(HERE.glob('pg-*.css'))}
PAGE_STYLED = {'archives', 'atlas', 'catalogue', 'further', 'goldbar', 'highlights', 'huangxing', 'keys', 'roosevelt', 'secret', 'sunintercepts', 'sunyatsen'}
SHARED_INLINE = ('.why', '.w-yes', '.w-no', '.w-lang', '.w-otp', '.w-short', '.w-fake', '.w-open', '.item', '.item h3', '.item .meta2', '.ct', '.callout', '.callout h3', '.tw')

def credit_figures(s):
    """Every image on a page names its own source: <figure data-credit="Biblioth&egrave;que nationale de France, fr. 3976
    f. 133v, via Gallica"> becomes an "Image: ..." line at the end of the caption. The credit is per figure, never a
    page default, because one page often mixes holders (the letter, a sibling key, a printed edition, a diagram of our
    own). docs/_check_writeup.py fails a page with an image figure that has no data-credit."""
    s = re.sub(r' ?<span class="credit">[^<]*</span>(?=</figcaption>)', '', s)
    def add(m):
        fig, own = m.group(0), re.search(r'data-credit="([^"]*)"', m.group(1))
        if not own or not own.group(1).strip(): return fig
        span = f' <span class="credit">Image: {own.group(1).strip().rstrip(".")}.</span>'
        if '</figcaption>' in fig: return fig.replace('</figcaption>', span + '</figcaption>', 1)
        return fig.replace('</figure>', f'<figcaption>{span.strip()}</figcaption></figure>', 1)
    return re.sub(r'<figure((?! class="(?:party|lead))[^>]*)>.*?</figure>', add, s, flags=re.S)

NO_TRANSLATE_CLASSES = ('cipherstrip', 'lr-readable', 'lr-excerpt', 'cr-tiles', 'cr-grid')

def protect_text(s):
    """translate="no" on ciphertext, transcriptions, original-language readings and keys, so a browser's page
    translation leaves them alone: every <pre> and <code>, the classes above, and any element with a non-English lang."""
    def mark(m):
        tag, attrs = m.group(1), m.group(2)
        return m.group(0) if re.search(r'\btranslate=', attrs) else f'<{tag}{attrs} translate="no">'
    s = re.sub(r'<(pre|code)(?![\w-])([^>]*)>', mark, s)
    cls = '|'.join(NO_TRANSLATE_CLASSES)
    s = re.sub(r'<(?!html)([a-z][a-z0-9]*)([^>]*\bclass="(?:[^"]*\s)?(?:%s)(?:\s[^"]*)?"[^>]*)>' % cls, mark, s)
    s = re.sub(r'<(?!html)([a-z][a-z0-9]*)([^>]*\blang="(?!en)[^"]*"[^>]*)>', mark, s)
    return s

BASE_URL = 'https://cyphersolver.com/'
DESC_MAX = 200

def short_desc(full):
    """The first sentences of a description that fit what search results and share cards show."""
    if len(full) <= DESC_MAX: return full
    out = ''
    for sent in re.split(r'(?<=[.!?])\s+', full):
        if len(out) + len(sent) + 1 > DESC_MAX: break
        out = (out + ' ' + sent).strip()
    if len(out) >= 90: return out
    return full[:DESC_MAX - 1].rsplit(' ', 1)[0].rstrip(' ,;:&') + '&hellip;'

def share_image(slug, s):
    """The picture a shared link shows: the page's lead image, else its first figure, else the site's."""
    im = IMAGES.get(slug)
    if im: return im[0]
    m = re.search(r'<figure[^>]*>\s*(?:<a[^>]*>\s*)?<img\b[^>]*?\bsrc="([^"#?]+)"', s)
    return m.group(1) if m and not re.match(r'(?:https?:|data:|//)', m.group(1)) else 'hero_poster.png'

def head_tags(slug, s):
    """The short description, and the canonical address, share card and feed link of a page. Moved-page stubs keep theirs."""
    s = re.sub(r'<!-- social:start -->.*?<!-- social:end -->\n?', '', s, flags=re.S)
    if slug == '404' or re.search(r'<meta name="robots" content="noindex"', s): return s
    m = re.search(r'<meta name="description" content="([^"]*)"(?: data-full="([^"]*)")?>', s)
    desc = ''
    if m:
        full = m.group(2) if m.group(2) and m.group(1) == short_desc(m.group(2)) else m.group(1)   # an edited content wins
        desc = short_desc(full)
        new = f'<meta name="description" content="{desc}"' + (f' data-full="{full}">' if desc != full else '>')
        s = s[:m.start()] + new + s[m.end():]
    url = BASE_URL if slug == 'index' else f'{BASE_URL}{slug}.html'
    tags = [f'<link rel="canonical" href="{url}">', f'<link rel="alternate" type="application/atom+xml" title="Cyphersolver: new write-ups" href="{BASE_URL}feed.xml">']
    if 'property="og:title"' not in s:      # the home page has its own
        t = re.search(r'<title>(.*?)</title>', s, re.S)
        title = t.group(1).strip() if t else SITE
        kind = 'article' if any(p['slug'] == slug for p in PAGES) else 'website'
        tags += [f'<meta property="og:type" content="{kind}">', f'<meta property="og:site_name" content="{SITE}">', f'<meta property="og:url" content="{url}">',
                 f'<meta property="og:title" content="{title.replace(chr(34), "&quot;")}">', f'<meta property="og:description" content="{desc}">',
                 f'<meta property="og:image" content="{BASE_URL}{share_image(slug, s)}">', '<meta name="twitter:card" content="summary_large_image">']
    return s.replace('</head>', '<!-- social:start -->\n' + '\n'.join(tags) + '\n<!-- social:end -->\n</head>', 1)

def readjump_html(page, lr, tb):
    """A button under the hero to the page's text: George Lasry's report when there is one, else Full texts."""
    if lr: href, label = '#lasry-report', 'Go to the decipherment'
    elif tb and re.search(r'(?:<summary>|"ftext">)(?:Reading|Translation)', tb): href, label = '#texts', 'Go to the full text'
    elif tb: href, label = '#texts', 'Go to the transcriptions'
    else: return ''
    return f'<p class="readjump"><a href="{href}">{label} &darr;</a></p><!-- /readjump -->'

CITE_ROLES = [r for r in CR.DIRECT if r != 'pointer']      # a pointer to a source, or a key used, is credited, not cited
def cite_authors(page):
    """The authors a citation names: the page's author and every person who contributed directly to its target(s).
    A contributed result names its contributors first."""
    own = plain(page.get('author', 'Daniel Bourdeau'))
    cs = [c for c in page.get('credits') or [] if c.get('role') in CITE_ROLES and CONTRIB.get(c.get('who'), {}).get('kind') == 'person']
    order = sorted({c['who'] for c in cs}, key=lambda w: (min(CITE_ROLES.index(c['role']) for c in cs if c['who'] == w), CONTRIB[w]['name']))
    names = [n for n in dict.fromkeys(plain(CONTRIB[w]['name']) for w in order) if n not in own]
    return names + [own] if page.get('provenance') == 'contributed' else [own] + names

def cite_html(page, rec):
    """Cite this page: the words, and a button each for the words and for BibTeX (site.js copies them)."""
    title, slug = plain(page['title']), page['slug']
    names = cite_authors(page)
    author = names[0] if len(names) == 1 else ', '.join(names[:-1]) + ' and ' + names[-1]
    url = f'{BASE_URL}{slug}.html'
    posted, updated = fmt_date(rec['first']), fmt_date(rec['updated'])
    when = f'posted {posted}' + (f', updated {updated}' if updated != posted else '')
    text = f'{author}, \u201c{title}\u201d, Cyphersolver, {when}, {url}.'
    year = rec['first'][:4]
    bib = (f'@misc{{cyphersolver-{slug},\n  author = {{{" and ".join("{" + n + "}" if "," in n else n for n in names)}}},\n  title = {{{title}}},\n  year = {{{year}}},\n'
           f'  howpublished = {{Cyphersolver}},\n  note = {{{when}}},\n  url = {{{url}}}\n}}')
    esc = lambda t: html.escape(t, quote=True)
    return (f'<!-- cite:start -->\n<details class="cite" id="cite"><summary>Cite this page</summary>\n<p class="citetext">{esc(text)}</p>\n'
            f'<p class="citebtns"><button type="button" data-copy="{esc(text)}">Copy citation</button>'
            f'<button type="button" data-copy="{esc(bib)}">Copy BibTeX</button></p>\n</details>\n<!-- cite:end -->\n')

def process(path):
    slug = path.stem
    s = path.read_text(encoding='utf-8')
    if s.startswith('﻿'): s = s[1:]
    rec = page_dates(slug, s)
    page = next((p for p in PAGES if p['slug'] == slug), None)
    if page and '<section class="hero">' not in s:
        print(f'  note: {slug}.html has no hero section (kicker, title, byline); every write-up has one')
    nav = nav_html(slug)
    s = re.sub(r'\n?<div class="search" id="search".*?</div>\n</div>', '', s, count=1, flags=re.S)
    if '<!-- site:nav -->' in s: s = s.replace('<!-- site:nav -->', nav, 1)
    else: s = re.sub(r'<header class="nav">.*?</header>|<nav class="nav">.*?</nav>', lambda m: nav, s, count=1, flags=re.S)
    s = re.sub(r'(</div></header>)(\s*</div></header>)+', r'\1', s)      # stray closers left by an earlier build
    foot = footer_html(slug)
    if '<!-- site:footer -->' in s: s = s.replace('<!-- site:footer -->', foot, 1)
    else:
        ms = list(re.finditer(r'<footer.*?</footer>', s, re.S))
        if ms: m = ms[-1]; s = s[:m.start()] + foot + s[m.end():]
        else: s = s.replace('</main>', '</main>\n' + foot, 1)
    # George Lasry's report at the top of the body (lasry_report_html), regenerated on every build
    s = re.sub(r'<!-- lasry:start -->.*?<!-- lasry:end -->\n?', '', s, flags=re.S)
    lr = lasry_report_html(page) if page else ''
    if lr and 'id="verification"' not in s: lr = lr.replace('under <a href="#verification">Verification</a>', 'further down')
    if lr and '<main>' in s:
        s = re.sub(r'(<main>\n(?:<nav class="toc".*?</nav>\n)?)', lambda m: m.group(1) + lr, s, count=1, flags=re.S)
    # give every h2 an id so the contents strip and deep links work
    used = set(re.findall(r'<h2 id="([^"]+)"', s))
    def add_id(m):
        text = re.sub(r'<span class="num">.*?</span>', '', m.group(2)); text = html.unescape(re.sub(r'<[^>]+>', '', text))
        base = re.sub(r'[^a-z0-9]+', '-', text.lower()).strip('-')[:40] or 'section'
        hid = base; k = 2
        while hid in used: hid = f'{base}-{k}'; k += 1
        used.add(hid); return f'<h2 id="{hid}"{m.group(1)}>{m.group(2)}</h2>'
    s = re.sub(r'<h2((?![^>]*\bid=)[^>]*)>(.*?)</h2>', add_id, s, flags=re.S)
    # contents strip
    s = re.sub(r'<nav class="toc".*?</nav>\n*', '', s, flags=re.S)      # also eat blank lines an earlier build left
    if slug not in ('index', 'findings'):
        toc = toc_html(s)
        if toc: s = re.sub(r'<main>\n*', lambda m: '<main>\n' + toc, s, count=1)
    # lead figure: pages that have an image in the manifest but no figure of their own get one after the contents strip
    im = IMAGES.get(slug)
    s = re.sub(r'<figure class="lead">.*?</figure>\n?', '', s, flags=re.S)
    if im and '<figure' not in s:
        cap = im[1] + (f'. {im[2]}.' if im[2] else '.')
        fig = f'<figure class="lead"><img src="{im[0]}" alt="{im[1]}"><figcaption>{cap}</figcaption></figure>\n'
        if '<nav class="toc"' in s:
            s = re.sub(r'(<nav class="toc".*?</nav>\n)', lambda m: m.group(1) + fig, s, count=1, flags=re.S)
        else:
            s = s.replace('<main>', '<main>\n' + fig, 1)
    s = credit_figures(s)
    # the correspondents: sender and recipient portraits from _portraits.json, under the hero title
    s = re.sub(r'\n?<div class="parties">.*?</div><!-- /parties -->', '', s, flags=re.S)
    if PICTURED.get(slug) and '<section class="hero">' in s:
        s = re.sub(r'(<section class="hero">.*?</h1>)', lambda m: m.group(1) + parties_html(PICTURED[slug]), s, count=1, flags=re.S)
    # drop inline style blocks made of shared rules only
    def strip_style(m):
        rules = re.findall(r'([^{}]+)\{', m.group(1))
        if rules and all(r.strip() in SHARED_INLINE for r in rules): return ''
        return m.group(0)
    s = re.sub(r'<style>(.*?)</style>\s*', strip_style, s, flags=re.S)
    # page-specific rules live under body.pg-<slug>, in style.css or in the page's own pg-<slug>.css (PAGE_CSS); a page keeps no <style> block of its own
    if slug in PAGE_STYLED: s = re.sub(r'<style[^>]*>.*?</style>\s*', '', s, flags=re.S)
    # dateline: when the finding landed, and when the page last really changed
    mm = re.search(r'<p class="meta">(.*?)</p>', s, re.S)
    if mm: s = s[:mm.start()] + meta_html(page, rec, mm.group(1), slug) + s[mm.end():]
    # the outcome line under the dateline: method (linked to the glossary) and extent, from the profile
    s = re.sub(r'\n?<p class="outcome">.*?</p><!-- /outcome -->', '', s, flags=re.S)
    oc = outcome_html(page) if page else ''
    if oc and '<section class="hero">' in s:
        onmap = f' &middot; <a href="atlas.html#slug={slug}">On the map</a></p><!-- /outcome -->' if slug in ATLAS_SLUGS else '</p><!-- /outcome -->'
        s = re.sub(r'(<section class="hero">.*?<p class="meta">.*?</p>)', lambda m: m.group(1) + '\n' + oc.replace('</p><!-- /outcome -->', onmap), s, count=1, flags=re.S)
    # the At a glance badge follows the profile: method label and extent as the outcome line gives them, so the two cannot disagree
    em = re.search(r'Extent: ([^<]*)</p>', oc) if oc.startswith('<p class="outcome">Method:') else None
    if em and page.get('method') in M.LABEL:
        s = re.sub(r'(<span class="gl-res">).*?(</span>)', lambda m: m.group(1) + M.LABEL[page['method']].capitalize() + ' &middot; ' + em.group(1) + m.group(2), s, count=1, flags=re.S)
    s = re.sub(r'\n?<p class="credits">.*?</p><!-- /credits -->', '', s, flags=re.S)
    cl = credits_html(page) if page else ''
    if cl and '<section class="hero">' in s:
        anchor = r'(<section class="hero">.*?<p class="meta">.*?</p>(?:\n<p class="outcome">.*?</p><!-- /outcome -->)?)'
        s = re.sub(anchor, lambda m: m.group(1) + '\n' + cl, s, count=1, flags=re.S)
    # the lead figure lies faintly under the right of the hero, as the home page's manuscript lies under its own
    # (style.css .hero-ms); pages with no lead figure keep the plain hero
    s = re.sub(r'\n?<div class="hero-ms"[^>]*>.*?</div><!-- /hero-ms -->', '', s, flags=re.S)
    lead = IMAGES.get(slug)
    if lead and lead[0].lower().endswith(('.jpg', '.jpeg', '.png', '.webp')) and '<section class="hero">' in s:
        s = s.replace('<section class="hero">', f'<section class="hero">\n<div class="hero-ms" aria-hidden="true"><img src="{lead[0]}" alt=""></div><!-- /hero-ms -->', 1)
    # the kicker's last segment names the outcome in older pages; it follows the profile's method now
    if page and page.get('method'):
        s = re.sub(r'(<p class="kicker">.*?)(?:&middot;|·)\s*(?:solved|read|read in part|solved in part|partly read|partly solved|attempted|attempted, open|'
                   r'not solved|unsolved|explained|found solved|already solved|in progress)\s*(</p>)',
                   lambda m: m.group(1).rstrip() + m.group(2), s, count=1, flags=re.S)
    s = re.sub(r'<meta name="(?:date|last-modified)"[^>]*>\n?', '', s)
    s = s.replace('</head>', f'<meta name="date" content="{rec["first"]}">\n'
                             f'<meta name="last-modified" content="{rec["updated"]}">\n</head>', 1)
    # the wax seal pressed into a write-up's hero: its outcome, in the colour of its badge
    s = re.sub(r'\n?<div class="seal [a-z]+" aria-hidden="true">.*?</div>', '', s)
    if page and page['slug'] not in SURVEYS and '<section class="hero">' in s:
        word = M.INFO[page['method']][2] if page.get('method') else plain(page['stt']) if len(plain(page['stt'])) <= 14 else verb_of(page)
        long = ' class="long"' if max(len(w) for w in re.split(r'[\s-]+', word)) > 8 else ''   # smaller type, see style.css
        seal = f'\n<div class="seal {page["st"]}" aria-hidden="true"><span{long}>{html.escape(word)}</span></div>'
        s = re.sub(r'(<section class="hero">.*?)(\n</section>)', lambda m: m.group(1) + seal + m.group(2), s, count=1, flags=re.S)
    # "Watch it decipher": a page with docs/reveal/<slug>.json and no reveal of its own gets one, once, right after the h2
    # the data names as its "anchor" (else before the sources); from then on it is ordinary page content
    rv = HERE / 'reveal' / f'{slug}.json'
    if slug != 'index' and rv.exists() and 'class="creveal"' not in s and '<main>' in s:
        anchor = json.loads(rv.read_text(encoding='utf-8')).get('anchor', '')
        fig = f'<figure class="creveal" data-src="reveal/{slug}.json"></figure>\n'
        m = anchor and re.search(r'<h2 id="%s"[^>]*>.*?</h2>\n?' % re.escape(anchor), s, re.S)
        m2 = re.search(r'<!-- replay:start -->|<h2 id="sources"', s)
        if m: s = s[:m.end()] + fig + s[m.end():]
        elif m2: s = s[:m2.start()] + fig + s[m2.start():]
        else: s = s.replace('</main>', fig + '</main>', 1)
    if 'class="creveal"' in s and 'cipher-reveal.js' not in s:
        s = s.replace('</body>', '<script src="cipher-reveal.js" defer></script>\n</body>', 1)
    # "Full texts": every document's transcription and decryption, and the key, from profile outcome.texts (_texts.py)
    s = re.sub(r'<!-- texts:start -->.*?<!-- texts:end -->\n?', '', s, flags=re.S)
    s = re.sub(r'<a href="#texts">Full texts</a>', '', s)
    tb = texts_html(page) if page else ''
    if tb:
        m = re.search(r'<!-- replay:start -->|<h2 id="sources"', s)
        s = s[:m.start()] + tb + s[m.start():] if m else s.replace('</main>', tb + '</main>', 1)
        s = re.sub(r'(<nav class="toc"[^>]*>.*?)(<a href="#sources">|</nav>)',
                   lambda m: m.group(1) + '<a href="#texts">Full texts</a>' + m.group(2), s, count=1, flags=re.S)
    # "How it was solved": the replay of the profile's solution steps, before the sources
    s = re.sub(r'<!-- replay:start -->.*?<!-- replay:end -->\n?', '', s, flags=re.S)
    s = re.sub(r'<script src="solve-replay\.js[^"]*" defer></script>\n?', '', s)
    if slug in STEPS:
        block = f'<!-- replay:start -->\n<figure class="sreplay" data-src="steps/{slug}.json"></figure>\n<!-- replay:end -->\n'
        m = re.search(r'<h2 id="sources"', s)
        s = s[:m.start()] + block + s[m.start():] if m else s.replace('</main>', block + '</main>', 1)
        s = s.replace('</body>', f'<script src="solve-replay.js?v={VERSION}" defer></script>\n</body>', 1)
    # the deep-zoom viewer on every page with a figure image (zoom.js; overlays from docs/zoom/<image>.json)
    s = re.sub(r'<script src="zoom\.js[^"]*" defer></script>\n?', '', s)
    if re.search(r'<figure[^>]*>\s*<img', s):
        s = s.replace('</body>', f'<script src="zoom.js?v={VERSION}" defer></script>\n</body>', 1)
    # versions, anchor for "Top", script
    s = re.sub(r'<link rel="stylesheet" href="style.css[^"]*">', f'<link rel="stylesheet" href="style.css?v={VERSION}">', s)
    if 'href="style.css' not in s: s = s.replace('</head>', f'<link rel="stylesheet" href="style.css?v={VERSION}">\n</head>', 1)
    s = re.sub(r'<link rel="stylesheet" href="pg-[a-z]+\.css[^"]*">\n?', '', s)
    if slug in PAGE_CSS:
        s = s.replace(f'<link rel="stylesheet" href="style.css?v={VERSION}">', f'<link rel="stylesheet" href="style.css?v={VERSION}">\n<link rel="stylesheet" href="pg-{slug}.css?v={PAGE_CSS[slug]}">', 1)
    # the tab icon: a wax seal with a key (favicon.svg, PNG fallbacks rendered from it)
    s = re.sub(r'<link rel="(?:icon|apple-touch-icon)"[^>]*>\n?', '', s)
    s = s.replace('</head>', ICONS + '</head>', 1)
    # page scripts carry a hash of their own content, so an edit reaches browsers without a VERSION bump
    s = re.sub(r'<script src="(secret|cipher-reveal|atlas|archmap|herovid)\.js(?:\?[^"]*)?"',
               lambda m: f'<script src="{m.group(1)}.js?v={hashlib.sha1((HERE / (m.group(1) + ".js")).read_bytes().replace(b"\r\n", b"\n")).hexdigest()[:8]}"', s)
    s = re.sub(r'<script src="site.js[^"]*"></script>\s*', '', s)
    s = s.replace('</body>', f'<script src="site.js?v={VERSION}"></script>\n</body>', 1)
    s = re.sub(r'<body(?![^>]*id=)', '<body id="top"', s, count=1)
    if slug in PAGE_STYLED and f'pg-{slug}' not in s.split('</head>')[-1][:200]:
        s = re.sub(r'<body([^>]*?)(?: class="([^"]*)")?>', lambda m: f'<body{m.group(1)} class="{(m.group(2) + " " if m.group(2) else "")}pg-{slug}">', s, count=1)
    if slug == 'findings':
        s = list_findings(s)
    if slug == 'index':
        s = mirror_findings(s)
        import _contributors_page as CP
        s = re.sub(r'<!-- help:start -->.*?<!-- help:end -->', lambda m: CP.helpband(PAGES, PROFILES), s, flags=re.S)
        s = re.sub(r'<!-- browse:start -->.*?<!-- browse:end -->', lambda m: browse_html(), s, flags=re.S)
        s = re.sub(r'\n*<!-- contrib:start -->.*?<!-- contrib:end -->', '', s, flags=re.S)
        s = s.replace('<!-- catalogue:end -->', '<!-- catalogue:end -->\n\n' + CP.strip(PAGES, PROFILES, CONTRIB), 1)
        s = re.sub(r'<!-- live:start -->.*?<!-- live:end -->\n?', '', s, flags=re.S)
        s = re.sub(r'<script src="home\.js[^"]*" defer></script>\n?', '', s)
        # the random button sits on the counts strip under the hero (.herostrip), or with the hero's buttons where there is none
        live_at = 'herostrip' if '<div class="herostrip">' in s else 'hero-cta'
        s = re.sub(r'(<div class="%s">.*?)(\s*</div>)' % live_at, lambda m: m.group(1) + '\n' + live_html() + m.group(2), s, count=1, flags=re.S)
        s = s.replace('</body>', f'<script src="home.js?v={VERSION}" defer></script>\n</body>', 1)
        feat = [next(p for p in PAGES if p['slug'] == f) for f in FEATURED]
        cards = ('<!-- cards:start -->\n<h2 id="featured">Start with these</h2>\n<div class="cards featured">\n' + ''.join(card_html(p) for p in feat) + '</div>\n'
                 '<p class="allws"><a href="highlights.html">Thirty favourites: the funny, the historic, the ingenious &rarr;</a></p>\n<!-- cards:end -->')
        s = re.sub(r'<!-- catintro:start -->.*?<!-- catintro:end -->', lambda m: catintro_html(), s, flags=re.S)
        # the hero's open count follows the catalogue on every build; the rest of the hero's counts come from _build_stats.py
        import _catalogue_page as C
        still_open = sum(1 for e in C.DATA['entries'] if C.is_open(e))
        s = re.sub(r'(<b>)[\d,]+(</b> ciphers still open)', lambda m: f'{m.group(1)}{still_open:,}{m.group(2)}', s, count=1)
        s = re.sub(r'<!-- cattop:start -->.*?<!-- cattop:end -->\n?', '', s, flags=re.S)
        s = re.sub(r'(<h2 id="catalogue">.*?)(\n<p><a class="more" href="catalogue\.html")', lambda m: m.group(1) + '\n' + cattop_html().rstrip('\n') + m.group(2), s, count=1, flags=re.S)
        s = re.sub(r'<!-- cards:start -->.*?<!-- cards:end -->', lambda m: cards, s, flags=re.S)
    # the button under the hero that goes straight to the text
    s = re.sub(r'\n?<p class="readjump">.*?</p><!-- /readjump -->', '', s, flags=re.S)
    jump = readjump_html(page, lr, tb) if page else ''
    if jump and '<section class="hero">' in s:
        s = re.sub(r'(<section class="hero">.*?</h1>(?:\s*<div class="parties">.*?</div><!-- /parties -->)?)', lambda m: m.group(1) + '\n' + jump, s, count=1, flags=re.S)
    # how to cite the page, at the end of the body
    s = re.sub(r'<!-- cite:start -->.*?<!-- cite:end -->\n?', '', s, flags=re.S)
    if page and '</main>' in s: s = s.replace('</main>', cite_html(page, rec) + '</main>', 1)
    s = head_tags(slug, s)
    s = IMG.annotate(s)
    s = protect_text(s)
    after = content_hash(s)
    if after != rec['hash']:     # a generated element normalise() does not know about
        print(f'  note: {slug} rehashed after build; check normalise()')
        rec['hash'] = after
    path.write_text(s, encoding='utf-8')
    return slug

# ---------------------------------------------------------------------------
# Search.  search-t.json / search-b.json (titles, then body texts) are a flat list of entries that the overlay in
# site.js loads when the box is opened and when the first query is typed: one entry per page (title, blurb and
# opening text) and one per h2 section (heading and the section's text), each
# with the URL that lands on it, plus one per entry of ../catalogue.json.  The
# text is the page as a reader sees it, tags removed, so a word from a quoted
# cipher line or a footnote is found as readily as a title.  Keys: u url,
# t title, h section heading, p page label, y year, st status class,
# stt status text, b body text.
def visible_text(frag):
    frag = re.sub(r'<(script|style|svg)\b.*?</\1>', ' ', frag, flags=re.S)
    frag = re.sub(r'<[^>]+>', ' ', frag)
    frag = html.unescape(frag).replace('\xa0', ' ')
    return re.sub(r'\s+', ' ', frag).strip()

def search_entries():
    out = []
    for path in sorted(HERE.glob('*.html')):
        slug = path.stem
        if slug in ('catalogue', 'writeups', '404'): continue   # catalogue from catalogue.json below; writeups is a list of the pages
        s = path.read_text(encoding='utf-8')
        s = re.sub(r'<!-- cite:start -->.*?<!-- cite:end -->', ' ', s, flags=re.S)
        s = re.sub(r'<header class="nav">.*?</header>|<div class="search" id="search".*?</div>\n</div>|<footer.*?</footer>|'
                   r'<nav class="toc".*?</nav>', ' ', s, flags=re.S)
        p = next((q for q in PAGES if q['slug'] == slug), None)
        tm = re.search(r'<h1[^>]*>(.*?)</h1>', s, re.S) or re.search(r'<title>(.*?)</title>', s, re.S)
        title = visible_text(p['title'] if p else (tm.group(1) if tm else slug))
        m = re.search(r'<main>(.*?)</main>', s, re.S)
        body = m.group(1) if m else s
        hero = re.search(r'<(header|section|div) class="hero.*?</\1>', s, re.S)
        hero = re.sub(r'<div class="cipherstrip">.*?</div>', ' ', hero.group(0), flags=re.S) if hero else ''   # decorative digits
        base = dict(p=visible_text(p['label']) if p else {'index': 'Overview'}.get(slug, title), y=visible_text(p['year']) if p else '',
                    st=p['st'] if p else '', stt=visible_text(p['stt']) if p else '')
        parts = re.split(r'(?=<h2 id="[^"]+")', body)
        intro = visible_text((p['blurb'] if p else '') + ' ' + hero + ' ' + parts[0])
        out.append(dict(base, u=f'{slug}.html', t=title, h='', b=intro))
        for part in parts[1:]:
            hm = re.match(r'<h2 id="([^"]+)"[^>]*>(.*?)</h2>', part, re.S)
            if not hm: continue
            head = visible_text(re.sub(r'<span class="num">.*?</span>', '', hm.group(2)))
            text = visible_text(part[hm.end():])
            if not text and not head: continue
            out.append(dict(base, u=f'{slug}.html#{hm.group(1)}', t=title, h=head, b=text))
    try:
        cat = json.loads((HERE.parent / 'catalogue.json').read_text(encoding='utf-8'))
        for e in cat['entries']:
            b = ' · '.join(str(e.get(k) or '') for k in ('correspondents', 'place', 'shelfmark', 'status', 'why', 'verify', 'outcome'))
            out.append(dict(u=f'solve/{e["id"]}.html', t=e['title'], h='', p='Catalogue',
                            y=str(e.get('date') or e.get('year') or ''), st='', stt=f'no. {e["id"]}', b=visible_text(b)))
    except FileNotFoundError:
        pass
    return out

SEARCH_SHARDS = 16      # site.js has the same number

def write_search_index():
    # A first visit to the search box costs the small file: search-t.json (every key but b) is what the palette fetches
    # on opening. The b texts are in SEARCH_SHARDS files, search-b/NN.json ([[url, text], ...]), which the palette fetches
    # one at a time after the first query and stops fetching when it is closed. A page always falls in the same shard,
    # so a new write-up rewrites one small file, not the whole index.
    entries = search_entries()
    dump = lambda o: json.dumps(o, ensure_ascii=False, separators=(',', ':'))
    (HERE / 'search-t.json').write_text(dump([{k: v for k, v in e.items() if k != 'b'} for e in entries]), encoding='utf-8')
    shards = [[] for _ in range(SEARCH_SHARDS)]
    for e in entries:
        shards[int(hashlib.sha1(e['u'].split('#')[0].encode()).hexdigest()[:6], 16) % SEARCH_SHARDS].append([e['u'], e['b']])
    (HERE / 'search-b').mkdir(exist_ok=True)
    for i, rows in enumerate(shards):
        (HERE / 'search-b' / f'{i:02d}.json').write_text(dump(rows), encoding='utf-8')
    for old in (HERE / 'search.json', HERE / 'search-b.json'):
        if old.exists(): old.unlink()
    return len(entries)

# The home page's live header (home.js): a random-cipher button, and the list of
# reveal passages the header deciphers in turn (reveal/index.json).
def live_html():
    rv = sorted(p.stem for p in (HERE / 'reveal').glob('*.json') if p.stem != 'index')
    titles = {p['slug']: plain(p['label']) for p in PAGES}
    (HERE / 'reveal' / 'index.json').write_text(json.dumps([dict(slug=r, label=titles.get(r, r)) for r in rv if r in titles],
                                                           ensure_ascii=False), encoding='utf-8')
    return '<!-- live:start -->\n<button type="button" class="randbtn" aria-label="Open a random write-up">Random cipher &rarr;</button>\n<!-- live:end -->'

# steps/<slug>.json: the solution steps of each target's profile.json, with its conditions and outcome, for the
# "How it was solved" replay (solve-replay.js).  A profile folder is its page's slug, give or take case.
STEPS = set()
def write_steps():
    slugs = {p['slug'] for p in PAGES}
    out = HERE / 'steps'; out.mkdir(exist_ok=True)
    for folder, f in M.profile_paths().items():
        slug = PROFILE_SLUG.get(folder, folder)
        if slug not in slugs: continue
        pr = json.loads(f.read_text(encoding='utf-8'))
        steps = pr.get('solution') or []
        if len(steps) < 3: continue
        c = pr.get('conditions', {})
        d = dict(slug=slug, title=pr.get('title', ''), steps=steps, outcome=pr.get('outcome', {}),
                 attack=c.get('attack'), inputs=c.get('inputs', []), prior=c.get('prior_solution', {}),
                 human=c.get('human_role'), first=c.get('first_date'), last=c.get('last_date'))
        (out / f'{slug}.json').write_text(json.dumps(d, ensure_ascii=False, separators=(',', ':')), encoding='utf-8')
        STEPS.add(slug)
    return len(STEPS)

KEY_KINDS = {'contemporary key', 'archive key', 'DECODE key record', "scholar's key", 'rebuilt here'}
KEY_HOWS = {'read unchanged', 'adapted', 'rebuilt from', 'partial', 'explained'}

def check_keys(meta):
    """docs/keys.json, the key web: every edge points at a key and a page that exist, kinds and edge types from fixed lists."""
    kw = json.loads((HERE / 'keys.json').read_text(encoding='utf-8'))
    slugs, errs = {m['slug'] for m in meta}, []
    ids = [k['id'] for k in kw['keys']] + [s['id'] for s in kw.get('sources', [])]
    errs += [f'duplicate id {i}' for i in sorted({i for i in ids if ids.count(i) > 1})]
    for k in kw['keys']:
        if k.get('kind') not in KEY_KINDS: errs.append(f"{k['id']}: kind {k.get('kind')!r} not in {sorted(KEY_KINDS)}")
        if '&' in k.get('label', '') and ';' in k['label']: errs.append(f"{k['id']}: HTML entity in label (write plain text)")
        if not (k.get('year') is None or type(k['year']) is int): errs.append(f"{k['id']}: year {k['year']!r} is not an integer or null")
        im = k.get('image')
        if im and (not (HERE / im['src']).exists() or not im.get('credit')): errs.append(f"{k['id']}: image missing or uncredited")
    for kind, rows in (('link', kw['links']), ('tried', kw.get('tried', []))):
        for l in rows:
            if l['key'] not in ids: errs.append(f"{kind} {l['key']} -> {l['target']}: no such key")
            if l['target'] not in slugs: errs.append(f"{kind} {l['key']} -> {l['target']}: no page {l['target']}.html")
            if kind == 'link' and l.get('how') not in KEY_HOWS: errs.append(f"link {l['key']} -> {l['target']}: how {l.get('how')!r}")
    for l in kw.get('source_links', []):
        if l['source'] not in ids or l['key'] not in ids: errs.append(f"source link {l['source']} -> {l['key']}: no such node")
    hub = {l['key'] for l in kw.get('source_links', []) if l['source'] == 's-cyphersolver'}
    errs += [f"{k['id']}: rebuilt here but not linked to s-cyphersolver (source_links)" for k in kw['keys'] if k['kind'] == 'rebuilt here' and k['id'] not in hub]
    linked = {l['target'] for l in kw['links']}
    errs += [f'unlinked {t} also has a key link' for t in kw.get('unlinked', {}) if t in linked]
    if errs: raise SystemExit('docs/keys.json:\n  ' + '\n  '.join(errs))
    return len(kw['keys']), len(kw['links']), len(kw.get('tried', []))


def shared_checkout_note():
    """The main checkout is shared by several sessions. A build there rewrites about 2,000 generated files, which then
    block every pull until someone discards them (9 Nov 2026 audit). Linked worktrees and CI are the places to build."""
    if os.environ.get('GITHUB_ACTIONS') or not (HERE.parent / '.git').is_dir(): return ''
    return ('note: this is the shared main checkout. Build in your own worktree (git worktree add) where you can; if you '
            'build here, commit or restore every generated file you changed before you stop (git status -sb docs).')


if __name__ == '__main__':
    if shared_checkout_note(): print(shared_checkout_note())
    print('findings moved from index.html to findings.html:', absorb_findings())
    print('solution replays:', write_steps())
    import _catalogue_page as C                 # catalogue.html reads README results and open PRs too: rebuilt every time
    C.build_html()
    import _further_page as F                   # further.html: the readings left partial, from each NOTES.md Remaining gaps
    print('further: %d partial readings' % F.build_html(PAGES))
    import _archives_page as AR                 # archives.html: requests for archives and libraries, from archive_requests.json
    print('archives: %d open requests' % AR.build_html(PAGES))
    sys.path.insert(0, str(HERE.parent / 'tools')); import seed_archive_requests as SAR
    new, gone = SAR.main(dry=True, quiet=True)
    if new or gone: print(f'archives: {new} needs-physical-access gaps not in archive_requests.json, {gone} gone from NOTES; run python tools/seed_archive_requests.py')
    for f in sorted(HERE.glob('*.html')):      # date every page before any menu is built: the menu lists the newest
        page_dates(f.stem, f.read_text(encoding='utf-8').lstrip('﻿'))
    (HERE / 'writeups.html').write_text(writeups_html(), encoding='utf-8')
    (HERE / 'glossary.html').write_text(glossary_html(), encoding='utf-8')
    import _contributors_page as CP
    (HERE / 'contributors.html').write_text(CP.page(PAGES, PROFILES, CONTRIB, DATES['pages'], VERSION, TODAY), encoding='utf-8')
    done =[process(p) for p in sorted(HERE.glob('*.html'))]
    C.build_solve_pages()                       # docs/solve/<id>.html take the nav and footer from the built catalogue.html
    print('further pages:', F.build_pages(PAGES))   # docs/further/<slug>.html, likewise from the built further.html
    save_dates(DATES)
    print('search index:', write_search_index(), 'entries')
    write_menu()
    import _feeds as FD
    print('feed:', FD.write_feed([p for p in PAGES if p['slug'] not in SURVEYS], DATES['pages'], plain), 'entries; sitemap:', FD.write_sitemap(DATES['pages']), 'urls')
    readme_glance()
    # pages.json: label, year and outcome of every write-up, for the atlas and the key web
    meta = [dict(slug=p['slug'], label=plain(p['label']), title=plain(p['title']), y=p['y'], st=p['st'], stt=plain(p['stt']),
                 **({'m': M.KEY[p['method']]} if p.get('method') in M.KEY else {}),
                 **({'people': [{k: q[k] for k in ('role', 'name', 'img')} for q in PORTRAITS[p['slug']]]} if PORTRAITS.get(p['slug']) else {}))
            for p in PAGES if p['slug'] not in SURVEYS]
    (HERE / 'pages.json').write_text(json.dumps(meta, ensure_ascii=False, separators=(',', ':')), encoding='utf-8')
    sys.path.insert(0, str(HERE.parent / 'tools')); import atlas_places    # atlas letters from profile routes/places
    print('atlas: %d letters from profiles (%d new places)' % atlas_places.sync({m['slug']: m for m in meta}))
    import _atlas_data as AD                                               # the Atlas's reading panel, unread layer and chapters
    (atfiles, attexts), (atopen, atopenall), atstories, atpeople = AD.build(PAGES, PROFILES, IMAGES)
    print(f'atlas: {atfiles} write-ups with panel data, {attexts} letters with a text, {atopen} of {atopenall} open letters placed, {atstories} chapters, {atpeople} letters with their own people')
    print('key web: %d keys, %d links, %d tried' % check_keys(meta))
    print('built', ', '.join(done))
