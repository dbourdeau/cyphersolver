# shuffle_lasa.py key tx n seed : guarded German 4-gram baseline (Simplicissimus 1668, md5 + 'Language: German' header asserted).
# true = mean log10 joint quadgram prob over decoded cipher words joined with '#'; shuffle = random permutation of plaintext values
# among the cipher letter types present in tx. Reports shuffles >= true.
import sys, hashlib, random
sys.path.insert(0, '/home/claude/en/trackB/b160_hunt_north/scripts')
import solve_mono as S
kf, tf, n, seed = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4])
print('key md5', hashlib.md5(open(kf, 'rb').read()).hexdigest(), 'tx md5', hashlib.md5(open(tf, 'rb').read()).hexdigest())
k = {}
for l in open(kf):
    if l.startswith('#'): continue
    for p in l.split(): a, b = p.split('='); k[a] = b
W = S.load(tf); ct = '#' + '#'.join(W) + '#'
allt = sorted(set(ct) - {'#'}); unk = [t for t in allt if t not in k]; print('types not in key (decode as ?):', unk)
for t in unk: k[t] = '?'
types = [t for t in allt if t not in unk]
def sc(m): return S.score_str(''.join(m.get(c, c) for c in ct))
true = sc(k); rnd = random.Random(seed); vals = [k[t] for t in types]; X = []
for i in range(n):
    v = vals[:]; rnd.shuffle(v); X.append(sc(dict(zip(types, v))))
X.sort()
print(f'corpus Simplicissimus {len(S.C)} chars; words {len(W)}; letters {len(ct)-ct.count("#")}; types {len(types)}')
print(f'seed {seed}: true {true:.4f}; shuffles {n}; >= true {sum(x >= true for x in X)}; best {X[-1]:.4f}; median {X[n//2]:.4f}')
