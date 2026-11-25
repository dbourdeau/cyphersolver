# Juan Manuel to the Catholic Monarchs, Genoa, 10 November and 18 December 1496 (BNE MSS/20212/61/1 and /2; catalogue 1270)

Status: in progress. Deciphered in part with George Lasry's key for BnF Espagnol 318 no. 95 (8 January 1497), applied
unchanged: **653 of 933 cipher words (70.0%) of the letter of 18 December and 253 of 388 (65.2%) of the letter of
10 November read**, by the repository's word rule (below). Both documents are classified as decoded, not read. The code groups in Latin
letters are all unread. The key passed planned tests on text that nobody had decoded before, and an independent check
with its own readers passed on both letters; the misses on the way are listed in order below. The reading awaits a
reviewer's `reading_review`; no write-up page yet. All of this was done by AI agents on 17 Nov 2026; no person has
checked any transcription, reading or translation.

One key, one entry: both letters are in the same cipher, in the same volume, under the same catalogue row (1270), so
they are one target. A third letter in this key, Juan Manuel's of 14 April 1497 in Zaragoza (catalogue 2857), is the
sibling target `../juanmanuel1497/`; it has its own catalogue row and archive. The tests on unseen text below are the
evidence for the key in both targets.

## The documents

Biblioteca Nacional de España, MSS/20212/61/1-7 (Gayangos), "Cartas de Don Juan Manuel a los Reyes Católicos y al
Emperador Carlos V", seven letters 1496-1522. Record: <https://bnedigital.bne.es/bd/card?oid=0000186690> (BNE Digital
bdh0000186690). Juan Manuel was the Spanish envoy at Genoa.

- **Letter 1, MSS/20212/61/1: Genoa, 10 November 1496.** Cipher on f. 2v (25 lines, here L01-L25) and f. 3r (21 lines,
  R01-R21, headed "1496"): 1,527 sign positions in the transcription. Nothing is written between the lines: no
  decipherment of the time.
- **Letter 2, MSS/20212/61/2: Genoa, 18 December 1496.** Cipher on f. 6r (34 lines, A01-A34, headed "1496"), f. 6v
  (36 lines, B01-B36) and f. 7r (25 lines, C01-C25, ending in ordinary handwriting): 3,674 sign positions. Heavy
  show-through from the other side of the leaf on ff. 6r and 6v. No decipherment of the time on the leaves.
- The clear pages that open each letter were not transcribed.

**Images: none in this folder.** The library's record says the volume is in the public domain, "CC BY 4.0 o
equivalente. Atribución a la Biblioteca Nacional de España"; Europeana's copy of the same record
(<https://www.europeana.eu/item/2022717/bnesearch_detalle_bdh0000186690>) gives CC BY-NC-SA 4.0. The work used the
library's own PDF of each letter at the largest size it serves (page spreads of 2029 x 1475 and 2048 x 1488 pixels).
Nothing from Lasry's key image is copied either.

## The key: Lasry's no. 95 key, by reference

`../esp318no95/lasry2021/ctts/key.txt` (sha256 5ee40781ca8a562dcfd1a760b88806a24f458140007c3ea376cb638c4f08fb06), read by
`decode.py` by relative path, hash checked. 44 invented signs for 21 letters, three special signs (his null `D`, his `9`
"[y?]", his `oN` "[aunque?]") and 11 code groups written in letters. **No value of ours is used in the main reading:**
nothing was changed, added or refitted. Signs that are not in his table have no value.

**One late mapping, reported apart.** An S-shaped stroke that the readers' sign sheet first left without a value was
matched afterwards to Lasry's own `S` (value d): his four `S` glyphs on f. 122r, located with his own position files,
have the same hook at the top opening left, slanting stem and tail curling left at the foot, and are plainly unlike his
plain 7. The match was made after decodes had been seen, so it is not a test: the transcriptions write the sign `S`,
the main decodes and every count give it no value, and `decode_*_with_S.txt` show what it adds. It completes six words,
all of which then read as Spanish: L10 *podemos* and *del*, A10 *dar*, B01 *mandarme*, B04 *necesidad*, B06 *funda*
(four more words gain a d and stay unread: A01, A20, B03, R17).

## How the transcriptions were made (all readers AI agents)

- **The sign sheet.** Value-free: each row shows examples of one sign cut from the 1496 letters themselves, with a neutral
  id (W01-W49); the readers never saw a value, Lasry's names, the key or a decode. Each row was mapped to one of
  Lasry's sign names by shape, against his own glyphs cut from his photograph of no. 95 with his position files. Rows
  W01-W38 and their mapping were fixed and hashed before any reader started on letter 2 and before any decode of it
  (`records/unseen_text_test/hidden/sheet_mapping.tsv`). Rows W39-W49 were added afterwards for signs the first readers
  had met without a row; that mapping was made by an agent that had seen decodes of f. 7r, so it is not blind
  (`records/sheet_mapping_v2.tsv`). Signs with no counterpart in Lasry's key keep their row name in the transcription:
  `<W26>` barred u/v, `<W27>` eight, `<W48>` a 6 or G shape, `<W49>` a # shape.
- **Letter 2.** Two independent teams of blind readers transcribed every line from enlarged line images; a script
  aligned their texts and kept a position only where both agree (76.0% of positions; f. 7r 93%, ff. 6r-6v 70-72%
  because of the show-through) (`records/unseen_text_test/transcriptions/`). Then the show-through on ff. 6r-6v was
  reduced digitally: the other side of the leaf, mirrored and registered onto the page, was subtracted (the originals
  were kept, and every reader had the unprocessed line beside the treated one). Two fresh readers per page re-read
  ff. 6r-6v (agreement 86.9% and 78.6%), and a third fresh reader looked at each place where they differed. On f. 7r the
  open stretches were re-read by two fresh readers and a third where they differed.
- **Letter 1.** First read by two blind readers with a sign sheet cut from Lasry's key image (81.6% agreement; see the
  first test below); re-read by two fresh teams with the sheet cut from the 1496 hand (91.2%); open stretches then
  re-read as for f. 7r.
- **Restored holes.** The independent check found that a step had deleted a sign at 36 places on ff. 6r-6v because a
  third reader left the answer blank (two of five such places it sampled were wrong). All 43 such places (36 on
  ff. 6r-6v, 7 on f. 7r and in letter 1; 71 positions) were restored as holes, and two fresh blind readers looked at
  them and at 10 places where the check's own readers saw a sign the text lacked. A sign was to be added only where
  both new readers agreed: none was, and 8 of the 10 places got one hole each. No position was deleted. At the line
  starts of f. 6v the readers split two against two between faint signs and show-through; holes are the record.
- The texts here are `transcription_<letter>.txt`, in Lasry's sign names, one line per manuscript line; `_` is a hole
  (248 positions in letter 2, 39 in letter 1).

## Tests, in order, with every miss

1. **Letter 1, first blind transcription (sheet cut from Lasry's key image; plan hashed before the readers started).**
   Letter trigrams with no word division: -1.130 log10 per letter, above all 1,000 permuted tables (best -1.354) but at
   the 3.3rd percentile of period Spanish (Zurita samples of the same run lengths; mark: the 5th percentile, -1.126):
   **MISS**, by 0.004. Share of letters in words: 0.304 against a mark of 0.348 set on Lasry's own letter at the same
   share of holes (permuted tables at most 0.149): **MISS**. Cause identified: both readers took Lasry's S sign `7o` for
   the P tile of his key image and his P sign `np` for the Y tile, because the key image draws them misleadingly; a
   decode with those two fixed passes both measures, but that was not planned and is not counted. Additions tested on
   that text: barred sign = o, no result (no agreed occurrence); `dal` = King Ferdinand, no result; `dif` = King of
   France, **MISS** by that plan's rule; `bnm`, no result (absent).
2. **Letter 2, the test on unseen text** (`records/unseen_text_test/`; plan `PLAN_round4.md`, sha256
   c0416ad6447bc3f38ffb7f96228bd5477b9103119c0ae7470b87bd51a76fb17b, hashed with the sign mapping before any reader
   started and before any decode of letter 2; output `tests/tests_output_letter2.txt`). On the two teams' agreed
   positions (2,897 letters, hole share 0.253), Lasry's key unchanged:
   - letter trigrams: **-1.043 log10 per letter**, against a best of -1.336 among 1,000 permuted tables (mean -1.602)
     and a mark of -1.122 (5th percentile of period Spanish, Zurita); it sits above all 1,000 Spanish samples: **PASS**;
   - share of letters in words: **0.338**, against a mark of 0.255 set by rule on Lasry's own letter with holes at the
     same share (5th percentile of 200 draws; median 0.295); permuted tables 99th percentile 0.104, maximum 0.140:
     **PASS**;
   - additions, each tested on letter 2 only: barred u/v sign = o, **MISS** (o makes words at 22 of 33 places and breaks
     11; the rule allowed no break); `dal` = King Ferdinand, **no result** (every context reads as the addressee, and
     "sea [dal] cierta" is feminine); `dif` = King of France, **no result** (one agreed occurrence); `dcf` = King of the
     Romans, **no result** (no agreed `dcf`; both teams write `def`); `bnm`, **no result** (absent).
   - Weak point, found by the independent check: the test script itself (`scripts/tests4.py`) was not hashed, and its
     last change is later than the readers' outputs; nothing shows that a mark changed, and the marks in the plan match
     the script.
3. **Independent check** (`records/independent_check/`; plan `PLAN.md`, sha256
   43047291a45296ff62d7fb9985fad30ffcd4010b2108ffc3b0cb2d15ed27dcd4, hashed before any file of the earlier work was
   opened; `HASHES.txt`). Its own value-free sheet, its signs cut from Lasry's leaf (f. 122r) at his own positions,
   with examples of the same shapes from lines of letter 2 that were not drawn; its own two blind readers; 24 randomly
   drawn lines of letter 2 and 12 of letter 1 from the unprocessed images; reader agreement 71.8% (letter 2) and 93.6%
   (letter 1). Lasry's key unchanged, one run (`test_output.txt`; trigram scores in bits per letter):

   | | Letter 2 (the test) | Letter 1 (secondary) |
   |---|---|---|
   | Positions / letters / hole share | 1,011 / 718 / 0.290 | 401 / 370 / 0.077 |
   | Trigrams, bits per letter | -3.232 | -3.308 |
   | 1,000 permuted tables | max -4.784 (mean -6.078): mark T1 **PASS** | max -4.877: **PASS** |
   | 1,000 period-Spanish samples (Villa, *Memorias*, held out) | 1st pct -4.047, median -3.388: mark T2 **PASS** | 1st pct -4.114, median -3.253: **PASS** |
   | Word share | 0.615 against mark 0.561 (permuted max 0.487): mark W **PASS** | 0.873 against mark 0.863 (permuted max 0.668): **PASS** |

   A defect it reports: on sloping lines five of its 36 lines are two half-lines joined; this does not change any
   mark. Its comparison with the transcription here (`compare_with_round5.tsv`): at its 1,105 agreed positions the
   transcription gives the same letter at 95.5% (letter 2 94.9%, letter 1 96.5%).
4. **Consistency check after the restored holes (not a test).** The trigram and word-share measures of the unseen-text
   test, rerun unchanged on the final texts: letter 2 -0.995 per letter, word share 0.633 against 0.559 at its hole
   share: no warning. **Letter 1: word share 0.629 against its mark of 0.637: a warning.** The likely cause, not settled:
   in letter 1 a plain 7 (Lasry's d) stands several times where Spanish wants s (below); whether the clerk wrote a plain
   7 for s, or the bar of the s-form is lost in the tight, sloping lines, is **open**.

## Reliability, per page

| Page | Two readers agree | Positions closed after a third reader | Independent check: same letter at its agreed positions | Statement |
|---|---|---|---|---|
| f. 6r | 86.9% | 95.4% | 93.4% | usable with errors |
| f. 6v | 78.6% | 92.3% | 93.3% | usable with errors |
| f. 7r | 93.2% | 98.9% | 97.6% | reliable |
| Letter 1 (ff. 2v / 3r) | 91.2% | 97.8% | 96.5% (98.5% / 94.1%) | reliable |

The independent figure is the stronger one, but its agreed positions are the easier ones. On ff. 6r-6v ink shows through
from the reverse; the digital subtraction was used, the originals were kept, and 43 places were restored as holes.

## The readings

For each letter: `decode_<letter>.txt` (mechanical, line by line), `diplomatic_<letter>.txt` (every kind of hole told
apart), `reading_<letter>.md` (the words of the word table, with punctuation added, and line by line),
`translation_en_<letter>.md` (English, made by an AI agent), `words_<letter>.tsv` (one row per cipher word: decode,
reading, read or not, why). The cipher has no word division; the division is ours.

**What they say**, in outline (code groups unread; a word in `[?...]` is not counted read; holes are not filled):

- **10 November 1496.** "y el [dif] [?a enbiado] [?al] [bcd] de san [?Pedro] uincula hazia [?Saona]": the cardinal of
  San Pietro in Vincoli sent towards Savona; "seys mil alemanes pagados y quince mil [?ducados] para dar a algunas
  [?personas] de aqui"; micer Juan Luis de Fiesco (Gian Luigi Fieschi) away from Genoa and suspected; the writer works
  with the legate and the ambassadors of [del] to have the [def] come to [?Alexandria]; French ships come from the west
  to Provence; [dal] knows that the [def] is displeased with the English marriage; "ocho [?barcas] [?vizcaynas] mal
  aderecadas"; the departure of [dal] from [?Girona] was made "sin consultarlo".
- **18 December 1496.** In Genoa "las iustificaciones y tenplancas y cortesias de que se han usado con francia" are
  given other names, though [dal] "gasta mas que [?] [?] por defender lo a [?Genova]", which "seria ya del [dif]"; the
  matter of a carrack; if the French came the writer fears they would carry the city off; the Venetians and the League;
  before the letter was closed the legate wrote that the [def] "se yua a [?Chiavenna], que es un [?lugar] iunto con
  alemanna"; letters from Rome and Naples seized on the road.

**Read share.** The rule: cipher words only; a word is read only if every sign has a value and the decode is the word
itself; each code group is one word and unread; every departure from the decode (a letter supplied or changed by sense,
a doubtful sign) makes the word unread. Measured from the word tables:

| | Main count | without the line-end rule | with the late `S` | with `S`, without the line-end rule |
|---|---|---|---|---|
| f. 6r | **241 / 341 (70.7%)** | 231 (67.7%) | 242 (71.0%) | 232 (68.0%) |
| f. 6v | **231 / 351 (65.8%)** | 226 (64.4%) | 234 (66.7%) | 229 (65.2%) |
| f. 7r | **181 / 241 (75.1%)** | 176 (73.0%) | 181 (75.1%) | 176 (73.0%) |
| **18 Dec 1496** | **653 / 933 (70.0%)** | 633 (67.8%) | 657 (70.4%) | 637 (68.3%) |
| f. 2v | **159 / 234 (67.9%)** | 156 (66.7%) | 161 (68.8%) | 158 (67.5%) |
| f. 3r | **94 / 154 (61.0%)** | 92 (59.7%) | 94 (61.0%) | 92 (59.7%) |
| **10 Nov 1496** | **253 / 388 (65.2%)** | 248 (63.9%) | 255 (65.7%) | 250 (64.4%) |

The main count is the headline. It counts a word that runs over a line end once, and lets it be read when every sign
has a value: README Conventions count holes and reads by words, and a word divided at a line end is one word (nothing
there makes it unread for being divided). "Without the line-end rule" counts every such word unread, as the unseen-text
test did. The late `S` is left out of the headline because it was mapped after decodes had been seen.

**Not counted, though the decode gives them, in letter 1:** words where a plain 7 (Lasry's d) stands where Spanish wants
s: L08 *e?dto* (esto), L09 *e?dta* (esta), L19 *edta* (esta), L20 *edtaria* (estaria), L12 *dtodas* and *dlas* (the d
may be the s of the word before); words where Lasry's `b++` (z), a dotted T crossed from the next line, stands for r or
s: L12 *ciezto* (cierto), L11 *ezta*, *ezto*; R18 *celos* (the independent check's two readers saw a plain 7 for its s);
L24 *certinidad*, read only by sense. In letter 2 the same check finds one: C17 *sodtener* (sostener).

## Code groups (unread)

62 occurrences of 25 groups written in Latin letters (letter 2: 39, letter 1: 23), every one with its context in
`code_groups_contexts.tsv` (with the three of 14 April 1497); **no value is given to any**. Lasry's key lists labels
for some names from no. 95 (`bcd` cardenal, `bac` ciudad, `bon` gente, `dif` "rey de romanos?"); they are not used.
What the contexts suggest, as suggestions only:
- `dal` (14 times) stands where the addressee fits: "sea [dal] cierta", with a feminine, as "Vuestra Alteza" would take.
- `def` (10 times) stands where Maximilian, King of the Romans, fits: "el [def] se yva a Chiavenna ... junto con
  Alemanna".
- `dif` (3 times) stands where the King of France fits ("el [dif] ha enviado al [bcd] de San Pedro ad Vincula hazia
  Saona"; Genoa "sería ya del [dif]"), not where Lasry's "rey de romanos?" would.

## Outside checks (not tests)

Five statements of the readings were compared with Marino Sanuto's *Diarii*, vol. I, and Zurita's *Historia del rey
don Hernando* (1580). All five are consistent; none is a test, and none was used to choose a reading.
1. Letter 2, "el legado ... [def] se yva a Chiavenna ... junto con Alemanna": Zurita III xxxvii (Maximilian raised the
   siege of Livorno, went back to Pisa on 22 November 1496 and crossed the Apennines to join the legate, the Cardinal of
   Santa Cruz); Sanuto I (December 1496: the King of the Romans went by the Valtellina meaning to go to Chiavenna).
2. Letter 1, "la yda de [dal] de Girona": Sanuto I (September 1496: a letter from Spain says the king had arrived at
   Gerona).
3. Letter 1, the Cardinal of San Pietro in Vincoli towards Savona: Sanuto I (December 1496, from Genoa: the Cardinal of
   San Pietro in Vincoli and Battistino Fregoso coming against Genoa; troops wanted for Genoa and Savona).
4. Letter 2, "so color de tregua": Zurita III xxxvi-xxxvii (the truce Don Enrique Enríquez made with the French in
   Roussillon after Salses).
5. Letter 1, "barcas vizcaynas mal aderecadas": Sanuto I (August-September 1496: ships of Genoese, Biscayans and
   Spaniards badly fitted out); Sanuto's entry is earlier than the letter.

## Prior work

**None found.** Searched: the library's record (no edition or bibliography); Galende Díaz, "La escritura cifrada durante
el reinado de los Reyes Católicos y Carlos V" (*Cuadernos de Estudios Medievales* 18-19, 1994): Juan Manuel's two
private ciphers (BRAH 9/15), not this system, and no Genoa letter; C. Villanueva Morte and Á. Fernández de Córdova
Miralles, *El embajador Claver* (CSIC 2025): never cites MSS/20212/61; six Internet Archive full-text searches for the
shelfmark and distinctive phrases: nothing; DECODE: no record; this repository: no earlier transcription or decode of
the volume. A Google Books search returned no data.
**Not seen:** L. Suárez Fernández, *Política internacional de Isabel la Católica*, vols. IV-V (not online; it drew on
the Biblioteca Nacional, so a print of these letters cannot be ruled out); Galende Díaz, *Criptografía* (1995); the full
catalogue record at catalogo.bne.es; any copy or decipherment at Simancas or the RAH; Sanuto beyond vol. I.

Contamination: no reading of these letters existed anywhere we could find, before or during the work.

## What was not checked

- **No person has checked any transcription, reading or translation.** All readers were AI agents, working blind to
  the key; the readings and the English are an AI agent's.
- The clear pages of both letters, and the clear ending of letter 2, were not transcribed.
- The mapping of rows W39-W49 to Lasry's signs was not made blind; W41 against W42 (Lasry's `a_` and `ee`) rests on a
  faint bar that cannot be told occurrence by occurrence at this resolution.
- Two shapes reported by the readers have no row and stay holes: two small o's joined by a level stroke, and a 3 with a
  small loop below.
- Suárez Fernández IV-V and Galende Díaz 1995 (above).

## Catalogue notes for the maintainers

This folder edits neither `catalogue.json` nor `research/leads.json`.

- **Row 1270 covers seven letters**, not listed one by one in the row. From the library's viewer (the letters' own
  dates; what the pages seen show):

  | Letter | Date and place | To | Cipher |
  |---|---|---|---|
  | 1 | Genoa, 10 Nov 1496 | the Catholic Monarchs | yes, ff. 2v-3r, Lasry's no. 95 system: this target |
  | 2 | Genoa, 18 Dec 1496 | the Catholic Monarchs | yes, ff. 6r-7r, Lasry's no. 95 system: this target |
  | 3 | Rome, 21 Jan 1521 (pencil note: 16) | Charles V | none on the pages seen |
  | 4 | Rome, 12 May 1520 (pencil note "S.l.") | Charles V | none on the pages seen |
  | 5 | Rome, 13 Aug 1521 | Charles V | almost all, another system (Latin-letter syllable groups with signs); not tested |
  | 6 | Genoa, 24 Nov 1522 | Charles V | none on the pages seen |
  | 7 | no date on the pages seen | (presumably Juan Manuel) | all, a third system |

- Row 1270's "1497 letter duplicates catalogue 1014" is a slip: 1014 is Dr Walles's letter of 1663 (TNA SP 29), and none
  of the seven letters is dated 1497. Catalogue 1049 (RAH Salazar N-23 f. 36, Rome 23 June 1497) is another letter, not a
  duplicate.
- Row 1270's "Tomokiyo covers the 1521-22 letters" is not right for these: his page covers the RAH letters (BRAH
  9/23-24), not MSS/20212/61.
- Rows 2854-2857 give the repository as `bne`, but those four letters are in the Archivo Histórico Provincial de
  Zaragoza (Colección Zurita).
- Row 2857 (Juan Manuel, Genoa, 14 April 1497) is now deciphered in part with the same key: target `juanmanuel1497`.

## Remaining gaps

- code groups in Latin letters, 62 occurrences of 25 groups (dal 14, def 10, dif 3, del 3, gal 3 and others) - blocker: open-codes; none in Lasry's list with a sure value, and the proposed values (dal, dif, dcf, bnm) gave no result on unseen text; contexts in code_groups_contexts.tsv
- barred u/v sign <W26>, 50 places in letter 2 and 41 in letter 1 - blocker: no-key-material; not in Lasry's table; o missed its planned test on letter 2 (22 makes, 11 breaks), and the places are not one shape (plain, with a dot above, a pi-like form); no further unseen text in this cipher is known
- the S-shaped stroke (S), 10 places - blocker: no-key-material; matched to Lasry's S only after decodes had been seen, so not counted; no unseen text in this cipher is left to test it on
- Lasry's 9 (2 places), the eight <W27> (2), the 6 or G shape <W48> (5), the # shape <W49> (4) - blocker: no-key-material; no value in Lasry's table (his own 9 is "[y?]")
- holes, 248 positions in letter 2 and 39 in letter 1 - blocker: illegible; show-through on ff. 6r-6v, strokes from neighbouring lines, damage in B31-B34; readers of the library's largest images do not agree
- letter 1's d-for-s and z-for-r words (L08, L09, L11 twice, L12 three times, L19, L20, R18) and C17 sodtener - blocker: needs-physical-access; only the original or a sharper image can show whether the bar or o of the s-form is there
- words read only by sense or with a doubtful sign (77 words "letter changed by sense", 126 "not understood" in the word tables) - blocker: illegible; each turns on a sign that the library's largest image does not settle
- the two shapes with no sheet row (joined o's; a 3 with a loop) - blocker: no-key-material; not in Lasry's table

## Escalation

- [x] siblings: both cipher letters of BNE MSS/20212/61 transcribed blind; letters 3-7 of the volume checked (clear, or two other systems); the 14 April 1497 letter in this key is ../juanmanuel1497; Lasry's no. 95 compared sign by sign; catalogue 1049 (RAH, Rome 23 June 1497) is not digitised and was not seen
- [x] clear-pages: no decipherment of the time on any leaf; the clear pages were not transcribed
- [x] known-keys: Lasry's no. 95 key applied unchanged and tested on unseen text; Juan Manuel's two private ciphers printed by Galende Díaz (BRAH 9/15) are other systems
- [x] print: library record, Galende Díaz 1994, the 2025 Claver book, six Internet Archive full-text searches, DECODE, this repository: nothing; Suárez Fernández IV-V and Galende Díaz 1995 not seen
- [n/a] key-rebuild: by design the key is applied unchanged; each proposed addition (barred sign, dal, dif, dcf, bnm) was tested on unseen text and missed or gave no result, and no further unseen text in this cipher is known
- [x] retry: every open stretch re-read by fresh blind readers (two, then a third where they differed); the 43 deletions restored and re-read; the d-for-s words checked by the independent check's readers on the unprocessed images

## Files

- `transcription_10nov1496.txt`, `transcription_18dec1496.txt`: Lasry's sign names, one line per manuscript line.
- `decode.py`: reads Lasry's `key.txt` from `../esp318no95/` (hash checked) and writes `decode_<letter>.txt` and
  `decode_<letter>_with_S.txt`. Standard library, deterministic.
- `diplomatic_<letter>.txt`, `reading_<letter>.md`, `translation_en_<letter>.md`, `words_<letter>.tsv`,
  `code_groups_contexts.tsv`.
- `records/unseen_text_test/`: the test on letter 2, kept unchanged: plan and hash file, the hidden sign mapping, the
  reader instructions, the crop manifest, the eight readers' transcriptions (hashed on arrival, `HASHES_helpers.txt`),
  the agreed texts, the test script and its outputs.
- `records/independent_check/`: kept unchanged: plan, `HASHES.txt`, the draw, its hidden sheet mapping, the reader
  instructions, both readers' transcriptions, the agreement, the test output, the comparison and the three samples;
  `scripts/align.py`. Its test script is not included because it names an absolute path of the machine it ran on:
  `scripts/tests.py.sha256.txt` gives its sha256 (also in `HASHES.txt`).
- `records/sheet_mapping_v2.tsv`: the mapping of all 49 sheet rows to Lasry's names, unchanged.
- The records name files by the paths of the folders they were made in, and two plans name the model that ran the
  readers. The sign-sheet images, the line images and the page images are not included (hashes in the records).

## Credits

- George Lasry: the key (his CTTS key for BnF Espagnol 318 no. 95, his target `esp318no95`).
- Andrew Beling, with AI agents: the match of these letters to Lasry's key, the transcriptions, the tests and the
  reading.

## Review status, 17 November 2026

Both 1496 documents are marked decoded, not read, pending an independent reading review. No reading_review has been invented; the sure-word counts remain as reported.

AI agents did this work; no person has checked it.

## 23-24 Nov 2026 - two blind sign-shape sheets and the <W26> = 77 merge (Brice Dudout, with Claude), `dudout/sign_check_2026-11/`

A reviewer's pass. Andrew Beling's files and figures above are unchanged, and Lasry's key is unchanged with no value
added. No image is committed.

- **Sheet 2311 (controls 3/3).** 5 words read: pero, posible; aqui, remedio, Proencia.
- **Sheet 2411b (controls 3/3).** Three <W26> seen as the 77 form give comendador, con and lo.
- **Counts.** 18 Dec 653 -> 658 of 933; 10 Nov 253 -> 256 of 388; both 906 -> 914 of 1,321.
- **The <W26> -> 77 (o) merge.** The reviewer remarked that <W26> and 77 are one sign written two ways, and the six
  places of sheet 2411b show a continuum of shapes. The merge was adopted as a variant:
  - no read word breaks, and 42 words become read (18 Dec 685, 73.4%; 10 Nov 271, 69.8%; both 956 of 1,321);
  - all 42 are **{probable}**, because the identification was made after the decodes had been seen, like the S;
  - in 7 places the sense does not want o (A23, C09; L08, L09, L12, R04, R10), so they need a look first.
- The new figures are left to the target's author and the reviewer to adopt.
