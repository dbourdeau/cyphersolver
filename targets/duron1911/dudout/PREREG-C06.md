# PREREG-C06 (12/11/2026, agent Opus, fil 🔓) — 18.1777.1-6 (Durón), 17.1648.2-3 (Gabriel), 14.1354.1 (Luque)
# Écrit et gelé (protocole/PREREG-C06.sha256, avec scripts/measure_c06.py) AVANT tout décodage de ces trois pièces
# dans cette session. Transcriptions gelées : T-sanantonio-durón-v1.txt (100db048…, C01, revérifiée sur l'image ce jour,
# aucune différence) ; T-c06-luque.txt (11a686d1…).

## Ce qui est déjà su (C01) — biais déclaré
- C01 a passé les fiches 1557.1 (lettres) sur 1777.1-6 et 1648.2-3 par la sélection « car » : meilleurs 0,298 / 0,325
  (Herrera Moreno), aucune retenue ; « pas de Caesar sur l'alphabet de 1777.2-6 » pour 1777.1-6. Rien n'a été lu.
- Vu ce jour avant ce gel : lettres et fréquences seulement (IC Durón 0,076 avec « ll » = 1 signe, 107 signes, 18 lettres
  dont aucune de a b o p q s u z ; IC Gabriel 0,070, 76 lettres). Ces IC sont ceux d'une SUBSTITUTION simple ; une
  transposition (grille 8×8 de C04) garderait les fréquences espagnoles (a, o, s absents ici) → grille exclue sans essai.
- Pièce sœur : 1777.2-6 (« Elisa », 4:21 pm, 97 signes) N'EST PAS le même télégramme que 1777.1-6 (Durón, 9:10 pm,
  n° 428, 115 lettres) : contenus de longueurs différentes, heures et numéros différents. Aucun déchiffrement d'époque de
  1777.1-6 dans le dossier 1777 (3-6 = avis de non-remise, 4-6 et 5-6 = Herrera Moreno). Le « Tema » de la fiche CEHM de
  1777.1-6 est celui du dossier.

## Matériel trop court : déclaration
Durón 107 signes, Gabriel 76 lettres codées, Luque 44 nombres. Aucune portion tenue à l'écart de ≥ 300 lettres n'est
possible (ni par pièce, ni ensemble : 183 lettres). **Déclaré d'avance : aucune lecture de C06 ne peut être VALIDÉE ;
toute lecture compte au mieux « read in part », sans validation**, quelle que soit la qualité apparente.

## Étape 1 — clés d'archive telles quelles (mesure descriptive unique : scripts/measure_c06.py, une exécution)
- Familles : décalage « Elisa » ±10 sur 28 signes (a…l ll m n ñ o…z) ; fiches .tsv de cle/ (fwd/rev) ; tableaux
  .tab.json de cle/ (dont G.A.) en RC et CR, paires par groupe ou groupes réunis (C04). Aucune case corrigée.
- W = part des lettres décodées couvertes par des mots d'un lexique (1795.1 OCR + clair d'époque C03 + 40 mots-outils),
  segmentation optimale, mots ≥ 2 lettres. Témoins : 200 substitutions aléatoires, chacune maximisée sur autant de
  variantes que de clés essayées (graine 1462). « APPLIQUE » si W ≥ 0,60 ET W − ctrl_max ≥ +0,25 ; sinon « ne s'applique
  pas ». Sortie brute : protocole/MESURE-C06.txt. Aucune seconde exécution.
- Ce verdict identifie une clé ; il ne VALIDE pas (matériel < 300).

## Étape 2 — si aucune clé d'archive ne s'applique : cryptanalyse (clé construite SUR le texte)
- Substitution simple (signes « ll » regroupés ou non ; alphabets 26/27/28 ; décalages, alphabets à mot-clé, puis
  substitution générale par recuit sur trigrammes de 1795.1). Clé construite sur tout le texte : aucune mesure, statut au
  mieux « read in part », non validé. Critère d'échec fixé d'avance : si moins de 50 % des signes donnent des mots espagnols
  plausibles en contexte (après relecture), échec Opus → OPUS-ESSAI-C05.md + paquet Fable lot 8 (non envoyé).

## Étape 3 — 14.1354.1 (code numérique)
- Les fiches numériques 1557.1 (vues 1, 2, 3, 20, 21, 24, 25) seront transcrites AVANT d'y chercher un seul nombre de
  Luque (gel SHA-256), puis appliquées telles quelles. « S'applique » si ≥ 70 % des 44 nombres sont dans la table ET que
  la phrase obtenue est grammaticale autour du clair (jugement déclaré, non mesuré). Sinon : non lu (un code de 150
  mots sur 44 occurrences est insoluble sans la table) ; noter seulement les identifications contextuelles probables.

## Compte
Règle de Daniel (95 %, mots) pour chaque pièce ; S/P/R/I déclarés ; aucune publication tant que non validé, sauf
décision de Brice.
