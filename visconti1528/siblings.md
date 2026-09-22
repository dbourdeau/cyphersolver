# Sibling letters in the Visconti cipher: first pass (escalation step "siblings")

## Where they are

| letter | Gallica ark | view | local file |
|---|---|---|---|
| BnF fr. 3045 f.28 no.24, Visconti to Angelo Bolano, Alessandria, 15(?) Oct 1528 (clear date line reads "ali XV de ottobre 1528") | ark:/12148/btv1b9060156p | f54 (single leaf; the address leaf "A m. Gio Angelo Bolano ... a Mons. de Vilandry" is f55) | siblings/fr3045_f28_v54.jpg (4433x5861) |
| BnF fr. 3096 f.91 no.47, Visconti to Francis I, "in campo in la pieve de Loccate ali XV(?) de Giugno 1529" | ark:/12148/btv1b9060015d | f94 (double-page opening; f.91r is the right half, x > 4300) | siblings/fr3096_f91_v94.jpg (8667x5879) |

fr. 3045 f.28 has 21 cipher lines, then a clear close: "che sarà la fine de la mia, cum ricomandarme ala sua bona gra[tia]. Da Alexandria ali XV de ottobre 1528", signed "W[?] Galeazo". fr. 3096 f.91r has about 22 cipher lines opened in clear ("Syre: Sapendo ..."), then a clear close ("Syre, io suplico V[ost]ra M[aes]tà cum tuto il core mio che me facia pagare in mane del mio li mey duoy quarteri; ne puosso più vivere per la fede et sacramento li porto et debio; che sarà la fine, cum pregare Dio che doni a V[ost]ra M[aes]tà buona et longa vitta. Dat[um] in campo in la pieve de Loccate ali XV de Giugno 1529").

Both hands use the same sign set as fr. 3034 f.154 (ψ, 7, ∂, ne-sign, me-sign, far, crossed ψ, y, n, k, θ, rr, qq).

## Key check on a sibling line

fr. 3045, last cipher line: `far n y ne 7 y a d n e y ψ ψ ψ n p 7 me a k a 7 a p d y a n`. With the merged key the end reads
`p 7 me` = MAL and `a k a 7 a p d y a n` = TRATAMENTO, giving **"mal tratamento"**. That confirms a=T, k=R, 7=A, p=M, d=E, y=N, n=O, me=L on a second letter.
fr. 3045 line 9 (strip s45_2): `far d ∂ ψ ne o d k 7 a` = CHE D I S P E R A T, **"che disperat[o/a]"**. That confirms ∂=D, ψ=I, ne=S, o=P.

## Findings on the open items

1. **Person codes. The "crossed psi" is a crossed 4, so the codes are two-digit numbers (4x).**
   - fr. 3045 line 1 opens `Bolano · 4 2 · ne n me ...`. The first cipher group after the addressee's name is a numeral pair, **42**. Its first sign is the same crossed stroke as the 3034 "ǂ".
   - fr. 3096 f.91r, cipher line 9: `lsp me 7 f θ 7 a L · ∂ ψ 4 8 p 7 f l n me ...`. Here **∂ψ 48**, "di [48]", stands in the King's letter. It is the same group as 3034's "a casa de [ǂ8]", and its second sign is a clear figure 8.
   - So 3034's ǂ8, ǂθ and ǂr are best read as numeric code groups 48, 4θ(=4 + a digit-like sign) and 4r. They are person/place codes from a numbered nomenclator, not letters. The ǂ = O reading in "opinione" (r02) should be re-checked: the plain cipher may have a separate crossed-psi O, or r02 may carry a code.
   - Who 48 is: the siblings do not name him in clear. In the 3096 letter 48 appears in a letter to Francis I in 1529, so 48 is a person active in the Lombard war in both 1528 and 1529 (e.g. Saint-Pol or the Duke of Milan's side). **Identity still open.**
   - **peu**: no occurrence found in either sibling on this pass. It stays unresolved. (3096 is addressed to the King, who would be "V.M." in clear, so a King-code would not be needed there.)
2. **so/lo/do final pair (y Y')**: not found in the siblings on this pass. Open.
3. **One-off signs**:
   - **rr is a recurring group**, not a one-off. In fr. 3045 it occurs at least 3 times: line 1 `... ear rr ne 7 s n y L.`, line 11 `rr me ...` and line 12 `. rr ne d 7 y ∂ ...`. In fr. 3096 it occurs twice: line 3 `... yn rr ∂ k ψ lsp ψ me ...` and line 10 `... ψ ne ∂ 7 ψ rr ∂ ψ k n ...`. In fr. 3096 line 3 it carries an overbar like a code group. This supports reading 3034's [r r ᵽ] (r21) as the code group **rr** followed by one sign, and the small r of [ǂr]/[Y r] as a code element. The value of rr is not established.
   - **qq is a group**, recurring in fr. 3045 line 13 `... ψ y L · qq me ψ me 7 y l d ...`. This argues against 3034's "[q q]uolse = volse" (two q's = V). Treat qq as a code group, with "uolse" read separately or not at all.
   - [mur·][ω], [v b], Π: no clear occurrence seen on this pass, so nothing proves them nulls.
4. **+ (O or A)** and **q = H/F by shape**: not settled on this pass. q in both siblings is written as a 9-like loop (fr. 3096 line 3 `ψ q 7 k L`, line 4 `q d ∂ ∂`), with no F-shaped variant distinguished.

## Not done (for the next pass)
A full glyph-by-glyph transcription of both siblings. The line strips are reproducible from the native files: fr. 3045 text block x 450-4350, y 1150-5700; fr. 3096 f.91r x ≈ 4540-8270, y ≈ 300-3300. The next pass should decode the 42/48/rr/qq contexts in full, to identify the persons and check whether peu occurs.
