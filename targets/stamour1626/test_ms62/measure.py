# measure.py — PREREG-MS62-K239.md §2-3. Usage : python3 -I measure.py KEY.json LEXIQUE.txt CHIFFRE-MS62.tsv OUT.json
import sys, json, csv, random
key, lexf, tsv, out = sys.argv[1:5]
K = json.load(open(key))
dec = {}
for part in ('table', 'au_dessus_des_lettres', 'notes_haut_gauche'):
    dec.update(K[part])
lex = set(w.strip() for w in open(lexf) if w.strip())
lex = {w for w in lex if len(w) >= 2}
# lecture des jetons
toks = []; prev = None; n_ill = 0; n_tot = 0
for row in csv.reader(open(tsv, encoding='utf-8'), delimiter='\t'):
    if not row or row[0].startswith('#') or row[0] == 'img': continue
    if len(row) < 5: continue
    pid = (row[0], row[1]); t = row[4].strip()
    if pid != prev: toks.append('|'); prev = pid
    if t == '' : continue
    if t == '|': toks.append('|'); continue
    if t.startswith('[ill'): n_ill += 1; toks.append('|'); continue
    n_tot += 1
    toks.append(t.rstrip('?').strip())
def decode(d):
    s = []
    for t in toks:
        s.append(d.get(t, '|') if t != '|' else '|')
    segs = [x for x in ''.join(s).split('|') if x]
    return segs
def cover(seg):
    n = len(seg); best = [0] * (n + 1)
    for i in range(1, n + 1):
        best[i] = best[i - 1]
        for j in range(max(0, i - 20), i - 1):
            if seg[j:i] in lex: best[i] = max(best[i], best[j] + (i - j))
    return best[n]
def M(d):
    segs = decode(d); L = sum(len(x) for x in segs)
    return (sum(cover(x) for x in segs) / L if L else 0.0), L
m, L = M(dec)
signs = list(dec); vals = [dec[s] for s in signs]
rng = random.Random(1626); ctr = []
for _ in range(200):
    v = vals[:]; rng.shuffle(v); ctr.append(M(dict(zip(signs, v)))[0])
mx = max(ctr)
n_in = sum(1 for t in toks if t != '|' and t in dec)
verdict = ('PAS DE MESURE (portion < 300 signes décodables)' if n_in < 300 else
           'VALIDEE' if (m >= 0.85 and m >= mx + 0.30) else 'PARTIELLE' if m >= mx + 0.30 else 'ECHEC')
res = dict(M=round(m, 4), lettres=L, signes_transcrits=n_tot, signes_decodables=n_in, illisibles=n_ill,
           hors_cle=n_tot - n_in, temoin_max=round(mx, 4), temoin_moy=round(sum(ctr) / 200, 4), verdict=verdict,
           decodage=decode(dec))
json.dump(res, open(out, 'w'), ensure_ascii=False, indent=1)
print({k: v for k, v in res.items() if k != 'decodage'})
