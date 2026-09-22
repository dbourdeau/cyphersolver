"""Count tokens.txt: read / sense open / unread / code, per page and in total.
Usage: python count_tokens.py [tokens.txt] [--lines]"""
import sys
fn = next((a for a in sys.argv[1:] if not a.startswith('--')), 'tokens.txt')
pages = {}
per_line = []
for ln in open(fn, encoding='utf8'):
    if ln.startswith('#') or not ln.strip():
        continue
    name, *toks = ln.split()
    c = dict(read=0, open=0, unread=0, code=0)
    for t in toks:
        v = t.split('=', 1)[1]
        if v.startswith('['): c['code'] += 1
        elif v == '?': c['unread'] += 1
        elif v.endswith('?'): c['open'] += 1
        else: c['read'] += 1
    per_line.append((name, len(toks), c))
    pg = 'recto r01-r15' if name[0] == 'r' and int(name[1:]) <= 15 else 'recto r16-r30' if name[0] == 'r' else 'verso v01-v09'
    p = pages.setdefault(pg, dict(total=0, read=0, open=0, unread=0, code=0))
    p['total'] += len(toks)
    for k in c: p[k] += c[k]
if '--lines' in sys.argv:
    for n, t, c in per_line:
        print(n, t, c)
tot = dict(total=0, read=0, open=0, unread=0, code=0)
for pg, p in pages.items():
    print(f"{pg:15s} {p}")
    for k in tot: tot[k] += p[k]
print(f"{'total':15s} {tot}")
print(f"read as sense: {tot['read']}/{tot['total']} = {100*tot['read']/tot['total']:.1f}%")
