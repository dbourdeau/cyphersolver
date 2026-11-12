# Avenant 2-bis (11/11/2026, agent Opus 5.5) — écrit APRÈS l'étalonnage §4 de l'Avenant 2, AVANT toute mesure (V et N non décodés)
1. **Résultat de l'étalonnage prévu** (`ETALONNAGE.json`, 476 groupes hors V, clé b, 200 permutations) : L1 z = 3,50 (gap 0,171) ;
   L2 z = 2,75 (gap 0,041) ; L3 z = 3,50 (gap 0,172). Aucun n'atteint z ≥ 4 → selon l'Avenant 2, aucun critère retenu.
2. **Cause** (constatée sur l'apprentissage seulement) : les témoins permutent aussi les valeurs longues (« votreexcellence »,
   « lempereur », « ministre », « leczar », « les »…) ; une permutation qui les place sur un nombre fréquent fabrique du français
   et gonfle la variance et le maximum des témoins. Remède : neutraliser ces valeurs dans le calcul du critère.
3. **Candidats ajoutés, testés sur l'apprentissage seulement** (`scripts/etalonnage_bis.py`, `ETALONNAGE-BIS.json`) :
   L5 = L1 − log-vraisemblance unigramme (information séquentielle) : z 3,74 ; **L6** = L1 avec toute valeur de longueur ≥ 3
   remplacée par « # » (vraie clé et témoins) : z 7,27, gap 0,659 ; **L7** = L5 avec la même neutralisation : **z 10,32, gap 0,627,
   score 0,4793, moyenne témoins −0,3394**. Règle de choix inchangée (plus grand z, gap > 0, z ≥ 4) → **L7 retenu**.
   Écart déclaré : la liste des candidats a été étendue après l'échec de la première liste, sur l'apprentissage seul.
4. **Test B' inchangé dans sa forme**, avec L7 et la clé c neutralisée de même (valeurs ≥ 3 lettres → « # ») sur N (R22-0091,
   353 groupes) contre 200 permutations (graine 1717) : **VALIDÉ si z_N ≥ 5,16 (= max(4 ; 0,5 × 10,32)) ET gap_N ≥ 0,314
   (= 0,5 × 0,627) ET score_N ≥ 0,070 (= mi-chemin entre 0,479 et −0,339)** ; PARTIEL si seule la 1ʳᵉ condition tient ; sinon ÉCHEC.
5. A' inchangé (Avenant 2 §2). Une seule exécution de `scripts/mesure2.py`.
