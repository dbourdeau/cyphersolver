# PREREG — Walsingham–Wotton 1585, BL Add MS 32657 (DECODE)

Écrit le 09/11/2026, avant toute construction de clé et avant d'avoir vu R4837 ou R4845.
Seules images déjà vues à l'écriture : R4689 P1 et P2 (paire d'apprentissage).
🔴 Recherche privée : images DECODE jamais republiées ni dérivées ; citer « DECODE R<n> ».

## Antériorité constatée avant ce PREREG (détail dans RESULTAT.md)
Daniel Bourdeau (cyphersolver) a déjà les cibles `walsingham1585` (R4838, R4839, R4840, R4844) et `wotton1585`
(R4841-R4843). Lus : R4838-R4839 (en clair, CSP Scotland viii nos 40 et 65), R4840, R4841-R4843 (brouillons en clair).
Ouvert chez lui : **les ~14 mots en alphabet de signes de R4844 (10/9/1585)**, « too short », interligne d'époque
biffé, « no key found » ; **les codes de noms 13, 14, 23, 30, 32, 37** (et 27, 28, 29, 36, 3, 11 seulement M/C/I).
Il n'a pas utilisé les paires déchiffrées R4689, R4835-R4837, R4845. Notre apport possible porte donc sur ces deux
trous seulement.

## Deux systèmes, traités séparément
- **Système S (alphabet de signes)** : mots en signes avec gloses interlinéaires d'époque dans les paires.
  Seul système mesuré au niveau caractère.
- **Système N (code de noms à deux chiffres)** : nombres glosés dans les paires. Pas de mesure caractère : on relève
  chaque nombre et sa glose, on note le nombre d'attestations concordantes, et on applique aux trous de Daniel.

## Apprentissage (système S)
- Paires d'apprentissage : **R4689 (ff. 93-94), R4835 (95-96), R4836 (109-110)**.
- Pour chaque mot en signes glosé : transcription des signes (étiquettes fixées dans `INVENTAIRE-SIGNES.md`, écrit
  pendant l'apprentissage) + glose. Les gloses ou interlignes sont le déchiffrement d'époque.
- Clé K = table signe → lettre (homophones permis, nulles → vide), construite par alignement mot/glose.
  K est écrite dans `CLE-S.tsv` et hachée (SHA-256 dans HANDOFF.md) **avant** la mesure.

## Partie H (tenue à l'écart)
- **H = R4845 (ff. 198-199)**. Si R4845 contient moins de 40 signes glosés, **H = R4837 (ff. 111-112)**, et R4845 rejoint
  l'apprentissage. R4837 n'entre dans l'apprentissage qu'après la mesure (clé v2, étiquetée « après mesure »).
- Le chiffre de H est transcrit **par un agent séparé** qui reçoit l'inventaire des signes mais pas la clé, et ne
  relève pas les gloses : fichier `H-chiffre.txt`, haché avant toute lecture des gloses.
- Les gloses de H sont ensuite transcrites **par un second agent séparé** qui ne reçoit ni la clé ni l'inventaire :
  `H-gloses.txt`, haché avant le décodage. Un mot sans glose lisible est écarté à ce stade (avant décodage).

## Mesure (une seule)
- Normalisation : minuscules, lettres seules, i=j, u=v (et w laissé tel quel).
- Décodage de chaque mot de H par K ; signe inconnu de K → « ? » (compté faux).
- Score = Σ (len(glose) − Levenshtein(décodé, glose)) / Σ len(glose), plancher 0 par mot.
- Nul : 200 clés mélangées (permutation aléatoire des lettres de K entre les signes non nuls ; graine 1585).
- Marge = score(K) − max(score des 200 clés).
- **Seuils : score ≥ 0,85 et marge ≥ 0,30 = validé ; marge ≥ 0,30 seule = partiel ; sinon échec.**
- Script : `mesure.py`, haché avec la clé.

## Si validé ou partiel
- Décoder les mots en signes des pièces non déchiffrées (en pratique R4844 ; vérifier aussi R4838-R4843) et lire
  au sens. Compte de Daniel : sûrs / probables / restitués / irrésolus ; seuil 95 % de lu par le sens.
- Système N : appliquer les gloses des paires aux codes ouverts de Daniel (13, 14, 23, 30, 32, 37…).

## Si échec
- Pas de lecture du système S. Système N rapporté seul (gloses relevées, sans mesure).

## Interdits
Pas de PR, pas de mail, pas de `rm`, rien sur le Toshiba, aucune image ni dérivé publié (découpes dans le scratchpad
de session seulement).
