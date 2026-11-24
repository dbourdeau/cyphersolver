# Francia 346, alternate digit key: R5634, R5638, and R5639 (catalogue 880)

Archivio Apostolico Vaticano, Segreteria di Stato, Francia 346. Three digit cipher records (`R5634` ff. 190r to 190v, `R5638` ff. 218r to 218v, `R5639` ff. 220r to 220v) that share a separate key from `targets/ceva1632` and the 22 Ceva-key letters of `targets/francia346`.

Status: in progress. Contributed by `prabal-rje` as a pull request (responding to issue #879). The maintainer sets the folder name, status, class, and reading review. All three records are filed as **decoded, not read; cipher words not counted**.

## The cipher and key

- Two-digit codes stand for Italian letters (`18=e`, `55=i`, `17=a`, `36=o`, `44=s`, `94=r`, `12=t`, `71=n`, `70=l`, `79=u`, `59=c`, `92=d`, `37=p`, `62=m`, `90=h`, `77=g`, `27=f`, plus homophones), interleaved with single-digit nulls (`1, 3, 4, 5, 6, 7, 8, 9`) and two-digit nulls (`01, 04`).
- `key.tsv` lists all 59 codes with their source (`from ciphertext`), count, and grade (`firm`, `probable`, `tentative`).
- Unlike the Ceva key (`targets/francia346`), `6` is not a word space and `2x` pairs are not a null block (`scripts/test_ceva_mismatch.py` and `check.md`).

## Frozen ciphertext-only record

- Committed to `prabal-rje/branicki-1757` at commit `681ed424180eb3690b2fd33928fce4de9ace553d` (`2026-11-22 21:34:50 -0500` / `2026-11-23T02:34:50Z`), before opening, copying, or checking against any clerk's decipherment on these leaves.
- SHA-256 digests of the frozen files and of this folder's files are recorded in `FROZEN.sha256`.

## Unedited mechanical decode

- `scripts/decode.py` decodes all six pages strictly from `key.tsv` via frequency-weighted dynamic programming (zero external language model, zero manual editing). `r5634.md`, `r5638.md`, and `r5639.md` print its unedited output.
- No document is claimed read under the 19 November rule because unread gaps (`127` across the three records) and tentative rare codes still break paragraphs into fragments.

## Remaining gaps

- Unread gaps and doubtful digits in the unverified machine transcription (`54` gaps in `R5634`, `16` in `R5638`, `57` in `R5639`) - blocker: illegible / transcription-unverified; human verification against DECODE scans is needed.
- Rare homophones and tentative codes in `key.tsv` (`22` tentative codes, including single-digit `0=l` and `2=b`) - blocker: open-codes; causes single-letter slips and occasional segmentation ambiguity.
- Contemporary clerk's decipherments on the leaves of `R5634`, `R5638`, and `R5639` have not yet been opened or aligned as a held-out check - blocker: not-attempted.
- No verified word-divided reading in complete sentences - blocker: not-attempted.

## Escalation

- [x] siblings: pooled all three records sharing this alternate key (`R5634`, `R5638`, `R5639`)
- [x] known-keys: tested the published Ceva key (`targets/francia346`) via `scripts/test_ceva_mismatch.py` with `R5635` as positive control; Ceva key ruled out
- [x] key-rebuild: 59-code key recovered from ciphertext alone and frozen in `FROZEN.sha256`
- [ ] clear-pages: contemporary clerk's decipherments on the leaves not yet opened for independent grading
- [ ] print: not searched
- [ ] retry: human verification of the six digit files against the DECODE scans, then a sentence-level reading

## Credit

- **DECODE**, the database of historical ciphers of the DECRYPT project: records `R5634`, `R5638`, `R5639` (`https://de-crypt.org/decrypt-web/RecordsView/<n>`).
- **The archive:** Archivio Apostolico Vaticano, Segreteria di Stato, Francia 346.
- **The database:** Héder, M. and Megyesi, B. (2022), "The DECODE Database of Historical Ciphers and Keys: Version 2", HistoCrypt, https://doi.org/10.3384/ecp188397.
- No DECODE image and no DECODE transcription file is published.
