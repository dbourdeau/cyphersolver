"""DECODE records search (de-crypt.org/decrypt-web/RecordsList?cmd=search&search=...): print the number of records and the first rows. usage: decode_q.py term [term ...]"""
import sys, re, html, time, requests
for q in sys.argv[1:]:
    S = requests.Session(); S.headers['User-Agent'] = 'Mozilla/5.0'
    x = S.get('https://de-crypt.org/decrypt-web/RecordsList', params={'cmd': 'search', 'search': q, 'searchtype': '='}, timeout=60).text
    m = re.search(r'Records?\s*(\d+)\s*to\s*(\d+)\s*of\s*(\d+)', re.sub(r'<[^>]+>', ' ', x)); n = m.group(3) if m else ('0' if re.search(r'No records found', x) else '?')
    rows = re.findall(r'<tr[^>]*data-rowindex[^>]*>(.*?)</tr>', x, re.S)
    print(f'{q!r}: {n} records')
    for r in rows[:6]: print('   ', html.unescape(re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', r))).strip()[:230])
    time.sleep(2)
