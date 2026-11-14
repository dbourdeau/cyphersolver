# Carleton, 25 September 1782: held-out-clear comparison

**The unchanged Army List key and frozen Clinton associations produced a substantial partial reading before the clear copy was opened.** The subsequent comparison preserves the failures. This tests a modern local transcription against an existing historical decipherment; it is not a first decipherment, perfectly blind trial or identification of the word-code book.

## Procedure and source coverage

1. Acquired and inspected only the cipher witnesses: LAC B.148 pp.123–125 and differently arranged duplicate pp.126–128, [H-1649 frames1205–1210](https://heritage.canadiana.ca/view/oocihm.lac_reel_h1649/1205). These are nineteenth-century Canadian transcripts of BL AddMS21808, not the British Library originals.
2. Transcribed the entire main cipher witness in its unusual column-across-pages order. The duplicate was inspected for order and selected ambiguous readings, not exhaustively independently transcribed.
3. Froze 200 editorial units and mechanical predictions under the byte-identical Army List key and frozen Clinton table. The coordinator independently reran the checker and verified all three checkpoint hashes **before either agent consulted the separate clear witness**. Broad subject/date context was already known, and the transcriber could see the key, so this is specifically a held-out-clear test.
4. Then acquired [B.148 p.102, frame1183](https://heritage.canadiana.ca/view/oocihm.lac_reel_h1649/1183), [p.103 subscription/docket, frame1184](https://heritage.canadiana.ca/view/oocihm.lac_reel_h1649/1184), and [B.146 p.54, frame616](https://heritage.canadiana.ca/view/oocihm.lac_reel_h1649/616). The latter confirms the date and resolves the creek-name reading as Pines; its subsequent-page continuation was not acquired.

The images, source URLs and hashes are preserved locally. The original manuscript and printed word-code source remain unacquired/unidentified. No contact, order, posting, commit or modification of prior frozen work occurred.

## Frozen prediction results

| Class | Frozen units | Later comparison |
|---|---:|---|
| Army List spelled groups |43|36 exact under declared i/j, case and spacing normalization;6 literal mismatches;1 extra cipher group absent from clear |
| Stronger Clinton word-code associations |58|56 exact;2 mismatches |
| Qualified Clinton associations |25|21 clear forms belong to the frozen set;3 mismatches;1 extra cipher unit absent from clear |
| Uncovered word-code occurrences |56|Remain unpredicted; later meanings do not count as successes |
| Already clear text/suffixes/notation |18|Excluded from numeric prediction successes |

These are editorial units, not a lexical success percentage. The 43 S groups include split names (Pensyl/vania and Ver/plan/ks), and contain 276 letter positions. Qualified-set agreement is weaker than an unambiguous prediction.

The strongest failures are **hundred versus thousand** at frozen 43-19, **has versus have**, and qualified **in/on versus near**. Two spelling failures reflect group boundaries discovered after opening the clear text:17-17 supplies assembly's final y, and23-1 supplies repairing's final g. The freeze was not changed to improve the score. Special-q explanations for Susquehannah and require remain provisional. The cipher's repeated “to Pines Creek” is absent from both clear witnesses.

The previously inferred imprint line 29 of the unchanged key now has this held-out-clear support: principal twice, Irwin, plan and new agree exactly; escapedo remains a sixth imperfect group. This supports that fixed line's use here, not a new discovery of the Army List key.

## Readable result and evidence

The letter reports projected incursions involving Potter and Irwin, movements toward the Seneca country, instructions to Paterson in Nova Scotia, and troop/fleet positions. These historical assertions are reported as letter content, not independently verified events.

- `preclear/PREDICTIONS.md` shows exactly what was available before clear consultation, including unknown numbers and awkward literals.
- `postclear/CLEAR_COPY.md` gives the readable English body and source boundaries. No separate translation is needed.
- `postclear/comparison.tsv` aligns every frozen unit with the clear witness and retains all failures.
- `postclear/DIFFERENCES.md` and `PROPOSALS_REVIEW.md` explain witness variants, strict versus contextual readings, and limits.
- `postclear/new_associations.tsv` contains39 distinct associations uncovered by this Clinton-only predictor. These are **post-clear** associations, not tested predictions or necessarily new to all prior project work. Suffix forms are qualified; misgrouped letters are excluded.

## Reproduction and next work

Run `python3 -I output/carleton_sept25_2026-11-12/check.py` from the workspace root. It requires complete manifests, checks the exact pre-clear checkpoint, unchanged input key/table, source hashes, frozen prediction outputs and score arithmetic. It cannot validate handwriting or historical assertions.

Useful next work is to resolve43-19 and special-q shapes against the British Library original, then test candidate printed word lists against the expanded coordinate sample. Keep conflicting and inflected/suffix-based associations qualified. A future new letter can test a separately frozen expanded training set; this letter cannot be treated as unseen again.
