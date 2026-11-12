# Duplessis-Mornay circle: undeciphered figures printed in the 1824 *Mémoires et correspondance*

Status: in progress (1593 figures read with Brice Dudout's key, 27 Oct 2026; 1595-98 figures open; vols. 7-12 searched and two more keys tested, 11-12 Nov 2026, Andrew Beling, `beling/`)

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
| 6, CVII, pp. 179-181 | Loménie → Duplessis, Paris 24 Feb 1595 | bare figures, different system (many groups x10: 610, 810, 910), plus small numbers as name codes (3, 11, 16, 25, 26, 98, 99) |
| 6, CIX | Duplessis → his wife, 1595 | short bare run |
| 7, LXVI-LXVII, CXLI and others | Duplessis, Jan-Oct 1597 | bare figures |
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

## Remaining gaps

- Loménie 1595 (95 groups): unread; neither the Rohan 1594 key nor Dudout's folded 1593 key fits (steps 5, 7). Cribs from the editors' note and the king's cipher letter CVI (step 8) give "de Camor" and probably "de Bretagne" - blocker: no-key-material; the original of CVI or of Loménie's letter would give the key
- Duplessis's own figures, 1595-99 (to his wife and to Cargroy; about 240 groups incl. the name codes 81 63, 153 63, 33): unread, few x10 codes, probably a different table from Loménie's - blocker: no-key-material
- Rohan 1597 (vol. 7 LXXXII, CXLI; 50 groups): the 1594 key fits; 672, 134, 160 inferred and not seen again; 38 seen once more (1599) and not supported by the pre-registered test; runs R1 and R18 not read - blocker: too-short
- Rohan 1611-12 (vol. 11; 84 groups) and the unsigned 1612 letter (9 groups): a different table, unread - blocker: no-key-material
- 1593 sign 44 (x/y, end of P1 and P2) - blocker: too-short; 44 occurs twice, b never (the two possible dropped groups in P1 and S1 were settled by step 6)

## Escalation

- [x] siblings: bare figures in vols. 5-12 transcribed (vols. 7-8 by step 7, vols. 9-12 and the vol. 8 name code by step 8; vols. 10 and 12 have none in the OCR).
- [n/a] clear-pages: printed edition; the editors printed decipherments only where they had them (vol. 6 Rohan 1594). The king's cipher letter of 24 Feb 1595 (vol. 6 CVI) is printed in clear and covers the same affair as Loménie's (step 8).
- [x] known-keys: Rohan 1594 key fits Rohan 1597 (step 7), not Rohan 1611-12 (step 8); on 1595-98 Duplessis/Loménie neither the Rohan key (step 5) nor the folded 1593 key (step 7) fits.
- [ ] print: originals possibly AN 402AP/13 (requested 25 Oct 2026) and the Mornay papers (Nantes BM Dugast-Matifeux DM2/92-94, Institut / BnF); in particular Loménie's letter and the king's cipher letter CVI of 24 Feb 1595.
- [ ] key-rebuild: structural look at the 1595-99 figures and two cribs (step 8); no key.
- [ ] retry: after the print step.
