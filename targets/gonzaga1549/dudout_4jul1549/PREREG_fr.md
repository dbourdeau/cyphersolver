# PREREG-C12 — 1549-07-04 (Estense, Autografoteca Campori, Lettera K, Karl V, sfasc. III, cc. 40-45) — 17/11/2026, agent Opus 5.5

Écrit et haché AVANT toute lecture des cc. 41-44 (seule une planche de mise en page à 140 px de large a été vue : 41r écriture courante,
41v page dense d'aspect chiffré, 42r une dizaine de lignes, 43r-44v autre main = probablement le déchiffrement annexé ; rien n'est lisible
à cette taille). Le catalogue Lodovico dit : « copia di lettera parzialmente cifrata (con testo decifrato annesso) » → PAIRE.

## Antériorité (vérifiée le 17/11 avant le gel)
- `gh pr list -R dbourdeau/cyphersolver --state all --search "gonzaga1549 OR ferrante1549 OR campori OR 1549"` : aucune PR sur le 4 Jul 1549.
- origin/main 66b985bef : `targets/gonzaga1549` (Daniel, WAINUT/ferrante1549 fusionné, McBratney 27 May) ne mentionne ni 4 Jul 1549,
  ni sfasc. III cc. 40-45, ni l'uuid fe5db48d (seulement dans labels.json, liste brute). Aucune PR ouverte d'un tiers sur ce document.
- Nos dossiers : C01 a « vu » la pièce (tri visuel du 29/10, aucune transcription, aucune mesure) ; jamais transcrite ni décodée ensuite.
- La lettre porte un déchiffrement d'époque → le contenu n'est pas une première ; l'apport est la validation de la clé (et la lecture).

## Clé (gelée avant ce PREREG)
KEY-C12.tsv = KB3-C.tsv de C03 octet pour octet (sha256 107a2eea…, cf. SHA-KEY-C12.txt). Aucune valeur de McBratney intégrée : sa clé
(key_cv1549.tsv, = sign_table.tsv de Daniel) emploie d'autres libellés de formes ; la fusion demanderait des choix de correspondance
faits à la main, donc elle n'est pas faite. Elle sert de comparaison extérieure DESCRIPTIVE, après la mesure, non décisive.

## Portion tenue à l'écart
- c. 41v, TOUT le texte chiffré, ligne par ligne, dans l'ordre (mots en clair exclus, notés entre crochets `[...]` et hors jetons).
- Si 41v donne moins de 300 jetons, on continue sur c. 42r (puis 41r si 42r est en clair) dans l'ordre de lecture jusqu'à ≥ 300 jetons ;
  la coupure est la fin de la ligne où le 300ᵉ jeton est atteint.
- Images : pleine résolution par tuiles IIIF (curl, recette NOTES gonzaga1549 « Access »), sur SPOF_2 seulement, étude seulement, jamais publiées.
- Formes : notation GLYPHES.md + GLYPHES-C02.md + GLYPHES-C03.md (liste close de KB3) ; forme inconnue → libellé nouveau (décodé `#`) ; illisible → `?`.

## Transcription
- Passe A puis passe B, B faite sur les mêmes recadrages SANS regarder A (fichier A non relu pendant B). Arbitrage des écarts sur l'image,
  sans clair et sans décoder. Fichier gelé `T41v-arb.txt` (sha256 dans SHA-T-C12.txt) AVANT toute ouverture de cc. 43-44 et avant tout décodage.
- Accord A/B (jetons alignés) rapporté.

## Référence
Le déchiffrement d'époque annexé (cc. 43-44, ou là où il se trouve dans cc. 41-45), lu APRÈS le gel de la transcription : passage contigu
correspondant à la portion, bornes fixées par les mots en clair de la copie qui encadrent les blocs chiffrés ; si le texte d'un bloc n'a pas de
correspondant, le bloc est exclu des deux côtés (déclaré). Abréviations : seules q → que, dho → dicho, V.M./S.M. laissées telles.

## Mesure unique
`python3 score_c12.py T41v-arb.txt REF-C12.txt KEY-C12.tsv 704 <segments>` : normalisation et métrique de C02 (tools_metric : car. = 1 − distance
d'édition normalisée), 200 témoins = permutations des valeurs de la clé (graine 704).
- **VALIDÉE** si M_car ≥ 0,85 ET M_car ≥ (témoin max + 0,30). Mots : rapportés, non décisifs.
- **PARTIELLE** si rang 1/201 mais sous 0,85 (livrable en « read in part » seulement).
- Sinon NON VALIDÉE. Une seule mesure ; la portion est grillée ensuite.

## Ensuite
- Compte strict de Daniel (≥ 95 % des mots lus par le sens) sur la portion décodée, en marquant sûrs / {probables} / [restitués] / ‹irrésolus›.
- Comparaison descriptive avec McBratney/Daniel (sign_table.tsv) sur les formes communes, non décisive.
- Livraison : PR seulement si VALIDÉE ou partielle exploitable ; créditer McBratney et WAINUT si leur travail sert ; catalogue.json non touché.
