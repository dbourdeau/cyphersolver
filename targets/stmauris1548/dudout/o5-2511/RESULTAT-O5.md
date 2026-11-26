# RESULTAT-O5 — stmauris1548 (cible WAINUT), lettre du 12 mars 1548, cc. 6v-8r (portion Q) — 25/11/2026, Claude Opus 5.5 (fil 🔓)

**Verdict : FAIL** (C1, C2 et C3 non remplis). Exécution unique selon PREREG-O5 (SHA ebd2429b…, vérifié avant toute action ;
`shasum -c PREREG-O5.sha256` : 11 fichiers OK). Brice : « Lance O5 dès que le PREREG est gelé » (relayé le 25/11).

## Chaîne (horodatée, 25/11)
| heure | étape | fichier | SHA-256 |
|---|---|---|---|
| 10:53:44 | préenregistrement (vérifié) | PREREG-O5.md | ebd2429ba2a12b92b530eaa7534d5543b899e74571289d16221bebb50a4df7e7 |
| ~10:54 | images 6v-8v revérifiées = PREREG §2 | c06v ab26245b…, c07r 181f5bee…, c07v 5a58769a…, c08r 0e44580a…, c08v 9a5ec564… | |
| 10:57:52 | outil de découpe v1 (remplacé, voir point 2) | tools/make_crops_o5.py | b5d4dbbe9c3c38941cb33aa96c48bedf16fcf3aa0f91b2b77641af776992987d |
| 10:58:31 | outil de découpe v2, AVANT la passe A | tools/make_crops_o5.py (+ .sha256) | ae5189973828d4deb0325feb5a9629a89f43e737e8a0a58521d72248bef1c1ee |
| 10:58 | 265 recadrages (87 lignes ×3 + 4 vues d'ensemble) | CROPS.sha256 (liste) | — |
| 11:10:26 | passe B (agent Opus neuf, aveugle) | passe-B/transcription_passB.txt | e1ba6a7944d5167f246d45fe756b8dbd1bb34d3d608d43504f1aa2b71ff92e79 |
| 11:13:27 | passe A (agent Opus neuf, aveugle) | passe-A/transcription_passA.txt | b0288e12f8ebb937a4d8606f85fd331ed54d9ca8e17b8df656eb082038da2329 |
| 11:13:49 | comparaison A/B (../o4-2511/tools/compare_o4.py) | COMPARAISON-AB.txt | 4f8f44d8bfe1e3b12c1494ed90dba3ffa507504f4c1f82393e38cfdbb6a3c325 |
| 11:14 | paquet d'arbitrage (arb_package_o4.py, sans valeurs) | ARBITRAGE/disputes.json 7cfd3e30…, CANDIDATS-DESCRIPTIONS.md a2f02b27… | |
| ~11:28 | arbitrage aveugle (agent Opus neuf C) | ARBITRAGE/ARBITRAGE.tsv | 2192fc62e0f251fbb70128d5c74f9479bd39c81d0e16619d8aa070ff198cecea |
| 11:28:40 | fusion GELÉE avant décodage (merge_o5.py) | transcription_1548-03-12_Q_merged.txt | f1f94f2ac39b54778de403fb0017df0eb56993f84be36b69d49b2730783f7c1e |
| 11:28:4x | étape de nommage déclarée (name_step_o5.py) | transcription_1548-03-12_Q_merged_named.txt | 8b0f58cf3102cabf5f781c2d3407601e6b2507e10213976c65160fc85660c41b |
| 11:28:47 | **décodage + mesure uniques** (graine 251125) | MESURE-O5.txt / MESURE-O5.json | abd0ac79… / 5bf554d6… |
| 11:28 | décodage seul pour les lecteurs | lecture-input/DECODE-O5.txt | 54582b9d95a26daedb58c8a96571945812d5fc701f84f007b55679edce14d46f |
| ~11:37 | lecture L1 (agent Opus neuf) | lecture-L1/LECTURE.txt 7231c62a…, JUSTIFICATIONS.tsv a88d103d…, L1.json 16ea20b1… | |
| ~11:37 | lecture L2 (agent Opus neuf, sans accès à L1) | lecture-L2/LECTURE.txt 086a8223…, JUSTIFICATIONS.tsv 71ffa7ac…, L2.json ff125cfe… | |
| 11:37:22 | accord L1/L2 et verdict | ACCORD-L1L2.json ad1877c6… ; VERDICT-O5.txt 12ed8170… | |

## Chiffres
- Portion Q : 87 lignes (6v L01-L28 ; 7r L01-L27, dont L01 et L21 partielles, après des mots en clair masqués ; 7v L01-L24 ;
  8r L01-L08) ; **8v : 0 ligne chiffrée** (adresse, mention « In Milano », sceau, transparence).
- **Accord A/B 0,830** (1 422/1 714, 250 désaccords) ≥ 0,80 → on continue. Motifs principaux : dd/tB-t1 ×75, tA-t3/vt ×45,
  tA-t8/tB-t7 ×23, tA-t1/tB-t2 ×15.
- Arbitrage C : A 64, B 183, « neither » 3 (→ NIL).
- Taille : 1 498 jetons à nom de clé ≥ 300.
- Nommage : 36 jetons → tS- (`n` ×27, `13` ×3, `,` ×1, `2`, `4t12`, `5`, `6t7`, `mx3` ×1).
- Mesure : 1 713 jetons, 1 498 avec valeur (87,4 %), 1 526 lettres ; **M = 0,6592** ; témoins max **0,4079**, moyenne 0,1913,
  écart-type 0,0636 ; **marge 0,2513** ; z 7,36 (information).
- Lecteurs (décodage de 1 741 caractères dont 215 `?`) :
  | | sûrs | probables | restitués | irrésolus | total | **lus** | restitués | nulles |
  |---|---|---|---|---|---|---|---|---|
  | L1 | 193 | 95 | 35 | 57 | 380 | **0,850** | 0,092 | 4 car. |
  | L2 | 201 | 93 | 29 | 68 | 391 | **0,826** | 0,074 | 3 car. |
  L1 : une nulle `(?)` collée à `[MOnsieur]` → ce mot compté irrésolu (garde-fou §8, avertissement de l'outil).
- Accord L1/L2 : kappa 5 classes 0,864 (accord 0,904) ; kappa lu/non lu 0,795 ; **F1 de segmentation 0,880** ; 330 mots
  identiques, de même classe à 98,5 %.

## Critères (PREREG-O5 §10)
C0 lettres ≥ 300 **OUI** · C1 lus ≥ 0,95 **NON** (0,850 / 0,826) · C2 restitués ≤ 0,05 **NON** (0,092 / 0,074) ·
C3 marge ≥ 0,30 **NON** (0,251) · C4 F1 ≥ 0,80 **OUI** (0,880) → **FAIL**.

## Conséquence (§11, appliquée telle quelle)
Q (cc. 6v-8r) est grillée ; **la lettre du 12 mars 1548 est épuisée pour cette clé**. Le décodage et les deux lectures restent
des données. Pas de proposition à Daniel (elle n'était prévue qu'en cas de succès) ; rien poussé, posté ni envoyé.

## Observations hors critère (ne changent pas le verdict)
- Les deux lecteurs, indépendants, lisent le même texte suivi (kappa 0,86) : Écosse et Anglais, bandes italiennes licenciées en
  Piémont (Cornelio Bentivoglio), querelle des princes et d'Andelot, duché de Milan, Guyenne/Bordeaux/Gascogne désarmées,
  capitaines (« Francisque Bernadin ») envoyés en Piémont avec des charges de froment. La clé produit du français ; l'échec tient
  aux trous du décodage, pas à un texte absent.
- Cause principale des trous (diagnostic fait APRÈS le verdict, sans recalcul) : 215 `?`. La forme « ∞ » (deux anneaux accolés
  sans barre), 95 jetons, a été nommée `tB-t1` par la passe B et préférée à `dd` par l'arbitre (dd = « two such loops joined »,
  qui vaut r dans la clé). Les deux lecteurs remplissent ces `?` presque toujours par **o**. Il s'agit sans doute d'une variante
  du `O` (haltère) de SIGNS.md, que ni les transcripteurs ni l'arbitre n'ont rattachée à ce nom : c'est une lacune de la liste
  des formes, pas de la clé. S'y ajoutent `n` (27 jetons, sans ligne dans key.tsv).
- Confusions apparentes de valeurs relevées par les deux lecteurs (b pour q, q pour x/b, u pour x, l pour e) : à vérifier sur
  les formes (paires de signes proches) ; non utilisées.
- Clair et notes de 6v-8v : pas de note marginale ni de glose interlinéaire de déchiffrement sur ces pages (vues réduites) ; les
  passages en clair de 7r, 7v et 8r appartiennent au texte même de la lettre (alternance clair/chiffre), ils ne recouvrent pas
  le chiffre et n'ont pas été lus ni comparés. Rien de comparable à la note de 5r.
- Les trois mesures lexicales précédentes et celle-ci (0,718 / 0,784 / 0,780 / 0,659) et les lectures à 83-85 % convergent :
  la clé de WAINUT donne du français lisible mais incomplet avec les listes de formes actuelles.

## Écarts et points d'exécution
1. **Vues des pages** : pour placer lignes et masques, l'orchestrateur a vu les cinq pages en vignettes réduites (1/5, puis
   zones 1/3 et deux zooms 1/1 de 500-600 px sur les bornes clair/chiffre de 7r L01 et L21, et une bande de 7v). Le clair n'a été
   ni transcrit ni utilisé ; quelques mots ont pu être aperçus en réglant ces bornes.
2. **Outil de découpe v1 → v2 avant la passe A** : v1 (b5d4dbbe…, 10:57:52) faisait commencer 7r L21 à x = 2690 et coupait le
   premier signe (vu sur le recadrage) ; v2 (ae518997…, 10:58:31) x = 2605 ; recadrages refaits. Aucun agent n'avait vu v1.
   Deux lignes corrigées après la vue des lignes-guides avant le premier hash (7r L25, 7v L24).
3. Demi-hauteur : 7r 101 px (interligne médian < 170 → 0,6 × interligne), autres pages 100 px. Masques : 7r (mots en clair en tête
   de L01 et L21, ligne en clair entre L20 et L21, grand paraphe), 7v (paraphe sous L24), 8r (date au-dessus de L01) ; quelques
   hampes du clair restent visibles au-dessus de 7r L01 ; la marque haute du 1er signe de 8r L01 est peut-être sous le masque
   (signalée par les deux passes).
4. Les deux passes ont fait un `ls` de la racine o5-2511 (noms de dossiers visibles, rien ouvert).
5. `,` (virgule, 7r L19) n'est pas retirée par compare.load : renommée tS-, elle a produit un `?` de plus (1 sur 215).
6. L'arbitre a encadré et zoomé sur SPOF_2 (`ARBITRAGE/boxes`) puis tout effacé ; aucune case gardée. Il a changé sa règle N2/N18
   en cours de route et revu les cas antérieurs (D134 → neither).
7. Les lecteurs ont gardé des fichiers de travail dans leur scratchpad (hors dépôt, sans image).
8. `measure_o4.py` imprime « VERDICT FAIL » selon l'ancien seuil 0,85 : ignoré comme prévu (§6).
9. Images, recadrages, vignettes : SPOF_2 seulement ; zooms temporaires des agents effacés ; rien republié.
