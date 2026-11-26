# RESULTAT-O4 — stmauris1548 (cible WAINUT), lettre du 12 mars 1548, cc. 5r + 5v + 6r — 25/11/2026, Claude Opus 5.5 (fil 🔓)

**Verdict : FAIL** (M 0,780 < 0,85). Mesure unique, faite une seule fois, selon PREREG-O4 (SHA f95a74e4…, vérifié avant toute action).
Brice : « lance » (25/11), y compris les descriptions de formes WAINUT (input/SHAPES-KEY-NAMES.md) à la place du bloc de conventions de c. 1r.

## Chaîne (horodatée, 25/11)
| heure | étape | fichier | SHA-256 |
|---|---|---|---|
| 10:05 | préenregistrement (vérifié) | PREREG-O4.md | f95a74e4af6dde254bdfa17daa2e03134b7653ad706c9c3ae9a6f3a5b5a8ba7a |
| — | entrées revérifiées = PREREG | SIGNS.md 678be0a4…, SHAPES-KEY-NAMES.md 107506b1…, BRIEF-PASSE-O4.md a1c7b711…, measure_o4.py f940b354…, wainut-key.tsv b9e69238…, compare.py 364d8233…, corpus 813012bd…, c05r bc867847…, c05v cc17c276…, c06r 5b206984… | |
| 10:12:23 | outil de découpe (avant la passe A) | tools/make_crops_o4.py | 49138df631fb988b1762d9da7797f7b9f97d3554efbbc247b87581c7245f5856 |
| 10:12 | 216 recadrages (71 lignes ×3 + 3 vues d'ensemble) | CROPS.sha256 (liste) | — |
| 10:25:48 | passe A (agent Opus neuf, aveugle) | passe-A/transcription_passA.txt | 2459fac4f204b8d64230626da8057c2082f0a1356506276c942594090a35b5fa |
| 10:24:38 | passe B (agent Opus neuf, aveugle, sans accès à A) | passe-B/transcription_passB.txt | 037e227a724b280dae90b4ad9f81f31c8ad8e01583358f900821e3d25a8e9c30 |
| 10:26:11 | comparaison A/B (après gel des deux passes) | COMPARAISON-AB.txt (tools/compare_o4.py b8037565…) | 1525e12545533b730c67b4e7044f7297d3e6ead260be97f83565ea64159e0a26 |
| 10:26 | paquet d'arbitrage (sans valeurs) | ARBITRAGE/disputes.json 5d38d642…, CANDIDATS-DESCRIPTIONS.md 0190673d… (tools/arb_package_o4.py ab60deb4…) | |
| 10:35 | arbitrage aveugle (3ᵉ agent Opus neuf) | ARBITRAGE/ARBITRAGE.tsv | ea65722193bc072982fdb8f1766a9d9d5213c818f81114b866703e0593400066 |
| 10:35:07 | transcription fusionnée GELÉE avant décodage | transcription_1548-03-12_P_merged.txt (tools/merge_o4.py 8491108d…) | b6aee4f022f46e49a14c440ad5889086ceb3e33901fd5a06694dda3d12243d7d |
| 10:35:15 | garde de measure_o4.py : ABORT avant décodage (13, @2, N6o, mx3) | — | — |
| 10:35:25 | étape de nommage consignée (17 jetons → tS-…) | transcription_1548-03-12_P_merged_named.txt (tools/name_step_o4.py e6ebe9fc…) | e6c62d5b4adf75a0dc9ab7909a7210e63d8128ca27bce960e3eb6b038b6a787b |
| 10:35:26 | **mesure unique** (graine 120348) | MESURE-O4.txt / MESURE-O4.json | 583744a3… / ff605e63… |

Commande : `python3 -I tools/measure_o4.py transcription_1548-03-12_P_merged_named.txt ../o2-2311/wainut-key.tsv ../../../_shared/cyphersolver/lang/corpora/fr-1520s-diplomatic.txt 120348`

## Chiffres
- Portion P : 71 lignes (5r L01-L14 : 3 lignes en tête, partielles, + 11 en bas ; 5v L01-L30 ; 6r L01-L27). 1 486 jetons après fusion (hors ponctuation).
- **Accord A/B : 0,926** (1 377/1 487 positions alignées, 104 désaccords) ≥ 0,80 → on continue. Désaccords surtout des noms `t` propres à chaque passe (tous des désaccords par construction) : tA-t2/phi ×24, tA-t4/tB-t2 ×15, tA-t5/tB-t4 ×10, fs/fz ×9, tA-t3/dd ×7.
- Arbitrage : A 68, B 34, « ni l'un ni l'autre » 2 (→ NIL). 5 égalités entre deux noms `t` de même description données à A (sans effet : aucun nom `t` ne donne de lettre).
- **Règle de taille** : 1 382 jetons à nom de clé ≥ 340 → **aucune extension** ; la réserve R (6v, 7r, 7v, 8r, 8v) n'a été ni recadrée ni ouverte.
- **Mesure** : 1 382 jetons avec valeur (93,0 %), 1 409 lettres décodées ; **M = 0,7800** ; témoins (200 permutations, graine 120348) max **0,4146**, moyenne 0,2310, écart-type 0,0651 ; marge 0,3654 ; **z = 8,43** (information seulement).
- Critères : lettres ≥ 300 OUI ; M ≥ 0,85 **NON** ; M ≥ max témoins + 0,30 OUI → **FAIL**.

## Conséquence (PREREG-O4 §6, appliqué tel quel)
Rien sur cc. 5r-6r n'est un texte validé ; le décodage reste une donnée (MESURE-O4.txt). **cc. 5r, 5v, 6r sont grillées** pour un test.
La réserve R (cc. 6v-8v) reste neuve (non ouverte) pour un éventuel O5 avec son propre PREREG. Aucune PR, rien posté, envoyé ni publié.

Observation (non validée, hors critère, ne change pas le verdict) : le décodage des 3 premières lignes de 5r donne une phrase
française suivie (« comme l'on en avoit … fait grand cas en vous … imputant le tort »). Elle semble correspondre à la note en clair
de la marge de 5r (exclue de la portion et non lue par l'orchestrateur ; seule sa présence était connue par le profil WAINUT). Si
cette note est un déchiffrement d'époque, c'est un indice indépendant fort que la clé est juste ; à vérifier par Brice / par sens,
sans rien changer au FAIL. Comme en O2 et O3, l'échec tient au seuil absolu M ≥ 0,85 (orthographe du XVIᵉ s., lexique limité,
104 jetons sans valeur), pas aux témoins (marge 0,37, z 8,4). Trois mesures (0,718 / 0,784 / 0,780) restent sous 0,85 : le seuil
absolu de ce protocole semble hors de portée pour cette clé sur ce corpus, quel que soit le soin de transcription.

## Points d'exécution déclarés (aucun ne touche la clé, measure_o4.py, la graine ni les seuils)
1. **Lignes inclinées** : les lignes de 5r (bas) penchent d'environ 3° ; chaque ligne est donnée par son centre à gauche et à droite
   (ajustement par profil d'encre sur pages réduites + contrôle visuel de lignes-guides) et redressée par cisaillement affine.
   Demi-hauteur 100 px (lignes voisines partiellement visibles, consigne « ignorez-les »).
2. **Clair masqué sur 5r** : tout ce qui n'est pas ligne chiffrée (texte en clair, note marginale, mots en clair avant L01 et après L03)
   est peint en blanc AVANT découpe ; quelques hampes descendantes du clair au-dessus de 5r L04 restent visibles à droite.
   L'orchestrateur a vu le clair en vignette réduite pour placer les lignes, sans le transcrire ni s'en servir.
3. Le PREREG dit « ⩾ 300 letters » et « < 340 jetons » : 1 382 → sans objet.
4. Nommage : `13`, `@2`, `N6o`, `mx3` (composés base + marque haute de SIGNS.md / SHAPES-KEY-NAMES.md, sans ligne dans key.tsv)
   ont fait ABORT la garde ; renommés `tS-…` (17 jetons, aucune lettre) dans une étape consignée, comme prévu au §4. La fusion gelée
   b6aee4f0… n'est pas modifiée ; le fichier mesuré en est une copie qui ne diffère que par ce préfixe (vérifié par diff).
5. Arbitrage : comme en O3, l'agent C a lui-même localisé et encadré chaque position (ARBITRAGE/boxes → SPOF_2) à partir du rang et du
   contexte. Les descriptions des noms `t` des passes ont été copiées de leurs en-têtes (renommées tA-/tB-).
6. Images : scans, recadrages, vignettes (preview/) et cases d'arbitrage sur SPOF_2 seulement (liens symboliques `crops`, `preview`,
   `ARBITRAGE/boxes`) ; zooms temporaires des agents effacés ; licence CC BY-NC-SA, rien republié.
7. Le chemin `../PROGRAMME-RELECTURES-2311.md` de la consigne est en fait `dechiffrements-europe/PROGRAMME-RELECTURES-2311.md` ; ligne ajoutée là.
