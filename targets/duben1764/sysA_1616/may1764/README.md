# duben1764, system A: key_c02 (unchanged) passes its second pre-registered test, on the 15/4 May 1764 letter

Work of 17 Nov 2026 (Brice Dudout's session, Claude Opus 5.5, AI agent). Riksarkivet K 259 (IIIF A0073297), images 105-108.
Text files only; images on the Riksarkivet IIIF server (`https://lbiiif.riksarkivet.se/arkis!A0073297_NNNNN/full/max/0/default.jpg`).

| file | what it is |
|---|---|
| `PREREG-C02b.md`, `SHA256SUMS-PREREG`, `SHA256SUMS-PREREG.time` | the plan, with the reading order fixed from material evidence, frozen and pushed (commit 62abb40f6) before any transcription or decode of this letter |
| `SHA256SUMS-AMEND1` | Amendment 1 (transcriptions frozen, preconditions), pushed (commit c21ae6291) before the measure |
| `scripts/measure_may.py` | the one measure: same code as `../aug1764/scripts/measure_aug.py`, seed 17640515, plus a reported-only page-wise CA |
| `transcr/may1764_cipher_merged.txt` | the cipher in the fixed order 105R -> 106L -> 107R -> 108L line 1, 52 number lines, 835 groups of 100 or above |
| `transcr/may1764_clear_106R-107L.txt` | the contemporary decipherment (34 lines, 1,900 letters) |
| `transcr/passes/`, `transcr/disagreements_may.txt` | pass 1 (this session), pass 2 (blind sub-agent), and the 32 substantive + 41 doubt-mark differences with their arbitration |
| `outputs/measure_result.json`, `outputs/measure_result_full.txt` | the result as printed, and the decode string |
| `reading_1764-05-15.md` | strict count, English translation and summary |

## Reading order (fixed before transcription, without reading the clear)
105R carries the date and "Mon cher Comte"; its header shows through, mirrored, on 106L (same leaf); the first number line of
107R shows through, mirrored, on 108L (same leaf); 108L ends the letter (one number line, then a clear paragraph and the
subscription). Order: 105R, 106L, 107R, 108L. The decipherer's leaf 106R/107L is bound between the two cipher leaves.

## Prior state
Bryan Payne (PR #185) transcribed this cipher once (870 groups) and compared it with the tables 218-220 only; the clear was never
transcribed; no key had been applied to these pages and no measure made (repository, all PRs, issues and fork branches, and our
own files, checked 17 Nov 2026). Payne's file was not used for the passes.

## Pre-registered result (run once, 17 Nov 2026 18:51 CET)
| | value |
|---|---|
| groups >= 100 | 835 (key_c02 covers 92.7 %) |
| clear letters / groups (precondition 1.8-2.8) | 1,900 / 835 = 2.275 |
| **CA** (share of decoded letters in matching blocks of >= 4 letters with the clear) | **0.916** |
| best of 200 permuted-key controls (mean) | 0.077 (0.048) |
| bar | CA >= 0.85 and CA >= controls max + 0.30 |
| verdict | **PASS** |
| M (clear letters covered; reported) | 0.803 (controls max 0.075) |
| page-wise CA (order-free; reported) | 0.916 |

The portion (cipher 105R-108L line 1, clear 106R-107L) is now burnt for any later key test. key_c02 is unchanged
(SHA-256 1813621c87e8...). Its first test (20/31 Aug 1764) stays a FAIL.

## Reading
Read through its contemporary decipherment: 418 words, 415 sure, 3 probable: strict share 0.993, **read** (`reading_1764-05-15.md`).
Transcriptions by AI agents, not checked by a palaeographer.
