"""Control for the crib fit: fit each text of texts_reread.txt onto the tokens of a different line (same page
order, shifted by K lines across the whole letter) and count tokens 'read' (outside gaps, channel >= THR).
Compare with the true-line fits."""
import sys, os, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('ALPHA', '0.4'); os.environ.setdefault('BETA', '0.4'); os.environ.setdefault('CLEN', '0.3')
import dec, fit, refit
model = refit.model
items = []
for l in open('texts_reread.txt', encoding='utf8'):
    m = re.match(r'\s*(f3\d[rv])\s+l\.(\d+)\s*\|\s*(\w+)\s*\|(.*)$', l)
    if m: items.append((m.group(1), int(m.group(2)), m.group(4).strip()))
alll = [(pg, ln, toks) for pg in dec.PAGES for ln, toks in dec.load_ct(pg)]
pos = {(pg, ln): i for i, (pg, ln, _) in enumerate(alll)}
def count(toks, text):
    s, out = fit.fit(toks, refit.clean_it(text), model)
    if s is None: return 0, len(toks), None
    return sum(1 for k, lc, gp in out if k and not gp and lc >= refit.THR), len(toks), s
for K in [0] + [int(x) for x in (sys.argv[1:] or ['5', '11'])]:
    r = n = nofit = 0
    for pg, ln, text in items:
        toks = alll[(pos[(pg, ln)] + K) % len(alll)][2]
        a, b, s = count(toks, text)
        r += a; n += b; nofit += s is None
    print('shift %2d: read %d of %d tokens (%.1f%%), no fit %d of %d lines' % (K, r, n, 100 * r / n, nofit, len(items)))

if os.environ.get('PERLINE'):
    import statistics
    shifts = list(range(3, 63, 4))
    print('per line (THR %g): true read / tokens, control mean max over %d shifts' % (refit.THR, len(shifts)))
    for pg, ln, text in items:
        toks = alll[pos[(pg, ln)]][2]
        a, b, s = count(toks, text)
        cs = []
        for K in shifts:
            t2 = alll[(pos[(pg, ln)] + K) % len(alll)][2]
            cs.append(count(t2, text)[0])
        flag = 'WEAK' if a < max(cs) + 3 else ''
        print('%s l.%d  %2d/%2d  ctl mean %.1f max %d %s | %s' % (pg, ln, a, b, statistics.mean(cs), max(cs), flag, text))
