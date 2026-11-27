# Règle de sélection — planche aveugle « Poussard, lettre B » boissiran-lettreB-2711, 27/11/2026

Écrite et hachée (REGLE-SELECTION.sha256, avec scripts/items.py) AVANT toute vignette de la planche. Une planche-contact
de repérage (cadres seulement, hors page) a servi à placer les boîtes ; trois boîtes y ont été recalées (E9a, T5, E0b).
Noyau : PLANCHES/_outils/planche_core.py v2, copié tel quel dans scripts/ ; post-traitement dans make_planche.py :
vignettes JPEG ≤ 560 px, CSS `.opt .v img{max-width:40vw}`, refus si page > 1,8 Mo. Graines 2711261 / 1725.

Pièce : lettre B de la liasse AD Charente-Maritime 4 J 1524 (fonds Boissiran), « a Bordeaux le 14 aoust 1725 »,
signée Poussard ; chiffre de chiffres (table 3 de la feuille de clé : 0 a/x · 1 d/p · 2 f/r · 3 b/h · 4 m/y · 5 e/l ·
6 c/g/u · 7 i/n · 8 q/s · 9 o/t), clé gelée (CLE-GELEE.md 9e0590…5d4d) validée par PREREG-2.
Images : photos de Dominique Chaigneau-Billaud (CGAunis), 20261126_161214.jpg (p. 1) et 20261126_161231.jpg (p. 2),
tournées de 90° (img/p1.jpg, img/p2.jpg). 🔴 Images privées : la planche reste locale (LAN), n'est jamais publiée ni
versée dans un dépôt ; cle-PRIVEE.json sous prive/, jamais dans la page. Export `reponses-boissiran-lettreB-2711.json`.

## Pourquoi cette planche
Lettre B (recompte du 27/11) : 254 mots, 224 sûrs, 5 {probables}, 3 [restitués], 22 ‹irrésolus› → lu par le sens
232/254 = 91,3 % (sûrs seuls 88,2 %). Il faut 95 % sur la lettre. Plusieurs trous tiennent à UN chiffre dont la forme
est douteuse (écarts entre les deux passes aveugles, ou confusions connues de cette main : 4/9, 9/4/7, 8/3/5, 1/7).
On demande, pour ce seul chiffre, à quelle forme de la même main il ressemble. Chaque option est un chiffre différent,
de valeur différente, montré par deux exemples sûrs (mots lus) ; aucune valeur ni aucun mot n'est affiché.

## Questions (8 : 5 cibles + 3 contrôles cachés) — un chiffre encadré, libellés « forme 1… », aucune glose
Lieu = ligne de TRANSCRIPTION-ARBITREE-lettreB.txt, rang du groupe (g), rang du chiffre dans le groupe.
- T1 p1.09 g1 `62?725`, 3ᵉ chiffre (passes 4 / 9, arbitré 4). Options 4, 9, 7. **9 → « croire »** (« qui ne scauroit
  croire ») ; 4 = étiquette, rien ne change ; 7 consigné, sans mot.
- T2 p1.12 g7 `5?625`, 2ᵉ chiffre (doute [9/4], « empâté »). Options 9, 4, 7. **7 → « liure »** (« a la liure ») ;
  9 ou 4 : pas de mot, rien ne change.
- T3 p2.06 g3 `?89`, 1ᵉʳ chiffre (doute [8/3], « repassé »). Options 8, 3, 5. **5 → « est »** ; 8 ou 3 : rien.
- T4 p2.01 g3 `86778?`, 6ᵉ chiffre (passes 4 / 5, arbitré 4). Options 4, 5, 9. **5 → « quinse »** ; 4 = étiquette ; 9 consigné.
- T5 p2.01 g4 `?9628`, 1ᵉʳ chiffre (lu 1 ; confusion 1/7 attestée dans les écarts de B). Options 1, 7, 4.
  **7 → « iours »** (« tout les quinse iours ») ; 1 = étiquette (« pours », sans sens) ; 4 consigné.
Toute autre réponse (« aucune / autre forme », « illisible », « pas un signe ») : rien ne change, consigné.
Référence pour l'équilibre des places = l'étiquette de la transcription (T1 4, T2 9, T3 8, T4 4, T5 1).

Exemples (2 par chiffre, chiffres de mots sûrs, hors lignes des cibles et des contrôles quand c'est possible) :
4 : p1.06 « 497 » (mon), p1.05 « 497 » ; 9 : p1.06 « 497 », p1.06 « 1962 » (pour) ; 7 : p1.06 « 497 », p1.05 « 497 » ;
8 : p1.05 « 865 » (que), p1.06 « 1987355 » (posible) ; 3 : p1.06 « 1987355 », p1.17 « 6352 » (cher) ;
5 : p1.06 « 75 » (je), p1.06 « 1987355 » ; 1 : p1.06 « 1962 », p1.17 « 01756 » (adieu) ;
0 : p1.06 « 25204 » (feray), p1.14 « 0607 » (auan) ; 6 : p1.01 « 6352 », p1.17 « 01756 » ;
2 : p1.06 « 25204 », p1.01 « 6352 ». Boîtes exactes : scripts/items.py.

Contrôles cachés (3), réponse connue (chiffre d'un mot sûr), jamais exemples ni cibles, options sans forme jumelle
de la réponse attendue :
- K1 p1.05 g6 « 22525 » (frere), 1ᵉʳ chiffre `2` — options 2, 0, 6.
- K2 p1.10 g1 « 1078 » (dans), 1ᵉʳ chiffre `1` — options 1, 6, 8.
- K3 p1.21 g7 « 397 » (bon), 1ᵉʳ chiffre `3` — options 3, 0, 6.
Un contrôle raté → rien n'est intégré ; on en parle avec Brice (sauf défaut de construction démontré, consigné).
Les points suscrits (fréquents et sans valeur dans cette main, cf. arbitrage) sont dans le cadre quand ils sont juste
au-dessus du chiffre, pour les cibles comme pour les exemples.

## Contrôle d'absence de sosie et des cadres (avant envoi)
Sur crops/_contact.jpg : (1) les options d'une question ont des formes et des valeurs différentes deux à deux ;
(2) les deux exemples d'une option sont la même forme ; (3) le chiffre de chaque contrôle n'a de sosie que dans son
option attendue ; (4) chaque cadre contient le chiffre entier, point suscrit compris, sans voisin. Échec → exemple
remplacé par un autre chiffre sûr de même valeur, consigné en avenant ; une cible mal cadrable est retirée, consignée.

## Gain maximal (calculé avant la planche)
Planche seule, les 5 cibles du côté du mot : 232 → 237 / 254 = 93,3 %.
La lettre n'atteint 95 % qu'avec, EN PLUS, cinq lectures par le sens proposées le 27/11 sans changer un chiffre
(à valider par le lecteur, hors planche) : `0679621364` = auiourdhuy (p1.19), `6297978` = croiois (p1.14),
`0170 8958` = a dix sols (p1.13 : 2 trous → 3 mots lus), `0994` = a toy (p2.03 : 1 trou → 2 mots lus), `9967962` =
touiour (p2.06) → 240 / 256 = 93,75 % sans la planche ; avec la planche : 5 cibles 245 / 256 = 95,7 %, 4 cibles
244 / 256 = 95,3 %, 3 cibles 243 / 256 = 94,9 %. Il faut donc au moins 4 des 5 cibles du côté du mot.
Recompte après réponses : même méthode que le recompte du 27/11 (PR #1006), pas promis.

## Copies
planche.html (SPOF_2) → _planches-serve/boissiran-lettreB-2711/planche.html et _planches-tel/93-boissiran-lettreB.html
(LAN seulement).
