"""shuffle_control.py CORPUS KEY TX N SEED : guarded German 4-gram shuffled-key control (same arithmetic as
scripts/original/shuffle_lasa.py, b160, with the corpus path as an argument instead of an import).
Corpus: Grimmelshausen, Simplicissimus (1668), Project Gutenberg #55171, md5 f476bb74... and 'Language: German' asserted.
true = mean log10 quadgram probability over the decoded cipher words joined with '#'; each shuffled key is a random
permutation of the key's plaintext values among the cipher letter types present in the transcription.
What it tests: that the frozen key gives German letter statistics far beyond chance on this text. What it does not test:
whether any word is read correctly (that is the strict count), or the reader's transcription."""
import sys, re, math, random, hashlib, collections
cf, kf, tf, n, seed = sys.argv[1], sys.argv[2], sys.argv[3], int(sys.argv[4]), int(sys.argv[5])
raw = open(cf, 'rb').read(); assert hashlib.md5(raw).hexdigest() == 'f476bb7446c9c38f858a455d5c91602d', 'corpus md5'
txt = raw.decode('utf-8', 'replace'); assert re.search(r'^Language: German', txt, re.M), 'not German'
a = txt.find('*** START'); b = txt.find('*** END'); assert a > 0 and b > a + 100000
def norm(s):
    s = s.lower().replace('ß', 'ss').replace('ä', 'a').replace('ö', 'o').replace('ü', 'u').replace('ſ', 's')
    return re.sub('[^a-z]', '', s)
words = [w for w in (norm(w) for w in re.findall(r'\w+', txt[a:b])) if w]
C = '#' + '#'.join(words) + '#'; Q = collections.Counter(C[i:i+4] for i in range(len(C)-3)); TOT = sum(Q.values()); LP = {}
def score_str(s):
    t = 0
    for i in range(len(s)-3):
        g = s[i:i+4]; v = LP.get(g)
        if v is None: v = LP[g] = math.log10(Q[g] / TOT) if g in Q else math.log10(0.01 / TOT)
        t += v
    return t / (len(s)-3)
def load(fn):
    ws = []
    for l in open(fn):
        if l.startswith('#'): continue
        for w in l.replace('|', ' ').split(): ws.append(re.sub('[^a-z]', '', w.lower()))
    return [w for w in ws if w]
print('key md5', hashlib.md5(open(kf, 'rb').read()).hexdigest(), 'tx md5', hashlib.md5(open(tf, 'rb').read()).hexdigest())
k = {}
for l in open(kf):
    if l.startswith('#'): continue
    for p in l.split(): x, y = p.split('='); k[x] = y
W = load(tf); ct = '#' + '#'.join(W) + '#'
allt = sorted(set(ct) - {'#'}); unk = [t for t in allt if t not in k]; print('types not in key (decode as ?):', unk)
for t in unk: k[t] = '?'
types = [t for t in allt if t not in unk]
def sc(m): return score_str(''.join(m.get(c, c) for c in ct))
true = sc(k); rnd = random.Random(seed); vals = [k[t] for t in types]; X = []
for i in range(n):
    v = vals[:]; rnd.shuffle(v); X.append(sc(dict(zip(types, v))))
X.sort()
print(f'corpus Simplicissimus {len(C)} chars; words {len(W)}; letters {len(ct)-ct.count("#")}; types {len(types)}')
print(f'seed {seed}: true {true:.4f}; shuffles {n}; >= true {sum(x >= true for x in X)}; best {X[-1]:.4f}; median {X[n//2]:.4f}')
