"""Stricter held-out figure: only groups whose reference is a whole word carried by one group (the independent check's classification, written 14 Nov 2026 by a second AI agent;
by line and position in the first agent's holdout/no262_transcription.txt). Also lists table support for each hit."""
import re, csv, random, os
B = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
tab = {r['group']: r for r in csv.DictReader(open(B + '/key/table_frozen_v1.tsv'), delimiter='\t')}
W = {'H01': '718 1213 1537 925 777 436 229 994 770', 'H02': '1533 1533 994 441 240 994 69 556 994 240 1304',
     'H03': '436 458 1409 1053 561 179 716', 'H04': '532 1537 1300 756 240 223 492 506', 'H05': '1537 1396 492 506 1518 565',
     'H06': '330 492 920 1213 556 677 1250 1333 994 815 517 556', 'H07': '925 1072 240 677 565 994 506 1409 1213',
     'H08': '1053 1231 996 716 855 532 925 1145', 'H09': '240 994 240 994 240', 'H10': '1042 330 641'}
items = []
for line in open(B + '/test/no262_transcription.txt'):
    m = re.match(r'(H\d+):\s*(.*)', line.strip())
    if not m: continue
    want = W[m.group(1)].split()
    for tok in m.group(2).split():
        g, v = tok.split('=', 1)
        if '?' in g or v.endswith('#') or v == '?': continue
        if g in want: want.remove(g); items.append((g, v.lower()))
    assert not want, (m.group(1), want)
def sc(t): return sum(1 for g, v in items if g in t and t[g] == v)
t0 = {g: r['value'].lower() for g, r in tab.items()}
hit = sc(t0); cov = sum(1 for g, v in items if g in t0)
gs, vs = list(t0), list(t0.values()); sh = []
for s in range(1, 201):
    random.seed(s); v2 = vs[:]; random.shuffle(v2); sh.append(sc(dict(zip(gs, v2))))
print(f'whole-word single-group items: {len(items)}; hits {hit} ({hit/len(items):.3f}); coverage {cov}; precision {hit/cov:.3f}; shuffled max {max(sh)} mean {sum(sh)/len(sh):.2f}')
weak = [(g, v, tab[g]['n_rows'], tab[g]['n_gloss']) for g, v in items if g in tab and t0[g] == v and int(tab[g]['n_rows']) <= 1]
print('hits resting on a single table row:', weak)
nog = [(g, v, tab[g]['n_rows']) for g, v in items if g in tab and t0[g] == v and tab[g]['n_gloss'] == '0']
print('hits whose table value has no clerk-gloss row (print-aligned only):', nog)
