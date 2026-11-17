"""Google Books gdata feed query: print title, id, and the preview link (which carries pg= when a page matched)."""
import sys, re, html, urllib.parse, urllib.request
q = sys.argv[1]
req = urllib.request.Request('https://www.google.com/books/feeds/volumes?max-results=20&q=' + urllib.parse.quote(q), headers={'User-Agent': 'Mozilla/5.0'})
t = urllib.request.urlopen(req, timeout=30).read().decode('utf8', 'replace')
for e in re.findall(r'<entry>(.*?)</entry>', t, re.S):
    title = ' / '.join(html.unescape(x) for x in re.findall(r'<dc:title>(.*?)</dc:title>', e))
    vid = re.search(r'volumes/([\w-]+)</id>', e).group(1)
    prev = re.search(r"rel='http://schemas.google.com/books/2008/preview'[^>]*href='([^']*)'", e)
    pg = re.search(r'pg=(\w+)', prev.group(1)) if prev else None
    date = re.findall(r'<dc:date>(.*?)</dc:date>', e)
    desc = html.unescape(re.sub('<[^>]+>', '', ' '.join(re.findall(r'<dc:description>(.*?)</dc:description>', e, re.S))))[:300]
    print(vid, date, title[:110], '| pg=', pg.group(1) if pg else '-', '|', desc)
