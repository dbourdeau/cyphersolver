# QA report: one entry per key

14 Oct 2026, revised the same day after George Lasry's review. Snapshot: `origin/main` at 044576987.

This report replaces `mixed_cipher_entries_2026-10-14.md`, the earlier same-day audit, which was a first pass
over the site pages only. Its findings are folded in below (see *The earlier audit*). The report changes no
target; each fix that is agreed goes in as its own commit.

## The rule

George Lasry, 14 Oct 2026:

> In general, solutions should be presented by keys/ciphers. Combining two entries with different ciphers just
> because they have something else in common (same collection, or same recipient, or same sender) is highly
> confusing and error prone.

His review of the first version added the following points. The second round applied them.

- **One key, one entry.** Each demonstrated key or cipher gets its own public solution entry and its own
  countable record, with its own documents, results and credits. Source folders may stay shared, and scans need
  not move. Per-key `outcome.parts` are enough only if the site, catalogue, exports and statistics really treat
  them as separate entries.
- **Keys belong to passages, not only documents.** One letter can change key between body and postscript.
  `soria1523` is an example: R9492's body is key A and its close is key B (`NOTES.md:57`).
- **Unknown keys do not merge** just because both are labelled "unknown".
- **A shared-key assignment needs evidence:** matching signs and values, tested in the passages concerned.
- **Two recoveries of one key are two contributions, not two ciphers.**

## Method

1. **Round 1.** A script (`key_split_scan.py`) scored all 384 profiles for mixed-key signals. The 90 highest,
   including every multi-document entry George solved or has a prior solution on, were reviewed by hand, with
   each target's NOTES, profile and page read.
2. **Round 2** (after George's review). The other 300 entries were reviewed, most of them single-document:
   - 139 with any signal were read in full. This set included the three page-only slugs `legation`, `mondoucet`
     and `vatican`, and the targets listed only in the earlier audit.
   - 161 with no signal had their profile read, and NOTES too when anything pointed to a second key.
3. **Verdicts:**
   - **MIXED:** one entry presents two or more keys as one result.
   - **SPLIT-OK:** several keys, already separated per key.
   - **FIXED:** split on main since the first snapshot.
   - **UNCLEAR:** the shared key is assumed but not tested, or the files do not say.
   - **SINGLE:** one key throughout.

   The verdicts are the reviewers' (Claude agents'). The headline cases and every point George raised were
   checked by hand against the repository.

## Results

All 390 entries were reviewed:

| Verdict | Count |
|---|---|
| MIXED | 59 |
| UNCLEAR | 12 |
| SPLIT-OK | 6 |
| FIXED | 2 |
| SINGLE | 311 |

Round 2 found 22 more MIXED and 9 more UNCLEAR. Most are single-document entries or entries the keyword scan
missed.

These totals count entries, not keys. As George notes, the number of distinct keys should not be quoted until
the splits are made and the open key relationships are settled.

### Corrections from George's review (checked against main)

| Entry | Correction |
|---|---|
| superscript | Already split on main (ce30cf199) into `ghinucci1527` and `gilino1527`. Done. Round 2 checked both: `ghinucci1527` SINGLE, `gilino1527` SPLIT-OK. |
| vasto1527 | Ranzo's code moved to `ranzo1528` (ce30cf199). `vasto1527` keeps Cipher 2. Cipher 1 (no. 10) must stay separately identified. `ranzo1528` lists 2 documents, but George's package covers five letters (`targets/ranzo1528/lasry/NOTES.md:21`). |
| riksarkivet1628 | The first version said R4282 was "counted twice". It is not: the exporter leaves out contributed results (`docs/_export_profiles.py:36`), so the paper data keeps only the stale "not read" row. Remove R4282 here and point to `decode4282`. |
| matignon1586 | **Error in the first version:** f. 79r is Cipher-1, not Cipher-2 (`NOTES.md:264`). Cipher-2 material is fr. 15572 ff. 218-219 (`NOTES.md:24`). Two active groups. Recalculate both fractions after the split. |
| dubellay | Not unclear: Tomokiyo distinguishes the 1528(-29) cipher George re-solved in 2022 from Bayonne's 1529 cipher (`NOTES.md:41-55`). George's credit sits on 1529 documents; scope it to the 1528 key. |
| segur | George's saved decryptions (15 Oct 2024) cover ff. 143, 233, 239, 288v. f. 143 is a different key of the same design (`NOTES.md:7,150`), so his 2024 work spans two keys. ff. 321/333 are a third key. Do not extend his credit to ff. 321, 333, 366. |
| hm1645 | Four keys: SP106, SP106-2, SP106-5, SP106-8. Applying a supplied key (SP106-5 on R929) is a different outcome from reproducing his decipherments (the other five letters). |
| esp318 | Separate nos. 5, 92 and 95. His alphabet is no. 95 only. Nos. 93-94 stay unresolved; "four keys" is not a verified count. |
| siena1421 | Remove nos. 6/24 (now `siena1431`). Do not count the unresolved documents as established key groups. |
| dandini1580 | R72 and R73 have different letter assignments. Credit his prior solution of R73, not only use of its key. |
| gramont1529 | Four keys. The Mâcon letter belongs with the Mascon subgroup of `rome1536`. |
| rome1536 | R4248 separated from the Mascon-key documents and out of his Mascon credit. |
| louis1615 | Sabran R2748 and Brûlart R2785/R2786 are separate key entries. |

### Records in two entries, and keys counted twice

Round 2 found more cases like `riksarkivet1628`. In these, a record sits in two profiles, or the same key is
counted as two:

- **rohan1636** lists fr. 3758 nos. 100 and 104 as "not solved, no key material". George has them read as
  `louis1635` and `chatillon1635`.
- **siena1421** still lists nos. 6/24 (`siena1431`).
- **bergamo1585** R17 is read with the Morosini key, Meister no. 40, and NOTES calls it a Morosini letter. It
  belongs with `morosini1588`.
- **sormano** and **sormano1529** are one key and the same three letters, with two folders, profiles and pages
  that disagree (read, and 5% read in part).
- **One key in two entries:**
  - `guise1587` / `mercoeur1587`
  - `sessa1523` / `sessa1524`
  - `r3708` / `nevers1588`
  - `visconti1528` / `visconti1529`

  These are fine as separate letters if the key recovery is counted once, and a second independent recovery is
  credited as a second contribution, not a second cipher.
- **bordeaux**: George's "prior solution" credit is for item B, the 1654 letter, which is in a different key
  from the 1653 text (`NOTES.md:36-37`).

### George's entries

Besides the corrections above, these are George's entries that round 2 found mixed or unclear:

- **morosini1588**: Meister no. 40 and the F22b key (R53/R54, unread) share one 0.99 fraction and one credit.
- **bergamo1585**: R16 uses the F18/Ragazzoni key, R17 the Morosini key; one pooled 0.99.
- **conti1649**: nos. 41-42 (his letter cipher) and no. 43 (a numeric code rebuilt from glosses) share one method.
  NOTES says "nos. 41-43 do not share a cipher".
- **adfgvx**: 22 messages under several period keys, ten under no known key, filed as one document "complete".
- **sessa1597** (unclear): the Archduke Albert letter of 1596 is under the Cp.39 key with Philip II's 1597 letters.
  Nothing shows it was tested against Cp.39.
- **entragues1581** (unclear): the second letter (ff. 780-781) has not been shown to use the f. 761r key.
- **gilino1527** (split-ok): George's independent recovery agrees with the archival key R5258 on 101 of 106 signs.
  That makes it one key and two contributions, which is how it should be recorded.

### Worst of the rest

- **potocka1714**: Potocka's key reads 95.3%. The entry shows 75.5% only because Mniszech's R7524, in another key,
  is unread.
- **r1871**: two despatches 122 years apart share "read from existing decipherment". The 1680 decipherment was
  never found.
- **r1854**: four letters in four keys under one ciphertext-only method and a pooled 0.922. P1 is unsolved and P3
  was read from its gloss.
- **kaa4591b**: three unrelated keys pooled at 0.946, which hides R9414 at 92.2%, under the read bar.
- **sp106box10**: at least four systems under one "read with known key". The known key's own letter, R657, is
  not read.
- **guiche1551, r4349, urquhart, walsingham1585, mondoucet, swieten1757**: one fraction pools a read key with an
  unread or unrelated one.
- **legation**: the profiles are split (`erving1807`, `jqa`), but the site still shows one card. It has one badge
  (jqa's method) and one credit line naming Ford for Erving's code too.
- **sunyatsen**: credits Dudout and wanglu for other correspondents' keys on a single-telegram entry.
- **michell1751, nevers1593, bl32305, throckmorton, deswart1782, hereditary1796**: the README row claims more than
  the per-key results support.

### The earlier audit

`mixed_cipher_entries_2026-10-14.md` judged 54 entries from their pages. Its high- and medium-confidence cases
are all confirmed here as MIXED or SPLIT-OK, and `mondoucet` is UNCLEAR. It differs from this report on four
entries:

- **segur**: judged fine there. Here it is MIXED, and George confirms two keys inside his own scope.
- **hm1645**: judged fine there. Here it is MIXED, with four keys, which George confirms.
- **benedict1399**: judged fine there. Here it is MIXED: the Vico 1398 line is in another, unknown key, and the
  entourage letters were never tested against the Benedict key.
- **castelcicala1816**: "to check" there. Here it is MIXED: R9586/R9588 use a second code.

### Why it happens

- **No key field per document or passage.** The schema knows keys only through one `system` block and optional
  `outcome.parts`, so nothing catches a merge.
- **Folders follow the source, not the key.** Targets were opened from a catalogue number, DECODE group, volume or
  correspondent, and later documents of the same origin were added to them.
- **The exporter repeats target-level results on every document row** (`docs/_export_profiles.py:45`). A pooled
  fraction or method is copied onto documents it does not describe.
- **Pooled fractions** hide both the read and the unread key.

### Schema and checker (George approved the direction, with these amendments)

1. A stable `key_id` on cipher passages, not only whole documents (body and postscript can differ).
2. A `keys[]` registry in each profile. Each key has its own system description, document and passage ranges,
   results, counts, sources and credits.
3. Key identity kept apart from solution history: two recoveries of one key are two contributions.
4. "Unknown" keys never merge by label. A shared `key_id` needs recorded evidence: signs and values tested in
   the passages concerned.
5. `_check_profile.py` rejects a record (a DECODE R-number or shelfmark) that sits in two profiles. That check
   would have caught `riksarkivet1628`/`decode4282` and `rohan1636`.
6. The exporter, the site statistics and the catalogue count per key, not per target.

### Proposed fix order

1. The double counts, starting with `riksarkivet1628`/`decode4282` and `rohan1636`/`louis1635`/`chatillon1635`,
   then `siena1421`, `bergamo1585`, `sormano`.
2. George's entries and the corrections table above.
3. Entries where the merge changes a headline result: `potocka1714`, `r1871`, `kaa4591b`, `michell1751`,
   `vich1511`, `nevers1593`.
4. The schema, checker and exporter changes, so new targets cannot merge keys.
5. The remaining MIXED entries, then the UNCLEAR ones (test the assumed shared key, or record that it is
   untested).

## Open questions for George

1. **segur**: your files cover ff. 143, 233, 239, 288v. Is f. 143 read in your 2024 solution, or only its key
   identified? Your saved OTA output is not readable French, so the scope cannot be settled from the files.
2. **siena1431**: the profile credits you with a key "recovered ciphertext-only with Claude and the help of
   ChatGPT Astra, then matched to DECODE R4755". Your assistant's notes say R4755 was found by Astra. How should
   the credit line read?
3. **riksarkivet1628 / decode4282**: decode4282 says "read with scattered gaps". Your assistant counted 801 of
   1,085 signs read, which is a partial break. Which is the right outcome?
4. **ranzo1528**: should all five letters of your package be listed as documents? That includes fr. 3019 no. 27
   and the Clair. 327 copy.
5. **One entry or parts**: for entries where the documents share only the archive (for example `r1871`,
   `louis1615`, `kaa4591b`), we propose separate entries. For entries with one sender and one key change
   (`soria1523`, `mondoucet`, `deswart1782`), is a per-key part with its own page section and README row enough?
6. **Withheld targets** (fr. 3029, fr. 3092): checked. The details are kept out of this public report. Shall I send
   them to you privately?

Per-target findings follow. The raw reviewer output, with withheld targets reduced to their verdict, is in
`key_split_findings.jsonl`.

## Summary table

| Target | Verdict | Lasry involvement | Keys |
|---|---|---|---|
| adfgvx | MIXED | key or decipherment used (period keys, with Niebel/Kopal/Wacker; sixteenth CHI key); prior solution (2017 thread) | 4 |
| bergamo1585 | MIXED | key or decipherment used (F18 key D3103/D3105, R16 only); prior R15 reading noted | 2 |
| bordeaux | MIXED | prior solution (credited, but for item B, a different key) | 2 |
| conti1649 | MIXED | key or decipherment used (nos. 41-42, HistoCrypt 2023) | 2 |
| dandini1580 | MIXED | prior solution of R73 (decryption D3191 + key D3190 on DECODE, 2020), recorded only as 'key or decipherment used' | 2 |
| dubellay | MIXED | prior solution (re-solved the 1528 cipher in 2022, GL.htm) - credited on a profile whose documents are all 1529 | 2 |
| esp318 | MIXED | key or decipherment used (no. 95 alphabet, 2022) | 4 |
| gramont1529 | MIXED | key or decipherment used (2023 GL.htm tables, all four keys); prior solution (decoded all four texts 2023, unpublished) | 4 |
| hm1645 | MIXED | key or decipherment used (four reconstructed keys + plaintexts on DECODE, 2020); effectively prior solution of all six | 4 |
| louis1615 | MIXED | prior solution of R2748 (Sabran 1631 cipher, 2022) | 2 |
| matignon1586 | MIXED | prior solution credit for fr. 15572 f. 43 (2022), a leaf excluded from the target | 3 |
| morosini1588 | MIXED | key or decipherment used (partial Meister-40 reconstruction on R18, and the F22b key for R53/R54) - one credit spanning two keys | 2 |
| riksarkivet1628 | MIXED | solution of R4282 (in the separate target decode4282, 14 Oct 2026); not reflected here | 6 |
| rohan1636 | MIXED | readings of fr. 3758 nos. 100 and 104 (filed as louis1635, chatillon1635); not credited here | 3 |
| rome1536 | MIXED | key or decipherment used (2023 re-tabulation of Mascon's cipher, GL.htm) | 2 |
| segur | MIXED | prior solution (unpublished 2024, scope not stated per folio) | 3 |
| affry1757 | MIXED |  | 2 |
| beatrice1482 | MIXED |  | 3 |
| benedict1399 | MIXED |  | 3 |
| bl32305 | MIXED |  | 4 |
| caprile1519 | MIXED |  | 3 |
| castelcicala1816 | MIXED |  | 2 |
| champagne1590 | MIXED |  | 4 |
| dedem1788 | MIXED |  | 2 |
| deswart1782 | MIXED |  | 2 |
| foix1563 | MIXED |  | 2 |
| geertruidenberg | MIXED |  | 2 |
| guiche1551 | MIXED |  | 3 |
| heidelberg597 | MIXED |  | 3 |
| hellen1752 | MIXED |  | 3 |
| hereditary1796 | MIXED |  | 2 |
| ilten1697 | MIXED |  | 2 |
| kaa4591 | MIXED |  | 9 |
| kaa4591b | MIXED |  | 3 |
| legation | MIXED |  | 2 |
| maisse1592 | MIXED |  | 2 |
| michell1751 | MIXED |  | 2 |
| nevers1593 | MIXED |  | 2 |
| orpo1942 | MIXED |  | 2 |
| papai1706 | MIXED |  | 2 |
| potocka1714 | MIXED |  | 2 |
| r1854 | MIXED |  | 4 |
| r1871 | MIXED |  | 2 |
| r4349 | MIXED |  | 2 |
| rakoczi1704 | MIXED |  | 3 |
| sessa1593 | MIXED |  | 2 |
| siena1421 | MIXED | none in profile credits (Lasry solved nos. 6/24, now in siena1431) | 8 |
| sieniawski1708 | MIXED |  | 5 |
| sp106box10 | MIXED | none (his SP 106 keys tested on R931, do not fit) | 4 |
| sunyatsen | MIXED |  | 3 |
| swieten1757 | MIXED |  | 2 |
| thurloe | MIXED |  | 4 |
| transylvania1645 | MIXED |  | 3 |
| urquhart | MIXED |  | 2 |
| vanreede1787 | MIXED |  | 2 |
| vich1511 | MIXED |  | 2 |
| walsingham1585 | MIXED |  | 2 |
| windischgraetz1720 | MIXED |  | 2 |
| wod1568 | MIXED |  | 3 |
| entragues1581 | UNCLEAR | solution (Lasry, BnF cipher research) | 2 |
| sessa1597 | UNCLEAR | solution (Lasry, BnF cipher research) | 2 |
| charlesi | UNCLEAR |  | 2 |
| damiata1624 | UNCLEAR |  | 2 |
| lopehurtado1523 | UNCLEAR |  | 2 |
| middelmore1563 | UNCLEAR |  | 2 |
| mondoucet | UNCLEAR |  | 2 |
| nevers1574 | UNCLEAR |  | 2 |
| scorpion | UNCLEAR |  | 2 |
| sp95box136 | UNCLEAR |  | 2 |
| throck1560 | UNCLEAR |  | 2 |
| throckmorton | UNCLEAR |  | 3 |
| gilino1527 | SPLIT-OK | solution (independent ciphertext-only reconstruction of the same key, PR #34) | 1 |
| ferdinand3 | SPLIT-OK |  | 3 |
| malsburg1637 | SPLIT-OK |  | 2 |
| rupert | SPLIT-OK |  | 4 |
| sanchez1522 | SPLIT-OK |  | 2 |
| soria1523 | SPLIT-OK |  | 2 |
| superscript | FIXED | solution (Gilino R8572 edition, ciphertext-only per his notes) | 2 |
| vasto1527 | FIXED (in part) | key or decipherment used (Cipher 2, no. 6); prior solution (Cipher 1, no. 10); solution (Ranzo code, 14 Oct 2026) | 3 |
| acciaiuoli1757 | SINGLE | key or decipherment used (reconstructed key DOC_R25_D3232 on R25, R195-R201) | 1 |
| alessandrino1568 | SINGLE | key or decipherment used (2020 polyphonic key on R93-R102, R115) | 1 |
| bianchi | SINGLE | solution (Lasry, BnF cipher research, with ChatGPT Astra 6 and Opus 5.5) | 1 |
| bizozola1520 | SINGLE | key or decipherment used (GL.htm key for fr. 3034 f. 156) | 1 |
| bossuet | SINGLE | lasry: solution (BnF cipher research, 10 Oct 2026) | 1 |
| ceva1632 | SINGLE | key or decipherment used (reconstructed key on R74-R84; his decipherments of R74, R77, R78, R82 used as gold) | 1 |
| clair460alpha | SINGLE | lasry: solution | 1 |
| colonia1721 | SINGLE | key or decipherment used (ASV-C15 key and decryption on DECODE R24) | 1 |
| decode4282 | SINGLE | solution (CTTS transcription and homophonic solver) | 1 |
| duquesne1681 | SINGLE | lasry: solution | 1 |
| egmond | SINGLE | prior solution (2023 key, GL.htm s.2); pointer | 1 |
| florence1429 | SINGLE | pointer (suggested siblings for the full key) | 1 |
| forster | SINGLE | prior solution (unpublished, credited in Pitt's repository) | 1 |
| goring1645 | SINGLE | key or decipherment used (key 'TNA SP106-3' and plaintext on DECODE R932) | 1 |
| guise1587 | SINGLE | key or decipherment used (fr. 15564 key table, GL.htm 2022) | 1 |
| labbe1582 | SINGLE | verification (independent ciphertext-only solution, Oct 2026) | 1 |
| lucca | SINGLE | pointer (apparent polyphony = errors) | 1 |
| lucini1767 | SINGLE | key or decipherment used (key reconstructed from sibling R121, attached to R120) | 1 |
| marechaux1520 | SINGLE | key or decipherment used (fr. 3081 key; f. 41r read by him) | 1 |
| mellon136 | SINGLE | prior solution credit: transcription of p. 24 (2022), used as a check | 1 |
| memoire1560 | SINGLE | prior solution (2023, unpublished) | 1 |
| mercoeur1587 | SINGLE | key or decipherment used (2022 Guise-Mercoeur key, extended here); f.27 read by Lasry | 1 |
| nuncio1566 | SINGLE | key or decipherment used (reconstructed key on DECODE R85-R90, 2020) | 1 |
| nunzio1718 | SINGLE | key or decipherment used (S364 key and segmented decipherment on DECODE R154-R177, 2020) | 1 |
| nunzio1736 | SINGLE | key or decipherment used / prior solver: key 'ASV - S423' and segmented decipherment of all 11 items (24 Oct 2020) | 1 |
| pallotto1629 | SINGLE | pointer (identified that 6960 uses the 6956 key) | 1 |
| r1892 | SINGLE | prior solution (solved independently 2021, unpublished) | 1 |
| ranzo1528 | SINGLE | solution (independent recovery of Ranzo's code, 5 letters, Biermann transcription) | 2 |
| rupert1645 | SINGLE | key or decipherment used (King-Queen key 'TNA SP106-5', DECODE R929, 2020, applied unchanged) | 1 |
| sauli1579 | SINGLE | key or decipherment used (Portugal nunciature key; decryption of R190-R191) | 1 |
| sega1591 | SINGLE | solution (Lasry, BnF cipher research) | 1 |
| siena1431 | SINGLE | solution (key recovered ciphertext-only, readings of nos. 6 and 24) | 1 |
| sormano | SINGLE | lasry: key or decipherment used (2023 fr. 3096 key) | 1 |
| sormano1529 | SINGLE | key or decipherment used (2023 key on francis.htm) | 1 |
| sp106r927 | SINGLE | pointer (reported the Richards 1974 decipherment) | 1 |
| vatican | SINGLE | lasry: transcription (2019 MysteryTwister), pointer | 1 |
| vatican5 | SINGLE | transcription (MysteryTwister 2019) and pointer | 1 |
| visconti1528 | SINGLE | lasry: key or decipherment used | 1 |
| visconti1529 | SINGLE | key or decipherment used (GL.htm key 'BNF Francais 3045f28 and 3034f154') | 1 |
| R1942 | SINGLE |  |  |
| R1944 | SINGLE |  |  |
| abwehr | SINGLE |  | 1 |
| adrian1521 | SINGLE |  | 1 |
| aerssen1601 | SINGLE |  |  |
| andreae1616 | SINGLE |  |  |
| anne1711 | SINGLE |  |  |
| armstrong | SINGLE |  | 1 |
| augurelio1535 | SINGLE |  | 1 |
| ayala1516 | SINGLE |  | 1 |
| bagno1652 | SINGLE |  | 1 |
| balbases1677 | SINGLE |  |  |
| baner1640 | SINGLE |  | 1 |
| battier1686 | SINGLE |  | 1 |
| bay1706 | SINGLE |  | 1 |
| bayard1526 | SINGLE |  | 1 |
| berny1607 | SINGLE |  |  |
| bertelot | SINGLE |  |  |
| bethune | SINGLE |  |  |
| bethune1629 | SINGLE |  |  |
| beuningen1676 | SINGLE |  | 1 |
| birago | SINGLE |  | 1 |
| birago1571 | SINGLE |  |  |
| blancmesnil | SINGLE |  |  |
| blasco1597 | SINGLE |  |  |
| blume | SINGLE |  | 1 |
| bonzagni1512 | SINGLE |  |  |
| boswell | SINGLE |  | 1 |
| boswell1628 | SINGLE |  | 1 |
| bouillon1650 | SINGLE |  |  |
| breves1603 | SINGLE |  | 1 |
| breves1610 | SINGLE |  |  |
| brienne1067 | SINGLE |  |  |
| brienne5160 | SINGLE |  |  |
| buda1489 | SINGLE |  | 1 |
| burghley1559 | SINGLE |  |  |
| burghley1572 | SINGLE |  | 1 |
| burgo1527 | SINGLE |  |  |
| caracciolo1537 | SINGLE |  | 1 |
| carpio1677 | SINGLE |  |  |
| catinat1691 | SINGLE |  | 1 |
| catokwacopa | SINGLE |  | 1 |
| censorship | SINGLE |  |  |
| charles1536 | SINGLE |  |  |
| charlesixducroc | SINGLE |  |  |
| chatillon1635 | SINGLE |  |  |
| chaulnes | SINGLE |  |  |
| chodkiewicz1575 | SINGLE |  |  |
| cifuentes1534 | SINGLE |  |  |
| clair1161 | SINGLE |  |  |
| clair1225 | SINGLE |  |  |
| clair357 | SINGLE |  |  |
| clair460bar | SINGLE |  |  |
| clair460num | SINGLE |  |  |
| cobham1588 | SINGLE |  | 1 |
| cocquet | SINGLE |  | 1 |
| colbert | SINGLE |  | 2 |
| coligny1563 | SINGLE |  |  |
| conley1652 | SINGLE |  |  |
| copenhagen | SINGLE |  |  |
| dagapeyeff | SINGLE |  |  |
| dampierre1589 | SINGLE |  |  |
| debosnys | SINGLE |  |  |
| desmarets1710 | SINGLE |  | 1 |
| destaing | SINGLE |  | 1 |
| dinteville1592 | SINGLE |  | 1 |
| dubellay1555 | SINGLE |  |  |
| dubellay65 | SINGLE |  |  |
| ducroc | SINGLE |  |  |
| dupuy155 | SINGLE |  |  |
| dupuy468 | SINGLE |  |  |
| eichel1758 | SINGLE |  | 1 |
| enigma | SINGLE |  | 1 |
| erving1807 | SINGLE |  |  |
| erving1807aug | SINGLE |  |  |
| esterhazy1744 | SINGLE |  |  |
| estrada1503 | SINGLE |  | 1 |
| eugenie1859 | SINGLE |  |  |
| fagel1804 | SINGLE |  | 1 |
| ferdinand1619 | SINGLE |  | 1 |
| feuquieres | SINGLE |  |  |
| feuquieres1678 | SINGLE |  |  |
| feynman | SINGLE |  | 1 |
| florence1414 | SINGLE |  |  |
| fogliani1568 | SINGLE |  |  |
| fr14765p351 | SINGLE |  |  |
| fr3029 | SINGLE |  |  |
| fr3029f134 | SINGLE |  |  |
| fr3092 | SINGLE |  |  |
| fr3321dc | SINGLE |  |  |
| fr3575f56 | SINGLE |  |  |
| fr4696num | SINGLE |  |  |
| ghinucci1527 | SINGLE |  | 1 |
| goertz1717 | SINGLE |  | 1 |
| goldbar | SINGLE |  |  |
| gondi1594 | SINGLE |  |  |
| gonzaga1590 | SINGLE |  | 1 |
| haga1620 | SINGLE |  | 1 |
| hamilton | SINGLE |  |  |
| hamilton1569 | SINGLE |  | 1 |
| harley1582r8499 | SINGLE |  | 1 |
| harley1582r8500 | SINGLE |  |  |
| harley1582r8504 | SINGLE |  |  |
| harley1582r8505 | SINGLE |  | 1 |
| harley286 | SINGLE |  |  |
| harley287 | SINGLE |  | 1 |
| harley6345 | SINGLE |  |  |
| harley7001 | SINGLE |  | 1 |
| henter1707 | SINGLE |  |  |
| herbault1625 | SINGLE |  |  |
| herbault1626 | SINGLE |  |  |
| hernannunez1674 | SINGLE |  | 1 |
| hesse1603 | SINGLE |  | 1 |
| hesse1672 | SINGLE |  |  |
| hesse1824 | SINGLE |  |  |
| heusner1637 | SINGLE |  | 1 |
| hyde | SINGLE |  | 1 |
| ilten1743 | SINGLE |  | 1 |
| isabella1531 | SINGLE |  |  |
| it1583 | SINGLE |  |  |
| jantini1517 | SINGLE |  | 1 |
| jeannin1607 | SINGLE |  |  |
| joachim1530 | SINGLE |  |  |
| jones1753 | SINGLE |  | 1 |
| joyeuse | SINGLE |  | 1 |
| jqa | SINGLE |  |  |
| kaliningrad | SINGLE |  |  |
| kauderbach1754 | SINGLE |  |  |
| kurtz1639 | SINGLE |  |  |
| laboderie1608 | SINGLE |  |  |
| lanssac | SINGLE |  | 1 |
| lebel1593 | SINGLE |  | 1 |
| lee1526 | SINGLE |  | 1 |
| lerouge | SINGLE |  |  |
| letellier | SINGLE |  |  |
| lodi1584 | SINGLE |  |  |
| loeschnen1816 | SINGLE |  |  |
| lomer1563 | SINGLE |  |  |
| lopehurtado | SINGLE |  | 1 |
| lorraine1592 | SINGLE |  | 1 |
| louis1635 | SINGLE |  |  |
| lucinge1588 | SINGLE |  |  |
| mai1531 | SINGLE |  |  |
| malvezzi1548 | SINGLE |  | 1 |
| marburg1635 | SINGLE |  |  |
| maria1435 | SINGLE |  | 1 |
| matthias1482 | SINGLE |  |  |
| medici1425 | SINGLE |  | 1 |
| mellon29 | SINGLE |  | 1 |
| mendoza1589 | SINGLE |  |  |
| mercoeur1586 | SINGLE |  | 1 |
| mercy1648 | SINGLE |  |  |
| meryvic1589 | SINGLE |  |  |
| milroy | SINGLE |  | 1 |
| moncada1524 | SINGLE |  | 1 |
| mondesir1769 | SINGLE |  |  |
| moray | SINGLE |  | 1 |
| muxetula1531 | SINGLE |  |  |
| napoleon | SINGLE |  | 1 |
| needham1587 | SINGLE |  |  |
| nevers1587 | SINGLE |  |  |
| nevers1588 | SINGLE |  | 1 |
| nevers1589 | SINGLE |  |  |
| nevers1594gondi | SINGLE |  |  |
| nevers1595 | SINGLE |  | 1 |
| nino1522 | SINGLE |  | 1 |
| norfolk1570 | SINGLE |  | 1 |
| norreys1567 | SINGLE |  | 1 |
| orbais | SINGLE |  | 1 |
| ormanetto1573 | SINGLE |  | 1 |
| ormanetto1576 | SINGLE |  |  |
| ormonde | SINGLE |  | 1 |
| ottobon | SINGLE |  | 1 |
| paleologue1562 | SINGLE |  |  |
| palm1727 | SINGLE |  |  |
| pelissier1592 | SINGLE |  | 1 |
| percy1559 | SINGLE |  | 1 |
| perwich | SINGLE |  |  |
| portugal1667 | SINGLE |  |  |
| poupet1522 | SINGLE |  |  |
| poyntz1527 | SINGLE |  |  |
| prussia1702 | SINGLE |  |  |
| r1212 | SINGLE |  | 1 |
| r1818 | SINGLE |  |  |
| r1862 | SINGLE |  | 1 |
| r1874 | SINGLE |  |  |
| r1875 | SINGLE |  | 1 |
| r2232 | SINGLE |  | 1 |
| r2234 | SINGLE |  | 1 |
| r2242 | SINGLE |  |  |
| r2276 | SINGLE |  | 1 |
| r3708 | SINGLE |  | 1 |
| r4157 | SINGLE |  | 1 |
| r4817 | SINGLE |  | 1 |
| r688 | SINGLE |  |  |
| r7707 | SINGLE |  | 1 |
| r8356 | SINGLE |  | 1 |
| r8358 | SINGLE |  |  |
| r8361 | SINGLE |  |  |
| r8362 | SINGLE |  |  |
| r8364 | SINGLE |  |  |
| r8870 | SINGLE |  |  |
| r8871 | SINGLE |  |  |
| r9658 | SINGLE |  |  |
| raince | SINGLE |  | 1 |
| rakoczi1707 | SINGLE |  | 1 |
| randolph1570 | SINGLE |  |  |
| rangone1530 | SINGLE |  | 1 |
| rechteren1785 | SINGLE |  |  |
| renard1554 | SINGLE |  |  |
| renard1556 | SINGLE |  |  |
| rennes1563 | SINGLE |  | 1 |
| richelieu | SINGLE |  |  |
| roell1809 | SINGLE |  | 1 |
| rondinelli1590 | SINGLE |  |  |
| ronquillo1676 | SINGLE |  | 1 |
| roosevelt | SINGLE |  |  |
| sadler1543 | SINGLE |  |  |
| sadoleto1482 | SINGLE |  |  |
| salviati1525 | SINGLE |  |  |
| sanchez1523 | SINGLE |  | 1 |
| santacroce1552 | SINGLE |  |  |
| schiner1516 | SINGLE |  | 1 |
| scipion1585 | SINGLE |  |  |
| sega1593 | SINGLE |  |  |
| segura1596 | SINGLE |  |  |
| selve1535 | SINGLE |  | 1 |
| sessa1523 | SINGLE |  | 1 |
| sessa1524 | SINGLE |  | 1 |
| sg1629 | SINGLE |  | 1 |
| sinzendorff1578 | SINGLE |  | 1 |
| sloane3188 | SINGLE |  |  |
| smith1562 | SINGLE |  | 1 |
| soglia1848 | SINGLE |  |  |
| soria1527 | SINGLE |  |  |
| sp106r597 | SINGLE |  | 1 |
| sp53 | SINGLE |  |  |
| spaen1808 | SINGLE |  |  |
| sperantio1534 | SINGLE |  | 1 |
| spinelly1516 | SINGLE |  |  |
| stafford1586 | SINGLE |  | 1 |
| stepney | SINGLE |  | 1 |
| stowe166 | SINGLE |  | 1 |
| szembek1689 | SINGLE |  | 1 |
| throck1569 | SINGLE |  | 1 |
| toledo1565 | SINGLE |  | 1 |
| toulon1803 | SINGLE |  | 1 |
| tranchedini1452 | SINGLE |  |  |
| turenne1528 | SINGLE |  |  |
| ungnad1576 | SINGLE |  | 1 |
| vanreede1792 | SINGLE |  | 1 |
| vargas1552 | SINGLE |  |  |
| vergier1696 | SINGLE |  |  |
| vetesi1705 | SINGLE |  |  |
| vieuville1587 | SINGLE |  |  |
| villardeau | SINGLE |  |  |
| villeneuve1737 | SINGLE |  |  |
| villeroy258 | SINGLE |  |  |
| visconti1727 | SINGLE |  |  |
| vizani1637 | SINGLE |  |  |
| vulcob1573 | SINGLE |  |  |
| waldeck1744 | SINGLE |  |  |
| walsingham1572 | SINGLE |  | 1 |
| walsingham1572nov | SINGLE |  |  |
| walsingham1581 | SINGLE |  |  |
| warsaw | SINGLE |  | 1 |
| wesselenyi1664 | SINGLE |  | 1 |
| windischgraetz1721 | SINGLE |  | 1 |
| wotton1585 | SINGLE |  |  |
| yard1699 | SINGLE |  | 1 |
| zeschau1841 | SINGLE |  |  |
| zhongshan | SINGLE |  |  |

## Entries that combine documents in different keys (59)

### adfgvx  (Lasry entry)

**Verdict:** MIXED  
**Lasry:** key or decipherment used (period keys, with Niebel/Kopal/Wacker; sixteenth CHI key); prior solution (2017 thread)

| Key / cipher | Documents | Outcome |
|---|---|---|
| ADFGVX period key Nov 1-3 (len 19) | pp. 100, 105, 109 ... | read by 2017 readers with known key |
| ADFGVX period key Nov 4-6 | pp. 132, 146 ... | read by 2017 readers |
| Lasry's 16th key CHI 13 Nov | the CHI pair | read by Lasry 2017 |
| none fits | 10 open messages | not solved |

**Where it is merged:** Twenty-two messages under several three-day period keys (and ten under no known key) are one profile document 'residue22' with one method 'read with known key', fraction 'unknown', parts null; README row says 'complete'. The page table does give the key per message, so the split exists only on the page.

**Risk:** medium: one system but many keys; the profile records solved and unsolved keys as one 'read with known key' result; README 'complete' overstates 9 solved, 3 partial, 10 open.

**Proposed fix:** outcome.parts per period key (solved/partial/open counts and solver per key, open group as 'not solved'); README status should not be 'complete' for the open ten.

**Evidence:** docs/adfgvx.html:84-90 (table with per-message key column: Nov 1-3, Nov 4-6, 'none fits'); targets/adfgvx/profile.json documents=1 'residue22', outcome.parts null, fraction 'unknown'; README.md:318 'complete ... 9 solved, 3 partial, 10 open'

### bergamo1585  (Lasry entry)

**Verdict:** MIXED  
**Lasry:** key or decipherment used (F18 key D3103/D3105, R16 only); prior R15 reading noted

| Key / cipher | Documents | Outcome |
|---|---|---|
| F18 key (Lasry D3105) + Ragazzoni 1583 nomenclator (Meister p.324 no.2) | R16 (R15 already Lasry's) | read with known key; codes 18/48 open |
| Meister p.393 no.40 (Morosini 1587), the morosini1588 decoder | R17 (Morosini-period letter, not Bergamo/Nazareth) | read with known key; 5 codes open |

**Where it is merged:** R17 is in a different key and from a different nuncio (Morosini) but sits in this entry because it is filed in the same volume Francia 18 and DECODE series R15-R17. Profile: one method, one pooled fraction 0.99, parts null; README one row 'complete'.

**Risk:** medium: both parts use the same method so the badge is not wrong, but the paper counts two keys as one cipher; R17 is a second application of the morosini1588 key and belongs with that key's tally.

**Proposed fix:** Add outcome.parts per key (F18/R16; Meister no.40/R17) with separate fractions; README row and system.summary should name both keys (summary now describes only the F18 two-digit system); cross-reference R17 from morosini1588.

**Evidence:** targets/bergamo1585/NOTES.md:14-20 (R16 F18 key + Meister p.324), :31-34 (R17 Meister no.40, 'a Morosini-period letter ... not Bergamo/Nazareth'); profile.json outcome.parts null, fraction_read 0.99; README.md:274

### bordeaux  (Lasry entry)

**Verdict:** MIXED  
**Lasry:** prior solution (credited, but for item B, a different key)

| Key / cipher | Documents | Outcome |
|---|---|---|
| Bordeaux 1653 syllabary, English key sheet R7537 | item A, BL Add MS 4200 ff. 88-90 (R8390; dups R8391, R8393) | read after matching with key from external sources |
| Mazarin-Bordeaux 1654 key (Lasry 2025) | item B, Mélanges de Colbert 11 ff. 479-481 (R9482) | solved by Lasry; not handled here, no images |

**Where it is merged:** Profile outcome.credits and the page credits line give Lasry 'prior solution'/'earlier solution' on the item A entry, but his solution is of item B, which NOTES says is a different key ('The 1654 key does not read the 1653 text ... so the keys differ'). Item B is not in documents[]. A reader/paper export sees Lasry as having earlier solved this target.

**Risk:** high for credits/contamination: the paper's prior-solution field would wrongly mark item A as previously solved.

**Proposed fix:** Drop the lasry credit from bordeaux/profile.json (or change role to 'pointer' with note 'design comparison only, different key'); on docs/bordeaux1653.html move Lasry out of the Credits line into the text about the related 1654 letter; item B stays its own (not-counted) entry.

**Evidence:** targets/bordeaux/NOTES.md:36-37 'The 1654 key does not read the 1653 text ... so the keys differ'; targets/bordeaux/profile.json outcome.credits[2] 'item B ... solved'; docs/bordeaux1653.html:50 'George Lasry (earlier solution)'

### conti1649  (Lasry entry)

**Verdict:** MIXED  
**Lasry:** key or decipherment used (nos. 41-42, HistoCrypt 2023)

| Key / cipher | Documents | Outcome |
|---|---|---|
| poly-homophonic lower-case letter cipher (Lasry 2023 key) | BnF fr. 3854 nos. 41-42 (26-27 Mar 1649) | read from existing decipherment (Lasry key and text in hand; re-transcribed, small corrections) |
| numeric letter-and-syllable code, four interleaved alphabets, nulls 99-250 | BnF fr. 3854 no. 43 (5 Mar 1649, mémoire pour Laigue) | key recovered from adjacent plaintext (contemporary interlinear glosses), unglossed 12-line opening read |

**Where it is merged:** One profile, one outcome.method ('read with known key'), one fraction ('unknown'), one README row and one system summary for two unrelated systems; outcome.parts is null. The NOTES themselves say nos. 41-43 do not share a cipher. Page does have separate sections (#nos41-42, #no43) but one badge.

**Risk:** high: the paper data counts one cipher with one method; Lasry's prior solution of 41-42 and the new key work on 43 are merged, so 'read with known key' understates no. 43 and overstates 41-42 as our reading.

**Proposed fix:** Add outcome.parts: {nos. 41-42: read from existing decipherment, credit lasry} and {no. 43: key recovered based on adjacent plaintext, credit contemporary}; split system summary per part; give each part its own fraction; consider two README rows/badges.

**Evidence:** targets/conti1649/NOTES.md:16 'no, nos. 41–43 do not share a cipher'; profile.json outcome.method 'read with known key', parts null, fraction_read 'unknown'; README.md:248 one row for nos. 41–43

### dandini1580  (Lasry entry)

**Verdict:** MIXED  
**Lasry:** prior solution of R73 (decryption D3191 + key D3190 on DECODE, 2020), recorded only as 'key or decipherment used'

| Key / cipher | Documents | Outcome |
|---|---|---|
| Lasry's key D3190 (even-second-digit letter homophones + 3-digit^ nomenclator) | R73 (ASV Francia 283C ff. 89r-90r) | read from existing decipherment (Lasry 2020); 32 illegible groups, 5 nomenclator groups open |
| R72 letter key (same frame and nomenclator, different letter assignment), rebuilt here by DP parse + swap annealing, then aligned with the leaf's decipherment | R72 (f. 52, 16 May 1580) | text read at the time (contemporary decipherment below the figures); key recovered here (ciphertext-only anneal within Lasry's frame, confirmed on adjacent plaintext) |

**After George's review:** Confirmed by George: R72 and R73 have different letter assignments despite shared structure. Credit his prior solution of R73, not only use of its key.

**Where it is merged:** Grouped by sender/recipient and volume. NOTES ('## Two keys in one frame', NOTES.md:21) and the page (sections 02/03) separate the two keys clearly, but the profile has no outcome.parts: one outcome.method 'read from existing decipherment' for both, system.summary merges them into one frame description, fraction_read 'unknown'; Lasry's role on R73 is logged as 'key or decipherment used' rather than 'prior solution'.

**Risk:** Lasry's R73 solution is not recorded as his prior solution in the paper data; the R72 key reconstruction (our own work) and Lasry's R73 reading collapse into one 'existing decipherment' outcome; a reader of the README row may think Lasry's key reads R72 (it 'gives nonsense on R72', NOTES.md:24).

**Proposed fix:** Add outcome.parts: R73 'read from existing decipherment' (credit lasry, prior solution); R72 'read from existing decipherment' for the text plus contribution 'key recovered' for the letter key. Optionally split into dandini1580-r72 and dandini1580-r73.

**Evidence:** NOTES.md:15-17 'Decrypted by George Lasry'; NOTES.md:21-27 'It reads R73 but gives nonsense on R72 ... a different letter assignment'; profile credits lasry role 'key or decipherment used'; no outcome.parts; README.md:336

### dubellay  (Lasry entry)

**Verdict:** MIXED  
**Lasry:** prior solution (re-solved the 1528 cipher in 2022, GL.htm) - credited on a profile whose documents are all 1529

| Key / cipher | Documents | Outcome |
|---|---|---|
| Bayonne's cipher (1529), Tomokiyo table from Clair. 333, extended | 16jun1529 (fr. 3078 no. 3, R3688), 22jun1529 (fr. 3078 no. 4), 17oct1529 (R3691), 30jun1529 (fr. 3040 f. 68, R4229), 22oct1529 (fr. 3005 f. 165) | read from existing decipherment (Le Grand 1688, Scheurer 1969, interlinear); 16 June block 98.5% |
| du Bellay's 'first' cipher of 1528 (key recovered by Bourrilly & de Vaissiere 1905; re-solved by Lasry 2022 as 'Bayonne's Cipher (1528-1529)') | fr. 3077 no. 23 (28 Oct 1528, = Clair. 328 f. 291, DECODE R2287); 21 Oct 1528 stretch; named in README row and profile title but not in profile documents[] | read from existing decipherment (Bourrilly 1905 prints in clear); nothing done here |

**After George's review:** Resolved after George's review: Tomokiyo (GL.htm, francis.htm) distinguishes the 1528(-29) cipher George re-solved in 2022 from Bayonne's 1529 cipher (NOTES.md:41-55). Two keys; the profile documents are all 1529, so George's credit sits on documents outside his key. Scope the credit to the 1528 key.

**Where it is merged:** Profile title and README row (README.md:364) say '1528-29 ... fr. 3077 nos. 18, 23', and outcome.credits include Bourrilly ('28 Oct 1528 cipher') and Lasry ('re-solved the 1528 cipher in 2022'), but documents[] and system.summary cover only Bayonne's cipher of 1529. NOTES calls the 1528 cipher du Bellay's 'first' cipher (NOTES.md:43) yet Lasry's table title spans 1528-1529 (NOTES.md:46), so whether 1528 and 1529 are one key with revisions or two keys is not settled in the files. Page h1 says only 'London 1529'.

**Risk:** Lasry is credited as prior solver on a profile whose listed ciphertexts he did not (per the files) work on; the paper's prior-solution/contamination field for the 1529 letters is wrong if the 1528 key is different; README credits Bourrilly's 1528 key recovery to a 1529-cipher entry.

**Proposed fix:** Compare Bourrilly's 1528 key / Lasry's GL.htm table with Tomokiyo's 1529 table. If two keys: either add the 28 Oct 1528 letter as a document with its own outcome.parts entry (1528 key, read from existing decipherment, Bourrilly 1905; Lasry 2022 prior solution) or drop it and move the Bourrilly/Lasry credits off; retitle the README row to the 1529 cipher. If one key: say so in system.summary and list R2287 as a document.

**Evidence:** targets/dubellay/NOTES.md:41-46 'recovered the lost key of du Bellay's first cipher'; NOTES.md:55 'Bayonne's Cipher (1529)'; profile.json credits lasry 'prior solution ... re-solved the 1528 cipher'; README.md:364 'fr. 3077 nos. 18, 23 ... 1528-29'; docs/dubellay.html h1 'London 1529'

### esp318  (Lasry entry)

**Verdict:** MIXED  
**Lasry:** key or decipherment used (no. 95 alphabet, 2022)

| Key / cipher | Documents | Outcome |
|---|---|---|
| EscrivÃ  no. 1 key | no. 5 (ff. 5-6v, 11 Jan 1497) | read from existing decipherment (Parisi 2020) |
| Cifra general de los RRCC (Galende DÃ­az 1994) | no. 92 (f. 116r-v, 17 Aug 1500) | read with known key, ~3/4 |
| Lasry 2022 alphabet (no. 95) | no. 95 (f. 122r-v, 8 Jan 1497) | read with known key in stretches, ~2/3 of f. 122r; f. 122v unread |
| suspected Gran cifra 1501-04 (not obtained) | nos. 93, 94 | not solved |

**After George's review:** Per George: separate nos. 5, 92 and 95; his alphabet applies to no. 95 only. Keep nos. 93 and 94 unresolved until their key relationship is established; "four keys" is not a verified count.

**Where it is merged:** Grouped by volume (BnF Espagnol 318 / catalogue item 9). Profile has one system block ('a different key per letter', system.notes 'Five letters under at least four keys'), one outcome.method 'read with known key', one fraction_read 0.4 (an estimate by letter averaging five keys), no outcome.parts; one README row (README.md:298) and one page. Page sections per letter (no5, no92, no95, no9394) do separate them, but the profile/README do not.

**Risk:** Paper data credits a single 'read with known key' outcome across letters where no. 5 is a prior print, no. 92 a Galende key, no. 95 Lasry's key and 93/94 unread; the 0.4 fraction mixes keys; Lasry's key credit at entry level may read as covering nos. 92-94; system.nomenclator entries 683 is the Cifra general count applied to all.

**Proposed fix:** Add outcome.parts per letter/key (no. 5 read from existing decipherment; no. 92 read with known key Cifra general; no. 95 read with known key Lasry 2022, partial; nos. 93-94 not solved); scope Lasry's credit to no. 95; or split into esp318-no92, esp318-no95 (Lasry), esp318-no93-94, with no. 5 as prior-solved note.

**Evidence:** profile system.summary 'a different key per letter'; system.notes 'Five letters under at least four keys'; outcome.notes fraction 'an estimate by letter'; NOTES.md:139-142, 176-178

### gramont1529  (Lasry entry)

**Verdict:** MIXED  
**Lasry:** key or decipherment used (2023 GL.htm tables, all four keys); prior solution (decoded all four texts 2023, unpublished)

| Key / cipher | Documents | Outcome |
|---|---|---|
| Avranches' cipher 1 (= Tomokiyo fr. 3005 f. 107) | langeac1529 = BnF fr. 3083 no. 8 ff. 20-21 (Langeac, Venice, 14 Jan 1529) | read with known key (Lasry); read in full bar two short groups |
| Gramont's cipher (1529) (= fr. 3040 f. 16, Clair. 330 f. 53) | gramont1529 = fr. 3091 no. 23 ff. 45r-47v (11 Oct 1529) | read with known key (Lasry); read in full |
| Gramont's cipher (1530) (= fr. 3019 f. 20) | gramont1530 = fr. 3071 no. 7 f. 17 (21 July 1530) | read with known key (Lasry); ~85% |
| Mascon's cipher (= fr. 3053; same key as target rome1536) | macon1537 = fr. 3071 no. 4 ff. 9-10 (11 Apr 1537) | read with known key (Lasry); ~90%; f. 9bis contemporary slip agrees |

**After George's review:** Confirmed by George: four keys (Avranches 1, Gramont 1529, Gramont 1530, Mascon). The Mâcon letter belongs with the matching Mâcon subgroup of rome1536, not with the whole mixed target.

**Where it is merged:** Four letters by three writers in four different keys grouped only as catalogue item 6 / recipient Montmorency. profile.json has one system (system.summary 'Four separate keys, each a homophonic substitution...' profile; system.types merged), one outcome.method 'read with known key' and outcome.parts = null, fraction_read 'unknown'. README row (README.md:267) is one row 'complete' for 'Gramont, MÃ¢con and Langeac'. The page does have one h2 per letter (langeac, tarbes, cardinal, macon), so the per-letter reading is visible, but nothing per key in the profile. The MÃ¢con 1537 letter is in Mascon's cipher, the same key as rome1536 (fr. 3053), yet sits in a different entry from its key-siblings.

**Risk:** Paper statistics treat four keys as one 'system' and one solve; key-level counts (number of Lasry keys applied) are undercounted by 3; the 'read'/complete status hides that Gramont 1530 is ~85% and MÃ¢con ~90%; Mascon's cipher is reported under two targets (gramont1529 and rome1536) with no cross-link at key level, so its statistics and corrections (rome1536 'split by sign shape', curly X = Q/U) may not be applied to the 1537 letter.

**Proposed fix:** Add outcome.parts with one part per key (Avranches 1, Gramont 1529, Gramont 1530, Mascon) each with records, method, extent and measured fraction; or split into four profiles. Preferably move fr. 3071 no. 4 (MÃ¢con 1537) to the Mascon's-cipher entry with rome1536 (or cross-reference it there as a part). README: one row per key or at least name the four keys in the row title.

**Evidence:** targets/gramont1529/NOTES.md:7 'each letter has its own key'; NOTES.md:15-18 key table; profile.json system.summary 'Four separate keys'; outcome.parts null; README.md:267 'Four letters, four keys (not three)'; NOTES.md:18 macon key = "Mascon's cipher" (= fr. 3053)

### hm1645  (Lasry entry)

**Verdict:** MIXED  
**Lasry:** key or decipherment used (four reconstructed keys + plaintexts on DECODE, 2020); effectively prior solution of all six

| Key / cipher | Documents | Outcome |
|---|---|---|
| Lasry 'TNA SP 106' (Sept 1645, homophonic, words 124+) | R785 (ff. 213-215), R790 (ff. 230-232), R923 (ff. 233-234) | read from Lasry's existing decipherment; not checked here |
| Lasry 'SP106-2' (July-Aug 1645, homophonic with nomenclator) | R787 (ff. 216-217, French) | read from Lasry's existing decipherment; not checked here |
| Lasry 'SP106-8' (Jan 1646, numbered word list 100+) | R924 (ff. 235-236) | read from Lasry's existing decipherment; not checked here |
| Lasry 'SP106-5' (Jan 1646, letter+digit nomenclator; also the King-Queen key used for rupert1645) | R929 (f. 247) | key applied here independently to Pettersson's transcription; matches Lasry's plaintext |

**After George's review:** Confirmed by George from his original files: four keys (SP106, SP106-2, SP106-5, SP106-8). Distinguish applying a supplied key (SP106-5 on R929, done here) from reproducing his existing decipherments (the other five letters).

**Where it is merged:** Six letters in four of Lasry's keys grouped by correspondence (household -> Charles I) and volume (SP 106/10 ff. 213-247). NOTES has a clear per-record key table and the page has a 'letters and the keys' section, but profile.json has one system (summary 'four key periods per Lasry'), parts = null, one outcome.method 'read with known key' and class 'already solved' for all six; documents[] carry no key. The only check done here (SP106-5 on R929) is reported as if for the target. Siblings R752, R788, R789, R925, R928 (catalogue 54, 55, 60) are declared 'resolved' (outcome.notes) without being documents.

**Risk:** Method 'read with known key' suggests the project applied keys to all six; it applied one key to one letter and took Lasry's plaintexts for five (method should be 'read from existing decipherment' for those). Per-key Lasry credit is lost for the paper; catalogue 54/55/60 closed with no record in the profile.

**Proposed fix:** Add outcome.parts per Lasry key (TNA SP 106: R785, R790, R923; SP106-2: R787; SP106-8: R924; SP106-5: R929) with method 'read from existing decipherment' for the five unchecked and 'read with known key' for R929; list the sibling records or give them their own entries.

**Evidence:** targets/hm1645/NOTES.md:13-17 four keys 'one per key period'; NOTES.md table rows R785 ... 'TNA SP 106', R787 'SP106-2', R924 'SP106-8', R929 'SP106-5'; NOTES 'Check done here: Applied Lasry's SP106-5 alphabet to ... f. 247 (R929)'; profile.json outcome.parts null, method 'read with known key'

### louis1615  (Lasry entry)

**Verdict:** MIXED  
**Lasry:** prior solution of R2748 (Sabran 1631 cipher, 2022)

| Key / cipher | Documents | Outcome |
|---|---|---|
| Louis XIII-Sabran cipher of 1631 (letters, digits, signs; Lasry's key on cryptiana GL.htm) | R2748, BnF Baluze 155 f. 79-80, 28 Mar 1631 | solved by Lasry 2022 (read from existing decipherment; key not re-applied here) |
| Brulart de Leon cipher of 1615-18 (figures with diacritics; Tomokiyo's reconstruction) | R2785 (fr. 18043 f. 83-84, 15 Sep 1615), R2786 (fr. 18044 f. 109-110, 25 Jul 1617) | read by Tomokiyo 2021, residue unread (probably nulls) |

**After George's review:** Confirmed by George: Sabran R2748 and Brûlart R2785/R2786 need separate key entries.

**Where it is merged:** NOTES itself says 'The catalogue grouped three unrelated items because DECODE lists all three with Louis XIII as author' (NOTES.md:9), yet one profile holds both keys: system.summary 'Two different keys', system.types merged, one outcome.method 'read from existing decipherment', fraction_read 'unknown', no outcome.parts; title joins Sabran 1631 and Brulart 1615/1617. No page or README row (Status: no write-up), but the profile still feeds the paper data.

**Risk:** In the paper export one record credits Lasry and Tomokiyo jointly for a 3-document target; Lasry's 1631 solution is counted together with Tomokiyo's 1615-17 work, and the 1615-17 residue (unread passages) is hidden under the same outcome; system statistics (types, symbol kind) mix two unrelated ciphers.

**Proposed fix:** Split into two folders/profiles: sabran1631 (R2748, Lasry prior solution, sibling fr. 4134/4135) and brulart1615 (R2785, R2786, Tomokiyo). Or at minimum add outcome.parts per key with records and credit each solver only on his part.

**Evidence:** NOTES.md:9 'The catalogue grouped three unrelated items'; NOTES.md:11-15 table (R2748 Lasry 2022; R2785/R2786 Tomokiyo 2021); profile system.summary 'Two different keys: the Brulart de Leon cipher of 1615-18 ... and the 1631 Sabran cipher'; outcome.parts null; credits tomokiyo + lasry

### matignon1586  (Lasry entry)

**Verdict:** MIXED  
**Lasry:** prior solution credit for fr. 15572 f. 43 (2022), a leaf excluded from the target

| Key / cipher | Documents | Outcome |
|---|---|---|
| Mayenne-Forget Cipher-1 (Tomokiyo partial tables, re-derived) | fr. 15572 ff. 110, 123-124, 143r/v, 150, 154, 173, 196, 201; fr. 15571 f. 177 (all 13 profile documents) | read with known key, read in part, 28% measured |
| Matignon Cipher-3 (Tomokiyo partial table) | fr. 15572 f. 276; fr. 15571 f. 179 (not in documents[]; f276/, f179/) | read with known key by alejandrozarco PR #25, 96.2% and 92.9%, not in the total |
| Mayenne-Forget Cipher-2 (f. 79r crib) | mentioned only (NOTES:25, :271) | not part of the reading |

**After George's review:** Corrected after George's review: f. 79r is Cipher-1, not Cipher-2 (NOTES.md:264 withdraws the earlier claim). Genuine Cipher-2 material is fr. 15572 ff. 218-219 (NOTES.md:24). Two active reading groups (Cipher-1, Cipher-3); Cipher-2 is a third only if ff. 218-219 stay in scope. Recalculate the percentages after separating them.

**Where it is merged:** One README row (README.md:303) and one target cover Cipher-1 and Cipher-3: the row says 'Partial, in progress (28% measured)' for Cipher-1 then appends 'Matignon's Cipher-3 leaves added ... f. 276 deciphered (96.2%)'. profile.json has no outcome.parts; documents[] lists only Cipher-1 leaves while outcome.credits carries zarco's Cipher-3 solution and Lasry's f. 43 prior solution, so credits describe documents not in the record. Title says 'in Mayenne-Forget Cipher-1' but the folder/row hold Cipher-3 too.

**Risk:** Paper data: zarco's Cipher-3 96% reading and Lasry's f. 43 credit attach to a Cipher-1 profile whose fraction 0.28 and method describe a different key; per-key statistics (Cipher-3 near-complete vs Cipher-1 28%) are blurred; Lasry appears as prior solver of a target he did not solve.

**Proposed fix:** Split Cipher-3 (ff. 276, fr. 15571 f. 179, with the deciphered siblings ff. 189, 277-280, 282) into its own folder/profile/README row (e.g. matignon1586c3) credited to zarco + Tomokiyo; keep matignon1586 Cipher-1 only; move Lasry's f. 43 credit out (or to a note, role 'pointer'), or give f. 43 its own record if it is a separate key.

**Evidence:** profile title 'in Mayenne-Forget Cipher-1'; NOTES.md:5-6 'Cipher-3 leaves f. 276 ... measured separately ... not yet in the total'; NOTES.md:21-23; NOTES.md:327-328; README.md:303; profile outcome.parts null; credits zarco 'Cipher-3 leaves f. 276 deciphered' and lasry 'f. 43 ... (left out of this target)'

### morosini1588  (Lasry entry)

**Verdict:** MIXED  
**Lasry:** key or decipherment used (partial Meister-40 reconstruction on R18, and the F22b key for R53/R54) - one credit spanning two keys

| Key / cipher | Documents | Outcome |
|---|---|---|
| Meister 1906 no. 40 (Morosini 1587) | 34 enclosures R18-R22, R27-R49, R51, R52, R55-R58 | read with known key, ~99.4% of digits |
| F22b second syllabic key (Lasry partial, ~70 elements) | R53, R54 (items 22/32-33, spring 1589) | R53 not decoded, R54 read in part; blocker no-key-material, but key-rebuild escalation not done |

**Where it is merged:** Two keys are in one profile/README row/page with one method ('read with known key'), one fraction_read 0.99 and one 'read' badge; outcome.parts is null. The single lasry credit covers both his Meister-40 partial reconstruction and his F22b key.

**Risk:** medium: the F22b part (a distinct key, essentially unsolved) disappears into a 99% 'read' result; Lasry's F22b contribution is merged with the Meister-key credit.

**Proposed fix:** Add outcome.parts: part 1 Meister-40 (34 docs, read with known key, 0.994); part 2 F22b (R53/R54, read in part/not solved, method from Lasry's partial key). Split the lasry credit into two (one per key). Give the page a separate section for the F22b letters and a separate README line or part.

**Evidence:** targets/morosini1588/NOTES.md:8-9 'R53, R54 ... are in a second key reconstructed only in part by Lasry'; :33 'Second key (F22b ...): syllabic'; profile.json outcome.fraction_read 0.99, parts null; README.md:275 single row

### riksarkivet1628  (Lasry entry)

**Verdict:** MIXED  
**Lasry:** solution of R4282 (in the separate target decode4282, 14 Oct 2026); not reflected here

| Key / cipher | Documents | Outcome |
|---|---|---|
| Bremen band key (6-column grid homophones) | R4330, R4331 (Bremen -> Salvius 1631) | key from adjacent plaintext (glosses), read in full |
| ~40-sign letter cipher | R4282 (lada II:113) | here 'not read'/'open'; actually key recovered ciphertext-only by Lasry, read (targets/decode4282, README row 58) |
| homophonic numbers (108 values) | R4284 (1628, Camerarius) | not solved |
| numbers 5-203 | R4306 (1632?) | not solved |
| Rusdorff numeric code | R4333-R4337 | surveyed, not worked (not in documents[]) |
| E 708 two-digit letter code + 4-digit nomenclator | R4338-R4341 | read in part at the time, not worked (not in documents[]) |

**After George's review:** Corrected after George's review: the profile exporter leaves out contributed results (docs/_export_profiles.py:36), so decode4282 is excluded and the paper data keeps only the stale "not read" R4282 row here. It is not counted twice; the reading is missing. Fix: remove R4282 from this entry and point to decode4282 as its canonical entry.

**Where it is merged:** Catalogue 207 grouped by archive ('four unrelated groups', NOTES.md:8). system.summary describes only the Bremen key; one outcome.method 'key recovered based on adjacent plaintext' for all; no outcome.parts; fraction_read 0.30 pools Bremen with three unrelated ciphers; page h2 'The three ciphers not solved' and NOTES.md:69 still list R4282 as unsolved/not-attempted although Lasry's decode4282 reads it.

**Risk:** Contradiction on Lasry's own solve: R4282 is 'not read' here and 'key recovered from ciphertext-only' in decode4282, so it is double counted with opposite outcomes in the paper data; README row 198 reads as one result for 14 records.

**Proposed fix:** Retitle riksarkivet1628 to Bremen 1631 (R4330/31) only, or turn it into a research/ survey; remove R4282 from documents (point to decode4282); give R4284 and R4306 their own attempted/open entries (or parts with 'not solved'); update page section 04 and NOTES gaps.

**Evidence:** profile system.summary 'Bremen 1631: two-digit homophonic ...'; documents R4282 read='not read'; NOTES.md:8 'four unrelated groups'; NOTES.md:69 'R4282 ... blocker: not-attempted'; docs/riksarkivet1628.html:80; README.md:58 (decode4282, 'Contributed by George Lasry'); docs/_build_site.py:712

### rohan1636  (Lasry entry)

**Verdict:** MIXED  
**Lasry:** readings of fr. 3758 nos. 100 and 104 (filed as louis1635, chatillon1635); not credited here

| Key / cipher | Documents | Outcome |
|---|---|---|
| unknown Rohan 1636 cipher(s) | BnF fr. 5190 nos. 171-172 (d'Emery and Rohan's reply), nos. 214-215 (Savoy, Canisy; printed deciphered 1758) | not solved; ciphertext not in hand |
| Louis XIII's cipher with the marshals (Lasry read it) | BnF fr. 3758 no. 100, 30 Jun 1635 | here: not solved; Lasry: 74.7% (louis1635) |
| Breze-Servien 'German journey' cipher | BnF fr. 3758 no. 104, 3 Aug 1635 | here: not solved; Lasry: 93.7% (chatillon1635) |

**Where it is merged:** one catalogue entry, profile and page join at least three correspondences in different (unknown) ciphers because they concern the same campaign: the Rohan/Valtellina letters of 1636 and two Franco-Dutch letters of 1635, one of which says it uses the Breze-Servien cipher. The page itself says it is not known whether d'Emery used the same key. The fr. 3758 letters are now read by Lasry and filed as louis1635/chatillon1635, but this profile still lists them as documents with method 'not solved', fraction 0 and gaps 'no-key-material': the same two letters are counted twice with contradictory outcomes

**Risk:** high: double-counted documents in the paper data; stale 'not deciphered' claim on the public page

**Proposed fix:** drop fr. 3758 nos. 100/104 from rohan1636 (pointer to louis1635 and chatillon1635); keep rohan1636 for the fr. 5190 Rohan letters only, and keep d'Emery apart from Savoy/Canisy unless a shared key is shown; update page, README row 386 and profile

**Evidence:** targets/rohan1636/NOTES.md:6-10 'George Lasry ... deciphered both Francais 3758 letters ... filed as targets/louis1635 and targets/chatillon1635 ... This target's own outcome is unchanged'; NOTES gaps 'no-key-material'; docs/rohan1636.html s.02 'nor whether d'Emery used the same key'; s.04 'Breze then gave him the cipher the two had used on their German journey'

### rome1536  (Lasry entry)

**Verdict:** MIXED  
**Lasry:** key or decipherment used (2023 re-tabulation of Mascon's cipher, GL.htm)

| Key / cipher | Documents | Outcome |
|---|---|---|
| Mascon's cipher (Tomokiyo reconstruction, Lasry 2023 table) | R4233, R4234, R4235, R4238, R4239, R4240, R4247 (BnF fr. 3053 ff. 6, 16, 21, 32, 35, 40, 77) | read with known key, read in part (~95% after pass 5) |
| second, unrelated fr. 3053 cipher (Tomokiyo's second fr. 3053 table) | R4248 (fr. 3053 f. 85; decipherment f. 86) | read from existing decipherment (contemporary clear decipherment f. 86); key not tabulated |

**After George's review:** Confirmed by George: separate R4248 from the Mascon-key documents; its contemporary decipherment and different assignments do not belong under his Mascon-key credit.

**Where it is merged:** profile.json has one system ('Homophonic substitution on digit-like graphic signs...' i.e. Mascon's only; notes add 'The f. 85 record (R4248) uses a second, unrelated fr. 3053 cipher'), one outcome.method 'read with known key' and parts = null, so R4248 is credited as read with Mascon's key (Tomokiyo/Lasry) although it was read from the f. 86 contemporary decipherment. fraction_read 0.95 mixes both. README.md:291 says 'every cipher passage of the eight records deciphered, seven in part; the eighth resolved'. The page does have a separate h2 id='second'. The Mascon's-cipher letter of 11 Apr 1537 (fr. 3071 no. 4) is filed under gramont1529 instead.

**Risk:** R4248 counted as a document read with Lasry's/Tomokiyo's Mascon key and with the same method; its glyph count and the system's distinct_symbols=50 could absorb a different cipher; paper's method tallies wrong for one document.

**Proposed fix:** Add outcome.parts: (1) Mascon's cipher, R4233-R4247, read with known key, partial ~95%; (2) second fr. 3053 cipher, R4248, read from existing decipherment, complete. Or move R4248 to its own small target. Cross-reference / move gramont1529's macon1537 document here as a Mascon's-cipher part.

**Evidence:** targets/rome1536/NOTES.md:13-14 'its cipher is not MÃ¢con's at all but a second fr. 3053 cipher'; NOTES.md:160-161 'MÃ¢con's key gives nonsense'; profile.json system.notes; outcome.parts null; docs/rome1536.html h2#second

### segur  (Lasry entry)

**Verdict:** MIXED  
**Lasry:** prior solution (unpublished 2024, scope not stated per folio)

| Key / cipher | Documents | Outcome |
|---|---|---|
| Navarre 1585-86 key A (letters 1-53, syllabary 54-123), recovered here | ff. 233, 239, 288v (f. 366 'probably this key', open) | key recovered from ciphertext-only; read in substance |
| Tomokiyo's f. 321 key (same design, letters shifted +8, syllabary 63-142, adds h/j rows) | f. 333 (and f. 321 key letter) | read with known key (Tomokiyo), extended by 24=f,34=l,36=m; blind re-derivation only under design assumption |
| f. 143 (1583) third key | f. 143 (not in documents[]) | not read |

**After George's review:** Per George: his saved decryptions (15 Oct 2024) cover ff. 143, 233, 239 and 288v. NOTES.md:7,150 say f. 143 is in a different key of the same design, so his 2024 work spans two keys. Ff. 321/333 use a third key (Tomokiyo: the f. 321 key reads f. 333). Keep his credit to the documented folios; do not extend it to ff. 321, 333 or 366. Open question below.

**Where it is merged:** profile documents[] includes f333 alongside f233/f239/f288v/f366 under one system (summary gives key A's numbers 1-53/54-123 only) and one outcome.method 'key recovered from ciphertext-only', class 'read', no outcome.parts. f. 333 was read with Tomokiyo's different key (NOTES.md:152, :169, :175 'the f. 321 key is the ff. 233 key shifted'). f366 is unread but counted in the 'read' entry. README row (README.md:89) correctly names only ff. 233/239/288v, but page (docs/segur.html h3 'The rest of the volume, f. 333 and f. 366') and profile fold f.333 in.

**Risk:** f. 333 is counted as a ciphertext-only recovery in the paper data when it was read with a published key; Lasry's 'prior solution' credit applies to the whole entry including f.333/f.366 although his 2024 solve presumably concerned the Tomokiyo-listed letters; f366 (unread) inflates the 'read' class.

**Proposed fix:** Add outcome.parts: (1) ff. 233/239/288v key A, ciphertext-only; (2) f. 333 Tomokiyo f.321 key, read with known key; (3) f. 366 not solved. Or move f. 333 (and f. 321) to its own entry 'Navarre f.321 key'. Ask Lasry which folios his 2024 solution covers and scope the credit.

**Evidence:** profile sys.sibling_key 'Tomokiyo's f. 321 key (same design, shifted by eight) used to read f. 333'; outcome.notes 'f. 333 read with the sibling key; f. 366 left open'; no outcome.parts; NOTES.md:150-152,169-175

### affry1757

**Verdict:** MIXED

| Key / cipher | Documents | Outcome |
|---|---|---|
| d'Affry nomenclator ~1,200 groups (codes A+B, shown to be one code, key_U.json) | R1052, R1053, R1062-R1065, R1072, R1073, R1075, R1076 (A); R1054, R1066-R1070, R1074, R2067 (B) | key from adjacent plaintext (Lyonet's decipherments), 0.89 read as sense |
| code C (different) | R1071 (to Choiseul, 7 Aug 1757) | not solved |

**Where it is merged:** Grouped by sender and file (KHA inv. 192). Profile documents still list 'codeA' and 'codeB' as separate documents although NOTES.md:31-33 says they are one code; R1071 code C is included under the same method 'key recovered based on adjacent plaintext' with no outcome.parts; fraction 0.82 includes R1071 (0.89 without). system.summary does say 'R1071 in another code'.

**Risk:** Low: R1071's different code is counted under the main code's method and drags the fraction; profile's codeA/codeB split suggests two keys where there is one.

**Proposed fix:** Merge codeA/codeB into one document group (or label them 'one code'), move R1071 into its own attempted/open entry or an outcome.part 'not solved', and report 0.89 for the main code.

**Evidence:** profile system.summary 'R1071 in another code'; NOTES.md:31-33 'the cosine split reflects homophone habits, not two codes ... R1071 (C) is different'; fraction_read_source 'R1071 (761, code C) unread. Without R1071: 0.890'

### beatrice1482

**Verdict:** MIXED

| Key / cipher | Documents | Outcome |
|---|---|---|
| 1482 graphic alphabet (old cipher) | R1140 (31 May 1482), R1141 (8 Jun 1482) | read from existing decipherment (MDE III 1877 nos. 10, 12) |
| 1486 graphic alphabet(s); March 1486 letter says a new key is enclosed, so March and May 1486 may differ | R1142 (8 Mar 1486), R1143 (2 May 1486, decipherment slips) | read from existing decipherment (MDE III no. 54, 75; IV suppl. 45; Berzeviczy 1914) |
| none (plain Italian letter) | R1154 (29 May 1505) | not applicable |

**Where it is merged:** Grouped by sender (Beatrice) and archive. RESULT.md itself warns 'the 1482 and 1486 alphabets look different; the old/new-cipher statement makes pooling all four letters under one key especially unjustified', yet profile has one system (types ['undetermined'], summary 'graphic substitution systems'), parts = null and one method for five records including a non-cipher; README.md:356 one 'complete' row.

**Risk:** Low for credit (all from print), but the paper would count one 'system' where there are two or three plus a non-cipher; R1154 counted as an 'already solved' cipher.

**Proposed fix:** Add outcome.parts: 1482 key (R1140-R1141), 1486 key(s) (R1142-R1143), R1154 not a cipher; or split R1154 out as not-a-cipher and keep per-key parts.

**Evidence:** targets/beatrice1482/RESULT.md:87 'pooling all four letters under one key especially unjustified'; profile.json system.notes 'Cipher alphabets differ; March 1486 closing states a new key is enclosed. R1154 is not a cipher.'; outcome.parts null

### benedict1399

**Verdict:** MIXED

| Key / cipher | Documents | Outcome |
|---|---|---|
| Benedict XIII's one-sign-per-letter substitution (20 values + dotted-V name sign + null separators), rebuilt from the p. 475 facsimile | benedict-1399-1403 (Benedict -> Climent; plate = letter XXXV, doc. 1068) | read from existing decipherment (Puig 1920); key rebuilt here, 91.4% of the plate confirmed |
| unverified: Puig says 'La clave o claves'; the entourage letters may share the key or not | entourage-1399-1416 (Santa Cruz, Exea, Comuel -> Climent, Puig app. XXIX, LXIV, CXVI, CXXXV) | read from existing decipherment (Puig); no image, key not checked on them |
| unknown key ('de clave desconocida') | vico-1398-line (Fr. Pedro de Vico -> Guillem Carbonell, 4 Dec 1398) | not read; not printed, no image |

**Where it is merged:** Grouped by archive (Climent's papers, ACB). One outcome.method 'read from existing decipherment', fraction_read 0.914 measured on the p. 475 plate only, no outcome.parts, while documents[] includes the Vico line in an explicitly different, unknown key (NOTES.md:123) and letters from other senders over 1399-1416 whose key was never checked. Puig's own note says 'La clave o claves' (NOTES.md, p. 466 quote), i.e. possibly more than one key. README row (README.md:340) presents Benedict and 'his circle' as one deciphered set.

**Risk:** The Vico 1398 line (unread, different key) is counted inside a 'read' target; the 91.4% sign-level confirmation and the rebuilt key are implied to cover the entourage letters (to 1416) which were not tested and may use other keys.

**Proposed fix:** Add outcome.parts: (1) Benedict letters, plate-checked key, read from existing decipherment; (2) entourage letters, read from existing decipherment, key unverified; (3) Vico 1398 line, not solved, different key. Or drop the Vico line into a separate open record. Say in system.notes that the key is verified only on doc. 1068.

**Evidence:** NOTES.md:123 'Sigue una lÃ­nea cifrada, de clave desconocida'; NOTES.md Puig p. 466 'La clave o claves que me han servido'; profile outcome.method 'read from existing decipherment', frac 0.914 (plate); documents vico-1398-line read 'not read'; outcome.parts null

### bl32305

**Verdict:** MIXED

| Key / cipher | Documents | Outcome |
|---|---|---|
| Paris 1719 two-part 3-figure code (~900 groups) | R2964 (f. 6), R2965 (f. 7) | not solved; ~12 contemporary glosses (33/354 groups) |
| 'Carre' 1742-45 two-part 3-figure code (~800 groups) | R2968, R2970, R2972 | not solved, 0 read |
| German 'Marquis' letter, figures for names/words | R2963 (f. 5) | read at the time (interlinear); not in documents[] |
| 2-figure letter cipher of 1749 | R2974 (ff. 25-28) | read at the time; not in documents[] |

**Where it is merged:** Grouped by volume (Add MS 32305, 'unidentified cipher keys'). NOTES.md:9-10 'They are not one correspondence'. One profile with system.summary covering two codes jointly, one outcome.method 'not solved', outcome.parts null, and fraction_read 0.09 that counts only the 1719 glosses (outcome.notes) but stands for the whole two-code set. credits 'R2963 and R2974 deciphered at the time' refer to records not in documents[]. README row (README.md:401) and page title join 1719 and Carre, date range '7 Feb 1719 - 17 Nov 1749' runs to R2974.

**Risk:** The 9% 'read' is applied to the Carre code, of which nothing is read; credits for R2963/R2974 readings attach to a target whose documents are all unread; two codes' sizes (900 vs 800) and stats blended.

**Proposed fix:** Split into bl32305-1719 (R2964/R2965, glosses 9%) and bl32305-carre (R2968/R2970/R2972, 0%); or add outcome.parts per code with own fraction_read; record R2963/R2974 as separate read-at-the-time documents or drop them from credits.

**Evidence:** NOTES.md:9-10 'They are not one correspondence'; NOTES.md:14,25,31; profile outcome.notes 'fraction_read counts the contemporary glosses in R2964 (33 of 354 groups)'; outcome.parts null; README.md:401

### caprile1519

**Verdict:** MIXED

| Key / cipher | Documents | Outcome |
|---|---|---|
| 1520-21 homophonic sign cipher (rebuilt from Somogyi 2025 cribs) | R1139, R1136 (8 Mar 1520), V1921, R1138 (Somogyi), V1920 | key recovered based on plaintext from external sources; V1921 97.0%, R1139 89.7%, R1136 66.9% |
| 1519 two-tier cipher | R1128 (target); R1129-R1135 read at the time/1882 | R1128 not read; R1129-R1135 read from existing decipherments |
| Cistarelli two-digit numeric cipher | R1137 (catalogue 158, different sender) | fragments only, ciphertext-only anneal; effectively not solved |

**Where it is merged:** Three systems and two senders (catalogue 157 + 158) grouped by archive box (ASMo Ungheria b. 4) and mission. Profile system.types ['homophonic'] and distinct_symbols 49 describe only the 1520-21 cipher; one outcome.method 'key recovered based on plaintext from external sources' and one fraction_read 0.3 (estimated) across all; no outcome.parts. Single README row (README.md:118) and page title 'Caprile and Cistarelli'. NOTES table classes R1128-R1135 as '1519 two-tier' and R1137 'two-digit numeric' (NOTES.md:25-34).

**Risk:** Paper data attributes the external-crib key recovery to R1128 and R1137, which use different ciphers and are unread; Cistarelli (catalogue 158) appears read in part under Caprile's key; system statistics (49 signs, homophonic) misdescribe the 1519 and numeric systems.

**Proposed fix:** Split into caprile1520 (1520-21 key: R1136, R1138, R1139, V1920, V1921), caprile1519 (two-tier: R1128 + R1129-R1135 as key material, open) and cistarelli1520 (R1137, open); at minimum add outcome.parts per system and per-system system blocks.

**Evidence:** profile system.summary '1520-21: homophonic ... 1519: a two-tier sign cipher; Cistarelli: two-digit figure cipher'; outcome.notes 'R1128's two-tier system and R1137's numeric key are not'; NOTES.md:14-15,25-34

### castelcicala1816

**Verdict:** MIXED

| Key / cipher | Documents | Outcome |
|---|---|---|
| Neapolitan two-part syllabic homophonic code (~2,450 groups), key rebuilt from glosses | R9553-R9567, R9569-R9571, R9579, R9582-R9585, R9587, R9589 (25 docs) | key from adjacent plaintext, read in part (45% valued; R9569/R9571/R9589 read at the time) |
| different code, values 100-1100, pencil syllabic glosses | R9586, R9588 | not attempted, not solved |

**Where it is merged:** Mostly one code (catalogues 166+167 merged correctly by code), but R9586/R9588 are a different code included by shared busta/sender; system.summary describes only the main code; no outcome.parts; fraction_read_source says it 'Includes the different-code R9586/R9588'. Minor case.

**Risk:** Small: the two other-code letters dilute the 43% figure and are implicitly labelled with the main code's key and method.

**Proposed fix:** Move R9586/R9588 to a separate attempted/open entry (or an outcome.part 'not solved'), and exclude them from fraction_read.

**Evidence:** NOTES.md:34 'R9586 and R9588 are in a different code'; NOTES.md:126; profile fraction_read_source 'Includes the different-code R9586/R9588'; README.md:190 'R9586/R9588 another code'

### champagne1590

**Verdict:** MIXED

| Key / cipher | Documents | Outcome |
|---|---|---|
| nine-entry name code, key slip bound on f. 36r | n23 = fr. 3623 no. 23 (Bienvenut, 28 Feb 1590, R9453) | read with known key (contemporary slip), complete |
| two-digit alphabetical homophonic alphabet + code numbers | n24-25-60 = fr. 3623 nos. 24, 25, 60 (June 1590, R9454, R9455, R9459) | key recovered based on adjacent plaintext (interlinear glosses), partial 63/104 |
| Nevers key no. 57 (fr. 3995 ff. 102-103, La Verriere/Lauriere, Feb 1593) | n55 = fr. 3625 no. 55 (9 Jul 1593); fr. 3625 no. 10 (13 Jul 1593, blind test, not a profile document); f3985_58 = fr. 3985 f. 58 (12 Aug 1593) | read with known key (identified by setsunaatto, issue 13); no. 55 85/86, f. 58 94.8% |
| unknown (one group of ~6 signs) | n78 = fr. 3623 no. 78 (1591, R9460) | not solved (too short) |

**Where it is merged:** Four systems from different writers and years (1590 news-letters vs Lauriere's 1593 letters in three other volumes) in one target under catalogue item 30 / recipient Nevers. outcome.parts = null; one outcome.method 'key recovered based on adjacent plaintext' (true only for nos. 24/25/60); one fraction 0.863 ('All counted letters: 383 of 444') pooled across keys; system.summary describes only no. 23 and 24/25/60 (key 57 only in system.notes). Page h1 'Champagne news letters ... 1590-91' though half the reading is Lauriere 1593 with key 57. README (README.md:196) one 'partial' row. Page sections are per letter, so a reader can follow, but the record cannot.

**Risk:** setsunaatto's key-57 reading is filed under an 'adjacent plaintext' method; 86.3% merges a known-key reading (~95%) with a partly rebuilt key (61%); key 57's documents and statistics hidden; no. 10 used as a test but not listed.

**Proposed fix:** Add outcome.parts per key (name code no. 23; alphabetical 2-digit table nos. 24/25/60; key no. 57 nos. 55, 10, f. 58; no. 78 unread). Better: split Lauriere/La Verriere 1593 (key no. 57) into its own target and retitle; one README row per key.

**Evidence:** targets/champagne1590/profile.json system.summary 'No. 23: a small name code ...; nos. 24/25/60: a two-digit homophonic alphabet'; system.notes 'No. 55 ... is Nevers key no. 57'; NOTES.md:340-341 'key no. 57 ... give no sense ... they use a different, alphabetical two-digit system'; outcome.parts null; docs/champagne1590.html h1 '1590-91'

### dedem1788

**Verdict:** MIXED

| Key / cipher | Documents | Outcome |
|---|---|---|
| 1788-93 homophonic code (R2120, R2122, R2131) |  |  |
| R1895 1799 Croiset-style marked system |  |  |

**Where it is merged:** R1895 in a different system placed in the same entry

**Risk:** Low: R1895 unread, outcome not solved/0

**Proposed fix:** Move R1895 to its own entry

**Evidence:** system.summary: "R1895 (1799) uses a different marked system"

### deswart1782

**Verdict:** MIXED

| Key / cipher | Documents | Outcome |
|---|---|---|
| Croiset 1765 Russia-legation codebook (DECODE R1038) | R1036 (whole) + R1040 from group 180 of image 5459 to the end | read after matching with external key: R1036 96.7%; R1040 second segment 84-90%/page |
| missing Rechteren-family nomenclator (NA inv. 158?) | R1040, first 1,928 groups | not solved |

**Where it is merged:** R1040 changes codebook mid-letter; its first 1,928 groups are in another key, yet R1040 sits in documents[] as one document with no outcome.parts, and the README row gives extent 'complete'. The page does separate it (section 04), and the profile notes say so in prose

**Risk:** medium: paper data counts R1040 as one document in the Croiset key; the Rechteren segment belongs with the Rechteren key family (rechteren1785 R1039 / R2032, R2051, R2052)

**Proposed fix:** split R1040 into two passage entries in profile (outcome.parts per key: Croiset segment read, Rechteren segment not solved); README extent per key; cross-reference the Rechteren segment to the Rechteren-code entry rather than counting it here

**Evidence:** targets/deswart1782/NOTES.md:146-150 'coded ... with two codebooks. The switch point is at group 180 of image 5459 ... The first 1,928 groups use a missing Rechteren-family nomenclator'; profile outcome.parts null; README.md:218 extent 'complete'

### foix1563

**Verdict:** MIXED

| Key / cipher | Documents | Outcome |
|---|---|---|
| R9238 Coligny/Conde graphic-sign cipher (R335) |  |  |
| R9241 Catherine-Foix Latin letters+digits cipher, not Forbes key |  |  |

**Where it is merged:** Two letters in different ciphers in one entry

**Risk:** Low: fraction 0, R9238 only matched to print, R9241 open

**Proposed fix:** Split into R9238 and R9241 entries

**Evidence:** NOTES: R9241 sign values do not match; types unknown

### geertruidenberg

**Verdict:** MIXED

| Key / cipher | Documents | Outcome |
|---|---|---|
| Torcy's two-part code of 800+ values with homophones (values to 823) | torcy, BL Add MS 61575 ff. 38-41 (R8755), 3 Apr 1710 | not solved |
| Villars' smaller code (values to 560) | villars, BL Add MS 61575 f. 44 (R8756), 1 Jun 1710 | not solved |

**Where it is merged:** Grouped by volume/recipient (Geertruidenberg conference, Add MS 61575). profile system.summary 'Two different numerical codes'; one outcome.method 'not solved', no outcome.parts; one page and one README row (README.md:377) 'no key fits either code'.

**Risk:** Low because both are unread and the README says 'a different code'. Risk: system statistics (types, symbol counts) and any future reading of one code would be credited to the pair; paper counts one target where there are two ciphertext-only problems of different size.

**Proposed fix:** Add outcome.parts per code (Torcy R8755 / Villars R8756, both not solved) and per-code length fields; split into two folders if either is ever read.

**Evidence:** profile system.summary 'Two different numerical codes. Torcy ... Villars: a smaller code'; outcome.parts null; README.md:377 'Villars: 173 groups ... a different code'

### guiche1551

**Verdict:** MIXED

| Key / cipher | Documents | Outcome |
|---|---|---|
| La Guiche 22-sign simple substitution |  |  |
| Noailles 1558 other symbol alphabet |  |  |
| Seure 1558 homophonic ~60 signs + numeral codes |  |  |

**Where it is merged:** 3 letters in 3 different ciphers under one entry; fraction_read 0.17 pools them

**Risk:** High: one outcome/fraction for three keys

**Proposed fix:** Split into guiche1551 / noailles1558 / seure1558 entries or score La Guiche only

**Evidence:** profile system.notes: Noailles and Seure use other symbol alphabets; outcome.notes pools signs

### heidelberg597

**Verdict:** MIXED

| Key / cipher | Documents | Outcome |
|---|---|---|
| Key A, the compiler's 24-sign 'new abc' (f. 1r) | f. 1r ll. 3-4, recipe names ff. 7r-22r, 46r-v, 54r-61r, f. 5v-6r mixed | read from existing decipherment (Wattenbach 1869), alphabet recovered from images |
| Key B, stroke and figure signs (ff. 6v, 91v) | f. 6v invocation, f. 91v | read from existing decipherment (Wattenbach 1869) |
| Set C (ff. 1r ll.1-2, 5v-6r, 44v, 93r) | f. 93r, f. 44v, glossary f. 6r | partly fixed from the 2014 catalogue crib (external plaintext); f. 44v and the glossary unread |

**Where it is merged:** Three independent sign alphabets in one manuscript under one profile outcome ('read from existing decipherment', fraction 'unknown', parts null) and one system entry ('Three simple sign alphabets'). The page separates them (#keya, #keyb, #setc), but set C's partial recovery from Kalning's crib and the unread set C passages are absorbed into Wattenbach's 1869 credit.

**Risk:** medium: the method and 'already solved' class overstate set C, which Wattenbach did not fully give and which is only partly read.

**Proposed fix:** Add outcome.parts for key A, key B, set C with their own method/credit/fraction (set C: key recovered based on plaintext from external sources, Kalning 2014 crib, partial).

**Evidence:** targets/heidelberg597/NOTES.md:41-49 survey assigning passages to key A / key B / set C; NOTES.md:90 'lines 1–2 are in set C, lines 3–4 (the alphabet) in key A'; profile.json outcome.method 'read from existing decipherment', parts null

### hellen1752

**Verdict:** MIXED

| Key / cipher | Documents | Outcome |
|---|---|---|
| 1752 code |  |  |
| 1756 code |  |  |
| 1763 code (provisional families) |  |  |

**Where it is merged:** Three provisionally distinct code families in one entry

**Risk:** Low: unsolved, fraction 0

**Proposed fix:** Split by family if any ever read

**Evidence:** NOTES: grouped provisionally into 1752, 1756 and 1763 code families

### hereditary1796

**Verdict:** MIXED

| Key / cipher | Documents | Outcome |
|---|---|---|
| French numbered word-list code (~250 entries) rebuilt from R2237 | R2239 (and R2237 as key source) | key recovered from adjacent plaintext; R2239 read except entry 244 |
| unknown Dutch list(s), numbers to ~390 and ~2835 | R2236 'Copie No 1' and 'Copie No 2' | not solved, not transcribed |

**Where it is merged:** R2236 is said to use another list, yet it is a document of this profile with a single outcome (no outcome.parts, fraction 'unknown'); README row says extent 'complete' and the page summary groups R2236 and R2239 as catalogue item 218. Two unknown/different keys under one entry

**Risk:** medium for paper data (document count and per-document outcome); low on the page, which states R2236 not decrypted

**Proposed fix:** remove R2236 from documents[] (or add outcome.parts: R2239 word-list code read / R2236 other list not solved) and give R2236 its own open catalogue/DECODE entry

**Evidence:** targets/hereditary1796/NOTES.md:20-22 'R2236 ... Not read: its numbers run past the rebuilt list, and the clear words show Dutch. It is probably another list'; profile.json:94 'R2236 uses another list'; README.md:177 'complete'

### ilten1697

**Verdict:** MIXED

| Key / cipher | Documents | Outcome |
|---|---|---|
| code A: numeric syllabic nomenclator, groups to ~505, null 62 (1697) | A, Hattorf -> Ilten, 7 Nov 1697 (Ms XXIII 1245:4 ff. 212-213) | read from existing decipherment (interlinear), read |
| code B: numeric syllabic nomenclator, groups to 1010, null 91 (1705-06) | B (Heusch, Berlin, 10 Oct 1705), C (Hattorf, 31 Jan 1706), D (Elector Georg Ludwig, 25 May 1706) | read from existing decipherment (interlinear), read; 7 unglossed tokens open |

**Where it is merged:** Mild. Grouped by recipient (Ilten) and catalogue 346. profile system.summary names both codes, but one system.types list, one outcome.method, a pooled fraction_read 0.986, no outcome.parts. Page has one 'The codes' section (ilten1697.html:73) and reads per letter.

**Risk:** Low: both codes have the same outcome (interlinear decipherments). Paper statistics (code size, nulls, fraction) blend a ~505-group and a ~1010-group code from different correspondents.

**Proposed fix:** Add outcome.parts per code (A: letter A; B: letters B, C, D) with measured fractions; optionally per-code system notes.

**Evidence:** profile system.summary 'Two numeric syllabic nomenclators: code A ... and code B ...'; NOTES.md:62,65 'Code B is one code for all three later letters'; outcome.parts null

### kaa4591

**Verdict:** MIXED

| Key / cipher | Documents | Outcome |
|---|---|---|
| System A' (R9407 Augurelio key carried over, gloss of R9427) | R9408, R9409, R9410 (f.244r and Latin ff.246-247), R9413, R9427 | key from adjacent plaintext (glosses), read in part 77-90% |
| System B (Laski) | R9322, R9323, R9417 | key from adjacent plaintext (glosses), read (R9323 3/13 lines) |
| key R9324 (letter substitution + nomenclator) | R9325 (Fulda 1576) | read with known key (key filed in the volume), read |
| key R9423 block 2_4 'H. Wilh.' | R9367 (1535) | read with known key + context, read in part |
| R9416 pp.1-2 system (glossed) | R9416 f.262 | read at the time / existing decipherment |
| R9416 pp.3-4 homophonic | R9416 f.263 | key recovered ciphertext-only, read in part (separate README row 102) |
| Latin-letter substitution | R9424 | not solved |
| dot grille | R9319 (1583) | not solved, blocked (cover letters not imaged) |
| none (key fragment) | R9291 | not applicable |

**Where it is merged:** Catalogue entry 161 grouped by volume (the Bavarian key volume). system.summary says 'Not one system: at least six' and types ['unknown']; outcome.parts has only 2 parts and part 1 lumps System A', System B and R9325 (a filed key R9324, i.e. read with known key, not key-from-adjacent-plaintext) under one method; R9367 (key R9423), R9416 f.262 (read at the time), R9424, R9319 have no parts; fraction_read 0.893 has no source and mixes systems; README row 200 is one row for 'fourteen ciphertexts' (R9416 f.263 already split to row 102).

**Risk:** R9325 and R9367 are counted as key recovered from adjacent plaintext when they were read with filed keys; the unread R9424/R9319 vanish inside an 89% figure; per-system difficulty statistics impossible.

**Proposed fix:** Split per system: kaa4591-systemA (R9408-R9413, R9427, with R9368/R9407 siblings), kaa4591-laski (System B: R9322/23/17), kaa4591-r9325 (key R9324), kaa4591-r9367 (key R9423), keep R9416 f.263 separate, list R9424/R9319 as attempted/open entries. At minimum one outcome.parts per system with its own method and measured fraction.

**Evidence:** profile system.summary 'Not one system: at least six'; outcome.parts[0] label 'the glossed systems (A', B) and R9325'; NOTES.md:13-15 'separate letters in at least six systems'; NOTES.md:22 R9325 key 'R9324 (f.124-127)'; NOTES.md:280-286 R9367 key R9423; README.md:200

### kaa4591b

**Verdict:** MIXED

| Key / cipher | Documents | Outcome |
|---|---|---|
| System B (Łaski, e/r swapped; key from glosses on sibling records R9322/R9417 in kaa4591) | R9403 | read with known key (sibling-derived), 99.5% |
| homophonic system L (rebuilt from own gloss + anneal) | R9415 | key recovered from adjacent plaintext, 95.8% |
| homophonic system G (rebuilt from own gloss + anneal) | R9414 | key recovered from adjacent plaintext, 92.2% (under bar) |

**Where it is merged:** Three unrelated keys grouped because they share a volume (KAA 4591) and a catalogue number (162); profile has one system block listing all three, one outcome.method ('key recovered based on adjacent plaintext', wrong for R9403), one pooled fraction 0.946, parts null; README one row 'partial'.

**Risk:** high: pooled fraction hides that two keys pass the read bar and one fails; R9403 method miscategorised; paper counts three keys as one cipher.

**Proposed fix:** Add outcome.parts per key (B/R9403 read with known key 0.995; L/R9415 adjacent plaintext 0.958; G/R9414 adjacent plaintext 0.922) or split into three entries; README row should state per-key outcomes (page already has per-record sections).

**Evidence:** targets/kaa4591b/NOTES.md:16-20 (table: System B / new homophonic L / new homophonic G); profile.json system.summary 'Three graphic-sign ciphers'; profile.json:284 fraction_read 0.946 pooled; outcome.parts null; README.md:191 one row

### legation

**Verdict:** MIXED

| Key / cipher | Documents | Outcome |
|---|---|---|
| JQA's St Petersburg code (the = 1385), rebuilt here | No. 88, 25 Jun 1812 (jqa profile: two passages, same code) | key recovered from adjacent plaintext, 380/390 groups |
| Madrid legation / Pinckney's code (the = 1651) | Erving No. 21, 24 Mar 1807 (erving1807 profile) | read from existing decipherment, holes closed |

**Where it is merged:** profiles and README rows are already separate (jqa README.md:167, erving1807 README.md:343), but the site has one PAGES card/page 'Erving & Adams' with one blurb, one badge (PAGE_PROFILES: the badge takes the first method) and a merged credits line (Ford credited on a page that also holds Erving, which he had no part in)

**Risk:** medium: the card/badge present two different codes as one result; erving1807's method (read from existing decipherment) is hidden behind jqa's

**Proposed fix:** split into two pages (jqa1812, erving1807) with their own cards, badges and credits, or at least per-section method and credit lines. erving1807aug (same Pinckney code) is already its own README row, which is correct

**Evidence:** docs/_methods.py:161-162 '(the badge takes the first method in METHODS order)' PAGE_PROFILES = {'legation': ['jqa', 'erving1807'], ...}; docs/_build_site.py:1356-1358 'Two American legation codes'; docs/legation.html 'Credits · Contemporary ... · Worthington Chauncey Ford'

### maisse1592

**Verdict:** MIXED

| Key / cipher | Documents | Outcome |
|---|---|---|
| Maisse's Cipher (1592), homophonic figure cipher (Tomokiyo henryiv_Maisse1.png) | BnF fr. 16093 ff. 370, 373 | f. 370 read with known key and checked letter for letter against the Brienne 13 clear copy; f. 373 read from the clear copy only |
| Maisse's Cipher (1592-1593), mixed letter-symbol + figure nomenclator, the Breves cipher (henryiv_Maisse2.png) | ff. 404/406, 410 (412 duplicate) | read from existing decipherment (Brienne 13 clear copies); not deciphered with the key |

**Where it is merged:** Grouped by recipient (Henri IV -> Maisse). system.summary and the page ('Four leaves, two ciphers') state the two systems, but there are no outcome.parts; one outcome.method 'read from existing decipherment' and fraction_read 1.0 for both, although only f. 370 (81 characters) was deciphered with a key (NOTES.md:8-11 flags this).

**Risk:** Low-medium: the two ciphers get one outcome; the 1.0 fraction implies the Breves cipher was verified on the leaves when it was not; the Breves cipher sits in a 'Maisse' entry where a search by key (Breves 1593-1602) would miss it.

**Proposed fix:** Add outcome.parts per cipher (ff. 370/373: read with known key for f. 370, existing decipherment for f. 373; ff. 406/410: read from existing decipherment), and set fraction per cipher; or split ff. 406/410 into a Breves-cipher entry.

**Evidence:** profile system.summary 'Two ciphers, not one'; NOTES.md:8-11 'the key was checked letter for letter on f. 370 only'; NOTES.md:157-176; docs/maisse1592.html:61; README.md:338

### michell1751

**Verdict:** MIXED

| Key / cipher | Documents | Outcome |
|---|---|---|
| Frederick II's cabinet code of 1751 to Michell (groups 2-6472) | R1957 (KHA inv. 198) | read from existing decipherment (PC 8 no. 5263 matched), complete; key recovered from external plaintext by WAINUT, partial 69.5% |
| Michell's envoy code (groups 2-5346, half-groups), key material R1050/R1051 | R1955 (ministerial rescript, same day) | read after matching with key from external sources (WAINUT), partial 26.4%, fragments |

**Where it is merged:** Two different Prussian codes grouped by date/route/volume (KHA inv. 198, 28 Dec 1751). outcome.parts does separate them (three parts, R1955 its own), and system.summary says 'Two different Prussian numerical codes'. But top-level outcome.method 'read from existing decipherment', class 'already solved' and the README row (README.md:357) status 'complete', 'Solved earlier by Printed in Politische Correspondenz' sit over R1955, which is not in print and is 26.4% read; outcome.notes still says 'R1955 is attempted, open'. Page title names only the R1957 letter; no h2 for R1955.

**Risk:** README/site badge says R1955 was already solved in print when it was not; scoreboards count it 'complete'.

**Proposed fix:** Either move R1955 to its own target (michell1751-rescript, partial, WAINUT credit) or set README row to 'partial' and name both codes; add a page section for R1955; reconcile outcome.notes ('attempted, open') with parts[2] (read in part).

**Evidence:** targets/michell1751/profile.json system.summary 'Two different Prussian numerical codes'; outcome.parts[2] 'R1955 in Michell's envoy code ... 26.4%'; outcome.notes 'R1955 is attempted, open'; README.md:357 'complete | Solved earlier by Printed in Politische Correspondenz'

### nevers1593

**Verdict:** MIXED

| Key / cipher | Documents | Outcome |
|---|---|---|
| Nevers cipher no. 46 (two-digit alphabet with homophones, barred/plain/dotted word lists; fr. 3995 f. 87) | f209 (fr. 3985 f. 209, 8 Sep 1593), f168 (fr. 3986 f. 168, 14 Oct 1593), to Pisany | read with known key: f209 read, f168 read in part |
| Court symbol cipher no. 60 (symbol alphabet ~5 homophones/letter + syllabary; ff. 108-111) | f88 (fr. 3985 f. 88, 21 Aug), f146v, f157v (to Revol); also ff. 176, 198 named but not in documents[] | f88 read in part (tunarob, issue #32); f146v, f157v not read |

**Where it is merged:** Grouped by sender and catalogue item 21. profile system.notes: 'Two keys in one catalogue item; system fields describe no. 46' (system.types, homophones, nomenclator are no. 46 only). One outcome.method 'read with known key', fraction_read 0.3 estimated 'by letters (2 of 7 read ...)', outcome.parts null. The page separates the keys (nevers1593.html:45 'two letters in the numerical key no. 46, five in the symbol cipher no. 60', section 05 'The letters to Revol and key no. 60'), but the README row (README.md:300) is titled 'Nevers -> Pisany' only and still says of the Revol letters 'none read yet', though f88 is now read in part.

**Risk:** No. 60 letters inherit no. 46's system description and the 'read with known key' method in the paper data; the 30% blends a near-complete no. 46 reading with a barely started no. 60; credits (tunarob key corrections to no. 60, Tomokiyo partial readings of no. 46 letters) are not tied to their key.

**Proposed fix:** Split into nevers1593 (no. 46, Pisany: f209, f168) and nevers1593revol (no. 60: ff. 88, 146v, 157v, 176, 198) with their own system blocks and credits; or at least add outcome.parts per key with measured fractions, and update the README row title and the f88 status.

**Evidence:** profile system.notes 'Two keys in one catalogue item; system fields describe no. 46'; outcome.notes 'fraction_read 0.3 is an estimate by letters'; outcome.parts null; docs/nevers1593.html:45,125; README.md:300 'none read yet'; credits tunarob 'partial reading of f. 88r'

### orpo1942

**Verdict:** MIXED

| Key / cipher | Documents | Outcome |
|---|---|---|
| Doppelkasten daily key of 27 Feb 1942 (4 discriminators WOJ/OSX/ANR/WYY) | D33, D34, E72, D67 (7 parts, 970 letters); possibly C43 (XOS = OSX) | not solved |
| Doppelkasten daily key of 16 Jun 1942 (discriminator ARTTN) | A115 (223 letters) | plaintext exists from Bletchley's decrypt (Hanyok 2005): read at the time / read from existing decipherment; key-free alignment here failed |

**Where it is merged:** Two different daily keys are one entry with one method 'not solved', class 'not read', fraction 0. The 27 Feb grouping is evidenced (shared discriminators), but A115 is a different key whose plaintext is known (Schmeh's 'partially solved' refers to it), so its outcome differs and is hidden in the pooled verdict. The README row covers both dates.

**Risk:** medium-low: per-key outcome lost (A115 effectively read by Bletchley, 27 Feb unread); paper sees a single unsolved Doppelkasten.

**Proposed fix:** outcome.parts: 27 Feb key (not solved, 970 letters) and A115 key (read from existing decipherment by Bletchley, alignment not reproduced); README row/page section per key; decide whether C43 belongs to the 27 Feb key and list it in documents[] if so.

**Evidence:** targets/orpo1942/NOTES.md:30-37 'all seven parts (970 letters) are one key'; :16 'Message A115 has a plaintext: Bletchley's decrypt'; :26 '"partially solved" refers to A115'; README.md:422

### papai1706

**Verdict:** MIXED

| Key / cipher | Documents | Outcome |
|---|---|---|
| Papai envoy key DECODE R580/R581 (Hungarian syllabic nomenclator 10-322) | R740, R741, R757, R765, R784, R793-R796, R805, R823 (11 letters) | read with known key, 99.7% of groups |
| graphic-sign substitution (~25 signs), no key | R731 (6 Mar 1710, Belgrade) | not solved, not reliably transcribed |

**Where it is merged:** Grouped by sender (Papai). system.summary mentions R731's separate alphabet, but there are no outcome.parts; one outcome.method 'read with known key' and fraction 0.97 adds R731's ~330 signs as unread to the R580 groups. README row 293 merges catalogue 46, 47 and 50 (same key: fine).

**Risk:** Low: R731 is labelled 'read with known key' by method; the class 'read in part' for the R580 letters is caused only by a different-system letter.

**Proposed fix:** Split R731 into its own attempted/open entry or add outcome.parts (R580 letters: read with known key, complete; R731: not solved); compute the R580 fraction alone.

**Evidence:** profile system.summary 'R731 uses a separate graphic-sign alphabet'; fraction_read_source 'R731's ~330 signs added as unread'; NOTES.md:101-108; README.md:293

### potocka1714

**Verdict:** MIXED

| Key / cipher | Documents | Outcome |
|---|---|---|
| Potocka's partly ordered numerical alphabet with doubled homophones and person codes | R7525-R7530, R7534-R7536 (Barbara Potocka -> Jakub Dunin, 1714-16) | key recovered from ciphertext-only (from the R7526 Polish postscript), 844/886 = 95.3% sense (meets the read bar) |
| Mniszech's separate word-divided homophonic system (77 signs) | R7524 (Jozef Mniszech -> Dunin, 1714; 232 tokens) | not solved |

**Where it is merged:** Grouped by recipient (Dunin) and archive (Archiwum Sanguszkow). outcome.parts = null and outcome.credits = null; one outcome.method 'key recovered from ciphertext-only'; fraction_read 0.771 / 75.5% pools both; NOTES.md:3 'Mniszech R7524 not read, so the target is 75.5%' and outcome.notes 'the target stays read in part because one document (R7524) is unread'. system.summary covers both but counts describe Potocka only.

**Risk:** The Potocka key, which meets the 95% read bar, is reported 'read in part' at 75.5% because an unrelated key's letter is unread; the paper's result for Potocka's cipher is understated and Mniszech's failure is hidden inside a 'ciphertext-only' success.

**Proposed fix:** Split R7524 into its own target (mniszech1714, not solved) and mark potocka1714 read at 95.3%; or add outcome.parts (Potocka key: ciphertext-only, complete; Mniszech: not solved) and compute the class per part.

**Evidence:** targets/potocka1714/NOTES.md:8 'R7524, Jozef Mniszech to Dunin, uses a separate, still unread numerical system'; NOTES.md:3 'so the target is 75.5%'; profile.json outcome.notes 'the target stays read in part because one document (R7524) is unread'; outcome.parts null

### r1854

**Verdict:** MIXED

| Key / cipher | Documents | Outcome |
|---|---|---|
| P1 letter-like sign system (Pandolfo Malatesta), unidentified | R1854 image 1, Rome 22 Apr 1428 | not solved (262 signs, no key material) |
| P2 homophonic + nulls + codes ARW/ARO | R1854 image 2, Rome 9 Aug 1428 | key recovered from ciphertext-only, 0.966 |
| P3 homophonic + name codes (Forlì informant) | R1854 image 3, Forlì 6 Nov 1428 | read from existing decipherment (contemporary interlinear gloss), 0.972 |
| P4/P5 Cattanei homophonic with et/con/-rum signs | R1854 images 4-5, Rome 13 and 21 Feb 1430 | key recovered from ciphertext-only, 0.967 / 1.0 |

**Where it is merged:** Four distinct keys (NOTES table column 'cipher' differs per letter; system summary 'Three different homophonic substitutions ... P1 ... not identified') sit in one profile with one outcome.method 'key recovered from ciphertext-only' and one pooled fraction_read 0.922; outcome.parts is null. The P3 key came from the contemporary gloss, not ciphertext-only. Grouped only because DECODE filed them under one record. Page and README do describe each letter separately.

**Risk:** high: paper data counts one ciphertext-only break where there are two ciphertext-only breaks, one read-at-the-time, one unsolved; the pooled 0.922 hides P1 = 0.

**Proposed fix:** Add outcome.parts per key (P1 not solved; P2 ciphertext-only; P3 read from existing decipherment; P4+P5 ciphertext-only) with per-part fraction and system; method of the entry should not be the P2/P4 method alone; consider separate badges per letter.

**Evidence:** targets/r1854/NOTES.md:16-23 per-letter cipher table; NOTES.md:4 'Key: recovered for P2, P3 (from the contemporary gloss), P4/P5; none for P1'; profile.json outcome.method 'key recovered from ciphertext-only', fraction 0.922, parts null

### r1871

**Verdict:** MIXED

| Key / cipher | Documents | Outcome |
|---|---|---|
| Venetian nomenclator, base letter + superscript letter (Bonavoglia 'Cifra n. 3' family), 1558 | R1873, ASVe Busta 30 ff. 4-6, Mocenigo, Rome 25 Apr 1558 | read from existing decipherment (Bonavoglia, saved r1873_bonavoglia.txt) |
| Foscarini's 1680s 3-digit numerical nomenclator (Paris/Madrid) | R1871, ASVe Busta 30 f. 4, Foscarini, Paris 11 Sep 1680 | not read here; Bonavoglia lists it but his decipherment could not be retrieved; attempted ciphertext-only, failed |

**Where it is merged:** NOTES.md:8 'Catalogue 264 ... merges two records that belong to different despatches, 122 years apart', yet one folder/profile keeps both: one outcome.method 'read from existing decipherment' for both, fraction_read 'unknown', outcome.parts null, system.types ['nomenclator'] with a summary describing both ciphers. NOTES.md:5 'Verdict: both already read, by Paolo Bonavoglia' although R1871's decipherment was never seen (NOTES.md R1871 section 'His decipherment could not be retrieved'). Folder named after R1871, the unread one. No page/README row (Status: no write-up).

**Risk:** Paper data counts R1871 as 'read from existing decipherment' though no decipherment was obtained and the attempt here failed; the 1558 and 1680 ciphers' statistics are pooled; the contamination question (reading existed and was seen) is answered 'yes' for a document whose reading was not seen.

**Proposed fix:** Split into r1873 (Mocenigo 1558, read from existing decipherment, Bonavoglia) and r1871 (Foscarini 1680, not solved / decipherment exists but unretrieved, ciphertext-only attempt failed); or add outcome.parts per record with distinct methods. Change the NOTES verdict to 'R1873 read by Bonavoglia; R1871 listed by him, decipherment unseen'.

**Evidence:** NOTES.md:5 'both already read'; NOTES.md:8 'merges two records ... 122 years apart'; NOTES.md 'His decipherment could not be retrieved'; 'Attempt here (22 Sep 2026): not read'; profile outcome.method 'read from existing decipherment', outcome.notes 'R1871 attempted, not read'; outcome.parts null

### r4349

**Verdict:** MIXED

| Key / cipher | Documents | Outcome |
|---|---|---|
| vowel-shift colophon cipher (Uppsala catalogue 1992) | C 513 f. 19v colophon, 1517, 125 letters | read with known key, read in full (already in print) |
| unknown six-sign signature cipher, later hand | slip pasted on f. 1r | not solved (too short); vowel shift tested and fails |

**Where it is merged:** Two unrelated ciphers (different hand, date, system; the vowel shift was tested on the slip and fails) are one profile, one README row and one fraction: 125/131 = 95.4% pools the colophon with the slip; system describes only the vowel shift; method 'read with known key' covers the slip too; outcome.parts null.

**Risk:** medium: fraction and badge describe a combination; the DECODE-described piece (the slip) is the unread one but the entry reads 95.4%.

**Proposed fix:** outcome.parts: part 1 colophon (read with known key, 125/125); part 2 slip (not solved, 0/6, blocker too short); report fractions per part, not pooled; README row gives the two results separately.

**Evidence:** targets/r4349/NOTES.md:3-4 'the manuscript holds two ciphered pieces'; :110 'Tried ... the colophon's vowel shift (none of b f k p x occurs)'; README.md:285 '(125 of 131 cipher tokens, 95.4%, measured). Two ciphers.'

### rakoczi1704

**Verdict:** MIXED

| Key / cipher | Documents | Outcome |
|---|---|---|
| Bonac-Groffey French nomenclator, DECODE R639 | R912, R922 (1707) | read after matching with external key (R639), ~97%; about a third read at the time interlinear |
| a different issue of the R639 table | R852 (Dantzig 22 Jan 1706) | read from its own clear copy (existing decipherment) |
| Rakoczi's Latin syllabic key (rebuilt from the interlinear by align483.py) | R483 (Lwow 27 June 1711) | key recovered from adjacent plaintext (interlinear decipherment) |

**Where it is merged:** Grouped by catalogue 44 / DECODE author 'Rakoczi'. system.summary describes only the one-part French nomenclator 10-560; one outcome.method 'read after matching with key from external sources' for all four; no outcome.parts (NOTES.md:100: 'A parts split ... is for the main session to decide'); README row 223 says 'Read' for the whole set. Page sections are per letter, good.

**Risk:** R483 (Latin, own key rebuilt from interlinear) and R852 (clear copy) are counted as external-key matches; R483's key is described as the French R639 table.

**Proposed fix:** Split R483 into its own target (Rakoczi 1711 Latin syllabary, key from adjacent plaintext); keep R852/R912/R922 together but add outcome.parts (R912/R922 external key R639; R852 existing decipherment / different issue).

**Evidence:** profile system.summary 'One-part numerical French nomenclator, values 10-560'; NOTES.md:7-8 'its syllabic key has been rebuilt from that decipherment'; NOTES.md:50 'R852 uses a different issue of the table'; NOTES.md:100; README.md:223

### sessa1593

**Verdict:** MIXED

| Key / cipher | Documents | Outcome |
|---|---|---|
| Spanish office cipher 1592-93 (office key BnF fr. 3995 f. 97, DECODE R4076-R4077; Tomokiyo phelippes2.png) | no45 = fr. 3983 no. 45 (Miranda->Feria, 25 Feb 1593); no79 = fr. 3983 no. 79 (Sessa->Ibarra, 11 Mar 1593); no47 = fr. 3984 no. 47 (Sessa->Philip II, 30 Jun 1593) | read with known key, partial ~92.5%; checked against no. 47 interlinear |
| Feria-Mansfeld cipher 1593 (Tomokiyo spanish3mansfeld.png; nomenclature missing) | no68 = fr. 3984 no. 68 (Ibarra, Paris, 10 Jul 1593) | read with known key (alphabet/syllables only), partial 37.5%; three-letter word codes open |

**Where it is merged:** Two different ciphers (two different correspondences: the office cipher of Sessa/Miranda, and Feria-Mansfeld's syllabic cipher used by Ibarra in Paris) in one target grouped as catalogue item 19 / year 1593. outcome.parts = null; one outcome.method 'read with known key'; one fraction_read 0.753 pooling 92.5% and 37.5%; system.types merged and system.summary describes the office cipher with no. 68 as an add-on clause; README row (README.md:284) leads with 'The Spanish office's own key survives' for all four. The page does have h2#keys and a per-letter h3 for no. 68.

**Risk:** The 75.3% figure is meaningless for either key; Arya's office-key credit ('read all four letters in part') covers a letter in another cipher; paper per-system stats (distinct_symbols 133, alphabetical key order) mix two systems.

**Proposed fix:** Add outcome.parts: (1) office cipher, nos. 45/79/47, read with known key, partial 92.5%; (2) Feria-Mansfeld cipher, no. 68, read with known key, partial 37.5%. Or split no. 68 into its own target (ibarra1593) and retitle; README one row per cipher.

**Evidence:** targets/sessa1593/NOTES.md:88 'no. 68 is in the other cipher'; NOTES.md:242 'a different cipher - the Feria-Mansfeld key'; NOTES.md:5 '92.5% of nos. 45/79/47, 37.5% of no. 68, 75.3% overall'; profile.json outcome.parts null, fraction_read 0.753

### siena1421

**Verdict:** MIXED  
**Lasry:** none in profile credits (Lasry solved nos. 6/24, now in siena1431)

| Key / cipher | Documents | Outcome |
|---|---|---|
| no. 25 own key (rebuilt ciphertext-only) | no. 25 (R4813) | key recovered ciphertext-only, 96.2% read |
| no. 18 own key (Ziegler articles) | no. 18 (R4806) | key recovered ciphertext-only, ~87% |
| no. 14 own key | no. 14 (R4802) | key recovered ciphertext-only, ~60% read in part |
| Borghesi 1456 key | no. 4 (R4793) | key from adjacent plaintext (fragment + recipient glosses), 114/144 |
| R4755 Cristofano | nos. 6, 24 (R4795, R4812) | solved by Lasry, moved to siena1431, still listed here 'read in part' |
| nos. 20+23 system | R4808, R4811 | unread, no key |
| separate unidentified keys | nos. 7, 11 (Acciaiuoli 1478), 17 (1528), R4794, 9/15/19/21 | unread |
| contemporary decipherments | nos. 8, 10, 13/16, 22; no. 12 DECODE 'Decrypted' | read at the time / existing decipherment |

**After George's review:** Per George: remove analytical ownership of nos. 6/24 and reference siena1431. Do not count the assorted unresolved documents as established key groups.

**Where it is merged:** A whole busta (1421-1547) grouped by collection. system.summary admits 'each letter uses its own ... key ... so the system is per document', yet the profile has NO outcome.parts, one outcome.method 'key recovered from ciphertext-only' and one fraction_read 0.22 pooled over ~13,400 tokens of many keys; README row (README.md:75) is one row for 'the cipher letters of the Concistoro'.

**Risk:** No. 4 (glosses = adjacent plaintext) and contemporary/DECODE readings are scored as ciphertext-only; the 0.22 fraction is meaningless across 10+ systems; nos. 6/24 double-counted with siena1431 (Lasry's solve); per-key results (no. 25 96% read) are hidden under 'read in part'.

**Proposed fix:** Split per key: siena-no25, siena-no18, siena-no14, siena-no4 (Borghesi 1456) as their own targets (as siena1431 already was), leave siena1421 as a survey in research/ or at least add outcome.parts per letter with its own method and fraction; drop no06/no24 documents.

**Evidence:** profile system.summary 'each letter uses its own Sienese or foreign key'; outcome.parts absent; fraction_read_source 'no. 25 477/496, no. 18 1,271/1,459, no. 14 ~757/1,291, no. 4 114/144, over ~13,400'; NOTES.md:3, NOTES.md:290-301

### sieniawski1708

**Verdict:** MIXED

| Key / cipher | Documents | Outcome |
|---|---|---|
| Schenck letters: 2-digit alphabetical-block letter table + 3-digit person codes | R7486-R7500 (AKM 21 plik 30/1; 'Sidon' in Vienna -> Baron Schenck, 1706) | key recovered from ciphertext-only, partial (93.5% of letter numbers, 63.6% of all tokens; 65/77 codes open) |
| key A (Wallachian chancellery key, Kaczka 2012 fn. 21) | R7468-R7474, R7477-R7480, R7483 (Brancoveanu/Cantacuzino -> Sieniawski 1709-14) | read from existing decipherment (Kaczka 2012 print), sample checked |
| key B (Turculet key, Kaczka fn. 22) | R7481-R7482 | read from existing decipherment (interlinear), 99.6-100% |
| alphabetical homophonic table rebuilt from the gloss | R7475 (adviser, 1707) | read from existing decipherment (interlinear), ~99.6% |
| Chomentowski 3-digit syllabary | R7476, R7484-R7485 (Chomentowski 1713-14) | read from existing decipherment (interlinear); R7476 ~94.4-94.9%, R7484 96.5%, R7485 100% |

**Where it is merged:** Five systems and two unrelated correspondences (a Vienna agent to Schenck 1706 vs Wallachian/Polish writers to Sieniawski 1707-14) in one folder, profile and page, joined only by the DECODE range R7468-R7500 / catalogue 333. README is split into two rows (README.md:103, 368) and outcome.parts has three parts, but part 3 ('unprinted Sieniawski letters') lumps key B, the R7475 table and the syllabary; documents[] are grouped by collection (one document 'nr 13 and nr 5' for 11 records). Top-level system.summary, distinct_symbols=143, outcome.method 'key recovered from ciphertext-only' and fraction_read 0.636 describe only the Schenck letters, yet sit over all 33 records.

**Risk:** The ciphertext-only break and 63.6% figure attach to the whole target including 18 letters read from print/interlinears; system statistics (143 symbols, alphabetical order) applied to four other systems; per-key outcomes for key B/syllabary not recoverable.

**Proposed fix:** Split into two targets: sieniawski1708 (Sieniawski letters) and a new schenck1706 (R7486-R7500). Inside the Sieniawski target give outcome.parts one entry per key (A, B, R7475 table, syllabary) and documents[] per record or per key.

**Evidence:** targets/sieniawski1708/profile.json system.summary 'the Sieniawski letters use four other systems (keys A and B, an alphabetical homophonic table, a 3-digit syllabary)'; outcome.notes 'R7468-R7500 are four collections'; NOTES.md:31 'Sieniawski group, several systems'; README.md:103 'Split entry, part 1 of 2'

### sp106box10

**Verdict:** MIXED  
**Lasry:** none (his SP 106 keys tested on R931, do not fit)

| Key / cipher | Documents | Outcome |
|---|---|---|
| System A: two-figure Italian nomenclator, codebreaker's key R725 | R657 (ff. 128-138) + worksheets | key transcribed; R657 'not read' (not worked against R725) |
| System B: three-figure syllabic code (grid R658) | R660, R664, worksheet R720; also R722 (Venetian secretary 1625) and the R703 'Venetian cifar' dossier with R656, R661, R663, R667, R684, R701, R702 | about 45 values rebuilt from interlinear glosses; R660/R664/R722 read in fragments; R722 code not deciphered |
| System C: letter-and-figure syllabary | R704, R721 (R722 first filed here, now moved to B) | not read |
| English royalist numerical code of Sept 1645 (~260 values) | R931 | not solved; page says it 'does not belong to the case' |

**Where it is merged:** One profile/page/README row for at least four systems grouped by box (SP 106/10). profile system.types merges nomenclator+homophonic+syllabic+code; one outcome.method 'read with known key' and fraction_read 0.1 with outcome.parts null, though the 'known key' R725 is system A and R657 (system A) is 'not read'; the fragments actually read are system B values rebuilt from glosses (key recovered from adjacent plaintext). credits only 'R725, grid R658 and interlinear solutions'. README row (README.md:295) presents 'the seven records are one case ... the cipher explained'. R931 (1645, different code, unrelated) is in documents[].

**Risk:** Method misclassification: system B fragments are scored as 'read with known key' using system A's key; the 10% fraction mixes three systems and an unrelated 1645 letter; DECODE/paper readers may think R725 reads the file. R931's 'not read' inflates the denominator of an unrelated case.

**Proposed fix:** Add outcome.parts per system (A: key R725 known, R657 not read; B: key recovered from adjacent plaintext (glosses), R660/R664/R722 fragments; C: not solved; R931: not solved); better, split into sp106box10a (R657+R725), sp106box10b (R660/R664/R720/R722 + R703 dossier + grid R658) and sp106box10c (R704/R721), and move R931 to its own target or to the 1645 royalist group.

**Evidence:** profile system.summary 'Three ciphers in one codebreaker's file: (A) ... (B) ... (C)'; docs/sp106box10.html:118 'The file holds three ciphers, not one'; html section 08b 'R931 does not belong to the case'; profile R657 read 'not read'; outcome.method 'read with known key', parts null; README.md:295

### sunyatsen

**Verdict:** MIXED

| Key / cipher | Documents | Outcome |
|---|---|---|
| Swatow condenser table (April 1916) | JACAR B03050738800 frame 680682, 3 Apr 1916 | key recovered from ciphertext-only |
| July-Nov 1916 G0/Y0 condenser systems (other correspondents, own keys) | y1916 series, JACAR intercept files | decoded by Brice Dudout (outside decipherment); separate README row 87, ~7 keys, no profile of its own |
| 1917 variants | y1917 series | identification by wanglu (issue #23) |

**Where it is merged:** The Swatow profile (one telegram, one key) carries credits for other keys: dudout 'solution' for the July-November 1916 G0/Y0 systems and 'transcription' corrections to the 1916 forms, wanglu 'identification' for 1917 variants. NOTES says each correspondent has its own key. The series row (README.md:87) has no profile, so its credits sit on the Swatow entry.

**Risk:** high: paper data would credit Dudout with a 'solution' on the Swatow key, which was recovered here ciphertext-only; the series keys get no per-key outcome.

**Proposed fix:** Move dudout/wanglu credits into a y1916/y1917 profile (or outcome.parts per series key); keep the Swatow profile to its one key.

**Evidence:** targets/sunyatsen/NOTES.md:131 'each correspondent with its own key. See y1916/NOTES.md'; profile.json credit dudout role 'solution' note 'decoded the July-November 1916 G0/Y0 systems (y1916)'; targets/sunyatsen/y1916/NOTES.md:111 'Outside decipherment: Brice Dudout, July–November 1916'

### swieten1757

**Verdict:** MIXED

| Key / cipher | Documents | Outcome |
|---|---|---|
| 1757 table 202-586 (R955) |  |  |
| 1759 table 100-442 (R956/R957) |  |  |

**Where it is merged:** Two different alphabetical syllabary tables in one entry; status read covers R955 (decipherment) and R956/7 (rebuilt)

**Risk:** Medium: reading credits both keys; fraction 0.962 is R956+R957 only

**Proposed fix:** Split R955 (1757 key) from R956/R957 (1759 key)

**Evidence:** NOTES: "A different table, 100-442"; profile fraction_read note

### thurloe

**Verdict:** MIXED

| Key / cipher | Documents | Outcome |
|---|---|---|
| (a) figure substitution + small code (8 code groups) | a-beverning-1653, TSP i.435 | not solved |
| (b) figures mixed with letters | b-dugard-1656, TSP v.78-79 | not solved |
| (c) ten-digit cipher | c-brussels-1656, TSP v.267 | not solved |
| (d) homophonic figures with two codes (226, 243) | d-waddall-1656, TSP v.337 | not solved |

**Where it is merged:** Grouped by printed source (Thurloe State Papers, cryptiana item #9). profile system.summary 'Four unrelated short ciphers'; system.types ['undetermined'] 'for the set'; nomenclator.entries pools (a) and (d); one outcome.method 'not solved', no outcome.parts; README row (README.md:415) 'Four short pieces, all period keys fail'; no page.

**Risk:** Low today (all unread, stated as four systems). Paper counts one target for four separate ciphertext-only problems, and the control run (done on (a)'s layout) is reported for the whole set; system statistics are pooled/undetermined.

**Proposed fix:** Add outcome.parts per piece (a)-(d), each 'not solved' with its own length/system; or split into four profiles if the paper counts per cipher. Keep the README row but say 'four different ciphers'.

**Evidence:** profile system.summary 'Four unrelated short ciphers'; system.notes 'Four separate systems, so types is undetermined for the set ... nomenclator.entries counts the 10 code groups seen in (a) and (d)'; outcome.notes control 'on (a)'; README.md:415

### transylvania1645

**Verdict:** MIXED

| Key / cipher | Documents | Outcome |
|---|---|---|
| Hungarian substitution 'shared alphabet family' (c=p, p=c, g=u, q=t) | R4936 (1645), R4940 (1648), fragments R4937, R4942 | key recovered from ciphertext-only; R4940 23 letters read, others partial/unverified |
| 'Different substitution' (unsolved) | R4941 (1648) | not solved |
| unknown, not inspected | R4933 (1628/1658), R4934, R4935 (1628, KemÃ©ny_XIX), R4938, R4939 | not transcribed |

**Where it is merged:** Ten DECODE records grouped by a DECODE number range across two collections (KemÃ©ny_XIX_1628 vs Keresdi_Bethlen_14/15) and dates 1628-1658, title '1645'. NOTES.md:33 'R4941 | 1648 | Different substitution'. Profile system.types 'undetermined' with summary 'the other systems remain to be inspected', yet one outcome.method 'key recovered from ciphertext-only', class 'read in part', no outcome.parts. Status: in progress; no README row or page yet.

**Risk:** If written up as is, a single read-in-part entry would credit a ciphertext-only recovery to ten records of which only R4940 (23 letters) is read, and the 1628 KemÃ©ny letters (different writer, decade, likely key) would be counted under the 1645-48 Bethlen key.

**Proposed fix:** Before write-up, classify each record by system; split into keresdi1645 (records sharing the R4936/R4940 alphabet), a separate entry for R4941, and kemeny1628 (R4933-R4935); give each outcome.parts; until then set documents' outcome per record.

**Evidence:** profile system.summary 'R4936 shows alphabetic ciphertext; the other systems remain to be inspected'; outcome.notes 'R4940 cipher expressions read, others unverified or untranscribed'; NOTES.md:24-35

### urquhart

**Verdict:** MIXED

| Key / cipher | Documents | Outcome |
|---|---|---|
| octastich book cipher on The Jewel (1652), page k word n initial | octastich + Decagram, 285 numbers | read with known key (rule verified), 274/285 = 0.961 |
| distich: unknown construction ('another construction, or this one on a text' not identified) | Cyphral Distich, 64 numbers (Logopandecteision 1653) | not solved; Proquiritation rule at chance |

**Where it is merged:** Two cryptograms in two books with (as tested) different keys share one profile and one fraction_read 0.785 = 274/349 pooled; system describes only the octastich rule; outcome.parts null. The pooled number is neither cryptogram's result.

**Risk:** medium: paper data gets 0.785 for a read octastich and an unread distich.

**Proposed fix:** outcome.parts: octastich (read with known key, 0.961) and distich (not solved, 0); drop pooled 0.785 or label it explicitly; page/README state each separately (title already does).

**Evidence:** targets/urquhart/NOTES.md:33 'octastich 274/285 = 0.961 (read); with the unread distich, 274/349 = 0.785'; :153 'The distich is another construction'; :185 distich blocker no-key-material

### vanreede1787

**Verdict:** MIXED

| Key / cipher | Documents | Outcome |
|---|---|---|
| William V 1782 Grand Chiffre (DECODE R1024) | R1026 (29 Dec 1787), R1027 (4 Mar 1788) | read with known key, 452/472 groups |
| marked three-digit code (no key) | R1893 (24 Mar 1793, Staten-Generaal inv. 6695) | not solved |

**Where it is merged:** Grouped by sender (van Reede). system.summary names both codes, but there are no outcome.parts; one outcome.method 'read with known key' and fraction 0.383 (447/1167) pool the read Grand Chiffre letters with the unread R1893 code; title 'Dispatches of A. W. C. van Reede from Berlin, 1787-1793' implies one series.

**Risk:** R1893 inherits 'read with known key' in method counts; the 38% figure understates the Grand Chiffre result and overstates R1893; anyone attacking R1893 might assume R1024.

**Proposed fix:** Split R1893 into its own target (attempted, open), or add outcome.parts: R1026/R1027 'read with known key'; R1893 'not solved'; fraction per key.

**Evidence:** profile system.summary 'R1893 uses a distinct three-digit marked-number code'; no outcome.parts; fraction_read_source 'all of R1893 unread; 447/1167'; README.md:292

### vich1511

**Verdict:** MIXED

| Key / cipher | Documents | Outcome |
|---|---|---|
| Ferdinand-Vich nomenclator of 1511-12 (rebuilt from deciphered siblings N.46, N.52BIS) | N.45 (4 Apr 1511), N.57 (5 Jun 1512), N.60 (1 Sep 1512), AHN Estado 8715 | key recovered based on adjacent plaintext, read in part (3-8% of groups unread) |
| unknown 1515 system (different key; N.74 is a third system) | N.73 (26 Oct 1515, Pedrezuela; 3,177 tokens) | not solved |

**Where it is merged:** N.73 is grouped with the 1511-12 letters only by sender/recipient (Ferdinand -> Vich) and bundle (AHN Estado 8715). outcome.parts = null; one outcome.method 'key recovered based on adjacent plaintext' for all four; fraction_read 0.865 pools the read key with 3,177 unread N.73 tokens (outcome.notes even gives 0.74 for the same pool); system.types includes the 1511-12 system only, summary says '(N.73 is a different, unread system)'. Page h1 'Ferdinand the Catholic to Jeronimo de Vich, 1511-12' but includes h2#n73; README row (README.md:193) title lists N.73 under '1511-12'.

**Risk:** The 1511-12 key is held below the read bar purely by an unrelated 1515 cipher (NOTES.md:165 'N.73 ... alone caps the target at ~0.90'); N.73 is counted as attacked-with-adjacent-plaintext instead of 'not solved'; inconsistent fractions (0.865 vs 0.74).

**Proposed fix:** Move N.73 to its own target (vich1515, status attempted/open) or add outcome.parts: (1) 1511-12 nomenclator, N.45/N.57/N.60, adjacent plaintext, partial; (2) N.73, not solved. Measure fraction_read over N.45/N.57/N.60 only.

**Evidence:** targets/vich1511/NOTES.md:16 'different key, not read'; NOTES.md:165 'N.73 (3,177 tokens, other key) alone caps the target at ~0.90'; NOTES.md:191 'different system, no deciphered sibling'; profile.json outcome.parts null

### walsingham1585

**Verdict:** MIXED

| Key / cipher | Documents | Outcome |
|---|---|---|
| two-digit name code |  |  |
| sign alphabet with homophones/nulls (R4844 10 Sep) |  |  |

**Where it is merged:** Name code and a separate sign alphabet counted in one fraction_read 0.49

**Risk:** Medium: fraction mixes code identification and sign-word reading

**Proposed fix:** Score name code alone; treat 10 Sep sign alphabet as separate key/unread

**Evidence:** system.summary: "plus, in one letter, a few words in a sign alphabet"

### windischgraetz1720

**Verdict:** MIXED

| Key / cipher | Documents | Outcome |
|---|---|---|
| Chancellery two-part nomenclator R5017 (1-977) | No. 1, 3 Feb 1720 (R5019 autograph, R5020 copy) | read with known key, read |
| Emperor's private key R5018 (numbers 10-38 + graphic signs, codes 39-210) | Nos. 2, 3, 6 (R5021/R5022, R5023, R5024), 1720-22 | read with known key, read |

**Where it is merged:** Mild. The page separates the keys (windischgraetz1720.html:73 'The letters and the two keys', :97 No. 1, :137 'Nos. 2, 3 and 6 in the private key') and system.summary names both, but profile.json has no outcome.parts, a single fraction_read 0.995 and single system.types/homophone counts ('Homophone counts are for R5018'); grouping is by sender/recipient. README row (README.md:271) names both keys.

**Risk:** Low: both keys survive and both readings are by known key, so the method is right for both. Risk is only statistical: per-key fraction, key size and homophone counts are blended or describe R5018 only, so the paper cannot tell how R5017 (one letter) vs R5018 (three) performed.

**Proposed fix:** Add outcome.parts: one part 'No. 1, key R5017' (records R5019/R5020) and one 'Nos. 2, 3, 6, key R5018' (R5021-R5024), each with its own measured fraction; optionally separate system notes per key.

**Evidence:** profile system.summary 'Two keys: No. 1 in ... R5017 ..., Nos. 2, 3, 6 in the private key R5018'; system.notes 'Homophone counts are for R5018'; outcome.parts null; docs/windischgraetz1720.html:73,97,137

### wod1568

**Verdict:** MIXED

| Key / cipher | Documents | Outcome |
|---|---|---|
| Throckmorton Cipher 1 (Tomokiyo key image, 7 values corrected) | R2988 f. 32: Throckmorton to Elizabeth 10 July 1559 | read with known key, ~85-90% |
| word-sign margin code (222 groups), undetermined | R2988 f. 32 margin | not solved |
| Moray-Wood 1568 cipher family, undetermined | R2989 f. 33: John Wood to Cecil 6 Sept 1568 | not solved (Bain crib did not align) |

**Where it is merged:** Three systems from 1559 and 1568 grouped by leaves (BL Add MS 4136 ff. 32-33, catalogue 97). Profile system.types 'undetermined' and system.summary describe only the two unread systems, while outcome.method 'read with known key' and class 'read in part' come from the Throckmorton Cipher 1 letter, which is not a separate document in documents[] (only R2989 and R2988). No outcome.parts. fraction_read 0.3 'is over all three texts'. README row (README.md:280) and page title combine all three (page h2s do separate them).

**Risk:** The paper data pairs a 'read with known key' outcome with an 'undetermined' system; readers/statistics may take the Wood 1568 line or margin code as partly read. The read text (1559) is a different letter, date and sender than the catalogue's 'John Wood 1568' item.

**Proposed fix:** Split documents[] into three (1559 letter, margin code, Wood line) with outcome.parts (read with known key / not solved / not solved) and per-system descriptions; or split into wod1568 (Wood line + margin, unread) and throck1559 (read with Cipher 1). Retitle README/page so the catalogue item's own ciphers are shown as unread.

**Evidence:** profile system.summary 'R2989: same symbol families as the Moray-Wood 1568 cipher ... R2988 margin: a shorthand-like sign system'; outcome.basis 'The text reported as read is Throckmorton's own 10 July 1559 letter'; outcome.notes 'fraction is over all three texts'

## Unclear from the files (12)

### entragues1581  (Lasry entry)

**Verdict:** UNCLEAR  
**Lasry:** solution (Lasry, BnF cipher research)

| Key / cipher | Documents | Outcome |
|---|---|---|
| name key f761r ('Copia d una cifra trovata'), 28 signs | ff759r-760v (letter on the England enterprise) | read with known key, partial; spot-checked here |
| assumed same name key | ff780r-781v ('a separate letter' on a prisoner's statements) | included in Lasry's 87 elements / 89.7%, not separately checked |

**Where it is merged:** two letters under one page titled 'The letter'; the spot-check covered only f759v and f761r; nothing here shows the ff780-781 signs match the f761r key. Sender 'd'Entragues' also looks wrong for ff759 (the writer speaks of 'mons. d'Entragues' in the third person)

**Risk:** low-medium (name signs only, Lasry's own entry)

**Proposed fix:** check the ff780-781 signs against f761r; if they match, say so on the page; if not, split them. Revisit the sender field

**Evidence:** targets/entragues1581/NOTES.md:17 'A separate letter discusses a prisoner's statements'; docs/entragues1581.html 'Our check': 'checked on his crops of f759v and f761r'

### sessa1597  (Lasry entry)

**Verdict:** UNCLEAR  
**Lasry:** solution (Lasry, BnF cipher research)

| Key / cipher | Documents | Outcome |
|---|---|---|
| Spanish Rome cipher Cp.39 (Tomokiyo reconstruction from fr. 15972) | Philip II -> Sessa, Madrid 31 Mar 1597 (f.145r) | read with known key, partial; spot-check confirmed on f.145r |
| unstated (Archduke Albert's cipher? not shown to be Cp.39) | Archduke Albert -> Philip II, 25 Aug 1596 (Hulst) | included in the combined 379 elements / 89.7%; not checked here |

**Where it is merged:** two letters from different correspondences (Madrid->Rome ambassador; Brussels governor->King) under one entry with one key ('174 codes') and one percentage. A Philip II-Sessa cipher is not expected to be the Archduke's; nothing on the page shows the 1596 letter's codes tested against Cp.39

**Risk:** medium: likely two keys combined; title, sender/recipient and fraction merged

**Proposed fix:** ask Lasry (or check the 1596 folio) which key reads the Albert letter; if different, split into two entries with their own counts; if the same, record the test

**Evidence:** targets/sessa1597/NOTES.md:12-17 'Sender: Philip II / Archduke Albert ... Date: 31 March 1597 / 25 August 1596 ... Key: 174 codes'; docs/sessa1597.html 'Our check' covers only f145r 'El Rey / Duque de Sessa'

### charlesi

**Verdict:** UNCLEAR

| Key / cipher | Documents | Outcome |
|---|---|---|
| unknown numeric nomenclator A | 1648-05-22 (Charles I -> Edward Worsley, 112 groups, Albin 1795 p. 237) | not solved |
| unknown numeric nomenclator B (postscript says 'This Cypher which now I write in, is that which was sent you by the noble frend') | 1648-08-01 (Charles I -> Prince Charles, 88 groups; DECODE R8342, Harley 6988 f. 208) | not solved |

**Where it is merged:** Two letters to two different recipients grouped by sender/date (Isle of Wight 1648). The files exclude the published keys for both, but never state whether the two letters share one key; the 1 Aug postscript says it uses a cipher sent by the bearer, which suggests a key different from the Worsley one. system.summary describes only the 22 May letter ('uses 1-97 and 204-416 only'). One outcome 'not solved' for both, so no false credit.

**Risk:** Low (both unread). If the two are different keys, pooled statistics (band gaps, near-repeat test) and any future break would be misattributed; DECODE R8342 is in this target and possibly also in an untracked charles1648 folder in the local checkout.

**Proposed fix:** State in NOTES/profile whether the two letters share a key (compare number ranges/band structure); if different, give each its own system notes or outcome.parts, and retitle README row to name both recipients.

**Evidence:** targets/charlesi/NOTES.md:71-73 postscript 'This Cypher which now I write in ...'; NOTES.md:15 'both letters remain unread'; profile.json system.summary 'the 22 May cipher ...'; README.md:408

### damiata1624

**Verdict:** UNCLEAR

| Key / cipher | Documents | Outcome |
|---|---|---|
| Lasry/Biermann-Bosbach key R60 (R59,R60,R61 figures) |  |  |
| R61 line of letter-sign cipher, not in this key |  |  |

**Where it is merged:** R61 has an extra letter-sign line outside the key, not attacked

**Risk:** Low: not read, so not folded into reading

**Proposed fix:** Note R61 letter-sign line as excluded from the entry/fraction

**Evidence:** NOTES: "letter-sign line in R61 is not in this key and was not attacked"

### lopehurtado1523

**Verdict:** UNCLEAR

| Key / cipher | Documents | Outcome |
|---|---|---|
| 1523 key variants |  |  |
| 1524 key (key_1524.tsv) |  |  |

**Where it is merged:** Key changed between 1523 and 1524 (tef=paz vs nec-); letters of both years pooled at 0.45

**Risk:** Low-medium: possible two keys if variants are distinct

**Proposed fix:** Check whether 1523 and 1524 are one key with drift; else split

**Evidence:** NOTES: "The key moved between 1522 and 1524"; key_1523_additions vs key_1524

### middelmore1563

**Verdict:** UNCLEAR

| Key / cipher | Documents | Outcome |
|---|---|---|
| Middelmore's own cipher (~25 signs + code signs), tested on 26 July only | R9246 (19 Jul 1563, passages 1-46) and R9247/f. 157 (26 Jul 1563, passages 1-26) | read from existing decipherment (Forbes 1741) |
| different cipher on f. 155 top (passages 16-22 of an earlier letter) | f. 155 top | excluded; not identified |

**Where it is merged:** profile.system says 'Middelmore's own cipher ... Checked on passages (1),(2),(4),(6),(9) of 26 July'; the 19 July letter is assigned the same key without any sign/value test. Also R9247 is byte-identical to R9246 image 3, so documents[] presents a duplicate record as the second letter. fraction_read 1.0 rests on Forbes's print for both.

**Risk:** low (no write-up, read from print), but a shared-key assumption without evidence for 19 July.

**Proposed fix:** Spot-check 2-3 passages of 19 July against Forbes ii 470-75 (same sign values?) or record the 19 July key as 'unknown'; fix documents[] so R9246 holds both letters and R9247 is noted as duplicate.

**Evidence:** targets/middelmore1563/NOTES.md:19-24 (records; f.155 top 'a different cipher'; R9247 byte-identical), :32-37 spot-check on the 26 July letter only

### mondoucet

**Verdict:** UNCLEAR

| Key / cipher | Documents | Outcome |
|---|---|---|
| Mondoucet 1572 key (fitted on the glossed 16 July 1572 crib, ff. 62-64) | 13 Jul 1572 (ff. 60-61) assigned to it; 16 Jul 1572 crib | 13 July not solved (~1-8% of 1,082 glyphs); key reads its own crib ~60% |
| Mondoucet 1573 key (key1573_split2, 'extended form of the 1572 key') | 9 Sept 1573 (ff. 135-137), 4 Jan 1573 (ff. 126v-127v) | 9 Sept read from the Court's verbatim decipherment (ff. 139-141); 4 Jan decoded ciphertext-only to ~55-60%, then found in Didier 1891 |

**Where it is merged:** Folder research/gallica_sweep/mondoucet. One profile, one method ('key recovered based on adjacent plaintext'), one fraction 0.864 pooled over three letters with three different outcomes; outcome.parts null; page blurb speaks of 'the keys'. 1572 vs 1573 key identity has some evidence (1573 key scores 56.2% on the 16 July block vs 60.3% for the 1572 key, chance 12-15%), but the 13 July 1572 letter's assignment to that key is untested: it reads 1-8% with both keys while the crib three days later reads 60%. NOTES attributes this to key quality ('the limit is the key'), which is not evidence that the key is the same.

**Risk:** medium: if 13 July is in another key, an unread key is folded into an 86% entry; even if one key, per-document outcomes (read at the time / ciphertext-only plus print / not solved) are pooled under one method.

**Proposed fix:** outcome.parts per document (or per key): 9 Sept read from existing decipherment; 4 Jan key recovered ciphertext-only then confirmed in print; 13 July not solved with key 'unknown (1572 key assumed, not confirmed)'. Report fractions per part. Test 13 July for a different key (IC/sign-inventory comparison with the 16 July block) before asserting same key.

**Evidence:** research/gallica_sweep/mondoucet/NOTES.md:3-13, 19-21 ('scores only ~60% on that same block, so the limit is the key'), :28 ('the 1573 key ... same system ... extended form'), :33-35 (56.2% with the 1573 key; 13 July ~8% lenient, ~1% strict); profile.json fraction_read_source pools 7,293 glyphs

### nevers1574

**Verdict:** UNCLEAR

| Key / cipher | Documents | Outcome |
|---|---|---|
| Birago's cipher (f.21 flap), not transcribed sign by sign | f.21, Birago, Italian, 28 Sept 1574 | read from the clear fair copy under the flap (complete) |
| duchess's cipher (f.15), alphabet not established | f.15-16, Henriette de Clèves, French, 16 Sept | interlinear decipherment read only at opening and clear ending |

**Where it is merged:** Two letters from different senders in different languages are given one system description ('Graphic substitution alphabet ... close to Nevers no. 2') and one pooled fraction 0.4. NOTES says 'Their alphabet' and plans to rebuild the table on f.21 and 'then apply that table to f.15', but no sign comparison between f.15 and f.21 was made (f.21 'not transcribed sign by sign'). The shared key rests on same volume/recipient/place/month.

**Risk:** medium: an untested shared-key assumption written into profile.system; fraction mixes a complete letter with a mostly unread one.

**Proposed fix:** Split outcome.parts per letter (f.21 complete from clear copy; f.15 partial from interlinear); mark the key relation as 'unknown' until signs of f.15 and f.21 are compared; reword NOTES/next-step so f.21's table is tested on f.15 rather than applied.

**Evidence:** targets/nevers1574/NOTES.md:1 (Duchess and Birago), :18 ('Their alphabet is very close to Nevers collection no. 2'), :60-61 ('align the f. 21 signs ... then apply that table to f. 15'), :63 ('The f. 21 cipher was not transcribed sign by sign'); profile.json fraction_read 0.4, parts null

### scorpion

**Verdict:** UNCLEAR

| Key / cipher | Documents | Outcome |
|---|---|---|
| S1 (70 symbols, weak period-5 evidence) | S1 | not solved |
| S5 (180 symbols, 16 alphabets in rotation) | S5 | not solved |

**Where it is merged:** Two passages with different measured behaviour (period 16 vs a weak period 5) share one profile, one system entry ('S5 ... 16 alphabets ..., S1 weakly like five') and one 'not solved' outcome; no claim that they share a key, and no parts. Both unsolved, so no reading is merged.

**Risk:** low: no result is overstated, but the profile counts one cipher where the evidence points to two systems.

**Proposed fix:** Add outcome.parts S1/S5 (each not solved) or state in system that the two are not shown to share a key.

**Evidence:** targets/scorpion/NOTES.md:16 'What the two ciphers are, measured'; profile.json system notes 'S5 ... 16 alphabets in strict rotation, S1 weakly like five', parts null

### sp95box136

**Verdict:** UNCLEAR

| Key / cipher | Documents | Outcome |
|---|---|---|
| unknown; candidates Swedish/French keys R7721, R7723, R7724/R7725 (Scheffer, Wynantz 1749-53) or Spanish R7801 (Grimaldi-Canis at Stockholm 1752) | SP95-136 (TNA SP 95/136, 1748-55, contents unseen) | not applicable (blocked on images) |
| unknown; candidate Spanish R7801 ('& Marq. del Puerto at the Hague') or R7793-R7795 | SP87-24-33 (del Puerto, 19 Mar 1748) | not applicable (blocked on images) |

**Where it is merged:** Two unrelated TNA items (Swedish supplementary volume and a Spanish ambassador's intercept in Cumberland's papers) grouped by the TNA label 'not deciphered'. Ciphertexts not seen, so whether they share a key is unknown; system.types ['undetermined'], one outcome 'not applicable', no outcome.parts. No page or README row (Status: blocked).

**Risk:** If images arrive, a reading in one key (e.g. R7801 for del Puerto) could be credited to the whole two-item target; Swedish and Spanish key statistics would be mixed.

**Proposed fix:** When images are obtained, split per key found (likely sp95box136 for the Swedish volume, sp87del-puerto1748 for SP 87/24/33), or add outcome.parts per item from the start.

**Evidence:** NOTES.md title and 'What the target is' (two TNA items); profile system.summary 'Not seen'; system.sibling lists Spanish R7801/R7793 and Swedish R7721/R7723/R7724; outcome.notes 'key none because no key is yet tied to these letters'

### throck1560

**Verdict:** UNCLEAR

| Key / cipher | Documents | Outcome |
|---|---|---|
| unknown: one of Throckmorton's ciphers (R9260 first/second, R9262 third), 'third' likely | R3026a, 8 Feb 1560 (to Cecil) | read from existing decipherment (Forbes 1740, CSP ii 706) |
| unknown (as above) | R3026b, 20 Feb 1560 (to the Council) | read from existing decipherment (Forbes 1740, CSP ii 751) |

**Where it is merged:** No images; key not testable. Both letters are put under one 'undetermined' Throckmorton system; NOTES is careful ('cannot be tested without images', third cipher 'likely'), but the profile holds one system for two letters whose keys are both unknown, which George says must not be merged just because both are unknown.

**Risk:** low (no write-up, no page, read from print)

**Proposed fix:** Keep system 'undetermined' per document; say explicitly that the two letters' keys are unknown and not assumed equal; no shared-key claim until images are seen.

**Evidence:** targets/throck1560/NOTES.md:29-31 'Which one applies to ff.100-101 cannot be tested without images'; profile.json system 'undetermined'

### throckmorton

**Verdict:** UNCLEAR

| Key / cipher | Documents | Outcome |
|---|---|---|
| Throckmorton's 'third cipher' (DECODE R9262, Add MS 4136 ff.180-185) | verified only on R9220 (27 tokens) and R9230 (15 tokens) | read from existing decipherment (Forbes 1740-41), two samples checked against the key |
| Throckmorton's first and second ciphers (DECODE R9260) | not assigned; any of the other 18 records (1560-63) may use them | not tested |
| other writers' keys (e.g. Thomas Smith on f.169) | R9255 (composite: Smith on f.169 + Throckmorton to the Queen) | not verified |

**Where it is merged:** Twenty records grouped by volume (BL Add MS 4136 = Forbes Papers V) and sender. NOTES itself says three Throckmorton ciphers survive (R9262 'third cipher', R9260 'contains the first and second', NOTES.md:52-53) and that R9255 is composite with other writers (NOTES.md:17, 104), but profile system.summary describes only the third cipher ('The sampled Throckmorton passages use the archived third cipher'), parts = null, one method 'read from existing decipherment' and class 'already solved' for all 20. README.md:354 status 'complete', 'Archived key and prior printed plaintext verified', while NOTES.md:3 says 'Status: in progress'.

**Risk:** README and profile imply all twenty records are in one verified key; which of the three Throckmorton ciphers each record uses is not established, and R9255's non-Throckmorton material is counted as solved by Forbes; DECODE corrections could assign R9262 as key to records in cipher 1 or 2.

**Proposed fix:** Assign each record to a key (first/second from R9260, third R9262, Smith key) by date and sign shapes; add outcome.parts per key with the records covered and 'verified' vs 'matched to print only'; split R9255's Smith part out; set README status to match NOTES (in progress).

**Evidence:** targets/throckmorton/NOTES.md:52-53 'R9262 is headed Sir Nicholas Throckmorton's third cipher. R9260 contains the first and second'; NOTES.md:17 'R9255 is composite'; profile.json system.summary 'The sampled ... passages use the archived third cipher'; README.md:354 'complete'

## Several keys, already presented per key (leftovers noted) (6)

### gilino1527  (Lasry entry)

**Verdict:** SPLIT-OK  
**Lasry:** solution (independent ciphertext-only reconstruction of the same key, PR #34)

| Key / cipher | Documents | Outcome |
|---|---|---|
| Sforza chancery key DECODE R5258 | R8572 Cotton Vesp. C IV ff. 214-218, 15 Sep 1527 | read after matching with key from external sources, 0.961 (project route); key recovered from ciphertext-only (Lasry's route) |

**Where it is merged:** None now: the Gilino letter was split on 14 Oct 2026 from the combined 'superscript' target, where it sat with the Ghinucci material only because both use superscript numbers. Same key, two routes, compared on 106 numbered signs (101 agree). Lasry's route is a credit only; outcome.method records the project's matching route.

**Risk:** low

**Proposed fix:** optional: record Lasry's ciphertext-only recovery as its own contribution (e.g. outcome.parts or a second method entry) so the paper counts two contributions of one cipher.

**Evidence:** targets/gilino1527/NOTES.md:89-91 'split from the combined superscript target ... They are not [about the same key]'; NOTES.md:97 'Same key, two routes ... agree with R5258 on 101 of 106'

### ferdinand3

**Verdict:** SPLIT-OK

| Key / cipher | Documents | Outcome |
|---|---|---|
| 1635 alphabet (from draft R954) | R1889 | key recovered based on adjacent plaintext, complete 97.2% |
| 1640: R1889 alphabet + AEIOU syllabary | R1890 | key recovered from ciphertext-only (syllabary), complete |
| 1634 different vowel-series repertoire | R1887 | key recovered based on adjacent plaintext (in-letter crib), partial 88.4% |

**Where it is merged:** Grouped by correspondents (the two Ferdinands) and shelfmark (AGR SEA 540). Mitigated: outcome.parts per letter, README split into three rows ('Split entry, part 1/2/3 of 3', README.md:104, :203, :204), page h2 per record. Residual: one profile-level outcome.method ('key recovered based on adjacent plaintext', which is wrong for R1890) and one fraction_read 0.959 averaging the complete and the partial letters; system.types merges both repertoires.

**Risk:** Low. Top-level method/fraction could be used by the paper analysis instead of parts, misclassifying R1890 and hiding R1887's partial status.

**Proposed fix:** Keep as is; ensure the analysis uses outcome.parts; optionally move R1887 (different key) to its own folder ferdinand1634.

**Evidence:** profile sys.sibling_key 'R1887 shares only the vowel-series principle'; system.summary '1634: a different repertoire'; outcome.parts x3

### malsburg1637

**Verdict:** SPLIT-OK

| Key / cipher | Documents | Outcome |
|---|---|---|
| Malsburg numerical homophonic table + nomenclator | HCPortal 496-509 (ff. 3-33), incl. the French letter signed 232 and news extracts, 'same key' | key recovered from ciphertext-only (Bourdeau), complete 95.9% |
| period-five alphabetic shift cipher (4,5,3,6,2 over 24 letters) | ten-line block at the foot of image 0012 (HCPortal 497) | key recovered from ciphertext-only (Beck with ChatGPT, PR #17), partial |

**Where it is merged:** Properly separated: outcome.parts one per system, outcome.notes 'Overall fraction and code totals are unknown because the distinct systems are not combined', page has h2#letter-block, README row names the separate block and its contributor. Residual: top-level fraction_read 0.959 is the numerical part only while class 'read in part' reflects the block; one physical document (497) carries both systems, which is stated.

**Risk:** low; top-level fraction could be read as covering the alphabetic block.

**Proposed fix:** none essential; label top-level fraction as numerical-system only.

**Evidence:** targets/malsburg1637/profile.json outcome.parts (two systems); outcome.notes 'the distinct systems are not combined'; docs/malsburg1637.html h2#letter-block

### rupert

**Verdict:** SPLIT-OK

| Key / cipher | Documents | Outcome |
|---|---|---|
| f. 106 lower alphabet (graphic-sign substitution, key R8727) | BL Add MS 72438 f. 107r (R8728) | read with known key, complete (95.3%) |
| Maurice's 'your cipher' (unknown numeric nomenclator) | Maurice to Rupert 7 Jul 1645 (Warburton iii.133) | not solved |
| f. 9 key (no group above 343) and a different f. 10 key (groups to 697) | R8623 (f. 9), R8624 (f. 10) | not solved |
| unknown numeric keys | R8725 (f. 104), R8433 (Trevor, Add MS 18982 ff. 51-52) | not solved |

**Where it is merged:** Mostly split: outcome.parts gives one part per group, the page has separate sections (rupert.html:91-104) and README has a separate row for f. 107 (README.md:245) and one for the unread letters (README.md:376). Residual merges: the top-level outcome.method 'read with known key' and fraction_read 0.0864 pool f. 107 with five unread ciphers; the part 'Cryptiana #6, Add MS 72438 f. 9 ... and f. 10' joins two documents whose keys differ (system.notes 'f. 9 and f. 10 use different keys'); the part for f. 104 + Trevor joins two unrelated letters; system.types merges nomenclator and the f. 107 monoalphabetic; f. 107 is grouped only because it sits in the same volume.

**Risk:** Paper statistics: the target counts as 'read with known key' though the read piece (f. 107) is an unrelated letter found in the same volume and the cryptiana targets are all unread; the 8.6% blends keys. Low risk of crediting a reading to the wrong document since parts and page are explicit.

**Proposed fix:** Move f. 107 (R8727/R8728) into its own folder/profile (e.g. addms72438f107) with method read with known key; leave rupert as 'not solved'; split the f. 9 / f. 10 part into two parts and f. 104 / Trevor into two parts.

**Evidence:** profile system.notes 'f. 9 and f. 10 use different keys (f. 9 has no group above 343, f. 10 runs to 697)'; outcome.parts labels; outcome.method 'read with known key', fraction_read 0.0864; docs/rupert.html:6 title 'still unread; f. 107 deciphered'; README.md:245 and :376

### sanchez1522

**Verdict:** SPLIT-OK

| Key / cipher | Documents | Outcome |
|---|---|---|
| Alonso Sanchez's 1522 Venice cipher (Tomokiyo reconstruction, extended) | R9653, R9635 (profile documents); other Sanchez records of R9593-R9657 open | read with known key, partial (0.6 of code groups on the two leaves) |
| Lope Hurtado de Mendoza's 1522 Rome cipher (third member of the family) | R9634, R9644-R9646, R9648-R9650, R9652, R9656 - now its own target lopehurtado (README.md:185) | handled in target lopehurtado |

**Where it is merged:** Profile documents and system cover only Sanchez's key and NOTES says the Hurtado letters 'deserve their own target' (they now have one). Residual: README.md:314 row title still reads 'Alonso Sanchez (Venice) -> Charles V, and Lope Hurtado de Mendoza, 1522 ... DECODE R9593-R9657, 29 records', so the nine Hurtado records appear under both rows; page keeps an h2#hurtado section. Juan Manuel's Rome cipher is a sibling, not included.

**Risk:** Double-counting the Hurtado records; a reader of the README row thinks Sanchez's key covers Hurtado's letters.

**Proposed fix:** Retitle the README row to Sanchez only and state the record range excluding R9634/R9644-R9656; link the page's hurtado section to the lopehurtado target.

**Evidence:** targets/sanchez1522/NOTES.md:303 'The Lope Hurtado de Mendoza letters are not in Sanchez's cipher'; NOTES.md:313 'third member of the same family'; README.md:314 title 'and Lope Hurtado de Mendoza'; README.md:185 separate Lope Hurtado row

### soria1523

**Verdict:** SPLIT-OK

| Key / cipher | Documents | Outcome |
|---|---|---|
| key A (June-July 1523) | R9488-R9490, R9492-R9493 (body) | key recovered from ciphertext-only, complete (June 99.5%, July body 98.0%) |
| key B (from late July 1523; also in R9844) | R9491, R9492-R9493 (post data), R9494-R9498 | key recovered based on plaintext from external sources (R9844 + court decipherment), partial (94.0%) |

**Where it is merged:** Properly split: outcome.parts per key, README has two rows 'Split entry, part 1 of 2' / 'part 2 of 2' (README.md:101, 123), page has h2#keys and per-letter sections. Residual: top-level outcome.method 'key recovered from ciphertext-only', fraction_read 0.966 and class 'read' are pooled over both keys, though key B alone is 94.0% (below the read bar) and came from external plaintext. One letter (R9492-R9493) uses key A body + key B post data, correctly stated.

**Risk:** Analysis reading only top-level outcome.method/fraction would credit key B with a ciphertext-only break and 'read'.

**Proposed fix:** Keep the split; ensure the paper analysis uses outcome.parts; note top-level fraction is pooled.

**Evidence:** targets/soria1523/profile.json outcome.parts (two keys); README.md:101 'Split entry, part 1 of 2'; README.md:123 'part 2 of 2'; parts[1].basis '94.0% over the key-B letters'

## Fixed on main since the first snapshot (2)

### superscript  (Lasry entry)

**Verdict:** FIXED  
**Lasry:** solution (Gilino R8572 edition, ciphertext-only per his notes)

| Key / cipher | Documents | Outcome |
|---|---|---|
| Ghinucci/Worcester syllabic superscript-digit cipher (sibling key of R8476/R8589/R8590) | R8613 (target); R8476, R8589, R8590 key material | key recovered based on plaintext from external sources, 97.9% |
| Milanese Sforza key DECODE R5258 (Gilino) | R8572 | read after matching with key from external sources, 96.1%; Lasry independent reconstruction contributed 14 Oct |

**After George's review:** Split on main in ce30cf199 into ghinucci1527 (R8613) and gilino1527 (R8572); superscript.html is now a stub. The round-2 review checks the two new entries for surviving combined statistics or credits.

**Where it is merged:** Two unrelated ciphers grouped only because both are in Cotton Vespasian C IV/1527. Mitigated: outcome.parts per key, README split into two rows ('Split entry, part 1 of 2'/'2 of 2', README.md:124, :232), page h2 per record. Residual: one folder/profile/page ('Ghinucci to Wolsey and Gilino to Sforza, 1527 â€” Read'); system.types/summary describe only the Worcester cipher, Gilino only in system.notes; single outcome.method (Worcester's) and single fraction_read 0.965 averaging both; Lasry's credit (role 'solution') sits at entry level, not on the R8572 part; page h2 'Key' (unnumbered, after section 04) shows Lasry's Gilino key without a caption tying it to R8572 only.

**Risk:** Entry-level Lasry 'solution' credit and the badge read as if he solved Ghinucci R8613; paper statistics (one method, one fraction, system.types) treat Gilino as a Worcester-type syllabic cipher. Lasry's Gilino method (crib/pattern, no external key) is not recorded as a part, so his ciphertext-only result vs project's external-key match is conflated.

**Proposed fix:** Split into targets/superscript (Ghinucci R8613) and a new targets/gilino1527 (R8572) with its own profile/page; or at minimum put Lasry's credit on the R8572 part, add his method as a separate part/credit, give Gilino its own system block, and caption the page 'Key' section 'Gilino (R8572) key, George Lasry'.

**Evidence:** profile system.notes: 'Gilino R8572 is a different (Milanese) system'; outcome.parts two entries; credits lasry role 'solution' note 'Contributed Gilino R8572 edition'; NOTES.md:207-209; docs/superscript.html h2 list

### vasto1527  (Lasry entry)

**Verdict:** FIXED (in part)  
**Lasry:** key or decipherment used (Cipher 2, no. 6); prior solution (Cipher 1, no. 10); solution (Ranzo code, 14 Oct 2026)

| Key / cipher | Documents | Outcome |
|---|---|---|
| Gasto-Charles V Cipher 1 (Lasry 2023) | BnF fr. 3022 no. 10 (ff. 26-28 + f. 39) | read from existing decipherment (Lasry/Tomokiyo), partial, not reworked or measured |
| Gasto-Charles V Cipher 2 (Lasry 2026 key, extended here) | fr. 3022 no. 6 (ff. 16v-17v); no. 19 (ff. 40-43) same key, not transcribed | read with known key, 98.0% measured |
| Ranzo/Garbino code (initial letter + number) | fr. 3022 no. 20; fr. 2988 ff. 9-10 (DECODE R1894, copy R4450) | read from existing decipherment: Rosson key (79.8% no. 20, 93.1% R1894 in connected stretches) and Lasry's independent 871-entry key; not by us |

**After George's review:** Ranzo's code moved to ranzo1528 in ce30cf199; vasto1527 now keeps Cipher 2 (no. 6) with no. 10 (Cipher 1) as a cross-reference. Still open: Cipher 1 must stay separately identified wherever it is kept, and ranzo1528's profile lists 2 documents while George's package covers five letters (targets/ranzo1528/lasry/NOTES.md:21).

**Where it is merged:** Three different systems grouped by volume (fr. 3022) / catalogue item 7. outcome.parts are per key (good), but: system.summary 'Nos. 6/10: Caesar-shifted substitution ...' treats Cipher 1 and Cipher 2 as one system; system.types merges homophonic+code; single outcome.method 'read with known key' covers all; fraction_read 0.5485 pools Cipher 2 tokens with Ranzo-code groups and is stale ('no. 20: 0 of 1,321 groups') while parts say 79.8%; NOTES verdict table still says no. 20 'not solved'; Ranzo part basis names only Rosson, Lasry's 14 Oct solution is a credit but not in parts; README row title implies one del Vasto solution.

**Risk:** Paper/scoreboard counts one 'read with known key' result for what is three outcomes (one ours-with-Lasry-key, two others' readings); the pooled 54.85% is neither key's figure; Lasry's Ranzo solution and Cipher 1 reading may be credited to the 'del Vasto' entry as a whole or lost; Cipher 1 described with Cipher 2's key structure.

**Proposed fix:** Split into vasto1527 (Cipher 2: no. 6 + no. 19), vasto1527-cipher1 (no. 10, read from Lasry/Tomokiyo, no write-up or short) and ranzo1528 (no. 20 + R1894/R4450, Rosson and Lasry solutions). At minimum: per-key system entries, fraction_read only over no. 6, update no. 20 status, add Lasry to the Ranzo part's basis.

**Evidence:** profile system.summary 'Nos. 6/10: Caesar-shifted substitution'; NOTES.md:10 'Gasto-Charles V Cipher 1'; NOTES.md:22 '## No. 6 / Cipher 2'; NOTES.md:12 no. 20 '**not solved.**'; profile fraction_read_source 'no. 20: 0 of 1,321 groups'; NOTES.md:189 'George Lasry's independent Ranzo contribution'; README.md:297

## One key throughout (311)

Checked and found to use a single key (or one key with minor revisions): acciaiuoli1757, alessandrino1568, bianchi, bizozola1520, bossuet, ceva1632, clair460alpha, colonia1721, decode4282, duquesne1681, egmond, florence1429, forster, goring1645, guise1587, labbe1582, lucca, lucini1767, marechaux1520, mellon136, memoire1560, mercoeur1587, nuncio1566, nunzio1718, nunzio1736, pallotto1629, r1892, ranzo1528, rupert1645, sauli1579, sega1591, siena1431, sormano, sormano1529, sp106r927, vatican, vatican5, visconti1528, visconti1529, R1942, R1944, abwehr, adrian1521, aerssen1601, andreae1616, anne1711, armstrong, augurelio1535, ayala1516, bagno1652, balbases1677, baner1640, battier1686, bay1706, bayard1526, berny1607, bertelot, bethune, bethune1629, beuningen1676, birago, birago1571, blancmesnil, blasco1597, blume, bonzagni1512, boswell, boswell1628, bouillon1650, breves1603, breves1610, brienne1067, brienne5160, buda1489, burghley1559, burghley1572, burgo1527, caracciolo1537, carpio1677, catinat1691, catokwacopa, censorship, charles1536, charlesixducroc, chatillon1635, chaulnes, chodkiewicz1575, cifuentes1534, clair1161, clair1225, clair357, clair460bar, clair460num, cobham1588, cocquet, colbert, coligny1563, conley1652, copenhagen, dagapeyeff, dampierre1589, debosnys, desmarets1710, destaing, dinteville1592, dubellay1555, dubellay65, ducroc, dupuy155, dupuy468, eichel1758, enigma, erving1807, erving1807aug, esterhazy1744, estrada1503, eugenie1859, fagel1804, ferdinand1619, feuquieres, feuquieres1678, feynman, florence1414, fogliani1568, fr14765p351, fr3029, fr3029f134, fr3092, fr3321dc, fr3575f56, fr4696num, ghinucci1527, goertz1717, goldbar, gondi1594, gonzaga1590, haga1620, hamilton, hamilton1569, harley1582r8499, harley1582r8500, harley1582r8504, harley1582r8505, harley286, harley287, harley6345, harley7001, henter1707, herbault1625, herbault1626, hernannunez1674, hesse1603, hesse1672, hesse1824, heusner1637, hyde, ilten1743, isabella1531, it1583, jantini1517, jeannin1607, joachim1530, jones1753, joyeuse, jqa, kaliningrad, kauderbach1754, kurtz1639, laboderie1608, lanssac, lebel1593, lee1526, lerouge, letellier, lodi1584, loeschnen1816, lomer1563, lopehurtado, lorraine1592, louis1635, lucinge1588, mai1531, malvezzi1548, marburg1635, maria1435, matthias1482, medici1425, mellon29, mendoza1589, mercoeur1586, mercy1648, meryvic1589, milroy, moncada1524, mondesir1769, moray, muxetula1531, napoleon, needham1587, nevers1587, nevers1588, nevers1589, nevers1594gondi, nevers1595, nino1522, norfolk1570, norreys1567, orbais, ormanetto1573, ormanetto1576, ormonde, ottobon, paleologue1562, palm1727, pelissier1592, percy1559, perwich, portugal1667, poupet1522, poyntz1527, prussia1702, r1212, r1818, r1862, r1874, r1875, r2232, r2234, r2242, r2276, r3708, r4157, r4817, r688, r7707, r8356, r8358, r8361, r8362, r8364, r8870, r8871, r9658, raince, rakoczi1707, randolph1570, rangone1530, rechteren1785, renard1554, renard1556, rennes1563, richelieu, roell1809, rondinelli1590, ronquillo1676, roosevelt, sadler1543, sadoleto1482, salviati1525, sanchez1523, santacroce1552, schiner1516, scipion1585, sega1593, segura1596, selve1535, sessa1523, sessa1524, sg1629, sinzendorff1578, sloane3188, smith1562, soglia1848, soria1527, sp106r597, sp53, spaen1808, sperantio1534, spinelly1516, stafford1586, stepney, stowe166, szembek1689, throck1569, toledo1565, toulon1803, tranchedini1452, turenne1528, ungnad1576, vanreede1792, vargas1552, vergier1696, vetesi1705, vieuville1587, villardeau, villeneuve1737, villeroy258, visconti1727, vizani1637, vulcob1573, waldeck1744, walsingham1572, walsingham1572nov, walsingham1581, warsaw, wesselenyi1664, windischgraetz1721, wotton1585, yard1699, zeschau1841, zhongshan.

