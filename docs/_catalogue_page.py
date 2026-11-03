"""Build docs/catalogue.html and the tables in ../CATALOGUE.md from ../catalogue.json.

Run from docs/:  python _catalogue_page.py   (it runs _build_site.py afterwards for the nav, footer and contents
strip; a catalogue.html left with the bare <!-- site:nav --> marker has no navigation bar).

catalogue.json is the single source: entries with 1-5 scores for importance, solvability and difficulty.
The page embeds the JSON and computes a priority score client-side from adjustable weights; it also renders a
static table for readers without JavaScript. CATALOGUE.md gets its table (counted entries, default weights) and
its "Also noted" list rewritten between <!-- table:start --> / <!-- table:end --> and <!-- also:start --> /
<!-- also:end --> markers; the prose around them is hand-written and left alone.
"""
import json, html, pathlib, re, datetime
import _methods as M
import _claims

HERE = pathlib.Path(__file__).parent
ROOT = HERE.parent
DATA = json.loads((ROOT / 'catalogue.json').read_text(encoding='utf-8'))
W = DATA['weights_default']
GALLICA = 'https://gallica.bnf.fr/ark:/12148/'
CONTRIB = {c['id']: c for c in json.loads((ROOT / 'contributors.json').read_text(encoding='utf-8'))['contributors']}


def priority(e, w=W):
    """0-10: weighted mean of importance, solvability and ease (6 - difficulty), each 1-5, rescaled."""
    tot = w['importance'] + w['solvability'] + w['ease']
    v = (w['importance'] * e['importance'] + w['solvability'] * e['solvability'] + w['ease'] * (6 - e['difficulty'])) / tot
    return round((v - 1) / 4 * 10, 1)


def is_open(e):
    """Still in the open ranking: no outcome, or attempted but not read."""
    return not e.get('outcome') or e['outcome'].startswith('attempted')


def esc(t):
    return html.escape(str(t), quote=False)


def is_ark(a):
    return bool(re.match(r'^(btv1b|bpt6k)\w+$', a or ''))


AS_OF = DATA.get('status_as_of', '')            # the day every entry's known/open split was last checked


def fmt_day(iso):
    if not iso: return ''
    y, m, d = iso.split('-')
    return f"{int(d)} {['Jan','Feb','Mar','Apr','May','June','July','Aug','Sept','Oct','Nov','Dec'][int(m)-1]} {y}"


# ---------- what has left the catalogue ----------
# The README result tables are the ledger of finished targets; a row that cites "catalogue N" says that catalogue
# number (or part of it) has an outcome. Read them so a reader holding an old catalogue number can see where it went.
CAT_RE = re.compile(r'catalogue(?: items?| nos?\.)? (\d+(?:\s*(?:\+|,|and|&)\s*\d+)*)')
OPEN_SECTIONS = {'Not solved', 'Not applicable', 'In progress', 'Surveys'}


def solved_map():
    """{catalogue id: [(target, method, landed, slug or None, part)]} from README.md's Results tables."""
    out, sec = {}, None
    for line in (ROOT / 'README.md').read_text(encoding='utf-8').splitlines():
        if line.startswith('## '): sec = None
        if line.startswith('### '): sec = line[4:].strip()
        if not sec or sec in OPEN_SECTIONS or not line.startswith('| ') or line.startswith('| Target') or line.startswith('|---'): continue
        cells = [c.strip() for c in line.strip().strip('|').split('|')]
        if len(cells) < 5: continue
        m = CAT_RE.search(cells[0])
        if not m: continue
        ids = [int(x) for x in re.findall(r'\d+', m.group(1))]
        name = re.sub(r'\*\*|\[|\]\([^)]*\)', '', cells[0])
        name = re.sub(r'\s*\((?:[^()]|\([^()]*\))*(?:catalogue|DECODE)(?:[^()]|\([^()]*\))*\)\s*$', '', name).strip()
        slug = re.search(r'dbourdeau\.github\.io/cyphersolver/([\w-]+)\.html', line)
        part = bool(re.search(r'catalogue(?: item)? \d+[^)]*?part|split \d|from catalogue', cells[0]))
        for i in ids:
            out.setdefault(i, []).append((name, sec, cells[2], slug.group(1) if slug else None, part))
    return out


def open_prs():
    """Open pull requests, refreshed with gh when it is available, else the copy cached at the last build."""
    cache = HERE / '_open_prs.json'
    try:
        import subprocess
        r = subprocess.run(['gh', 'pr', 'list', '--state', 'open', '--json', 'number,title,url,author,updatedAt'],
                           capture_output=True, text=True, encoding='utf-8', timeout=30, cwd=ROOT)
        if r.returncode == 0:
            prs = json.loads(r.stdout)
            cache.write_text(json.dumps(prs, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
            return prs
    except Exception:
        pass
    return json.loads(cache.read_text(encoding='utf-8')) if cache.exists() else []


def link_pairs(e):
    """(label, href) for each Gallica ark and each extra link (e['links'], e.g. DECODE records); href None = text only."""
    out = []
    for k in ('ark', 'ark2'):
        a = e.get(k)
        if a: out.append((a, GALLICA + a if is_ark(a) else None))
    for l in e.get('links') or []:
        out.append((l['label'], l['href']))
    return out


def ark_links(e):
    return ' · '.join(f'<a href="{h}" rel="noopener">{esc(t)}</a>' if h else esc(t) for t, h in link_pairs(e))


def md_links(e, sep):
    return sep.join((f'[{t}]({h})' if h else t) if not is_ark(t) else f'ark {t}' for t, h in link_pairs(e))


# ---------- Markdown ----------
def md_table(entries, outcome=False):
    first = 'Outcome' if outcome else 'Prio.'
    rows = [f'| {first} | # | Date | Item | Shelfmark / access | Status & prior art | Why it matters | Imp. | Solv. | Diff. | Cls | Seen |',
            '|---|---|---|---|---|---|---|---|---|---|---|---|']
    for e in entries:
        arks = md_links(e, '; ')
        shelf = e['shelfmark'] + (f' ({arks})' if arks else '') + (f'; {e["folio_note"]}' if e.get('folio_note') else '')
        seen = '●' if seen_image(e) else '◇'
        lead = f"**{e['outcome']}**" if outcome else f"**{priority(e)}**"
        st = f"**Known ({e.get('as_of') or AS_OF}):** {e['known']} **Open:** {e['open']}" if e.get('known') else e['status']
        rows.append(f"| {lead} | {e['id']} | {e['date']} | {e['title']}: {e['correspondents']} | {shelf} | {st} | {e['why']} | {e['importance']} | {e['solvability']} | {e['difficulty']} | {e['cls']} | {seen} |")
    return '\n'.join(rows)


def md_also(entries):
    out = []
    for e in entries:
        arks = md_links(e, ', ')
        out.append(f"- **{e['title']}**, {e['date']}, {e['shelfmark']}{(', ' + arks) if arks else ''}. {e['status']} {e['why']} "
                   f"Imp. {e['importance']}, solv. {e['solvability']}, diff. {e['difficulty']}, class {e['cls']}, priority {priority(e)}.")
    return '\n'.join(out)


def update_md():
    p = ROOT / 'CATALOGUE.md'
    s = p.read_text(encoding='utf-8')
    counted = sorted([e for e in DATA['entries'] if e['counted'] and is_open(e)], key=lambda e: (-priority(e), e['id']))
    also = sorted([e for e in DATA['entries'] if not e['counted']], key=lambda e: (-priority(e), e['id']))
    s = re.sub(r'## The \d+ open targets, by priority', f'## The {len(counted)} open targets, by priority', s)
    s = re.sub(r'<!-- table:start -->.*?<!-- table:end -->', lambda m: '<!-- table:start -->\n' + md_table(counted) + '\n<!-- table:end -->', s, flags=re.S)
    s = re.sub(r'<!-- also:start -->.*?<!-- also:end -->', lambda m: '<!-- also:start -->\n' + md_also(also) + '\n<!-- also:end -->', s, flags=re.S)
    p.write_text(s, encoding='utf-8')


# ---------- HTML ----------
# Correspondents with a public-domain portrait on the site (_portraits.json), matched by hand-checked patterns
# on the "correspondents" field; a wrong face is worse than none, so ambiguous names carry a date test.
PORTRAITS = {}
for _v in json.loads((HERE / '_portraits.json').read_text(encoding='utf-8')).values():
    for _p in _v:
        if _p.get('img'): PORTRAITS.setdefault(_p['name'], _p['img'])
FACES = [
    (r'Frederick II', 'Frederick II', lambda e: 1740 <= e['year'] <= 1786),
    (r'Henry Percy', 'Henry Percy', None),
    (r"Catherine de' Medici|Catherine de M[ée]dicis", "Catherine de' Medici", None),
    (r'Charles I\b', 'Charles I', lambda e: 1625 <= e['year'] <= 1649),
    (r'Charles I\b|Charles V\b', 'Charles V', lambda e: 1516 <= e['year'] <= 1558),
    (r'Francis I(?:st)?\b|Franis I\b', 'Francis I', lambda e: 1515 <= e['year'] <= 1547),
    (r'Montmorency', 'Anne de Montmorency', lambda e: 1520 <= e['year'] <= 1567),
    (r'duke of Nevers|duc de Nevers|Duke of Nivernois', 'Duke of Nevers', lambda e: 1565 <= e['year'] <= 1595),
    (r'Merc(?:œ|oe)ur', 'Duc de Mercœur', None),
    (r'Henri II\b', 'Henry II', lambda e: 1547 <= e['year'] <= 1559),
    (r'R[áa]k[óo]czi', 'Francis II Rákóczi', lambda e: 1700 <= e['year'] <= 1735),
    (r'Oxenstierna', 'Axel Oxenstierna', None),
    (r'Secretary Cecil|Burghley|Burleigh|Baurleigh', 'William Cecil', lambda e: 1550 <= e['year'] <= 1598),
    (r'Walsingham', 'Francis Walsingham', lambda e: 1568 <= e['year'] <= 1590),
    (r'Elizabeth R\b', 'Elizabeth I', lambda e: 1558 <= e['year'] <= 1603),
    (r'William V\b', 'William V', lambda e: 1766 <= e['year'] <= 1806),
    (r'Maarten van der Goes', 'Maarten van der Goes', None),
    (r'Dirk van Hogendorp', 'Dirk van Hogendorp', None),
    (r'Starhemberg|Staremberg', 'Gundaker Starhemberg', lambda e: 1700 <= e['year'] <= 1745),
]

def faces(e):
    """(name, image) for each correspondent of e with a portrait, in the order they appear (sender first)."""
    c, out = e['correspondents'], []
    for pat, name, ok in FACES:
        m = re.search(pat, c)
        if m and re.match(r'\w*\s?\?', c[m.end():]): m = None      # a name the catalogue itself queries
        if m and name in PORTRAITS and (ok is None or ok(e)) and name not in [n for _, n, _ in out]:
            out.append((m.start(), name, PORTRAITS[name]))
    return [(n, i) for _, n, i in sorted(out)]

def people_html(e):
    f = faces(e)
    if not f: return ''
    tip = esc(' → '.join(n for n, _ in f)).replace('"', '&quot;')
    return f'<span class="avs" title="{tip}">' + ''.join(f'<img src="{i}" alt="" loading="lazy">' for _, i in f) + '</span>'

def blank_html(e):
    """No portrait: a small wax roundel with the entry's language initial."""
    return f'<span class="avs none" aria-hidden="true"><i>{esc((e.get("language") or "?")[:2])}</i></span>'



# ---------- HTML ----------
def dots(v, cls=''):
    return f'<span class="dots {cls}" title="{v} of 5">' + ''.join(f'<i class="{"on" if i < v else ""}"></i>' for i in range(5)) + '</span>'


SOLVED = solved_map()
# Target folders that name an entry at the head of their NOTES.md (_claims.py). A claimant whose Status is "in
# progress" tags the entry "in progress" on the table and its page, whatever outcome catalogue.json carries: the
# "attempted, open" tag only arrives when the writeup skill closes the target.
CLAIMS = _claims.claims()


def progress(e):
    """The folders working on e now, as (folder, state, status line)."""
    return _claims.in_progress(CLAIMS.get(e['id'], []))


def parts_html(e):
    """Links to the write-ups of pieces of an open entry that already have an outcome (README rows citing its number)."""
    L, seen = [], set()
    for n, _, _, sl, _ in SOLVED.get(e['id'], []):
        if sl and sl not in seen: seen.add(sl); L.append((n, sl))
    if not L: return ''
    return ('<span class="ko"><i class="k">written up</i> '
            + ' · '.join(f'<a href="{sl}.html" title="{esc(n).replace(chr(34), "&quot;")}">{sl}</a>' for n, sl in L) + '</span>')


# The table shows one thin row per cipher; everything else, with the instructions for an AI agent, is on the
# cipher's own page, docs/solve/<id>.html, so a helper can hand an agent one URL (feedback of 26 Oct 2026).
SITE = 'https://dbourdeau.github.io/cyphersolver/'
REPO = 'https://github.com/dbourdeau/cyphersolver'
CLASS_TEXT = {
    'A': 'a sibling letter with a decipherment is in the same volume or series, so matching it is the first move',
    'B': 'part of a key or a known cipher family of the same office is in print or on DECODE',
    'C': 'no key and no deciphered sibling is known, so expect a ciphertext-only attack',
}


def short_outcome(e):
    return 'in progress' if progress(e) else (e.get('outcome') or 'open').split(':')[0]


def solve_href(e):
    return f'solve/{e["id"]}.html'


HELP = {'obtain': ('Help obtain', 'the document is not online: the first step is a copy, from the archive or a reading-room photograph'),
        'read': ('Help read', 'the key material exists; what is left is the reading'),
        'solve': ('Help solve', 'the ciphertext is online and no key is known')}


def help_kind(e):
    """George Lasry's three stickers (30 Oct 2026): which help the entry needs first."""
    if e.get('access') == 'archive': return 'obtain'
    if e.get('workable'): return 'read'
    return 'solve'


def frame_info(e):
    """(state, text, href) for the page/frame where the cipher was confirmed. state: confirmed | viewed | unconfirmed."""
    fc = e.get('frame_check') or {}
    if fc.get('result') == 'confirmed':
        return ('confirmed', f"{fc.get('frame', '')}: {fc.get('saw', '')} (checked {fc.get('date', '')} by an LLM on the page)", fc.get('href', ''))
    if fc.get('result') == 'no_cipher_at_frame':
        return ('missing', f"The frame named in the description ({fc.get('frame', '')}) shows no cipher: {fc.get('saw', '')} {fc.get('note', '')} (checked {fc.get('date', '')})", fc.get('href', ''))
    v = e.get('vetting') or {}
    sn = v.get('seen') or {}
    if sn.get('kind') in ('scan', 'facsimile', 'transcription'):
        m = re.search(r'https?://\S+', sn.get('where') or '')
        return ('confirmed', f"{sn.get('cipher', '')} ({sn.get('where', '')}; checked {v.get('date', '')} by {v.get('by', 'an LLM')})",
                m.group(0).rstrip(').,;') if m else '')
    if e.get('seen') != 'catalogue':
        return ('viewed', 'The cipher was viewed on the image when the entry was written; the frame is not recorded separately.', '')
    return ('unconfirmed', 'No one has yet confirmed the cipher on a specific page or frame. The location comes from the written description of the document, not from a page.', '')


def row(e):
    href = solve_href(e)
    seen = '<span class="seen img" title="viewed on the image">●</span>' if seen_image(e) else '<span class="seen cat" title="catalogue description only">◇</span>'
    tip = f' title="being worked in targets/{", targets/".join(f for f, _, _ in progress(e))}/"' if progress(e) else ''
    pill = f'<span class="pill{" att" if e.get("outcome") or tip else ""}"{tip}>{esc(short_outcome(e))}</span>'
    if e.get('workable'): pill += '<span class="pill work" title="the key material exists (siblings, glosses); what is left is work, not an outside blocker">no outside blocker</span>'
    if e.get('access') == 'archive': pill += '<span class="pill arch" title="the ciphertext or the key material is not online; it needs the archive to digitise it or someone to photograph it">needs archive scans</span>'
    if (e.get('vetting') or {}).get('key_in_volume'): pill += '<span class="pill work" title="a key is filed in the same volume or unit and no decipherment exists; a reading would be read with known key">key in volume</span>'
    hk = help_kind(e)
    pill = f'<span class="pill help-{hk}" title="{esc(HELP[hk][1])}">{HELP[hk][0]}</span>' + pill
    if frame_info(e)[0] == 'unconfirmed': pill += '<span class="pill unf" title="no one has confirmed the cipher on a specific frame yet">frame unchecked</span>'
    link = ''.join(f'<a href="{h}" rel="noopener">{esc(t)}</a>' if h else esc(t) for t, h in link_pairs(e)[:1])
    return (f'<tr class="e" data-id="{e["id"]}" data-href="{href}">'
            f'<td class="prio"><b>{priority(e):.1f}</b></td>'
            f'<td class="date">{esc(e["date"])}<span class="num">no. {e["id"]}</span></td>'
            f'<td class="item"><a class="t" href="{href}">{seen} {esc(e["title"])}</a>{pill}<span class="sub">{esc(e["why"])}</span></td>'
            f'<td class="shelf"><span class="sm" title="{html.escape(e["shelfmark"])}">{esc(e["shelfmark"])}</span>{link}</td>'
            f'<td class="sc">{dots(e["importance"])}</td><td class="sc">{dots(e["solvability"])}</td><td class="sc">{dots(e["difficulty"], "diff")}</td>'
            f'<td class="cls"><span class="badge {e["cls"]}">{e["cls"]}</span></td></tr>')


# ---------- filter keys ----------
# The catalogue fields are free text written by many sweeps ('Polish/French (unknown which; ...)', 'Archivportal-D
# sweep', 'images'), so the table filters on a few clean keys derived here, in entry['f'], not on the raw values.
# Language keys are the lowercase names the writeups.html Language facet uses, so a #lang=french link works on both.
CAT_LANGS = ['French', 'German', 'English', 'Portuguese', 'Italian', 'Spanish', 'Latin', 'Dutch', 'Polish', 'Swedish',
             'Danish', 'Hungarian']
LANG_ALIAS = {'castilian': 'Spanish', 'scots': 'English'}
OTHER_LANGS = {'Russian', 'Czech', 'Catalan', 'Turkish', 'Greek', 'Arabic', 'Hebrew', 'Croatian', 'Romanian', 'Lithuanian'}
CENTURIES = [('1400s', '1400s'), ('1500s', '1500s'), ('1600s', '1600s'), ('1700s', '1700s'), ('1800s', '1800s'),
             ('1900s', '1900s'), ('undated', 'undated')]
SOURCES = [('decode', 'DECODE'), ('sweep', 'archive sweeps'), ('cryptoole', 'Cryptoole'), ('bnf', 'BnF / Gallica'),
           ('print', 'print and literature'), ('contributed', 'sent in')]
STATUSES = [('new', 'not attempted'), ('progress', 'in progress here'), ('attempted', 'attempted here'), ('skipped', 'skipped')]
ACCESS = [('online', 'no archive trip needed'), ('workable', 'no outside blocker'), ('archive', 'needs archive scans')]
CLASSES = [('A', 'A · sibling deciphered'), ('B', 'B · partial key known'), ('C', 'C · no key')]


def lang_keys(e):
    """'German / French' is both; 'French (some clear text translated into English)' is French; 'unknown (French/
    Polish)' falls back on the bracket. Names outside CAT_LANGS are 'other'."""
    v = str(e.get('language') or '')
    def names(s):
        ws = {LANG_ALIAS.get(w.lower(), w.capitalize()) for w in re.findall(r'[A-Za-z]+', s)}
        return (ws & set(CAT_LANGS)) | ({'other'} if ws & OTHER_LANGS else set())
    out = names(re.sub(r'\([^)]*\)', '', v)) or names(v)
    if not out:
        out = {'other'} if re.search(r'[A-Za-z]', v) and not re.match(r'(?i)\s*(unknown|none)', v) else {'unknown'}
    return sorted(l.lower() for l in out)


def century_key(e):
    y = e.get('year')
    return f'{y // 100}00s' if isinstance(y, int) and 1400 <= y < 2000 else 'undated'


def source_key(e):
    s = (e.get('source') or '').lower()
    if 'decode' in s: return 'decode'
    if 'cryptoole' in s: return 'cryptoole'
    if 'bnf' in s or 'gallica' in s: return 'bnf'
    if 'github' in s or 'hcportal' in s: return 'contributed'
    if re.search(r'print|calendar|literature|cryptiana', s): return 'print'
    return 'sweep'


def seen_image(e):
    return e['seen'] != 'catalogue'


def filter_keys(e):
    o = e.get('outcome') or ''
    return {'lang': lang_keys(e), 'century': century_key(e), 'region': e['region'], 'cls': e['cls'],
            'status': 'progress' if progress(e) else 'skipped' if 'skipped' in o else 'attempted' if o.startswith('attempted') else 'new',
            'access': [k for k, on in (('online', e.get('access') != 'archive'), ('workable', e.get('workable')), ('archive', e.get('access') == 'archive')) if on],
            'help': help_kind(e), 'frame': frame_info(e)[0],
            'source': source_key(e), 'seen': 'image' if seen_image(e) else 'catalogue',
            'counted': 'counted' if e['counted'] else 'noted'}


def facet(name, label, values, keys):
    """values: (key, label) pairs; a value no entry has is left out. Each chip carries a live count."""
    have = {k for f in keys for k in ([f[name]] if isinstance(f[name], str) else f[name])}
    opts = ''.join(f'<button type="button" class="chip" data-facet="{name}" data-val="{esc(k)}" aria-pressed="false">'
                   f'{esc(l)}<span class="n"></span></button>' for k, l in values if k in have)
    return f'<div class="facet" role="group" aria-label="{label}"><span class="flabel">{label}</span><span class="opts">{opts}</span></div>'


def dropdown(label, body, name=''):
    """A toolbar button that opens a small panel; the button shows what is chosen in it (filled in by the script)."""
    return (f'<details class="dd"{f' data-dd="{name}"' if name else ''}><summary><span class="dl">{label}</span><span class="dv"></span></summary>'
            f'<div class="pop">{body}</div></details>')


def by_count(keys, name, last=()):
    """The values of one facet, commonest first, with any in last kept at the end."""
    n = {}
    for f in keys:
        for k in ([f[name]] if isinstance(f[name], str) else f[name]): n[k] = n.get(k, 0) + 1
    return [(k, k) for k in sorted(n, key=lambda k: (k in last, -n[k], k))]


def is_blocked(e):
    o = e.get('outcome') or ''
    return 'blocked' in o or o.startswith('attempted, skipped')


def status_html(E):
    """The two lists a reader needs before starting work: what is known and what is still open, both dated."""
    day = fmt_day(datetime.date.today().isoformat())     # the build day: solved list, counts and PRs are computed now
    ids = {e['id'] for e in E}
    gone = sorted(set(SOLVED) - ids)
    part = sorted([e for e in E if (e.get('known') and not e['known'].startswith('Nothing')) or e['id'] in SOLVED], key=lambda e: e['id'])
    opn = sorted(E, key=lambda e: (-priority(e), e['id']))
    n_prog = sum(1 for e in E if progress(e))
    n_blk = sum(1 for e in E if is_blocked(e) and not progress(e))
    n_att = sum(1 for e in E if (e.get('outcome') or '').startswith('attempted') and not is_blocked(e) and not progress(e))
    prs = open_prs()

    def one(e, field):
        t = e.get(field) or e['status']
        return f'<li><a href="{solve_href(e)}">no. {e["id"]}</a> <b>{esc(e["title"])}</b> <span class="d">{esc(e["date"])}</span> &mdash; {esc(t)}</li>'

    gone_rows = ''.join(
        f'<tr id="e{i}g"><td>{i}</td><td>' + '<br>'.join(
            (f'<a href="{sl}.html">{esc(n)}</a>' if sl else esc(n)) + (' <span class="d">(part)</span>' if pt else '')
            for n, _, _, sl, pt in SOLVED[i]) + '</td><td>' + '<br>'.join(esc(m) for _, m, _, _, _ in SOLVED[i])
        + '</td><td>' + '<br>'.join(esc(l) for _, _, l, _, _ in SOLVED[i]) + '</td></tr>' for i in gone)
    pr_li = ''.join(f'<li><a href="{esc(r["url"])}" rel="noopener">#{r["number"]}</a> {esc(r["title"])} '
                    f'<span class="d">{esc((r.get("author") or {}).get("login", ""))}, updated {fmt_day(r["updatedAt"][:10])}</span></li>' for r in prs)
    html_ = f"""<section class="state" id="status">
<h2>Where things stand, {day}</h2>
<p>Before starting on an entry, read its <b>known</b> and <b>open</b> lines on its page and the open pull requests below. Work that has landed is folded into both lists at each rebuild; work still in a pull request is not. If a number you were given is not in the table, it has left the catalogue: <a href="#gone">look it up</a>. The lists and the pull requests are recomputed at every rebuild; each entry&rsquo;s known and open lines were written by hand and carry the day they were checked (all of them on {fmt_day(AS_OF)} at the latest full pass).</p>
<div class="cols">
<div class="scard"><h3>What is solved or known so far</h3>
<p><b>{len(gone)}</b> catalogue numbers have been deciphered, explained or found in print and have left the open list (<a href="#gone">the list</a>; every write-up is on the <a href="writeups.html">write-ups</a> page). <b>{len(part)}</b> of the entries still open have pieces already deciphered or identified.</p>
<details><summary>the {len(part)} open entries with known pieces</summary><ul class="sl">{"".join(one(e, "known") for e in part)}</ul></details>
</div>
<div class="scard"><h3>What is still unsolved</h3>
<p><b>{len(E)}</b> entries are open ({sum(1 for e in E if e['counted'])} counted targets, the rest also noted): <b>{n_prog}</b> in progress here (a target folder is working on them; its notes are linked from the entry&rsquo;s page), <b>{n_blk}</b> blocked from outside (no images online, an archive order needed, or no key known to exist), <b>{n_att}</b> attempted here without a decipherment, <b>{len(E) - n_prog - n_blk - n_att}</b> not yet attempted. <b>{sum(1 for e in E if e.get('workable'))}</b> have their key material at hand and no outside blocker ({', '.join(f'<a href="{solve_href(e)}">no. {e["id"]}</a>' for e in E if e.get('workable'))}): good places to start.</p>
<details><summary>the {len(E)} open entries, by priority, with what is still open</summary><ul class="sl">{"".join(one(e, "open") for e in opn)}</ul></details>
</div>
</div>
<div class="scard wide"><h3>Work in progress: {len(prs)} open pull request{"s" if len(prs) != 1 else ""}</h3>
{f'<ul class="sl">{pr_li}</ul>' if prs else '<p>None.</p>'}</div>
</section>"""
    return html_, gone_rows, len(gone)


# page rules live in style.css under body.pg-catalogue (the site build strips inline <style> from catalogue.html).
# The table script: search, facets, reweighting, sort; a row click opens the cipher's page. __GONE__ is replaced by
# the numbers that have left the catalogue, so an old catalogue.html#eNN link still lands somewhere useful.
CAT_JS = r'''
(function(){
document.body.classList.remove('nojs');
var D=JSON.parse(document.getElementById('catdata').textContent),E=D.entries,G=__GONE__,byId={};E.forEach(function(e){byId[e.id]=e;});
var hm=/^#e(\d+)$/.exec(location.hash);
if(hm&&byId[hm[1]]){location.replace('solve/'+hm[1]+'.html');return;}
if(hm&&G[hm[1]]){var hn=document.getElementById('hashnote');hn.innerHTML='Catalogue no. '+hm[1]+' is no longer open: '+G[hm[1]].map(function(x){var t=x[0].replace(/&/g,'&amp;').replace(/</g,'&lt;');return x[1]?'<a href="'+x[1]+'.html">'+t+'</a>':t;}).join(' · ');hn.hidden=false;}
var tb=document.querySelector('#cat tbody'),rows={};
Array.prototype.forEach.call(tb.querySelectorAll('tr.e'),function(r){rows[r.dataset.id]=r;});
var state={q:'',sort:'prio',dir:-1,w:{imp:D.weights.importance,sol:D.weights.solvability,eas:D.weights.ease},f:{}};
var chips=Array.prototype.slice.call(document.querySelectorAll('.chip[data-facet]')),clr=document.getElementById('reset'),qi=document.getElementById('q'),dds=Array.prototype.slice.call(document.querySelectorAll('.cfilters details.dd'));
dds.forEach(function(d){d.addEventListener('toggle',function(){if(!d.open)return;dds.forEach(function(o){if(o!==d)o.open=false;});
 var p=d.querySelector('.pop');p.style.left='';p.style.right='';if(p.getBoundingClientRect().right>document.documentElement.clientWidth-8){p.style.left='auto';p.style.right='0';}});});
document.addEventListener('click',function(ev){if(!ev.target.closest('.cfilters details.dd'))dds.forEach(function(d){d.open=false;});});
document.addEventListener('keydown',function(ev){if(ev.key==='Escape')dds.forEach(function(d){if(d.open){d.open=false;d.querySelector('summary').focus();}});});
function prio(e){var w=state.w,t=w.imp+w.sol+w.eas||1;var v=(w.imp*e.importance+w.sol*e.solvability+w.eas*(6-e.difficulty))/t;return Math.round((v-1)/4*100)/10;}
// e.f holds the clean filter keys built in Python; a facet matches when the entry has any of its chosen values
function vals(e,k){var v=e.f[k];return v==null?[]:[].concat(v);}
function hit(e,k){var s=state.f[k];if(!s||!s.length)return true;var v=vals(e,k);return s.some(function(x){return v.indexOf(x)>=0;});}
function texthit(e){if(!state.q)return true;var h=(e.id+' '+e.title+' '+e.correspondents+' '+e.place+' '+e.shelfmark+' '+e.why+' '+e.status+' '+(e.known||'')+' '+(e.open||'')+' '+e.region+' '+e.language+' '+e.date+' '+e.year).toLowerCase();return h.indexOf(state.q)>=0;}
function match(e,skip){if(!texthit(e))return false;for(var k in state.f)if(k!==skip&&!hit(e,k))return false;return true;}
// each chip's count: entries it would show, given every other facet and the search
function counts(){var c={};chips.forEach(function(b){c[b.dataset.facet+'|'+b.dataset.val]=0;});var ks={};chips.forEach(function(b){ks[b.dataset.facet]=1;});
 Object.keys(ks).forEach(function(k){E.forEach(function(e){if(match(e,k))vals(e,k).forEach(function(v){var x=k+'|'+v;if(x in c)c[x]++;});});});
 chips.forEach(function(b){var on=(state.f[b.dataset.facet]||[]).indexOf(b.dataset.val)>=0,n=c[b.dataset.facet+'|'+b.dataset.val];b.setAttribute('aria-pressed',on?'true':'false');b.querySelector('.n').textContent=n;b.classList.toggle('z',!n&&!on);});}
// each dropdown button names what is chosen in it: 'Language: French, Polish'
function labels(){dds.forEach(function(d){var ks=(d.dataset.dd||'').split(' '),on=[];ks.forEach(function(k){(state.f[k]||[]).forEach(function(v){var b=d.querySelector('.chip[data-facet="'+k+'"][data-val="'+v+'"]');if(b)on.push(b.firstChild.textContent);});});
 d.querySelector('.dv').textContent=on.length?': '+(on.length>2?on.length+' chosen':on.join(', ')):'';d.classList.toggle('act',on.length>0);});}
function save(){var p=[];for(var k in state.f)if(state.f[k].length)p.push(k+'='+state.f[k].map(encodeURIComponent).join(','));if(state.q)p.push('q='+encodeURIComponent(state.q));
 try{history.replaceState(null,'',p.length?'#'+p.join('&'):location.pathname);}catch(x){}}
function load(){var h=location.hash.slice(1);if(h.indexOf('=')<0)return;h.split('&').forEach(function(kv){var i=kv.indexOf('=');if(i<1)return;var k=kv.slice(0,i),v=decodeURIComponent(kv.slice(i+1));if(k==='q'){state.q=v.toLowerCase();qi.value=v;}else state.f[k]=v.split(',').filter(Boolean);});}
function key(e){var s=state.sort;if(s==='prio')return prio(e);if(s==='cls'||s==='title')return e[s];return +e[s];}
function render(keep){var L=E.filter(function(e){return match(e);});L.sort(function(a,b){var x=key(a),y=key(b);if(x<y)return -1*state.dir;if(x>y)return 1*state.dir;return a.id-b.id;});
 var shown={};L.forEach(function(e){var r=rows[e.id];r.querySelector('td.prio b').textContent=prio(e).toFixed(1);tb.appendChild(r);r.hidden=false;shown[e.id]=1;});
 E.forEach(function(e){if(!shown[e.id])rows[e.id].hidden=true;});
 var nf=0;for(var k in state.f)nf+=state.f[k].length;
 document.getElementById('count').textContent=(L.length===E.length?'All '+E.length:L.length+' of '+E.length)+' ciphers';
 clr.hidden=!(nf||state.q);clr.textContent=nf?'clear '+nf+' filter'+(nf>1?'s':''):'clear search';
 counts();labels();if(!keep)save();
 document.getElementById('v_imp').textContent=state.w.imp.toFixed(2);document.getElementById('v_sol').textContent=state.w.sol.toFixed(2);document.getElementById('v_eas').textContent=state.w.eas.toFixed(2);
 Array.prototype.forEach.call(document.querySelectorAll('#cat th[data-sort]'),function(h){h.setAttribute('aria-sort',h.dataset.sort===state.sort?(state.dir<0?'descending':'ascending'):'none');});}
Array.prototype.forEach.call(tb.querySelectorAll('tr.e'),function(r){r.addEventListener('click',function(ev){if(ev.target.closest('a'))return;if(ev.ctrlKey||ev.metaKey)window.open(r.dataset.href);else location.href=r.dataset.href;});});
Array.prototype.forEach.call(document.querySelectorAll('#cat th[data-sort]'),function(h){h.addEventListener('click',function(){var s=h.dataset.sort;if(state.sort===s)state.dir=-state.dir;else{state.sort=s;state.dir=(s==='year'||s==='title'||s==='cls'||s==='difficulty')?1:-1;}render();});});
chips.forEach(function(b){b.addEventListener('click',function(){var k=b.dataset.facet,v=b.dataset.val,s=state.f[k]=state.f[k]||[],i=s.indexOf(v);if(i<0)s.push(v);else s.splice(i,1);if(!s.length)delete state.f[k];render();});});
qi.addEventListener('input',function(ev){state.q=ev.target.value.trim().toLowerCase();render();});
[['w_imp','imp'],['w_sol','sol'],['w_eas','eas']].forEach(function(p){document.getElementById(p[0]).addEventListener('input',function(ev){state.w[p[1]]=ev.target.value/100;render();});});
clr.addEventListener('click',function(){state.q='';state.f={};qi.value='';render();});
document.getElementById('wreset').addEventListener('click',function(){state.sort='prio';state.dir=-1;state.w={imp:D.weights.importance,sol:D.weights.solvability,eas:D.weights.ease};document.getElementById('w_imp').value=state.w.imp*100;document.getElementById('w_sol').value=state.w.sol*100;document.getElementById('w_eas').value=state.w.eas*100;render();});
var qm=/[?&]q=([^&#]+)/.exec(location.search);if(qm){var qv=decodeURIComponent(qm[1].replace(/\+/g,' '));qi.value=qv;state.q=qv.trim().toLowerCase();}
if(!(hm&&G[hm[1]])){if(location.hash.indexOf('=')<0){state.f.access=['online'];state.f.status=['new'];}load();}
render(!location.hash||hm);
if(hm&&G[hm[1]])document.getElementById('hashnote').scrollIntoView();
})();
'''


def build_html():
    E = DATA['entries']
    state, gone_rows, n_gone = status_html(E)
    gone_js = json.dumps({i: [[n, sl] for n, _, _, sl, _ in SOLVED[i]] for i in sorted(set(SOLVED) - {e['id'] for e in E})}, ensure_ascii=False).replace('</', '<\\/')
    ordered = sorted(E, key=lambda e: (not is_open(e), not e['counted'], -priority(e), e['id']))
    counted = [e for e in E if e['counted'] and is_open(e)]
    keys = [filter_keys(e) for e in E]
    langs = [(l.lower(), l) for l in CAT_LANGS] + [('other', 'other'), ('unknown', 'unknown')]
    data_js = json.dumps({'weights': W, 'entries': [dict(e, f=k) for e, k in zip(E, keys)]}, ensure_ascii=False).replace('</', '<\\/')
    n_all, n_img = len(E), sum(1 for e in E if seen_image(e))
    n_dec = sum(1 for e in E if e.get('source') == 'DECODE')
    n_arch = sum(1 for e in E if e.get('access') == 'archive' and is_open(e))
    years = [e['year'] for e in E if e['year']]
    page = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>The Unsolved Catalogue — {len(E)} ciphers nobody has read</title>
<meta name="description" content="{len(E)} undeciphered historical cipher letters, {min(years)}–{max(years)}. Each has its own page with the sources, what has been tried, and instructions to hand to an AI agent.">
<link rel="stylesheet" href="style.css">
</head>
<body id="top" class="nojs">
<!-- site:nav -->

<section class="hero">
  <p class="kicker">{min(years)}–{max(years)} · {len(E)} ciphers · {n_gone} moved out to <a href="writeups.html">write-ups</a> · status as of {fmt_day(AS_OF)}</p>
  <h1>The Unsolved <span class="stk">Catalogue<a class="sticker" href="#list" title="Pick a cipher below"><span><b>Help<br>Solve!</b><small>pick one below</small></span></a></span></h1>
  <p class="sub">Historical cipher letters that nobody has read. Pick one, open its page, and give that page&rsquo;s address to your AI agent: the page holds the sources, what has been tried and the instructions.</p>
  <ol class="steps"><li><b>1</b>pick a row</li><li><b>2</b>open its page</li><li><b>3</b>point your agent at the URL</li><li><b>4</b>send back what it finds</li></ol>
</section>

<main>
<div id="hashnote" hidden></div>
<div class="callout archnote" data-term-ok><strong>Many of these cannot be read from a desk.</strong> {n_arch} of the open entries are marked <span class="pill arch">needs archive scans</span>: the ciphertext, or the key material that would unlock it, is not online, so nothing can be deciphered until the archive digitises it or someone photographs it in the reading room. They are listed because a request to the archive, or a visit, is the first step.</div>
<div class="cfilters jsonly" id="list" role="search">
  <input type="search" id="q" placeholder="Search: name, place, shelfmark, year…" aria-label="Search the catalogue">
  {dropdown('Language', facet('lang', 'Language', langs, keys), 'lang')}
  {dropdown('Century', facet('century', 'Century', CENTURIES, keys), 'century')}
  {dropdown('Region', facet('region', 'Region', by_count(keys, 'region', last=('Other',)), keys), 'region')}
  {dropdown('Class', facet('cls', 'Class', CLASSES, keys), 'cls')}
  {dropdown('Status', facet('status', 'Status', STATUSES, keys) + facet('access', 'Access', ACCESS, keys) + facet('help', 'Help needed', [('solve', 'Help solve'), ('read', 'Help read'), ('obtain', 'Help obtain')], keys), 'status access help')}
  {dropdown('More', facet('source', 'Found in', SOURCES, keys)
            + facet('seen', 'Checked on', [('image', 'the image'), ('catalogue', 'catalogue description only')], keys)
            + facet('frame', 'Cipher located on a frame', [('confirmed', 'confirmed'), ('missing', 'none at the named frame'), ('viewed', 'viewed earlier'), ('unconfirmed', 'not yet confirmed')], keys)
            + facet('counted', 'Ranking', [('counted', 'counted'), ('noted', 'noted only')], keys)
            + f'''<div class="facet weights"><span class="flabel">Priority</span><span class="opts">
    <label>importance <input type="range" id="w_imp" min="0" max="100" value="{int(W['importance']*100)}"><span class="wv" id="v_imp"></span></label>
    <label>solvability <input type="range" id="w_sol" min="0" max="100" value="{int(W['solvability']*100)}"><span class="wv" id="v_sol"></span></label>
    <label>ease <input type="range" id="w_eas" min="0" max="100" value="{int(W['ease']*100)}"><span class="wv" id="v_eas"></span></label>
    <button type="button" class="chip" id="wreset">default weights</button></span></div>''', 'source seen frame counted')}
  <span class="count" id="count" aria-live="polite"></span>
  <button type="button" class="chip clear" id="reset" hidden>clear filters</button>
</div>

<div class="tw"><table class="cat" id="cat">
<colgroup><col class="c-prio"><col class="c-date"><col class="c-item"><col class="c-shelf"><col class="c-sc"><col class="c-sc"><col class="c-sc"><col class="c-cls"></colgroup>
<thead><tr>
<th class="prio" data-sort="prio" aria-sort="descending">Priority</th><th data-sort="year">Date</th><th data-sort="title">Cipher</th><th>Where</th>
<th class="sc" data-sort="importance">Import.</th><th class="sc" data-sort="solvability">Solvab.</th><th class="sc" data-sort="difficulty">Difficulty</th><th class="cls" data-sort="cls">Class</th>
</tr></thead>
<tbody>
{"".join(row(e) for e in ordered)}
</tbody></table></div>
<div class="legend"><span>click a row for its page</span><span>● viewed on the image</span><span>◇ catalogue description only</span><span>gold dots importance / solvability</span><span>red dots difficulty</span><span>class A sibling deciphered · B partial key in print · C no key</span></div>

{state}

<h2 id="gone">Numbers that have left the catalogue</h2>
<p>{n_gone} catalogue numbers as of {fmt_day(datetime.date.today().isoformat())}, with the write-ups that took them out and the day each landed. <i>(part)</i> marks a split entry: that piece has an outcome, and any piece still open stays in the table above under its number.</p>
<div style="overflow-x:auto"><table class="gone"><thead><tr><th>No.</th><th>Write-up</th><th>Outcome</th><th>Landed</th></tr></thead><tbody>{gone_rows}</tbody></table></div>

<h2>About the catalogue</h2>
<p>What is still in cipher in the digitised diplomatic volumes, and nobody has read. The first entries came from the French volumes on Gallica; the rest ({n_dec}) from the DECODE database, every ciphertext record it marks non-decrypted or partly decrypted, grouped into letters and series and checked against this repository's own targets and Tomokiyo's list. A sweep of 22 Sept 2026 added candidates for new solves and outside reads: DECODE records never classified, letters Tomokiyo calls undeciphered while naming a key, Gallica notices and the printed calendars. On 14 Oct 2026 open items were pulled from Satoru&rsquo;s <a href="https://cryptoole.satoru.net/" rel="noopener">Cryptoole</a> index and checked against the repository. {len(counted)} entries are counted targets, {len(E) - len(counted)} are noted only. Class <b>A</b> means siblings with decipherment in the same volume, <b>B</b> a partial key or known family in print, <b>C</b> no key and no sibling. Entries read, partly read, resolved or found already in print are taken out of the catalogue and written up; those attempted here without a reading stay, tagged <b>attempted, open</b>. An entry a target folder is working on now is tagged <b>in progress</b>, read at each rebuild from the head of the folder&rsquo;s NOTES.md, and its page links those notes.</p>
<p>Scores are judgements from catalogue descriptions and the literature, not from the leaves: {n_img} of {n_all} entries have been viewed on the image, and each page carries the check that would confirm it is open. Data: <a href="https://github.com/dbourdeau/cyphersolver/blob/main/catalogue.json" rel="noopener">catalogue.json</a> · text: <a href="https://github.com/dbourdeau/cyphersolver/blob/main/CATALOGUE.md" rel="noopener">CATALOGUE.md</a> · how to send a result: <a href="contribute.html">contribute</a>.</p>

<h2>How the scores were set</h2>
<p><b>Importance</b> asks what a full reading would add: 5 for a first-hand report of a major event by a principal witness (du Bellay in London 1529, Lanssac at the Polish election), 2 for routine business. <b>Solvability</b> asks whether the material online is enough: 5 when deciphered siblings of the same hand and year sit in the same volume, 1 for one short letter in an unknown language. <b>Difficulty</b> is the technical work at the keyboard: 1 for aligning a known sibling, 5 for a statistics-only attack on a large homophonic nomenclator. The default priority weights importance {W['importance']}, solvability {W['solvability']} and ease {W['ease']} (ease is 6 minus difficulty), rescaled to 0–10; change them under &ldquo;More&rdquo; above the table. Every score is a judgement made before viewing the leaf, so treat the order as a work plan, not a finding.</p>
<p><b>Checked:</b> catalogue descriptions and item numbering; presence or absence of a decipherment item in each volume; shelfmarks from the IIIF manifests. For the DECODE entries: the record metadata and notes, key records from the same archive series, overlap with this repository's targets and with Tomokiyo's list. Entries tagged <i>rule-scored</i> were scored by a script from DECODE's metadata and not yet reviewed by hand. Verify each entry on the image and in the literature before attacking it.</p>
</main>
<!-- site:footer -->
<script id="catdata" type="application/json">{data_js}</script>
<script>{CAT_JS.replace('__GONE__', gone_js)}</script>
</body>
</html>
'''
    (HERE / 'catalogue.html').write_text(page, encoding='utf-8')
    print('wrote catalogue.html', len(page), 'entries', len(E))


# ---------- one page per cipher: docs/solve/<id>.html ----------
def target_folders(e):
    """Repository folders on the entry that exist on disk: those whose NOTES.md claims it (in progress first), then
    any named in the entry's own text."""
    claimed = sorted(CLAIMS.get(e['id'], []), key=lambda c: c[1] != 'in progress')
    found = dict.fromkeys([f for f, _, _ in claimed] + re.findall(r'targets/([\w-]+)', json.dumps(e, ensure_ascii=False)))
    return [f for f in found if (ROOT / 'targets' / f).is_dir()]


def notes_url(f):
    return f'{REPO}/blob/main/targets/{f}/NOTES.md'


def outcome_text(e):
    """What the project has done with e: in progress (and where), else the catalogue's outcome; '' for neither."""
    prog = progress(e)
    if not prog: return e.get('outcome') or ''
    s = 'In progress here, in ' + ' and '.join(f'targets/{f}/' for f, _, _ in prog)
    return s + (f' (earlier: {e["outcome"].rstrip(".")})' if e.get('outcome') else '') + '.'


def issue_url(e, template='solution.yml'):
    from urllib.parse import urlencode
    return f'{REPO}/issues/new?' + urlencode({'template': template, 'title': f'Solution: catalogue {e["id"]}', 'target': f'catalogue {e["id"]}'})


def agent_text(e):
    """The task for an AI agent, as plain text: everything it needs is in this one block."""
    url = SITE + solve_href(e)
    links = link_pairs(e)
    lines = [f'TASK: help read Unsolved Catalogue no. {e["id"]} of the cyphersolver project',
             f'This page: {url}',
             '',
             'You are helping a public research project read historical cipher letters that nobody has read yet.',
             '']
    if progress(e):
        lines += ['START HERE: the project is already working on this cipher. Read these notes before anything else and',
                  'build on them; they record what was transcribed, tried and ruled out, and the next step:']
        lines += [f'  {notes_url(f)}  (status: {st})' for f, _, st in progress(e)]
        lines.append('')
    lines += ['THE CIPHER',
             f'  Title:          {e["title"]}',
             f'  Date:           {e["date"]}',
             f'  Correspondents: {e["correspondents"]}',
             f'  Place:          {e["place"]}',
             f'  Language:       {e["language"]} (expected)',
             f'  Held at:        {e["shelfmark"]}' + (f'; {e["folio_note"]}' if e.get('folio_note') else '')]
    if links:
        lines.append('  Images/records:')
        for t, h in links:
            lines.append(f'    - {t}' + (f': {h}' if h else '') + (f'  (IIIF manifest: https://gallica.bnf.fr/iiif/ark:/12148/{t}/manifest.json)' if is_ark(t) else ''))
    lines += ['', 'WHAT IS KNOWN']
    if e.get('known'):
        lines += [f'  Known so far (checked {fmt_day(e.get("as_of") or AS_OF)}): {e["known"]}', f'  Still open: {e["open"]}']
    lines += [f'  {"History and prior art" if e.get("known") else "Status"}: {e["status"]}',
              f'  Outcome so far: {outcome_text(e) or "not yet attempted by the project"}']
    if e.get('prior_art'): lines.append(f'  Prior-art check: {e["prior_art"]}')
    lines.append(f'  Check first: {e["verify"]}')
    lines.append(f'  Class {e["cls"]}: {CLASS_TEXT.get(e["cls"], "")}.')
    for f in target_folders(e):
        lines.append(f'  Project notes (read these before anything else; they record what was tried and ruled out): {notes_url(f)}')
    if e.get('writeup'): lines.append(f'  Related write-up: {SITE}{e["writeup"]}')
    lang = e['language'] if e['language'] and e['language'] != 'unknown' else 'the expected language'
    folders = target_folders(e)
    folder = f'targets/{folders[0]}/' if folders else 'targets/<writer><year>/ (a new folder, e.g. sega1593)'
    methods = [f'     - {M.LABEL[m]}: {M.DEFINE[m]}' for m in M.METHODS]
    lines += ['',
              'STEPS',
              '0. Set up. If you can run a shell, fork and clone the repository and work inside it:',
              f'     git clone {REPO}.git',
              '   Then read, in this order: CONTRIBUTING.md (how a contribution is sent and credited); README.md, sections',
              '   "Repository layout" and "Conventions" (how readings are measured and named); ' + (f'{folder}NOTES.md (everything' if folders else 'and'),
              ] + (['   already tried on this cipher, with the files it used); and lang/README.md (shared language models).'] if folders else
                   ['   lang/README.md (shared language models).']) + [
              f'   Put all your work in {folder}: transcription, key, decipherment, scripts. '
              + ('Add your findings to its NOTES.md' if folders else 'Write a NOTES.md that says'),
              ('   under a dated heading, without rewriting what is there. Keep WORKLOG.md there too:' if folders else
               '   what the document is, the system, the key, the reading, and what is open and why. Keep WORKLOG.md there too:'),
              '   one dated line per step (transcription, hypothesis, solver run, crib, key found, control), failures included.',
              '   Do not edit docs/ (the site is generated and rebuilt on merge) and do not commit large images: link them.',
              '   If you cannot run a shell, do the same work in files you keep and send them with the issue below.',
              '1. Make sure it is still unread. Search the web and the literature for the shelfmark, the correspondents and the date:',
              '   printed editions and calendars of the correspondence, Satoshi Tomokiyo\'s cryptiana pages',
              '   (https://cryptiana.web.fc2.com/), the DECODE record and the files attached to it, and the project notes above.',
              '   If a decipherment already exists, stop and report where it is. That is a useful result.',
              '2. Get the images. For Gallica items, a page image is',
              '   https://gallica.bnf.fr/iiif/ark:/12148/<ark>/f<page>/full/full/0/native.jpg (page numbers from the manifest).',
              '   DECODE records (de-crypt.org) need a free account: if you cannot log in, ask your human to download the images for you.',
              '3. Look for key material before attacking the ciphertext, in this order: a decipherment written between the lines or',
              '   in the margin; a clear copy or a deciphered sibling letter in the same volume or DECODE series; a key sheet from the',
              '   same office and years (DECODE key records, Tomokiyo\'s articles, printed editions); clear passages in the letter',
              '   itself that can serve as a crib.',
              '4. Transcribe exactly what is on the page: one token per sign or number group, line by line, with folio and line',
              '   numbers, unclear signs marked with ?. Keep the transcription as a file. It is worth sending even if nothing else works.',
              '5. If no key exists, identify the system (count the distinct symbols, tokens and repeats: simple or homophonic',
              '   substitution, nomenclator with code words, syllabary, two-digit figures) and recover the key from the ciphertext',
              f'   with a solver scored on a language model of the period ({lang}). In the clone, use the shared models in lang/',
              "   (from lang import lm; lm.load('<model>'), lm.best_language(text)) rather than building your own; add a corpus there",
              '   if none fits. Before trusting a result, run the same solver on a control text you encipher yourself in the same',
              '   system and at the same length. If it cannot solve the control, its output on the real letter means nothing.',
              '6. Measure the result against the project\'s bar (README.md, Conventions). A text is "complete" only when (1) at least',
              '   95% of its cipher tokens give sense, counted from a reading file, not estimated; (2) no gap is left untried;',
              '   (3) every letter in the item is covered; (4) what stays open is scattered code groups or names, or pieces blocked',
              '   from outside (no key material, too short, illegible, needs the archive). Otherwise it is "partial": say which',
              '   pieces are open and why. Mark every uncertain word with [?] and leave unread groups as their numbers or signs.',
              '   Never fill gaps with plausible guesses. A failed attempt that records what was ruled out is still a contribution.',
              '7. Name how the text was obtained with one of the project\'s methods (do not write just "solved" or "read"):',
              ] + methods + [
              '',
              'REPORT BACK',
              f'With a clone: open a pull request with your {folder.split(" ")[0]} folder. Say in the description how you want to be',
              '  credited (name, initials or handle, and a link) and include the same points as the issue below.',
              f'Without one: open an issue: {issue_url(e)}',
              f'(other kinds of contribution: {REPO}/issues/new/choose). Include:',
              f'  - Target: catalogue {e["id"]}',
              '  - the documents and the images you worked from;',
              '  - the key: sign-to-value table, code groups with values, nulls;',
              '  - the decipherment line by line against the ciphertext, with uncertain passages marked;',
              '  - the method (step 7), the share of tokens that give sense, complete or partial (step 6), and whether the',
              '    reading was already published anywhere;',
              '  - your step log (WORKLOG.md), and the tools and the AI model you used.',
              'If you cannot open issues or pull requests, write this report for your human to send. Credit goes to the person who sends it.']
    return '\n'.join(lines)


# page rules live in style.css under body.pg-solve

SOLVE_JS = '''<script>(function(){var b=document.querySelector('.agentbox .copy'),p=document.getElementById('agent');if(!b||!p)return;
b.addEventListener('click',function(){var t=p.textContent;(navigator.clipboard?navigator.clipboard.writeText(t):Promise.reject()).then(function(){b.textContent='Copied';setTimeout(function(){b.textContent='Copy';},1600);},function(){var r=document.createRange();r.selectNodeContents(p);var s=getSelection();s.removeAllRanges();s.addRange(r);});});})();</script>'''


def help_note(e):
    hk = help_kind(e)
    if hk != 'obtain': return ''
    return ('<div class="callout"><p><strong>First step: obtain the document.</strong> The ciphertext is not online. '
            'Ask the archive to digitise it, or photograph it in the reading room, and send the images in.</p></div>\n')


STK = {'obtain': ' arc', 'read': ' alt', 'solve': ''}


def frame_html(e):
    st, txt, href = frame_info(e)
    lab = {'confirmed': 'Cipher located and confirmed', 'missing': 'No cipher at the named frame', 'viewed': 'Cipher viewed', 'unconfirmed': 'Cipher location not yet confirmed'}[st]
    link = f' <a href="{esc(href)}" rel="noopener">open that page</a>' if href else ''
    return f'<h2>Where the cipher is</h2>\n<p class="frame {st}"><b>{lab}.</b> {esc(txt)}{link}</p>\n'


def solve_page(e, shell):
    url = SITE + solve_href(e)
    links = ' · '.join(f'<a href="{h}" rel="noopener">{esc(t)}</a>' if h else esc(t) for t, h in link_pairs(e)) or '&mdash;'
    folders = ''.join(f'<li><a href="{notes_url(f)}" rel="noopener">targets/{f}/NOTES.md</a>: what was tried and ruled out '
                      f'(<a href="{REPO}/tree/main/targets/{f}" rel="noopener">the folder</a>)</li>' for f in target_folders(e))
    prog = ''.join(f' <a href="{notes_url(f)}" rel="noopener">targets/{f}</a> is working on this cipher (status: {esc(st)}).' for f, _, st in progress(e))
    if prog:
        prog = (f'<div class="callout blue"><p><strong>In progress here.</strong>{prog} Read its NOTES.md before you start, and hand it to '
                f'your agent with this page: it records what was transcribed, tried and ruled out, and the next step.</p></div>\n')
    who = people_html(e)
    title = esc(e['title'])
    body = f'''<section class="hero solve">
  <p class="kicker"><a href="catalogue.html">Unsolved Catalogue</a> · no. {e["id"]} · class {e["cls"]} · priority {priority(e):.1f} · {esc(short_outcome(e))}</p>
  <h1>{title}</h1>
  <p class="sub">{esc(e["why"])}</p>
  <dl class="facts">
    <dt>Date</dt><dd>{esc(e["date"])}</dd>
    <dt>Correspondents</dt><dd>{who}{esc(e["correspondents"])}</dd>
    <dt>Place</dt><dd>{esc(e["place"])}</dd>
    <dt>Language</dt><dd>{esc(e["language"])}</dd>
    <dt>Held at</dt><dd>{esc(e["shelfmark"])}{(" · " + esc(e["folio_note"])) if e.get("folio_note") else ""}</dd>
    <dt>Images</dt><dd>{links}</dd>
  </dl>
</section>

<main>
{prog}<h2>Hand this page to your AI agent</h2>
<p>Give your agent (Claude, ChatGPT or any assistant that can open web pages) this address and ask it to do the task on the page:</p>
<p class="urlline">{url}</p>
<p>Or copy the block below into the chat. It is the whole task: what the cipher is, where the images are, what has been tried, the steps, and how to report back.</p>
<div class="agentbox"><span class="sticker{STK[help_kind(e)]}" aria-hidden="true"><span><b>{HELP[help_kind(e)][0].replace(" ", "<br>")}!</b><small>give this to your agent</small></span></span><button type="button" class="copy">Copy</button><pre id="agent">{html.escape(agent_text(e), quote=False)}</pre></div>

{frame_html(e)}{help_note(e)}<h2>What is known</h2>
{(f'<p class="ko"><i class="k">known</i> <span class="asof">checked {fmt_day(e.get("as_of") or AS_OF)}</span> {esc(e["known"])}</p><p class="ko"><i class="o">open</i> {esc(e["open"])}</p>') if e.get("known") else ''}
{f'<p>{parts_html(e)}</p>' if parts_html(e) else ''}
<p><b>{"History and prior art" if e.get("known") else "Status and prior art"}.</b> {esc(e["status"])}</p>
<p><b>Outcome so far.</b> {esc(outcome_text(e) or "Not yet attempted by the project.")}{(" Prior-art check: " + esc(e["prior_art"]) + ".") if e.get("prior_art") else ""}</p>
<p><b>Check first.</b> {esc(e["verify"])}</p>
{f'<ul>{folders}</ul>' if folders else ''}
{f'<p>Related write-up: <a href="{e["writeup"]}">{esc(e["writeup"])}</a></p>' if e.get("writeup") else ''}

<h2>Scores</h2>
<dl class="facts">
  <dt>Importance</dt><dd>{dots(e["importance"])} {e["importance"]} of 5</dd>
  <dt>Solvability</dt><dd>{dots(e["solvability"])} {e["solvability"]} of 5</dd>
  <dt>Difficulty</dt><dd>{dots(e["difficulty"], "diff")} {e["difficulty"]} of 5</dd>
  <dt>Class {e["cls"]}</dt><dd>{CLASS_TEXT.get(e["cls"], "")}</dd>
  <dt>Note</dt><dd>{esc(e["score_note"])}</dd>
</dl>

<h2>Send a result</h2>
<p>A reading, a partial reading, a transcription, or a source that shows it was read long ago: all of it counts and is credited to you on the site.</p>
<div class="btns"><a class="primary" href="{esc(issue_url(e))}" rel="noopener">Open a solution issue</a><a href="{REPO}/issues/new/choose" rel="noopener">Other kinds of report</a><a href="contribute.html">How credit works</a><a href="catalogue.html">&larr; All unsolved ciphers</a></div>
</main>
'''
    return (f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<base href="../">
<title>No. {e["id"]}: {title} — help solve it</title>
<meta name="description" content="{esc(e["why"]).replace('"', '&quot;')} An unread cipher of {esc(e["date"])}, with instructions for an AI agent.">
{shell["head"]}
</head>
<body id="top" class="pg-solve">
{shell["nav"]}

{body}
{shell["footer"].replace('href="#top"', f'href="{solve_href(e)}#top"')}
{SOLVE_JS}
{shell["scripts"]}
</body>
</html>
''')


def build_solve_pages():
    """Run after _build_site.py: the nav, footer and scripts are taken from the built catalogue.html."""
    s = (HERE / 'catalogue.html').read_text(encoding='utf-8')
    shell = dict(
        head='\n'.join(re.findall(r'<link rel="(?:stylesheet|icon|apple-touch-icon)"[^>]*>', s)),
        nav=re.search(r'<header class="nav">.*?</header>\n<div class="search" id="search".*?</div>\n</div>', s, re.S).group(0),
        footer=re.search(r'<footer>.*?</footer>', s, re.S).group(0),
        scripts='\n'.join(re.findall(r'<script src="[^"]+"></script>', s)))
    out = HERE / 'solve'
    out.mkdir(exist_ok=True)
    keep = set()
    for e in DATA['entries']:
        p = out / f'{e["id"]}.html'; keep.add(p.name)
        p.write_text(solve_page(e, shell), encoding='utf-8')
    for p in out.glob('*.html'):          # entries read and removed from the catalogue lose their page
        if p.name not in keep: p.unlink()
    print('wrote', len(keep), 'pages in docs/solve/')


if __name__ == '__main__':
    update_md()
    build_html()
    import subprocess, sys
    subprocess.run([sys.executable, '_build_site.py'], check=True, cwd=pathlib.Path(__file__).parent)
