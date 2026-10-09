"""List the '?' tokens of high/medium hand-read lines with dec.py's choice (dec_out/<page>_fh.txt) and margin."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import dec
sys.stdout.reconfigure(encoding='utf-8')
pages = sys.argv[1:] or dec.PAGES
for pg in pages:
    t = open('dec_out/%s_fh.txt' % pg, encoding='utf8').read().splitlines()
    de = [x for l in t if l.startswith('dec:') for x in l.split()[1:]]
    mg = [float(x) for l in t if l.startswith('marg:') for x in l.split()[1:]]
    ct, rd, pairs = dec.page_pairs(pg)
    m = {}
    for r, h, conf, bi, i in pairs: m.setdefault(bi, []).append((h, i))
    for bi, b in enumerate(rd):
        if b['conf'] not in ('high', 'medium'): continue
        hs = m.get(bi, [])
        if not any('?' in h for h, _ in hs): continue
        line = []
        for h, i in hs:
            d = de[i]; v = dec.VAL.get(d, '-') or '_'
            if '?' in h: line.append('<%s|%s=%s m%.1f>' % (h, d, v, mg[i]))
            else: line.append(dec.VAL.get(h, h) or '_')
        print('%s l.%s: %s' % (pg, b['line'], ' '.join(line)))
        print('      hand it: ' + b['it'])
