import sys, os, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import aev
for i in sys.argv[1:]:
    h = aev.get('https://scopequery.vs.ch/detail.aspx?Id=' + i)
    open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'src', 'aev_%s.html' % i), 'w', encoding='utf8').write(h)
    t = aev.text(h)
    a = t.find('Ref. code'); a = t.find('Signatur') if a < 0 else a
    print('===', i, t[max(a,0):max(a,0)+2500]); time.sleep(1)
