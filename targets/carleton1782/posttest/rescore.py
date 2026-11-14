"""Re-score the frozen 25 Sep 1782 predictions against an independent hand alignment of the clear copy.

    python targets/carleton1782/posttest/rescore.py

Inputs: ../carleton_1782-09-25/preclear/predictions.tsv (frozen, unchanged) and clear_alignment_25sep.tsv (each unit's
clear word typed from B.148 p.102, frame 1183, on 13 Nov 2026, without reference to the predictions).
The 12 Nov scorer (postclear/score.py) defaulted the clear word to the prediction for every unit not in its
exception lists, so a disagreement there could not be seen; this script compares every unit.
Outputs: comparison.tsv, SCORE.json (with a shuffled-table control).
"""
import csv, json, random
from collections import Counter
from pathlib import Path

H = Path(__file__).resolve().parent
PRE = H.parent / 'carleton_1782-09-25/preclear'
read = lambda p: list(csv.DictReader(p.open(encoding='utf-8'), delimiter='\t'))
norm = lambda s: ''.join(c for c in s.lower() if c.isalpha()).replace('j', 'i')

pred = read(PRE / 'predictions.tsv')
clear = read(H / 'clear_alignment_25sep.tsv')
assert [p['order'] for p in pred] == [c['order'] for c in clear]

def status(basis, prediction, c):
    if basis == 'already clear on cipher witness': return 'already_clear_or_notation'
    if basis == 'uncovered word code': return 'uncovered_before_clear'
    if not c: return 'no_clear_counterpart'
    if basis == 'Clinton qualified':
        return 'qualified_set_agrees' if norm(c) in [norm(x) for x in prediction.split(' / ')] else 'qualified_mismatch'
    return 'agrees' if norm(c) == norm(prediction) else 'fails'

out = []
for p, c in zip(pred, clear):
    out.append(dict(order=p['order'], kind=p['kind'], tokens=p['tokens'], prediction=p['mechanical_prediction'],
                    basis=p['basis'], clear_p102=c['clear_p102'], status=status(p['basis'], p['mechanical_prediction'], c['clear_p102']),
                    note=c['note']))
with (H / 'comparison.tsv').open('w', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=list(out[0]), delimiter='\t'); w.writeheader(); w.writerows(out)

classes = {b: dict(Counter(r['status'] for r in out if r['basis'] == b)) for b in dict.fromkeys(r['basis'] for r in out)}
fails = [(r['order'], r['tokens'], r['prediction'], r['clear_p102']) for r in out
         if r['status'] in ('fails', 'qualified_mismatch') and r['kind'] == 'W']

# Shuffled-table control: permute the (reading, status) pairs of the 100 frozen codes among the codes, 200 times,
# and count how many of the 58 unqualified-prediction units would then agree with the clear word.
table = read(PRE / 'evidence/clinton_word_constraints.tsv')
codes = [t['tokens'] for t in table]
vals = [(t['local_readings'], t['constraint_status']) for t in table]
rng = random.Random(1782)
counts = []
targets = [(r['tokens'], r['clear_p102']) for r in out if r['basis'] == 'Clinton candidate lexical constraint']
for _ in range(200):
    v = vals[:]; rng.shuffle(v); m = dict(zip(codes, v))
    counts.append(sum(1 for t, c in targets if m[t][1] == 'candidate lexical constraint' and norm(m[t][0]) == norm(c)))
real = sum(1 for r in out if r['basis'] == 'Clinton candidate lexical constraint' and r['status'] == 'agrees')
mean = sum(counts) / len(counts)
summary = {
    'frozen_units': len(out),
    'classes': classes,
    'word_code_failures': fails,
    'unqualified_agree': real,
    'unqualified_total': sum(classes['Clinton candidate lexical constraint'].values()),
    'shuffled_control': {'shuffles': 200, 'seed': 1782, 'mean_agreements': round(mean, 2),
                         'sd': round((sum((x - mean) ** 2 for x in counts) / len(counts)) ** 0.5, 2),
                         'max': max(counts), 'reaching_real': sum(x >= real for x in counts),
                         'note': 'the 58 units that carried an unqualified prediction; a shuffled code counts only if its new value is also unqualified'},
    'note': 'Frozen predictions unchanged. Spelled groups scored as frozen, so the transcription slip escapedo stays a failure here; see CORRECTIONS.md.',
}
(H / 'SCORE.json').write_text(json.dumps(summary, indent=2) + '\n', encoding='utf-8')
print(json.dumps(summary, indent=2))
