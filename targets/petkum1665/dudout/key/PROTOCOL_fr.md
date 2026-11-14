# PROTOCOLE — n° 2530 petkum-1665 (gelé 2026-11-11, agent V3H-A, AVANT toute transcription et tout calcul)

Unité : Rigsarkivet, TKUA, Speciel del, England, Gesandtskabsrelationer A III 52, Simon de Petkum ; AO unité 261267 (epid 19852633).
Inventaire des feuillets glosés / non glosés : _shared/cyphersolver/research/sweep_2026-11-11_tkua_paging_3/petkum_leaves.json (Daniel/cloud, 11/11).

## 1. Portion tenue à l'écart (H) — désignée ici, avant transcription
H = les groupes chiffrés GLOSÉS des feuillets suivants, dans cet ordre, jusqu'à atteindre ≥ 150 groupes (on prend le feuillet entier qui fait franchir 150, puis on s'arrête) :
  H1 = img 561 L+R (au roi, Oxford, nov. 1665)
  H2 = img 553 L (au roi)
  H3 = img 541 L (au roi)
  H4 = img 638 R (au roi, 13 avr. 1666)
  H5 = img 505 L+R (au roi) ; H6 = img 501 R (au roi) — réserves dans cet ordre.
Les feuillets H ne sont PAS utilisés pour construire la table. Leur transcription (groupes + gloses) est faite APRÈS le gel de la table T, et gelée par SHA-256 avant la mesure.
Apprentissage (A) = tous les autres feuillets glosés de la liste deciphered_leaves (lettres au roi et à Biermann).

## 2. Table T
T : groupe (ou suite de groupes) → clair, apprise des gloses de A seulement. Gelée (SHA-256) avant la transcription de H.
Déchiffrement de H par T : groupe par groupe ; si une suite multi-groupes est dans T (ex. 222.100.215 = faire, 389.288 = Votre Majesté), plus longue correspondance d'abord ; groupe inconnu → chaîne vide.

## 3. Mesure (une seule)
Normalisation : minuscules, accents ôtés, garder a-z seulement (u/v et i/j/y non fusionnés ; abréviations de la glose développées telles qu'écrites).
Référence R = concaténation des gloses de la chancellerie sur H (dans l'ordre). Prédiction P = concaténation des valeurs T.
Score car. = 1 − Levenshtein(P, R) / max(|P|, |R|).
Témoins : 200 tables permutées (valeurs de T réattribuées au hasard entre les clés de T, graines 1..200), même score.
Critère décisif (fixé ici) : score ≥ 0,85 ET score ≥ meilleur témoin + 0,30.
Accord en mots (glose par glose : valeur T de la chaîne = glose normalisée) : calculé et rapporté, non décisif.
Si H < 150 groupes glosés même avec les réserves : pas de mesure, PLAFONNÉ (pas de choix d'une autre portion après coup sans nouvel addendum haché avant transcription).

## 4. Ensuite
Si validé : lecture des lettres non glosées à Biermann (img 573, 641, 572…) ; fiche règle de Daniel (sûrs / probables {x} / restitués [x] / irrésolus ‹…›).

## Addendum 1 (2026-11-11, avant transcription de H, après gel de T)
- Normalisation de la référence : les abréviations de la glose sont développées en mots pleins (Mr→monsieur, Mrs→messieurs, Chanc./Chancr→chancelier, Angl.→angleterre, Vre/V.→votre, Mate/Ma.→majeste, T.C.→tres chrestien), puis a-z seulement. Même convention pour les valeurs de T.
- Groupes de H sans glose au-dessus : exclus de P et de R (la mesure porte sur les seules suites glosées). Le découpage de H en « suites glosées » (glose + groupes sous elle) est noté à la transcription ; on concatène dans l'ordre.
- Signes notés : g, 9, x, beta, lambda, ll, 4, m7, 6, d, ct, theta, y, T, #, 2, f (et tout autre signe avec un nom descriptif ; inconnu de T → chaîne vide).
- Témoins : permutation des VALEURS de T entre toutes les clés de T (graines 1..200), appliquée au même H.

## Addendum 2 (2026-11-11, après la mesure 1 — ÉCHEC du critère : car. 0,7976 < 0,85, marge +0,491 sur meilleur témoin 0,3066)
Re-test UNIQUE (BRIEF-VAGUE23 point 10) sur portion NEUVE, jamais regardée :
- H2 = groupes glosés de img 553 L + img 541 L + img 638 R (les trois en entier, même si > 150) ; si < 150 groupes glosés : ajouter 505 L+R puis 501 R, entiers, dans cet ordre.
- Clé testée : T2 (work/table_T2.py) = T + valeurs lues dans les gloses de H (561, grillé). Aucune valeur tirée des lettres non glosées.
- Même normalisation, même score, mêmes 200 témoins (permutation des valeurs de T2), même critère : car. ≥ 0,85 ET ≥ meilleur témoin + 0,30. Une seule mesure ; en cas d'échec : PLAFONNÉ, aucune autre mesure.
