# duron1911 - validation: declared impossible in advance (not validated)

**The key is not validated, and by our protocol it cannot be.** This was declared before any decoding.

## What was frozen, and when (12 Nov 2026, Brice Dudout's project)

| File | SHA-256 | Role |
|---|---|---|
| T-sanantonio-duron-v1.txt (transcription of the batch, incl. 1777.1-6) | 100db0484fb2ab57fa7e788f2431a104f371de0b31a4fcb500edbb4580ca7e16 | frozen before any key was tried; rechecked on the image 12 Nov, unchanged |
| `PREREG-C06.md` (in this folder, French, verbatim) | e2dcfc2aa369b78f74ab76dbaec114151b9e5ee94d105fcb77c1017515d009d8 | protocol, frozen before decoding |
| measure_c06.py (not included) | e99f7c57082842ac0eee694d8fe0c1aec120460da3a8e526536a5faf27aa0041 | the single descriptive measure of step 1 |
| `MESURE-C06.txt` (in this folder, raw output) | f019088ddf4745af387275d96ed9a7d0dccf0768bd8e4da3baedbaff85b01c3e | result of that one run |

The PREREG covers three pieces (1777.1-6 Durón, 1648.2-3 Gabriel, 1354.1 Luque); only Durón was read. Gabriel and
Luque failed and are not part of this PR.

## The declaration (PREREG-C06, section "Matériel trop court", in English)

Durón has 107 signs, Gabriel 76 coded letters, Luque 44 numbers. No held-out portion of 300 letters or more is
possible, for any piece or for the three together (183 letters). **Declared in advance: no reading in C06 can be
VALIDATED; any reading counts at best as "read in part", without validation, whatever its apparent quality.**

## Step 1: archive keys as they are (one run, `MESURE-C06.txt`)

- Every key of the fonds was tried as is: the "Elisa" shift (+-10 on 28 signs) of the sister telegram 1777.2-6, the
  .tsv cards and the tables of the cards CMXV.16.1557.1 (including the Clave G.A.).
- Statistic: W = share of decoded letters covered by words of a Spanish lexicon (1795.1 OCR + period plaintext + 40
  function words), against 200 random substitutions, each maximised over as many variants as keys tried.
- Rule fixed in advance: "applies" if W >= 0.60 and W - best control >= +0.25.
- Result for 1777.1-6: best W 0.259 (Elisa +10), best control 0.365. **No archive key applies.**

## Step 2: key built on the text (no measure possible)

- A general substitution anneal, with no shift assumption, came out at "...madero de licenciado... reyes retana y
  compañeros... correo detalles". The table it found is a shift.
- A sweep of every shift on six alphabets (26, 27, 28, 28 without w, 27 with ch-ll, 29) then gave one reading only:
  29 signs, +22 (score -10.1 against at best -13.2 for every other shift and alphabet).
- The key was built on the whole text, so nothing is left to test it on. The PREREG failure criterion for step 2
  (under 50 % of signs giving plausible Spanish words) is not met: 102 of 105 text signs do.
- Observed after the reading, **not counted**: shift = header sign 1 - header sign 2, as in the sister telegram.

## Status

**Read in part, not validated.** 15 sure + 3 probable of 19 words (94.7 %; strict 78.9 %). The reading rests on the
sense of the Spanish and on the two independent routes to the same key (free anneal, shift sweep); a second telegram
in the same key, or a period decipherment, would be needed to validate it.
