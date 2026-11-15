import json, gzip, random, sys
base = sys.argv[1]
K = json.load(open(base + '/key_frozen.json'))['key']
lex = json.load(gzip.open(sys.argv[2], 'rt'))
words = set(w.lower() for w in (lex if isinstance(lex, list) else lex.keys()))
words |= {'ye', 'yt', 'newbury', 'kimball', 'molly', 'bartletts', 'furlough'}
toks = [w for l in open(base + '/heldout_glyphs.txt') if not l.startswith('#') for w in l.split()]
toks = [t for t in toks if len(t) >= 2]
def dec(t, k):
    return ''.join(k.get(c, '?') for c in t)
def share(k):
    return sum(dec(t, k) in words for t in toks) / len(toks)
s0 = share(K)
rnd = random.Random(1779); g = list(K.keys()); v = list(K.values()); sh = []
for _ in range(200):
    rnd.shuffle(v); sh.append(share(dict(zip(g, v))))
sh.sort()
print('words', len(toks), 'frozen share %.3f' % s0, 'shuffled max %.3f p99 %.3f mean %.3f' % (sh[-1], sh[197], sum(sh) / 200))
for t in toks:
    d = dec(t, K)
    if d not in words: print('  not in lexicon:', t, '->', d)
