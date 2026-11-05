# In-volume Google Books search (jscmd endpoint answers past the CAPTCHA wall).  python gb_search.py <id> <term> [...]
import json, re, html, sys, urllib.request, urllib.parse
vid = sys.argv[1]
for q in sys.argv[2:]:
    url = 'https://books.google.com/books?' + urllib.parse.urlencode({'id': vid, 'jscmd': 'SearchWithinVolume2', 'q': q})
    t = urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'}), timeout=60).read().decode('utf8', 'replace')
    try:
        d = json.loads(t)
    except Exception:
        print('==', q, 'not json:', t[:120]); continue
    print('==', q, 'hits', d.get('number_of_results'))
    for s in d.get('search_results', [])[:20]:
        print(' ', s.get('page_id'), html.unescape(re.sub('<[^>]+>', '', s.get('snippet_text', '')))[:320])
