# PREREG-3 — clé structurée modulo 24 (rédigé le 27/11/2026, accord de Brice relayé ; AVANT toute transcription/lecture de la portion 3)

## Hypothèse (vue APRÈS la mesure 1, d'où ce nouveau test)
Les nombres 40–199 forment une table de 24 cases répétée : lettre(n) = T[n mod 24].
Clé K' (algorithme fixé ici, appliqué ensuite UNE fois puis gelé) : pour chaque résidu r, T[r] = lettre majoritaire
de la somme des votes de CLE-K.json (SHA 77dfe736…ad5a, inchangée) pour tous les n ≡ r (mod 24) ; égalité → « ? ».
Codes ≥ 200 : table de K inchangée (inconnu → « ? »). Aucune autre donnée n'entre dans K'.

## Portion 3 (neuve) et garantie de séparation
Blocs chiffrés écrits en MARGE des concepts sortants, fol. 318r, 318v, 319r (doubles pages 317v-318r, 318v-319r).
Si le total < 300 nombres : extension, dans cet ordre et seulement pour les pages qui ont des blocs : 300v, 301r, 161v, 162r, 314v.
Séparation : (1) folios d'apprentissage de K = colonne 1 de T1–T4 (160r…339v ; 318r/318v/319r/300v/301r/161v/162r/314v absents, vérifié
par `cut -f1 apprentissage/*.tsv` le 27/11 avant rédaction) ; (2) portions grillées 297r–298v et portion PREREG-2 (336r, 321r) exclues ;
(3) le script de mesure refuse toute ligne dont le folio figure dans ces listes (assertion) ; (4) les transcripteurs ne reçoivent ni K ni K'.
Transcription : 2 passes aveugles indépendantes des blocs (P3-A, P3-B), arbitrage sur image, gel SHA-256 ; concept clair des mêmes pages
transcrit séparément (P3-C, sans les blocs déchiffrés), gelé.

## Métrique (fixée d'avance)
Pour chaque bloc : déchiffrement par K' (normalisé norm.py) ; alignement LOCAL (Smith-Waterman +1/−1/−1, scripts/sw.py) contre le texte
clair normalisé de la page de concept portant le bloc (pages 318r/318v/319r prises ensemble si le renvoi est incertain).
Accord = Σ caractères justes ÷ Σ caractères déchiffrés (« ? » = faux). Minimum 300 nombres.
Témoins : 200 permutations des 24 cases de T (graine 24683), même calcul.

## Seuil et justification (à partir de la seule portion grillée)
Calibration SANS clé (scripts/calib_rho.py, exécuté avant ce PREREG) : les mots EN CLAIR de la lettre 297r–v, alignés de la même
manière sur leur concept 298r–v, ne concordent qu'à ρ = 0,653 (943 caractères, 38 suites de mots) : c'est le plafond observé
de l'écart concept ↔ original (variantes de rédaction + bruit de transcription des deux textes). Un accord de 0,85 n'est donc pas
atteignable même avec une clé parfaite. Seuil = 0,85 × ρ = **0,555**, ET ≥ meilleur témoin + 0,30.
(Les blocs marginaux sont chiffrés depuis le concept même ; l'écart réel devrait être moindre — le seuil est donc prudent côté
« pas de faux échec », et la marge +0,30 sur les témoins protège contre le faux succès de l'alignement local.)

## Mesure unique ; rapporté en plus (non décisif)
Accord en mots ; lecture par le sens selon la règle de Daniel (sûrs / {probables} / [restitués] / ‹irrésolus›).
Portion 3 grillée après la mesure. Aucune retouche de K', des transcriptions ni du script après le gel.
