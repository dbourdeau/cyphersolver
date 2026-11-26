# Journal de la mesure unique (26/11/2026)
- PREREG-BOISSIRAN-A.md + measure.py hachés (PREREG-BOISSIRAN-A.sha256) avant exécution ; exécution unique : python3 -I measure.py.
- Résultat : 78 groupes, 353 chiffres ; M(H1) = 0,987 ; meilleur témoin = 0,974 ; moyenne des témoins = 0,914 → critère (≥ 0,85 ET ≥ témoin + 0,30) NON ATTEINT.
- Diagnostic : la métrique (découpage en mots d'un lexique de 49 486 formes, mots de 2 lettres admis, 2-3 lettres par chiffre) n'est pas discriminante : presque toute suite se découpe. C'est un défaut de conception de la mesure, pas un indice contre la clé. Portion p2.23–p3.08 grillée pour toute nouvelle mesure.
- La lecture par le sens (LECTURE-PORTION-A.md) atteint 97,5 % sur cette même portion, avec un texte suivi (affaire de caution, meunier, incendie d'un moulin, 2000 livres, signature féminine, date « ce 26 may 1726 »).
- Prochaine étape proposée : PREREG-2 sur une portion neuve (p1.01–p1.09) avec une métrique discriminante (mots ≥ 4 lettres seulement, ou relecture aveugle du clair par un agent sans clé contre clés témoins). À décider par Brice.

## PREREG-2 (27/11/2026, accord de Brice)
- Contrôle de puissance sur la portion grillée : M = 0,7255 contre 0,2745 au mieux pour les témoins.
- PREREG-2-BOISSIRAN-A.md et measure2.py hachés (PREREG-2-BOISSIRAN-A.sha256 : c80fcd2e…, ef5a7099…), puis mesure unique sur p1.01–p1.09 (40 groupes de 4 chiffres et plus) : M(H1) = 0,85 ; meilleur témoin = 0,425 (aléatoire de même structure), 0,325 (permuté) ; moyenne des témoins = 0,121.
- Critère (M ≥ 0,50 et ≥ témoin + 0,30) ATTEINT : clé VALIDÉE. Portion p1.01–p1.09 grillée.
