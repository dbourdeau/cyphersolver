# Proposal for `targets/capilupi1546` (image 02r), sign plate of 25 Nov 2026

For Daniel Bourdeau. Prepared with Brice Dudout's agreement; not yet sent.

## Credit

This folder is ours (Brice Dudout, PRs #497 and #521). The transcriptions of Camillo Capilupi's c. 48 and c. 49r by
LcCompany / WAINUT (capilupi1545) were part of the build set of the key, as the profile says; nothing here changes
that, and no file of theirs is touched. The pointer to the letters is Daniel's catalogue 1555. No other person's work
is used.

## What this changes

Image 02r goes from 118 to **122 of 128 = 95.3 %** sure words (strict count), over the 95 % bar. The last word,
*suplica*, rests on plate 2511c (26 Nov 2026, see point 3). Whether the class of 02r follows is Daniel's decision
(review of #984, point 2). The other folios are not recoded here.

*Revised on 26 Nov 2026 after Daniel's review of #984:* plate 2511 (three targets, under the schema's eight) is
recorded in NOTES and as a solution step, not in `outcome.sign_check`; the interlinear "5 1" of *suplica* were put on
a blind plate (2511c), which confirmed them.

## How

1. **Sign sheets C and R (18 Nov 2026).** Their two 02r answers are already in NOTES (Sign checks, 18 Nov 2026), but the
   committed transcription was not recoded. This patch recodes them: 02r line 15, digit 10: 9 -> 3 (*senza*); 02r line
   7, digit 15: [9/3] -> 3 (*contiene*).
2. **Sign plate 2511 (25 Nov 2026).** Six questions: three target signs and three hidden controls of known answer (a 6
   of *imparata*, a 0 of *io*, a 1 of *ho*, all on 02r line 10). All 3 controls were answered right. Each question
   showed the line, the boxed sign and real examples of each candidate shape, cut from sure words of the same hand; no
   value, word or place was shown. The selection rule was written and hashed before any thumbnail was cut; one
   amendment, made before any answer, only re-cropped two boxes. The plate was built and scored by AI agents (Claude
   Opus 5.5). The checker, Brice Dudout, is the contributor of the reading, not an independent reader.
   - 02r line 10, digit 14, [6/0]: answered **0**. *quasi* is now given by the key: sure.
   - 06r line 9, digit 23, "1": answered **1**, as transcribed. *{Io}* stays probable. (Not in this patch: no change.)
   - 02r line 8, first sign, "6~?": answered "none / other shape", with the remark "several signs? on the right probably
     a 5". A new look at the image agrees: a loop with a faint ascender (6?) and an s-shaped stroke with a small top flag
     (5?), the same stroke as the 5 of this hand. It is now transcribed `6? 5?`. The key gives "as", which is not a word
     (the sense would want *che*). No value is taken from the sense: the word stays unresolved, now ‹as›.
3. **A reading rule decided on 25 Nov 2026.** A clear correction written by the writer above the line, in the same hand,
   is read in place of the sign it corrects. It applies once here: at *suplica* (02r line 7) a sign is blotted out and
   "5 1" is written above it. The transcription had `#^51`; it now has `#~ 5 1`, and the key gives *suplica*.
   The two digits were read by the model, not by the checker, and on sheet C this hand's 1 was a 5 or a 7 at five
   places. **Plate 2511c (26 Nov 2026)** put the two digits blind, each against shapes 1, 5 and 7 cut from sure words
   of 02r, with three hidden controls (a sure 1, 5 and 7 of the same hand): controls 3 of 3; the first digit answered
   5, the second 1, as transcribed. The checker remarked of both that they are written above another line, which is
   what they are. *suplica* is now **sure**. Rule, answers and results: `sign_check_2511c/`.

## Count of 02r (README rule; Daniel's count of 12 Nov as the base)

| | words | sure | probable | restored | unresolved | strict | sure + probable |
|---|---|---|---|---|---|---|---|
| committed | 128 | 118 | 6 | 2 | 2 | 92.2 % | 96.9 % |
| after this patch | 128 | **122** | 4 | 0 | 2 | **95.3 %** | 98.4 % |

The four words that move: *contiene* and *senza* (restored -> sure, sheets C and R), *quasi* (probable -> sure, plate
2511), *suplica* (probable -> sure, interlinear rule and plate 2511c). The margin is one word. Whole system Y with only
02r recoded: 635 of 692 sure = 91.8 % (was 91.2 %).

## Applying it

From the repository root: `git apply targets/capilupi1546/dudout/capilupi1546-planche-2511.patch`
It applies cleanly to `main` (2134221795). It touches `dudout/transcription_02r.txt` (4 digit lines, with a comment
line under each change), the 02r line of `dudout/decryption.txt`, `dudout/reading.md` (02r text and the count tables)
and `dudout/translation.md` (three marks dropped: contains, almost, without). After it, the longest-code-first decoder
with `KEY-1555.json` (the one that reproduces `decryption.txt` exactly on all seven Y folios) gives the patched 02r
line. 05r, the held-out folio, is not touched, so `measure_1555.py` gives the same M.

Target-level files (in this branch, not in the patch): plate 2511 is a solution step of 25 Nov 2026 in `profile.json`
and a "Sign plate 2511" section in NOTES, with the reading rule and the open point on *suplica*; it is not an
`outcome.sign_check` entry (three targets, under the eight the schema asks for). Plate 2511c (two targets) is recorded the same way. If the patch is
applied, img-02r has `read_share` 0.953 (122/128); `fraction_read` 0.918 if only 02r is recoded. Whether 02r's class
moves to "read" is Daniel's decision. The target stays "read in part" (05r-05v, 06r-07r and system X).

## Files (all in `targets/capilupi1546/dudout/`)
- `PROPOSAL-2511.md`: this file.
- `capilupi1546-planche-2511.patch`: the patch above.
- `RECOMPTE-2511.md`: the recount, word by word (in French).
- `sign_check_2511/`: the selection rule and its amendment (in French; the `.sha256` files check them), the answers
  (`answers-2511-capilupi.json`) and their meaning in English (`results.tsv`).
- `sign_check_2511c/`: plate 2511c, its rule (in French, `.sha256` checks it), the answers and `results.tsv`.
- `SHA256SUMS-2511`: hashes of the files above.

Images: Estense, Autografoteca Campori, cc. 80a-80h (Lodovico, CC BY-NC-SA), used for study only. No image, crop or
derivative is included.

Brice Dudout (with Claude)
