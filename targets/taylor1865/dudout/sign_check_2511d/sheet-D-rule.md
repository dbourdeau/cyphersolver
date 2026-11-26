# Règle de sélection — planche « Taylor (d) » (taylor1865-2511d, n° 60) du 25/11/2026, écrite AVANT toute vignette

Pièce : NARA RG 109 ch. II vol. 196 (naId 45485022), frame 0018, MS p. 31 : Taylor à Beauregard, Meridian, 10 février 1865
(`v196-0018-beauregard`). Image publique NARA (SPOF_2 taylor-1865/images/, lien symbolique). Suite de la planche 2411-a (contrôles 3/3,
intégrée ; 0018 = 28/44 mots sans [?]). Étape 0 (25/11, `gh pr list --state open --search taylor1865`) : seule #963 (Daniel), qui ne
touche pas taylor1865 ; #950 (la nôtre, planches 2411-a/b/c) mergée. Cible de tiers (Payne/« nov1 », intégrée par Daniel) : résultat PROPOSÉ avec crédit.

Type : (b) alphabet (E/F/F2, I/L, N/M, R/V, G/S, C/E, I/G, Z/E). **Gain maximal : 11 mots** (12 glyphes ; MOBILE en demande 2) →
28/44 → 39/44 mots sans [?]. Le télégramme fait < 300 caractères chiffrés : **aucune bascule en « lu » au sens de la règle des 95 %**
(portion trop courte) ; le gain est un gain de mots et d'alphabet.

## Segmentation
Les groupes g26-g49 n'avaient pas de boîtes : segmentés le 25/11 à l'œil sur quadrillages (work/planche-2511d/v/, privés), boîtes en
coordonnées image 7699 × 5645 dans scripts/boites_2511d.json. Boîtes g1-g25 reprises de 2411-a (boites_v196-0018.json) ; la boîte gA p5
de 2411-a est décalée d'une lettre (elle tombe sur le N) → recalculée ici. Clé non consultée pour juger les formes.

## Cibles (12) = lettres où le glyphe lu (raw_candidate) diffère de la reconstruction par la clé (nov1_alignment.tsv)
| code | lieu | mot | lu / clé | boîte | options |
|---|---|---|---|---|---|
| Z5 | g5p1 | BRIGADES | E / Z | (4515,1040,4578,1082) | Z / E |
| G14 | g14p2 | RETURNING | I / G | (6975,1415,7034,1458) | I / G |
| CE23 | g23p5 (gA) | LITTLE | C / E | (6094,1974,6160,2022) | C / E |
| GS27 | g27p2 | SERVICE | G / S | (6558,2100,6620,2148) | G / S |
| TF29 | g29p2 | MOBILE | T / F | (4598,2263,4666,2312) | T / F / E |
| EF29 | g29p5 | MOBILE | E / F | (4815,2262,4870,2310) | E / F / F2 |
| RV31 | g31p1 | QUICKER | R / V | (4528,2402,4598,2448) | R / V |
| IL32 | g32p2 | THAN | I / L | (4840,2398,4902,2445) | I / L |
| NM34 | g34p1 | SENT | N / M | (5468,2396,5598,2440) | N / M |
| EF35 | g35p4 | EAST | E / F | (6255,2390,6332,2435) | E / F / F2 |
| IL37 | g37p1 | BUT | I / L | (6612,2390,6682,2432) | I / L |
| IL48 | g48p3 | FURLOUGHS | I / L | (6512,2665,6575,2710) | I / L |
Écartées : AND g2p1-2 (deux glyphes pour un mot, D/B et N/H ne sont pas des formes jumelles) ; OF g19p1 (N/W, formes sans parenté).

## Formes (exemples réels de ce clerc dans ce télégramme, lettres sûres par la clé, jamais une cible ni un contrôle)
E = g8p4, g22p1 ; F = g8p5, g25p1 (gC p1) ; F2 = g4p1 seul (alphabet corrigé du 24/11, sans valeur) ; T = g18p4, g3p4 ;
I = g4p2, g22p3 ; L = g8p2, g8p9 ; N = g3p3, g6p2 ; M = g1p3, g4p3 ; R = g1p4, g16p4 ; V = g3p2, g20p1 ;
Z = g13p2, g17p2 ; G = g7p3, g24p3 (gB p3) ; S = g13p3, g21p4 ; C = g8p6, g24p1 (gB p1).
Toute boîte d'exemple corrigée après la planche-contact est consignée dans un avenant (coordonnées seulement, mêmes lieux).

## Contrôles (3), lettres sûres de g26-g49, jamais exemples
K1 g26p3 L (NELSYW) (4745,2120,4808,2165) : I / L, attendu L.
K2 g39p2 M (GMSQ) (4604,2543,4727,2590) : N / M, attendu M.
K3 g36p1 F (F) (6445,2383,6527,2437) : E / F / F2, attendu F.

## Intégration (après réponses ; sur copie ; rien écrit chez Daniel sans accord de Brice)
1. Un contrôle raté (dont « impossible à distinguer ») → rien intégré.
2. Forme choisie = forme de la clé → glyphe relu ; le mot devient sûr si toutes ses lettres divergentes sont confirmées (MOBILE : les deux).
3. Forme choisie = forme lue → divergence confirmée (erreur du clerc) ; le mot reste [?].
4. « impossible à distinguer » → les deux formes = un glyphe de ce clerc à ce lieu ; rien ne change.
5. **Forme propre** (« aucune / autre forme » + remarque, ou F2 choisi) → nouvelle étiquette dans l'alphabet du clerc (sans valeur),
   relecture des autres lieux de ce glyphe (alphabet corrigé sur indication de Brice) ; valeur tirée du seul sens = {probable} (#728).
6. Recompte des mots sans [?] de v196-0018 ; proposition à Daniel (crédit Payne/nov1, Brice relecteur) seulement avec l'accord de Brice.
Graines 20261160 / 2511. Noyau planche_core v2 (copie alger-2511). Export reponses-taylor1865-2511d.json. ≤ 1,6 Mo, autonome.
