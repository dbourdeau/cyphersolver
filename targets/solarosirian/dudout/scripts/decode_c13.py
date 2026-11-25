# -*- coding: utf-8 -*-
"""C13 — décodage mécanique de la transcription arbitrée par la table v5 gelée (aucune valeur ajoutée).
Usage : python3 -I decode_c13.py TABLE.json TRANSCRIPTION.json OUT.md"""
import json, sys
t = json.load(open(sys.argv[1], encoding='utf-8'))
tr = json.load(open(sys.argv[2], encoding='utf-8'))['signs']
def val(c):
    if c in t['subst']: return '/'.join(t['subst'][c]['v'])
    return '/'.join(t['ordinaire'].get(c, [])) or '?'
units = {}
for s in tr: units.setdefault(s['unit'], []).append(s)
L = ['# C13 — décodage mécanique (table v5 gelée)', '', 'Forme [valeur] ; ? = pas de valeur dans la table.', '']
nv = 0
for u, ss in units.items():
    L.append(f"- **{u}** : " + ' · '.join(f"{s['code']} [{val(s['code'])}]" for s in ss))
    nv += sum(1 for s in ss if val(s['code']) != '?')
L += ['', f'Signes : {len(tr)} ; avec valeur : {nv} ({nv/len(tr):.0%}).']
open(sys.argv[3], 'w', encoding='utf-8').write('\n'.join(L) + '\n')
print(len(tr), nv)
