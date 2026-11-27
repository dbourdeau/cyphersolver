# PREREG E — lettres sœurs du « Matignon's Cipher-1 » : BnF fr. 15567 f. 54r (E1) et BnF fr. 3255 f. 85r (E2)
# Gelé le 17/11/2026 AVANT toute transcription et tout décodage de ces deux folios (décision de Brice du 17/11).

Antériorité de mesure : jamais mesurés ni transcrits par nous (grep des dossiers bellievre-matignon-1584 et
matignon-1584-f151 ; PR de bdudout : #709 matignon1584c1 = fr. 15568 ff. 151-152 ; #711 hautefort1584 = fr. 15567
ff. 158-161, autre système). Mesures antérieures de la même clé : A (f. 152r, RÉUSSITE 0,876), C (f. 151v, ÉCHEC 0,767),
D (fr. 15567 f. 24, ÉCHEC 0,764). Ces mesures E1 et E2 sont les 4e et 5e de la famille ; résultats déclarés tels quels.

Images (Source gallica.bnf.fr / BnF), openapi.bnf.fr IIIF full/max :
- E1 : fr. 15567, ark btv1b90639282, vue 60 (page de droite, folio 54). Lettre au roi (« Sire, vostre ma.té … monsieur de
  Bellievre »), ~21 lignes chiffrées après 7 lignes de clair. Gloses interlinéaires sur les 2 premières lignes chiffrées
  et quelques mots plus bas. Tomokiyo : « the last line on f.54r appears to be all nulls ». 🔴 Indépendance partielle :
  Tomokiyo a reconstitué sa table à partir de f. 24 ET f. 54 (sans doute par les gloses) ; key_D contient ses valeurs.
- E2 : fr. 3255, ark btv1b9059888k, vue 88 (page de droite, folio 85). Lettre « relative à la renprynse de Périgueux et au
  Sr d'Aubeterre » ; BAM : « en chiffre, avec déchiffrement » → déchiffrement interlinéaire D'ÉPOQUE sur presque toutes
  les lignes (EXISTING : aucune lecture nouvelle ne sera revendiquée, la mesure n'éprouve que la clé). Ni Tomokiyo ni nous
  n'avons tiré de valeur de ce folio : document le plus indépendant de la clé.

Portions (signes chiffrés seulement ; gloses interlinéaires, clair, adresse, signature exclus ; lignes comptées à partir de
la 1re ligne chiffrée de la page) :
- E1 = f. 54r, lignes chiffrées 3 à 12 incluses (les ll. 1-2, glosées, et la dernière ligne, nulles, exclues). Si moins de
  300 étiquettes non nulles, ajouter les lignes 13, 14 … jusqu'à ≥ 300.
- E2 = f. 85r, toutes les lignes chiffrées (1 à la dernière). Si moins de 300 étiquettes non nulles : E2 non mesurable
  (pas de mesure, déclaré tel quel).

Transcription : deux passes indépendantes de FORMES (étiquettes du BRIEF matignon-1584-f151, étalons holdout_final.txt et
f24_portion_final.txt), par sous-agents aveugles qui ne voient ni clé ni décodage ni l'autre passe ; arbitrage sur l'image
SANS clé ; gel SHA des transcriptions arbitrées et des scripts (PREREG-E2) AVANT tout décodage. Forme nouvelle = étiquette
nouvelle, décodée « ? ».

Clé figée : key_D.tsv TELLE QUELLE, sha256 eb00fd85de7f22d406b642779de93929ae4696301aef496cdf3538e9fee43404. AUCUNE modif.
Scripts : scripts/decode.py 9206a6a0c7548b15cb2af759cb35d487b04b2b46355af5c8a0e76a73509097f0 ; measure.py de Daniel
(targets/matignon1586c3/f276/scripts/measure.py, 9407804172883b8fb15da76efadd2cea6d5ba4c383e57602367ee56bb20d4d15),
fr-1600-letters, mincount 20, 200 clés permutées, graine du script.
Statistique M = part des signes non nuls lus (suites ≥ 3 mots du lexique totalisant ≥ 10 lettres).
Seuils, pour CHAQUE portion séparément : RÉUSSITE si M ≥ 0,85 ET M ≥ max(200 témoins) + 0,30 ; sinon ÉCHEC.
UNE exécution par portion (scripts/run_measure_E.sh fait E1 puis E2 en une fois) ; sorties brutes mesure/RESULTAT_E1.txt
et mesure/RESULTAT_E2.txt ; les deux portions sont ensuite grillées. Pas de correction des seuils pour tests multiples
(déclaré) ; une réussite de E1 seule sera signalée avec la réserve d'indépendance ci-dessus.
Après mesure : compte strict de Daniel (sûrs / probables / restitués / irrésolus) sur E1 ; sur E2, comparaison au
déchiffrement d'époque.
