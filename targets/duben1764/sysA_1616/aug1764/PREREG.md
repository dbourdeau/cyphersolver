# PREREG — key_c02 on the 20/31 August 1764 letter (Chiffer n:o 1, system A)

Written 17 Nov 2026, BEFORE any look at the full-size images 110-117 in this session, before any transcription of the
August cipher or of its clear, and before any decoding of it. Brice Dudout's session (Claude Opus 5.5, AI agent).
Frozen by SHA-256 (`SHA256SUMS-PREREG`). Any change after this point goes into a dated amendment below, never into this text.

## Key (frozen now)
`../keyc02/key_c02.json`, SHA-256 `1813621c87e836f3b20610b544239e892726b419ea5a02fc9ff71fa768b87285`.
324 groups, 306 with a value (key_c01: 217 / 197). Built from key_c01 by (a) a monotone alignment of four system A letters
with their contemporary clears (letter 96 + 100R / L096; 6 Mar 1764 101R-102L / 102R-103L.08; 15 June 1764 108R-109L /
109R-110L; 15 Nov 1765 / its interlinear gloss), with the acceptance rule written in `../keyc02/scripts/learn_iter.py`;
(b) values read by sense in the undeciphered letter 90R-93L, each checked against the alphabetical place of the group in
this one-part code (`../keyc02/additions_from_90R-93L_sense.json`); (c) 16 single-occurrence values set by hand from the
training alignment where the alphabetical place agrees. Every change is listed in `../keyc02/key_c02_changes.json`.
No group, value or text of images 110-117 was used. No value is added, removed or corrected before the measure.

## Material (never used by either key)
- Cipher: the number lines of the letter of 20/31 August 1764 ("Votre lettre du 3 de ce mois ...", INVENTORY), images
  110R-115 of Riksarkivet K 259 (IIIF A0073297), EXCLUDING the lines of 110R that end the 15 June 1764 letter (NOTES,
  14 Nov 2026: three lines at the top of 110R and four inside a clear paragraph; they are placed by the June clear 110L).
  If the boundary between the two letters on 110R is not clear on the image, all cipher on 110R is left out.
- Clear: the contemporary decipherment on images 116-117 (archivist's note "Till chifferbrevet av 20/31 aug. 1764"),
  all of its text as written, nothing removed (extra text in the clear does not lower CA, see below).

## Preconditions, checked on the images BEFORE transcription is frozen, without any decoding
1. The archivist's note on 116/117 names the 20/31 Aug 1764 letter, and the cipher pages carry that date or are bound
   with it as one letter (date line, "Mon cher Comte", continuity of pages).
2. The cipher of the letter has at least 300 groups of 100 or above, and the clear at least 300 letters.
3. The numbers are system A (groups 1-~760 with nulls below 100; not the Chiffer n:o 2 profile).
If a precondition fails, the measure is NOT run, the portion is not burnt, and this is reported.

## Transcription (before decoding)
Two passes of the cipher and of the clear: pass 1 by this session; pass 2 by a blind sub-agent that sees neither pass 1
nor any key nor this file. Differences arbitrated on the full-resolution image. The merged files are hashed in an
amendment BEFORE the measure is run. Doubtful groups keep their first reading with "?". This scribe's open 3 is
recorded as written and noted, not normalised, unless the amendment states the normalisation before the measure.

## The one measure
`scripts/measure_aug.py` (frozen here), run ONCE:
- decode every group >= 100 with the first value of key_c02 (unknown group or empty value -> nothing);
- **CA** (decision metric, character level) = share of the DECODED letters that lie in difflib matching blocks of >= 4
  letters between the decode and the normalised clear (a-z, accents stripped);
- M (reported only) = share of the clear letters covered by the same blocks (the metric of check2.py / measure_june.py);
- 200 controls: random permutations of the non-empty values over the groups that have one, `random.seed(17640820)`.

## Thresholds (fixed now; the project default)
**PASS** if CA >= 0.85 AND CA >= (max of the 200 controls) + 0.30. **FAIL** otherwise; a fail is reported as a fail.
For the record (known before this prereg, in-sample or held-out on other letters, not the August letter): CA of key_c02
in-sample is 0.966 (L096), 0.892 (6 Mar), 0.828 (15 June, a transcription with 74 doubtful groups), 0.919 (15 Nov 1765);
key_c01 held-out on 15 June 1764 gave CA 0.655. A held-out CA of 0.85 is therefore not assured.

## After the measure (not part of the test)
The portion is burnt for any later key test. Reading of the August letter is from its contemporary clear (existing
decipherment). The strict reading share of 90R-93L (Daniel's rule: "read" only at >= 95 % of words sure) is recounted
with key_c02, sure words only.
