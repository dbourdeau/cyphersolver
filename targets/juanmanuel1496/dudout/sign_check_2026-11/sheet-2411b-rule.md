# Règle de sélection — planche « Juan Manuel 1496 » 2411b du 24/11/2026 (cible cyphersolver juanmanuel1496, travail d'Andrew Beling), écrite AVANT toute construction de vignettes

Pièce : BNE MSS/20212/61/1 (10/11/1496, ff. 2v–3r) et /61/2 (18/12/1496, f. 7r, lignes C01–C25). Images : pages extraites des
PDF BNE (CC BY 4.0, « Imágenes procedentes de los fondos de la BNE ») déjà sur SPOF_2 …/juanmanuel1496/planche-2311-work/img/
(L1-002.jpg, L2-003.jpg) ; aucun téléchargement. 🔴 Cible d'un tiers : PR #757 (ajbeling, mergée, « reading review pending ») ;
étape 0 (24/11) : `gh pr list --search juanmanuel1496 --state all` → #757 et #817 (catalogue) seulement ; aucune PR ouverte.
Le résultat sera PROPOSÉ à Beling (crédit Beling + Lasry + relecteur Brice) ; ses fichiers ne sont pas modifiés.
Base : planche-2311/integration/ (transcription_*-v2.txt, words_*-integree.tsv), clé de Lasry inchangée. Rang = rang 1-based dans
la ligne de transcription (comme la planche 2311). Départ : 18/12 655 / 933 ; 10/11 256 / 388.

## Pourquoi une planche 2411b
1. **J2** (10/11 R10 rang 10, « enbi? ») non intégré en 2311 : remarque de Brice « forme 1 comprend 2 caractères différents ».
   Vérifié : les deux exemples x̄ (X_) de 2311 étaient mal cadrés (C09/33 prenait le m voisin ; C06/12 tombait sur un ϕ).
   Nouveaux exemples x̄, vérifiés à 4× : C06 rang 2 (« dar », 1137-1156 × 305-328) et C09 rang 2 (« gam… », 1145-1164 × 413-436).
2. **J6** (18/12 C03 rang 28, « ninero », ϟ lu n, le sens veut d) répondu « aucune / autre forme » en 2311 : vérifié, l'exemple
   « 7 » de 2311 (C03/25) coupait le 7 en deux. Reposé avec des 7 entiers (C10 rang 8 « mendador », C03 rang 25 « del ») et la
   forme voisine 7- (L09 rang 15 « luys », seul 7- net : ceux de f. 7r sont liés au X suivant).
3. **Ce qui reste d'utile** : la planche 2311 a montré que ∇ (<W26>) se distingue du π (77 = o) à l'œil (J1, J4 ∇ ; J3 π ;
   contrôle π réussi). Or f. 7r porte ∇ dans 15 mots où le sens veut o (legad?, c?mendador, p?r, c?n ×2, l?…). Si certains
   sont en fait des π, le mot est lu par la clé de Lasry. On pose 6 de ces lieux (lignes nettes, ∇ isolé) ; C09 rang 17 et
   C06 rang 36 restent EXEMPLES de ∇ (comme en 2311) et ne sont pas posés.

## Cibles (8)
Options ∇/π/x̄ : ∇ [C09 r17, C06 r36] / π [C07 r12 « estos », C03 r24 « esto »] / x̄ [C06 r2, C09 r2].
- **J2** 10/11 R10 r10 « enbi? » (L1, 1392-1414 × 545-568).
- **V1** C05 r8 « legad? » (1257-1276 × 272-296) ; **V2** C10 r4 « c?mendador » (1185-1204 × 450-473) ; **V3** C10 r37 « p?r »
  (1920-1938 × 450-472) ; **V4** C12 r12 « c?n » (1360-1379 × 519-541) ; **V5** C15 r5 « c?n » (1216-1235 × 624-647) ;
  **V6** C16 r21 « l? » (1588-1606 × 668-692).
Options 7 / ϟ / 7- : 7 [C10 r8, C03 r25 (boîte entière)] / ϟ (7+) [C09 r8, C17 r3] / 7- [L09 r15].
- **J6** C03 r28 « ninero » (1733-1752 × 207-234).

## Contrôles (3), signes de mots lus, jamais montrés à Brice
- K1 C08 r2 π (« por », 1151-1170 × 380-402) : ∇/π/x̄, attendu π.
- K2 C15 r10 7 (« ayuda », 1332-1353 × 628-662) : 7/ϟ/7-, attendu 7.
- K3 C10 r7 ϟ (« mendador », 1244-1265 × 448-480) : 7/ϟ/7-, attendu ϟ.
Boîtes vérifiées à 4× (planches-contact de travail, scratchpad lotA/jm, 24/11).
Page : un seul signe encadré ; aucune glose ; « forme n » ; titre « Planche J (b) ». Options texte habituelles + remarque.
planche_core v2 (copie : JPEG 64, signe ~180 px), graines 20261126 / 1497. Export : reponses-2411b-juanmanuel.json.

## Intégration (après réponses, sur une copie de planche-2311/integration ; rien chez Beling sans accord)
1. Un contrôle raté (y compris « impossible à distinguer ») → rien intégré ; noté dans HANDOFF.
2. J2 : x̄ → « enbia » (lu, +1) ; π → « enbio » noté, non compté ; ∇ → ∇ confirmé, inchangé.
3. V1-V6 : π → transcription corrigée (77!), mot lu par la clé de Lasry (+1) ; ∇ → « ∇ confirmé » (classe homogène pour un futur
   test de valeur ∇ = o ; AUCUNE valeur donnée ici, ∇ = o reste {probable} par le sens) ; x̄ → noté, mot inchangé.
4. J6 : 7 → « dinero » (+1) ; ϟ → inchangé ; 7- → « sinero » noté, non compté.
5. « aucune / autre forme » avec remarque de forme → nouvelle étiquette de signe (forme propre), sans valeur ; alphabet corrigé
   dans la copie (consigne 24/11). Autres réponses texte → mot inchangé, remarque reportée.
6. Recompte (#728) et entrée HANDOFF datée ; proposition à Beling. Gain maximal : 18/12 +7 → 662 / 933 ; 10/11 +1 → 257 / 388.

## Avenant 1 (24/11, après la 1ʳᵉ planche-contact, AVANT toute présentation à Brice) — hash initial ef6ccc209c18b0bf52bff051d1b4c02449033fcc004587bd69787f9907a5db37
- Exemple ∇ C06 r36 RETIRÉ : sa vignette prend la haste d'un signe de la ligne au-dessus et une marque sous la ligne (deux
  signes) ; ∇ n'a plus qu'un exemple (C09 r17). C06 r36 n'est pas posé en cible pour autant.
- Exemple 7 C10 r8 REMPLACÉ par C15 r14 (« dios », 1419-1441 × 628-662) : le Z voisin entrait dans la vignette.
Aucune cible, aucun contrôle ni règle d'intégration changé.
