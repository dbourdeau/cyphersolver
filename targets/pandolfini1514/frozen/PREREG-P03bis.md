# PREREG-P03bis — pandolfini-francia-1514-15 (cat. Bourdeau 2389) — 09/11/2026 ≈ 02:55 CET
Accord d'avance de Brice transmis par le coordinateur. Écrit et haché AVANT toute transcription de 342, avant la construction
du modèle de n-grammes et avant la calibration. PROTOCOLE.md, PREREG-P02, PREREG-P03 (dbcef856…) restent en vigueur pour le reste.

## Regards déclarés (voir mesure/RESULTAT_P03.md)
Vignettes des hauts de pages 867-878 (½ échelle) ; 867 haut (en-tête + 3 lignes de clair « Le ultime mie furono … ») ;
870 entière à ½ échelle (chiffre, non transcrit) ; 873 haut ; 876 entière à ½ échelle (quelques mots du corps de 343).
Aucun jeton de 342 transcrit, rien décodé.

## Clé : cle/CLE_v3.json (ae5f0b9f…), FIGÉE, inchangée.

## H4 (bloc mesuré)
- 342, PREMIER bloc chiffré continu de la lettre (pos. 867 puis suite), du premier signe chiffré jusqu'au premier passage en clair
  d'au moins trois mots ; si moins de 4 lignes, + le bloc suivant (même règle). Jetons LEGENDE.md (+ ajouts de forme consignés,
  sans valeurs). Gel transcription/TRANSCRIPTION_H4.sha256 avant la mesure. Rien décodé avant la mesure.

## Critère INDÉPENDANT de la paire : log-vraisemblance de n-grammes italiens
- Corpus fixé maintenant (aucune pièce Pandolfini) : cistarelli-1520/sources/corpus/pg56498.txt (Machiavelli, Mandragola /
  Clizia / Belfagor), pg61704-6.txt (Villari, Machiavelli e i suoi tempi I-III) ; en-têtes/licences Gutenberg retirés
  (entre les marqueurs « *** START » / « *** END »). Le dernier 5 % de pg56498 est tenu à l'écart = échantillon italien de référence.
- Normalisation = norm() de measure_p03.py (minuscules, lettres seules, h supprimé, j/y→i, v→u, k→c, x→s, ph→f, doubles réduites) ;
  « ? » (signe inconnu) gardé comme symbole.
- Modèle : trigrammes de caractères sur le texte normalisé (mots concaténés comme dans la mesure), lissage additif k = 0,1,
  alphabet = lettres du corpus normalisé + « ? ». LL(t) = moyenne par caractère de log P(c_i | c_{i-2} c_{i-1}).
- Pour un bloc H : S = LL(norm(décodage v3)) ; 200 témoins (permutation base/vowels comme P01-P03, graine 20261111) ;
  B = max des LL témoins ; S_it = LL de l'échantillon italien de référence.
  SCORE NORMALISÉ N = (S − B) / (S_it − B)  (0 = pas mieux que la meilleure clé mélangée ; 1 = italien de référence).
- Calibration UNIQUEMENT sur 340/341 (grillés) : B_340 = max LL des 200 témoins sur H2 (même graine) ; la référence R2 (341, clair
  normalisé) est dégradée par substitution aléatoire uniforme de lettres à l'exactitude a (50 tirages par a, graine 7) :
  N(a) = moyenne de (LL(R2 dégradé) − B_340) / (S_it − B_340).
  * N_V = N(0,85) (équivalent du seuil 0,85) ;
  * N_P = N(meilleur témoin en caractères de P02 sur 340 + 0,30) = N(0,6412) (équivalent « marge ≥ 0,30 »).
  Contrôle rapporté (non décisif) : N de 340 décodé par v3 (accord 0,715) doit tomber entre N_P et N_V.
  N_V et N_P sont écrits dans mesure/CALIB_P03bis.json et hachés AVANT la transcription de 342.
- SEUILS (décisifs) : VALIDÉE si N ≥ N_V ; PARTIEL si N_P ≤ N < N_V ; NON VALIDÉE si N < N_P. Une seule mesure. H4 grillée dans tous les cas.

## Après la mesure seulement
- Comparaison avec 343 : chercher si le décodé est le clair de 343 (diagnostic déclaré, SANS valeur de validation).
- VALIDÉE ou PARTIEL : lettres nues 307, 309, 310, 311, 322, 333 — contrôle EXISTING puis lecture au compte de Daniel
  (sûrs / probables {x} / restitués [x] / irrésolus ‹…›, % lu par le sens) ; PARTIEL ⇒ toute lecture dite partielle ; PR-PREP à jour.
- NON VALIDÉE : rien n'est présenté comme lu.
