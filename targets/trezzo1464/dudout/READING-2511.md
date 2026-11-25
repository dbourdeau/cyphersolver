# trezzo1464: a person's look at ten signs of f. 392 (plate 2511) and what it changes

Plate: `sign_check_2511/` (hashed rule, frames, key written with the plate, answers as given, results). A person (Brice
Dudout) chose, for each boxed sign of view 393, the closest of three shapes cut elsewhere in the same hand, without any
value or reading shown. **Controls: 3 of 3 passed.** No remark.

## Labels: what the answers settle
| shape | answers | consequence for the transcriptions |
|---|---|---|
| p7 vs pz | p7 at both places asked (392.06 #26, 392.07 #15) | c392 was right; keep p7 (s) apart from pz (t). Our own pass had lumped them. |
| hr | hr at both places (392.10 #27, 392.13 #20) | c392 right (ell). |
| 4e | 4e at both places (392.04 #3, 392.06 #20) | c392 right (es). |
| long r vs y | r (392.10 #20) | c392 right. |
| δ^u vs δ~ | δ^u at both places asked (392.07 #10, 392.09 #14) | **c392 lumps δ^u into δ~ here.** The other δ~ of c392 (5 on f. 392, 20 on 283r, 19 on 283v-284r) should be looked at again: δ^u aligns with "on", δ~ with "or". |
| L with a caret | 392.10 #14 is none of L, L^a, L^u | a separate form (L with a caret, like the ^ sign written above); c392's L^a there is doubtful. |

Patch proposal (not applied to `c392.txt`): `c392-planche-2511.patch` (392.07 #10 and 392.09 #14 δ~ -> δ^u; 392.10 #14
L^a -> L^a?). `docs/_check_profile.py trezzo1464` is unaffected (the patch is not applied).

## The sense reading of f. 392 after the answers
With the key top values (`decode392_keytop.txt`) and h = qu where the next signs spell quest-/quell- (the refine step had
turned h into "non" at these places). Values taken from sense only are marked {probable}.

| place | signs (c392) | before | after |
|---|---|---|---|
| 392.04 | h 4o 4e pz δo cs o- δ^u | "...arestitucione" | unchanged, 4e confirmed: "...restitucione" |
| 392.06 | ... 4e δ 4π o- oo 4e p7 4π o7 | "desiderio essere" | unchanged, 4e and p7 confirmed |
| 392.07 | q~ 4^a y o- **δ^u** | "electior(e)" | "electione" {probable} |
| 392.07 | h **p7** pz oo | "non s t o" | "questo" {probable} |
| 392.09 | **δ^u** pz ar y | "or t en t" | "(c)ontent-" {probable} |
| 392.10 | q~ r 4^a **r** 4a oto | "el r ec r et o" | unchanged, r confirmed: "-creto" (decreto/secreto) |
| 392.10 | h **hr** o~ | "non ell e" | "quelle" {probable} |
| 392.13 | h **hr** op a | "non ell a u" | "quella" {probable} |

Count: the fragments NOTES lists (8: "...amente", "restitutione", "quali hanno effecto", "desiderio essere", "alcuno
che", "la S.V.", "amici", "nella") become 13 with "electione", "questo", "contento", "quelle", "quella", all {probable};
about 13 words out of roughly 120. Still no sentence: **decoded, not read** (no change to the profile).

On ff. 283r-284r (the key material) the answers change no reading by themselves; they say which labels of c283/c284
need a second look (above all δ~, 39 tokens, and the 168 `p` tokens NOTES already names).

## What is left before a measure
1. Re-transcribe 283r-284r and 392 with the finer inventory (p7/pz, δ^u/δ~, hr, 4e, long r/y, L with a caret), then
   re-run the aligner on the whole 16 July letter.
2. A fresh portion for the measure: f. 392 has been used for our own measure of the #648 key (25 Nov, failed, not
   claimed), so a measure has to be made on another Trezzo letter of 1463-1464 (italien 1589 ff. 245 and 288 are not yet
   transcribed anywhere), with the metric and threshold written before any decoding.
