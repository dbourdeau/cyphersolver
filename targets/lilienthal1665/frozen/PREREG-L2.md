# PREREG-L2 — amendement de la partie L (Lilienthal, lead 2316), écrit le 10/11/2026 (agent Opus 5.5), remplace la partie L de PREREG.md
Écrit AVANT toute vue rapprochée de la page tenue à l'écart. Pages vues de près jusqu'ici : 38 (1 recadrage), 42 (vignette + 1 recadrage
des 5 premières lignes), 47 (vignette + recadrages). 45 et 31 : jamais regardées (ni vignette).

## Système
Nomenclateur 2-3 chiffres (≈ 23-390) : lettres, syllabes et mots ; allemand ; glose d'époque partielle (allemande ou latine).

## Clé K_L
Tirée des seules paires chiffré/glose des pages glosées de R0000814, images 28-49, **sauf 31 et 44-46** (exclues pour éviter une copie
de la portion H). 42 n'est plus tenue à l'écart : elle sert à la clé. Valeurs = chaînes (lettre, syllabe ou mot) ; une valeur
n'entre que si l'alignement mot glosé ↔ groupes est univoque. Gel KEY-LILIENTHAL.tsv + sha256 AVANT de regarder 45 de près.

## Portion H_L
**R0000814 image 45** : les 160 premiers groupes, en ordre de lecture (page gauche puis droite), pris dans les séries qui portent une
glose au-dessus (séries nues sautées et notées). Si 45 en compte moins de 160 : compléter avec image 31, même règle.
Transcription des codes seuls → H_L-CHIFFRE.txt + sha256 ; ensuite glose de ces séries → G_L-GLOSE.txt + sha256 ; ensuite script.
Limite : la glose est visible en transcrivant ; elle peut ne pas couvrir chaque groupe (résumé) → la mesure en est minorée.

## Mesure (une seule) : scripts/measure.py, système L, mêmes règles que PREREG.md (SW, 200 témoins graine 1666,
car ≥ 0,85 ET marge ≥ 0,30 → VALIDÉ ; marge ≥ 0,30 → PARTIEL ; sinon ÉCHEC). Codes hors K_L = « ? ».
## Ensuite : si VALIDÉ ou PARTIEL, décodage des séries sans glose (38 etc.) et lecture au sens, décompte de Daniel.
