# PREREG P05 — plan B : K_G25 inchangée, mesure sur gloses PARTIELLES (alignement local) — gelé le 20/11/2026

**Statut : GELÉ.** Accord de Brice le 20/11/2026 (« Fais le 1, plan B ») pour écrire et exécuter le plan B prévu dans
p04/PREREG-P04.md (section « Plan B si NON MESURABLE », gelée 60fae8c9…14c3a7). Écrit et haché (PREREG-P05.sha256) AVANT
toute nouvelle transcription (T3 B, arbitrage, 444-07, bords P03) et avant tout décodage. Aucune séquence de la portion n'a
jamais été décodée ni alignée par personne (P03 et P04 se sont arrêtés avant décodage, NON MESURABLE). Une seule mesure ;
jamais rétroactif ; tout écart = avenant daté, haché avant l'usage qu'il touche.

## Ce que l'agent qui gèle a vu (biais déclarés)
1. L'agent principal P05 (Opus 5.5) connaît K_G25 (structure, nombre de formes par lettre). Il a lu les fichiers TSV gelés de
   P03 et P04 (signes et gloses) pour écrire les règles de découpage des gloses ; il n'a décodé ni aligné aucune séquence, et
   n'a regardé aucune image de la portion. Il ne transcrit pas, n'arbitre pas, ne marque pas de bord.
2. Contrôle de taille fait AVANT ce gel, sans décodage (`--size`, comptes seuls, sur P04_SIGNES_T2/P04_GLOSE_T2 et sans bords
   P03) : doc. 97 seul donne 21 unités, **531 lettres de glose** (443 : 17 unités, 458 lettres ; 444 : 4, 73), 698 F, part X:
   0,111 ; filtre T97 : 9 séquences exclues. Le seuil de 300 lettres est donc atteignable sur doc. 97 seul.
3. Historique de la portion : doc. 97 est dans T (P01) ; 25 séquences courtes de 443 ont servi à K_T et K_T a été comparée à
   la clé 25 (test g3, 14/11 ; comptes, pas de décodage de 443) → filtre T97 mécanique gardé (ci-dessous). Le reste de 443 a été
   vu en P01 (page entière) sans transcription ; 444 n'a jamais été transcrite avant P04. Les pages P03 (158, 159, 161, 167,
   351, 254, 300, 299) n'ont jamais servi à K_T (avenant A1 : T = docs 6, 21, 32, 62, 97) ; elles ont été transcrites à
   l'aveugle le 14/11, jamais décodées : non grillées.
4. K_G25 (gelée le 14/11, kg25/K_G25.json) vient de la feuille Gabbrielli n° 25 (Yale Dataverse, Ilardi reel 58) ; passe 1
   agent principal (avait lu le résumé g3), passe 2 aveugle (feuille seule) : accord sauf un double nn/mm. Clé, carte F→G et
   catalogue F inchangés. K_G25 n'a ni b, ni g, ni z : plafond structurel (≈ 2-4 % des lettres) accepté tel quel.
5. Transcripteurs et arbitre : sous-agents aveugles (Opus), qui ne voient ni K_G25, ni K_T, ni CLE_KT.json, ni
   T_doc97_p443.txt, ni ce dossier, ni ses résultats, ni #589 / #797, ni les planches de la feuille Gabbrielli. B ne voit pas T2.

## Objets gelés (SHA-256, aussi dans PREREG-P05.sha256)
- kg25/K_G25.json = 3a81cd6d1c12e14a70530b9a251c28e5162a8a99200f9b22f9dc15f1c2c41611
- kg25/MAP_F_vers_G.json = eb23f56e49f38193309403ac1b55587e171fe43a042ed843b5404a4a4ec1461e
- SPOF_2 …/kg25-work/CATALOGUE_F.jpg = 5cbd6f5e4a1320136c2064f3bed682d1380b0f890c7ae08bb593d5d8dc8fab0a
- p05/measure_p05.py (sha dans PREREG-P05.sha256 ; testé à blanc, sortie p05/BLANC_P05.txt)
- transcription/T_doc97_p443.txt (lu par le filtre) = d958eefd9603a99a4cd66c544ce1676f0f8e112a5c477271894f7f5c4cb30925
- P04 (gelés 20/11) : P04_SIGNES_T2.tsv = 8059e6c5…95348 ; P04_GLOSE_T2.tsv = a1d9de8f…cb5e7
- P03 (gelés 14/11, « P03 FINAL » réutilisé tel quel) : P03_SIGNES_T2.tsv = ef6f9c6c…f93f5 ; P03_GLOSE_T2.tsv = 47231ba9…54a6d4fc ;
  P03X_SIGNES_A2.tsv = c58ea0b9…00dbf ; P03X_GLOSE_A2.tsv = 03316fc2…ad8f64 ; (P03_SIGNES_T3.tsv = a5910b4c…a7c7, non utilisé)
- p05/P05_LISTE_BORDS_P03.tsv (liste mécanique des séquences P03 à faire marquer par E, sortie de `--list-p03`)
- Images SPOF_2 …/images/ : 443 = 129351b3…9d9e ; 444 = c21eff91…29f1 ; 158 = ea3ada16…0034 ; 159 = 58222950…eeb7 ;
  161 = 661ec05c…05bd ; 167 = b92dfe34…f73b5 ; 254 = 997465a4…0a24 ; 299 = f39faff9…d61d ; 300 = c9ce3f25…347b ;
  351 = 071a70c6…2c27 (valeurs complètes dans PREREG-P05.sha256).

## Portion
- **Doc. 97, pos. 443 (reste) + 444** : toutes les séquences chiffrées transcrites par A (P04, gelées) + **444-07** (ajoutée par
  l'arbitre, voir procédure), signes arbitrés T2/T3. Souscription et date (clair) exclues.
- **P03** (pages 158, 159, 161 : T2 du transcripteur A ; 167, 351, 254, 300, 299 : A2) : transcriptions aveugles gelées le
  14/11, réutilisées telles quelles. Précision : P03 n'a pas de fichier FINAL (ni arbitrage T2/T3 sur la base, ni T3 sur
  l'extension : NON MESURABLE avant) ; « P03 FINAL » = T2 ∪ A2 tels que gelés. Pas de nouvel arbitrage P03.
- Hors portion : 332 (H), 329-331 (P02), nues 2380 (183, 209, 357, 403), 2381 (439-442).
- Après la mesure, toute la portion est **grillée** (doc. 97 et les 8 pages P03), quel que soit le résultat.

## Unités
- Séquences marquées **P** (glose partielle) dont un **bord** a été marqué **« gauche » ou « droite »** par un transcripteur
  AVANT la mesure ; « incertaine », bord absent, et séquences **C** exclues (le plan B porte sur les P).
  - doc. 97 : bord lu dans la colonne notes de la glose (`aligne:gauche|droite|incertaine`), écrite par A le 20/11 ; pour 444-07,
    marqué par l'arbitre.
  - P03 : les transcripteurs de P03 n'ont pas marqué les bords de façon systématique. Précision fixée ici : une passe aveugle
    **E** (sous-agent neuf, Opus) marque, sur l'image, le bord de chacune des 73 séquences de P05_LISTE_BORDS_P03.tsv (séquences
    P03 marquées P ayant au moins un fragment de glose ≥ 5 lettres, liste tirée par le script, sans décodage), sans rien changer
    aux signes ni aux gloses. Fichier P05_BORDS_P03.tsv (`id<TAB>bord`), haché AVANT la mesure. Règle : « gauche » si le
    premier mot lisible de la glose est au-dessus du premier signe chiffré de la séquence ; « droite » si le dernier mot lisible
    est au-dessus du dernier signe ; les deux → « gauche » ; sinon « incertaine ».
- **Filtre T97** (gardé, mécanique, avant décodage) : toute séquence de 443/444 dont la glose normalisée (après retrait des
  {…} et […], normalisation de la mesure) contient en entier la glose normalisée d'une des 25 séquences de T_doc97_p443.txt de
  longueur ≥ 3 lettres (« et » exclu) est retirée. Il s'applique au doc. 97 seulement (portion de P04, comme dans P04) ; les
  pages P03 n'ont jamais été dans T et ne sont pas filtrées. Le filtre est conservateur (motifs courts del, col, pos…) : accepté.

## Glose → fragments (règle fixée ici, appliquée par le script)
- {…} (mots portés par un jeton K:) retirés, comme P03/P04.
- **Lacune** (coupe la glose en fragments) : « ... » / « .. » / « … » ; crochet isolé (entouré d'espaces : [?], [..],
  [illisible], [struck], [gloss ends…]) ; jeton fait seulement de « ? » (« ?? »).
- Crochet collé à un mot (« pote[?] », « [ri?]sentire ») : retiré sans coupure. « ? » dans ou autour d'un mot : retiré (le mot
  compte, comme en P03).
- Chaque fragment est normalisé comme en P03 (minuscules ; v→u, j/y→i, k→c, h supprimé ; hors a-z supprimé ; doubles réduites).
  **Fragments < 5 lettres normalisées retirés** (trop courts pour un alignement local : inflation). Une unité sans fragment est
  retirée. Les lettres comptées = lettres des fragments retenus.

## Mesure (UNE seule) :
`python3 -I p05/measure_p05.py --measure P05_SIGNES_FINAL.tsv P05_GLOSE_FINAL.tsv P05_BORDS_P03.tsv`
- Décodage = P03 : F → G → valeur K_G25 ; « ? » final ignoré (le choix compte) ; X: et K: → vide ; puis normalisation.
- **Métrique (plan B)** : alignement local à coûts unitaires (Smith-Waterman, coût 1 par substitution / trou) des fragments de
  la glose, **dans leur ordre**, sur des sous-chaînes disjointes du décodage de la séquence ; le décodage est sauté gratuitement
  avant, entre et après les fragments (la glose partielle ne couvre qu'une partie de la séquence ; les lacunes cachent un nombre
  inconnu de lettres). Coût d'une unité ≤ ses lettres de glose.
  **Accord = 1 − Σ coûts / Σ lettres de glose** (normalisé par la longueur de la glose, agrégé comme P03).
- **Seuil de taille : Σ lettres de glose ≥ 300**, sinon NON MESURABLE.
- **Témoins clé** : 200 clés = valeurs de K_G25 permutées entre les 39 formes, `random.Random(2380)`, même alignement.
- **Témoins glose** : 200 permutations des listes de fragments entre unités, `random.Random(2381)`, clé K_G25, même alignement
  (points fixes permis : conservateur).
- **Critère : accord ≥ 0,85 ET accord ≥ max(meilleur témoin clé, meilleur témoin glose) + 0,30.** Non modifiable.
- **Règle X:** : si les jetons X: dépassent 20 % des jetons (F + X: + K:) des unités retenues → « NON CONCLUANT (catalogue F
  inadapté) », ni validation ni infirmation.
- Rapportés, **non décisifs** : par source (P04/doc. 97 vs P03) et par page (accord, meilleur témoin) ; accord en mots (mots de
  glose ≥ 3 lettres retrouvés tels quels dans le décodage) ; plafond b/g/z ; séquences exclues par T97 ; détail par unité ;
  comptes de l'arbitrage (jetons changés T2→FINAL, désaccords T2/T3).

## Test à blanc (fait avant le gel ; p05/BLANC_P05.txt, données factices chiffrées avec K_G25)
| blanc | cas | lettres | accord | témoin clé max | témoin glose max | résultat |
|---|---|---|---|---|---|---|
| 1 | 10 gloses partielles (≈ 56-62 lettres, une lacune interne) sur leurs séquences | 436 | 0,9702 | 0,3670 | 0,6124 | VALIDE |
| 2 | inflation : 60 gloses de 6 lettres sur ≈ 80 lettres décodées | 360 | 0,9806 | 0,4944 | 0,6389 | VALIDE |
| 2b | inflation forte : 70 gloses de 5 lettres sur ≈ 180 lettres | 350 | 0,9686 | 0,5571 | 0,7543 | **NON VALIDE** |
| 3 | = 1 + 25 % de X: | 436 | 0,9702 | 0,3670 | 0,6124 | NON CONCLUANT |
| 4 | < 300 lettres | 135 | — | — | — | NON MESURABLE |
| 5 | signes faits avec une autre clé | 436 | 0,3257 | 0,3739 | 0,3326 | NON VALIDE |
| 6 | clé juste, 30 % des jetons F faux | 436 | 0,7477 | 0,3670 | 0,5298 | NON VALIDE |
| 7 | clé juste, 15 % des jetons F faux | 436 | 0,8234 | 0,3601 | 0,5505 | NON VALIDE |
Filtre T97 vérifié (séquence factice « il signor lodovico andava a genova » exclue ; bord incertain et C exclus).
Leçons déclarées d'avance, sans rien changer : (a) l'alignement local **gonfle les témoins** quand la glose est courte devant
le décodage (témoin clé 0,37 → 0,56 ; témoin glose 0,61 → 0,75) ; le témoin glose est le plus haut (italien contre italien
avec la vraie clé) et, avec peu d'unités, il varie beaucoup ; (b) le critère est **sévère pour les erreurs de transcription** :
à 15 % de jetons faux, une clé juste échoue (0,82). Un NON VALIDE ne vaut donc pas infirmation de K_G25 si la qualité de
transcription est en cause ; il est rapporté tel quel (leçon Fuensalida : témoins hauts dits tels quels).

## Procédure (dans cet ordre ; chaque fichier haché avant l'étape suivante)
1. Gel de ce PREREG + script + liste P03 (PREREG-P05.sha256). Dossiers de travail neufs sur SPOF_2 …/p05-work/{B,E,A}
   (copies des images de la portion + CATALOGUE_F.jpg seulement ; rien d'autre).
2. **T3 (sous-agent B, aveugle, Opus)** : signes de toutes les séquences chiffrées de 443-444, y compris la dernière ligne de 444
   (444-07 si chiffrée), mêmes conventions que P04 (Fxx, X:, K:, « ? »). P05_SIGNES_T3.tsv haché. B ne voit pas T2.
3. **Bords P03 (sous-agent E, aveugle, Opus ; en parallèle de 2)** : images P03 + CATALOGUE_F + liste des 73 séquences
   (id, glose) + signes gelés de ces séquences pour les repérer. P05_BORDS_P03.tsv haché.
4. **Arbitrage (sous-agent A′, aveugle neuf, Opus ; A de P04 n'est plus disponible)**, après le hachage de T3 : reçoit T2 et
   T3 (signes seuls), arbitre jeton par jeton sur l'image, garde le découpage et les ids de T2 (aucune scission ; tout changement
   de bornes noté), ajoute 444-07 (signes). Journal P05_ARBITRAGE.md. **P05_SIGNES_FINAL.tsv haché.** Puis, seulement
   après ce hachage, glose de 444-07 (C/P, notes `aligne:…`) avec les conventions de P04 ; **P05_GLOSE_FINAL.tsv** =
   P04_GLOSE_T2.tsv + la ligne 444-07, haché. Les autres gloses ne sont pas arbitrées.
5. **UNE mesure** avec le script gelé (sortie RESULTAT_P05_brut.txt, hachée). Portion grillée.
L'agent principal ne transcrit pas, n'arbitre pas, ne marque pas de bord et ne modifie aucun fichier des sous-agents.

## Suite selon résultat
- VALIDE : K_G25 validée sur gloses partielles ; la lecture des nues 2380 (docs 42, 49, 81 c. 177r, 90) est l'étape suivante,
  **soumise à Brice, non faite ici** (secondes passes possibles : transcriptions de McBratney #797, à lui créditer).
- NON VALIDE / NON CONCLUANT / NON MESURABLE : plafonné ; aucun décodage présenté ; voie restante : filza 39 Dieci di Balìa (ASF)
  ou reproduction HD.
- Aucune PR, aucun post, aucun mail, aucun navigateur, aucune API payante dans P05.
