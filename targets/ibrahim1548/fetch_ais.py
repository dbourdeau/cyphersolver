"""Download the public AIS scans of catalogue 885 (HHStA StAbt Tuerkei I 7-4-4, 7-4-5, 7-4-9).
python fetch_ais.py   -> img/<label>_<n>.jpg (img/ is git-ignored)
No login is needed: GET the detail page for the session cookie, then getimage.aspx with a Referer
(route from research/aut_hhsta/README.md and targets/maximiliana1510/fetch_ais.py)."""
import os, re, time, requests

UNITS = [('7040827', '744'), ('7040824', '745'), ('7040845', '749')]
here = os.path.dirname(os.path.abspath(__file__))
os.makedirs(os.path.join(here, 'img'), exist_ok=True)
s = requests.Session(); s.headers['User-Agent'] = 'Mozilla/5.0 (research)'
for vid, label in UNITS:
    detail = 'https://www.archivinformationssystem.at/detail.aspx?ID=' + vid
    page = s.get(detail, timeout=60).text
    pages = [int(x) for x in re.findall(r'sqnznr=(\d+)', page, re.I)]
    if not pages:
        print(label, 'no image links on the detail page'); continue
    for i in range(1, max(pages) + 1):
        out = os.path.join(here, 'img', '%s_%02d.jpg' % (label, i))
        if os.path.exists(out): continue
        r = s.get('https://www.archivinformationssystem.at/getimage.aspx?veid=%s&deid=10&sqnznr=%d&width=4000&klid=9'
                  % (vid, i), headers={'Referer': detail}, timeout=120)
        open(out, 'wb').write(r.content)
        time.sleep(1)
    print(label, max(pages), 'images')
