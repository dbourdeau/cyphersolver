# run_controls.py: shuffled-key controls for despatches/. Standard library only.
#   python3 -I despatches/scripts/run_controls.py SWEDISH_CORPUS_DIR FRENCH_CORPUS_DIR  > writes controls/shuffle.txt
# Model and test as ../despatch1677/scripts/shuffle_control.py and the session scripts (shuffle_sv.py, shuffle_fr.py):
#   character 4-gram model, add-0.01 smoothing, Project Gutenberg texts between the START and END marks, accents stripped,
#   letters only, w folded to v for Swedish; every corpus file must carry 'Language: Swedish' / 'Language: French' or the
#   script stops. Only letter values (tiers of the row, without H) are scored; a clear word, a cut numeral, a word code or a
#   number with no value ends a run. 5,000 keys made by shuffling the same values over the same numbers (random.Random(seed));
#   reported: how many score >= the true key. Rows with a line range (327R, lines 4-10) use those lines only.
# Tests: every first-pass page (seed 20261112); every despatch's first pass pooled per key state and every second
#   transcription pooled (seeds 20261112 and 7). Re-scores are not tested (not held-out).
import os, sys, re, math, random, collections, unicodedata, glob

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = lambda *a: os.path.join(HERE, *a)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build  # same folder: torfmt, rlines, load_key

def model(corpus, lang):
    fold = lang == 'Swedish'
    def norm(t):
        t = unicodedata.normalize('NFD', t.lower()); t = ''.join(c for c in t if unicodedata.category(c) != 'Mn')
        t = re.sub(r'[^a-z]+', ' ', t)
        return t.replace('w', 'v') if fold else t
    txt = ''
    paths = sorted(glob.glob(os.path.join(corpus, '*.txt'))); assert paths, 'no corpus files in ' + corpus
    for f in paths:
        raw = open(f, encoding='utf-8', errors='replace').read()
        assert re.search(r'^Language: %s' % lang, raw, re.M), f
        a = raw.find('*** START'); b = raw.find('*** END'); txt += norm(raw[a:b]).replace(' ', '') + ' '
    cnt = collections.Counter(); ctx = collections.Counter()
    for w in txt.split():
        for i in range(len(w) - 3): cnt[w[i:i + 4]] += 1; ctx[w[i:i + 3]] += 1
    return norm, cnt, ctx

def test(name, rows, mdl, seeds):
    norm, cnt, ctx = mdl
    r0 = rows[0]; tiers = r0['tiers'].replace('H', '')
    key = {g: norm(s).strip() for g, (s, t) in build.load_key(os.path.normpath(P(r0['keyfile']))).items() if t in tiers}
    runs = []
    for r in rows:
        text = open(P(r['despatch'], r['transcription']), encoding='utf-8').read()
        if r['rformat'] == 'torfmt': text = build.torfmt(text)[0]
        for _, body in build.rlines(text, r['lines']):
            cur = []
            for part in re.findall(r'"[^"]*"|\S+', body):
                g = re.sub(r'[^0-9]', '', part)
                if part.startswith('"') or part.endswith('~') or g not in key:
                    if cur: runs.append(cur)
                    cur = []
                else: cur.append(g)
            if cur: runs.append(cur)
    def score(s):
        t = 0.0
        for i in range(len(s) - 3): t += math.log((cnt[s[i:i + 4]] + 0.01) / (ctx[s[i:i + 3]] + 0.26))
        return t, max(len(s) - 3, 0)
    def total(k):
        t = 0; n = 0
        for rr in runs:
            a, b = score(''.join(k[g] for g in rr)); t += a; n += b
        return t / n
    types = sorted({g for rr in runs for g in rr}); vals = [key[g] for g in types]; true = total(key); out = []
    for seed in seeds:
        rnd = random.Random(seed); ge = 0; res = []
        for i in range(5000):
            v = vals[:]; rnd.shuffle(v); s = total(dict(zip(types, v))); res.append(s); ge += (s >= true)
        res.sort()
        line = '%s: runs %d tokens %d types %d true %.4f shuffles>=true %d of 5000 best %.4f median %.4f seed %d%s' % (
            name, len(runs), sum(len(rr) for rr in runs), len(types), true, ge, res[-1], res[2500], seed, '   FAILED (shuffles >= true)' if ge else '')
        out.append(line); print(line, flush=True)
    return out

def main():
    sv = model(sys.argv[1], 'Swedish'); fr = model(sys.argv[2], 'French')
    cols = None; rows = []
    for l in open(P('manifest.tsv'), encoding='utf-8'):
        if l.startswith('#'): continue
        f = l.rstrip('\n').split('\t')
        if cols is None: cols = f; continue
        rows.append(dict(zip(cols, f)))
    out = ['# Shuffled-key controls, 5,000 keys each (scripts/run_controls.py). Character 4-gram models: Swedish and French corpora of controls/CORPUS.txt.',
           '# A line marked FAILED means shuffled keys scored as well as the true key: the test does not support the reading of that text.']
    for d in dict.fromkeys(r['despatch'] for r in rows):
        out.append(''); out.append('## ' + d)
        ds = [r for r in rows if r['despatch'] == d]
        for r in [r for r in ds if r['role'] == 'first']:
            out += test('[page] %s key %s' % (r['page'], r['key']), [r], fr if r['lang'] == 'fr' else sv, [20261112])
        for k in dict.fromkeys(r['key'] for r in ds if r['role'] == 'first'):
            g = [r for r in ds if r['role'] == 'first' and r['key'] == k]
            out += test('[first pass pooled, key %s] %s' % (k, '+'.join(r['page'] for r in g)), g, fr if g[0]['lang'] == 'fr' else sv, [20261112, 7])
        g = [r for r in ds if r['role'] == 'second']
        if g: out += test('[second transcription pooled, key %s] %s' % (g[0]['key'], '+'.join(r['page'] for r in g)), g, sv, [20261112, 7])
    open(P('controls', 'shuffle.txt'), 'w', encoding='utf-8').write('\n'.join(out) + '\n')

if __name__ == '__main__':
    main()
