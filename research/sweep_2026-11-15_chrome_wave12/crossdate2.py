"""Wave 12: second date cross-check: any 'the Nth of Month YYYY' dateline on the matching CSP vol. 2 month page, with the 450 characters before it."""
import re, os
H = os.path.dirname(os.path.abspath(__file__))
MON = ['January','February','March','April','May','June','July','August','September','October','November','December']
L = {2870: ['1522-10-26','1523-05-11','1523-06-08','1523-07-05','1523-07-15','1523-09-12','1524-02-20'], 2871: ['1523-01-10','1523-01-28'],
     2872: ['1522-08-19','1523-03-22','1523-06-13','1524-04-11','1524-12-07'], 2873: ['1522-09-30','1523-03-02'],
     2876: ['1522-02-12','1522-02-17','1522-03-20','1523-01-04','1523-04-30','1523-05-02','1524-01-20','1524-02-21']}
for lid, ds in L.items():
    for d in ds:
        y, m, dd = d.split('-'); idx = (int(y) - 1522) * 12 + int(m) - 1; n = 79737 + idx + (1 if idx >= 6 else 0)
        nodes = [n] + ([79743] if (y, m) == ('1522', '06') else [])
        out = []
        for nn in nodes:
            b = open(os.path.join(H, 'csp_pages', f'{nn}.txt'), encoding='utf8').read()
            for mm in re.finditer(r'the %d(?:st|nd|rd|th)? of %s,? %s' % (int(dd), MON[int(m) - 1], y), b):
                out.append(b[max(0, mm.start() - 120):mm.end() + 20])
        print(lid, d, len(out))
        for o in out: print('     ', o)
