# Selvatico Estense -> Giuseppe Riva, two cipher letters from Paris, October 1719 (new target, not in the catalogue)

Status: read in part (3 Nov 2026), for the two 1719 letters: the 2 Oct letter is read in part, the 27 Oct letter is
decoded with the frozen key but not read (fragmentary). Lead 1568 (the 1722 letters) and the two undated letters are
not solved. Work by WAINUT, with AI language-model agents:

| Letter | Shelfmark (Modena, Biblioteca Estense, Autografoteca Campori, Lettera S, Selvatico Estense) | Kind of job | Outcome |
|---|---|---|---|
| Paris, 2 Oct 1719 | cc. 4-7 | transcription (contemporary interlinear decipherment, legible in part) | read in part: 159 of 249 words in the cipher passages read without a mark (64%) |
| Paris, 27 Oct 1719 | cc. 12-13 | break with the frozen key (no running interlinear found on the scans) | decoded, not read: fragmentary; 116 of 190 tokens unmarked (61%), many of them fragments |
| Vienna, 10 Jun, 29 Jul, 8 Aug, 12 Aug 1722 | cc. 21-22, 25-26, 35-36, 23-24 | break | not solved: another table; the 1719 key does not read them |
| '2 gennaio', unsigned; '10 dicembre' | cc. 2-3, 14-15 | break | not solved; number profile like the 1722 letters |

These letters are not in Dan's `catalogue.json`. The four 1722 letters are the letters of lead 1568 (the Riva lead);
**lead 1568 stays unsolved**. The two 1719 letters and the two undated ones were found next to them in the same
Estense file. This target is about the 1719 letters only; the 1722 and undated letters are listed as not read.
Lead 1568 also lists five Starhemberg letters to Riva (1721-1727); they were not worked.

## The 1719 system and key

Small homophonic alphabet with syllable signs and a nomenclator. Vowels 1-5 (a e i o u/v), consonants 6-15
(l m n p . b c d f g), syllables 21-24 (la le li lo), 25 r, 26 s, 27 t, 29 z, second homophones 31 a, 34 o, 35 v;
underlined small numbers are short words (3_ in, 4_ il, 7_ con, 8_ e); numbers above about 40 are code words
(40_ Stati, 68 Corte, 82 Duca, 166 questo/questa, 168 quale, 173 Re, 175 Francia, 281 Orléans). Many groups begin
with a curl; the curl is not a sign: c31/31, c26/26, c13/13 read the same letter wherever the gloss covers both.
Some groups are written run together with dots ('8.4.3', '1.13'); they are split into their groups.

`key_frozen.tsv` is the key built only from the gloss pairs on ff. 4r-5r and frozen before any test; the decryption
and every count use it. `key.tsv` is the frozen key plus the four values seen after the test (18 n, 20 qu, 32 e,
33 i); in the readings these are always marked in brackets (`[18 n]`).

## Transcription

Two independent sign passes per letter (rules: `TRANSCRIPTION_RULES.md`), from full-size crops, before any
decoding. 1719: pass A fully blind to the interlinear gloss (`work/pass_a_1719.txt`); pass B transcribed each line
before reading its gloss and never revised the numbers after. Agreement 704 of 1024 groups (curl splits and 2/7/4
shapes account for most differences, `work/diff_1719.txt`). `transcription_1719.txt` is pass B with the five
corrections below. 1722 and cc. 2r, 14r: passes A and B in `work/` (1497 of 1664 groups agree).

Corrections made on 3 Nov 2026 after the independent check (`VERIFY.md`), each settled on a full-size crop:

| Line | Was | Now | Why |
|---|---|---|---|
| 5v.L11 | `c23 31 1` | `c25 3 1` | the second digit is an s-shaped 5, unlike the B-shaped 3 beside it; gloss "la furia" |
| 6r.L09 | `c3` | `c23` | the 2 is clear; gloss "valida" |
| 6r.L10 | `1.73` | `173` | one code group (Re); gloss "Re" over it |
| 6r.L15 | `1 7 3` | `173` | spacing a little wide, but one group; gloss "Re" |
| 6r.L02 | `3` | `3_?` | a stroke runs under the 3 (3_ = in; gloss "impiego"); it may belong to the gloss of the line below, so it is kept as doubtful |

No disagreement with the check was left: all five were confirmed on the crops.

## Decryption and the parser

`decryption_1719.txt` is the byte-for-byte output of `python scripts/decrypt.py key_frozen.tsv transcription_1719.txt`.
The first version of the parser kept only tokens of one group: 18 tokens with an inner dot, '=', a non-ASCII
superscript or '#' were dropped with no placeholder, and the checker could not see them. One reading line (6r.L10)
had left out 173 = Re unmarked because of this. Now every token is split into its groups, a group the key does not
cover prints as `[n]`, an unparsable piece as `[?]`, and `scripts/check_marks.py` lets only a bracket in the reading
absorb them: a group can be neither read nor left out silently. Three reading lines failed on this and were
corrected (4v.L08, 6r.L10, 13r.L08); several dotted groups now decrypt (6v.L01 gelosia, 12r.L14 "mi sono",
13r.L08 "la mia").

## Reading and counts

`reading_1719_1002.md` and `reading_1719_1027.md` give the reading line by line, then a continuous Italian text;
`translation_1719_1002.md` and `translation_1719_1027.md` the English. Holes are marked in place.
`python scripts/check_marks.py` rebuilds the decryption, fails on any unmarked departure, and counts:

| Part | words | read without a mark |
|---|---|---|
| 2 Oct, ff. 4r-5r (the key was built from this gloss: circular as key evidence) | 136 | 88 (65%) |
| 2 Oct, ff. 5v-6v (held out) | 113 | 71 (63%) |
| 27 Oct, ff. 12r-13v (no gloss) | 190 | 116 (61%) |
| all | 439 | 275 (63%) |

These shares count every unmarked token as a word, including fragments that do not read as sense. In the 27 Oct
letter that matters: the verifier estimates about 50% reads as sense, and the reading is a string of fragments.
That letter is therefore given as decoded, not read. Both letters are far below the ~95% needed for "read".

## Held-out test (scripted)

`python scripts/heldout_5v6v.py` compares the frozen key with the contemporary gloss over the held-out pages
(ff. 5v-6v), word by word, from `gloss_heldout_5v-6v.tsv`. That file replaces the rough gloss alignment of pass B,
which had misread gloss words (apparenza for assistenza, denaro for demerito, che for Re, arrive for animo,
intimone for insinuare). Gloss words on 5v.L11-15 and f. 6r were read by the independent verifier before opening
any solver file; those on f. 6v by the packager after the freeze (not blind to the key; flagged `P` in the file).

| | gloss words | exact with the frozen key | needs only a post-test value | other ending (questo/questa) | uncovered code | miss |
|---|---|---|---|---|---|---|
| all | 63 | 44 | 7 | 4 | 7 | 1 |
| read by the verifier (5v, 6r) | 45 | 30 | 5 | 3 | 6 | 1 |

Of the 56 gloss words with no uncovered code group, 44 (79%) come out of the frozen key exactly; the one miss is
52 = "buona" against the gloss "buon". No gloss word contradicts a letter value of the frozen key. The 4 "ending"
cases are 166 written with a superscript a or a dot for "questa", a mark the frozen key does not interpret.
NOTES of 2 Nov had "about 31 of 40" from a hand count; this script replaces it.

The 27 Oct letter has no gloss, so it gives only a sense test, not a graded one.

## Why the 1722 letters are not read

Same writer and recipient, but another table. The 1722 groups are mostly 50-95 (60, 52, 80, 61, 71, 74, 63 ...),
with heavy underlining; the 1719 alphabet sits in 1-35. The 1719 key covers 33% of the 1722 groups as letters and
gives no words; shifts by 30, 50 and 60 give nothing (`scripts/test_1722.py`). A quick ciphertext-only homophonic
attack (`scripts/solve_1722.py`, simulated annealing with Italian quadgrams from Italian plaintexts in this
repository) did not converge to sense in two runs (`work/solve_1722_out*.txt`); it was not tuned further. Repeated
runs worth a crib attack: `60 7_ 50 52_ 64_'` (three times, in 21r, 21v and 25r), `3_ 92 50 81 5` (21r, 25r),
`6 72_ 80 91`.

## Context

Benedetto Selvatico Estense (1673-1735) wrote from Paris in Oct 1719 to Giuseppe Riva, Modena's agent then in
London, on the peace congress after the War of the Quadruple Alliance, the succession of Tuscany against Lorraine,
a marriage plan with Mademoiselle de Valois (daughter of the Regent Orléans; she married the heir of Modena,
Francesco d'Este, in 1720), Lord Stair, and Count Scotti. The marriage negotiation itself is known history; these
letters add the envoy's cipher passages on it. In the 27 Oct letter, "the Queen mother" and "the Duchess of Berry"
are conjectures from "la [17]i madre" and "be[ivi]", not readings.

## Remaining gaps

- The four 1722 letters of lead 1568 (cc. 21-22, 23-24, 25-26, 35-36) and cc. 2-3, 14-15 - blocker: no-key-material; another table, not read by the 1719 key; two untuned annealing runs failed. A crib attack on the repeated runs, or that key from an archive (Archivio di Stato di Modena, Cancelleria ducale, ambasciatori, Vienna 1722, may hold minutes or the cifrario), is the way on. The two sign passes are in `work/`.
- The five Starhemberg letters listed in lead 1568 - blocker: not-attempted; not worked.
- Code numbers of the 1719 letters - blocker: open-codes; 0_, 16_, 17, 28, 55, 57, 60, 69, 71, 76, 78, 79, 80, 87, 91, 93, 121, 126, 127, 138, 139, 140, 151, 155, 160, 170, 171, 174, 185, 190, 200, 208, 226, 264 are unidentified or only proposed (55 Conte, 69 corriere, 138 ministri, 139 maneggio from the gloss of the held-out pages, not added). 37% of the words of the 1719 cipher passages are still marked.
- The 27 Oct 1719 letter as a continuous text - blocker: open-codes; decoded with the frozen key, fragmentary, no gloss.
- Groups where the two passes disagree (`work/diff_1719.txt`) outside the verifier's sample - blocker: not-attempted; settled on crops only for 5v.L11-15 and f. 6r.
- Clear text of the letters - blocker: not-attempted; abridged in braces only, and the English covers the cipher passages only.
- No human palaeographer checked the transcription - blocker: not-attempted.

## Escalation

- [x] siblings: all eight Selvatico cipher letters in the Estense file opened and transcribed in two passes; the 1719 key tried on the 1722 and undated letters (it does not apply)
- [x] clear-pages: the 2 Oct letter's interlinear gloss used for the key (4r-5r) and the test (5v-6v); the 27 Oct letter checked for an interlinear (only a few superscript letters by the writer)
- [ ] known-keys: no other key of Selvatico, Riva or the Modena legations of 1719-1722 was found or tried; the Archivio di Stato di Modena cifrari were not searched
- [x] print: web searches for an edition or decipherment (see Prior art); none found. Calendars of the Modena legations not searched
- [ ] key-rebuild: the four post-test values are kept out of the frozen key; the code numbers listed above were not rebuilt beyond what the gloss gives
- [ ] retry: groups where the two passes disagree retried on crops only in the verifier's sample (5v.L11-15, f. 6r)

## Prior art (checked 3 Nov 2026)

Dan's catalogue, leads and Dudout list: 1568 is the Riva lead (the 1722 letters); the 1719 and undated items are not
in them. Web searches ("Selvatico Giuseppe Riva Modena 1719 1722 cifra"; "Benedetto Selvatico Estense 1719 Parigi
Vienna 1722 inviato modenese"; the verifier's "Selvatico Estense lettere Giuseppe Riva 1719 Parigi cifra Mademoiselle
de Valois Autografoteca Campori"): no edition or decipherment found. Lindgren and Timms print Riva's Steffani
letters, not these.

## Scripts

- `decrypt.py`: the mechanical decryption (standard library).
- `check_marks.py`: rebuild and mark check, word counts per part (standard library).
- `heldout_5v6v.py`: the held-out test against the gloss (standard library).
- `test_1722.py`, `solve_1722.py`: the 1722 tests (standard library; `solve_1722.py` reads Italian plaintexts of
  this repository with `git show`).
- `fetch.py`: IIIF fetch (needs Pillow), one request at a time; images go to `scans/`, which is not committed.

## Images

Estense IIIF manifests https://edl-jarvis.cultura.gov.it/meta/iiif/<uuid>/manifest: f63082e8-940a-40f6-a750-3f79f0e92747
(cc. 4-7), 50c0581b-9def-497e-88ac-54678e5eca0e (cc. 12-13), 0c61023d-19aa-48e9-affa-89ec7da5ed67 (cc. 21-22),
b398032c-89f0-4267-8ace-e5aa4d76a8e9 (cc. 25-26), 3cf6cbb0-da58-4f26-ae4f-c6a3e250b065 (cc. 35-36),
d65064be-e2e4-4e16-9289-367b8ec682ad (cc. 23-24), 179df476-88bd-4f95-b4bd-574569bf8b6d (cc. 2-3),
761ee342-8fd0-49dd-8e4f-1872bb3d19d9 (cc. 14-15). CC BY-NC-SA; fetched as tiles, not committed.
