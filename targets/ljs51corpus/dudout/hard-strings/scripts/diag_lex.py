"""Diagnostic exploratoire : couverture lexicale du decodage par la cle de Daniel vs du decodage aveugle
(piste 2), et score mot = somme log((c+0.5)/N) avec OOV = log(0.5/N) - 3."""
import sys, math
sys.path.insert(0, "/Users/bdudout/Documents/Veille cyber/dechiffrements-europe/ljs51-aveugle/scripts")
B = "/Users/bdudout/Documents/Veille cyber/dechiffrements-europe/ljs51-22r1-61r3/"
AV = "/Users/bdudout/Documents/Veille cyber/dechiffrements-europe/ljs51-aveugle/"
lex = {}
for l in open(B + "modele/lex.tsv"):
    w, c = l.rstrip('\n').split('\t'); lex[w] = int(c)
N = sum(lex.values())
def ws(text):
    s = 0; inl = 0; ww = text.split()
    for w in ww:
        c = lex.get(w, 0)
        if c >= 2: inl += 1
        s += math.log((c + 0.5) / N) if c >= 2 else math.log(0.5 / N) - 3
    return inl / len(ww), s, len(ww)
dan = {l.split('\t')[0]: l.rstrip('\n').split('\t')[9] for l in open(B + "diag/objectif.tsv").read().split('\n')[1:] if l}
res = {l.split('\t')[1]: l.split('\t') for l in open(AV + "mesure/RESULTATS.tsv").read().split('\n')[1:] if l}
print("chaine\taccord_aveugle\tcouv_Daniel\tcouv_aveugle\tscoremots_Daniel\tscoremots_aveugle\tdelta(D-A)")
for cid, d in dan.items():
    a = res[cid][15]
    cd, sd, n = ws(d); ca, sa, _ = ws(a)
    print(f"{cid}\t{res[cid][8]}\t{cd:.2f}\t{ca:.2f}\t{sd:.0f}\t{sa:.0f}\t{sd-sa:+.0f}")
