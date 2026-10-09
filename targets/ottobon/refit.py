"""Re-fit hand-read lines: for each rd block, fit the first-pass tokens to its Italian ('it:') with fit.fit and
count tokens read (outside gaps, channel log-prob >= THR). Reports per page; with --texts <file> uses the texts
there (lines 'page l.N | conf | text') instead of the rd 'it:' lines; with --write rewrites rd_<page>.txt blocks."""
import sys, os, re, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('ALPHA', '0.4'); os.environ.setdefault('BETA', '0.4'); os.environ.setdefault('CLEN', '0.3')
import dec, fit
sys.stdout.reconfigure(encoding='utf-8')
THR = float(os.environ.get('THR', -8))
model = dec.Model(dec.PAGES)
def clean_it(it):
    it = it.replace('…', '...')
    it = re.sub(r'\[\.\.\.\]|\.\.\.', ' ... ', it)
    it = re.sub(r'\?', '', it)
    it = re.sub(r"[,;:.!()'’-]", ' ', it.replace('...', '\x01')).replace('\x01', '...')
    return it
def run(page, texts=None, write=False, verbose=False):
    ctl = dict(dec.load_ct(page))
    rd = dec.load_rd(page)
    tot = rd_old = rd_new = 0; blocks = []
    for b in rd:
        ln = b['line']; toks = ctl.get(ln)
        conf = b['conf']; it = b['it']
        if texts and (page, ln) in texts: conf, it = texts[(page, ln)]
        n_old = sum('?' not in t for t in b['toks']) if b['conf'] in ('high', 'medium') else 0
        if toks is None or (texts is not None and (page, ln) not in texts):
            blocks.append(None); tot += len(b['toks']); rd_old += n_old; rd_new += n_old; continue
        s, out = fit.fit(toks, clean_it(it), model) if it.strip() else (None, [])
        if s is None:
            codes = b['toks']; read = n_old if conf in ('high', 'medium') else 0
        else:
            codes = []
            for t, (k, lc, gp) in zip(toks, out):
                if k is None: codes.append(t.rstrip('?') + '?')
                elif gp or lc < THR: codes.append(k + '?')
                else: codes.append(k)
            read = sum('?' not in c for c in codes) if conf in ('high', 'medium') else 0
        if read < n_old:          # never lose a hand-read token: keep the earlier block
            tot += len(toks); rd_old += n_old; rd_new += n_old; blocks.append(None)
            if verbose: print('%s l.%d kept hand block (fit %d < hand %d)' % (page, ln, read, n_old))
            continue
        tot += len(toks); rd_old += n_old; rd_new += read
        if verbose: print('%s l.%d %s old %d new %d  %s' % (page, ln, conf, n_old, read, it))
        blocks.append((ln, codes, conf, it, s is not None))
    if write:
        f = open('rd_%s.txt' % page, 'w', encoding='utf8')
        f.write('# %s reading, re-fitted %s by refit.py (fit.py crib fit of the Italian onto the first-pass tokens;\n' % (page, '2026-10-09'))
        f.write("# '?' = token in a gap, or channel log-prob < %g). Earlier hand pass in rd_hand1/.\n" % THR)
        for b, x in zip(rd, blocks):
            if x is None:
                f.write(b['raw']); continue
            ln, codes, conf, it, ok = x
            vals = ' '.join((dec.VAL.get(c.rstrip('?'), '?') or '_').replace(' ', '~') + ('?' if '?' in c else '') for c in codes)
            f.write('# f.%s l.%d\nct:  %s\nrd:  %s\nit:  %s\nconf: %s\n' % (page[1:], ln, ' '.join(codes), vals, it, conf))
        f.close()
    return tot, rd_old, rd_new
if __name__ == '__main__':
    args = sys.argv[1:]; texts = None; write = '--write' in args; verbose = '-v' in args
    if '--texts' in args:
        tf = args[args.index('--texts') + 1]; texts = {}
        for l in open(tf, encoding='utf8'):
            m = re.match(r'\s*(f3\d[rv])\s+l\.(\d+)\s*\|\s*(\w+)\s*\|(.*)$', l)
            if m: texts[(m.group(1), int(m.group(2)))] = (m.group(3).lower(), m.group(4).strip())
    pages = [a for a in args if re.match(r'f3\d[rv]$', a)] or dec.PAGES
    T = [0, 0, 0]
    for pg in pages:
        r = run(pg, texts, write, verbose)
        print('%s tokens %d read before %d after %d' % (pg, *r))
        T = [a + b for a, b in zip(T, r)]
    print('ALL tokens %d read before %d (%.1f%%) after %d (%.1f%%)' % (T[0], T[1], 100 * T[1] / T[0], T[2], 100 * T[2] / T[0]))
