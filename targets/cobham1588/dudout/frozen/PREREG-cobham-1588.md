# PREREG — Cobham 1588 (BL Harley MS 287) : clé apprise sur DECODE R8489, contrôle sur une partie tenue à l'écart, puis lecture de DECODE R8490

Rédigé et haché le 2026-11-09, AVANT toute mesure. Agent Opus, fil Déchiffrement.

## Antériorité (vérifiée avant ce PREREG, gh api)
- Daniel : `targets/cobham1588/` (catalogue n° 131, « attempted, open » ; audit du 22-23/10 : « decoded, not read », seul le passage des otages de R8490 construit une phrase). Sa clé `signs.tsv` est reconstruite sur les gloses de R8488, R8489, R8493 ; ses lectures `texts/R8490_reading.md`. Il glose les codes 7, 10, 15, 16 ; **22 et 27 restent non identifiés** chez lui.
- R8489 lui-même est « Decrypted » sur DECODE (glose d'époque) : rien de neuf à revendiquer sur R8489.
- CSP Foreign 21 pt 4 ne calendre pas ces lettres Harley (vérifié par Daniel ; non revérifié ici).
- Conséquence : tout résultat est une **contribution au dossier de Daniel** (validation indépendante de la clé, identification de codes, corrections de lecture), pas une lecture nouvelle à notre nom.

## Déclaration d'honnêteté
- Les vignettes à 0,12× des deux pages de R8489 (ff. 78r et 78v) ont été vues avant ce PREREG : quelques mots de glose de f. 78v ont été aperçus. La clé, elle, est apprise **uniquement** sur f. 78r (fichier ci-dessous). Le chiffre de f. 78v (partie H) sera transcrit sur des découpes serrées des lignes chiffrées et haché AVANT de lire ses gloses à pleine résolution. Le risque résiduel est un biais de transcription de H ; il est déclaré.
- La clé de Daniel (`signs.tsv`) a été lue avant l'apprentissage ; elle a servi de nomenclature des signes, pas de valeurs : toutes les valeurs de `cle_R8489_f78r.tsv` sortent des alignements de f. 78r.

## Fichiers gelés
- Entraînement : `R8489_f78r_entrainement.tsv` SHA256 3f7b9aff1eee9699d74e4e077ceca51c3838a2968aeedef2607d81631f4bf59e
- Clé : `cle_R8489_f78r.tsv` SHA256 2b3216e65e9d6ebaa0b6d0ca082ba46f08e427ff361a776633fb16f5b7130566
- Partie H : `R8489_f78v_H_chiffre.tsv` (chiffre seul), haché dans l'addendum A1 avant lecture des gloses ; gloses ensuite dans `R8489_f78v_H_gloses.tsv`.

## Mesure (UNE seule)
- Sur H : chaque signe-lettre de chaque mot glosé dont le nombre de signes = nombre de lettres de la glose ; codes numériques et ◻ exclus ; mots dont la longueur ne colle pas exclus (liste dans le résultat).
- Déchiffrement par la valeur PRINCIPALE de la clé (une lettre par signe). Signe absent de la clé = échec. Équivalences : u=v, i=j.
- Accord caractères = lettres correctes / lettres comparées.
- Témoins : 200 clés obtenues en permutant la colonne « valeur » entre les 22 signes (graine 20261109), même calcul.
- **Critère : clé VALIDÉE si accord ≥ 0,85 ET accord ≥ meilleur témoin + 0,30.** Accord en mots (mot entier exact) rapporté, non décisif. Accord « ensemble » (lettre ∈ ensemble des valeurs) rapporté, non décisif.
- Pas de révision de la clé ni de la transcription après la mesure ; H est grillée ensuite.

## Après la mesure
Si validée ou partielle : lecture au sens de R8490 (ff. 80r-v) avec la clé gelée + codes, au compte de Daniel (fiche sûrs / probables {x} / restitués [x] / irrésolus ‹…›), puis PR-PREP.md (anglais), mention « DECODE R8489 / R8490 », sans image.
