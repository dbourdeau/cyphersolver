# PREREG P04 — K_G25 inchangée sur la lettre glosée doc. 97 (MAP LXXIV, pos. 443-444) — gelé le 20/11/2026

**Statut : GELÉ.** Tiré du brouillon du 19/11 (p04/PREREG-P04-DOC97-BROUILLON.md, conservé tel quel). Accord de Brice
le 20/11/2026 (« Vas-y ») pour geler et exécuter. dbourdeau/cyphersolver#797 (McBratney) est mergée. Écrit et haché
(PREREG-P04.sha256) AVANT toute transcription de signes ou de gloses de la portion. Aucune transcription, aucun décodage,
aucune mesure n'a été faite pour P04 avant ce gel. L'agent qui gèle (agent principal P04, Opus 5.5) n'a pas regardé les
pages 443-444 ; l'agent du brouillon les avait seulement regardées entières (1272 px) pour compter les lignes.
Rien dans ce texte ne change après le gel ; tout changement = avenant daté, haché avant usage.

## Pourquoi cette source (recherche du 19/11)
- Le seuil de P03 (≥ 300 signes sous glose complète) n'a pas été atteint : 86 signes.
- **Filza 39 des Dieci di Balìa, Responsive** : pas numérisée en ligne à notre connaissance ; rien chez nous. Elle reste
  la meilleure source « de la clé 25 » mais demande une reproduction ASF (DEMANDES-ARCHIVES.md, non envoyée).
- **Pages voisines déjà sur SPOF_2** (vérifiées à l'œil le 19/11) : 020, 087, 268 (suites des docs 6, 21, 62) sont presque
  tout en clair, avec quelques groupes chiffrés courts ; inutiles pour 300 signes.
- **Doc. 97 (Angelo Niccolini, Milan, « xx Julij 149? » ; f. 222 au numérotage moderne)** : lettre presque entièrement
  chiffrée, **glose interlinéaire d'époque au-dessus de chaque ligne**, sur les deux pages. Estimation visuelle (± 20 %) :
  pos. 443 ≈ 24 lignes chiffrées × ~45 signes ≈ 1 050 signes ; pos. 444 ≈ 6 lignes ≈ 230. P01 n'en a transcrit que
  25 séquences courtes de 443 (≈ 140 jetons, T_doc97_p443.txt), retenues pour K_T. Le reste de 443 et toute la page 444
  n'ont jamais été transcrits, décodés ni mesurés.

## Biais déclarés
1. Doc. 97 est dans T (P01) : 25 séquences de 443 ont servi à K_T, et K_T a été comparée à la clé 25 dans le test g3
   du 14/11 (comptes, pas un décodage de 443). Ces séquences sont EXCLUES (règle mécanique ci-dessous).
2. Le reste de 443 a été vu en P01 (page entière), sans transcription ni alignement : déclaré, non grillé.
3. 444 n'a jamais été transcrite : c'est la part la plus propre. Son résultat est rapporté à part.
4. K_G25 (gelée le 14/11) vient de la feuille Gabbrielli ; la passe 2 aveugle (feuille seule) a confirmé la passe 1 sauf
   un double (nn/mm). Clé et catalogue F inchangés.
5. Les transcripteurs ne voient ni K_G25, ni K_T, ni CLE_KT.json, ni T_doc97_p443.txt, ni ce dossier, ni ses résultats,
   ni #589 / #797. Ils ne voient que les images 443-444 et CATALOGUE_F.jpg, copiées dans un dossier de travail neuf
   (SPOF_2 …/p04-work/A et …/p04-work/B), sans les planches de la feuille Gabbrielli.

## Objets gelés (SHA-256)
- kg25/K_G25.json = 3a81cd6d1c12e14a70530b9a251c28e5162a8a99200f9b22f9dc15f1c2c41611
- kg25/MAP_F_vers_G.json = eb23f56e49f38193309403ac1b55587e171fe43a042ed843b5404a4a4ec1461e
- SPOF_2 …/kg25-work/CATALOGUE_F.jpg = 5cbd6f5e4a1320136c2064f3bed682d1380b0f890c7ae08bb593d5d8dc8fab0a
- p04/measure_p04.py = 13b8535f74af1adb610e5e80dd4aa9e35a51a3244dd6ce54f294a862d22ca691
- transcription/T_doc97_p443.txt (lu par le filtre) = d958eefd9603a99a4cd66c544ce1676f0f8e112a5c477271894f7f5c4cb30925
  (identique à TRANSCRIPTION_T.sha256 de P01)
- Images (SPOF_2 …/images/) : F74_A0000443.jpg = 129351b33bc1730e90743393eb8c76a37be6602a491572694dcfc4e4126c9d9e ;
  F74_A0000444.jpg = c21eff91997855ba95a003b4471ab0fd022d47141aa1605c2c08b2c6463729f1
- Ce PREREG : PREREG-P04.sha256.

## Script et test à blanc (fait avant le gel)
measure_p04.py = measure_p03.py (décodage, normalisation, métrique, témoins inchangés) + filtre T97 + rapport séparé
443-reste / 444 + règle X: 20 %. Test à blanc (`python3 -I measure_p04.py --blank`, données factices codées avec K_G25) :
- Blanc 1 : 6 séquences C, filtre T97 = 23 motifs (25 séquences moins « di » et « et ») ; la séquence factice contenant
  « andava » et « a genova » est bien exclue ; 468 F retenus (443 : 313, 444 : 155) ; **accord car. 0,9575** (manque = b
  de « republica », plafond b/g/z 3,8 %) ; **témoins : meilleur 0,3248, moyenne 0,2052, médiane 0,2038** ; → VALIDE.
- Blanc 2 : mêmes données + 25 % de jetons X: → part X: 0,2508 → **NON CONCLUANT** (règle X: appliquée).
- Blanc 3 : 155 F → **NON MESURABLE**.
- Observation du test (avant gel, sans rien changer à la règle) : les motifs courts (« del », « col », « pos », « dele »,
  « nome ») frappent aussi des mots sans rapport (« nicolo », « colpa », « della »…). Sur les gloses ≥ 20 lettres déjà
  transcrites en P02/P03 (autres pages), 5 gloses sur 26 seraient exclues (189 lettres sur 817, 23 %). Le filtre est donc
  conservateur et peut retirer des séquences propres ; c'est accepté tel quel (règle approuvée), la perte est rapportée.

## Portion
Toutes les séquences chiffrées de **pos. 443 et 444 (doc. 97)**, sauf :
- toute séquence C dont la glose normalisée contient en entier la glose normalisée d'une des 25 séquences de
  T_doc97_p443.txt de longueur ≥ 3 lettres (« et » exclu du filtre) — filtre appliqué par script, avant le décodage.
  Précision fixée au gel : le filtre s'applique à toute la portion (443 et 444), comme écrit ; « glose normalisée » =
  glose après retrait des {…} et […] puis normalisation de la mesure ;
- la souscription et la date (clair).
Une « séquence » = une suite continue de signes chiffrés sur une même ligne écrite, coupée par les mots en clair ;
identifiant `PPP-LL-S` (page 443/444, ligne comptée depuis la 1re ligne écrite du corps, rang de la séquence dans la ligne).
Pas d'extension prévue. Une fois mesurée, la portion est grillée. 332 (H), 329-331 (P02), 158-161/167/351/254/299-300
(P03, non grillées mais réservées) hors portion.

## Transcription (comme P03)
1. T2 (sous-agent A, aveugle, modèle Opus) : signes en F01-F39, X:<desc>, K:<forme>, « ? » final = doute (un seul choix).
   P04_SIGNES_T2.tsv haché AVANT la glose.
2. Glose (même sous-agent, après le hachage) : C / P, {…} sur K:, […] notes. P04_GLOSE_T2.tsv haché.
3. T3 (sous-agent B, aveugle, ne voit pas T2) : signes de toute la portion, mêmes identifiants si possible. Haché.
4. Arbitrage jeton par jeton par A sur l'image (après gel de T2/T3), journal noté (P04_ARBITRAGE.md) ;
   P04_SIGNES_FINAL.tsv haché AVANT la mesure. Les gloses ne sont pas arbitrées (sauf C/P si l'arbitrage change le
   découpage d'une séquence, noté) ; P04_GLOSE_FINAL.tsv = P04_GLOSE_T2.tsv sauf ces cas, haché AVANT la mesure.
L'agent principal n'arbitre pas (il connaît K_G25) ; il ne modifie aucun fichier des transcripteurs.

## Mesure (UNE seule : `python3 -I p04/measure_p04.py P04_SIGNES_FINAL.tsv P04_GLOSE_FINAL.tsv`)
- Unités : séquences C après filtre. Seuil : Σ jetons F ≥ 300, sinon NON MESURABLE (plan B ci-dessous, PREREG séparé).
- Décodage, normalisation, métrique décisive (caractères = 1 − Σ édition / Σ longueur glose), témoins (200 permutations,
  graine 2380) : identiques à P03.
- **Critère : accord ≥ 0,85 ET ≥ meilleur témoin + 0,30**, sur l'ensemble 443-reste + 444.
- Couverture du catalogue : si les jetons X: dépassent 20 % des jetons des séquences C (précision fixée au gel :
  dénominateur = jetons F + X: + K: des séquences C retenues après filtre), le résultat est rapporté
  « NON CONCLUANT (catalogue F inadapté à la main de Niccolini) » et ne vaut ni validation ni infirmation de K_G25.
  Seuil fixé ici, non modifiable.
- Rapportés, non décisifs : 444 seule ; 443-reste seul ; accord en mots ; détail par séquence ; plafond b/g/z ;
  séquences exclues par le filtre et leurs jetons F.
- Leçon Fuensalida (comme P03) : si les témoins sortent hauts, on le dit tel quel, sans rien changer.

## Plan B si NON MESURABLE : mesure sur gloses partielles (à préenregistrer à part, jamais rétroactive)
- Unités : séquences P dont la glose couvre un segment contigu, avec bord gauche ou droit identifiable sur l'image
  (noté par le transcripteur AVANT la mesure : « glose alignée à gauche / à droite / incertaine » ; incertaine exclue).
- Métrique : meilleur alignement local (Smith-Waterman, coût 1 par substitution / trou) du décodage de la séquence
  contre la glose, normalisé par la longueur de la glose ; mêmes témoins par permutation, même alignement local.
- Contrôle propre au plan B : témoin supplémentaire = gloses permutées entre séquences (200, graine 2381).
  Critère : ≥ 0,85 ET ≥ max(meilleur témoin clé, meilleur témoin glose) + 0,30, sur ≥ 300 lettres de glose.
  Transcriptions aveugles P03 (non décodées, non grillées) réutilisables.
Le plan B n'est ni écrit ni exécuté dans le cadre de P04 ; il demande un PREREG séparé et l'accord de Brice.

## Suite selon résultat
- Validée : lecture des nues 2380 (docs 42 c. 90r, 49 c. 104r, 81 c. 177r, 90 c. 200r) avec K_G25 — étape suivante,
  soumise à l'accord de Brice (non faite dans P04) ; les quatre transcriptions aveugles et la feuille de McBratney
  (#797, targets/milan1494/niccolini/) peuvent servir de seconde passe, **créditées à Malcolm McBratney** ; fiche stricte,
  règle #728 (mots sûrs seuls ; plancher des textes courts : < 40 mots chiffrés → « read » si ≤ 2 trous). 2381 non
  revendiqué (#589).
- Non validée ou non concluante : plafonné ; aucun décodage présenté.
- Dans tous les cas, livrable possible chez Daniel : K_G25 + transcriptions aveugles + résultats P02/P03/P04, sans images
  (ASF), comme proposé sur #797 — sur accord de Brice seulement.
