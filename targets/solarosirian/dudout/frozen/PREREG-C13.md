# PREREG C13 — mesure unique de la convention (table v5) sur une portion neuve

Séance C13, 16/11/2026, lecteur : Claude Opus 5.5 (sous-agent, nouvelle conversation) + Opus 5.5 par API (2 runs au plus, plafond 8 USD au total).
Ce fichier est gelé par SHA-256 (consigné dans `PREREG-C13.sha256` et dans le handoff) AVANT toute lecture signe à signe de la portion neuve. Rien n'y sera modifié après le gel. Les écarts éventuels seront écrits dans un fichier séparé.

## 1. Objet
Il ne s'agit pas d'un « chiffre » au sens strict : l'écriture énigmatique égyptienne est une **convention d'écriture** (substitution de signes et graphies rares). La question testée est la suivante : la table forme → valeur établie en C03–C12 (table v5, gelée ci-dessous) lit-elle une portion jamais lue, mieux que le hasard, et à quel niveau ?

Notre apport est une vérification à l'aveugle avec mesure, pas une première lecture. Lectures publiées : Darnell 2004 (OBO 198) ; Darnell & Darnell 2018 (WAW 39) ; Piankoff, MIFAO 72 ; Drioton 1949 (JEA 35) ; Guilmant, MIFAO 15 (1907).

## 2. Portion neuve (N13), définie par zones avant lecture
Aucun de ces signes n'a été lu ni décodé par une séance antérieure. Exception à déclarer : en C12, les légendes 2–6 ont été décrites en quatre formes, sans valeur ni lecture (« S28 · insecte · barre · 3 points »).
- **A. Guilmant pl. LXXXI, légendes du registre des serpents numérotées 2 à 9 par Guilmant.** Image `h-092r.png` (page PDF 92 à 300 ppp, tournée de 90° dans le sens antihoraire), zone x 0–5106, y 1000–1520. La ligne horizontale ordinaire numérotée 10 et la ligne énigmatique du haut (lue en C07) sont exclues.
- **B. Guilmant pl. LXXXI, légendes 48 à 58 du registre inférieur** (entre les personnages). Même image, zone x 1300–5106, y 1960–2660. Les colonnes 11–47 (lues en C12) sont exclues.
- **C. Guilmant pl. LXXX, légendes 15 à 21.** `h-091.png` (page PDF 91 à 300 ppp), zone x 250–1700, y 1900–2560. Les colonnes 3–14 (lues en C12) sont exclues.
- **D. Piankoff pl. II (chapelle 2, côté gauche), registre inférieur.** Toutes les colonnes et lignes de texte : `working/c01/plates/p-001.jpg`, zone x 420–1795, y 503–705. Figures et décor sont exclus.
- **Règle d'extension (écrite avant)** : si A + B + C + D font moins de 300 signes dans la transcription arbitrée, on ajoute **E. pl. II, registre supérieur** (p-001.jpg, x 400–1745, y 120–310), en entier.
- **Exclusions** : cartouches royaux, numéros de Guilmant, éléments de scène. Un signe qui paraît relever de l'écriture ordinaire reste dans la portion. On le note seulement.

Expositions connues (déclarées) :
- C03 a vu la translittération que Piankoff (fasc. 1, p. 37–38) donne des **débuts** des légendes des registres haut et bas de la pl. II. Ces débuts ne sont pas recopiés dans le dossier. Le lecteur de C13 ne les a pas vus. La formule d'ouverture (*nn n nṯrw m sḫrw pn*) est de toute façon prévisible.
- Le sens général de la paroi de Ramsès IX (serpents percés de flèches, Rê) est connu depuis C06/C07.
- `working/c09/darnell-extrait.txt` (PDF 570–610) n'est pas ouvert avant le gel de la lecture.

## 3. Table gelée
`working/c13/table-v5.json`, SHA-256 `f3ad6282d19f52ef3801a79591b86f0e39d24b046d69e702085b5bfb5c7221bd`.
- La valeur d'un signe est `subst[code]` s'il existe, sinon `ordinaire[code]`, sinon aucune valeur.
- Les équivalences de mesure (s/z, t/ṯ, d/ḏ, i/y/j, ꜣ, k/ḳ) sont déclarées dans la table.
- Aucun ajout ni correction après le gel.

## 4. Ordre des opérations
1. Gel du présent fichier (SHA).
2. Découpes des zones A–D (fichiers sur SPOF_2), avec planches de contrôle numérotées. Sens de lecture établi à partir de l'orientation des signes et de la scène, avant toute valeur.
3. **Transcription, passe 1** (Claude, sous-agent) : codes de forme (Gardiner ou classes de la table), par légende ou colonne, de haut en bas, avec degré de confiance.
4. **Transcription, passe 2** (Opus 5.5 par API, run 1), sans accès à la passe 1. Les découpes et la liste des codes de forme lui sont fournies. Il ne reçoit ni la table ni aucune valeur. Dans la même requête, une fois sa transcription écrite, il peut proposer des segmentations, mais sans valeurs de la table.
5. **Arbitrage** sur l'image (Claude) → `transcription-arbitree.json`. Les désaccords non tranchés vont dans la planche de Brice. Le code retenu en attendant sa réponse est celui de la passe 1. Ce fichier est gelé par SHA.
6. Décodage mécanique par la table, puis lecture aveugle mot à mot par Claude (sûrs / probables / restitués / irrésolus), gelée par SHA. Ensuite seulement, ouverture de Darnell 2018 (passages correspondants), de Piankoff fasc. 1 (pl. II) et de Darnell 2004 s'il est accessible.
7. **Référence** (run 2, Opus 5.5 par API). Il reçoit la transcription arbitrée (identifiants + codes de forme, sans table ni décodage) et les traductions et translittérations publiées. Pour chaque signe, il donne la valeur qu'il a dans le texte publié : valeur phonétique, `PL`, `DET` ou `?`. Sortie : `reference.json`.
8. **Mesure unique** : `python3 -I cryptanalysis/c13/measure_c13.py working/c13/table-v5.json transcription-arbitree.json reference.json mesure.json`. Script SHA-256 `95c9d862a6c85722a7002465a96dad80c3a1f6c571c292e3078cc03fd95ebb2f`.

## 5. Mesure et seuils (écrits avant)
- **M** = part des signes dont la référence a une valeur phonétique ou `PL` (les `DET` et `?` sont exclus) et dont cette valeur figure dans l'ensemble donné par la table.
- **Témoins** : 200 tables où les ensembles de valeurs sont permutés entre les codes présents dans la portion (graine 20261116).
- **Succès** (« la convention v5 lit une portion neuve ») : M ≥ 0,70 **et** M ≥ max(témoins) + 0,30.
- **Échec partiel** : M ≥ max(témoins) + 0,30 mais M < 0,70. Le signal est réel, mais la table est incomplète.
- **Échec** : sinon.
- Indicateurs secondaires, sans décision : couverture de la table (part des signes ayant une valeur) ; M restreint aux seules substitutions (`subst`) ; M par zone (A–C Guilmant / D chapelle).

## 6. Lecture (règle de Daniel)
- Fiche par mot : sûrs / {probables} / [restitués] / ‹irrésolus›, avec la justification de chaque cas. Le classement est fait **après** comparaison avec les publications, et la source de chaque mot est indiquée.
- Le texte compte comme « read » seulement si au moins 95 % des mots sont lus par le sens (sûrs + probables) grâce à la table et aux formes. Sinon : « read in part ».
- Ce qui ne vient que des publications est compté « restitué ».

## 7. Limites déclarées
- La référence est produite par un modèle qui connaît les valeurs ordinaires des signes. Elle favorise donc la part « ordinaire » de la table. Les témoins permutés ne profitent pas de ce biais ; M restreint aux substitutions est donné à part.
- La pl. II est à environ 15–20 px par signe. Les erreurs de forme y pèseront plus que chez Guilmant (environ 60 px par signe).
- Droits : images IFAO (Piankoff) envoyées à l'API pour étude seulement. Elles ne vont jamais dans le dépôt, ni dans une PR ou une publication. Les images de Guilmant (1907) ne seront republiées qu'après vérification de la source.

Gel : 2026-11-16 18:49 CET.
