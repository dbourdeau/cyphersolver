# Avenant C03 — écrit et haché AVANT transcription gelée et avant tout calcul (abel-paris-1797, 2026-10-28 ~21:45)

## Constat de tri (déclaré, vu en lisant les images, aucun calcul)
- Bü 699 (1798) : Bild 20, 22 et 53 emploient un AUTRE système (groupes 60–89 seulement, séparateurs « | »,
  même mot chiffré différemment : « Treilhard » = 80.70.76.75.86.74.87.69.82 au Bild 22 mais 87.65.61.83.86.60.61.67.86 au Bild 53)
  → K3 NE s'applique PAS ; ces pièces ont leur clair (glose lettre à lettre Bild 22, glose Bild 20, fiche Bild 55 pour Bild 53). Hors lecture.
- Bild 21, 48–49, 60, 61 : table K3, glosés (interlinéaire ou fiche). Hors lecture.
- **Bild 75 (12 juil. 1798), 86 (30 juil.), 90 (août)** : table K3 (groupes 1–99 + codes de 2 lettres), AUCUNE glose sur la page,
  aucune fiche vue aux Bild voisins (74 journal, 76 suite et fin de la lettre, 77 lettre suivante ; 85–87, 89–91 idem).
  En triant, j'ai vu ces lignes à l'œil et formé des hypothèses (dem, weis, Geist, Revolution, gehalten, Taleyrand, nach, Barras, Antrag) :
  le critère ci-dessous est donc un test d'APPLICABILITÉ de K3 (structure de la table), pas une validation de lecture.
- Bü 706 (Normann 1801) : groupes à 3 chiffres (100–199) massivement employés comme signifiants + gloses interlinéaires → autre table, hors K3.

## Critère d'applicabilité de K3 (fixé d'avance)
- Données : mots entièrement numériques de Bü 699 Bild 75, 86, 90 (transcription gelée, SHA, avant score).
- Modèle : bigrammes de lettres (add-one, début/fin de mot) appris sur TOUTES les gloses d'époque du dossier
  (colonne 3 des fichiers transcription/*.tsv), normalisées comme au protocole v2 (doubles simplifiés, j/y→i, k→c, umlauts).
- Mesure : log-probabilité moyenne par caractère de la lecture K3 (KEY_K3.json, inchangée ; 8→σ / 8d→0d ; « 90 » seul = und ; ≥ 100 = nulle).
- Témoins : 200 permutations des valeurs de la table numérique de K3 (graine 1799).
- K3 S'APPLIQUE si sa mesure > max des 200 témoins. Sinon : « table changée », on ne force pas, pas de lecture.
- Si elle s'applique : lecture selon la règle de Daniel (≥ 95 % des mots lus par le sens ; sûrs / probables {x} / restitués [x] /
  irrésolus ‹…›). Codes de 2 lettres absents de K3 : probables seulement si position dans l'ordre alphabétique du répertoire
  ET sens concordent ; sinon irrésolus. Aucun avenant après score.
