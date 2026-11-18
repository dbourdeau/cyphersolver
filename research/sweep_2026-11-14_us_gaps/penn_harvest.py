"""PACSCL / Philadelphia Area Archives (findingaids.library.upenn.edu, ArcLight): HTML search, plain curl works."""
import re, json, time, html, urllib.parse, urllib.request, sys
TERMS = ['cipher','cypher','ciphers','ciphered','cryptogram','"secret writing"','"code book"','"in code"','"in cipher"','decipher','deciphered','deciphering','cryptograph*','"numerical code"','"secret code"','encoded','encrypted','"key to the cipher"','enciphered','cryptographic','"secret ink"','"private cipher"','"cypher key"']
out = {}
def get(u):
    r = urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'})
    return urllib.request.urlopen(r, timeout=40).read().decode('utf8', 'replace')
for q in TERMS:
    n = 0
    for p in range(1, 8):
        u = 'https://findingaids.library.upenn.edu/?' + urllib.parse.urlencode({'q': q, 'per_page': 100, 'page': p})
        try: t = get(u)
        except Exception as e: print(q, p, 'err', e); break
        arts = re.findall(r'<article.*?</article>', t, re.S)
        for a in arts:
            id_ = re.search(r'data-document-id="([^"]+)"', a).group(1)
            m = re.search(r'<a itemprop="name" href="([^"]+)">(.*?)</a>', a, re.S)
            def f(c):
                x = re.search(r'blacklight-%s ">.*?</dt>\s*<dd class="blacklight-%s">(.*?)</dd>' % (c, c), a, re.S)
                return html.unescape(re.sub(r'<[^>]+>', ' ', x.group(1))).strip() if x else ''
            rec = out.setdefault(id_, {'id': id_, 'href': m.group(1) if m else '', 'title': html.unescape(re.sub(r'\s+',' ',m.group(2))).strip() if m else '',
                'date': f('display_date_ssim'), 'repo': f('repository_ssi'), 'abstract': re.sub(r'\s+',' ',f('abstract_scope_contents_tsi')), 'terms': []})
            rec['terms'].append(q)
        n += len(arts)
        if len(arts) < 100: break
        time.sleep(2)
    print(q, n, len(out)); time.sleep(2)
json.dump(out, open('_tmp/penn_raw.json', 'w', encoding='utf8'), ensure_ascii=False, indent=0)
