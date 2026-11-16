# -*- coding: utf-8 -*-
"""C13 — mesure UNIQUE de la table v5 sur la portion neuve (gelé avec PREREG-C13.md).

Usage : python3 -I measure_c13.py TABLE.json TRANSCRIPTION.json REFERENCE.json OUT.json
- TRANSCRIPTION.json : {"signs": [{"id": "...", "code": "..."}]}  (transcription arbitrée, gelée)
- REFERENCE.json     : {"signs": [{"id": "...", "ref": "<valeur>" | "DET" | "?"}]}  (référence informée, faite APRÈS le gel)
Mesure M = part des signes de référence à valeur non-DET et non-? (valeurs phonétiques + PL) dont la valeur
de référence appartient à l'ensemble de valeurs que donne la table (après équivalences déclarées).
Témoins : 200 tables où les ensembles de valeurs sont permutés entre les codes présents dans la portion
(graine 20261116). Seuil (écrit avant) : succès si M >= 0.70 ET M >= max(témoins) + 0.30.
"""
import json, random, sys, unicodedata

def norm_factory(eqs):
    rep = {}
    for grp in eqs:
        for ch in grp:
            rep[ch] = grp[0]
    def norm(v):
        v = unicodedata.normalize('NFC', v.strip())
        if v in ('PL', 'DET', '?'):
            return v
        v = v.replace('.', '').replace('=', '').replace('-', '')
        return ''.join(rep.get(c, c) for c in v)
    return norm

def values_for(table, code):
    if code in table['subst']:
        return table['subst'][code]['v']
    return table['ordinaire'].get(code, [])

def score(mapping, items, norm):
    ok = sum(1 for code, ref in items if norm(ref) in {norm(x) for x in mapping.get(code, [])})
    return ok / len(items) if items else 0.0, ok

def main():
    table = json.load(open(sys.argv[1], encoding='utf-8'))
    tr = {s['id']: s['code'] for s in json.load(open(sys.argv[2], encoding='utf-8'))['signs']}
    ref = {s['id']: s['ref'] for s in json.load(open(sys.argv[3], encoding='utf-8'))['signs']}
    norm = norm_factory(table['equivalences_mesure'])
    items = [(tr[i], r) for i, r in ref.items() if i in tr and r not in ('DET', '?')]
    codes = sorted({c for c in tr.values()})
    mapping = {c: values_for(table, c) for c in codes}
    M, ok = score(mapping, items, norm)
    cover = sum(1 for c in tr.values() if mapping[c]) / len(tr)
    rng = random.Random(20261116)
    wit = []
    vals = [mapping[c] for c in codes]
    for _ in range(200):
        v = vals[:]
        rng.shuffle(v)
        wit.append(score(dict(zip(codes, v)), items, norm)[0])
    best = max(wit)
    res = {'M': round(M, 4), 'justes': ok, 'n_scores': len(items), 'n_signes': len(tr),
           'couverture_table': round(cover, 4), 'temoins_max': round(best, 4),
           'temoins_moyenne': round(sum(wit) / len(wit), 4),
           'seuil': 'M >= 0.70 et M >= max(témoins) + 0.30',
           'succes': bool(M >= 0.70 and M >= best + 0.30)}
    # détail par signe (diagnostic, ne change pas la mesure)
    res['detail'] = [{'id': i, 'code': tr[i], 'table': mapping[tr[i]], 'ref': r,
                      'juste': norm(r) in {norm(x) for x in mapping[tr[i]]}}
                     for i, r in ref.items() if i in tr and r not in ('DET', '?')]
    json.dump(res, open(sys.argv[4], 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(json.dumps({k: v for k, v in res.items() if k != 'detail'}, ensure_ascii=False))

if __name__ == '__main__':
    main()
