import collections
c = collections.Counter(); w = collections.Counter(); tot = 0
for l in open('align1887.txt', encoding='utf8'):
    if l.startswith('#') or '|' not in l: continue
    t, lit, rd, st = [x.strip() for x in l.split('|')]
    n = len(t.split()); c[st] += n; w[st] += 1; tot += n
print('tokens', tot, dict(c)); print('words', dict(w))
sense = c['ok'] + c['emend']
print('sense (ok+emend) %.1f%%; ok only %.1f%%; with conj %.1f%%; open+null %d' % (100*sense/tot, 100*c['ok']/tot, 100*(sense+c['conj'])/tot, c['open']+c['null']))
