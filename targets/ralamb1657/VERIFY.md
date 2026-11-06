# Independent verification, catalogue 2258 (Rålamb and Vellingk, Constantinople 1657)

> Published copy, 6 Nov 2026: unchanged except that one phrase in section 6 (the list of names grepped for) was made general.
> The file was renamed from `VERIFY_2026-11-06.md`. Its figures and file
> references predate the six fixes it asks for, which were made afterwards and are listed in NOTES.md ("Independent verification and
> what changed"). `scans/` and `work/` are not in the folder.

WAINUT, 6 November 2026. Adversarial check of the solver's folder. Before writing section 1, the verifier read only NOTES.md and
SIGN_CONVENTIONS.md and the scans. No transcription, decryption, reading or key file had been opened.

## 1. Blind transcription (written before opening the solver's files)

Crops were made by the verifier from the full-size scans `scans/max/114.jpg`, `104.jpg` and `075.jpg`, at 1.2x to 3x.
Notation follows SIGN_CONVENTIONS.md: `.` between groups, `|` marks clear words in between (left out here), `?` marks a doubtful
group, `[gutter]` marks a run going into the fold.

### Image 114 (bare letter), 10 sample lines

| # | Place | Blind text |
|---|---|---|
| B1 | left page, line 1 | 71.6.80.8.16.70.84.34.37.17.32.36 . 37.17.9.2 [gutter] |
| B2 | left page, line 2 start | 13.71.10.6 . |
| B3 | left page, line 3 | 12.8.64?.34.6 . 72.17.4.33 [gutter] |
| B4 | left page, line 5 | 97?.10.12.8.36 . / 45.5.4.71.6.17 . / 70.18.6.38? [gutter] |
| B5 | left page, line 6 | 4.40.10.41.34.37.74.34.102 . |
| B6 | left page, lines 7-8 | 36.69.35.6.71.5.37 . 41.40.10.8 [gutter] / 13.84.71.102 . |
| B7 | right page, lines 4-5 | 8.37.102 . 80.37.69.10.102 . 33.18.9?.32.97? . / 37.69.35.32 . 33.17.7.17.84.8.36 |
| B8 | right page, line 6 | 4.34.74 . / 41.40.10.12.8 . 31.69.36.32.5 . |
| B9 | right page, lines 8-10 | 71.4.9.17.41.33.71.6 . / 92.35.8.36.69.5 . / 4.40.10 + 20.77.101 . / 72.38.36.35.8.36 . 6.9.34.18 . |
| B10 | right page, lines 21-26 | 42.33.4.37.17.36 . / 12.8 . / 37.34.10.74.71.10.8.36 . / 67.71.6.80.34 . 43.17.9.64.6.37.10.64.8 . / 10.11.6.80.8.36 . / 71.43.64.80.37.8.36.16.8 . / 5.33.4.37.17 . / 73.11.6 . 74.17.9.13.69.5.42.8.36 . / 6.34 . |

Notes made while copying: in B7 the third group of `33.18.9?` is written over another figure, and the last group is either 97
or 93 (the second figure has the hooked foot of the clerk's 7; read 97). In B3 the third group could be 64 or 84. In B4 the
first group looks like 97; the last group runs into the fold (38 likely). 41 in B9 is retouched but legible.

### Image 104 (bare letter), the one run

47.69.42 . 8.10.6.13.82 . 50.45.17.80.82.10.9.17.35.8 . 84.8.80.17.49.82.36.74.45.73.43 . 37.38? / 46.13 .

(37.38: the last figure is an open-topped 8 or a 9; read 38.)

### Image 75 (held-out passage), numbers only

The interlinear gloss of image 75 is written right above the numbers and could not be covered on the crop; the numbers were
copied by shape only.

| # | Blind text |
|---|---|
| H1 | 80.50.71.37.46.17.37.8.36 . 41.40.10.47.38.12 . |
| H2 | 42.34.36.35.8.9 . 79.82.86.45.83 . |
| H3 | 70.36.12.45.8.4.31.38.83.49.8.37 . |
| H4 | 78.105.84.9 / 77.72.8.36 . |
| H5 | 65.47.17.64.6 . |
| H6 | 79.38.73.35.8.18 / 82.73.101.17.36.72.71.10 . |

## Verdict

**Confirm.** The sign transcription is good, the key pairs are real, and the key holds. The held-out test is real, and
the mark check works. The statuses stand: image 104 **read** (4 of 4 words verbatim from the signs) and image 114 **read in
part** (31 of 40 words verbatim, 77.5%). Images 22-23 and 75 are claimed only as key source and test, which is correct:
they carry a contemporary decipherment, so they would be transcription jobs. There are minor fixes (see the end), and none
of them changes a status.

## 2. Comparison with the solver's transcription

Compared with `transcription_114.txt` (L01-L09, L15-L30), `transcription_104.txt` and `transcription_heldout_075.txt`
(`difflib` on the group sequences, word stops ignored).

- Groups compared: 297 (114: 199; 104: 33; 75: 65).
- Raw: 4 disagreements, touching 5 group positions, which is **1.7% of groups**. At digit level 3 of 535 digits (0.6%).
  104 agrees group for group (33/33).
- Word-stop placement differs in three places (114 L02 `37 17 9 . 2`; 75 `skatt . liten`, `månge . penningar`). These were
  checked on the image, the solver's stops are right, and they do not change any letter.

Each disagreement settled on a 2x-3x crop of the full-size scan:

| Place | Verifier (blind) | Solver | Settled |
|---|---|---|---|
| 114 L03, 3rd group | 64? | 84 | **solver right.** The first figure has a closed upper loop like the clerk's 8 (compare `70.84` in L01). His 6 has an open, tall stem |
| 114 L09, last group before the fold | 8 | 80? | **solver right (doubtful).** A second figure starts after the 8 and runs into the fold. 80? is the honest reading |
| 114 L15, last group | 97? | 93 | **unresolved.** The second figure has a flat top and a z-shaped hooked foot, written over something. It can be 7 or 3. Both are open codes, so the reading (`uplo[93]`) is unaffected, but the solver should write `93?`. If it is 97, then 97 occurs twice (L04, L15) |
| 75 L03, 5th-6th groups | 8 . 4 | 84? | **verifier right on the signs.** There is a clear point between 8 and 4 at the same height as the other separators (`45. 8.4. 31`). The solver's `84?` follows the gloss "underhåldet". It is most likely the clerk's slip for 84 (r), but the signs as written give two groups |

After settling: 1 place where the solver normalised to the gloss (75 L03) and 1 unresolved (114 L15). That is **2 of 297
groups (0.7%)**. In the bare runs (114, 104) it is 1 unresolved of 232 (0.4%), on an open code.

## 3. Key

- **The pairs are real.** On image 22 the verifier saw in the scan `31,37,17,72,45. 74,17,64,8,36,12,45,47.` under the gloss
  "tijender", and `4,33,10,6,37,8,36. 47,71,35,32,16,17,108. 6,13,33,9,46,8. 19,34,10,71. 37,32,79, 71,9,17,37,8,10.
  47,70,64,73,82,84,99,102` under "Fursten Ragocy skulle wara totaliter ruinerat". Both agree with `pairs_022_023.txt`
  L01-L02. The gloss is interlinear, so cipher and decipherment are aligned word by word.
- **The values hold.** `key_frozen.tsv` was run over all 15 pair lines. Every word decrypts to its gloss word, apart from
  two groups cut at the crop edge (L08 `3?`, L10 `7?`). By position, **41 codes with 2 or more occurrences hold at every
  aligned occurrence**, for example 6 s (15), 8 e (19), 10 r (18), 12 d (13), 17 i (14), 34 a (15), 36 n (20), 37 t (23),
  45 e (16), 71 a (11), 82 e (9).
- The same values hold in the bare runs. The 114 and 104 decryptions are coherent Swedish. There is one marked change
  (77 ö) and one context value per word at most. Every 9 in the bare runs gives l (til, aflifuas, silistrie, tilkommen,
  keiserlige), as NOTES.md says.
- Exceptions, all in NOTES.md except the last two:
  - 79 = t in "totaliter" (image 22) against m twice in 75. On a 1.5x crop the 22 group reads 79 (closed head). It stands at
    the line end next to the fold, though, so 74 (t) cannot be fully ruled out. If it is 74, the conflict goes away and
    79 = m everywhere.
  - 9 = m once in 75.
  - 77 = y in 23 and ö in 75.
  - **Not in NOTES.md:** in pairs L10 ("trängsmål", `74 47 7? 36 35 31 5 75 46`), code 31 stands where the gloss has s.
    The key gives 31 h "sure". It is a one-off, but it should be listed.
  - **Not in NOTES.md:** in the same word, the cut group `7?` sits at the ä position, while `key.tsv` makes 7 = z from 114
    "uiziren". The `7?` is a cut group, so this is not a contradiction, but it should be said.
- **Context values** (`key.tsv`, added after the freeze): 50 k is backed by the contemporary gloss "skatt" on 75 (80 50 71 37),
  so it is not a guess. 72 g, 86 d and 105 ö are also backed by the 75 gloss. Only 67 p and 7 z rest on the bare runs alone
  ("passa silistrie", "uiziren"). Both are plausible, and each gives one verbatim word.

## 4. Held-out test (image 75)

- Rerun: `python scripts/heldout.py` **crashes on a Windows console** (`UnicodeEncodeError` on "≠", cp1252). With
  `PYTHONIOENCODING=utf-8` it reproduces the NOTES.md figure exactly: 64 groups, 55 right (86%), 4 wrong, 5 not in the frozen
  key. NOTES.md leaves out the word score the script prints: **4 of 10 words right**.
- Genuine in kind: the test is graded against the contemporary interlinear decipherment of 75, not the solver's reading.
  `key_frozen.tsv` matches the first 57 rows of `key.tsv` exactly. It keeps 79 = t, which 75 contradicts, and it lacks 50,
  72, 86 and 105, which only 75 supplies. That is what an untuned key looks like.
- Blindness caveat: the freeze cannot be proven. There is no commit or hash. `key_frozen.tsv` is dated 13:37,
  `transcription_heldout_075.txt` 13:43, and `pairs_022_023.txt` was modified at 13:45, after the freeze. The pair check above
  shows no frozen value that needs 75, so the risk is low.
- On the signs as written (75 L03 `8 . 4`), "underhåldet" also fails: about 54 of 64 groups (84%) and 3 of 10 words. The
  script compares by position, so if the extra group is fed to it, everything after it shifts and the score falls to 48/64.
  That figure is an artefact and should not be quoted.
- It is a small test (64 groups, 10 words). It supports the key, but it is not a strong figure on its own. The stronger
  evidence is that the frozen key alone turns the bare runs into sense: "skrifuit ... skrifuit", "togo uiziren fat",
  "aflifuas", "passa silistrie", "tilkommen".

## 5. Mark check

- `python scripts/check_marks.py`: **exit 0**. "decryption_114.txt: rebuilt, identical; words 40; verbatim from the signs 31
  (77.5%); with a marked repair 1; with a hole 8"; "decryption_104.txt: rebuilt, identical; words 4; verbatim 4 (100.0%)".
- Tamper tests on a scratch copy, each giving **exit 1**: (a) `förb{ö/y}n` changed to `förbön` without a mark gives
  "FAIL L20: reading implies 'förbön', signs give 'förbyn'"; (b) transcription 114 L03 `84` changed to `64` leaves the
  decryption stale, giving "FAIL decryption_114.txt is not what decrypt.py gives"; (c) 104 `tålk` changed to `tolk` gives
  "FAIL L01". So every departure in the marked blocks is marked, and the check catches unmarked ones.
- Not covered by the check: the "clear frame" table in `reading_114.md` puts the cipher words in bold in normalised form
  without marks ("assistence" where the signs give asistence, "förbön" for förbyn, "skrifwit", "aflifwas", "Viziren",
  "inve[c]kla"). The table is labelled approximate, but its bold cipher words should either copy the marked text or carry
  the marks.

## 6. Status against the rules

- **104: read.** 4 of 4 words verbatim (100%, rule: 95%). Every value used comes from a contemporary gloss (frozen key plus
  50 k from the 75 gloss "skatt"). There is no decipherment on the page, so it is not a transcription job. The run is
  short (one phrase of 33 groups), and the headline should say so.
- **114: read in part.** 31 of 40 words verbatim (77.5%), 1 marked change, 8 holes (5 in the gutter, 3 open codes). Correct.
  Without the two bare-run context values (67 p, 7 z) it would be 29 of 40. It is still "read in part" either way.
- **22-23, 75:** key source and test only. They are not claimed as read, which is correct because they carry a contemporary
  decipherment.
- **Names:** a grep of all .md, .txt, .tsv and .py files for vendor or model names and for other archive names found
  nothing. The only archive named is Riksarkivet (Swedish). AI use is described as "AI language-model agents".
  `fetch.py` uses User-Agent `WAINUT-research` and sleeps 1.6 s.
- **Not to commit:** `scripts/__pycache__/` (a .pyc embeds local paths), all of `scans/`, and the crops in `work/`.

## Must fix before a PR (none changes a status)

1. `transcription_heldout_075.txt` L03: write the signs as they are (`45 8 . 4 31` or `8 4?` with a note) instead of `84?`.
   Say in NOTES.md that the clerk probably slipped (gloss "underhåldet"), and give the held-out result both ways
   (55/64 = 86%, or about 54/64 on the signs as written). Add the word score (4/10).
2. `scripts/heldout.py`: set stdout to UTF-8 (`sys.stdout.reconfigure(encoding='utf-8')`) so it runs on a Windows console.
3. `transcription_114.txt` L15: `93` becomes `93?` (it could be 97, and it is overwritten).
4. Key notes: list the pairs-L10 exception (31 opposite s in "trängsmål") and the cut `7?` at the ä position. Add that the
   image 22 `79` sits at the fold and could be 74, which would remove the 79 = t/m conflict.
5. `reading_114.md` frame table: bold cipher words should follow the marked text, or carry its marks.
6. Record the freeze (commit `key_frozen.tsv` on its own, or give its hash) and say that `pairs_022_023.txt` was edited
   after the freeze.
