# solve_mono.py tx restarts seed : ciphertext-only monoalphabetic anneal, German 4-grams with word boundaries.
# Corpus: b6b9/lm/pg55171.txt (Simplicissimus 1668), md5 and 'Language: German' header asserted.
import sys, re, math, random, hashlib, collections
CF = '/home/claude/en/trackB/b6b9/lm/pg55171.txt'; raw = open(CF, 'rb').read()
assert hashlib.md5(raw).hexdigest() == 'f476bb7446c9c38f858a455d5c91602d', 'corpus md5'
txt = raw.decode('utf-8', 'replace'); assert re.search(r'^Language: German', txt, re.M), 'not German'
a = txt.find('*** START'); b = txt.find('*** END'); assert a > 0 and b > a + 100000
def norm(s):
    s = s.lower().replace('ß', 'ss').replace('ä', 'a').replace('ö', 'o').replace('ü', 'u').replace('ſ', 's')
    return re.sub('[^a-z]', '', s)
words = [norm(w) for w in re.findall(r'\w+', txt[a:b])]; words = [w for w in words if w]
C = '#' + '#'.join(words) + '#'
Q = collections.Counter(C[i:i+4] for i in range(len(C)-3)); T = collections.Counter(C[i:i+3] for i in range(len(C)-2))
TOT = sum(Q.values())
def lp4(g): return math.log10(Q[g] / TOT) if g in Q else math.log10(0.01 / TOT)
LP = {}
def score_str(s):
    t = 0
    for i in range(len(s)-3):
        g = s[i:i+4]
        v = LP.get(g)
        if v is None: v = LP[g] = lp4(g)
        t += v
    return t / (len(s)-3)
def load(fn):
    ws = []
    for l in open(fn):
        if l.startswith('#'): continue
        for w in l.replace('|', ' ').split(): ws.append(re.sub('[^a-z]', '', w.lower()))
    return [w for w in ws if w]
HOMO = len(sys.argv) > 4 and sys.argv[4] == 'homo'
if __name__ == '__main__':
    W = load(sys.argv[1]); ct = '#' + '#'.join(W) + '#'
    syms = sorted(set(ct) - {'#'}); alpha = 'abcdefghiklmnopqrstuwxyz'  # j=i, v=u merged (period German)
    rnd = random.Random(int(sys.argv[3])); best = (-99, None)
    def dec(k): return ''.join(k.get(c, c) for c in ct)
    for r in range(int(sys.argv[2])):
        pl = list(alpha); rnd.shuffle(pl); ext = syms + ['_%d' % i for i in range(len(alpha) - len(syms))] if len(syms) < len(alpha) else syms
        k = dict(zip(ext, pl)); cur = score_str(dec(k)); Tm = 0.6
        for it in range(20000):
            if HOMO and rnd.random() < 0.5:
                x = rnd.choice(syms); old = k[x]; k[x] = rnd.choice(alpha); n = score_str(dec(k))
                if n >= cur or rnd.random() < math.exp((n - cur) / Tm * 50): cur = n
                else: k[x] = old
                Tm = max(0.02, Tm * 0.9997); continue
            x, y = rnd.sample(ext, 2); k[x], k[y] = k[y], k[x]
            n = score_str(dec(k))
            if n >= cur or rnd.random() < math.exp((n - cur) / Tm * 50): cur = n
            else: k[x], k[y] = k[y], k[x]
            Tm = max(0.02, Tm * 0.9997)
        if cur > best[0]: best = (cur, dict(k))
        print(r, round(cur, 4), dec(k)[:120], flush=True)
    print('BEST', round(best[0], 4)); print(' '.join(f'{s}={best[1][s]}' for s in syms)); print(dec(best[1]))
