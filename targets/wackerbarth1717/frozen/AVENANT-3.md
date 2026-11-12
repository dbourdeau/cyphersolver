# Avenant 3 au PROTOCOLE (11/11/2026, soir, agent Opus 5.5, fil 🔓) — condition de lecture de la Relation XXII
Figé par SHA-256 (`AVENANT-3.sha256`) AVANT toute lecture nouvelle : avant le relevé de 0094–0099, avant tout décodage
de 0092–0099 et avant toute lecture par le sens. Le PROTOCOLE, l'Avenant 1, l'Avenant 2 et l'Avenant 2-bis restent valables
sauf la règle §5 de l'Avenant 2, remplacée ici pour la seule Relation XXII.
🔴 Images InC (Dresde) : recherche privée, jamais republiées. 🔴 A.-S. Rous (Tartu) travaille sur ce corpus : toute lecture
est une découverte simultanée, à nommer avec son rapport (dspace.ut.ee, item 3b294689-0a66-4b84-80f3-f3d2ab78f45d).

## 1. Décision (citée)
Brice Dudout, 11/11/2026 au soir, sur la proposition (1) d'ESSAI-OPUS.md : « wackerbarth, vas y ton conseil ».
Le conseil retenu : **le test B' (portion neuve 0091, critère L7 étalonné, z = 11,5, gap 0,74) est accepté SEUL comme
condition de lecture de la Relation XXII**, à deux conditions :
- (a) la lecture par le sens selon la règle de Daniel (sûrs + probables ≥ 95 %) sert de **contrôle final** : en dessous de
  95 %, la Relation XXII est une lecture partielle, non proposée comme déchiffrement ;
- (b) **l'échec de A' et le fait que cette décision a été prise APRÈS la mesure** sont déclarés en clair partout (fiches,
  résumé, HANDOFF, PR-DRAFT).

## 2. Déclaration : décision post hoc
- La règle §5 de l'Avenant 2 exigeait A' (VALIDÉ ou PARTIEL) ET B' VALIDÉ. La mesure unique (`MESURE2.json`) a donné
  **A' ÉCHEC** (exactA 0,3385 ; marge 0,210 < 0,30) et **B' VALIDÉ** (z 11,54 ; gap 0,742 ; score 0,6453). Cette règle,
  appliquée telle quelle, interdisait la lecture. Le présent avenant la change APRÈS avoir vu les deux résultats : c'est
  une décision post hoc, et elle est présentée comme telle.
- Pourquoi A' est écarté comme condition (diagnostic après la mesure, ESSAI-OPUS.md) :
  1. **A' manquait de données d'apprentissage** : retirer la lettre de vérité (28/05, 0057–0061) laissait 476 groupes
     français glosés ; la clé b en sortait avec des valeurs fausses ou absentes sur des nombres fréquents (23, 44, 13/15,
     33, 34) et sans nomenclateur 170 / 217 / 292 ;
  2. **son seuil n'était pas étalonné** : 0,60 de mots exacts et 0,30 de marge ont été fixés sans calcul, alors que B'
     a été étalonné sur l'apprentissage ; l'exactitude mot à mot punit chaque lettre fausse et chaque abréviation de
     glose (« S. M. », « Mr. », « St. », « Angl. ») ;
  3. il n'existe pas d'autre vérité terrain glosée ≥ 300 groupes en S1 (la feuille 0042–0043 est grillée) : refaire A'
     proprement est impossible dans ce volume.
- Ce qui reste établi sans la décision : B' montre, sur une portion neuve et avec un critère étalonné d'avance, que la
  clé c rend du français séquentiel sur la Relation XXII. La lecture par le sens est le contrôle de ce qui est lu.

## 3. Règles de la lecture (inchangées par rapport à l'Avenant 2 §5, précisées)
- Clé : `KEY-W1717c.tsv` (sha256 3322ae87…c49c), telle que gelée. Les valeurs manquantes du nomenclateur (nombres absents
  de c) restent des **trous** ‹n›, jamais devinés comme valeurs de clé ; une restitution par le sens est marquée [x] et
  comptée hors des sûrs/probables.
- Relevés 0094–0099 : faits AVANT tout décodage, sans corriger d'après le sens, puis gelés (`releves/R22b.sha256`). Une
  lecture qui suggère une autre lecture d'un nombre est notée dans la fiche (« relevé N, sens suggère M ») et n'est
  jamais reportée dans le relevé gelé.
- Classement des mots (règle de Daniel) : **sûrs** (décodage direct par c, mot attesté) ; **probables {x}** (une lettre
  d'écart sur un homophone de sûreté « probable » ou une lecture N/M? du relevé) ; **restitués [x]** (lettres comblées
  par le sens, trou de clé) ; **irrésolus ‹…›**. Taux = (sûrs + probables) / mots du chiffre. Seuil 95 %.
- Une fiche `LECTURE-*.md` par lettre (Relation XXII d'abord, 0089–0099 ; puis autres lettres S1 non glosées de mars–juin
  si relevées), avec sûrs/probables/restitués/irrésolus et justifications, + `RESUME-HISTORIQUE.md`.
- Les corrections de valeurs de c suggérées par la lecture sont listées à part (KEY-W1717d éventuelle), jamais rétroactives
  sur MESURE2.
- Les autres lettres (hors Relation XXII) ne sont couvertes par B' que par extension (même système S1, même clé) : leurs
  fiches le disent.
- S2/K0 (nov.–déc.) : décodage par K0 hors mesure, constat seulement.

## 4. Suites
- Relation XXII ≥ 95 % → `PR-DRAFT/` préparé pour Daniel (texte et clé seulement, aucune image), NON ouvert ; Rous citée
  comme découverte simultanée ; avenant post hoc et échec de A' déclarés.
- < 95 % → lecture partielle expliquée, pas de PR-DRAFT.
- Rien publié ; pas de PR, pas de mail, pas de navigateur, pas de rm. Écarts → HANDOFF.md (ajout seulement).
