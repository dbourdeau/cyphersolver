"""Word-layer control for the nomenclator's whole-word codes (own code, standard library).
usage: python3 -I word_control.py <folder> <n> <seed> [<seed> ...]
1. Word codes: a key code counts as a WORD code when at least one gloss pair writes a whole gloss word over that code alone
   and the code's key value spells that word (case, umlauts and ß folded). Built separately from the v1 and v2 gloss files.
2. Evidence per value: every attestation (image, side, line strip, gloss word) of each word code that occurs in the 537L passage.
3. Held-out test: on the held-out pages (342R with v1, 413 with v2), each glossed group whose FIRST token is a word code is
   checked: does the folded gloss begin with the folded value? True count = groups that agree.
4. Shuffle: the values are permuted at random among all word codes of the key (the key's own word inventory) and the
   held-out test is re-scored; reported = shuffles reaching the true count. This tests whether the word values that recur
   on held-out pages are right as assigned, against the same inventory put on the wrong numbers. It does not test word codes
   that never recur on a held-out page, and the 537L passage itself has no gloss, so no word code in it is tested there."""
import sys, re, random, pathlib, collections
F = pathlib.Path(sys.argv[1]); n = int(sys.argv[2]); seeds = [int(x) for x in sys.argv[3:]]
def fold(s):
    s = s.lower()
    for a, b in (('ä', 'a'), ('ö', 'o'), ('ü', 'u'), ('ß', 'ss'), ('ſ', 's')): s = s.replace(a, b)
    return re.sub('[^a-z]', '', s)
def key(p):
    K = {}
    for l in open(p, encoding='utf-8'):
        q = l.rstrip('\n').split('\t')
        if q[0] == 'tok': K[q[1]] = q[2]
    return K
def pairs(p): return [l.rstrip('\n').split('\t') for l in open(p, encoding='utf-8') if l.strip() and not l.startswith('#')]
def words(K, P):
    W = {}; ev = collections.defaultdict(list)
    for img, toks, gl, seg in P:
        if ',' not in toks and toks in K and fold(re.sub(r'\(.*?\)', '', gl)) == fold(K[toks]): W[toks] = K[toks]
    for img, toks, gl, seg in P:
        for t in toks.split(','):
            if t in W: ev[t].append('%s "%s"' % (img, gl))
    return W, ev
K1 = key(F / 'gloss/KEY_HB_v1.tsv'); K2 = key(F / 'gloss/KEY_HB_v2.tsv')
W1, E1 = words(K1, pairs(F / 'gloss/gloss_pairs_v1_b179.tsv')); W2, E2 = words(K2, pairs(F / 'gloss/gloss_pairs_v2_all.tsv'))
print('1. word codes: v1 %d, v2 %d' % (len(W1), len(W2)))
print('   v2 word codes:', ', '.join('%s=%s' % (k, v) for k, v in sorted(W2.items(), key=lambda x: (not x[0].isdigit(), int(x[0]) if x[0].isdigit() else 0))))
tx = [t for l in open(F / 'transcriptions/heespen_1676-04-17_537L.txt', encoding='utf-8') if l.strip() and not re.search(r'[a-z]{4,}', l) for t in l.split()]
print('2. word codes in the 537L passage (evidence per value):')
for name, W, E in (('v1 (figure of record)', W1, E1), ('v2 (non-blind)', W2, E2)):
    hit = collections.Counter(t for t in tx if t in W)
    print('   %s: %s' % (name, ', '.join('%s=%s x%d' % (t, W[t], c) for t, c in hit.items()) or 'none'))
    for t in hit: print('      %s=%s: %d attestations: %s' % (t, W[t], len(E[t]), '; '.join(E[t])))
def held(page):
    p = F / ('heldout/342R_glosses.tsv' if page == '342R' else 'heldout/413_transcription_glosses.tsv')
    return [(l.split('\t')[0].split(), l.rstrip('\n').split('\t')[1]) for l in open(p, encoding='utf-8') if l.strip() and not l.startswith('#')]
tests = []
for page, W in (('342R', W1), ('413', W2)):
    for tk, gl in held(page):
        if tk[0] in W: tests.append((page, tk[0], gl, W))
def score(assign): return sum(fold(gl).startswith(fold(assign[p][c])) for p, c, gl, W in tests)
true_assign = {'342R': W1, '413': W2}
tv = score(true_assign)
print('3. held-out groups opening with a word code: %d' % len(tests))
for p, c, gl, W in tests: print('   %s %s=%s gloss "%s": %s' % (p, c, W[c], gl, 'agrees' if fold(gl).startswith(fold(W[c])) else 'DISAGREES'))
print('   true: %d of %d agree' % (tv, len(tests)))
for s in seeds:
    rnd = random.Random(s); X = []
    for i in range(n):
        A = {}
        for p, W in (('342R', W1), ('413', W2)):
            ks = sorted(W); vs = [W[k] for k in ks]; rnd.shuffle(vs); A[p] = dict(zip(ks, vs))
        X.append(score(A))
    print('4. seed %d: %d shuffles of the word inventory; >= true (%d): %d; best %d; mean %.3f' % (s, n, tv, sum(x >= tv for x in X), max(X), sum(X) / n))
