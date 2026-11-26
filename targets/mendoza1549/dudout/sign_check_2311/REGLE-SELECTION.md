# Règle de sélection — planche « Mendoza 1549, c. 44r » du 23/11/2026 (cible cyphersolver mendoza1549), écrite AVANT toute construction de vignettes

Pièce : Modène, Biblioteca Estense, Autografoteca Campori, Hurtado de Mendoza, sfasc. I, c. 44r (Mendoza à Ferrante Gonzaga,
Sienne, 3 avril 1549). Image : assemblage des 12 tuiles natives du 04/11 (SPOF_2 …/mendoza-gonzaga-1549/planche-2311-src/
c0044r_stitch.png, SHA256SUMS ; coordonnées = image assemblée). Images Estense : étude privée seulement, jamais republiées.
🔴 Cible d'un tiers : mendoza1549 est de LcCompany (PR #519 mergée, contribution WAINUT ; Brice crédité pour l'identification
de c. 42r). Étape 0 (23/11) : `gh pr list --search mendoza1549 --state all` → #519 seule ; profil main = clone f280c87b99.
Le résultat sera PROPOSÉ à LcCompany/WAINUT (commentaire ou PR, crédit LcCompany + WAINUT + relecteur Brice) ; rien chez eux.
Base : targets/mendoza1549 (SIGN_CONVENTIONS.md, transcription_44r.txt, align_44r.txt, NOTES.md « Shape splits ») :
`x` vaut de (8 lieux) et no (6), `o'` vaut ga (3) et ta (2) — « probablement deux formes voisines fusionnées ».

## Critère
Les deux scissions de forme les plus fréquentes du NOTES (x, o'), seules à donner ≥ 5 lieux ; à l'image (×0,9, 23/11) deux
formes se voient : x « rond » (deux courbes jointes) et x « bouclé » (grand ꭓ à boucle montante) ; o' « petit rond » et
o' « plat et large ». Pour chaque scission : 2 lieux (un de chaque valeur) servent d'EXEMPLES, tous les autres sont des cibles.
Les cinq autres scissions (n, lo, q', 9, e : 2-3 lieux chacune) : hors planche (exemples trop peu nombreux pour séparer).

## Cibles retenues (13) — index de signe à partir de 0 dans transcription_44r.txt
x : **X1** L05 s22 ; **X2** L06 s18 ; **X3** L07 s19 ; **X4** L08 s17 ; **X5** L12 s9 ; **X6** L13 s8 ; **X7** L13 s26 (dernier) ;
**X8** L14 s1 ; **X9** L14 s15 ; **X10** L15 s20 — options : x rond / x bouclé.
o' : **O1** L15 s3 ; **O2** L15 s13 ; **O3** L16 s12 — options : o' petit rond / o' plat.

## Contrôles nets (2), signes sans ambiguïté de forme
- **K1** L08 s1 ω (w) : ω / mo, attendu ω. **K2** L12 s3 mo : ω / mo, attendu mo.

## Alphabet (exemples ; jamais une cible ni un contrôle)
x rond : L03 s13, L08 s4 ; x bouclé : L03 s14, L05 s4 ; o' petit rond : L06 s6 ; o' plat : L16 s7 ; ω : L12 s2 ; mo : L08 s2.
Boîtes vérifiées sur planches-contact de travail (scratchpad, 23/11) puis crops/_contact.jpg.
Page : un seul signe encadré ; aucune glose ; « forme n » ; titre « Planche D ». Options texte habituelles. Ordre : planche_core v2
(copie P2, vignettes agrandies), graines 20261123 / 1549. Export : reponses-2311-mendoza.json.

## Intégration (après réponses, sur une copie locale ; rien n'est écrit chez LcCompany sans leur accord)
1. Un contrôle raté (y compris « impossible à distinguer ») → rien intégré ; noté dans HANDOFF.
2. Si chaque cible x reçoit la forme qui correspond à sa valeur d'alignement (rond = no, bouclé = de) → la scission x est
   CONFIRMÉE à l'image : proposer deux noms (`x` / `xo`) et une valeur unique chacun ; les « repairs » portés par x tombent.
   Une cible contraire ou « impossible à distinguer » → la scission n'est pas tenue pour ce lieu ; noté.
3. o' : même règle (petit rond = ga, plat = ta). 4. Aucune valeur nouvelle n'entre par la planche ; recompte selon #728 sur
   copie, entrée HANDOFF datée ; proposition à LcCompany (crédit).
