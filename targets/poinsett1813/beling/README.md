# Poinsett's code is WE025: the letter of 20 February 1813 read in part

Contributed by Andrew Beling, with AI agents, 11 November 2026.
This folder adds to `targets/poinsett1813/`. It changes nothing in Daniel Bourdeau's files or in Brice Dudout's
`dudout/`; the edits to `../NOTES.md` and `../profile.json` that go with it are in the same pull request.

In short: Poinsett's "code 1355" (1355 = the, 1397 = of) is the code that Ralph E. Weber, *United States Diplomatic
Codes and Ciphers, 1775-1938* (1979), prints in full as WE025 (pp. 470-480). With it, 406 of the 437 transcribed groups
of the 20 Feb 1813 letter read as they were frozen (92.9%), and all nine coded passages P1-P9 join Manning's clear
text. That is under the 95% read bar, so the letter is **read in part**.

## 1. What is here

| File | What it is |
|---|---|
| `reading_1813-02-20.md` | the reading as sentences, holes marked, with a summary and the context |
| `decryption_1813-02-20.txt` | the decryption line by line against `../transcription.tsv`, group by group |
| `groups_1813-02-20.tsv` | every group: our frozen reading, the number used, its WE025 element, status (D A R I H) and note |
| `transcription/numerals_1813_frozen.txt` | our own transcription of the numerals, frozen 1 Nov 2026 01:51 UTC (sha256 `d31b3043...`), ten days before WE025 was tried |
| `transcription/corrections_after_freeze.txt` | the rereads made after that freeze (one changed a group: P9.3 1160 to 1106) |
| `key/we025_poinsett.tsv` | the WE025 rows for the 341 numbers that occur in the Poinsett documents here (1811, 1813, 1814), not Weber's whole table |
| `key/we025_corrections.tsv` | our corrections to the text layer of Weber's table, each checked on the page image, made before the freeze |
| `key/we025_postfreeze_corrections.tsv` | the one correction made after the freeze: 668 = fect |
| `key/we025_SHA256.txt` | the hashes of our full transcription of the table, frozen 2026-11-11T10:37:23Z before any decoding with it |
| `key/extract_key.py` | how `we025_poinsett.tsv` was cut from the full table (needs the full table; `--check` verifies it) |
| `scripts/` | `texts.py` (loaders), `reading_1813.py` (the decode and the counts), `make_decryption.py`, `heldout_1814.py` (the test) |
| `tests/heldout_1814_result.txt`, `tests/reading_1813_lines.txt` | outputs of the test and of the decode |
| `CHECKS.txt`, `SHA256SUMS.txt` | checker output and script runs; file hashes |

No images are included. The frames are the NARA catalogue JPEGs named in `../NOTES.md` section 1.

## 2. The code: WE025

Weber prints WE025 complete, 1,592 numbered elements (pp. 470-480). We transcribed it from the text layer of the book,
checked 16 places on the page images (`key/we025_corrections.tsv`: three blanks in the text layer are punctuation,
1114 full stop, 1140 closing quote, 1227 colon; 618 is printed "iu", i standing for j), and froze the
result by sha256 at 2026-11-11T10:37:23Z, before decoding anything with it (`key/we025_SHA256.txt`). One correction
was made after the freeze: 668 is printed "fect", not "feet" as the text layer has it. It was missed in the
pre-freeze pass and found when P4 read "into ef feet" (`key/we025_postfreeze_corrections.tsv`).

Against the clerk's values of 14 June 1814 (`../key_1814.tsv`, 95 values), WE025 differs at 27 groups:

- 21 come from how `key_1814.tsv` split the clerk's words into syllables, where WE025 has pri-ce, en-de-au-our,
  dispose-i-tion, ex-pose-d, per-ma-ne-nt, foot, sl-op with the circle for "sloops", and so on.
- 462 1495 is dra-w ("draw"), where `key_1814.tsv` has 462 should, 1495 draw. Group 39, which the clerk and Manning
  left blank in "a ship [39] should draw", is "should" in WE025.
- 618: Weber prints "iu", i standing for j; `key_1814.tsv` and our table write "ju".
- 337 and 435 are transcription errors, checked on the images: 337 is 338 "never" (frame 0098) and 435 is 485 "dom",
  in "sel-dom" (clear on frame 0100).
- Not explained: Poinsett writes 1315 three times in 1814 where "a" is wanted, and Weber prints "hu"; the clerk wrote
  nothing over it each time. 1315 does not occur in the 1813 groups.

## 3. The test on the letter of 14 June 1814

`scripts/heldout_1814.py` decodes the 123 groups of `../ciphertext_1814.txt` with WE025 alone and compares the letters
with the clerk's interlinear decipherment (`../transcription_1814.tsv`), against 200 keys made by shuffling WE025's
elements over its numbers (fixed seed):

| Groups | WE025 | 200 shuffled keys |
|---|---|---|
| as Daniel Bourdeau transcribed them | 0.935 of letters matched (376 of 401) | mean 0.184, best 0.306; z = 16.3 |
| with the two image rereads (337 to 338, 435 to 485) | 0.954 (383 of 401) | mean 0.185, best 0.302 |

**This test is not blind.** The agent that identified the code had seen the clerk's values of 1814 before it did so.
It shows that WE025 reproduces the clerk's decipherment, not that it was predicted unseen. Our files record no pass
threshold set in advance.

The shuffled keys need all 1,592 elements, so the control runs only with our full transcription of the table
(`--full-table PATH`, which the repository does not hold); without it the script gives the WE025 score alone, which
needs only `key/we025_poinsett.tsv`. Both runs are in `CHECKS.txt`.

## 4. The letter of 20 February 1813

**Transcription.** We transcribed the numerals of P1-P9 ourselves from frames 0093-0094 and froze them on
1 Nov 2026, before WE025 was tried (`transcription/numerals_1813_frozen.txt`; doubtful digits kept open as `{a|b}`).
That transcription is not independent of Daniel Bourdeau's: the reader had seen his decode and research notes, as
the file's header says. Of the 437 groups, Daniel's number is our first frozen reading at 420 and our second at 5;
the two differ at 5 (1030/1038, 1347/1397, 452/952, 870/890, 1415/1413), and one or both leave a digit unread at 7.
The decryption is laid out line by line against his `transcription.tsv`, whose 41 rows match our 41 lines one to
one. Where his number differs from the one the reading uses (31 groups, mostly the A, R and I groups below), a
further row gives what WE025 has for his number.

**Decode.** `scripts/reading_1813.py` applies WE025 to the frozen numerals and records a status for each group:

| Status | Groups | Share | Meaning |
|---|---|---|---|
| D | 385 | 88.1% | our first frozen reading, element used as is |
| A | 21 | 4.8% | the other of two frozen readings `{a|b}` |
| R | 4 | 0.9% | number reread on the image after decoding (697 number, 739 mean, 1355 the, 1331 sea) |
| I | 20 | 4.6% | a digit assumed misread, at a blot or the page edge; not confirmed on the image |
| H | 7 | 1.6% | hole: no element that makes sense (55, 12, 502, 774, 487, 122, 1261 at those places) |

D + A = 406 of 437 = 92.9% read straight from the frozen numerals; with R, 410 (93.8%). `read_share`, measured on
the reading as sentences with `research/reading_audit/v10_relabel.py` `share()`, is 0.916 (360 words, 33 holes).
That measure counts the clear words taken from Manning that open each passage as read, and every `[?word]` as a
hole.

**Reading.** The sentences are in `reading_1813-02-20.md`. All nine coded passages join Manning's clear text on both
sides. P0, on frame 0092, is still not legible after contrast enhancement; only the group 807 can be read.

Notes on the doubtful places:

- P1 "number": frozen as 657 (ice); on the image the middle digit is 9 or 5, so 697 (number) or 657. Marked doubtful.
- P2 "means": frozen as 789 (pire) with a diamond; reread at 3x as 739 (mean) with the diamond. Marked doubtful.
  "in-struct[?ions]": the group after "struct" is 55 (spect) with a diamond and a faint stroke before it;
  "instructions" rests on context alone.
- P3 "law of nature, self preservation": the groups are 664 law, 1397 of, 541 natur, 670 self, 1385 505 1223 601
  pre-ser-va-tion. Our working summary of 11 Nov quoted it as "the first law of self preservation", leaving out 541.
- P4 "the loss": the group is 720, which Weber prints "lose". "on the part": frozen as 1356 (sm) with a doubt between
  5 and 6; reread as 1355 (the). "these seas": frozen 78?1; reread as 1331 (sea) with a diamond. "[?off]": 1387
  (what) at the page edge, taken as 1397 (of) with a cross. "[12]": 12 is "quire"; "t" (market) was expected.
  "dis[502][774]": 502 is "forty" and 774 "force"; they may belong to one word. "[487]": 487 is "phy"; "must" or
  "ought" was expected.
- P5: the full stop could also come after "return": "... leave them in the hands of patriots on our return.
  Independance will be declared throughout the kingdom." No group stands for "be".
- P6 "[122][1261]-sion": 122 (course) is at the page edge, and 1261 is "nat". "Confusion" would need 1209 1201
  (con-fu); a weak guess, not adopted.
- P7 "[?Brasil]": bra-si-l from 1450|1459 (blotted, taken as 1458 bra), 1547 si, 120 l. "[?of B. Ayres]": b-ay-res,
  with 17 (blotted) taken as 1397 (of), 1450 b, and 1317|1327 taken as 1517 (ay).
- The other doubtful groups are digits assumed misread; each is in `groups_1813-02-20.tsv` (status I) with the number
  frozen and the number used.

**Review pending.** No `reading_review` is recorded in `../profile.json`. That is for a human reviewer to add after
reading the sentences against the images and the decryption.

## 5. The open points in NOTES.md and dudout/README.md

From our files, nothing more:

- **NOTES.md section 2** ("not any US code table in the repo"): the repository had no copy of WE025; the code is
  WE025 as Weber prints it. The section's description fits: common words as single groups, longer words from
  syllables, values not in alphabetical order.
- **1215 = a or "at"** (Dudout): WE025 has 1215 = a and 1413 = at. Poinsett uses 1413 for "at" in 1814 ("at any
  price") and in 1813 ("is at my disposal"). So in the 1811 line "from the U States at private contract" the code
  gives "a"; "at" is the decoder's word.
- **708 = posi** (Dudout): WE025 has 708 = i (Weber prints "i. j", the letter). In 1814 "disposition" is 696 708 601,
  dispose-i-tion, so the split "posi" in `key_1814.tsv` was wrong. In 1813, 708 is the pronoun "I": "I have taken a
  part", "I have not urged", "I already mentioned"; Dudout's "posi have" is "I have", as he suspected.
- **The marks.** Read from use only, not from any key: a diamond or circle over a group adds -s (act-s, mean-s,
  sea-s, arm-s); a cross doubles a letter (tin+ in cut-tin-g, of+ = off); a caret adds -ed (carry^, mention^).

`key/we025_poinsett.tsv` shows, beside each WE025 value, the value in `../key_1814.tsv` and in
`../dudout/key_1811_additions.tsv` where they have one. Of Dudout's 13 new values, 12 are WE025's. The thirteenth,
210 = form (in "informed", 1348 210^), is "cur" in WE025, which has "form" at 216. We have not looked at his
photograph, so we leave this to him.

## 6. Other "code 1355" items: pointers only

We also scored WE025 on the other group spans in this code that our earlier work had collected with a plain-text label:
the plain text of each span against WE025's elements, "exact" when the letters agree. The inputs are outside the
repository, so the script is not included. Figures only, for anyone who takes these up:

| Item | Exact spans |
|---|---|
| Shaler, Dec 1810 (T20 roll 2, 198R; clear copy 196R) | 14 of 15 |
| Poinsett, 11 Jan 1811 (HSP, clear copy) | 8 of 12 |
| Monroe to Poinsett, 30 Apr 1811 (HSP; NARA M78) | 27 of 32 |
| Poinsett, 8-9 Mar 1812 (HSP, interlinear) | 6 of 6 tested (7 spans) |
| Crawford, 24 May 1814, enclosure (M36 roll 1, frame 97) | 78 of 99 |
| Clay to Crawford, 11 Aug 1814 (*Papers of Henry Clay* vol. 1, printed) | 94 of 115 |

The HSP blocks of 1811 that we have cannot be tested: their digits are not legible at the resolution we have.
Crawford's letter of 8 Apr 1814 and Poinsett's Mexico despatches are in another code, Weber's WE028, so Crawford
evidently held both.

## 7. Limits

- P0 (frame 0092) is not read; it needs a better image.
- 7 holes, and 20 groups that rest on a digit we assume was misread and have not confirmed on the image.
- 1315 = "hu" in Weber, used three times for "a" in 1814: not explained.
- The meaning of the marks is inferred from use only.
- One reader. No second, independent transcription or reading of the 1813 groups. The 1814 test is not blind.
- Our transcription of WE025 is from the book's text layer, with 16 places checked on the page images and one more
  after the freeze. Other text-layer errors in rows we did not check may remain; the rows used are in
  `key/we025_poinsett.tsv`, marked by how each was read.

## 8. Prior art

Searched before this work (11 Nov 2026): Weber 1979, this repository (local copy, upstream, GitHub code search),
Tomokiyo's Cryptiana and Manning 1925. Nothing tied Poinsett's code of 1810-1815 to WE025. Searched again while
preparing this folder (11 Nov 2026): the repository at `origin/main` 84eb800e (all files for "WE025" and "Poinsett"),
the open pull requests and all pull requests and issues mentioning "Poinsett" or "WE025", and the commits of
9-11 Nov 2026. WE025 is mentioned only in `targets/king1797` (Weber's attribution of a King letter of 1797) and in
the Code No. 16 word list of `targets/pinckney1793/beling`. Nothing found ties Poinsett to WE025.

## 9. Running it

From this folder, with Python 3 and nothing else installed:

    python3 scripts/reading_1813.py > tests/reading_1813_lines.txt   # writes groups_1813-02-20.tsv, prints the counts
    python3 scripts/make_decryption.py                                # writes decryption_1813-02-20.txt
    python3 scripts/heldout_1814.py                                   # the 1814 score (WE025 only)
    python3 scripts/heldout_1814.py --full-table PATH/we025_table.tsv # with the shuffled keys; writes tests/heldout_1814_result.txt
    python3 key/extract_key.py PATH/we025_table.tsv --check           # checks key/we025_poinsett.tsv against the full table

`../` is `targets/poinsett1813/`: the scripts read Daniel Bourdeau's `transcription.tsv`, `transcription_1814.tsv`,
`ciphertext_1814.txt` and `key_1814.tsv`, and Dudout's `dudout/README.md` and `key_1811_additions.tsv`. They
reproduce the figures above exactly (`CHECKS.txt`).

## Credit

Andrew Beling, with AI agents. The work builds on Daniel Bourdeau's transcription of the 1813 and 1814 letters and
his alignment of the clerk's 1814 decipherment, and on Brice Dudout's 1811 values and the two open points he
recorded. The code table is WE025 as Ralph E. Weber printed it in 1979.
