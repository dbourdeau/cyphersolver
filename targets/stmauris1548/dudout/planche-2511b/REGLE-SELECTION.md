# Règle de sélection — planche aveugle « Saint-Mauris 1548, planche G » stmauris1548-2511b (68-stmauris-b), 25/11/2026

Écrite et hachée (REGLE-SELECTION.sha256) AVANT toute vignette de cette planche. Lieux choisis sur les fichiers texte (passes
A/B d'O4 et d'O5, ARBITRAGE.tsv d'O5). Suite de la planche stmauris1548-2511 (K1 levé par Brice le 25/11 ; intégration :
planche-2511/integration/INTEGRATION-2511.md). Brice : « Lève k1 et intègre et si nécessaire refais des planches ».

Pièce : lettre de Saint-Mauris à Ferrante Gonzaga, 12 mars 1548, cc. 5r-8r. Images : recadrages de lignes d'O4 (5r-6r) et
d'O5 (6v-8r), SPOF_2 seulement, lus par chemin. La page n'embarque que des vignettes data: ; elle va à Brice seul.
Correspondance : work/prive/cle-PRIVEE.json (SPOF_2), jamais dans la page. Export : `reponses-stmauris1548-2511b.json`
(téléchargé + copié + zone de texte copiable, pour le téléphone). Noyau : planche_core.py v2 de planche-2511 (inchangé).
Graines 2511252 (questions) / 3122 (options).

## 🔴 Statut : PAS une mesure
Comme 2511 : cc. 5r-8r grillées ; aucune mesure, aucun verdict changé (O4, O5 FAIL). Usages : (a) liste des formes
(SIGNS-ajout-2511.md) pour un PREREG sur une autre lettre ; (b) lecture « avec planche » du 12/3/1548. Une valeur n'est
« avec planche » que si elle vient de la clé de WAINUT (inchangée) appliquée à un nom de forme choisi par Brice.

## Leçon de 2511 appliquée : pas d'option jumelle
- Plus d'option « la forme elle-même » à côté d'une forme de clé qu'elle pourrait reproduire : l'alternative est
  « aucune / autre forme » (+ remarque).
- **Contrôle d'absence de sosie, après construction et avant envoi** : sur crops/_contact.jpg et chaque vignette,
  l'orchestrateur vérifie que (1) les options d'une même question sont visuellement distinctes deux à deux, (2) les deux
  exemples d'une option sont la même forme, (3) le signe de chaque contrôle n'a de sosie que dans son option attendue.
  Un échec → l'exemple ou le contrôle fautif est remplacé par le lieu suivant de la même liste (avenant), jamais une cible.

## Questions (12) — un signe encadré par question ; libellés « forme 1… » ; aucune glose, lettre ni valeur dans la page
Rang = rang dans la ligne de la passe A (sans `.`, `/`, `(`), comme `sign_number` d'ARBITRAGE.tsv.

### Groupe V — `vt` contre « ox » (tA-t3, 45 désaccords tA-t3/vt arbitrés vt). 4 cibles :
V1 7r L06 r10 (D096) · V2 8r L02 r15 (D237) · V3 7v L17 r11 (D205) · V4 6v L23 r5 (D061).
Options (3) : `vt` accord A/B O4 (5r L04 r9, 5v L05 r10) ; `x` accord Q (6v L01 r20, 7v L22 r13) ; `xo` accord Q (6v L03 r12,
7v L08 r11). Référence : `vt`.
Effet : ≥ 3/4 `vt` → les 45 jetons restent `vt` (s), confirmés avec planche ; SIGNS-ajout : variante « ox » de `vt` établie.
≥ 3/4 « aucune / autre forme » → nom `ox` sans valeur ; les 45 jetons perdent s dans la lecture (sens seul → {probable}).
≥ 3/4 `x` → a ; ≥ 3/4 `xo` → c (45 jetons). Sinon → seuls les lieux posés changent ; classe inchangée.

### Groupe N — petite boucle fermée à amorce en haut à gauche (tA-t1/tB-t2, 22 jetons, sans valeur). 4 cibles :
N1 7r L24 r9 (D151) · N2 7r L16 r2 (D130) · N3 6v L15 r4 (D039) · N4c 7v L09 r6 (D184). (N3 et N4c ont servi d'exemples en
2511 : déclaré.)
Options (4) : `N4` en boucle en v / D ; `N4` en anneau rond ; `d` accord Q (6v L01 r10, 6v L14 r5) ; `a` accord Q (6v L04 r7,
6v L12 r2). Les exemples `N4` : les 26 lieux accord A/B d'O4 (`5r L01 r3, 5r L03 r3, 5r L04 r14, 5r L05 r18, 5r L06 r5,
5r L08 r11, …` liste de cand.py) sont parcourus dans cet ordre ; chacun est classé à l'œil « v/D » ou « rond » sur son seul
recadrage d'exemple (jamais sur une cible) ; on prend les 2 premiers de chaque sous-forme ; classement consigné en avenant.
Référence : `N4` v/D.
Effet : ≥ 3/4 `N4` (l'une ou l'autre sous-forme, même valeur) → les 22 jetons deviennent `N4` → **m** (clé) ; SIGNS-ajout :
variante établie. ≥ 3/4 `d` → r ; ≥ 3/4 `a` → i (22 jetons). ≥ 3/4 « aucune » → nom `ot` sans valeur. Sinon → seuls les lieux posés.
Sous-question (liste des formes seulement) : si Brice déclare « N4 v/D = N4 rond » ou non, consigné sans effet de valeur.

### Groupe P — le contre-exemple « Piemont » (6v L15, `sq ∞ O tA-t1 N3 x: 3o` = p?e?ont). 1 cible :
P1 6v L15 r2 (D038, ∞ nommé `w` depuis l'intégration 2511, ce qui donne « poe… »).
Options (3) : `w` accord O4 (5r L10 r11, 5v L09 r4) ; `a` accord Q (6v L04 r7, 6v L12 r2) ; `O` accord Q (7r L04 r14, 7r L09 r11).
Référence : `w`. Effet : `w` → reste o (« Poemont » : graphie ou faute du chiffreur, mot irrésolu, déclaré) ; `a` → i (P1 seul,
« Piemont » lu avec planche) ; `O` → e ; autre → rien.

### Contrôles cachés (3), réponse connue, jamais exemples ni cibles, hors lignes des cibles, à des places différentes
- K1 (jeu V) : `x`, accord A/B Q, 6v L26 r5.
- K2 (jeu N) : `d`, accord A/B Q, 6v L18 r17.
- K3 (jeu P) : `O`, accord A/B Q, 6v L05 r11.
Un contrôle raté → rien n'est intégré ; on en parle avec Brice (sauf défaut de construction démontré, consigné).

Options texte habituelles sur chaque question : « aucune / autre forme », « impossible à distinguer », « illisible »,
« pas un signe (tache, trait) » + champ remarque.

## Cadre
Boîte = le signe entier, voisin exclu, repérée par comptage des amas (locate.py) puis vérifiée ; contrôle final sur
crops/_contact.jpg. Cadre impossible → cible suivante de la réserve : V : 7v L17 r18 (D207) ; N : aucune (question retirée).

## Copies
work/planche.html (SPOF_2) → _planches-serve/stmauris1548-2511b/planche.html et _planches-tel/68-stmauris-b.html ; à Brice seul.
