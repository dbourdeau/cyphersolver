# Hard unsolved targets outside DECODE, scan of 23 Sept 2026

Goal: refill the unsolved catalogue with genuinely unread ciphertexts (1400-1900) with images online, needing a
ciphertext-only break. Scores are importance/solvability/difficulty (1-5). Each entry was grepped against
catalogue.json, CATALOGUE.md, TARGETS.md, SOLVED_CATALOGUE.md, README.md and folder names.

## Candidates

### 1. Esterházy papers, box 636: six cipher letters of 1744 with no plaintext (Slovak National Archives)
- **Date**: 1744 (War of the Austrian Succession). **Collection**: Slovenský národný archív, Bratislava, fond Esterházi, čeklíska vetva, box no. 636.
- **Content**: six encrypted documents: one fully encrypted draft and five letters, five in French and one in German. One is
  from Maria Theresa to Count Nicolaus Esterházy (1711-1764); the other correspondents are not identified. The
  paper says "the corresponding plain text parts are not available for these documents". Box 634 holds the
  1756-57 Esterházy–Kaunitz exchange in German, with 41 encrypted documents in at least two digit systems, one with
  separators and markups and one without. Most have separate decipherments, which can serve as cribs or a key
  source for the same chancery.
- **Cipher type**: digits-only nomenclator. The keys preserved in the same fonds (7 Daun keys, 2 Üchtritz keys) do NOT match, and neither
  do the HHStA and Hungarian keys the authors tried.
- **Length**: not stated per document. The collection has ~300 pages of ciphertext across 96 documents; box 636 is several pages.
- **Images**: the archive has 4160×6240 scans. The authors planned to publish them on HCPortal (hcportal.eu); check the
  HCPortal API (`api.hcportal.eu/api/cryptograms/<id>`, sent with a browser UA and `Origin: https://crypto.hcportal.eu`). Figure 6 of the paper shows one.
- **Prior art**: Antal, Marák, Zajac, Lengyelová, Duchoňová, "Encrypted Documents and Cipher Keys From the 18th and 19th
  Century in the Archives of Aristocratic Families in Slovakia", HistoCrypt 2023 (ecp.ep.liu.se/index.php/histocrypt/article/view/689).
  No decipherment of box 636 is reported; the paper covers transcription (YOLOv7), not solving.
- **Why hard/breakable**: Austrian diplomatic French in digits, probably with homophones and a code section. With six letters in one or more
  systems, a ciphertext-only homophonic attack on French is realistic, and box 634 gives same-chancery key shapes.
- **Score** (importance/solvability/difficulty): 3/3/4. **Not in repo** (grep Esterh/Slovak: none).

### 2. Leonard Niedźwiecki, "Tekst pisany szyfrem", Paris 23 Jan 1855 (Kórnik Library BK 02411)
- **Date**: 23 January 1855 (Paris), in a folder dated 1852-1863. **Shelfmark**: PAN Biblioteka Kórnicka, BK 02411 (microfilm Mf.1257),
  among the papers of Leonard Niedźwiecki (1810-1892), secretary of the Polish emigration (Hotel Lambert circle) and correspondent of Napoleon Feliks Żaba.
- **Content**: one full page of an unfamiliar symbol script (hooks, loops, x-marks, ~25-30 distinct signs, ~350-450 tokens). It is headed in clear
  "Paris, January 23rd 1855" and addressed "Newton Hanson Esq. M.D., Viaduct House, Brighton", with more symbols above the date.
- **Images**: https://www.wbc.poznan.pl/dlibra/publication/edition/218680/content (PDF: http://www.wbc.poznan.pl/Content/218680/247747.pdf), free.
- **Prior art**: none found (catalogue title only: "text written in cipher by Niedźwiecki"). **Caveat**: rule out an English
  shorthand system (Pitman 1837 / Taylor) before treating it as a cipher; the English address makes English plaintext likely.
- **Why hard/breakable**: an unknown glyph set of one page, probably a simple or homophonic substitution into English or Polish.
  Short, but the heading gives a crib (date and place), if the top symbol lines are a cipher heading.
- **Score**: 2/3/3. **Not in repo**.

### 3. "Anonymous cipher diary, 1776-1845", Massachusetts Historical Society Ms. Sbd-133
- **Date**: 1776-1845. **Shelfmark**: MHS Ms. Sbd-133. Found in the library of Theophilus Parsons Sr. (1749-1813) and given in 1841 by Theophilus Parsons Jr.
- **Content**: a small bound volume of dated entries (Arabic-numeral years, months and days in clear), in an unknown shorthand or cipher.
  Long entries on one side of the page and short ones on the other; ~70 years of entries, so thousands of signs.
- **Images**: only sample images in the MHS Beehive post (masshist.org/beehiveblog/2009/05/can-you-crack-the-cipher/); a full scan must be
  requested from MHS. Schmeh lists it as Encrypted Book List no. 00065, status unsolved.
- **Prior art**: unsolved as of the 2009 post; Benjamin Lynde Oliver Jr. (a 19th-c. MHS member) could not read it. No later solution found.
- **Why hard/breakable**: probably a personal shorthand-cipher of a Parsons family member. The clear dates segment the text into
  diary entries (the dated-entry structure is a crib source: weather, births and deaths, sermons). It has a long ciphertext, but the shorthand risk is high.
- **Score**: 3/2/5. **Not in repo**.

### 4. Otto von der Malsburg cipher correspondence, 1636-1637 (Hessisches Staatsarchiv Marburg, HStAM 4 h Nr. 1411)
- **Date**: 23 Feb 1636 to 1637. **Shelfmark**: HStAM 4 h Nr. 1411 ("Korrespondenz in Chiffren mit dem Generalkommissar Otto v.d.
  Malsburg betr. Kriegführung in Münster und Westfalen"), ff. 3-33. These are Hesse-Kassel's Thirty Years' War campaign in Westphalia.
- **Content**: 10 HCPortal records (ids 496-509: ff. 3-4, 12-13, 14, 15-17, 18, 23-24, 25, 28-29, 30-31, 32-33; f. 32-33 holds 3 messages).
  These are German letters, clear text with long cipher passages. The f. 3 letter, 5/15 Jan 1637, is signed by Otto von der Malsburg and has ~16 lines of cipher.
- **Cipher type**: a nomenclator of 2-digit groups separated by dots (values ~10-99, e.g. `27.39.13.95`), mixed with capital letters and dotted
  letter signs (`N`, `ƒ`, `H`, `R`, `Y`), which are probably code or name signs. It is probably homophonic.
- **Length**: ~250-350 groups on f. 3 alone; ~2,000+ groups across the file.
- **Images**: HCPortal media, e.g. https://api.hcportal.eu/media/1392/35901677515129.jpg (record 496, 2946×2312). The API needs a browser UA and
  `Origin: https://crypto.hcportal.eu`. Arcinsys Hessen may also have scans.
- **Prior art**: HCPortal marks all ten "Not solved". Antal & Mírka (HistoCrypt 2022, "Wrong Design of Cipher Keys...Marburg")
  studied the keys of this archive; no reading of 4 h 1411 was found. The repo has only `marburg1635` (HStAM 4 d Nr. 1218, a different system).
  **Check** whether any of the Marburg keys in 4 d Nr. 1219-1224 (HCPortal 519-523) fits before a blind attack.
- **Why hard/breakable**: a homophonic nomenclator on German with clear context (the same correspondent and campaign, with dates and places in clear) across 10+
  letters, well within reach of a homophonic hill-climber plus crib work on the nomenclator.
- **Score**: 4/4/3. **Not in repo**.

### 5. "Militärische Nachrichten für Fürst Carl August Friedrich (in Chiffre)", 1744 (HStAM 118 a Nr. 3954)
- **Date**: 1744 (War of the Austrian Succession). **Shelfmark**: HStAM 118 a Nr. 3954, ff. 3-4. The fonds is Waldeck; the recipient is Prince Carl August Friedrich of Waldeck-Pyrmont,
  an Imperial and Dutch general.
- **Content**: a report headed "Durchlauchtigster Fürst" and then wholly in code. It is a German military intelligence report.
- **Cipher type**: 3-digit code groups (1-999, with some 1-2 digit groups), dot-separated; a one-part or two-part code of ~1000 groups, with
  frequent repeats (e.g. 341, 447, 937, 298, 192).
- **Length**: ~330 groups on f. 3; f. 4 continues (two pages, so ~600 groups).
- **Images**: HCPortal record 517, https://api.hcportal.eu/media/1448/30811677522617.jpg and .../1449/51031677522617.jpg.
- **Prior art**: HCPortal "Not solved"; no key identified; nothing in print found.
- **Why hard/breakable**: a large code on a single report is the hardest class. It is breakable only with more traffic in the same code: other
  Waldeck reports in HStAM 118 a should be searched. Otherwise it needs a known-plaintext anchor (a 1744 campaign event).
- **Score**: 3/2/5. **Not in repo**.

### 6. Waldeck counts' ciphers, 1638 and 1646 (HStAM 115/01 Nr. 2602 and Nr. 1290)
- **Content**: Nr. 2602 ff. 2-3 is "Übermittlung einer Chiffre durch Graf Christian an seinen Sohn Philipp VII." (1638), Count Christian of Waldeck-
  Wildungen to Philipp VII. It is either a key or a test message, so check which. Nr. 1290 f. 11, 27 Apr 1646, is an unidentified cipher (HCPortal "???").
- **Images**: HCPortal records 516 (media 1445/1446) and 515 (media 1443).
- **Prior art**: HCPortal "Not solved". If 2602 is a key, it may read 1290 and other Waldeck traffic, so pair them.
- **Score**: 2/3/3. Low length; worth it as a pair or cluster. **Not in repo**.

### 7. Polyalphabetic cipher message, 20 Feb 1824 (HStAM 9 a Nr. 259, f. 249)
- **Content**: one page described by HCPortal as "encrypted with a polyalphabetic cipher" (record 513, image 2928×4416, media 1439).
  Fonds 9 a is Hessian (Kurhessen) state papers. The rarity is a real-world 1820s polyalphabetic cipher, a Vigenère-family or Gronsfeld table.
- **Prior art**: HCPortal "Not solved"; nothing found.
- **Why hard/breakable**: a periodic polyalphabetic cipher of one page is routinely breakable (Kasiski/IoC) unless it is autokey or running-key. It is a good
  difficulty-graded target for the paper.
- **Score**: 2/4/3. **Not in repo**.

### 8. Letters to Jobst Hermann von Ilten "nicht dechiffriert", 1697-1706 (GWLB Hannover, Nachlass Ilten, Ms XXIII 1245)
- **Items** (Kalliope, search "Ilten dechiffriert"; GWLB catalogue flags each as not deciphered). The Hanoverian ministerial correspondence is in French or German:
  - Johann Ernst von Hattorf to Ilten, Hannover 7 Nov 1697, Ms XXIII, 1245:4, Bl. 212-213 (2 leaves).
  - Johann Wilhelm von Heusch to Ilten, Berlin 10 Oct 1705, Ms XXIII, 1245:7, Bl. 201-204 (4 leaves).
  - Hattorf to Ilten, Hannover 31 Jan 1706, Ms XXIII, 1245:7, Bl. 288-289.
  - Duke Georg Wilhelm of Brunswick-Lüneburg (Celle) to Ilten, 25 May 1706, Ms XXIII, 1245:7, Bl. 329-330.
  - Also, to Johann Georg von Ilten: anon. 26 Feb 1743 (Ms XXIII, 1234:29,2, pp. 73-75) and Ernst von Steinberg, London 29 Mar 1743 (pp. 119-121);
    the same Nachlass has "Sammlunge von Krieges Commissariat" volumes 1741-46 (1234:29,2 and 1234:31,1) with cipher.
- **Why interesting**: these are Hanover-Celle ministerial ciphers of the Succession years (Hanoverian succession, War of the Spanish Succession), outside
  DECODE and outside the British SP series. Several letters are probably in one Hanoverian system, and Ilten's own key may be elsewhere in the Nachlass.
- **Images**: **not confirmed online** (GWLB digitises selectively; ask or check the GWLB digital library). **Prior art**: none found.
- **Score**: 3/3/3 (if images can be had). **Not in repo**.

### 9. Staten-Generaal: "diverse briefjes in cijferschrift", Spanish invasion of the Veluwe, 1629 (Nationaal Archief 1.01.02 inv. 12579.26)
- **Content**: a packet of correspondence with the States-General deputies at Arnhem about the Spanish-Imperial invasion of the Veluwe (1629, the year of the siege of
  's-Hertogenbosch), containing "diverse briefjes in cijferschrift". No decipherment is mentioned (compare inv. 12561.142, "in cijferschrift ... met vertalingen").
- **Images**: Nationaal Archief scans exist for much of 1.01.02; confirm for 12579.26 (handle hdl.handle.net/10648/d2944105-cffb-9283-e053-6df0900aec3e).
- **Prior art**: none found. The Dutch 1620s field ciphers are small, so check DECODE for Dutch 1629 keys first.
- **Why hard/breakable**: several short notes, probably one field cipher in Dutch; short per note but combinable.
- **Score**: 3/3/3. **Not in repo**.

### 10. TNA intercepts flagged "undeciphered": marquis del Puerto 1748, Sweden "Letters not deciphered" 1748-55
- **SP 87/24/33** (ff. 96-97): "Undeciphered letter from the marquis del Puerto, Spanish ambassador to The Hague", 19 Mar 1748, an intercept during the
  Breda/Aix negotiations. It is probably a Spanish numerical nomenclator; Spanish 1740s keys are not in the repo.
- **SP 95/136** (1748-1755): "Supplementary: Letters not deciphered" (State Papers Foreign, Sweden), a whole volume. Establish whether these are
  Swedish intercepts or British despatches the office never deciphered; the former would be a large Swedish-code target.
- **Also**: SP 78/111/93 (f. 212), a French letter "entirely in cipher", 20/30 Sep 1642; SP 35/46/59 "Undecyphered paper", c. 1723 (Atterbury plot);
  SP 36/74/1/60 "Z Ball to [unknown]. In cipher", 19 Nov 1745 (Jacobite rising).
- **Images**: State Papers Online (Gale, subscription) or TNA copy order; **not free**. **Prior art**: TNA catalogue says undeciphered; nothing in print found.
- **Score**: del Puerto 3/3/4; SP 95/136 4/3/4 (pending inspection). **Not in repo** (grep del Puerto / 95/136: none).

### 11. "List zaszyfrowany", Szembek papers (PAN Biblioteka Kórnicka BK 1560)
- **Content**: an encrypted letter (Latin per catalogue) in a 150-leaf volume partly from the archive of Jan Szembek, Crown Chancellor (1700-1731).
  Polish Crown diplomacy of the Great Northern War era.
- **Images**: DjVu, free: https://www.wbc.poznan.pl/dlibra/publication/edition/343124/content (WBC, "dla wszystkich bez ograniczeń").
- **Prior art**: none found; length and system not yet checked (open the DjVu). Szembek's keys may survive in Kórnik or AGAD (Archiwum Koronne).
- **Score**: 3/3/3 provisional. **Not in repo**.

### 12. Hesse-Kassel / Denmark message with enciphered parts, 4 May 1672 (HStAM 4 f Dänemark Nr. 125, ff. 2-4)
- **Content**: a 3-page letter with encrypted passages (HCPortal 494, "Partially solved"; media 1385-1387). Hessian-Danish diplomacy before the Scanian War.
- **Prior art**: HCPortal partial solution only (details on the record); no publication found.
- **Why**: a partial solution means the system is identified, and completing the nomenclator is a workable "read in part → read" target.
- **Score**: 2/4/2. **Not in repo**.

## Checked and rejected (so they are not re-proposed)
- **Jung-Stilling cipher diaries 1799/1806/1813** (UB Basel NL 67 Nachtrag B:1-3, e-manuscripta DOIs 10.7891/e-manuscripta-25125, -23619, -26194):
  a fine word-divided symbol substitution of ~600 pp., but Schwinge's *Jung-Stilling Briefe* says each diary is in Nachlass Schwarz "mit Transkript",
  and Benrath 1975 printed the 1803 diary. A contemporary/family decipherment exists, so it is not a ciphertext-only target (usable as an easy benchmark only).
- **Tartu "Kaks lehekülge dešifreerimata teksti"** (Chr. D. Beck, hdl 10062/12944): illegible handwriting, not a cipher.
- **Jablonski→Ráday 1704-12** (SBB, Nachl. A. H. Francke 11,2/14-17): drafts with the Latin plaintext under the cipher.
- **Tattenbach 1644, Vienna** (Nüchterlein photos, Cipherbrain Oct 2018): system broken in the blog comments; the rest is keyed reading, and there are no public images.
- **Cornwallis Papers PRO 30/11 "undeciphered"** (1780-81): Saberton decoded the southern British ciphers (JAR 2019).
- **"Subtelty of Witches"** (BL): solved, HistoCrypt 2022. **Bucquoy 1619, Rabenhaupt 1640s, Heusner 1637, Chodkiewicz, Maximilian II 1575**: solved.
- **Hindoo Theology 1814** (HCPortal 21): a Masonic "cipher" (abbreviation) ritual whose plaintext is the published Essenes ritual; not a crypto target.
- **Charles Emmanuel I 1606 (fr. 3789 f.3)**: Tomokiyo, partially solved; fr. 3789 is already `breves1610`.
- **GLA Karlsruhe 52 Hennenhofer Nr. 49 "Chiffren"** (Franckenberg to Hennenhofer): appears to be a key sheet, not traffic.
- **HCPortal box BF388a** (Czech cryptograms 11 210 etc.): 20th-century exercise material.
