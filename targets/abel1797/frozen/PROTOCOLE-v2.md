# Protocole v2 — écrit et haché AVANT tout calcul de C02 (abel-paris-1797, 2026-10-28 ~20:45)

Remplace, pour C02, le critère de C01 (dont le résultat 0,895 / 0,621 reste acquis et publié tel quel dans le HANDOFF).

## Constat préalable (vérification des vignettes, déclaré)
Vérification en vignette puis en pleine définition de HStAS A 16 a Bü 702 Bild 16 (rapport du 22 févr. 1799) :
- passage chiffré dont les PREMIÈRES lignes portent un déchiffrement d'époque ÉCRIT AU-DESSUS de chaque ligne chiffrée
  (la ligne « Gestern theilte mir der Schweizer Gesandte » est la glose de la ligne chiffrée 1), puis des lignes
  chiffrées soulignées SANS glose ; Bild 17 : mêmes dispositifs (à trier).
- En vérifiant, j'ai lu les lignes chiffrées 1–3 de Bild 16 avec leur glose (j'y ai remarqué : le « 0 » du secrétaire
  ressemble à un 8 ; go = gestern ; 72 = o ; 81 = s ; 87 = w). Ces trois lignes sont donc EXCLUES du jeu tenu à l'écart.

## Données
- Entraînement K2 : TOUS les passages glosés de Bü 696 (Bild 7, 8, 9, 29, 30, 31, 44, 50 ; Bild 29/44/50 étaient le
  jeu tenu à l'écart de C01 : ils passent à l'entraînement, le jeu C01 étant consommé).
- Jeu tenu à l'écart (jamais transcrit) : lignes chiffrées GLOSÉES de Bü 702 Bild 16 (à partir de la ligne 4) et Bild 17.
  Si < 25 mots entièrement numériques : compléter par le premier passage glosé de Bü 702 Bild 18–39, puis Bü 699, dans
  l'ordre des Bild, avant tout score. Les lignes NON glosées ne sont pas scorées (elles sont l'objet de la lecture).
- Transcription du jeu tenu à l'écart : jetons d'abord (colonne 2), glose ensuite (colonne 3), fichier gelé (SHA) AVANT score.
  Conventions de signes identiques à C01 : σ (cercle à queue) → « o » ; cercle/zéro → « 0 » ; un « 0 » initial collé
  à un chiffre (02, 07) est transcrit tel quel ; le « 8 » ressemblant du secrétaire de 1799 est classé σ/0 ou 8 selon la forme.

## Règle « doubles écrits simples » (fixée à l'avance, appliquée PARTOUT)
Le chiffreur écrit une lettre double une seule fois (congres, desen, lasen). Donc, pour l'alignement d'entraînement
ET pour le score de la clé ET pour celui des 200 témoins : la glose est normalisée (i/j/y → i ; c/k → c ; ä/ö/ü → ae/oe/ue ;
ß → ss) puis toute suite de lettres identiques est réduite à une seule ; la lecture par la clé subit la même réduction.

## Clé K2
- Jeton numérique → lettre majoritaire dans l'alignement des mots entièrement numériques (longueur égale après la règle
  des doubles ; sinon non aligné, ignoré pour le vote). Codes alphabétiques → mot glosé. Jetons ≥ 100 → nulles si
  l'alignement l'établit (cas « Taleyrand » de Bild 29).
- K2 gelée (SHA-256 dans GEL-CLE-K2.sha256) AVANT transcription du jeu tenu à l'écart.

## Score (identique pour la clé et les témoins)
- Unité : mots entièrement numériques du jeu tenu à l'écart (nulles connues retirées, jetons inconnus → « ? »).
- Caractères : Σ max(0, |g| − lev(lecture, g)) / Σ |g| ; Mots : part des mots dont lecture = glose (après normalisation).
- Codes alphabétiques : rapportés à part (part reconnue par K2), hors critère.
- Témoins : 200 permutations des valeurs de la table numérique de K2 (graine 1799).
- SUCCÈS si car. ≥ 0,85 ET mots ≥ 0,75 ET clé > max des 200 témoins sur les deux mesures. Aucun avenant après score.

## Lecture (seulement si succès)
Passages non glosés (Bü 702 Bild 19 en entier, lignes non glosées de Bild 16–17, autres trouvés) : règle de Daniel
(≥ 95 % des mots lus par le sens ; sûrs / probables {x} / restitués [x] / irrésolus ‹…›, avec justification).
