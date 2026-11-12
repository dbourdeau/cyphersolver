"""PREREG measure for sanchez-1522 (see ../PREREG.md). Frozen before decoding.
usage: measure.py TRANSCRIPTION KEY_CODES_TSV CORPUS [seed]
Decodes a shape-label transcription with Daniel's key (key_codes.tsv, unchanged) and the sign map SIGNS below
(taken from alpha.py + R9593_signs.txt legend + NOTES, origin/main 62b62c5b5), scores it with a 4-gram character
model (no spaces) trained on CORPUS, and compares with 400 controls."""
import sys, re, math, random, unicodedata, collections
SIGNS = {'n':'a','Z':'a','b':'b','z':'c','4':'e','y':'e','3':'d','oo':'d','P':'f','L':'g','X':'h','x':'h',
         'ai':'i','9':'l','B':'m','&':'n','t4':'n','#':'o','ao':'p','tt':'p','g':'r','Q':'s','q':'s','Yo':'s',
         'm':'v','o':'x','A':'z','Lo':'t'}
NULLS = {'ll', '#t', '#o', '|'}
def clean(s):
    s = unicodedata.normalize('NFD', s.lower()); s = ''.join(c for c in s if unicodedata.category(c) != 'Mn')
    s = s.replace('ñ', 'n').replace('ç', 'c')
    return re.sub('[^a-z]', '', s.replace('u', 'v').replace('j', 'i').replace('y', 'i'))
def load_key(path):
    K = {}
    for line in open(path, encoding='utf-8').read().splitlines()[1:]:
        c, p = line.split('\t'); p = re.sub(r' *\[.*?\]', '', p)
        p = p.split('/')[0]
        K[c.rstrip('?')] = re.sub(r'\(.*?\)', '', p).replace('?', '')
    return K
def tokens(path):
    out = []
    for line in open(path, encoding='utf-8'):
        line = line.split('#', 1)[0] if line.startswith('#') else line
        if not line.strip(): continue
        for t in line.split()[1:]:
            if t.startswith('=') or t in NULLS or t.startswith('['): continue
            out.append(t.rstrip('?'))
    return out
def decode(toks, K, S):
    out = []; unk = 0
    for t in toks:
        if t in S: out.append(S[t])
        elif t in K: out.append(clean(K[t]))
        else: unk += 1
    return ''.join(out), unk
class LM:
    def __init__(self, text, n=4, k=0.1):
        self.n = n; self.k = k; self.c = collections.Counter(); self.h = collections.Counter()
        for i in range(len(text) - n + 1):
            g = text[i:i+n]; self.c[g] += 1; self.h[g[:-1]] += 1
        self.V = len(set(text))
    def per_char(self, s):
        if len(s) < self.n: return float('-inf')
        tot = 0.0
        for i in range(len(s) - self.n + 1):
            g = s[i:i+self.n]; tot += math.log((self.c[g] + self.k) / (self.h[g[:-1]] + self.k*self.V))
        return tot / (len(s) - self.n + 1)
def main():
    tr, kp, cp = sys.argv[1:4]; seed = int(sys.argv[4]) if len(sys.argv) > 4 else 20261112
    raw = open(cp, encoding='utf-8').read()
    a = raw.find('*** START'); b = raw.find('*** END'); raw = raw[a:b] if a >= 0 and b > a else raw
    lm = LM(clean(raw))
    K = load_key(kp); toks = tokens(tr)
    real, unk = decode(toks, K, SIGNS); s_real = lm.per_char(real)
    rng = random.Random(seed); ctrl = []
    codes = list(K); plains = [K[c] for c in codes]; sl = list(SIGNS); sv = [SIGNS[x] for x in sl]
    for i in range(200):                       # C1: permuted key (codes among codes, signs among signs)
        p = plains[:]; rng.shuffle(p); v = sv[:]; rng.shuffle(v)
        d, _ = decode(toks, dict(zip(codes, p)), dict(zip(sl, v))); ctrl.append(lm.per_char(d))
    for i in range(200):                       # C2: true key, token order shuffled
        t = toks[:]; rng.shuffle(t); d, _ = decode(t, K, SIGNS); ctrl.append(lm.per_char(d))
    mu = sum(ctrl)/len(ctrl); sd = (sum((x-mu)**2 for x in ctrl)/len(ctrl))**.5
    z = (s_real - mu)/sd; mx = max(ctrl)
    print('decoded_chars', len(real), 'tokens', len(toks), 'unknown_codes', unk)
    print('S_real %.4f  controls n=%d mean %.4f sd %.4f max %.4f  z %.2f' % (s_real, len(ctrl), mu, sd, mx, z))
    print('max C1 %.4f  max C2 %.4f' % (max(ctrl[:200]), max(ctrl[200:])))
    ok = len(real) >= 300 and s_real > mx and z >= 5
    print('VERDICT', 'PASS' if ok else 'FAIL'); print('decoded:', real)
if __name__ == '__main__': main()
