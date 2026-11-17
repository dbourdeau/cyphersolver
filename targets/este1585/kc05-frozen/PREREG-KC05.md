# PREREG KC05 — test unique de la clé K-C05 sur une page NEUVE, BnF fr. 16041 f. 272 v (v553) — 17/11/2026 soir (agent Opus, accord de Brice « Tous »)

Haché (SHA-256) AVANT toute transcription et tout décodage du bloc. Prolonge PREREG-KC04 (e9d3ea33…), PREREG-KC03b (10272c72…) + AVENANT-1 KC03b (44060a11…).

## Contrôle « page neuve » (fait avant ce texte)
- Grillées : Colbert 338 V1–V5, p. 523, p. 517 L4-fin, fr. 16041 f. 271 v (KC03b), f. 272 r (KC04). f. 272 r sert d'apprentissage (DERIVATION-KC05.md).
- **f. 272 v (Gallica btv1b9060909s, vue 553, image 3948 × 5881, SHA e68f3afb…)** : jamais transcrite, jamais décodée, jamais mesurée. Vue seulement en
  réduction 600 px (mise en page, 17/11 soir) : ≈ 17 lignes chiffrées puis ≈ 6 lignes en clair (bas de page).
- Autres contributeurs (17/11) : `gh search prs/issues` « 16041 », « Este », « Villeroy 1584 » sur dbourdeau/cyphersolver → seulement nos PR #278, #557, #767 et l'issue #206 ;
  dépôt de Daniel (clone _shared à jour 17/11 14:36) : 16041 n'apparaît que dans nos fiches et dans la note Tomokiyo (« f. 259, 264, etc. », aucun clair publié).
  Chez nous : f. 272 v n'est cité que comme « non transcrit » (HANDOFF, PREREG-KC03b/KC04). Choix entre f. 272 v et f. 273 r : f. 272 v (page chiffrée plus longue ;
  f. 273 r est surtout en clair). f. 273 r ne sera pas décodée avant la mesure.

## Clé (gelée, `K-C05.tsv`)
K-C05 = K-C04 + g8 = e (au lieu de m), new4 = l, new6 = u, ß = x, sdot = m — appris sur f. 272 r après sa mesure (dérivation chiffrée dans `DERIVATION-KC05.md`).
Étalonnage sur portions VUES (informatif) : f. 272 r 0,499 (K-C04 : 0,414) ; f. 271 v 0,443 (K-C04 : 0,462). Formes absentes de la clé : sans valeur (coupure).

## Bloc de mesure
**B = tous les signes chiffrés de f. 272 v, dans l'ordre de lecture.** Lignes en clair du bas de page exclues ; mot en clair dans une ligne chiffrée → `CLAIR` (coupure).
Gloses interlinéaires : MASQUÉES sur les découpes données aux passes (repérées par la taille de l'écriture sur une réduction où elles ne sont pas lisibles) ;
non lues avant la mesure. Si B < 300 signes après retrait des séparateurs : B s'étend aux lignes chiffrées de f. 273 r (v554f), mêmes règles.

## Transcription (deux passes aveugles, par deux sous-agents)
Écart déclaré d'avance (comme KC04) : les DEUX passes sont faites par deux sous-agents AVEUGLES distincts (A et B), sans clé, sans valeurs, sans l'autre passe, sans
lecture de f. 272 r ; alphabet = `GLYPHES.md` + `FORMES-SUPPLEMENT.md` (ce dossier, hachés avec ce texte, rappels de nommage eq/tt et o/dl inclus) ; découpes de lignes
masquées sur SPOF_2 …/work/kc05/. Chaque passe hachée avant l'arbitrage. Arbitrage des seules divergences, sur l'image, par règles de FORME écrites (`ARB-REGLES.tsv`)
avant tout décodage ; `B-f272v-chiffre-sep.txt` puis `B-f272v-chiffre.txt` (sans `|`, strip_sep.py 03930a35…) gelés par SHA ; aucun décodage avant le gel.

## Mesure (une seule) : `python3 -I tools/mlex2.py K-C05.tsv B-f272v-chiffre.txt 2722`
Même métrique que KC04 : M5bi = max(M5 fr, M5 it), script identique (b57eaff9…) ; 200 témoins (valeurs d'une lettre mélangées, graine 2722).
Décision (barres de KC04, inchangées) :
- **Barre stricte (décision) : R = M5bi / 0,634 ≥ 0,85 (soit M5bi ≥ 0,539) ET M5bi ≥ témoin max + 0,30 → VALIDÉE.**
  0,634 = M5bi moyen du clair de nos lectures vues (plafond lexical, PREREG-KC04). Déclaré : aucune portion vue n'atteint R 0,85 (f. 272 r avec K-C05 : R 0,79) ; l'échec est probable.
- Barre de la lignée (rapportée) : M5bi ≥ 0,45 ET écart ≥ 0,30 → validée (lignée) ; écart ≥ 0,30 seul → PARTIELLE ; sinon ÉCHEC.
B grillée après la mesure.

## Après
Lecture de f. 272 v avec K-C05 ; compte STRICT (règle de Daniel : sûrs seuls, ≥ 95 % = read) ; tout mot qui demande une correction après la mesure = probable ;
fiche sûrs / {probables} / [restitués] / ‹irrésolus› ; traduction anglaise ; gloses transcrites après la mesure (comparaison informative). Images : source gallica.bnf.fr / BnF, jamais commitées.
