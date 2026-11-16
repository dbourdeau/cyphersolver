# Amendement PREREG n° 2 — mesure de la clé figée R5318 sur une lettre neuve de la piste 1317 (14/11/2026, soir)

Écrit et gelé (SHA-256 dans `HASHES-1317.txt`) AVANT toute transcription signe à signe de la portion et AVANT tout décodage.
Seules ont été vues : les vignettes entières (≤ 1400 px) de ital. 1585 vues 67-68 (f. 35 r-v) et 137 (f. 71), pour repérer la mise en page.
Accord de Brice (14/11 soir) : « Pour Tranchedini aussi, tu peux » ; la piste 1317 lui est réservée chez Daniel jusqu'au 14/12.

## Clé (inchangée)
`../nicodemus-r5318/R5318_crosswalk.tsv` sha256 04c8ae96e8a4e1c625abf95414f6c89d10fb778ee2ed2bcbcf1aa784f01437c1
(gelée par `PREREG-AMENDEMENT-R5318.md` sha 30c70fcc…). Elle n'a jamais vu f. 35 : R5318 est une feuille de clé indépendante ;
la correspondance de forme a été faite sur f. 28 seulement. Aucune retouche de la clé.

## Portion (une seule)
- **BnF ital. 1585 f. 35 recto** (Gallica btv1b52525947w, vue 67, image tournée de −90°), Tranchedini, Florence, 29 février 1448 :
  **toutes les plages chiffrées du recto, dans l'ordre**, de la première ligne à la dernière.
- Si le recto donne moins de 300 signes chiffrés, on ajoute toutes les plages chiffrées du verso (vue 68), dans l'ordre ; rien d'autre.
- Portion jamais transcrite ni décodée par nous ni (d'après le dépôt de Daniel, ital1584_copies_B.md) par personne : intacte.
- Non retenues ici (restent intactes) : ital. 1585 f. 71 (1449, déchiffrement d'époque f. 70) et ital. 1584 f. 353 (1447, copie f. 352).

## Référence
Copie claire tardive ff. 34r-v + 36r (vues 65, 66, 69 ; « complete, no blanks seen » selon Daniel). Pour chaque plage de f. 35,
les mots de référence sont pris dans la copie grâce aux mots clairs qui l'encadrent sur f. 35, AVANT décodage, et écrits dans
`texts/f34_36_reference.txt` (format `Rn: mots`). Un tiret ou blanc du copiste = `[—]` (aucune lettre).

## Transcription
Étiquettes de `sign_legend.md` (table 1448) ; formes absentes → `@Nxx`. Deux passes : A (moi) et B (sous-agent qui ne voit ni la copie,
ni la clé, ni la passe A) ; désaccords tranchés sur l'image (zoom), sans regarder la copie ni la clé ; résultat `texts/f35_signs.txt`.
La passe A est faite sans regarder la copie ni la clé (je ne lis la copie qu'après l'arbitrage, pour la référence).

## Mesure (une seule) — `measure_f35.py` (sha dans HASHES-1317.txt)
- Décodage : valeur R5318 de chaque étiquette (valeurs multiples `x|y` : la première) ; étiquette absente de la clé → rien.
- Normalisation (comme PREREG.md) : minuscules, lettres seules, v→u, y→i, j→i, h supprimé, lettres doublées simplifiées.
- Score = 1 − Σ Levenshtein(plage décodée, référence) / Σ longueur des références.
- Témoins : 200 clés mélangées à l'intérieur des classes (étiquettes minuscules = lettres/syllabes ; MAJUSCULES = signes de mots), graine 5318.
- Seuils : **lu** si score ≥ 0,85 ET score ≥ meilleur témoin + 0,30 ; **partiel** si seulement ≥ meilleur témoin + 0,30 ; sinon **échec**. z rapporté.
- Après la mesure, f. 35 r (et v si ajouté) est grillé pour cette clé.

## Après la mesure (seulement si « lu »)
Lecture de la lettre (f. 35 r-v), compte strict par mots à la Daniel : sûrs / {probables} / [restitués] / ‹irrésolus> ; ≥ 95 % = read.
Sinon : rapport des chiffres, aucune lecture revendiquée.
