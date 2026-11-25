# INTEGRATION-2511 — planche aveugle stmauris1548-2511 (65-stmauris), réponses de Brice — 25/11/2026, Claude Opus 5.5 (fil 🔓)

## ⚠️ AVENANT 25/11 ~20 h 30 — K1 levé, intégration APPLIQUÉE (le texte d'origine suit, inchangé)
- **Décision de Brice** (relayée par le coordinateur, ses mots) : « Lève k1 et intègre et si nécessaire refais des planches […] ». K1 raté **par défaut de construction** (option jumelle ∞ / w, §3.1) ; **levé sur décision de Brice** ;
  K2 et K3 réussis.
- **Appliqué** : groupe I → les 95 jetons tB-t1 (« ∞ ») sont nommés **`w`** → **o** (clé WAINUT inchangée), « avec planche ».
  Groupes II (vt/ox) et III (N4 / boucle à amorce) **restent non concluants** → reposés en planche **stmauris1548-2511b**.
- **Recompte appliqué** (lecture seulement ; O5 reste FAIL, aucun verdict changé, aucune mesure) : `recompte_planche.py`
  → `recompte-planche.json`, `LECTURE-L1-avec-planche.txt`, `LECTURE-L2-avec-planche.txt`, `DECODE-O5-avec-planche.txt`
  (1 741 car., 120 ?), `transcription_1548-03-12_Q_avec-planche.txt` (95 tB-t1 → w, rien d'autre). Chiffres = tableau §6 :
  L1 S 255 / P 52 / R 15 / I 58, lus 0,847, restitués 0,040 ; L2 S 261 / P 50 / R 11 / I 69, lus 0,824, restitués 0,028.
  Les fichiers « conditionnels » restent comme trace.
- **Conflit [pIeMont] traité à l'image** (6v L15 r2, D038 ; zooms sur SPOF_2 seulement, planche-2511/integration-tmp/) : le
  signe de r2 est le même ∞ (petite hampe à gauche, deux anneaux, sans barre) que celui de r9 qui donne « pour » dans la même
  ligne ; ce n'est pas le `a` (α) qui vaut i. Avec la planche, la clé donne « poe?ont » (r4 = tA-t1, la boucle à amorce, à la
  place du m). Le mot passe **irrésolu** ‹poe?ont› dans les deux lectures (une majuscule ne remplace jamais une lettre du
  décodage) ; « Piemont » reste lisible par le sens seulement. Graphie ou faute du chiffreur probable ; **reposé en 2511b (P1)**.
  Aucun mot sûr cassé.
- Indice pour le groupe III (hors règle) : tA-t1 est à la place du m dans « p?e?ont » (6v L15) et « ?ied?ont » (6v L21).
- SIGNS.md : toutes les copies sont figées par un SHA de PREREG (o5-2511/input/SIGNS.md 678be0a4…) → ajouts écrits dans
  `../../SIGNS-ajout-2511.md` (section « ajout 25/11 après O5, pour un futur PREREG sur une autre lettre »).
- Planche suivante : `../../planche-2511b/` (REGLE-SELECTION.md 1fe966ee…, hachée 20:25:36 avant toute vignette).

---

**Résultat d'origine (avant l'avenant) : RIEN N'EST INTÉGRÉ.** Le contrôle caché K1 (q03) est raté au sens de la règle (REGLE-SELECTION.md §0 :
« Un contrôle raté → rien n'est intégré ; la planche est discutée avec Brice »). Ce raté s'explique par un **défaut de
construction** de la planche (voir §3), pas par un manque d'attention. Tout ce qui suit sous « conditionnel » est une
information pour la discussion avec Brice, rien n'est appliqué. Aucun verdict ne change (O4 FAIL, O5 FAIL) ; aucune mesure
nouvelle ; clé de WAINUT inchangée ; SIGNS.md / SHAPES-KEY-NAMES.md non modifiés.

## 1. Vérifications préalables
| objet | SHA-256 | état |
|---|---|---|
| REGLE-SELECTION.md | 91feba569c660f9ea5016d3472c9afd1ae14be64ee28e6e3a671e6f4f0090d3c | = REGLE-SELECTION.sha256 ✔ |
| reponses/reponses-stmauris1548-2511.json (export 18:57:24Z) | 8956a94b05a19bb7f712f2e71fe498ccf364d8a41c2d4882eb05825d79dc05de | = attendu et .sha256 ✔ |
| work/prive/cle-PRIVEE.json (SPOF_2, via le lien `work`) | cede47b5763154534934c0e009f2761d9f5840cbe9e4a5ee4a0874bc20383b49 | = work/SHA256SUMS ✔ (planche.html et 7 scripts OK aussi) |
| planche.html | 9b71bb3b… | ne contient pas la correspondance (0 occurrence de « forme »/clé) ✔ |

`../RULES-AGENTS.md` : absent. Vignettes : 9 fichiers par forme d'exemple, **aucun fichier partagé entre deux formes
différentes** (SHA des recadrages) : pas de vignette en double au sens fichier.

## 2. Contrôles cachés (étape 1)
| q | code | attendu | choix de Brice | résultat |
|---|---|---|---|---|
| q03 | K1 (`w`, 6r L07 r15, O4) | forme 4 = `w` | forme 3 = `∞` (tB-t1) | **RATÉ** |
| q04 | K2 (`O`, 7v L03 r6) | forme 1 = `O` | forme 1 | réussi |
| q08 | K3 (`x`, 8r L06 r2) | forme 2 = `x` | forme 2 (remarque : « forme 3 et 4 sont les mêmes » = ox/vt) | réussi |

→ §0 de la règle appliqué : **aucune intégration**.

## 3. Défauts de construction révélés par les remarques
1. **`∞` et `w` sont la même forme sur la planche.** Brice : q01 « f3 = f4 » (∞ = w), q02 « f1 = f3 » (w = ∞). Vu par
   l'orchestrateur sur les vignettes (lecture seule, SPOF_2) : les exemples `w` d'O4 (5r L10 r11, 5v L09 r4) et les exemples
   `∞` de Q (6v L27 r2, 7v L20 r17) sont le même signe (hampe gauche + deux anneaux accolés, sans barre). La planche
   proposait donc deux options identiques dans le jeu du groupe I, et le contrôle K1 (`w`) avait un jumeau parmi les options :
   **K1 n'était pas discriminant.** Le constat de repérage noté à la construction (« la forme ∞ = le `w` des passes O4 »)
   annonçait ce risque ; il aurait fallu ne garder qu'une des deux options ou prendre K1 dans une autre forme.
2. **`ox` et `vt` sont la même forme sur la planche** (q08 f3 = f4, q10 f3 = f4, q11 f1 = f3) : même défaut dans le jeu du
   groupe II (le contrôle K3 = `x`, distinct, n'en souffre pas).
3. **Exemples `N4` hétérogènes** (q06, remarque « forme 1 a deux formes différentes dont une comme forme 3 ») : vu sur les
   vignettes, `N4` ex. 1 (5r L06 r5) = boucle en v à amorce, identique aux exemples de la forme « elle-même » (tA-t1/tB-t2) ;
   `N4` ex. 2 (5v L17 r11) = anneau rond fermé. Un des deux lieux « accord A/B net » d'O4 est donc soit une variante, soit un
   nom erroné dans les passes O4.
4. Cadres : un seul signe par cadre sur les 13 vignettes-cibles (planche-contact) ; pas de défaut de cadre relevé.

## 4. Décisions par question — application de la règle, À TITRE CONDITIONNEL (non appliquées, K1 raté)
Remarques « f_a = f_b » traitées comme demandé : options identiques menant à des valeurs différentes → non concluant pour
cette distinction ; même valeur → retenue.

| q | cible | choix | remarque | lecture conditionnelle |
|---|---|---|---|---|
| q13 | I1 6v L07 r2 | `w` | — | w |
| q05 | I2 6v L13 r6 | `∞` | — | ∞ |
| q01 | I3 7r L08 r21 | `∞` | ∞ = w | ∞≡w |
| q09 | I4 7r L22 r15 | `∞` | — | ∞ |
| q07 | I5 7v L09 r16 | `w` | — | w |
| q12 | I6 7v L16 r11 | `∞` | — | ∞ |
| q02 | I7 8r L05 r3 | `∞` | w = ∞ | ∞≡w |
| q11 | V1 7r L06 r10 | `ox` | vt = ox | non concluant (vt → s / ox → sans valeur) |
| q10 | V2 8r L02 r15 | `ox` | vt = ox | non concluant (idem) |
| q06 | P1 7r L24 r9 | « elle-même » (`ot`) | un exemple `N4` = `ot` | non concluant (N4 → m / ot → sans valeur) |

- **Groupe I** : lecture littérale de la règle = 5/7 `∞` + 2/7 `w` → case « 4 ou 5 sur 7 » (seuls les lieux renommés, classe
  à reposer). Avec les remarques : les deux options sont une seule forme → **7/7 ∞-ou-w**. Les deux branches donnent la
  même lettre **o** (w = o dans la clé ; ∞ lu o par les deux lecteurs), mais pas le même statut : `w` = valeur de clé
  (« avec planche »), `∞` seul = {probable}. Le passage au statut « clé » suppose de nommer ces 95 jetons `w`, ce que les
  remarques de Brice soutiennent ; **décision réservée à Brice** à cause de K1.
- **Groupe II** : non concluant ; les 45 jetons restent comme dans la fusion O5 (`vt`, s) — statu quo, rien de changé.
- **Groupe III** : non concluant pour P1 ; aucun nom `ot` ajouté. Observation : dans le décodage O5, `c??pte` (6v L02) a
  tB-t1 puis tB-t2 et les deux lecteurs y lisent « coMpte » : compatible avec `N4` = m, à poser dans une planche suivante.

## 5. La forme « ∞ » (95 jetons tB-t1 de la fusion O5)
Ce que la planche établit : **`∞` n'est ni le `O` haltère, ni `dd`, ni `N14`** (0 choix sur 7 cibles ; K2 `O` bien reconnu) ;
**elle est la forme `w`** de SIGNS.md/O4 (« small cursive w with loops ») telle que tracée dans cc. 5r-8r — Brice déclare les
deux options identiques (q01, q02) et a lui-même classé un `w` de contrôle comme ∞. Ce n'est donc pas une variante de `O`
(hypothèse de RESULTAT-O5, à corriger) ni une forme propre : c'est `w`, que les passes d'O5 n'ont jamais nommé (0 `w` en Q
contre 66 en O4). Formellement non intégré (K1).

## 6. Effet sur la lecture d'O5 — recompte CONDITIONNEL (si Brice lève K1 et nomme les 95 ∞ `w` = o)
Outil : `recompte_conditionnel.py` (SHA 012114ea…), sorties `recompte-conditionnel.json` (9ac63a18…),
`LECTURE-L1-conditionnelle-inf-w.txt` (afb8967e…), `LECTURE-L2-conditionnelle-inf-w.txt` (5e0e070d…). Décodage O5 reproduit
à l'identique avant substitution (assertion). Règles : majuscule O posée sur un ∞ → lettre du décodage ; autre majuscule sur
un ∞ → conflit, mot irrésolu ; irrésolus et nulles non relus ; reclassement mécanique (règles de check_lecture_o5.py).

| | sûrs | probables | restitués | irrésolus | total | lus | restitués |
|---|---|---|---|---|---|---|---|
| L1 O5 | 193 | 95 | 35 | 57 | 380 | 0,850 | 0,092 |
| L1 conditionnel | 255 | 52 | 15 | 58 | 380 | 0,847 | 0,040 |
| L2 O5 | 201 | 93 | 29 | 68 | 391 | 0,826 | 0,074 |
| L2 conditionnel | 261 | 50 | 11 | 69 | 391 | 0,824 | 0,028 |

- `?` du décodage : 215 → 120. Les lecteurs avaient posé O sur 78 (L1) / 73 (L2) des 95 ∞ : tous confirmés par la clé ;
  78 / 74 mots reclassés vers le haut (ex. font, anglois, escosse, loing, auoit, courir P→S ; coMpte R→P).
- **Un conflit** dans chaque lecture : `[pIeMont]` (le lecteur met I sur un ∞) → irrésolu : ce n'est pas un mot sûr cassé
  (il était restitué), mais c'est un contre-exemple (à revoir : ∞ mal nommé à cet endroit, ou graphie).
- Aucun mot sûr cassé. La part « lus » ne bouge pas (−0,003) : la planche change la *qualité* (sûrs +62/+60, restitués
  sous 5 %), pas la couverture ; les irrésolus restants tiennent aux 120 autres `?` (`n` ×27, tA-t8/tB-t7, etc.).
- Information hors protocole : pas une mesure, aucun verdict ; O5 reste FAIL ; rien appliqué tant que K1 n'est pas tranché.

## 7. SIGNS.md pour un futur PREREG (autre lettre)
Oui, cela le justifie, **sans dépendre du verdict de la planche** : la correction de la liste des formes est figée avant toute
vue de la nouvelle lettre. Proposition (non écrite, à valider par Brice) :
- `w` : ajouter « tracé aussi comme deux anneaux accolés sans barre, petite hampe à gauche (∞), surtout cc. 6v-8r » ;
  préciser contre `O` (barre horizontale) et `dd` (arche haute).
- `vt` : ajouter la variante « boucle fermée liée à une croix oblique (ox) ».
- `N4` : décrire la boucle en v à amorce en haut à gauche (forme tA-t1/tB-t2) comme variante probable, à confirmer.
- Prochaine planche (si Brice le veut) : une seule option par forme jumelle, contrôles pris hors des paires suspectes ;
  N4 vs `o` rond ; ∞ de 7r L24 « Piémont ».

## Ce qui n'a pas été fait
Rien intégré, rien modifié dans o5-2511, SIGNS.md, SHAPES-KEY-NAMES.md, la clé ou chez WAINUT/Daniel. Vignettes regardées sur
SPOF_2 seulement (aucun recadrage, aucune image copiée hors SPOF_2). Pas de mail, navigateur, push, PR ni publication.
