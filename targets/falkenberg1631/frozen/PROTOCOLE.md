# Protocole (écrit avant tout calcul) — n° 1126, Falkenberg → Gustave-Adolphe, 28 mars 1631

Rédigé le 29/10/2026 avant toute construction de clé. Haché (SHA-256 en fin de HANDOFF).

Système observé (inspection visuelle seulement) : nombres à 2 chiffres (10–99) = lettres (homophones probables) ;
nombres à 3–4 chiffres (≈ 100–3999) = nomenclateur (mots, noms) ; abréviations (rr, ee, ll, d.g., Eq, ff, nn, x, v) =
probables nulles ou mots courts ; mots en clair intercalés.

1. Matériel de clé : UNIQUEMENT les gloses interlinéaires d'époque des autres lettres de Falkenberg du même volume
   (SE/RA/1133/1133.07/~/10, images R0000785_00112 à _00132), et la paraphrase de Dittmar 1885 pour contrôle.
2. Tenue à l'écart : la lettre du 17 mars 1631 (image 131, ff. 99) est mise de côté AVANT construction ; ses gloses ne
   servent pas à la clé K1. La clé K1 est construite sur les autres lettres glosées, gelée (SHA), puis appliquée aux
   groupes de la lettre du 17 mars.
3. Mesures sur le texte tenu à l'écart : (a) lettres : part des signes 10–99 dont la valeur K1 = la glose (car.) ;
   (b) codes : part des nombres ≥ 100 dont la valeur K1 = la glose (mots), sur les groupes où K1 a une valeur.
   Seuils : 0,85 car. / 0,75 mots. Témoins : 200 clés obtenues en permutant au hasard les valeurs de K1 (même
   ensemble de valeurs, graine fixée 1126) ; le score réel doit dépasser le maximum des 200 témoins.
4. Si la validation passe : clé finale K2 = K1 + gloses du 17 mars, gelée (SHA), appliquée à la lettre du 28 mars
   (image 133). Lecture notée selon la règle de Daniel (95 % des mots lus par le sens) : sûrs / {probables} /
   [restitués] / ‹irrésolus›. Une restitution ne contredit jamais des lettres sûres ; orthographe du chiffre gardée.
5. Contrôle externe partiel : la 2ᵉ partie chiffrée doit retrouver le contenu de la copie « D. v. F. » paraphrasée par
   Dittmar (n° 21 : Garleben, Saltwedel, « Wan E. M. nicht bald kombt, sein wir verloren », etc.).
