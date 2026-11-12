# PROTOCOLE — n° 2525, Cyprianus de Kloge Søren (DFS 1997/020) — mesure unique sur portion réservée

Rédigé et figé le 2026-11-11 AVANT tout regard sur la portion réservée.

## Portion d'entraînement (déjà lue)
Images 003 D, 004 G/D, 005 G/D, 006 G/D, 007 G (pp. 3 à 6 v°) : 1 591 signes transcrits
(transcr/p003R … p007L.txt, notation transcr/NOTATION.md).
Clé obtenue (1) par mots probables (titres clairs « 3 gange », formules « i Navnet Gud Fader, Gud Søn og Gud
den Hellige Aand, Amen », ordinaux des titres chiffrés « Andet / Tredie Begreb »), puis (2) confirmée par un
recuit À L'AVEUGLE (substitution simple, quadrigrammes danois Gutenberg avec espace, seul l'espace fixé) :
le recuit retrouve seul « saa sandt … dette blod ei mere flyde i navnet gud fader gud søn og gud den hellige
aand amen » (score −10,56/quadrigramme, 10 relances, 6 convergent).
Couverture lexicale de l'entraînement avec la clé figée : 0,575 ; clés permutées (200) max 0,141 ;
signes mélangés (200) max 0,095.

## Portion réservée (jamais regardée à ce jour)
Image DFS_1997_020_4_030 (les deux pages de l'ouverture). Aucune vignette, aucun recadrage, aucune
planche de cette image n'a été produit ou vu avant le gel. Elle sera transcrite dans la MÊME notation,
fichier transcr/RESERVE-p030.txt, dont le SHA-256 sera noté dans le HANDOFF AVANT tout décodage.
Si l'image 030 compte moins de 300 signes chiffrés, on ajoute l'image 031 (même règle), décidé au vu du
seul nombre de signes, avant décodage.

## Mesure (une seule fois)
`python3 -I mesure.py KEY.json lexique-gutenberg-da.txt RESERVE-p030.txt[,RESERVE-p031.txt] 200 20261111`
- Clé : KEY.json (figée, hachée ci-dessous) ; décodage mécanique jeton → lettre.
- COV = part des signes appartenant à des mots (≥ 2 lettres) présents dans le lexique Gutenberg danois
  (fréquence ≥ 2), avec la tolérance orthographique déclarée t↔f, o↔ø, i↔j, e↔æ, y↔ø (homophonies du chiffre
  et graphies du XIXᵉ).
- Contrôles : 200 clés permutées (mêmes valeurs, réaffectées au hasard) ; 200 mélanges des signes de la
  réserve (longueurs de mots conservées). Graine 20261111.

## Critères (tous requis)
- C1 : COV ≥ 0,40.
- C2 : COV ≥ max(clés permutées) + 0,25.
- C3 : COV ≥ max(signes mélangés) + 0,25.
- S (sens) : au moins deux lignes consécutives de la réserve se lisent en danois suivi sans
  correction, et la lecture complète (lecture par le sens, règle de Daniel) est faite après la mesure.
Si un critère échoue : ÉCHEC consigné tel quel dans ESSAI-OPUS.md, pas de seconde mesure avec une autre
clé sur cette réserve.

## Biais déclarés
- La transcription de la réserve est faite par le même lecteur (agent Opus) qui connaît déjà la clé : risque
  d'ajuster inconsciemment les formes aux lettres attendues. Garde-fou : transcription figée par SHA avant
  décodage ; contrôles par permutation ; la lecture par le sens signalera les mots forcés.
- La clé confond f et t (signe croix), o et ø (deux points), b/c/h/j sous la forme « trait + point » (Ir) :
  ces confusions abaissent COV sans favoriser la mesure.
