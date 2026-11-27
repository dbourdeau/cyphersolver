# Règle de sélection — planche « champagne1590-2511b », écrite AVANT les vignettes (26/11/2026)

Suite de la planche champagne1590-2511 (réponses SHA-256 421b178c…, contrôle K3 manqué → rien intégré, HANDOFF 26/11).
Accord de Brice (relayé par le coordinateur, 26/11) pour cette planche b. Même cible, mêmes images (Gallica IIIF
openapi.bnf.fr, ark btv1b525245007 : f85 = no 25, f83 = no 24, f185 = no 60), même main (Beling ; gloses du déchiffreur).
Cadres : `scripts/boxes.py`, gelé avec cette règle ; vérifiés sur planche-contact (63 → 62 cadres) AVANT ce hachage :
recadrés à la planche-contact : K3, n3_b, n4_b, n1_b, pl_a, m_a, d_a, d_b ; retiré : c_c (« combatoient », cadre
incertain) ; G de « Gonesse » (no 24) classé « G bouclé » et non « G en 6 » à la planche-contact.

Leçon de la planche 2511 : K3 (r de « trop ») avait un sosie (r rond après t ≈ « c » de cette main). Ici, aucun contrôle
ne met en options deux formes qui se ressemblent dans cette main ; les r de contrôle et d'exemple sont des r en z hors
ligature t-r. Les options G en 6 et G bouclé ont la même valeur (G) : c'est voulu (deux vraies variantes de la main),
la question reste concluante si l'une ou l'autre est choisie.

## Questions (9) — T2 retirée (la réponse « Y » ne change rien)
| code | cadre | options (valeur ← exemples) | effet |
|---|---|---|---|
| T1 | no 25 l.34, signe sous la barre fin de groupe | 9 ← 9 barré no 24 l.23 (le [9̄ = Roy], barre en arc), 9 de 39 l.29, 9 de 93 l.30 · 3 ← l.29 « 43 », l.30 « 93 » · 7 ← l.30 « 75 », « 37 » | 9 → « du [Roy] » lu, no 25 20 → 21/22 (95,5 %) ; « aucune » + remarque « 39 » → La Noue, idem ; sinon rien |
| T3 | no 24 l.9, 1er chiffre de « 36/56 » ; vignette élargie (ligne 1600 px, marge 80 px) | 3 ← no 24 l.9 38, 39, 93 ; l.23 43 · 5 ← no 24 l.9 45, 52 ; l.23 56, 35 | 5 → Ludouic confirmé ; 3 → Budouic, no 24 18 → 17/21 |
| T4 | no 25 l.2, initiale Gonnesse/Compiegne | G (en 6) ← Guische (no 25 l.23 ; seul G en 6 hors T4, un exemple) · G (bouclé) ← Givry (no 24 l.34), Geneve (no 25 l.40), Gonesse (no 24 l.36) · C ← Chastillon, Cependant (no 25 l.38) | G (l'une ou l'autre) → Gonnesse ; C → Compiegne |
| T5 | no 25 l.8, cadre recadré sur les DEUX premières lettres (Brice voyait un « H ») | pl ← « plain » l.9, « plus » l.11 · fl ← « Conflans » l.3, « souflemant » no 24 l.10 | pl → platines ; fl → flatteries |
| T6 | no 25 l.21, 2e lettre | u ← nous, esperdu · o ← nous, tenons | u → Ruelle ; o → force |
| T7 | no 25 l.27, initiale | c (initial) ← « ce » l.30, « cestuy » l.6 · t (initial) ← « tenons » l.10, « tenez » l.17, « tant » l.25 | c → croions ; t → treuvons |
| T8 | no 25 l.30, 3e lettre | u ← nous, esperdu · r (en z) ← affaires l.29, pour l.13 | u → d'Auvergne ; r → d'Arques |
| T9 | no 25 l.44, initiale | c ← ce, cestuy · r (en z) ← affaires, pour | c → commerce ; r → riviere |
| T10 | no 25 l.49, initiale | p ← party l.7, pour l.13 · m ← malheur l.28, demeure l.52 | p → puissance ; m → misericorde |

## Contrôles cachés (3), neufs, sans sosie
| code | cadre | attendu | options |
|---|---|---|---|
| K1 | no 25 l.29, 8 de « 48 » (glose h) | 8 | 8 ← 38 l.29, 89 l.30 · 4 ← 43 l.29, 84 l.30 · 1 ← 12, 19 l.27 |
| K2 | no 25 l.48, d de « dernier » | d | d ← « de faire » l.48, « demeure » l.52 · m ← malheur, demeure · f ← faict, face |
| K3 | no 25 l.24, r en z de « pour » (pour soy retirer) | r | r ← affaires, pour (l.13) · o ← nous, tenons · t ← tenons, tenez, tant |
Règle : un contrôle manqué → rien n'est intégré (second regard).

## Application
Une question est concluante si une seule valeur est choisie et qu'aucune remarque ne la contredit ; « aucune / autre
forme », « impossible à distinguer », « illisible » = rien ne change (sauf T1 avec remarque « 39 »). Réponses de la
planche 2511 non reprises ; seules celles de 2511b comptent. Mesure de Daniel (mots chiffrés) recomptée avant toute PR ;
mot tiré du sens seul = {probable}. Pas de PR ni de commentaire sans accord.
Page : vignettes JPEG ≤ 560 px, page ≤ 1,8 Mo, `.opt .v img{max-width:40vw}`, même format de sortie JSON
(`reponses-champagne1590-2511b.json`), graine d'ordre 15902.

## Avenant 1 (26/11, après le hachage et la première génération, avant toute réponse)
Contrôle visuel des vignettes : l'exemple fl_a (« Conflans ») ne montrait que le f → cadre élargi de (1072,795,1110,862)
à (1080,785,1145,860) pour prendre f + l ; fl_b (« souflemant », no 24 l.10) retiré : le premier signe est un s long
sans barre, pas un f sûr. L'option fl n'a donc qu'un exemple (seul fl en minuscule des trois lettres hors T5), comme
l'option G en 6. Rien d'autre ne change (questions, options, valeurs, effets, graine). boxes.py et make_planche.py ré-hachés.
