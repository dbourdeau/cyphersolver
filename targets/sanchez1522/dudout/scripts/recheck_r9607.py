"""recheck_r9607.py R9607_SIGNS LEXICON_CORPUS KEY_CODES_TSV EXTRA_WORDS : declared re-check of C02's R9607 letter runs (PREREG_lot2.md §3).
For each maximal run of single-sign tokens (between code groups / clear words / nulls) of the frozen lot-1 transcription,
enumerate the declared alternatives (table ALT; adjacent 'm' 'o' may also be read 'h'), and segment each candidate string
into lexicon words. Report per run the segmentations with the fewest words; a run is 'unique' iff exactly one candidate
string reaches that minimum. Lexicon = words seen >= 2 times in the corpus + EXTRA_WORDS (one per line), normalised
u->v, j->i, y->i, accents dropped. Output only; any change to a reading is then applied by hand, with sense, as P."""
import sys, re, itertools, unicodedata, collections
ALT = {'n':'a','Z':'asc','b':'b','z':'c','4':'e','y':'e','3':'de','oo':'d','P':'fs','L':'g','X':'h','x':'h','mo':'h',
       'ai':'i','9':'l','B':'mr','&':'n','t4':'n','#':'o','ao':'p','tt':'pn','g':'ri','Q':'s','q':'st','Yo':'st','Lo':'t',
       'm':'v','o':'x','xo':'s','A':'z'}
NULLS = {'ll','#t','#o','|'}
def norm(s):
    s = unicodedata.normalize('NFD', s.lower()); s = ''.join(c for c in s if unicodedata.category(c) != 'Mn')
    return re.sub('[^a-z]', '', s.replace('ñ','n').replace('u','v').replace('j','i').replace('y','i'))
def lexicon(corpus, extra):
    raw = open(corpus, encoding='utf-8').read(); a = raw.find('*** START'); b = raw.find('*** END')
    raw = raw[a:b] if a >= 0 and b > a else raw
    c = collections.Counter(norm(w) for w in re.findall(r"[A-Za-zÁÉÍÓÚáéíóúñÑüÜ]+", raw))
    L = {w for w, n in c.items() if n >= 2 and (len(w) >= 2 or w in ('a','e','o','i'))}
    for w in open(extra, encoding='utf-8'): 
        w = norm(w.strip())
        if w: L.add(w)
    return L
def segs(s, L, memo):
    if s in memo: return memo[s]
    if not s: return [[]]
    best = None
    for i in range(1, min(len(s), 18) + 1):
        if s[:i] in L:
            for rest in segs(s[i:], L, memo):
                cand = [s[:i]] + rest
                if best is None or len(cand) < len(best[0]): best = [cand]
                elif len(cand) == len(best[0]) and cand not in best: best.append(cand)
    memo[s] = best or []
    return memo[s]
def main():
    L = lexicon(sys.argv[2], sys.argv[4]); K = set()
    for line in open(sys.argv[3], encoding='utf-8').read().splitlines()[1:]:
        if '\t' in line: K.add(line.split('\t')[0].rstrip('?'))
    for line in open(sys.argv[1], encoding='utf-8'):
        if line.startswith('#') or not line.strip(): continue
        f = line.split(); ref, toks = f[0], [t.rstrip('?') for t in f[1:]]
        runs, cur = [], []
        for t in toks + ['|']:
            if t in ALT: cur.append(t)
            else:
                if cur: runs.append(cur)
                cur = []
        for r in runs:
            opts = []
            i = 0
            while i < len(r):                        # m + o may be read as the single sign mo = h
                if r[i] == 'm' and i + 1 < len(r) and r[i+1] == 'o': opts.append(['v'+'x', 'h']); i += 2
                else: opts.append(list(ALT[r[i]])); i += 1
            n = 1
            for o in opts: n *= len(o)
            if n > 4096: print(ref, ' '.join(r), '=> TOO MANY (%d)' % n); continue
            results = []
            for combo in itertools.product(*opts):
                s = ''.join(combo); sg = segs(s, L, {})
                if sg: results.append((len(sg[0]), s, sg))
            if not results: print(ref, ' '.join(r), '=> none'); continue
            m = min(x[0] for x in results); top = [x for x in results if x[0] == m]
            tag = 'UNIQUE' if len(top) == 1 and len(top[0][2]) == 1 else 'ambiguous(%d)' % sum(len(x[2]) for x in top)
            print(ref, ' '.join(r), '=>', tag, ' | '.join(' '.join(sg) for x in top[:4] for sg in x[2][:2]))
if __name__ == '__main__': main()
