"""Check every row of texts/R912_fills_2026-11-12.tsv: the groups stand in that order on the named tr/ line(s), and the
R639 values column is what decode_tr.py gives for them. usage: python check_fills.py <target folder>"""
import sys, re, csv, importlib.util, pathlib
T = pathlib.Path(sys.argv[1])
s = importlib.util.spec_from_file_location('d', T / 'decode_tr.py'); d = importlib.util.module_from_spec(s); sys.argv = ['x']; s.loader.exec_module(d)
def lines(page):
    return [re.sub(r'[^\d ]', ' ', l.replace('-', ' ')).split() for l in (T / 'tr' / f'R912_{page}.txt').read_text(encoding='utf-8').splitlines()
            if l.strip() and not l.startswith('#')]
bad = 0
for r in csv.DictReader(open(T / 'texts' / 'R912_fills_2026-11-12.tsv', encoding='utf-8'), delimiter='\t'):
    a, _, b = r['line'].partition('-'); a = int(a); b = int(b or a)
    L = lines(r['page']); run = [g for l in L[a - 1:b] for g in l if d.key.get(g, 'x') != '']  # nulls (97-119) skipped
    gs = r['groups'].split(); ok = any(run[i:i + len(gs)] == gs for i in range(len(run)))
    vals = ' '.join(d.key.get(g) or f'[{g}]' for g in gs if d.key.get(g, 'x') != '')
    vok = vals == r['R639 values']
    bad += not (ok and vok)
    print('ok ' if ok and vok else 'BAD', r['page'], r['line'], r['groups'], '|', vals, '' if vok else f"(tsv: {r['R639 values']})")
print('all rows hold' if not bad else f'{bad} rows fail'); sys.exit(bool(bad))
