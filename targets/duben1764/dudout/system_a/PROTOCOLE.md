# C01 — protocole (écrit le 2026-10-27 02:20 CET, AVANT tout calcul de décodage)

Matériau : trois tables de chiffre du volume (images 218, 219, 220) ; pages chiffrées (images 59–60, 87–126) ;
pages en clair rangées à côté des chiffrés, dont au moins une portant une note d'archiviste « Hör till chiffreringen
"15.73.100.347.503.401.107.536." » (image 97, p. droite) = déchiffrement contemporain rattaché à un chiffré précis.

Règles lues sur les tables (à vérifier, non supposées) :
- T218 : « Au commencement et à la fin de chaque période ou mot chiffré, on ajoute deux nombres qui ne sont comptés pour
  rien en déchiffrant, non plus que les zéros qu'on ajoute indifféremment. Et on compte toujours par trois en déchiffrant. »
  → hypothèse H1 : on supprime les 0, on concatène les chiffres et on regroupe par 3 (les points sont trompeurs).
- T220 : « La marque de ce chiffre est ##. Les apostrophes sont désignés par un ou plusieurs zéros, qui d'ailleurs ne servent
  qu'à remplir et à déguiser le chiffre. NB on commence toujours par sept chiffre(s) qui ne signifient rien. »
  → H2 : même regroupement, 7 chiffres initiaux nuls.
- T219 : table 9×9 (valeurs xy1–xy7) « Chiffern använt mellan Lovisa Ulrika och Kronprinsen under dennes franska resa »
  (1770–71) ; déjà imprimée selon la note (Svenska Akademiens handlingar 29, s. 259) ; hors cible chronologique, test de contrôle seulement.

Tests prévus, dans l'ordre, sur une page transcrite intégralement (image 107 p. droite, puis la page qui commence par
15.73.100… si elle est trouvée) :
1. Chaque table × {lecture des groupes tels qu'écrits ; H1 (sans zéros, par 3)} × {décalage 0,1,2}.
2. Critère « la clé lit » : ≥ 80 % des triplets trouvés dans la table ET le texte produit des mots français reconnaissables
   sur ≥ 3 segments consécutifs de 10 triplets. Témoin : même calcul sur la même page avec les chiffres mélangés
   (permutation aléatoire des chiffres, 20 tirages) ; le score réel doit dépasser le maximum des témoins.
3. Validation : confrontation au clair contemporain (note « Hör till chiffreringen ») — accord mot à mot mesuré,
   le clair n'étant PAS utilisé pour construire ou corriger la clé (seulement pour mesurer).
4. Les valeurs de clé illisibles ou les triplets absents de la table restent ‹nnn› ; lecture classée : mot certain,
   {x} probable, ‹x› irrésolu. Pas de comblement par conjecture.
