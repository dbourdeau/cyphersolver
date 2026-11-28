# Protocole d'exécution de l'ADDENDUM-2 § 2a-6 (relecture aveugle Opus) — figé AVANT tout tirage — 14/11/2026 ≈ 17:10
Base : ADDENDUM-2 (SHA edd81f4a…5bc00e). Sortie Fable figée : fable-lot13/SHA256SUMS.txt (GLOSS 32b84fa3…).
Aucune planche de Brice n'existe à ce stade (2b sans objet ; si elle arrive, elle prime).

## Unités (G05-G20 de GLOSS-113R-G01-G20.tsv, colonne transcription)
- Lettre « sûre » = un caractère alphabétique hors {…} et hors ‹…›.
- Lettre « douteuse » = un groupe {x|y|…} (une unité, même si une option a 2 lettres : ff, iä, ij).
- Zone illisible = un ‹…n›.
## Échantillon des sûres
- k = ceil(0,10 × N_sûres de G05-G20) ; positions tirées par random.Random(1676200).sample(liste ordonnée (ligne, index), k).
## Présentation au vérificateur (sous-agent Opus, sans la sortie Fable, sans nos lectures, sans clé, sans H-secret/)
- Pour chaque item : ligne Gk, demi-page probable, n° du mot, position approximative dans la ligne (%), contexte 2 lettres
  de chaque côté (lettres sûres de Fable ; lettres douteuses du contexte masquées « · » ; cible « [?] »).
- Options : EXACTEMENT 3 lettres(-chaînes) en ordre aléatoire (graine 1676201) + « autre » + « illisible ».
  Douteuses : les options de Fable (« ? » de Fable exclu), complétées par des confusables pour arriver à 3.
  Sûres : la lettre de Fable + 2 confusables. (Ainsi le vérificateur ne distingue ni sûres/douteuses ni la préférence.)
- Zones ‹…n› : lecture libre (n estimé donné), avec « illisible » permis.
## Arbitrage (ADDENDUM-2 § 3)
- Douteuse : choix du vérificateur s'il est une option de Fable ; sinon (confusable, autre, illisible) → « # » × longueur
  de la 1ʳᵉ option de Fable.
- Sûre échantillonnée : retenue si le vérificateur choisit la lettre de Fable ; sinon « # » (et compte comme désaccord).
- ‹…n› : lecture du vérificateur retenue seulement s'il la donne « sûre » ; sinon « # » × n.
- Comparaison insensible à la casse et après w=v, j=i.
## Garde-fous
- Désaccord sur l'échantillon des sûres = choix ≠ lettre de Fable (confusable, autre ou illisible) ; si > 10 % → lecture
  REJETÉE, arrêt.
- Référence G05-G20 (concaténée, normalisée : minuscules, w=v, j=i, a-z å ä ö, « # » conservé) < 300 lettres hors « # »
  → mesure IMPOSSIBLE, arrêt. Sinon référence figée par SHA-256 AVANT gel de clé et décodage de H.
