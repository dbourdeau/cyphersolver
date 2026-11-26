# Catalogue 2346: Marcello Griffoli to Cosimo I, Siena, cipher in figures (ASF Mediceo del Principato 443, 451)

WAINUT, 6 Nov 2026. Work done with AI language-model agents; every digit was read from the ASF images at full
available resolution (2000 px, the IIIF maximum) and checked by script as described below. No human palaeographer has
checked the text. An independent AI language-model agent checked the work (`VERIFY.md`); the fixes made after that
check are listed at the end of this file.

Status: in progress (not yet written up). Next step (24 Nov 2026 review): transcribe 451 c. 25v (about 19 lines, ASF PAD online), write Dudout's six readings into c. 315, parse the decoded runs, then recount. Read in part, 6 Nov 2026: 443 c. 315 and 451 c. 25r are read in part; the
2 Feb letter (443 cc. 316v, 318r) is a transcription job covered by its contemporary decipherment and served as key
source and held-out test; 451 c. 25v is not transcribed. No site page or README row; escalation steps remain open
(see Remaining gaps and Escalation).

## Result in one paragraph

The cipher is a two-digit homophonic substitution with 0 as a null/separator and a small set of code units
(et, che, non, si, per, come, quanto, V. Ecc., Montalcino). The key was rebuilt from the 2 Feb letter
(443 cc. 316v-318r, cipher) against its contemporary decipherment (c. 317r), frozen, and tested on held-out cipher
(318r): 22 of 24 words agree with c. 317 (graded by hand, spelling apart), and 89 of 98 letters (90.8%) by script
against a shuffled-key baseline of 49.9% (max 69.4% in 1,000 shuffles). The test is small and has limits (below).
The same key reads both bare pieces in part:
**443 c. 315r-v (1 Feb): read in part. 159 of 187 words (85.0%) verbatim from the signs; 2 with a marked repair,
11 context fills of holes (counted as guesses), 1 with a hole inside, 14 decoded but not parsed; 10 holes.**
**451 c. 25r (3 Jan): read in part. 92 of 129 words (71.3%) verbatim; 1 marked repair, 5 context fills, 1 with a
hole, 30 decoded but not parsed (r04-r05 and r17-r21); 7 holes. 451 c. 25v (about 19 lines) is not transcribed.**
451 is in the same key as 443; no change of system. Neither bare piece reaches the 95% needed for "read".

## Documents

| doc | shelfmark | date as written | cipher | status |
|---|---|---|---|---|
| k316 | ASF MdP 443 c. 316v (two blocks, 7 + 13 lines) and c. 318r (4 lines); decipherment c. 317r | Siena, 2 Feb 1555 | key source | transcription job (glossed by c. 317) |
| c315 | ASF MdP 443 c. 315r (20 lines) + c. 315v (5 lines) | Siena, 1 Feb 1555 | bare | read in part (85.0% verbatim) |
| c25 | ASF MdP 451 c. 25r (23 lines); c. 25v about 19 lines more | Siena, 3 Jan 1555 | bare | 25r read in part (71.3% verbatim); 25v not done |

Dates: the letters are dated in the Florentine year. A Medici commissioner writing "di Siena" in January-February
fits 1556 (Siena surrendered in April 1555; Montalcino held out as the republic in exile until 1559), so 1 and 2 Feb
1555 are very likely 1 and 2 Feb 1556 modern; the content (plots against Montalcino, a "trattato" in Siena) fits that.
Not checked against other sources.

Images (ASF PAD, public, no login):
443 c. 315r https://archiviodistatofirenze.cultura.gov.it/archividigitali/riproduzione/?id=601904&ua=443 ,
c. 315v ...?id=601905&ua=443 , c. 316r 601906, c. 316v 601907, c. 317r 601908, c. 317v 601909, c. 318r 601910;
451 c. 25r https://archiviodistatofirenze.cultura.gov.it/archividigitali/riproduzione/?id=614508&ua=1010 ,
c. 25v 614509, c. 26r 614510. IIIF files: `mdp_carteggio_universale/443/0636_C_315_R.ptif` ... `0642_C_318_R.ptif`,
`mdp_carteggio_universale/451/0056_C_025_R.ptif`, `0057_C_025_V.ptif`. Scans are not in git.

## System

- Units are two digits, each from 1-9. The digit 0 is a null/separator written between most units (sometimes two
  units run together, sometimes several 0s in a row). Evidence: splitting every line on 0 gives stretches of even
  length throughout (27 odd stretches against 1,590 units in the three transcriptions, at misreads, stray digits,
  blots or the joined "2_2" form).
- Letters have homophones (a 22/23/28, e 43/44/49, i 45/46, o 72/73, m 33/93, t 76, ...). Codes in the 1x row
  (11 et, 12 che, 13 per, 14 come, 15 in, 18 quanto), 24 non, 25 si, 85 V. Ecc., 91/92 Montalcino.
- No doubling sign was found; double letters are mostly written single (tuto, comisione, Pogio).
- `key.tsv`: 35 frozen rows + 3 rows from later context (15 in, 28 a, 46 i), each holding at every occurrence.
  Values used only in the readings and marked there as context fills: 78 s/r, 83 m, 84 p/v, 88 u, 36 t/u, 79 s
  (one to three places each; 84, 78 and 36 do not hold one value at every place, so they stay out of the key).
  Unknown: 29, 71, 86, 97 (probably code words or names).
- Thirteen values hold at every occurrence with no repair in all three documents, with dozens of places each
  (11, 12, 24, 25, 32, 39, 43, 45, 47, 52, 74, 75, 76; counts in `VERIFY.md` section 3).

## Key source and held-out test

- Pairs: 316v block a (7 lines) = c. 317r lines 1-3 ("Acapi il tutto ... di cosa alcuna"); 316v block b (13 lines)
  = c. 317r "Si è imposto ... Collonello ... sarà domandata da Montalcino come li ho". The key was built from these
  only and frozen in `key_frozen.tsv` (6 Nov 2026, 13:50).
- Held out: 318r block c (4 lines: 77 two-digit units and one odd group, 83223), which c. 317r covers in its last
  lines ("persuaso et ordinato ... servitio di V. Ecc."; `gloss_c317_heldout.txt`). Mechanical decryption with the
  frozen key:
  `persuaso et ordinato che solo uoglino [?83223] proteczione di V.Ecc. et io non poso fare di core si non quanto e
  seruizio di V.Ecc.` Against c. 317's 24 words: 22 agree (spelling apart), 1 differs (cipher "che", c. 317 a sign
  first read "et"), 1 unread (`[?83223]` where c. 317 has "la"; probably 32 23 with a stray 8). No unit in the
  held-out block was missing from the frozen key.
- Letter level, by script (`python scripts/heldout.py`): 89 of the gloss's 98 letters are matched in order by the
  frozen-key decryption (90.8%); 1,000 keys with the same values shuffled among the units score 49.9% on average,
  69.4% at most.
- **Limits of the test.** (1) It is small: 24 words, 77 units. (2) The held-out decipherment is on the same page as
  the training pairs (c. 317r, its last three lines). The solver viewed that page, and the cipher of block c, before
  the key was frozen: the pass-1 digits of block c (`work/b3_p1.txt`) were written at 13:34, before the freeze at
  13:50. The independent check found no file from before the freeze that aligns block c with c. 317
  (`work/b1_units.txt` covers block a only), but the separation rests on the order of work, not on blinding.
  (3) The word score was graded by hand. (4) The shuffled baseline was added after the independent check.
- **A possible correction of the score.** On c. 317r the word graded "et" before "solo" is a looped sign that is not
  the "et" spelled out two words before it. On c. 317r the sign occurs eight times: six times where the cipher has
  unit 12 (che: a05, b01, b02, b03, b05, c01), and in b10 after "per" (unit 13, keyed "per" from this pair) and at
  an odd digit group. Where the cipher has 11, c. 317 spells "et" every time. The sign may be an abbreviation of che
  (c. 317 also spells "che" twice, a02 and a03). If so, the held-out score is 23 of 24 words (91.9% of letters). This
  was noticed after the test and changes no key value; the headline stays 22 of 24.
- The cipher and c. 317 differ in several places in blocks a-b. Some look like clerk slips in the cipher, some like a
  free rendering in c. 317: a01 `acapiqtut[?722]` against "Acapi il tutto" and `connresteza` against "con destrezza";
  a06-a07 "non si mancherà né di [29] ... di altro" against "di cosa alcuna"; b01 "ci ha imposto" against "Si è
  imposto"; b02-b03 `subto come ti` against "subito commetti"; b10 `cse[?4744912]` against "crede"; b12 `pa quale`
  against "la quale". (A first list named only three places and said the cipher read cleanly in each; that was too
  strong.) None of these touches the held-out block.

## Reading (summary)

- **443 c. 315 (1 Feb).** Griffoli recalls his letter of the 2nd [January] asking that ladders and fire-trumpets
  be sent to Poggio Imperiale; no news from Montalcino; his note ("polizza") to "il medico" went well. A man called
  Milandrone has been promised pardon and a pension by the French and has accepted; he is to draw out the
  confidants the French have in Siena by pretending a plot ("trattato") in Siena, and to come with their witnesses to
  reconnoitre an unwatched stretch of wall, so that their people become known. Someone fled to Montalcino for fear
  of the plot; something was discovered in Siena; the ten men "who are there for us in Montalcino" are gathered.
  Full marked reading in `reading_c315.md`, English in `translation_c315.md`.
- **451 c. 25r (3 Jan).** Griffoli waited for the return of "il medico di Montalcino": three leading citizens of
  Montalcino with the following of the whole town are won over; they wait for a messer Lelio and an Alessandro,
  their kinsmen, to take charge of the arms; they were heads of the faction; the order will come with the
  capitulations. Lines r17-r21 are decoded but not parsed. `reading_c25.md`, `translation_c25.md`.
- Open stretches are marked «...» (decoded but not parsed) and `[nn]` / `[?ddd]` (unknown units, odd digit groups).

## Word counts (from `scripts/check_marks.py`)

A word is **verbatim** when every letter is the mechanical decryption with no mark. A **marked repair** changes a key
value (`{o/t}`) or drops a stray digit group (`{[?ddd]/}`). A **context fill** supplies letters for a hole
(`{[nn]/x}`, `{[?ddd]/x}`) that the signs do not give; it is counted with the guesses. A word **with a hole** has
letters from the signs around an unread unit.

| doc | words | verbatim | marked repair | context fill or guess | with a hole | decoded, not parsed | holes | from a gloss |
|---|---|---|---|---|---|---|---|---|
| c315 | 187 | 159 (85.0%) | 2 | 11 | 1 | 14 | 10 | 0 |
| c25 (25r only) | 129 | 92 (71.3%) | 1 | 5 | 1 | 30 | 7 | 0 |

Words are counted per line, so a word split by a line-end hyphen counts twice; "V. Ecc." counts once.

## Transcription

Two passes per document: pass 1 from half-line strips (1.2-1.5x), pass 2 from fresh third-line strips with a wider
crop (1.15-1.6x), both read without the key in view. Disagreements settled on the image:
k316 a04 (end of line in the gutter: pass 1 lost "3922"), 451 r09 (pass 1 crop cut the line start; pass 2 "3223").
451 r22-r23 had pass 1 only. Pass 2 was logged as its differences from pass 1: the `_pass1` files are the raw first
pass (identical to `work/*_p1.txt`); there is no separate raw file of pass 2.
Overwritten or blotted digits are kept as the top ink: 443 c. 315 r04 "73" (the reading needs t: marked `{o/t}`),
r16 "748 43" (8 probably a 0), 451 c. 25 r02, r06, r10, r13-r16 (blots).
Many of the odd stretches (`[?722]`, `[?222]`, `[?47222]`) contain the joined "2_2" form; its value is not settled.

Two places changed after the independent check, each settled on 5-9x crops of the full-size scan:

| place | was | now | why |
|---|---|---|---|
| 443 c. 315r r01, line end | `...394304` | `...39430` | the last mark is a 0 with a line-end flourish, not a 4 (the verifier's blind reading); the reading no longer needs to delete a stray `[?4]` |
| 451 c. 25r r02 | `...4932 2 0 74...` | `...4932 0 74...` | one overwritten sign, not two digits: a closed oval in lighter ink over the tail of a 2. Kept as the top ink, 0. 49 32 then reads "el" ("aspettava el ritorno"), and the context fill `{[?49322]/ il}` falls away. Not certain: 2 under 0 cannot be excluded |

## Files

`transcription_<doc>.txt` (+ `_pass1`), `decryption_<doc>.txt` (mechanical, `scripts/decrypt.py`),
`reading_c315.md`, `reading_c25.md` (marked reading and running Italian text), `translation_c315.md`,
`translation_c25.md` (English, same holes), `key_frozen.tsv`, `key.tsv`,
`gloss_c317_heldout.txt`, `SIGN_CONVENTIONS.md`, `VERIFY.md`, `work/` (raw pass-1 digits and the pre-freeze key
work, kept for the timing of the held-out test), `scripts/` (decrypt.py, reading.py, check_marks.py, heldout.py;
strips.py, crop.py, profile.py, align.py were the image and exploration tools).
`python scripts/check_marks.py` rebuilds the three decryptions and checks every reading line against them; it passes.

## Prior art (checked 6 Nov 2026)

- Catalogue vetting of the same day: known.py (DECODE dump and ledgers), Tomokiyo's Cryptiana, Lasry's list: nothing
  on Griffoli. ASF inventory vol. VII p. 362 notes 40-41 name the key (Cifrari II serie F. III, not online) and the
  decipherment at c. 317 for the 2 Feb letter only; vol. VIII p. 137 note 3 says "Parzialmente in cifra" for 451.
- Web search 6 Nov 2026 ("Griffoli" Montalcino 1555 "Poggio Imperiale" ... cifra): no transcription, edition or
  decipherment of these letters found. Cantagalli, La guerra di Siena (1962) not seen; it may quote these despatches.
- The 2 Feb letter is a transcription job (c. 317 covers it). The 1 Feb letter and 451 c. 25 have no decipherment
  on record as far as checked.

## Changes after the independent check (6 Nov 2026)

`VERIFY.md` confirmed the statuses and the key and asked for three fixes. All are made:

1. **Context fills are no longer counted as repairs.** `reading.py` now counts a word whose letters fill a hole from
   context as a guess, a word with a hole inside it apart, and a dropped stray group as a repair. Two counting faults
   were found and fixed on the way: a fill of several words (`{[?1182543]/ et si è}`) had counted all but its first
   word as verbatim, and a «...» stretch that runs over several lines (451 r17-r21) had been counted as not parsed
   only on its first line. The verbatim shares fall from the first figures (443: 161 of 187; 451: 114 of 131, the
   verifier's 86.1% and 87.0%) to 159 of 187 (85.0%) and 92 of 129 (71.3%). The 93% and 92% "read as sense" figures
   of the first version are withdrawn.
2. **The two doubtful places were re-checked on the image** (table under Transcription).
3. **NOTES corrected**: "70 units" is 77 units and one odd group; the list of differences between the cipher and
   c. 317 is complete and no longer says the cipher reads cleanly in each.

Added after the check: the letter-level held-out score with a shuffled-key baseline (`scripts/heldout.py`), the
note on the c. 317 sign, the limits of the held-out test, and UTF-8 console output in every script.
`VERIFY.md` is the check as written; its figures predate these changes.

## 14 Nov 2026: issue #613 (Brice Dudout), six open places of 443 c. 315 tested

Brice Dudout sent six readings for open places of c. 315 from his own transcription of the letter (two partial passes
and a blind reading of single signs, 9 Nov 2026; the transcription itself was not sent). Each was tested here against
`key.tsv` and against the ASF image (IIIF, 2000 px wide, the maximum; crops enlarged 4 to 7 times, one reader, no
second pass). In every place the letters he proposes are the key values of the units already in
`transcription_c315.txt`, once one stray digit is dropped; no new key value is needed.

| place | transcription here | his reading | units under `key.tsv` | image, as read here | result |
|---|---|---|---|---|---|
| r09 | `53 43 0 74533 0 45` | si so fermi | 53 f, 43 e, 74 r, 33 m, 45 i; the 5 is over | 7, 4 and two 3-like signs before `0 45`; no separate 5 seen | fermi stands; `74533` is probably `7433` |
| r20 | `52 55 45 0 65345 0 47222 0 39 72` | chi fida{r}no | 53 f, 45 i, 47 d, 22 a, 39 n, 72 o; the 6 and one 2 are over | after `45` one oval sign (a 0 with a blot, or a 6), then 5 3 4 5 0 4 7 2 2 2 | "in chi fidano" stands with no added r; the 6 is doubtful, the third 2 is on the page |
| v01 | `39 0 477 0 72 0 32 23` | non riesendo la del medico | 47 d, 72 o; one 7 is over | 4, 7, then 0 7 2; a second 7 is not clear either way (show-through) | riesendo stands |
| v02 | `45 0 72423 0 15` | si fugira | 74 r, 23 a | 7, 4, a blotted oval, 2, 3: `74 0 23` | fugira stands; `72423` is probably `74023` |
| v03 | `52 0 722 0 34 74 0 45 0 74222 0 15` | si scoprira | 72 o, 74 r, 22 a; one 2 is over in each group | as transcribed: `72 2` and `74 22 2` | scoprira stands if the extra 2 is dropped in both groups |
| v04 | `75 76 0 23 0 3` (line end) | stan (probable) | 39 n would need a 9 | after the 3 a small sign with a descender against the gutter, 9 or 7 | probable, as he says; `39` not certain |

What follows from it:
- The extra 2 after 22 or 72 (the joined "2_2" form) can be dropped in all four places where it stands inside a word
  that then reads: r07 polizi-a (already so read), r20 fid-a-no, v03 sc-o-pri-r-a twice. Its value, a second null or a
  pen habit, is still not settled, but "drop it" now holds at four of four.
- The verso then runs on: "di modo che non riesendo la del medico, subito si fugirà in Montalcino per paura del
  tratato. Si scoprirà in Siena, et racolti li dieci homini che stan là per noi in Montalcino subito si farà": two
  futures after the plot is announced, where the reading had two past tenses and a hole. The translation's "someone
  fled to Montalcino" and "something was discovered in Siena" are therefore doubtful and should become futures.
- Not applied yet: `transcription_c315.txt`, `decryption_c315.txt`, `reading_c315.md`, `translation_c315.md` and the
  word counts are unchanged. The three digit corrections (r09, r20, v02) rest on one reader at 2000 px against the
  contributor's two passes, and need a second pass before the transcription is changed. Brice Dudout's own recount,
  about 177 of 186 words (95%), is his and unmeasured; by the count of this folder the six places move about
  ten words out of "decoded, not parsed", "context fill" and "with a hole" (159 verbatim of 187 now; about 169 of 187,
  90%, if all ten became verbatim), which does not reach 95%; r05-r06 and "del orladino" stay unparsed.
- His two unsettled digit readings are recorded for the same second pass: r10 `03946` here, `03976` or `03946` in
  his; r06 `2387645` here, `2387643` or `2387645` in his.

## Remaining gaps

- 451 c. 25v (about 19 lines) not transcribed; same key, should read on the same terms. (not attempted)
- 451 c. 25r r04-r05, r17-r21 and the «...» stretches of 443 c. 315: decoded, not parsed. (not attempted)
- Units 29, 71, 86, 97 and the single-place values 36, 78, 79, 83, 84, 88. (open codes)
- 443 c. 315 r09, r20, v01-v04: six readings by Brice Dudout (issue #613) tested and supported, not yet written into
  the transcription and the reading; three digit corrections wait for a second pass. (not attempted)
- The joined "2_2" groups and the blotted digits on 451 c. 25r; the overwritten sign in r02 is read as 0, not
  certainly. (illegible in part)
- The held-out test is small (24 words, 77 units). (too short)
- Names: Milandrone, "il medico" of Montalcino, Lelio, Alessandro. Check against Cantagalli and the ASF key
  (Cifrari II serie F. III) if anyone sees it. (not attempted)

## Escalation

- [x] siblings: the 2 Feb letter (443 cc. 316v-318r) in the same filza gave the key; 451 c. 25r is read with it
- [x] clear-pages: c. 317r (contemporary decipherment) used for the key (blocks a, b) and the held-out test (block c)
- [ ] known-keys: the ASF key (Cifrari II serie F. III) is named by the inventory but not online; not seen
- [ ] print: web search only; Cantagalli, La guerra di Siena (1962), not seen
- [ ] key-rebuild: units 29, 71, 86, 97 and the single-place values not rebuilt; 451 c. 25v would give more places
- [ ] retry: blotted digits on 451 c. 25r and the odd groups not retried beyond the two places in the table above.
  14 Nov 2026: six places of 443 c. 315 retried with Brice Dudout's readings (issue #613), all six supported by the key
  and the image (section above); still to do: a second pass on r09, r20 and v02, then the files and the recount
