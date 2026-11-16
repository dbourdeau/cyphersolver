"""Build docs/corrections.html: the corrections log, newest first.

Every row comes from the profiles (targets/<folder>/profile.json and the nested research sweeps), nothing is typed
in by hand:
  - outcome.credits[] with role 'key corrected' (who, date, note, source), unless marked published: false;
  - outcome.human_check with result 'corrected' (by, date, passage, note).
The link column is the credit's source when it is a URL, an issue or pull request number (#N) in the source or the
note, or a repository path; otherwise the source is shown as text.

Called from _build_site.py before the pages are processed, so corrections.html gets the nav and footer like any page.
"""
import html, re
import _methods as M

REPO = 'https://github.com/dbourdeau/cyphersolver'
MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec')
KIND = {'credit': 'key corrected or extended', 'check': 'image check: corrected'}


def esc(t):
    return html.escape(str(t), quote=False)


def fmt(d):
    """YYYY, YYYY-MM or YYYY-MM-DD, as the site writes dates."""
    parts = (d or '').split('-')
    if len(parts) == 3 and all(x.isdigit() for x in parts): return f'{int(parts[2])} {MONTHS[int(parts[1]) - 1]} {parts[0]}'
    if len(parts) == 2 and all(x.isdigit() for x in parts): return f'{MONTHS[int(parts[1]) - 1]} {parts[0]}'
    return esc(d or 'undated')


def checks_of(prof):
    hc = ((prof or {}).get('outcome') or {}).get('human_check')
    return [h for h in (hc if isinstance(hc, list) else [hc] if hc else []) if isinstance(h, dict)]


def entries(profiles):
    out = []
    for folder, prof in profiles.items():
        for c in ((prof or {}).get('outcome') or {}).get('credits') or []:
            if isinstance(c, dict) and c.get('role') == 'key corrected' and c.get('published') is not False:
                out.append(dict(folder=folder, kind='credit', date=c.get('date') or '', who=c.get('who'),
                                what=c.get('note') or '', source=c.get('source') or ''))
        for h in checks_of(prof):
            if h.get('result') == 'corrected':
                what = '; '.join(x for x in (h.get('passage'), h.get('note')) if x)
                out.append(dict(folder=folder, kind='check', date=h.get('date') or '', by=h.get('by') or '',
                                what=what, source=''))
    out.sort(key=lambda e: (e['date'], e['folder']), reverse=True)
    return out


def link_html(e):
    src = e['source']
    m = re.match(r'https://github\.com/dbourdeau/cyphersolver/(issues|pull)/(\d+)', src)
    if m: return f'<a href="{esc(src)}" rel="noopener">{"issue" if m.group(1) == "issues" else "PR"} #{m.group(2)}</a>'
    if src.startswith(('http://', 'https://')): return f'<a href="{esc(src)}" rel="noopener">source &#8599;</a>'
    m = re.search(r'(?:issue|pull request|PR)\s+#(\d+)', src) or re.search(r'(?:issue|pull request|PR)\s+#(\d+)', e['what'])
    if m: return f'<a href="{REPO}/issues/{m.group(1)}" rel="noopener">#{m.group(1)}</a>'
    if re.match(r'(targets|research)/[\w./-]+$', src): return f'<a href="{REPO}/blob/main/{esc(src)}" rel="noopener">file &#8599;</a>'
    return esc(src) if src else '&ndash;'


def target_html(e, folder_page, paths):
    p = folder_page.get(e['folder'])
    if p: return f'<a href="{p["slug"]}.html">{p["label"]}</a> <span class="yr">{p["year"]}</span>'
    path = paths.get(e['folder'])
    rel = path.parent.relative_to(M.ROOT).as_posix() if path else f'targets/{e["folder"]}'
    return f'<a href="{REPO}/tree/main/{esc(rel)}" rel="noopener">{esc(e["folder"])}</a>'


def who_html(e, contrib):
    if e['kind'] == 'check': return esc(e['by'])
    c = contrib.get(e['who'])
    return f'<a href="contributors.html#{esc(e["who"])}">{esc(c["name"])}</a>' if c else esc(e['who'] or '')


def build_html(here, pages, profiles, contrib, version):
    folder_page = {f: p for p in pages for f in p.get('folders') or []}
    paths = M.profile_paths()
    E = entries(profiles)
    rows = ''.join(
        f'<tr><td class="date"><time datetime="{esc(e["date"])}">{fmt(e["date"])}</time></td>'
        f'<td>{target_html(e, folder_page, paths)}</td><td>{KIND[e["kind"]]}</td>'
        f'<td>{esc(e["what"])}</td><td>{who_html(e, contrib)}</td><td>{link_html(e)}</td></tr>\n' for e in E)
    page = (
        '<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
        f'<title>Corrections log &mdash; {len(E)} entries from the profiles</title>\n'
        '<meta name="description" content="Keys corrected or extended, and readings corrected on the image, as recorded '
        'in the targets&rsquo; profile.json files: newest first, with date, author and source.">\n'
        f'<link rel="stylesheet" href="style.css?v={version}">\n</head>\n<body id="top">\n<!-- site:nav -->\n\n'
        '<section class="hero">\n'
        f'  <p class="kicker">Reference &middot; {len(E)} entries</p>\n'
        '  <h1>Corrections log</h1>\n'
        '  <p class="sub">Read from each target&rsquo;s <code>profile.json</code> at every build: the credits with the '
        'role &ldquo;key corrected&rdquo; (a key corrected or extended) and the checks of a passage against the image '
        'whose recorded result is &ldquo;corrected&rdquo;. Newest first.</p>\n'
        '  <p class="meta">Daniel Bourdeau and contributors</p>\n</section>\n\n<main>\n\n'
        '<h2 id="log">Newest first</h2>\n'
        '<div class="tw"><table>\n<thead><tr><th>Date</th><th>Target</th><th>Kind</th><th>Note in the profile</th>'
        '<th>By</th><th>Source</th></tr></thead>\n<tbody>\n' + rows + '</tbody></table></div>\n\n'
        '</main>\n<!-- site:footer -->\n</body>\n</html>\n')
    (here / 'corrections.html').write_text(page, encoding='utf-8')
    return len(E)
