import sys, difflib, random, unicodedata, re, csv
key_path, ct_path, gl_path = sys.argv[1:4]
key = {}
with open(key_path, encoding='utf-8') as f:
    r = csv.reader(f, delimiter='\t'); next(r)
    for row in r:
        v = row[1].strip()
        if v == '?' or v == '': v = ''
        key[int(row[0])] = v.split('/')[0]
def norm(s):
    s = unicodedata.normalize('NFD', s.lower())
    return re.sub('[^a-z]', '', ''.join(c for c in s if not unicodedata.combining(c)))
groups = []
for line in open(ct_path, encoding='utf-8'):
    if line.startswith('#') or not line.strip(): continue
    for t in line.split()[1:]:
        t = t.rstrip('*')
        if t.isdigit(): groups.append(int(t))
gloss = norm(' '.join(l for l in open(gl_path, encoding='utf-8') if not l.startswith('#')))
def dec(k): return norm(''.join(k.get(g, '') for g in groups))
d = dec(key)
acc = difflib.SequenceMatcher(None, d, gloss, autojunk=False).ratio()
cells = sorted(key); vals = [key[c] for c in cells]
rng = random.Random(20261123); wit = []
for _ in range(200):
    v = vals[:]; rng.shuffle(v); k2 = dict(zip(cells, v))
    wit.append(difflib.SequenceMatcher(None, dec(k2), gloss, autojunk=False).ratio())
best = max(wit); mean = sum(wit)/len(wit)
print('groupes', len(groups), 'lettres_decodees', len(d), 'lettres_glose', len(gloss))
print('accord %.4f meilleur_temoin %.4f moyenne_temoins %.4f' % (acc, best, mean))
ok = len(d) >= 300 and acc >= 0.85 and acc >= best + 0.30
print('VERDICT', 'NON MESURABLE' if len(d) < 300 else ('CODE I CONFIRME' if ok else 'NON CONFIRME'))
print('DECODE', ' '.join((key.get(g) or '‹%d›' % g) for g in groups))
