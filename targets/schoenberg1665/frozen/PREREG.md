# PREREG — schoenberg-1665 (LATh – StA Altenburg, Schönbergische Sammlung Nr. 107, vue 0233, fol. 114r)
Écrit le 09/11/2026 (agent Opus 5.5, fil Déchiffrement), APRÈS la transcription gelée (`H-CHIFFRE.txt`,
SHA-256 be650ff10c350a7d423e28ae497b8b5797c7c57dd85217cd67cbcf8b37fd4f66) et le comptage des lettres,
AVANT toute clé essayée et avant tout décodage d'une partie quelconque.

## Ce que j'ai vu au moment d'écrire (déclaration de contamination)
- Comptage sur les 179 lettres : x 36, s 18, k 17, q 15, b 10, d 10, g 9, a 8, u 8, i 8, p 7, w 6, z 6, t 4, c 4, n 3, y 3,
  l 2, m 2, r 1, f 1, o 1 (22 signes). x ≈ 20 % → allemand très probable (et le clair autour est allemand).
- En regardant le texte chiffré entier, j'ai remarqué des mots courts répétés (« bxq », « xq », « bxs », « ksb »),
  dont certains sont dans H. Aucune valeur n'a été attribuée ni écrite. Cette contamination est déclarée ; la
  procédure ci-dessous interdit d'utiliser H pour ajuster la clé.
- Contexte en clair vu : « … ihn aber auch in einer sache also gan- / gen - » [chiffre] « Frankreich habe … ».

## Découpage (fixé ici)
- **Apprentissage A = lignes L1–L5** (17 mots, 105 lettres) : lues librement, clé ajustée seulement sur A.
- **Tenue à l'écart H = lignes L6–L9** (16 mots, 74 lettres) : jamais décodées avant le gel de la clé.
  (Découpage en lignes fixes, choisi avant tout essai ; H est la fin du passage.)

## Clé mesurée K (une seule)
- K : lettre chiffrée → lettre claire, substitution simple, construite à la main et/ou par recherche automatique en
  ne lisant QUE A. Un signe chiffré absent de A n'a pas de valeur dans K (décodé « ? »). Aucun ajout tiré de H.
- Langue : celle dans laquelle A se lit (allemand, latin ou français, testés dans cet ordre de vraisemblance) ;
  si A ne se lit dans aucune des trois → ÉCHEC déclaré sans mesure.
- K gelée dans `KEY.tsv` + `KEY.sha256` avant de lancer `scripts/measure.py`.
- Clés connues essayées d'abord (étape 3, sur A seulement, descriptif) : voir CLES-CONNUES.md.

## Mesure (une seule) — `scripts/measure.py`
- Mots de H : tokens de `parse.words(H-CHIFFRE.txt, L6–L9)` (le mot coupé « wx=/gssxs » appartient à A).
- Décodage par K ; normalisation : minuscules, v→u, j→i, umlauts/accents retirés (lexique normalisé ainsi).
- Lexique : `cyphersolver/lang/lexicons/<langue>.json.gz` (de : allemand 1470–1770 normalisé ; la ; fr), au commit
  local de ce jour ; un mot décodé est **lisible** s'il figure au lexique avec une fréquence ≥ 5 et ne contient pas « ? ».
- **lis = mots lisibles / mots de H** (tous les tokens, y compris d'une lettre).
- **200 témoins** : permutations des valeurs claires de K entre les signes de K (graine 1665) ; même calcul ;
  **marge = lis − max(témoins)**.
- **Seuils (fixés ici) : lis ≥ 0,70 ET marge ≥ 0,30 → VALIDÉ ; marge ≥ 0,30 seule → PARTIEL ; sinon ÉCHEC.**
- Rapporté, non décisif : couverture (part des lettres de H ayant une valeur dans K), liste des mots décodés.
- Limites déclarées d'avance : H est très court (16 mots) ; les fins de ligne au bord de la reliure peuvent avoir
  perdu une lettre (notées [?]) — cela ne peut que baisser lis ; lexique moderne/normalisé : une graphie d'époque
  absente compte comme illisible. Aucun réglage après coup (ni seuils, ni découpage, ni lexique, ni K).

## Ensuite
- VALIDÉ ou PARTIEL : lecture complète au compte de Daniel (sûrs / probables {x} / restitués [x] / irrésolus ‹…›),
  résumés FR + EN ; les corrections de lecture faites après la mesure sont signalées comme telles.
- ÉCHEC : pas de lecture présentée comme validée.
