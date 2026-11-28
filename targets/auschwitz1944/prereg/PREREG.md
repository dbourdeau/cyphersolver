# PREREG — message clandestin d'Auschwitz du 4/9/1944 (mots chiffrés en nombres)

Rédigé le 27/11/2026, AVANT tout test. Haché (SHA-256 dans PREREG.sha256) avant l'exécution de `essais/mesure.py`.

## Données d'entrée (gelées)
- Transcription arbitrée : `TRANSCRIPTION-GELEE.txt`, SHA-256 a83492f67ff3c2cec70e74f8020e903007062ca070ed1948263236b20d7bb5e6.
- Pour chaque nombre, on prend la **valeur retenue** (le premier terme de a?b). Le signe « ? » de G28 pos. 1 est un joker : il est accepté par n'importe quelle lettre dans le lexique.
- Lexique : `essais/lexique_pl.txt` (4 352 formes polonaises tirées du texte de la thèse Paszek, pp. publiques), SHA-256 9ea97c09db4447d04382870b4d34e14129c2047c93de2b4002a5f98ec7495522. Il est fixé avant le test. Le modèle de bigrammes vient du même texte.

## Transparence
Avant ce hachage, j'ai fait UN seul essai mental : G37 (8-17-11-4-6) avec la clé F1-a (lecture par position). Il donne « oaesę », un échec. Aucun autre essai n'a été fait.

D'après la citation de Kłodziński (Paszek p. 127, d'après Paczyńska pp. 33-34), on a k=1, t=2, o=3, s=4, i=5, ę=6, w=7, o=3, p=9, i=10, e=11, k=1, ę=6, p=9. La numérotation suit donc la **position** de la lettre. Une lettre répétée peut reprendre le numéro de sa première occurrence (homophones). Au déchiffrement, le nombre n renvoie à la n-ième lettre du texte. La reprise du premier numéro ne change rien à cette lecture. Les digrammes (sz, cz, rz) ne forment pas de signe à part : on compte chacune de leurs lettres.

## Familles de clés (liste close, 6 clés)
- **F1-a** : position, version **1579** (Kochanowski) « Kto się w opiekę poda Panu swemu, A całym sercem szczerze ufa jemu… ».
- **F1-b** : position, version **chantée** « Kto się w opiekę odda Panu swemu, A całym sercem zaufa jemu… ».
- **F1-c** : position, texte **tel que Kłodziński le cite** : « Kto się w opiekę podda Pany swemu… », puis la suite de la version 1579.
- **F2** : doublons sautés. Chaque lettre distincte reçoit un numéro à sa première occurrence dans le texte 1579 (k1 t2 o3 s4 i5 ę6 w7 p8 e9…). Cette clé contredit p=9, mais elle reste dans la liste.
- **F3** : position, clé de Cyrankiewicz « **Komu w opiekę** poda Panu swemu, a całym sercem… » (texte 1579 à partir de « opiekę »).
- **V1** (variante) : F1-a numérotée à partir de 0, c'est-à-dire avec un décalage de −1.

## Métrique
- **Principale** : nombre de groupes de **longueur ≥ 2** dont le déchiffrement est une forme du lexique (joker « ? » admis).
- **Secondaire** : log-vraisemblance moyenne des bigrammes par lettre, sur tous les groupes.
- **Témoins** : pour chaque clé, 200 permutations aléatoires (graine 19440904) de la table nombre→lettre de cette clé. On garde ainsi le même multiensemble de lettres.

## Portions
- **Mise au point** : G1–G19.
- **Validation, tenue à part** : G20–G39.
- La meilleure clé est choisie sur la mise au point, d'après la métrique principale, puis la secondaire en cas d'égalité. La **mesure unique** est ensuite faite sur la validation, avec cette clé seule.

## Seuil de succès (sur la validation)
Il faut les deux conditions suivantes :
- le score principal est strictement supérieur à celui des 200 témoins (p < 0,005) ;
- au moins 30 % des groupes de longueur ≥ 2 sont des mots du lexique.

En cas d'échec, le résultat est déclaré négatif et on ne fait **aucun** ajustement ex post de la clé sur ces données. Toute nouvelle clé exigerait un nouveau PREREG.

## En cas de succès
Lecture par le sens selon la règle de Daniel : 95 % des mots lus sur au moins 300 caractères. Les mots sont comptés à part selon leur statut : sûrs, {probables}, [restitués], ‹irrésolus›. Une valeur tirée du seul sens reste {probable}.
