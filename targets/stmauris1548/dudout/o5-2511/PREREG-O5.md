# PREREG-O5 — stmauris1548 (cible WAINUT), lettre du 12 mars 1548, cc. 6v-8v — lecture par le sens — 25/11/2026, Claude Opus 5.5 (local), fil 🔓

Préparé le 25/11/2026 à la demande de Brice (accord pour préparer une mesure par lecture du sens sur une portion NEUVE, les
pages jamais ouvertes). Gelé par SHA-256 (`PREREG-O5.sha256` + ligne de HANDOFF.md) AVANT toute découpe, transcription,
décodage ou lecture de cc. 6v-8v, et sans que personne ait regardé ces pages (seules leurs dimensions ont été lues avec `sips`,
sans affichage). **Ce fichier ne transcrit, ne décode, ne lit et ne mesure rien.** L'exécution demande un « lance » de Brice.

## 0. Pourquoi O5, et ce qui change
- O2 (c. 1r), O3 (cc. 1v-2r) et O4 (cc. 5r-6r) ont mesuré la clé de WAINUT par la couverture lexicale M (seuil absolu 0,85) :
  0,718 / 0,784 / 0,780, trois FAIL, toujours sur le seul seuil absolu (marges sur les témoins 0,28 / 0,39 / 0,37 ; z O4 8,4).
- En O4, la note marginale en clair de 5r, lue après la mesure, est un déchiffrement d'époque des lignes L01-L03 : elle
  concorde mot pour mot avec le décodage O4 (`../o4-2511/NOTE-MARGE-5r.md`). Tout le décodage de 5r-6r
  (`../o4-2511/MESURE-O4.txt`) se lit en français suivi du XVIᵉ s. ; M le sous-évalue (texte sans coupure, graphie d'époque).
- O5 remplace donc le critère par la **règle de Daniel (lecture par le sens, ≥ 95 %)**, appliquée par deux lecteurs
  indépendants qui ne voient que le décodage, et garde M comme **contrôle contre les témoins** (marge ≥ 0,30), sans seuil absolu.
- **cc. 5r, 5v, 6r sont grillées** : jamais réutilisées, recalculées ni montrées aux agents d'O5 ; rien de leur décodage ni de la
  note de 5r n'entre dans la clé ou dans un brief. Les lettres de 1547 (cc. 1r-2r, O2/O3) le sont aussi.

## 1. Les règles (rappel, appliquées telles quelles)
- **Règle de Daniel Bourdeau** (`_shared/cyphersolver/CONTRIBUTING.md`, l. 36, commit b13dd55072, SHA-256 du fichier
  3b2847636d59a04bd5b08b0b8574f7ec580844725bbff6b827a650c4e3d035f6) : un document compte comme **lu quand 95 % de ses mots se
  lisent par le sens**. On rapporte séparément les mots **sûrs**, **{probables}**, **[restitués par le sens]** et
  **‹irrésolus›**, chaque mot non sûr avec sa justification. **Une valeur tirée du seul sens reste {probable}** (au mieux).
  **Une restitution [x] ne contredit jamais des lettres sûres du chiffre.** **On garde la graphie du chiffre**, sans moderniser.
- **Portion ≥ 300 caractères chiffrés**, blocs déclarés d'avance (pages et lignes ; le nombre de lignes n'étant pas connu sans
  ouvrir les pages, c'est la règle de choix qui est déclarée, §2).
- **Clé de WAINUT figée** (§3) ; rien appris d'O2-O4 (décodages, note de 5r) n'y est ajouté ; les noms sans valeur (13, @2,
  N6o, mx3…) restent sans valeur.
- Portion déjà mesurée = grillée ; une seule exécution ; jamais rétroactif.

## 2. Portion Q — désignée AVANT toute vue des pages
- **Q = toutes les lignes chiffrées de cc. 6v, 7r, 7v, 8r, 8v** (canevas 3 à 7 du manifest 65514839…), dans l'ordre des pages,
  lignes numérotées `6v L01…`, `7r L01…`, … de haut en bas dans chaque page. C'est toute la réserve R laissée neuve par O4.
- **Règle de choix des lignes** (appliquée par l'orchestrateur sur vues réduites ≤ 1/4, sans lire) : est une ligne de Q toute
  ligne d'écriture qui porte des signes chiffrés, y compris les lignes partielles en début ou fin de bloc. Une ligne mêlant
  clair et chiffre : seule la partie chiffrée est gardée (le clair est masqué). Sont exclus : texte en clair, notes marginales,
  gloses interlinéaires d'une autre main, adresse, souscription, mentions dorsales et cotes. Une page sans ligne chiffrée
  compte 0 ligne (consigné). La liste (page, nombre de lignes, coordonnées) est figée dans `tools/make_crops_o5.py`, dont le
  SHA-256 est consigné avec l'heure AVANT le lancement de la passe A.
- **Clair et notes de 6v-8v** : s'il y en a, ils sont **masqués (peints en blanc) avant la découpe** et **ne sont lus par
  personne avant le verdict** ; ni les transcripteurs, ni l'arbitre, ni les lecteurs ne les voient. L'orchestrateur ne les voit
  qu'en vignette réduite pour poser les masques, sans les transcrire ni s'en servir. Après le verdict seulement, ils peuvent être
  lus et comparés au décodage (comme la note de 5r), hors critère, sans rien changer au verdict.
- **Taille** : après la fusion (§4) et AVANT le décodage, on compte les jetons fusionnés dont le nom est un nom de clé (noms
  seulement). **< 300 → NON MESURABLE, arrêt** (aucune autre page neuve dans cette lettre ; une suite éventuelle = une autre
  lettre et un nouveau PREREG). Aucune extension, aucun ajout de pages grillées.
- Dimensions des images (lues par `sips`, sans affichage) et SHA-256 (= ceux de PREREG-O4 §1, revérifiés le 25/11) :
  c06v.jpg 4983×7103 ab26245b16c2da866925db8c1178fdacc95bc033af0511a402dd467d208bf9be (canevas 3)
  c07r.jpg 5007×7124 181f5beed7cb8cfb5be077401dec532e3bad7c967999674b6576d494fd612bec (canevas 4)
  c07v.jpg 5007×7144 5a58769a159ef0b6ade1f5c492abae963c97d62a032dac71e75a9025a3f17f76 (canevas 5)
  c08r.jpg 4971×7116 0e44580a8652908eab6be08c73ca767b1a34fcbb5391eaa05162ca39fdb31eff (canevas 6)
  c08v.jpg 5011×7152 9a5ec5641b57b804841a1c454fa980136a8a08cbf89e9a59224829619f6dd5ee (canevas 7)
  Sur SPOF_2 seulement (`scans` → `../o2-2311/scans` → /Volumes/SPOF_2/…/o2-2311/scans), Estense CC BY-NC-SA, jamais republiées.
  Recadrages, vues d'ensemble, cases d'arbitrage : sur SPOF_2 seulement (liens symboliques `crops`, `preview`,
  `ARBITRAGE/boxes` vers /Volumes/SPOF_2/Archives-Veille-cyber/dechiffrements-europe/stmauris-granvelle-1548/o5-2511/).

## 3. Entrées gelées
- Clé : `../o2-2311/wainut-key.tsv` **b9e69238cd30569c01b1566bc6548fb1d16a030c652ecca053c6a98b89d5e034** (= cyphersolver
  main b81c613843, = PREREG-O4), utilisée INCHANGÉE.
- Transcripteurs (`input/`, mêmes fichiers qu'O4) : `SIGNS.md` 678be0a407b03ba391d5594e13d88b21c1e0394e856d830b6c1243c7c2ef85aa ;
  `SHAPES-KEY-NAMES.md` 107506b175d73aeb7d833cf900bfdd4b40446f5a403dabcf6f7296c41cf0509c ; brief `BRIEF-PASSE-O5.md`
  43683a71d8a50424e762a5f042739c0d2d02a9e2125248329466fb413b5ffaa5 (= BRIEF-PASSE-O4 sur le fond, pages et chemins changés).
- Lecteurs : `BRIEF-LECTURE-O5.md` 87935890c3211625a2b22aecf16724ddc01a7cd84fb0ee6808a2fd9e1bf0f909.
- Lexique du contrôle M : `../../../_shared/cyphersolver/lang/corpora/fr-1520s-diplomatic.txt`
  813012bd28f1ee3111fe8c0800cfa35ab638b83c7038ab3eef16c63e088b617e.
- Outils repris d'O4, INCHANGÉS (lancés depuis `o5-2511/`, chemins relatifs au dossier courant) :
  | outil | SHA-256 | rôle en O5 |
  |---|---|---|
  | `../o4-2511/tools/compare_o4.py` | b80375653a1e8fc9f40747b9ded2802a11e7f6c343033916c390e7e9a220c038 | accord A/B, `disputes.json` |
  | `../o4-2511/tools/arb_package_o4.py` | ab60deb45f0296054eca2930cd80acc2a252694119cf6a5aa73b5edfe6d3639c | descriptions pour l'arbitre (sans valeurs) |
  | `../o4-2511/tools/measure_o4.py` | f940b3545e51bb3f5f65dfeafded612a80d418d71f39141c76b5f5655ae6c4b7 | décodage mécanique + M + 200 témoins + z |
  | `../o2-2311/wainut-scripts/compare.py` | 364d8233f783da376b4342a7f39bbbef497e5c3517951a5af05c3512df14a3f3 | `load` seulement (pas de BMAP) |
  | `../o4-2511/tools/make_crops_o4.py` | 49138df631fb988b1762d9da7797f7b9f97d3554efbbc247b87581c7245f5856 | modèle de `make_crops_o5.py` |
- Outils neufs d'O5, écrits et testés sur données inventées (aucune donnée de 6v-8v ni de 5r-6r) AVANT ce gel :
  | outil | SHA-256 | rôle |
  |---|---|---|
  | `tools/merge_o5.py` | 8a3ae8bd11b2303de13ae85dadeb69c5fb7af2dc8d27212bab7938245bdd145b | fusion (= merge_o4 générique) + compte des jetons à nom de clé |
  | `tools/name_step_o5.py` | 319ef995551ede189bc1f13eea261802b8ea38f50de5e9e82a2743095d6e0285 | renommage tS- déclaré d'avance (§5) |
  | `tools/extract_decode_o5.py` | b45938a6706e3e0aecdd00af1463fe0d75a72ec0fdf11fd794b5abd0cdeab3a7 | décodage seul → `lecture-input/DECODE-O5.txt` |
  | `tools/check_lecture_o5.py` | 76e3acac8727662097ca17a4f31d9521f83c0a5035cb8541bb33edb0520c53b4 | forme + décompte d'une lecture |
  | `tools/compare_lectures_o5.py` | 5144d4d8298d4572a60e89d2ec72d5254917ca46dc1f05b45269d746e42a2fa9 | kappas et accord L1/L2 |
  | `tools/verdict_o5.py` | 82e41a2cd5ac852d40a49d0f816fd427f20c526355ad4a989dea1a37c5a7c248 | verdict unique (§10) |
- Écrit à l'exécution (comme en O4), SHA consigné avant la passe A : `tools/make_crops_o5.py` = make_crops_o4.py avec le seul
  tableau PAGES de 6v-8v (lignes, masques) et `HERE` = `o5-2511/`. Il découpe des images ; il ne lit ni nom ni valeur.
- Python : toujours `python3 -I`. PIL n'est pas visible sous `-I` : `make_crops_o5.py` (seul outil qui en a besoin) ajoute
  explicitement le chemin site-packages de l'utilisateur à `sys.path`, pour PIL seulement (même procédé que PREREG-O4 §1) ;
  dimensions et contrôles d'images par `sips`.

## 4. Protocole (étapes 1-2) : deux passes aveugles, porte, arbitrage aveugle, fusion gelée
1. **Passes A et B** : deux agents Opus neufs, séparément ; chacun ne voit que les recadrages de Q, `input/SIGNS.md`,
   `input/SHAPES-KEY-NAMES.md` et `BRIEF-PASSE-O5.md`. Ni clé, ni valeur, ni décodage, ni clair, ni l'autre passe, ni O2-O4.
   Chaque passe gelée par SHA-256 avant la comparaison. Noms propres `t1…` (illisible `t?`), préfixés `tA-…` / `tB-…`.
   Vérifié : aucun nom de clé ne commence par `t` ni n'est `NIL` (measure_o4.py l'affirme).
2. **Porte** : accord A/B (`compare_o4.py`, ligne par ligne, difflib, noms comparés tels qu'écrits) **< 0,80 → ARRÊT, rien
   n'est décodé**. Toute position `t` est un désaccord par construction.
3. **Arbitrage aveugle** : un 3ᵉ agent Opus neuf (C) voit, pour chaque position disputée, le recadrage (position encadrée par
   lui-même à partir du rang et du contexte, comme en O4 point 5) et les descriptions des candidats
   (`ARBITRAGE/CANDIDATS-DESCRIPTIONS.md`, par `arb_package_o4.py`), jamais de valeur ; il choisit A, B ou « neither » (→ `NIL`,
   répété max(len A, len B)). Égalité entre deux noms `t` de même description → A (sans effet : aucun `t` ne donne de lettre).
4. **Fusion** `transcription_1548-03-12_Q_merged.txt` (`merge_o5.py`) **gelée par SHA-256 avant tout décodage**. Plus aucune
   retouche de signe. Compte des jetons à nom de clé → règle de taille du §2.

## 5. Étape de nommage, déclarée d'avance (leçon d'O4, point 4)
`name_step_o5.py` renomme `tS-<nom>` tout jeton de la fusion qui n'est ni nom de clé, ni `NIL`, ni `t…`, ni barré (`…_`) —
en pratique les composés base + marque haute sans ligne dans key.tsv. Copie `…_Q_merged_named.txt` (SHA consigné), journal des
noms et effectifs ; la fusion gelée n'est pas modifiée. Ces jetons ne donnent aucune lettre. Ce n'est pas une seconde mesure :
aucune lettre n'a encore été produite. La garde de measure_o4.py ne doit alors plus rien trouver ; si elle s'arrête quand même
(ABORT), arrêt et consignation, sans autre changement.

## 6. Étape 3 : décodage mécanique (et contrôle M), une seule fois
`python3 -I ../o4-2511/tools/measure_o4.py transcription_1548-03-12_Q_merged_named.txt ../o2-2311/wainut-key.tsv ../../../_shared/cyphersolver/lang/corpora/fr-1520s-diplomatic.txt 251125 > MESURE-O5.txt`
puis `tail -1 MESURE-O5.txt > MESURE-O5.json` et `python3 -I tools/extract_decode_o5.py` → `lecture-input/DECODE-O5.txt`
(lignes de décodage seules : ni M, ni témoins, ni verdict, ni noms). **Graine 251125.** Clé inchangée ; `?` = signe sans valeur.
La ligne `VERDICT` de measure_o4.py (seuil 0,85 d'O2-O4) est **ignorée** ; M, max/moyenne/écart-type des 200 témoins et z sont
repris par verdict_o5.py. Une seule exécution ; aucune correction du décodage.

## 7. Étapes 4-5 : deux lectures par le sens, indépendantes
- **Lecteur L1**, puis **lecteur L2** : agents Opus neufs, séparés (L2 n'a aucun accès à L1, ni l'inverse). Chacun ne voit que
  `lecture-input/DECODE-O5.txt`, `lecture-input/BRIEF-LECTURE-O5.md` (copie du brief gelé) et
  `lecture-input/check_lecture_o5.py` (copie de l'outil gelé) ; ni images, ni signes, ni transcriptions, ni clé, ni M, ni O2-O4
  (en particulier ni le décodage de 5r-6r ni la note de 5r), ni web. Seul contexte donné : « français du milieu du XVIᵉ s.,
  correspondance diplomatique » (BRIEF-LECTURE-O5).
- Chacun segmente tout le texte et classe **chaque mot** : sûr / {probable} / [restitué] / ‹irrésolu› (et `(nulle)`, qui n'est
  pas un mot), selon le format de BRIEF-LECTURE-O5 : toutes les lettres du décodage reprises dans l'ordre, aucune changée ;
  lettres données par le sens en MAJUSCULES (elles remplissent un `?` ou s'insèrent, ne remplacent jamais une lettre) ;
  graphie du chiffre gardée. Il écrit `LECTURE.txt` et la fiche `JUSTIFICATIONS.tsv` (une justification par mot non sûr).
- Le lecteur corrige la FORME jusqu'à `FORME OK` (contrôle sans jugement de sens). Lecture et fiche gelées par SHA-256 à la
  remise ; plus aucune retouche. Un lecteur qui ne livre pas une lecture `FORME OK` est remplacé une fois par un agent neuf ;
  second échec → ARRÊT (« lecture non livrée », pas de verdict).

## 8. Décompte (par `check_lecture_o5.py --json`, pour chaque lecteur)
- Sûr : lettres du décodage seules, ni majuscule ni `?`. Probable : lettres du décodage, au plus 1 lettre donnée par le sens
  par mot et au moins 2 lettres du décodage. Restitué : au-delà (ou mot entier ajouté). Irrésolu : 1 mot, ou n avec `‹…|n›`.
- **lus = sûrs + probables + restitués ; total = lus + irrésolus** ; part lue = lus / total ; part restituée = restitués / total.
- Garde-fous : une nulle collée à un mot qui contient une lettre donnée par le sens fait compter ce mot comme irrésolu
  (remplacement déguisé interdit) ; si les caractères marqués nuls dépassent **5 %** des caractères du décodage, chaque nulle
  compte en plus comme 1 mot irrésolu.

## 9. Accord entre lecteurs (`compare_lectures_o5.py`)
kappa de Cohen à 5 classes (S/P/R/I/N) sur les caractères du décodage, kappa lu / non lu, et **accord de segmentation**
F1 = 2 × mots identiques / (mots L1 + mots L2) (même étendue dans le décodage, mêmes lettres, y compris celles données par le
sens). Les kappas sont rapportés ; le F1 est un critère (§10).

## 10. Critère de succès (étape 6), verdict unique (`verdict_o5.py`)
`python3 -I tools/verdict_o5.py MESURE-O5.json lecture-L1/L1.json lecture-L2/L2.json ACCORD-L1L2.json`
**PASS si et seulement si toutes ces conditions sont remplies :**
- C0 lettres décodées ≥ 300 (sinon **NON MESURABLE**, pas FAIL) ;
- C1 **part des mots lus par le sens ≥ 0,95**, pour L1 **et** pour L2 ;
- C2 **part des mots restitués ≤ 0,05** (plafond), pour L1 **et** pour L2 ;
- C3 **marge lexicale M − max(200 témoins, graine 251125) ≥ 0,30** (M lui-même : information, sans seuil absolu) ;
- C4 accord de segmentation L1/L2 F1 ≥ 0,80.
Rapportés pour information : M, moyenne et écart-type des témoins, z, kappas, effectifs S/P/R/I et nulles de chaque lecteur.

## 11. Conditions d'arrêt et d'échec (fixées maintenant)
- **ARRÊT avant décodage** : un SHA d'entrée ≠ ce PREREG ; un agent (transcripteur, arbitre) a vu clé, valeur, décodage, clair
  de 6v-8v ou une page grillée (sa sortie est annulée et refaite une fois par un agent neuf ; second incident → arrêt) ; porte
  A/B < 0,80 ; < 300 jetons à nom de clé (NON MESURABLE) ; ABORT de la garde après l'étape de nommage.
- **ARRÊT après décodage, sans verdict** : un lecteur a vu autre chose que les trois fichiers permis (sa lecture est annulée et
  refaite une fois par un agent neuf ; second incident → arrêt) ; lecture non livrée (§7).
- **FAIL** : C1, C2, C3 ou C4 non rempli. Q est alors grillée : aucune nouvelle lecture, transcription, clé ou mesure sur Q ;
  la lettre du 12 mars 1548 est épuisée pour cette clé. Le décodage et les lectures restent des données.
- **PASS** : la clé de WAINUT est validée sur une portion neuve par la règle de Daniel et contre les témoins. Suite possible,
  seulement avec l'accord de Brice : lecture complète de la lettre (5r-8v, lecture et non test) et proposition à WAINUT/Daniel
  avec crédit à WAINUT ; statut « read » seulement si la lecture de tout le document atteint 95 %.
- Dans tous les cas, `RESULTAT-O5.md` donne la chaîne des SHA horodatés, l'accord A/B, l'arbitrage, la taille, M et témoins,
  les décomptes des deux lecteurs, les kappas, les conditions C0-C4 et tout point d'exécution. Pas de PR, rien poussé, posté ni
  envoyé sans l'accord de Brice.

## 12. Écarts d'O4 déclarés d'avance cette fois
1. **Redressement des lignes penchées** : chaque ligne est donnée par son centre à gauche et à droite (profil d'encre sur pages
   réduites + contrôle visuel de lignes-guides) et redressée par cisaillement affine ; demi-hauteur 100 px, réduite à 0,6 ×
   l'interligne médian de la page si celui-ci est < 170 px (consigné).
2. **Masquage du clair** : sur toute page de Q qui porte du clair, une note ou une glose, tout ce qui n'est pas ligne chiffrée
   est peint en blanc AVANT découpe (polygones à garder dans make_crops_o5.py) ; des hampes du clair peuvent rester visibles au
   bord ; consigne aux transcripteurs : les ignorer.
3. **Garde des noms sans ligne de clé** : renommage `tS-<nom>` journalisé (§5), prévu cette fois, appliqué à tout nom concerné
   (et non à une liste fixée après coup).
4. **Arbitre** : C localise et encadre lui-même chaque position (cases sur SPOF_2), descriptions `t` copiées des en-têtes des
   passes (renommées tA-/tB-).
5. **Fusion générique** : merge_o4.py avait 104 désaccords et un en-tête en dur ; merge_o5.py lit le nombre dans ARBITRAGE.tsv.
6. **Seuil absolu 0,85 abandonné** pour la règle de Daniel + marge sur les témoins (accord de Brice : mesure par le sens).
7. Images, recadrages, vignettes et cases sur SPOF_2 seulement ; zooms temporaires des agents effacés ; rien republié.
