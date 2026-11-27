# Règle de sélection — planche « Capilupi 1546 (95 %) » (56-capilupi / capilupi1546-2511), 25/11/2026, écrite AVANT toute vignette

Pièce : Estense, Autografoteca Campori, Capilupi Ippolito, cc. 80a-80h (images Lodovico, `sources/1555/cropsC/<f>_native.png` sur
SPOF_2) : étude seulement, jamais publiées ; planche PRIVÉE. Cible capilupi1546 (la nôtre : #497/#521 mergées ; #970 ouverte = nos
crédits) ; aucune PR tierce ouverte (gh, 25/11). Base : copie v4 (`planche_prive/v4/`, après planches C, R, C3), clé figée
KEY-1555.json, reading.md de la cible. Recherche mécanique : `scripts/cand_2511.py` (= cand_c3.py sur v4, folios 02r/06r/06v/07r),
`ctx_2511.py` (contexte chiffres/décodage), relevé des jetons marqués ?, [x/y], ~, # (v4). Repérage des signes fait à l'image
(zooms privés, scratchpad) AVANT cette règle ; aucune vignette découpée avant le hachage.

Compte #728 (sûrs seuls) : 02r 120/128 = 93,8 % (seuil 95 % : 122/128, ou 121/127) ; 06r-07r 272/288 = 94,4 % (seuil 274).

## 1. Cibles retenues (3) — doute de FORME réel sur l'image
- T1 **quasi** 02r_10 pos13 (14e chiffre), transcrit [6/0] (indécis, sous la tache brune) ; correctif unique 0 → « quasi » entier
  par la clé (cand_2511). Boîte 02r (1180, 1684, 1208, 1720). Formes 0 / 6 / 4.
- T2 **‹a›** 02r_08 pos0 (1er signe), transcrit « 6~? » (arbitrage : « 6 avec hampe, barré ; ni 4 ni 5 ») ; il décode le mot irrésolu
  ‹a› (« con tuto il core ‹a› non voglia »). Boîte 02r (600, 1365, 700, 1465). Formes 6 / 4 + option texte propre
  « signe biffé (barré par le scripteur) ».
- T3 **Io** 06r_09 pos22 (23e chiffre), « 1 » : trait oblique attaché au 0 suivant ; correctifs uniques = suppression de ce 1
  (ou 8 → 3 au pos21, écarté ci-dessous). Boîte 06r (1903, 1588, 1945, 1652). Formes 1 / 9 / 7 ; réponse utile = « pas un signe ».

## 2. Écartées (chiffre net = faute du chiffreur ou question de valeur, pas de forme)
- che 02r_03 : les correctifs demandent pos5 8 → 3 ou pos6 9 → 3 ; à l'image le 8 (797-845 × 652-735) est un 8 net à deux boucles
  et le 9 une longue descente nette → faute du chiffreur.
- Io pos21 « 8 » 06r_09 (1855-1890) : 8 net.
- suplica 02r_07 : il manque u = 51 ; le scripteur a biffé un signe et écrit « 5 1 » au-dessus (interligne, 5 et 1 NETS). Ce n'est
  pas une forme : c'est une règle de lecture (prendre la correction interlinéaire), à décider à part ; +1 si on l'admet.
- non 02r_02 (313 = nz), la 02r_09 (r au lieu de l : il manque un 1), più 06r_10 (2 = o au lieu de 51 = u), del 06v_07 (6 = a, il
  manque le 9 de 69 = d), e 06v_03 et Ragionavan 06v_15 (aucun changement d'un signe ne répare), causa 06r_13 et usato 06r_23
  (découpage glouton 515 = st, pas un signe douteux), ‹ao› 02r_02 (6 sous la tache + 2 net : le « o » resterait) : aucun correctif
  d'un signe, ou chiffres nets.
- Déjà posés (C, R, C3) : rien n'est reposé.

## 3. Contrôles (3), chiffres nets de mots SÛRS de 02r, jamais exemples, jamais posés
- K1 6 de « imparata » 02r_10 pos18, boîte (1400, 1648, 1444, 1702), formes 0 / 6 / 4, attendu 6.
- K2 0 de « io » 02r_10 pos0, boîte (640, 1715, 682, 1757), formes 0 / 6 / 4, attendu 0.
- K3 1 de « ho » 02r_10 pos2, boîte (741, 1705, 757, 1744), formes 1 / 9 / 7, attendu 1.

## 4. Formes (alphabet de la planche C3, même main 02r/06r/06v) et exemples
Exemples = chiffres de mots SÛRS, vérifiés à l'œil sur crops/_contact.jpg : jeu B de C3 pour 0, 1, 4, 7, 9 (06r/06v) ;
6 = 02r_03 pos2 « opera » (676, 650, 712, 712) et 06r_09 pos20 « Eccelenza » (1783, 1588, 1822, 1637). Étiquettes neutres « forme n »,
aucune glose, valeur, lieu ni mot sur la page. Options texte habituelles (aucune / impossible à distinguer / illisible / pas un signe)
+ remarque. Noyau planche_core v2 (copie alger-1767/planche-2511), graines 20261125 / 1546. Export reponses-capilupi1546-2511.json.
Cadres ajustés seulement si la planche-contact montre un cadre mal placé (consigné dans AVENANT-CADRES.md haché).

## 5. Intégration (mécanique, sur une COPIE v5 ; v4 et tout le reste intacts)
1. Un contrôle raté (toute réponse autre que la forme attendue) → rien n'est intégré ; noté au HANDOFF.
2. T1 = forme 0 → pos13 = 0 ; « quasi » devient SÛR si l'écart disparaît au recompte. 6 / 4 / autre → inchangé.
3. T2 = « signe biffé » ou « pas un signe » → le signe est retiré ; le mot irrésolu ‹a› sort du compte (02r : 128 → 127 mots).
   Forme 6 ou 4 → inchangé (‹a› reste irrésolu). « Autre forme » + remarque → nouvelle étiquette sans valeur (consigne 24/11).
4. T3 = « pas un signe » → le 1 est retiré ; « Io » devient SÛR si l'écart disparaît. Forme 1 → transcription confirmée.
5. « impossible à distinguer », « illisible », pas de réponse → inchangé.
6. Recompte #728 (sûrs seuls ; S + {x}) par lettre ; entrée HANDOFF datée.

## Gain maximal et condition de bascule
- 02r : T1 + T2 → 121/127 = 95,3 % → **bascule en lu possible (les DEUX sont nécessaires)** ; T1 seul 121/128 = 94,5 % ;
  T2 seul 120/127 = 94,5 %. (Avec en plus la correction interlinéaire de suplica, hors planche : 122/127 = 96,1 %.)
- 06r-07r : T3 → 273/288 = 94,8 % : **pas de bascule possible** (une seule cible de forme subsiste).
- Total Y : 650/692 → au plus 652/691 = 94,4 %.
