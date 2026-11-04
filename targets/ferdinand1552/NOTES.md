# 1332: Ferdinand I to Castaldo, Oct 1552 (Ambrosiana G 275 inf.)

Status: in progress. Not yet written up: no site page or README row. Read in part, or not read, with escalation steps still open (see its status below, Remaining gaps and Escalation). The status below is the contributor's.

Status: read in part (3 Nov 2026), for the entry as a whole. The one letter with no contemporary decipherment is read; the other three
are transcription jobs, not done.

| Document | Cipher | Job | Words | Reads as sense | No restored or changed letter | Firm, every doubtful sign out | Status |
|---|---|---|---|---|---|---|---|
| 15 Oct 1552, ff. 34r-36r | 34r foot, 34v, 35r, 35v top: 82 lines, 1904 signs, 130 of them nulls | no decipherment in the file | 317 | 316 (99.7%) | 311 (98.1%) | 306 (96.5%) | **read** |
| 13 Oct 1552, ff. 9r-15v | long | transcription job, margin gloss | | | | | not transcribed; table fits |
| 18 Oct 1552, ff. 37r-42v | long | transcription job, margin gloss | | | | | not transcribed; table fits |
| 22 Oct 1552, ff. 43r-48v | long | transcription job, margin and foot gloss | | | | | not transcribed; table fits |

"Read" means the cipher of that letter at the 95% rule. The one word not read is code sign Q7. If the numeral at 34v.06 is also held
open, 315 of 317 (99.4%) read as sense. The clear text of the letter is also given, as a first transcription. Transcription and
reading were done by AI language-model agents viewing the images. No human palaeographer has checked them.

Signs: 1904 are listed, 1903 without the faint mark at 35r.24. Of these 130 are nulls, and the rest give 1803 letters and 8 code
places. The independent check quotes 1835 and 1834 letters. Those are lengths of the decryption string, which counts each code place
as four characters.

## Earlier work you should know about

Your own ledger has this. `research/dudout_2026-10-29/CORRECTIONS-FOR-DANIEL-2026-10-29.txt` says Brice Dudout read the 15 Oct letter
with a key rebuilt from the sister glosses, and names `targets/castaldo1552`, PR prepared locally. `research/dudout_2026-10-29/README.md`
says his email withdrew that (validation 0.731 of words) and that the item is held until he confirms. No such target or branch is at
origin/main 3c777efd5. We have not seen his files, and our work is independent of them. We did read those two public notes. They name
Q8 = Lippa at f. 45v; our value for Q8 comes from f. 39v, where the gloss has `illum Lippen.` against the sign. The target is called
`ferdinand1552` so that his name stays free. He has not been contacted by us. How to handle the overlap is for you to decide.

His note that the other three letters are glossed holds on what we viewed. One point looks like an exception and is not: f. 46r has
14 cipher lines with an empty margin, but the gloss runs at the foot of f. 45v and covers them.

## The system

A letter table with 2-3 homophones per common letter, doubled letters as numbers, nulls and a few code signs. About 55 signs in all.
It is not syllabic: on f. 9r the gloss has 122 letters and the cipher about 130 signs.

- Letters: `key.tsv`. No word division.
- Doubled letters, as numbers: 3 cc (a plain 3, while the ticked 3 is i), 5 ff, 6 gg, 7 ll, 8 mm, 9 pp, 10 rr, 11 ss, 14 nn.
- Nulls: Ex, Eo, epsilon, n:, m:, d:, q:, the double-barred 6, +Th, and the clear words Sicut, Insuper, Postq.
  They fall inside words: `V U Ex Ls` = tur, `A 5 Z# P z < ou V n:` = efficient. 130 of 1904 signs here.
- Codes, rho with a numeral and H with a 9: Q3 Hamet, Q4 Bassa Budensis, Q6 Transiluania, Q8 Lippa, H9 exercitus, Q7 unknown.
- The writer corrects by adding a sign above the line, with a pair of small strokes above and below the place.

Repo keys: `malvezzi1548` and `huyson1547` (the same alphabet) do not apply. The method is the same family: numbers for doubled letters
with 3 cc, 5 ff, 6 gg, 7 ll, 8 mm shared, and Latin words as nulls. But the numbers differ (ss 11 here, 13 there; rr 10, 14; nn 14, 16),
and shapes present in both have other values: the Venus sign is c here and t there, inverted T a here and p there, lambda e here and h
there, cross f here and c there, 7 ll here and i there. This was compared against `KEY_BRIEF.md` by hand. R367 images need a login
and were not used.

## How the key was obtained

1. Every cipher line of ff. 9r, 9v, 10r, 34r, 34v, 35r, 35v was cut into connected shapes by script. The shapes were clustered with no
   language and named by eye from contact sheets. A nearest-neighbour classifier then labelled every shape: `pass_A_machine.txt`.
2. Those labels for 9r-9v were aligned with the gloss of 9r-9v, typed earlier in this folder before any key existed, by
   expectation-maximisation from random tables.
3. Frozen as `key_frozen.tsv` on 3 Nov 2026, before ff. 34-35 were read line by line and before 10r was decrypted.

**Correction to an earlier version of this note.** It said the table came "with no value supplied by us". That was wrong for the run on
disk. `scripts/em.py` as used fixes 14 sign values in every restart (the dict `known`: 3 i, oo s, V t, Ls r, A e, < e, U u, ou n, u a,
Th o, P c, Hs r, D m, I: m). The 197 failed restarts quoted before cannot be reproduced from it. Seven frozen nulls (Ex, Eo, n:, m:, d:,
e, ii) were also set by hand; EM gave them letters.

The seeds do not change the result. `python scripts/em.py 3 150 noseed` starts every restart from a fully random table. It stayed under
170 for 20 restarts, locked at restart 21 (score 1249), and reached 1259 at restart 32. All 36 frozen letter values came out the same.
The independent check found the same with its own rerun (restart 6, score 1254).

Nothing is committed, so the freeze rests on the order of work and file times, not on a hash.

## Held-out tests

A. f. 10r against its gloss. Neither was used for the table. Frozen table, raw machine labels with no correction, gloss as typed by the
earlier solver before any key existed (518 letters). Local alignment score 754 of a possible 1036; 100 shuffled tables: mean 13.8,
best 23. Gloss letters found in order: 442 of 518 = 85.3%; shuffled mean 36.7%, best 41.5%.

The signs also corrected the typed gloss in places, for example `inuenien...darum pecuniarum` and `rerum nostrarum`.

B. The letter itself, key-free. Pass A on ff. 34r-35v, passed through `key.tsv`, against the final decryption: 1664 of 1835 characters
= 90.7% in order; 200 shuffled tables: mean 32.2%, best 39.0%. Rerun with the final key and transcription:
`scripts/step_machine_check.py`. The classifier was trained on shapes that include these pages, and the comparison is with our own final
text, so this shows the shapes, not a fully unseen page. No language was used in labelling.

C. Code values. f. 46r l. 11 reads `quidem [Q3] cum [H9] ad Agriam`. The foot of f. 45v has "quandoquidem Hamet cum exercitu ad Agriam
moratur". f. 39v has `a reliquo [H9] opem`, gloss "a reliquo exercitu opem". The values of Q3 and H9 are therefore contemporary, not ours.

## Independent check

`VERIFY.md` is the report, unchanged. Its figures for signs and words predate the fixes below. The checker is an AI language-model reader,
like the solver, and read the signs before opening any solver file; the hashes of its blind files are in the report.

- f. 34r, all 16 lines, 350 signs against the eye transcription: 6 differences (1.7%), all one hash shape it had merged; 0 of 350 after
  zoom. This covers only the first 18% of the letter.
- The phantom sign at 35r.11 lay outside that sample and was found on a separate, non-blind look at the line ends. So the blind rate does
  not bound the rest of the letter.
- Its own blind pages through `key.tsv` against its own typed gloss: 10r 93.2%, 39v 95.1%, 45v 95.9%; best of 200 shuffled tables 45.2%,
  43.1%, 42.9%.
- A table fitted by it from random starts to its own readings of those three pages, with no value supplied, gave 303 of the 334 letters
  of its blind 34r in order.
- Trigram model built from its own typed glosses: `key.tsv` -2.567 per trigram; 500 shuffled tables best -3.512.

Fixes made after it, all logged in `corrections_log.tsv`:

- 35r.11: the last sign does not exist. Bare paper after `Ls`, confirmed at 4x. The repair `nostr{a/e}{-a}` went with it: the text is
  `cura nostra si`.
- 35r.24: a faint sign at the line end, in the stain. Its structure matches `z` at seven clear places. Added as doubtful, so `industria`
  has its i on the page and is no longer a repair.
- 35r.27: V is clear; no separate A can be made out. `milit{+?e}s`: the e is sense, and the word leaves the count with no restored letter.
- 34v.06: the numeral is marked doubtful. **One disagreement:** the check calls it nearer S or 5. Against the writer's four 5s on these
  pages it is not a 5, as it has a closed lower bowl and no flat top bar, so we keep 8 and mark it doubtful.
- The blot in `quamuis`, sign 24 in `nihil` and the overwritten u of `uident` are now marked in the reading too, so the mark check covers
  every doubtful sign.

## Changes after the freeze

These were made on ff. 34-35 and are in `key.tsv`, with reasons. Test A ran with the frozen table unchanged.

- Hh frozen as o, changed to l: 21 of 21 places on ff. 34-35. The frozen value came from one aligned place on f. 9v.
- ii frozen as null, changed to ss.
- 7 frozen as l, changed to ll.
- Added: `*` o, wave p, the numbers, q:, Eb, +Th and the clear-word nulls.

Doubtful: 24 (one use, value from context alone), 14 (one use on these pages, pannorum; also "pannorum" in the 10r gloss), 10, 6 and 8 (one
use each).

## Transcription

Two passes. Pass A is the machine, with no key and no language. Pass B is the final file: every line read by eye on strips at 1.6x, with
the machine labels printed under the signs. Disputed shapes were viewed at 4x. Pass B was not blind. The reader knew the table, and
the text was often recognisable while reading, so sense may have steered choices between look-alikes. The eye corrected the machine
in 170 stretches (`pass_diff_15oct.txt`), many of them split or merged shapes and clear words beside the cipher. Agreement in order
is 89.8% of signs. At 35r.11 pass B followed the machine into a phantom sign, so "read by eye" did not hold at that spot.

The hash signs H2, Hh and H3 were settled on a gallery of crops on shape alone. C against d is the weakest pair: one place, 34v l. 9,
was first typed C and corrected to d on a zoom after "presibio" appeared in the decryption, so that one was found by sense first.

Files: `transcription_15oct_ff34r-35v.txt` (signs), `decryption_15oct_ff34r-35v.txt` (letter for letter, nulls dropped, doubtful signs in
round brackets), `reading_15oct_ff34r-36r.md` (Latin and English, with holes and every repair marked), `translation_15oct_ff34r-36r.md`
(the English alone). `python scripts/check_marks.py` rebuilds the decryption from the signs and the key, walks the reading against it
letter by letter, fails on any unmarked departure or unmarked doubtful sign, and prints the counts.

## Reading, in brief

Ferdinand tells Castaldo he would have liked a demonstration towards Lippa, to draw the Ottoman army off the siege of Eger and to
support what Maurice of Saxony is doing on this side with his army. He thinks the Turks at [?Temesvar] and Lippa would have been
alarmed and might have had to call on Hamet. He concedes that Castaldo's difficulties prevented it. Money has been sent to the soldiers
and now more, with a large quantity of cloth, so they should drop any thought of leaving; they cannot leave safely in any case, and
their going would do great harm. Castaldo is to keep soldiers and subjects to their duty. The enemy cannot stay in the field
with winter coming, should achieve nothing at Eger, and will be drawn off by the army's advance or driven off by winter.

## Context

Dated 15 Oct 1552, three days before the Ottomans gave up Eger (siege September to 18 Oct 1552, defended by Dobó). Ferdinand plainly did not
know that. Hamet is Ahmed Pasha, who took Temesvár that summer (Wikipedia, Hungarian Defence article; general reference, not checked
further). The diversion fits V. Kanász's 2023 article in *Arrabona*, seen only as an abstract: Maurice camped below Győr and
ran diversions in Transdanubia instead of marching to Eger. The gloss of f. 11r has him `ad Iaurinum nunc castrametatus`. The clear
close concerns the Aldana inquiry and the death of Friar George (Martinuzzi).

## Q7: search of the glosses, 3 Nov 2026

Q7 occurs once in this letter, 34r l. 17, paired with Lippa: `Turce illi ad [Q7] et [Q8] relicti`. Its value is **not found in the glosses
viewed**.

- Read by eye at full image size: the left margins of ff. 9r-14v, 37v-42r and 43v-46v (29 pages), and the top and foot bands of the
  same pages. No form of Temesvár occurs in them. The places named are Deva, Cassovia, Iaurinum, Agria, Transiluania, Lippa, Vesprimium
  and Alba Regalis. The reading was for this one word, not a transcription of the glosses. Gloss in a hand this small can be missed.
- Rho signs were sought on the cipher pages by a shape filter and a contact sheet, looser than the earlier template search. It found 11 on
  the sister pages, with numerals 1, 3, 4, 6 and 8, and no 7: 9r (6), 39v (8, three times), 41r (6), 41v (a sign like 1 or i, twice),
  43r (6), 44r (4), 46r (3), 46v (6). The filter also misses signs, so this does not prove there is no rho 7.
- In passing: the rho with the stroke on f. 41v stands in a passage whose margin has `princeps Turcarum`. It looks like another code sign,
  Q1. Not aligned and not used here.
- Veress prints a Moldavian envoy's paper of about 30 Oct 1552 naming `Themeswarum, Lyppa, Becheque et Bechkereke` together as the
  places to recover (see below). That supports the pairing as context. It does not give the value of the sign.

`[?Themeswar]` therefore stays a proposal from context.

## Prior art (3 Nov 2026): open

We do not claim the Latin is new to print.

- Collision: no target and no commit at origin/main 3c777efd5. See "Earlier work" above.
- Veress, *Documente privitoare la istoria Ardealului, Moldovei și Țării-Românești* I (1929), opened as the scan at
  https://mek.oszk.hu/26600/26634/pdf/26634_01.pdf, by its text layer and the pages for autumn 1552. **The letter of 15 Oct is not in it:**
  No. 134 is of 28 Sept 1552 and No. 135 of 18 Oct.
- **Veress does print parts of the sister letters.** No. 135 (18 Oct, pp. 105-106) and No. 137 (22 Oct, p. 107) are excerpts from
  Ferdinand to Castaldo, cited `Bibl. Ambrosiana. Milano. Codice ff. 6`. No. 135 agrees with the gloss of f. 39r as far as we compared it
  (`tolendum e medio Valachum`, `ambas provincias illas amicas habere`), so a passage of the glossed cipher has been in print since
  1929. His index gives Ambrosiana for Nos. 43, 50, 135, 137 and 144; we did not read 43, 50 or 144. His shelfmark is not G 275 inf., and we
  did not trace it. He prints excerpts that bear on the Romanian lands, so this says nothing about other editions of the 15 Oct letter.
- Hurmuzaki was not opened. A clear minute may survive at Vienna (HHStA, Hungarica), not checked. The 1972 Eger museum yearbook listing of
  Ferdinand's 1552 letters (https://library.hungaricana.hu/en/view/MEGY_HEVE_agria08_09/?pg=212) has items of 17 Oct but, per a search
  extract, none to Castaldo of 15 Oct.
- Two web searches by the solver and two by the checker found no edition of this letter.
- Carpentieri, *Verbum* 13/2 (2012), p. 471, full text searched by keyword, not read through: the cipher of ff. 9r-15v, 37r-42v and 43r-48v
  was deciphered in the margins. She does not list the other, and says the existence of editions of these documents remains to be
  established. Domokos 2025: on the codex; nothing found on the 15 Oct cipher.

## Remaining gaps

- Q7, 34r l. 17 - blocker: not-attempted; value not found in the glosses viewed and `[?Themeswar]` is context only; transcribing the sister letters would show any rho 7 and its gloss.
- The numeral at 34v.06 - blocker: illegible; 8 is kept and marked doubtful, and Q5 cannot be excluded on the image.
- Doubtful signs at 35r.24, 35r.27, 34v.05 and 35r.18 - blocker: illegible; faint, at the binding edge, blotted or overwritten; a better image or the original would settle them.
- Sign 24 at 34v.22 - blocker: too-short; one use, value from context alone.
- Blind reading of ff. 34v-35v - blocker: not-attempted; a blind reader has covered only f. 34r of this letter.
- Letters of 13, 18 and 22 Oct 1552 - blocker: not-attempted; transcription jobs with this table, not done. The images are good and the gloss covers the pages viewed. 6 scrawled lines on f. 14v under the date were not examined, the last line of f. 46r was not traced to a gloss, and gloss coverage of every cipher block was not checked.
- Clear text of the letter - blocker: not-attempted; a first transcription only.
- Prior art - blocker: not-attempted; other editions, Hurmuzaki and the Vienna minute were not checked.

## Escalation

- [x] siblings: all four letters of the entry opened and the table tried on samples of each; the ledger's note that ff. 17r-25v are in clear was not rechecked
- [x] clear-pages: glosses and page feet of the sister letters read for Q7; f. 34r-36r has no decipherment of its own
- [x] known-keys: malvezzi1548 and huyson1547 compared by hand against `KEY_BRIEF.md`; they do not apply. R367 images need a login and were not used
- [x] print: Veress I opened, the letter is not there; the rest is open (see Prior art)
- [n/a] key-rebuild: every sign has a value except Q7, which occurs once here and has nothing to build on but the pairing with Lippa
- [x] retry: every doubtful sign rechecked on crops at 4x to 12x on 3 Nov 2026; each stays doubtful, and Q7 was searched as above

## Image sources

Ambrosiana IIIF, loaded by script, one request at a time, 1 s apart, User-Agent `WAINUT-research`, no block seen. `scripts/fetch.sh`:
`https://digitallibrary.unicatt.it/iiif/3/veneranda&SEPdata&SEPpublic&SEPcontents&SEP0b&SEP02&SEPda&SEP82&SEP80&SEP27&SEPc8&SEPd4&SEP<NNNN>_G275inf._c.<folio><r|v>.jp2/full/max/0/default.jpg`
with NNNN = 2*(folio-10)+21 for a recto, +1 for a verso. Native size about 1434x2000. No images in git.

`marginal_gloss_9r_9v.txt` is the gloss as typed by the earlier solver, read by eye, not checked against a second reading.

## Files

- `transcription_15oct_ff34r-35v.txt`, `decryption_15oct_ff34r-35v.txt`, `reading_15oct_ff34r-36r.md`, `translation_15oct_ff34r-36r.md`.
- `key.tsv` (final, with reasons), `key_frozen.tsv` (as frozen), `sign_inventory.md` (the shape names).
- `VERIFY.md` (independent check, unchanged), `corrections_log.tsv` (what was done with each of its corrections).
- `pass_A_machine.txt` (machine labels), `pass_diff_15oct.txt` (machine against eye), `marginal_gloss_9r_9v.txt`.
- `scripts/check_marks.py` and `scripts/decode.py` need only the files here. `scripts/step_heldout_10r.py` and
  `scripts/step_machine_check.py` run from this folder and need numpy. `scripts/em.py` needs numpy. `fetch.sh`, `seg2.py`, `cluster.py`,
  `classify.py`, `strips.py` and `crop.py` need the images and are a record of the method.
