# PREREG — NLA Hannover, Hann. 9g Nr. 1687 (Regensburg 1730, relations de Diede), écrit le 10/11/2026 (agent Opus 5.5)
Écrit AVANT toute transcription. Vu jusqu'ici : aufn 027 (recadrages pleine résolution, page gauche + haut de la page droite),
028, 029, 033, 061 en vue d'ensemble 1300 px (gloses illisibles à cette échelle). 032, 034, 035, 036 : jamais regardées.

## Système
Groupes de 2-4 chiffres séparés par des points (≈ 15-1500), nomenclateur syllabique allemand (lettres, syllabes, mots, noms),
dans des relations en clair. Glose interlinéaire d'époque PARTIELLE : premières/dernières lignes de chaque passage glosées ;
le milieu de beaucoup de passages est barré d'un trait oblique et non glosé (nulles ? texte non déchiffré ?) ; Relat. 16
(aufn 060-065) sans glose ni soulignement. Pas le système de mecklenburg1734 (chiffres continus, groupes de 5, Vienne).

## Clé K
Tirée des seules paires chiffre/glose des séries glosées de 1687 aufn 004, 025, 026, 027, 028, 029, 030, 031.
Valeur = chaîne (lettre, syllabe, mot) ; une valeur n'entre que si l'alignement glose ↔ groupes est univoque ou confirmé par
≥ 2 occurrences cohérentes. Gel KEY.tsv + sha256 AVANT toute vue rapprochée de 032-036.

## Portion H
aufn 033, 034, 035, 036 (ff. 542-545), dans cet ordre, page gauche puis droite : les 160 premiers groupes pris dans les séries
qui portent une glose au-dessus (séries nues et blocs barrés sautés et notés). Si moins de 160 : compléter avec aufn 032, même
règle. Transcription des chiffres seuls → H-CHIFFRE.txt + sha256 ; puis glose de ces séries → G-GLOSE.txt + sha256 ; puis mesure.
Limite : la glose est visible en transcrivant les chiffres ; elle peut ne pas couvrir chaque groupe → mesure minorée.

## Mesure (une seule) : scripts/measure.py (Smith-Waterman caractères, normalisation ä→a, ß→ss, j→i, y→i, v/w→u),
codes hors K = « ? » ; 200 témoins (valeurs de K permutées parmi les codes présents), graine 1730.
car ≥ 0,85 ET car ≥ max témoins + 0,30 → VALIDÉ ; marge ≥ 0,30 seule → PARTIEL ; sinon ÉCHEC. Portion mesurée = grillée.

## Ensuite : si VALIDÉ ou PARTIEL, décodage des séries sans glose (blocs barrés de 027-036 : texte ou nulles ? ; Relat. 15-16,
aufn 056-057, 060-065) et lecture au sens ; décompte de Daniel (sûrs / probables / restitués / irrésolus).
