"""Construit le corpus suédois ancien (indépendant de F 470) pour le modèle n-grammes.
usage: corpus.py <carlson_djvu.txt> <ws_dir> <outdir>
- Carlson 1893 : bloc <pre>…</pre> ; lignes de notes (commençant par chiffre+espace), lignes entre [ ], lignes d'en-tête « N:r » écartées.
- sv.wikisource (lexique/ws) : page gardée si orthographe ancienne (part de w parmi w+v ≥ 0,5 ET ≥ 2000 lettres).
- normalisation : minuscules ; é/è→e, ü→y, v→w ; dh→d ; gh en fin de mot→g ; seules lettres a-z å ä ö gardées, mots collés (pas d'espace).
- découpage en blocs de 2000 lettres : 1 bloc sur 10 → held-out (calibration), le reste → entraînement."""
import sys, os, re, unicodedata
def norm_words(t):
    t = t.lower().replace('é','e').replace('è','e').replace('ü','y').replace('v','w')
    ws = re.findall(r'[a-zåäö]+', t)
    out = []
    for w in ws:
        w = w.replace('dh','d')
        if w.endswith('gh'): w = w[:-1]
        out.append(w)
    return ''.join(out)
src = open(sys.argv[1], encoding='utf-8', errors='ignore').read()
m = re.search(r'<pre>(.*)</pre>', src, re.S); txt = m.group(1)
keep = []
for line in txt.split('\n'):
    s = line.strip()
    if not s: continue
    if re.match(r'^\d+\s', s) or s.startswith('[') or s.startswith('N:r'): continue
    keep.append(s)
carl = norm_words('\n'.join(keep))
ws = ''
for f in sorted(os.listdir(sys.argv[2])):
    if not f.endswith('.txt'): continue
    t = open(os.path.join(sys.argv[2], f), encoding='utf-8', errors='ignore').read()
    t = re.sub(r'<[^>]+>|\{\{[^}]*\}\}|\[\[[^\]|]*\||\]\]|\[\[', ' ', t)
    low = t.lower(); nw = low.count('w'); nv = low.count('v')
    s = norm_words(t)
    if len(s) >= 2000 and nw + nv > 0 and nw / (nw + nv) >= 0.5: ws += s
allt = carl + ws
tr, ho = [], []
for i in range(0, len(allt), 2000):
    (ho if (i // 2000) % 10 == 9 else tr).append(allt[i:i+2000])
os.makedirs(sys.argv[3], exist_ok=True)
open(os.path.join(sys.argv[3], 'corpus_train.txt'), 'w').write('\n'.join(tr))
open(os.path.join(sys.argv[3], 'corpus_heldout.txt'), 'w').write('\n'.join(ho))
print('carlson', len(carl), 'ws', len(ws), 'train', sum(map(len, tr)), 'heldout', sum(map(len, ho)))
