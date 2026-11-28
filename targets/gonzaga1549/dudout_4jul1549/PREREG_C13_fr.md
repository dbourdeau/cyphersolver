# PREREG-C13 — 1549-07-04 (Estense, Autografoteca Campori, Lettera K, Karl V, sfasc. III, cc. 40-45) — 17/11/2026, agent Opus 5.5

Écrit et haché AVANT toute vue lisible de la portion neuve (41v l. 19-31 et 42r) et AVANT toute ouverture du bas de 43v (après
« se havra de ») et de 44r. Les recadrages L19-L31 / M19-M31 de 41v existent sur SPOF_2 (faits par C12) mais n'ont pas été
ouverts ; 42r n'a jamais été téléchargé à pleine résolution (C12 : vue à 140 px seulement).

## Historique déclaré
- C12 : KB3 gelée, mesure unique sur 41v l. 1-18 (322 jetons) : M_car 0,744, témoins max 0,135 → PARTIELLE. Portion GRILLÉE.
- KB4 (ci-dessous) est apprise sur cette portion grillée. Contrôle descriptif EN-ÉCHANTILLON (même portion grillée, donc
  non probant) : M_car 0,807. On s'attend donc plutôt à PARTIELLE qu'à VALIDÉE ; on le déclare avant.

## Clé gelée : KB4.tsv (sha256 dans SHA-C13.txt)
KB4 = KB3 (KEY-C12.tsv, 107a2eea…) avec exactement trois changements, tous appris sur la portion grillée 41v l. 1-18 ↔ 43v,
comparés à la table de McBratney/Daniel (targets/gonzaga1549/mcbratney_27may1549/key_cv1549.tsv = sign_table.tsv, PR #684) :
1. `cp` = que (KB3 : nu, dérivé). Grillée ×6. McBratney/Daniel : « cslash = que » (concordant ; crédit McBratney).
2. `o-` = g (KB3 : ga). Grillée ×6 (tengays, pongan, luego, diligencia, tenga, llegada). Note de McBratney : g se trace o d'abord,
   l (`-o`) trait d'abord (concordant ; crédit McBratney).
3. Famille `E` (nouvelle) = base r : E re, E. ra (grillée ×3 et ×6-7), E- re, E: ri, Eo ro, Ep ru, E_ ra (règle du système ;
   rangée McBratney « ra re ri ro ru, g/8-foot base », g-bar re, g-1dot ra, g-2dots ri ; crédit McBratney). Conflit déclaré :
   l'unique E- grillé irait vers « ne » (vienen) ; on garde la règle (re).
Aucune autre valeur de McBratney n'est reprise. Constats grillés NON appliqués (déclarés, pour une éventuelle KB5) : `g` lu y ×4
(tengays, procureys, obra y, y en esto) contre re ailleurs ; `4` lu o ×2 (luego, obra) contre que (KB3) ; `x` lu de ×1.

## Portion neuve (tenue à l'écart)
- c. 41v l. 19-31 puis c. 42r, tout le texte chiffré, ligne par ligne, dans l'ordre ; mots en clair notés `[...]`, hors jetons.
- Attendu ≥ 300 jetons (≈ 13 + ≈ 10 lignes de 16-20 jetons). Si moins de 300 : on prend tout ce qui est chiffré et on déclare l'écart.
- Images : tuiles/recadrages IIIF natifs (curl, recette NOTES gonzaga1549 « Access »), sur SPOF_2 seulement, étude seulement, jamais publiées.
- Notation : GLYPHES.md / GLYPHES-C02 / GLYPHES-C03 + formes de T41v-arb (dont E, G, Z_, vn, o7) ; forme inconnue → libellé nouveau
  (décodé `#`) ; illisible → `?`.

## Transcription (2 passes aveugles)
- Passe A : par un SECOND sous-agent aveugle (Opus), sur les mêmes recadrages, avec pour seul étalonnage les recadrages 41v l. 1-18
  et T41v-arb.txt (grillés) ; il ne voit ni la clé, ni la référence, ni aucun décodage. Si ce sous-agent échoue, passe A par moi, déclarée.
- Passe B : par moi, SANS regarder A (fichier A non ouvert avant que B soit écrite et hachée).
- Arbitrage des écarts sur l'image, sans clair et sans décodage. `T13-arb.txt` gelé (sha256) AVANT toute ouverture du bas de 43v / de 44r
  et avant tout décodage. Accord A/B (jetons alignés) rapporté.

## Référence (déchiffrement d'époque, autre main, 43v bas → 44r)
- Texte du déchiffrement qui suit « … como se havra de » (fin de la référence C12), jusqu'au mot qui correspond à la fin du chiffre de 42r.
- Début : la queue de la l. 18 (12 jetons après `q E.`, grillés) n'est pas dans la portion ; on retire du début de la référence un
  préfixe de r × 12 lettres, r = 488/322 (taux C12), coupé à la frontière de mot la plus proche (égalité → la plus courte).
- Mots en clair internes de la copie : servent d'ancres (segments), exclus des deux côtés. Fin : si le chiffre de 42r se termine sur un
  mot en clair, la référence s'arrête au mot qui précède son correspondant ; sinon, longueur r × n (jetons du dernier segment), coupée à la
  frontière de mot la plus proche (égalité → la plus courte).
- Bloc sans correspondant dans le déchiffrement : exclu des deux côtés (déclaré). Abréviations développées comme en C12
  (q/q̃ → que, vra → vuestra, V.M./S.M. laissées), lettres incertaines notées telles quelles.

## Mesure unique
`python3 score_c13.py T13-jetons.txt REF-C13.txt KB4.tsv 1307 <segments>` (= score_c12.py : normalisation et métrique de C02,
car. = 1 − distance d'édition normalisée ; 200 témoins = permutations des valeurs de KB4, graine 1307).
- **VALIDÉE** si M_car ≥ 0,85 ET M_car ≥ témoin max + 0,30. Mots : rapportés, non décisifs.
- **PARTIELLE** si rang 1/201 mais sous l'un des seuils (livrable « read in part » seulement).
- Sinon NON VALIDÉE. Une seule mesure ; la portion est grillée ensuite.

## Ensuite
- Compte strict de Daniel : « read » seulement si ≥ 95 % des mots sont SÛRS (décision) ; sûrs + probables rapporté à part, non décisif
  sur la portion, sûrs / {probables} / [restitués] / ‹irrésolus›.
- Livraison : mise à jour de la PR #763 (dossier targets/gonzaga1549/dudout_4jul1549/), sans images, catalogue.json non touché, en anglais ;
  crédits McBratney (3 corrections ci-dessus) et WAINUT/Daniel si utilisés.
