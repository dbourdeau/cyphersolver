"""shuffle_control.py: shuffled-key controls for both Pentz documents, re-implementing the two original controls exactly
(scripts/original/b106_dec_pentz.py, lines 47-end; scripts/original/b157_shuffle_pz.py). Standard library only.
usage (from the target folder):
  python3 -I scripts/shuffle_control.py vienna SEED CORPUS_DIR        (de_21000 de_2229 de_22367 de_6079, see controls/CORPUS.txt)
  python3 -I scripts/shuffle_control.py glueckstadt SEED PG55171_TXT
Corpora are not in git; controls/CORPUS.txt gives their SHA-256. Each must carry 'Language: German' (asserted).
Vienna: German character 4-gram (add-0.1 smoothing) over the word units decoded with T1/T2; a shuffle permutes the letter
values among the figures of each table (random.sample), 5,000 times.
Glueckstadt: German 4-gram (log10, floor 0.01/total) over the six runs of table-1 figures; a shuffle permutes the decoded
letters among the 23 distinct figure types, 5,000 times.
"""
import sys, re, math, random, hashlib, collections, unicodedata, os

def md5(p): return hashlib.md5(open(p, 'rb').read()).hexdigest()
def sha(p): return hashlib.sha256(open(p, 'rb').read()).hexdigest()
KF = 'key_history/KEY_pentz1636_T1T2.py'
assert md5(KF) == '8306f733e78da38f1f86ac61d6bfd582'
ns = {}; exec(open(KF).read(), ns); T1, T2 = ns['T1'], ns['T2']
doc, seed, src = sys.argv[1], int(sys.argv[2]), sys.argv[3]
N_SHUF = 5000

if doc == 'vienna':
    SHA = {'de_21000.txt': None, 'de_2229.txt': None, 'de_22367.txt': None, 'de_6079.txt': None}
    exp = {l.split('\t')[0]: l.split('\t')[2].strip() for l in open('controls/CORPUS.txt', encoding='utf8') if l.startswith('de_')}
    corp = [os.path.join(src, f) for f in SHA]
    for f in corp: assert sha(f) == exp[os.path.basename(f)], 'corpus sha256 ' + f
    SEG = []
    for l in open('segmentation/vienna_1636-03-26_seg.tsv', encoding='utf8'):
        if l.startswith('#') or l.startswith('n\t'): continue
        n, figs, kind, decl = l.rstrip('\n').split('\t'); SEG.append((figs, kind))
    def dec(a, b):
        return [''.join(({'1': a, '2': b}[k]).get(int(x), '?') if x.isdigit() else '?' for x in s.split()) for s, k in SEG if k in '12']
    def norm(s):
        s = s.lower().replace('ß', 'ss'); s = unicodedata.normalize('NFD', s); s = ''.join(ch for ch in s if unicodedata.category(ch) != 'Mn')
        return re.sub(r'[^a-z]', '', s).replace('v', 'u').replace('j', 'i')
    cs = []
    for f in corp:
        t = open(f, encoding='utf8', errors='replace').read()
        assert re.search(r'^Language: German', t, re.M), f
        i = t.find('*** START'); j = t.find('*** END'); assert 0 < i < j
        cs += [norm(w) for w in re.findall(r"[^\W\d_]+", t[i:j])]
    cs = '#'.join(w for w in cs if w)
    N = 4; cnt = collections.Counter(cs[i:i+N] for i in range(len(cs)-N+1)); ctx = collections.Counter(cs[i:i+N-1] for i in range(len(cs)-N+1))
    def lp(ws):
        s = '#' + '#'.join(w.replace('?', '') for w in ws) + '#'; tot = 0; m = 0
        for i in range(len(s)-N+1):
            g = s[i:i+N]; tot += math.log((cnt.get(g, 0)+0.1)/(ctx.get(g[:-1], 0)+2.7)); m += 1
        return tot/m
    true = lp(dec(T1, T2))
    random.seed(seed); ge = 0; best = -99; X = []
    for _ in range(N_SHUF):
        a = dict(zip(sorted(T1), random.sample(list(T1.values()), len(T1)))); b = dict(zip(sorted(T2), random.sample(list(T2.values()), len(T2))))
        sc = lp(dec(a, b)); best = max(best, sc); ge += sc >= true; X.append(sc)
    X.sort()
    print(f'vienna_1636-03-26; corpus de_21000+de_2229+de_22367+de_6079, chars {len(cs)}; seed {seed}')
    print('true %.4f; shuffles %d; >= true %d; best %.4f; median %.4f' % (true, N_SHUF, ge, best, X[N_SHUF//2]))

elif doc == 'glueckstadt':
    TX = 'transcriptions/glueckstadt_c1630_img2.txt'
    assert md5(TX) == '1e70795fd31a4ee8c1c30dce00354226'
    raw = open(src, 'rb').read(); assert hashlib.md5(raw).hexdigest() == 'f476bb7446c9c38f858a455d5c91602d', 'corpus md5'
    txt = raw.decode('utf-8', 'replace'); assert re.search(r'^Language: German', txt, re.M), 'not German'
    a = txt.find('*** START'); b = txt.find('*** END'); assert a > 0 and b > a + 100000
    def norm(s): s = s.lower().replace('ß', 'ss').replace('ä', 'a').replace('ö', 'o').replace('ü', 'u').replace('ſ', 's'); return re.sub('[^a-z]', '', s).replace('v', 'u').replace('j', 'i')
    body = norm(txt[a:b]); Q = collections.Counter(body[i:i+4] for i in range(len(body)-3)); tot = sum(Q.values()); fl = math.log10(0.01/tot); LP = {k: math.log10(v/tot) for k, v in Q.items()}
    runs = []; cur = []
    for l in open(TX):
        if not l.startswith('L'): continue
        for t in l.split('|')[1].split():
            if t in '.,': continue
            if t.startswith('{'):
                if cur: runs.append(cur); cur = []
                continue
            n = int(t.rstrip('?'))
            if n in T1: cur.append(n)
            else:
                if cur: runs.append(cur); cur = []
    if cur: runs.append(cur)
    types = sorted({x for r in runs for x in r}); base = {k: T1[k] for k in types}
    def score(m):
        sc = 0; n = 0
        for r in runs:
            s = ''.join(m[x] for x in r)
            for i in range(len(s)-3): sc += LP.get(s[i:i+4], fl); n += 1
        return sc/n
    true = score(base); rnd = random.Random(seed); vals = [base[k] for k in types]; X = []
    for i in range(N_SHUF):
        v = vals[:]; rnd.shuffle(v); X.append(score(dict(zip(types, v))))
    X.sort()
    print(f'glueckstadt_c1630_img2; corpus pg55171 {len(body)} letters; runs {len(runs)}; figures {sum(map(len, runs))}; types {len(types)}; seed {seed}')
    print(f'true {true:.4f}; shuffles {N_SHUF}; >= true {sum(x >= true for x in X)}; best {X[-1]:.4f}; median {X[N_SHUF//2]:.4f}')
else:
    sys.exit('doc must be vienna or glueckstadt')
