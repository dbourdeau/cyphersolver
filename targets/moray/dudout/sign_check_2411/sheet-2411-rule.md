# Règle de sélection — planche « Moray 1568, f. 213v » du 24/11/2026 (cible cyphersolver moray), écrite AVANT toute construction de vignettes

Pièce : British Library, Add MS 32091 f. 213v, Moray (régent d'Écosse) à John Wood, Édimbourg, 13 juillet 1568 : post-scriptum
chiffré de 4 lignes (134 signes). Image : DECODE R8345, image I38545, page 4 (`src/IMG_R8345_I38545_P4.jpg`, lien symbolique vers
SPOF_2 …/DECODE-planches-2411/, SHA256SUMS sur place ; coordonnées = pixels natifs 6971×9718). 🔴 Image DECODE / BL : planche
privée seulement, jamais publiée, aucun dérivé publié, jamais copiée dans un dépôt ; citer « DECODE R8345 ».
🔴 Cible d'un TIERS : lecture d'Andrew Aymeloglu (aaymeloglu, issue #553 fermée par Daniel « sous la règle des 4 jours », dossier
targets/moray/aaymeloglu/, commit f91bd95e4f du 14/11). Étape 0 (24/11) : `gh pr list --search moray --state all` → aucune PR ;
issue #553 : Daniel attend « the five split places as crops or a transcription » pour la rouvrir. Le résultat sera PROPOSÉ (issue
ou PR, sans image ni crop DECODE) avec crédit aaymeloglu (clé, transcription) + Tomokiyo (transcription d'origine) + relecteur Brice.
Base : targets/moray/NOTES.md (« 14 Nov 2026 », cinq scissions) ; aaymeloglu/transcription.txt (étiquettes) ; elizabeth_moray.txt
(Tomokiyo) ; aaymeloglu/FRESH-MANUSCRIPT-REVIEW.md (mot final L4). Alignement position à position (134 = 134) refait le 24/11.

## Critère
Les cinq scissions de Tomokiyo que la lecture d'aaymeloglu exige (U/M, x/P, F/s, z3 en trois, e/c) + les deux signes ouverts du
mot final de 7 signes (L4.2 « x3 », L4.4 « Xs »). Pour chaque scission, les lieux d'une forme qui n'ont qu'un seul exemplaire,
ou qui servent d'exemples, ne sont pas cibles. Positions = « Lligne.rang » dans aaymeloglu/transcription.txt (rang à partir de 1,
« | » non compté). Au plus ~15 questions : U/M réduit à 3 cibles (formes nettement différentes à l'œil, l'enjeu est que chaque
lieu tombe du bon côté), e/c réduit à la seule place disputée.

## Cibles retenues (12)
- U/M (Tomokiyo « 19 ») : **UM1** L2.27 (U) ; **UM2** L3.19 (U) ; **UM3** L2.32 (M) — options : U / M.
  Exemples U : L1.1, L1.42 ; M : L1.15, L1.39. (L1.15, L1.39 exemples ; L2.38, L3.9 non posés.)
- x/P (Tomokiyo « x ») : **XP1** L2.21 (P) — options : x (L1.5, L2.3) / p simple (L2.4, L2.31) / P bouclé (L1.3, seul autre P).
- F/s (Tomokiyo « s ») : **FS1** L1.32 ; **FS2** L3.36 (tous deux F chez aaymeloglu) — options : F (L1.46, L2.11, = « f » de
  Tomokiyo) / s (L3.16, seul s).
- z3 (Tomokiyo « z3 ») : **Z1** L1.25 (Z5) ; **Z2** L2.37 (Z3) ; **Z3** L4.5 (Z2, identification disputée) — options : Z5 (L1.38) /
  Z3 (L1.10, L1.44) / Z2 (L1.40, L3.14).
- e/c (Tomokiyo « e ») : **EC1** L1.27 (c) — options : e (L1.11, L1.41) / c (L1.23).
- Mot final : **F1** L4.2 (« x3 », revue : plutôt n) ; **F2** L4.4 (« Xs », revue : plutôt u) — options : x (L1.5, L3.30) /
  xd (L1.17) / X (L2.30, L3.28).

## Contrôles nets (3), signes sans ambiguïté de forme
- **K1** L3.21 triangle : A / a, attendu A (exemples A : L1.16, L2.36 ; a : L1.24, L3.1).
- **K2** L3.23 a rond : A / a, attendu a (mêmes exemples).
- **K3** L2.40 r : r / Tc, attendu r (exemples r : L2.8, L3.20 ; Tc : L2.19, L3.13).

## Exclus
L1.3 (P) : boucle mêlée à g (L1.4) → exemple seulement, pas cible. L3.16 (s) : seul exemplaire → exemple. L4.1 (Zz) : même famille
que L3.3-4, ne départage rien. Tout signe trouvé illisible agrandi sur la planche-contact est retiré et noté au HANDOFF.
Boîtes vérifiées sur planches-contact de travail (scratchpad, 24/11) puis crops/_contact.jpg.
Page : un seul signe encadré ; aucune glose ; « forme n » ; titre « Planche 18 ». Options texte habituelles (planche_core v2,
copie P2, vignettes agrandies, signe ≥ 130 px). Graines 20261124 / 1568. Export : reponses-2411-moray.json.

## Intégration (après réponses, sur copie locale ; rien n'est écrit chez Daniel / aaymeloglu sans proposition créditée)
1. Un contrôle raté (y compris « impossible à distinguer ») → rien intégré ; noté dans HANDOFF.
2. U/M : si UM1-UM3 reçoivent chacun la forme de leur étiquette aaymeloglu → scission U/M CONFIRMÉE à l'image (le « 19 » de
   Tomokiyo porte deux signes). Une réponse contraire ou « impossible » → scission non tenue pour ce lieu ; noté.
3. x/P : XP1 = « P bouclé » → P confirmé distinct de x ; = x → la valeur v de L2.21 (evil) tombe ; = p simple → noté (p = m).
4. F/s : FS1, FS2 = F → la fusion s-Tomokiyo/f-Tomokiyo d'aaymeloglu est confirmée ; = s → scission non tenue.
5. z3 : chaque cible confirmée si elle reçoit sa famille aaymeloglu (Z5 / Z3 / Z2) ; Z3 (L4.5) ≠ Z2 confirme la réserve de la revue.
6. e/c : EC1 = c → c confirmé (Carlyle « r ») ; = e → noté.
7. Mot final : F1, F2 sont des observations de forme (aucune valeur nouvelle n'entre par la planche) : la réponse est notée pour
   la revue de L4, sans changer la clé.
8. Recompte selon #728 sur copie, entrée HANDOFF datée ; proposition à Daniel/aaymeloglu (crédit), transcription des lieux en
   texte (jamais de crop DECODE).
