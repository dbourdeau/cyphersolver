# Francia 346, alternate digit key: R5634, R5638, and R5639 (catalogue 880)

Archivio Apostolico Vaticano, Segreteria di Stato, Francia 346. Three digit cipher records (`R5634` ff. 190r to 190v, `R5638` ff. 218r to 218v, `R5639` ff. 220r to 220v) that share a separate key from `targets/ceva1632` and the 22 Ceva-key letters of `targets/francia346`.

Status: read in part (contributed by `prabal-rje` in pull request #926, responding to issue #879). `R5638` (159 of 246 cipher words sure, 0.646) and `R5639` (115 of 202 cipher words sure, 0.569) carry strictly aligned word-divided Italian readings and English translations; `R5634` stays **decoded, not read**. The maintainer sets the final folder name, status, class, and independent reading review.

## The cipher and key

- Two-digit codes stand for Italian letters (`18=e`, `55=i`, `17=a`, `36=o`, `44=s`, `94=r`, `12=t`, `71=n`, `70=l`, `79=u`, `59=c`, `92=d`, `37=p`, `62=m`, `90=h`, `77=g`, `27=f`, plus homophones), interleaved with single-digit nulls (`1, 3, 4, 5, 6, 7, 8, 9`) and two-digit nulls (`01, 04`).
- `key.tsv` lists all 59 codes with their source (`from ciphertext`), count, and grade (`firm`, `probable`, `tentative`).
- Unlike the Ceva key (`targets/francia346`), `6` is not a word space and `2x` pairs are not a null block (`scripts/test_ceva_mismatch.py` and `check.md`).

## Frozen ciphertext-only record

- Committed to `prabal-rje/branicki-1757` at commit `681ed424180eb3690b2fd33928fce4de9ace553d` (`2026-11-22 21:34:50 -0500` / `2026-11-23T02:34:50Z`), before opening, copying, or checking against any clerk's decipherment on these leaves.
- SHA-256 digests of the frozen files and of this folder's files are recorded in `FROZEN.sha256`.

## Unedited mechanical decode and strict readings

- `scripts/decode.py` decodes all six pages strictly from `key.tsv` via frequency-weighted dynamic programming (zero external language model, zero manual editing). `r5634.md`, `r5638.md`, and `r5639.md` print its unedited output.
- `r5638_reading.md` / `r5638_en.md` and `r5639_reading.md` / `r5639_en.md` provide word-divided Italian readings and English translations strictly aligned to the unedited mechanical decode. Every supplied or altered letter stands inside `[x]`, every unread or unparsed stretch stands as `[...]`, and `scripts/verify_readings.py` verifies zero unmarked departures from the mechanical decode (`R5638`: 159 of 246 sure = 0.646; `R5639`: 115 of 202 sure = 0.569; combined: 274 of 448 = 0.612).
- `R5634` (54 unread spans in 23 rows) stays **decoded, not read; cipher words not counted**.

## Transcription doubts

The six digit files in `transcription/` are unverified machine transcriptions of the DECODE images; no person has checked them against the scans. Every unread span (`[...]`) and every ambiguous digit or tentative-code slip stays open and is counted as a hole in `scripts/verify_readings.py`.

- Unread spans `[...]` (R5634 54 spans, R5638 16 spans, R5639 57 spans) - read: `[...]` (left open); checked: image, decode; machine pass on the DECODE images could not settle the digits and the decode leaves them open as holes.
- Single-digit codes `0` (`l`) and `2` (`b`) and rare tentative pairs in `key.tsv` (throughout R5638 and R5639, e.g. `f. 218r C03 lauiunta`, `C05 untoglio`, `C15 sarefe`, `C19 defo`) - read: kept literal in `r5638.md`/`r5639.md`, bracketed `[x]` as holes in the readings; checked: image, decode; single-letter slips against Italian context are never silently corrected and remain counted as holes.
- Damaged or faded rows in `R5634` (`f. 190r C01-C07`, `f. 190v C01-C07`) - read: open (`decoded, not read`); checked: image, decode; dense gaps prevent connected sentence reading without higher-resolution human verification of the scans.

## Remaining gaps

- `R5634` ff. 190r-190v and 127 unread spans across `R5634` (54), `R5638` (16), and `R5639` (57) - blocker: illegible; dense unread spans in the unverified machine transcription require human check against the DECODE scans.
- 22 tentative rare codes in `key.tsv` (including single-digit `0=l` and `2=b`) causing single-letter slips (`[x]` holes) in `R5638` and `R5639` - blocker: open-codes; too few occurrences in the three records to pin every rare homophone from ciphertext alone.

## Escalation

- [x] siblings: pooled all three records sharing this alternate key (`R5634`, `R5638`, `R5639`)
- [n/a] clear-pages: contemporary clerk's decipherments on the leaves were deliberately kept unopened to preserve a strictly ciphertext-only recovery
- [x] known-keys: tested the published Ceva key (`targets/francia346`) via `scripts/test_ceva_mismatch.py` with `R5635` as positive control; Ceva key ruled out
- [x] print: checked Lasry (2020) and `targets/ceva1632` / `targets/francia346`; this alternate digit key is not the published Ceva key
- [x] key-rebuild: 59-code key recovered from ciphertext alone and frozen in `FROZEN.sha256`
- [x] retry: ran `scripts/decode.py`, `scripts/test_ceva_mismatch.py`, and `scripts/verify_readings.py` on all three records; `R5638` and `R5639` build coherent sentences while `R5634` stays decoded, not read
