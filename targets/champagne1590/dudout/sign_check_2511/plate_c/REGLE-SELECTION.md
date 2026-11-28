# Règle de sélection — planche « champagne1590-2511c », écrite AVANT les vignettes (27/11/2026)

Nouveau test complet, accord de Brice (option B, relayé par le coordinateur, 27/11). Il ne lève AUCUN contrôle des
planches a (K3 manqué) et b (K3 manqué) : leurs réponses restent non intégrées et ne servent ici que de condition de
concordance (elles peuvent seulement restreindre, jamais ajouter). Même cible, mêmes images (Gallica IIIF
btv1b525245007 : f85 = no 25, f83 = no 24), même main.

## Planche-contact (faite avant ce hachage, vignette par vignette)
61 cadres (`scripts/boxes.py`), contrôlés un à un sur la planche-contact, puis à fort grossissement (×3, grille 10 px)
pour les contrôles et leurs exemples. Corrigés : K3 (bord droit avant le « a »), g_a (bord avant le « r »), g_b
(« Ligue » abandonné : la boucle du g passe sous le u ; remplacé par le g de « ung » l.7), M_b (cadre d'abord sur « de »,
replacé sur le M de « Mayenne »), d_a (resserré). Cibles T1 à T10 : cadres inchangés depuis la b, chacun vérifié centré
sur UN signe ; T1 couvre le seul 9 sous la barre, le 3 qui précède est hors du cadre (pas « entre deux signes » comme K1 b).
Exemples n8/n4/n1 (contrôle K1 de la b) retirés.

## Contrôles cachés (3), neufs, sans aucun r, signes isolés dans des mots sûrs, sans sosie parmi les options
| code | cadre | attendu | options (exemples) |
|---|---|---|---|
| K1 | no 25 l.9, g de « grandes » | g | g (grandeur l.17, ung l.7) · d (de faire l.48, demeure l.52) · p (party l.7, pour l.13) |
| K2 | no 25 l.10, « a » isolé (« irrité a faire ») | a | a (a Creçy l.3, serviront a l.4) · t (tenons, tenez, tant) · f (faict, face) |
| K3 | no 25 l.32, M de « Mais en vain » | M | M (Mais l.15, Mayenne l.14) · C (Chastillon, Cependant l.38) · d (idem K1) |

## Cibles (9), options identiques à la planche b (aucun cadre défectueux trouvé)
T1 9/3/7 · T3 3/5 (vignette élargie) · T4 G en 6 / G bouclé / C (les deux G valent G) · T5 pl/fl · T6 u/o · T7 c/t ·
T8 u/r · T9 c/r · T10 p/m. Effets : ceux des règles a et b.

## Tirage (graine 15903), contraintes fixées AVANT le tirage
1. Ordre des 12 questions : permutation tirée de la graine (random.Random(15903).shuffle).
2. Ordre des options de chaque question : shuffle avec le même générateur, dans l'ordre des questions.
3. Contrainte : les positions (forme 1/2/3) des réponses attendues des trois contrôles doivent être deux à deux
   différentes ; tant qu'elles ne le sont pas, les options des trois contrôles sont re-tirées (même générateur).

## Critères d'intégration (écrits avant toute réponse)
- Contrôles : 3 sur 3 exigés. Un contrôle est réussi si la forme attendue est choisie et qu'aucune remarque ne
  conteste la valeur ; sinon rien n'est intégré.
- Une réponse de cible est concluante si une seule valeur est choisie et qu'aucune remarque ne la contredit
  (« aucune », « impossible à distinguer », « illisible » = non concluant ; remarque disant que le cadre est entre
  deux signes = non concluant).
- Concordance a/b/c : une cible ne compte que si la réponse c est concluante ET égale aux réponses a et b,
  elles-mêmes concluantes (comparaison par valeur : G en 6 = G bouclé = G). Si a ou b est non concluante sur cette
  cible (cas de T5 : a = « aucune, H majuscule », T7 a avec réserve), la cible ne compte pas ; elle est seulement notée.
- Désaccord a/b/c : la cible ne compte pas, le désaccord est noté (aucune valeur retenue).
- Les cibles qui comptent sont appliquées aux textes avec la mention « relecture aveugle sur forme, Brice Dudout,
  planches 2511 a/b/c » ; recompte selon la règle de Daniel (95 % des mots lus par le sens, ≥ 300 caractères ; sûrs,
  {probables}, [restitués], ‹irrésolus› séparés ; un mot tiré du sens seul reste {probable}) avant toute PR.
  T3 = 3 (Budouic) contredit les deux lecteurs : même concordant, il est signalé comme correction à revoir, pas appliqué
  sans second regard.

## Page
Vignettes JPEG ≤ 560 px, page ≤ 1,8 Mo, `.opt .v img{max-width:40vw}`, même format de sortie JSON
(`reponses-champagne1590-2511c.json`), clé privée SPOF_2 `planches-pistes-2511/champagne1590/prive/cle-PRIVEE-c.json`,
vignettes `vignettes-c/`.
