# shuffle_control.py: shuffled-key control. Standard library only.
#   python3 -I scripts/shuffle_control.py KEY TIERS CORPUS_DIR LANGUAGE SEED TRANSCRIPTION [TRANSCRIPTION ...]
# Same model and scoring as the original scripts (scripts/original/b101_shuffle3.py; the Swedish variant differs only in
# its corpus, its language header and w folded to v):
#   - character 4-gram model, add-0.01 smoothing, trained on every *.txt in CORPUS_DIR between the Project Gutenberg
#     START and END marks, accents stripped, letters only, word breaks kept as run breaks;
#   - GUARD: every corpus file must carry the header 'Language: <LANGUAGE>' or the script stops;
#   - only key values of the given TIERS are scored; a clear word, a cut numeral or a number outside those tiers ends a run;
#   - the true key's mean log-probability per 4-gram is compared with 5,000 keys made by shuffling the same values over
#     the same numbers (random.Random(SEED)); the count of shuffled keys scoring >= the true key is reported.
# Several transcriptions are pooled into one test.
import sys, re, math, random, collections, unicodedata, glob, os

keyf, tiers, corpus, lang, seed = sys.argv[1:6]
files = sys.argv[6:]
fold_w = lang == 'Swedish'

def norm(t):
    t = unicodedata.normalize('NFD', t.lower()); t = ''.join(c for c in t if unicodedata.category(c) != 'Mn')
    t = re.sub(r'[^a-z]+', ' ', t)
    return t.replace('w', 'v') if fold_w else t

txt = ''
paths = sorted(glob.glob(os.path.join(corpus, '*.txt')))
assert paths, 'no corpus files'
for f in paths:
    raw = open(f, encoding='utf-8', errors='replace').read()
    assert re.search(r'^Language: %s' % lang, raw, re.M), f
    a = raw.find('*** START'); b = raw.find('*** END'); txt += norm(raw[a:b]).replace(' ', '') + ' '
N = 4; cnt = collections.Counter(); ctx = collections.Counter()
for w in txt.split():
    for i in range(len(w) - N + 1): cnt[w[i:i+N]] += 1; ctx[w[i:i+N-1]] += 1

def score(s):
    if len(s) < N: return 0.0, 0
    t = 0
    for i in range(len(s) - N + 1): t += math.log((cnt[s[i:i+N]] + 0.01) / (ctx[s[i:i+N-1]] + 0.26))
    return t, len(s) - N + 1

key = {}
for l in open(keyf, encoding='utf-8'):
    if l.startswith('#') or not l.strip(): continue
    g, s, t = l.rstrip('\n').split('\t')
    if t in tiers: key[g] = norm(s).strip()
runs = []
for fn in files:
    for l in open(fn, encoding='utf-8'):
        m = re.match(r'R\d+:\s*(.*)', l)
        if not m: continue
        cur = []
        for part in re.findall(r'"[^"]*"|\S+', m.group(1)):
            g = re.sub(r'[^0-9]', '', part)
            if part.startswith('"') or part.endswith('~') or g not in key:
                if cur: runs.append(cur)
                cur = []
            else: cur.append(g)
        if cur: runs.append(cur)

def total(k):
    t = 0; n = 0
    for r in runs:
        a, b = score(''.join(k[g] for g in r)); t += a; n += b
    return t / n

types = sorted({g for r in runs for g in r}); vals = [key[g] for g in types]
true = total(key); rnd = random.Random(int(seed)); ge = 0; res = []
for i in range(5000):
    v = vals[:]; rnd.shuffle(v); s = total(dict(zip(types, v))); res.append(s); ge += (s >= true)
res.sort()
print('%s: runs %d tokens %d types %d true %.4f shuffles>=true %d of 5000 best %.4f median %.4f seed %s' % (
    '+'.join(os.path.basename(f)[:-4] for f in files), len(runs), sum(len(r) for r in runs), len(types), true, ge, res[-1], res[2500], seed))
