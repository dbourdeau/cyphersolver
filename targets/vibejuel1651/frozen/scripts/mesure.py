"""Mesure unique (PROTOCOLE.md).
M1 (principal) : log-prob moyenne par caractère (modèle lm.py ordre 4 construit sur corpus/) du texte déchiffré (mots chiffrés seuls, séparés par une espace).
M2 (secondaire) : part des mots chiffrés de >= 4 lettres présents dans lexique.txt.
Contrôles (graine 20261111, 200 tirages chacun) : (A) table d'ouvreurs mélangée (k au hasard 0..3 par valeur d'ouvreur) ;
(B) k au hasard 0..3 par mot ; (C) alphabet du corps permuté (table vraie).
usage : python3 mesure.py corpus/ lexique.txt transcription.txt (modèle reconstruit à l'identique depuis corpus/, SHA figés)"""
import sys, re, random, pickle, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vdec, lm
def words(txt):
    ws = []; carry = None
    for line in txt.splitlines():
        if line.startswith('#') or not line.strip(): continue
        for tok in re.findall(r'\[[^\]]*\]|\S+', line):
            if tok.startswith('[') or tok.startswith('C'): continue
            hy = tok.endswith('='); nums = [int(x) for x in tok.rstrip('=').split('.') if x.isdigit()]
            if carry is not None: nums = carry + nums; carry = None
            if hy: carry = nums; continue
            if len(nums) >= 2: ws.append(nums)
    return ws
def dec(nums, k, A):
    if k is None: return 'x' * (len(nums) - 1)
    out = []
    for n in nums[1:]:
        if 32 <= n <= 34: n -= 31
        i = n - 1 - k
        out.append(A[i] if 0 <= i < 23 else 'x')
    return ''.join(out)
def run(ws, kf, A, M, lex):
    d = [dec(w, kf(w), A) for w in ws]
    m1 = M.per_char(' '.join(d))
    long = [x for x in d if len(x) >= 4]
    m2 = sum(1 for x in long if x in lex) / max(1, len(long))
    return m1, m2
if __name__ == '__main__':
    import glob; M = lm.build(sorted(glob.glob(sys.argv[1] + '/*.txt'))); lex = set(open(sys.argv[2]).read().split())
    ws = words(open(sys.argv[3]).read()); A = vdec.A
    t1, t2 = run(ws, lambda w: vdec.kof(w[0]), A, M, lex)
    rnd = random.Random(20261111); C = {'A': [], 'B': [], 'C': []}
    for _ in range(200):
        t = {o: rnd.randrange(4) for o in range(1, 40)}; C['A'].append(run(ws, lambda w: t.get(w[0]), A, M, lex))
        kk = {id(w): rnd.randrange(4) for w in ws}; C['B'].append(run(ws, lambda w: kk[id(w)], A, M, lex))
        P = list(A); rnd.shuffle(P); C['C'].append(run(ws, lambda w: vdec.kof(w[0]), ''.join(P), M, lex))
    print('mots', len(ws), 'signes (nombres)', sum(len(w) for w in ws))
    print('VRAI  M1 %.3f  M2 %.3f' % (t1, t2))
    mx1 = max(v[0] for c in C.values() for v in c); mx2 = max(v[1] for c in C.values() for v in c)
    for k, v in C.items():
        print('ctrl %s  M1 max %.3f moy %.3f | M2 max %.3f moy %.3f' % (k, max(x[0] for x in v), sum(x[0] for x in v)/200, max(x[1] for x in v), sum(x[1] for x in v)/200))
    print('C1 M1 >= max(ctrl)+0.30 :', t1 >= mx1 + 0.30)
    print('C2 M2 >= max(ctrl)+0.20 :', t2 >= mx2 + 0.20)
