# Amendement PREREG n° 3 — clé K2 et mesure unique sur ital. 1584 f. 353r (14/11/2026, soir)

Écrit et gelé (SHA-256 dans `HASHES-1317-K2.txt`) AVANT toute transcription signe à signe de f. 353 et AVANT toute lecture de la
copie f. 352. Mandat de Brice (14/11 soir) : compléter la clé R5318, la figer, faire UNE mesure sur la lettre intacte ital. 1584
f. 353, garder f. 71 en réserve. Vu de f. 352-353 jusqu'ici : les vignettes entières 1000 px des vues 346-348 (mise en page seulement ;
illisibles à cette taille), aucun recadrage.

## Clé figée K2
- `K2_key.tsv` (étiquette de forme → valeur ; x|y → première valeur ; '' = nulle) et `sign_legend_K2.md` (formes seules, sans valeur).
- Construite seulement sur : feuille R5318, f. 28 + clair f. 27, f. 30 + clair f. 29, f. 35r + clair ff. 34r-v (grillé), gloses
  f. 134 ; scripts `k2/common.py`, `k2/explore.py` (alignement → comptes) ; contrôles d'image sur crops d'entraînement (SPOF_2 `k2crops/`).
- Changements par rapport à R5318_crosswalk (04c8ae96…) : 21 formes nouvelles valuées (`LTL` = Re de Ragona, `MINL` = ambassadore,
  `lolli` c, `ribbon` le, `heart` lu, `tribar` me, `hookl` pu, `rstem` se, `bslash` t, `pix` x, `rc` a, `rcb`/`baro` f, `zz` z,
  `fa3` fa, `CLOVER` milan, `MEANDER` denaro, `OBLOOP` facto, `DIAMDOT` pace, `RCAP` fiorini, `UDOT` italia, …) ; nulles :
  `DEL`, `otee`, `o3`, `rho` ; corrigés : `tt` cc (pas sa), `dd` sa, `ri` ri (pas bi), `rb` ra, `ne` ne, `VEN` li Venetiani
  (usage 1448 ; duca en 2ᵉ valeur, non utilisée), `COSIMO` cosimo, `oc` d. Contrôle en-échantillon (non probant, entraînement) :
  f. 35 0,840, f. 30 0,860.

## Portion (une seule)
- **BnF ital. 1584 f. 353 recto** (Gallica btv1b100373864, vue 347, page de droite), Tranchedini, Florence, 14 octobre 1447 :
  **toutes les plages chiffrées de la page, dans l'ordre**, première ligne à dernière. Le verso (vue 348) ne porte que l'adresse.
- Jamais transcrite ni décodée par nous. Après la mesure, f. 353 est grillé. **ital. 1585 f. 71 reste intact (réserve).**

## Différences de date / période de clé (consignées avant mesure)
- f. 353 = 14 oct. 1447 : après la mort de Filippo Maria (13 août 1447), République ambrosienne ; entre R5318 (clé de 1446,
  barre-o-barre-o = Duca) et les lettres de févr. 1448 (VEN = Venetiani). La clé a pu changer entre-temps (nomenclateur réaffecté).
- On garde VEN = « li Venetiani » (première valeur) ; « Milanesi » sera sans doute fréquent (CLOVER = milan + e + si).
- Image : microfilm noir et blanc (ff. 28/30/35 : couleur) → transcription plus difficile.

## Référence
Copie f. 352 r-v (vue 346 page de droite + vue 347 page de gauche), lue seulement APRÈS le gel de la transcription.
Pour chaque plage, les mots de la copie entre les mots clairs qui l'encadrent sur f. 353, écrits dans `texts/f352_reference.txt`
(format `Rn: mots`) AVANT tout décodage ; blanc / tiret du copiste = `[—]`. Si une plage ne se retrouve pas dans la copie
(saut du copiste), elle est retirée de la portion AVANT décodage, et notée.

## Transcription
Étiquettes de `sign_legend_K2.md` ; formes absentes → `@Nxx` (aucune valeur, aucun rattachement après coup).
Passe B et passe C par des sous-agents aveugles (ni clé, ni valeurs, ni copie, ni page de gauche) ; chaque passe peut être faite par
deux sous-agents sur deux moitiés de page séparées par une ligne fixée d'avance. Arbitrage sur l'image par un 3ᵉ sous-agent aveugle
→ `texts/f353_signs.txt`. Je ne transcris pas (je connais la clé). Image de travail : page de droite seule, recadrée.

## Mesure (une seule) — `measure_f353.py`
- Métrique identique à f. 35 : première valeur ; normalisation (minuscules, lettres seules, v→u, y→i, j→i, h supprimé, doubles simplifiées) ;
  score = 1 − Σ Levenshtein / Σ longueur des références.
- Témoins : 200 clés mélangées à l'intérieur des classes (signes de mots = étiquettes MAJUSCULES ; nulles ; lettres/syllabes), graine 1447.
- Seuils : **lu** si score ≥ 0,85 ET ≥ meilleur témoin + 0,30 ; **partiel** si seulement ≥ meilleur + 0,30 ; sinon **échec**. z rapporté.

## Après la mesure
Seulement si « lu » : lecture de la lettre, compte strict par mots à la Daniel (sûrs / {probables} / [restitués] / ‹irrésolus›) ; ≥ 95 % = read ;
livrable `lead1317/pr/`. Sinon : rapport des chiffres, aucune lecture revendiquée, f. 71 non touché.
