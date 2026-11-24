# Règle de sélection — planche de SUIVI capilupi1546 (lettre r, soir 18/11/2026), écrite AVANT le choix des signes et avant toute réponse

But : faire monter les SÛRS SEULS (#728) après la planche C. La règle du sens (95 %) est déjà passée sur les 4 documents Y.
Entrée : copie v2 des transcriptions (planche_prive/v2/, après les 8 corrections confirmées de la planche C), clé figée KEY-1555.json,
reading.md de la cible ; recherche `scripts/cand_r.py` -> `work/cand_r.json`.

1. Candidats : écarts lecture/décodage restants dont le mot est {x} (probable) ou [x] (restitué), et qu'UN remplacement d'un seul
   chiffre fait disparaître sans créer d'autre écart (coût du folio = coût avant − coût de l'écart).
   - remplacement par 0-7, ou par 9 seulement s'il entre dans un code (pas de nulle ajoutée : ni 8, ni 9 isolé, ni « 31 ») ;
     pas de suppression ;
   - la correction doit être UNIQUE (une seule position et un seul chiffre) ; sinon le mot est écarté comme ambigu ;
   - aucun signe déjà posé sur la planche C (questions ou contrôles) ne revient.
2. Ordre :
   (a) les [x] (gain sous les deux règles), document le plus bas en sûrs seuls d'abord (05r-05v 89,2 % < 06r-07r 91,7 % < 02r 93,0 % < 04r 97,5 %), puis ordre des lignes ;
   (b) les {x} de 05r-05v (document le plus bas) ;
   (c) les {x} dont la correction est 1 -> 5 (même confusion que la série « mm », 5 confirmations sur 5 en planche C), ordre des folios ;
   (d) les autres {x}, document le plus bas d'abord, puis ordre des lignes.
   On prend les 10 premiers. Un candidat est écarté (remplacé par le suivant) si, à l'image native, le signe ne peut pas être
   encadré seul (ligature, tache couvrant le signe).
3. Deux contrôles NEUFS (jamais posés ni utilisés comme vignette en planche C) : un 9 crochet net et un 1 net, chacun dans un
   code d'un mot sûr, non marqué [a/b], ?, ~, ^.
4. Options : 3 formes (la forme transcrite, la forme proposée, une troisième forme voisine), vignettes reprises des jeux déjà
   vérifiés un par un pour la planche C (05r pour 02r/05r/05v, 06r pour 06r/06v/07r ; le 3 vient toujours de 05r),
   découpées dans des codes de mots sûrs.
5. Ordre des questions et des options : graines 20261119 / 1546, planche_core v2 (places des références équilibrées).
