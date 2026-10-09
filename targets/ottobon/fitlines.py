"""Show the crib fit of each text in a texts file (lines 'page l.N | conf | text'), optionally only one page."""
import sys, os, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('ALPHA', '0.4'); os.environ.setdefault('BETA', '0.4'); os.environ.setdefault('CLEN', '0.3')
import dec, fit, refit
sys.stdout.reconfigure(encoding='utf-8')
model = refit.model
only = sys.argv[2:]
for l in open(sys.argv[1], encoding='utf8'):
    m = re.match(r'\s*(f3\d[rv])\s+l\.(\d+)\s*\|\s*(\w+)\s*\|(.*)$', l)
    if not m: continue
    pg, ln, conf, text = m.group(1), int(m.group(2)), m.group(3), m.group(4).strip()
    if only and pg not in only and '%s:%d' % (pg, ln) not in only: continue
    toks = dict(dec.load_ct(pg))[ln]
    print('== %s l.%d [%s] %s' % (pg, ln, conf, text))
    s, out = fit.fit(toks, refit.clean_it(text), model)
    if s is None: print('   NO FIT'); continue
    bad = sum(1 for k, lc, gp in out if k is None or gp or lc < refit.THR)
    print('   %d/%d read; ' % (len(toks) - bad, len(toks)) + '  '.join('%s>%s%s(%.0f)' % (t, (dec.VAL[k] or '_').replace(' ', '~') if k else '-', '~' if gp else '', lc) for t, (k, lc, gp) in zip(toks, out)))
