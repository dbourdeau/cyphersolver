# PREREG-2 — système à index 1644-45 (unité 274999, img 321-323, 402-425) — gelé le 14/11/2026 AVANT toute construction de clé v3 et tout décodage de la portion tenue à l'écart

Antériorité : McBratney, `targets/pentz1636` (PR #522) : tables 1-2 (key v1) ; key v2 (b110, glose Günther img 48 de l'unité 260651) : index 62/63/64→T1, 13/12/11→T2, 10/9/8→T3, T3 t19 e35 n25 a29.
Observé avant ce gel : img 321 (lettre de Pentz, Glückstadt, 29 avril 1644, recto) porte un déchiffrement interlinéaire d'époque au-dessus de toutes les figures ;
img 322 (= 323, deux prises de la même page) = verso de la même lettre, seule la 1re ligne chiffrée est glosée. J'ai vu les gloses de 321 (lecture en cours) ; rien n'a été décodé sur 322 L2+ ni sur 425.

1. Clé v3 (KEY-v3.json) construite UNIQUEMENT à partir de : key v1/v2 de pentz1636 + gloses d'époque de img 321 et de la ligne 1 de img 322.
   Valeurs non attestées : remplies par la règle de la table (T1/T2 comme pentz1636 ; T3 = miroir de T1 : a-i montants à partir de 29, k-z descendants à partir de 28), marquées « rule ».
   Gloses contredisant la règle : la glose l'emporte. Clé gelée par SHA-256 (HASHES-KEY-v3.sha256) avant la mesure.
2. Portion tenue à l'écart = (a) img 322, page gauche, toutes les lignes chiffrées après la ligne 1 (non glosées) ; (b) img 425 (lettre au chancelier, 1645), tout le bloc chiffré.
   Aucune lecture des gloses éventuelles de 425 avant la mesure. Attendu ≥ 150 groupes ; sinon pas de mesure.
   Deux passes de transcription (B sur recadrages refaits, sans regarder A), arbitrage sur l'image, gel SHA-256 (HASHES-HELDOUT.sha256) avant la mesure.
3. Mesure unique : `python3 -I measure2.py KEY-v3.json HELDOUT.json` (script gelé ici).
   Décodage à index (table courante = la dernière annoncée par un index ; T1 par défaut) ; nombres ≥ 100 = codes (ignorés).
   Statistique : log-prob moyen par caractère, 4-grammes allemand (corpus de-gutenberg du dépôt, SHA 4828ed84…), normalisée N comme PREREG.md ;
   200 témoins = valeurs lettres permutées à l'intérieur de chaque table (seed 20261114) ; 50 fenêtres d'allemand réel.
   **PASS si N ≥ 0,75 ET N ≥ N(meilleur témoin) + 0,30 ET couverture (figures < 100 hors index résolues par la clé) ≥ 90 %.**
4. PASS ≠ lecture. Lecture par le sens par document (jamais de mise en commun des comptes), règle de Daniel (≥ 95 % = read), fiche sûrs/{probables}/[restitués]/‹irrésolus›.
