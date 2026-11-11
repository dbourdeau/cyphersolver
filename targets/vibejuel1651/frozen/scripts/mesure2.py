"""Mesure 2 (PROTOCOLE-2.md). Unité = fichier de transcription (une image / une lettre).
Dans chaque unité, pour chaque valeur d'ouvreur o, k_o = argmax_{k in -4..4} somme des log-probs (lm.py, ordre 4) des mots ouvrant par o
(chaque mot décodé seul, entouré d'espaces). M1 = log-prob moyenne par caractère du texte entier décodé avec ces k.
Contrôles (graine 20261112, 100 tirages chacun, MÊME optimisation) : C = alphabet du corps permuté ; D = nombres du corps mélangés dans chaque mot ;
E = corps remplacés par des nombres tirés au hasard (1..23) à longueur égale.
usage : python3 mesure2.py corpus/ fichier1 [fichier2 ...]"""
import sys, os, random, glob
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lm, mesure, vdec
KS = range(-4, 5)
def dec(nums, k, A):
    out = []
    for n in nums[1:]:
        if 32 <= n <= 34: n -= 31
        i = n - 1 - k
        out.append(A[i] if 0 <= i < 23 else 'x')
    return ''.join(out)
def fit(unit, A, M):
    by = {}
    for w in unit: by.setdefault(w[0], []).append(w)
    tab = {}
    for o, ws in by.items():
        tab[o] = max(KS, key=lambda k: sum(M.per_char(' ' + dec(w, k, A) + ' ') * (len(w) + 1) for w in ws))
    return tab
def total(units, A, M):
    txt = []; tabs = []
    for u in units:
        t = fit(u, A, M); tabs.append(t); txt += [dec(w, t[w[0]], A) for w in u]
    return M.per_char(' '.join(txt)), tabs
if __name__ == '__main__':
    M = lm.build(sorted(glob.glob(sys.argv[1] + '/*.txt'))); A = vdec.A
    units = [mesure.words(open(f).read()) for f in sys.argv[2:]]
    t1, tabs = total(units, A, M)
    for f, t in zip(sys.argv[2:], tabs): print(os.path.basename(f), dict(sorted(t.items())))
    rnd = random.Random(20261112); C = {'C': [], 'D': [], 'E': []}
    for _ in range(100):
        P = list(A); rnd.shuffle(P); C['C'].append(total(units, ''.join(P), M)[0])
        C['D'].append(total([[[w[0]] + rnd.sample(w[1:], len(w) - 1) for w in u] for u in units], A, M)[0])
        C['E'].append(total([[[w[0]] + [rnd.randint(1, 23) for _ in w[1:]] for w in u] for u in units], A, M)[0])
    print('mots', sum(len(u) for u in units), 'nombres', sum(len(w) for u in units for w in u))
    print('VRAI M1 %.3f' % t1)
    for k, v in C.items(): print('ctrl %s max %.3f moy %.3f' % (k, max(v), sum(v) / len(v)))
    mx = max(max(v) for v in C.values())
    print('C1 M1 >= max(ctrl)+0.30 :', t1 >= mx + 0.30, '(marge %.3f)' % (t1 - mx))
