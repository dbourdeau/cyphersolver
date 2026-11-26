# Graham to Madison, Pittsburgh 12 Nov and Marietta [22 Nov] 1806: Burr reports in a State Department code (catalogue 482)

Status: no write-up. Attempted and closed open 26 Oct 2026: nothing added to the Madison Papers editors' partial
decode, so there is no page. Blocked from outside: no images online and the code's key (Weber 1979 pp. 419-30) was
not obtained (see Escalation). Reopen if someone supplies Weber's table, Lewis's key or the LoC microfilm frames.
22 Nov 2026: Weber's table was tried (section "The 2 Jan 1806 sibling in Weber's WE023"). It reads the January
sibling but not the [22 Nov] extract, so the target stays open and still has no write-up. The LoC frames are what is
left.

## The documents

- **12 Nov 1806**, Pittsburgh, RC, LoC Burr Conspiracy Collection; Founders Madison/02-13-02-0044, PJM-SS 13:39-40.
  Short; the coded words are all decoded (Wagner interlinear, completed by the editors with James E. Lewis's partial
  key): Blennerhassett, expected (enc. "expecteb"), attempts. Nothing open in this letter.
- **[22 Nov 1806]**, Marietta, extract in Graham's hand, enclosed in his 28 Nov letter; LoC Burr Conspiracy Collection;
  Founders Madison/02-13-02-0081, PJM-SS 13:78-79. Most of the extract is coded. The editors decoded it with Lewis's
  partial key; **12 groups have no reading** (10 19 30 33 35 36 39 41 51 61 65 77) and **6 more carry a "?"
  conjecture** (18 army?, 46 separation?, 54 officers?, 67 president?, 71 Union?, 73 West?), 21 of the tokens in all.
  Text with the open groups marked: `founders_22nov.txt`.

The code groups of the decoded words are not printed, so the open groups cannot be placed in the code from Founders
alone: the manuscript is needed.

## The code

- Not the Pinckney "Cypher of the Legation" (`../erving1807aug/key_pinckney.tsv`: 6 money, 18 mit, 39 ms, 71 im) and
  not Armstrong's THE=972 code (`../armstrong/`: 36 Germany, 41 however, 61 minister). Neither fits the context.
- **Lead:** Graham's 2 Jan 1806 letter from New Orleans (Founders Madison/02-11-02-0004, RC in NARA RG 59 Territorial
  Papers, Orleans, vol. 8) was decoded by Wagner "using the code provided by the State Department"; the editors say
  a copy of that code is printed in **Ralph E. Weber, *United States Diplomatic Codes and Ciphers, 1775-1938* (1979),
  pp. 419-30**. That letter also carries clerk-inserted numerals 1590-1700 that "do not correspond to numbers in the
  code". This is probably the code Graham took west as Secretary of Orleans Territory, and the first thing to check.
- Weber's book is on the Internet Archive only as a print-disabled loan (`ia_meta.json`), so its tables were not read
  here. From the layout visible in search-inside results, pp. 419-30 print the code in number order, three columns of
  49 groups a page, and group 73 or 74 falls among *pres / present / president*. If Graham used that code, the
  editors' "West?" for 73 is wrong and "president?" sits on the wrong number (67). This is unchecked: it rests on a row
  position read from OCR coordinates, not on the page.

## The 2 Jan 1806 sibling in Weber's WE023 (Andrew Beling, with AI agents, 11 and 22 Nov 2026)

Files: [`beling/`](beling/README.md). Weber's table is cited, not copied. **The table test cannot be rerun without a
copy of Weber 1979.** A reader without the book can rerun the held-out test and the 22 Nov statistics.

- **Source.** The 2 Jan 1806 letter is online. NARA T260 roll 8 (Territorial Papers, Orleans), file unit
  [221215877](https://catalog.archives.gov/id/221215877), frames 0006-0011, docket 0012. The letter starts on frame
  0006. It is the recipient's copy, with Jacob Wagner's words written above the code. Frame hashes are in
  `beling/README.md`.
- **Transcription.** 57 coded runs, 614 groups, 275 distinct (`beling/transcription_2jan1806.txt`). **It is not
  strictly blind:** Wagner's words are on the same images as the digits. Frames 0006-0009 were read before any table
  was opened. Frames 0010-0011 were read after about 40 groups had been looked up in WE023, and groups re-read after a
  lookup are marked doubtful and left out. Two groups on 0008 first read as 114 were corrected to 1114 on a zoom after
  the first run. A second reader has not checked it.
- **Table test** (418 usable words). For each word: do the table's elements at those numbers spell Wagner's word?
  Lenient allows one letter of difference. Controls: 200 shuffles of each table
  (`beling/PLAN.md`, `beling/verify.py`, `beling/results.json`). No pass mark was set before the first run.

  | table | strict | lenient | best of 200 shuffles (strict / lenient) |
  |---|---|---|---|
  | WE023 | 383 | 405 | 9 / 42 |
  | WE016, WE018, WE022, WE024-WE028 | 0-4 | 0-10 | 4-13 / 13-41 |

  The first run on 11 Nov drew all tables' shuffles from one random stream and gave a best of 36 for WE023. The rerun
  seeds each table separately. The real scores are the same in both runs.
- **Held out, no table.** A key built from Wagner's single-group words on frames 0006-0008 gives his word for 116 of
  the 118 groups it covers on 0009-0011 (200 permuted keys: mean 1.6, best 13). The reverse gives 90 of 91 (best 11).
  The table that scores best on 0006-0008 alone is WE023, and it scores 222 strict and 234 lenient of 243 words on
  0009-0011. **The 2 Jan 1806 letter is in WE023 number for number, as the Madison editors said.**
- **Where WE023 misses.** Four of the 13 lenient misses fall on cells that look like errors in our text layer of
  Weber, which was not corrected by hand (879 twice, 1159, 967), and 1593 is unreadable in it. One is Graham's (848 in
  "mulattoe"). The rest are:
  - Wagner's word choices ("near" over the group for "nearly", "nothing" over "no");
  - endings the scorer does not allow (enemies, and themselves twice);
  - three words whose syllables do not join as he wrote them (frontiers, Indians, classes).

  Graham also writes 1225 for "are" four times, beside 1228 three times. Weber's page images have not been checked at
  these cells.
- **The [22 Nov] extract is not in that code.**
  - The January key gives a value for none of the 18 open or conjectured numbers.
  - At 17 of the 18, WE023's entries are syllables and words of its *pa-pre* stretch that give no sense in the
    extract. At 30 its entry could fit ("I would 30. now arrest"), but one place cannot carry the code. The January letter itself writes "President" with a group in that stretch, not 67.
  - Only 11 of the 613 readable January groups are 77 or below. Eighteen distinct numbers drawn evenly from 1-1593
    would all fall at 77 or below with a probability of about 2 × 10^-24.
  - So either the extract is in a different, smaller code, or the numerals printed on Founders are not Graham's
    groups. Only the manuscript can settle which.
- **The November manuscripts.** The 12 Nov letter, the [22 Nov] extract and the 28 Nov covering letter are in the
  Library of Congress Burr Conspiracy Collection (MSS14415), a single bound volume, Box 1, Reel 1 (microfilm 17,112).
  The finding aid has no item list, and the volume is not digitised. So the frames have to be found on the reel.

## Remaining gaps

| groups | blocker |
|---|---|
| 10 19 30 33 35 36 39 41 51 61 65 77 (no reading) | needs-physical-access: not in WE023, the January code (`beling/`); the manuscript (LoC microfilm 17,112) is needed to see what Graham wrote; Lewis's key unpublished |
| 18 46 54 67 71 73 (conjectures) | same: WE023 does not confirm them; the manuscript is needed |
| all code groups of the decoded words | needs-physical-access: Burr Conspiracy Collection is not digitised (LoC microfilm 17,112) |

## Escalation

- Siblings: Founders search (author Graham, keyword code) gives 7 coded Graham letters: Madrid 1802-03 (key not found;
  Pinckney-era), 2 Jan 1806 (State Department code, Weber 419-30), 12 and 22 Nov 1806. The 2 Jan 1806 letter was
  aligned on 22 Nov 2026 (above): it is in WE023, and the 22 Nov extract is not.
- Clear pages: none known; Graham's 28 Nov 1806 covering letter (the "next" link from 02-13-02-0081 on Founders) describes the extract; not yet read for clear restatements.
- Known keys: Pinckney and THE=972 ruled out (above); Weber pp. 419-30 is the candidate.
- Print: James E. Lewis, *The Burr Conspiracy: Uncovering the Story of an Early American Crisis* (Princeton, 2017) may
  print or describe his partial key. Not checked (no access).
- Images: LoC catalogue mm75014415: 100 items, 1 container, 1 microfilm reel (no. 17,112, 1977), no online images;
  findingaids.loc.gov sits behind a bot check. The 2 Jan 1806 sibling is filmed and online, NARA T260 roll 8
  frames 0006-0012 (naId 221215877).
- Retry: not possible from the ciphertext alone. 21 numeric groups with no repeats beyond 18/46/73 is far too short
  for a solver.

## Next steps

1. Done 22 Nov 2026 (`beling/`): Weber's WE023 at groups 10-77 does not fit the extract (one possible word, at 30),
   although it reads the 2 Jan 1806 letter. Optional: check Weber's page images at 848, 879, 967, 1159, 1311 and 1593.
2. Ask the Madison Papers (UVA) or James E. Lewis for the partial key and the group numbers of the decoded words.
3. Order LoC microfilm 17,112 frames for the two letters.
