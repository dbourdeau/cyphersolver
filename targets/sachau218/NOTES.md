# Sachau 218 f. 231a: four lines of signs in a Syriac-Karshuni miscellany from Midyat (Berlin SBB)

Status: attempted, 16 Nov 2026. Not read. One key tested (abjad numerals) and not supported, but the test turned
out to have almost no power at this length (see the matched control). The lines may be a reckoning table and
not a cipher. Catalogue entry 2943 (lead 2933 before the renumbering in PR #706).

## The document

- **Shelfmark.** Staatsbibliothek zu Berlin, Sachau 218 (Sachau, *Verzeichniss der syrischen Handschriften*, 1899,
  no. 188), f. 231a (= 231r). A miscellany "angelegt von einem Geistlichen zu Midjad im Tur Abdin", Syriac and in
  smaller part Karshuni. The SBB METS dates the volume 17XX.
- **Images.** SBB digital collections, PPN618589309, image 467 (f. 231r); images 466 and 468 are ff. 230v and 231v.
  Record: <https://digital.staatsbibliothek-berlin.de/werkansicht?PPN=PPN618589309> (METS:
  <https://content.staatsbibliothek-berlin.de/dc/PPN618589309.mets.xml>). The METS names no licence, so no image or
  crop is in this folder; open the leaf in the SBB viewer.
- **What is on the leaf.** Four underlined lines at the top, written right to left, after the Karshuni Prayer of
  Solomon against the Red Wind (ff. 225a-230b). Below them, lines 5-9 in large Karshuni script give a method for
  knowing whether a sick person will recover ("لمعرفة المريض..."), with red dots used as Karshuni diacritics.
  Sachau: "vier Zeilen in einer Chiffreschrift, bestehend aus Ziffern, Buchstaben und willkürlich erfundenen
  Zeichen", with no reading.

## Prior work

None found. The catalogue 2943 vetting (PR #706) searched DECODE, Tomokiyo, Lasry and the web. On our side we found
nothing on Sachau 218 or Midyat in our files, and no issue or PR in this repository apart from #706.

## Transcription

`transcription.txt` (SHA-256 in `transcription.sha256`, frozen before any decoding): **59 signs of 26 shapes in
about 13 groups**, so fewer than the 120-160 estimated at vetting. `/` marks a clear blank between groups;
`python docs/_check_profile.py --measure` counts the 9 slashes as tokens (68), the signs are 59.
Labels are neutral names for shapes; the full inventory, the two passes and the arbitration are in
`TRANSCRIPTION.md` (French working notes). In short:

- Some signs look like Eastern Arabic numerals: I (vertical stroke, ١ or alaph), F (the Persian 4, ۴), E (the
  Arabic 4, ٤), N9 (٩), O (small loop, ٥ or waw), L (Λ, ٨), R (٢ or rish), W (٣).
- Some look like Serto letters (loops like waw/he, wavy signs like semkath/shin), and some like nothing in either script.
- Commonest: I 8, F 6, M 5, D 5, Q 4, R 4, C 4, N9 3.
- What is not a sign: the hooks at the right and the lassos at the left of each line belong to the underlining.
  The strokes that look like lamadh-alaph ligatures at the end of line 4 are the ascenders of line 5.
- Red dots: only the dot under the first F of line 1 is surely a diacritic of a sign; the others may belong to the
  underlining or to the lines above (`tools/reddots.py` found them on a BMP crop).
- Two passes by the same reader (Claude Opus 5.5) at two scales agreed at 55 of 59 positions. All four
  differences were segmentation, not shape, and were settled on the image. The passes are therefore not independent.

## The test (pre-registered, one run)

`PREREG.md` (French; SHA-256 in `PREREG.sha256`) was frozen before any decoding.

- **Key K1, abjad numerals.** Each numeral-shaped sign stands for the letter with that abjad value: I = ا, R = ب,
  W = ج, E and F = د, O = ه, L = ح, N9 = ط. The red dot under the first F multiplies by ten (٤٠ = م). Sachau's
  "Ziffern" suggested this key, and so did the alphabet "of Simon", in which letters are written with numbers.
  The other 18 shapes are left unknown, and no value was adjusted.
- **Measure.** Mean log-probability of the adjacent letter pairs that are both decoded inside a group, under an
  Arabic bigram model (Tanzil Qur'an text, simple-clean, reduced to the 22-letter Karshuni alphabet). The null is
  200 keys that give the same 8 classes 8 random letters (seed 2933).
- **Bar.** Score at least the best null **and** at least 3 groups decoded entirely into attested Arabic or Syriac
  words.
- **Result** (`MEASURE.txt`): −2.80 on 12 bigrams. The nulls' maximum is −2.49 and their median −4.04, so K1 is 12th
  of 201. No group gives a whole word (fragments such as `?اهدا?`, `?دابدج`). **K1 is not supported.**
  Re-run: `python3 tools/measure.py <corpus> transcription.txt` (re-run at integration, same output). The corpus is
  the Tanzil text, which is not in the repository; lines are `sura|aya|text`.
- **No held-out portion.** The text has 59 signs and there is no second document in the same system. PREREG
  declares this departure from the protocol.

## Matched control (added after the measure)

Is a synthetic text of 59 signs relevant? Yes: it asks whether the frozen test could have recognised the true key
at all. `tools/matched_control.py` (output in `matched_control.txt`) takes 200 runs of 13 consecutive Arabic words
of 55-63 letters. The runs come from the last 15% of the same corpus, and the bigram model is retrained on the
first 85%. Each run is enciphered with K1's design: the 7 letters K1 values get K1's sign classes, every other
letter an unknown sign. The **true** key is then scored exactly as K1 was, against 200 random keys.

- The true key comes **first of 201 (the pass rule) in only 16 of 200 trials**. Its median rank is **12**, the
  same as K1's rank on the leaf. 52% of the true keys rank 12th or worse.
- The true key decodes on average 0.23 groups of two or more letters entirely. **No trial reaches the 3 whole words
  the sense rule asks for.**

So the frozen test could almost never have passed, even with the right key. K1's failure says little: K1 is **not
supported, but it is not ruled out**. A fair test of K1 needs more text in the same system, or values for more of
the 26 shapes. The control uses Qur'anic Arabic, while the leaf's plaintext could be Karshuni or Syriac. That makes
the control, if anything, kinder to the test than the leaf would be.

## Other key material looked at

- Sachau 116 f. 1r (PPN873368509, image 7) has several alphabets (letters with red equivalents, alphabets in
  circles and strokes). None looks like the signs of 218.
- Sachau 93 f. 75 (PPN1851354778, image 152) has a Syriac atbash table (ܐ↔ܬ, ܒ↔ܫ, ܓ↔ܪ ...) and a ladder-shaped
  cipher in the margin. These were not tested: the signs of 218 do not read consistently as Serto letters, so no
  objective test could be frozen.
- Sachau's 1899 index of secret scripts (Bardesanes, Simon, Narsai, and others) is only described in the OCR text.
  The tables themselves were not all opened.

## Language and nature: open

The plaintext language is not settled. There are weak signs of Karshuni: the Karshuni context on f. 230v and in
lines 5-9, and the red dots used as in the copyist's Karshuni. A second reading should be kept open: the four lines
may be a table of values (letters and numerals) for the sick-person reckoning that follows. That would make them a
prognostic table, not a cipher. Nothing here settles it.

## Related item in progress: Sachau 221 f. 20b

Sachau 221 f. 20b (= 20v; Sachau 1899 no. 179; PPN187305548X, image 40) has two lines under a red title. They are
in a different system from 218, a "tree" script (branches to the left and right of a stem). Work on it is in
progress and its check is not finished: **no reading or value is offered here.** It is not yet a lead.

## Remaining gaps

- A reader of Serto and Karshuni to re-check the transcription. Twenty-six shapes are too many for a clean simple
  substitution, so some labels probably need merging. Blocker: not-attempted.
- A second text in the same system (other Midyat manuscripts, the Sachau volumes with "Chiffreschrift"), to give
  a test with power and a held-out portion. Blocker: too-short.
- Whether the lines are a prognostic table rather than a cipher. Blocker: not-attempted.
- The Syriac atbash of Sachau 93 f. 75 and the alphabets of Bardesanes, Simon and Narsai, untested.
  Blocker: not-attempted.

## Credits and tools

Brice Dudout chose the lead and set the rule (transcription and test frozen before any decoding, one run). Claude
Opus 5.5 agents transcribed, measured and wrote this up; the matched control was added at integration. Lead and
vetting: Daniel Bourdeau with a Claude Code session (Arabic sweep 2, PR #706). No human has checked the transcription.
