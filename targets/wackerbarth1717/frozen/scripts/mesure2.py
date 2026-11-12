# MESURE UNIQUE 2 (PROTOCOLE-AVENANT-2 §2 + AVENANT-2BIS). Une seule exécution : python3 scripts/mesure2.py > MESURE2.txt
import os, sys, re, json, random, difflib, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lm import *

def verdictA(s, mx):
    if s >= 0.60 and s - mx >= 0.30: return 'VALIDÉ'
    if s - mx >= 0.30: return 'PARTIEL'
    return 'ÉCHEC'

# ---------- A' : vérité terrain V = 0057-0061, clé b ----------
units = []  # (G, spans, nums)
for s in ['0057', '0058', '0059', '0060', '0061']:
    for p in read_releve(os.path.join(REL, f'T-{s}.txt')):
        lines = {}
        order = []
        for lid, toks, g in p['lines']:
            if lid not in lines: lines[lid] = [[], '']; order.append(lid)
            lines[lid][0] += toks; lines[lid][1] += ' ' + g
        nums = []; words = []
        for lid in order:
            toks, g = lines[lid]
            n = [v for k, v in toks if k == 'n']; nums += n
            if g.strip() and n:
                for w in re.split(r"[\s'’\-.,;:()|]+", g):
                    w = norm(w).replace('#', '')
                    if w: words.append(w)
        if not words: continue
        G = ''; spans = []
        for w in words: spans.append((len(G), len(G) + len(w))); G += w
        units.append((G, spans, nums))

def exactA(K):
    ok = tot = cch = tch = 0
    for G, spans, nums in units:
        Dd = dec(K, nums)
        cov = [False] * len(G)
        for b in difflib.SequenceMatcher(None, G, Dd, autojunk=False).get_matching_blocks():
            if b.size >= 3:
                for i in range(b.a, b.a + b.size): cov[i] = True
        for a, z in spans:
            tot += 1; ok += all(cov[a:z])
        cch += sum(cov); tch += len(G)
    return ok / tot, cch / tch, tot

Kb = load_key('KEY-W1717b.tsv')
sA, cA, nW = exactA(Kb)
tA = [exactA(k)[0] for k in perms(Kb, random.Random(1717))]
gV = sum(len(u[2]) for u in units)
covV = sum(1 for u in units for n in u[2] if n in Kb) / gV
RA = dict(groupes=gV, mots_glose=nW, couverture_cle_b=round(covV, 4), exactA=round(sA, 4), car_couverts=round(cA, 4),
          max_temoins=round(max(tA), 4), moy_temoins=round(sum(tA) / 200, 4), marge=round(sA - max(tA), 4), verdict=verdictA(sA, max(tA)),
          decodage=[dec(Kb, u[2]) for u in units], gloses=[u[0] for u in units])

# ---------- B' : portion neuve N = R22-0091, clé c neutralisée, critère L7 ----------
nN = []
for line in open(os.path.join(REL, 'R22-0091.txt'), encoding='utf-8'):
    m = re.match(r'[GD]\d+ C: ?(.*)', line)
    if m: nN += [v for k, v in tokens(m.group(1)) if k == 'n']
M = LM()
def U(s):
    t = 0; n = 0
    for ch in s:
        if ch == '#': continue
        t += math.log((M.C[1][ch] + KADD) / (M.N1 + KADD * M.V)); n += 1
    return t / max(1, n)
def L7(s): return M.L1(s) - U(s)
Kc = load_key('KEY-W1717c.tsv'); Kc7 = {n: (v if len(v) <= 2 else '#') for n, v in Kc.items()}
st = stats(L7, Kc7, nN)
c1 = st['z'] >= 5.16; c2 = st['gap'] >= 0.314; c3 = st['score'] >= 0.070
vB = 'VALIDÉ' if (c1 and c2 and c3) else ('PARTIEL' if c1 else 'ÉCHEC')
RB = dict(groupes=len(nN), couverture_cle_c=round(sum(1 for n in nN if n in Kc) / len(nN), 4),
          **{k: round(v, 4) for k, v in st.items()}, conditions=[c1, c2, c3], verdict=vB, decodage_c=dec(Kc, nN))
json.dump(dict(A=RA, B=RB), open(os.path.join(D, 'MESURE2.json'), 'w'), ensure_ascii=False, indent=1)
print('A', {k: v for k, v in RA.items() if k not in ('decodage', 'gloses')})
print('B', {k: v for k, v in RB.items() if k != 'decodage_c'})
