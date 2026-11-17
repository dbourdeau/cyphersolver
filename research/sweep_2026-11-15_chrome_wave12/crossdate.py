"""Wave 12: date + sender cross-check of the narrowed leads 2870-2873 against the full CSP Spain vol. 2 pages (1522-24)."""
import re, os
H = os.path.dirname(os.path.abspath(__file__))
def page(n): return open(os.path.join(H, 'csp_pages', f'{n}.txt'), encoding='utf8').read()
MON = {'01':'Jan','02':'Feb','03':'Mar','04':'Apr','05':'May','06':'Jun','07':'Jul','08':'Aug','09':'Sep','10':'Oct','11':'Nov','12':'Dec'}
def node(y, m): return 79737 + (int(y) - 1522) * 12 + (int(m) - 1) + (1 if (y, m) > ('1522', '06') else 0) - (1 if (y, m) > ('1523', '11') and False else 0)
L = {2870: ('Lannoy|Viceroy of Naples', ['1522-10-26','1523-05-11','1523-06-08','1523-07-05','1523-07-15','1523-09-12','1524-02-20']),
     2871: ('Colonna', ['1523-01-10','1523-01-28']),
     2872: ('Adorno', ['1522-08-19','1523-03-22','1523-06-13','1524-04-11','1524-12-07']),
     2873: ('Adrian|Pope|Tortosa', ['1522-09-30','1523-03-02']),
     2876: ('Najera|Nagera|Marin|Abbot', ['1522-02-12','1522-02-17','1522-03-20','1523-01-04','1523-04-30','1523-05-02','1524-01-20','1524-02-21'])}
for lid, (sp, dates) in L.items():
    for d in dates:
        y, m, dd = d.split('-'); dd = int(dd)
        # month nodes: 79737 = Jan 1522 ... Jun split in two (79742, 79743), so later months shift by 1
        idx = (int(y) - 1522) * 12 + int(m) - 1
        n = 79737 + idx + (1 if idx >= 6 else 0)
        nodes = [n] + ([79743] if (y, m) == ('1522', '06') else [])
        hits = []
        for nn in nodes:
            b = page(nn)
            for mm in re.finditer(r'(?:—|--)\s*[A-Z][\w\-\' ]{2,30}[, ]+(?:the )?%d(?:st|nd|rd|th)? (?:of )?%s' % (dd, MON[m]), b):
                seg = b[max(0, mm.start() - 700):mm.end()]
                if re.search(sp, seg): hits.append(b[max(0, mm.start() - 260):mm.end() + 60])
        print(lid, d, n, len(hits))
        for h in hits[:2]: print('    ', h[-330:])
