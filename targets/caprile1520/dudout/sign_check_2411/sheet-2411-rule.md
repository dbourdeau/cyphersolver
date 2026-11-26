# Règle de sélection — planche « Caprile 1520-21, R1139 / R1136 » (cible cyphersolver caprile1520), écrite AVANT toute construction de vignettes (nuit du 23 au 24/11/2026)

Pièces : ASMo, Ambasciatori, Ungheria b. 4 — DECODE R1139 (billet du 6 avril 1521, image IMG_R1139_I5752_P2.png) et DECODE R1136
(lettre du 8 mars 1520, IMG_R1136_I5740_P1.png). Images : `src/` = lien symbolique vers SPOF_2 …/DECODE-planches-2411 (SHA256SUMS,
PROVENANCE.md) ; coordonnées = pixels natifs 3240 × 4320. 🔴 Images DECODE : planche privée seulement, jamais publiées ni copiées
dans un dépôt ; citer « DECODE R1139 / R1136 ».
🔴 Cible d'un tiers : caprile1520 (R1139, R1136 « decoded, not read ») est le travail de Daniel Bourdeau (NOTES, R1139/R1136_reread_log,
b18 du 22-23/10). Étape 0 (23/11) : `gh pr list --search caprile1520 --state all` → #38 seule (découpage, Daniel) ; origin/main 31295a96a3.
Notre planche C02/C09 (23/10, 29/10) portait sur le chiffre 1519 (R1128/R1135), pas sur ces signes : rien de déjà posé ici.
Le résultat sera PROPOSÉ à Daniel (commentaire ou PR, crédit Daniel Bourdeau + relecteur Brice Dudout) ; rien n'est écrit chez lui.
Base : targets/caprile1520 (R1139_transcription_b18.txt, r1136_pass4.txt, R1139_corrections.tsv, seg21/signs.md) : blocages listés
« 4 8 1 7 », le signe 4 (6 lieux), p+ et q+ (lieu unique chacun), « q+ PHI o 1 1 » en fin de L07.

## Question de forme
À l'image (×4, 23/11), le « 4 », le q+ et le q? de L06 ont la même allure : une boucle de q dont la hampe porte une barre ; le y barré
(ɏ) leur ressemble. Question : chacun de ces signes est-il un « 4 » (forme des exemples), un q simple, ou un y barré ?
p+ : p barré (comme ailleurs) ou φ ou ƀ (b barré) ? « 1 1 » de fin de L07 : u ou deux traits « 1 » ?

## Cibles retenues (9)
- Famille q/4/y : **A1** R1139 L01 « z 4 o » (1833,2128,1850,2168) ; **A2** R1139 L01 fin « ss 4 8 1 7 » (2754,2112,2773,2149) ;
  **A3** R1136 L10 « QB 4 x » (1113,1633,1140,1677) ; **A4** R1136 L12 début « 4 Z » (922,1808,953,1836) ;
  **A5** R1139 L04 q+ (2299,2331,2328,2378) ; **A6** R1139 L07 fin q+ (2720,2522,2761,2572) ; **A7** R1139 L06 « AST 8 q? » (2554,2458,2586,2510).
  Options : 4 / q / y barré.
- **P1** R1139 L03 p+ (2676,2257,2702,2292) — options : p barré / φ / ƀ.
- **U1** R1139 L07 fin « 1 1 » (2846,2518,2862,2542) — options : u / 1 (petit signe, ×6-7 : gardé car les deux traits restent nets).

## Contrôles nets (3)
- **K1** R1139 L07 x (2589,2530,2611,2558) : x / AST, attendu x. **K2** R1139 L04 λ (2499,2318,2519,2352) : λ / A, attendu λ.
- **K3** R1139 L05 fin q simple (2844,2378,2860,2432) : 4 / q / y barré, attendu q.

## Alphabet (exemples ; jamais une cible ni un contrôle)
4 : R1139 L02 fin (2839,2181,2860,2220), R1136 L05 début (920,1255,953,1296) ; q : R1139 L02 (2540,2196,2558,2234), L06 (2594,2458,2610,2504) ;
y barré : R1139 L06 (2358,2468,2380,2507), L07 (2604,2533,2629,2584) ; p barré : L05 (1782,2405,1803,2444), L02 (2584,2196,2601,2228) ;
φ : L01 (1196,2121,1216,2174), L07 (2774,2519,2798,2570) ; ƀ : L01 (1883,2104,1904,2142) ; u : L03 (1307,2271,1328,2295) ; 1 : L05 (1823,2398,1835,2425) ;
x : L04 (2652,2322,2685,2352) ; AST : L06 (2491,2463,2516,2497) ; λ : L04 fin (2848,2318,2864,2352) ; A : L05 (2589,2386,2611,2418).

## Écartés
- « 8 » de « 4 8 1 7 » et « 1 7 » (L01, L02) : forme nette (8, 1, 7 sans voisin ambigu) ; le blocage est la valeur, pas la forme.
- R1139 L04 fin « # » (deux points minuscules au bord, illisibles agrandis) ; R1139 L10 « Z? » (entre dans le clair).
- R1136 L01-L03 sous la tache et les « # » de L02, L03, L06 : aucune forme candidate à proposer (lecture ouverte, pas un choix de forme).
- Paires c/CE/e, QB/8, AMP/EL de R1136 : hors mandat de cette planche (fond pâle et bruité ×6, risque « Trémais »).
Boîtes vérifiées sur planches-contact de travail (scratchpad, 23/11) puis crops/_contact.jpg.
Page : un seul signe encadré ; aucune glose ; « forme n » ; titre « Planche C ». Ordre : planche_core v2 (copie P2 : vignettes agrandies),
graines 20261124 / 1520. Export : reponses-2411-caprile.json.

## Intégration (après réponses, sur une copie locale ; rien n'est écrit chez Daniel sans son accord)
1. Un contrôle raté (y compris « impossible à distinguer ») → rien intégré ; noté dans HANDOFF.
2. Famille A : si A1-A4 (étiquetés 4) ET au moins un de A5-A7 (q+ / q?) reçoivent « 4 » → proposer que q+ et q? soient le MÊME signe que 4
   (un seul nom, 9 lieux au lieu de 6 + 3) ; une cible « 4 » répondue « y barré » ou « q » → proposer le changement d'étiquette pour CE lieu
   seulement. « impossible à distinguer » / « aucune » → étiquette inchangée, noté.
3. P1 : « p barré » → p+ = p (valeur de clé EL/p déjà connue, n'entre que comme hypothèse à tester) ; φ ou ƀ → nouvelle étiquette proposée.
4. U1 : « u » → « 1 1 » devient U ; « 1 » → inchangé.
5. Aucune valeur nouvelle n'entre par la planche : les étiquettes changées sont re-décodées avec key21 sur copie, recompte selon #728,
   entrée HANDOFF datée ; proposition à Daniel (crédit).
