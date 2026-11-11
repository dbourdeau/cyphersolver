"""Reconstruit une table de chiffre commune à plusieurs documents, par EM « souple ».

Sources acceptées (on peut en donner plusieurs) :
  --paire CHIFFRE CLAIR [ANCRES]  chiffré (lecture ou consensus) + son déchiffrement séparé,
                                  ancres facultatives (gloses : ref, rang du groupe, mot)
  --interligne FICHIER            chiffré avec le clair ligne par ligne (lignes fNNN Lnn / fNNN Tnn)

Modèle : chaque nombre vaut une unité (morceau de mot, mot entier, 2-3 petits mots) ou rien.
P(valeur | nombre) est partagée entre tous les documents ; pénalité fixe de longueur par
groupe pour éviter les solutions dégénérées. Lectures incertaines : ensemble de candidats.

Sorties : PREFIXE_table.tsv et PREFIXE_alignement.txt
"""
import argparse
import math
import re
import unicodedata
from collections import Counter, defaultdict

LMAX, MOTS_MAX, MULTI_MAX, BANDE = 14, 3, 7, 300
ALPHAS = [8, 4, 2, 1, 0.5, 0.3, 0.2, 0.2, 0.2, 0.2]
P_LEN = {0: 0.04, 1: 0.12, 2: 0.28, 3: 0.24, 4: 0.14, 5: 0.08, 6: 0.05, 7: 0.03, 8: 0.02,
         9: 0.012, 10: 0.008, 11: 0.005, 12: 0.003, 13: 0.002, 14: 0.001}


def normaliser(t):
    t = unicodedata.normalize("NFD", t.lower())
    return re.sub(r"[^a-z0-9]", "", "".join(c for c in t if unicodedata.category(c) != "Mn"))


def decouper_mots(txt):
    return [n for n in (normaliser(m) for m in re.split(r"[\s'’\-]+", re.sub(r"\[[^\]]*\]", "", txt))) if n]


def cands(t):
    t = t.lstrip("_")
    alt = re.search(r"\[([\d|]+)\]", t)
    if alt:
        return tuple(int(x) for x in alt.group(1).split("|") if x)
    d = re.sub(r"\D", "", re.sub(r"\[.*", "", t))
    return (int(d),) if d else (-1,)


def lire_groupes_lignes(chemin):
    """Renvoie {ref: [(candidats, douteux), ...]} dans l'ordre du fichier."""
    lignes, ordre = {}, []
    lire = True
    for l in open(chemin, encoding="utf-8"):
        if re.match(r"\s*(GLOSES|DOUTES|NOTES|DESACCORDS)\b", l):
            break
        if re.match(r"\s*CLAIR\b", l):
            lire = False
            continue
        if re.match(r"\s*CHIFFRE\b", l):
            lire = True
            continue
        if not lire:
            continue
        m = re.match(r"\s*(f\d+[rv]?)\s+(L\d+)\s*:\s*(.*)$", l)
        if not m:
            continue
        ref = f"{m.group(1)} {m.group(2)}"
        toks = []
        for bloc in re.findall(r"\{A:([^|}]*)\|[^}]*\}|(\S+)", m.group(3)):
            if bloc[0]:
                toks += [(cands(t), True) for t in bloc[0].split()]
            elif bloc[1] and bloc[1][0] not in "{«\"":
                toks.append((cands(bloc[1]), "?" in bloc[1]))
        lignes[ref] = toks
        ordre.append(ref)
    return lignes, ordre


class Segment:
    def __init__(self, nom, groupes, refs, rangs, mots, gloses=None):
        self.nom, self.groupes, self.refs, self.rangs, self.mots = nom, groupes, refs, rangs, mots
        self.gloses = gloses or [None] * len(groupes)
        self.clair = "".join(mots)
        self.mot_de, self.debuts, self.fins, pos = [], set(), set(), 0
        for i, m in enumerate(mots):
            self.debuts.add(pos)
            self.mot_de += [i] * len(m)
            pos += len(m)
            self.fins.add(pos)
        M = len(self.clair)
        self.unites = {}
        for j in range(M + 1):
            opts = [(j, "", False)]
            if j < M:
                w = self.mot_de[j]
                for k in range(j + 1, min(M, j + LMAX) + 1):
                    if self.mot_de[k - 1] != w:
                        break
                    opts.append((k, self.clair[j:k], j in self.debuts and k in self.fins))
                if j in self.debuts:
                    k, n = j, 0
                    while k < M and n < MOTS_MAX:
                        wk = self.mot_de[k]
                        while k < M and self.mot_de[k] == wk:
                            k += 1
                        n += 1
                        if n >= 2 and k - j <= MULTI_MAX:
                            opts.append((k, self.clair[j:k], True))
            self.unites[j] = opts

    def bonus(self, i, j, s):
        g = self.gloses[i]
        if g is None:
            return 0.0
        w, poids = g if isinstance(g, tuple) else (g, 6.0)
        if w == "":
            return math.log(poids) if s == "" else 0.0
        if not s or j >= len(self.clair):
            return 0.0
        mot = self.mots[self.mot_de[j]]
        return math.log(poids) if (w == mot or (len(w) >= 3 and (w in mot or mot in w)) or s in w) else 0.0


def charger(args):
    segs = []
    for p in args.paire or []:
        chiffre, clair = p[0], p[1]
        lignes, ordre = lire_groupes_lignes(chiffre)
        groupes, refs, rangs = [], [], []
        for r in ordre:
            for k, (c, d) in enumerate(lignes[r]):
                groupes.append((c, d))
                refs.append(r)
                rangs.append(k + 1)
        mots = []
        for l in open(clair, encoding="utf-8"):
            m = re.match(r"\s*(f\d+[rv]?)\s+(L\d+)\s*:\s*(.*)$", l)
            if m:
                mots += decouper_mots(m.group(3))
        gloses = [None] * len(groupes)
        if len(p) > 2:
            anc = {}
            for l in open(p[2], encoding="utf-8"):
                r, g, w = l.rstrip("\n").split("\t")
                anc[(r, int(g))] = w
            gloses = [anc.get((r, k)) for r, k in zip(refs, rangs)]
        segs.append(Segment(chiffre, groupes, refs, rangs, mots, gloses))
    for f in args.interligne or []:
        lignes, ordre = lire_groupes_lignes(f)
        textes, positions = {}, {}
        for l in open(f, encoding="utf-8"):
            m = re.match(r"\s*(f\d+[rv]?)\s+T(\d+)\s*:\s*(.*)$", l)
            if m:
                textes[f"{m.group(1)} L{m.group(2)}"] = m.group(3)
            m = re.match(r"\s*(f\d+[rv]?)\s+P(\d+)\s*:\s*(.*)$", l)
            if m and "indistinct" not in m.group(3):
                approx = m.group(3).lstrip().startswith("~")
                poids = 4.0 if approx else 20.0
                pos = {}
                for g1, g2, w in re.findall(r"g(\d+)(?:-g(\d+))?\s*=\s*([^|]+)", m.group(3)):
                    mots_w = decouper_mots(w) if "rien" not in w else [""]
                    a, b = int(g1), int(g2 or g1)
                    for k in range(a, b + 1):
                        # un groupe sous plusieurs mots : on garde le mot correspondant si possible
                        idx = min(k - a, len(mots_w) - 1) if mots_w else 0
                        pos[k] = (mots_w[idx] if mots_w else "", poids)
                positions[f"{m.group(1)} L{m.group(2)}"] = pos
        for r in ordre:
            if r in textes and lignes[r]:
                g = lignes[r]
                pos = positions.get(r, {})
                segs.append(Segment(f"{f}:{r}", g, [r] * len(g), list(range(1, len(g) + 1)),
                                    decouper_mots(textes[r]), [pos.get(k) for k in range(1, len(g) + 1)]))
    return segs


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--paire", nargs="+", action="append")
    ap.add_argument("--interligne", action="append")
    ap.add_argument("--sortie", required=True)
    args = ap.parse_args()
    segs = charger(args)
    tout = "".join(s.clair for s in segs)
    uni = Counter(tout)
    luni = {c: math.log(v / sum(uni.values())) for c, v in uni.items()}
    fmots = Counter(m for s in segs for m in s.mots)
    print(f"{len(segs)} segments, {sum(len(s.groupes) for s in segs)} groupes, {len(tout)} lettres")

    def lprior(s, entier):
        if not s:
            return math.log(0.03)
        p = 0.55 * sum(luni.get(c, -9) for c in s)
        if entier:
            p += math.log(4) + 0.6 * math.log(1 + fmots.get(s, 0))
        if len(s) == 1:
            p += math.log(0.3)
        return p

    table = defaultdict(Counter)

    def emission(cs, s, entier, alpha):
        best, arg = -math.inf, cs[0]
        for n in cs:
            if n < 0:
                v = lprior(s, entier)
            else:
                c = table.get(n)
                tn = sum(c.values()) if c else 0.0
                v = math.log(((c.get(s, 0.0) if c else 0.0) + alpha * math.exp(lprior(s, entier))) / (tn + alpha))
            if v > best:
                best, arg = v, n
        fixe = math.log(P_LEN.get(len(s), 0.0005)) + (math.log(3) if entier and s else 0.0)
        return best + fixe + (math.log(1 / len(cs)) if len(cs) > 1 else 0.0), arg

    def passe(seg, alpha, viterbi=False):
        N, M = len(seg.groupes), len(seg.clair)
        if N == 0:
            return None
        bande = BANDE if N > 60 else 10 ** 6
        def lims(i):
            c = i * M / N
            return max(0, int(c - bande)), min(M, int(c + bande))
        fw = [dict() for _ in range(N + 1)]
        fw[0][0] = (0.0, None, None) if viterbi else 0.0
        cache = []
        for i in range(N):
            cs = seg.groupes[i][0]
            lo, hi = lims(i + 1)
            ci = {}
            for j, val in fw[i].items():
                sc = val[0] if viterbi else val
                for k, s, ent in seg.unites[j]:
                    if k < lo or k > hi:
                        continue
                    key = (j, k, s)
                    if key not in ci:
                        lp, n = emission(cs, s, ent, alpha)
                        ci[key] = (lp + seg.bonus(i, j, s), n)
                    v = sc + ci[key][0]
                    if viterbi:
                        if k not in fw[i + 1] or fw[i + 1][k][0] < v:
                            fw[i + 1][k] = (v, j, (s, ci[key][1]))
                    else:
                        o = fw[i + 1].get(k, -math.inf)
                        m_ = max(o, v)
                        fw[i + 1][k] = m_ + math.log(math.exp(o - m_) + math.exp(v - m_)) if o > -math.inf else v
            cache.append(ci)
        if M not in fw[N]:
            return None
        if viterbi:
            res, j = [], M
            for i in range(N, 0, -1):
                _, jp, sn = fw[i][j]
                res.append(sn)
                j = jp
            return res[::-1]
        Z = fw[N][M]
        bw = [dict() for _ in range(N + 1)]
        bw[N][M] = 0.0
        comptes = []
        for i in range(N - 1, -1, -1):
            for (j, k, s), (lp, n) in cache[i].items():
                if j not in fw[i] or k not in bw[i + 1]:
                    continue
                v = lp + bw[i + 1][k]
                o = bw[i].get(j, -math.inf)
                m_ = max(o, v)
                bw[i][j] = m_ + math.log(math.exp(o - m_) + math.exp(v - m_)) if o > -math.inf else v
                post = fw[i][j] + v - Z
                if post > -12:
                    comptes.append((n, s, math.exp(post)))
        return Z, comptes

    for it, alpha in enumerate(ALPHAS):
        nouv = defaultdict(Counter)
        LL = 0.0
        for seg in segs:
            r = passe(seg, alpha)
            if r is None:
                print("  segment sans alignement :", seg.nom)
                continue
            Z, comptes = r
            LL += Z
            for n, s, w in comptes:
                if n >= 0:
                    nouv[n][s] += w
        table = nouv
        nets = sum(1 for c in table.values() if c and c.most_common(1)[0][1] / sum(c.values()) > 0.9)
        print(f"tour {it + 1} (alpha {alpha}) : LL {LL:.0f}, nombres à valeur nette {nets}/{len(table)}")

    final = defaultdict(Counter)
    with open(args.sortie + "_alignement.txt", "w", encoding="utf-8") as f:
        for seg in segs:
            res = passe(seg, ALPHAS[-1], viterbi=True)
            if res is None:
                continue
            f.write(f"\n### {seg.nom}")
            prec = None
            for (cs, d), r, (s, n) in zip(seg.groupes, seg.refs, res):
                if r != prec:
                    f.write(f"\n{r}: ")
                    prec = r
                if n >= 0:
                    final[n][s] += 1
                lect = n if len(cs) == 1 else f"{n}<{'|'.join(map(str, cs))}>"
                f.write(f"{lect}={s or '∅'} ")
            f.write("\n")
    with open(args.sortie + "_table.tsv", "w", encoding="utf-8") as f:
        f.write("nombre\tvaleur\toccurrences\tautres\tprobabilite_EM\n")
        for n in sorted(final):
            (v, c), *autres = final[n].most_common()
            em = table.get(n, Counter())
            pem = em.get(v, 0) / sum(em.values()) if em else 0
            f.write(f"{n}\t{v or '(nulle)'}\t{c}\t{' '.join(f'{a or chr(8709)}:{k}' for a, k in autres)}\t{pem:.2f}\n")
    print("écrit :", args.sortie + "_table.tsv", args.sortie + "_alignement.txt")


if __name__ == "__main__":
    main()
