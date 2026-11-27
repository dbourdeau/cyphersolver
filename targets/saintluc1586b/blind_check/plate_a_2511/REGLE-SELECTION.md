# Règle de sélection — planche aveugle « Saint-Luc, Brouage 1586 » saintluc1586b-2511, 25/11/2026

Écrite et hachée (REGLE-SELECTION.sha256) AVANT toute vignette. Lieux choisis sur les fichiers texte seulement :
transcription et décodage ligne à ligne de Michael Brackx (dépôt de Daniel, targets/saintluc1586b/brackx2026/, issue #90),
lectures texts/reading_f260r.md et _v.md, alignement jeton → valeur du décodeur (scripts/align.py → src/align.tsv).
Rang = rang du jeton dans la ligne de la transcription, diviseurs `/` exclus (colonne `rang` de align.tsv).

Pièce : Saint-Luc à Henri III, Brouage, juin 1586, BnF fr. 15572 f. 260r (Gallica btv1b9061879d f268, page de droite)
et f. 260v (f269, page de gauche). Images Gallica publiques (« Source gallica.bnf.fr / BnF ») ; la planche reste privée
(Brice seul) jusqu'à intégration. Travail : work/ → SPOF_2 planches-pistes-2511/saintluc1586b ; correspondance
work/prive/cle-PRIVEE.json, jamais dans la page. Export `reponses-saintluc1586b-2511.json` (téléchargé + copié + zone
copiable). Noyau : PLANCHES/_outils/planche_core.py (v2, ordre équilibré), copié tel quel. Graines 2511253 / 1586.

## Pourquoi ces questions et pas les 8 étiquettes elles-mêmes
Brackx a déjà comparé, par gabarits et planches-contacts, les jetons de chaque étiquette multivaluée regroupés par valeur
(issues #95, #99) : seules S et d se séparent. Reposer « ce 9 = n ressemble-t-il à ce 9 = g ? » mettrait deux options
jumelles côte à côte (leçon stmauris 2511). On pose donc l'autre question, que personne n'a posée : là où la lecture
exige une valeur que l'étiquette n'a PAS (9 lu q, 3 lu u, Π lu ff, ʒ lu h dans un mot douteux), le signe a-t-il été mal
étiqueté ? Les options sont des signes DIFFÉRENTS de la table, chacun à valeur unique. Une réponse « la forme de
l'étiquette » laisse tout en l'état.

## Questions (13 : 10 cibles + 3 contrôles cachés) — un signe encadré, libellés « forme 1… », aucune glose

### Groupe Q — `9` (ϙ, n/m/g) là où la lecture demande q. 3 cibles :
Q1 260v l.26 r18 (« [?consequence] ») · Q2 260v l.13 r14 (« [?quand] ») · Q3 260r l.23 r3 (« [?ce] qu'il »).
Options : `9` (260v l.6 r1 « nous », l.6 r7 « mander ») ; `###` signe q (260v l.10 r26 « quoy », 260r l.25 r24 « iusques ») ;
`9q` (260v l.5 r28 « humblement », 260v l.1 r35 « premiers »). Référence : `9`.
Effet par cible : `###` → q, le mot passe de [?] à lu avec planche (consequence, quand, ce) ; `9` ou `9q` → rien (valeur
au sens, inchangé). ≥ 2/3 `###` → hypothèse « q-sign fondu dans 9 » consignée : les autres `9` des mots [?] (liste à
tirer de align.tsv) iront dans une planche suivante ; aucune réétiquette en masse sans elle.

### Groupe U — `3` / `z3` (3 plat, m) là où la lecture demande u. 4 cibles :
U1 260v l.23 r32 (`3`, « la [?] » → guerre) · U2 260v l.20 r42 (« [?leuee] ») · U3 260v l.20 r46 (« [?du] ») ·
U4 260v l.24 r47 (« de [?uos] »).
Options : `z3` (260v l.1 r9 « maintenant », l.6 r5 « mander ») ; `z` ʒ à queue bouclée (260v l.6 r3 « nous », l.10 r27
« quoy ») ; `v` (260v l.5 r21 « humblement », l.1 r25 « murmurent »). Référence : `z3`.
Effet : `z` ou `v` → u : U1 « la guerre » (avec 9 = g, C = rr, valeurs de la clé), U2 « leuee », U3 « du », U4 « uos »
lus avec planche ; `z3` → rien (mots restent douteux ; la clé de Brackx garde 3 = m). ≥ 3/4 `z`/`v` → hypothèse
« z3 ⊃ ʒ » consignée pour les 12 autres z3/3.

### Groupe H — `z` lu m par le décodeur, h par Brackx (260r l.1 r7, « arriua [?hier] »). 1 cible : H1.
Options : `z` (mêmes exemples que U) ; `zc` ʒ à queue barrée, h (260r l.3 r5 « chalupes », l.8 r5 « pescher ») ;
`z3` (mêmes exemples que U). Référence : `z`.
Effet : `zc` → « hier » lu avec planche ; `z` → rien (choix au sens) ; `z3` → « mier », mot non lu (déclaré).

### Groupe F — `P` (Π, nul) là où la lecture demande ff (« [?affaires] », « [?affaire] »). 2 cibles :
F1 260v l.25 r2 · F2 260v l.27 r2.
Options : `Pi` ⊓ nul (260r l.8 r31, 260v l.12 r11) ; `L` ⊥ f (260r l.4 r18 « fort », 260v l.28 r17 « francoys ») ;
`pi` π/ϖ (260v l.1 r7, 260r l.4 r32 « pas »). Référence : `Pi`.
Effet : `L` → f, « afaire(s) » lu avec planche (graphie à f simple, déclarée) ; `pi` → f/s, idem si f retenu (déclaré) ;
`Pi` → rien (nul, mot reste à trou).

### Contrôles cachés (3), réponse connue (étiquette de Brackx dans un mot lu sûr), jamais exemples ni cibles,
hors lignes des cibles, à des places différentes :
- K1 (jeu Q) : `9`, 260v l.5 r4 (« donner »).
- K2 (jeu U) : `z3`, 260v l.10 r13 (« marine »).
- K3 (jeu F) : `L`, 260v l.22 r12 (« francois »).
Un contrôle raté → rien n'est intégré ; on en parle avec Brice (sauf défaut de construction démontré, consigné).

Options texte habituelles : « aucune / autre forme », « impossible à distinguer », « illisible », « pas un signe » +
remarque.

## Contrôle d'absence de sosie (avant envoi)
Sur crops/_contact.jpg : (1) options d'une même question distinctes deux à deux ; (2) les deux exemples d'une option
sont la même forme ; (3) le signe de chaque contrôle n'a de sosie que dans son option attendue. Échec → l'exemple fautif
est remplacé par le jeton suivant de même étiquette et valeur dans align.tsv (ordre page r puis v, ligne, rang), consigné
en avenant ; si `9q` est sosie de `###`, l'option `9q` est retirée du groupe Q (avenant), jamais une cible.

## Cadre
Boîte = le signe entier, voisin exclu, repérée par comptage des amas de la ligne puis vérifiée à l'œil sur la bande de
ligne. Cadre impossible (signes soudés, rang ambigu) → la question est retirée (pas de réserve), consigné.

## Gain si tout tombe bien
260v : 8 mots (consequence, quand, guerre, leuee, du, uos, affaires, affaire) sur 275 → part lue 85,1 → ≈ 88,0 % ;
260r : 2 mots (hier, ce) sur 197 → 76,1 → ≈ 77,2 %. Pas de bascule en « lu » : le blocage du profil (33,8-39,4 % des
lettres sur étiquettes multivaluées) ne bouge que de quelques jetons, sauf si une hypothèse systémique (Q, U) se confirme
dans une planche suivante.

## Copies
work/planche.html (SPOF_2) → _planches-serve/saintluc1586b-2511/planche.html et _planches-tel/69-saintluc.html.
