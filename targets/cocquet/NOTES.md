# Cocquet → Mangot, Rome, 13? November 1616 (BnF Clairambault 369, ff. 316-317)

Session 2026-09-16. Gate check only: fetched, measured, not attacked.

## Source

- Tomokiyo, *Ciphers during the Reign of Louis XIII* (cryptiana `louisxiii.htm`): "BnF Clair 369 (Gallica) contains a
  partially enciphered letter dated Rome, 13? November 1616 from Cocquet to Mangot (f.316). It is not deciphered." His
  image `BnFClair369f317.png` (632 × 456) is in `../../research/gallica_siblings/src/`.
- Gallica: Clairambault 369 = `ark:/12148/btv1b9000782k`, 359 canvases, all labelled NP. Canvas 322 shows f. 310, so
  **f. 316 is canvas 328 and f. 317 canvas 329** (right pages; f. 316v on the left of canvas 329). Full-resolution IIIF
  images (about 6100 × 5000) saved as `img/c328_f316.jpg`, `img/c329_f317.jpg` (git-ignored); cipher block
  `img/block.jpg`; strips `lines/R01.png` … `R12.png`.
- f. 316 is entirely in clear (Turin and Savoy news: Béthune, the Grand Duke, the Duchess of Mantua, "la Royne" — Marie de
  Médicis). The cipher sits on f. 317, in the lower half, interleaved with clear French:
  "… que la Roy[ne] estoit mort a Millan … [86 …] … Cet homme est dangereux et mal[icieux?] … que le meschant discours
  … qui le poussent a faire ce qu'il fait … Vous me pardonnerez Monseigneur, si j'ose vous dire que le mo[y]en …
  y aura moyen qu'il sache ces affaires, ce sera le meilleur … soit faire la guerre … et encores a … ne tend a autre
  but que de pouvoir …" and a last cipher line with a flourish. Cribs are plentiful; the cipher runs are short.

## Measurement (the gate)

| | |
|---|---|
| Cipher runs | 9 (two full lines, the rest half-lines between clear phrases) |
| Tokens | about 150-170 glyphs (segmentation into units uncertain: letters run together in the hand) |
| Alphabet | letter shapes and ligatures (ſ, s, g, y, l, d, q, z, w-like ω, π, ct, ſt, a crossed t, a 8-with-tail ϑ, ⌗, $) with a few figures (86 ×3, ·89, 2, 4, 5, 6, 8) |
| Recurring units | "pu" (≥ 8), "ot" (≥ 6), ϑ (≥ 10), 86 (3), "ſq", "dq", "ϑd" |
| Marks | underlined pairs "y z" (twice) and an underlined "c"; ö with two dots (twice) |
| Distinct units (provisional) | about 40-50 |

## Key-application test

Tomokiyo reconstructs three ciphers from the same volume — de Baugy (f. 109: figures with umlaut, letters and syllables),
de Castille (ff. 11, 13: letter and ligature homophones, Caesar-like, nulls) and Du Maurier (ff. 229, 294: two-figure
syllabary) — and two anonymous keys from Clair 372 f. 169 and Clair 373 f. 303 (images in `../../research/gallica_siblings/src/`).
None matches on sight: Baugy and Du Maurier are figure ciphers, Cocquet's is mostly letters; Castille's repertoire
(4, θ, //, ⊕, ∂, ſ, ſſ, q, ⊤, Ϫ …) shares only the generic ſ/q/g shapes, and its word codes (numbers 14-99) are not what
the plain numbers here look like. The anonymous Clair 372/373 keys use different letter forms and numeric word codes.
Not run as decodes — the repertoires do not overlap enough to map more than a handful of glyphs.

## Verdict

Not attacked. About 160 tokens over 40-50 units is the du Croc regime (`targets/ducroc/`: 147 tokens, 40 symbols), where the
matched homophonic control was recovered at 28-41 % — below threshold without segmentation or a key. The cribs in clear
are the one lever (the runs sit inside French sentences whose gaps are constrained), but each run is 5-20 glyphs and a
crib-fixed anneal at this length cannot be validated against a control. **Below threshold; closed at the gate.**

What would reopen it: another Cocquet letter in the same cipher (Clair 368-373 hold the 1616-17 Mangot correspondence;
a contact sheet of canvases 280-359 of Clair 369 at 400 px was made but is too coarse to spot cipher — not checked), or
the ambassador's key (the French embassy in Rome in 1616 was the marquis de Trainel's; Cocquet is presumably an agent or
secretary — not identified here).

## Files

- `img/`, `lines/` — git-ignored; regenerate from the IIIF URLs above.
- Contact sheet: `../../research/gallica_siblings/src/clair369_sheet/sheet.jpg` (git-ignored).

Checked: canvas identification, clear-text frame, run and token counts, repertoire comparison with five period keys.
Not checked: unit segmentation, a labelled transcription (not made), sibling letters in Clair 368-373, Cocquet's identity.
User must verify: the counts before quoting them.

## Second pass, 2026-09-16 evening: sibling and key search — closed, not solvable online

- **Not in DECODE.** Searches for "Cocquet", "Mangot", "Trainel" return nothing; "Clairambault" returns only Clair 325
  (1526), 417, 574, 577 and 580 (1645-68). No Clair 368-373 record exists there, so no transcription or key has been
  deposited for any of the 1616-17 Mangot correspondence.
- Tomokiyo's Louis XIII article names no second Cocquet letter; the only Rome item is this one. The three reconstructed
  Clair 369 keys (Baugy, Castille, Du Maurier) and the two anonymous ones (Clair 372 f. 169, Clair 373 f. 303) were
  compared above and do not share the repertoire.
- With ~160 letter-shaped glyphs in nine runs, no sibling and no key, there is no key-matching test left to run and no
  ciphertext-only attack that can be validated (du Croc regime, see the gate above).

**Verdict: not solvable with what is online, 2026-09-16.** Reopen only with a second Cocquet letter or the embassy key.

Checked: DECODE search index for five terms, Tomokiyo's Louis XIII page for other Cocquet/Mangot items. Not checked:
a page-by-page scan of Clair 368-373 for further Rome letters (the 400-px contact sheet of Clair 369 canvases 280-359 is
too coarse). User must verify: that Cocquet's identity and the Rome embassy key are not documented elsewhere.

## 14 Nov 2026: labelled transcription and family lead (Brice Dudout's agents)

- **Transcription** (`transcription_f317.txt`). Image: Gallica view 329 at full size (6124 x 5431; Source gallica.bnf.fr / BnF).
  Two blind passes by independent agents from the image only (188 and 187 cipher tokens; neither saw the other),
  compared sign by sign; disagreements were settled on 2-4x crops. Result: **186 cipher tokens in nine lines,
  about 45-50 distinct signs**, nine places left as `{x|y}`. The passes agreed on segmentation almost everywhere;
  the main label differences were naming only (the small flat-topped 8, here `B`, and the round d).
  Settled on the image: the last sign of line 1 has two bars (T2, probable); line 2 has a three-bar sign followed by a
  two-bar sign; the two signs after "a" in line 5 are the clear abbreviation "f[air]e", not cipher; the dot-slash
  marks at the end are punctuation. Open: whether "soy" in line 8 is clear or cipher (+3 tokens).
- **Repertoire** (most frequent): round d 16, B 13, PU 12, theta 10, infinity loop 9, `ot` 9, q 8, L 8, I 7,
  underlined pi 6, g 6, s 6, $ 6; numbers 86 (three times) and 89; o with two dots (three times); underlined y, n, C.
- **Family lead, not measured.** Tomokiyo's reconstruction of **de Castille's cipher (Clair 369 f. 11, 1616)**,
  `../../research/gallica_siblings/src/louisxiii_Castille.png`, is built the same way: letter homophones drawn as
  d, theta, H, eta, q, g, long s, a barred ff and a barred #, pi among the nulls, two-digit syllable codes in the
  73-99 band (85 con, 88 de, 89 di, 93, 99 est), and digits with two dots for syllables. Cocquet has every one of
  these classes (86 x3, 89, o with two dots, pi, theta, round d, H, eta, q, g, long s, barred ff). Baugy and Du
  Maurier are figure ciphers; the Clair 372/373 keys use numeric word codes. This revises the 16 Sept note
  ("only generic shapes"): the overlap is in structure, though Cocquet's values may differ from Castille's.
  Castille's key was **not** applied; it is the first test to run (one held-out measure against shuffled keys).
- Not done: a quantitative family test (sign-set overlap against shuffled witnesses); it needs Castille's key
  transcribed with the same labels.
