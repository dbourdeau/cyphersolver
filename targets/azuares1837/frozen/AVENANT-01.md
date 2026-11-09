# AVENANT-01 — n° 2421 (Azuares, Londres 8/9/1837) — 2026-11-09, gelé AVANT tout décodage nouveau
Contexte : protocole 1 NÉGATIF (MESURE-2421.json, M5 0,198, marge 0,00 ; H = vue 12, grillée).

## Déclarations préalables
- Vues 03 et 05 : TOUTES leurs lignes chiffrées (V03a, V03b, V05a, V05b) ont été décodées pendant l'essai 1 (recuit sur
  le passage entier). Il n'y reste AUCUNE ligne jamais décodée → ces passages ne peuvent pas être mesurés ; leurs lectures
  restent « probables, non validées ». Vue 12 : grillée (H du protocole 1) → lue par le sens seulement, hors mesure.
- Le lot contient d'autres passages chiffrés (vues 04, 06-11), jamais transcrits ni décodés avant cet avenant.
  Transcription : TRANSCRIPTION-2421-AV01.txt (SHA 28cd1de3…), faite avant ce document, sans aucune table appliquée.
- Constat déclaré AVANT décodage : des chaînes chiffrées identiques reviennent d'un passage à l'autre (« ſ y n l e »
  P062/P092 ; « g l ñ o m g l n ſ p p l » v10 l.13/P112 ; « g l y a h n ſ o t ll » v09 l.7/v10 l.12 ; « a p o ll t o »
  v06 l.6/P063) → le modèle « une table par passage » est peut-être faux (table unique + homophones/erreurs de lecture ?).
  On applique quand même le protocole demandé, sans rien changer : table apprise par passage, sur sa moitié A seule.

## Passages mesurés (≥ 100 unités transcrites ; A = ⌈n/2⌉ premières lignes, H = le reste, jamais décodées)
| passage | lignes (vue.ligne) | A (apprentissage) | H (mesure) |
|---|---|---|---|
| P062 | 06.09-06.14 | 06.09-11 | 06.12-14 |
| P063 | 06.17-06.23 | 06.17-20 | 06.21-23 |
| P081 | 08.03-08.09 | 08.03-06 | 08.07-09 |
| P092 | 09.17-10.02 | 09.17-20 | 09.21, 10.01-02 |
| P112 | 11.04-11.09 | 11.04-06 | 11.07-09 |
Passages plus courts (v04 l.2-3 et 16-18 ; v06 l.5-7 ; v07 ; v08 l.12-22 ; v09 l.1, 7-9 ; v10 l.6-15, 16-20 ; v11 l.1-3,
12, 21-22) : non mesurés, lus seulement (étape 4).

## Apprentissage
Par passage, sur A SEULEMENT : recuit (4-grammes espagnols eslm.4.pkl, SPOF_2) + retouches à la main sur A seulement.
Tables gelées dans KEY-2421-AV01.json, hachées AVANT tout décodage de H. Unité absente de A = non définie (« ? »).

## Mesure (une par passage, unique)
scripts/measure_2421_av01.py (SHA 87757f26…) : lisibilité en mots de H décodée par SA table ; lexique es.json.gz
(SHA 0c49f0d49d93f853…, fréq ≥ 20, mots ≥ 3 lettres) replié sur les graphies du XIXᵉ s. (v/b, y/i, x/j, z/c, ge-gi/je-ji) —
approximation déclarée d'un dictionnaire du XIXᵉ s. Témoins : 200 tables mélangées par passage (graine 2421) ;
correction pour comparaisons multiples : référence = MAX des 1 000 témoins (5 × 200), commune aux 5 mesures.
Verdict par passage : VALIDÉ si M5 ≥ 0,60 ET marge ≥ 0,30 ; PARTIEL si marge ≥ 0,30 ; NÉGATIF sinon.
Aucun ajustement après ; chaque H grillée après sa mesure.
