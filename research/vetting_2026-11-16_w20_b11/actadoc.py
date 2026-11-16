"""Fetch one ACTApro record by plain curl-style GET: https://archive.spk-berlin.de/actaproweb/document/Vz_<uuid>
(the archive.xhtml?id=Vz++++++<uuid> permalink returns only the JSF frame; the /document/ route returns the full view).
Usage: python -I -X utf8 actadoc.py <uuid> [<uuid> ...]   (uuid with or without the Vz_ / Vz++++++ prefix)"""
import re, sys, time, html, urllib.request

for a in sys.argv[1:]:
    u = re.sub(r'^(Vz_|Vz\+*|Vz\s*)', '', a)
    url = 'https://archive.spk-berlin.de/actaproweb/document/Vz_' + u
    t = urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (research script)'}), timeout=40).read().decode('utf8', 'replace')
    t = re.sub(r'<(script|style).*?</\1>', '', t, flags=re.S)
    t = re.sub(r'<[^>]+>', ' ', t)
    t = re.sub(r'\s+', ' ', html.unescape(t))
    i = t.find('Vollansicht')
    j = t.find('Archiv: Geheimes Staatsarchiv PK', i)
    print('=====', url)
    print(t[i:j + 40] if i >= 0 else t[:3000])
    time.sleep(1)
