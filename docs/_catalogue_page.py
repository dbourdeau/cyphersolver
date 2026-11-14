"""Build docs/catalogue.html and the tables in ../CATALOGUE.md from ../catalogue.json.

Run from docs/:  python _catalogue_page.py   (it runs _build_site.py afterwards for the nav, footer and contents
strip; a catalogue.html left with the bare <!-- site:nav --> marker has no navigation bar).

catalogue.json is the single source: entries with 1-5 scores for importance, solvability and difficulty.
The page embeds the entries as compact JSON and the script draws the list from it, 30 rows at a time, in four views
(try from a desk, needs an archive, all open, left the catalogue), with the priority computed from adjustable weights;
the first page of the default view is also written out as a static table for readers without JavaScript. The
holding archives come from ../repositories.json (_repositories.py) and make the "Where the ciphers are" index. CATALOGUE.md gets its table (counted entries, default weights) and
its "Also noted" list rewritten between <!-- table:start --> / <!-- table:end --> and <!-- also:start --> /
<!-- also:end --> markers; the prose around them is hand-written and left alone.
"""
import json, html, pathlib, re, datetime, collections
import _methods as M
import _claims
import _repositories as RP

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
        ms = list(CAT_RE.finditer(cells[0]))      # every "catalogue N" of the row: a folded row names two (159 and 160)
        if not ms: continue
        ids = list(dict.fromkeys(int(x) for m in ms for x in re.findall(r'\d+', m.group(1))))
        name = re.sub(r'\*\*|\[|\]\([^)]*\)', '', cells[0])
        name = re.sub(r'\s*\((?:[^()]|\([^()]*\))*(?:catalogue|DECODE)(?:[^()]|\([^()]*\))*\)\s*$', '', name).strip()
        slug = re.search(r'dbourdeau\.github\.io/cyphersolver/([\w-]+)\.html', line)
        part = bool(re.search(r'catalogue(?: item)? \d+[^)]*?\bpart\b|split \d|from catalogue', cells[0]))
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
SITE = 'https://cyphersolver.com/'
REPO = 'https://github.com/dbourdeau/cyphersolver'
CLASS_TEXT = {
    'A': 'a sibling letter with a decipherment is in the same volume or series, so matching it is the first move',
    'B': 'part of a key or a known cipher family of the same office is in print or on DECODE',
    'C': 'no key and no deciphered sibling is known, so expect a ciphertext-only attack',
}


def reserved(e):
    """The entry's live reservation (research/SWEEP.md, "Reserving a lead"): its finder tries it first until the date."""
    r = e.get('reserved')
    return r if isinstance(r, dict) and r.get('by') and str(r.get('until', '')) >= datetime.date.today().isoformat() else None


def short_outcome(e):
    return 'in progress' if progress(e) else (e.get('outcome') or 'open').split(':')[0]


def solve_href(e):
    return f'solve/{e["id"]}.html'


_ARCH = None


def entry_href(e):
    """Where a catalogue row leads: a 'Help obtain' entry needs an archive, not an agent prompt, so it goes to its
    request on the To the Archive page (archives.html#c<id>) when the ledger has one; every other entry to its own page."""
    global _ARCH
    if _ARCH is None:
        f = pathlib.Path(__file__).resolve().parent.parent / 'archive_requests.json'
        rq = json.loads(f.read_text(encoding='utf-8')).get('requests', []) if f.is_file() else []
        _ARCH = {str(r['catalogue']) for r in rq if r.get('catalogue') and not r.get('target') and r.get('status') in ('open', 'claimed', 'requested')}
    if help_kind(e) == 'obtain' and str(e['id']) in _ARCH: return f'archives.html#c{e["id"]}'
    return solve_href(e)


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


def flags(e):
    """The small markers a row carries after its outcome pill, as letters the page script reads (see row())."""
    v = e.get('vetting') or {}
    return ''.join(c for c, on in (('w', e.get('workable')), ('a', e.get('access') == 'archive'), ('v', v.get('key_in_volume')),
                                   ('h', v.get('key_held')), ('u', frame_info(e)[0] == 'unconfirmed')) if on)


FLAG_PILLS = {'w': ('work', 'the key material exists (siblings, glosses); what is left is work, not an outside blocker', 'no outside blocker'),
              'a': ('arch', 'the ciphertext or the key material is not online; it needs the archive to digitise it or someone to photograph it', 'needs archive scans'),
              'v': ('work', 'a key is filed in the same volume or unit and no decipherment exists; a reading would be read with known key', 'key in volume'),
              'h': ('work', 'a key is held here, on DECODE or in print, and no decipherment is known', 'key held'),
              'u': ('unf', 'no one has confirmed the cipher on a specific frame yet', 'frame unchecked')}


def row(e):
    """One table row. The page script draws the same markup from the embedded data (CAT_JS row()); this one is the
    first page of the default view, for readers without JavaScript."""
    href = entry_href(e)
    seen = '<span class="seen img" title="viewed on the image">●</span>' if seen_image(e) else '<span class="seen cat" title="catalogue description only">◇</span>'
    tip = f' title="being worked in targets/{", targets/".join(f for f, _, _ in progress(e))}/"' if progress(e) else ''
    hk = help_kind(e)
    pill = (f'<span class="pill help-{hk}" title="{esc(HELP[hk][1])}">{HELP[hk][0]}</span>'
            f'<span class="pill{" att" if e.get("outcome") or tip else ""}"{tip}>{esc(short_outcome(e))}</span>')
    pill += ''.join(f'<span class="pill {FLAG_PILLS[c][0]}" title="{FLAG_PILLS[c][1]}">{FLAG_PILLS[c][2]}</span>' for c in flags(e))
    link = ''.join(f'<a href="{h}" rel="noopener">{esc(t)}</a>' if h else esc(t) for t, h in link_pairs(e)[:1])
    r = RP.info(RP.of(e))
    return (f'<tr class="e" data-id="{e["id"]}" data-href="{href}">'
            f'<td class="prio"><b>{priority(e):.1f}</b></td>'
            f'<td class="date">{esc(e["date"])}<span class="num">no. {e["id"]}</span></td>'
            f'<td class="item"><a class="t" href="{href}">{seen} {esc(e["title"])}</a>{pill}<span class="sub">{esc(e["why"])}</span></td>'
            f'<td class="shelf"><span class="ar" title="{html.escape(arch_place(r))}">{esc(r.get("short") or r["name"])}</span>'
            f'<span class="sm" title="{html.escape(e["shelfmark"])}">{esc(e["shelfmark"])}</span>{link}</td>'
            f'<td class="sc">{dots(e["importance"])}</td><td class="sc">{dots(e["solvability"])}</td><td class="sc">{dots(e["difficulty"], "diff")}</td>'
            f'<td class="cls"><span class="badge {e["cls"]}">{e["cls"]}</span></td></tr>')


def arch_place(r):
    """'Haus-, Hof- und Staatsarchiv, Vienna, Austria': the full name and where it is, for a tooltip."""
    return ', '.join(x for x in (r['name'], r.get('city'), r.get('country')) if x and x not in r['name'])


# ---------- filter keys ----------
# The catalogue fields are free text written by many sweeps ('Polish/French (unknown which; ...)', 'Archivportal-D
# sweep', 'images'), so the table filters on a few clean keys derived here, in entry['f'], not on the raw values.
# Language keys are the lowercase names the writeups.html Language facet uses, so a #lang=french link works on both.
# cls, help, arch and country are added by the page script from the entry's own fields, to keep the page small.
CAT_LANGS = ['French', 'German', 'English', 'Portuguese', 'Italian', 'Spanish', 'Latin', 'Dutch', 'Polish', 'Swedish',
             'Danish', 'Hungarian']
LANG_ALIAS = {'castilian': 'Spanish', 'scots': 'English'}
OTHER_LANGS = {'Russian', 'Czech', 'Catalan', 'Turkish', 'Greek', 'Arabic', 'Hebrew', 'Croatian', 'Romanian', 'Lithuanian'}
CENTURIES = [('1400s', '1400s'), ('1500s', '1500s'), ('1600s', '1600s'), ('1700s', '1700s'), ('1800s', '1800s'),
             ('1900s', '1900s'), ('undated', 'undated')]
# how an entry was found, as against where it is held (repository): the 140-odd sweep labels in "source", in six families
FOUND = [('sweep', 'archive and library catalogues', 'searches of national and regional archive portals, finding aids and library catalogues for letters described as in cipher'),
         ('print', 'printed sources', 'calendars of state papers, editions and the literature, mostly searched in full text on the Internet Archive and HathiTrust'),
         ('decode', 'DECODE', 'the database of historical cipher documents: the records it marks not decrypted or partly decrypted'),
         ('bnf', 'BnF / Gallica', 'the French diplomatic volumes digitised on Gallica, where the catalogue began'),
         ('cryptoole', 'Cryptoole', 'open items in Satoru&rsquo;s <a href="https://cryptoole.satoru.net/" rel="noopener">Cryptoole</a> index'),
         ('contributed', 'sent in', 'readers&rsquo; issues on GitHub and HCPortal')]
SOURCES = [(k, l) for k, l, _ in FOUND]
STATUSES = [('new', 'not attempted'), ('progress', 'in progress here'), ('attempted', 'attempted here'), ('skipped', 'skipped')]
ACCESS = [('online', 'no archive trip needed'), ('workable', 'no outside blocker'), ('archive', 'needs archive scans'), ('unchecked', 'access not checked')]
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
    if 'decode' in s and 'sweep' not in s: return 'decode'
    if 'cryptoole' in s: return 'cryptoole'
    if re.search(r'\bbnf\b|gallica', s) and 'archives et manuscrits' not in s: return 'bnf'
    if 'github' in s or 'hcportal' in s: return 'contributed'
    if re.search(r'print|calendar|literature|cryptiana|internet archive|hathitrust|wikisource|masked dispatches|repertory|frus', s): return 'print'
    return 'sweep'


def seen_image(e):
    return e['seen'] != 'catalogue'


def access_unchecked(e):
    """No access value and only the catalogue description seen: nobody has looked for the images yet."""
    return e.get('access') is None and not seen_image(e)


def has_known(e):
    """An open entry with pieces already read or identified: its known line, or a write-up citing its number."""
    return bool((e.get('known') and not e['known'].startswith('Nothing')) or e['id'] in SOLVED)


def filter_keys(e):
    o = e.get('outcome') or ''
    k = {'lang': lang_keys(e), 'century': century_key(e), 'region': e['region'],
         'status': 'progress' if progress(e) else 'skipped' if 'skipped' in o else 'attempted' if o.startswith('attempted') else 'new',
         'access': [k for k, on in (('online', e.get('access') != 'archive' and not access_unchecked(e)), ('unchecked', access_unchecked(e)),
                                    ('workable', e.get('workable')), ('archive', e.get('access') == 'archive')) if on],
         'frame': frame_info(e)[0], 'source': source_key(e), 'seen': 'image' if seen_image(e) else 'catalogue',
         'counted': 'counted' if e['counted'] else 'noted'}
    if has_known(e): k['pieces'] = 'known'
    return k


def all_keys(e, k):
    """filter_keys plus the keys the page script derives (for the facets' value lists, built here)."""
    r = RP.info(RP.of(e))
    return dict(k, cls=e['cls'], help=help_kind(e), arch=r['id'], country=r.get('country') or 'none')


def facet(name, label, values, keys):
    """values: (key, label) pairs; a value no entry has is left out. Each chip carries a live count."""
    have = {k for f in keys for k in ([f[name]] if isinstance(f.get(name), str) else f.get(name) or [])}
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


# ---------- the views ----------
# One list, four views: what a desk can work, what needs an archive first (grouped by archive), everything open, and the
# numbers that have left. 'try' and 'archive' are cut on the access keys; CAT_JS inView() is the same test.
VIEWS = [('try', 'Try from a desk', 'The cipher, and any key material, is online: open a row and hand its page to your agent.'),
         ('archive', 'Needs an archive', 'The ciphertext, or the key that would unlock it, is not online: the first step is a scan from the archive or a reading-room photograph. Grouped by the archive that holds it; requests and volunteers are on the <a href="archives.html">To the archive</a> page.'),
         ('all', 'All open', 'Every open entry, whatever its access.'),
         ('gone', 'Left the catalogue', 'Numbers deciphered, explained or found in print, grouped by how the reading was reached; each links to the write-up that took it out.')]


def in_view(k, v):
    if v == 'try': return 'online' in k['access'] or 'workable' in k['access']
    if v == 'archive': return 'archive' in k['access']
    return True


def short_name(n):
    """'Mondoucet → Charles IX, Brussels 13 July 1572 (BnF ...)' -> 'Mondoucet → Charles IX'."""
    s = re.split(r',|;| \(| — ', n, maxsplit=1)[0].strip()
    return s if len(s) <= 56 else s[:56].rsplit(' ', 1)[0] + '…'


def summary_html(E, keys, n_gone, prs):
    """The strip under the title: what is open, what a desk can do, what needs an archive, what has left."""
    day = fmt_day(datetime.date.today().isoformat())
    n_try = sum(in_view(k, 'try') for k in keys)
    n_arch = sum(in_view(k, 'archive') for k in keys)
    n_unc = len(E) - n_try - n_arch
    n_prog = sum(1 for e in E if progress(e))
    tiles = [('all', '', len(E), 'open ciphers', f'{sum(e["counted"] for e in E)} counted targets, the rest noted'),
             ('try', '', n_try, 'to try from a desk', 'online, or the key material at hand'),
             ('archive', '', n_arch, 'need an archive first', 'not online: a scan or a photograph comes first'),
             ('all', 'progress', n_prog, 'in progress here', 'a target folder is working on them'),
             ('gone', '', n_gone, 'have left the catalogue', 'deciphered, explained or found in print')]
    t = ''.join(f'<a class="tile t-{v}{" t-prog" if st else ""}" href="#v={v}{"&status=" + st if st else ""}" data-go="{v}"{f' data-status="{st}"' if st else ""}>'
                f'<b>{n}</b><span>{lab}</span><small>{sub}</small></a>' for v, st, n, lab, sub in tiles)
    bar = (f'<div class="sbar" role="img" aria-label="{n_try} to try from a desk, {n_arch} need an archive, {n_unc} with access not yet checked">'
           f'<i class="b-try" style="flex:{n_try}"></i><i class="b-arch" style="flex:{n_arch}"></i><i class="b-unc" style="flex:{n_unc}"></i></div>'
           f'<p class="skey"><span class="k-try">{n_try} from a desk</span><span class="k-arch">{n_arch} need an archive</span>'
           f'<span class="k-unc">{n_unc} access not yet checked</span></p>')
    pr_li = ''.join(f'<li><a href="{esc(r["url"])}" rel="noopener">#{r["number"]}</a> {esc(r["title"])} '
                    f'<span class="d">{esc((r.get("author") or {}).get("login", ""))}, updated {fmt_day(r["updatedAt"][:10])}</span></li>' for r in prs)
    prl = (f'<details class="prs"><summary>{len(prs)} open pull request{"s" if len(prs) != 1 else ""}</summary><ul class="sl">{pr_li}</ul></details>'
           if prs else '<span>no open pull requests</span>')
    return (f'<div class="stand" id="status">\n<div class="tiles">{t}</div>\n{bar}\n'
            f'<div class="asof">Counts as of {day}; each entry&rsquo;s known and open lines were last checked by hand on {fmt_day(AS_OF)} or later. '
            f'Before starting, read the entry&rsquo;s page and the work still in review: {prl}</div>\n</div>')


def gone_html(gone):
    """The numbers that have left, as compact links grouped by outcome method (the README section that holds them)."""
    by = {}
    for i in gone: by.setdefault(SOLVED[i][0][1], []).append(i)
    def chip(i):
        rows = SOLVED[i]
        n, _, landed, sl, _ = rows[0]
        tip = ' · '.join(x[0] + (' (part)' if x[4] else '') for x in rows) + f' (landed {landed})'
        more = f' <i>+{len(rows) - 1}</i>' if len(rows) > 1 else ''
        q = f'{i} ' + ' '.join(x[0] for x in rows)
        return (f'<li id="e{i}g" data-q="{html.escape(q.lower())}"><a href="{sl + ".html" if sl else f"solve/{i}.html"}" title="{html.escape(tip)}">'
                f'<b>{i}</b> {esc(short_name(n))}</a>{more}</li>')
    return ''.join(f'<section class="gm"><h3>{esc(m)} <span class="n">{len(by[m])}</span></h3><ul class="gl">{"".join(chip(i) for i in by[m])}</ul></section>'
                   for m in sorted(by, key=lambda m: -len(by[m])))


def sources_html(E):
    """Where the open entries are held, by country, and how they were found."""
    n = collections.Counter(RP.of(e) for e in E)
    by = {}
    for rid, k in n.items(): by.setdefault(RP.info(rid).get('country') or '', []).append((rid, k))
    def a(rid, k):
        r = RP.info(rid)
        return (f'<a href="#v=all&amp;arch={rid}" data-arch="{rid}" title="{html.escape(arch_place(r))}">{esc(r.get("short") or r["name"])}</a>'
                f'&nbsp;<b>{k}</b>')
    def line(rows):
        return ' · '.join(a(rid, k) for rid, k in sorted(rows, key=lambda x: (-x[1], RP.info(x[0])['name'])))
    cs = sorted((c for c in by if c), key=lambda c: (-sum(k for _, k in by[c]), c))
    rows = ''.join(f'<div class="cty"><h3>{esc(c)} <span class="n">{sum(k for _, k in by[c])}</span></h3><p>{line(by[c])}</p></div>' for c in cs)
    if by.get(''):
        rows += f'<div class="cty other"><h3>No single archive <span class="n">{sum(k for _, k in by[""])}</span></h3><p>{line(by[""])}</p></div>'
    n_rep = len([r for r in n if RP.info(r)['kind'] not in ('print', 'unknown')])
    fam = collections.Counter(source_key(e) for e in E)
    found = ''.join(f'<li><a href="#v=all&amp;source={k}" data-src="{k}"><b>{fam[k]}</b> {l}</a><span>{d}</span></li>' for k, l, d in FOUND if fam[k])
    labels = collections.Counter(e.get('source') or 'unknown' for e in E)
    every = ' · '.join(f'{esc(s)}&nbsp;<b>{k}</b>' for s, k in sorted(labels.items(), key=lambda x: (-x[1], x[0])))
    return f'''<h2 id="where">Where the ciphers are</h2>
<p class="lede">The {len(E)} open entries are held by <b>{n_rep}</b> archives, libraries and collections in <b>{len(cs)}</b> countries; {sum(k for r, k in n.items() if RP.info(r)['kind'] == 'print')} are known only from a printed edition and {sum(k for r, k in n.items() if RP.info(r)['kind'] == 'unknown')} sit in an archive not yet identified. Click an archive to list its ciphers. Data: <a href="https://github.com/dbourdeau/cyphersolver/blob/main/repositories.json" rel="noopener">repositories.json</a>.</p>
<div class="archidx">{rows}</div>
<h3 class="fh">How they were found</h3>
<ul class="found">{found}</ul>
<details class="every"><summary>All {len(labels)} searches, with the entries each found</summary><p>{every}</p></details>
'''


# page rules live in pg-catalogue.css under body.pg-catalogue (the site build strips inline <style> from catalogue.html).
# The page script: views, search, facets, reweighting, sort, paging; a row click opens the cipher's page. __GONE__ is
# replaced by the numbers that have left the catalogue, so an old catalogue.html#eNN link still lands somewhere useful.
CAT_JS = r'''
(function(){
document.body.classList.remove('nojs');
var D=JSON.parse(document.getElementById('catdata').textContent),E=D.entries,A=D.arch,G=__GONE__,byId={};
E.forEach(function(e){byId[e.id]=e;var a=A[e.r]||['','','',''];e.f.cls=e.c;e.f.help=e.k;e.f.arch=e.r;e.f.country=a[2]||'none';});
var hm=/^#e(\d+)$/.exec(location.hash);
if(hm&&byId[hm[1]]){location.replace(byId[hm[1]].h||'solve/'+hm[1]+'.html');return;}
function esc(s){return String(s==null?'':s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');}
if(hm&&!G[hm[1]]){var h0=document.getElementById('hashnote');h0.textContent='Catalogue no. '+hm[1]+' is no longer in the catalogue: it was merged into another entry or withdrawn.';h0.hidden=false;}
if(hm&&G[hm[1]]){var hn=document.getElementById('hashnote');hn.innerHTML='Catalogue no. '+hm[1]+' is no longer open: '+G[hm[1]].map(function(x){return x[1]?'<a href="'+x[1]+'.html">'+esc(x[0])+'</a>':esc(x[0]);}).join(' · ');hn.hidden=false;}
var PAGE=30,GROUPS=8,ROWS_PER_GROUP=3;
var tb=document.querySelector('#cat tbody'),tw=document.getElementById('tw'),gp=document.getElementById('gonep'),more=document.getElementById('more'),bar=document.getElementById('cbar'),top=document.getElementById('list'),cf=document.querySelector('.cfilters'),lg=document.querySelector('.legend'),vd=document.getElementById('vdesc');
var tabs=[].slice.call(document.querySelectorAll('.views [data-v]')),gli=[].slice.call(gp.querySelectorAll('li[data-q]')),gsec=[].slice.call(gp.querySelectorAll('section.gm'));
var state={v:'try',q:'',sort:'prio',dir:-1,w:{imp:D.weights.importance,sol:D.weights.solvability,eas:D.weights.ease},f:{},n:PAGE,g:GROUPS};
var chips=[].slice.call(document.querySelectorAll('.chip[data-facet]')),clr=document.getElementById('reset'),qi=document.getElementById('q'),dds=[].slice.call(document.querySelectorAll('.cfilters details.dd'));
dds.forEach(function(d){d.addEventListener('toggle',function(){if(!d.open)return;dds.forEach(function(o){if(o!==d)o.open=false;});
 var p=d.querySelector('.pop');p.style.left='';p.style.right='';if(p.getBoundingClientRect().right>document.documentElement.clientWidth-8){p.style.left='auto';p.style.right='0';}});});
document.addEventListener('click',function(ev){if(!ev.target.closest('.cfilters details.dd,.fsheet'))dds.forEach(function(d){d.open=false;});});
document.addEventListener('keydown',function(ev){if(ev.key==='Escape')dds.forEach(function(d){if(d.open){d.open=false;d.querySelector('summary').focus();}});});
function prio(e){var w=state.w,t=w.imp+w.sol+w.eas||1;var v=(w.imp*e.i+w.sol*e.so+w.eas*(6-e.df))/t;return Math.round((v-1)/4*100)/10;}
// the views: 'try' is what a desk can work (access online, or the key material at hand); the Python in_view() is the same test
function inView(e,v){var a=e.f.access;if(v==='try')return a.indexOf('online')>=0||a.indexOf('workable')>=0;if(v==='archive')return a.indexOf('archive')>=0;return true;}
function vals(e,k){var v=e.f[k];return v==null?[]:[].concat(v);}
function hit(e,k){var s=state.f[k];if(!s||!s.length)return true;var v=vals(e,k);return s.some(function(x){return v.indexOf(x)>=0;});}
function texthit(e){if(!state.q)return true;var a=A[e.r]||[];var h=e._h||(e._h=(e.id+' '+e.t+' '+e.w+' '+e.s+' '+e.d+' '+e.y+' '+a[3]+' '+a[1]+' '+(e.q||'')).toLowerCase());return h.indexOf(state.q)>=0;}
function match(e,skip){if(!texthit(e))return false;for(var k in state.f)if(k!==skip&&!hit(e,k))return false;return true;}
// each chip's count: entries it would show in this view, given every other facet and the search
function counts(){var c={},ks={};chips.forEach(function(b){c[b.dataset.facet+'|'+b.dataset.val]=0;ks[b.dataset.facet]=1;});
 Object.keys(ks).forEach(function(k){E.forEach(function(e){if(inView(e,state.v)&&match(e,k))vals(e,k).forEach(function(v){var x=k+'|'+v;if(x in c)c[x]++;});});});
 chips.forEach(function(b){var on=(state.f[b.dataset.facet]||[]).indexOf(b.dataset.val)>=0,n=c[b.dataset.facet+'|'+b.dataset.val];b.setAttribute('aria-pressed',on?'true':'false');b.querySelector('.n').textContent=n;b.classList.toggle('z',!n&&!on);});}
function labels(){dds.forEach(function(d){var ks=(d.dataset.dd||'').split(' '),on=[];ks.forEach(function(k){(state.f[k]||[]).forEach(function(v){var b=d.querySelector('.chip[data-facet="'+k+'"][data-val="'+v+'"]');if(b)on.push(b.firstChild.textContent);});});
 d.querySelector('.dv').textContent=on.length?(on.length>2?on.length+' chosen':on.join(', ')):'';d.classList.toggle('act',on.length>0);});}
function save(){var p=[];for(var k in state.f)if(state.f[k].length)p.push(k+'='+state.f[k].map(encodeURIComponent).join(','));if(state.q)p.push('q='+encodeURIComponent(state.q));if(p.length||state.v!=='try')p.unshift('v='+state.v);
 try{history.replaceState(null,'',p.length?'#'+p.join('&'):location.pathname);}catch(x){}}
// a link with filters and no view (writeups.html sends #lang=french) opens on all open entries, as before the views
function load(){var h=location.hash.slice(1),sv=0;if(h==='gone'){state.v='gone';return;}if(h.indexOf('=')<0)return;h.split('&').forEach(function(kv){var i=kv.indexOf('=');if(i<1)return;var k=kv.slice(0,i),v=decodeURIComponent(kv.slice(i+1));
 if(k==='q'){state.q=v.toLowerCase();qi.value=v;}else if(k==='v'){if(D.views[v]){state.v=v;sv=1;}}else state.f[k]=v.split(',').filter(Boolean);});if(!sv)state.v='all';}
var SK={year:'y',title:'t',importance:'i',solvability:'so',difficulty:'df',cls:'c'};
function key(e){var s=state.sort;if(s==='prio')return prio(e);if(s==='cls'||s==='title')return e[SK[s]];return +e[SK[s]];}
function sorter(a,b){var x=key(a),y=key(b);if(x<y)return -1*state.dir;if(x>y)return 1*state.dir;return a.id-b.id;}
function nf0(){var n=0;for(var k in state.f)n+=state.f[k].length;return n;}
var HELP=D.help,FP=D.flags;
function dots(v,c){var s='<span class="dots'+(c?' '+c:'')+'" title="'+v+' of 5">';for(var i=0;i<5;i++)s+='<i class="'+(i<v?'on':'')+'"></i>';return s+'</span>';}
// the same markup as row() in _catalogue_page.py
function row(e){var href=e.h||('solve/'+e.id+'.html'),a=A[e.r]||['','','',''];
 var p='<span class="pill help-'+e.k+'" title="'+esc(HELP[e.k][1])+'">'+HELP[e.k][0]+'</span><span class="pill'+(e.at?' att':'')+'"'+(e.pg?' title="being worked in targets/'+esc(e.pg)+'/"':'')+'>'+esc(e.o)+'</span>';
 (e.x||'').split('').forEach(function(c){var f=FP[c];p+='<span class="pill '+f[0]+'" title="'+esc(f[1])+'">'+f[2]+'</span>';});
 var ln=e.l?(e.l[1]?'<a href="'+esc(e.l[1])+'" rel="noopener">'+esc(e.l[0])+'</a>':esc(e.l[0])):'';
 var seen=e.im?'<span class="seen img" title="viewed on the image">●</span>':'<span class="seen cat" title="catalogue description only">◇</span>';
 return '<tr class="e" data-id="'+e.id+'" data-href="'+href+'"><td class="prio"><b>'+prio(e).toFixed(1)+'</b></td><td class="date">'+esc(e.d)+'<span class="num">no. '+e.id+'</span></td>'
 +'<td class="item"><a class="t" href="'+href+'">'+seen+' '+esc(e.t)+'</a>'+p+'<span class="sub">'+esc(e.w)+'</span></td>'
 +'<td class="shelf"><span class="ar" title="'+esc(a[4])+'">'+esc(a[0])+'</span><span class="sm" title="'+esc(e.s)+'">'+esc(e.s)+'</span>'+ln+'</td>'
 +'<td class="sc">'+dots(e.i)+'</td><td class="sc">'+dots(e.so)+'</td><td class="sc">'+dots(e.df,'diff')+'</td><td class="cls"><span class="badge '+e.c+'">'+e.c+'</span></td></tr>';}
function btn(act,label){return '<button type="button" class="chip" data-act="'+act+'">'+label+'</button>';}
function render(keep){
 var v=state.v,nf=nf0();
 tabs.forEach(function(t){var tv=t.dataset.v,n=tv==='gone'?gli.filter(function(li){return !state.q||li.dataset.q.indexOf(state.q)>=0;}).length:E.filter(function(e){return inView(e,tv)&&match(e);}).length;
  t.setAttribute('aria-selected',tv===v?'true':'false');t.querySelector('.n').textContent=n;});
 vd.innerHTML=D.views[v];bar.classList.toggle('vgone',v==='gone');
 lg.hidden=v==='gone';
 if(v==='gone'){tw.hidden=true;gp.hidden=false;more.innerHTML='';var n=0;
  gli.forEach(function(li){var ok=!state.q||li.dataset.q.indexOf(state.q)>=0;li.hidden=!ok;if(ok)n++;});gsec.forEach(function(s){s.hidden=!s.querySelector('li:not([hidden])');});
  document.getElementById('count').textContent=(state.q?n+' of '+gli.length:gli.length)+' numbers';clr.hidden=!state.q;clr.textContent='clear search';if(!keep)save();return;}
 tw.hidden=false;gp.hidden=true;
 var L=E.filter(function(e){return inView(e,v)&&match(e);}).sort(sorter),base=E.filter(function(e){return inView(e,v);}).length,h='',m='';
 var ga=state.f.arch&&state.f.arch.length===1;
 if(v==='archive'&&!ga){var g={},order=[];L.forEach(function(e){if(!g[e.r]){g[e.r]=[];order.push(e.r);}g[e.r].push(e);});
  order.sort(function(a,b){return g[b].length-g[a].length||(A[a][0]<A[b][0]?-1:1);});
  order.slice(0,state.g).forEach(function(r){var rs=g[r],a=A[r];
   h+='<tr class="grp"><td colspan="8"><b>'+esc(a[3])+'</b>'+(a[1]?' <span>'+esc(a[1]+(a[2]&&a[1].indexOf(a[2])<0?', '+a[2]:''))+'</span>':'')+' <span class="gn">'+rs.length+'</span></td></tr>';
   rs.slice(0,ROWS_PER_GROUP).forEach(function(e){h+=row(e);});
   if(rs.length>ROWS_PER_GROUP)h+='<tr class="gmore"><td colspan="8"><button type="button" class="chip" data-arch="'+r+'">all '+rs.length+' at '+esc(a[0])+' &rarr;</button></td></tr>';});
  if(order.length>state.g)m=btn('g','Show '+Math.min(GROUPS,order.length-state.g)+' more archives')+'<span class="d">'+(order.length-state.g)+' archives not shown</span>';}
 else{L.slice(0,state.n).forEach(function(e){h+=row(e);});
  if(L.length>state.n)m=btn('n','Show '+Math.min(PAGE,L.length-state.n)+' more')+btn('all','Show all '+L.length)+'<span class="d">'+state.n+' of '+L.length+' shown</span>';}
 tb.innerHTML=h||'<tr><td colspan="8" class="none">Nothing matches. <button type="button" class="chip" data-act="clear">clear the filters</button></td></tr>';more.innerHTML=m;
 var msrt=document.getElementById('msort');if(msrt)msrt.value=state.sort;
 document.getElementById('count').textContent=(L.length===base?base:L.length+' of '+base)+' ciphers';
 clr.hidden=!(nf||state.q);clr.textContent=nf?'clear '+nf+' filter'+(nf>1?'s':''):'clear search';
 counts();labels();if(!keep)save();
 document.getElementById('v_imp').textContent=state.w.imp.toFixed(2);document.getElementById('v_sol').textContent=state.w.sol.toFixed(2);document.getElementById('v_eas').textContent=state.w.eas.toFixed(2);
 [].forEach.call(document.querySelectorAll('#cat th[data-sort]'),function(th){th.setAttribute('aria-sort',th.dataset.sort===state.sort?(state.dir<0?'descending':'ascending'):'none');});}
function reset(){state.n=PAGE;state.g=GROUPS;}
function go(v,f,scroll){state.v=v;if(f){state.f=f;state.q='';qi.value='';}reset();render();if(scroll)top.scrollIntoView({block:'start'});}
tabs.forEach(function(t){t.addEventListener('click',function(ev){ev.preventDefault();go(t.dataset.v);});});
[].forEach.call(document.querySelectorAll('a[data-go]'),function(a){a.addEventListener('click',function(ev){ev.preventDefault();go(a.dataset.go,a.dataset.status?{status:[a.dataset.status]}:{},true);});});
[].forEach.call(document.querySelectorAll('.archidx a[data-arch]'),function(a){a.addEventListener('click',function(ev){ev.preventDefault();go('all',{arch:[a.dataset.arch]},true);});});
[].forEach.call(document.querySelectorAll('.found a[data-src]'),function(a){a.addEventListener('click',function(ev){ev.preventDefault();go('all',{source:[a.dataset.src]},true);});});
tb.addEventListener('click',function(ev){var b=ev.target.closest('button');
 if(b){if(b.dataset.arch){state.f.arch=[b.dataset.arch];reset();render();top.scrollIntoView({block:'start'});}else if(b.dataset.act==='clear'){state.q='';state.f={};qi.value='';reset();render();}return;}
 if(ev.target.closest('a'))return;var r=ev.target.closest('tr.e');if(!r)return;if(ev.ctrlKey||ev.metaKey)window.open(r.dataset.href);else location.href=r.dataset.href;});
more.addEventListener('click',function(ev){var b=ev.target.closest('button');if(!b)return;var a=b.dataset.act;if(a==='n')state.n+=PAGE;else if(a==='all')state.n=1e9;else if(a==='g')state.g+=GROUPS;render(true);});
[].forEach.call(document.querySelectorAll('#cat th[data-sort]'),function(th){th.addEventListener('click',function(){var s=th.dataset.sort;if(state.sort===s)state.dir=-state.dir;else{state.sort=s;state.dir=(s==='year'||s==='title'||s==='cls'||s==='difficulty')?1:-1;}render();});});
chips.forEach(function(b){b.addEventListener('click',function(){var k=b.dataset.facet,v=b.dataset.val,s=state.f[k]=state.f[k]||[],i=s.indexOf(v);if(i<0)s.push(v);else s.splice(i,1);if(!s.length)delete state.f[k];reset();render();});});
var qt;qi.addEventListener('input',function(ev){clearTimeout(qt);var v=ev.target.value;qt=setTimeout(function(){state.q=v.trim().toLowerCase();reset();render();},140);});
// phones: a menu replaces the column headings as the sort control (the Filters button and sheet are built in site.js)
(function(){
 var s=document.createElement('select');s.id='msort';s.setAttribute('aria-label','Sort by');[['prio','Sort: priority'],['year','Sort: date'],['title','Sort: name'],['importance','Sort: importance'],['solvability','Sort: solvability'],['difficulty','Sort: difficulty']].forEach(function(o){var x=document.createElement('option');x.value=o[0];x.textContent=o[1];s.appendChild(x);});
 s.addEventListener('change',function(){state.sort=s.value;state.dir=(s.value==='year'||s.value==='title'||s.value==='difficulty')?1:-1;render();});qi.after(s);})();
[['w_imp','imp'],['w_sol','sol'],['w_eas','eas']].forEach(function(p){document.getElementById(p[0]).addEventListener('input',function(ev){state.w[p[1]]=ev.target.value/100;render();});});
clr.addEventListener('click',function(){state.q='';state.f={};qi.value='';reset();render();});
document.getElementById('wreset').addEventListener('click',function(){state.sort='prio';state.dir=-1;state.w={imp:D.weights.importance,sol:D.weights.solvability,eas:D.weights.ease};document.getElementById('w_imp').value=state.w.imp*100;document.getElementById('w_sol').value=state.w.sol*100;document.getElementById('w_eas').value=state.w.eas*100;render();});
var qm=/[?&]q=([^&#]+)/.exec(location.search);if(qm){var qv=decodeURIComponent(qm[1].replace(/\+/g,' '));qi.value=qv;state.q=qv.trim().toLowerCase();}
if(hm&&G[hm[1]])state.v='gone';else load();
render(!location.hash||hm||location.hash.indexOf('=')<0);
if(hm&&G[hm[1]]){var gi=document.getElementById('e'+hm[1]+'g');if(gi)gi.classList.add('hit');document.getElementById('hashnote').scrollIntoView();}
else if(location.hash.indexOf('=')>0||location.hash==='#gone')top.scrollIntoView({block:'start'});
})();
'''


def data_entry(e, k):
    """What the page script reads of an entry, under short keys (the page embeds all of them)."""
    rid = RP.of(e)
    d = {'id': e['id'], 't': e['title'], 'd': e['date'], 'y': e['year'], 'w': e['why'], 's': e['shelfmark'],
         'i': e['importance'], 'so': e['solvability'], 'df': e['difficulty'], 'c': e['cls'], 'r': rid, 'k': help_kind(e),
         'o': short_outcome(e), 'f': k,
         'q': ' '.join(str(x) for x in (e['correspondents'], e['place'], e['region'], e['language'], e.get('known') or '', e.get('open') or '') if x)}
    if flags(e): d['x'] = flags(e)
    if seen_image(e): d['im'] = 1
    if e.get('outcome') or progress(e): d['at'] = 1
    if progress(e): d['pg'] = ', targets/'.join(f for f, _, _ in progress(e))
    if entry_href(e) != solve_href(e): d['h'] = entry_href(e)
    lp = link_pairs(e)[:1]
    if lp: d['l'] = list(lp[0])
    return d


def build_html():
    E = DATA['entries']
    ids = {e['id'] for e in E}
    gone = sorted(set(SOLVED) - ids)
    gone_js = json.dumps({i: [[n, sl] for n, _, _, sl, _ in SOLVED[i]] for i in gone}, ensure_ascii=False).replace('</', '<\\/')
    fk = [filter_keys(e) for e in E]
    keys = [all_keys(e, k) for e, k in zip(E, fk)]
    counted = [e for e in E if e['counted'] and is_open(e)]
    langs = [(l.lower(), l) for l in CAT_LANGS] + [('other', 'other'), ('unknown', 'unknown')]
    used = sorted({RP.of(e) for e in E})
    arch = {rid: [RP.info(rid).get('short') or RP.info(rid)['name'], RP.info(rid).get('city') or '', RP.info(rid).get('country') or '',
                  RP.info(rid)['name'], arch_place(RP.info(rid))] for rid in used}
    n_arch = collections.Counter(k['arch'] for k in keys)
    arch_vals = [(rid, arch[rid][0]) for rid in sorted(used, key=lambda r: (-n_arch[r], arch[r][0]))]
    data_js = json.dumps({'weights': W, 'arch': arch, 'help': HELP, 'flags': {c: list(v) for c, v in FLAG_PILLS.items()},
                          'views': {v: d for v, _, d in VIEWS},
                          'entries': [data_entry(e, k) for e, k in zip(E, fk)]},
                         ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')
    n_all, n_img = len(E), sum(1 for e in E if seen_image(e))
    years = [e['year'] for e in E if e['year']]
    first = sorted((e for e, k in zip(E, keys) if in_view(k, 'try')), key=lambda e: (-priority(e), e['id']))[:30]
    prs = open_prs()
    tabs = ''.join(f'<a role="tab" href="#v={v}" data-v="{v}" aria-selected="{"true" if v == "try" else "false"}">{lab} <span class="n">'
                   f'{sum(in_view(k, v) for k in keys) if v != "gone" else len(gone)}</span></a>' for v, lab, _ in VIEWS)
    page = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>The Unsolved Catalogue — {len(E)} ciphers nobody has read</title>
<meta name="description" content="{len(E)} undeciphered historical cipher letters, {min(years)}–{max(years)}, held by {len([r for r in used if RP.info(r)['kind'] not in ('print', 'unknown')])} archives and libraries. Each has its own page with the sources, what has been tried, and instructions to hand to an AI agent.">
<link rel="stylesheet" href="style.css">
</head>
<body id="top" class="nojs">
<!-- site:nav -->

<section class="hero">
  <p class="kicker">{min(years)}–{max(years)} · {len(E)} ciphers · {len(gone)} moved out to <a href="writeups.html">write-ups</a> · entries last checked {fmt_day(AS_OF)}</p>
  <h1>The Unsolved <span class="stk">Catalogue<a class="sticker" href="#list" title="Pick a cipher below"><span><b>Help<br>Solve!</b><small>pick one below</small></span></a></span></h1>
  <p class="sub">Historical cipher letters that nobody has read. Pick one, open its page, and give that page&rsquo;s address to your AI agent: the page holds the sources, what has been tried and the instructions.</p>
  <ol class="steps"><li><b>1</b>pick a row</li><li><b>2</b>open its page</li><li><b>3</b>point your agent at the URL</li><li><b>4</b>send back what it finds</li></ol>
{summary_html(E, keys, len(gone), prs)}
</section>

<main>
<div id="hashnote" hidden></div>
<h2 id="list">The ciphers</h2>
<div class="cbar" id="cbar">
<nav class="views jsonly" role="tablist" aria-label="Which ciphers">{tabs}</nav>
<p class="vdesc" id="vdesc">{VIEWS[0][2]}</p>
<div class="cfilters jsonly" role="search">
  <input type="search" id="q" placeholder="Search: name, place, archive, shelfmark, year…" aria-label="Search the catalogue">
  {dropdown('Archive', facet('country', 'Country', by_count(keys, 'country', last=('none',)), keys) + facet('arch', 'Archive', arch_vals, keys), 'country arch')}
  {dropdown('Language', facet('lang', 'Language', langs, keys), 'lang')}
  {dropdown('Century', facet('century', 'Century', CENTURIES, keys), 'century')}
  {dropdown('Region', facet('region', 'Region', by_count(keys, 'region', last=('Other',)), keys), 'region')}
  {dropdown('Class', facet('cls', 'Class', CLASSES, keys), 'cls')}
  {dropdown('Status', facet('status', 'Status', STATUSES, keys) + facet('pieces', 'Known pieces', [('known', 'some pieces already read')], keys) + facet('access', 'Access', ACCESS, keys) + facet('help', 'Help needed', [('solve', 'Help solve'), ('read', 'Help read'), ('obtain', 'Help obtain')], keys), 'status pieces access help')}
  {dropdown('More', facet('source', 'Found via', SOURCES, keys)
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
</div>

<div class="tw" id="tw"><table class="cat" id="cat">
<colgroup><col class="c-prio"><col class="c-date"><col class="c-item"><col class="c-shelf"><col class="c-sc"><col class="c-sc"><col class="c-sc"><col class="c-cls"></colgroup>
<thead><tr>
<th class="prio" data-sort="prio" aria-sort="descending">Priority</th><th data-sort="year">Date</th><th data-sort="title">Cipher</th><th>Where</th>
<th class="sc" data-sort="importance">Import.</th><th class="sc" data-sort="solvability">Solvab.</th><th class="sc" data-sort="difficulty">Difficulty</th><th class="cls" data-sort="cls">Class</th>
</tr></thead>
<tbody>
{"".join(row(e) for e in first)}
</tbody></table></div>
<div class="more jsonly" id="more"></div>
<noscript><p class="vdesc">Without JavaScript only the {len(first)} highest-priority entries that can be worked from a desk are listed. The whole catalogue is in <a href="https://github.com/dbourdeau/cyphersolver/blob/main/CATALOGUE.md">CATALOGUE.md</a>, and every entry has its own page at solve/&lt;number&gt;.html.</p></noscript>
<div class="legend"><span>click a row for its page</span><span>● viewed on the image</span><span>◇ catalogue description only</span><span>gold dots importance / solvability</span><span>red dots difficulty</span><span>class A sibling deciphered · B partial key in print · C no key</span></div>

<div class="gonep" id="gonep">
<h3 id="gone">Numbers that have left the catalogue <span class="n">{len(gone)}</span></h3>
<p class="d">If a number you were given is not in the list, it is here. <i>+1</i> marks a number split between write-ups; a piece still open stays in the list under its number. Hover a number for its write-ups and the day each landed.</p>
{gone_html(gone)}
</div>

{sources_html(E)}

<h2 id="about">About the catalogue</h2>
<p>Historical cipher documents that nobody has read: ciphertext with no decipherment known in the document itself, in DECODE, in Tomokiyo&rsquo;s and Lasry&rsquo;s lists, in the edition or in the literature. It began with the French diplomatic volumes on Gallica and the records DECODE marks not decrypted, and grew through sweeps of archive portals, finding aids and printed calendars (<a href="#where">where the ciphers are</a>). Since the October 2026 sweeps a new find enters only after vetting: the ciphertext seen, prior art searched, keys recorded, duplicates checked; the rest wait as leads. {len(counted)} entries are counted targets, {len(E) - len(counted)} are noted only.</p>
<p>Class <b>A</b> means a sibling with a decipherment in the same volume, <b>B</b> a partial key or a known family in print, <b>C</b> no key and no sibling. An entry read, partly read, resolved or found in print leaves the catalogue and is written up (<a href="#v=gone" data-go="gone">left the catalogue</a>); one attempted here without a reading stays, tagged <b>attempted, open</b>; one a target folder is working on is tagged <b>in progress</b>, read at each rebuild from the head of the folder&rsquo;s NOTES.md. Data: <a href="https://github.com/dbourdeau/cyphersolver/blob/main/catalogue.json" rel="noopener">catalogue.json</a> · text: <a href="https://github.com/dbourdeau/cyphersolver/blob/main/CATALOGUE.md" rel="noopener">CATALOGUE.md</a> · how to send a result: <a href="contribute.html">contribute</a>.</p>
<details class="about"><summary>How the scores were set</summary>
<p><b>Importance</b> asks what a full reading would add: 5 for a first-hand report of a major event by a principal witness (du Bellay in London 1529, Lanssac at the Polish election), 2 for routine business. <b>Solvability</b> asks whether the material online is enough: 5 when deciphered siblings of the same hand and year sit in the same volume, 1 for one short letter in an unknown language. <b>Difficulty</b> is the technical work at the keyboard: 1 for aligning a known sibling, 5 for a statistics-only attack on a large homophonic nomenclator. The default priority weights importance {W['importance']}, solvability {W['solvability']} and ease {W['ease']} (ease is 6 minus difficulty), rescaled to 0–10; change them under &ldquo;More&rdquo; above the list. Every score is a judgement made before viewing the leaf, so treat the order as a work plan, not a finding.</p>
</details>
<details class="about"><summary>What was checked</summary>
<p>Scores are judgements from catalogue descriptions and the literature, not from the leaves: {n_img} of {n_all} entries have been viewed on the image, and each page carries the check that would confirm it is open. Checked for every entry: the catalogue description and item numbering, the presence or absence of a decipherment in the volume, and the shelfmark. For the DECODE entries: the record metadata and notes, key records from the same archive series, overlap with this repository&rsquo;s targets and with Tomokiyo&rsquo;s list. Entries tagged <i>rule-scored</i> were scored by a script from DECODE&rsquo;s metadata and not yet reviewed by hand. Verify each entry on the image and in the literature before attacking it.</p>
</details>
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
    rv = reserved(e)
    if rv and rv.get('kind') == 'claim' and not prog:
        prog = (f'<div class="callout blue"><p><strong>Being worked on.</strong> {esc(rv["by"])} announced work on this cipher on '
                f'{esc(rv["since"])}; the notice stands until {esc(rv["until"])}. It is there to avoid double work and holds nothing back: '
                f'a verified result from anyone is still merged and credited.</p></div>\n')
    elif rv and not prog:
        prog = (f'<div class="callout blue"><p><strong>Reserved until {esc(rv["until"])}.</strong> {esc(rv["by"])} found this cipher and '
                f'asked to try it first (reserved {esc(rv["since"])}). Checking it against the vetting bar is still open to anyone; '
                f'a decipherment attempt by someone else waits until the date has passed.</p></div>\n')
    elif prog:
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
<link rel="canonical" href="{url}">
<meta property="og:type" content="article">
<meta property="og:site_name" content="Cyphersolver">
<meta property="og:url" content="{url}">
<meta property="og:title" content="No. {e["id"]}: {title.replace(chr(34), '&quot;')}">
<meta property="og:image" content="{SITE}hero_poster.png">
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


def gone_page(i, shell):
    rows = SOLVED[i]
    links = ''.join(f'<li><a href="{sl}.html">{esc(n)}</a> ({esc(sec)})</li>' if sl else f'<li>{esc(n)} ({esc(sec)})</li>' for n, sec, _, sl, _ in rows)
    first = next((sl for _, _, _, sl, _ in rows if sl), None)
    return (f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<base href="../">
<title>No. {i} has left the catalogue</title>
<meta name="robots" content="noindex">
{f'<link rel="canonical" href="{SITE}{first}.html">' if first else ''}
{shell["head"]}
</head>
<body id="top" class="pg-solve">
{shell["nav"]}

<section class="hero solve">
  <p class="kicker"><a href="catalogue.html">Unsolved Catalogue</a> · no. {i}</p>
  <h1>No. {i} has left the catalogue</h1>
  <p class="sub">This address used to hold the task for catalogue no. {i}. The cipher now has an outcome, so the task has closed and the work is written up here:</p>
</section>

<main>
<ul>{links}</ul>
<p><a href="catalogue.html">&larr; The ciphers still open</a></p>
</main>
{shell["footer"].replace('href="#top"', f'href="solve/{i}.html#top"')}
{shell["scripts"]}
</body>
</html>
''')


def build_solve_pages():
    """Run after _build_site.py: the nav, footer and scripts are taken from the built catalogue.html."""
    s = (HERE / 'catalogue.html').read_text(encoding='utf-8')
    shell = dict(
        head='\n'.join(re.findall(r'<link rel="(?:stylesheet|icon|apple-touch-icon)"(?![^>]*href="pg-)[^>]*>', s)),
        nav=re.search(r'<header class="nav">.*?</header>\n<div class="search" id="search".*?</div>\n</div>', s, re.S).group(0),
        footer=re.search(r'<footer>.*?</footer>', s, re.S).group(0),
        scripts='\n'.join(re.findall(r'<script src="[^"]+"></script>', s)))
    out = HERE / 'solve'
    out.mkdir(exist_ok=True)
    keep = set()
    for e in DATA['entries']:
        p = out / f'{e["id"]}.html'; keep.add(p.name)
        p.write_text(solve_page(e, shell), encoding='utf-8')
    # a number that has left the catalogue keeps its address: people and agents were given it, so it says where the work went
    gone = 0
    for i in sorted(set(SOLVED) - {e['id'] for e in DATA['entries']}):
        p = out / f'{i}.html'; keep.add(p.name); gone += 1
        p.write_text(gone_page(i, shell), encoding='utf-8')
    for p in out.glob('*.html'):          # anything else has no page: 404.html explains
        if p.name not in keep: p.unlink()
    print('wrote', len(keep) - gone, 'pages and', gone, 'moved notices in docs/solve/')


if __name__ == '__main__':
    update_md()
    build_html()
    import subprocess, sys
    subprocess.run([sys.executable, '_build_site.py'], check=True, cwd=pathlib.Path(__file__).parent)
