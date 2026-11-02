# Richard Taylor's telegram letter-books, Meridian 1865: Confederate Vigenere, key COME RETRIBUTION (catalogue 681)

Status: in progress. Four telegrams of March-April 1865 are read from the NARA images with the known Confederate
key COME RETRIBUTION; the 6 April telegram needed 11 of its 57 letters corrected and is settled only with the clear
text printed in the Official Records. Two of them (6 and 8 April) are printed in clear in the Official Records, so for
those this is an earlier solution; for the other two (12 and 30 March) we found no printed text. The other cipher
passages in the three volumes are not read yet. Contributed by WAINUT (https://github.com/WAINUTAI), 27 Oct 2026;
the work was done with AI language-model agents. Every cipher word was read on the NARA images, and a second agent
read all four telegrams again on its own crops and decrypted them with its own code.

## The documents

NARA RG 109, War Department Collection of Confederate Records, Chapter II, letter-books of telegrams sent by the
Department of Alabama, Mississippi and East Louisiana (Lt. Gen. Richard Taylor), Meridian, Mississippi:

- vol. 196, Feb-Mar 1865: <https://catalog.archives.gov/id/45485022>
- vol. 11, 1865: <https://catalog.archives.gov/id/12127054>
- vol. 10, 1864-65: <https://catalog.archives.gov/id/16878212> (not read here)

The clerks copied each telegram in clear, but the passages that went by cipher were copied in cipher only, in
capitals, with dashes between the words. The volumes carry the "War Records COPIED" stamp.

| doc | frame, MS page | date | from, to | cipher letters | prior print |
|---|---|---|---|---|---|
| v196-0061 | vol. 196 fr. 0061, p. 117 | 12 Mar 1865 | Taylor (W. F. Bullock Jr., AAG) to Maj. Gen. D. H. Maury, Mobile | 180 | none found |
| v11-0022 | vol. 11 fr. 0022, pp. 40-41 | 30 Mar 1865 | E. Surget, AAG, to Lt. Gen. Taylor, Selma | 52 | none found |
| v11-0036 | vol. 11 fr. 0036, p. 69 | 6 Apr 1865 | Surget to Lt. Col. Wm. M. Levy, Mobile | 57 | OR I/49/2 p. 1209 |
| v11-0039 | vol. 11 fr. 0039, p. 75 | 8 Apr 1865 | Surget to Lt. Gen. R. Taylor, Demopolis | 61 | OR I/49/2 p. 1216 |

Image links are on each catalogue page above (frame numbers as in the NARA file names, e.g.
`chapter-2-volume-196-0061.jpg`). No images are kept here.

## Key and method

Vigenere with the key COMERETRIBUTION, running over the cipher letters only, starting at offset 0 with the first
cipher letter of each telegram (`key.md`). The key was already known for this correspondence: catalogue entry 681
had read frame 0061 and the vol. 11 OCR runs with it, and it is the known key of Confederate telegraph traffic in
1864-65. Applied to the vol. 11 passages, it fits each from its first letter.
The 12 March telegram has 180 cipher letters, exactly 12 turns of the key.

`python decrypt.py` checks every word of `alignment.tsv` and writes `<doc>_cipher.txt` and `<doc>_decryption.txt`.

## The clerk's capitals

The cipher capitals are written in a looped copperplate. A few letter forms mislead, and the same confusions recur.
The letters as read give the plaintext directly at 171 of 180 places (12 Mar), 50 of 52 (30 Mar), 46 of 57 (6 Apr)
and 59 of 61 (8 Apr). Every other place is explained by one glyph:

- the barred capital that looks like E is often F (EVEQRXXA = strength, BEVOZX = -nstant, TSNIQEL = courier, ME =
  to, IRUBEE = advanta-);
- T for F (ITQON = point, HCHTKRQ = outside), R for J (IIRX = west), N for G (CNAH, EQXLVNI), Y for V (PBYBBG),
  X for W (WXGF), Z for E (PCDXYIKZ), U for M (KUILM), C for B (CH = of);
- in IRUBEE (6 April) a U-like or II-like glyph stands for IC, so the word has 7 letters, not 6.

No correction needs more than one glyph per place. Corrections that were not checked again on a fresh crop are
marked [?] in `alignment.tsv` and the decryptions. The 6 April telegram is the weakest by itself (EQXLVNI needs three
fixes to give "returns"), but the Official Records print it in clear, word for word, which settles it.

## Reading

The four telegrams as sentences: `v196-0061_reading.md`, `v11-0022_reading.md`, `v11-0036_reading.md`,
`v11-0039_reading.md` (cipher words in capitals). Line-by-line decryptions: `<doc>_decryption.txt`.

- **12 March 1865, Taylor to Maury, Mobile.** "Telegraph in cipher what CAVALRY YOU HAVE ON EACH SIDE OF BAY, its
  STRENGTH AND NAME OF COMMANDER. Direct CAVALRY SO KEEP CLOSE as possible TO ENEMY, and to arrange to KEEP IN
  CONSTANT TELEGRAPHIC COMMUNICATION WITH Genl D. W. Adams and with these Head Quarters. Also indicate in cipher
  [?west] POINT you have decided upon OUTSIDE THROUGH WHICH TO COMMUNICATE WITH these Head Quarters, SO COURIER
  LINE may be established. Answer." Canby's advance on Mobile was beginning; Taylor wants Maury's cavalry kept in
  touch with the enemy and a courier point outside the city. The cipher gives WEST POINT where "what point" would
  fit the sense; Taylor had just returned from West Point, Mississippi (facing page), so the clerk may have
  enciphered the wrong word. One hole, read_share 0.989.
- **30 March 1865, Surget to Taylor, Selma.** After clear news (Lee's and Pillow's despatches; Dana's report at
  Vicksburg that Sherman had been wounded; Federal ambulances allowed between Big Black and Jackson): "War Dept
  ought to be again recommended to RELIEVE COL WATTS. Have no official CHARGES AGAINST HIM BUT HIS HABITS UNFIT HIM
  entirely for the position." Watts is probably Lt. Col. N. G. Watts, the agent for the exchange of prisoners (the
  telegram above it on p. 40 is about prisoner shipments and names Col. Watts).
- **6 April 1865, Surget to Levy, Mobile.** "SEE THAT SAM DUNCAN RETURNS PROMPTLY ON TIME. You will understand it is
  TO HIS ADVANTAGE TO DO SO. Think the enemy have crossed river at Selma and going East but have nothing definite."
  (Wilson's raid had taken Selma on 2 April.)
- **8 April 1865, Surget to Taylor, Demopolis.** "NORTHERN PAPERS JUST RECEIVED by General Hodge SAY RICHMOND FELL BY
  ASSAULT ON THIRD INST. He will send them here." The news of the fall of Richmond reaching Taylor's headquarters.

## Controls (`python decrypt.py --controls`, `controls.txt`)

Run on the letters as read, with no corrections:

| telegram | COME RETRIBUTION, offset 0: chi2 / letters agreeing | best other offset, chi2 | COMPLETE VICTORY chi2 | MANCHESTER BLUFF chi2 | 200 random keys, chi2 min / median | shuffled words, letters agreeing, mean / max |
|---|---|---|---|---|---|---|
| 12 Mar | 37 / 171 of 180 | 676 | 381 | 1072 | 402 / 1110 | 10.3 / 21 |
| 30 Mar | 19 / 50 of 52 | 156 | 184 | 323 | 75 / 434 | 3.0 / 10 |
| 6 Apr | 33 / 46 of 50 | 130 | 242 | 133 | 95 / 422 | 3.8 / 12 |
| 8 Apr | 22 / 59 of 61 | 92 | 132 | 273 | 117 / 456 | 5.2 / 25 |

COMPLETE VICTORY agrees in part (71 of 180 letters on 12 Mar) because it shares the key letters C, O, M, E and T in
6 of its 15 places with COME RETRIBUTION; it does not give English. The 6 April control leaves out IRUBEE (read with
6 letters for 7). The second agent ran its own controls on its own readings and got the same result for 12 March,
30 March and 8 April; its 6 April control, which kept IRUBEE, went out of step after that word.

## Earlier solutions and prior print

War of the Rebellion: Official Records, Ser. I vol. 49 pt. 2 (Washington 1897), archive.org
`warofrebellion014902rootrich`, and pt. 1, `warofrebellion014901rootrich` (correspondence to 15 March 1865).
Searched in the OCR full text with the whitespace normalised:

- **6 April, to Levy: printed**, OR I/49/2 p. 1209, word for word with the reading (page checked again on the OCR
  page headers and in the index, "Duncan, Sam. Mentioned 1209").
- **8 April, to Taylor: printed**, OR I/49/2 p. 1216, word for word ("on 3d instant" for THIRD INST; page checked again on the OCR page headers). A first search
  missed this one because the OCR text has double spaces between words; the second agent found it.
- **12 March, to Maury: not found** in OR I/49/1 (which prints the other Meridian telegrams of 12 March, to S. D.
  Lee, Gov. Watts, Forrest and D. W. Adams, about pp. 1050-1051) or pt. 2. Searches: "each side of bay", "courier
  line", "Adams and with", "what cavalry", "cavalry you have", Meridian 12-13 March followed by Maury.
- **30 March, on Col. Watts: not found** in OR I/49/2 ("relieve Col. Watts", "habits unfit", "official charges",
  "Sherman had been wounded", "Federal ambulances", "Big Black and Jackson").

An OCR search can miss a page, so "not found" means not found by that search. OR vols. 45 pt. 2 and 39 pt. 3 were
not checked. We know of no modern decipherment of these letter-book passages; the catalogue entry's own check
(known.py, web search) found none.

## Proposed catalogue changes (entry 681)

- status: four telegrams read in full from the images with COME RETRIBUTION (key over cipher letters only, offset 0
  at each telegram): vol. 196 fr. 0061 (12 Mar 1865), vol. 11 frs. 0022 (30 Mar), 0036 (6 Apr), 0039 (8 Apr). The
  6 and 8 April telegrams are printed in clear in OR I/49/2 pp. 1209 and 1216; the 12 and 30 March telegrams were
  not found in OR I/49 pts. 1-2.
- status: the quoted reading of frame 0061 should read "on each side of bay" (not "which side") and "[?west] point"
  (the cipher gives west; the catalogue's "[what]" is the sense, not the cipher). 180 cipher letters.
- prior_art: OR I/49 pts. 1-2 checked (27 Oct 2026); two of four telegrams printed in clear there.
- Suggested status: read in part (4 telegrams); vol. 10 and the other passages of vols. 11 and 196 open.

## Remaining gaps

- Vol. 196: only frame 0061 read - blocker: not-attempted; the catalogue's OCR run list (about 40 runs) is noisy
  (frame 0027, checked on the image, has no cipher words), so the frames need a visual screen first.
- Vol. 11: frames 0041-0046 and 0076-0081 not read - blocker: not-attempted; mechanical with the known key.
- Vol. 10 (about 8 runs; the OCR suggests COMPLETE VICTORY): not read - blocker: not-attempted; the date of the key
  change is therefore open.
- OR vols. 45 pt. 2 and 39 pt. 3 not searched for the remaining passages - blocker: not-attempted.

None of these has an outside blocker, so this is not a stopping point: the folder stays "in progress" until the
remaining passages are read (mechanical with the known key; vol. 10 probably COMPLETE VICTORY).

## Escalation

- [x] siblings: the three volumes are the sibling set; four telegrams read, the rest listed above.
- [x] clear-pages: the clear text around each cipher passage was used to check the sense.
- [x] known-keys: COME RETRIBUTION fits all four; COMPLETE VICTORY and MANCHESTER BLUFF tested as controls.
- [x] print: OR I/49 pts. 1-2 searched; two telegrams printed, two not found.
- [n/a] key-rebuild: the key is known.
- [ ] retry: the remaining passages of vols. 10, 11 and 196.

## Files

- `<doc>_transcription.txt`: each telegram as written, cipher words as read.
- `<doc>_cipher.txt`: cipher words only (written by `decrypt.py`).
- `alignment.tsv`: each cipher word as read, corrected, and its plaintext, with the glyph notes.
- `<doc>_decryption.txt`: line by line; `<doc>_reading.md`: the telegram as sentences.
- `key.md`; `decrypt.py`; `controls.txt`.

## 28 October 2026 — continuation: January volume, an additional key and prior print

This section adds to, and does not replace, WAINUT's 27 October work above.
Work by OpenAI Codex (GPT-6); no subagents. Scope: vol. 10 frames 0049, 0054,
0056 visually inspected; 0049 and 0056 transcribed. No claim to have screened
all frames of any of the three volumes.

### 9 January, Taylor to Davis: existing decipherment located; different key

Vol. 10 fr. 0049, MS p. 92 is printed in clear in **OR I/45/2 p. 772**,
Internet Archive `warofrebellion014502rootrich` (printed page header checked
in OCR; scan-page image not independently checked). The printed text warns
that moving Hood's army before rest, consolidation and reorganization will
make it worthless, and explicitly says Taylor is using a former keyword for
prudential reasons. See `v10-0049_reading.md` for the full telegram.

Matching the manuscript against that plaintext yields the 15-letter key
**THENAVYOURPRIDE / THE NAVY OUR PRIDE**, offset 0, cipher letters only.
This key is absent from the original three-key tests. The final working
candidate transcription gives 86/94 letters directly; eight discrepancies
remain explicit (C/G, U/V, E/F, V/Y and T/F forms). This is **key from external
plaintext**, together with **existing decipherment** for the text, not a
ciphertext-only solution or a new historical plaintext. The first 39 letters
contain a key candidate; it predicts 51/55 remaining letters. This is a
retrospective partition check after key/transcription refinement, not an
independent blind holdout. All other key
rotations were tested: best COMPLETE VICTORY 18/94, COME RETRIBUTION 25/94,
MANCHESTER BLUFF 14/94. OUR NAVY OUR PRIDE gives 67/94 and is distinct.

A related OUR NAVY OUR PRIDE phrase is reported for Chisolm's Beauregard
apparatus in *The Civil War in 50 Objects*, object 20. NYHS MS 670.5 holds
the apparatus. No key sheet with the exact THE NAVY OUR PRIDE phrase was
found here. Do not substitute the related phrase for the recovered string
or claim that this key was previously unknown. See `continuation_key.md`.

### 18 January, Taylor to Davis: provisional known-key reading

Vol. 10 fr. 0056, MS p. 107 substantially reads with COMPLETE VICTORY at
zero offset. Taylor asks for Johnston to command the Army of Tennessee,
proposes Beauregard in Carolina and Johnston here, and offers service in the
Trans-Mississippi or any subordinate capacity. Full transcription and
provisional coherent reading: `v10-0056_transcription.txt` and
`v10-0056_reading.md`. 239/259 candidate cipher letters agree with the proposed
plaintext; 20 differences affect 15 lexical words. Those words are marked
[?] until another visual pass or external plaintext settles them. This is
partial, below the project's word bar, and must not be counted as complete.
No matching full plaintext was located in OR I/45/2's normalized OCR.
A modern alternate-history forum quotes matching clauses with the same date
(https://civilwartalk.com/threads/gibraltar-dream-%E2%80%93-what-if-fort-fisher-held-firm.201713/).
That is a prior-print LEAD only: do not rely on its hypothetical narrative.
Find its underlying Taylor/Davis source before making a novelty claim.

### Reproduction and limits

`python3 continue_analysis.py` writes both word alignments and controls from
`continuation.json`. It separates candidate glyphs from re-enciphered
reconstructions. `continuation_alignment.tsv` never silently replaces raw
ciphertext with letters inferred from a desired reading. `continuation_sources.json`
records exact image URLs and the upstream tree commit. Images are external.
Arithmetic round-trip control passes; 1000 random 15-letter keys achieve at
most 28/94 matches for 9 January. This is an alignment check, not a trained
solver, so no language model was needed.

The initial three-key trial on 9 January failed. A speculative THE NATIONS
PRIDE guess from noisy C-P letters was rejected; the repeated alignment
supports THE NAVY OUR PRIDE instead. Raw palaeography remains the limiting
factor. Fr. 0054 is faint and was inspected but not claimed transcribed/read.

### Remaining work after this continuation

- Retain all earlier gaps above: the target is still in progress.
- Resolve the eight candidate-letter differences in 0049 on independent crops;
  inspect the OR printed scan page; look for the exact key in contemporary key material.
- Resolve 0056's 15 proposed words and locate its earlier printed source.
- Transcribe 0054 and visually screen the other volume-10 frames. The OCR run
  list does not establish exhaustive coverage.
- Screen the remaining vols. 11/196 passages as previously listed.
- Record key use per telegram. The 9 January reversion to an older key means
  observations cannot establish one universal chronological replacement date.

`REPORT-2026-10-28.md` is the ready-to-review continuation report. Nothing
has been submitted externally; existing `profile.json` and earlier alignments
are retained unchanged pending review.

## 28 October 2026 — second continuation: April passages and more prior print

Two further telegrams now have full readings backed by printed decipherments:

| document | manuscript | earlier plaintext | cipher letters | raw candidates agreeing |
|---|---|---|---:|---:|
| v11-0044b | 10 Apr, Surget to Maury, fr. 0044 p. 84, second telegram | OR I/49/2 p. 1223 | 79 | 74 |
| v11-0076-77a | 20 Apr, Taylor to Secretary of War, frs. 0076–0077 pp. 148–149 | OR I/49/2 p. 1255 | 124 | 114 |

Both use COME RETRIBUTION. Cipher-letter numbering continues across clear
prose and, for the 20 April message, across the frame boundary. The 20 April
message explicitly repeats a dispatch of 14 April; these are not two separately
transcribed cipher witnesses. All 18 and 27 lexical cipher words respectively
have printed plaintext; the listed candidate-glyph differences stay explicit.
Full `<doc>_transcription.txt`, `<doc>_reading.md`, and generated alignments are
included. Method: existing decipherment, checked using the known key. Printed
page numbers are verified from OCR headers; print scan images remain unchecked.

The 10 April telegram says troops and stores must move toward headquarters
and predicts that the force assembling at Vicksburg will move westward before
the week's end. The 20 April telegram reports Mobile's evacuation and asks
whether to unite with Cobb in Georgia or protect the Alabama/Mississippi
supply region. It says Taylor cannot decide without knowing government policy.

A second 20 April telegram, on p. 149 below that message, is ALSO printed in
clear on OR p. 1255. It reports completion of equipment of Mobile's garrison
and no indication of decided enemy movement. Its flowing cipher capitals were
not in the original capital-run hits. Beginning GEGMGQX agrees with COME
RETRIBUTION, but it is not yet fully aligned. See `v11-0077b_prior-print.md`.

Two other passages were transcribed provisionally and remain partial:
- `v11-0044a_transcription.txt`: a Maury quotation about Blakely and evacuation.
  The first passage's key alignment/letter count is unresolved; the second
  passage gives TROOPS AND STORES MUST BE MOVED IN THIS DIRECTION at key
  offset 3, with glyph corrections still proposed. No nulls are asserted.
- `v11-0045b_transcription.txt`: TROOPS SHOULD NOT BE SENT TO DEMOPOLIS AND
  PORTION OF THE ... is probable, but the final FX EVWJ JMNCH remains unread.
  An initially inserted false C in XCYKG shifted the rest of the text; correcting
  the word length restores AND PORTION OF. No ending has been invented.

Frame 0046 was viewed as a full page but is not yet transcribed; no reading
is claimed. These additional gaps are kept separate from the completed items.

### January source checks in this session

Taylor's *Destruction and Reconstruction* (Gutenberg 23747) and Alfred Roman,
*Military Operations of General Beauregard*, vol. II (IA
`milloperations02romarich`) were searched in normalized full text. The expected
18 January clauses were not found. This is a bounded OCR/text search, not proof
of absence from all editions. The January 18 reading retains its 15 uncertain
words. The previously speculative forum quotation remains only a lead.

### Reproduction and next work

`python3 continue_analysis.py` now checks four continuation items and writes
the updated TSV and controls. The two original January candidate streams and
all upstream WAINUT files except append-only NOTES remain unchanged. Sources
and JPEG references are recorded in `continuation_sources.json`. No generated
site files or original profile were changed; nothing was submitted externally.

Next: resolve 0044a/0045b, transcribe 0046 and 0077b, then continue screening
vol. 196. The three-volume target remains in progress; neither the OCR hit list
nor these selected frames constitute exhaustive volume coverage.

## 28 October 2026 — third continuation: dated orders introducing COME RETRIBUTION

**New evidence for the key chronology:** vol. 196 fr.0055, MS p.105 has two
telegrams dated **9 March 1865**, sent by W.F. Bullock Jr. AAG from Meridian,
"By order," to (1) Wirt Adams, Jackson, Mississippi, and (2) D.W. Adams,
Montevallo or Selma, Alabama. Both read:

> In sending cipher dispatches after this date use the following key word,
> "Come Retribution." Acknowledge receipt.

The orders themselves use **COMPLETE VICTORY**, with the key running only over
cipher letters from offset zero. The cipher-only plaintext sequence is
CIPHER DISPATCHES FOLLOWING KEY WORD COME RETRIBUTION: seven lexical words,
47 letters per copy. Each candidate transcription agrees directly at 46/47
places, with one N/M ambiguity in NXM/MXM (=KEY). No other correction is needed.

The Wirt Adams copy has the complete decipherment pencilled above the cipher
words. This is existing adjacent plaintext; the pencil annotator and date are
unknown. The D.W. Adams copy is unannotated but duplicates the instruction.
Method: existing adjacent decipherment checked with known key (Wirt); known
key applied and checked against annotated sibling (D.W.). Neither is a new
ciphertext-only break. Both are distinct documents for coverage, but not
independent key recoveries. Full files: `v196-0055-wirt_*`, `v196-0055-dw_*`.

`KEY-CHANGE-1865-03-09.md` is the focused evidence report with the exact primary
image link. `continue_analysis.py` now reproduces six continuation alignments
and key controls for the two orders. COMPLETE VICTORY gives 46/47 matches;
COME RETRIBUTION only 20/47 (its partially shared letters), with no other offset
improving that. The three other keys/all offsets do not fit the orders.

### Scope of the historical result

This establishes an instruction **issued on 9 March to these two recipients**,
with implementation phrased "after this date." It does not establish receipt
time, a precise first-use day elsewhere, or a simultaneous global switch.
The 9 January older-key reversion remains relevant. OCR-only 8 March traffic
that appears to fit COME RETRIBUTION still needs image checking, so do not
force all channels into one switch chronology.

Normalized OR I/49/1 and I/49/2 OCR searches returned no match for retribution,
"after this date use," key-word or keyword. This bounded search is not proof
that the orders were never printed elsewhere; the pencilled decipherment
already shows they were read before this session.

### Other work in this session

Re-inspected the troublesome 0045b ending and 0044a alignment. They remain
unresolved; no guessed ending or null was promoted into the text. Viewed vol.11
0046 again; its faint cipher remains untranscribed. Fetched vol.196 metadata
and OCR, screened OCR for frs.0010,0018,0022,0052,0053,0055,0056,0064,0065,0071,
and viewed full images 0010,0055 (and downloaded 0056). OCR screening is not a
visual survey of those frames. Fr.0010 has additional ciphertext, including
flowing capitals in the left telegram; no full reading is claimed.

The April partials and January uncertainties are still open. The overall
three-volume target remains in progress. Priority next step is to check
8 March key usage on images against the 9 March instructions, then finish
unread telegrams and the page-by-page inventory. No public submission made.

### Third-session follow-up: 8 March channel checked on the image

After the key-change report above, downloaded and viewed vol.196 fr.0052,
MS p.99, dated **8 March 1865**, Taylor to Col. George Wm. Brent at Augusta.
The opening cipher candidates `GBQQP EN CMBNM BKRPHK XYSNJIOX` give ENEMY AU
LEATT TWENTY THOUSAND with COME RETRIBUTION, or ENEMY AT LEAST TWENTY THOUSAND
with two N/M candidate ambiguities (24/26 letters direct). The closing
`DSOZVH ZKWA AQFFL` gives MOVING FROM NORTH exactly at local key offset 4.
The middle remains untranscribed and full key continuity is not established;
`v196-0052_partial.txt` is explicitly partial. This image check replaces the
"OCR only" status of that lead above, not its incomplete coverage status.

Thus COME RETRIBUTION is supported in the Brent channel on 8 March, while
the 9 March orders tell Wirt Adams and D.W. Adams to adopt it. The recipient-
specific chronology is essential: the orders do not date its first use at
headquarters, much less the entire Confederacy.

## 1 November 2026 — community check and local continuation

PR #186 was merged by dbourdeau on 29 Oct 01:30:55 UTC (28 Oct Pacific).
No comments/reviews or later upstream target changes were found in today's
GitHub check. User requested research only, stopping submission preparation.

The 8 March Brent message (vol.196 fr0052 p99) now follows COME RETRIBUTION
continuously: STRONG is split STR / ONG at the line break. The final MOVING
FROM NORTH follows naturally from the beginning. 116/124 working candidate
letters agree with the contextual reconstruction; Montgomery, evacuated,
force and adequate retain uncertainty labels. This improves the prior partial
without silently replacing its historical file. No complete-reading claim.

The 4 February Taylor–Davis Navy telegram (vol.196 fr0010 p15) has an existing
printed decipherment, OR I/49/1 p955. A long downstream sequence matches COME
RETRIBUTION, pushing our selected image-checked examples back into February.
The beginning has a garbled eight-letter VESSELS group. An apparent missing
letter in A FARCE was resolved on a fresh enlarged crop: UYIFPG contains a
narrow I, so no insertion is needed. These revisions are explicit in the alignment. The raw ending FTXIIUCGO gives OPERATING exactly, revealing a wording variant:
manuscript "never co-operating with the army" versus printed "never in
co-operation with the army." No IN insertion or final-two-letter correction
is required. This supports channel-specific
early use, not a universal switch or first-use date. Full caveats and provenance:
REPORT-2026-11-01.md; reproducer nov1_analysis.py; raw candidates and reconstructed
streams nov1_alignment.json/.tsv, nov1_controls.txt. No submission changes.

### Further coverage in the same 1 November session

- Vol196 fr0031 p56,21February, Taylor/Bullock to Wirt Adams: COMPLETE VICTORY,
  76/80 candidate positions; provisional full sense, uncertain M&O abbreviation.
  This is a direct old-key witness for an addressee of the9March change order.
- Vol196 fr0018 p31,10February, Taylor to Beauregard: COME RETRIBUTION,
  174/203 positions; heavily provisional, decoded not read. Brigades/furloughs/
  Mobile-versus-east movement. New reading marks all unresolved words.
- Vol11 fr0077b p149,20April: equipment telegram now aligns over80 cipher
  letters,79 direct. **of any** is clear; OF must not advance the key. Complete
  existing printed decipherment OR I/49/2 p1255, one final D/F ambiguity.
- Vol11 fr0041 p79,8April: readiness of Maury's regiment and Richmond news.
  Existing decipherment OR I/49/2 p1216 located after known-key reading.
  Manuscript TOWARDS versus printed TOWARD; final Danville group remains
  uncertain in segmentation. This frame has one cipher telegram, not two;
  the next clear telegram merely requests a reply "in cypher."

All six session documents have separate reading files, raw/reconstructed
alignment, key controls, and exact image URLs (`nov1_sources.json`).
Additional OR I/47/2,47/3,52/2 and Rowland Davis vol5,6,7 OCR searches did not
locate the January18 counterpart; this does not establish nonpublication.
April10 gaps remain. April11 fr0046 re-inspection and exploratory key tests
remain unresolved; uncertain transcription prevents inference of a new key.

Final community follow-up: PR#111 comments are the27October review and reply;
no later discussion was found there. The accepted earlier work remains the
latest upstream target update. All new1November findings remain local.

Final source check: vol10 fr0054 p102 is15January1865 Taylor–Davis, printed
in full OR I/45/2 p785. COMPLETE VICTORY matches opening/later phrase patterns;
full raw transcription still needed. `v10-0054_prior-print.md` labels its
predicted cipher groups explicitly; they must not be mistaken for raw evidence.
This fills a prior-print lead, not a new plaintext recovery.

### Follow-up submission

At the user's subsequent request, this work is now documented for a follow-up PR.
Six new profile records carry measured cipher-only word shares and full candidate
transcription/alignment/prose files. Navy and equipment have model-reviewed
readings; Brent, Wirt and Richmond remain in part, Beauregard decoded not read.
No independent human review or full-collection completion is claimed.
