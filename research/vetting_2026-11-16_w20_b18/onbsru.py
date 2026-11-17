"""ONB Alma SRU (open to scripts, 16 Nov 2026): python onbsru.py '<cql>' [max] -> prints MARC fields per record."""
import sys, urllib.request, urllib.parse, xml.etree.ElementTree as ET, time
q = sys.argv[1]; mx = sys.argv[2] if len(sys.argv) > 2 else '20'
start = sys.argv[3] if len(sys.argv) > 3 else '1'
u = ('https://obv-at-oenb.alma.exlibrisgroup.com/view/sru/43ACC_ONB?version=1.2&operation=searchRetrieve'
     '&maximumRecords=%s&startRecord=%s&query=%s' % (mx, start, urllib.parse.quote(q)))
x = urllib.request.urlopen(urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'}), timeout=60).read()
ns = {'s': 'http://www.loc.gov/zing/srw/', 'm': 'http://www.loc.gov/MARC21/slim'}
r = ET.fromstring(x)
print('N =', r.findtext('s:numberOfRecords', namespaces=ns))
for rec in r.iter('{http://www.loc.gov/MARC21/slim}record'):
    print('-----')
    for f in rec:
        tag = f.get('tag')
        if f.tag.endswith('controlfield'):
            if tag in ('001', '009'): print(tag, f.text)
            continue
        if tag in ('035', '040', '042', '049', '970', '971', '998', '999', 'AVA', 'AVE', '983', '984'): continue
        print(tag, ' | '.join('%s:%s' % (s.get('code'), s.text) for s in f))
