# Catalogue 2354: Claudia de' Medici to Ottavio Piccolomini, Innsbruck 1646 (inv. 24793 and 24800)

WAINUT, 6 Nov 2026. Work done with AI language-model agents viewing the photographs, and checked by script as
described below. No human palaeographer has checked the text. An independent AI language-model agent checked the
work (`VERIFY.md`); the fixes made after that check are listed near the end of this file.

Status: in progress (not yet written up). Read in part, 6 Nov 2026: both bare letters are read in part. 24793 sits
right at the read bar (95.2% verbatim counting the code groups, 94.9% without them) and is not claimed as read.
No site page or README row; the open points are under Remaining gaps.

## Result in one paragraph

The cipher is a simple substitution of letters by signs (digits, letters, a cross, a triangle and a few special
shapes), with two signs for i and five two-figure code groups for names and titles. The key was rebuilt from the
contemporary interlinear decipherment of two sibling letters (inv. 24784 and 24796; the pairs are in `pairs.tsv`)
and from Vlnas 2017's printed table, frozen, and tested on held-out cipher of a third glossed sibling (24786): 13 of
13 words agree with the gloss in sense, 10 of them letter for letter (the other three are spelling variants). The
frozen key, unchanged, reads both bare letters:
**24793 (1646, day not on the frame): read in part. 79 of 83 cipher words verbatim from the signs (95.2%); 1 with a
doubtful sign shape ("forze"), 3 with a marked one-sign repair; no guesses, no holes. Without the 4 code groups,
75 of 79 (94.9%).**
**24800 (Innsbruck, 25 September 1646): read in part. 28 of 33 verbatim (84.8%); 5 with marked repairs, of which
one phrase ("indisciplinate genti", 2 words) is a conjecture. Without the 2 code groups, 26 of 31 (83.9%).**

## Documents

| inv. | date | cipher | status |
|---|---|---|---|
| 24793 | Innsbruck 1646 (day and month not on the frame; the page may continue on a sheet not in the zip) | 16 lines, 83 cipher words | **read in part**: 79 verbatim (95.2%; 94.9% without code groups), 1 doubtful sign, 3 marked one-sign repairs, no holes |
| 24800 | Innsbruck, 25 September 1646 ("Inspruch a 25. di 7bre 1646"), signed Claudia | 8 lines, 33 cipher words | **read in part**: 28 verbatim (84.8%), 5 with marked repairs, of which one phrase (2 words) is a conjecture |

Both are bare: no gloss over or beside the cipher. Originals: SOA Zámrsk, Rodinný archiv Piccolominiů (Náchod),
inv. č. 24793 and 24800 (microfilm label "31/2"). Images: photographs of the microfilm frames in the appendix of
Václav Vlnas, *Počítačová analýza šifrované korespondence rodu Piccolomini* (BA thesis, Univerzita Hradec Králové
2017, theses.cz/id/p3p2kb): Vlnas 2017, appendix zip P_lohy_A_a_B.zip (theses.cz/id/p3p2kb), frame 24793.jpg and
frame 24800.jpg; the key sources are frames 24784.jpg, 24796.jpg and the held-out test frame 24786.jpg of the same
zip. The photographs are rotated 90 degrees and soft; clean scans would have to be ordered from SOA Zámrsk (not
done). No images and no copy of the thesis are in this folder.

## System

Simple substitution of letters by signs, with homophones only for i (g/9 and y), plus two-figure code groups for
names and titles followed by a point. Word gaps are mostly real word breaks. Same system in all of Claudia's 1646
letters on microfilm 31/2 that we looked at.

Key (`key_frozen.tsv`; `key.tsv` has the same values; tokens defined in `SIGN_CONVENTIONS.md`):
2 a, m b, 5 c, D d, r e, 3 f, l g, K h, g/y i, c l, 4 m, s n, + o, Q p, 7 q, d r, x s, 8 t, A u/v, I z;
codes 18 = Duca di Lorena, 34 = S.A., 37 = Re, 57 = S.M.tà Catt., iio = V.E. Letters not seen: k, x, j.

## Key source

- **Glossed pairs, `pairs.tsv`** (42 cipher words with the contemporary gloss over each, written as signs).
  24784 (Claudia, Innsbruck 23 [?] 1646, interlinear decipherment by the recipient's office): trattato, concluso,
  dal marchese di Castel Rodrigo, con il S.r Duca di Lorena (18), Dio voglia, che partorisca buon effetto, la
  sicurezza delle piazze, fidategli, la qualità dell'umor di S.A. (34), ben noto ai spagnuoli, giunti i deputati
  Olandesi per trattar una tregua con S.M.tà Catt. (57). 24796 (Innsbruck, 1646): "del Re" over `D r c 37`, "di V.E."
  over `D g iio`, "con V.E." over `5 + s iio`. `scripts/check_pairs.py` decrypts every row with the frozen key: all
  42 give their gloss letter for letter, and together they attest all 21 letter signs and all 5 code groups.
  The pairs file was written after the independent check, from 3x-5x crops with the gloss in view; it is a record
  for rechecking the key, not a blind copy. Writing it showed that h is glossed too ("che", "marchese"); the first
  version of these notes said h came from Vlnas and sense alone.
- **Vlnas 2017, ch. 4.3, table 5** (rebuilt from inv. 24790, with his decipherment of that frame). It agrees with
  our key for every sign he lists: his 2 a, 5 c, £ d (our D), r e, 3 f, l g, ß h (our K), g and o i, c l, 4 m, s n,
  + o, & p (our Q), d r, a u (the triangle), 8 t. Differences: (1) his "ά = si" is the plain s sign (our x); in his
  own decipherment of 24790 it gives "si te" where the letters are "ste"; (2) his "i8. = da. di Corena" is the code
  18 = Duca di Lorena (the gloss on 24784 reads "Lorena"); (3) his "iio = initials of a name" is V.E. (glossed on
  24796); (4) he has no b, q, z, which the 24784 glosses add (m, 7, I); (5) his "c-" = k was not seen by us;
  (6) his "o = i" was not seen by us and is not in the key.

## Held-out test

Frame 24786 (Innsbruck, 9 Feb 1646, glossed) was not used to build the key. The key was frozen before its crops
were opened. Three partial cipher lines were transcribed by sign (`heldout_24786_transcription.txt`) and decrypted
mechanically (`heldout_24786_pairs.tsv`, graded by `scripts/check_pairs.py`):

| mechanical decryption with the frozen key | gloss on the frame |
|---|---|
| real seruitio mentre si communica con | [...] real servitio · mentre · si comunica · con |
| prudenti sensi | prudenti sensi |
| menti del [Duca di Lorena] doppo l accordato col | [fonda]menti del S.r D. di Lor. dopo l'accordato con il |

13 of 13 cipher words agree with the gloss in sense; **10 agree letter for letter**. The other three are spelling
variants: "communica" (double m in the cipher), "doppo" (gloss "dopo") and "col" (gloss "con il"). No sign failed.
The code group 18 agrees with the gloss "S.r D. di Lor.".

Limits, stated plainly: (1) the test is small, three partial lines and 13 words; (2) the gloss sits right above the
signs and was visible on the crops; the copy was not blind to it, and the first copy followed the gloss once (it
had `D + Q +`, "dopo"; the image has `D + Q Q +`, "doppo"; corrected after the independent check); (3) the freeze
cannot be proven. `key_frozen.tsv` is dated 15:07 and the held-out transcription 15:15 on 6 Nov 2026 (file times
only). No commit or hash was made at the time. The file's SHA-256, taken when this folder was packaged (after the
test), is `30246474278519d0356fdf772ebb5440c9337ef578e93e025b0b5d28fd337766`; it fixes the file from here on and
proves nothing about the order of work. The stronger evidence is that the frozen key alone turns both bare frames
into fluent Italian, and that Vlnas's separate decipherment of 24790 uses the same values.

## Reading

- 24793: `reading_24793.md` (marked text and Italian), `translation_24793.md` (English). Three repairs, each one
  sign: L02 an r-like sign for c in "con"; L04 and L08 a g/9 sign without its cross-bar for d in "de'" and "dall'".
  One doubtful sign: L03 "forze", whose fourth sign is an n-like form with a stroke over it, not the key's z shape
  (`I?` in the transcription); only z gives a word. The cipher text: success in Flanders depends on acting in
  concert and quickly while the Catholic and enemy forces are even; the opportunity should be used also on the Duke
  of Lorraine's side, unless he has hidden aims ruled by his passions or inconstancy; the King did well to order
  Piccolomini to stay in Flanders this year too, since the French will push their enterprises; may God give him
  complete victory.
- 24800: `reading_24800.md`, `translation_24800.md`. The news is "not very good for the interests of the King";
  affairs in Flanders go badly, much of it caused by "the disorders of the undisciplined [?troops] of the Duke of
  Lorraine", which, as Piccolomini wrote, could bring still greater ruin. Repairs: `2/Q` read as p in "per" (the
  sign's loop is unclear on the photograph); a cross read as 4 (m) in "prudentemente"; one d added in "addosso"
  (the writer's spelling "adosso" may be intended). The signs give `indisciplinitelenti`; we read "indisciplinate
  genti" with two changed signs (y read a, c read as the tall g sign). That phrase is a conjecture and both words
  are flagged `[?...]` in the Italian and the English.
- Mechanical decryptions: `decryption_24793.txt`, `decryption_24800.txt` (`scripts/decrypt.py`).

## Word counts (from `scripts/check_marks.py`)

| inv. | cipher words | verbatim | doubtful sign | marked repair | guess | hole | verbatim share | without code groups |
|---|---|---|---|---|---|---|---|---|
| 24793 | 83 | 79 | 1 | 3 | 0 | 0 | 95.2% | 75 of 79, 94.9% |
| 24800 | 33 | 28 | 0 | 5 | 0 | 0 | 84.8% | 26 of 31, 83.9% |

Code groups ([Duca di Lorena], [S.A.], [Re], [V.E.]) are counted as cipher words: their values come from glosses on
the sibling letters, and in these two letters each stands where the sense needs it. They are 4 of the 83 words in
24793 and 2 of the 33 in 24800. The second figure leaves them out.

**The margin of 24793.** Before the independent check the count was 80 of 83 (96.4%). With "forze" counted as
doubtful it is 79 of 83 (95.2%), just over the 95% bar; without the code groups it is 75 of 79 (94.9%), just under
it. One more doubtful word would put even the first figure under 95%, and both the solver's sign copy and the
verifier's were made knowing the sense. We therefore mark 24793 **read in part**, not read. A clean scan of the
frame, which would settle the "forze" sign and the three repaired shapes, could justify "read".

`python scripts/check_marks.py` rebuilds both decryptions from the transcriptions and the frozen key, checks that
every departure of the readings from the signs is marked (including every doubtful sign shape), prints the counts
above, and rechecks the glossed pairs and the held-out test. It passes (6 Nov 2026). It shows consistency only.

## Method

Sign conventions written first (`SIGN_CONVENTIONS.md`). Each bare frame transcribed twice from separate crops
(pass 1: 2.1x crops of two-line bands; pass 2: fresh 2.0x single-line strips, plus 4x crops of doubtful spots), then
reconciled on the image (`transcription_<inv>_pass1.txt`, `..._pass2.txt`, `transcription_<inv>.txt`; the
reconciliation notes are at the head of each reconciled file). In honesty: the alphabet is small and the plaintext
became obvious during pass 1, so the sign copy was not made blind to the sense. The places where sense and shape
pull apart are left as the shape shows and repaired in the reading with a mark, not changed in the transcription.
The 5/s (c/n) and g/D (i/d) pairs are the hardest to separate on these photographs.

## Prior art (checked 6 Nov 2026)

- Vlnas 2017 lists 24793 and 24800 in appendix B ("photocopies of cipher texts not deciphered in the thesis") as
  B07 and B12, and gives no text for them. His ch. 4 deciphers 25039, 24873, 24790 and 25106 only. His table 5 and
  24790 decipherment were used here as a key source and crib, not as a reading of these frames.
- Web search "Claudia de' Medici Piccolomini 1646 lettere cifrate Duca di Lorena Fiandra": only biographies of
  Claudia and unrelated finding aids; no edition or decipherment of these letters.
- The catalogue entry's earlier checks (DECODE dumps, Tomokiyo, Lasry, HistoCrypt 2018 summary of Vlnas) found
  nothing either.
- This repository (6 Nov 2026): no target folder for Piccolomini, Zámrsk or Vlnas; the only note is the Czech
  regional-archives sweep that listed the lead (catalogue 2354). No open pull request on this archive.

## Historical context

Claudia de' Medici (1604-1648), widow of Archduke Leopold V, governed Tyrol for her son Ferdinand Charles until he
came of age in 1646; these letters are still signed "Claudia". Ottavio Piccolomini, Duke of Amalfi, commanded for
Philip IV in the Spanish Netherlands in 1644-1647. The summer and autumn of 1646 went badly for Spain in Flanders:
Courtrai and Mardyck fell, and Dunkirk fell to Enghien in early October 1646, a few weeks after 24800. Charles IV of
Lorraine, whose army served Spain, was a doubtful ally; both letters single him out. The glossed siblings of the same
year (24784, 24794) also report the Dutch deputies at Münster negotiating a truce with Spain.

## Files

| file | what |
|---|---|
| `SIGN_CONVENTIONS.md` | token names for the sign shapes |
| `key_frozen.tsv`, `key.tsv` | the key as frozen before the held-out test; the working copy (same values, one source note added) |
| `pairs.tsv` | the glossed words of 24784 and 24796 as signs, with their gloss |
| `heldout_24786_transcription.txt`, `heldout_24786_pairs.tsv` | the held-out lines and their word-by-word comparison with the gloss |
| `transcription_<inv>.txt`, `transcription_<inv>_pass1.txt`, `_pass2.txt` | reconciled and first-pass sign copies |
| `decryption_<inv>.txt` | mechanical decryption with the frozen key |
| `reading_<inv>.md`, `translation_<inv>.md` | marked text and Italian; English |
| `scripts/` | `decrypt.py`, `reading.py`, `check_pairs.py`, `check_marks.py` (standard library only) |
| `VERIFY.md` | the independent check, as written |

## Changes after the independent check (6 Nov 2026)

`VERIFY.md` confirmed the key, the sign copy and the mark check, and asked for six fixes, none of which it expected
to change a status. All are made:

1. Held-out L03: `D + Q +` corrected to `D + Q Q +` ("doppo"); 10 of 13 words letter for letter, not 11; the
   visibility of the gloss on the crops is stated.
2. 24793 L03: the fourth sign of "forze" is now `I?` (near the z shape, not equal to it); `decrypt.py` prints it
   `(z)` and the reading marks it `{?z}`. 24793 L02: `D g` is now `D y` (same value).
3. The margins of 24793 are given, and code groups are said to be counted as cipher words. `reading.py` now prints
   the share without code groups and counts doubtful signs apart.
4. `pairs.tsv` added, with `scripts/check_pairs.py`.
5. The freeze: recorded as far as it can be now (file times and a hash taken at packaging; see Held-out test).
6. "indisciplinate" is flagged as well as "genti" in the Italian and the English.

Consequence for the status: with "forze" doubtful, 24793 falls from 80 to 79 verbatim words (95.2%), and without
the code groups to 94.9%. The independent check had confirmed "read" on the old figure; we now mark it read in part
(see Word counts). Also added: UTF-8 console output in every script, Vlnas's "o = i" in the comparison with his
table, and the English translations moved to their own files. `VERIFY.md` is the check as written; its figures
predate these changes.

## Remaining gaps

- The date of 24793 (and whether it continues on another page) is not on the frame.
- The phrase "indisciplinate genti" in 24800 needs a clean image of L05.
- The "forze" sign in 24793 L03 and the five single-sign repairs (5/s and g/D shapes) need clean scans of inv. 24793
  and 24800 from SOA Zámrsk.
- Not used: glossed frames 24787, 24788, 24789, 24794, 24799, 24799_1, 24806 (24806_1 is a blank verso). They would
  give a larger held-out test.
- No human has checked any sign.

## Escalation

- [x] siblings: the glossed letters 24784 and 24796 of the same writer and year gave the key; 24786 the held-out test
- [x] clear-pages: the contemporary interlinear decipherments on those siblings used (pairs.tsv)
- [x] known-keys: Vlnas 2017, table 5 (from inv. 24790), compared sign by sign; it agrees
- [x] print: Vlnas 2017 (24793 and 24800 listed as not deciphered), one web search; no edition found
- [x] key-rebuild: every letter sign and code group in both letters has a value; nothing left to rebuild
- [ ] retry: the 'forze' sign, the five repaired shapes and 'indisciplinate genti' need clean scans from SOA Zámrsk
  (not ordered); the unused glossed siblings would enlarge the held-out test
