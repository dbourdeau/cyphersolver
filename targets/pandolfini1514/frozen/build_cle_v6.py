#!/usr/bin/env python3
"""Construit cle/CLE_v6.json = fusion déclarée de CLE_v5a (16a6d2de…) et CLE_v5b (9d5cf3d5…) + arbitrage (ARBITRAGE-v6.md).
Lit v5a et v5b sans les modifier. usage: python3 -I scripts/build_cle_v6.py"""
import json, hashlib, collections
D = '/Users/bdudout/Documents/Veille cyber/dechiffrements-europe/pandolfini-francia-1514-15/cle/'
def load(n):
    b = open(D + n, 'rb').read()
    return json.loads(b), hashlib.sha256(b).hexdigest()
a, ha = load('CLE_v5a.json'); b, hb = load('CLE_v5b.json'); v4, h4 = load('CLE_v4.json')
assert ha.startswith('16a6d2de') and hb.startswith('9d5cf3d5') and h4.startswith('1848f692')
assert a['base'] == b['base'] == v4['base'] and a['vowels'] == b['vowels'] and a['codes'] == b['codes']
tok = collections.OrderedDict(v4['tokens'])
conflits = {}
for k in sorted(set(a['tokens']) | set(b['tokens'])):
    va, vb = a['tokens'].get(k), b['tokens'].get(k)
    if va is not None and vb is not None and va != vb:
        conflits[k] = (va, vb)
# arbitrage (ARBITRAGE-v6.md)
arb = {'α': 'per', '4#': 'll'}
assert set(conflits) == set(arb), conflits
for k in list(a['tokens']) + list(b['tokens']):
    tok[k] = arb.get(k, a['tokens'].get(k, b['tokens'].get(k)))
k6 = collections.OrderedDict()
k6['_source'] = ("CLE v6 = FUSION DÉCLARÉE (09/11/2026, agent arbitrage) de CLE_v5a.json (16a6d2de…, agent 307/309) et CLE_v5b.json "
  "(9d5cf3d5…, agent 311/333), toutes deux dérivées déclarées de CLE_v4 (1848f692…) ; v3 (ae5f0b9f…, seule clé gelée), v4, v5a, v5b "
  "NON modifiées. Union des valeurs ; deux conflits tranchés par ARBITRAGE-v6.md (α, 4#) ; aucune valeur nouvelle hors arbitrage. "
  "AUCUNE valeur n'est validée par une mesure : statut de la clé = PARTIEL (P03bis). Construite par scripts/build_cle_v6.py.")
k6['vowels'] = a['vowels']; k6['base'] = a['base']; k6['codes'] = a['codes']; k6['tokens'] = tok
k6['_regles'] = b['_regles'] + " v6 : appliquer _contexte_machine (scripts/decode_v6.py) avant la valeur par défaut."
k6['codes_contexte'] = a['codes_contexte']
k6['_contexte_machine'] = collections.OrderedDict([
  ('O + r nu', "O suivi de r NU → c (digramme ch) (v5b)"),
  ('2^5 y 3…', "2^5 devant « y 3^x » (bande/bandi) → ba ; ailleurs ca (v5a + v5b)"),
  ('.4.', "maesta si le décodé précédent finit par « a » OU si les 3 jetons précédents sont « S^4 6 8 » / « S^4 6 8^5 » (questa) ; sinon cristianissimo (v2 + v5b)"),
])
k6['_alternatives_non_appliquees'] = collections.OrderedDict([
  ('0 + 8 = tt (règle v5b, NON reprise)', "ARBITRAGE-v6.md § 4 : 0 = c partout ; « c t » est la graphie latinisante de chancellerie (tucto, decto, mactina, lectera, intractengono ; cf. clairs 343 « effecti », « predecte », 341 « satisfactione ») : même mot, seule la graphie du décodé change"),
  ('2^3 = bi', "bianca (311 A4), dubio (307 L18) ; défaut ci (amici, sollicitano)"),
  ('2 + voyelle = b + voyelle', "signe 2 polyphone b/c (v5a + v5b) : bo dans bona/bono (311), bi dans dubio (307), bu dans buon (307) ; décision par le sens à la lecture"),
  ('O + 8 = ct', "facto, auctorità (311) ; contre : « r^1 O 8^4 » = suo te(nessi) (v5b)"),
  ('9^4 = ze', "Svizero, forze (307, note v5a) ; contre : 9^4 G# W 3 = veggia (309)"),
  ('5 nu = h', "v4, non appliquée"),
  ('A (Δ) nu = a', "v5a, non tranché"),
  ('α = et', "REJETÉE (ARBITRAGE-v6.md) : α ≡ P = per, attesté par trois clairs d'époque ; aucune occurrence n'exige « et »"),
  ('4# = gg', "REJETÉE (ARBITRAGE-v6.md) : 4# = ll (333 ↔ 332, 342 ↔ 343) ; 4# et G# sont deux signes distincts"),
])
k6['_conflits_v5a_v5b'] = {k: {'v5a': va, 'v5b': vb, 'v6': arb[k]} for k, (va, vb) in conflits.items()}
k6['_attestations'] = v4['_attestations']
k6['_attestations_v5a'] = a['_attestations_v5a']
k6['_attestations_v5b'] = {k: v for k, v in b['_attestations'].items() if k not in v4['_attestations']}
k6['_regles_contexte_v5b'] = b['_regles_contexte']
k6['_arbitrage_v6'] = collections.OrderedDict([
  ('α = per (≡ P)', "Le signe α (a fermé à queue, ∝) est le signe déjà noté « P » dans T (318 gloss « P D^n 8^2 = per conto »), 340, 342 et 346 "
   "(vérifié sur l'image 346 c. 441r : même forme ; note de forme de H4_342 : « α (signe « per ») = P comme en 340 »). Clairs d'époque : "
   "346 ↔ 345 « per lo incontro de Svizeri », « per ancora non si tirono », « per aspettare », « per volersi », « per potere », « per sua parte » ; "
   "342 ↔ 343 « per certo », « per intendere », « per succedere » ; 340 ↔ 341 « per le ultime ». Lettres nues : 311 ×18 (dont « et α » = « et per » ×3, "
   "et « sa-α-e » = sapere à l'intérieur d'un mot, qui excluent « et »), 307 ×6, 309 ×1, tous lisibles « per ». Pas d'homophonie démontrée (1 seul cas, 307 L16, où « et » se lirait mieux). Sûr."),
  ('4# = ll ; G# = gg (deux signes)', "4# (« 4 » anguleux + #) = ll : 333 ×3 ↔ 332 « dalle bande di qua » ; 342 L2 « 4? Q 2^5 y^4 » ↔ 343 « dalle bande » (# non vu, appui faible) ; "
   "322 L8, 311 ×16 (dont 3 où « ll » ne donne pas le mot : C9 accidente, C12, C13 — confusion de forme ou gl, déclarée). G# (δ fermé + #) = gg : 309 B1 ve-gg-ia (1 attestation, forme vue sur l'image, ronde, distincte de 4#). v5a n'a jamais "
   "rencontré 4# (absent de 307/309) ; v5b n'a jamais rencontré G# (absent de 311/333) : pas de conflit réel, seulement l'héritage 4# = gg de v4."),
  ('0 + 8', "v5a : 0 = c ; v5b : 0 devant 8 = t. Tranché pour v5a (graphie ct = tt d'époque) ; aucun mot ne change."),
  ('2 = b ou c', "Accord v5a/v5b : défaut c (ca, ce, ci, co, cu) ; b par le sens (bande par règle de contexte ; bona, bono, buon, bon, dubio en lecture)."),
])
json.dump(k6, open(D + 'CLE_v6.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('conflits', conflits)
print(hashlib.sha256(open(D + 'CLE_v6.json', 'rb').read()).hexdigest())
