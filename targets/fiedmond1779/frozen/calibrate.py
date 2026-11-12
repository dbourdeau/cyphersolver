# Étalonnage SUR L'APPRENTISSAGE SEULEMENT : copies d'envoi f09/f16 (portion de contrôle physiquement absente).
import os, random, statistics, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *

T = os.path.join(ROOT, 'transcription')
docs = {'f09': load_lines(os.path.join(T, 'f09-envoi-lot4.txt')), 'f16': load_lines(os.path.join(T, 'f16-envoi-lot4.txt'))}
for d, L in docs.items():
    assert not any(tuple(l.split()) in HOLD for l, _ in L), 'ligne de contrôle présente !'
lx = lexicon()
Kb = load_key(os.path.join(ROOT, 'cryptanalysis/c08/K-Guy1780b.tsv'))
Kc = load_key(os.path.join(HERE, 'K-Guy1780c.tsv'))
TARGET = 118
wins = []
for d, L in docs.items():
    cur, n, ids = [], 0, []
    for lid, toks in L:
        cur += toks; n += sum(1 for t in toks if t != 'C'); ids.append(lid)
        if n >= TARGET:
            wins.append((d, ids[0], ids[-1], cur)); cur, n, ids = [], 0, []
rng = random.Random(SEED)
NW = 100
rows = []
for d, a, b, toks in wins:
    sb = S(toks, Kb, lx)[0]; sc = S(toks, Kc, lx)[0]
    wp = max(S(toks, k, lx)[0] for k in witnesses(Kc, NW, rng, 'permutee'))
    wm = max(S(toks, k, lx)[0] for k in witnesses(Kc, NW, rng, 'melangee'))
    wbp = max(S(toks, k, lx)[0] for k in witnesses(Kb, NW, rng, 'permutee'))
    wbm = max(S(toks, k, lx)[0] for k in witnesses(Kb, NW, rng, 'melangee'))
    rows.append((d, a, b, sb, sc, max(wp, wm), max(wbp, wbm), wp, wm))
out = []
out.append(f'# Étalonnage avenant C09 — {len(wins)} fenêtres de >= {TARGET} groupes (apprentissage f09/f16 hors contrôle) ; {NW} témoins permutés + {NW} mélangés par fenêtre et par clé ; graine {SEED}')
out.append('doc\tdébut\tfin\tS_Kb\tS_Kc\tmaxTém_Kc\tmaxTém_Kb\tmaxPerm_Kc\tmaxMél_Kc')
for r in rows: out.append('\t'.join([r[0], r[1], r[2]] + [f'{x:.3f}' for x in r[3:]]))
def q(xs, p): xs = sorted(xs); return xs[max(0, min(len(xs) - 1, int(round(p * (len(xs) - 1)))))]
SB = [r[3] for r in rows]; SC = [r[4] for r in rows]; WC = [r[5] for r in rows]; WB = [r[6] for r in rows]
out.append('')
out.append(f'S_Kb (hors échantillon pour K-b) : min {min(SB):.3f} q10 {q(SB,.1):.3f} médiane {statistics.median(SB):.3f} max {max(SB):.3f}')
out.append(f'S_Kc (EN échantillon, optimiste) : min {min(SC):.3f} q10 {q(SC,.1):.3f} médiane {statistics.median(SC):.3f} max {max(SC):.3f}')
out.append(f'max témoins (K-c) par fenêtre : min {min(WC):.3f} médiane {statistics.median(WC):.3f} max {max(WC):.3f}')
out.append(f'max témoins (K-b) par fenêtre : min {min(WB):.3f} médiane {statistics.median(WB):.3f} max {max(WB):.3f}')
gb = [r[3] - r[6] for r in rows]
out.append(f'écart K-b − max témoins K-b : min {min(gb):.3f} q10 {q(gb,.1):.3f} médiane {statistics.median(gb):.3f}')
for dl in (0.10, 0.15, 0.20, 0.25, 0.30):
    out.append(f'  part des fenêtres où K-b >= max témoins + {dl:.2f} : {sum(1 for x in gb if x >= dl)}/{len(gb)}')
open(os.path.join(HERE, 'calibrate_result.txt'), 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('\n'.join(out))
