# Montcalm’s War code (“code W”) and the cipher texts of 4 November 1757

Status: in progress (folder only, no page)

Class: read in part (key recovered based on adjacent plaintext). The partial key is rebuilt from the period interlinear decipherment, and the French prose is that decipherment, transcribed and normalized. This is a source-and-key contribution, not an independent solution.

**The anonymous period clerks who deciphered these passages read them first.** Andrew Beling, with AI agents, transcribed the archival copies, rebuilt the code evidence and translated the texts in November 2026.

## Documents and limits of coverage

Service historique de la Défense (SHD, the French army archives at Vincennes), GR A1, volume 3457: Montcalm to the war minister Paulmy, Québec, 4 November 1757, pièce 179, and the attached cipher sheet, pièce 180. The copies made for the Public Archives of Canada, now Library and Archives Canada (LAC), MG4 B1 série A1, reel C-12578, preserve both the figures and the interlinear plaintext. [Letter start, frame 523](https://heritage.canadiana.ca/view/oocihm.lac_reel_c12578/523); [cipher start, frame 525](https://heritage.canadiana.ca/view/oocihm.lac_reel_c12578/525); [food passage, frame 530](https://heritage.canadiana.ca/view/oocihm.lac_reel_c12578/530); [annex, frame 537](https://heritage.canadiana.ca/view/oocihm.lac_reel_c12578/537).

Declared reading units: **all cipher extracts** of 179 (copy pp. 505–506 and 510–513, 610 groups), and **all of the cipher annex** 180 (pp. 517–518, 306 groups). The clear sections of 179 are outside the claimed text and are not described as fully transcribed. Supporting 1756–1759 letters and one page of the Lévis 1759 cipher are supplied as research evidence in `support/`, not counted as documents read here.

Each declared unit has the full figure transcription (`transcriptions/`), the period decipherment line by line (`line_by_line_*.txt`, `contemporary_*.txt`), normalized French (`reading_fr_*.txt`) and English (`translation_en_*.txt`). The texts discuss Louisbourg’s defences; the bread and meat crisis; and the defence of Québec between the Montmorency falls and the Saint-Charles. The annex also discusses planned expeditions and supplies for the western posts.

## Historical context

The cipher passages are what Montcalm hid from the clear text: an officer’s report that Louisbourg’s works “ne vaut rien”, the quarter-pound bread ration with cod and horse for beef, Vaudreuil and Bigot asking him “de vous à moi” to press the King, and, on the annex, a plan to force an English landing onto the shore between the Montmorency falls and the Saint-Charles and hold it with redoubts, lines and cannon. According to the Dictionary of Canadian Biography (W. J. Eccles on Montcalm and Vaudreuil, C. P. Stacey on Wolfe, J. F. Bosher and J.-C. Dubé on Bigot), that shore was fortified under Montcalm’s direction in 1759 and the French army held it at Beauport; Wolfe’s attack there on 31 July 1759 failed, his landing at the Anse au Foulon led to the battle on the Plains of Abraham on 13 September 1759, where Wolfe was killed and Montcalm mortally wounded, and Québec capitulated on 18 September. Louisbourg had surrendered on 26 July 1758. The 1757 sheet anticipates the 1759 Beauport line, but nothing read here shows that the 1759 works were built from it; the 1758–59 proposals of Montcalm, Lévis and others were not read, and the same biography notes that as late as March 1759 Montcalm thought Québec had little to fear from the river.

## System and key

“Code W” is our working label for the War Department numerical code, not the title of a recovered key sheet. Numbers stand for letters, syllables, words and names, without alphabetical order. `key/W_1757_attestations.tsv` indexes 318 clearly numbered groups from the 1757 cipher/decipherment pairs, keeping conflicting values and sic observations with their counts (`KEY_SCOPE.md`). `key/uncertain_digits.tsv` withholds two uncertain numbered occurrences, so that a miscopied group does not create a false homophone. The expanded 430-entry alignment table from the exploratory work is deliberately not presented as a key.

The digit rechecks corrected p. 511, 13? to 83; confirmed 886 and the problematic literal 63 on p. 517; and left two groups unsettled: p. 506, 6?0 (670 or 690: the middle stroke is open like this copyist’s 7s, though two earlier readers saw a 9) and the middle digit of p. 518, 2?5. On p. 510 the first group is a clear 159, and the copyist’s “+” stands after 139 (“toujours”), so his margin “sic pro 159 = une” means “une livre de bœuf”; the reading and translation follow the correction. Supporting p. 167 (1758) reads 60 and 83, not 670? and 13?. The 1756 group ?59 remains uncertain. Details in `DIGIT_AUDIT.md`.

Not the Vaudreuil table. Brice Dudout’s `targets/vaudreuil1760/` (with `vaudreuil1759a`–`c`) reads Vaudreuil’s letters to the Marine minister with the 1757 Vaudreuil numerical table, ANOM COL C11E 10 (Archives nationales d’outre-mer, colonial series), LAC sheet e001295274 (`targets/vaudreuil1760/key/key274.json`). Code W is a different code: of the 243 numbers present in both that table and our attestation index, none has the same value (checked 13 November 2026). Casgrain’s *Collection des manuscrits du maréchal de Lévis*, III (1890), p. 64 prints Paulmy’s letter of 10 April 1757 sending Montcalm “un petit chiffre”. Whether that is code W is uncertain: Paulmy offers it for a private and secret correspondence, apart from Montcalm’s ordinary letters to the war minister, while code W is used in the ordinary dispatches and is already in Montcalm’s cipher postscript of 3 November 1756 (`support/W1756-11-03_A1_3417_duplicata.txt`).

Follow-up done on 13 November 2026 by one of our AI agents (not yet rechecked by a second one): the third numerical sheet of the same volume, LAC e001295276 (`targets/vaudreuil1760/NOTES.md` says the volume holds a 1758 Montcalm table without naming the sheet; that table is sheet e001295272, not this one), was transcribed twice and compared. It is a second handwritten copy of the Vaudreuil table on e001295274 (592 of 680 cells agree) and agrees with code W on 1 of 238 shared numbers, no better than 200 shuffled tables. It is not W.

## Prior readings, editions and our contribution

- The period French decipherment is written between the lines of the archival copy. The anonymous decipherers are credited; their identity and the date of the decipherment are not asserted beyond the source.
- *Documents relative to the Colonial History of the State of New-York* (NYCD), X (1858), pp. 669–671 prints an English translation of the covering letter and omits the cipher paragraphs (“a paragraph in cipher, which is omitted”); the attached cipher sheet is also absent from that edition (`support/NYCD_omission_check.md`). We say only that this edition omits them.
- Phrase searches of the OCR of Casgrain’s Lévis collection (I–XII), Chapais 1911 and the available years of the *Rapport de l’archiviste de la province de Québec* (RAPQ, 1920–1942) found none of these passages. OCR negatives do not establish a first publication, and the 1924–1927 RAPQ volumes were not available to us.
- Casgrain’s edition (vol. III, 1890) also prints cipher/plain pairs of two other Montcalm codes (B and I); those tables are different systems and are not used for W.
- *Collection de manuscrits … relatifs à la Nouvelle-France* (CMNF), IV (1885), p. 153 already prints the memoir’s French prose. Its residual groups 583 878 110 103 83 give «peuples» with the 1757 values, the last word of its preceding clear sentence; that identifies a word, it does not reveal a new passage. Its 31-group footnote remains only partly resolved. [CMNF scan](https://archive.org/details/collectiondemanu04blan).

`support/research_summary.md` and `support/research_readings.md` keep the earlier exploratory record. These notes, the revised transcriptions and the digit audit supersede its older claims (320 clean entries, 13 = s, 670 = rt, confident digit readings). Supporting evidence: [1756 postscript](https://heritage.canadiana.ca/view/oocihm.lac_reel_c12577/934), [May 1758](https://heritage.canadiana.ca/view/oocihm.lac_reel_c12578/1022), [September 1758](https://heritage.canadiana.ca/view/oocihm.lac_reel_c12579/172), [Lévis 1759 cipher sample](https://heritage.canadiana.ca/view/oocihm.lac_reel_c10523/345).

## Remaining gaps

- Unsettled 1757 numerals, p. 506 6?0 (670 or 690, read “rt”) and p. 518 2?5 (read “em”) - blocker: needs-physical-access; the LAC copy is ambiguous and the readers disagree, so both are withheld from the key; the French originals at Vincennes would settle them.
- Conflicting 1757 values, chiefly 63 written over “s” where the usual reading is “vivres” - blocker: open-codes; copy slip or enciphering slip cannot be told apart without the original key or the original letters.

Outside the declared units, and not counted as gaps in them: the clear text of the covering letter, the full Lévis 1759 sequence, and a fuller prior-publication check (the RAPQ volumes for 1924–1927 were not available to us).

## Escalation

- [x] clear-pages: the period interlinear decipherments of both declared units located on LAC C-12578 and transcribed.
- [ ] siblings: 1756–1759 supporting pages sampled (`support/`); the complete Lévis 1759 sequence and the French originals not yet inspected.
- [ ] known-keys: Casgrain’s codes B and I and the Vaudreuil table e001295274 compared, none is W; sheet e001295276 tried on 13 November 2026 and found to be a second copy of the Vaudreuil table, not W; no original W key located.
- [ ] print: NYCD X, Casgrain I–XII, CMNF IV, Chapais and RAPQ 1920–1942 screened; RAPQ 1924–1927 not checked; no claim that the text is unpublished everywhere.
- [x] key-rebuild: 318 clearly numbered values indexed from the period plaintext; conflicting values and uncertain digits withheld or qualified.
- [ ] retry: the doubtful digits retried with a second AI reader on fresh crops; a comparison with the French originals and a retry of every source slip not done.

The LAC copies supplied adjacent plaintext, so this was source alignment, not ciphertext-only cryptanalysis. Further key recovery should use the untranscribed Lévis cipher pages and the French originals.

## Independent recheck, 13 November 2026

A second AI agent of ours, which had not seen our conclusions, rechecked 25 table entries against the reel images (24 confirmed, 1 unsettled: the p. 506 group above) and read p. 511 and p. 517 lines 1–11 digit for digit, with no differences. It also found the p. 510 sic placement and two loose translation phrases (“out of every eight days”; “and an expedition”), now corrected. It is not a person and not an outside check.

## Internal prose review, 12 November 2026

One of our own AI agents (the coordinating model, not a person) read both complete normalized French texts against their English translations. The final clause of 179 now reads conditionally: without the provisions taken from the English, the country would have been lost. Words supplied in 180 stay marked in the English as in the French. The profile records grade A reviews limited to this prose comparison and selected digit crops; they are not an exhaustive check against the images, and not an outside or human check. The independent digit check was also by an AI reader, with the interlinear plaintext visible.

## Coverage and validation

`measure_reading.py` counts editorial holes in the two normalized French reading units, treating every unmarked word as known: **637 of 648 words unmarked** (424/431 in 179, 213/217 in 180; `reading_measurements.json`). This is the share of words in our edition of the period decipherment that carry no uncertainty mark. It is not cipher-group coverage and not a measure of accuracy; both units stay “read in part” because of the withheld digits and source slips above. The French sentence checker gives 0.946 and 0.950 clean sentence shares, a different measure.

Held-out statistical validation is recorded as not applicable (`docs/_validate.py --na`): the table was built from these same period cipher/plain pairs and the prose is the existing decipherment, so a shuffled-key test would not validate an independent recovery. Testing the table on a new W ciphertext remains possible future work.
