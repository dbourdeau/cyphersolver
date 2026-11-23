# PREREG — montcalm-carillon-1758 (écrit et haché AVANT tout calcul, 23/11/2026)

## Objet
ANOM COL F3 15 f. 194 r°–v° (vues FRANOM82_247MIOM013_F3_015_336–337), Montcalm au ministre de la Marine,
« Duplicata », camp de Carillon, 1er septembre 1758 : chiffré en groupes numériques avec déchiffrement d'époque
interlinéaire (= EXISTING ; clair déjà connu par le transcrit LAC C-10528 1188-1189, cité dans
cyphersolver targets/montcalm1758i/NOTES.md). Question : ce chiffré est-il dans le « code I » (table du ministère,
ANOM COL C11E 10 f. 288 = LAC e001295272) ? Test aveugle demandé par montcalm1758i (« a test on a text the table has
never seen »).

## Clé (gelée par un tiers, non modifiée par nous)
cle/table_e001295272.tsv = targets/montcalm1758i/key/table_e001295272.tsv de dbourdeau/cyphersolver,
SHA-256 d13fcfac7c82654c573ef6bc3d023c1adc1f66b23ba00454123396a23bee36cf (identique au FREEZE.txt amont du
13/11/2026). Colonne « reading » ; « ? » = vide ; statuts clear et doubtful utilisés tels quels ; si la cellule
porte plusieurs valeurs séparées par « / », la première. Aucune correction (ni levis_*, ni corrections_post_freeze).

## Portion mesurée
La lettre entière (f. 194 r° et v°), jamais vue par la table. Regards déclarés : j'ai vu la vue 336 réduite
(1400 px) et quelques groupes de la 1re ligne (475 185 315 475 29 …) ; aucune valeur de la table consultée avant
ce PREREG. Transcription (après ce PREREG, avant calcul) : validation/chiffre.txt (groupes, ligne par ligne) et
validation/glose.txt (glose interlinéaire telle qu'écrite) — gelées par SHA-256 (validation/SHA256.txt) avant
l'exécution de validation/mesure.py. Groupes illisibles ou coupés au bord notés « ? » et ignorés.

## Mesure (une seule)
- Décodage : chaque nombre → reading ; mots en clair dans le chiffré conservés.
- Normalisation : minuscules, accents ôtés, lettres a-z seulement.
- Accord caractères = difflib.SequenceMatcher(None, décodé, glose, autojunk=False).ratio() sur la lettre entière.
- Témoins : 200 tables obtenues en permutant au hasard les 700 readings sur les 700 cellules
  (random.Random(20261123)), même mesure.
- Critère fixé d'avance : CODE I CONFIRMÉ si accord ≥ 0,85 ET ≥ meilleur témoin + 0,30.
  Sinon : non confirmé (pas de second essai sur cette lettre avec une autre table sous ce protocole ; un essai
  ultérieur serait exploratoire et déclaré comme tel).
- Si la lettre décodée fait < 300 lettres : « non mesurable ».
- Accord en mots rapporté, non décisif.
