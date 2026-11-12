# Blind second reader (R2) notes. b64 Part 1
Reader: Claude subagent, blind. Opened ONLY the 8 page images copied from b56/img (c31r..c34v). Did not open b56 tx/, work/, scripts/, LOG, crops, or any decipherment. No IIIF tiles fetched: the copied images are already ~3000x4250 px, signs ~60-80 px tall, which was enough.

## Scope
- Cipher text found on c31r (22 lines, letter of 4 Nov 1537), c31v (14 lines, continuation; then autograph plaintext postscript), c33r (17 lines, letter of 8 Nov 1537; then autograph plaintext). c32r/v, c33v, c34r/v: address leaves, no cipher.
- Plaintext (not transcribed as units) [measured, read from image]: c31v: "havendo pensato che a questa V. Ex.tia havera havuta la zifra ho scritto questa in la qual ... mi trovaret[e] qualche cosa ... basandoli le mani humilmente mi li racc.o di San Secondo li iiij di gbre 1537". c33r: "et a V. S.ria ... humilmente basando le mani mi li racc.o et p[re]go dio la conservi felicemente ... di Sansecondo li viij di gbre". Address leaves: "Al Ill.mo et Ecc.mo S.or et Pron. S.or Don Ferr.do Gonz.a vice Re di Sicilia. In Messina o dove sera."
- Line centres (px, full image) used for crops: c31r 1338..3850 (22), c31v 685..2210 (14), c33r 1467..3591 (17).

## Method
Line strips at 1.0x and zooms at 1.1-1.6x (scripts/strips*.py, crop.py in b64/scripts). Each line read left to right; colon written after a sign is kept as its own unit 'co'. Every line was cross-checked across the overlap of adjacent strips.

## Totals [measured, from R2.txt]
2,521 units on 53 lines; 57 flagged doubtful ('?' suffix or bare '?').

## Look-alike splits made
- HAT vs TICK vs plain: P = large hook curling over top; R = small tick/flag at top or separate tick; I = plain upright (nearly always + co); G = flat-topped Γ (2). D = closed bowl + hooked ascender. The P/R boundary is the weakest split: most hats are clearly large; R was given only where the top was a short flag. Many R are marked '?'.
- Bowls: q (closed bowl, straight descender) vs 9 (open top) vs PH (stem rises through/above bowl) vs Q (circle with crossed descender, doubtful). q/PH split is shaky at this resolution where ink is heavy.
- TH (closed oval with bar) vs 6 (open curved top): 6 only 3 times (c31r.15, c31r.16, c31r.22).
- U (u with left-curling tail) vs V.
- 8 vs S vs 5 (flat top).
- T (upright on base bar) vs bare '_' (2).
- F (small loop+cross) vs E (big loop rising to tall hooked ascender).

## Known weak spots
- c31r.22 is faded; c31r.06 and c31r.13 have ink blots ('?').
- 'f u i t' at start of c31v.10 looks like Latin script letters, perhaps a plaintext word or alphabetic signs. Kept as 4 units with '?'.
- Ambiguity in segmentation: 'I co' might be one sign (I with colon); 'co' after other signs might be a diacritic. Kept separate.
- Repeated strings noted (consistency check, not decipherment): c33r.03 "S T pm q P T H Z P co TH D co T Z co H" = c33r.09 same string; c33r.13 "S Z co 7 F co S" ~ c33r.16 "S Z co 7 F co S T"; "V co D H I co I co H" c33r.16 ~ c31r.04 "V q? D H I co I co H".
