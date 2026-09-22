"""Build code_table.tsv, one value per code number, from every source:
  pairs_jqa.txt (frames 0206/0189 clerk decodes, first session; I = slot inference)
  clerk_*.tsv   (clerk interlinear decodes on other frames: 0182, 0184-0185, 0190, 0183, 0194, 0198)
  ford_pairs*.tsv (alignment with Ford's printed decipherments, grade C)
  overrides.tsv (hand decisions; always win; grade and note given there)
Vote per normalised value: H 3, C 3, M 1, I 0.5 per attestation. The grade of the chosen value is the best grade
among its attestations; a value that wins only on M/I support stays M/I. Numbers whose attestations disagree are
listed in code_conflicts.txt.  python consolidate.py"""
import glob, os, re
os.chdir(os.path.dirname(os.path.abspath(__file__)))
W = {'H': 3, 'C': 3, 'M': 1, 'I': 0.5}
R = {'H': 0, 'C': 1, 'M': 2, 'I': 3}
def key(s):
    return re.sub(r'[^a-z]', '', re.sub(r'\(.*?\)', '', s.lower()))
src = {}
files = ['pairs_jqa.txt'] + sorted(glob.glob('clerk_*.tsv')) + sorted(glob.glob('ford_pairs*.tsv')) + sorted(glob.glob('ford1812_pairs*.tsv')) + sorted(glob.glob('slot_*.tsv'))
for f in files:
    for l in open(f, encoding='utf8'):
        p = l.rstrip('\n').split('\t')
        if l.startswith('#') or len(p) < 4 or not p[0].strip().isdigit():
            continue
        g = p[3].strip()[:1]
        g = g if g in W else 'I'
        src.setdefault(int(p[0]), []).append((p[1].strip(), g, f.replace('.tsv', '').replace('.txt', '') + ':' + p[2].strip()))
over = {}
if os.path.exists('overrides.tsv'):
    for l in open('overrides.tsv', encoding='utf8'):
        p = l.rstrip('\n').split('\t')
        if l.startswith('#') or len(p) < 3 or not p[0].strip().isdigit():
            continue
        over[int(p[0])] = (p[1].strip(), p[2].strip(), p[3].strip() if len(p) > 3 else 'override')
out = open('code_table.tsv', 'w', encoding='utf8')
con = open('code_conflicts.txt', 'w', encoding='utf8')
out.write('# JQA St Petersburg code (the = 1385), one value per number, built by consolidate.py\n')
out.write('# number\tvalue\tgrade (H clerk decode, C Ford-aligned, M uncertain, I slot inference)\tsupport\n')
nH = {'H': 0, 'C': 0, 'M': 0, 'I': 0}
for n in sorted(set(src) | set(over)):
    if n in over:
        v, g, note = over[n]
        out.write(f'{n}\t{v}\t{g}\toverride: {note}\n'); nH[g[:1]] = nH.get(g[:1], 0) + 1
        continue
    votes = {}
    for v, g, s in src[n]:
        k = key(v) or v
        d = votes.setdefault(k, {'score': 0, 'grades': [], 'forms': [], 'srcs': []})
        d['score'] += W[g]; d['grades'].append(g); d['forms'].append(v); d['srcs'].append(s)
    best = max(votes, key=lambda k: (votes[k]['score'], -min(R[g] for g in votes[k]['grades'])))
    d = votes[best]
    g = min(d['grades'], key=lambda x: R[x])
    others = [k for k in votes if k != best]
    # a disputed value keeps its grade only if it wins clearly
    if others and g in 'HC' and d['score'] < 2 * max(votes[k]['score'] for k in others):
        g = 'M'
    form = max(set(d['forms']), key=d['forms'].count)
    out.write(f'{n}\t{form}\t{g}\t{len(d["srcs"])}x' + (f'; also {"/".join(others)}' if others else '') + '\n')
    nH[g] += 1
    if others:
        con.write(f'{n}: ' + ' | '.join(f'{k} ({votes[k]["score"]}; {",".join(sorted(set(votes[k]["grades"])))}; {"; ".join(votes[k]["srcs"][:3])})' for k in votes) + '\n')
print('numbers', sum(nH.values()), nH)
