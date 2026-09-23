"""Count signs in a *_signs.txt file: letters = read, '.' = null, '?' = unread, '#' = code sign read from a gloss,
'N' = numeral. Usage: python stats.py R4232_signs.txt"""
import sys, collections
c = collections.Counter()
for line in open(sys.argv[1], encoding='utf-8'):
    if not line.strip() or line.startswith('#'): continue
    body = line.split(None, 1)[1].strip()
    for ch in body:
        if ch.islower(): c['read'] += 1
        elif ch == '.': c['null'] += 1
        elif ch == '?': c['unread'] += 1
        elif ch == '#': c['code_gloss'] += 1
        elif ch == 'N': c['numeral'] += 1
        elif ch == ' ': pass
        else: c['other:' + ch] += 1
tot = sum(v for k, v in c.items())
sig = tot - c['null']
print(dict(c), 'total signs', tot)
print('read (letters + glossed code + numeral) / non-null signs: %.1f%%' % (100 * (c['read'] + c['code_gloss'] + c['numeral']) / sig))
print('read incl. nulls as read / all signs: %.1f%%' % (100 * (tot - c['unread']) / tot))
