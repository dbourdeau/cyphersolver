"""Single held-out measure of key v7 (PR #699, Malcolm McBratney) on fresh glossed leaves of unit 261267.

Usage: python3 -I measure_v7.py KEY.tsv FINAL.tsv  -> JSON on stdout.
Rules fixed in PREREG.md (frozen by SHA-256 before any transcription):
- FINAL.tsv rows: image<TAB>line<TAB>tokens (space separated)<TAB>gloss ; gloss '-' = no gloss over the run (excluded).
- token cleaning: trailing '~' dropped; '?', '?x?', '{...}' -> no value; '[struck ...]' dropped.
- value of a token = key row value; variants = text outside parentheses, and text inside parentheses when present.
- abbreviations expanded the same way for values and glosses (expand()), then a-z only (accents dropped, i/j/y, u/v not merged).
- per glossed run, the variant combination nearest the gloss is chosen (product capped at 64; tokens past the cap use variant 1);
  P = concatenation of chosen decodes, R = concatenation of glosses; score = 1 - Levenshtein(P, R) / max(|P|, |R|).
- 200 controls: the value bundles of all key rows permuted among the key's tokens (random.Random(seed), seeds 1..200), same procedure.
- pass bar: score >= 0.85 AND score >= best control + 0.30.
- strict count (reported): a glossed run is SURE when every token has a value whose tier is not C and does not end in '?',
  and its chosen decode equals the normalized gloss. Also given per gloss word (gloss split on spaces, runs of one word only).
"""
import sys, re, json, random, unicodedata, itertools

def expand(s):
    s = ' ' + s + ' '
    reps = [(r'\bV\.\s*M\.?(?=\W)', ' votre majeste '), (r'\bS\.\s*M\.?(?=\W)', ' sa majeste '),
            (r'\bV\.\s*Ma?\.?\s*te\b', ' votre majeste '), (r'\bT\.\s*C\.?(?=\W)', ' tres chrestien '),
            (r'\bMrs\b\.?', ' messieurs '), (r'\bMessrs\b\.?', ' messieurs '), (r'\bMr\b\.?', ' monsieur '),
            (r'\bChancr\b\.?', ' chancelier '), (r'\bChanc\.', ' chancelier '), (r'\bAngl\.', ' angleterre '),
            (r'\bVre\b\.?', ' votre '), (r'\bV\.(?=\s)', ' votre '), (r'\bMa\.?\s*te\b', ' majeste '),
            (r'\bMate\b', ' majeste '), (r'\bMté\b', ' majeste '), (r'\bM\.(?=\s)', ' monsieur ')]
    for a, b in reps:
        s = re.sub(a, b, s)
    return s

def norm(s):
    s = unicodedata.normalize('NFD', expand(s).lower())
    return re.sub('[^a-z]', '', s)

def load_key(path):
    k = {}
    for l in open(path, encoding='utf8'):
        if l.startswith('#') or not l.strip():
            continue
        p = l.rstrip('\n').split('\t')
        v = p[1]
        m = re.match(r'^(.*?)\s*\((.*)\)\s*$', v)
        var = [norm(m.group(1)), norm(m.group(2))] if m else [norm(v)]
        var = [x for x in var if x] or ['']
        k[p[0]] = (var, p[2] if len(p) > 2 else '')
    return k

def clean(tok):
    if tok.startswith('[struck'):
        return None
    tok = tok.rstrip('~')
    if not tok or '?' in tok or tok.startswith('{'):
        return ''
    return tok

def load_runs(path):
    runs = []
    for l in open(path, encoding='utf8'):
        if l.startswith('#') or not l.strip() or l.startswith('image\t'):
            continue
        p = l.rstrip('\n').split('\t')
        img, line, toks, gl = p[0], p[1], p[2], p[3] if len(p) > 3 else '-'
        if gl.strip() in ('-', ''):
            continue
        # struck groups are written '[struck 204]' and may contain a space: join them first
        toks = re.sub(r'\[struck[^\]]*\]', '', toks)
        tt = [c for c in (clean(t) for t in toks.split()) if c is not None]
        runs.append((img, line, tt, gl))
    return runs

def lev(a, b):
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i]
        for j, cb in enumerate(b, 1):
            cur.append(min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (ca != cb)))
        prev = cur
    return prev[-1]

def dec_run(tt, k, ref):
    opts = [k[t][0] if t in k else [''] for t in tt]
    n = 1
    lim = []
    for o in opts:
        if n * len(o) <= 64:
            lim.append(o); n *= len(o)
        else:
            lim.append(o[:1])
    best = None
    for combo in itertools.product(*lim):
        p = ''.join(combo)
        d = lev(p, ref)
        if best is None or d < best[0]:
            best = (d, p)
    return best[1]

def run_all(runs, k):
    P, R, segs = [], [], []
    for img, line, tt, gl in runs:
        ref = norm(gl)
        p = dec_run(tt, k, ref)
        P.append(p); R.append(ref); segs.append((img, line, tt, gl, p, ref))
    P, R = ''.join(P), ''.join(R)
    return 1 - lev(P, R) / max(len(P), len(R), 1), segs, len(P), len(R)

def main():
    k = load_key(sys.argv[1])
    runs = load_runs(sys.argv[2])
    s, segs, lp, lr = run_all(runs, k)
    keys = list(k)
    vals = [k[x] for x in keys]
    wit = []
    for seed in range(1, 201):
        r = random.Random(seed)
        v = vals[:]
        r.shuffle(v)
        wit.append(run_all(runs, dict(zip(keys, v)))[0])
    best = max(wit)
    def solid(t):
        return t in k and not k[t][1].endswith('?') and k[t][1] != 'C'
    sure = [x for x in segs if all(solid(t) for t in x[2]) and x[4] == x[5]]
    one = [x for x in segs if len(x[3].split()) == 1]
    sure1 = [x for x in one if x in sure]
    out = {'glossed_runs': len(segs), 'tokens': sum(len(x[2]) for x in segs), 'len_P': lp, 'len_R': lr,
           'score_char': round(s, 4), 'best_control': round(best, 4), 'mean_control': round(sum(wit) / 200, 4),
           'controls_at_or_above': sum(1 for w in wit if w >= s), 'margin': round(s - best, 4),
           'bar': 'score >= 0.85 and >= best control + 0.30', 'pass': s >= 0.85 and s >= best + 0.30,
           'strict_sure_runs': '%d/%d' % (len(sure), len(segs)),
           'strict_sure_one_word_runs': '%d/%d' % (len(sure1), len(one)),
           'unknown_tokens': sorted({t for x in segs for t in x[2] if t not in k})}
    print(json.dumps(out, ensure_ascii=False, indent=1))
    if len(sys.argv) > 3:
        with open(sys.argv[3], 'w', encoding='utf8') as f:
            f.write('# image\tline\ttokens\tgloss\tdecode_v7\tgloss_norm\tmatch\n')
            for img, line, tt, gl, p, ref in segs:
                f.write('\t'.join([img, line, '.'.join(tt), gl, p, ref, 'Y' if p == ref else 'N']) + '\n')

if __name__ == '__main__':
    main()
