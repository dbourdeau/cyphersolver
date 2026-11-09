# PREREG-P02 — pandolfini-francia-1514-15 (cat. Bourdeau 2389) — 09/11/2026 ≈ 02:25 CET
Écrit et haché AVANT : la clé v2, toute localisation, tout regard et toute transcription de MAP LXXII 340 et 341.
P01 (PROTOCOLE.md 7d790482…, vérifié intact ce jour) reste en vigueur pour tout ce que P02 ne change pas.

## Regards déclarés avant ce prérapport
- P01 : mesure unique faite sur H = 346 c. 441r (1er bloc) contre 345 → 0,788 / témoin 0,338 : NON VALIDÉE ; 345/346
  sont GRILLÉS et passent au matériau d'apprentissage (T2). Je les ai relus ce jour (H_346_c441r.txt, REF_H_345.txt,
  RESULTAT_MESURE_UNIQUE.json, découpes H_L1/L3/L5/L8 du scratchpad).
- AUCUN regard sur 340 ni 341 (ni vignette, ni position) : ils forment la nouvelle portion tenue à l'écart.
  342/343 non regardés (repli seulement).

## Apprentissage T2 (clé v2)
- Point de départ : cle/CLE.json gelé (ee22509c…), inchangé.
- Compléments tirés UNIQUEMENT de pièces déjà vues hors 340/341 : T de P01 (308, 318, 319) et la paire grillée 345/346
  (alignement de H_346_c441r.txt sur REF_H_345.txt, consigné dans cle/T2_alignements_345_346.tsv).
- Corrections annoncées par le diagnostic P01 : f (« y » + voyelle suscrite), g (signe δ fermé, distinct du d oncial),
  .4. = Maestà ; plus les signes-mots et codes que l'alignement 345/346 établit sans ambiguïté.
- Règle de lecture du code ambigu .4., fixée maintenant pour ne pas compter deux fois faux : .4. → « maesta » si le
  décodé qui précède immédiatement se termine par « a » (questa, sua, della…), sinon → « cristianissimo ».
- Clé v2 écrite dans cle/CLE_v2.json et gelée (cle/CLE_v2.sha256) AVANT toute localisation de 340/341.

## Portion tenue à l'écart H2 et référence R2 (règle fixée maintenant, sans avoir vu les pièces)
- Paire 340 (c. 430r selon l'inventaire) / 341. La pièce qui porte le chiffre donne H2, l'autre (copie claire ou
  déchiffrement) donne R2. Si les deux portent du chiffre, H2 = 340 et R2 = un déchiffrement d'époque interlinéaire
  s'il existe ; sinon repli.
- H2 = PREMIER bloc chiffré continu de la pièce chiffrée (du premier signe chiffré jusqu'au premier passage en clair
  d'au moins trois mots) ; si ce bloc a moins de 4 lignes, H2 = ce bloc + le suivant (même règle).
- R2 = le passage correspondant de la copie claire, borné par les mots en clair qui encadrent le bloc dans la pièce
  chiffrée (jamais par un décodage). Si le bloc commence la lettre, borne de début = début du texte de la copie après
  l'adresse ; si le passage est absent de la copie, repli.
- Repli (dans l'ordre, consigné) : 342/343 selon la même règle ; sinon aucune mesure.
- Ordre : localisation → transcription de H2 (jetons, LEGENDE.md + ajouts consignés) → gel TRANSCRIPTION_H2.sha256 →
  transcription de R2 (abréviations développées) → gel REF_H2.sha256 → mesure. Rien n'est décodé dans H2 avant la
  mesure ; R2 n'est jamais regardée en même temps qu'un décodage de H2.

## Mesure unique (sur H2)
- Script mesure/measure_p02.py = measure.py de P01 + règle de .4. ci-dessus ; testé d'abord sur données synthétiques,
  haché avant la mesure. Normalisation, formule d'accord en caractères (1 − Levenshtein/longueur R), accord en mots
  (rapporté, non décisif) : identiques à P01.
- 200 témoins : permutation des valeurs de « base » entre signes et de « vowels » entre chiffres, graine 20261109 ;
  codes et tokens gardés (comme P01).
- CRITÈRE (décisif, inchangé) : accord ≥ 0,85 ET accord ≥ meilleur témoin + 0,30. Sinon NON VALIDÉE, H2 grillée,
  aucun rattrapage.

## Après
- Validée : comparaison EXISTING (copies claires sans titre, par mots en clair et dates) pour chaque lettre nue avant
  lecture ; puis lecture au compte de Daniel (sûrs / probables {x} / restitués [x] / irrésolus ‹…›, % de mots lus par
  le sens, restitution jamais contre des lettres sûres) ; PR-PREP.md (aucune image ASF ni dérivé).
- Non validée : rien n'est présenté comme lu (une lecture « read in part » n'est possible qu'avec une clé validée).
