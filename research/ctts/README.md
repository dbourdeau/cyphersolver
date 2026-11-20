# Gold-standard transcriptions with CTTS

George Lasry's advice (20 Nov 2026): a gold-standard dataset is the one real task. Make it with CTTS
([CrypTool Transcriber & Solver](https://github.com/CrypToolProject/CTTS)), with an LLM producing the first pass in
CTTS's own file format, and straighten the page images first. Every sign gets a box and a symbol type, a person
corrects the boxes and types in CTTS (the symbol-type views put all signs of a type side by side, so misfits stand out),
and the corrected project is the ground truth. DECODE transcriptions are not used as reference.

## Pipeline

1. **Straighten** (`prep_pages.py`): crop the cipher area, find the text lines, cut bands of a few lines and deskew each
   band on its own (one angle per page is not enough for a photo of a bound volume).
2. **Candidate boxes** (`segment.py`): ink blobs; main strokes grouped into signs, then each mark (prime, dots, bar)
   attached to the sign below it; commas and full stops dropped. Writes `boxes.json` and numbered overlays.
3. **First-pass labels**: a fresh model agent sees only the overlays and the bands and labels every box in the project's
   notation (`25'`, `97¨`, `94‾`, `4-`, `d`, `δ` ...), flags boxes that hold two signs (`!split`) or part of one
   (`!part`), and lists signs with no box (`missed`). Output: `labels_<model>.json`.
4. **CTTS project** (`to_ctts.py`): writes `positions/<image>_positions.txt` (`x y w h type`, image pixels) and
   `colors.txt` (`colour;name;order`), the files CTTS restores a project from. Flagged boxes get their own types
   (`15 !split`, `3 !part`) so they can be fixed together.
5. **Human correction in CTTS**: fix boxes, split and merge, add missed signs, move signs between types. Record the time
   spent. Save with ESC or F10; CTTS writes the corrected `positions/` and `transcription/` files.
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
| `bordeaux1653` | Bordeaux to Brienne, 30 May 1653, BL Add MS 4200 f. 88 (DECODE R8390), page 1 | 5 bands, 238 candidate boxes, Fable 5.2 first pass (222 signs, 94 types; 13 split, 40 part, 16 junk, 8 missed). Corrected and saved in CTTS on 20 Nov 2026 (14:21–15:04): all splits and parts fixed, junk removed, the 8 missed signs added (15, 28¨, u, 54', 64', 56', ll, plus 39' split out of "ll39"), 99' moved out of 99¨. Then compared with the target's image-checked transcription (`targets/bordeaux/ct2.txt`, page 1 = 223 tokens; 213 agreed) and each difference re-checked on the enlarged band image. Fixed in CTTS at 15:10–15:23: `q o` → `90` (the round sign has the form of the digit 0 in 20¨, not the tailed letter o), `6` → `6¨` and `5` → `5¨` (a dot is visible above each), `33`+`2` → `332` and `44` → `344` (three-digit codes; the 3 of 344 is under a stain), `?φ` merged back into `φ`, and a box `?52'` added for the stained sign at the start of band 3 (on the page only a prime tick and a stroke show; 52' is the reading of the duplicate copy, R8393). **Now 224 signs, 83 types; 219 of 223 tokens agree with `ct2`.** Left as is, where the image supports CTTS: `96‾` (ct2 `96=`; a single bar), `63` (ct2 `63'`; no prime, the stroke is the δ's curl), `3` + `96‾` (ct2 `396‾`; the bar covers only 96; open). Time: about 5 min in the browser review app (`review_server.py`, `review_log.jsonl`), 43 min in CTTS, 13 min for the validation fixes. Claude Opus 5.5 made the CTTS corrections and readings by driving the GUI while the user watched. **Human check, 20 Nov 2026: a person went over the final CTTS sign table and found it correct except `?52'` (the sign under the stain, head of band 3), which stays unconfirmed.** Still uncertain (band.line in the positions file, 0-based, before the validation fixes): 4.22 `25'` (which sign the prime belongs to), 5.5 `d` (the prime over the d left unassigned). Primes are assigned to the sign before them (written top right). Backups: `backups/before_ctts_correction_1420/`, `backups/after_ctts_correction_1504/`, `backups/after_validation_1523/`. |
