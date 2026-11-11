# PREREG-1730 — Amendement A1 (11/11/2026, agent Opus 5.5), écrit et haché AVANT toute vue de aufn 0004
Décision de l'orchestrateur : option (a).
## Clé
KEY.tsv 1687 GELÉ, inchangé : ../1687/KEY.tsv sha256 4d83b4f794e64e551c82c089cb357af029d969871992e5390b4512a337e0d8df.
Valeurs « sûr » + « probable » seulement ; « douteux » et groupes absents = hors clé. RIEN de 0003 (ni 281, 26, 279, ni autre) n'est
ajouté. C'est le re-test UNIQUE de KEY.tsv (règle du 10/11) ; 0004 est grillée après la mesure.
## Portion
H = aufn 0004, 160 premiers groupes en ordre de lecture (page gauche puis droite), image sha256 bd100edb… (PREREG-1730.md).
Transcription par un sous-agent SANS clé ni glose, fichier 1730/H-0004.txt, haché avant décodage. Groupes illisibles transcrits « ? »
comptent comme hors clé.
## Mesure M5 (une seule exécution) : python3 scripts/m5.py ../1687/KEY.tsv H-0004.txt LEX-M5.txt 160
- Décodage groupe à groupe ; groupe hors clé = une position « ? » jamais couverte (= échec) ; nulle = rien.
- Couverture = lettres couvertes par la segmentation optimale (programmation dynamique) en mots de LEX-M5.txt / positions totales.
- LEX-M5.txt (scripts/mklex.py) : formes de la prose claire de chancellerie de Nr. 1687 (lignes CLEAR, clair P.S.16, glose H 1687),
  + Gutenberg allemand (n ≥ 3) ; mots ≥ 3 lettres + liste fermée de mots courts. Aucune donnée de 1149/1.
- Témoins : 200 clés brassées (permutation des valeurs des codes présents dans H), graine 1730.
- Seuils : VALIDÉ si couverture ≥ 0,60 ET couverture ≥ max des 200 témoins + 0,30 ; PARTIEL si seule la marge ≥ 0,30 ; ÉCHEC sinon.
- Étalonnage (fait AVANT, sur matériel 1687 non tenu à l'écart, donc optimiste ; calib/CALIB.txt) : lectures réelles 0,634-0,794,
  max témoins 0,306-0,394. Le seuil 0,60 est sous la plus faible lecture réelle d'étalonnage.
- Compte à la Daniel rapporté après mesure : sûr / probable / restitué / irrésolu, par groupe.
- Si ÉCHEC : diagnostic post hoc seulement, aucune autre mesure.
