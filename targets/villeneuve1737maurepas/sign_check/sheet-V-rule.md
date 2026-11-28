# Règle de sélection — planche « villeneuve » du 23/11/2026 (villeneuve1737maurepas, n° 538), écrite AVANT toute construction de vignettes

Pièce : Archives nationales, AE/B/I/414, Villeneuve (Constantinople) → Maurepas, T1 = 18/2/1737 (vues 0060-0062),
T2 = 2/4/1737 (vues 0092-0096) ; images AN (SPOF_2 …/RECUS-ARCHIVES/an-AE-B-I-414-villeneuve-2026-11-20/) : étude seulement,
jamais publiées.
Base : transcription fusionnée SPOF_2 …/villeneuve-1737/transcr/merged_cipher.json (2 passes aveugles + arbitre aveugle),
clé K2 gelée (key/KEY-K2-frozen.tsv, statuts S/W, PREREG-2), compte règle #728 (scripts/count728.py,
PR/targets/villeneuve1737maurepas/count728_detail.txt). Rien de cela n'est modifié par la planche.
Départ chiffré : T1 106 sûrs / 255 mots chiffrés (0,416) ; T2 348 / 838 (0,415).

## Critère
On ne pose qu'UN chiffre par mot, et seulement si (1) le mot est aujourd'hui non sûr (#728), (2) soit la forme transcrite
du chiffre donne un groupe S de K2 dont la valeur fait le mot que le sens demande mais la transcription n'est pas réglée
(passes A/B en désaccord, « ? » des deux passes, arbitre « probable » ou « unsure »), soit une autre forme de ce seul
chiffre donne un tel groupe ; (3) le chiffre, regardé à l'image le 23/11, est réellement hésitant (pli de reliure,
petite taille, confusion 3/5/9 de la main, 1/2). Recherche : tous les groupes de T1/T2, chaque chiffre remplacé un à un par
les neuf autres + confirmation des groupes non réglés, recompte #728 ligne par ligne (script inline, 23/11), puis tri à
l'œil sur l'image et au sens. Groupes à 3 chiffres coupés au pli : acceptés, car les codes de K2 ne dépassent pas 499
(un 4e chiffre perdu est exclu) ; groupes à 1-2 chiffres coupés au pli : écartés (un chiffre a pu disparaître).

## Cibles retenues (9)
Notation : vue+page.ligne/rang du groupe dans la ligne (merged_cipher.json).
- V1 T2 0094L.L06/1 « 304 » (passe A 904, passe B 304, arbitre 304 probable), 1er chiffre : 3 / 9 / 5. Juste après le clair
  « il seroit à souhaitter que ». 3 → 304 = le (S) : « que le traitt… » (+1 sûr). 9 → 904, 5 → 504 : absents de K2,
  mot inchangé. Forme : un arc ouvert à longue queue descendante, sans boucle fermée.
- V2 T2 0094L.L06/5 « 239 » au pli, 3e chiffre : 9 / 8 / 6. 9 → 239 = port (S) : « [la] Porte fera avec le Roy des Siciles »
  (+1 sûr, −1 trou). 8 → 238 = me, 6 → 236 = qu : le sens ne les demande pas, mot inchangé. Doute faible (boucle et queue
  visibles, mais coupées par le pli) — posé parce que la transcription n'est pas réglée.
- V3 T2 0094L.L11/10 « 318 » (passe A 328, passe B 318, arbitre 318 probable), 2e chiffre : 1 / 2. 1 → 318 nulle (S)
  confirmée : « dans le port du Grand [Seigneur] », −1 trou (aucun mot sûr en plus). 2 → 328 absent, inchangé.
  Forme : jambage à tête crochue ; la question est la base plate du 2.
- V4 T2 0094L.L13/8 « 2 » (après « 117, », au pli, suivi d'un point), seul chiffre : 2 / 3 / 1. 2 → le (S) :
  « ayant communication d'un mémoire que le … » (+1 sûr, −1 trou). 3 → a, 1 → y (W) : mot inchangé.
- V5 T2 0093L.L12/11 « 495 » au pli, 3e chiffre : 5 / 3 / 9. 5 → de (S) : « du Roy de[s] Siciles » (la ligne suivante
  commence par … si ci) (+1 sûr, −1 trou). 3 → 493 = ne (S) : transcription corrigée, mais le mot reste un trou (le sens
  ne demande pas « ne », valeur non fixée par le contexte). 9 → 499 (W) : inchangé. Forme : S long (ſ) de la main.
- V6 T2 0095L.L06/3 « 32 » (deux passes « ? »), 1er chiffre : 3 / 5 / 9. 3 → 32 = l (S) : « et que l'on fera au pr[ès] »
  (+1 sûr). 5 → 52 = si : « que si on fera » agrammatical → transcription corrigée, mot inchangé (trou). 9 → 92 absent.
  Forme : même arc ouvert à queue que V1.
- V7 T2 0095L.L06/12 « 203 » au pli (petit), 3e chiffre : 3 / 5 / 8. 3 → la (S) : « au pr[ès] de la [cour] » (+2 sûrs :
  de, la). 5 → 205 absent ; 8 → 208 (W) : inchangé.
- V8 T1 0061L.L03/9 « 366 » au pli (petit, deux passes « ? »), 3e chiffre : 6 / 9 / 0. 6 → par (S) : « fait connoistre
  même par … » (+1 sûr, −1 trou). 9 → 396 = les (S) : « même les … » également possible au sens → compté de même
  (+1 sûr) ; transcription corrigée en 396. 0 → 360 absent : inchangé.
- V9 T1 0062L.L04/9 « 270 » au pli (passe B « ? »), 3e chiffre (petit, surélevé) : 0 / 2 / 9. 0 → a (S) : « [avan]tages
  contraires à » (+1 sûr, −1 trou). 2 → 272 = luy : le sens ne le demande pas, inchangé. 9 → 279 absent.

## Contrôles nets (3), chiffres de groupes sûrs (S, deux passes d'accord), attendu connu
- C1 0094L.L07/6 « 495 », 3e chiffre = 5 (options 5 / 3 / 9).
- C2 0094L.L11/8 « 318 », 1er chiffre = 3 (options 3 / 9 / 5).
- C3 0094L.L13/5 « 238 », 3e chiffre = 8 (options 8 / 9 / 6).
Placés à des places différentes par planche_core v2 (build() refuse sinon).

## Écartés après examen (et pourquoi)
- Codes absents de K2 (234 groupes cibles, p. ex. 440 « l'[intention] », 427 « au pr[ès] », 444, 146, 249, 207, 110) :
  doute de CLÉ, pas de forme ; aucune variante d'un chiffre ne donne un groupe S que le sens demande. 259 (0061R.L04,
  0094L.L10) → 239 port : 259 revient deux fois, 5 net (ſ) → code absent, pas un doute de forme.
- Codes W (54 lation, 22 uelila, 451 i, 198 traitt, 46, 390, 484, 31…) et 134 n/W → 154 n/S (0093L.L07) : 134 revient
  6 fois, 3 net → doute de VALEUR.
- Groupes au pli à 1-2 chiffres (0062L.L02 « 27 », 0062L.L03 « 78 », 0093L.L11 « 17? », 0061L.L04 « 22? », 0093L.L06
  « 25? », 0094L.L07 « 37? », 0095L.L15 « 37? », 0094L.L16 « 2? » invisible) : un chiffre a pu se perdre dans la reliure ;
  une réponse de forme ne trancherait pas.
- Sous le timbre AE : 0061R.L09 « 124? 169|149 », 0094R.L08 « 75? », 0095R.L08 « 441? 9? » (arbitre « unsure ») : trait du
  timbre mêlé au chiffre, question non équitable.
- 0094L.L14 « 30 » (A 90) : la forme 3 donnerait « auoit » à la place de « au » + trou : gain nul au compte.
- 0094L.L15 et 0096L.L11 « 414 / 444 » : les deux lectures absentes de K2. 0093R.L06 « 43 / 13 » : « cou » ne fait pas de mot
  sans le r. 0060S.L03 « 321 / 324 » : 321 W, 324 absent. 0094L.L10 « 441? » (444/441) : sens de la ligne obscur.
- 0093L.L16 « 2^2 » et « 148? » : signe suscrit / chiffres tassés au-dessus de la ligne au pli. 0061L.L05 et 0096L.L09
  « 203? » : « p la » est un découpage du compteur dans « pla… », le sens ne demande pas « la ». 0095R.L08 « 441? » et
  0096L.L06 « 2? » : gain mécanique sans sens (« ibere de ordre », « …e il le »).
- Choix mécaniques à mot de 2-3 lettres sans appui du sens (p. ex. 1 → 2 le / 3 a en 0061L.L14 au pli) : écartés.

## Alphabet (consigne de Brice)
Formes proposées : 3 (deux arcs ouverts à gauche, petite queue), 9 (boucle FERMÉE en tête + longue queue), 5 (S long ſ, à
hampe montante et queue descendante), 8 (deux boucles superposées), 6 (boucle basse fermée + hampe montante),
1 (jambage seul, tête crochue), 2 (tête bouclée + base plate horizontale), 0 (petite boucle ovale, sans hampe ni queue).
Chaque option se distingue des autres options de sa question par un trait constant (boucle fermée ou non, base plate,
hampe, nombre de boucles), non par l'encre ou la taille. La hauteur n'est pas renseignée : tous les exemples sont des
chiffres de taille normale posés sur la ligne (seuls les cibles au pli sont petites ; c'est la forme qui est demandée).
Exemples : chiffres de groupes SÛRS (S et deux passes d'accord), de la même main (vues 0094-0095), jamais une cible ni un
contrôle ni un chiffre d'un groupe contrôle ; chaque vignette vérifiée à l'œil sur la planche-contact locale.
Aucune glose, lecture, valeur, lieu ni date sur la page ; étiquettes « forme n ».
Options texte : « aucune / autre forme », « impossible à distinguer », « illisible », « pas un signe (tache, trait) ».
Ordre : planche_core v2 (copie de PLANCHES/_outils + option « impossible à distinguer »), graines 20261123 / 1737.
Export : reponses-2311-villeneuve.json.

## Intégration (après réponses, mécanique, sur une copie ; merged_cipher.json, K2, PR/ et prereg/ ne sont pas modifiés)
1. Contrôles : si UN contrôle est raté (réponse ≠ forme attendue, y compris « impossible à distinguer »), la planche
   n'est PAS intégrée : aucun mot ne change ; on le note dans HANDOFF et on ne refait pas de question sur ces signes ce soir.
2. Cible, réponse = forme qui donne le mot (V1 3, V2 9, V3 1, V4 2, V5 5, V6 3, V7 3, V8 6 ou 9, V9 0) : le groupe est
   réglé (statut « planche-sure », noté « ! ») et le compte #728 est refait ; le mot devient SÛR s'il l'est par la règle
   (V8 : 6 → par, 9 → les, tous deux sûrs).
3. Cible, réponse = autre forme donnant un groupe de K2 que le sens ne demande pas (V2 8/6, V4 3/1, V5 3, V6 5, V9 2) :
   transcription corrigée, mot laissé en trou ; aucune valeur fixée par le contexte n'entre dans la clé.
4. Réponse = forme donnant un code absent, « impossible à distinguer », « aucune / autre forme », « illisible »,
   « pas un signe » : mot inchangé ; remarque reportée.
5. Recompte strict #728 (T1, T2) et entrée HANDOFF datée. Statut : « read in part » quel que soit le résultat.
Gain maximal si tout confirme : T1 106 → 108 sûrs / 255 (0,424) ; T2 348 → 355 sûrs / 841 mots (0,422 ; le découpage de
deux lignes change le nombre de mots) ; soit +9 mots sûrs au total (≈ +0,7 point).
