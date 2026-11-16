# Decrypt audit, 16 Nov 2026: does the published reading follow from the key and the transcription?

Kind: audit of our own results. Area: every target whose key was recovered here.

## Why

C. Pierrot and C. Desenclos (The Conversation, 10 Nov 2026) showed on `memoire1560` that the letters the key gives
and the letters of the published reading differed without the page saying so. `targets/memoire1560/` was checked
by hand and corrected (its NOTES, "Audit against the mechanical decrypt"): 362 of 1,709 words departed from the
decrypt and 108 had been marked. The 7 Nov 2026 review of all pages compared pages with their notes; it did not
re-apply any key. This audit asks the same question of every target with a recovered key.

## What `audit.py` does

For each of the 344 targets whose `outcome.method` starts "key recovered" (938 entries of `outcome.texts`):
it parses the key file named in the profile, applies it to the transcription with nothing edited, and aligns the
letters of that mechanical decrypt with the letters of the published text (the reading file, else the decryption
file). Case, accents, u/v and i/j/y are folded. The alignment is anchored on runs of 8 letters common to both, and
only the short gaps between anchors are compared, so headers, notes and clear passages in the published file are
left out. A word of the published text "departs" when it holds a letter outside [ ] that the decrypt does not give.
Key column order and tokenisation are chosen to reproduce the published text as well as possible, the choice most
favourable to the reading. It reads files only. Run `python research/decrypt_audit/audit.py` (needs `rapidfuzz`);
`results.tsv` has one row per text, `results.json` the totals.

## Result

Two passes. The script (`audit.py`) flagged 55 targets on 16 Nov 2026. Each of the other 54 was then opened by a
checker working from `TARGET_BRIEF.md`, who re-applied the key with the target's own conventions, compared the
result with the reading and recorded the cause in the target's `NOTES.md` ("Decrypt audit, 16 Nov 2026") and
`profile.json`. Their reports are in `targets/<folder>.json`. `memoire1560` was done first and separately.

### What the checkers found (54 targets)

- **The script's flags were mostly its own artefacts.** It dropped a sign named `#` or `=`, read line labels
  ("L07:", "M16") as signs or letters, did not strip doubt marks from tokens, could not apply pair or context
  rules, and counted clear text printed around the cipher as text the key failed to give. It also knew only
  square brackets as a mark. Those faults are corrected in the script where a general rule exists (see below).
- **35 of the 54 targets do have words that depart from the key with no mark in the published reading:
  about 918 words in all,** by the checkers' counts (some by hand, some by alignment; none against the images).
  In most it is a handful of words. It is large in 7: kauderbach1754, branicki1757, santacruz1630, lopehurtado1520, bonde1676, martinique1778, mendoza1549.
  None is a second `memoire1560`: no other target was found with signs merged in the transcription, and where
  the checkers rebuilt the decrypt it matched the target's own decryption file.
- **15 targets had key values that stood only in a script, in NOTES or in another file.** They are now in a
  key file listed in the profile, each with its source; no value was added from what a reading "needs", and no
  frozen key was altered.
- **Several published "readings" are not the output of the key at all**: the register's clear copies
  (`affry1757`), the contemporary gloss (`hopken1740` first despatch), the contemporary clears (`duben1764`),
  the archive's clear copies (`deboli1789`, twelve texts), Jefferson's sheets and the editors' text
  (`jefferson1787`). Each file says so in its header; the profile's "decryption" slot does not.
- **In `kaa4591b` the transcription of one letter (R9403) was generated from the reading**, so its agreement with
  the key shows nothing. Recorded in its NOTES; not yet resolved.
- **32 write-up pages carry a statement these findings make false** (66 statements, quoted in the reports), such as
  "letters as the key gives them" or "spelling of the letter kept". Not yet corrected.
- No reading, decryption or translation file was changed in this pass. Marking the unmarked words is the next step.

| target | unmarked words | causes found | key values moved into a key file | false page statements | the unmarked changes, or the main cause |
|---|---|---|---|---|---|
| kauderbach1754 | 240 | key file incomplete, unmarked change, normalised spelling, files out of step, audit artefact |  | 5 | Letters changed in the hand readings without a mark: about 240 of 2,044 words in the nine letters that read (garbled groups and look-alike figures of the transcription, e.g. 41 for 71, 09 for 69, 14 for 44, put right in the … |
| branicki1757 | 165 | key file incomplete, unmarked change, normalised spelling, clear text or other material, audit artefact | 5 | 3 | Letters corrected in the readings without a mark, about 165 words (own count: 1398 about 130 of 561 words, 1399 about 19 of 863, 1400 about 8 of 469, 446 about 7 of 354). Only reading_1398.md declares it in its header ('the … |
| santacruz1630 | 141 | key file incomplete, unmarked change, normalised spelling, clear text or other material | 5 | 2 | within the 141, not separated one by one: abbreviations expanded unmarked ('mi s r s' > ministros x3), final letters supplied (copia>copias, veni>venir), decrypted letters left out ('se os ‹fri› z e' printed 'se os ‹fri›') |
| lopehurtado1520 | 59 | key file incomplete, unmarked change, normalised spelling, clear text or other material, files out of step, audit artefact |  | 3 | about 59 words of the decryption.txt line readings print a letter no value of the sign gives, unmarked (cota>cosa, con>como, sedores>señores); 39 places where 63 transcribed signs are left out of the reading (2 marked) |
| bonde1676 | 36 | key file incomplete, unmarked change, normalised spelling, clear text or other material, audit artefact | 1 |  | memorial, nine held-out pages: 5 words with one unbracketed letter key v3 does not give (all class-E units, no count affected). Memorial, image 324: 31 of 145 cipher words (39 letters) against the v3 decode, 65 words (96 … |
| martinique1778 | 35 | key file incomplete, unmarked change, normalised spelling, clear text or other material, audit artefact |  | 2 | about 35 places in f. 19 (3), f. 70 (8), f. 114 (about 24), hand count: unvalued groups filled without brackets, valued syllables replaced, words supplied or dropped |
| mendoza1549 | 28 | unmarked change, audit artefact |  |  | 28 words (38 sign places) of reading_44r.md print a repaired value with no mark in that file; all 38 are marked in the companion reading_44r_marked.md ({x/y}, {-x}), which with marks resolved gives the same letters as … |
| jefferson1787 | 19 | key file incomplete, unmarked change, normalised spelling, clear text or other material, audit artefact |  | 3 | 19 groups graded H (16 words) print the editors' word where Jefferson's interlinear gives another, no bracket in the reading files; 13 more groups print Jefferson's own correction written under the group, unmarked |
| hopken1740 | 18 | unmarked change, normalised spelling, clear text or other material, audit artefact |  | 2 | none in the sense of an undocumented change; but reading_khan1742.md prints 18 repaired words (21 changed values) with no mark in the text, the marks being only in marked_khan1742.txt (7 explained in about_reading_khan1742.txt) |
| geleen1633 | 17 | unmarked change, normalised spelling, clear text or other material, audit artefact |  | 2 | 17 cipher words printed as certain with no mark whose letters are not the key's: 11 change or supply a letter (6 read l where the transcription has 15 = u/v; tausent, mit, starck, solche; desto over an illegible pair), 13 of … |
| joachim1530 | 14 | unmarked change, clear text or other material, audit artefact |  | 1 | 13 position-specific emendations (listed in key.json 'emendations' and reading_tokens.tsv) printed without brackets in clair331_reading.md, plus 'partite' for 'parutite' stated in the header only; 14 letters in 14 words |
| montauti1692 | 14 | unmarked change, normalised spelling, clear text or other material, audit artefact |  |  | 14 places in the *_it.txt reading files with a letter changed, dropped or supplied and no bracket (P1: GRIMANI, D'ACCASARE, SÌ IN, POLONIA, LIEGI x2, LE S[UE] NOZZE with code [22] dropped, L'AUGUSTISSIMA CASA E; P2: … |
| swieten1759 | 14 | key file incomplete, unmarked change, clear text or other material, audit artefact |  | 2 | R956: 12 places inside the cipher runs differ from the decrypt with no mark; R957: 2 words (les, beaucoups) follow the contemporary decipherment against the figures, plus 'supposition' which is documented in the Notes but not … |
| longlee1590 | 12 | key file incomplete, unmarked change, normalised spelling, clear text or other material, audit artefact | 7 |  | 12 places in words printed as certain (no braces): 4 letters changed, 1 added, 7 left out; 8 of 335 unbracketed words by the audit's own count on decryption.txt in page order |
| ridolfi1646 | 12 | unmarked change, clear text or other material, files out of step, audit artefact |  | 2 | 12 words printed as certain and unbracketed where the decrypt of the published transcription gives another letter; all 12 are listed in reading.md's table 'Corrections confirmed on the images' (digits confirmed at the blind … |
| r1862 | 11 | unmarked change, clear text or other material, audit artefact |  | 1 | 11 places where tx/R1862_reading.md changes a letter of tx/plain.txt with no mark (9 words with a letter/syllable added, 1 letter dropped, 1 moved into a clear passage), against the reading header 'Letters as the decipherment … |
| riva1722 | 11 | unmarked change, normalised spelling, clear text or other material, files out of step, audit artefact |  | 2 | 11 words in units marked S (counted read) with a letter changed or supplied and no bracket: impegnar- for IN-pe (3), porterebbe/riporterebbe for po-r-ta-re-be (3), sofferti and dalli (8 Aug 35r.L11), mandargliele and onorari … |
| jqa | 9 | key file incomplete, unmarked change, normalised spelling, clear text or other material, files out of step | 1 | 2 | 8 words unbracketed and unexplained in the folder: second 'it' (gap l.4), events, all, affairs (gap l.9-10), disclosed (rem l.1), system (rem l.3, sy-em), proposition (rem l.4, pro-po-si for), making to (rem l.12, 611 500 = … |
| lopehurtado1523 | 9 | key file incomplete, unmarked change, normalised spelling, clear text or other material, files out of step, audit artefact | 7 | 3 | R9867: 9 words changed with no mark and no row in R9867_corrections.tsv (5 are r>a/ha, the ʇʇ/ß look-alike); R9866: at least 1 seen (vencidos), not counted |
| stade1710 | 9 | key file incomplete, unmarked change, normalised spelling, clear text or other material | 8 | 2 | 9 words with a letter supplied or changed and no mark (herrorna x2 for ro-ra, Stater for sta-t-ä-r, fiendteligheter, uti, kommas, heelt, Ministri, wårt x2 for w-ä-r-t counted as 2); 4 clear words of the Rådet copy printed … |
| cattanei1430 | 6 | unmarked change, normalised spelling, audit artefact |  | 3 | 6 words in texts/R1854-P4_reading.md: Sollicitabo (decrypt solicitabo), offerendum (offerenuum), dominus (domicus; NOTES 5 Oct records c for n, reading_p4.md keeps [domicus]), male[c]ontentus (n not covered by the bracket), … |
| jablonski1705 | 6 | key file incomplete, unmarked change, normalised spelling, clear text or other material, audit artefact | 1 | 2 | 2 words follow the draft's Latin with no italics: 'Dn.' (no group stands for it) and 'Gallos' (232.46 decodes 'galliam'); also 'ita' printed plain where the decode has 'ita?' (doubtful group), and the 3 Caesar words are not … |
| deboli1789 | 5 | key file incomplete, unmarked change, normalised spelling, clear text or other material, audit artefact |  | 1 | c024 worded reading only: 5 places with letters supplied or changed without a mark (odprawie, iest, powiedzieć, przyszło że się, a doubled 'na') |
| dole1636 | 5 | unmarked change, normalised spelling, clear text or other material, files out of step, audit artefact |  | 1 | 4 words with a letter changed or added and no mark: pourez x2 (decrypt poures), soyez (soyes), affaires (afaires); plus R1 'pour' printed certain on a number transcribed as doubtful 15(1.5) |
| portstemarie1729 | 5 | unmarked change, normalised spelling, audit artefact |  | 1 | 4 glossed words emended without a mark (adresse for ad-ri-ser, [?fe]rez for ri, sçavoir for sçavoi, Mandez for man-des) plus the syllable 'se' of group 1019 dropped before [?maine]s (not seen by the script) |
| baner1640 | 3 | key file incomplete, unmarked change, clear text or other material, files out of step | 5 | 3 | 3 words in APUG568-239_reading.md, whose header says 'no letter changed': 'die in' (decrypt dein), 'Schlesien' (decrypt schlesiei), 'Marche' (decrypt arche) |
| exiles1736 | 3 | key file incomplete, unmarked change, normalised spelling, clear text or other material, audit artefact | 7 |  | 3 letter changes with no mark and no convention (repplika>replika, wo>W., z>ze), plus case endings supplied without mark on 9 of the 16 code names (Stanisława x5, Stanisławem, Augusta, Warszawy, Warszawie) |
| kaa4591b | 3 | key file incomplete, unmarked change, normalised spelling, files out of step, audit artefact | 3 | 3 | R9322: 1 unmarked emendation (signs 'principis', reading 'princeps'). |
| genes1643 | 2 | key file incomplete, unmarked change, normalised spelling, clear text or other material, audit artefact | 8 | 3 | 2 words: 'mandar' where the key gives 'ma n al r' (52 al for 57 da), 'negocio' where it gives 'gocio' (lic); not bracketed, both inside the 115 words counted certain |
| noailles1558 | 2 | unmarked change, normalised spelling, clear text or other material, audit artefact |  | 2 | 2 words: C5 'ritailles' (decode r-i-t-a-i-l-e-s, one l) and C3 'viennent' (decode v-u-i-e-n-n-e-n-t, W = u dropped); the second is invisible to the audit (letter only in the decrypt) |
| batavia1800 | 1 | unmarked change, normalised spelling, clear text or other material |  | 1 | 1 word: ver[ste]rking; the key gives verking, four letters are missing (s, t, e, r), three are bracketed, one r is outside the brackets |
| dahku1715 | 1 | key file incomplete, unmarked change, normalised spelling, clear text or other material, audit artefact |  |  | 1 clear word (not cipher): d11 '=potewaz' in transcription.txt/decryption.txt, 'ponieważ' in reading.md (table and running text), unmarked |
| malen1615 | 1 | clear text or other material, audit artefact |  |  | None |
| potocka1714 | 1 | unmarked change, normalised spelling, clear text or other material, audit artefact |  | 2 | 1 word: R7530 ⟦u venir⟧ where the key gives uenir (5 figures, 6 letters printed), no mark |
| toledo1479 | 1 | unmarked change, normalised spelling, clear text or other material, files out of step, audit artefact |  |  | 1 letter: L24 'El legato che c'era' from elegatochecera (second l has no sign, no mark); same in decryption.txt reading column |
| affry1757 | 0 | key file incomplete, clear text or other material, files out of step, audit artefact | 1 | 3 | key layered over three places, profile named two: key_X.tsv over key_M.json over H/M rows of read/R*_new.tsv (as measure_sense.py applies them); in R1072/R1074/R2067 59/41/36 groups take their value from key_X.tsv and 17/31/21 … |
| andreae1616 | 0 | clear text or other material |  | 1 | all 8 flagged words: 'Venus' and 'hohen' are printed in clear over the cipher line on p. 95 (not enciphered, stated in ciphertext.txt and the reading header), and the label 'p. 97, the tablet behind Venus's bed:' sits inside … |
| buda1490 | 0 | key file incomplete, normalised spelling, clear text or other material, audit artefact | 4 | 1 | 9 units in 11 read words used values held only in measure.py lines 39-40 (qA = i x4, t x3; y = ducenta milia / ducentorum milium x2), absent from key.json and key.md; the token-to-unit rules (oH, Ho, nq, ni, LL, Ga, Gp, ve, … |
| burr1804 | 0 | clear text or other material, audit artefact |  | 1 | clear words in quotation marks between the cipher words (made of more; The advice comes with double force; The; being about 20,000; To; To) are in the reading and not produced by the key: 4 of the 5 gaps |
| carranza1914 | 0 | clear text or other material, audit artefact |  |  | all 7 departing words: the audit skips the '>' lines of the reading file (the reading proper) and compares the 'Coded runs' section, taking the run labels C02 to C08 for text; each label gives one letter c |
| delcarretto1576 | 0 | audit artefact | 4 |  | all 17 unmarked gaps: 15 from tokenisation (key.tsv names the transcription groups oPo/oP/oPo./oP. as tokens 1/2/3; the script applied o=i, P=l sign by sign, giving il/ili for o/u), 2 from line labels (L of 'L06:' taken as … |
| duben1764 | 0 | key file incomplete, clear text or other material, files out of step, audit artefact |  |  | key c04 is partial as recorded, not repairable from the folder: 18 of 44 gaps (5 Oct) and 2 of 19 (31 Dec) touch a group with no value (644, 180, 36, 734, 333 x3, 145, 209, 635, 566 x2, 397, 349, 728, 562, 552, 413, 438; 481 … |
| edmondes1594 | 0 | clear text or other material, audit artefact |  |  | transcription/calendar_entry.txt is the whole printed entry, about nine tenths clear English; the 280 departing words are all clear-text words |
| ercole1544 | 0 | clear text or other material, files out of step, audit artefact |  |  | unread markers [...], unidentified codes [L^30] and [?word] proposals in the two readings stand where the decrypt has signs (the long sample gaps) |
| friedrichwilhelm1655 | 0 | normalised spelling, clear text or other material, audit artefact |  |  | stated convention: 3.3 decrypts 'uu', readings write 'w' (head of each reading file) |
| gonzalez1913 | 0 | clear text or other material, audit artefact |  |  | All 12. The reading file has no '## Reading' heading, so the audit takes the whole file and reads the run labels M01..M16 of its 'Coded runs' section as a letter m before each run. Key value 59=m is present and used. |
| rakoczi1632 | 0 | normalised spelling, clear text or other material, audit artefact |  |  | 3 words: u after q not written (quo, requisiverint, substantiasque), stated in NOTES System |
| rinaldo1697 | 0 | audit artefact |  |  | 5 of 6 unmarked gaps: the script does not strip line labels V01-V17 and folds v to u, so each 73v label in the reading counts as a u absent from the decrypt; the 6th gap is the marked {+c} of spi{+c}chi. The key has 6 = u and … |
| rucellai1482 | 0 | clear text or other material, audit artefact |  | 1 | ‹unresolved› stretches copied from the raw decoding and [che] for '?' in the card; ‹ › is not a bracket for the audit |
| schoenberg1665 | 0 | normalised spelling, audit artefact |  |  | umlauts printed in 4 words (Churfürst, möchte, behü{ten}, darüber) though the 24-letter key has none; convention not stated; image not checked |
| stmauris1548 | 0 | key file incomplete, audit artefact |  |  | profile named only key.tsv; the 2 Aug reading is marked against key_frozen.tsv (already in the folder). No sign value missing from either key file. |
| testi1630 | 0 | clear text or other material, audit artefact |  |  | clear words inside cipher lines ({..} in the transcription, italics in the reading) counted as reading-only, about 4 gaps (e.g. 'Sin dal principio', 'Supponiamo che') |
| vanhalen1840 | 0 | normalised spelling, clear text or other material, audit artefact |  |  | u printed as v in ve[n]ir |
| vittoria1686 | 0 | normalised spelling, clear text or other material, files out of step, audit artefact |  |  | main cause: clear words of the letters ('nessun modo', 'Il Sig.or Marchese di Casale Nuovo', 'Per amor di Dio ci compatisca ...'), [ ] in the transcription, outside << >> in edit_numbers.txt |

### The marking round (same day)

Each checker went back to its own targets under `TARGET_BRIEF2.md`: marks and header lines only, no wording
change. Every changed reading file was then compared with its previous state letter by letter (marks, case and
punctuation set aside): the only lines whose letters differ are header lines and the page sentences listed in the
reports. Reports: `targets_marked/<folder>.json`.

- **858 places are now marked in 31 targets**, in each file's own convention. The two large estimates were
  replaced by exact counts from scripts kept in the folders: `kauderbach1754` 211 places in 202 of 2,044 words
  (estimate: about 240); `branicki1757` 168 places in 150 of 2,247 words.
- **A contributor's reading is not marked inside.** For `branicki1757`, `lopehurtado1520` and `santacruz1630`
  the marks are in a companion `*_marked.md` file and the reading stays as given; for `noailles1558`,
  `longlee1590` and `stade1710` the departures are listed in the header or NOTES.
- **A text from another source is labelled, not marked**: the register copies (`affry1757`, where 142 places
  differ from the figures), the contemporary gloss or clears (`hopken1740`, `duben1764` in NOTES because its
  files are hash-frozen, `deboli1789`), Jefferson's sheets and the editors' text (`jefferson1787`).
- **Not marked, and why:** a letter the reading drops cannot carry a bracket (listed in each NOTES, about 60
  places, 37 of them in `lopehurtado1520`); `bonde1676` image 324 (31 words, declared in its header);
  `kauderbach1754` R1954 (37 words, no machine decrypt for its transcription); spelling conventions, now stated in
  the headers.
- **Counting a mark as a hole, as the read bar does, these texts classed "read" now measure over 5% holes:**
  `kauderbach1754` (all seven letters classed read, 5% to 20%), `santacruz1630` (11.5%, marked copy),
  `lopehurtado1520` (8.4%, marked copy), `branicki1757` letter 1398 (18.3%, marked copy), `swieten1759` R956
  (9.6% on a file that also holds other text), `jqa` nine lines of No. 88 (8.8%), `r1862` (7.0%), and
  `deboli1789` c024 by words. **No state, class or read share was changed.** Most of these marks are single
  letters; whether a one-letter mark should weigh as a whole unread word is a question for the read bar itself.
- **Pages:** the false statements were corrected on the pages concerned. Counts that the marks make stale were
  not recomputed (they are listed in the reports under `page_counts_now_stale`: `cattanei1430`, `dole1636`,
  `exiles1736`, `geleen1633`, `genes1643`, `jefferson1787`, `jqa`, `kaa4591b`, `kauderbach1754`,
  `lopehurtado1520`, `r1862`, `riva1722`, `santacruz1630`, `branicki1757`), and statements inside the generated
  "Full texts" blocks follow at the next build. **The page-review ledger was not updated for any of these
  targets**: each page still needs a reader before `--reviewed` is recorded.
- **Generator scripts that would undo marks on a rerun:** `jefferson1787` (`make_reading.py`, `make_texts.py`),
  `montauti1692` (`scripts/make_texts.py`, `scripts/make_bare_texts.py`), `riva1722` (overrides not yet added).

### The script after its corrections

`audit.py` now keeps key rows for signs named `#` or `=`, drops line labels from both files, strips doubt marks
from tokens, reads blockquote lines, and takes `{ }`, `‹ ›`, `⟨ ⟩`, `« »`, `< >` and `word°` as marks. Rerun on all
344 key-recovered targets: 75 have a text it can compare; 14 are at 3% of compared words or under, 18
between 3% and 10%, 43 over 10%. It still cannot apply pair or context rules, polyphonic signs or a layered key,
and it still counts clear text as departing unless the file brackets it, so its figure for a target is an upper
bound and the checkers' counts above are the ones to use.

- **757 of 938 texts, and 269 of 344 targets entirely, could not be checked by the script.** The reasons, by text:
  - 235: key covers N% of the transcription tokens
  - 182: only N% of the decrypt is found in the published text (codes kept as numbers or expanded to words, nulls, another key, or a text edited beyond letter changes)
  - 108: under 100 letters decrypted
  - 91: no key file the script can parse
  - 55: no transcription or no published text listed
  - 35: not prose (key sheet, list or figures)
  - 21: no key_file in the profile
  - 14: under 30 words compared
  - 7: transcription too short to tokenise
  - 6: transcription and published text are the same file
  - 3: a listed file is missing or remote
  For these the question has not been asked at all. The 54 opened by hand suggest what to expect: mostly sound
  key work, with small unmarked repairs in about two readings in three.

## How far to trust the script's figure

Calibration: `memoire1560` scored 29% before any correction. The script's figure rose and fell with things that
are not faults (clear text, labels, marks it did not know), and missed faults a hand count found (`riva1722`:
flagged by an artefact, eleven real unmarked words found by hand). Use it to choose what to open, not to judge.

## What is still to do

- Decide whether a one-letter mark counts as a hole on the read bar; then re-measure the texts listed above and
  reclass those that fall under 95% (README sections, manifest and scoreboard follow the class).
- Recompute the stale counts on the fourteen pages named above, have each page read, and record the reviews.
- Carry the marks into the three generator scripts, or retire them.
- Decide what the profile's "decryption" slot holds where the published text is a clear copy, a gloss or an
  editor's text.
- `kaa4591b`: make a transcription of R9403 that is independent of the reading, or say there is none.
- Open questions the checkers raised and left alone: `santacruz1630` "necesidad" three times where the key gives
  "e ma ne ra" (perhaps "de manera"), and `‹fri›` = di; `kauderbach1754` code 49 (sa in the key, "per" in the
  readings) and code 13; `dahku1715` potewaz / ponieważ; `jqa` word endings that may be marks on the film;
  `duben1764` four values suggested by the clears.
- None of this was checked against images. The targets the script cannot compare (about 270) have not been asked
  the question at all.
- The profile field `outcome.texts[].decryption` is described as "the deciphered text"; nothing requires it to be
  the unedited output of the key. A rule that it must be, with every departure in the reading marked, would let a
  checker enforce this for new targets. That is a change to README Conventions and the schema and has not been made.
