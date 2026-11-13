"""Guarded German character 4-gram shuffled-key control (own code, standard library; same method as run b179 shuffle_hb.py).
usage: python3 -I shuffle_control.py <key.tsv> <key_md5> <transcription.txt> <corpus.txt> <n> <seed>
Corpus: Project Gutenberg #55171 (Grimmelshausen, Simplicissimus, 1668), plain-text UTF-8; md5, 'Language: German' and the
body length are asserted (controls/CORPUS.txt). Text between unvalued tokens forms separate runs; only valued tokens are scored.
Shuffle: the decoded values are permuted at random among the distinct valued cipher-token types of the passage; the score is the
mean log10 4-gram probability per scored 4-gram. Reported: how many shuffled keys score at or above the true key.
What it tests: whether the key's letter/syllable assignment reads more like German than the same values put on the wrong signs.
What it does not test: whether any word-code value is right (see controls/word_layer.txt), nor which German is meant."""
import sys, re, math, random, hashlib, collections
kf, kmd5, tf, cf, n, seed = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], int(sys.argv[5]), int(sys.argv[6])
assert hashlib.md5(open(kf, 'rb').read()).hexdigest() == kmd5, 'key md5'
raw = open(cf, 'rb').read()
assert hashlib.md5(raw).hexdigest() == 'f476bb7446c9c38f858a455d5c91602d', 'corpus md5'
txt = raw.decode('utf-8', 'replace'); assert re.search(r'^Language: German', txt, re.M), 'not German'
a = txt.find('*** START'); b = txt.find('*** END'); assert a > 0 and b > a + 100000, 'no body'
def norm(s):
    s = s.lower().replace('ß', 'ss').replace('ä', 'a').replace('ö', 'o').replace('ü', 'u').replace('ſ', 's'); return re.sub('[^a-z]', '', s)
body = norm(txt[a:b]); assert len(body) > 200000
Q = collections.Counter(body[i:i + 4] for i in range(len(body) - 3)); tot = sum(Q.values()); fl = math.log10(0.01 / tot)
LP = {k: math.log10(v / tot) for k, v in Q.items()}
K = {}
for l in open(kf, encoding='utf-8'):
    p = l.rstrip('\n').split('\t')
    if p[0] == 'tok': K[p[1]] = p[2]
print('tx md5', hashlib.md5(open(tf, 'rb').read()).hexdigest())
toks = [t for l in open(tf, encoding='utf-8') if l.strip() and not re.search(r'[a-z]{4,}', l) for t in l.split()]
runs = []; cur = []
for t in toks:
    if t not in K:
        if cur: runs.append(cur); cur = []
        continue
    cur.append(t)
if cur: runs.append(cur)
types = sorted({t for r in runs for t in r})
def score(m):
    sc = 0; k = 0
    for r in runs:
        st = norm(''.join(m[t] for t in r))
        for i in range(len(st) - 3): sc += LP.get(st[i:i + 4], fl); k += 1
    return sc / k
base = {t: K[t] for t in types}; true = score(base); rnd = random.Random(seed); vals = [base[t] for t in types]; X = []
for i in range(n):
    v = vals[:]; rnd.shuffle(v); X.append(score(dict(zip(types, v))))
X.sort()
print(f'corpus pg55171 {len(body)} letters; tokens {len(toks)}; runs {len(runs)}; valued tokens {sum(map(len, runs))}; distinct types {len(types)}')
print(f'seed {seed}: true {true:.4f}; shuffles {len(X)}; >= true {sum(x >= true for x in X)}; best {X[-1]:.4f}; median {X[len(X) // 2]:.4f}')
