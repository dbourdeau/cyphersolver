# PREREG — Holbeck → Rowland Browne, 10/3/1550-51 (Hatfield CP 150/143 ; cat. 1015, ar-962) — gelé 16/11/2026 AVANT la mesure

Système (établi sur DEV = p. 1 et 2, transcription passe 2) : substitution simple, mots séparés, une partie des lettres garde
sa forme (t h e o b …), le reste substitué : 4=a, p=n, z=r (et k : forme proche), D=s/d, Q=l/d, 8=w, 9=g, 7=p, j=f, w(«10»)=m,
v=u, s=c, 2=i/y/k, y=p. Les ensembles {…} de la clé absorbent les confusions de formes de transcription.
Clé figée : cle/key-FROZEN.json. Script : cle/mesure.py. Lexique : /usr/share/dict/words (web2) + cle/lex-supp.txt
(formes anciennes relevées dans le DEV seulement ; mots inspirés de la p. 3 retirés avant le gel).

TEST (portion tenue à l'écart, définie et gelée avant le travail de clé, HOLDOUT-DEF.md sha 456e52f5…) : page 3,
transcription/p3-TEST-passe1.txt (sha 0308463d…, 1081 signes). Mesure UNIQUE.
Mesure : fraction des signes du TEST appartenant à des mots qui, décodés par la clé (une combinaison des ensembles au
moins), puis normalisés (minuscules, y→i, v→u, j→i, lettres doublées réduites, -e final ôté), sont dans le lexique.
Témoins : 200 clés obtenues en mélangeant les valeurs de la clé entre les signes (graines 0–199), même lexique.
Seuils : score ≥ 0,85 ET score ≥ meilleur témoin + 0,30 → clé validée hors échantillon.
Secondaire (rapporté, ne décide pas) : même mesure sur transcription/p3-TEST-passe2.txt (passe aveugle indépendante).
Valeurs DEV de référence (avant gel) : p1 0,847 (témoin max 0,478) ; p2 0,857 (0,444).
Réserve d'honnêteté : chiffre très faible (mots anglais en partie lisibles à l'œil) ; la p. 3 a été vue pendant sa
transcription par formes ; la mesure contrôle la clé mécaniquement, pas l'ignorance du lecteur.
