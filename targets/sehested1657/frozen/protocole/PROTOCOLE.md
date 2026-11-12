# PROTOCOLE — Sehested, Vienne 1657 (Daniel n° 2520) — rédigé et gelé AVANT la mesure (11/11/2026, agent Opus, fil 🔓)

Hypothèse testée : les lettres chiffrées de l'unité 260651 (img 109-170) sont une substitution monoalphabétique de l'allemand
(mots séparés par la croix †, nombres séparés par « : », 90 et 96 = s), clé = protocole/CLE-132.txt, relevée par paires sur
l'interligne d'époque de img 132 et contrôlée sur img 110 ↔ clair d'époque img 112. Les signes de nomenclateur (Λ, X, XX, Σ, a, ii…)
ne sont pas comptés.

- Outils gelés (SHA dans PROTOCOLE.sha256) : scripts/mesure.py, scripts/lm_de.py, protocole/CLE-132.txt, protocole/lm_de.pkl
  (modèle de caractères d'ordre 4 sur Merian, Topographia Hassiae 1655, copie Wikisource corpus/merian_ws_1655.txt).
- Calibrage (données déjà vues, PAS la réserve) : img 110 l. 1-5, 152 nombres : M −1,774 / lexique 0,633 ; contrôles max −3,649 / 0,167.
- RÉSERVE (jamais ouverte, aucune glose vue) : **img 145, page de GAUCHE, depuis la 1ʳᵉ ligne chiffrée, lignes entières, jusqu'à
  atteindre au moins 300 nombres** (on arrête à la fin de la ligne qui franchit 300). Si img 145 portait une glose interlinéaire
  ou un clair, on prend img 146 page gauche (même règle), et on le note. Transcription chiffre par chiffre AVANT tout décodage,
  dans working/transcr/reserve_145.txt, gelée par SHA-256 (protocole/RESERVE.sha256) ; nombre illisible = « ? » (compté inconnu).
- UNE exécution : `python3 scripts/mesure.py protocole/CLE-132.txt protocole/lm_de.pkl working/transcr/reserve_145.txt > protocole/MESURE.out`
- Contrôles (graine 1657, 300 chacun) : C = étiquettes de lettres permutées entre les 23 valeurs de la clé ; D = clé aléatoire
  (lettre tirée selon les fréquences allemandes pour chaque nombre) ; E = vraie clé appliquée aux nombres de la réserve mélangés
  (longueurs de mots conservées).
- Critères chiffrés :
  C1 : score par caractère M ≥ max(C, D, E) + 0,30 ;
  C2 : taux de mots (≥ 2 lettres) au lexique Merian ≥ 0,50 ET ≥ max des contrôles + 0,25 ;
  C3 : nombres inconnus de la clé (ou « ? ») ≤ 5 % ;
  S : le déchiffrement donne au moins deux suites d'au moins 8 mots allemands lisibles.
  **VALIDÉ si C1, C2, C3 et S** ; sinon ÉCHEC, documenté dans ESSAI-OPUS.md (pas de seconde mesure sur la même réserve).
- Lecture ensuite : règle de Daniel (sûrs + probables ≥ 95 %, restitués exclus, décompte par mot chiffré), fiche par lettre.
- Aveu préalable : la clé est connue de l'agent pendant la transcription ; la transcription se fait nombre par nombre, sans
  correction « au sens » (aucune retouche après décodage ; les corrections éventuelles de lecture vont dans un fichier séparé).
