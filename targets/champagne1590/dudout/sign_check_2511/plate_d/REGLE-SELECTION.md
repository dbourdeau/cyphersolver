# Règle de sélection — planche « champagne1590-2711d », écrite AVANT les vignettes (28/11/2026, agent Opus 5.5, fil 🔓)

Demande de Brice (27/11 ~22 h 30, relayée par le coordinateur) : planche d sur le no 24 (lu[y], au[o]it, [?Paris]),
le no 60 (Launan) et les cibles restées ouvertes du no 25 (T3, T5, T7), ≤ 15 questions. Mêmes images (Gallica IIIF
btv1b525245007 : f85 = no 25, f83 = no 24, f185 = no 60), recadrages et clé sur SPOF_2 seulement.
Noyau : `PLANCHES/_outils/planche_core.py` v2 copié tel quel (sha256 0c605bc9…) ; il utilise PIL (déclaré ici).

## Planche-contact (faite avant ce hachage)
`scripts/contact.py` : chaque cadre de `scripts/boxes.py` avec 30 px de marge, ×3, cadre rouge. Vus un à un, cibles et
contrôles compris. Corrigés avant le hachage : D1 et T7 (bord droit sur la lettre suivante), b_b, v_b, n3_b, l_b, c_c
(décalés), p3_a/p5_a/p5_b/k8_b/q_b/y_b/fl_c (d'abord sur le mauvais signe), y_a remplacé par y_c (« ay » en ligature),
c_d abandonné (« cela » non trouvé). Cible O1 (inciter/inviter) abandonnée : le signe décisif est un petit trait qu'un
cadre ne sépare pas des jambages voisins.

## Ce qui a été écarté, et pourquoi (avant toute vignette)
- **lu[y]** : le 99 avant le 9̄ est un 9 net (pas 96 = y) ; le y n'existe que comme glose au-dessus de 99. Aucune forme
  du chiffre ne fournit le y : non décidable par une planche de formes.
- **T2 de la planche a** (forme du dernier chiffre « 64 » du no 60) : 6 et 4 nets ; rien à gagner. Reste la glose (N60).

## Cibles (9)
| code | lieu | options (exemples) | effet |
|---|---|---|---|
| D1 | no 24 l.12, 2ᵉ signe de « Lbm » (marge/début de ligne) | b (bruict, combien) · v (voiage, vous) | v → « lviij » = 58 = Paris (feuille de clé, villes lviii-…, Beling) → [?Paris] **sûr**, +1 mot chiffré no 24 ; b → rien ne change (lecture par convention, reste probable) |
| D2 | no 24 l.23, 1ᵉʳ chiffre de « 05 » (avec le trait qui monte vers la glose) | 0 (5000 ×2, 1590) · 6 (86, 16) | 6 → 65 = o → « auoit » chiffré en entier ; 0 → au[o]it reste restitué |
| D3 | no 24 l.23, glose au-dessus de « 05 » | glose o (au-dessus de 67, no 24 l.9 et no 60 l.1) · 2 (de 92 no 24, de 62 no 60) · glose a (au-dessus de 35 no 24, de 32 no 60) | glose o → le déchiffreur lisait o : au[o]it → {probable} documenté (pas de gain au compte, comme Launan) ; sinon rien |
| T3 | no 24 l.9, 1ᵉʳ chiffre du 5ᵉ groupe « 36/56 » (cadre inchangé) | 3 (no 25 : 43, 93 ; no 60 l.5 : 39, 43) · 5 (no 60 l.5 : 56, 35) — **exemples neufs**, aucun du no 24 | 5 → « Ludouic » confirmé, désaccord avec c (3) noté, T3 reste ouvert ; 3 → 4ᵉ « 3 », reste signalé, non appliqué |
| N60 | no 60 l.5, glose au-dessus du dernier chiffre (64) | glose n (au-dessus de 62, **même ligne**, nouvel exemple ; au-dessus de 64 no 25 l.27) · y (no 24 « il y a », no 25 « roy ») | n → la glose s'accorde à la clé → « Launan » ; y → conflit glose/clé maintenu |
| T5 | no 25 l.8, deux premières lettres (cadre inchangé) | pl (no 24 « plustost » neuf ; no 25 « plus ») · fl (no 25 « flandre » neuf ; « Conflans ») | pl → « platines » ; fl → « flatteries » |
| T7 | no 25 l.27, initiale (cadre resserré : bord droit avant le r) | c (no 24 « combien » neuf ; no 25 « cestuy ») · t (no 24 « tesmoigner », « tort », neufs) | c → « croions » ; t → « treuvons » |
| O2 | no 25 l.17, initiale « Or quoy / De quoy » | O (no 24 « Or de vous dire ») · D (no 24 « Du 15 juin », no 25 « De flandre ») | O → « Or quoy » (Beling) ; D → « De quoy » (Brackx) ; clair seulement |

## Contrôles cachés (3), neufs, aucun r, signes isolés et nets, options sans sosie (vérifiées à ×3)
| code | cadre | attendu | options (exemples) |
|---|---|---|---|
| K1 | no 24 l.23, 4 de « 54 » | 4 | 4 (45 no 24 l.9, 94 no 60) · 2 (92 no 24, 62 no 60) · 9 (39, 93 no 25) |
| K2 | no 24 l.9, 8 du 1ᵉʳ « 38 » | 8 | 8 (2ᵉ 38 no 24 l.9, 38 no 60 l.5) · 1 (16 no 24 l.23, 15 no 24 l.50) · 7 (67 no 24 l.9, 75 no 25 l.30) |
| K3 | no 25 l.17, q de « quoy » | q | q (« que » no 25 l.17, « qui » no 24 l.14) · l (« le » no 24 l.11, « le » no 25 l.42) · t (« tenons », « tenez » no 25) |
Places : réparties par le noyau v2 (contrôles à des places deux à deux différentes, références équilibrées ; build()
refuse sinon). Graines : ordre des questions 27111, ordre des options 27112.

## Critères d'intégration (écrits avant toute réponse)
1. **Contrôles : 3 sur 3.** Réussi = forme attendue choisie et aucune remarque qui conteste la valeur. Sinon rien n'est
   intégré (réponses notées seulement).
2. **Réponse concluante** = une seule forme choisie, aucune remarque qui la contredit ; « aucune / autre forme »,
   « illisible », « pas un signe », ou remarque « entre deux signes » = non concluante.
3. **Planches antérieures** : a et b (contrôle manqué chacune) ne servent plus de condition ; la planche c (valide, 3/3)
   reste condition de concordance pour T3, T5, T7. Cible reposée : compte si d concluante = c. Désaccord c/d : ne compte
   pas, noté.
4. **Cibles neuves** (D1, D2, D3, N60, O2) : une réponse concluante sur d suffit, SAUF si elle va contre la lecture de
   tous ceux qui ont regardé l'image (même règle que T3) : alors elle est **signalée, non appliquée**, second regard exigé.
   Concrètement : D1 = v suit la piste de Beling (« possibly lviij = Paris ») → appliqué. D2 = 6 contredit « 05 »
   (Beling + vérification d'intégration 25/25 chiffres) → signalé. N60 = n contredit « dotted y » (Beling, coordinateur)
   → signalé. T3 = 3 → signalé (contre les deux lecteurs). O2, T5, T7 : clair, l'une des deux lectures → appliqué.
5. Application avec la mention « relecture aveugle sur forme, Brice Dudout, planche 2711d » ; recompte selon la règle de
   Daniel (mots chiffrés ; sûrs, {probables}, [restitués], ‹irrésolus›) avant toute PR ; rien poussé sans accord.

## Compte (mots chiffrés), écrit à l'avance
Avant : profil 40/46 = 0,870 ; avec la PR #1029 (planche c, ouverte) 41/46 = 0,891 (no 25 21/22 ; no 24 18/21 ; no 60 2/3).
- Appliqué directement si D1 = v : no 24 18 → 19/21 (90,5 %) ; document 41 → 42/46 (0,913).
- Signalés (second regard) : D2 = 6 → no 24 20/21 (95,2 %) ; N60 = n → no 60 3/3 ; maximum théorique 44/46 = 0,957.
- T3 = 5 ou 3 : aucun mot ne change d'état sur cette planche (Ludouic reste lu ; 3 reste signalé).

## Page
Page autonome (base64), vignettes JPEG du noyau, sortie `reponses-champagne1590-2711d.json` (téléchargée + copiée),
copies `_planches-tel/99-champagne1590-d.html` et `_planches-serve/champagne1590-2711d/planche.html`. Clé privée :
SPOF_2 `planches-pistes-2511/champagne1590/prive/cle-PRIVEE-d.json` ; recadrages : `…/champagne1590/build-d/crops/`.
