# PREREG D — BnF fr. 15567 f. 24r (catalogue 2838), Matignon's Cipher-1 — gelé 17/11/2026 AVANT toute transcription et tout décodage de f. 24

Antériorité : cible sœur matignon1584c1 (fr. 15568 ff. 151-152, PR #709 ouverte 16/11) ; portions A (f. 152r + der. l. f. 151v,
RÉUSSITE 0,876) et C (f. 151v ll. 1-9, ÉCHEC 0,767 < 0,85) GRILLÉES. f. 24 n'a jamais été transcrit ni décodé par nous.
Tomokiyo (cryptiana, henryiii.htm) a reconstitué la table à partir de f. 24 et f. 54, sans lecture : les gloses interlinéaires
de f. 24 sont au-dessus de la 1re ligne chiffrée.

- Portion : f. 24r, bloc chiffré, lignes 2 à 10 (tous les signes chiffrés), la ligne 1 (glosée) étant exclue.
  Si les lignes 2-10 font < 300 signes non nuls, la portion devient les lignes 1-10.
- Transcription : deux passes indépendantes de FORMES (étiquettes du BRIEF de matignon-1584-f151, étalons
  holdout_final.txt), la 2e par un sous-agent aveugle ; arbitrage sur l'image SANS clé ; gel SHA de la transcription
  arbitrée (PREREG-D2) avant décodage. Forme nouvelle = étiquette nouvelle, décodée « ? ».
- Clé figée : key_D.tsv = copie de matignon-1584-f151/key_read.tsv (table de Tomokiyo + valeurs établies sur fr. 15568
  ff. 151-152) sha256 eb00fd85de7f22d406b642779de93929ae4696301aef496cdf3538e9fee43404. AUCUNE modification.
- Scripts : scripts/decode.py 9206a6a0c7548b15cb2af759cb35d487b04b2b46355af5c8a0e76a73509097f0 ; measure.py de Daniel
  (targets/matignon1586c3/f276/scripts/measure.py, 9407804172883b8fb15da76efadd2cea6d5ba4c383e57602367ee56bb20d4d15),
  fr-1600-letters, mincount 20, 200 clés permutées, graine 2.
- Statistique M = part des signes non nuls lus (suites ≥ 3 mots du lexique totalisant ≥ 10 lettres).
- Seuils : RÉUSSITE si M ≥ 0,85 ET M ≥ max(200 témoins) + 0,30 ; sinon ÉCHEC. Une seule exécution ; sortie brute
  mesure/RESULTAT.txt ; la portion est ensuite grillée.
- Mention : 3e mesure de la famille de clés (A réussie, C échouée), sur un AUTRE document (catalogue 2838) ; le résultat
  sera déclaré tel quel, y compris un échec.
