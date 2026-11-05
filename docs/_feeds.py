"""The files that outside readers and machines use: feed.xml (the newest write-ups, Atom), sitemap.xml and robots.txt.
Written at the end of every build from the manifest and _dates.json; only stable fields go in, so a rebuild that
changes nothing leaves them unchanged.
"""
import html, pathlib, re

HERE = pathlib.Path(__file__).parent
BASE = 'https://cyphersolver.com/'
FEED_SIZE = 40

def x(s): return html.escape(s, quote=True)

def stamp(rec, key='first'):
    """An RFC 3339 time from a _dates.json record: 'posted' for the first day when it is known."""
    if key == 'first' and rec.get('posted'): return rec['posted']
    return f'{rec[key]}T00:00:00Z'

def write_feed(pages, dates, plain):
    rows = sorted((p for p in pages if p['slug'] in dates), key=lambda p: stamp(dates[p['slug']]), reverse=True)[:FEED_SIZE]
    entries = []
    for p in rows:
        rec, url = dates[p['slug']], f'{BASE}{p["slug"]}.html'
        entries.append(f'<entry><title>{x(plain(p["title"]))}</title><link href="{url}"/><id>{url}</id>'
                       f'<published>{stamp(rec)}</published><updated>{max(stamp(rec), stamp(rec, "updated"))}</updated>'
                       f'<category term="{x(plain(p["stt"]))}"/><summary>{x(plain(p.get("blurb", "")))}</summary></entry>')
    newest = max((re.search(r'<updated>(.*?)</updated>', e).group(1) for e in entries), default='2026-09-18T00:00:00Z')
    feed = ('<?xml version="1.0" encoding="utf-8"?>\n<feed xmlns="http://www.w3.org/2005/Atom">\n'
            '<title>Cyphersolver: new write-ups</title>\n'
            '<subtitle>Historical ciphers: what has been deciphered, by whom and how.</subtitle>\n'
            f'<link href="{BASE}feed.xml" rel="self"/>\n<link href="{BASE}"/>\n<id>{BASE}</id>\n<updated>{newest}</updated>\n'
            '<author><name>Daniel Bourdeau and contributors</name></author>\n' + '\n'.join(entries) + '\n</feed>\n')
    (HERE / 'feed.xml').write_text(feed, encoding='utf-8', newline='\n')
    return len(entries)

def is_stub(s):
    return bool(re.search(r'<meta name="robots" content="noindex"', s[:1500]))

def write_sitemap(dates):
    urls = []
    for path in sorted(HERE.glob('*.html')):
        if path.stem == '404' or is_stub(path.read_text(encoding='utf-8')): continue
        rec = dates.get(path.stem)
        loc = BASE if path.stem == 'index' else f'{BASE}{path.name}'
        urls.append(f'<url><loc>{loc}</loc>' + (f'<lastmod>{rec["updated"]}</lastmod>' if rec else '') + '</url>')
    for folder in ('solve', 'further'):
        for path in sorted((HERE / folder).glob('*.html')):
            if not is_stub(path.read_text(encoding='utf-8')): urls.append(f'<url><loc>{BASE}{folder}/{path.name}</loc></url>')
    (HERE / 'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
                                      + '\n'.join(urls) + '\n</urlset>\n', encoding='utf-8', newline='\n')
    (HERE / 'robots.txt').write_text(f'User-agent: *\nAllow: /\n\nSitemap: {BASE}sitemap.xml\n', encoding='utf-8', newline='\n')
    return len(urls)
