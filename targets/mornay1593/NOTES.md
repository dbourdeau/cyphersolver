# Duplessis-Mornay circle: undeciphered figures printed in the 1824 *Mémoires et correspondance*

Status: in progress (1593 figures read with Brice Dudout's key, 27 Oct 2026; Loménie 1595 and Duplessis to Cargroy Jan 1597 read in part with two ten-figure letter keys, 27-28 Nov 2026, Shawn Grening, `grening/`; Duplessis's figures to his wife open; vols. 7-12 searched and two more keys tested, 11-12 Nov 2026, Andrew Beling, `beling/`)

Opened 25 Oct 2026. Found while checking whether Archives nationales 402AP/13 (catalogue 365, "lettres chiffrées"
of the Mornay family) was already in print. It is not, but the printed edition itself carries unread cipher.

## Source

*Mémoires et correspondance de Duplessis-Mornay* (Paris: Treuttel et Würtz, 1824-25), 12 vols. archive.org
`mmoiresetcorre01morn` … `mmoiresetcorre12morn` (vol. 7 text is short in that copy; use `mmoiresetcorresp07morn`).
Page images: `https://archive.org/download/<id>/page/n<leaf>_w1600.jpg`; leaf from `<id>_page_numbers.json`
(vol. 5: printed p. 471 = leaf 480, p. 487 = leaf 496).

Editors' note, vol. 6 p. 82 n. 1: they kept the figures they had a translation for (printed above them) "afin que le
lecteur puisse y recourir pour traduire les chiffres dont nous n'avons pas la clef". So passages printed as bare
figures were unread in 1824.

## Inventory of cipher in the edition

| Vol./letter | Writer → recipient, date | State |
|---|---|---|
| 5, CCI, pp. 471-475 | Du Maurier → Duplessis, "mardi .. juin 1593" (= Tuesday 20 July 1593, Dudout) | bare figures, 6 passages, 72 groups; **read 27 Oct 2026 (Dudout key)** |
| 5, pp. 487-488 | J. de Serviez → Duplessis, 6 Jul 1593 | bare figures, 2 passages, 21 groups, same system; **read 27 Oct 2026** |
| 6, LVI, pp. 82-85 | Catherine de Parthenay (Mme de Rohan) → Mme Duplessis, Paris 30 Jul 1594 | figures printed **with** decipherment above; a ready key (syllabic/homophonic, e.g. 158 = re, 162 = Sa, 49 = n) |
| 6, CVII, pp. 179-181 | Loménie → Duplessis, Paris 24 Feb 1595 | bare figures, different system (many groups x10: 610, 810, 910), plus small numbers as name codes (3, 11, 16, 25, 26, 98, 99); **read in part 27 Nov 2026 (`grening/`, step 9)** |
| 6, CIX | Duplessis → his wife, 1595 | short bare run |
| 7, LXVI-LXVII, CXLI and others | Duplessis, Jan-Oct 1597 | bare figures; **LXVI (to Cargroy, C1-C8) read in part 28 Nov 2026 (`grening/`, step 10)** |
| 8, p. ~507 | Duplessis, 14 Apr 1598 | short run |
| 7, LXXXII p. 169 and CXLI pp. 306-307 | Mme de Rohan → Mme Duplessis, 27 Feb and 4 Aug 1597 | bare figures, 50 groups; Rohan 1594 key fits (11 Nov 2026) |
| 7, pp. 335, 347; 8, pp. 197, 261, 307 | Duplessis → his wife, Sep 1597-Apr 1598 | bare figures, 79 groups, transcribed 11 Nov 2026 |
| 8, pp. 193-306 | Duplessis → his wife, Mar-Apr 1598 | name code 81 63, twelve places (12 Nov 2026) |
| 9, pp. 209-251 | Duplessis → his wife, Jan-Mar 1599 | 153 63, 33, three runs; 30 groups (12 Nov 2026) |
| 9, CLXIX p. 297 | Mme de Rohan → Duplessis, 30 Oct 1599 | 4 groups (12 Nov 2026) |
| 11, CXCII, CXCVII, CC, CCXXXII | Mme de Rohan → Duplessis, Nov 1611-Mar 1612 | 84 groups, another table (12 Nov 2026); CXCVII is dated 19 Nov 1611 by the OCR date line and has a ten-figure run (this row replaces "11, CXCVII, 2 Dec 1611, name codes only") |
| 11, CCXLII | unsigned → Duplessis, 25 Jul 1612 | 9 groups (12 Nov 2026) |

Not yet transcribed: everything after vol. 5. The Rohan 1594 key should be tested on the 1595-98 figures first: same
household, and the editors expected readers to do exactly that. (11-12 Nov 2026: vols. 7-12 searched and their figures
transcribed, `beling/`; steps 7-8.)

## The 1593 system (vols. 5)

`ciphertext.txt` has all eight passages with their clear context. 93 groups, 62 distinct; repeats 149, 912, 129, 2210,
515 (x4). Groups split into two numbers of 2-24 (2210 = 22|10, 1020 = 10|20, 912 = 9|12), and both halves use the same
set of values (1 and 3 never occur in either half).

Context cribs:
- P5 "la maison de [10 groups]": the house of the vicomte de Pont-du-Château, younger brother of the marquis de
  Canilhac (family Beaufort-Montboissier-Canillac). P1 and P5 both open with 192.
- P1 follows "une particularité … que," and precedes "avec les cérémonies et circonstances": the July 1593 conversion
  of Henri IV is the topic of the letter.
- S2 "le roy est [1014 215 17]".

## Steps

1. Literature: no decipherment found (web search, 25 Oct 2026).
2. Hypothesis A, two letters per group: annealed number→letter onto `fr-1600-letters` with a frequency penalty
   (`anneal_pairs.py`). No French in 10 restarts. Failed.

3. Rohan 1594 key built from the printed decipherment (`rohan1594_key.tsv`, 78 values: letters 6-65, syllables
   88-175, words 660-919 with 810 = de and 910 = les, names 10 = le roi, 87 = Paris, 95 = Tours, 96 = Saumur).
4. Transcribed Loménie 24 Feb 1595 (`lomenie1595.txt`, 15 passages) and Duplessis 18-19 Jan 1597 to Cargroy and to
   his wife (`duplessis1597.txt`, 11 passages) from the page images.
5. Applied the Rohan key to both: no French; most groups unvalued, place names fall mid-word. **The key does not
   fit.** Partial sign in Loménie: "du sieur 810 62 110 4" = "du sieur de …", so the x10 word codes (810, 910, 410,
   610) may belong to a shared series even though the letters differ. In the 1597 letter to his wife the editors
   printed some letters among the figures ("e. 77. v. 36. 71. 5", "15. 102. 32. tr. 89 …").

6. **27 Oct 2026: read by Brice Dudout** (email to Daniel; published on Europe chiffrée,
   `bdudout.github.io/europe-chiffree/en/documents.html#mornay-1593`, crediting this folder and hypothesis A).
   Hypothesis A was right (two letters per group); the alphabet is folded: a = 2, c-m on rising odd numbers
   (c 5, d 7, e 9, f 11, g 13, h 15, i 17, l 19, m 21), n-u on falling even numbers (n 22, o 20, p 18, q 16, r 14,
   s 12, t 10, u/v 8), 44 = x/y (probable); 1 and 3 never occur, b unattested. He built it on P1-P5 and S1 and read
   P6 and S2 held out. Key in `key_dudout.tsv`; `apply_dudout.py` applies it to our transcription and writes
   `reading_dudout.txt`: 93/93 groups give letters, three groups split two ways (219 me/al, 213 an/na, 215 ah/mc),
   the sense decides each. Readings:
   - P1 "l'arrest estoit adressé contre le duc de Guise pour le tirer à quatre chevaux"
     (12 Nov 2026: the figures give "estoit ia dressé", already drawn up; see beling/reading_1593.md)
   - P2 "Touraine" (244 = a + x/y: "Tour{ay}ne"); P3 "Montrichart"; P4 "Vautorneuf" (unidentified)
   - P5 "la duchesse d'Angolesme"; P6 "[le] conte de Gramont ne soit de la partie"
   - S1 "le chancelier et Sourdis font l'entreprinse"; S2 "le roy est trahi"
   Differences from his text: our P1 gives "larest" and S1 "lenteprinse" (his "l'arrest", "l'entreprinse").
   Settled 27 Oct 2026 (his second email): no group is missing. The cipher itself gives "larest" (la re st ...) and
   "lenteprinse" (... tl en te pr in se), each with a single r or none; "l'arrest" and "l'entreprinse" on his page
   are the normalised spelling of the established text. He will say so on the page. He also dates Du Maurier's letter Tuesday 20 July 1593 (the
   edition prints "mardi .. juin"; the letter anticipates the abjuration of Sunday 25 July).

7. **11 Nov 2026, Andrew Beling (`beling/`).** Pre-registered (`beling/PREREG.md`), one run, inputs frozen by sha256.
   - Dudout's folded 1593 key on Loménie 1595 and Duplessis Jan 1597 (203 groups): coverage 0.655 against a best of
     0.616 for 200 random number sets (pass needed 0.85 and margin 0.30); language score −3.43 per letter, beating
     193/200 permuted keys, against −2.24 for the 1593 control. Verdict by the rule: inconclusive. The output has no
     words; the key does not fit these letters. Shifting the key numbers by 1-100 gives nothing (best −3.00).
   - Transcribed the rest of the bare figures in vols. 7-8 (`beling/transcription/v7v8_figures.tsv`, context in a
     separate file): Duplessis to his wife Sep 1597-Apr 1598 (15 passages, 79 groups; also not fitted by either key)
     and **two letters of Mme de Rohan to Mme Duplessis**, vol. 7 LXXXII (27 Feb 1597, p. 169) and CXLI
     (4 Aug 1597, pp. 306-307), 19 passages, 50 groups.
   - The Rohan 1594 key on the Rohan 1597 figures: coverage 0.78, −2.26 per letter, beating 197/200 permuted keys.
     Verdict: fits (small sample). Mechanical output "M. de vi l le [672] et de [134] me ni e", "M. de ca r [38] [160] i s",
     "M. de c la s ti l [134] n"; with 672 = roy, 134 = lo, 38 = g, 160 = ro these read M. de Villeroy et de Loménie,
     M. de Cargrois, M. de Chastillon (one sign off: 111 is printed "la" in 1594). The new values are inferences.

8. **11-12 Nov 2026, Andrew Beling (`beling/`, round 2).** Pre-registered (`beling/PREREG_round2.md`), one run.
   - Vols. 9-12 searched (OCR of both scans, then the page images): Duplessis to his wife Jan-Mar 1599 (name code
     153 63, 33 alone, three short runs; 30 groups), **Mme de Rohan to Duplessis** 30 Oct 1599 (vol. 9 CLXIX,
     "M. de 121 174 38 143") and Nov 1611 - Mar 1612 (vol. 11 CXCII, CXCVII, CC, CCXXXII; 84 groups), an unsigned
     letter of 25 Jul 1612 (vol. 11 CCXLII, 9 groups). None in vols. 10 and 12 (OCR search only).
     `beling/transcription/v9v12_figures.tsv`, context in a separate file. The twelve places of 81 63 in vol. 8 are in
     `beling/transcription/v8_namecode.tsv`.
   - The 1594 Rohan key on the new Rohan figures: coverage 0.57, −2.69 per letter, beats 85/200 permuted keys.
     **Does not fit**: by 1611 Mme de Rohan used another table with Duplessis. The four values inferred in step 7: only
     38 recurs ("M. de la vi [38] ne", 1599); extended key beats 130/200 random-value controls, **not supported** (one
     group, almost no power). Rohan 1597 runs R1 and R18 still unread.
   - 1595 Loménie: no clear copy found (archive.org, the 1625 edition, web). Cribs found: the editors' note under the
     letter (vol. 6 p. 181: the affair is the sieur de Camor's plan to seize Mercœur, "Pour la dame de Querveno") and
     the king's cipher letter of the same day printed in clear (vol. 6 CVI). They make "du sieur 810 62 110 4" =
     "du sieur de Camor" and "810 44 109 27 32 10" = "de Bretagne" likely; not a key. Loménie's x10 word codes (23 of
     95 groups) hardly occur in Duplessis's own letters (4 of 239): probably two systems.
   - `beling/transcription/repo/` holds unchanged copies of `lomenie1595.txt`, `duplessis1597.txt` and
     `ciphertext.txt`, frozen by sha256 for the tests.

9. **27 Nov 2026, Shawn Grening (`grening/`), from Beling's two cribs (step 8).** Not pre-registered.
   - With 10 read as one figure, 810 62 110 4 is seven figures for "de Camor" and 810 44 109 27 32 10 is eleven for
     "de Bretaigne" (the king's spelling in CVI). They give a 2, b 4, c 6, d 8, e 10: **one figure 1-10 per letter,
     two letters per group** (810 = d e), and the alphabet folded onto the ten figures: a-e on 2 4 6 8 10, f g h i l
     on 1 3 5 7 9, m n on 1 2, o-s on 10 8 6 4 2, t u x y z on 9 7 5 3 1. The x10 groups are a letter plus e or o,
     not word codes. Each figure stands for two or three letters. Key in `grening/key_lomenie1595.tsv`.
   - **13 of the 15 passages encode exactly to the printed figures** (158 letters, `grening/lomenie1595_decryption.txt`):
     L1 "province de Bretaigne", L2 and L4 "de Camor", L3 "les despesches", L5 "de Vennes", L6 "ville de seureté de
     Bretaigne", L7 "la necessité", L9 "d'edicts", L10 "l'assamblée de Saumur", L11 "Bearn", L12 "la messe",
     L13 "de Boisdauphin", L14 "le marquis de Belisle". Reading and translation in `grening/lomenie1595_reading.md`.
   - L8 "du [?roy]": d u r o certain, then the print has 8 where the rule gives y = 3; y occurs nowhere else.
     L15 "[...] querelles": 100 76 not read. f, x, z do not occur and are inferred. Name figures not read.
   - Tests written afterwards (`grening/scripts/test_key.py`, `grening/results/test_key.txt`): with the crib letters
     fixed, the rule beats 2,000 of 2,000 random fillings of the other ten letters on the passages the cribs do not
     touch (z = 3.9). Annealing from random keys with no cribs does not find the key and reaches higher letter
     scores than it: the cribs are needed, and a letter model alone does not decide.
   - Duplessis's figures of Jan 1597: the key gives no words (looked at, not scored).

10. **28 Nov 2026, Shawn Grening (`grening/README_1597.md`).** Duplessis to Cargroy, 19 Jan 1597 (C1-C8). Not
    pre-registered.
   - Hypothesis after step 9: the same method with another table, the alphabet in order, ten letters to a round.
     That leaves ten keys. **a = 7** (a 7, b 8, c 9, d 10, e 1, f 2 ...) gives words; the other nine do not
     (letter-model score -2.222 per figure against -2.753 to -3.128). No crib. Key in
     `grening/key_duplessis1597.tsv`.
   - **6 of the 8 passages encode exactly to the printed figures** (132 of 155 figures,
     `grening/duplessis1597_decryption.txt`): C2 "un prisonnier de qualité", C3 "pour signal une eguillete bleue au
     pourpoint ou a la mandille", C4 "vos gens de Poitou dient", C6 "Courbejoliere", C7 "ruine sur sa maison",
     C8 "Monbarot". Both men are named in clear elsewhere in vol. 7. Reading and translation in
     `grening/duplessis1597_reading.md`.
   - An odd number of letters is filled with a final e, so the last group is 11 (C2, C3, C6). "5. 10." is printed as
     two groups, not 510 (C3, C4).
   - C1 "du [?parti] [?contraire]": "du part" and "contrai" exact, with 11 where "parti" wants 5. C5 not read.
     f, h, x, y, z inferred.
   - Tests written afterwards (`grening/scripts/test_key_1597.py`, `grening/results/test_key_1597.txt`): with the
     letters of the two names fixed, the rule beats 2,000 of 2,000 random fillings of the other ten letters on C2,
     C3, C4, C7 (z = 2.2). Annealing with no cribs: 5 of 24 runs score a little above the key with other tables.
   - It is not Loménie's table shifted, and the letter to his wife (W1-W3) is a third system.

## Integration check (12 Nov 2026)

- Re-run: hash lists check; the vol. 6 OCR from archive.org (`mmoiresetcorre06morn_djvu.txt`) has the sha256 stated in
  `beling/results/external_inputs.sha256`; `test_folded.py` and `test_round2.py` give the committed results (T1
  inconclusive: coverage 0.655 against a best of 0.616; T2 fits: coverage 0.78, language beats 197/200; T3 does not fit;
  T4 not supported); `explore_system.py` reruns. No second decoder was written and no archive.org page image was
  compared with the figure tables at the integration check.
- Strictness: the T2 "fits" is a coverage and language statistic on 50 groups. Of the 39 groups that take a value,
  only `10` = le roy (R10, R13, R15) and `11` = Madame (R12) read as sense without an inferred value; the single-figure
  runs R3, R4, R6, R11, R14, R16, R17 and R18 give single letters that are name codes (the table says the letter values
  do not apply), and R2, R7, R19 need the inferred 672, 134, 160, 38. The strict read share is therefore (93 + 4) /
  534 = 0.182; the contributor's 0.247 (132/534) is every group that takes a value.
- Order of events (tests pre-registered, inputs hashed first) is by the contributor's record.
- Not a stopping point: the escalation steps print, key-rebuild and retry are open below, so no page. Dudout's 1593
  reading predates this work and is unchanged.
- Overlap: no other target holds vols. 7-12 figures; catalogue 365 (Mornay family, Archives nationales 402AP/13) and
  371 (this target) are separate leads.

## Read share over cipher words only (16 Nov 2026)

README Conventions, 16 Nov 2026: the read share counts the words written in cipher. Neither 1593 entry had a read
share; `beling/reading_1593.md` has no "## Reading" heading, so a whole-file score (0.994) counts its notes and the
printed clear text, and gave one figure for both letters.

| document | before | after | state |
|---|---|---|---|
| Du Maurier, July 1593, P1-P6 | none (whole file 0.994) | 0.931 (27 of 29 cipher words) | read -> read in part |
| Serviez, 6 July 1593, S1-S2 | none (whole file 0.994) | 0.857 (6 of 7) | read -> read in part |

- How the cipher was separated: the reading gives each passage in the printed sentence around it, the deciphered words
  in **bold**; each letter's section was counted on its bold words only.
- Du Maurier: the two holes are the two words that use sign 44 (x/y), whose value is probable (Remaining gaps):
  *Tour[ay]ne* (P2) and *chevaux* (P1). The x of *chevaux* is not marked in the reading, and x is the only value of the
  sign that gives a word there, but the sign's value is probable, not attested, so the word is not a sure word (the
  coordinator's decision, 16 Nov 2026; the first count of the day had it as read, 0.966). *l'arrest* (P1) counts as read: the figures give *larest*, a spelling of
  the period, which the reading normalises.
- Serviez: the hole is *l'entreprinse* (S1). The figures give *lenteprinse*, and no group is missing (step 6, settled
  27 Oct 2026), so the *r* is a letter supplied where the cipher has nothing; the key is rebuilt, so the one-digit-slip
  rule does not apply. The reading prints the normalised spelling unmarked. On 7 words this one hole takes the letter
  under the bar: read in part.
- Both 1593 letters are now read in part. The class stays read in part (`fraction_read` 0.182 of all groups; the 1595-99 figures are open).

## Remaining gaps

- Loménie 1595, L8 (87 410 8): "du ro" then 8; "du roy" fits but the rule gives y = 3 and y occurs nowhere else (step 9) - blocker: needs-physical-access; the manuscript would show whether the figure is 3 or 8
- Loménie 1595, L15: 100 76 before "querelles" unread; 100 holds the only 0 that is not part of a 10, perhaps a name figure like 98 and 99 - blocker: too-short
- Loménie 1595 name figures in the clear text (3, 11, 14, 16, 25, 26, 98, 99), and the letters f, x, z, which do not occur and are inferred from the pattern - blocker: open-codes
- Duplessis to Cargroy Jan 1597, C1 (119 where "parti" wants 5; "contrai" without ending) and C5 (75 87 95 66, no word with the key) (step 10) - blocker: needs-physical-access; the manuscript would show whether the print's figures are right
- Duplessis's figures to his wife, Jan 1597 (W1-W3) and Sep 1597-1599 (about 130 groups incl. the name codes 81 63, 153 63, 33): unread, another system (40, 80, 132, letters printed among the figures) - blocker: no-key-material
- Rohan 1597 (vol. 7 LXXXII, CXLI; 50 groups): the 1594 key fits; 672, 134, 160 inferred and not seen again; 38 seen once more (1599) and not supported by the pre-registered test; runs R1 and R18 not read - blocker: too-short
- Rohan 1611-12 (vol. 11; 84 groups) and the unsigned 1612 letter (9 groups): a different table, unread - blocker: no-key-material
- Serviez S1, *l'entreprinse*: a letter the writer left out of the cipher (the figures give *lenteprinse*: no r, and no group missing, step 6) - blocker: needs-physical-access; every sign that is there is read, and the missing letter cannot be recovered from any file here. The checker offers no blocker type for letters left out; this is the nearest.
- 1593 sign 44 (x/y, end of P1 and P2; *chevaux* and *Touraine*, two holes in the read share since 16 Nov 2026) - blocker: too-short; 44 occurs twice, b never (the two possible dropped groups in P1 and S1 were settled by step 6)

## Escalation

- [x] siblings: bare figures in vols. 5-12 transcribed (vols. 7-8 by step 7, vols. 9-12 and the vol. 8 name code by step 8; vols. 10 and 12 have none in the OCR).
- [n/a] clear-pages: printed edition; the editors printed decipherments only where they had them (vol. 6 Rohan 1594). The king's cipher letter of 24 Feb 1595 (vol. 6 CVI) is printed in clear and covers the same affair as Loménie's (step 8).
- [x] known-keys: Rohan 1594 key fits Rohan 1597 (step 7), not Rohan 1611-12 (step 8); on 1595-98 Duplessis/Loménie neither the Rohan key (step 5) nor the folded 1593 key (step 7) fits.
- [ ] print: originals possibly AN 402AP/13 (requested 25 Oct 2026) and the Mornay papers (Nantes BM Dugast-Matifeux DM2/92-94, Institut / BnF); in particular Loménie's letter and the king's cipher letter CVI of 24 Feb 1595.
- [x] key-rebuild: Loménie 1595 letter key rebuilt from the two cribs (step 9); Duplessis to Cargroy Jan 1597 key found among ten ordered tables (step 10); his figures to his wife still without a key.
- [ ] retry: after the print step.

## 14 Nov 2026 full-texts audit

Seven documents of `documents[]` had no entry in `outcome.texts`: Loménie 1595, Duplessis Jan 1597, Duplessis 1597-98, Duplessis 1599, Rohan 1599, Rohan 1611-12 and the unsigned letter of 1612. All are unread. Their transcriptions were in the folder (`lomenie1595.txt`, `duplessis1597.txt`, rows M of `beling/transcription/v7v8_figures.tsv`, rows D, R20-R62 and U of `beling/transcription/v9v12_figures.tsv`), and so were mechanical decodes with the two known keys (`beling/results/mechanical.txt`, `beling/results/round2_mechanical.txt`, the pre-registered tests of 11-12 Nov 2026). Each is now listed with those two files and state `decoded, not read`; each note names the section of the result file that holds its lines and says that neither key gives words. Nothing was decoded again and no count changed.

## Transcription doubts (Loménie 1595, 27 Nov 2026)

- 8 (L8, last figure, p. 180) - read: 8; checked: image, decode; the print is a clear 8, the decode wants 3 for "du roy". Left as printed; the word is marked doubtful.
- 100 (L15, first group, p. 181) - read: 100; checked: image, decode; clear on the print, and no letter value fits a bare 0. Left as printed; not read.
- 10 10 810 (L10, across the line break on p. 180) - read: 10. / 10 810.; checked: image, decode; the print has no stop after the second 10, and the figures read "l'assamblée de" either way.
- 119 (C1, fourth group, vol. 7 p. 124) - read: 119; checked: image, decode; clear on the print, the decode wants 59 for "parti c". Left as printed; the word is marked doubtful.
- 5 10 (C3 and C4, vol. 7 p. 125) - read: 5. 10.; checked: image, decode; printed as two groups in both places, and the figures read the same either way.

The groups of C1-C8 in `duplessis1597.txt` were compared with the page images of vol. 7 pp. 124-126 and agree.
The other groups of `lomenie1595.txt` were compared with the page images of pp. 179-181 and agree.
