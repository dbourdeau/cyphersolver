# Règle de sélection — planche « Ercole Gonzaga 1544 » (58-ercole / ercole1544-2511), 25/11/2026, écrite AVANT toute construction

Cible de LcCompany/WAINUT chez Daniel (targets/ercole1544, PR #221 mergée ; notre #491 mergée ; aucune PR ouverte au 25/11).
Résultat éventuel = proposition à Daniel en créditant LcCompany/WAINUT (transcription, table) ; rien posté sans accord de Brice.
Pièces : Biblioteca Estense, Autografoteca Campori, Lettera G, Gonzaga Ercole, sfasc. III, cc. 77-79 (78r = A, 78v = B, 79r = C)
et cc. 174-175 (174v = E, 175r = F, 175v = G). Images IIIF 1900 px (SPOF_2 campori-estense/, liens symboliques src/),
CC BY-NC-SA, usage d'étude : planche privée, jamais publiée.
Base : transcription_0078_0079.txt (SHA e17e527e…0f43) et transcription_0174_0175.txt (SHA 75abc086…4781), clone
_shared/cyphersolver b13dd55072 ; liste « Not settled on the image » de NOTES.md.

## Cibles (10) — coordonnées pixels des images 1900 px (x0, y0, x1, y1)
- T1 A05 « f n s ? e x », signe « comme un 3 » (78r 003 : 813,414,836,447). Formes g / z / chiffre 3.
- T2 B01 « n x ? g x » (aiuti), b/h (78v 004 : 830,236,856,272). Formes b / h.
- T3 B02 « g e b f ? 31 », signe sous la tache (78v : 736,294,764,320). Formes r / n.
- T4 B21 fin « h ? ? b », 2ᵉ signe, trait fin (78v : 1222,1293,1243,1318). Formes x / a / n.
- T5 B21 fin « h ? ? b », 3ᵉ signe (78v : 1247,1292,1271,1318). Formes a / n.
- T6 C07 « q x 5 ? », 2ᵉ chiffre du code 59/57 (79r 005 : 630,586,656,631). Formes chiffre 9 / chiffre 7 / z.
- T7 E21 « a g r e ? r a r », signe à queue (174v 002 : 1152,1350,1175,1391). Formes g / z.
- T8 F03 « t e n g x S x ? r » (gratissime), queue droite (175r 003 : 846,350,868,389). Formes z / q / g.
- T9 F08 « 2? » après « s n e x e r » (175r : 501,624,526,662). Formes chiffre 4 / q.
- T10 G06 « y 27 n ? n f » (masca/tasca) (175v 004 : 523,508,547,546). Formes g / z.
Écartées : A03 (tache noire sur plusieurs signes, pas un signe unique) ; B03 (b/o : lieu non désigné par NOTES, deux candidats) ;
F08 autres « 5 unsettled » (non localisés) ; G06 S/y g (ligature : question à deux signes).

## Formes — exemples réels de cette main, lieux transcrits sûrs (vérifiés à l'œil sur la planche-contact)
- g : 174v E21 1er g de « x a g r e » (1101,1347,1123,1393) ; 78v B03 « f g n g b » 1er g (903,343,921,378).
- z : 78v B03 « q x z x b » (mio) (1012,334,1036,371).
- 3 : 78v B01 « 30 » initial (214,253,244,292).
- b : 78v B03 « g b q » (950,326,970,370).
- h : 78v B21 « x a h x » (448,1284,471,1323).
- r : 78v B21 « a r t » (514,1300,532,1322).
- n : 78v B21 « t x n » (568,1298,591,1322) ; 78v B02 « q n 14 » (256,305,276,326).
- x : 78v B01 « e x p » (276,255,306,290).
- a : 78v B21 « x a h » (405,1298,434,1323) ; « x a r » (494,1298,517,1323).
- 9 : 78v B03 « 39 » (855,344,880,390).
- 7 : 174v E21 « 17 » (871,1354,894,1380) ; 175v G06 « 27 » (479,511,503,538).
- q : 78v B02 « q n 14 » (236,300,257,338) ; 79r C07 « L q x » (563,583,586,632).
- 4 : 78v B02 « 14 » (276,298,302,338).

## Contrôles (3), réponse connue (forme nette, lecture sûre), jamais montrés comme tels
- K1 78v B21 « 30 » chiffre 3 (597,1298,623,1341), options 3 / z / g, attendu 3.
- K2 78v B21 « q b h » b (1170,1288,1192,1318), options b / h, attendu b.
- K3 78v B21 « h x a r » x (467,1300,493,1323), options x / a / n, attendu x.

Options texte habituelles (aucune / impossible à distinguer / illisible / pas un signe) + remarque. Titre « Planche Ercole Gonzaga 1544 ».
Graines 20261125 / 1544. Export : reponses-ercole1544-2511.json. ≤ 1,6 Mo, autonome (data:), vignettes ≥ 130 px.

## Intégration
1. Un contrôle raté → rien intégré (les 10 restent « non tranchés »).
2. Réponse = une forme → étiquette correspondante portée sur une COPIE des deux transcriptions (originaux du clone intacts),
   décodage par key.tsv (règle de scripts/decode.py). Mot devenu italien cohérent → compté lu {forme confirmée} ; sinon reste [?].
   Une forme qui ne fait que confirmer la transcription actuelle lève la réserve « not settled » sans changer le mot.
3. « impossible / illisible / aucune » → reste non tranché (valeur actuelle gardée, marquée).
4. Cas « forme propre » : si une remarque de Brice décrit une forme à part (ex. g ouvert distinct de z, trait fin ≠ x/a),
   créer l'étiquette dans l'alphabet de la copie, relever ses autres lieux, valeur tirée du sens = {probable} seulement (consigne 24/11).
5. Crédit LcCompany/WAINUT dans toute proposition ; rien envoyé à Daniel sans accord de Brice.

## Avenant 1 (25/11 ~08:00, après la planche-contact, AVANT livraison ; cibles, formes et contrôles inchangés, seules des boîtes recadrées)
Version initiale hachée 762d8bf4164d1b4757a35f6d7384d1954730e21babd2bc0c8a9413799d776959. Lecture des coordonnées décalée sur les zooms :
- T5 → (1244,1292,1267,1318) ; T9 → (524,622,545,665) (la 1re boîte tombait sur le « 2 »).
- Exemples : g 2ᵉ → 79r C07 « x a g r a » (701,588,724,630) (l'ancien B03 n'était pas un g net) ; n 2ᵉ (B02) retiré (tombait sur « n 1 ») ;
  q 1er → (221,300,242,338) ; x → (266,253,296,290) ; a 2ᵉ → (488,1298,511,1323) ; 3 → (212,253,239,292).
