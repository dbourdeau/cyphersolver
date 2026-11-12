"""PROTOCOLE-2 — validation par vérité terrain (glose d'époque) sur une pièce tenue à l'écart.
Usage : python3 scripts/mesure2.py calib | buildkey | mesure
- calib    : n'ouvre que les TSV 32-41 ; clé sur l'ordre A (32-37) -> test ordre B (39-41) et inversement.
- buildkey : n'ouvre que les TSV 32-41 + feuille 1673 ; écrit working/KEY-v2.json.
- mesure   : UNE exécution ; clé = KEY-v2.json (figée) ; test = TSV 42-43 (lettre du 6 oct. 1674).
Unité = segment de glose : une ligne chiffrée dont la glose n'est pas « + », plus les lignes « + » qui la suivent.
Décodage = concaténation des valeurs de la clé ; exact si norm(décodage) == norm(glose)."""
import csv, json, re, random, sys, collections
D = "working/"
TRAIN_A = ["32", "33", "34", "35", "36", "37"]
TRAIN_B = ["39", "40", "41"]
HOLD = ["42", "43"]
REL = {**{i: "A1" for i in ("32", "33", "34")}, **{i: "A2" for i in ("35", "36", "37")},
       **{i: "A3" for i in ("39", "40")}, **{i: "A4" for i in ("41", "42", "43")}}
SEED = 20261111

def norm(s):
    s = s.lower()
    for a, b in (("w", "v"), ("ø", "o"), ("ö", "o"), ("æ", "e"), ("å", "aa"), ("ck", "k"), ("c", "k"), ("q", "k"),
                 ("ff", "f"), ("y", "i"), ("j", "i"), ("ß", "s")):
        s = s.replace(a, b)
    s = re.sub(r"(.)\1+", r"\1", s)
    return re.sub(r"[^a-z]", "", s)

def table():
    T = {}
    for r in csv.DictReader(open(D + "notation/TABLE-SIGNES.tsv"), delimiter="\t"):
        T[(r["releveur"], r["etiquette"])] = r["canon"].split("|")
    return T
TAB = table()
# Règles fixées AVANT la mesure pour les étiquettes à deux canons (entraînement : par la glose ; test : premier canon listé)
RULE = {("A1", "4"): lambda g: "SIG_4ouvert" if g[:1] in ("k", "c") else "SIG_4ferme",
        ("A4", "4"): lambda g: "SIG_tcroix" if g[:1] == "b" else "SIG_4ouvert",
        ("A4", "9"): lambda g: "SIG_g8" if g[:1] in ("i", "j") else "SIG_9",
        ("A1", "r"): lambda g: "SIG_Gflag" if g[:1] == "f" else "SIG_Gamma",
        ("A1", "[Π]"): lambda g: "SIG_II" if g[:1] == "n" else "SIG_Pi",
        ("A1", "Z"): lambda g: "SIG_Zn" if g[:1] == "n" else "SIG_S",
        ("A1", "#"): lambda g: "SIG_hbar" if g[:1] == "e" else "SIG_ffbar",
        ("A3", "m"): lambda g: "SIG_mbar_u" if g[:1] == "u" else "SIG_m"}

def canon(rel, tok, gloss=None, test=False):
    t = tok.strip()
    if test: t = t.replace("?", "") if re.fullmatch(r"[0-9?]+", t) else t
    if re.fullmatch(r"[0-9]+", t): return t
    c = TAB.get((rel, t))
    if c is None: return "RAW:%s:%s" % (rel, t)
    if c == ["SIG_?"]: return None
    if len(c) > 1:
        return RULE[(rel, t)](gloss or "") if (not test and (rel, t) in RULE) else c[0]
    return c[0]

def corrections():
    C = {}
    for r in csv.DictReader(open(D + "groupes-retrouves/CORRECTIONS-RELEVES.tsv"), delimiter="\t"):
        C[(r["img"], r["page"], r["ligne"], r["groupe_ancien"])] = (r["groupe_nouveau"], r["glose_nouvelle"].split(" (")[0].replace(" ?", ""))
    return C

def rows(imgs, corr=True):
    C = corrections() if corr else {}
    out = []
    for i in imgs:
        for r in csv.reader(open(D + "pairs/1674_img%s.tsv" % i), delimiter="\t"):
            if len(r) < 6 or r[0] == "img": continue
            k = (r[0], r[1], r[2], r[3].strip())
            if k in C: r = r[:3] + [C[k][0], C[k][1], r[5]]
            out.append([x.strip() for x in r[:6]])
    return out

def units(R, test=False):
    """liste d'unités : (tokens canonisés, glose, conf) ; une unité = tête + suites « + »."""
    U = []; cur = None
    for img, pg, ln, g, gl, cf in R:
        rel = REL[img]
        if g.startswith("[clair") : cur = None; continue
        if gl == "+" and cur is not None:
            cur[0].append(canon(rel, g, None, test)); continue
        cur = ([canon(rel, g, gl.lower(), test)], gl, cf); U.append(cur)
    return U

def scorable(u):
    toks, gl, cf = u
    return not (gl in ("", "-", "+") or gl.startswith("[") or "?" in gl or cf == "?" or norm(gl) == "")

def build_key(R, feuille=False):
    C = collections.defaultdict(collections.Counter)
    for toks, gl, cf in units(R):
        if len(toks) != 1 or toks[0] is None or not scorable((toks, gl, cf)): continue
        C[toks[0]][gl.lower()] += {"s": 2, "p": 1}.get(cf, 0.5)
    K = {c: cnt.most_common(1)[0][0] for c, cnt in C.items()}
    if feuille:
        for l in open(D + "key_feuille_1673.tsv"):
            if l.startswith("#"): continue
            p = l.rstrip("\n").split("\t")
            if len(p) >= 2 and re.fullmatch(r"\d{3}", p[0]) and p[0] not in K and "?" not in p[1]: K[p[0]] = p[1]
    return K

def decode(toks, K): return "".join(K.get(t, "#") if t else "#" for t in toks)

def score(U, K):
    S = [u for u in U if scorable(u)]
    ok = sum(1 for toks, gl, cf in S if "#" not in decode(toks, K) and norm(decode(toks, K)) == norm(gl))
    return ok / max(len(S), 1), ok, len(S)

def controls(U, K, N=200):
    rnd = random.Random(SEED); S = [u for u in U if scorable(u)]
    used = sorted({t for u in S for t in u[0] if t in K})
    num = [t for t in used if re.fullmatch(r"\d{3}", t)]; oth = [t for t in used if t not in num]
    perm = []
    for _ in range(N):
        k = dict(K)
        for grp in (num, oth):
            v = [K[t] for t in grp]; rnd.shuffle(v); k.update(zip(grp, v))
        perm.append(score(S, k)[0])
    shift = []
    for d in range(1, 21):
        ok = sum(1 for i, (toks, gl, cf) in enumerate(S)
                 if norm(decode(toks, K)) == norm(S[(i + d) % len(S)][1]) and "#" not in decode(toks, K))
        shift.append(ok / len(S))
    return max(perm), sum(perm) / N, max(shift)

if __name__ == "__main__":
    m = sys.argv[1]
    if m == "calib":
        for tr, te, nm in ((TRAIN_A, TRAIN_B, "A->B"), (TRAIN_B, TRAIN_A, "B->A")):
            K = build_key(rows(tr)); U = units(rows(te), test=True)
            acc, ok, n = score(U, K); pm, pmean, sh = controls(U, K, N=50)
            print("%s exact=%.3f (%d/%d) ; max 50 clés permutées=%.3f (moy. %.3f) ; max 20 décalages=%.3f" % (nm, acc, ok, n, pm, pmean, sh))
    elif m == "buildkey":
        K = build_key(rows(TRAIN_A + TRAIN_B), feuille=True)
        json.dump(K, open(D + "KEY-v2.json", "w"), ensure_ascii=False, indent=0, sort_keys=True)
        print("KEY-v2", len(K), "entrées")
    elif m == "mesure":
        K = json.load(open(D + "KEY-v2.json"))
        U = units(rows(HOLD, corr=False), test=True)
        acc, ok, n = score(U, K); pm, pmean, sh = controls(U, K)
        print("TENU A L'ECART (42-43) exact=%.3f (%d/%d) ; max 200 clés permutées=%.3f (moy. %.3f) ; max 20 décalages=%.3f" % (acc, ok, n, pm, pmean, sh))
