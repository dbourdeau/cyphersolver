Status: in progress (Brice Dudout, 9 Nov 2026; the Cobham alphabet passes a held-out test on DECODE R8489 f. 78v, 0.917 vs best of 200 shuffled keys 0.284; codes 22, 26, 27 and the square identified from the f. 78r gloss; R8490 cipher re-read in part: 35/43 cipher words = 81% (21 sure, 14 probable, 0 restored, 8 unresolved), 41/49 = 84% with the codes, below the 95% rule). Next step: the 8 unresolved words of R8490 (ll. 9, 10, 12, 19, 33, 34), then R8492.

# Cobham 1588: an independent check of the key, and four codes (Brice Dudout, with Claude)

A contribution to Daniel Bourdeau's target `cobham1588` (catalogue 131). Daniel's files are not changed; this folder adds
a held-out test of the alphabet and the codes glossed on f. 78r. No image, crop or derivative of the DECODE / British
Library scans is included: only text. Sources: DECODE R8489 (https://de-crypt.org/decrypt-web/RecordsView/8489) and
DECODE R8490 (https://de-crypt.org/decrypt-web/RecordsView/8490).

## Held-out test of the alphabet

- Protocol written and hashed before any measurement (`frozen/PREREG-cobham-1588.md`, in French, SHA-256 in
  `frozen/SHA256SUMS`; addendum A1).
- Key learnt **only** on the cipher words of f. 78r (R8489, Ostend, 16 April 1588) aligned with their contemporary
  interlinear gloss: about 70 glossed words, 22 signs (`frozen/R8489_f78r_entrainement.tsv` -> `key_R8489_f78r.tsv`).
  Daniel's `signs.tsv` was used for the sign names only, not for the values.
- Held-out part H = every glossed cipher word of f. 78v whose sign count equals the letter count of its gloss:
  76 words, 349 letters. The cipher of H was written and hashed (`frozen/R8489_f78v_H_chiffre.tsv`) before the gloss
  file (`frozen/R8489_f78v_H_gloses.tsv`).
- **Single measurement** (main value of each sign; `frozen/RESULTAT-mesure-H.txt`): character agreement **0.917**;
  200 keys with the value column shuffled (seed 20261109): best 0.284, mean 0.047. Criterion fixed in advance:
  >= 0.85 and >= best witness + 0.30 (0.584): **passed**. Word agreement 0.684 and set agreement 0.997 are reported,
  not decisive. Every error comes from the two shared signs already known (caret = s/t, gamma = r/y) and from d = o,
  absent from f. 78r.
- **Declared deviation**: the crops used to transcribe the cipher of f. 78v also showed the interlinear glosses
  (they sit just above the cipher lines). The key had been frozen before; the risk is a bias in the reading of a few
  ambiguous signs.

This confirms, on letters not used to build it, the alphabet that Daniel rebuilt from the glossed siblings.

## Codes glossed on f. 78r (new for this target)

| code | gloss on f. 78r | identification |
|---|---|---|
| 22 | "Sr J: Croftes", over "22 hath many crochettes in his head" | Sir James Croft, Controller of the Household, one of the five commissioners |
| 27 | "D: Dale and D: Rogers revoked ...", over "27 and 26 [revoked] and [others in their places]" | Dr Valentine Dale (first name of the gloss, first code) |
| 26 | same gloss | Dr John Rogers (second name, second code) |
| square | "ye States", after "to" (twice) | the States (General); probably the same code sign as the square of f. 80r, not checked there |

27 = Dale and 26 = Rogers follow the order of the gloss; the gloss covers the phrase, not each number.

## Applied to Daniel's reading of R8490 (f. 80r-v)

- f. 80r: "*[22: Sir James Croft]* is so *forwarde* yn the *action* that he promised Q[ueen] to *send to {Bruges} [27: Dr Dale]*
  to begyn the *openning of the [...]*".
- f. 80v: "*[22: Sir James Croft] hath a desire to retourne* from theym".

The two sentences gain their subject. Second pass the same day: see below. Historical sense only: Croft pursued his own contacts with Parma in 1588 and was imprisoned
on his return; Dale and Rogers were the two civil lawyers of the commission.

Prior work re-checked 9 Nov 2026: Daniel's target (the alphabet, codes 7, 10, 15, 16); DECODE marks R8489 "Decrypted"
(the gloss of the time, so nothing is claimed on R8489's text); no printed decipherment found (CSP Foreign 21 pt 4 does
not calendar these Harley letters, per Daniel's notes).

## R8490 cipher re-read in part (second pass, 9 Nov 2026)

Every cipher word of ff. 80r-80v (43 words + 6 codes) transcribed and hashed before decoding
(`frozen/R8490_chiffre.tsv`), decoded with the frozen f. 78r key unchanged (`frozen/R8490_decodage_cle_gelee.txt`),
new values only in a declared derived key with attestations and strengths (`frozen/cle_R8490_derivee.tsv`; not measured).
Word table, classes and passages: `reading_R8490.md` (the French working file is `frozen/LECTURE-R8490.md`).

- **35 of 43 cipher words read by sense = 81%** (21 sure, 14 probable, 0 restored, 8 unresolved); with the 6 glossed
  codes 41/49 = 84%. Below the 95% rule: R8490 is read in part.
- New: *send to {Bruges} [27: Dr Dale]*; "yt will *not be {kept}*"; *{treat} of {Breda}* letter by letter (b-r-e-d-a);
  *subiect* in the singular; *{termes}*.
- Sign distinctions: the small closed o = d (not ∞'s twin), the barred-c sign = o, d = o throughout.
- Unresolved: l. 9 (where forces are drawn from), l. 10 "...ances", l. 12 the state of the haven, l. 19 the verb
  ("to [...] ther surti"), l. 33 two words, l. 34 the mayor of [...].
