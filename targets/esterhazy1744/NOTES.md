# Esterházy papers, box 636: six digit-cipher documents of 1744 (Slovak National Archives; catalogue 344)

Closed 9 Oct 2026 as attempted, open. Only one partial page of the six documents is online, and no
1740s Habsburg key on DECODE fits it. The blockers are listed under Remaining gaps.

## Source

- Slovenský národný archív (Slovak National Archives), Bratislava, fond Esterházi – čeklíska vetva, box no. 636.
- Published description: E. Antal, P. Marák, P. Zajac, T. Lengyelová, D. Duchoňová, "Encrypted Documents and
  Cipher Keys From the 18th and 19th Century in the Archives of Aristocratic Families in Slovakia", *HistoCrypt
  2023*, Linköping Electronic Conference Proceedings 195, doi:10.3384/ecp195689
  (https://ecp.ep.liu.se/index.php/histocrypt/article/view/689). The PDF and the figures extracted from it are in
  `src/` (git-ignored).
- What the paper says about box 636 (section 2.1): six encrypted documents, one fully encrypted draft and five
  letters, five in French and one in German, all dated 1744. One is from Empress Maria Theresa to Count Nicolaus
  Esterházy; the other correspondents were not identified, and "the corresponding plain text parts are not
  available". Section 2 says the keys in the three fonds (seven Pálffy-Daun keys of the Spanish Succession war, two
  Üchtritz keys) do not match the ciphertexts. Nor do the "possibly related" keys the authors tried from Vienna and
  from Hungary. The same fonds hold box 631 (one German cipher letter, 1744), box 634 (Esterházy–Kaunitz
  1756–57, 41 documents, most with separate decipherments) and box 635 (letter drafts of 1741 and 1744 with nine
  short enciphered passages under their clear text).
- Images: the archive has 4160 × 6240 px scans. The authors planned to put the collection on HCPortal. As of 9 Oct
  2026 it is not there: the local harvest (`research/catalogue_harvest/hcportal/index.json`, ids to 1499) has no
  Slovak National Archives Esterházy record, and a live scan of ids 1500–2032 found only HCPortal postcards (ids
  1600–1881). DECODE has no Slovak National Archives records. The only image online is **Figure 6** of the paper.

## Figure 6: the Moscow letter of 5 Oct 1744

Figure 6 shows the upper part of one page (`src/p3_x9.jpeg`, 2496 × 1604 px as embedded in the PDF):

- Clear heading: *Moscau ce 5e d'octobre 1744. J'ai reçu avec un tres profond respect les Re- & Postscripts de
  Votre Majesté en date du 15e Septembre.*
- Eleven lines of dot-separated numbers.
- Clear text resumes: *La refutation de l'Imprimé de la Cour de Vienne est trop solide, pour ne pas …*

The letter is a despatch from the court of Russia, which was at Moscow in 1744, to a sovereign. The Vienna court's
printed refutation is presumably its answer to the Russian charges in the Botta affair of 1743. The writer is not
named on the visible part. Philipp Joseph Orsini-Rosenberg, Austrian ambassador at the Russian court from mid-1744,
writing to Maria Theresa, fits, but this is not established. A Saxon or other envoy writing to his king is not ruled
out. Why a copy lies in the Esterházy papers is open as well: Nicolaus Esterházy was then Maria Theresa's envoy in
Dresden. Do not cite the sender as known.

Transcription: `transcription/fig6_moscow_1744-10-05.txt` (176 groups, 157 distinct; measured with
`docs/_check_profile.py --measure --digits`). Four groups are uncertain and the underlinings are recorded in the
file header.

## The cipher (from the sample)

- Values 7–1737 (164 groups) plus a separate block 3018–3297 (12 groups). The groups under 1738 are spread evenly
  over every hundred from 0 to 1700.
- Six groups under 100 (7, 19, 24, 54, 77, 83). The 1745 circular-cipher instruction on DECODE R1598 tells the
  clerks to insert two-digit nulls "ad libitum", so these may be nulls in the same chancery style.
- 157 distinct of 176. Repeats: 1337 and 536 three times; 1240, 680, 661, 1491, 711, 1437, 795, 1137, 1599, 132,
  1513, 1631, 1440, 3049 and 1059 twice each. No repeated bigram.
- This is a code or large syllabic nomenclator of about 2,000 values, of the Viennese chancery kind (see the keys
  below). It is not a small homophonic alphabet.

## What was tried (9 Oct 2026)

1. **The paper and the images**: see Source. Only Figure 6 is available.
2. **DECODE keys of the Vienna chancery, 1740–1746** (`decode/`, images git-ignored; fetched with the saved cookie).
   Every dated HHStA key record of 1735–1750 in the DECODE harvest was listed. The ones in range were opened:
   - R1594 (Stk Int Chiffrenschlüssel Kt. 15 Fasc. 21 ff. 88–103): *Teutscher Circular Ziffer von anno 1745 zum
     aufschlüssen*, copy for Rosenberg, Wasner, Esterhasi, Colloredo, Cotheck, Batthiani, Bretlach, Reischach, Bernes,
     Boßard, Stolte. German; values 100–1500.
   - R1597 (ff. 106–119): *Französischer Circularziffer von anno 1745 zum Setzen*, same envoy list. French encipher
     table; values 101–1355, with punctuation at 1343–1353.
   - R1596 (f. 105): the decipher table of the same French circular (101 W, 102 wa, 103 Wasner …), with the 1300s
     and 1400s blank. Cover *Chiffre françoise … (174.)*.
   - R1595 (f. 104): a circular decipher table, values 101–1499. Cover *Französisch[er u.] Teutsch[er] circular
     Ziffer (174.)*.
   - R1598 (f. 120): *Pro Informatione*, the instruction for the circular cipher. It gives the dotted number
     notation and the inserted two-digit nulls, with a worked example.
   - R1593 (ff. 80–87, 1746): a multi-table key with column headings in the 2000s; R1601: a table-switching key
     with 2201… headings; R1562 (1743): German, values under 1000; R1574 (1740): German, values to about 2300;
     R1644 (1740) and R1691 (1741): small keys (DECODE transcriptions `DOC_R1644_*`, `DOC_R1691_*`).

   None of them covers both 1500–1737 and 3000–3297. The 1745 circulars come closest in style (Rosenberg and
   Esterházy are both on the distribution list), but the sample is 1744 and its values run past theirs. Ruled out
   by value range. No key was applied group by group.
3. **Print and the web**: searched for a reading of box 636 or of the Moscow letter; none found. The search
   turned up a sibling: Dorotheum, autograph sale of 17 Dec 2024, *Kaiserin Maria Theresia, Chiffriertes
   Schreiben, Wien, 31. 7. 1744*, to Esterházy as envoy in Dresden (blog post "The Empress's Code",
   blog.dorotheum.com/?p=62008, read through search snippets; the page itself is behind a bot check). Dorotheum
   describes a three-digit word code. It says a copy of the key survives in the Austrian State Archives and that
   the letter can be deciphered almost completely; content: Prussian approaches to the Porte, and an order to come to
   terms with Saxony. That letter is not in box 636. Its key, three-digit by Dorotheum's account, would not
   produce the four-digit groups of the Moscow sample.
4. **Ciphertext-only**: not run. With 176 groups from a code of about 2,000 values, 89% of them distinct, no
   frequency, pattern or language-model attack has anything to fit. This is a reason for not running one, not a
   solver failure, so no control was needed.

## Remaining gaps
- the six box-636 documents (only 176 groups of one shown in print) - blocker: needs-physical-access; the archive's scans are unpublished; order images of fond Esterházi - čeklíska vetva, box 636 from the Slovenský národný archív, Drotárska cesta 42, Bratislava
- the 1744 key - blocker: no-key-material; no DECODE key of 1740-1746 covers the values 1500-1737 and 3000-3297; the candidates are the HHStA Staatskanzlei keys for Russia and Saxony of 1744 (and the Maria Theresa - Esterházy Dresden key Dorotheum says is in the ÖStA), none of them on DECODE

## Escalation
- [x] siblings: boxes 631, 634, 635 of the same fonds are described in the paper but not online; the Dorotheum 31 July 1744 letter is a sibling with a key in the ÖStA, not imaged in full
- [n/a] clear-pages: the paper says no plaintext exists for box 636; the only image is Figure 6
- [x] known-keys: DECODE HHStA keys R1562, R1574, R1593-R1598, R1601, R1644, R1691 checked; none fits the value range
- [x] print: Antal et al. 2023; web and Dorotheum; HCPortal; nothing prints a reading
- [n/a] key-rebuild: nothing reads, so there is nothing to extend; 176 groups of a 2,000-value code cannot seed a rebuild
- [n/a] retry: no reading to retry

## What would move it

1. Images of box 636 (all six documents) from the Slovak National Archives. With about 1,000 groups or more,
   and the German document as a second language, a partial rebuild from repeated groups might be possible.
2. Box 635: its 1741/1744 drafts carry enciphered passages under their clear text. If they use the same 1744 key,
   they are cribs for box 636.
3. In Vienna (HHStA): the Staatskanzlei Chiffrenschlüssel for Russia and Saxony of 1744, and the key Dorotheum says
   accompanies the Maria Theresa–Esterházy letters of 1744.

## 3 Nov 2026: the sender may be Prussian, which changes where to look for the key

This revises the sender discussion and the key candidates above. It does not read the letter. The method stays *not solved*.

**Hypothesis: Axel von Mardefeld, Prussian envoy at the Russian court, to Frederick II. Inferred, not established.**

- The clear text praises "la refutation de l'Imprimé de la Cour de Vienne" as "trop solide". An Austrian envoy would hardly write that to Maria Theresa, or call his own court "la Cour de Vienne" in this way, so the Rosenberg reading above looks unlikely. The print need not concern the Botta affair either.
- The dispute fits. Vienna printed its *Beantwortung* of Dohna's declaration on 22 Aug 1744. Berlin answered with the *Widerlegung … Scheingründe* (Berlin, Gäbert, 1744), French title *Refutation du Memoire publié par la Cour de Vienne* (Koser, *Preussische Staatsschriften* I, 477-482; *Politische Correspondenz* III, 265 n. 1).
- Mardefeld is addressed "à Moscou" in 1744 and his reports are quoted in French ("J'ai reçu les ordres…", PC III, reports of 21 May and others). No. 1621 (29 Oct 1744) acknowledges his relations of 28 Sept and 1 Oct, so a report of 5 Oct fits his rhythm. "Re- & Postscripts" fits a ministerial rescript with a postscript.
- Open points. The 5 Oct relation is not quoted in PC III. The French *Refutation* went to the legations only on 20 Oct (Koser), so a paper received with a rescript of 15 Sept would be the German text or a manuscript, and that link is unproved. Another anti-Viennese court's envoy is not excluded. Nothing here explains for certain why the sheet is in the Esterházy papers. Vienna did hold intercepted Prussian despatches that autumn (the printed Schmettau papers of 16 Oct 1744), and Rosenberg passed one to Bestuzhev (Berlin to Mardefeld, 15 Dec 1744, quoted by Koser), but this does not show that this letter was intercepted.

**If this holds, the key and the plaintext are Prussian, not Viennese.** The HHStA Russia/Saxony keys are then the wrong place for this letter (the other box-636 letters, including Maria Theresa's, are a separate question).

- *Text:* the received, deciphered relation should be in the Geheimes Staatsarchiv PK, Berlin, Russia series (series not checked; I. HA Rep. 11 Russland or Rep. 96 are the likely ones). A matched copy would allow a key from external plaintext.
- *Key:* DECODE R4366, BL Add MS 32276 f. 37, dated 1744, "Prufsia", sender "Scholing?", a British Deciphering Branch table. Only 200 px thumbnails were seen; it needs a DECODE login. It may belong to another Prussian correspondent. R4367 (1745, Andrié) is a weaker second. R2824 ("cipher_Prussia_1746") was already rejected as a Prussian lead in `targets/hellen1752/AUDIT_2026-09-20.md`.

**Also new**

- Keys tested: 71 tables in this repository scanned by coverage. R596 (values to 3293) applied with its null rules gives 98 of 176 nulls, close to the 57% expected by chance, and no sentence: ruled out. The envoy table of `targets/r1955/` was not tested.
- The 3xxx block: 6 of 12 such groups stand first or last on a line, against 22 of 176 slots (permutation p about 0.001). The pattern was noticed after looking, so it is only a pointer. It may mean names, nulls or a habit of the copyist.
- Verso show-through in the figure: `transcription/fig6_verso_showthrough.txt`. Low confidence, not counted. It includes "… que ce Marquis [?] y est arrivé", so the same document has more clear text and more groups in the same value range.
- Ciphertext-only: still not run, for the reason given above. 140 of the 157 distinct groups occur once.

Sources: *Politische Correspondenz Friedrich's des Grossen* III and IV (Internet Archive `politischecorres03freduoft`, `politischecorres04fred`); Koser, *Preussische Staatsschriften* I (`bub_gb_HUguAAAAMAAJ`). OCR text, checked only where quoted; page references should be confirmed on the images.

### Remaining gaps, added 3 Nov 2026
- the sender hypothesis and its plaintext - blocker: needs-physical-access; request Mardefeld's relation of 5 Oct 1744 from the GStA PK, Berlin
- key test against R4366/R4367 - blocker: needs-physical-access; DECODE login needed for full images and transcriptions

## 3 Nov 2026, later: R4366 and R4367 tested, both ruled out; GStA files located

Images of both records were supplied by the contributor (not committed). Transcriptions are in `keys/`; both are first passes.

- **R4366** (BL Add MS 32276 ff. 37-38v, docket "Scholings Papers. Prussian. 1744"): a table to 1075, filled only to about 950, values 1-54 torn. 44 of the 78 sample groups in 55-950 fall on filled cells; distinct values 39 of 71 (55%), against a fill rate of 52% (P = 0.34). 80 sample groups lie above the table. The decode gives no sentence. Ruled out for this letter (`keys/test_r4366.py`).
- **R4367** (ff. 40-41, docket "Andrié 1745. Old Cyphers out of Use"): 1-2198, no 3xxx. Under a code of that range, 164 groups would all miss 1738-2198 with probability about 1.7e-17, while its 2001+ cells hold common items such as "Vre Majesté". The decode gives no sentence. Ruled out for this letter (`keys/test_r4367.py`).
- These tests say nothing against the Mardefeld hypothesis: they show only that these two Prussian tables are not this code.

**GStA PK files (Archivportal-D, read 3 Nov 2026; catalogue entries only, no documents seen, no digitisation shown):**

- I. HA Rep. 96, Nr. 55 C and Nr. 55 D, both "Schriftwechsel mit dem preußischen bevollmächtigten Minister Axel Freiherr von Mardefeld in St. Petersburg und Moskau", 1744 (Geheimes Kabinett). The entries do not say which holds October. Neighbours: Nr. 55 B (1743), Nr. 55 E (1745).
- I. HA GR, Rep. XI Russland: the ministerial series, likely for a report answering "Re- & Postscripts". Cited for a 1746 Mardefeld text as "Rep. XI Russland 91, 54 E" (vostlit edition); the 1744 file numbers were not found online.
- VI. HA, Nl Mardefeld, A. v. (1719-1748): his papers, which might hold drafts or cipher material; contents not seen.

The report of 5 Oct 1744 itself has **not** been seen, so it is not yet confirmed that it exists or that it is the same text.

## 3 Nov 2026, later: where Mardefeld's 1744 letters are, from Liechtenhan 1998

F.-D. Liechtenhan, "La Russie d'Élisabeth vue par des diplomates prussiens (1)", *Cahiers du monde russe* 39/3 (1998), 253-282, cites Mardefeld's letters to the King by file and folio (PDF supplied by the contributor; read by OCR, so check numbers on the page):

- **I. HA Rep. 96, Nr. 55 C:** letter of 11 Jan 1744 at fol. 13 (n. 66), letter of 26 May 1744 at fol. 178 (n. 44). The file therefore starts about January 1744 and is at fol. 178 by late May. **Nr. 55 D is the likelier place for October**, by inference only; nobody here has seen it.
- **I. HA GR, Rep. 11 Auswärtige Beziehungen, Nr. 171-175 Moskau (Russland), Konv. 46 B:** fol. 295 is cited for "la description de Mardefeld en 1744" (n. 19). The date of that piece is the only dating evidence for the Konvolut, so Konv. 46 is a candidate series for 1744, not a confirmed one. Other Konvolute cited: 49 C, 50 B, 54 E (the 1746 memorandum), 56 A (1748).

This corrects the shorter citation "Rep. XI Russland 91" used above: request the series as Rep. 11, Nr. 171-175 Moskau (Russland).

Context, not evidence for this letter: Mardefeld's own memorandum says Goldbach deciphered foreign ministers' despatches only when they were carelessly enciphered, and the article quotes a Russian postal report on his mail of 1745 (n. 105). So his post was watched. It does not show that this despatch was copied.

### Archive request, 3 Nov 2026

Jozef Krajčovič sent the enquiry to the GStA PK on 3 Nov 2026. It asks about Mardefeld's report of 5 Oct 1744 (Rep. 96 Nr. 55 D/C; Rep. 11 Nr. 171-175 Moskau, Konv. 46), the form it survives in, the rescript of 15 Sept 1744, any cipher key, and a quote for digital copies. No reply yet. The archive says it does not usually confirm receipt.
