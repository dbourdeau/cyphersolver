# PROTOCOL — ammen-1862 (lead Bourdeau n° 2097 = doublon du lead 1432)
Gelé le 2026-11-03 AVANT tout calcul de résolution (seule une lecture visuelle de la pièce a été faite pour la transcrire).

## Pièce
Ball State DMR, LSTACivWar 2072 (pages 2070, 2071), Henry County Historical Society. Daté en clair « Knoxville, Sept. 29 '64 » (et non 1862 : la date de notice 1862-09-29 est une erreur ; titres de pages HCHS_L_18640929).
Transcription gelée : working/transcription.txt (SHA-256 dans SHA256SUMS).

## Système (hypothèse a priori)
Chiffre de route du télégraphe militaire de l'Union (famille Stager) : mots en clair écrits en grille, relevés par colonnes selon une route (haut/bas), mots nuls (« arbitraries ») en fin de colonne, mot de commencement en tête. Il n'y a PAS de substitution de caractères : le texte chiffré est fait de mots anglais en clair.

## Conséquence pour la validation (déclarée AVANT calcul)
Le critère standard (accord en caractères ≥ 0,85 ET ≥ meilleur témoin + 0,30 sur portion tenue à l'écart, 200 témoins) suppose une clé de substitution appliquée à un texte de référence. Ici :
- il n'existe aucun clair de référence indépendant (pas d'interligne d'époque) ;
- la « clé » est une route (nb de colonnes, ordre, sens, nuls) ; pour 107 mots, une portion tenue à l'écart significative n'existe pas (une route ne se « valide » pas sur des lignes séparées : toutes les colonnes traversent toutes les lignes).
=> Le critère car. ≥ 0,85 est déclaré NON APPLICABLE ; aucune mesure ne sera présentée comme validation au sens du protocole permanent.

Mesure descriptive (une seule fois, non décisive, rapportée telle quelle) : si une route est trouvée, on calcule la part des paires de mots adjacents du clair reconstruit qui forment un bigramme attesté dans un petit corpus de référence fixé ici = le reste du texte n'est pas utilisable ; on utilisera donc une mesure purement interne : nombre de mots du clair restituant une phrase grammaticale lue par le sens (fiche sûrs/probables/irrésolus), et comparaison avec 200 routes témoins aléatoires (même grille, ordre et sens de colonnes tirés au hasard, graine 20261103) jugées sur le même compte automatique de bigrammes « fonctionnels » (liste fermée ci-dessous). Rapporté, non décisif.
Liste fermée de bigrammes fonctionnels : (the, X) suivi d'un nom/adj non-fonction ; paires « to + verbe » ; on n'en fera PAS un critère.

## Antériorité
Rechercher le clair dans les Official Records (OR, sér. I, vol. 39 pt 2–3, sept.–oct. 1864) et la littérature (Plum 1882, Bates 1907, Lasry, cipherbrain). Un clair d'époque publié => EXISTING.

## Publication
Aucune publication par cet agent. Publiable seulement si clé validée (impossible ici au sens strict) ET ≥ 95 % des mots lus par le sens.
