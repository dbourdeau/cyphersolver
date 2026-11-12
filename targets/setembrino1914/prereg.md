# PREREG — setembrino-1914 (catalogue n° 1470) — gelé AVANT tout essai de clé

Date : 2026-11-12. Transcription d'entrée : TRANSCRIPTION-AVEUGLE.txt, SHA-256 d2a2e4d6e7fb6695f873157c981804142bdd0d443fd1a148f5052723fdb885c1 (gelée, non modifiée ; les variantes de lecture se choisissent par les copies « Ct » et les options [A|B] déjà notées, jamais en inventant une lettre).
Connu avant ce PREREG (antériorité, non testé par nous) : vetting de Daniel Bourdeau (catalogue.json #1470, research/latam_vetting/1470_sample.txt) : Vigenère, clé de 8 reprise à chaque mot, MFTDBSJV (mars-avril), LETCARIV approx. (10 mars), clé ~10 lettres non établie (20 mai), LBQPOHVJ (7 oct., n° 1471, hors cible).

## Hypothèses
H1 (système) : chiffre de télégraphe du Ministère de la Guerre / État-major : Vigenère alphabet standard A-Z, clair = chiffré − clé (mod 26), clé périodique reprise au début de CHAQUE groupe (un groupe = un mot clair, parfois deux mots soudés). Variante H1b : Beaufort (clair = clé − chiffré). Variante H1c : clé continue (non reprise) — testée comme contrôle de structure.
H2 (clés) : une clé par période/expéditeur. Unités :
 - U-A : télégrammes 14 mars → 17 avril (p1319/1320, 1321-1322 « 52414 », 1324/1325, 1326, 1327, 1328, 1329), clé candidate MFTDBSJV (Daniel), à confirmer UNIQUEMENT sur p1319 + son déchiffrement au crayon d'époque (crib).
 - U-B : 10 mars, Pamplona (p1317), clé à établir (période 4-14), point de départ LETCARIV.
 - U-C : 20 mai, Rego Barros (p1330-1332), clé à établir ciphertext-only (période 4-14), le clair intercalé servant de contexte.
Cribs annexes demandés (FSC pce 1914.02.19/2, FSC cont 1914.10.07/2) : consultables seulement en appui, non requis par la mesure.

## Mesure unique (définie ici, appliquée telle quelle)
Lexique L : formes du corpus portugais Gutenberg téléchargé (lm/gutenberg/: Machado de Assis — Dom Casmurro, Braz Cubas, Quincas Borba, Historias sem data, Helena ; Eça — O Mandarim), minuscules, accents retirés, formes de fréquence ≥ 1 et de longueur ≥ 2 (+ « a », « e », « o »). Aucun mot ajouté à la main.
Score S(K, portion) = part des LETTRES chiffrées de la portion dont le groupe déchiffré est (i) dans L, ou (ii) découpable en 2 mots de L de longueur ≥ 2 chacun.
Contrôles (≥ 200, ici 1000 par famille) :
 C1 : 1000 clés aléatoires de même période sur la même portion ;
 C2 : la clé testée appliquée à 1000 versions de la portion où les lettres sont permutées au hasard À L'INTÉRIEUR de chaque groupe (longueurs conservées).
Critère de validation d'une clé : S ≥ 0,85 sur la portion tenue à l'écart ET S > max(C1 ∪ C2).
Portions tenues à l'écart :
 - U-A : clé fixée sur p1319 seul (95 lettres) ; portion tenue à l'écart = 52414 (p1321-1322) + p1329 (≈ 730 lettres ≥ 300). Les autres pièces U-A sont mesurées ensuite (rapportées, pas au critère).
 - U-B : 93 lettres seulement → pas de portion ≥ 300 possible ; clé obtenue par escalade sur la moitié des groupes (indices pairs), mesurée sur l'autre moitié ; résultat qualifié « petite portion ».
 - U-C : clé obtenue par escalade sur les groupes d'indice pair (copie p1331), mesurée sur les groupes d'indice impair (≈ 150 lettres < 300 : signalé) ; S rapporté aussi sur l'ensemble.
## Comptage (règle des 95 % de Daniel)
Chaque lettre chiffrée classée : sûre (mot lu tel quel), probable (une lettre corrigée par erreur de transmission attestée par une copie ou une option notée), restituée (≥ 2 corrections ou mot deviné par le sens), irrésolue. « Lu » si (sûres + probables) ≥ 95 % d'une portion ≥ 300 lettres ; sinon « read in part ». Fiche : LECTURE.md.
## Ce qui invalide
S < 0,85 sur la portion tenue à l'écart, ou S ≤ max contrôles → clé non validée, rien à publier pour cette unité.
