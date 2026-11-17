# Vetting, ajbeling (17 Nov 2026)

Run by Andrew Beling (GitHub ajbeling) with AI agents, from his own computer and network. One catalogue entry, 1001.
This is a correction, not a new result. No person has checked any reading below. Before starting, pull requests and
issues were searched for Guaras, Guerras and 1001 (17 Nov 2026): none.

## Lead

- **1001** Antonio de Guaras, London, 14 June 1574 (TNA SP 70/131 ff. 108-110; CSP Foreign 1572-74 no. 1452):
  `duplicate` of catalogue 303, and its ciphered passage has been in print in plain Spanish since 1888. The block
  supersedes the `open` block of 29 Oct 2026.

Count: duplicate 1.

## What entry 1001 is, and what it should say

The catalogue row reads: title "Declaration of Irish loyalty to the Catholic cause, with the Spanish armada on the
Irish coast; "a considerable portion not deciphered" (CSP Foreign Elizabeth 1572-74)"; correspondents "Irish lords (?)
-> Philip II (?) ; London copy"; language "English"; place "unknown"; and in its vetting block "No Guaras or Requesens
correspondence key held in the repo; none known in print."

The document is Antonio de Guaras's letter from London of 14 June 1574, in Spanish, four pages: f. 108r-v in clear
(English naval preparations under Winter and Hawkins), ff. 109r-110r in cipher (59 lines). The cipher passage is about
Killigrew's mission to have the Regent of Scotland seize the Prince of Scotland (James VI) and send him to England, the Queen's
hostility to the King of France, an offer of service in Ireland from a man who had offered his son as a pledge, and a
Scottish captain's plan, against 400 pounds, to bring his men into Flushing. Ireland appears in it once ("haria grandes
servicios por Irlanda"); there is no declaration by Irish lords. The vetting block of 29 Oct 2026 already noted that
the Irish declaration is the neighbouring calendar item.

**Already in the repository as catalogue 303.** `SOLVED_CATALOGUE.md`, section 4 ("Found already solved by others"):

> **Antonio de Guaras, London** (TNA SP 70 (CSP Foreign x no. 1452); catalogue 303): Read in part at the time (checked
> 22 Sept 2026). CSP Foreign x no. 1452 summarises the deciphered part and says 'a considerable portion not
> deciphered'. ...

Catalogue 303 has no target folder, so this note goes in a vetting folder.

**In print since 1888.** J. Kervyn de Lettenhove, *Relations politiques des Pays-Bas et de l'Angleterre sous le règne
de Philippe II*, vol. VII (Brussels 1888), pp. 176-178, in the footnote to no. MMDCCLVI: "Antonio de Guaras adressait de
Londres, le 14 juin 1574, la lettre suivante à don Pedro Menendez", followed by the clear part and the whole ciphered
passage in plain Spanish, from the words on Killigrew (p. 177) to "Dios le de esfuerço y prospero sucesso!" (p. 178).
The source note on p. 178 reads "(Record office, Cal., n° 1452.)", that is CSP Foreign 1572-74 no. 1452, p. 514, whose
summary ends "A considerable portion not deciphered". Internet Archive `relationspolitiq07nethuoft`:
[p. 177](https://archive.org/details/relationspolitiq07nethuoft/page/177/mode/1up) (scan leaf n208) and p. 178 (leaf
n209). The text layer garbles the source note; the number 1452 was read on the page image of p. 178.

The addressee is don Pedro Menéndez, as Lettenhove prints; the cipher passage addresses him as "Vuestra Excelencia".

## The key

Rebuilt by AI agents from the ciphertext; it is a by-product of identifying the text, not a new reading. One-to-one
substitution, 21 signs; `1001/key.json` gives each pair with its status.

| Cipher | Plain | Status |
|---|---|---|
| d e, f g, h i, m n, o p, q r, s t | e d, g f, i h, n m, p o, r q, t s | neighbour swap (14 pairs, each reciprocal) |
| z | a | forced by the text (a, la, para) |
| c | b | forced (enbiaron, onbre) |
| 6 | c | forced (con, doce) |
| k | l | forced (los, el, facil) |
| x | u | forced (que, aunque) |
| 8 | t | forced (tanbien, parte: the only two sure places, both at a line start). The key frozen for the first test had z here; corrected after the test |
| l | y | not forced: the sign occurs only as l with a raised p, an abbreviation ending (her[man]o, seru[ici]o, neg[oci]o) |

The signs are written as lower-case letters and figures; no image, crop or sign drawing is included (the page images
are licensed). Sign names are those of the transcriptions here.

## Tests, misses first

- **Word-share test: MISSED.** On a blind transcription of 20 random lines, 24 of 76 units (31.6%) decode to Spanish
  words, against a mark of 65% (1,000 permuted tables: median 7.9%, 95th percentile 13.2%). The letter has no word
  spaces, so the units were the chunks between commas, most of them holding several words. That is a flaw in the test
  design, set before the lack of word division was known; it is still a miss.
- **Word-split measure: VOID.** Share of letters covered by the best split into dictionary words: 87.0%, but the
  permuted tables reached a 95th percentile of 44.0%, above the plan's 20% limit, so it counts for nothing.
- **Solver's held-out test: not a clean test.** The first solver scored 70.07% on the held-out third against a mark of
  70%, but that third was scored three times and the plan changed twice in between. It is not offered as evidence.
- **Letter-trigram test without word division: PASS.** On the same 20 blind lines (two readers gave the same sure sign
  at 568 of 599 positions, 94.8%), the key scores -2.194 per letter; all 1,000 permuted tables score lower (best
  -3.339); 1,000 passages of real Spanish of the same run lengths have a 5th percentile of -2.308.
- **Against the print.** `1001/decode_sample.py` (standard library) applies the key to the 20 blind lines and prints
  each beside Lettenhove's words for it. Every legible line gives his words, apart from these letter-level differences:
  three at a sign pair the blind readers confused (z / i: "aonbre" for honbre, line 26, and "nioaauen" for Nio-Haven,
  line 55; c / e: "soldabos" for soldados, line 44), where the first full transcription has the printed letter or
  marks the place doubtful; and three spellings where both transcriptions agree with each other and differ from the
  print ("este" for esta, line 26; "enbiaron" for embiaron, line 2; "diec" for diez, lines 41-42). Line 40 is creased
  and stained and gives only fragments ("q?epara??e???tiran?es??a ar?a...", printed "que para resistir a nuestra
  armada"). "?" is a sign the two blind readers did not agree on.

## Files

- `vetting.json`: the block (verdict `duplicate`).
- `1001/key.json`: the key with the status of each pair.
- `1001/sample_20_lines_blind.txt`: the 20 random lines (`random.Random(1001)`) transcribed blind by two AI readers and
  reconciled mechanically; `?` where they differ; `P` is the sign l with a raised p; `^2` a raised abbreviation mark;
  `|` a comma or dot; `~` a doubtful boundary.
- `1001/transcription_full_ai_reading.txt`: all 59 lines (A01-A31 f. 109r, B01-B28 f. 110r), an AI reading in two
  blind passes reconciled mechanically; `{x|y}` marks the 29 places where the passes differ.
- `1001/lettenhove_1888_sample_lines.tsv`: Lettenhove's printed words for each sample line, copied from the page images.
- `1001/decode_sample.py`: prints decode and print side by side.

## Proposed changes to the catalogue

Not applied here (contributors do not edit `catalogue.json` or `research/leads.json`).

- Close 1001 as a duplicate of 303.
- Record the 1888 print (Kervyn de Lettenhove vol. VII pp. 176-178, from CSP Foreign no. 1452) on both 1001 and the
  303 line in `SOLVED_CATALOGUE.md`: the passage the calendar left undeciphered is printed in full, so 303 is more
  than "read in part at the time".
- If the row is kept anywhere: correspondents "Antonio de Guaras -> don Pedro Menéndez"; language Spanish; place
  London; shelfmark "TNA SP 70/131 ff. 108-110 (CSP Foreign 1572-74 no. 1452, p. 514)"; drop "Irish lords" and the
  Irish-loyalty title, which belong to the neighbouring calendar item.

## Not checked

- The newer *Calendar of State Papers, Scotland* vol. 5 and the *Colección de documentos inéditos* vols. 90-91
  (Guaras's printed letters) were not reached.
- No person has checked the transcriptions, the key, the tests or the match with the print.

## Credits

Kervyn de Lettenhove (1888) for the printed text. Andrew Beling, with AI agents, for the match with catalogue 303 and
the print, and for the rebuilt key.
