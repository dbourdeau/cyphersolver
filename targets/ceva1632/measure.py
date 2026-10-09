"""fraction_read for R75/R84: tokens excluding separator 6 and 2x nulls;
unread = 3-digit nomenclator elements without a value in cipher.NOMEN, and '?' noise digits.
Usage: python measure.py [suffix]   (default '2' -> r75.tokens2.json)"""
import sys, os, json, collections
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import cipher
suf = sys.argv[1] if len(sys.argv) > 1 else '2'
T = U = 0; open_codes = collections.Counter()
for tag in ('r75', 'r84'):
    tot = un = 0
    for l in json.load(open(os.path.join(HERE, '%s.tokens%s.json' % (tag, suf)))):
        for t in l:
            if t == '6' or t in cipher.NULLS: continue
            tot += 1
            if t.startswith('?'): un += 1; open_codes['?'] += 1
            elif t.startswith('#') and t[1:] not in cipher.NOMEN: un += 1; open_codes[t[1:]] += 1
    print('%s: tokens %d unread %d read %.3f' % (tag, tot, un, 1 - un / tot))
    T += tot; U += un
print('overall: tokens %d unread %d read %.3f' % (T, U, 1 - U / T))
print('open:', open_codes.most_common())
