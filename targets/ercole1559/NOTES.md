# ercole1559: Ercole II d'Este to Cornelio Bentivoglio, 28 May 1559 (catalogue 1566)

Status: read in part (3 Nov 2026), as a transcription job. Biblioteca Estense Universitaria, Modena, Autografoteca Campori, Lettera E, Este (d'), Ercole II d'Este, duca di Ferrara, cc. 50-51.

Catalogue 1566 holds three letters in three systems. One key, one entry: this folder has the 1559 letter to Bentivoglio and a note on Ariosto's c. 1, which is not solved, and `targets/alfonso1576` has the 1576 letter.

Transcription and reading were done by AI language-model agents viewing the images. No human palaeographer has checked them. An independent AI verifier checked the first version; its report is `VERIFY.md`, unchanged, and it covers both folders. This version applies its must-fix list. No independent check has been run on this final version.

| Signs | Job | Words | Reading as sense | No restored or changed letter | Status |
|---|---|---|---|---|---|
| 870 | transcription job; a contemporary interlinear decipherment covers it | 197 | 195 (99.0%) | 181 (91.9%) | read in part |

Words are counted in the cipher only. "No restored or changed letter" excludes every word with a `<x>` or `[?x]` mark. "Reads as sense" counts every word but the two wholly doubtful ones. `python scripts/check_marks.py 50` makes the count, and fails on any letter that departs from the decryption without a mark.

**The catalogue's vetting note is wrong on one point:** it says there is no decipherment, interlinear or gloss. The whole cipher of c. 50r has one. A brown-ink hand writes the plain text between the cipher lines. It was missed at 25%, where it looks like show-through. Hence a transcription job, not a break.

## System

A one-to-one simple substitution: 20 signs for 20 letters, plus one sign L for *et*. No nulls, no code groups, no word division. Each sign carries one dot above, filled or open, which we took as pen style. We looked for no value in the dots and found none. See `key_1559.tsv`.

The short 4-form is d and the long-tailed q form is g; these are separate signs. The catalogue's "about 25 shapes" comes from such variants. 2 appears with a square or a round loop, and ] sometimes as a small closed loop; we treat each as one sign.

## Key and held-out test

Built by a table-free hill-climb on rows 1-9 only, signs against the gloss as read. It found all 20 letters, with 388 of 407 gloss letters matched. L came out as t; we set it to *et* by context. Frozen, then applied to rows 10-19 of the second-pass copy, it agreed with the gloss at 382 of 398 letters (96.0%; 200 shuffled tables: mean 29.7%, best 38.7%; the verifier's shuffles: mean 32.4%, best 42.0%). That test is weak. The same reader read the gloss before the signs of those rows, and the verifier then showed that those signs had bent toward the gloss. On the third-pass copy the same count falls to 367 of 398 (92.2%). The key does not change: no sign moved value.

## Transcription: the third pass

The verifier compared 147 blind signs in rows 08-10 and found 7 errors, all toward the gloss (`VERIFY.md` section 1). So c. 50r was copied again, row by row, on strips that show only the band from the dots down, so that the gloss is off the strip (`scripts/row_copy.py`, `row_zoom.py`). Doubtful places went to 2.1x strips, where one dot per sign gives a count that needs no language.

All seven corrections hold on the image: chio, masime, duo, manera, Sanes|i, uogliono, sria. 33 sign places changed in all, over 26 entries, and the count falls from 880 to 870. See `sign_changes_c50r.tsv`. The verifier's rate of 7 in 147 had pointed to about 40 wrong signs on the page.

The other places matter more than the seven, because they move the sense:

- Row 17 ends with two signs, a heavy one and n, and not `per la`, five signs; ten dots for ten signs in that strip. So "[?i]n".
- Row 18 opens `Q A I 8 n V`: *questa*, not *quella*.
- Row 18 has `8 A I`: *sue*, not *sia*. With "dep`<e>`ndente" that gives "this matter and what depends on it".
- Row 16 has `n A n n T`: *in tutto*, not *intanto*.
- Row 19 has `d` at the sixth sign, the same shape as the other two c in the row, and not theta: *concoreno*, not *son coreno*. This settles the doubtful word of the first version, which had read the row with the gloss in view.
- Row 11 has *poter saper*, with no final e, as the gloss has it. Row 12 has *parimenti*, where the gloss has *partimente*. Row 13 has *littere*, where the gloss as first read has *litere*.

Limits. This reader had the earlier transcription and the gloss's text in mind, though not in view, and at the doubtful places it was thinking about sense. So the pass is sign-first but not blind. Rows 1-6 were read at 1.5-1.7x only. The third-pass readings at the end of the letter go against the gloss and have had no second reader. They should be the first thing a checker looks at.

Word count: 197 words, 195 reading as sense, 181 with no restored or changed letter (91.9%). The bar is 188, so it stays read in part, as a transcription job.

Two attempts at a language-free shape check failed: machine segments could not be paired with the transcription (k-fold 5.9% and 8.0%, against 8.6% and 9.3% best for shuffled labels). That says nothing for or against the signs.

## Reading

The Pope will not receive the ambassadors of "those lords", gone to him to ask favour. Ercole, who has less force than the Pope, must be careful. He has also heard that the capitulation between the two kings leaves the Sienese unable to give themselves to whom they wish. He hopes to know more in two or three days, and asks for Bentivoglio's opinion on everything further he should consider in this matter and what depends on it.

The address on c. 51v calls him lieutenant of His Most Christian Majesty in Tuscany. "Cotesti signori" must then be the Sienese republic in exile at Montalcino, whose fate was being settled after Cateau-Cambresis. One source puts Bentivoglio at Montalcino in July 1559 (https://www.theflorentine.net/?p=13411). The rest of this paragraph is from general knowledge and was not checked: the treaty of April 1559, Montalcino passing to Cosimo I that summer. Gioan Antonio di Gravina is not identified; a search found an Orsini of Gravina of that name, with no link to these events.

The long clear postscript in another hand is given in the reading file. Ercole wants to reassure Philip II before he sails for Spain and to visit both courts at the weddings. His son Alfonso, held in France for the jousts, delays it. It is worth a historian's look on its own, though it is not a cipher.

The word *dre a chi* is in the signs. *Dare* is a repair, the key sentence depends on it, and it stays marked. In the gloss the d has a small raised stroke, seen on a crop. It may be a superscript a, which would give *dare* in the decipherer's own hand. It is not plain, so this does not lift the mark.

## Claudio Ariosto, c. 1, 15 Jul 1559: not solved

Biblioteca Estense Universitaria, Modena, Autografoteca Campori, Lettera A, Ariosto, Claudio, c. 1. It is listed here because it is the third letter of catalogue 1566. It is not a document of this entry, and its key is not this key.

Clear letter announcing the death of His Most Christian Majesty, with a passage of about 35 signs in cipher, between "per quanto" and "la cap.ne della pace non si intende haver luogo col futuro". Mixed Greek and Roman shapes, a triangle, a box, the digits 1 3 in line, and digits above many signs. The Ercole key gives nothing here: `os a?gs l`. The shapes differ and the superscripts have no place in that system. There are no pairs, and the passage is too short for a ciphertext-only attack on a system whose rules we do not know. Stopped. First look only: `transcription_c1_1559-07-15_FIRSTLOOK.txt`, one reader, shapes approximate. The second leaf was not examined at full size.

## Prior art and collision (2-3 Nov 2026): open

- Collision: rechecked at upstream head 3c777efd5, and on 3 Nov against the open pull requests and head d06538173. No target folder, no commit, no pull request for these documents.
- The interlinear decipherment is the prior reading of c. 50r, and we used it to build the key.
- Web searches on Ercole II and Bentivoglio 1559 and on Bentivoglio at Montalcino found no edition or decipherment. Search results do not settle that. The history of the fall of Montalcino was not read, and letters of Bentivoglio to Ercole may be printed.
- The key-bearing archive is unopened: ASMo, Cancelleria ducale, Cifrario, 8 buste (https://www.filodiritto.com/la-parola-incognita-cifre-e-cifrari-alla-corte-estense). We make no claim that this text is unknown.

## Remaining gaps

- The heavy signs in rows 07, 10, 13 and 17 and the blots of rows 01 and 10 - blocker: illegible; the ink hides them. Multispectral images might settle them.
- "[?haura]", crowded signs - blocker: illegible.
- The third-pass readings of rows 16-19 go against the gloss and need a second reader - blocker: not-attempted.
- The gloss has only a first reading - blocker: not-attempted; rows 04, 10, 13 and 14 are incomplete, and whether the hand is the recipient's or his secretary's is open.
- c. 50v: the end of the clear text was read only for sense - blocker: not-attempted.
- Ariosto c. 1, about 35 signs - blocker: too-short; no pairs, unknown system.
- Prior art: ASMo Cifrario, Bentivoglio's correspondence - blocker: needs-physical-access.

## Escalation

- c. 50r: third pass on masked strips, as above.
- Ariosto c. 1: this key was tried, and failed. The 1576 key was not a fair test, as the shapes differ. No sibling text was found on the leaf.

## Image sources (links only; no scans in git; licence CC BY-NC-SA)

Lodovico IIIF manifests, `https://edl-jarvis.cultura.gov.it/meta/iiif/<uuid>/manifest`:

- `165f6b9d-ea12-48f5-8694-4f9b82bda5b8` Ercole II, cc. 50-51
- `f3fe3e9c-fffd-4baf-87d9-d5e2d4160635` Ariosto, c. 1

## Files

`transcription_cc50r_1559-05-28.txt`, `decryption_cc50r_1559-05-28.txt`, `reading_cc50-51_1559-05-28.md` (Italian with English, sentence by sentence), `key_1559.tsv`, `gloss_c50r_firstread.txt`, `sign_changes_c50r.tsv`; `transcription_c1_1559-07-15_FIRSTLOOK.txt`; `VERIFY.md`, the independent report, unchanged; `scripts/`.

`python scripts/check_decryption.py` reruns the key over the transcription. `python scripts/check_marks.py 50` counts the words and enforces the marks. Both need only the standard library. The other scripts need the images and are there as a record of the method; they use a `scans/` and a `work/` folder that are not in the repository.
