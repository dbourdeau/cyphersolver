# Règle de sélection — planche aveugle « Saint-Luc 1586, planche B » saintluc1586b-2511b, 25/11/2026

Écrite et hachée (REGLE-SELECTION.sha256) AVANT toute vignette de cette planche. Suite de saintluc1586b-2511 (intégration :
../planche-2511/integration/INTEGRATION-2511.md ; 3/3 contrôles). Consigne de Brice (25/11) : « l'alphabet n'était pas
complet » → pour chaque question, toutes les formes plausibles de la table de Brackx + les deux variantes qu'il a décrites
(« q avec 2 barres », « hampe avec un drapeau triangle »), exemples pris hors cibles, sans jumelle, 3 contrôles cachés.

Images Gallica (f268 = 260r, f269 = 260v), privées jusqu'à intégration. Travail : work/ → SPOF_2 planches-pistes-2511/
saintluc1586b-b ; clé work/prive/cle-PRIVEE.json. Noyau planche_core.py v2 inchangé. Graines 2511254 / 1587.
Rang = rang de align.tsv (transcription de Brackx, diviseurs exclus). Repérage des variantes : recherche par gabarit
(scripts/scan.py, NCC) sur les deux pages, pics vus à l'œil ; seuls trouvés hors cibles : ϙ à deux barres 260v l.3 r20
(étiqueté t2 par Brackx) ; hampe à drapeau 260v l.9 r2 et l.9 r35 (étiquetés v).

## Famille Q (« q à 2 barres ») — 3 cibles, les mêmes qu'en 2511 (Brice les a vues : déclaré)
Q1 260v l.26 r18 · Q2 260v l.13 r14 · Q3 260r l.23 r3.
Options (6) : `9` ϙ (260v l.6 r1, l.6 r7) ; `###` (260v l.10 r26, 260r l.25 r24) ; `q` ꝗ (260v l.5 r27, 260r l.1 r15) ;
`t2` ‡ (260r l.1 r20, l.1 r32) ; `tt` ŧ̶ (260r l.1 r16, l.1 r30) ; `Q2B` ϙ à deux barres (260v l.3 r20, seul exemple hors
cible). `9q` exclu (sosie de `9`, avenant 1 de 2511). Référence : `9`.
Effet par cible : `Q2B` → étiquette nouvelle « Q2B » (4 jetons : Q1-3 + v.3 r20), valeur q PROPOSÉE (3 lieux suivis de ʒ = u :
consequence, quand, ce qu'il), mots lus « avec planche, valeur au sens » (à déclarer à Daniel, pas une valeur de clé
attestée) ; `###` → q (clé) : mot lu avec planche ; `9` → rien ; `q` ou `t2` ou `tt` → e (ou r), mot non lu (déclaré).
≥ 2/3 `Q2B` → la variante est une forme stable ; 260v l.3 r20 (« du [?] [?] d'auril ») est à relire avec q (t2 = e de Brackx
mis en doute, sans effet de valeur ici).

## Famille F (« hampe à drapeau triangle ») — 2 cibles, les mêmes qu'en 2511 (déclaré)
F1 260v l.25 r2 · F2 260v l.27 r2.
Options (8) : `Pi` ⊓ (260v l.12 r11, l.12 r55) ; `P` Π (260r l.1 r1, seul autre jeton) ; `L` ⊥ (260r l.4 r18, 260v l.28 r17) ;
`pi` ⌒π (260v l.1 r7, 260r l.11 r8) ; `7` (260v l.5 r23, l.24 r41) ; `v` (260v l.5 r21, l.1 r25) ; `p` ρ (260v l.1 r11,
260r l.1 r28) ; `FF` hampe à drapeau (260v l.9 r2, l.9 r35). Référence : `Pi`.
Effet : `FF` → étiquette nouvelle « FF » (4 jetons : F1, F2, v.9 r2, v.9 r35), valeur ff PROPOSÉE (4 lieux : affaires, affaire,
effect, affin), mots lus « avec planche, valeur au sens » ; `L` → f (clé), « afaire(s) » lu avec planche ; `Pi`/`P` → rien ;
`7`, `v`, `p`, `pi` → valeur de la clé, mot non lu (déclaré).

## Contrôles cachés (3), forme connue, jamais exemples ni cibles, hors lignes des cibles
- K1 (jeu Q) : `###` 260r l.10 r14.
- K2 (jeu F) : `7` 260r l.17 r1.
- K3 (jeu F) : `v` 260r l.1 r34.
Un contrôle raté → rien n'est intégré.
Options texte habituelles + remarque.

## Contrôle d'absence de sosie (avant envoi)
Comme 2511 : options distinctes deux à deux, exemples d'une option de même forme, contrôle sans sosie hors option attendue.
En particulier `t2` contre `Q2B` (même famille de traits) : si sosies, `Q2B` est gardé (c'est la question) et `t2` retiré,
consigné. Remplacement d'un exemple fautif : jeton suivant de même étiquette dans align.tsv, hors lignes des cibles.

## Copies
work/planche.html → _planches-serve/saintluc1586b-2511b/planche.html et _planches-tel/<NN suivant>-saintluc-b.html.
