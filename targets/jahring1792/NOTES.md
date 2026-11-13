# jahring1792: Hofrat Jähring to Prince Georg Karl of Hesse-Darmstadt, 1792 (catalogue 2030)

Contributed by WAINUT (lccompany). Work of 12 Nov 2026 by AI language-model agents, from the archive's images.

## Documents

HStAD (Hessisches Staatsarchiv Darmstadt), D 4 Nr. 487/4, "Chiffrierte Briefe", letters of Hofrat Jähring to Georg Karl
of Hesse-Darmstadt (1754-1830). The catalogue entry calls him Landgrave; he was a prince of the house of
Hesse-Darmstadt, not the reigning landgrave, and the clear text addresses him as "Ew. Hochfürstliche Durchlaucht".
226 images. Images used:

- **119** (both pages) and **120, left page**: a numbered business letter (items 4-11 seen), signed by Jähring and dated
  "Darmstadt 1 Juny 1792" on 120 left. Twelve short cipher runs on 119 (one at item 9 of the left page, eleven on the
  right page). Files `*_119.*`.
- **120, right page**, and **121, left page and the top of the right page**: a report headed "Unterthänigster Bericht"
  (marked "B R 12/5"), signed by Jähring on 121 right. Undated as far as read. Four cipher runs in the upper half of 120
  (files `*_120.*`), one long run at the foot of 120 (run 120.5) and a block of about 10 cipher lines on 121 (files
  `*_121.*`).
- 121, right page, lower half: a short note in French ("Voici des dépêches arrivées dans ce moment de B. de G. ...")
  in another hand. No cipher; not worked.

Image route (direct JPEG, no viewer, fetched one at a time with User-Agent WAINUT-research):
`https://digitalisate-he.arcinsys.de/hstad/d_4/487--4/hstad_d_4_nr_487--4_<NNN>.jpg` (NNN = 119, 120, 121, 122).
Unit page: https://arcinsys.hessen.de/arcinsys/showArchivalDescriptionDetails.action?archivalDescriptionId=4590816.
Scans are not in this folder.

## System

Porta table with a running keyword. The key letter picks one of 13 reciprocal alphabets (key pairs ab, cd, ..., yz).
The keyword is **constantinopolitanus**. It starts again at its first letter with each cipher run and runs on across line
breaks inside a run. The cipher is written in Latin lower-case letters inside clear German written in Kurrent; word
division is not kept. Two sign shapes needed values (key.tsv): the looped, upright d-shape is f, and the heavy dot that
opens two runs on 119 is a blotted o.

## Key source

The keyword is contemporary: a second hand wrote "constantinopolitanus" over every cipher letter of the long run at the
foot of image 120 and of the cipher block on image 121, with a stroke from each key letter to its cipher letter, and
wrote "chandeltsnt" under the run on 120. No plain-text decipherment is written anywhere on these pages.

The table is ours. Before any run was read, the triage note recorded that Vigenère, Beaufort and variant tables with this
keyword had failed. We tried Porta, Vigenère, Beaufort and variant on the first 22 letters of run 120.5 (line 1, as
transcribed in a first rough pass) at all 20 key offsets. Porta at offset 0 gave "ernicht..."; nothing else read. The key
(Porta + keyword, restart per run) was then frozen (key_frozen.tsv) and applied to the other runs. They are all held
out: none was used to choose the table.

## Held-out test

Every run in runs.json (12 on 119, 4 on 120) is held out. Per letter position we compare the mechanical decryption with
the final reading; holes are left out and every position under a marked change counts as wrong (scripts/heldout.py,
output in heldout_result.txt):

| key | table | letters right |
|---|---|---|
| frozen key as frozen (looped d-shape read as d, dot dropped) | Porta | 303/346 = 0.876 |
| frozen key as frozen | Vigenère (control) | 1/346 = 0.003 |
| frozen key as frozen | Beaufort (control) | 4/346 = 0.012 |
| working key (looped d-shape = f, dot = o) | Porta | 330/348 = 0.948 |
| working key | Vigenère (control) | 0/348 = 0.000 |
| working key | Beaufort (control) | 3/348 = 0.009 |

These figures are after the five letter corrections of the blind review (see Review below). Before them the Porta
figures were 298/346 = 0.861 (frozen key as frozen) and 325/348 = 0.934 (working key); the controls did not change.
The reading against which the letters are scored was made by us, so the 0.948 is not independent of the reading. The
controls show what the same reading gives with the wrong table. The two sign values were set after the freeze, from the
held-out runs themselves: f for the looped d-shape fits at five places (gezogen, Miscredit, tausend twice, Casse), and o
for the dot at both runs it opens.

## Reading

Each run was decrypted mechanically (scripts/decrypt.py) and read with every departure marked ({x/y} changed letter,
{+a} added letter, [...] hole). scripts/check_marks.py rebuilds the decryption from the marked reading and fails on any
unmarked departure; it passes.

| text | runs | words | verbatim | marked change | hole | state |
|---|---|---|---|---|---|---|
| 119, letter of 1 June 1792 | 12 | 28 | 17 | 8 | 3 | not prose |
| 120 right, upper runs of the report | 4 | 37 | 29 | 7 | 1 | read in part |
| 120.5 and 121, rest of the report | 4 fragments | about 15 | | | | decoded, not read |

Most marked changes are one letter, and most of them are in the same few letter pairs: q, g and y (which differ only
in the tail in this hand), and y read where n is wanted. They are probably our transcription errors rather than the
writer's, but they are marked and counted as changes. The blind reviewer read g or y from the image at five of these
places (119.5, 119.13, 120.1, 120.2, 120.3); the transcription now follows the image there, and those five marked
changes fall away (counts above are after the correction; before it: 119 had 15 verbatim and 10 marked, 120 had 26
verbatim and 10 marked). The reading is the same.

What the runs say (with the clear text around them): the fair (probably the Frankfurt fair; the runs say only "Messe") ended "gloriously", instead of getting stuck as
Jähring had feared; "he" made a cash fund of 7,000 guilders for them at the fair; the prince is asked to say gracious
things to him when he sees him. The letter of 1 June complains of the building, the cash box, constant withdrawals of
credit and people trying to harm "our credit", which "we keep all the same"; the correspondents "are well disposed";
Jacobi and Kuppel are named.

Dan's reading checker (docs/_check_reading.py --file, run from a worktree of origin/main):

| file | clean share | sentences | note |
|---|---|---|---|
| reading_119.md (whole file) | 0.541 | 37 | the English header and notes count as sentences |
| reading_119.md, German sentences only | 0.70 | 10 | clear frame plus cipher runs |
| reading_120.md (whole file) | 0.500 | 28 | as above |
| reading_120.md, German sentences only | 0.857 | 7 | clear frame plus cipher runs |
| reading_121.md (whole file) | 0.286 | 21 | fragments |

The German sentences contain our working transcription of the clear text, which was not read word by word; the score
measures that frame as much as the cipher.

Run 120.5 and the block of 121 (decoded, not read): in the four transcribed line fragments, the words of the fragment
reading (reading_121.md, changed letters included) cover 7 of 35 letters (120.5 line 1, "er nicht"), 20 of 25 (120.5
line 4), 12 of 17 (121 line 1) and 13 of 21 (121 line 2), 52 of 98 in all. The rest of these lines is not
transcribed.

## Review

One independent AI language-model agent reviewed the folder blind on 13 Nov 2026 (it did not make the result). It
copied about 230 cipher letters from its own crops before opening our transcription (120.1, 120.2, 120.3 and 120.4,
119.5, 119.6, 119.13 and the first 14 letters of 121 line 1) and found about 93% letter agreement. Every difference was
in the q/g/y, r/v, s/d and k/x shapes, and none created or removed a word. At five letters its reading gives the wanted
letter where ours needed a marked change; these were taken over (transcription_119.txt and transcription_120.txt state
them in their headers). At the other differences the decryption favours our transcription; one letter is undecided
(see Remaining gaps). The reviewer reproduced check_marks.py (16 of 16 runs pass), the decryption of 120.1-120.3 with
its own Porta code, and the held-out figures, and confirmed that run 120.5, which chose the table, is not among the 16
scored runs. It agreed the three states (not prose; read in part; decoded, not read), grade B for each. It read the
four sentences of image 120 against the translation: 4 of 4 hold, with one hole in the second.

## Remaining gaps

One line per open piece, with its blocker type.

- Run 120.5 and the block of 121, the core of the report - blocker: not-attempted; run 120.5 (about 4 lines) and the
  block on 121 (about 10 lines) are overwritten by the second hand's key letters and strokes. Only four line fragments
  were transcribed, in one pass. The key works on all four, and the second hand's key letters give the key offset of
  each line, so these lines can be read with a careful transcription. Figures of 12,000, 10,000 and 1,000 stand among
  them.
- Holes in 119L.2 (6 letters), the middle of 119.7 (6), the end of 119.13 (3) and 120.2 (9) - blocker: not-attempted;
  the decryption does not read there, and these letters have not been re-checked on the image.
- 120.1, line 2, fourth letter - blocker: needs-physical-access; s (ours) or the looped d-shape (the reviewer's first
  reading) is undecided on this image; the original or a sharper image would settle it. s gives the a of "anstatt"; the looped d-shape would give x. Kept as s.
- Second reading of 9 of the 16 runs - blocker: not-attempted; the two transcription passes were made by the same
  agent. The blind reviewer checked about 230 letters in 7 of the 16 runs and the first 14 letters of 121 line 1 (see
  Review); 119L.1, 119L.2, 119.1, 119.2, 119.3, 119.7, 119.8, 119.10 and 119.12 were checked by no second reader.
- The clear text around the runs - blocker: not-attempted; it is a working transcription only, weak in places on 119
  ("geben mir immer fürchterlich gut"; "liege ich Kuppels Speyer und stellen unsern Correspondenten"), as the reviewer
  also noted.
- Images 1-118 and 122-226 of 487/4, and 487/6 - blocker: not-attempted; not paged through for further cipher. The
  vetting saw short runs elsewhere only on contact sheets. 487/6 (the second link in the catalogue entry) was not
  opened.
- The date of the report (120 right - 121) - blocker: not-attempted; "B R 12/5" may be a filing mark or a date.

img120_bericht_upper and img120_121_bericht_block are one report, split here by state. They could be one document
marked "read in part" with the 121 block as a remaining gap.

## Escalation

- [x] siblings: images 119-122 opened; the keyword on 120-121 is what gave the key; image 122 has no cipher seen at full
  size; the other images of 487/4 and 487/6 not opened
- [x] clear-pages: the French note on 121 right checked; it is not a decipherment. No plain-text decipherment on 119-121
- [ ] known-keys: no other Hesse-Darmstadt key of the 1790s tried (none was needed: the keyword is on the leaves)
- [ ] print: two web searches and the vetting of 3 Nov 2026 (DECODE, Tomokiyo, Lasry); no printed edition searched
- [ ] key-rebuild: not needed for the letters (Porta table and keyword complete); the ð and dot values rest on 5 and 2 places
- [ ] retry: the holes in 119L.2, 119.7, 119.13 and 120.2 not retried on the image

## Prior art

Checked 12 Nov 2026: two web searches (Jähring, Georg Karl, Hessen-Darmstadt, chiffrierte Briefe; Jähring, Darmstadt,
1792, Messe, Chiffre) found only archive finding-aid entries for the Jähring letter series (Arcinsys, Archivportal-D,
DDB) and no edition or decipherment. The vetting of 3 Nov 2026 (catalogue entry) found nothing in DECODE, Tomokiyo or
Lasry. The only decipherment work on the leaves is the contemporary second hand's keyword alignment.

## Collision check

12 Nov 2026: no folder under targets/ and no PR or issue on dbourdeau/cyphersolver covers HStAD D 4 487/4, Jähring,
"constantinopolitanus" or catalogue 2030 (searched open and closed PRs and issues; origin/main and the live main
7dcbe3f). Issue #207 (closed) concerns other Hesse-Darmstadt keys of 1652/1658. Re-checked 13 Nov 2026 on main
65cdcd9d5, after the PRs merged on 12 Nov: still no target folder, open PR or issue on these names, the shelfmark or
catalogue 2030; targets hesse1603, hesse1672 and hesse1824 are other documents.
