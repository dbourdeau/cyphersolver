# Règle de sélection — planche « Lope Hurtado 1524 (R9866, R9868, R9869) » du 24/11/2026 (cible cyphersolver lopehurtado1523), écrite AVANT toute construction de vignettes

Pièces : RAH, Colección Salazar A-30 (9/30), ff. 285r-v (R9866, 28 févr. 1524, à Gattinara), ff. 430r-v (R9868, 20 mars 1524,
à Gattinara), ff. 444r-v (R9869, 28 mars 1524, à l'Empereur). Images : DECODE R9866 (I45986 P1-P2), R9868 (I45991 P1-P2),
R9869 (I45994 P1-P2) ; R9867 sans image. Lien `src/` → SPOF_2 …/DECODE-planches-2411 (SHA256SUMS là-bas) ; aucune copie.
🔴 Images DECODE : planche privée seulement, jamais publiée, jamais copiée dans un dépôt ; citer « DECODE R<n> ».
Coordonnées = pixels natifs de chaque image (P1 = page de droite pour f. r, P2 = page de gauche pour f. v).
🔴 Cible d'un tiers : lopehurtado1523 est la lecture de Daniel Bourdeau (re-read b07 du 22/10, recompte #728 du 16/11 ;
nos corrections du 29/10 notées dans NOTES). Étape 0 (24/11) : `gh pr list --search lopehurtado1523 --state all` → #728
seule ; profil main = origin/main 31295a96a3. Le résultat sera PROPOSÉ à Daniel (issue ou PR, crédit Daniel + relecteur
Brice) ; rien n'est écrit chez lui sans son accord. La planche du 20/11 (planche_prive/, lopehurtado1520, AGS) est une
autre pièce : elle n'a posé aucun signe de R9866-R9869.
Base : targets/lopehurtado1523 (texts/R98xx_transcription.md, R98xx_corrections.tsv, R98xx_reading.md, key_merged.tsv,
NOTES « look-alike signs (∂ vs barred ∂, two- vs three-bar crosses, barred m = f or c) needing better images »).

## Critère
Les trois familles de formes jumelles nommées par NOTES, aux lieux où la lecture dépend de la forme. À l'image (24/11,
bandes graduées de travail) se voient : (M) un « m barré » (m avec trait, ex. ofrecio) et un « f long barré » (= `f`, c) ;
Daniel note `m̶` pour les deux → « m̶ = f ou c » ; (D) un ∂ à haste haute barrée, un petit ∂ à crochet sans haste, et le
ʋ (= m) ; (C) la croix à deux traits verticaux (`ʇʇ`, r) et à trois traits (`ʇʇʇ`, b). Une cible par lieu douteux ;
exemples pris ailleurs (jamais une cible ni un contrôle). Lieux à forme évidente (∂ barrés de perdido, puede, provea,
Prospero) : hors planche, servent d'exemples.

## Cibles retenues (12) — lieux de texts/R98xx_transcription.md
M (options : m barré / f long barré) : **M1** R9866 R1 l6 (`m̶` de « ofendido », lu f) ; **M2** R9866 R4 l12 (`m̶` de
« reputacion », lu c) ; **M3** R9869 R10 l4 (f. 444v, `m̶` de « confiança », lu f) ; **M4** R9868 R10 l3 (f. 430v, `m̶`
de « desconfiados », lu f).
D (options : ∂ haste barrée / petit ∂ à crochet / ʋ) : **D1** R9866 R3 l9 (`to ∂ 8 9 ω m`, non lu) ; **D2** R9866 R14 l18
(f. 285v, `∂ 4 8 c`, non lu) ; **D3** R9868 R17 l22 (f. 430v, `ʃu ∂ ⊤ σ`, « se puedan », relu ⊃).
C (options : croix 2 traits / croix 3 traits / ß) : **C1** R9866 R13 l14 (f. 285v, 1er signe, place b de « [?buscarian] ») ;
**C2** R9868 R13 l11 (f. 430v, « obedecele », relu ʇʇʇ) ; **C3** R9869 R11 l6 (f. 444v, `yaf ʇʇʇ φ`, non lu) ; **C4** R9866
R13 l13 (f. 285v, `4 ʇʇ φ`, non lu) ; **C5** R9866 R6 l21 (2e croix de `b ʇʇ ω ʇʇ T̄`, place b de « contribuciones »).

## Contrôles nets (3), formes sans ambiguïté
- **K1** R9866 R14 l17 (f. 285v) `ß` de `c ß zm` : ß / croix 2 traits, attendu ß.
- **K2** R9866 R3 l8 `φ` de `∂ φ 8 9 8` : φ / ω, attendu φ. **K3** R9866 R1 l5 `ω` de `9 ω b m` : φ / ω, attendu ω.

## Alphabet (exemples ; jamais une cible ni un contrôle)
m barré : R9869 R1 l1 (ofrecio), R9869 R8 l21 (ofrecer) ; f long barré : R9866 R4 l13 (cobrado), R9868 R1 l6 (gratificarle) ;
∂ haste barrée : R9866 R3 l8 (puede), R9868 R13 l12 (Prospero) ; petit ∂ à crochet : R9869 R1 l2, R1 l3 ; ʋ : R9866 R7 l24
(enemigos), R9866 R13 l15 (miedo) ; croix 3 traits : R9866 R4 l13 (cobrado, b) ; croix 2 traits : R9866 R4 l13 (cobrado, r),
R9866 R1 l5 (`ton ʇʇ 4`) ; ß : R9869 R10 l4 ; φ, ω : R9866 R4 l12.
Boîtes vérifiées sur bandes graduées de travail (scratchpad, 24/11) puis crops/_contact.jpg. Signe agrandi ≥ 160 px,
vignettes ≥ 130 px ; tout signe illisible agrandi est retiré (noté au HANDOFF), sans le remplacer par un autre lieu.
Page : un seul signe encadré ; aucune glose ; « forme n » ; titre « Planche LH ». Options texte habituelles (aucune / autre
forme, impossible à distinguer, illisible, pas un signe). Ordre : planche_core v2 (copie P2, vignettes agrandies),
graines 20261124 / 1524. Export : reponses-2411-lopehurtado.json.

## Intégration (après réponses, sur une copie locale ; rien n'est écrit chez Daniel sans son accord)
1. Un contrôle raté (y compris « impossible à distinguer ») → rien intégré ; noté dans HANDOFF.
2. M : si M1, M3, M4 (lus f) reçoivent « m barré » et M2 (lu c) « f long barré » → « m̶ = f ou c » est une confusion
   d'étiquette : proposer `m̶` = f seul, et l'étiquette `f` (= c) aux lieux de c (R9866 : cobrado, costa, provechosa…, à
   revoir à l'image par Daniel). Une cible contraire ou « impossible à distinguer » → la double valeur reste pour ce lieu.
3. D : D3 « haste barrée » confirme ⊃/∂̶ = p au lieu. D2 « petit ∂ » → forme distincte de ∂̶ attestée ici : proposer de
   séparer ∂ (t, key « form not yet separated ») de ∂̶ dans la transcription. D1 « ʋ » → proposer la relecture `to ʋ 8 9 ω m`
   (ʋ = m, valeur déjà confirmée) comme piste, sans l'adopter : le mot qui en sort reste à juger par Daniel.
4. C : « 3 traits » en C1/C5 (places b) confirme ʇʇʇ = b et corrige l'étiquette ʇʇ ; « 2 traits » → le trou reste. C2-C4 :
   la forme choisie est notée telle quelle ; aucune valeur nouvelle n'entre par la planche.
5. Recompte selon #728 sur copie seulement ; entrée HANDOFF datée ; proposition à Daniel (crédit Daniel, relecteur Brice).
