# Clinton, 22 February 1782: complete-body source-assisted comparison

Local research continuation, 12 November 2026. **The numeric cipher body is now covered from its opening through H.C., with explicit unresolved material.** This enlarges the frozen opening comparison to 320 editorial units across B.148 pp.11, 11A and 11B. It is not a claim of a new historical decipherment, flawless transcription or book identification.

## Primary sources and boundaries

The object is the nineteenth-century Canadian transcript of BL Add MS 21808 (LAC MG21 B.148), photographed on reel H-1649. The British Library original has not been inspected.

- [Frame 1077](https://heritage.canadiana.ca/view/oocihm.lac_reel_h1649/1077): clear quadruplicate p.8, title and body opening, dated New York 22 February 1782.
- [Frame 1078](https://heritage.canadiana.ca/view/oocihm.lac_reel_h1649/1078): clear p.9, remainder, subscription and postscript.
- [Frame 1079](https://heritage.canadiana.ca/view/oocihm.lac_reel_h1649/1079): p.10 docket; no further body text.
- [Frame 1080](https://heritage.canadiana.ca/view/oocihm.lac_reel_h1649/1080): p.11, four cipher columns. Its margin refers to clear pp.8–10.
- [Frame 1081](https://heritage.canadiana.ca/view/oocihm.lac_reel_h1649/1081): leaf marked 11A, five cipher columns.
- [Frame 1082](https://heritage.canadiana.ca/view/oocihm.lac_reel_h1649/1082): leaf marked 11B, five cipher columns ending H.C.; a white photographic defect damages part of column 4. Catchword Be points onward.
- [Frame 1083](https://heritage.canadiana.ca/view/oocihm.lac_reel_h1649/1083): numbered p.12, clear postscript and docket, including an additional money-account sentence absent from the quadruplicate.

All seven actual pages were inspected. 1077/1080 reuse the frozen opening images unchanged; the other five were acquired as public 2400-pixel IIIF JPEGs. `sources.json` gives URLs, hashes and requested image widths. Crops are analytic derivatives only; originals and frozen preceding package remain unchanged.

## Results and files

- `alignment.tsv`: 223 word-code occurrences, 44 spelled units, 52 unciphered units/suffixes, one explicit unread prefix. The **clear column is aligned reading**, not independently recovered plaintext. Its notes and `DIFFERENCES.md` are essential.
- `spellings.tsv`: literal fixed-key outputs. 39 of 44 words agree exactly with aligned readings allowing i/j and spacing; five discrepancies are retained. These 44 units contain 271 letter positions. No success percentage is asserted.
- `word_constraints.tsv`: 100 distinct word codes. Twenty-six also appear in the earlier Carleton 6 September alignment, 74 are additional to that alignment. These totals describe the sample, not 100 proven headwords. Shared forms include an/any, who/whose and returned/returning variants, so no claim that all shared readings are identical.
- `CLEAR_COPY.md`: complete clear body, subscription, postscript and separately reported p.12 variant. Since the source language is English, no translation is necessary.
- `DIFFERENCES.md`: witness variants, spelling/numeral uncertainty and falsifiable book constraints.
- `evidence/`: unchanged Army List key, prior Carleton alignment and frozen Clinton opening.

The 42 opening units are preserved exactly. The key is unchanged. Numerical corrections were prompted by fixed-key testing and then source reinspection; no blind-validation claim is made. Credit prior project work locating this pair, the historical decipherers/readers and the Canadian transcriber. This packet supplies a new local collation, not the first reading of the letter.

## Verification and next productive work

Run `python3 -I output/clinton_full_2026-11-12/check.py` from the workspace root. It verifies mandatory complete manifest, source/provenance hashes, unchanged frozen opening/key, schema, literal spelling outputs and recorded counts. It cannot validate handwriting or identify a book.

The original manuscript or better image can resolve the five spelling discrepancies, the glare-damaged reduce passage, and suspicious word-code variants. This archive access is not exhausted: it is a different witness, not currently acquired. The enlarged whole-letter word sample enables exact multi-coordinate testing of proposed printed sources, with qualified entries withheld from hard constraints.

Carleton 25 September is the next separate holdout. It has **not been opened or decoded in this packet**. Freeze this Clinton sample before consulting that clear witness. Some broad subject context was already known from prior project notes, so any future holdout must disclose that and avoid claiming perfect historical blindness.

No commits, publication, contact, order, paid action, key modification or frozen-package edits.
