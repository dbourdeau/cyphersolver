# Règle de sélection — planche aveugle « Saint-Mauris 1548, planche F » stmauris1548-2511 (65-stmauris), 25/11/2026

Écrite et hachée (REGLE-SELECTION.sha256) AVANT toute vignette et avant tout repérage de boîte. Les lieux ci-dessous sont
choisis sur les seuls fichiers texte (fusion O5, passes A/B, ARBITRAGE.tsv d'O5 et d'O4), sans regarder les images.

Pièce : lettre de Saint-Mauris à Ferrante Gonzaga, 12 mars 1548 (cible WAINUT stmauris1548), cc. 5r-8r. Images de travail :
recadrages de lignes d'O5 (o5-2511/crops, cc. 6v-8r) et d'O4 (o4-2511/crops, cc. 5r-6r), sur SPOF_2 seulement, lus par
chemin. La page n'embarque que des vignettes data: (comme les autres planches) ; aucune image n'est copiée ailleurs ni publiée.
Correspondance : work/prive/cle-PRIVEE.json (SPOF_2), jamais dans la page. Export : `reponses-stmauris1548-2511.json`.
Noyau : planche_core.py v2 copié de osnabrueck-magdeburg-1647/planche-2511e (ordre équilibré, contrôles à des places
différentes). Graines 20261125 (questions) / 312 (options).

## 🔴 Statut : ce n'est PAS une mesure
- Les portions 5r-6r (O4) et 6v-8r (O5) sont **grillées** pour mesurer la clé. Cette planche ne mesure rien et ne change aucun
  verdict (O4 FAIL, O5 FAIL restent tels quels).
- **Une nouvelle mesure de type O5 (ou O2-O4) sur cc. 5r-8r est exclue**, quelle que soit l'issue de la planche.
- Deux usages seulement :
  (a) **corriger la liste des formes** (SIGNS.md / SHAPES-KEY-NAMES.md) AVANT tout nouveau PREREG sur une AUTRE lettre ;
  (b) **améliorer la lecture** de la lettre du 12 mars 1548, qui pourra être présentée comme « lecture avec planche »,
      **jamais comme une mesure validée**.
- **Toute valeur tirée du seul sens reste {probable}.** Une valeur n'est « avec planche » que si elle vient de la clé de
  WAINUT (wainut-key.tsv, inchangée) appliquée à un nom de forme que Brice a choisi sur la planche.

## Questions (13) — un signe encadré par question, formes seulement (aucune glose, lettre ni valeur dans la page)
Rang = rang du signe dans la ligne de la passe A (sans `.`, `/`, `(`), comme `sign_number` d'ARBITRAGE.tsv.

### Groupe I — la forme « ∞ » (fusion O5 : `tB-t1`, 95 jetons ; passe A : `dd` ; arbitre : « two small loops side by side,
no bar, no tails »). 7 cibles, réparties sur 6v-8r, toutes à désaccord simple dd/tB-t1 arbitré B, anneaux décrits « closed » ou sans
mention d'ouverture :
- I1 6v L07 rang 2 (D013) · I2 6v L13 rang 6 (D031) · I3 7r L08 rang 21 (D103) · I4 7r L22 rang 15 (D146)
- I5 7v L09 rang 16 (D186) · I6 7v L16 rang 11 (D202) · I7 8r L05 rang 3 (D242)
Réserve, dans l'ordre, si le cadre d'une cible ne montre pas exactement un signe (remplacement consigné en avenant) :
6v L10 r9, 6v L24 r8, 7r L14 r15, 7r L26 r8, 7v L03 r11, 7v L21 r19, 8r L04 r17 (on prend la 1re de la même page).
Options (5 formes de la même lettre, 2 exemples chacune, hors lignes des cibles) :
- `O` haltère, accord A/B net en Q : 7r L04 r14, 7r L09 r11.
- `dd` en arche (choix de l'arbitre O5 contre tA-t4 « two loops joined by a high arch ») : 6v L16 r9 (D043), 7r L12 r9 (D120).
- `∞` elle-même (autres lieux tB-t1 de Q) : 6v L27 r2 (D073), 7v L20 r17 (D218).
- `w` (cursive w à boucles), accord A/B net en O4 (cc. 5r-6r ; **0 `w` en Q contre 66 en O4**) : 5r L10 r11, 5v L09 r4.
- `N14` (chaîne à deux boucles « u-o »), accord A/B net en O4 : 5r L05 r12, 5v L20 r13.
Référence d'équilibrage des places : `w`.

### Groupe II — `vt` contre tA-t3 « ox » (45 désaccords tA-t3/vt, tous arbitrés vt ; la passe A n'a jamais écrit `vt` en Q).
2 cibles : V1 7r L06 rang 10 (D096) · V2 8r L02 rang 15 (D237). Réserve : 7v L17 r11, 6v L23 r5.
Options (4) : `vt` accord A/B net en O4 (5r L04 r9, 5v L05 r10) ; la forme « ox » elle-même (7r L11 r6 D113, 7v L21 r12 D223) ;
`x` accord net en Q (6v L01 r20, 7v L22 r13) ; `xo` accord net en Q (6v L03 r12, 7v L08 r11). Référence : `vt`.

### Groupe III — petite boucle à amorce en haut à gauche (tA-t1 / tB-t2, 15 désaccords ; fusion : tA-t1 16 + tB-t2 6 = 22 jetons).
1 cible : P1 7r L24 rang 9 (D151). Réserve : 7r L16 r2.
Options (3) : `N4` accord net en O4 (5r L06 r5, 5v L17 r11) ; `d` accord net en Q (6v L01 r10, 6v L14 r5) ; la forme elle-même
(6v L15 r4 D039, 7v L09 r6 D184). Référence : `N4`.

### Contrôles cachés (3), réponse connue, jamais exemples ni cibles, hors lignes des cibles
- K1 (jeu d'options du groupe I) : `w`, accord A/B net en O4, 6r L07 rang 15.
- K2 (groupe I) : `O`, accord A/B net en Q, 7v L03 rang 6.
- K3 (groupe II) : `x`, accord A/B net en Q, 8r L06 rang 2.

Options texte habituelles sur chaque question : « aucune / autre forme », « impossible à distinguer », « illisible »,
« pas un signe (tache, trait) » + champ remarque. Libellés « forme 1…5 » seulement.

## Cadre (règle 6)
Boîte = le signe entier (anneaux, amorces, queues), voisin exclu, repérée sur la ligne par comptage des signes puis vérifiée
à 4-6× ; contrôle final sur crops/_contact.jpg et sur chaque crops/qNN_signe.jpg. Un cadre impossible → lieu suivant de la
réserve. Tout recadrage après contrôle visuel est consigné en avenant (lieux inchangés).

## Ce que chaque réponse change (sur copie ; rien chez WAINUT ni Daniel sans accord de Brice)
0. **Un contrôle raté → rien n'est intégré** ; la planche est discutée avec Brice.
1. Groupe I (95 jetons `tB-t1` de la fusion O5) :
   - ≥ 6 cibles sur 7 vues **`w`** → les 95 jetons deviennent `w` → valeur **o** (clé, ligne `w`, frozen) dans la lecture avec
     planche ; SIGNS.md : la description de `w` reçoit la variante « deux anneaux accolés sans barre (∞), cc. 6v-8r ».
   - ≥ 6/7 vues **`O`** → 95 jetons `O` → **e** (clé) ; SIGNS.md : variante de `O` sans barre.
   - ≥ 6/7 vues **`dd`** → 95 jetons `dd` → **r** (clé) ; SIGNS.md : `dd` précisé (avec ou sans arche).
   - ≥ 6/7 vues **`N14`** → 95 jetons `N14` → **q** (clé, valeur ajoutée après le test de WAINUT, signalée telle).
   - ≥ 6/7 vues **la forme elle-même** ou « aucune / autre forme » → nouveau nom de forme `oo` (SIGNS.md, sans valeur) ;
     la clé n'en donne aucune : la valeur lue par le sens (o chez les deux lecteurs) reste **{probable}** pour les 95 jetons.
   - 4 ou 5 sur 7 de même forme → seuls les lieux posés sont renommés ; la classe reste `tB-t1`, à reposer.
   - < 4 sur 7, ou « impossible / illisible » majoritaire → rien ne change ; doute consigné.
2. Groupe II (45 jetons tA-t3/vt arbitrés `vt`, valeur s) : 2/2 vues **`vt`** → les 45 restent `vt` (s), confirmés avec planche,
   SIGNS.md : `vt` reçoit la variante « boucle en v liée à une croix oblique (ox) » ; 2/2 **forme elle-même** → nom `ox` sans valeur,
   les 45 jetons perdent s (sens seul → {probable}) ; 2/2 **`x`** → a (45 jetons) ; 2/2 **`xo`** → c (45 jetons) ;
   réponses partagées → seuls V1/V2 changent.
3. Groupe III (22 jetons tA-t1/tB-t2, sans valeur) : P1 vue **`N4`** → valeur m pour P1 seulement, la classe (22) est notée
   « N4 probable » pour la liste des formes, à confirmer par une planche suivante ; vue **`d`** → r pour P1 seulement, idem ;
   vue **elle-même** → nom de forme `ot` (sans valeur) ajouté à SHAPES-KEY-NAMES.md ; sens seul → {probable}.
4. Aucun changement de valeur de la clé de WAINUT ; seuls des noms de formes changent.
5. Effet attendu maximal : jusqu'à 95 + 45 + 1 jetons nommés par la clé, soit jusqu'à 95 des 215 `?` du décodage O5 comblés
   par la clé (groupe I) — lecture avec planche, sans nouveau calcul de verdict ; pourcentages éventuels donnés « pour
   information, hors protocole ».
6. Les confusions relevées par les lecteurs (b/q, q/x, u/x, l/e) ne sont pas posées ici (pas de lieu sûr sans valeur) ; à
   traiter dans une planche suivante si Brice le souhaite.
