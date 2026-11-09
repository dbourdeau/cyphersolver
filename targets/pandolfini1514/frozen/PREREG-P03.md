# PREREG-P03 — pandolfini-francia-1514-15 (cat. Bourdeau 2389) — écrit le 09/11/2026
Écrit et haché AVANT : la clé v3, toute localisation, tout regard (vignette, en-tête, position) et toute transcription
de MAP LXXII 342 et 343. PROTOCOLE.md (7d790482…) et PREREG-P02 (09ffc035…) restent en vigueur pour tout ce que P03 ne change pas.

## Statut de P02, relu avant ce prérapport
PREREG-P02 ne prévoit QUE deux issues (« ≥ 0,85 ET ≥ témoin + 0,30 » = validée ; « sinon NON VALIDÉE ») : aucune
catégorie « partiel ». P02 (0,691 ; témoin 0,341 ; marge 0,350) reste donc NON VALIDÉE, sans repêchage. 340/341 sont grillés.

## Regards déclarés avant ce prérapport
- Déjà vus et grillés : T de P01 (308, 318, 319), 345/346 (P01), 340/341 (P02 : H2_340_c430r.txt, REF_H2_341.txt,
  RESULTAT_MESURE_P02.json, décodé D de P02).
- AUCUN regard sur 342 ni 343. Seuls les noms de fichiers des positions 867-878 ont été listés (aucune image ouverte).

## Clé v3 (cle/CLE_v3.json, gelée par cle/CLE_v3.sha256 AVANT tout regard sur 342/343)
- = CLE_v2.json (3617591e…) inchangée, PLUS des compléments tirés UNIQUEMENT de la paire grillée 340/341 (alignement du
  décodé de P02 sur REF_H2_341.txt), chacun consigné avec ses occurrences dans cle/T3_alignements_340_341.tsv :
  signe p = u (3/3 : ultime, uno, seguire) ; g# = gg (veggio) ; jeton 2^2 = co (4/4 : cose, cosa ×3 ; 2 nu/2^5 restent b) ;
  Q^0 = per (« et per fino »). Rien d'autre (les écarts dus à la lecture des signes ne sont pas « corrigés » dans la clé).
- Règle .4. de P02 inchangée.

## Portion tenue à l'écart H3 et référence R3 (règle fixée sans avoir vu les pièces)
- Paire attendue : 342 = pièce chiffrée ; 343 = son déchiffrement d'époque. Vérification PAR L'EN-TÊTE SEULEMENT
  (adresse/titre/date de 342 ; en-tête de 343 du type « D.r di … » ou mention de déchiffrement, ou même date/destinataire),
  sans lire le corps. Si l'en-tête ne permet pas d'établir la paire : AUCUNE mesure (pas d'autre repli), consigné.
- H3 = PREMIER bloc chiffré continu de 342 (du premier signe chiffré jusqu'au premier passage en clair d'au moins trois
  mots, ou la fin du texte) ; si ce bloc a moins de 4 lignes, H3 = ce bloc + le suivant (même règle).
- R3 = le passage correspondant de 343, borné par les mots en clair qui encadrent le bloc dans 342 (jamais par un décodage) ;
  si le bloc commence la lettre, début = début du texte de 343 après l'en-tête. Mots non lus de R3 omis et consignés.
  Si le déchiffrement est interlinéaire sur 342, R3 = la glose de ce bloc, transcrite après le gel de H3 sans décodage.
- Ordre : localisation → transcription de H3 (jetons LEGENDE.md + ajouts de forme consignés, sans appliquer de valeurs)
  → gel transcription/TRANSCRIPTION_H3.sha256 → transcription de R3 → gel transcription/REF_H3.sha256 → UNE mesure.
  Rien n'est décodé dans H3 avant la mesure ; R3 n'est jamais regardée en même temps qu'un décodage de H3.

## Mesure unique (sur H3)
- Script mesure/measure_p03.py = measure_p02.py (décodage, normalisation, formule 1 − Levenshtein/longueur R, accord en
  mots rapporté non décisif) + verdict à trois catégories ; testé sur données synthétiques et haché avant la mesure.
- 200 témoins : permutation des valeurs de « base » entre signes et de « vowels » entre chiffres, graine 20261110 ;
  codes et tokens gardés.
- SEUILS (décisifs, fixés maintenant) :
  * VALIDÉE : accord ≥ 0,85 ET accord ≥ meilleur témoin + 0,30 ;
  * PARTIEL : accord < 0,85 ET accord ≥ meilleur témoin + 0,30 (marge ≥ 0,30) : la clé lit, mais pas au seuil ;
  * NON VALIDÉE : accord < meilleur témoin + 0,30.
  Une seule mesure ; H3 grillée dans tous les cas ; aucun rattrapage.

## Après
- VALIDÉE ou PARTIEL : recherche, dans les images déjà sur disque, des pièces Pandolfini chiffrées SANS déchiffrement
  d'époque (vérification EXISTING par mots en clair et dates), puis lecture au compte de Daniel (sûrs / probables {x} /
  restitués [x] / irrésolus ‹…›, % de mots lus par le sens ; restitution jamais contre des lettres sûres) ; avec PARTIEL,
  toute lecture est présentée comme lecture partielle avec clé partiellement validée.
- NON VALIDÉE : la lecture au sens porte seulement sur 340 contre 341 (documentation de la clé), rien de neuf n'est présenté comme lu.
- PR-PREP.md : statut exact, apport (clé / texte non déchiffré à l'époque), crédits, aucune image ASF ni dérivé. Pas de PR.
