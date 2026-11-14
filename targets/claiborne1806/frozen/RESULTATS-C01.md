# C01 — Code de W. C. C. Claiborne (1805-1806) : résultats (2026-10-27 09:29 CET)

## 1. Antériorité
- **Textes : déjà entièrement lus (existing decipherment).** Chaque dépêche porte le déchiffrement interlinéaire de Jacob Wagner (Département d'État) ; PJM-SS 10, 11, 13 impriment ce décodage (italiques), et Rowland, *Official Letter Books* (1917), 3:211-213, imprime la copie de registre en clair (24 oct. 1805). Rien d'inédit côté contenu.
- **Clé : « key not found »** (PJM-SS, 5 dépêches : 24 oct. 1805 ; 13 janv., 18, 19, 25 nov. 1806). Weber 1979 (prêt restreint, non consulté) n'est pas en cause : les éditeurs l'utilisent pour d'autres lettres et ne l'y ont pas trouvée ; *Masked Dispatches* (NSA) ne cite pas Claiborne. Aucune reconstruction publiée trouvée.
- **Histoire du code (nouveau, sources imprimées)** : Claiborne demande un chiffre le 26 mars 1805 (Founders, abstract ; reçu le 22 mai) ; Wagner le lui envoie le **8 juillet 1805**, reçu le **12 août 1805** (Rowland 3:165). Le code « Weber pp. 419-30 » employé par Graham le 2 janv. 1806 est en fait celui **remis au gouverneur Sargent** (Mississippi), que Claiborne avait rangé dans son bureau (Claiborne à Madison, 9 janv. 1806, PJM-SS 11:169) — distinct du code de Claiborne.

## 2. Corpus et méthode
- Images NARA T260 publiques : roll 7 img 0224-0226 (24 oct. 1805, ≈ 270 groupes), roll 8 img 0045 (13 janv. 1806, ≈ 75), 0409 (25 nov. 1806, ≈ 45). Les deux lettres des 18-19 nov. 1806 sont à la LoC (Burr Conspiracy Collection), non accessibles : non utilisées.
- Roll 9 (1807-1808, 437 images) parcouru en planches-contact : **aucune autre page chiffrée** repérée.
- Alignement mot à mot : data/words.tsv (328 mots) ; clé : data/values.tsv (≈ 260 numéros, S/P/D).

## 3. Résultat : structure et clé partielle
- **Code d'environ 1 600 numéros, de type « un et demi »** : vocabulaire (lettres, syllabes, mots, quelques noms) rangé en ordre alphabétique **par segments de longueur variable**, segments permutés. Comme dans les codes de 1 700 éléments du Département (Weber, *Masked Dispatches* p. 66-67). **I/J et U/V fusionnés** (101 i, 146 ju ; 1151 u, 1154 val, 1155 va, 1171 vin, 1179 un).
- Test (PROTOCOL.md) : dans les pages de 50, **96 %** des paires de valeurs sûres/probables sont dans l'ordre alphabétique ; témoins mélangés : médiane 50 %, max 57 % sur 1 000 tirages.
- Validation sur lettre tenue à l'écart (25 nov. 1806, 0409, non utilisée pour établir les segments) : 23 groupes nouveaux testables, **22 tombent à leur place alphabétique** ; 1 échec (1509 character, frontière de segment), 5 non testables.
- Carte des segments (début de segment souvent en x01 = lettre seule : 1 a, 51 o, 101 i, 201 b, 301 g, 401 p, 701 d, 901 m, 1001 e, 1101 n) :
  - 1-50 A (a…ance) ; 966-1000 A (and…at)
  - 51-100 O (o…one) ; 601-650 O/R (or, order, ot, our, ous ; 649 ry)
  - 101-150 I/J/K (i…ju, k)
  - 151-160 L (l…late) ; 161-200 R (ri…ru) ; 801-850 Q/R (804 quarter ; 839 re, 841 rel, 846 rep)
  - 201-250 B (b…boa) ; 851-900 B/D (892 by, 899 dou)
  - 251-300 T (t…this) ; 1051-1100 T (thousand…tro, 1060 ti, 1065 tion)
  - 301-340 G (g…gu) ; 341-400 H (h…have) ; 1465-1500 H (he…hos) ; 1543 hundred
  - 401-435 P (p…pit) ; 450-460 P (port, post) ; 1301-1350 P (particular…put)
  - 461-500 W (way…would, 489 wise)
  - 501-566 C (ca…cy) ; 1401-1425 C (compli…contra) ; 1501-1540 C (character)
  - 567-600 S (s, sa, se, sho, si) ; 1280-1300 S (str…sus) ; 1351-1365 S (son…state)
  - 651-660 chiffres (651 = 0, 653 = 2, 654 = 3, 657 = 6, 659 = 8)
  - 670-700 F (flour…from) ; 751-800 F/L (775 fu ; 780 li, 797 ly) ; 1201-1250 F (fe…first)
  - 701-750 D (d…det)
  - 901-950 M (m…mil) ; 1426-1462 M (man…much) ; 1582 Mississippi, 1591 merchant
  - 951-965 Y (y, yet, you)
  - 1001-1035 E (e…eld) ; 1370-1400 E (es…express)
  - 1101-1150 N (n…nish) ; 1251-1275 N (no…number)
  - 1151-1200 U/V
- Signes annexes : crochet final (noté L) = **-s** (troop-s, work-s, mean-s, its = 140L) ; triangle (Δ) = **-ed** (order-ed, post-ed, contract-ed, repair-ed) ; 567 = -s en groupe séparé.

## 4. Petites corrections au texte imprimé (nouveau)
- 24 oct. 1805 : avant « measures », le chiffré porte **489** que Wagner ne glose pas ; la copie de registre a « **wise** measures » (note 4 de PJM) ; 489 tombe exactement entre 467 wel et 490 with → lire « would be [wise] measures ». Sûreté : bonne.
- 24 oct. 1805 : « of 235 arrival » : 235 = *bil* (Mo-bil-le ×3) → faute du commis pour 285 *the* ; « information » = 126 in · 611 *order* (!) · 925 mation → faute d'encodage (611 = order, sûr).
- 24 oct. 1805 : le commis a encodé « John » 101·51 sans 342·1101 (Wagner les ajoute en marge).
- Zones non résolues : 135 (pa-ir / lea-?), 143 (del-iv-ery / jud-?), 149 (Wilkinson), 362 et groupes barrés avant « of » (« the collecting »), 364 (defen-ce), 484 (Ge-ner-al / « a wish » 484·592), 1037/1087 (lea).

## 5. Sûreté
- Structure (segments alphabétiques permutés) : **forte** (test + validation tenue à l'écart).
- Valeurs : 89 sûres (S), 145 probables (P), 27 douteuses (D) — voir data/values.tsv. Clé **partielle** : 261 numéros sur ≈ 1 600.
- Texte : sans objet (déjà lu en 1805-1806).

## 6. Intérêt et suites
- Accroche : « Le code que personne n'a retrouvé : comment le Département d'État de Jefferson chiffrait les alertes de La Nouvelle-Orléans (1805-1806) » — de la menace espagnole (Pensacola, Baton Rouge, Fort St. John) au complot de Burr (« the Union of the States is seriously menaced »), avec l'épisode du chiffre de Sargent égaré dans un tiroir.
- Utilité directe : la clé partielle permet de **vérifier/compléter** les décodages de Wagner pour les deux lettres LoC des 18-19 nov. 1806 si leurs images deviennent accessibles (microfilm Burr Conspiracy Collection), et d'identifier tout autre document chiffré dans ce code (même liste remise à d'autres agents en 1805 ?).
- Planche de relecture aveugle : non (rien de douteux côté texte ; les incertitudes portent sur l'attribution syllabique, pas sur la lecture des chiffres).
