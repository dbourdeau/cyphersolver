# External blind reading of the 1623 cipher pages: alignment with our frozen transcription

27 Nov 2026 (AEST). Aligned by script (`align_external.py`, Python difflib on number groups; output in `alignment_output.txt`).
The checks were done with AI tools and no person checked each record by hand.

## Who read what [stated, from the package report]
- Readers: GPT-6.2 Sol (first reading of 1080_0376), GPT-6.2 Astra (first reading of 1080_0380), Gemini 4 Carbon (independent visual comparison of both).
- These are **non-Anthropic models**, run by Malcolm McBratney in a Perplexity session on 26 Nov 2026. They were given only the facsimiles of
  scans 1080_0376 and 1080_0380 (and 1575_0038, not filed here). Per the package, they saw no inv. 1079 scan, no margin glosses, no Claude
  transcription, no key, no proposed plaintext, no OCR or HTR. They are independent of our transcription.
- Package integrity: `SHA256SUMS` (25 files) verified OK on receipt, 27 Nov 2026 00:12 UTC [measured].

## Comparison basis
- Ours: `letters/1623_1634/T1623_transcription.txt` (frozen 25 Nov 2026 18:07:33 UTC, md5 5a9e290e...; see `FREEZE_1623.txt`), blocks A (scan 0376)
  and B (scan 0380). Our groups in `{}` were supplied from inv. 1079 where the 1080 copy is lost in the gutter.
- Theirs: `VOC-1080-0376.txt` and `VOC-1080-0380.txt`, kept diplomatic and unchanged. For comparison only, the script places the left-margin
  insertion `M02` at its cross mark (as our transcription does), reads `[?]` as a doubt flag, and reads `4[illeg]` / `2[illeg]` as a
  partial group. Separators `.` `:` `-` are treated as group separators; `/` as the word divider.

## Results [measured]
| page | our groups | their groups | same value | clean (no doubt flag either side) | word dividers same place |
|---|---|---|---|---|---|
| 1080_0376 (block A) | 124 | 124 | 121/124 = 97.6% | 120/124 = 96.8% | 26/26 |
| 1080_0380 (block B) | 127 | 127 | 127/127 = 100.0% | 127/127 = 100.0% | 23/23 |

Arithmetic: 121/124 = 0.9758; 120/124 = 0.9677; 127/127 = 1.000.

The four non-clean places on 0376 are all at the right-hand fold (gutter), where our base copy is also lost and we supplied the group from inv. 1079:
| package row/pos | package reading | ours (word) | assessment |
|---|---|---|---|
| row 03 pos 11 | `15[?]` | `{15}` (word 11) | same value; both flagged |
| row 05 pos 17 | `4[illeg]` (initial 4 only) | `{42}` (word 18) | consistent (first digit agrees); not a conflict |
| row 06 pos 16 | `[illeg]` | `{3}` (word 22) | no reading on their side; Gemini tentatively suggested `3` (package report), not delivered |
| row 07 pos 16 | `2[illeg]` (initial 2 only) | `{28}` (word 25) | consistent (first digit agrees); Gemini tentatively suggested `8` after the `2`, not delivered |

**No value conflicts.** Every group the external readers delivered as certain agrees with our frozen value. The only differences are
the four gutter places, where their partial or tentative readings are consistent with what we took from inv. 1079.
Their separator notes (0380 row 02 `28-50`; row 04 `35.15./`) do not change any group or word division.

## Effect on our figures
- **Candidate emendations: none.** No disagreement would change a decoded unit in our filed reading.
- The 1623 figure of record is unchanged: first pass 32/54 = 59.26%, **below our 65% line**. Nothing here was re-decoded.
- This supplies the independent second reading that `NOTES.md` listed as missing for 1623 ("1623 has none").

## Outside the cipher block (not in our transcription)
- 0376 `B: 63568.11[?].12`: an accounting figure in the prose; the package matches it to the amount Coolhaas printed (GM I p. 129). Not cipher.
- 0376 `P-before: 500`, `P-below: 1622.`; 0380 `P-article: 26[?]`, `P-quantity: 80`, `P-date: 25. … 1623`: numerals in ordinary prose. Not cipher.

## Not filed here
- Martin, Hooghly 11 Mar 1696 (inv. 1575 scan 0038): a different cipher and letter, not part of this target. Our own attempt on it failed
  (recorded locally, not filed). For the record, the same script found 272/275 = 98.9% same value against our local frozen transcription,
  overbars agreeing on 272/272 matched tokens; differences at row 10 (`30` with raised x, notation only), row 15 last group (`306[?]` v our
  `30?`) and row 18 group 10 (`39[?]` v our `89`).
- Facsimile JPEGs and the readers' PNG crops are not filed, following this target's practice (IMAGE_ACCESS.md). Their SHA-256 values are in
  `SHA256SUMS`. Public viewer pages:
  https://www.nationaalarchief.nl/onderzoeken/archief/1.04.02/invnr/1080/file/NL-HaNA_1.04.02_1080_0376 and
  https://www.nationaalarchief.nl/onderzoeken/archief/1.04.02/invnr/1080/file/NL-HaNA_1.04.02_1080_0380
