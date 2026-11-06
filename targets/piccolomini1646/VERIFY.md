# Independent verification, catalogue 2358 (Piccolomini cipher letters inv. 24874 and 24876, 1646)

> Published copy of the independent check of 6 Nov 2026, unchanged below this note. Its figures and file names
> describe the folder before the fixes listed in NOTES.md ("Changes after the independent check").
>
> Addendum, 6 Nov 2026: the reading review recorded in NOTES.md ("Reading review") lowered both letters from "read in
> part" to "decoded, not read" (holes in most sentences). Where this check says "read in part is correct", that
> status no longer stands; its findings on the signs and the key are unchanged.

WAINUT, 6 November 2026. Adversarial check of the solver's folder. Before writing section 1, the verifier read only NOTES.md,
SIGN_CONVENTIONS.md and the scans. No transcription, decryption, reading or key file had been opened. (NOTES.md quotes
a few sign groups and a summary reading, so the verifier knew some of the expected words; the sign copy below was made
from the crops, sign by sign.)

## 1. Blind transcription (written before opening the solver's files)

The verifier made the crops from `scans/24874.jpg`, `24876.jpg` and `24873_2.jpg`. Each frame was rotated upright, line
centres were found by row projection, and lines were copied from 2x crops, with 3x-4x zooms where needed. Tokens follow
SIGN_CONVENTIONS.md. The verifier wrote every s/5 shape as `S`, `?` marks a doubtful sign, and `[?]` / `[blot]` marks a
sign that could not be made out. Word breaks are left out. Line numbers count from the first cipher line of the block.

### 24874 (bare), 7 lines

| # | Line | Blind text |
|---|---|---|
| B1 | L08 | 6 1 4 u S 3? S S S l m 7 d 7 3 t G 7 G 3 r n 7 d 3 l 1 m S |
| B2 | L09 | l S 4 6 S 1 S 4 S c 7 m 3 d r? l G 4 7? G 3 r n 7 p 7 l S 6 S c 7 |
| B3 | L10 | d 3 S 4 S d 3 r 4 1 d G n G G 4 3 G n 1 G S G S t 1 3 t 4 6 p 3 r |
| B4 | L12 | G G 3 u l S 1 G 3 r t S m 3 n l S 2 c h 4 0 3 S 4 [blot] n 7 n 3 c 3 |
| B5 | L14 | n 4 7 n t 3 d S 1 r l 1 1 S p r? t 1 d G n G G 3 u? d? S? k? l 3 p 1 r |
| B6 | L17 | G 4? c 1 m S 7 S S G e? n 7 r 3 1 S 4 S c G r 1 n d 7 l 1 c 4 6 h 3 |
| B7 | L19 | h 1 G r 1 c 7 n S 7 2 l 1 t S 7 n 0 3 S n c 7? n 4 1 r 1 |

### 24876 (bare), 4 lines

| # | Line | Blind text |
|---|---|---|
| B8 | block A line 2 | l 4 2 7 c w h 3 S 4 S d 7 6? u b S 1 m 7 b? 1 t 2 4 t 3 r 3 3? 4 [?] |
| B9 | block A line 4 | G S 1 S 3 l S w r S S p 4 7 n a d 3? c 7 n e f 7 r 0 2 a 4 3 S l 6 S a S 7 2 G 3? |
| B10 | block B line 2 | 4 c 1 d S u b 1 G 4 S 3 r 1 G 6 G 7 G l 2 a S 1 S n 6? G t 4 1 6? S |
| B11 | block B line 3 | m 7 d S l 1 p 1 c 3 S 4 a S c 2 h 3 p? G 7 l 4 l : 6 a 2 u e? |

### 24873_2 postscript (held-out passage), 2 lines

| # | Line | Blind text |
|---|---|---|
| H1 | postscript line 1 | d 3 S S 2 d 3 r 1 S G 1 1 l t? 3? z 4 w 6 S l r 1 G 2 2 G G 1 2 G l S 7 d S l G l c? 2 2 3 l S l c? 7? S S 3? |
| H2 | postscript line 3 | G S G d S 0? c 1 4 h S S l m 3? G G 2 4 l S 7 c 4 h 3 G 3 n 3 n d 7 |

Notes made while copying: in B1 the sign after `6 1` is a crossed cluster, perhaps an s run into a 4 or written over one.
In B2 the sign in `p7lS?Sc7` and the sign after `lS4` have a closed bowl with a rising stroke, like the 6 in `46p3r`
(L10). In B4 an ink blot covers one sign. In B8 there are two b/6-shaped signs around the `u` of `d7?u?S1m7`.

## Verdict

**Confirm the statuses, with fixes.** The key is right: it is Vlnas's table 3, and it turns both bare letters into
coherent Italian on the verifier's own sign copy too. The sign transcription is good but not clean. **Both letters stay
"read in part"**, and on the strict count they are further from 95% than the headline suggests. 24874 has 78 of 116 words
verbatim (67%; NOTES gives 71% because it includes the marked repairs), and after this check 76 of 116 (66%). 24876 has
32 of 50 (64%; NOTES gives 72%). The main defect is that at three places in 24874 the reconciled transcription writes the
sign the sense needs where the solver's own two passes (and the blind copy) read something else. Those words then count
as "verbatim", and the mark check cannot see the departure. No status changes.

## 2. Comparison with the solver's transcription

Compared with `transcription_24874.txt` (L08, L09, L10, L12, L14, L17, L19) and `transcription_24876.txt` (L02, L04, L07,
L08), using `difflib` on the sign sequences with word breaks ignored.

- Signs compared: 357 (24874: 220; 24876: 137).
- Raw: **328 of 357 agree (91.9%)** when the solver's `5` and the verifier's `S` count as the same. If they count as
  different, 313/357 (87.7%). The solver uses `5` for "a clear five", while the verifier wrote every such shape as `S`
  under SIGN_CONVENTIONS.md, which says five and s are the same shape here. That is a convention gap (see fixes), not a
  disagreement about the image.
- L10 agrees sign for sign (33/33).

Each disagreement was settled on a 3x-4x crop:

| Place | Verifier (blind) | Solver | Settled |
|---|---|---|---|
| 24874 L08, `61St4G...` | `6 1 4 u S 3?` | `6 1 S t 4 G S` | **unresolved.** The sign after `61` is a crossed cluster (an s and a 4 run together or overwritten). The next sign is a two-minim u/w shape, not a closed G bowl, and there is an e-like loop the solver does not have. The word is a hole in the reading, so the count is unaffected |
| 24874 L09, `p7l5?5c7` (read "politico") | 6 | t | **verifier right on the sign.** It has a closed bowl with a rising stroke, the same shape as the 6 in L10 `46p3r`. This hand's t (in `3t`) is an open c with a top stroke. Both solver passes read 6 here (pass 1 `p7lS6Sc7`, pass 2 `p7l565c7`). The reconciled `t` follows the sense, not the image |
| 24874 L09, `l54t5` | 6 | t | **verifier right (as above).** Pass 1 also read 6. The word is a hole, so the count is unaffected |
| 24874 L09, `d?l` (read "dal") | r? | 1 | **unresolved.** A short hooked minim with no dot. Pass 1 read r, pass 2 read 1. "dal" rests on this sign |
| 24874 L12, `1G3rt?5m3n?5` (read "avertimenti") | l | t? | **verifier right on the sign.** A tall stroke with no cross-stroke. Both solver passes read l (pass 1 `m3nlS`, pass 2 `m3nlS`), and the reconciled file wrote `t?`. In 24876 the solver marks the same t/l case as a repair (`tu{t/l}ta`); in 24874 it puts the sense into the transcription instead |
| 24874 L12, `S4?n7` | [blot] | t | **unresolved.** An ink blot covers the sign. The solver should write `[?]` or `t?`. The word is a guess (`[?che_siano]`), so the count is unaffected |
| 24874 L14, `1Sp?t1` | r? | 7 | **solver right** (flat top, long descending stroke) |
| 24874 L14, `dGnGG3 ?d` | u? | n | **solver right** |
| 24874 L14, `nd h` | d? S? k? | d h | **solver right.** The verifier split the tall looped d and the h wrongly |
| 24874 L19, `Snc7n??S1r1` | `4` | `G 4 S` | **unresolved.** One crossed sign with a descender and a slanted stroke. Whether that is two signs or three cannot be decided at this resolution. The word is a hole |
| 24876 L02, `d7?u?S1m7` (dobiamo) | `6? u b` | `b u` | **verifier right: the solver missed a sign.** There are two b/6-shaped signs, one before the u and one after it. Both passes have only one. The reading is unaffected (the extra sign is a null 6, or a doubled b) |
| 24876 L04, `c7ne?7r02?43` | f, a | p, n | **unresolved for f/p** (a tall descender with a top hook and no clear bowl). **Verifier right for a**: a closed loop like the a in `S4aS`, not an n. The word is a hole |
| 24876 L04, `Sl?S72G3` | `6 S a S` | `b 1 S` | **unresolved, leaning verifier.** There are four signs before `7`, not three. The word is a hole |
| 24876 L07, `d5 ? b1G453r1` | extra u/a | none | **verifier right.** There is a dark u/a loop between `d5` and `b`, which both passes missed. It is a null either way |
| 24876 L07, `Snt?G?t?t5` (read "in tutti") | `6? G t 4 1 6?` | `t G l t a t` | **unresolved.** The end of the line is blurred. The reading already marks it (`tu{t/l}t{-t}i`) |

After settling, of 357 signs about 7 are solver errors (2.0%), about 15 are unresolved at this resolution (4.2%), and
the rest agree or were settled for the solver. Three of the solver errors fall in words counted as read: "politico"
(L09) and "avertimenti" (L12) as verbatim, and "dal" (L09) is open. The other errors are nulls or in holes.

Held-out lines: H2 agrees sign for sign with the solver's `c4h3 G3n3nd7`. In H1 the solver's 31 signs all agree, but the
solver leaves out four signs (`w 6 S l`, read "il") between `1lt3z4` and `r1G22GG12GlS7` and prints the two groups as if
they were adjacent. The remainder of the line (`dSlGlc223lSlc7SS3`, not read by either side) is also left out. The file
calls itself an excerpt, but the gaps inside a line are not shown.

## 3. Key

- **Agreement with Vlnas's table.** Vlnas 2017 p. 33, table 3: a b c ... z with a e i o u w x y as "–", 1 a, 3 e, 5 i,
  7 o, 9 u, and 2 4 6 8 as "–". `key.tsv` has the same values. It adds 0 = null (not in Vlnas's table, but used five times),
  f = s (long s), and the class tokens S and G. It leaves out the null rows for the plain letters i, o, x and y. No
  transcription uses them, so nothing changes, but the key should list them so that it equals the printed table.
  `key.tsv` = `key_frozen.tsv` (byte-identical, also checked by the script).
- **"Glossed pairs".** There is no contemporary gloss on 24873, 24874 or 24876. The only pairs are Vlnas's own modern
  decipherment of 24873 (p. 33-34), produced mechanically from the same table (his macro maps each sign by the table).
  Every value therefore "holds" in those pairs by construction. The check is circular and proves nothing beyond Vlnas's
  table. The independent support is that the frozen table, applied to the solver's and to the verifier's blind sign copy,
  gives running Italian on two new letters in two hands: "desidera dunque una giusta et per[...]", "queli avertimenti
  [...] necessarii", "di quelo so tralascio per non tediarla", "duca di Baviera vuoglia ... la pace", "considerare
  l'avantaggio". For a system this simple (consonants plain, vowels as odd digits), that is conclusive for the key.
- **Null rule.** The counts in NOTES are reproduced exactly: 24874 has 645 signs with 63 even digits (4: 40, 2: 12, 6: 7,
  0: 4), and 24876 has 299 signs with 42. A weak point that NOTES itself admits: "in this hand six and b are close". L06
  `esi{+b}isce` is marked as a repair for that reason, yet in L09 the same doubt (6 or t) was settled silently for the
  sense. The rule "even digits are nulls" is applied by sense where 6 and b/t are confusable.
- **Class choices.** In 24874, 77 class signs (S, G) are resolved by context, and in 24876, 29. Words counted "verbatim"
  include these choices. Strictly verbatim words with no class choice: **34 of 116 in 24874 (29%)** and **14 of 50 in
  24876 (28%)**. NOTES says this openly, but the headline percentage should give both figures.

## 4. Held-out test (24873_2 postscript)

- Genuine in kind. Vlnas deciphers only the cipher lines of frame 24873 (p. 33-34, "Sua Altezza desidera che Vostra
  Eccellenza avisi tutte le particolarità ..."). The 24873_2 postscript ("desidera Sua Altezza [il] ragguaglio ...") is a
  different text, listed in his appendix (A05) but not printed. It is new text of the same writer.
- Weak as a test: (a) the key is Vlnas's published table and cannot have been tuned, so "frozen before" adds little.
  (b) The solver chose the 14 groups ("only groups whose signs are clear") and scored them itself. There is no external
  decipherment to grade against. (c) In-line gaps are not marked (see section 2). (d) The freeze cannot be proven: nothing
  is committed, and `key_frozen.tsv` is dated 15:12 while `heldout_24873_2_transcription.txt` is dated 15:15, after the
  freeze and after the decryptions (15:14). "14 of 14" should be read as "the published key gives Italian on a selected
  excerpt", not as a blind score.
- The verifier's blind H1/H2 copy decrypts with the same key to "desidera Sua Altezza il ragguaglio" and "che venendo".
  The left-out part of H2 also gives Italian-like text (`m3?GG24lS7` = meglio). That supports the key, independently of
  the solver's selection.

## 5. Mark check

- `python scripts/check_marks.py`: **exit 0**. "decryption_24874.txt: rebuilt, identical"; "24874: words 116: verbatim from
  the signs 78, with a marked repair 4, guessed from context 7, holes 27; class signs resolved by context 77; read from
  signs 71%"; "decryption_24876.txt: rebuilt, identical"; "24876: words 50: verbatim 32, marked repair 4, guessed 2,
  holes 12; class 29; read from signs 72%".
- Tamper tests on a scratch copy, each giving **exit 1**: (a) `da{l/h}la` changed to unmarked `dalla` gives "FAIL L04:
  reading "dalla" vs decryption "dahla""; (b) transcription L09 `p7l5t5c7` changed to `p7l565c7` (the passes' reading)
  without rebuilding gives "FAIL decryption_24874.txt is not what decrypt.py gives"; (c) the same change after rebuilding
  gives "FAIL L09: reading "politico" vs decryption "poliico""; (d) L12 `m3nt?5` changed to `m3nl5` (both passes'
  reading) gives "FAIL L12: reading "avertimenti" vs decryption "aGertimenli"". So the check works mechanically. Every
  departure **from the reconciled transcription** is marked.
- Not covered by the check: departures moved into the transcription itself. L09 `t` (twice) and L12 `t?` were written
  where both solver passes read 6 and l. The check passes because the sense is already in the sign copy. This is the main
  defect of the folder. The header of `transcription_24874.txt` also understates it: it says "pass 2 6 for t" (L09) and
  "pass 2 l for the second t" (L12), but pass 1 has the same readings (`p7lS6Sc7`, `m3nlS`).
- Also not covered: a unit like `in_tu{t/l}t{-t}i` counts both words as "marked", although "in" is verbatim. That is
  harmless, and slightly conservative.

## 6. Status against the rules

- **24874: read in part.** On the solver's own count 78/116 verbatim (67%). If L09 "politico" and L12 "avertimenti" are
  marked as they should be, 76/116 (66%), and 75/116 if "dal" also goes. Strictly, with no class choice, 34/116 (29%).
  It is far below 95%, so "read in part" is correct. The NOTES headline "read from signs 71%" mixes in repairs. It should
  give verbatim 67% (or 66% after the fixes) first.
- **24876: read in part.** 32/50 verbatim (64%, not 72%). Strictly 14/50 (28%). Correct status.
- **24873, 24873_1, 24873_2:** key source and control only, not claimed as read. That is correct. There is no
  contemporary gloss on any frame, so none of them is a transcription job. 24873's cipher lines are already deciphered in
  Vlnas 2017 (prior art) and must not be claimed.
- **Names and paths:** a grep of all .md, .txt, .tsv and .py files in the folder found no vendor, model or tool names and
  no Dutch archive names. The archives named are SOA Zámrsk and the Hradec Králové thesis repository. There are no
  absolute local paths. NOTES.md does cite two internal workspace folders (`research/sweep_2026-11_czech_chrome/`,
  `research/vetting_2026-11/`) in the collision check. They mean nothing in the target repository and should come out.
- **Not to commit:** all of `scans/`, including the 4.7 MB thesis PDF and the appendix frames, which are third-party
  material.

## Must fix before a PR (none changes a status)

1. `transcription_24874.txt` L09: write the signs as both passes and the blind copy see them (`p7l565c7`, and `l546?5`
   for the first word), and mark the reading `poli{+t}ico` (a six where the sense needs t, as at L06 `esi{+b}isce`).
   L12: write `m3nl?5` and mark the reading `avertimen{t/l}i`, as 24876 already does for t/l. L09 `d1l`: write `d1?l`
   and flag "dal" as resting on a doubtful sign. Rerun the counts: 24874 becomes 76/116 verbatim (66%).
2. Correct the header of `transcription_24874.txt`: pass 1 and pass 2 agree on 6 (L09) and l (L12). Settling against both
   passes for the sense is a reading decision and belongs in the marks, not in the transcription.
3. `transcription_24874.txt` L12 `S4tn7`: the t is under an ink blot. Write `[?]` or `t?`.
4. `transcription_24876.txt` L02: add the missing b/6 sign (`d76?ubS1m7` or similar). L07: add the u/a sign between `d5`
   and `b1G...`. L04: `n` becomes `a` in `c7nep7r02?43`, and `p` becomes `p?`.
5. NOTES.md counts table: add a "verbatim %" column (67% / 64%) and a "verbatim with no class choice" column (34 / 14).
   Keep "read from signs incl. repairs" as a separate, clearly labelled figure.
6. `heldout_24873_2_transcription.txt`: show gaps inside a line (`1lt3z4 ... r1G22GG12GlS7`, or include `w6Sl` = "il").
   Describe the held-out result in NOTES as an excerpt chosen by the solver, not as a score. Record the freeze (commit
   `key_frozen.tsv` alone, or give its hash).
7. SIGN_CONVENTIONS.md says five and s are the same shape, yet the transcriptions and `key.tsv` use a separate token `5`
   ("when clearly a five"). Either define when `5` is used, or merge it into `S`. Add the Vlnas null rows i, o, x and y to
   the key. Note in the key that 0 = null is an extension of Vlnas's table.
8. NOTES.md: remove the two internal workspace folder names from the collision check.
