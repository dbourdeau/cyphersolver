# Amendement PREREG n° 4 — clé K3 et mesure unique sur ital. 1585 f. 71 (14/11/2026, nuit)

Écrit et gelé (SHA-256 dans `HASHES-1317-K3.txt`) AVANT toute ouverture des images de ital. 1585 f. 71 (vue 137) et f. 70 (vue 135),
y compris leurs vignettes. Mandat de Brice (14/11 soir) : « K3 et mesure unique sur f. 71 ». Vu jusqu'ici de ff. 70-71 : les seules
dimensions des fichiers (85_f137.jpg 3457×5063, 85_f135.jpg 3436×5083) ; et, d'après RAPPORT-1317, la date (18 juin 1449) et le titre
du déchiffrement d'époque f. 70 « Ex cifra Nicodemi ». **f. 71 = dernière lettre intacte de la piste 1317.**

## Clé figée K3
- `K3_key.tsv` (étiquette de forme → valeur ; x|y → première valeur ; '' = nulle) et `sign_legend_K3.md` (formes seules, sans valeur).
- Construite seulement sur matériau grillé ou d'entraînement : feuille R5318, ff. 28/30/35 + clairs, f. 353r (grillé) + copie f. 352,
  gloses f. 134 (via R5318_RAPPORT) ; scripts `k3/` ; planche aveugle de Brice (`_prive-planche-k3/`, PREREG d553da37…, réponses ea46acef…,
  contrôles 3/3, décisions `_prive-planche-k3/DECISIONS-K3.md`).
- Changements par rapport à K2 (bfa0c266…) : légende réécrite pour `pe` (trèfle sans rien dessous) / `CLOVER` (trèfle sur croix, milan) ;
  `re` (ꞔ⊣) / `rb` (ƅ, ra) / `hookl` (⅃ seul, pu) + `cbar` (ȼ, pu ; « cbar hookl » = deux signes, remarque de Brice q12) ;
  `oo+` (croix APRÈS les boucles = sig~sigismondo) / `FED` (croix SUR les boucles = sig~federico) / `MALA` (sig~malatesta) ;
  `SIGNORE` (♀ sur pied) ; `m8` → i ; nouveaux `n0` b, `ooo` be, `GDA` gente~darme, `o2L` nulle ; `o2` avec point intérieur = o2.
  Inchangés : `ss` s|p (1ʳᵉ s), `o3` nulle, `VEN` li~venetiani (usage 1448). En-échantillon (non probant) : f. 353 étiquettes corrigées 0,827.

## Différences de date (consignées avant mesure)
f. 71 = 18 juin 1449, seize mois après les lettres de févr. 1448 : le nomenclateur a pu être réaffecté (oo+/FED, VEN). On garde K3 tel quel.

## Portion (une seule)
- **BnF ital. 1585 f. 71** (Gallica btv1b52525947w, vue 137, fichier SPOF_2 …/tranchedini1317/85_f137.jpg) : **toutes les plages
  chiffrées de la page, dans l'ordre**, qui ont une contrepartie dans le déchiffrement d'époque f. 70. Si f. 71 porte aussi du chiffre
  sur une autre vue (verso), il n'est pris que si l'image est déjà sur SPOF_2 ; sinon noté et laissé hors portion.
- Barre de taille : ≥ 300 signes chiffrés. Si la portion couverte fait moins de 300 signes, la mesure est quand même faite et rapportée
  « below size bar » (non probante pour Daniel).
- Après la mesure, f. 71 est grillé.

## Transcription
Étiquettes de `sign_legend_K3.md` ; formes absentes → `@Nxx` (aucune valeur, aucun rattachement après coup). Marques de marge exclues ;
gloses interlinéaires éventuelles ignorées. Passe B et passe C par des sous-agents aveugles (ni clé, ni valeurs, ni f. 70, ni autre image) ;
une passe peut être partagée entre deux sous-agents sur deux moitiés de page, frontière fixée d'avance. Arbitrage sur l'image par un 3ᵉ
sous-agent aveugle → `texts/f71_signs.txt`, haché avant toute lecture de f. 70. Je ne transcris pas (je connais la clé) ; je ne fais que
recadrer la page (sans la lire au-delà du repérage des lignes) et fusionner mécaniquement.

## Référence
Déchiffrement d'époque f. 70 (vue 135), lu seulement APRÈS le gel de la transcription. Pour chaque plage de f. 71, les mots de f. 70
qui lui correspondent (repérés par les mots clairs qui l'encadrent sur f. 71), écrits dans `texts/f70_reference.txt` (format `Rn: mots`)
AVANT tout décodage ; blanc/illisible = `[—]`. Plage sans contrepartie : retirée de la portion avant décodage (`texts/f71_signs_portion.txt`), notée.

## Mesure (une seule) — `measure_f71.py` (reprend `measure_f353.py` à l'identique : clé K3, graine 1449)
- Métrique identique à f. 35 / f. 353 : première valeur ; normalisation (minuscules, lettres seules, v→u, y→i, j→i, h supprimé,
  doubles simplifiées) ; score = 1 − Σ Levenshtein / Σ longueur des références.
- Témoins : 200 clés mélangées à l'intérieur des classes (signes de mots = étiquettes MAJUSCULES ; nulles ; lettres/syllabes), graine 1449.
- Seuils : **lu** si score ≥ 0,85 ET ≥ meilleur témoin + 0,30 ; **partiel** si seulement ≥ meilleur + 0,30 ; sinon **échec**. z rapporté.

## Après la mesure
Seulement si « lu » : lecture de la lettre, compte par mots à la Daniel (sûrs / {probables} / [restitués] / ‹irrésolus›) ; ≥ 95 % = read ;
dossier PR (cible tranchedini1446 ou celle de la piste 1317) avec PR-BODY.md en anglais, sans image. Sinon : chiffres seulement, pas de lecture revendiquée.
