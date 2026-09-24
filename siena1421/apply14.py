import sys
key = dict(kv.split('=') for kv in open(sys.argv[2], encoding='utf-8').read().split())
words = open(sys.argv[1], encoding='utf-8').read().split()
out = []
for w in words:
    out.append(''.join(key.get(s, '[' + s + ']') for s in w.split('_')))
print(' '.join(out))
if len(sys.argv) > 3:
    for w in words: print('%-40s %s' % (w, ''.join(key.get(s, '[' + s + ']') for s in w.split('_'))))
