**CONFIRMED-BUT-OVERSTATED.** The French skeleton is convincing; 96.7% strictly gloss-attested coverage is overstated. This review is conditional on the supplied transcriptions, not independent manuscript inspection.

My parser rebuilt the key from 11 May ALIGN and 28 May SEG data without executing the authors’ programs or training on May 25. It recovered 524 and 677 assignments, respectively, rather than reproducing the claimed 679 for May 28. Normalization folds i/j/y and u/v; uncertain glyph labels remain an upstream limitation.

**Strict:** 57/61 claimed token values have direct matching attestations: **93.4%**; 56/61 have at least two: **91.8%**. Top-value agreement is also 57/61. Discrepancies: #19 `q_` gives **qui**, not **po**; #22 `42'` lacks an exact-label attestation; #12 `47'` and #61 `45'` are unidentified. The q notation may conflate distinct glyphs. Theta=f occurs once, hence M; C requires equating it with May 28’s B. Per-letter provenance covers 54/61 positions in May 11 and 56/61 in May 28.

**Generous:** accepting `42'=42` gives 58/61 (95.1%); additionally inferring `q_=po` gives 59/61 (96.7%); guessing Essex gives 60/61 (98.4%). The latter two additions are not directly gloss-attested values.

Validation reproduces **281/330=85.2%**, H **252/274=92.0%**. Fixed top values yield only **270/330=81.8%**. The algorithm selects alternatives against the answer, skips reference letters, and absorbs mismatches. Tokenization is not identical: cipher syllables/names versus running text; `...` is counted, and A19 is incomplete. Excluding the ellipsis gives 281/329. List A is a separate historical witness, but modern blindness/post-hoc editing cannot be audited without frozen versions. The final q_ evidence explicitly cites April; excluding it gives 279/330. Assuming comparable difficulty, H errors project to **4.1 among 51** target H tokens; restricting validation to target H types gives **2.5**. Thus 85% validation neither proves nor directly contradicts 96.7% attestation coverage.

Both 2,000-trial controls reproduce: real **0.838**; shuffle mean/max **0.395/0.667**; key permutation **0.401/0.726**. Removing custom words retains significance. However, free-gap dictionary segmentation rewards accidental fragments; key permutations change length from 105 to 99–212 letters. Length-preserving permutations also remain below real (maximum 0.619). These test structure, not grammatical correctness.

Phrase grades: first bracket **PLAUSIBLE**, with unresolved name/q; second **SOLID as a lexical skeleton**, retaining `{45'}`. *Par toute voye* is a plausible spacing; pronoun and following denunciation-clause attachment remain uncertain. Essex is **SPECULATIVE**; theta=f **PLAUSIBLE**, singly attested.

Illustrative 95% Wilson intervals: 57/61 **84.3–97.4%**; 59/61 **88.8–99.1%**; 60/61 **91.3–99.7%**. None establishes >95%; repeated symbols violate independent-trial assumptions.

Fixes: distinguish q glyphs, downgrade inferred entries, preserve unidentified names, freeze the key/transcription before fresh validation, and report coverage separately from accuracy. Scripts, token-level evidence, decoded output, and detailed limitations are saved alongside this review.
