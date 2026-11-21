# ADDENDUM 1 au PREREG code 1-246 — figé AVANT toute construction de clé — 14/11/2026
Base : PREREG-CODE246.md (SHA 06ffce5f…). H (113 d. lignes 19-33) est transcrite et figée par les sous-agents :
H-secret/H_final.tsv, SHA-256 d428dfd358ae68a7eb33528d96ef89c2cf1862427b789eaf77665ab64aa9e391 (301 groupes, glose 522 lettres).
L'agent principal n'a ouvert NI les nombres NI la glose de H (seulement les rapports chiffrés des sous-agents).

## Constat qui invalide la référence du PREREG (fait AVANT toute clé)
- Une lettre par nombre (homophones) : crayon tardif « N o v e m b r i s » sous 9 nombres (114 g., dernière ligne) ;
  crayon de la ligne 1 de 113 d. : « h e r | c a n t z l i r … » un par nombre.
- Mais chaque ligne de glose porte ≈ 2,2 fois plus de lettres que la ligne chiffrée qu'elle surmonte (glose de 114 g.
  l. 2-3 : ≈ 45 lettres pour 20 nombres). La glose avance donc ≈ deux fois plus vite que le chiffre : l'ensemble des
  gloses (113 d. G1-G33 + 114 g. G1-G4, finissant par « Carolus Bonde Paris d. 13 Novembris » puis « 1675 ») est le
  clair de TOUT le chiffre (113 d. + 114 g., lignes nues comprises, qui finissent par « …Novembris » + « 1675 »).
- Conséquence : le clair des nombres de H se trouve au MILIEU de la glose (≈ G8-G18), pas dans G18-G33 ; la
  référence du PREREG (G18 + G19… + 114 G1) ne correspond pas à H : la mesure prévue serait nulle par construction.
  Et les lignes nues de 114 g. sont probablement DÉJÀ glosées (glose basse de 113 d.) → lecture « EXISTING ».

## Nouvelle définition (remplace § Partage/Clé/Métrique seulement sur ces points)
- Nombres de H inchangés (H_final.tsv, figé). Les gloses G19-G33 (colonne 3 de H_final.tsv) passent en APPRENTISSAGE
  (clair probable des lignes nues de 114 g.) ; l'agent principal pourra lire la colonne 3 SEULE (cut -f1,3), jamais la 2.
- APPRENTISSAGE : nombres 113 d. L01-L18 + 114 g. G01-G32 ; toutes les gloses ; crayons ; corpus suédois (lectures
  McBratney, notre T.tsv) pour un modèle de langue.
- Référence de H = gloses G05 … G20 de 113 d., concaténées et normalisées (marges libres ; le clair attendu de H est
  ≈ 300-400 lettres à l'intérieur).
- Métrique, contrainte de longueur (≥ 0,8 × 301), 200 témoins (graines 1676000-1676199) et seuils (≥ 0,85 ET
  ≥ max témoins + 0,30) INCHANGÉS. Clé gelée par SHA avant le décodage de H. Une seule mesure ; H grillée ensuite.
- Fuite reconnue : la référence de H fait partie des gloses lues pour l'apprentissage ; sans les nombres de H, cela
  n'apprend aucune valeur de H (seulement le modèle de langue). Noté comme limite.
