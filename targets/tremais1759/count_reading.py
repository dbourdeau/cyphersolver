"""Count the cipher words of reading.md: sure (bold), conjectural (*[..?]*), unread runs ([ ... ]).
Unread runs carry no word count; they are estimated from the groups left over at the rate of the read words."""
import re, io, sys, csv
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
t = open('reading.md', encoding='utf-8').read()
G = {'f.346r': 248, 'f.346v': 457, 'f.347r': 535, 'f.347v': 37}
W = r"[A-Za-zÀ-ÿ]{2,}"
tb = tc = th = 0
for s in re.split(r'\n## ', t)[1:]:
    name = s.split('\n')[0]; body = s[len(name):]
    body = re.sub(r'Marginal note.*?(\n\n|$)', '', body, flags=re.S)
    conj = re.findall(r'\*\[([^\]]*)\]\*', body); body2 = re.sub(r'\*\[[^\]]*\]\*', '', body)
    wb = sum(len(re.findall(W, b)) for b in re.findall(r'\*\*(.+?)\*\*', body2, flags=re.S))
    wc = sum(max(1, len(re.findall(W, c))) for c in conj)
    h = body.count('[ … ]')
    print(f'{name}: sure {wb}, conjectural {wc}, unread runs {h}, groups {G[name]}')
    tb += wb; tc += wc; th += h
print(f'total: sure {tb}, conjectural {tc}, unread runs {th}')
open_groups = 0
for f in ('retry_346rv.tsv', 'retry_347rv.tsv'):
    for r in csv.DictReader(open(f, encoding='utf-8'), delimiter='\t'):
        if r['grade'].strip() == 'open':
            open_groups += len(re.findall(r'\d[\d\[\]]*', r['numbers_as_read']))
est_open = round(open_groups / 2.9)
print(f'groups in places graded open by the retry: {open_groups} (about {est_open} words at 2.9 groups a word)')
tot = tb + tc + est_open
print(f'estimated cipher words {tot}; sure share {tb/tot:.3f}; with conjectural {(tb+tc)/tot:.3f}')
