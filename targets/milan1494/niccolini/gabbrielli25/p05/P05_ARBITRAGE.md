# P05_ARBITRAGE — arbitrage aveugle A′ (signes seulement)

Sources : P04_SIGNES_T2.tsv (transcripteur A, référence d'identifiants/segmentation), P05_SIGNES_T3.tsv (transcripteur B), F74_A0000443/444.jpg, CATALOGUE_F.jpg. Gloses non consultées pour les valeurs ; pas de clé, pas de déchiffrement. Recadrages agrandis (x2–x8, Lanczos + autocontraste) dans crops/.

## Méthode

- Normalisation de T3 avant alignement : X:ʃ/X:5 + X:° → X:5^o ; X:L + X:⁹ → X:L^g ; X:2 + X:ᶜ → X:2^c ; X:ψ → X:psi ; X:ω → X:w ; X:θ → K:theta ; F25 et X:9 comptés comme identiques (T3 n'utilise jamais X:9).
- Alignement séquence par séquence (difflib) ; un « désaccord » = un token de la plus longue des deux parties d'un bloc non égal (forme, présence/absence, ordre).
- Règles de convention appliquées sans changement de forme : **R1** (T3 X:5 pour toutes les formes ʒ/ƀ/long-s ; T2 garde F39/F27/X:5 ; chaque F27 de T2 contesté a été vérifié sur recadrage : passé en F39 quand une barre traverse la haste haute) ; **R2** (T3 X:A/X:λ = signe « a à trait arrière » = F09 du catalogue).
- Tous les autres désaccords ont été tranchés sur l'image, un par un (raison ci-dessous). Accords T2=T3 gardés, sauf contradiction claire de l'image (444-06 #2 : ÷ → F01?, seul point en dot inférieur).

## Totaux

- Séquences : 32 (443 : 26, 444 : 6) ; aucune séquence ajoutée.
- Désaccords T2/T3 (tokens) : 233.
- Tokens modifiés dans FINAL par rapport à T2 (remplacements + insertions + suppressions, ajout/retrait de « ? » compris) : 78.
- Page 443 : F=876 X=113 K=10 (total 999).
- Page 444 : F=193 X=18 K=7 (total 218).

## Décision 444-07

T2 signalait une possible séquence chiffrée omise en « 444-07 ». Vérifié sur l'image (lignes 444-06 fin → bas de page) : après le dernier signe de 444-06-1 (F12) vient un point puis du texte clair (« Io ci ho bene… ») qui continue en ligne 07 ; lignes 07–09 en clair (formule de recommandation, « vale », date « xx julij 1494 »), puis souscription et mention dorsale/suscription d'une autre main, en clair. Les traces en bas de page sont des transparences en miroir du verso, pas des signes. **Aucune séquence chiffrée en 444-07 ni ailleurs en fin de 444 : pas de 444-07-1.** (T3 avait raison sur ce point.)

## Journal par séquence

### 443-02-1 — 0 désaccord(s) ; 0 token(s) modifié(s) vs T2

### 443-03-1 — 4 désaccord(s) ; 3 token(s) modifié(s) vs T2
- T2#0 `∅` / T3 `X:~` → #0 F17 → **X:bar? F17** : separate wavy dash before ⊥, distinct ink (T3 X:~); kept as doubtful isolated bar
- T2#2 `F06?` / T3 `F18` → #2 F06? → **F18?** : legs splay/cross like x under a top stroke; T2 doubtful π, T3 x
- T2#20 `F13` / T3 `F01` → #20 F13 → **F01** : bar with dot below only, no upper dot
- T2#33 `F24?` / T3 `F09` → #33 F24? → **F24?** : KEEP T2: loop sits on a bar extending left (F24), not free a (F09)

### 443-04-1 — 10 désaccord(s) ; 5 token(s) modifié(s) vs T2
- T2#2 `F39` / T3 `F12` → #2 F39 → **F39** : KEEP T2: crossbar through ascender visible
- T2#12 `F23?` / T3 `F11` → #12 F23? → **F23?** : KEEP T2: o has bar to the right
- T2#15 `X:bar` / T3 `∅` → #15 X:bar → **X:bar?** : bar at line level after ÷ (T3 omits); could be gloss tail -> doubtful
- T2#18 `F13` / T3 `F01` → #18 F13 → **F01** : dot below only
- T2#21 `F03` / T3 `F18` → #21 F03 → **F03** : KEEP T2: large cursive X (~2x size of ordinary x F18), matches catalogue F03
- T2#27 `F10? F39?` / T3 `F11? F12` → #27 F10? F39? → **F10? F12?** : d-like loop with ascender kept (F10?); following 6 has tall stem but no crossbar -> F12
- T2#38 `F11` / T3 `F23? X:5` → #38 F11 F27? → **F23 F39?** : o has bar to right (F23); next sign has tall crossed ascender (F39 class, T3 X:5)
- T2#40 `F27` / T3 `∅` → garde **F27** (artefact d'alignement : T3 a bien ce ʒ final ; cf. #38 ci-dessus, fin lue F31 F23 F39? F27)

### 443-05-1 — 10 désaccord(s) ; 1 token(s) modifié(s) vs T2
- T2#5 `F23` / T3 `F11` → #5 F23 → **F23** : KEEP T2: second o has bar to right
- T2#14 `F39` / T3 `X:5` → garde **F39** — R1 keep T2: T3 codes every ʒ/ƀ/long-s form as X:5; T2 separates F39 (crossed ascender, catalogue F39) / F27 (ʒ, catalogue F27) / X:5 (long-s); T2 shape kept (individual F27 cases checked on crops, changed only where a crossbar is visible)
- T2#19 `F39` / T3 `X:5` → garde **F39** — R1 keep T2: T3 codes every ʒ/ƀ/long-s form as X:5; T2 separates F39 (crossed ascender, catalogue F39) / F27 (ʒ, catalogue F27) / X:5 (long-s); T2 shape kept (individual F27 cases checked on crops, changed only where a crossbar is visible)
- T2#21 `F39` / T3 `X:5` → garde **F39** — R1 keep T2: T3 codes every ʒ/ƀ/long-s form as X:5; T2 separates F39 (crossed ascender, catalogue F39) / F27 (ʒ, catalogue F27) / X:5 (long-s); T2 shape kept (individual F27 cases checked on crops, changed only where a crossbar is visible)
- T2#25 `F24` / T3 `F09` → #25 F24 → **F24** : KEEP T2: loop on bar
- T2#27 `F09` / T3 `F25` → #27 F09 → **F25?** : closed bowl with short descender (q/9), not a-with-tail F09
- T2#30 `F13 F39 F24` / T3 `F36 F19? F09` → #30 F13 F39 F24 → **F13 F39 F24** : KEEP T2: ÷ has both dots; ƀ-class sign; loop on bar
- T2#35 `F14` / T3 `∅` → #35 F14 → **F14** : KEEP T2 (T3 omits): 11 visible between 4 and c

### 443-06-1 — 9 désaccord(s) ; 4 token(s) modifié(s) vs T2
- T2#0 `F27` / T3 `F39` → #0 F27 → **F27?** : ʒ with tall stroke above, crossbar not visible (T3 F39) -> doubtful
- T2#9 `F27?` / T3 `X:5` → garde **F27?** — R1 keep T2: T3 codes every ʒ/ƀ/long-s form as X:5; T2 separates F39 (crossed ascender, catalogue F39) / F27 (ʒ, catalogue F27) / X:5 (long-s); T2 shape kept (individual F27 cases checked on crops, changed only where a crossbar is visible)
- T2#11 `F29` / T3 `F25` → #11 F29 → **F29** : KEEP T2: loop with stroke down-left (ø/ϙ), stem not on right as q
- T2#14 `F13` / T3 `F36` → #14 F13 → **F36** : dot above only
- T2#22 `X:Vbar` / T3 `X:∇` → #22 X:Vbar → **X:Vbar** : KEEP T2 = T3 X:∇ (same sign, different label)
- T2#28 `F39` / T3 `F12` → #28 F39 → **F39** : KEEP T2: crossbar through ascender of the 6
- T2#31 `F29?` / T3 `∅` → #31 F29? → **∅** : stroke is the left stem of the triple-stem K:HH, not a separate sign (T3)
- T2#35 `F39? F09?` / T3 `X:5 F26?` → #36 F09? → **F26?** : 4-like: bowl with stroke crossing to the right (T3 F26?)

### 443-07-1 — 11 désaccord(s) ; 4 token(s) modifié(s) vs T2
- T2#1 `F27?` / T3 `X:5` → garde **F27?** — R1 keep T2: T3 codes every ʒ/ƀ/long-s form as X:5; T2 separates F39 (crossed ascender, catalogue F39) / F27 (ʒ, catalogue F27) / X:5 (long-s); T2 shape kept (individual F27 cases checked on crops, changed only where a crossbar is visible)
- T2#4 `F23 F13` / T3 `F11 F01` → #4 F23 F13 → **F11 F01** : plain o; the arched bar belongs to a ÷-type sign with only a lower dot
- T2#8 `F39` / T3 `X:5` → garde **F39** — R1 keep T2: T3 codes every ʒ/ƀ/long-s form as X:5; T2 separates F39 (crossed ascender, catalogue F39) / F27 (ʒ, catalogue F27) / X:5 (long-s); T2 shape kept (individual F27 cases checked on crops, changed only where a crossbar is visible)
- T2#18 `F39 X:L^g` / T3 `X:5 X:L F25` → #19 X:L^g → **X:L X:9** : the 9 stands on the line right of L (curved tail), not superscript; the loop above is gloss
- T2#22 `F39` / T3 `F19` → #22 F39 → **F39** : KEEP T2: tall stem, 5-like body (T3 F19?)
- T2#24 `∅` / T3 `F13` → #22 F39 → **F39** : KEEP T2: tall stem, 5-like body (T3 F19?); #23 X:2^c → **X:2^c** : KEEP T2: no separate ÷ between 2^c and 9 (T3 inserts F13); lower stroke = tail of 2
- T2#36 `F39` / T3 `∅` → #36 F39 → **F39** : KEEP T2: x 5 ƀ 11 ƀ 8 o -> seven signs visible (T3 drops one)
- T2#38 `F39?` / T3 `X:5` → garde **F39?** — R1 keep T2: T3 codes every ʒ/ƀ/long-s form as X:5; T2 separates F39 (crossed ascender, catalogue F39) / F27 (ʒ, catalogue F27) / X:5 (long-s); T2 shape kept (individual F27 cases checked on crops, changed only where a crossbar is visible)
- (sans désaccord T2/T3) #17 F15? → **F15?** : agree

### 443-08-1 — 9 désaccord(s) ; 3 token(s) modifié(s) vs T2
- T2#17 `F09` / T3 `X:A` → garde **F09** — R2 keep T2: T3 X:A/X:λ = the a-with-back-stroke sign, which is catalogue F09
- T2#23 `F13 F27?` / T3 `F36 X:5` → #23 F13 → **F36** : dot above only
- T2#26 `F39` / T3 `X:5` → garde **F39** — R1 keep T2: T3 codes every ʒ/ƀ/long-s form as X:5; T2 separates F39 (crossed ascender, catalogue F39) / F27 (ʒ, catalogue F27) / X:5 (long-s); T2 shape kept (individual F27 cases checked on crops, changed only where a crossbar is visible)
- T2#30 `F09 F27?` / T3 `X:A X:5` → #31 F27? → **F39?** : crossbar on tall ascender visible
- T2#35 `F27?` / T3 `X:5` → garde **F27?** — R1 keep T2: T3 codes every ʒ/ƀ/long-s form as X:5; T2 separates F39 (crossed ascender, catalogue F39) / F27 (ʒ, catalogue F27) / X:5 (long-s); T2 shape kept (individual F27 cases checked on crops, changed only where a crossbar is visible)
- T2#37 `F25` / T3 `F26` → #37 F25 → **F26?** : bowl with stroke extending right of stem (4-like)
- T2#40 `X:r` / T3 `F37?` → #40 X:r → **X:r** : KEEP T2: small r-like sign, not a 7 (no descending diagonal)

### 443-09-1 — 8 désaccord(s) ; 3 token(s) modifié(s) vs T2
- T2#0 `F39` / T3 `F12` → #0 F39 → **F39** : KEEP T2: tall ascender crossed at top
- T2#6 `F39?` / T3 `X:5` → garde **F39?** — R1 keep T2: T3 codes every ʒ/ƀ/long-s form as X:5; T2 separates F39 (crossed ascender, catalogue F39) / F27 (ʒ, catalogue F27) / X:5 (long-s); T2 shape kept (individual F27 cases checked on crops, changed only where a crossbar is visible)
- T2#11 `F23?` / T3 `F35 F11` → #11 F23? → **F35 F11** : v then o clearly separate (T3); no bar on o
- T2#25 `F29` / T3 `F07` → #25 F29 → **F29** : KEEP T2: same ϙ/ø shape as 443-06#11
- T2#27 `F39?` / T3 `X:5` → garde **F39?** — R1 keep T2: T3 codes every ʒ/ƀ/long-s form as X:5; T2 separates F39 (crossed ascender, catalogue F39) / F27 (ʒ, catalogue F27) / X:5 (long-s); T2 shape kept (individual F27 cases checked on crops, changed only where a crossbar is visible)
- T2#35 `F24?` / T3 `F09?` → #35 F24? → **F24?** : KEEP T2: a sits on a bar
- T2#38 `F31` / T3 `∅` → #38 F31 → **F31?** : n present but crossed by a long stroke (gloss line or strike) -> doubtful (T3 omits)

### 443-10-1 — 0 désaccord(s) ; 0 token(s) modifié(s) vs T2

### 443-11-1 — 10 désaccord(s) ; 5 token(s) modifié(s) vs T2
- T2#0 `F09` / T3 `X:A` → garde **F09** — R2 keep T2: T3 X:A/X:λ = the a-with-back-stroke sign, which is catalogue F09
- T2#2 `F24^c` / T3 `F11?` → #2 F24^c → **F24^c?** : loop on bar confirmed; c above uncertain (may be gloss)
- T2#4 `F39` / T3 `X:5` → garde **F39** — R1 keep T2: T3 codes every ʒ/ƀ/long-s form as X:5; T2 separates F39 (crossed ascender, catalogue F39) / F27 (ʒ, catalogue F27) / X:5 (long-s); T2 shape kept (individual F27 cases checked on crops, changed only where a crossbar is visible)
- T2#19 `F39?` / T3 `X:5` → garde **F39?** — R1 keep T2: T3 codes every ʒ/ƀ/long-s form as X:5; T2 separates F39 (crossed ascender, catalogue F39) / F27 (ʒ, catalogue F27) / X:5 (long-s); T2 shape kept (individual F27 cases checked on crops, changed only where a crossbar is visible)
- T2#21 `F39? F23` / T3 `X:5 F11` → #22 F23 → **F23?** : bar between o and đ may be the d crossbar; T3 plain o -> doubtful
- T2#28 `∅` / T3 `F37` → #27 F37 → **F37 F37** : two 7 visible before x (T3)
- T2#30 `F39? F23` / T3 `X:5 F11` → #31 F23 → **F23?** : same pattern ƀ o đ as #22 -> doubtful
- T2#36 `F29` / T3 `F26?` → #36 F29 → **F29?** : crossed loop with descender, 4 (T3) possible

### 443-12-1 — 7 désaccord(s) ; 4 token(s) modifié(s) vs T2
- T2#0 `F27` / T3 `X:5` → #0 F27 → **F27?** : tall ascender present, crossbar unclear
- T2#5 `F39 F39? X:Vbar?` / T3 `X:5 F37 F35` → #6 F39? X:Vbar? → **F37 F35** : clear 7 then plain v (T3); T2 both doubtful
- T2#30 `F13` / T3 `F36` → #30 F13 → **F36** : dot above only
- T2#38 `F39` / T3 `X:5` → garde **F39** — R1 keep T2: T3 codes every ʒ/ƀ/long-s form as X:5; T2 separates F39 (crossed ascender, catalogue F39) / F27 (ʒ, catalogue F27) / X:5 (long-s); T2 shape kept (individual F27 cases checked on crops, changed only where a crossbar is visible)
- T2#40 `∅` / T3 `F13?` → #39 X:2^c → **X:2^c** : KEEP T2: no separate ÷ before 9 (T3 inserts F13?)

### 443-13-1 — 5 désaccord(s) ; 1 token(s) modifié(s) vs T2
- T2#0 `F09` / T3 `X:A` → garde **F09** — R2 keep T2: T3 X:A/X:λ = the a-with-back-stroke sign, which is catalogue F09
- T2#8 `F27` / T3 `X:5` → garde **F27** — R1 keep T2: T3 codes every ʒ/ƀ/long-s form as X:5; T2 separates F39 (crossed ascender, catalogue F39) / F27 (ʒ, catalogue F27) / X:5 (long-s); T2 shape kept (individual F27 cases checked on crops, changed only where a crossbar is visible)
- T2#16 `F24` / T3 `F21?` → #16 F24 → **F24** : KEEP T2: small loop at right end of a bar (F24), not e= (F21)
- T2#28 `F39` / T3 `X:5` → garde **F39** — R1 keep T2: T3 codes every ʒ/ƀ/long-s form as X:5; T2 separates F39 (crossed ascender, catalogue F39) / F27 (ʒ, catalogue F27) / X:5 (long-s); T2 shape kept (individual F27 cases checked on crops, changed only where a crossbar is visible)
- T2#34 `F13` / T3 `F01` → #34 F13 → **F01** : dot below only

### 443-14-1 — 9 désaccord(s) ; 6 token(s) modifié(s) vs T2
- T2#4 `F39` / T3 `X:5` → garde **F39** — R1 keep T2: T3 codes every ʒ/ƀ/long-s form as X:5; T2 separates F39 (crossed ascender, catalogue F39) / F27 (ʒ, catalogue F27) / X:5 (long-s); T2 shape kept (individual F27 cases checked on crops, changed only where a crossbar is visible)
- T2#6 `F36?` / T3 `F13` → #6 F36? → **F13?** : dot below clear; upper element is a stroke (possibly gloss descender) -> doubtful ÷
- T2#11 `F27` / T3 `X:5` → garde **F27** — R1 keep T2: T3 codes every ʒ/ƀ/long-s form as X:5; T2 separates F39 (crossed ascender, catalogue F39) / F27 (ʒ, catalogue F27) / X:5 (long-s); T2 shape kept (individual F27 cases checked on crops, changed only where a crossbar is visible)
- T2#16 `F29` / T3 `X:psi F25` → #16 F29 → **X:psi F25?** : trident ψ followed by a separate q-like sign before the loop-on-bar (T3)
- T2#20 `F08` / T3 `F12?` → #20 F08 → **F08** : KEEP T2: 6/σ with flat top bar
- T2#31 `F13` / T3 `F36` → #31 F13 → **F36** : dot above only
- T2#34 `F13 F27` / T3 `F36 X:5` → #34 F13 F27 → **F36 F39** : dot above only; next sign has crossbar on tall ascender

### 443-15-1 — 3 désaccord(s) ; 0 token(s) modifié(s) vs T2
- T2#1 `F39` / T3 `X:5` → garde **F39** — R1 keep T2: T3 codes every ʒ/ƀ/long-s form as X:5; T2 separates F39 (crossed ascender, catalogue F39) / F27 (ʒ, catalogue F27) / X:5 (long-s); T2 shape kept (individual F27 cases checked on crops, changed only where a crossbar is visible)
- T2#6 `F39` / T3 `F27` → #6 F39 → **F39** : KEEP T2: tall crossed ascender (T3 F27)
- T2#9 `F23` / T3 `F11` → #9 F23 → **F23** : KEEP T2: o with bar before ⊙

### 443-16-1 — 9 désaccord(s) ; 4 token(s) modifié(s) vs T2
- T2#2 `F27` / T3 `X:5` → garde **F27** — R1 keep T2: T3 codes every ʒ/ƀ/long-s form as X:5; T2 separates F39 (crossed ascender, catalogue F39) / F27 (ʒ, catalogue F27) / X:5 (long-s); T2 shape kept (individual F27 cases checked on crops, changed only where a crossbar is visible)
- T2#7 `F27` / T3 `∅` → #7 F27 X:5? → **F27 F37** : ʒ then a clear 7 before A (T3)
- T2#9 `∅` / T3 `F37` → #7 F27 X:5? → **F27 F37** : ʒ then a clear 7 before A (T3)
- T2#10 `F39` / T3 `X:5` → garde **F39** — R1 keep T2: T3 codes every ʒ/ƀ/long-s form as X:5; T2 separates F39 (crossed ascender, catalogue F39) / F27 (ʒ, catalogue F27) / X:5 (long-s); T2 shape kept (individual F27 cases checked on crops, changed only where a crossbar is visible)
- T2#12 `F39` / T3 `F12` → #12 F39 → **F39** : KEEP T2: flat crossbar at top of 6
- T2#16 `F38` / T3 `F26` → #16 F38 → **F38** : KEEP T2: upright cross +, not 4
- T2#22 `X:9` / T3 `F26?` → #22 X:9 → **X:9?** : sign crossed by gloss strokes
- T2#35 `F39` / T3 `F12` → #35 F39 → **F12?** : 6 with tall stem, no crossbar (F12/F16 type)
- T2#40 `F23` / T3 `F11` → #40 F23 → **F11?** : bar right of o is the top bar of the following π

### 443-17-1 — 9 désaccord(s) ; 4 token(s) modifié(s) vs T2
- T2#2 `F08 F29` / T3 `F12 F26?` → #2 F08 F29 → **F08 F29** : KEEP T2: 6 with top bar; crossed loop
- T2#11 `F24` / T3 `∅` → #11 F24 → **∅** : only one loop-on-bar between the two ÷-type signs (T3)
- T2#14 `∅` / T3 `F07 F35` → #14 X:9 F35 F38 F24 → **F29? F35 F25? F17?** : ϙ-shape (as 443-06#11), v, q-like sign, ⊥ with long stem (T3 reading mostly)
- T2#15 `F35 F38 F24` / T3 `F17?` → #14 X:9 F35 F38 F24 → **F29? F35 F25? F17?** : ϙ-shape (as 443-06#11), v, q-like sign, ⊥ with long stem (T3 reading mostly)
- T2#26 `F10?` / T3 `F29?` → #26 F10? → **F10?** : KEEP T2: d-like crossed by gloss

### 443-18-1 — 11 désaccord(s) ; 2 token(s) modifié(s) vs T2
- T2#1 `F20?` / T3 `F01` → #1 F20? → **F20?** : KEEP T2: T-shape (vertical under bar), not bar-dot
- T2#6 `F09` / T3 `X:A` → garde **F09** — R2 keep T2: T3 X:A/X:λ = the a-with-back-stroke sign, which is catalogue F09
- T2#10 `X:5` / T3 `F27` → #10 X:5 → **X:5** : KEEP T2: tall long-s/hooked 5 (T2 legend X:5), not short ʒ
- T2#22 `F39?` / T3 `F12` → #22 F39? → **F12?** : b-like 6, ascender without crossbar
- T2#29 `F11 F32? F24` / T3 `F23 F01 F09` → #30 F32? → **F01** : bar with dot below (T3), not bar-then-o
- T2#35 `F38?` / T3 `F26?` → #35 F38? → **F38?** : KEEP T2: + visible
- T2#37 `F09 F39?` / T3 `X:A F12` → #38 F39? → **F39?** : KEEP T2: flag at top of 6
- T2#41 `F26` / T3 `F25?` → #41 F26 → **F26** : KEEP T2: 4-like final

### 443-19-1 — 13 désaccord(s) ; 3 token(s) modifié(s) vs T2
- T2#0 `F39` / T3 `X:5` → garde **F39** — R1 keep T2: T3 codes every ʒ/ƀ/long-s form as X:5; T2 separates F39 (crossed ascender, catalogue F39) / F27 (ʒ, catalogue F27) / X:5 (long-s); T2 shape kept (individual F27 cases checked on crops, changed only where a crossbar is visible)
- T2#5 `F39?` / T3 `F12` → #5 F39? → **F12** : plain 6, no crossbar
- T2#10 `∅` / T3 `X:°` → #9 F17 → **F17** : KEEP T2: loop above ⊥ belongs to the gloss (T3 X:° rejected)
- T2#11 `F39` / T3 `X:5` → garde **F39** — R1 keep T2: T3 codes every ʒ/ƀ/long-s form as X:5; T2 separates F39 (crossed ascender, catalogue F39) / F27 (ʒ, catalogue F27) / X:5 (long-s); T2 shape kept (individual F27 cases checked on crops, changed only where a crossbar is visible)
- T2#18 `F34?` / T3 `X:l? F38?` → #18 F34? → **F34?** : KEEP T2: long curved stroke before it read as gloss descender (T3 X:l?); crossing stroke on c from gloss
- T2#24 `F39` / T3 `X:5` → garde **F39** — R1 keep T2: T3 codes every ʒ/ƀ/long-s form as X:5; T2 separates F39 (crossed ascender, catalogue F39) / F27 (ʒ, catalogue F27) / X:5 (long-s); T2 shape kept (individual F27 cases checked on crops, changed only where a crossbar is visible)
- T2#27 `F27? F23 F39` / T3 `X:5 F11 X:5` → #28 F23 → **F23** : KEEP T2: o with bar
- T2#31 `F09?` / T3 `X:A` → garde **F09?** — R2 keep T2: T3 X:A/X:λ = the a-with-back-stroke sign, which is catalogue F09
- T2#35 `F13 K:dot` / T3 `F36` → #35 F13 K:dot → **F36 K:dot?** : dot above only; heavy blob kept as sign but doubtful (T3: blot)

### 443-20-1 — 8 désaccord(s) ; 4 token(s) modifié(s) vs T2
- T2#0 `F27` / T3 `X:5` → garde **F27** — R1 keep T2: T3 codes every ʒ/ƀ/long-s form as X:5; T2 separates F39 (crossed ascender, catalogue F39) / F27 (ʒ, catalogue F27) / X:5 (long-s); T2 shape kept (individual F27 cases checked on crops, changed only where a crossbar is visible)
- T2#2 `F39` / T3 `X:5` → garde **F39** — R1 keep T2: T3 codes every ʒ/ƀ/long-s form as X:5; T2 separates F39 (crossed ascender, catalogue F39) / F27 (ʒ, catalogue F27) / X:5 (long-s); T2 shape kept (individual F27 cases checked on crops, changed only where a crossbar is visible)
- T2#9 `F23 F39 F06` / T3 `F11 F12 F38` → #10 F39 F06 → **F12 F06?** : plain 6 without crossbar; π-like sign crossed by a gloss descender (T3 6 +)
- T2#33 `F39?` / T3 `F12` → #33 F39? → **F12** : plain 6
- T2#37 `F39` / T3 `X:5` → garde **F39** — R1 keep T2: T3 codes every ʒ/ƀ/long-s form as X:5; T2 separates F39 (crossed ascender, catalogue F39) / F27 (ʒ, catalogue F27) / X:5 (long-s); T2 shape kept (individual F27 cases checked on crops, changed only where a crossbar is visible)
- T2#41 `F13` / T3 `F01` → #41 F13 → **F01** : second ÷: dot below only

### 443-21-1 — 4 désaccord(s) ; 0 token(s) modifié(s) vs T2
- T2#0 `F39` / T3 `X:5` → garde **F39** — R1 keep T2: T3 codes every ʒ/ƀ/long-s form as X:5; T2 separates F39 (crossed ascender, catalogue F39) / F27 (ʒ, catalogue F27) / X:5 (long-s); T2 shape kept (individual F27 cases checked on crops, changed only where a crossbar is visible)
- T2#6 `F27` / T3 `X:5` → garde **F27** — R1 keep T2: T3 codes every ʒ/ƀ/long-s form as X:5; T2 separates F39 (crossed ascender, catalogue F39) / F27 (ʒ, catalogue F27) / X:5 (long-s); T2 shape kept (individual F27 cases checked on crops, changed only where a crossbar is visible)
- T2#19 `F27` / T3 `X:5` → garde **F27** — R1 keep T2: T3 codes every ʒ/ƀ/long-s form as X:5; T2 separates F39 (crossed ascender, catalogue F39) / F27 (ʒ, catalogue F27) / X:5 (long-s); T2 shape kept (individual F27 cases checked on crops, changed only where a crossbar is visible)
- T2#35 `F39` / T3 `X:5` → garde **F39** — R1 keep T2: T3 codes every ʒ/ƀ/long-s form as X:5; T2 separates F39 (crossed ascender, catalogue F39) / F27 (ʒ, catalogue F27) / X:5 (long-s); T2 shape kept (individual F27 cases checked on crops, changed only where a crossbar is visible)

### 443-22-1 — 5 désaccord(s) ; 1 token(s) modifié(s) vs T2
- T2#7 `F09` / T3 `X:λ` → #7 F09 → **F09** : KEEP T2: = T3 X:λ (alpha/lambda-like, catalogue F09)
- T2#11 `F02` / T3 `F31` → #11 F02 → **F02** : KEEP T2: three minims m
- T2#20 `F39?` / T3 `F12` → #20 F39? → **F39?** : KEEP T2: flat top bar visible
- T2#24 `F39` / T3 `X:5` → garde **F39** — R1 keep T2: T3 codes every ʒ/ƀ/long-s form as X:5; T2 separates F39 (crossed ascender, catalogue F39) / F27 (ʒ, catalogue F27) / X:5 (long-s); T2 shape kept (individual F27 cases checked on crops, changed only where a crossbar is visible)
- T2#35 `∅` / T3 `X:!?` → #35 X:A → **F17? X:A** : separate ⊥-like sign (vertical with gap over a bar) between 2 and A (T3 X:!?); alt. F36

### 443-23-1 — 6 désaccord(s) ; 0 token(s) modifié(s) vs T2
- T2#0 `F39?` / T3 `F12` → #0 F39? → **F39?** : KEEP T2: stroke across top of 6
- T2#7 `F39` / T3 `X:5` → garde **F39** — R1 keep T2: T3 codes every ʒ/ƀ/long-s form as X:5; T2 separates F39 (crossed ascender, catalogue F39) / F27 (ʒ, catalogue F27) / X:5 (long-s); T2 shape kept (individual F27 cases checked on crops, changed only where a crossbar is visible)
- T2#9 `F26` / T3 `F25` → #9 F26 → **F26** : KEEP T2: bar crosses right of the bowl (4)
- T2#20 `F39` / T3 `X:5` → garde **F39** — R1 keep T2: T3 codes every ʒ/ƀ/long-s form as X:5; T2 separates F39 (crossed ascender, catalogue F39) / F27 (ʒ, catalogue F27) / X:5 (long-s); T2 shape kept (individual F27 cases checked on crops, changed only where a crossbar is visible)
- T2#26 `F08` / T3 `F12` → #26 F08 → **F08** : KEEP T2: σ with flat top
- T2#38 `F39` / T3 `X:5` → garde **F39** — R1 keep T2: T3 codes every ʒ/ƀ/long-s form as X:5; T2 separates F39 (crossed ascender, catalogue F39) / F27 (ʒ, catalogue F27) / X:5 (long-s); T2 shape kept (individual F27 cases checked on crops, changed only where a crossbar is visible)

### 443-24-1 — 6 désaccord(s) ; 2 token(s) modifié(s) vs T2
- T2#0 `F01?` / T3 `F13?` → #0 F01? → **F01?** : KEEP T2: dot below; upper stroke = gloss
- T2#7 `F27?` / T3 `X:5` → #7 F27? → **F39?** : crossbar on tall ascender visible
- T2#24 `F26` / T3 `F25` → #24 F26 → **F25** : second q-like: closed bowl, straight stem, no crossing bar (T3)
- T2#27 `F39` / T3 `X:5` → garde **F39** — R1 keep T2: T3 codes every ʒ/ƀ/long-s form as X:5; T2 separates F39 (crossed ascender, catalogue F39) / F27 (ʒ, catalogue F27) / X:5 (long-s); T2 shape kept (individual F27 cases checked on crops, changed only where a crossbar is visible)
- T2#34 `F09 X:F` / T3 `X:A F39?` → #34 F09 X:F → **F09 X:F** : KEEP T2: ∂ then F-like sign with two bars, no bowl

### 443-25-1 — 10 désaccord(s) ; 2 token(s) modifié(s) vs T2
- T2#2 `F08 F39` / T3 `F12 X:5` → #2 F08 → **F08** : KEEP T2: σ with flat top
- T2#5 `∅` / T3 `F13` → #5 F14 → **F01? F14** : bar with a dot under it at line level after 7 (T3 F13); upper part = gloss
- T2#10 `F39` / T3 `X:5` → garde **F39** — R1 keep T2: T3 codes every ʒ/ƀ/long-s form as X:5; T2 separates F39 (crossed ascender, catalogue F39) / F27 (ʒ, catalogue F27) / X:5 (long-s); T2 shape kept (individual F27 cases checked on crops, changed only where a crossbar is visible)
- T2#15 `F25` / T3 `F26` → #15 F25 → **F25** : KEEP T2: q
- T2#17 `F34` / T3 `F11` → #17 F34 → **F34** : KEEP T2: open c
- T2#20 `F08` / T3 `F12` → #20 F08 → **F08** : KEEP T2: σ with flat top
- T2#28 `F39?` / T3 `F12` → #28 F39? → **F39?** : KEEP T2: big flag crossing top
- T2#33 `F33?` / T3 `F19?` → #33 F33? → **F33?** : KEEP T2: h-like, no crossbar seen (T3 F19?)
- T2#37 `F23` / T3 `F11` → #37 F23 → **F23?** : bar joins o to following 9, uncertain

### 443-26-1 — 6 désaccord(s) ; 3 token(s) modifié(s) vs T2
- T2#6 `F04?` / T3 `X:5` → #6 F04? → **X:5** : tall long-s/5 hooked stroke (= T2 legend X:5), not short round s F04
- T2#9 `F09` / T3 `X:A` → garde **F09** — R2 keep T2: T3 X:A/X:λ = the a-with-back-stroke sign, which is catalogue F09
- T2#12 `F26` / T3 `F25` → #12 F26 → **F26** : KEEP T2: 4-like with bar to right
- T2#32 `F39` / T3 `X:5` → garde **F39** — R1 keep T2: T3 codes every ʒ/ƀ/long-s form as X:5; T2 separates F39 (crossed ascender, catalogue F39) / F27 (ʒ, catalogue F27) / X:5 (long-s); T2 shape kept (individual F27 cases checked on crops, changed only where a crossbar is visible)
- T2#34 `F39? F26` / T3 `F12 F25` → #34 F39? F26 → **F12? F25** : b-like 6 with straight ascender, no crossbar; next is q (no crossing bar)

### 443-27-1 — 6 désaccord(s) ; 1 token(s) modifié(s) vs T2
- T2#14 `F39` / T3 `X:5` → garde **F39** — R1 keep T2: T3 codes every ʒ/ƀ/long-s form as X:5; T2 separates F39 (crossed ascender, catalogue F39) / F27 (ʒ, catalogue F27) / X:5 (long-s); T2 shape kept (individual F27 cases checked on crops, changed only where a crossbar is visible)
- T2#20 `X:brace?` / T3 `X:l` → #20 X:brace? → **X:brace?** : KEEP T2 (= T3 X:l)
- T2#22 `X:loop` / T3 `F12` → #22 X:loop → **X:loop** : KEEP T2: 6 with looped ascender, not plain 6
- T2#29 `F39` / T3 `X:5` → garde **F39** — R1 keep T2: T3 codes every ʒ/ƀ/long-s form as X:5; T2 separates F39 (crossed ascender, catalogue F39) / F27 (ʒ, catalogue F27) / X:5 (long-s); T2 shape kept (individual F27 cases checked on crops, changed only where a crossbar is visible)
- T2#33 `F08` / T3 `F12` → #33 F08 → **F12?** : 6 with curled top, no flat bar
- T2#36 `F39` / T3 `X:5` → garde **F39** — R1 keep T2: T3 codes every ʒ/ƀ/long-s form as X:5; T2 separates F39 (crossed ascender, catalogue F39) / F27 (ʒ, catalogue F27) / X:5 (long-s); T2 shape kept (individual F27 cases checked on crops, changed only where a crossbar is visible)

### 444-01-1 — 5 désaccord(s) ; 0 token(s) modifié(s) vs T2
- T2#6 `X:5t` / T3 `X:5` → #6 X:5t → **X:5t** : KEEP T2: crossbar on the second 5
- T2#8 `F29?` / T3 `F07` → #8 F29? → **F29?** : KEEP T2: ϙ/ø-shape (loop with stroke down), as 443-06#11
- T2#15 `F39` / T3 `X:5` → garde **F39** — R1 keep T2: T3 codes every ʒ/ƀ/long-s form as X:5; T2 separates F39 (crossed ascender, catalogue F39) / F27 (ʒ, catalogue F27) / X:5 (long-s); T2 shape kept (individual F27 cases checked on crops, changed only where a crossbar is visible)
- T2#25 `F39` / T3 `X:5` → garde **F39** — R1 keep T2: T3 codes every ʒ/ƀ/long-s form as X:5; T2 separates F39 (crossed ascender, catalogue F39) / F27 (ʒ, catalogue F27) / X:5 (long-s); T2 shape kept (individual F27 cases checked on crops, changed only where a crossbar is visible)
- T2#27 `F09` / T3 `X:λ` → garde **F09** — R2 keep T2: T3 X:A/X:λ = the a-with-back-stroke sign, which is catalogue F09

### 444-02-1 — 5 désaccord(s) ; 1 token(s) modifié(s) vs T2
- T2#0 `X:bar` / T3 `F17` → #0 X:bar → **X:bar** : KEEP T2: the vertical to the left does not touch the bar (gloss descender), not ⊥
- T2#4 `F39` / T3 `X:5` → garde **F39** — R1 keep T2: T3 codes every ʒ/ƀ/long-s form as X:5; T2 separates F39 (crossed ascender, catalogue F39) / F27 (ʒ, catalogue F27) / X:5 (long-s); T2 shape kept (individual F27 cases checked on crops, changed only where a crossbar is visible)
- T2#11 `F09 F27` / T3 `X:A X:5` → garde **F09 F27** — R1 keep T2: T3 codes every ʒ/ƀ/long-s form as X:5; T2 separates F39 (crossed ascender, catalogue F39) / F27 (ʒ, catalogue F27) / X:5 (long-s); T2 shape kept (individual F27 cases checked on crops, changed only where a crossbar is visible) / R2 keep T2: T3 X:A/X:λ = the a-with-back-stroke sign, which is catalogue F09
- T2#25 `F27` / T3 `X:5` → #25 F27 → **F39** : crossbar on tall ascender visible

### 444-03-1 — 7 désaccord(s) ; 1 token(s) modifié(s) vs T2
- T2#6 `F23?` / T3 `F12` → #6 F23? → **F12?** : 6-like loop with ascender, no bar to the right
- T2#9 `F25` / T3 `F26` → #9 F25 → **F25** : KEEP T2: q
- T2#13 `F09 F27` / T3 `X:A X:5` → garde **F09 F27** — R1 keep T2: T3 codes every ʒ/ƀ/long-s form as X:5; T2 separates F39 (crossed ascender, catalogue F39) / F27 (ʒ, catalogue F27) / X:5 (long-s); T2 shape kept (individual F27 cases checked on crops, changed only where a crossbar is visible) / R2 keep T2: T3 X:A/X:λ = the a-with-back-stroke sign, which is catalogue F09
- T2#21 `F39` / T3 `X:5` → garde **F39** — R1 keep T2: T3 codes every ʒ/ƀ/long-s form as X:5; T2 separates F39 (crossed ascender, catalogue F39) / F27 (ʒ, catalogue F27) / X:5 (long-s); T2 shape kept (individual F27 cases checked on crops, changed only where a crossbar is visible)
- T2#23 `F39` / T3 `X:5` → garde **F39** — R1 keep T2: T3 codes every ʒ/ƀ/long-s form as X:5; T2 separates F39 (crossed ascender, catalogue F39) / F27 (ʒ, catalogue F27) / X:5 (long-s); T2 shape kept (individual F27 cases checked on crops, changed only where a crossbar is visible)
- T2#27 `F27` / T3 `X:5` → garde **F27** — R1 keep T2: T3 codes every ʒ/ƀ/long-s form as X:5; T2 separates F39 (crossed ascender, catalogue F39) / F27 (ʒ, catalogue F27) / X:5 (long-s); T2 shape kept (individual F27 cases checked on crops, changed only where a crossbar is visible)

### 444-04-1 — 12 désaccord(s) ; 4 token(s) modifié(s) vs T2
- T2#1 `F10?` / T3 `∅` → #1 F10? → **∅** : no sign between N and 11 (T3)
- T2#8 `F39` / T3 `X:5` → garde **F39** — R1 keep T2: T3 codes every ʒ/ƀ/long-s form as X:5; T2 separates F39 (crossed ascender, catalogue F39) / F27 (ʒ, catalogue F27) / X:5 (long-s); T2 shape kept (individual F27 cases checked on crops, changed only where a crossbar is visible)
- T2#16 `F39 F39` / T3 `X:5 F37 X:5` → #16 F39 F39 → **F37? F39** : a 7 (with a gloss stroke touching its bar) then crossed ƀ (T3 had 5 7 5)
- T2#19 `F09 X:B` / T3 `X:A` → #20 X:B X:B → **X:B** : only one B before 2 (T3)
- T2#27 `F39` / T3 `X:5` → garde **F39** — R1 keep T2: T3 codes every ʒ/ƀ/long-s form as X:5; T2 separates F39 (crossed ascender, catalogue F39) / F27 (ʒ, catalogue F27) / X:5 (long-s); T2 shape kept (individual F27 cases checked on crops, changed only where a crossbar is visible)
- T2#32 `F13` / T3 `F01` → #32 F13 → **F01** : second ÷: dot below only
- T2#34 `F27` / T3 `X:5` → garde **F27** — R1 keep T2: T3 codes every ʒ/ƀ/long-s form as X:5; T2 separates F39 (crossed ascender, catalogue F39) / F27 (ʒ, catalogue F27) / X:5 (long-s); T2 shape kept (individual F27 cases checked on crops, changed only where a crossbar is visible)
- T2#36 `F39` / T3 `X:5` → garde **F39** — R1 keep T2: T3 codes every ʒ/ƀ/long-s form as X:5; T2 separates F39 (crossed ascender, catalogue F39) / F27 (ʒ, catalogue F27) / X:5 (long-s); T2 shape kept (individual F27 cases checked on crops, changed only where a crossbar is visible)
- T2#40 `F39` / T3 `X:5` → garde **F39** — R1 keep T2: T3 codes every ʒ/ƀ/long-s form as X:5; T2 separates F39 (crossed ascender, catalogue F39) / F27 (ʒ, catalogue F27) / X:5 (long-s); T2 shape kept (individual F27 cases checked on crops, changed only where a crossbar is visible)

### 444-05-1 — 7 désaccord(s) ; 2 token(s) modifié(s) vs T2
- T2#1 `∅` / T3 `F24?` → #1 X:L → **F24? X:L** : a second bar with a loop (partly under the gloss) before L (T3 F24?)
- T2#4 `F10 F23` / T3 `F25 F11` → #4 F10 → **F10?** : loop with descender after ÷: d-like or 9-like (T3 F25) -> doubtful; #5 F23 → **F23** : KEEP T2: o with bar
- T2#11 `F39` / T3 `X:5` → garde **F39** — R1 keep T2: T3 codes every ʒ/ƀ/long-s form as X:5; T2 separates F39 (crossed ascender, catalogue F39) / F27 (ʒ, catalogue F27) / X:5 (long-s); T2 shape kept (individual F27 cases checked on crops, changed only where a crossbar is visible)
- T2#16 `F39` / T3 `X:5` → garde **F39** — R1 keep T2: T3 codes every ʒ/ƀ/long-s form as X:5; T2 separates F39 (crossed ascender, catalogue F39) / F27 (ʒ, catalogue F27) / X:5 (long-s); T2 shape kept (individual F27 cases checked on crops, changed only where a crossbar is visible)
- T2#27 `F23` / T3 `F11` → #27 F23 → **F23** : KEEP T2: o with bar
- T2#34 `F23` / T3 `F11` → #34 F23 → **F23** : KEEP T2: o with bar

### 444-06-1 — 9 désaccord(s) ; 5 token(s) modifié(s) vs T2
- T2#3 `∅` / T3 `F24?` → #2 F13 F07? F23 F27 → **F01? F07? F23 F39** : dot below only; bar into p is part of the p (no extra F24); o with bar; crossed tall ascender
- T2#4 `F23 F27` / T3 `F11 X:5` → #2 F13 F07? F23 F27 → **F01? F07? F23 F39** : dot below only; bar into p is part of the p (no extra F24); o with bar; crossed tall ascender
- T2#9 `F13 F27` / T3 `F36 X:5` → #9 F13 F27 → **F36 F39** : dot above only; crossbar on ascender
- T2#13 `F25?` / T3 `F21?` → #13 F25? → **F21?** : e-like sign (T3), not q
- T2#16 `F39` / T3 `X:5` → garde **F39** — R1 keep T2: T3 codes every ʒ/ƀ/long-s form as X:5; T2 separates F39 (crossed ascender, catalogue F39) / F27 (ʒ, catalogue F27) / X:5 (long-s); T2 shape kept (individual F27 cases checked on crops, changed only where a crossbar is visible)
- T2#27 `F08` / T3 `F12` → #27 F08 → **F08** : KEEP T2: σ-like 6 with top bar
- T2#29 `F39` / T3 `X:5` → garde **F39** — R1 keep T2: T3 codes every ʒ/ƀ/long-s form as X:5; T2 separates F39 (crossed ascender, catalogue F39) / F27 (ʒ, catalogue F27) / X:5 (long-s); T2 shape kept (individual F27 cases checked on crops, changed only where a crossbar is visible)

## Difficultés
- Images JPEG basse résolution (signes ~12–15 px) : distinctions F12/F16/F39, F23/F11, F13/F01/F36, F25/F26/X:9 souvent à la limite ; « ? » maintenu dans ces cas.
- Interférence de la glose interlinéaire (hampes descendantes traversant la ligne chiffrée) : plusieurs « barres »/« points » attribués à la glose (443-14 #6, 443-19 #9/#18, 443-24 #0, 444-02 #0, 444-06 #2).
- F16 jamais utilisé par T2/T3 : les 6 à haste droite sans barre sont notés F12(?) par cohérence.
- 443-06 #11, 443-09 #25, 443-17 #14, 444-01 #8 : même signe « boucle + trait descendant à gauche » (ϙ) noté F29(?) faute de meilleure forme au catalogue.
