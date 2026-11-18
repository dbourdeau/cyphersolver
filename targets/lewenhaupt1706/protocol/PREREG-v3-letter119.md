# PREREG — F 470 (Alvin 634917), lettres 108 (glosée) et 119 (non glosée), 18/11/2026, fil 🔓 (agent Opus)

Écrit AVANT toute transcription et toute mesure. Haché (PREREG.sha256) avant de regarder les images 397, 399, 400.

## 0. Ce que j'ai déjà vu (déclaration d'exposition)
- RAPPORT.md de 🔎 (f470-suite-2026-11-18) ; vue d'ensemble réduite de l'image 366 (glose visible) pour estimer la mise en page.
- Pendant le contrôle d'antériorité, le fichier cle_K2.json de la série A (218 codes, v2 du 17/11) s'est affiché en entier.
  Risque de contamination de la table T108. Parade : T108 ne contient QUE des valeurs lues dans la glose de 108
  (366-367) ; aucun code de K2/K3 n'y est ajouté ; un code non glosé dans 108 reste inconnu dans T108.
- Images 397, 399, 400 (lettre 119) : JAMAIS regardées à ce stade (ni planche, ni crop c397a/c399a/c400a de 🔎).

## 1. Portion tenue à l'écart H
- H = la partie chiffrée de la lettre 119 (Altranstädt 30/4/1707), images 397, 399, 400. Aucune lettre de la série A
  ne reste neuve (L1-L4 lues ; L3 et L4 grillées le 17/11), d'où le choix de 119.
- La transcription des nombres de H est faite et gelée (SHA-256) AVANT d'appliquer T108. Le clair suédois
  intercalé dans 400 est lu comme contexte, pas compté dans la mesure.

## 2. Table T108
- Construite seulement à partir des gloses de 108 (366 gauche et droite, 367). Valeur = glose lue au-dessus du nombre.
  Gloses sûres et gloses douteuses/raturées séparées (colonne « statut »). Une glose raturée puis corrigée : la
  correction est la valeur, statut « corrigée ».
- T108 gelée (SHA-256) avant tout décodage de H. Aucune modification de T108 après le gel pour la mesure.

## 3. La mesure (une seule)
- Décodage mécanique de H par T108, puis lecture par le sens, mot à mot, en une seule passe, par moi.
- Comptage des mots de la lecture de H en quatre classes, rapportées séparément :
  - sûrs : tous les codes du mot sont dans T108 (statut sûr) et le mot est un mot suédois attesté, sans retouche ;
  - {x} probables : mot lu mais avec un code de T108 au statut douteux, ou une retouche d'orthographe d'une lettre ;
  - [x] restitués : au moins un code absent de T108, valeur restituée par le contexte (pas de retour dans T108) ;
  - ‹…› irrésolus : le reste (un bloc de codes sans sens = 1 mot irrésolu par mot estimé, estimé à 2 codes/mot).
- Grandeur décisive : P = (sûrs + {x}) / total des mots de H.
- Critère fixé avant : T108 « tient » sur la portion neuve si P ≥ 0,60. Sinon : échec, dit tel quel.
- Rapporté, non décisif : couverture mécanique (part des groupes de H présents dans T108).
- Après la mesure H est grillée. Toute amélioration ultérieure (ajout des valeurs de K3, de restitutions) = hors protocole.

## 4. Écarts déclarés aux règles permanentes (REGLES-AGENTS-VEILLE.md)
- Pas d'accord en caractères contre 200 témoins : il n'existe aucun clair de référence pour 119. La mesure est la
  lecture par le sens demandée par Brice (règle de Daniel, quatre classes). Elle est subjective : seuil et classes fixés ici.
- Pas de témoin automatique (une seule mesure annoncée, à la demande de Brice).

## 5. Ensuite (hors mesure)
- Appliquer T108 (puis T108 ∪ K3) aux lettres 82-89 (série A) et dire ce qu'elle ajoute (codes nouveaux, codes en conflit).
