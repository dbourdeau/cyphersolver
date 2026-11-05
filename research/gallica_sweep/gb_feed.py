# Google Books gdata feed search (answers when books.google.* shows the CAPTCHA). python gb_feed.py "<query>" [max]
import re, html, sys, urllib.request, urllib.parse
q = sys.argv[1]; n = sys.argv[2] if len(sys.argv) > 2 else '10'
url = 'https://www.google.com/books/feeds/volumes?' + urllib.parse.urlencode({'q': q, 'max-results': n})
t = urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'}), timeout=60).read().decode('utf8', 'replace')
print('total', re.findall(r'<openSearch:totalResults>(\d+)', t))
for e in re.findall(r'<entry>(.*?)</entry>', t, re.S):
    vid = re.findall(r'<dc:identifier>([^<]+)', e)[0]
    title = ' / '.join(re.findall(r'<dc:title>([^<]*)', e)); date = re.findall(r'<dc:date>([^<]*)', e)
    desc = html.unescape(html.unescape(' '.join(re.findall(r'<dc:description>([^<]*)', e))))
    print('-', vid, title[:90], date, '\n   ', desc[:400])
