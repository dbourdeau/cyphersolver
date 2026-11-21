# ADDENDUM 3 au PREREG code 1-246 — figé AVANT la 3ᵉ passe des nombres et avant toute nouvelle clé — 14/11/2026 ≈ 17:30
Base : PREREG-CODE246.md (06ffce5f…), ADDENDUM-1 (e0873adf…), ADDENDUM-2 (edd81f4a…), METHODE-CLE.md (2b83cbf0…),
référence de H figée verif-lot13/REFERENCE-G05-G20.txt (96e9e271…) et REFERENCE-G05-G20-lignes.tsv (bcb06431…).
Accord de Brice (14/11) : « pour Bonde, tente un nouveau passage ». Dernier état : clé lot 13 (key_candidate.json f0e3bd7e…)
resubstitution 0,619 < 0,85 → pas de mesure ; H (113 d. l. 19-33, H_final.tsv d428dfd3…) INTACTE, jamais décodée.
Tout ce qui suit porte sur l'APPRENTISSAGE seulement (113 d. L01-L18 ; 114 g. G01-G32). H_final.tsv colonne 2 n'est ouverte
par l'agent principal qu'après le gel de la clé, et seulement si le préalable est rempli.

## (a) 3ᵉ passe des nombres d'apprentissage
1. Positions à relire (liste calculée AVANT toute relecture, figée par SHA dans passe3/ITEMS-SECRET.json) : toute position
   d'un nombre de S1 (passA_113L) ou S2 (passA_114g) telle que
   - les passes A et B divergent (alignement des deux listes de la même ligne, difflib, nombre par nombre ; une position
     de A sans vis-à-vis dans B compte comme divergente), ou
   - passA marque l'incertitude (« x|y », « ? », « [?] »), ou
   - dans l'alignement du décodage par key_candidate.json (f0e3bd7e…) contre T (align() de build_key.py, inchangé),
     la lettre décodée n'est pas un appariement exact (substitution, lettre décodée non appariée, ou « ? »).
   Le décodage sert seulement à dire OÙ regarder ; il n'est montré à aucun relecteur ni à l'arbitre.
2. Deux relectures aveugles indépendantes (R1, R2) par des sous-agents Opus distincts : pour chaque position, la ligne,
   le rang du nombre dans la ligne et les deux nombres voisins de chaque côté (lecture A) comme repères ; ni la valeur
   de A ou B à cette position, ni aucune lettre, ni la clé, ni la glose attendue. Réponse : un nombre 1-246, « ? »
   (illisible), « AUCUN » (pas de groupe entre les repères) ou « n.m » (deux groupes).
3. Règle : si R1 = R2, cette lecture est retenue. Sinon, arbitre (3ᵉ sous-agent Opus) sur l'image : il voit les
   lectures candidates (A, B, R1, R2, dédoublonnées, ordre aléatoire graine 1676300, sans source ni lettre) et choisit
   d'après l'image, ou écrit une autre lecture, ou « ? ». « ? » → position supprimée (comme clean() de outils/data.py).
4. Les relecteurs et l'arbitre ne regardent pas 113 d. sous y = 2175 (lignes de H) ; images d'apprentissage seulement.
5. Résultat : passe3/S1_passe3.tsv et S2_passe3.tsv (= passA corrigé aux positions relues), figés par SHA avant la clé.

## (b) Normalisation déclarée de la référence et alignement
1. Abréviations (appliquées aux gloses BRUTES, insensible à la casse, dans cet ordre, puis normalisation habituelle
   minuscules, w=v, j=i, a-z å ä ö, « # » conservé ; mots = suites séparées par des blancs dans la glose brute) :
   - Maij:tz / Maij:ttz / Maij:ts / Maij:tts (et Maj:…) → « maiestets »
   - Maij:t / Maij:tt / Maij:~ / Maij: (et Maj:…) → « maiestet » ; M:t / M:tt → « maiestet »
   - Kongl: / Kongl. → « kongelig »
   - förben:~ / förbem:~ / förben: / förbem: / förb:te → « förbenämnde »
   - d. suivi d'un nombre → « den » ; & → « och » ; Exc: / Excell: / Exc. / Excell. → « excellens »
   Aucune autre substitution ; la liste ne sera pas étendue après avoir vu un résultat.
2. Alignement (fixe) : semi-global, extrémités de la référence libres, tout le décodé aligné ; coûts : appariement 0,
   substitution 1, lettre décodée non appariée 1, lettre de référence sautée 1, MOT ENTIER de référence sauté (mot
   présent seulement dans la glose) 1 par mot quelle que soit sa longueur ; « ? » (décodé) et « # » (référence) ne
   s'apparient jamais. Les mots présents seulement dans le chiffre restent comptés lettre à lettre (coût 1) : le chiffre
   n'a pas de séparateurs de mots et un saut bon marché côté décodé rendrait arbitraire le score des témoins (A est
   normalisé par la longueur décodée).
3. A = 1 − coût / longueur décodée (lettres décodées, « ? » compris), pour la resubstitution comme pour H.
4. Construction de la clé : METHODE-CLE.md inchangée (départ clé brouillon, align() d'origine pour le vote, ≤ 12
   itérations, vote majoritaire), avec S1/S2 = passe 3 et T = mêmes gloses qu'au lot 13 mais normalisées par (b)1.

## (c) Préalable et mesure — INCHANGÉS
- Préalable : resubstitution A_train (métrique (b)) ≥ 0,85 sur S1+S2 ; sinon PAS de mesure, H reste intacte.
  (Le score avec l'ancienne métrique sera aussi rapporté, sans valeur de décision.)
- Si rempli : clé gelée (KEY_code246.tsv + KEY.sha256), puis UN décodage de H (H_final.tsv col. 2, 1ʳᵉ option, « ? »,
  « [?] » ignorés) contre la référence G05-G20 (REFERENCE-G05-G20-lignes.tsv col. 2, normalisée par (b)1, « # »
  conservé). Longueur décodée ≥ 0,8 × 301. 200 témoins : permutation des lettres entre les nombres de la clé (une seule
  classe), graines 1676000-1676199, même métrique. SUCCÈS si A ≥ 0,85 ET A ≥ max(témoins) + 0,30. Une seule mesure ;
  H grillée ensuite.
- Aucun autre changement.
