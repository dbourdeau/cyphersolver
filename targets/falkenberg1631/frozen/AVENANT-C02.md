# Avenant C02 au protocole (n° 1126, Falkenberg 28/3/1631) — écrit AVANT tout calcul de K2

Rédigé le 29/10/2026 (séance C02, agent Opus), haché (SHA-256 dans HANDOFF.md, section C02) avant la construction de K2.
Le protocole C01 (PROTOCOLE.md) reste en vigueur ; K1.json reste gelée et n'est pas modifiée.

1. Matériel nouveau : gloses interlinéaires d'époque des lettres de Falkenberg du même volume
   (SE/RA/1133/1133.07/~/10), images R0000785_00102 à _00130 (sauf la lettre tenue à l'écart, §3).
   La 00100R est un AUTRE système (substitution de lettres sur texte suédois, glosée) : exclue.
   La 00104R (12/11/1630) est une lettre surtout en chiffre de lettres sans points : utilisée pour les lettres seulement.
2. K2 = K1 + chaque valeur nouvelle (code, sigle, homophone de lettre ou nulle) ATTESTÉE par une glose d'époque.
   Chaque ajout porte : la glose, l'image (vue) et la ligne (falkenberg/K2_ajouts.tsv). Une valeur dont la glose est
   illisible ou contradictoire n'entre pas dans K2 (elle peut servir de justification « probable » à la lecture, notée).
   Les nulles (numéros en bande 84–99 et 10) entrent dans K2 si au moins une glose les saute explicitement.
3. Nouvelle lettre tenue à l'écart, choisie AVANT de lire ses gloses : la lettre du 22 janvier 1631, image
   R0000785_00118 (page droite, f. 86 env.). Ses gloses ne servent pas à K2. Après gel de K2 (SHA), je relève les paires
   chiffre/glose de cette lettre et je mesure, séparément : (a) lettres : part des signes 10–99 (hors nulles K2) dont la
   valeur K2 = la glose ; (b) codes et sigles : part des nombres ≥ 100 et sigles définis dans K2 dont la valeur = la glose.
   Seuils : 0,85 lettres / 0,75 codes. Témoins : 200 permutations des valeurs de K2 (graine 1126) ; le score réel doit
   dépasser le maximum des témoins. Si 118 n'offre pas ≥ 15 codes/sigles définis, je complète AVEC la lettre 00123/00124
   (9/2/1631, feuillet collé) désignée ici comme réserve, sans en lire les gloses avant le gel.
4. Relecture de 1126 avec K2 (transcription cipher_133.txt inchangée) selon la règle de Daniel (≥ 95 % des mots lus par
   le sens) : sûrs (K2 glosé) / probables {x} / restitués [x] / irrésolus ‹…›. Une restitution ne contredit jamais des
   lettres sûres ; orthographe du chiffre gardée ; cribs : copie « D. v. F. » (Dittmar n° 21) et lettre suivante (Dittmar n° 34).
5. Vérification du n° 1127 (2/3/1631) dans le même volume : glosé ou non → statut (existing si glosé/déchiffré d'époque).
6. Publication seulement si ≥ 95 % ET inédit (Dittmar 1885 et toute édition vérifiés) ; sinon RÉSULTAT et point de reprise.
