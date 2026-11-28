# Règle de sélection — planche « champagne1590-2511 », écrite AVANT les vignettes de la planche (25/11/2026)

Cible : `champagne1590` chez Daniel (nouvelles de Champagne au duc de Nevers, juin 1590, BnF fr. 3623 nos 24, 25, 60 ;
clé Nevers no 25, appariée par Michael Brackx, issue #96 ; nos 24 et 60 lus par Andrew Beling, PR #422).
État (origin/main, 16/11) : « read in part » ; mesure sur les mots chiffrés : 40 / 46 = 0,87 (no 25 : 20/22 ;
no 24 : 18/21 ; no 60 : 2/3). Clair du no 25 : 892 mots, 72 trous (0,925), deux lecteurs en désaccord sur une
trentaine de mots (beling/results/n25_compare.md). Aucune PR ni issue ouverte « champagne1590 » le 25/11.
Images : Gallica IIIF openapi.bnf.fr, ark btv1b525245007, f85 = no 25 (f. 38r), f83 = no 24 (f. 37r), f185 = no 60
(f. 88r), pleine résolution (tuiles 1000 px, sans navigateur), sur SPOF_2 `planches-pistes-2511/champagne1590/images/`.
Cadres (pixels pleine résolution) : `scripts/boxes.py`, gelé avec cette règle ; vérifiés sur planche-contact avant ce
hachage (T4, T5, T6, T7, T8, T9, K2, et 15 exemples recalés ; l'exemple « n » de no 60 remplacé par une glose sûre du no 25).

Main : une seule main pour le clair des trois lettres (Beling) ; les gloses interlinéaires sont de la main du
déchiffreur. Particularités vues sur la planche-contact : le « c » a la forme d'un r moderne, le « r » la forme d'un z ;
le « G » capital a une forme en 6 (Guische) et une forme bouclée (Givry), les deux sont montrées dans l'option G ;
la glose « n » du déchiffreur a une variante à queue (au-dessus du 64 de l'union) qui ressemble à un y : elle est
montrée dans l'option n, à côté d'un n simple.

## Questions (10) — un signe encadré ; options = formes (un seul caractère chacune), 2 exemples sûrs chacune

| code | lieu | Brackx | Beling | options | ce que change la réponse |
|---|---|---|---|---|---|
| T1 | no 25 l.34, signe sous la barre à la fin du groupe « … 38 93 [ ] » | 39̄ (La Noue) | 9̄ (Roy) | 9 · 3 · 7 | 9 → « du [Roy] » lu ; « autre forme » + remarque « 39 » → « du M. de la Noue » lu ; dans les deux cas le trou de no 25 se ferme : 20 → 21/22 (90,9 → 95,5 %) |
| T2 | no 60 l.5, glose au-dessus du dernier chiffre (64) | — | y (Launay) | y · n | n → la glose est un n à queue, « Launan » sûr, no 60 : 2 → 3/3 ; y → conflit glose/clé maintenu (rien ne change) |
| T3 | no 24 l.9, 1er chiffre du 5e groupe (« 36 » ou « 56 ») | 56 | 56 (« 36 ou 56 ») | 3 · 5 | 5 → « de Ludouic » confirmé (aucun gain, protège) ; 3 → 36 = b, « Budouic » : un trou de plus (no 24 : 18 → 17/21) |
| T4 | no 25 l.2, initiale du lieu « a [G/C]… » | Compiegne | Gonnesse | G · C | G → « Gonnesse » ; C → « Compiegne » (correction du clair, pas du chiffre) |
| T5 | no 25 l.8, initiale du 2e mot « ny … ny [p/f]latines » | flatteries | platines | p · f | p → « platines » ; f → « flatteries » |
| T6 | no 25 l.21, 2e lettre « auec [R/f][u/o]… et d'Amours » | [?force] | [?Ruelle] | u · o | u → « Ruelle » (trou de Brackx fermé, +1 mot clair) ; o → « force » |
| T7 | no 25 l.27, initiale « [c/t]… bien la rupture » | treuvons | croions | c · t | c → « croions » ; t → « treuvons » |
| T8 | no 25 l.30, 3e lettre « la bataille d'A[u/r]… » | d'Arques | d'Auvergne | u · r | u → « d'Auvergne » (Issoire, mars 1590) ; r → « d'Arques » |
| T9 | no 25 l.44, initiale du 1er mot de la ligne « [c/r]…ere assiegée » | riviere | commerce | c · r | c → « commerce » ; r → « riviere » |
| T10 | no 25 l.49, initiale « a la [p/m]… du plus cruel » | misericorde | puissance | p · m | p → « puissance » ; m → « misericorde » |

Exemples (lieux sûrs, mots lus par les deux lecteurs, jamais un lieu de question) :
9 = no 25 l.29 « 39 » (nul), l.30 « 93 » (seruice) ; 3 = l.29 « 43 », l.30 « 93 » ; 7 = l.30 « 75 », l.30 « 37 » ;
3 (no 24) = l.9 « 38 », « 39 » ; 5 (no 24) = l.9 « 45 », l.23 « 56 » ;
y = no 60 l.1 « ay », no 25 l.2 « roy » ; n (glose) = no 25 l.27 gloses de l'union au-dessus de 64 (n à queue) et de 63 ;
G = no 25 l.23 « Guische », no 24 l.34 « Givry » ; C = no 25 l.38 « Chastillon », « Cependant » ;
p = l.7 « party », l.13 « pour » ; f = l.3 « faict », l.10 « face » ; m = l.28 « malheur », l.52 « demeure » ;
u = l.10 « nous », « esperdu » ; o = l.10 « nous », « tenons » ; t = l.10 « tenons », l.35 « l'autre » ;
r = l.29 « affaires », l.13 « pour » ; c = l.30 « ce », l.6 « cestuy ».

## Contrôles cachés (3), sans sosie parmi leurs options
| code | lieu | attendu | options |
|---|---|---|---|
| K1 | no 25 l.29, 7 de « 37 » dans « de chaseron » (glose c) | 7 | 7 · 3 · 9 |
| K2 | no 25 l.22, p de « passeport » | p | p · f · m |
| K3 | no 25 l.31, r de « trop » | r | r · c · u |
Règle : un contrôle manqué → toutes les réponses tenues pour faibles (second regard avant usage).

## Gain possible et application
Mesure de Daniel (mots chiffrés) : si T1 et T2 tombent (T3 = 5), 40 → 42/46 = 0,87 → 0,913 ; no 25 passe 95,5 %
(21/22), no 60 3/3 (trop court pour une classe). La cible reste « read in part » : les trous du no 24 (lu[y], au[o]it,
[?Paris] en marge) ne sont pas des questions de forme. Clair du no 25 : 7 mots départagés entre les deux lecteurs
(dont 1 trou de Brackx fermé, Ruelle), utile pour le « second lecteur » demandé par les gaps du profil.
« aucune / autre forme », « impossible à distinguer », « illisible » = rien ne change (sauf T1 avec remarque « 39 »).
Les réponses s'appliquent aux textes (texts/n25_reading.md, n24/n60) avec la mention « relecture aveugle sur forme,
Brice Dudout, planche 2511 » ; recompte avant toute PR. Pas de PR ni de commentaire sans accord.

## Avenant 1 (26/11, après le hachage, avant toute réponse)
T6 recadré : la vignette agrandie montrait le cadre sur la barre du t, pas sur la 2ᵉ lettre ; cadre déplacé de
(2300,2198,2322,2230) à (2320,2200,2340,2230). Rien d'autre ne change (question, options, effets). boxes.py ré-haché.
