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

**16 Nov 2026, print check for the key RALLY TO THE FRONT (Andrew Beling, with AI agents; not checked by a
person). Result: negative in the two Gaddy works read in full on their Civil War pages; Kahn not seen.**
- Kahn, *The Codebreakers* (New York: Macmillan, 1967; revised edition 1996): on the Internet Archive for controlled
  lending only, not borrowed, so no page was seen. Its text is in the archive's
  full-text index: a search for "Manchester Bluff" with "Complete Victory" returns nine copies of the book (for example
  `codebreakerssto00kahn`, 1967, and `codebreakersstor0000kahn_k4s3`, 1996), snippet "the Navy the two known
  keywords—MANCHESTER BLUFF and COMPLETE VICTORY". The search for "rally to the front" with "Manchester Bluff" returns
  no copy of Kahn and nothing in any key list; its only hits are two copies of Karen Abbott, *Liar, Temptress, Soldier,
  Spy* (2014), where the phrase was not seen in context. Page of Kahn's key passage: not given by the index, not seen.
- The standard key lists in the same index (83 items with both known keys: Friedman's lectures, Plum 1882, the
  Official Records of the Union and Confederate Navies, the *Century* 1882, Bauer's *Secret History*, Dooley 2022 and others) give
  COMPLETE VICTORY, MANCHESTER BLUFF, COME RETRIBUTION and, in some, IN GOD WE TRUST, "Interest" or "My Old Kentucky
  Home"; none of them also has "rally to the front". Two web searches found nothing either.
- Gaddy, read: "Internal Struggle: The Civil War", in Ralph E.
  Weber, *Masked Dispatches* (National Security Agency, Center for Cryptologic History, 2013 edition), pp. 88-103, read
  in full, with Gaddy's foreword (pp. v-vii), his chapters 14 (pp. 78-82) and 23 (pp. 188-191), the introduction
  (pp. ix-xv) and every other Civil War passage in the volume; the volume is typeset, so its text layer is the printed
  text. "Rochford's Cipher" (agency reprint, pp. 57-70), read in full. Neither work names any Confederate Vigenère key:
  not RALLY TO THE FRONT nor a near form, and not COMPLETE VICTORY, MANCHESTER BLUFF or COME RETRIBUTION either.
  The only key words are VICKSBURGH (sample) and EMILY NORTH, the keywords of a rotating grille used by Confederate navy
  agents in Britain in 1863 (Rochford pp. 60-61, 66). Gaddy says the Confederates adopted the Vigenère in 1862, kept
  plaintext word length, mixed clear and cipher, and that Southern telegraphy garbled the cryptograms (pp. 90-91); he
  says nothing on Taylor's department, on key changes or on April 1865 messages. Not seen: Tidwell, Hall and Gaddy,
  *Come Retribution* (1988), and *The Signal and Secret Service of the Confederate States* (1986 reprint, Gaddy's
  introduction), both lending only.
- VICKSBURGH and EMILY NORTH were tried as Vigenère keys (standard, Beaufort and variant Beaufort, at every starting
  place) on the nine unread words of the upper 11 April telegram and on every cipher stream of this folder: no English,
  and no score above the best of 1,000 random keys of the same length. The Library of Congress folder Gaddy used is
  online: Confederate States of America Records (the "Pickett Papers", MSS16550), Department of State, Box 9, microfilm
  reel 9, "Keys to the Confederate ciphers, undated", images 496-507 of https://www.loc.gov/item/mss16550009. It holds
  the Rochford grille instructions (key word VICKSBURGH), two grille dispatches whose key-letter lines use only the
  letters of EMILY NORTH, and four printed blank Vigenère squares: no Vigenère key phrase and no Vigenère ciphertext,
  so nothing there bears on the nine unread words.
- A full-text "not found" is not proof of absence (OCR can miss a phrase). Still open: Kahn's pages, on paper.

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

- 9-10 Nov 2026 (bdpayne, PR #388): seven further alignments added (vol. 10 fr. 0054; vol. 196 fr. 0022, 0053,
  0056, 0064, 0065, 0071), all conditional/provisional. Open: 8 March STEAMBOATS 11/10-letter group and the
  TLGAIIOKGS phase conflict; 9 March faint-R phase hypothesis; 17 March final MONTGOMERY group; 13/14 Feb
  duplicated OF/CAN boundaries; 13 March bracketed words; 11 April vol. 11 fr. 0046 lower telegram unread under
  every known key and convention - blocker: none outside for the first five (image re-reading), the 11 April one
  needs a new hypothesis. Re-run 11 Nov 2026: `nov9_analysis.py` reproduces every count (9 March is 124/135,
  not the 123/135 written below).

- 15 Nov 2026 (Andrew Beling, with AI agents; `blind_2026-11-15/README.md`): the open frames were transcribed twice
  blind and tested with the four known keys. Of the catalogue's open list, vol. 11 frames 0078-0081 hold no cipher
  (clear telegrams of 20-22 April and the back cover). The 9 March Levy telegram (fr. 0056 lower) is read
  (`v196-0056-levy_*`). Still open: fr. 0046 lower telegram, 11 April (fails every known key at every position; blind
  readers agree on 0.953 of its letters, so a new key or convention is needed - blocker: none outside); fr. 0046 upper
  telegram, nine middle cipher words (`v11-0046a-maury_*`; flowing capitals, readers agree on about two letters in
  three - blocker: legibility, a person's reading of the image would help).
- 15 Nov 2026, later (Andrew Beling, with AI agents; `blind_2026-11-15/rally_key/README.md`): the fr. 0046 lower
  telegram is decrypted with a new key, RALLY TO THE FRONT (`v11-0046b-maury_*`), verified on two further blind
  transcriptions. Still open there: WI[L]L needs J where the image shows the clerk's T (a hole); the M of EXACTLY at
  the gutter and the C of CLOCK under a blot are not settled; whether the key was used on any other telegram (none of
  this folder's cipher streams gives English under it) and where it came from (not in Official Records ser. I vol. 49,
  Friedman, Plum or Bates; Gaddy's chapter in *Masked Dispatches*, Kahn and Gaddy's *Cryptologia* articles not opened)
  - blocker: none outside. The first-pass candidate in `v11-0046_working.txt` is superseded by the new files.

None of these has an outside blocker, so this is not a stopping point: the folder stays "in progress" until the
remaining passages are read (mechanical with the known key; vol. 10 probably COMPLETE VICTORY).

## Escalation

- [x] siblings: the three volumes are the sibling set; four telegrams read, the rest listed above.
- [x] clear-pages: the clear text around each cipher passage was used to check the sense.
- [x] known-keys: COME RETRIBUTION fits all four; COMPLETE VICTORY and MANCHESTER BLUFF tested as controls.
- [x] print: OR I/49 pts. 1-2 searched; two telegrams printed, two not found.
- [n/a] key-rebuild: the key is known.
- [ ] retry: the remaining passages of vols. 10, 11 and 196 (PR #388 added seven alignments, 9-10 Nov 2026;
  11 April fr. 0046 retried under five keys, Vigenere/Beaufort/variant and all shifts, no reading; 15 Nov 2026 the
  lower telegram decrypted with a new key found by hill-climbing, RALLY TO THE FRONT, `blind_2026-11-15/rally_key/`).

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

## 9 November 2026 — continuation after PR205

PR205 merged2November; repository checks found no later target changes or new
catalogue681 discussion. The community snapshot and new work are in
REPORT-2026-11-09.md. Continuing existing source alignments and unresolved
readings locally; overall target remains in progress.

### 9 November 2026 — six further local alignments

PR205 merged2November; no later target change or new catalogue681 issue/PR
found in repository-scoped checks. Overall target still in progress.

Completed known-key checks of previously located15January OR I/45/2 p785
(190/213 candidate letters; manuscript RODDY, print RODDEY) and13/14February
finance OR I/49/1 pp978–979 (221/248; date and duplicated OF/CAN boundaries
unresolved). No new plaintext recovery claimed for these existing editions.

Added three provisional COME RETRIBUTION readings:13March Brandon/Tucker
reserves command,13March expected troops for possible Mobile relief,17March
attributed Orleans report about Selma/Montgomery. Added partial8March
D.W.Adams COMPLETE VICTORY reading concerning boats/railway protection,
aided by existing pencil decipherment (hand/date unknown). Eleven/ten-letter
STEAMBOATS segmentation and one unread ten-letter group remain;17March final
Montgomery group is also unequal. No full raw-continuous decipherment claimed.

April11 convention/known-key/global-shift experiments recovered synthetic
controls but no acceptable real text; all real outputs rejected. No different-key
inference. Bounded primary-edition OCR/phrase negatives do not establish novelty.
See REPORT-2026-11-09.md, nov9_alignment.json/.tsv, nov9_controls.txt, per-message
readings/notes and nov9_apr11_conventions_results.txt. Six records added locally,
with lexical measures and model reviews, not independent handwriting review.
No new PR/public submission this session.

Late8March follow-up: TLGAIIOKGS deciphers EACHENGINE exactly at COMPLETE
key offset3, versus continuing offset5. Adjacent GA and final ENEMY/USING/THEM
still fit their original phases. Saved as a strong local alternative with an
unresolved two-letter phase conflict; not silently inserted into continuous
alignment or counted as securely read.

Late9March Adams follow-up: seventh conditional reconstruction now saved.
Faint possibly cancelled R before ROAD accounts for one-letter phase gap;
raw retains it. Native crop resolves joined M in ENGINES and PRETEXT. Exact
ending ON PRETEXT OF helping Georgia Rail Roads replaces rejected PROPERTY/AS.
123/135 equal-group candidate agreements;140 raw/139 reconstructed letters.
Seven new records this session,23 total; inventory incomplete.

- 2026-11-10 (submission follow-up): User authorized another PR covering all work since PR205. Prepared seven new cases, methods, prior-text attribution, source manifest, raw/reconstructed alignments, rejected April11 experiments and remaining gaps; target stays in progress. New submission based on latest upstream main; earlier contributions preserved.

## 12 November 2026 — two telegrams of 21 February read (Brice Dudout, `dudout/`)

Vol. 196 fr. 0030 (MS p. 55, to Maury) and fr. 0031-0032 (MS pp. 57-58, to D. W. Adams), both 21 Feb 1865 and both on the
catalogue's open list, are read in full: the Maury telegram with COME RETRIBUTION (29/29 cipher words, 141/156 letters as
read; the key runs one place ahead from the seventh word), the Adams telegram with COMPLETE VICTORY (44/44, 195/206). OR
I/49/1 p. 1003 prints the Adams telegram with its cipher passage left out; the Maury telegram was not found in OR. Blind
transcription and pre-registration frozen by SHA-256 before any key was tried; the pre-registered measure picks COMPLETE
VICTORY for the Adams telegram and fails at offset 0 for the Maury one (its break is checked post hoc). Details, controls
and readings: `dudout/README.md`. Both keys on the same day fit the recipient-specific chronology above.

### Integration check of the 21 February telegrams (12 Nov 2026)

Done by an independent session after PR #438 was merged into the branch; the contributor's files in `dudout/` are unchanged.

- `prereg_measure.py` on the frozen transcription gives `measure_results.json` unchanged; the SHA-256 of the frozen transcription, the pre-registration and the script match; `posthoc_T1_break.py` and `align.py` give the stated figures (-1.2707 against a control maximum of -1.4633; 141/156 and 195/206 letters). An own decoder written from the two keys reproduces both decryptions, differing only at the corrected places.
- The NARA images (SHA-256 of fr. 0030 and 0032 as stated) were compared with the transcription: 28 of the 29 cipher words of fr. 0030 and 30 of the 44 of fr. 0032 viewed agree (EWELR: W or U), none disagrees. The rest of fr. 0032 was not compared.
- **The Maury telegram failed the pre-registered test at offset 0** (COME RETRIBUTION rank 10 of 201); the one-place key shift from the seventh word was found afterwards, so its check is post hoc. For the Adams telegram COMPLETE VICTORY is the winner, but COME RETRIBUTION also ranks 1 there; the measure alone does not separate related keys, and the reading is the evidence. The keys are known ones (WAINUT, Bryan Payne), so this is a reading with a known key (method: read with known key), not a recovery; the cipher passage of the Adams telegram is not printed in OR I/49/1 p. 1003, so it is not read from an existing decipherment.
- Words: 73 of 73 cipher words give English that fits the clear context; 21 of them (Maury 10, Adams 11) carry a one-glyph correction in the clerk's documented confusions. Decision of 12 Nov 2026: a word that needed a correction to fit is a hole, so the strict shares are 19 of 29 (0.655, Maury) and 33 of 44 (0.75, Adams), and `read_share` carries them; the contributor's 73 of 73 counts the corrected words as read and is his figure.
- The order of events (blind transcription 00:45 CET, pre-registration 00:50 CET, single commit) is by the contributor's record, as is the claim that no key was tried before.
- The target as a whole is unchanged: read in part, `fraction_read` unknown (the three volumes are not inventoried); the two telegrams are two more read documents. There is still no page for this target; `docs/_check_writeup.py --audit` listed it before this contribution.


### 12 November 2026 — bounded source audit of January 18 and April 10–11

A focused reread of the public NARA originals supports two words with the existing keys and fixed cipher-letter phases, CONTENT (18 January) and THE (10 April); a third, SENT (10 April), stays open. These are source-reading revisions, not new keys or complete telegram readings. All three were proposed from context in the 28 October 2026 continuation (bdpayne, PR #186): ODYXXRO→CONTENT in `v10-0056_decryption.txt`, and [?SENT], [?THE] in `v11-0045b_transcription.txt`. For CONTENT and THE this audit adds a reading of the original image that supports bdpayne's proposals; it does not find them. For SENT it does not settle his proposal either way. "Root" in the audit files means the coordinating AI agent of the same session, not an independent reader.

- January 18, vol. 10 fr. 0056, MS p. 107: two context-aware AI source readers prefer ODYXXRO to prior QDYXXRQ at cipher positions 243–249. COMPLETEVICTORY at zero-based phase 2 gives CONTENT exactly; the old candidate gave EONTENV. FMNA/FMNQ remains disputed, and both fresh readers prefer NEFM (literal UQOO), which worsens the proposed TROO alignment. No full-text share is revised.
- April 10, vol. 11 fr. 0045, MS p. 86, lower telegram: GJS gives THE under continuous COMERETRIBUTION. The group before it is read EIEX by one AI reader (giving SENT), but its first letter looks like this clerk's F, which gives FIEX → TENT; the coordinating agent did not check that word. SENT/TENT is open. The final groups EX FVWJ JMNH give ST ORDS BLTO and remain unread. Four visible forms JMNH replace the earlier five-letter candidate JMNCH in this comparison only. The rest of the old prefix is not certified by this audit.
- April 11, vol. 11 fr. 0046, MS p. 88, lower telegram: both source readings and meaningful glyph alternatives are preserved. A bounded standard-Vigenere comparison of three terminal variants against the five existing keys at all phases accepts no plaintext. This does not establish a new key or exclude missing-letter/segmentation errors.

Portable readings, source URLs/SHA-256 hashes, crop coordinates and deterministic checks are in `source_audit_2026-11-12/README.md`. No original images are included. Review was by AI models, with documentary context visible; it was not human paleographical certification or an entirely blind test. The opening of the 18 January telegram is already printed in *The Papers of Jefferson Davis*, vol. 11 (LSU Press, 2003), p. 339, located by Andrew Beling through the edition's official Rice index (https://jeffersondavis.rice.edu/volumes/volume-indexes/volume-11-september-1864-may-1865-index). Our coordinating AI agent read the image of p. 339 in the publisher-authorized Google Books preview (https://books.google.com/books?id=BXCeAgAAQBAJ&pg=PA339) on 12 November 2026; the image is kept locally and is not committed. Its citation is RG 109, Department of Alabama, Mississippi, and East Louisiana, Letters Sent, chapter 2, vol. 10:107, in cipher: the same page as frame 0056, so it is a modern edition of this witness, not an independent clear copy. The opening it prints agrees with the existing provisional reading. Page 340, with the ending, was not available in the preview and is unread. The Tulane Davis microfilm locator is only a potential independent witness, not an exact item located. Target ciphertexts, keys, profiles and complete-reading status are unchanged, as are Brice Dudout's two telegrams of 21 February 1865 (PR #438, `dudout/`) and the 12 November integration check of them; this audit does not touch those telegrams and does not change their read shares (0.655 and 0.75).

### Integration check (14 Nov 2026, PR #577)

Verified from the files by the integrating reader (an AI reader, not a person). No ciphertext file, key, status or read
share is changed by the audit or by this check.

- **Reproduced.** `source_audit_2026-11-12/check.py` passes; the two NARA images fetched again on 14 Nov 2026 (vol. 10
  frame 0056, vol. 11 frame 0045) have the sha256 values in `SOURCES.json`. A Vigenère routine of ours gives CONTENT
  for ODYXXRO at phase 2 of COMPLETE VICTORY (EONTENV for the old QDYXXRQ), and THE for GJS under COME RETRIBUTION.
- **Images, 18 January (frame 0056).** The 13 final groups were compared on the crop: ODYXXRO is clear (both round
  letters are O, not Q), and the sentence around it reads "but am [content] to serve in a subordinate capacity [in any
  field] you may direct". Eleven other groups agree; the third letter of OHTV and the first of MEFM/NEFM are not
  settled on the image, as the audit says.
- **Images, 10 April (frame 0045).** GJS and the four-letter JMNH agree with the audit. Two more groups read differently
  from `v11-0045b_transcription.txt` on the image: the second group looks like LYWVEW (not LVWVEW), which gives SHOUKD
  for SHOULD, and the group after EIEX/FIEX looks like MF (not NF), which gives TO. With these the line decrypts
  TQOOPS SHOUKD NOT BE SENT TO DEMO POLIS AND PORTIRN OF THE ST ORDS BLTO. The first letter of EIEX has the same form
  as the E of the group EX on the same line, which favours SENT; it is one reader's look at a 1,900-pixel crop and
  stays open with the rest. These two letters are recorded here for the next pass; the transcription file is not edited.
- **Not checked:** frame 0046 (11 April), the Davis Papers p. 339, the 225 comparisons beyond the script's own check.
- **Duplicates.** Brice Dudout's 21 February telegrams (`dudout/`) are separate and untouched. The repository's reading
  check fails on those two entries (state "read" at 0.655 and 0.75) on the coordinator branch as well; that is an older
  item, not part of this pull request.
- **Status.** In progress, no page. The audit supports two of bdpayne's contextual words on the image and leaves the rest
  open.

### Follow-up on the PR #577 notes (15 Nov 2026, Andrew Beling, with AI agents)

The three groups of 10 April (vol. 11 frame 0045, MS p. 86, lower telegram) that the integration check read differently
were looked at again on the full NARA frame (7331 x 4767 px, sha256 `a9afc23e...59a6` as in `SOURCES.json`), in two
passes by one AI reader (Claude), not by a person: pass 1 on enlarged grayscale crops of each group, pass 2 on the whole
line in original colour and in grayscale, with comparison letters from the same telegram.

- **LYWVEW, not LVWVEW.** The second letter has a long descender with a turned tail, the form of the Y in XCYKG on the
  next line and of the y in the clear word "why" above; it is not this clerk's V. Both passes agree. The group gives
  SHOUKD. The fifth letter has a top bar, a flagged middle stroke and a foot, the same form as the second letter of
  VEASGW; SHOULD and TROOPS would need F there, so the image gives E in both groups (an encoding or copying slip, or a
  form this clerk used for both letters); this is not settled here.
- **MF, not NF.** The first letter is a straight stroke, a diagonal and a hooked last stroke, the three-part form of the
  M in MRU (which decrypts to AND, so M is attested there) and in JMNH; this clerk's N in JMNH has two parts. Both passes
  agree. The group gives TO.
- **EIEX.** The first letter carries a foot stroke like the E of EX on the next line; the F of MF and of LFGH has none.
  This leans to E and SENT, as the integration check says; it rests on AI readers only and stays open.

`v11-0045b_transcription.txt` now carries these groups and the earlier ones as superseded. Decrypted with COME
RETRIBUTION from position 0: TQOOPS SHOUKD NOT BE SENT TO DEMO POLIS AND PORTIRN OF THE ST ORDS BLTO. No reading, share,
key, status or profile figure changes: the telegram stays outside the completed readings, and EX FVWJ JMNH stay unread.

## 15 November 2026 — the open frames transcribed twice blind; 9 March to Levy read (Andrew Beling, with AI agents)

Work by AI readers (Claude, Opus), not checked by a person. Details, figures and files: `blind_2026-11-15/README.md`.

- **Method.** Four readers transcribed the cipher groups of the open frames from the NARA images, each alone and
  without any earlier transcription, key or decryption, after passing a seed telegram (90% mark). A test plan was then
  frozen (sha256) before any key was applied: four known keys at all 15 positions on each reader's transcription,
  quadgram score, a one-slip model, 400 controls per telegram and reader (shuffles maximised over all four keys, and
  random keys); pass above the highest control.
- **Agreement.** 1230 of 1317 letters over twelve telegrams (0.934); weakest the flowing capitals of the first
  11 April telegram on fr. 0046 (60/94).
- **Test.** Positive controls pass. Eleven of twelve telegrams yield for both readers with the key the folder already
  gives for their date. **Miss:** the second 11 April telegram on fr. 0046 fails under every key and both models. The
  run was repeated by a verifier with identical figures.
- **New: 9 March 1865, Bullock for Taylor to Lt Col Wm. M. Levy** (fr. 0056 lower telegram;
  `v196-0056-levy_reading.md`): COMPLETE VICTORY from position 0. "The Lieut. Genl. Comdg. understands there are one
  hundred & fifty five CARS or [on] MOBILE and MONTGOMERY R. R. and thinks such of them as are not needed for daily use
  should immediately be TRANSFERRED ON TRUCKS to WIDE [?GUAGE] AT COLUMBUS, GA. ... It might be done UNDER PRETENSE
  OF ASSISTING ROADS in Georgia." 21 cipher words: 20 read; GUAGE needs I for J twice, and the image shows the clerk's
  J both times (a correction against the image, so a hole). COLUMBUS needs F where two readers read E: F is one
  reader's first reading and another's marked alternative (the stroke allows it). It is the order to Levy that the
  same day's telegram to D. W. Adams (`v196-0056-dw_reading.md`) announces. Not printed in OR I/49/1 (p. 1042 prints
  the clear telegram on the left of the same frame, Taylor to Maury, 9 March) or I/49/2.
- **New in part: 11 April 1865, Surget to Maury** (fr. 0046 upper telegram; `v11-0046a-maury_reading.md`): COME
  RETRIBUTION. "ONE [?OF] THE [?TRAINS] from Mobile last night brought [... 9] and quite a number of BALES OF COTTON
  FOR THE RAIL ROAD COMPANY." 21 cipher words: 10 read, 2 need one letter no reader saw (holes), 9 unread. Not in OR
  I/49/2 (pp. 1223-1226 print the clear telegrams of 10-11 April around it).
- **Confirmed** (blind transcriptions, same keys and phases as the earlier readings; the earlier files are not
  edited): 8 and 9 March to D. W. Adams, 13 March to the Secretary of War, 13/14 March to Maury, 17 March to Taylor
  (Bryan Payne, PR #388); 10 April to Taylor (fr. 0044 first passage) and to Maury (fr. 0045), and 18 January to Davis
  (Bryan Payne, 28 October and #388). The word-by-word comparison, including the words that still need a letter, is
  in `blind_2026-11-15/reading_tables.md`; these are proposals for the reviewers, not changed readings.
- **Verification.** An independent verifier and a second blind helper transcribed the Levy and the first 11 April
  telegrams from the images before seeing this work (107/109 and 67/91 letters agreeing between the two), decrypted
  their own transcriptions with every known key at every position and got the same words.
- **Not changed:** `profile.json` outcome, read shares and reading reviews. The two new telegrams are not yet entries
  in `outcome.texts`; their reading review is the reviewers' to record.

## 15 November 2026 — the second 11 April telegram decrypted with a new key, RALLY TO THE FRONT (Andrew Beling, with AI agents)

Work by AI agents (Claude, Opus), not checked by a person. Details, figures and files: `blind_2026-11-15/rally_key/README.md`.

- **Telegram.** Vol. 11 fr. 0046, left page, lower telegram (`v11-0046b-maury_reading.md`): Meridian, 11 April 1865,
  E. Surget, A.A.G., to Maj. Gen. D. H. Maury, Mobile; 107 cipher letters in 22 groups. It failed every known key in
  the blind test above.
- **Key.** RALLYTOTHEFRONT, standard Vigenère, key from the first cipher letter, over cipher letters only (the rule of
  the rest of the folder). Found by an unconstrained hill-climb over 15-letter keys after a frozen plan; the key that
  came out is an English phrase. The search's calibration missed its own mark (12 of 15 key letters on 5 of 7 known
  telegrams: 3 of 7 for both readers, 5 of 7 for either), so the find rests on the decryption and its checks.
- **Reading.** "Let me know EXACTLY HOW LONG YOU WI[L]L HOLD THE CITY as the RUNNING OF THE TRAINS DEPENDS on that. If
  you can HOLD ON UNTIL NINE O CLOCK TOMORROW Can have four or five ADDITIONAL TRAINS THERE." All 22 groups give
  words. WI[L]L needs J where every reader reads the clerk's T: a hole. Ten letters are readers' alternatives or
  shape readings the image supports, two are possible but unsettled (`v11-0046b-maury_decryption.txt`).
- **Verification.** Two new blind transcriptions (104 of 107 letters agree). Frozen test on their first choices:
  11 of 22 groups give words, **a miss** against the mark of 15 (12 of 25 against 17); every control 5 or below
  (400 random keys; the four known keys at all offsets). The misses come from three misreadings the image settles:
  this clerk's F (his E without the lower-right tick, read E by both), V (read Y) and the gutter M (read D). A blind
  shape test on 14 shuffled E/F letters sorted 12 as the key needs (mark 12).
- **Pencil.** Faint numerals "15" stand over cipher letters 30, 45 (very faint), 60, 75, 90 and 105, none over 15,
  and an unclear mark over letter 20 (the letter the reading cannot take from the image); seen by two blind helpers
  separately and by the verifier.
- **Other telegrams.** The key at all phases on every cipher stream of this folder, including the nine unread words of
  the first 11 April telegram: no English.
- **Literature.** The phrase is not a key in Official Records ser. I vol. 49 pts. 1-2, Friedman's Civil War lectures
  (which list COMPLETE VICTORY, MANCHESTER BLUFF, COME RETRIBUTION and IN GOD WE TRUST), Plum or Bates, nor in an
  Internet Archive full-text search. Not opened: Gaddy's chapter in *Masked Dispatches*, Kahn, Gaddy's articles.
- **Fit.** OR I/49/2 pp. 1225-1226 (Gibson withdraws the Mobile infantry and artillery on the night of 11 April;
  Bullock's clear telegram to Maury the same day) and p. 1255 (Taylor: "Mobile was evacuated by General Maury on night
  of 11th"). Not printed there.
- **Not changed:** `profile.json` outcome, read shares and reading reviews; the telegram is not an entry in
  `outcome.texts` (its reading review is the reviewers'). `key.md` notes the second key.

### Integration check (15 Nov 2026, PR #676)

Done by an AI reviewer for the maintainers. The contributor's files are unchanged. One person has since looked at the
disputed letters of the 11 April lower telegram (last point below); nothing else here was checked by a person.

- **The key stands; its frozen word test does not.** RALLYTOTHEFRONT was applied with a separate decoder to the filed
  letters and to each blind transcription of the 11 April lower telegram. Against the plaintext given, 1 letter differs
  on the filed letters (20), 6 on B1, 9 on B2, 12 on helper A and 11 on helper B: 15 places in all. Five of them have no
  reader's first choice (20, 34, 64, 76, 77). The frozen test on the two later transcriptions (11 of 22 groups as words
  against a mark of 15, controls at most 5) is a miss and stays recorded as failed.
- **Why the key is accepted all the same.** (1) With the fixed key the two later blind transcriptions, which had no part
  in the search, give HXACTLP HOW LNNG YNU WIVL HOLD THE CITY RTNNING OF THE TRAINS DEPENDS HOLD ON TNTIL NINE O CLNQK
  TOLARROW ADDITIONAL TRAINS THERE. (2) Own control with the shared English quadgram model (`lang`, en-modern): those
  texts score -3.66 and -3.71 per letter and the filed letters -2.25, against -4.10 for the best of 40 shuffles of the
  telegram, each hill-climbed over all 15-letter keys (median -4.44). A free 15-letter key on 107 letters does not reach
  this on shuffled text. (3) The search was not asked for a phrase and returned one. (4) Pencil "15" marks stand over
  every fifteenth letter from the 30th (seen again on the frame). The control is small (40 shuffles, one model).
- **On the image** (NARA frame 0046 fetched again; sha256 as recorded in `source_audit_2026-11-12/SOURCES.json`): the
  six letters the key needs as F (12, 16, 34, 64, 76, 81) lack the lower-right tick that the clerk's E carries in the
  same words (VXLNRE, HTTE, FLMWE, PEFQV, EMFC...); letter 1 has no descender (V); letter 20 is T; letter 77 has a
  tail or blot at its foot and is not settled; letter 7 is cut by the gutter.
- **Strict count.** 11 April lower telegram: 23 words in 22 groups, 21 sure; WILL and CLOCK are holes (0.913; the
  contributor counts one hole, 22 of 23): read in part. 9 March to Levy: 20 of 21 cipher words (0.952), GUAGE a hole:
  read. 11 April upper telegram: 10 of 21 cipher words, nine unread in the middle: decoded, not read, no entry in
  `outcome.texts`.
- **Recorded in `profile.json`:** documents and `outcome.texts` entries for the Levy telegram and the 11 April lower
  telegram, each with a reading review (grade A, by the reviewer, a model, not a person); `*_cipher.txt` and
  `*_read_measure.txt` for both; credits for Andrew Beling; one verification step. For the 11 April lower telegram the
  method is "key recovered from ciphertext-only"; the folder's method is unchanged.
- **Check by a person (15 Nov 2026).** Daniel Bourdeau was shown eight words cut from the frame at full resolution
  (`review_2026-11-15/taylor1865_review_sheet.jpg`), the
  letter in question boxed and a sure E boxed beside it, and agrees with the reviewer on each: F, not E, at 12, 16, 34,
  64, 76 and 81 (64 less sure: ink specks under the letter); V at letter 1; T at letter 20 (WILL stays a hole); Q at
  letter 77, the tail being a blot in darker ink (CLOCK stays a hole); letter 7 at the gutter not settled. It was not a
  blind check: he had the reviewer's reading and what the key needs in front of him. The count is unchanged: 21 of 23
  words, read in part. The Levy letter of 9 March has not been looked at by a person.
- **Prior art.** A web search and an Internet Archive full-text search for the phrase with "cipher" or "Confederate"
  found nothing. Gaddy (*Masked Dispatches*, *Cryptologia*) and Kahn are still not opened: the key is "not found in
  any key list opened", not "unknown".
- **Not re-run:** `rally_key/verification/run_verify.py` needs `/usr/share/dict/words`, absent here (its printed
  plaintexts equal ours); the key-search scripts need the Official Records text. The frozen hashes of the two helper
  transcriptions and of the test plan match the files; the order of events is by the contributor's record.

## 24 Nov 2026 - three blind sign sheets on vol. 196 fr. 0018, 0065, 0071, 0064, 0056 (Brice Dudout, with Claude), `dudout/sign_check_2411/`
The targets are 39 glyphs where the aided alignment's letter differs from the letter COME RETRIBUTION predicts. The
rules were hashed before the thumbnails, and the controls passed 9/9. The key and the alignments are unchanged.

- **Re-read as the key predicts:** 29 glyphs.
- **Confirmed as the clerk's own divergence:** 8.
- **Unresolved:** 2.
- **Words no longer marked [?]** (read_measure and reading files): fr. 0018 22 -> 28 of 44; 0065 11 -> 15 of 18;
  0071 9 -> 12 of 14; 0064 8 -> 9 of 13; 0056 (D. W. Adams) 19 -> 22 of 27. read_share is updated in `profile.json`.
- States are left to the maintainer. No image is committed.
- **States set at integration (owner's decision, 24 Nov 2026):** fr. 0071 is read by the short-text floor (14 cipher words,
  2 holes: SELMA, MONTGOMERY; `floor_used` in `profile.json`). The other four stay read in part. The target class stays read in
  part, as 12 documents are still read in part.

## 25 Nov 2026 - blind sign sheets D and E on fr. 0018 (Brice Dudout, with Claude), `dudout/sign_check_2511d/`
Sheet D continues sheet A on the Taylor to Beauregard telegram of 10 Feb 1865 (vol. 196 fr. 0018), groups 14-48.
Groups 26-49 were segmented by eye for this sheet; the g23p5 box of sheet A was recomputed. The rule was hashed before
any thumbnail was cut (`sheet-D-rule.md`, 4b0bc29d...; amendment 1 re-cropped two V examples before any answer). The key
and the alignment are unchanged. Merged as PR #982; integrated 26 Nov 2026.

- **Sheet D (12 targets, controls 3/3; in `outcome.sign_check`).** Re-read as the key predicts: 7 (F g29p2, g29p5,
  g35p4; L g32p2, g37p1, g48p3; M g34p1). Confirmed as the clerk's own divergence: 4 (g14p2 I, g23p5 C, g27p2 G,
  g31p1 R). g5p1: "none / other form", followed up on sheet E.
- **Sheet E (3 targets, controls 3/3; under the 8-sign minimum, so here and in a solution step only).** g5p1, g17p5 and
  g28p1 all Z. g5p1 is this clerk's Z written once with an irregular stroke; no new letter. The "TL" option on three
  questions is g5p1 itself, so the Z call rests on the choice of Z over T and L. No word changes (BRIGADES stays marked
  for g4p1).
- **Before / after (owner rule of 25 Nov: a blind shape call may move read_share when NOTES and a step give the
  counts).** Words without [?]: 28 -> 34 of 44 (MOBILE, THAN, SENT, EAST, BUT, FURLOUGHS unmarked; `owner-files.patch`
  applied to the read_measure and reading files). Glyphs agreeing with the key: 185 -> 192 of 203 after D, 193 after E.
  read_share 0.6364 -> 0.7727.
- **Still marked (10):** AND, OF (g19p1), not on a sheet; BRIGADES (g4p1 F2); THEIR, MEN, VERY (clerk's divergences,
  sheet A); RETURNING, LITTLE, SERVICE, QUICKER (clerk's divergences, sheet D). All read by sense.
- **State set at integration (26 Nov 2026):** fr. 0018 "decoded, not read" -> **read in part** by the house bar: 44
  cipher words, above the short-text floor, all read by sense in coherent sentences, 34 sure. Brice's "under 300 cipher
  letters, no change to read" is his own rule and is not applied. 12 documents are now read in part (count from `profile.json`); the target class
  stays read in part.
- **Redactions (declared, not checked):** the committed `sheet-D-answers.json` (remark at q11) and `sheet-E-rule.md`
  (the same remark quoted) are redacted; the original hashes are 61d312fe... and 12d17840... The glyphs on the NARA
  frame and the new boxes for groups 26-49 were not checked by the integration review.
