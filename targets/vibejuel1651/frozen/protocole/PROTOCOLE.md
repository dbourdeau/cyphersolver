# PROTOCOLE — Vibe → Juel (Daniel n° 2527), clé à décalage par mot — rédigé AVANT toute mesure (11/11/2026, agent Opus)

## Système (établi sur l'img 78 seule, glose interlinéaire d'époque, jeu de développement)
- Mot chiffré = OUVREUR + CORPS. Corps : n = rang(lettre) + k dans l'alphabet de 23 lettres
  `a b c d e f g h i k l m n o p q r s t u x y z` (i=j, u=v, pas de w/æ/ø) ; dans le corps 32/33/34 valent 1/2/3.
- Table des ouvreurs (FIGÉE) : 24–29 → k=0 ; 30–34 → k=1 ; 35–39 → k=2 ; 1–3 → k=3. Autre ouvreur → mot non déchiffré (xxx).
- Groupes à 3 chiffres isolés (211, 228, 818, 872…) = nomenclateur : NON résolus par la mesure, exclus du compte.
- Développement : img 78 (37 mots), scripts/vdec.py, scripts/mesure.py, scripts/lm.py, protocole/lexique.txt (scripts/build_lex.py).
  Calibrage sur img 78 : M1 vrai −2,33 ; contrôles max −2,99 (marge 0,67).

## Portion tenue à l'écart (RÉSERVE)
- Images 74 (N. 330, 20 sept. 1651) et 77 de l'unité 261583 — JAMAIS ouvertes avant ce gel (seule la planche-contact de Daniel les a vues).
- Si la réserve fait moins de 300 nombres, elle est complétée par l'image 79 (ni ouverte non plus).
- Ordre : (1) transcription chiffre par chiffre de la réserve (aucun déchiffrement, aucun essai de k) ; (2) gel de la transcription par SHA-256
  (protocole/RESERVE.sha256) ; (3) UNE seule exécution : `python3 scripts/mesure.py corpus protocole/lexique.txt working/transcr/reserve.txt > protocole/MESURE.out`.
- Aucune correction de transcription ni de table après la mesure n'entre dans la mesure (les corrections ultérieures vont dans la lecture, déclarées).

## Critères (décidés avant)
- C1 (principal) : M1 (log-prob/caractère, modèle d'ordre 4 sur corpus/ danois ancien) ≥ max des 600 contrôles (A tables d'ouvreurs mélangées, B k au hasard par mot, C alphabets permutés) + 0,30.
- C2 (secondaire, informatif) : M2 (mots ≥ 4 lettres dans lexique.txt) ≥ max contrôles + 0,20. Échec de C2 seul ≠ échec (orthographe du XVIIᵉ absente du lexique).
- S (sens) : le déchiffrement brut de la réserve doit donner au moins deux phrases danoises suivies lisibles sans retouche.
- VALIDÉ si C1 et S. Sinon : ÉCHEC → ESSAI-OPUS.md.

## Décompte de lecture (règle de Daniel)
- Par mot (chiffré + codes) : sûr (déchiffrement direct, mot attesté) / probable (1 nombre corrigé ou forme ancienne plausible) /
  restitué (code ou mot reconstruit au sens) / irrésolu. LU si (sûrs + probables) / total ≥ 95 %. Les restitués NE comptent PAS.

## Fichiers figés (SHA-256 dans PROTOCOLE.sha256)
scripts/vdec.py, scripts/mesure.py, scripts/lm.py, protocole/lexique.txt, corpus/*.txt (11 fichiers), ce fichier.
