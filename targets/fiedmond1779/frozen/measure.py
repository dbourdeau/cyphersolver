# MESURE UNIQUE de l'avenant C09 (AVENANT-C09.md). Refuse de tourner une 2e fois.
import os, sys, random, hashlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *

RES = os.path.join(HERE, 'measure_result.txt')
if os.path.exists(RES):
    sys.exit('mesure déjà faite : pas de seconde chance')

def sha(p): return hashlib.sha256(open(p, 'rb').read()).hexdigest()
T = os.path.join(ROOT, 'transcription')
EXPECT = {os.path.join(HERE, 'K-Guy1780c.tsv'): 'ae615f456bdca66965de8e07cf206d64628e93c60c9d94537185c2640dedd57c',
          os.path.join(T, 'f09.txt'): '4cd4a550bf2026c172768081362327d123c8912ac8265c2546e4b7aca8cdbb09',
          os.path.join(T, 'f16.txt'): '3b35bf277bc8b061d33d744759440293d81b49af643fd7da2a07ad5588c602e7'}
for p, h in EXPECT.items():
    assert sha(p) == h, f'SHA divergent : {p}'
# l'avenant, common.py et ce script doivent correspondre au fichier d'empreintes gelé
for ln in open(os.path.join(ROOT, 'SHA256-AVENANT-C09.txt'), encoding='utf-8'):
    if ln.startswith('#') or not ln.strip(): continue
    h, p = ln.split(None, 1); p = p.strip()
    assert sha(os.path.join(ROOT, p)) == h, f'fichier modifié après le gel : {p}'

THETA = 0.656
NW = 200
lx = lexicon(); model = lm_train()
Kc = load_key(os.path.join(HERE, 'K-Guy1780c.tsv'))
Kb = load_key(os.path.join(ROOT, 'cryptanalysis/c08/K-Guy1780b.tsv'))
ctrl9 = load_lines(os.path.join(T, 'f09.txt'), keep={l for l in HOLD if l[0] == 'v014g'})
ctrl16 = load_lines(os.path.join(T, 'f16.txt'), keep={l for l in HOLD if l[0] == 'v025d'})
assert len(ctrl9) == 8 and len(ctrl16) == 5
toks = [t for _, l in ctrl9 for t in l] + ['C'] + [t for _, l in ctrl16 for t in l]

rng = random.Random(SEED)
Wp = witnesses(Kc, NW, rng, 'permutee'); Wm = witnesses(Kc, NW, rng, 'melangee')
s_c, cov, ng = S(toks, Kc, lx)
sp = [S(toks, k, lx)[0] for k in Wp]; sm = [S(toks, k, lx)[0] for k in Wm]
wmax = max(sp + sm)
rank = 1 + sum(1 for x in sp + sm if x >= s_c)
ok = (s_c > wmax) and (s_c >= THETA)
lc, nch = LM(toks, Kc, model)
lp = [LM(toks, k, model)[0] for k in Wp]; lm_ = [LM(toks, k, model)[0] for k in Wm]
lrank = 1 + sum(1 for x in lp + lm_ if x >= lc)
s_b = S(toks, Kb, lx)[0]; l_b = LM(toks, Kb, model)[0]
known = sum(1 for t in toks if t not in ('C', '?') and t in Kc)
out = [
    '# MESURE UNIQUE — avenant C09 (session C11), ' + __import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    f'portion de contrôle : f9 v014g l11–l18 ({sum(len([t for t in l if t != "C"]) for _, l in ctrl9)} groupes) + f16 v025d l27–l31 ({sum(len([t for t in l if t != "C"]) for _, l in ctrl16)} groupes) = {ng} groupes ; {nch} lettres produites par K-c ; groupes ayant une valeur dans K-c : {known}/{ng}',
    f'DÉCISIF  S(K-c) = {s_c:.3f} ({cov}/{ng} groupes) ; témoins : max permutées {max(sp):.3f} (moy. {sum(sp)/NW:.3f}), max mélangées {max(sm):.3f} (moy. {sum(sm)/NW:.3f}) ; rang {rank}/{2*NW+1} ; seuil θ = {THETA}',
    f'VERDICT : {"PASSE" if ok else "ÉCHOUE"}  (conditions : S > max des {2*NW} témoins : {s_c > wmax} ; S >= θ : {s_c >= THETA})',
    f'non décisif : LM(K-c) = {lc:.3f} ; max permutées {max(lp):.3f}, max mélangées {max(lm_):.3f} ; rang {lrank}/{2*NW+1}',
    f'non décisif : K-Guy1780b sur la même portion : S = {s_b:.3f}, LM = {l_b:.3f}',
]
open(RES, 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('\n'.join(out))
# lecture mécanique (ouverte seulement après le verdict)
rd = ['# Lecture mécanique K-Guy1780c de la portion de contrôle : groupe=valeur[statut] ; ‹g› = sans valeur']
for lid, l in ctrl9 + ctrl16:
    rd.append(lid + ' : ' + ' '.join('«clair»' if t == 'C' else (f'{t}={Kc[t][0]}[{Kc[t][1]}]' if t in Kc else f'‹{t}›') for t in l))
open(os.path.join(HERE, 'controle_lecture_mecanique.txt'), 'w', encoding='utf-8').write('\n'.join(rd) + '\n')
