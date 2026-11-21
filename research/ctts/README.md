# Gold-standard transcriptions with CTTS

George Lasry's advice (20 Nov 2026): a gold-standard dataset is the one real task. Make it with CTTS
([CrypTool Transcriber & Solver](https://github.com/CrypToolProject/CTTS)), with an LLM producing the first pass in
CTTS's own file format, and straighten the page images first. Every sign gets a box and a symbol type, a person
corrects the boxes and types in CTTS (the symbol-type views put all signs of a type side by side, so misfits stand out),
and the corrected project is the ground truth. DECODE transcriptions are not used as reference.

## Pipeline

1. **Straighten** (`prep_pages.py`): crop the cipher area, find the text lines, cut bands of a few lines and deskew each
   band on its own (one angle per page is not enough for a photo of a bound volume).
2. **Candidate boxes** (`segment.py`; `segment_dense.py` for touching lines; `segment_lines.py` for cipher lines interleaved
   with clear text, line centres given by hand): ink blobs; main strokes grouped into signs, then each mark (prime, dots, bar)
   attached to the sign below it; commas and full stops dropped. Writes `boxes.json` and numbered overlays.
3. **First-pass labels**: a fresh model agent sees only the overlays and the bands and labels every box in the project's
   notation (`25'`, `97¨`, `94‾`, `4-`, `d`, `δ` ...), flags boxes that hold two signs (`!split`) or part of one
   (`!part`), and lists signs with no box (`missed`). Output: `labels_<model>.json`.
4. **CTTS project** (`to_ctts.py`; `apply_flags.py` first applies the first pass's own split/part/missed notes, then
   `to_ctts.py PROJECT labels_applied.json --boxes boxes_applied.json`): writes `positions/<image>_positions.txt` (`x y w h type`, image pixels) and
   `colors.txt` (`colour;name;order`), the files CTTS restores a project from. Flagged boxes get their own types
   (`15 !split`, `3 !part`) so they can be fixed together.
5. **Correction in CTTS**, in three parts (README Conventions, "Doubtful signs are checked, not carried"):
   - **5a. Structure.** Apply the first pass's own merge, split and missed-sign notes, fix boxes, move signs between types.
     This gives a usable CTTS file. In the pilot it changed no reading.
   - **5b. Doubts.** Every sign the first pass or the corrector flagged is checked on the sign enlarged with no overlay,
     and against the decoded text, before anything is final. Record each one (sign, location, reading, evidence).
   - **5c. Outside comparison.** Compare with an independent transcription only after 5a–5b, and record that you did:
     from then on the project is not independent of that transcription.

   Record the time spent. Save with ESC or F10; CTTS writes the corrected `positions/` and `transcription/` files. A
   person goes over the symbol-type views before the project counts as ground truth.
6. **Score** the first pass against the corrected project (signs and boxes), look at the confused symbol pairs as image
   pairs, and feed exemplars of confusable types back into the labelling prompt on held-out pages.

## Running CTTS

`tools/` (git-ignored) holds `ctts-3.7.0.jar` (from the CTTS GitHub release; it bundles JavaFX for Windows) and a
portable Temurin 21 JRE. From a project's `ctts/` folder:

```
..\..\..\tools\jdk-21.0.13.1+2-jre\bin\java.exe -jar ..\..\..\tools\ctts-3.7.0.jar
```

F11 or Tab: symbol-type views (F12 grid). F1/F2: next/previous image. F9: line alignment check. ESC: save and quit.

## Projects (images and CTTS files git-ignored under `projects/`, DECODE images are not public domain)

| project | document | state |
|---|---|---|
| `bordeaux1653` | Bordeaux to Brienne, 30 May 1653, BL Add MS 4200 f. 88 (DECODE R8390), page 1 | 5 bands, 238 candidate boxes, Fable 5.2 first pass (222 signs, 94 types; 13 split, 40 part, 16 junk, 8 missed). Corrected and saved in CTTS on 20 Nov 2026 (14:21–15:04): all splits and parts fixed, junk removed, the 8 missed signs added (15, 28¨, u, 54', 64', 56', ll, plus 39' split out of "ll39"), 99' moved out of 99¨. Then compared with the target's image-checked transcription (`targets/bordeaux/ct2.txt`, page 1 = 223 tokens; 213 agreed) and each difference re-checked on the enlarged band image. Fixed in CTTS at 15:10–15:23: `q o` → `90` (the round sign has the form of the digit 0 in 20¨, not the tailed letter o), `6` → `6¨` and `5` → `5¨` (a dot is visible above each), `33`+`2` → `332` and `44` → `344` (three-digit codes; the 3 of 344 is under a stain), `?φ` merged back into `φ`, and a box `?52'` added for the stained sign at the start of band 3 (on the page only a prime tick and a stroke show; 52' is the reading of the duplicate copy, R8393). **Now 224 signs, 83 types; 219 of 223 tokens agree with `ct2`.** Left as is, where the image supports CTTS: `96‾` (ct2 `96=`; a single bar), `63` (ct2 `63'`; no prime, the stroke is the δ's curl), `3` + `96‾` (ct2 `396‾`; the bar covers only 96; open). Time: about 5 min in the browser review app (`review_server.py`, `review_log.jsonl`), 43 min in CTTS, 13 min for the validation fixes. Claude Opus 5.5 made the CTTS corrections and readings by driving the GUI while the user watched. **Human check, 20 Nov 2026: a person went over the final CTTS sign table and found it correct except `?52'` (the sign under the stain, head of band 3), which stays unconfirmed.** Re-checked at 16:15 on enlarged, overlay-free crops and in CTTS, nothing changed: `25'` (band 4; the prime sits before the ll, and 25' = "pa" gives "separes"), `d` (band 5; the mark is the d's own flourish, and d = "u" gives "aussi"), and the lone `4` (band 4: a plain 4 whose crossbar stops at the stem, unlike `4-`; the decoded text wants the s-sign there, so the clerk probably meant `4-`, a decipherment point for the target's open [4]). Primes are assigned to the sign before them (written top right). Backups: `backups/before_ctts_correction_1420/`, `backups/after_ctts_correction_1504/`, `backups/after_validation_1523/`. |
| `marburg1635` | German cipher report to Hesse-Kassel, HStAM 4 d Nr. 1218 no. 49 (DECODE R4500), cipher lines 1-14; single-digit substitution with letter-like signs and marks; transcription and key both rebuilt here from the ciphertext (`targets/marburg1635/`) | Interlinear gloss over lines 1-4 defeats both line finders, so `segment_lines.py` (line centres given by hand, one straightened band per line): 14 bands, 633 candidate boxes. Blind Fable 5.2 first pass from bands, overlays and a notation sheet only (571 signs in boxes, 15 missed, 40 split, 41 part, 51 clear, 14 junk). Its own flags applied mechanically (`apply_flags.py`, then `to_ctts.py --boxes boxes_applied.json`: 640 boxes, 36 types). Claude Opus 5.5 read every line on enlarged overlay-free strips and 17 doubts on 3x crops (17:17-17:31), then corrected in CTTS by computer use while the user watched (17:32-17:49; ~30 type moves in the F12 grid view, 3 renames, 7 deletions, 1 merge, 2 boxes redrawn). **582 signs in 32 types (plus `_clear` for gloss strokes).** First pass vs final: 17.7% raw, 5.7% with its notes applied. Final vs the target's `cipher_tokens.txt` (compared only afterwards): 3.0% (565/576; marks not counted), 17 differences, all checked on the image. The marks the old transcription dropped carry key values (9 with bow = b/w, 0 with dots/bow = z, triangle with bar = ll, double-crossed long s = ss); no base key value changed; lines 4-7 now build a clause, lines 1-3 still do not (`targets/marburg1635/texts/R4500_ctts_test.md`, report `marburg1635_ctts_report.pdf`). Box geometry: deletions and two redraws only, auto-split boxes left equal-width, so the boxes are not a geometry gold standard. Model-made: no person has checked the sign table yet. Backups: `backups/before_ctts_correction_1717/`, `after_ctts_correction_1745/`, `after_validation_1749/`. |
| `it1583` | Two Sforza cipher slips of 4 May 1446, BnF italien 1583 f. 68 (DECODE R7898) and f. 70 (R7899 image P1); graphic-sign homophonic cipher whose key Lasry recovered from the ciphertext alone (`targets/it1583/`) | Binarized DECODE scans; lines ~37 px apart and touching, so `segment_dense.py` (2x upscale, line centres from the ink profile, touching strokes cut at the thinnest column): 7 bands, 1,129 candidate boxes. Blind Fable 5.2 first pass, one agent per letter, shown only bands, overlays and a shape notation (`NOTATION.md`): about 418 + 398 signs, 57 + 49 codes, 114 doubts, 193 part and 13 split boxes. Correction by Claude Opus 5.5, 20 Nov 2026 (about 17 min): part and clear runs merged, the two agents' codes for one shape unified, all 125 flagged signs checked on enlarged crops with no overlay (`decisions.tsv`), 74 box operations (`geomfix.log`). Computer use of the CTTS window came back denied, so at the user's choice the fixes were written to `positions/` and `colors.txt` and CTTS restored the project (834 boxes, 83 types). Then (5c, about 14 min) compared box by box with Lasry's CTTS project (fitted to the same images, scale 1.00, 2 px median offset) and fixed where image and decoded text side with him (`fix5c.log`): the dot groups `::` and `.:.` are cipher signs (z and a), 31 of them, dropped as separators because the notation sheet said so; b+cross = per; C with ÷ and 9 with barred m are compound signs; 18 single signs. **Final: 425 + 400 signs, 89 types.** Sign error rates vs final (f. 68 / f. 70): first pass raw 24.2% / 24.8%; with its own notes 12.7% / 9.2% (7.5% / 7.7% without the dot groups); CTTS pass before the comparison 10.8% / 6.8% (5.5% / 5.1%); final vs Lasry 1.9% / 5.2%; final vs the target's September draft (`f68_signs.txt`, `f70_signs.txt`) 14.1% / 14.6%, Lasry vs that draft 14.4% / 15.1%. **The key does not change**: of 27 boxes where the new class would give another letter, 21 go to Lasry by image and sense, 3 are naming only, 3 stay open. One reading gain: a caret-inserted o-sign on f. 68 line 10 that Lasry's project lacks ("octo o dece", eight or ten). Proposed for the open classes: #40 + (11) are one flourish. Corrections and readings are model-made; no person has checked the sign table yet. Scores: `score.py`, `scores.json`; report `it1583_ctts_report.pdf`. Backups: `backups/before_ctts_correction_1702/`, `before_ctts_gui_1709/`, `after_correction_1719/`, `after_5c_1729/`, `final_1732/`. |
