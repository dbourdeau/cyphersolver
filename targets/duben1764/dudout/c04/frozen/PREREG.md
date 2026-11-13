# C04 — PREREG (système B, 121-124L : valeurs irrésolues) — écrit et gelé AVANT toute résolution de valeur, 13/11/2026

## Contexte et limite déclarée
- Aucune autre portion du système B n'est disponible : 118-119R (5 oct. 1764) a servi à construire (118.00-119L.06) et à mesurer
  (119L.07-119R.05, grillée le 12/11) ; la lettre de mai 1764 (Payne, 105-108) et le 6 mars 1764 sont du système A
  (cosinus de profils de valeurs contre 121-124L : 0,108 et 0,080 ; 5 oct. contre 121-124L : 0,924).
- La portion neuve est donc prise DANS 121-124L : C = 121, 122L, 122R (695 groupes) pour dériver ; H = 123R + 124L (552 groupes) pour mesurer.
- Contamination déclarée : H a été décodé avec la clé c03b le 12/11 (lecture publiée, PR #477) et, ce 13/11 avant ce PREREG,
  un relevé des contextes des valeurs inconnues (c04/ctx_unknown.txt) incluant des occurrences de H a été affiché une fois.
  Pour limiter le biais : les valeurs N sont dérivées des seuls contextes de C (et des images de C) ; aucune ligne de H n'est
  rouverte décodée avant la mesure ; la mesure est mécanique (lexique), seuils fixés ici.

## Clé
- K0 = c03/construction/key_c03.json + c03/construction/c03b_ajouts.json (inchangés, SHA ci-dessous).
- N = c04/N_key.json : valeurs nouvelles ET corrections de valeurs de K0, dérivées de C seulement ; gelé par SHA-256
  (SHA256SUMS-N) AVANT l'exécution de la mesure. Chaque entrée justifiée dans c04/N_justif.md (contexte C).

## Mesure unique (scripts/measure_lex.py, graine 4504)
- Occurrences : chaque groupe de H dont la valeur est dans N avec une chaîne non vide.
- Coup : dans la fenêtre décodée de ±3 groupes (valeur inconnue = coupure), il existe un mot du lexique
  cyphersolver lang/lexicons/fr.json.gz (longueur ≥ 4, fréquence ≥ 2) qui couvre entièrement les lettres de la valeur.
- M = coups / occurrences.
- Témoins (400) : 200 permutations des chaînes de N entre les valeurs de N ; 200 tirages où chaque valeur de N reçoit
  une chaîne tirée au hasard parmi les chaînes de K0.
- Seuils : VALIDÉE si occurrences ≥ 12 ET M ≥ 0,60 ET M > max(témoins) ET M − moyenne(témoins) ≥ 0,25.
  Si occurrences < 12 : mesure non conduite, valeurs N restent « probables » non mesurées.
- Après la mesure, H est grillée pour toute valeur de N. Les valeurs présentes seulement dans H pourront être proposées
  ensuite par le contexte, marquées « non mesurées ».

## Lecture
- Règle des 95 % de Daniel (mots lus par le sens : sûrs + probables / mots), fiche S / {P} / [R] / ‹I›, traduction anglaise.
