# Catalogue 3807: result of the single held-out measure (27 Nov 2026, 13:36 CET)

## The freeze

- **Manifest:** frozen/MANIFESTE-GEL.txt, SHA-256 `be7b18a12362dcfd2926c46b01c988b7140cee806be2c430d359257440cfb82b`.
- **Posted before the measure:** issue #1023, comment https://github.com/dbourdeau/cyphersolver/issues/1023#issuecomment-7218330393. This follows the #1014 convention.
- **Checked before running:** all 12 file hashes matched. To repeat the check, run `cd prereg/frozen && grep -v '^#' MANIFESTE-GEL.txt | shasum -a 256 -c -`.
- **Contents of the frozen files:**
  - PREREG.md, written in French as frozen: the protocol, the portions and the criterion.
  - CLE-K1.json: the key.
  - REGLE-PORTION-RESERVEE.md: the rule fixing the held-out portion, hashed before the key was built.
  - PORTION-RESERVEE-L19-L46.tsv: the held-out groups, never decoded before the measure.
  - The transcriptions: two blind passes, then a blind arbiter who did not know the key.
  - scripts/: groups.py, measure.py, lexique.txt (a frozen generic lexicon) and SEUIL.txt (the threshold).

## The measure

The measure was run once. The command was `python3 -I measure.py ../transcription/ARBITREE.txt ../transcription/passe_B.txt ../CLE-K1.json lexique.txt "$PWD"`. The raw output is in MEASURE-20261127-1336.out.

| | value |
|---|---|
| Agreement on ARBITREE, L19–L46 (pass B, reported only) | **0.406** (0.384) |
| Controls: 200 permuted-value keys, seed 3807 | best 0.035, mean 0.003 |
| Criterion | ≥ 0.503 (0.85 × 0.592) **and** ≥ best control + 0.30 |

- **What the 0.503 threshold is:** 0.592 is the agreement on the key portion L01–L17, with the same lexicon. This calibration was declared before the freeze, because the reference here is a lexicon and not a gloss.
- **Verdict: FAIL.** The calibrated bar is not reached, although the margin over the controls (+0.37) is. The key is not validated, and the held-out portion is now burnt.

## Deviations found after the measure

These are declared here. They do not change the verdict, and nothing was changed retroactively.

1. **Bug in the frozen groups.py.** The arbitration table at the end of ARBITREE.txt ("# ARBITRAGE", rows such as "L30 | …") was parsed as manuscript lines.
   - Some groups were counted twice: 315 letters were measured instead of 272. The group 9po3, marked "clair?", was counted as well.
   - The true held-out portion therefore had 272 letters, below the 300 required.
   - Post hoc, on the body only (posthoc/ARBITREE-corps.txt and posthoc/POSTHOC-body-only.out), the agreement is 0.452 against a best control of 0.040. This is still a fail, and it is not a decisive figure.
2. **The low score comes from the lexicon, not the key.**
   - Read with K1 after the measure, the held-out lines are Latin and German: *appositi pro centenario viginti octo librae et quatuor lottones*; *solum die treibscherben lavare, eius loturam abicere und den … schlacken behalten*; *vitri*; *litargiri*; *huius regis*; *luna solita*.
   - Most of the words that fail are simply missing from the generic lexicon: centenario, viginti, octo, quatuor, loturam, abicere, behalten, vitri.
   - This observation is post hoc and is reported as such. It is not a validation.

## What a valid test would need

- **A fresh portion of at least 300 letters.** Butzmann reports cipher in earlier recipes of the same volume, which could serve; they are not yet located on the scans.
- **Fixes before a new freeze:** a corrected groups.py and an enriched lexicon.
- **Then:** a new PREREG and a new freeze posted before the measure.
