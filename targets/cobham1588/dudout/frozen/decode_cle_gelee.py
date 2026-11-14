#!/usr/bin/env python3
"""Codes = nombres à 2 chiffres et plus, ◻, [..] ou ·x· ; un 7 ou 8 isolé est un SIGNE-LETTRE (noter un code 7 comme [7]).
(13/11 : correctif — les {a|b} ne sont plus coupés par le séparateur de mots.)
Décodage brut à la clé GELÉE (cle_R8489_f78r.tsv, valeur principale) + valeurs dérivées de R8490 (cle_R8490_derivee.tsv) en alternatives.
Usage : python3 -I decode_cle_gelee.py R849x_chiffre.tsv > R849x_decodage_cle_gelee.txt
Sortie par passage : signes ; décodage principal (une lettre par signe, '?' = signe hors clé, codes entre crochets) ; ensembles de valeurs par signe."""
import sys, re, os, hashlib
here = os.path.dirname(os.path.abspath(__file__))
def load(fn):
    return open(os.path.join(here, fn), encoding='utf-8').read().splitlines()
prin, sets = {}, {}
for l in load('cle_R8489_f78r.tsv'):
    if l.startswith('#') or l.startswith('signe') or not l.strip(): continue
    s, v, e, n = l.split('\t')[:4]
    prin[s] = v; sets[s] = e.split(',')
for l in load('cle_R8490_derivee.tsv'):
    if l.startswith('#') or l.startswith('signe') or not l.strip(): continue
    f = l.split('\t'); s, v = f[0], f[1]
    if s not in prin: prin[s] = v
    sets.setdefault(s, [])
    if v not in sets[s]: sets[s].append(v)
for fn in ('cle_R8489_f78r.tsv', 'cle_R8490_derivee.tsv'):
    print('# %s sha256 %s' % (fn, hashlib.sha256(open(os.path.join(here, fn), 'rb').read()).hexdigest()))
src = sys.argv[1]
print('# source %s sha256 %s' % (src, hashlib.sha256(open(src, 'rb').read()).hexdigest()))
hdr = None
for l in open(src, encoding='utf-8'):
    l = l.rstrip('\n')
    if not l or l.startswith('#'): continue
    f = l.split('\t')
    if hdr is None: hdr = f; ci = hdr.index('chiffre'); continue
    pid, ch = f[0], f[ci]
    words = [w.strip() for w in re.split(r'\|(?![^{]*\})', ch)]
    outp, outs = [], []
    for w in words:
        toks = re.findall(r'\{[^}]*\}|·[^·\s]+·|\[[^\]]*\]|\S+', w)
        p, st = '', []
        for t in toks:
            if t.startswith('{'):
                alts = t[1:-1].split('|')
                vs = sorted({x for a in alts for x in sets.get(a, ['?'])})
                p += prin.get(alts[0], '?'); st.append('/'.join(vs))
            elif t.startswith('·') or t.startswith('[') or (t.isdigit() and len(t)>1) or t=='◻':
                p += '[%s]' % t; st.append(t)
            else:
                p += prin.get(t, '?'); st.append('/'.join(sets.get(t, ['?'])))
        outp.append(p); outs.append(' '.join(st))
    print('%s\t%s\n\tprincipal : %s\n\tensembles : %s' % (pid, ch, ' | '.join(outp), ' | '.join(outs)))
