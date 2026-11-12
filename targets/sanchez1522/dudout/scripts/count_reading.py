"""count_reading.py READING : per-page and total S/P/P†/R/I counts of a reading in the lot-1/lot-2 markup."""
import sys, re, collections
tot = collections.Counter(); pages = collections.OrderedDict()
for line in open(sys.argv[1], encoding='utf-8'):
    if line.startswith('#') or not line.strip(): continue
    ref, txt = line.split(' ', 1); page = ref.split('.')[0]
    txt = re.sub(r'«[^»]*»?', ' ', txt); txt = re.sub(r'^[^«]*»', ' ', txt) if '»' in txt else txt
    c = pages.setdefault(page, collections.Counter())
    for m in re.finditer(r'\{[^}]*\}|\[[^\]]*\]|<[^>]*>|[^\s{}\[\]<>]+', txt):
        w = m.group(0)
        if w.endswith('-'): continue                    # split word, counted where it ends
        k = 'P+' if w.startswith('{') and '†' in w else 'P' if w.startswith('{') else 'R' if w.startswith('[') else 'I' if w.startswith('<') else 'S'
        c[k] += 1; tot[k] += 1
def row(n, c):
    W = sum(c.values()); sp = c['S'] + c['P'] + c['P+']; strict = c['S'] + c['P']
    print('%-8s S %4d  P %3d  P† %3d  R %2d  I %3d  words %4d  read %.1f %%  strict %.1f %%' % (n, c['S'], c['P'], c['P+'], c['R'], c['I'], W, 100*sp/W, 100*strict/W))
for p, c in pages.items(): row(p, c)
row('letter', tot)
