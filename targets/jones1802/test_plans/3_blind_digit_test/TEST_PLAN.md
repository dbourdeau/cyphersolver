# Pre-registered plan: is a "2" in the Jones 1798 transcription really a 4? (written 15 Nov 2026, before any image is read)

All work by AI agents (one worker, Opus, plus two blind reading helpers and one cropping helper). No person has
checked it. Local only.

## Claim under test

The verifier (`output/jones1802_verify_2026-11-15/NOTES_jones_verify.md`, S1 and `work/scan24_fresh.txt`) found,
after the fact, that 22 groups of their `table_1798.tsv` (groups of IOR/L/PS/9/76/49) land on their exact Entick
line (1795_0/1796 setting, R2 numbering) if one or two 2s are read as 4. Claim: in the manuscript those digits are 4s.

## Items (crop = the FIRST occurrence listed; location = their transcription file, folio, manuscript line, token)

Locations come from `targets/jones1802/ct_49.txt`, `ct_212.txt` (read only, worktree
`output/push_2026-11-15/wt-main-readonly/`), found by `scripts/select_groups.py` (`work/candidates.tsv`).
Digit positions: P = page number, W = word number, d1 = first digit from the left.

### D: disputed (22; all ct_49) - scored digit(s) must be 4

| id | group | word | proposed | scored digit(s) | location |
|---|---|---|---|---|---|
| D01 | 22,51 | at | 24,51 | P d2 | 49 f.1v L8 t5 |
| D02 | 28,75 | by | 48,75 | P d1 | 49 f.1v L7 t12 |
| D03 | 35,26 | best | 35,46 | W d1 | 49 f.1r L12 t1 |
| D04 | 177,12 | have | 177,14 | W d2 | 49 f.1v L19 t3 |
| D05 | 177,12,2 | had | 177,14,2 | W d2 | 49 f.1r L1 t2 |
| D06 | 201,68 | very | 401,68 | P d1 | 49 f.1r L1 t6 |
| D07 | 202,72 | instant | 204,72 | P d3 | 49 f.1r L5 t7 |
| D08 | 211,52 | unexpected | 411,52 (or 411,54) | P d1 | 49 f.1v L2 t8 |
| D09 | 225,23 | morning | 245,43 | P d2 and W d1 | 49 f.1r L1 t4 |
| D10 | 227,26 | use | 427,46 | P d1 and W d1 | 49 f.1v L7 t10 |
| D11 | 232,57 | went | 432,57 | P d1 | 49 f.1r L9 t5 |
| D12 | 233,27 | whether | 433,47 | P d1 and W d1 | 49 f.1v L3 t2 |
| D13 | 235,32 | measure | 235,34 | W d2 | 49 f.1v L2 t2 |
| D14 | 235,51 | will | 435,51 | P d1 | 49 f.1v L24 t13 |
| D15 | 236,32 | wisdom | 436,34 | P d1 and W d2 | 49 f.1v L12 t2 |
| D16 | 236,58 | with | 436,58 | P d1 | 49 f.1r L7 t7 |
| D17 | 260,26 | opportunity | 260,46 | W d1 | 49 f.1v L4 t6 |
| D18 | 260,32 | opinion | 260,34 | W d2 | 49 f.1v L12 t8 |
| D19 | 275,12 | people | 275,14 | W d2 | 49 f.1v L22 t8 |
| D20 | 378,22 | tartar | 378,42 (or 378,44) | W d1 | 49 f.1v L10 t8 |
| D21 | 383,20 | this | 383,40 | W d1 | 49 f.1r L1 t3 |
| D22 | 383,22 | think | 383,24 | W d2 | 49 f.1v L6 t10 |

### T2: true 2s (11; ct_49, same two pages) - every 2 in P and W scored, must be 2

Word on the exact line by the verifier's IMAGE counts of 1795_0, and no 2<->4 change also fits.

| id | group | word | location |
|---|---|---|---|
| T2-01 | 22,33 | as | 49 f.1r L9 t8 |
| T2-02 | 128,26 | empire | 49 f.1v L11 t8 |
| T2-03 | 129,70 | enemies | 49 f.1r L7 t10 |
| T2-04 | 130,25 | english | 49 f.1v L18 t11 |
| T2-05 | 235,5 | me | 49 f.1r L2 t9 |
| T2-06 | 260,13 | openness | 49 f.1r L6 t9 |
| T2-07 | 260,52 | opposition | 49 f.1v L16 t4 |
| T2-08 | 286,76 | porte | 49 f.1r L7 t2 |
| T2-09 | 299,50 | prudence | 49 f.1v L12 t3 |
| T2-10 | 366,25 | strong | 49 f.1v L17 t6 |
| T2-11 | 382,22 | their | 49 f.1r L6 t8 |

### T4: true 4s (11) - every 4 in P and W scored, must be 4

/49 has only two 4-groups confirmed on their line, so nine come from /212 (the 1802 letter; a different hand is
possible: the T4 rate is also reported for the two /49 items alone). Their value is grade H (M for 383,40) and the
word is on the exact line (image counts where marked img, else 1795_0 machine counts).

| id | group | word | source | location |
|---|---|---|---|---|
| T4-01 | 128,24 | emphatically | img | 49 f.1v L21 t3 |
| T4-02 | 113,24 | displeasing | 1796 machine | 49 f.1v L25 t2 |
| T4-03 | 129,40 | end | img | 212 f.3r L7 t5 |
| T4-04 | 255,4 | november | img | 212 f.1r L2 t6 |
| T4-05 | 275,14 | people | img | 212 f.3v L24 t5 |
| T4-06 | 383,24 | think | img | 212 f.3v L1 t6 |
| T4-07 | 383,40 | this | img | 212 f.3r L15 t3 |
| T4-08 | 70,24 | commerce | 1795_0 machine | 212 f.3v L20 (token "70,24;") |
| T4-09 | 149,56 | firman | 1795_0 machine | 212 f.2r L5 t1 |
| T4-10 | 404,67 | vizier | 1795_0 machine | 212 f.1v L12 t1 |
| T4-11 | 431,74 | week | 1795_0 machine | 212 f.2v L25 t7 |

### S: secondary, NOT scored for the verdict (reported as a description only)

/49 4-groups not confirmed on a line: S1 2,54 (f.1v L10 t4); S2 24,2 (f.1r L3 t4); S3 80,24 (f.1r L3 t3);
S4 384,52 (f.1v L20 t5). Further 2->4 candidates found by `select_groups.py` but not in the verifier's list:
S5 50,12 (f.1r L8 t3); S6 97,20 (f.1v L15 t12); S7 154,22 (f.1r L7 t5); S8 302,19 (f.1v L2 t9).

## Procedure

1. Images: QDL IIIF, largest size the service gives, one request at a time, >= 3 s apart, honest User-Agent; stop at
   the first 403/429/bot page; at most 80 requests. Saved in `sources/raw/jones1802_digits_2026-11-15/`.
2. Crops: a cropping helper (who is not a reader and is not the worker) is given each item's location (folio,
   line, token, and the transcription line) and returns a box; the worker cuts the crop by script (group plus a
   small margin, enlarged to >= 300 px high), without viewing the D crops. Crops get neutral names (c01...c52) in an
   order shuffled with a fixed seed; the key file is written by script and not shown to the readers.
3. Readers: two Opus helpers, independently, see only the crops and are told only: "read the number groups in this
   crop digit by digit; where a digit could be two things give both with your first choice first". They do not see
   the transcription, the dictionary, or which crops are disputed. Answers saved before scoring.

## Scoring (once)

- Target group in a crop: of the groups a reader gives, the one closest to the transcribed group when 2 and 4 are
  treated as the same digit (Levenshtein distance on the digit-and-comma string). The FIRST choice counts.
- A scored digit is read correctly if the reader's digit at the same position of the same part (P or W, same
  number of digits in that part) is the expected one; a part with a different length counts as "other".
- Control accuracy, per reader: share of scored T2 digits read 2, and share of scored T4 digits read 4.
- Disputed: a D item counts as "read 4" if every scored digit is read 4; per reader, n of 22.
- Also per reader: share of scored D digits read 2 (rate_D2) against the share of T2 digits read 2 (rate_T2).

Verdict:
- **Images cannot decide** if, for either reader, true-2 accuracy or true-4 accuracy is under 85%.
- **Confirmed (2-as-4)** if controls pass and EACH reader reads at least 70% of D items as 4 (16 of 22, or 70% of
  the D items actually cropped).
- **Rejected** if controls pass and, for each reader, rate_D2 >= rate_T2 - 15 points (disputed digits read as 2
  about as often as true 2s).
- Otherwise **not decided** (between the marks), reported as such.
- Items that cannot be located or cropped are dropped and listed; if more than 3 D items are dropped, the result
  is reported as incomplete.

Second choices, other digit confusions and shapes are described only in a labelled after-the-fact note.
