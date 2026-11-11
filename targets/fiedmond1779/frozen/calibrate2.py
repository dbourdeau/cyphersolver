# Étalonnage n° 2 (apprentissage seulement) : score de langue LM sur les mêmes fenêtres.
import os, random, statistics, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *
T = os.path.join(ROOT, 'transcription')
docs = {'f09': load_lines(os.path.join(T, 'f09-envoi-lot4.txt')), 'f16': load_lines(os.path.join(T, 'f16-envoi-lot4.txt'))}
for d, L in docs.items(): assert not any(tuple(l.split()) in HOLD for l, _ in L)
model = lm_train()
Kb = load_key(os.path.join(ROOT, 'cryptanalysis/c08/K-Guy1780b.tsv')); Kc = load_key(os.path.join(HERE, 'K-Guy1780c.tsv'))
wins = []
for d, L in docs.items():
    cur, n, ids = [], 0, []
    for lid, toks in L:
        cur += toks; n += sum(1 for t in toks if t != 'C'); ids.append(lid)
        if n >= 118: wins.append((d, ids[0], ids[-1], cur)); cur, n, ids = [], 0, []
rng = random.Random(SEED); NW = 200
rows = []
for d, a, b, toks in wins:
    lb = LM(toks, Kb, model)[0]; lc, nch = LM(toks, Kc, model)
    wc = [LM(toks, k, model)[0] for kind in ('permutee', 'melangee') for k in witnesses(Kc, NW, rng, kind)]
    wb = [LM(toks, k, model)[0] for kind in ('permutee', 'melangee') for k in witnesses(Kb, NW, rng, kind)]
    wcp, wcm = max(wc[:NW]), max(wc[NW:])
    rows.append((d, a, b, nch, lb, lc, max(wc), max(wb), wcp, wcm, sum(1 for x in wb if x >= lb), sum(1 for x in wc if x >= lc)))
out = [f'# Étalonnage n° 2 — LM car. 5-grammes (log10/car.), {len(wins)} fenêtres >= 118 groupes, {NW} permutées + {NW} mélangées par clé et par fenêtre, graine {SEED}',
       'doc\tdébut\tfin\tn_car_Kc\tLM_Kb\tLM_Kc\tmaxTém_Kc\tmaxTém_Kb\tmaxPerm_Kc\tmaxMél_Kc\ttém>=Kb\ttém>=Kc']
for r in rows: out.append('\t'.join([r[0], r[1], r[2], str(r[3])] + [f'{x:.3f}' for x in r[4:10]] + [str(r[10]), str(r[11])]))
def q(xs, p): xs = sorted(xs); return xs[max(0, min(len(xs) - 1, int(round(p * (len(xs) - 1)))))]
gb = [r[4] - r[7] for r in rows]; gc = [r[5] - r[6] for r in rows]
out += ['', f'LM_Kb (hors échantillon) : min {min(r[4] for r in rows):.3f} q10 {q([r[4] for r in rows], .1):.3f} médiane {statistics.median(r[4] for r in rows):.3f}',
        f'LM_Kc (en échantillon) : min {min(r[5] for r in rows):.3f} q10 {q([r[5] for r in rows], .1):.3f} médiane {statistics.median(r[5] for r in rows):.3f}',
        f'max témoins K-b : médiane {statistics.median(r[7] for r in rows):.3f} max {max(r[7] for r in rows):.3f} ; max témoins K-c : médiane {statistics.median(r[6] for r in rows):.3f} max {max(r[6] for r in rows):.3f}',
        f'écart K-b − max témoins : min {min(gb):.3f} q10 {q(gb, .1):.3f} médiane {statistics.median(gb):.3f}',
        f'écart K-c − max témoins : min {min(gc):.3f} q10 {q(gc, .1):.3f} médiane {statistics.median(gc):.3f}',
        f'fenêtres où K-b bat les 400 témoins : {sum(1 for r in rows if r[10] == 0)}/{len(rows)} ; K-c : {sum(1 for r in rows if r[11] == 0)}/{len(rows)}']
for dl in (0.05, 0.10, 0.15, 0.20):
    out.append(f'  K-b >= max témoins + {dl:.2f} : {sum(1 for x in gb if x >= dl)}/{len(gb)}')
open(os.path.join(HERE, 'calibrate2_result.txt'), 'w', encoding='utf-8').write('\n'.join(out) + '\n'); print('\n'.join(out))
