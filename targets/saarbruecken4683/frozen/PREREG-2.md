# PREREG-2 — Saarbrücken 4683 (rédigé le 27/11/2026, APRÈS l'échec de la mesure 1, AVANT tout calcul sur la portion 2)

Contexte : mesure 1 (PREREG.md, portion 297r–297v contre le concept 298r–298v) = 0,707 < 0,85 → critère NON atteint ;
portion 1 grillée. Diagnostic : la lecture par K est cohérente, mais le concept n'est pas verbatim (variantes,
passages du concept très raturés/incertains) et l'alignement global sur 2 100 caractères pénalise. Rien n'est
modifié rétroactivement : la clé K reste CLE-K.json (SHA-256 77dfe736…ad5a), inchangée.

## Portion 2 (fraîche, jamais vue par l'apprentissage)
Lettre reçue fol. 336r (double page 335v-336r ; aucune ligne de T1–T4 ne vient de 335v/336r — vérifié par grep avant
rédaction). Référence = les résolutions interlinéaires d'époque de cette lettre (verbatim, groupe par groupe).
Si 336r a moins de 300 lettres chiffrées glosées, la portion est complétée par 320v-321r (321r), puis 339v-340r (340r) — dans cet ordre.

## Transcription
Deux passes indépendantes A2 / B2 (nombres + gloses par groupe), sans la clé ; arbitrage sur image ; gel SHA-256 avant la mesure.

## Mesure (UNE seule)
Pour chaque groupe glosé (nombres < 200 seulement ; groupes contenant un code ≥ 200 : le code compte 1 position,
juste si K donne le mot de la glose) : déchiffrement par K, normalisé comme norm.py, aligné (Needleman-Wunsch
+1/−1/−1) sur la glose normalisée DU MÊME GROUPE. Accord caractères = Σ caractères justes ÷ Σ nombres déchiffrés
(« ? » = faux). Taille minimale 300 nombres. Témoins : 200 permutations de K (graine 46832).
Critère : accord ≥ 0,85 ET ≥ meilleur témoin + 0,30. Accord en mots (groupes entièrement justes) rapporté, non décisif.
