# shuffle_control.py CORPUS1 CORPUS2 ... > controls.txt   (run from the target folder; standard library only; python3 -I)
# Shuffled-key control: for each job (transcription or pool of transcriptions, key, seeds), the spelled values of the key
# (letters and syllables of tier A or B, three letters or fewer) used in the text are shuffled among the tokens that carry them,
# 5,000 times per seed, and each decode is scored by a French character 4-gram model. Code words, unknown tokens and tier C values
# are breaks ('#') and are never scored or shuffled. Reported: the true score, how many shuffles score at or above it, the best and
# the median shuffle. Logic and arithmetic are those of the contributor's shuffle_b146.py / decode_v2.py (b94, b146), unchanged;
# only the job loop is new, so that the model is built once.
#
# Corpus: Project Gutenberg French texts 4650, 13951, 17489, 5097 (plain-text UTF-8 files as downloaded, with their headers).
# Guard (b146): every corpus file must declare 'Language: French' in its header and hold more than 100,000 characters between
# its START and END markers, or the run stops. The corpus is not in this folder (about 7 MB); give the four file paths.
# Pools are the listed transcriptions read one after another, in the order given (the order of the pooled files of the record).
import sys, re, math, random, unicodedata, collections, json, os, hashlib

F = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def P(*a): return os.path.join(F, *a)

corpus = sys.argv[1:]
assert len(corpus) > 0, 'NO CORPUS GIVEN'
for f in corpus:
    h = open(f, encoding='utf8', errors='replace').read(20000)
    assert 'Language: French' in h, 'CORPUS NOT FRENCH OR NO HEADER: ' + f
    t = open(f, encoding='utf8', errors='replace').read()
    assert '*** START' in t and '*** END' in t and t.find('*** END') - t.find('*** START') > 100000, 'EMPTY/SHORT CORPUS: ' + f

def norm(s):
    s = unicodedata.normalize('NFD', s.lower()); return re.sub(r'[^a-z]', '', ''.join(ch for ch in s if unicodedata.category(ch) != 'Mn'))
corp = ''
for f in corpus:
    t = open(f, encoding='utf8', errors='replace').read()
    i = t.find('*** START'); j = t.find('*** END'); corp += ' ' + t[i:j]
cs = '#'.join(norm(w) for w in re.findall(r"[^\W\d_]+", corp))
N = 4
cnt = collections.Counter(cs[i:i + N] for i in range(len(cs) - N + 1)); ctx = collections.Counter(cs[i:i + N - 1] for i in range(len(cs) - N + 1))
def lp(s):
    tot = 0; n = 0
    for i in range(len(s) - N + 1):
        g = s[i:i + N]; tot += math.log((cnt.get(g, 0) + 0.1) / (ctx.get(g[:-1], 0) + 0.1 * 27)); n += 1
    return tot / max(n, 1)

def load_key(path):
    key = {}
    for l in open(path, encoding='utf8'):
        if l.startswith('#') or not l.strip(): continue
        p = l.rstrip('\n').split('\t'); key[p[0]] = (p[1], p[2])
    return key
def load_lines(paths):
    lines = []
    for path in paths:
        for l in open(path, encoding='utf8'):
            if l.startswith('#') or '|' not in l: continue
            lid, body = l.rstrip('\n').split('|', 1); lines.append((lid, body))
    return lines

def control(txs, keyf, seed, n=5000):
    key = load_key(keyf); lines = load_lines(txs)
    runs = [[t.strip() for t in r.split('.') if t.strip()] for lid, b in lines for r in re.findall(r'<([^>]*)>', b)]
    def stream(k):
        out = []
        for r in runs:
            for t in r:
                if t in k and k[t][1] in 'AB' and len(norm(k[t][0])) <= 3: out.append(norm(k[t][0]))
                else: out.append('#')
            out.append('#')
        return ''.join(out)
    true = lp(stream(key))
    used = sorted({t for r in runs for t in r if t in key and key[t][1] in 'AB' and len(norm(key[t][0])) <= 3})
    vals = [key[t] for t in used]
    random.seed(seed); ge = 0; best = -1e9; sc = []
    for i in range(n):
        v = vals[:]; random.shuffle(v); k = dict(key)
        for t, x in zip(used, v): k[t] = x
        s = lp(stream(k)); sc.append(s)
        if s >= true: ge += 1
        best = max(best, s)
    sc.sort()
    return {'true_score': round(true, 4), 'shuffles': n, 'shuffles_ge_true': ge, 'best_shuffle': round(best, 4), 'median_shuffle': round(sc[n // 2], 4), 'tokens_used_in_shuffle': len(used), 'seed': seed}

T = lambda *ids: [P('transcriptions', i + '.txt') for i in ids]
K3 = P('key.tsv')
FIVE = ['petkum_1665-04-28', 'petkum_1665-06-23', 'petkum_1665-09-17', 'petkum_1666-01-18', 'petkum_1666-04-06']
JOBS = [
 ('A1 30 Nov 1665 R1 p2-3 (573), key v1 as filed', T('petkum_1665-11-30_p2-3_R1'), P('gloss', 'KEY_v1_gloss_377_401.tsv')),
 ('A1 30 Nov 1665 R1 p1+p4 held out, key v2 as filed', T('petkum_1665-11-30_p1-p4_R1_heldout'), P('gloss', 'KEY_v2.tsv')),
 ('A2 30 Nov 1665 R2 blind, all four pages, KEY_v3', T('petkum_1665-11-30_R2_blind_keynames'), K3),
 ('B 24 Mar 1665', T('petkum_1665-03-24'), K3), ('B 23 Nov 1665', T('petkum_1665-11-23'), K3),
 ('B 10 Dec 1665', T('petkum_1665-12-10'), K3), ('B 13 Apr 1666', T('petkum_1666-04-13'), K3),
] + [('C ' + i[7:], T(i), K3) for i in FIVE] + [
 ('C pool of five (first reader)', T(*FIVE), K3),
 ('D pool of five (blind reader)', T(*[i + '_blind' for i in FIVE]), K3),
 ('E 25 Apr 1664 (Paulmyer)', T('paulmyer_1664-04-25'), K3), ('E 2 May 1664', T('paulmyer_1664-05-02'), K3),
 ('E 16 May 1664', T('paulmyer_1664-05-16'), K3), ('E 19 Jun 1664', T('paulmyer_1664-06-19'), K3),
 ('E3 pool 2 May + 16 May + 19 Jun', T('paulmyer_1664-05-02', 'paulmyer_1664-05-16', 'paulmyer_1664-06-19'), K3),
 ('E4 pool 2 May + 16 May + 19 Jun + 25 Apr', T('paulmyer_1664-05-02', 'paulmyer_1664-05-16', 'paulmyer_1664-06-19', 'paulmyer_1664-04-25'), K3),
]
only = os.environ.get('ONLY')  # optional: run only jobs whose label contains this text
print('controls.txt: written by scripts/shuffle_control.py (python3 -I). Char 4-gram, add-0.1, %d corpus files, %d letters; corpus md5: %s'
      % (len(corpus), len(cs), ', '.join(os.path.basename(f) + ' ' + hashlib.md5(open(f, 'rb').read()).hexdigest()[:8] for f in corpus)))
print('label\tseed\ttrue\tge_true/shuffles\tbest\tmedian\tspelled tokens shuffled')
for label, txs, kf in JOBS:
    if only and only not in label: continue
    for seed in (20261112, 7):
        r = control(txs, kf, seed)
        print('%s\t%d\t%.4f\t%d/%d\t%.4f\t%.4f\t%d' % (label, seed, r['true_score'], r['shuffles_ge_true'], r['shuffles'], r['best_shuffle'], r['median_shuffle'], r['tokens_used_in_shuffle']), flush=True)
