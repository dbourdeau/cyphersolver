"""Per line: the hand reading (rd_*.txt) next to dec.py's output (dec_out/<page><tag>.txt) and each token's top
candidates (channel + prior). Usage: python -I lineview.py <page> [tag] [line numbers...]"""
import sys, os, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('ALPHA', '0.4'); os.environ.setdefault('BETA', '0.4'); os.environ.setdefault('CLEN', '0.3')
import dec
sys.stdout.reconfigure(encoding='utf-8')
pg = sys.argv[1]; tag = sys.argv[2] if len(sys.argv) > 2 else '_fh'
want = set(int(x) for x in sys.argv[3:])
model = dec.Model(dec.PAGES)
L = open('dec_out/%s%s.txt' % (pg, tag), encoding='utf8').read().splitlines()
rd = {b['line']: b for b in dec.load_rd(pg)}
i = 1
while i < len(L):
    ln = int(re.search(r'l\.(\d+)', L[i]).group(1))
    rdct = L[i + 1].split()[1:]; de = L[i + 2].split()[1:]; it = L[i + 4][6:]
    mg = L[i + 5].split()[1:]
    i += 7
    if want and ln not in want: continue
    b = rd.get(ln)
    print('=== %s l.%d' % (pg, ln), '| hand(%s): %s' % (b['conf'], b['it']) if b else '')
    if b: print('   hand ct: ' + ' '.join(b['toks']))
    print('   dec it : ' + it)
    row = []
    for j, (t, d, m) in enumerate(zip(rdct, de, mg)):
        s = '%d:%s>%s=%s' % (j + 1, t, d, dec.VAL.get(d, '-')[:12] or '_')
        if float(m) < 2.5:
            c = [k for _, k in model.cands(t)[:5] if k != d][:4]
            s += '{' + ','.join('%s=%s' % (k, dec.VAL[k][:8] or '_') for k in c) + '}'
        row.append(s)
    print('   ' + '  '.join(row))
