# PREREG P02 — clé extérieure Gabbrielli n° 25 (K_G25) sur doc. 78 pos. 329-331 — 14/11/2026
Écrit et haché AVANT toute ouverture des images F74_A0000329/330/331 (personne ne les a regardées : aucune découpe, aucune
mention dans les fichiers du dossier hors « réserve »). Clé figée AVANT : K_G25.json (SHA 3a81cd6d…41611), table de formes
neutres MAP_F_vers_G.json (SHA eb23f56e…1e) et planche CATALOGUE_F.jpg (sans valeurs ; SHA dans CATALOGUE_F.sha256).
K_G25 est une clé d'époque extérieure (copie Gabbrielli 1863-64 de la clé « an. 1492, Alamannis (de) Petrus »), transcrite
sur la feuille seule en deux passes (la seconde par un sous-agent qui n'a vu que la feuille). Aucune valeur de K_T n'y entre.

## Portion
Doc. 78 (Niccolini, déc. 1492), MAP LXXIV, positions 329, 330, 331 (images ASF 1272 px déjà sur SPOF_2). Pos. 332 (H de P01)
est grillée et exclue.

## Transcription (sous-agent T2, aveugle : ne voit ni K_G25, ni MAP→valeurs, ni K_T, ni CLE_KT.json, ni HANDOFF, ni RAPPORT g3,
ni l'issue #589)
1. Passe signes : chaque séquence chiffrée de 329-331, jeton par jeton, avec les identifiants F01…F39 de CATALOGUE_F.jpg ;
   signe absent du catalogue → `X:<description>` ; nombre à plusieurs chiffres ou groupe-code évident (22, 40, 100, HH, Hg,
   cercle pointé…) → `K:<forme>`. Gel SHA (P02_SIGNES.sha256) avant la passe glose.
2. Passe glose : glose interlinéaire d'époque telle qu'écrite au-dessus de chaque séquence ; marque C (glose complète et
   lisible) / P (partielle, illisible ou absente) ; pour chaque jeton K: le ou les mots de glose qu'il porte, entre [ ].
   Gel SHA (P02_GLOSE.sha256).
3. Deuxième lecture aveugle (règle commune 2) : un second sous-agent T3, mêmes interdits, transcrit les signes des séquences C
   sans voir T2 ; arbitrage sur l'image par T2 ou l'agent principal, jeton par jeton, AVANT tout décodage ; la version
   arbitrée est gelée (P02_FINAL.sha256). L'agent principal n'arbitre qu'en notant chaque choix (journal d'arbitrage).

## Mesure (une seule)
- Unités : séquences C. Seuil de taille : Σ jetons F (hors K:, hors X:) des séquences C ≥ 300. **Sinon : NON MESURABLE**
  (pas de décodage décisif, pas de mesure de repli sur une autre portion dans ce PREREG).
- Si 329-331 ne portent pas de glose (ou < 300 signes glosés) : non mesurable par accord de caractères ; on le dit et on s'arrête.
- Décodage : F → G (MAP_F_vers_G) → valeur K_G25 ; X: → chaîne vide ; K: → chaîne vide et les mots [ ] correspondants sont
  retirés de la glose.
- Normalisation des deux côtés (= P01) : minuscules ; v→u, j/y→i, k→c, h supprimé ; espaces et ponctuation supprimés ;
  lettres doublées réduites à une ; abréviations de glose développées seulement si notées à la passe glose.
- Accord car. = 1 − Σ distance d'édition(décodage, glose) / Σ longueur(glose normalisée).
- Témoins : 200 clés = valeurs de K_G25 permutées au hasard entre ses 39 formes (random.seed(2380)), même calcul.
- **Critère : accord ≥ 0,85 ET ≥ meilleur témoin + 0,30.** Une seule mesure, K_G25 inchangée, jamais rétroactif.
- Rapporté non décisif : accord en mots ; accord sans les X: ; part des jetons couverts par le catalogue.

## Suite selon résultat
- Validée : lecture des nues 2380 (docs 42, 49, 81, 90) avec K_G25, fiche stricte (sûrs / {probables} / [restitués] /
  ‹irrésolus›), règle des 95 % ; dossier relance/ seulement si utile. 2381 n'est PAS revendiqué (issue #589 d'aaymeloglu, ouverte).
- Non validée : plafonné ; décodage indicatif seulement.
