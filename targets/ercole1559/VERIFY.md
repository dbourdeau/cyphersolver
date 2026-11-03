# VERIFY: Catalogue 1566, Este ciphers 1559 and 1576

Independent check, 3 Nov 2026. Claim under test: `NOTES.md`, the keys, transcriptions, decryptions and readings in this folder. The solver's files were not edited.

**Verdict: confirmed with corrections.** Both keys hold and both texts are real Italian that fits their dates. Three statements in NOTES do not hold:

1. **"One shape for two letters" is wrong for cc. 76-77.** The clerks wrote a looped g and a straight q. The 339 signs "chosen by sense" can be read by shape.
2. **The c. 50r transcription leans on the gloss.** 7 of 147 blind signs were wrong, and all 7 moved toward the gloss. The word counts for 1559 are not measurements.
3. **"The name Ariosto was not seen on the leaf" is wrong.** A note at the foot of c. 77r names him and Venice.

| Document | NOTES claim | My status |
|---|---|---|
| Alfonso II, cc. 76-77, 1576 | read, first pass; 737/740 sense, 705/740 clean | **read in part, at the bar.** Sign copy good. 702-705 of 740 clean (94.9-95.3%); the bar is 703. Do not claim "read" until the must-fix items are done |
| Ercole II, cc. 50-51, 1559 | read, as a transcription job; 186/198 clean | **transcription job, read in part.** Sense is safe from the contemporary gloss. The sign copy is not fit to submit |
| Claudio Ariosto, c. 1, 1559 | not solved | not solved; not tested here |

## 1. Blind test

I read from the full-resolution scans before opening any transcription, key or note, and saved the readings before opening those files.

| document | signs | where | raw disagreement | after settling on crops |
|---|---|---|---|---|
| cc. 76-77 | 287 | c. 76r ll. 1-3, c. 77r ll. 4, 10 (includes second hand) | 6 (2.1%) | solver wrong 2 (0.7%), me wrong 4 |
| c. 50r | 147 (3 short of the 150 asked) | rows 08-10 | 8 (5.4%) | solver wrong 7 (4.8%), me wrong 0, 1 blot open |

The comparison for cc. 76-77 merged g and q, because my blind copy did not separate them reliably. See section 2 for that test.

**cc. 76-77.** The copy is good.

| place | me | solver | settled |
|---|---|---|---|
| 76r.02 pos 6 | z | 7 | **7.** No lower bar; solver right |
| 77r.10 pos 15, 37 | v | u | u; solver right |
| 77r.10 pos 44 | s | B | B, with a long top stroke; solver right |
| 76r.02 pos 24 | f | l | the sign has f's long descender and foot, with no bar. It is f, so "particola<r>e" needs no restoration |
| 76r.02 between pos 41 and 42 | a tall sign | nothing | a tall sign is squeezed between a and o and is missing from the transcription. A B there gives **"et il sospetto"**, the letter's usual spelling, for the reading's "e il". Plausible; check on a crop |

**c. 50r.** Every sign carries one dot, so on a crop signs can be counted against dots with no language. I did this at each spot.

| row | solver signs | image | solver gives | signs give | gloss |
|---|---|---|---|---|---|
| 08 | `d + I U T` | `d + U T`, 5 dots for 5 signs | che io | **chio** | che io |
| 08 | `V 8 8 U` | one dark oval, one dot | massime | **masime** | massime |
| 09 | `A I W I` | third sign is T with curved foot | due re | **duo re** | due re |
| 09 | `7 V 2 U I W V` | no U; 6 dots for 6 signs | maniera | **manera** | maniera |
| 09 | ends `V 2 I` | ends `V 2 I 8`; 4 dots | sane, then i | **sanes**, then i | sane |
| 10 | `G ] U 2 T` | `G ] U T 2 T`; 7 dots | uoglino | **uogliono** | uoglino |
| 10 | `8 V W U V` | `8 W U V`; 6 dots | saria | **sria** | saria |

All seven move the solver's signs toward the gloss. I saw the same gloss, and my reading went against it each time. NOTES warns of this danger; this shows it happened after the solver's second pass. Three rows give 7 changed words out of about 37. If that holds, the full page has about 40 wrong signs.

The row 09 entry matters for the reading. **Sane<s>i needs no restoration:** the final s of row 09 is on the leaf, and the note "a single sign seems to be left out" is the solver's own omission.

**My decryption of my own blind signs:**

- c. 50r, with key_1559: `gnachioguardibenedinoninciampareetmasimehauendoint / esochelacapitulationetraliduorestainmanerachesanes / inonspssonodreachilorouoglionochesriaungranpass`. Good Italian. 127 of 137 gloss letters match.
- cc. 76-77, with * for the q-forms: `uede**i*oquantoci*criue*teconlaletterauo`, `dareteade**oincognitoetintenderetedalta**onediche`. Same text as the solver.

## 2. The q-form: g and q are two signs

NOTES says cipher q and cipher g share one shape, and that 339 signs have their value "chosen by sense". On full-size crops the hand writes two signs:

- **Looped tail.** The descender sweeps left and back up in a large oval: cipher g = **s**.
- **Straight tail with a short foot:** cipher q = **m**.

Both are ordinary italic letter forms, and this fits the table's own block pattern.

**Sealed test.** I chose lines I had not viewed, recorded each q-form's tail in left-to-right order, wrote them to a file and hashed it (`1ccdd891`, 76v lines), added the second-hand lines, and only then opened the labels.

| lines | signs scored | agreement with solver's s/m |
|---|---|---|
| 76v.16-19, 77r.12-14 (sealed) | 37 (2 left open as unclear) | **37 of 37**; Fisher one-sided p = 8e-9 |
| 76v.13-15 (first look) | 17 | 17 of 17 |

Limit: I had already read the decryption file, so this reader is not language-blind. Two lines I tried to score before the seal (76r.15-16) were dropped when I noticed myself expecting the letters. The loop and the foot are physical features of the ink, and they are plain on the crops. Both hands do it.

**Why the solver's test missed it.** `work/qtails.json` does not point at the q-forms. Of 5 crops I traced back to their target sign, 4 sat 4-6 signs away (for example a crop on p for target `mpotda[q]mpm`). So 61%, AUC 0.62 and AUC 0.47 say nothing about shape, and the conclusion drawn from them should go. My own quick machine rerun on those positions also failed (AUC 0.51-0.55), for the same reason.

This helps the claim. The s/m choices agree with shape in all 54 tested signs, so they no longer rest on sense alone. 285 are still unchecked.

The merger also explains an oddity in the break: with q and g merged, the annealer had to put m somewhere and gave it to null y in both halves.

## 3. Rerun, held-out, shuffled control

- **Decryption of cc. 76-77, own script.** 3,689 signs, 3,435 after nulls, no unknown sign. Reading letters align to these with the differences listed in section 5.
- **Decryption of c. 50r.** Reproduced; see section 1 for the signs.

**1576 held-out: reproduced, and sound as a machine test.**

| test | real key | shuffled tables |
|---|---|---|
| solver's script | -10.165 | 200: mean -15.014, best -13.379 |
| my model from Ariosto letters only, without the 1567 texts | -10.18 | 500: mean -15.10, best -13.56 |
| final key on the full letter, quadgram | -9.10 | 200: mean -15.45, best -14.10 |
| final key on the full letter, word coverage | 64% | 200: mean 1.4%, best 8% |

Was the passage truly unused? In code, yes. `solve_bij.py` uses the half and a corpus built at 00:11 from Ariosto and the 1567 files. Key A is written at 00:33:48, before key B at 00:34:06, and `heldout.py` applies key A only. But it was not set up in advance: the whole-text key dates from 00:12, 21 minutes before the split. It is a valid machine check, not a preregistered one.

"18 of 21 agree" is too generous. Two of the 18 are y=m (y is a null in the final key) and q=s (only half true). 16 of the 18 match the final table.

**"Pass 1 was truly blind" needs a footnote.** `work/all.txt` (00:10) has z at c. 76r l. 2 pos 6. `f76r_p1.txt` was rewritten at 00:25, after the break, and has 7. That is the only sign that changed, and it is not in `p1_to_p2.tsv`. The 7 is correct, but the change came after the break and should be logged.

**1559 held-out.** 382 of 398 reproduced. My shuffles: mean 32.4%, best 42.0% (NOTES 29.7%, 38.7%). NOTES calls the test weak. It is weaker than that: section 1 shows the signs themselves bent toward the gloss.

## 4. Language, events, English

**cc. 76-77.** Fluent ducal chancery Italian, with period forms (*vedessimo*, *potressimo*, *soggiungerete*, *crimen lese maestatis*). Long subordinate sentences run across line and page breaks. Nothing reads as forced. The English follows the Italian. Doubtful words are marked: [?puntino], [?ti], [?gagliarde].

- Fit, from general knowledge, unchecked: Rovigo under Venice, plague scares of 1575-77, Venetian Inquisitors.
- *Giudice de' Savi* is a Ferrarese office, and Montecatino fits Ferrara.
- **The note at the foot of c. 77r reads "A Monsig.r Ariosti Ambasciatore / Venezia",** in a later hand. NOTES says the name was not seen on the leaf and treats Venice as inference. It is later testimony, not the writer's, but it is on the leaf.
- A search summary of a Mazzei article has Claudio Ariosto at Venice 1565-1577 and 1579. I did not open the article.

**cc. 50-51.** Fits: Bentivoglio as French lieutenant, the Sienese at Montalcino, the two kings' capitulation, Philip going to Spain, the weddings and jousts. A web article (theflorentine.net, the source NOTES cites) has Bentivoglio at Montalcino in July 1559. The English follows, including the "themselves" supplied for *possono dare*.

**The gloss at "dre a chi":** the gloss's d has a small raised stroke to the right. It may be a superscript a, which would give *dare* in the decipherer's own hand. NOTES says the decipherer copied the slip. Plausible, not settled; check on a crop.

## 5. Silent or wrong marks in cc. 76-77

Aligning the reading to the decryption, letter by letter:

| reading | signs give | problem |
|---|---|---|
| ben egli (76r.10-11) | bene egli | a letter dropped, unmarked |
| sommamente (76r.16) | somamente | a letter added, unmarked |
| per (77r.06) | pe + l + h, "pephor" | in the table, but unmarked in the text and counted clean |
| nost<r>i | r is in the signs; the blot is the i | mark on the wrong letter |
| inq<u>isitione | u is in the signs; the blot is the i | mark on the wrong letter |
| e il (76r.02) | see section 1 | possibly a sign left out |

The table's "11 r written without the bar" is also inexact. Of the 9 sites I viewed, 8 are plain l stopping at the baseline; the bar is not lost, the sign is a different one. Only 76r.02 has f's descender. So the clerk wrote l for r repeatedly. Treat this as a slip, or a second value, not as pen wear. The readings stand.

## 6. Words under the 95% rule

**cc. 76-77.** Rerun: 739 words and 704 clean by my split, or 740 and 705 with the digit 7, which is NOTES's count.

| change | clean words |
|---|---|
| NOTES | 705 |
| "per" marked | 704 |
| particola<r>e accepted as clean | 705 |
| ben, sommamente left as printed, so they must be marked | 703, or print the signs and stay 705 |
| strict, with the descender point refused | 702 |

So 702-705 of 740, or 94.9-95.3%. The bar is 703. By hand: first hand 533 of 556 (95.9%), second hand 171 of 183 (93.4%). A two-word margin, on a copy with 285 q-forms still to read by shape and second-hand strokes unrecorded, does not carry "read".

**c. 50r.** 198 words. Marks reproduce (187 clean by my split, 186 by NOTES, which counts [?son coreno] as two). Net effect of my seven corrections on the count is small, but the count no longer measures what it says. Under 95% in any case: read in part, as a transcription job.

## 7. Prior art

Two searches found no print of either letter. A search does not settle it. ASMo's ambassadors' series and Bentivoglio's own correspondence stay unopened, as NOTES says. The claim "we do not claim the reading is new" is the right wording.

## Must fix before a PR

1. Split q and g in `transcription_cc76-77`, `key_1576.tsv` and the decryption; read all 339 signs by tail; list any conflict with sense. Replace the "one shape" section of NOTES, and drop its test table or say the crops missed their targets.
2. Re-copy the signs of c. 50r with the gloss hidden, row by row, counting dots. Then recount. Fix at least the seven in section 1, including Sanes|i.
3. Fix the marks in section 5 and recount; check the tall sign at c. 76r l. 2.
4. Correct NOTES: the note at the foot of c. 77r; "r without the bar"; "18 of 21"; log z to 7 in `p1_to_p2.tsv`.
5. Do not call cc. 76-77 "read" until items 1 and 3 are done. Keep it read in part if the count stays at the bar.
