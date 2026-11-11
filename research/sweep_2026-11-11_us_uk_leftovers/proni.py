"""PRONI eCatalogue search by plain HTTP (ASP.NET form), 11 Nov 2026.

Usage: python3 proni.py <scratch dir> <term> [EXP|ALL|ANY]
Posts the search form at apps.proni.gov.uk/eCatNI_IE/SearchPage.aspx with its hidden fields and saves the result
page(s) as <scratch>/proni/<term>_<n>.html; prints the rows found. Page size 50 (the largest offered is used).
"""
import html, os, re, sys, time
import requests

S, term = sys.argv[1], sys.argv[2]
match = sys.argv[3] if len(sys.argv) > 3 else 'EXP'
U = 'https://apps.proni.gov.uk/eCatNI_IE/SearchPage.aspx'
s = requests.Session()
s.headers['User-Agent'] = ('Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 '
                           'Safari/537.36')
os.makedirs(os.path.join(S, 'proni'), exist_ok=True)


def hidden(h):
    d = {}
    for m in re.finditer(r'<input type="hidden" name="([^"]+)" id="[^"]*" value="([^"]*)"', h):
        d[m.group(1)] = html.unescape(m.group(2))
    return d


h = s.get(U, timeout=60).text
sizes = re.findall(r'<option[^>]*value="(\d+)"', h[h.find('ddPageSize'):h.find('ddPageSize') + 800])
d = hidden(h)
P = 'ctl00$ContentPlaceHolder1$'
d.update({P + 'txtWords': term, P + 'radWordSearchFields': 'BOTH', P + 'radWordMatch': match,
          P + 'UCStartDate$txtYear': '', P + 'UCEndDate$txtYear': '', P + 'txtPRONIRef': '',
          P + 'ddPageSize': max(sizes, key=int) if sizes else '10', P + 'SearchArchiveBtn': 'Search'})
for k in ('UCStartDate$cmbMonth', 'UCStartDate$cmbDay', 'UCEndDate$cmbMonth', 'UCEndDate$cmbDay'):
    d[P + k] = ''
m = re.search(r'name="ctl00\$ContentPlaceHolder1\$ddSortBy".*?<option selected="selected" value="([^"]*)"', h, re.S)
d[P + 'ddSortBy'] = m.group(1) if m else ''
r = s.post(U, data=d, timeout=90)
n = 1
while True:
    t = r.text
    open(os.path.join(S, 'proni', f'{term.replace(" ", "_")}_{n}.html'), 'w').write(t)
    print('url', r.url, 'len', len(t))
    for m in re.finditer(r'(Showing[^<]{0,80}|[0-9,]+ (?:results|records)[^<]{0,40}|Request Rejected)', t):
        print(' ', m.group(1))
    break
