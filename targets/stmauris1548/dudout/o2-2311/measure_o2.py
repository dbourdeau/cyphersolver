"""measure_o2.py (PREREG-O2.md, 23 Nov 2026) - ONE measure of WAINUT's stmauris1548 table on the 1547 letter, c. 1r.
usage: python3 measure_o2.py TRANSCRIPTION KEY_TSV CORPUS [seed]
TRANSCRIPTION: blind sign names (SIGNS.md), rows '1r L01: ...' (parsed by WAINUT's compare.load: quotes, '.', '/', '(' dropped,
'?' stripped). KEY_TSV: sign<TAB>value ('-' = null), comment lines start with '# '. Signs absent from the key give no letter
and break word coverage. M = share of decoded letters covered by a max-coverage segmentation into lexicon words of 3-15
letters; lexicon = word types of CORPUS (fr-1520s-diplomatic), normalised like the decode (accents off, j->i, v->u, k->c,
w dropped). Controls: 200 tables with the values permuted among the signs of the key (as WAINUT's heldout.py).
PASS iff decoded letters >= 300 AND M >= 0.85 AND M >= max(controls) + 0.30."""
import sys, os, re, random, unicodedata
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'wainut-scripts'))
from compare import load
def norm(s):
    s = unicodedata.normalize('NFD', s.lower()); s = ''.join(c for c in s if not unicodedata.combining(c))
    return re.sub('[^a-z]', '', s.replace('j', 'i').replace('v', 'u').replace('k', 'c').replace('w', ''))
def lexicon(path):
    t = open(path, encoding='utf-8', errors='ignore').read()
    return {w for w in (norm(x) for x in re.findall(r"[^\W\d_]+", t)) if 3 <= len(w) <= 15}
def key(path):
    K = {}
    for l in open(path, encoding='utf-8'):
        if not l.strip() or l.startswith('# '): continue
        p = l.rstrip('\n').split('\t')
        if len(p) >= 2: K[p[0]] = '' if p[1] == '-' else norm(p[1])
    return K
def decode(toks, K):
    return ''.join(K[t] if t in K else '|' for t in toks)
def coverage(s, lex):
    tot = 0; cov = 0
    for seg in s.split('|'):
        n = len(seg); tot += n
        if not n: continue
        best = [0] * (n + 1)
        for i in range(1, n + 1):
            b = best[i - 1]
            for L in range(3, min(15, i) + 1):
                if seg[i - L:i] in lex and best[i - L] + L > b: b = best[i - L] + L
            best[i] = b
        cov += best[n]
    return (cov / tot if tot else 0.0), tot
def main():
    tr, kp, cp = sys.argv[1:4]; seed = int(sys.argv[4]) if len(sys.argv) > 4 else 1547
    rows = load(tr); toks = [t for r in rows.values() for t in r]; K = key(kp); lex = lexicon(cp)
    s = decode(toks, K); M, n = coverage(s, lex)
    signs = sorted(K); vals = [K[x] for x in signs]; rng = random.Random(seed); ctrl = []
    for _ in range(200):
        v = vals[:]; rng.shuffle(v); ctrl.append(coverage(decode(toks, dict(zip(signs, v))), lex)[0])
    known = sum(1 for t in toks if t in K)
    print('rows %d tokens %d with a key value %d (%.1f%%) decoded letters %d lexicon %d types' % (len(rows), len(toks), known, 100*known/max(1, len(toks)), n, len(lex)))
    print('M %.4f  controls n=200 max %.4f mean %.4f  margin %.4f' % (M, max(ctrl), sum(ctrl)/200, M - max(ctrl)))
    ok = n >= 300 and M >= 0.85 and M >= max(ctrl) + 0.30
    print('VERDICT', 'PASS' if ok else ('NOT MEASURABLE (<300 letters)' if n < 300 else 'FAIL'))
    for k, r in rows.items(): print('%s %s: %s' % (k[0], k[1], ''.join(K.get(t, '?') for t in r)))
if __name__ == '__main__': main()
