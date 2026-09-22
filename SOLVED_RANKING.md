# Solved targets, ranked

Compiled 2026-09-16 from the Solved and Read rows of [README.md](README.md) and [TARGETS.md](TARGETS.md).
Where the tracker ranks open targets by *feasibility*, this list ranks the finished ones by what they were
worth: how hard the cipher was, how much research it took, what the text says, whether anyone had read it
before, how prominent the item was on the source lists, and how solid the reading is.

All scores are judgments on a 1–5 scale, not measurements. The composite is a weighted mean and the weights
are stated; change them and the order changes. Entries marked * carry an inference that the notes do not
verify (see the last section).

## Axes and weights

| Axis | Weight | 1 | 5 |
|---|---|---|---|
| **D** Cryptanalytic difficulty | 25 % | Key or table already in print; decoding only | Ciphertext-only recovery of an unknown system from images, no crib |
| **H** Historical weight of the content | 25 % | Private or trivial matter | Decision of state, or content that changes a known account |
| **N** Novelty | 20 % | Plaintext already in print before this work | No reading anywhere before this work* |
| **R** Research and archival effort | 10 % | Transcription supplied; one source | Images fetched and transcribed, siblings hunted across volumes, catalogues corrected |
| **F** Profile on the source lists | 10 % | Not on any list | Schmeh Top 50 entry with a live public dispute |
| **V** Completeness and verification | 10 % | Partial reading, controls weak | Read end to end, controls or a printed clear text agree |

## Composite ranking

| # | Target | Date | D | H | N | R | F | V | Score | Why it sits here |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **Henry of Navarre → Ségur**, 500 Colbert 401 ff. 233, 239, 288v (+ f. 366, f. 333) | 1585–86 | 5 | 4 | 5 | 5 | 2 | 4 | **4.35** | The only target solved from the manuscript images with no transcription and no key family known in advance: 461 figures transcribed from Gallica, the syllabary found by the mod-5 test, a structured annealer at 97 % on a matched control, then the whole 440-canvas volume swept. Content is the German levy of 1585–86 and Casimir; the sender is corrected from Henry III to Navarre. Word-signs partly open |
| 2 | **Swatow telegram to Sun Yat-sen**, JACAR B03050738800 | 1916 | 4 | 4 | 5 | 3 | 2 | 4 | **3.90** | Code condenser over the Chinese telegraph code recovered by brute force over 57,600 keys with a character language model. Reports the Chaozhou rising and the fall of Swatow in the 1916 anti-Yuan campaign; 41 of 44 characters, the rest garbled by the operator |
| 3 | **Fra Giovanni di Lucca → Ferdinand III**, DECODE R2159 | 1644 | 4 | 4 | 5 | 2 | 2 | 4 | **3.80** | Polyphonic figure alphabet (17 = i/n, 19 = t/s) beaten ciphertext-only after Tomokiyo's crib proved self-contradictory. An offer to turn the Ottomans and Moldavia against Rákóczi and to supply 2,000 Cossacks, at the close of the Thirty Years' War. Three spellings and the speaker's name need the images |
| 4 | **Feuquières → Catinat**, Pignerol, 25 Jan 1691 (petit chiffre) | 1691 | 4 | 3 | 4 | 4 | 2 | 4 | **3.55** | Two-part code with no table in print, read by finding a second letter in the same code printed with its translation, and carrying alignment between them by hand (586/601 tokens). Fixes the plan for the Veillane surprise. Bazeries read it in 1893 but never published |
| 5 | **Maltravers → Ormonde** | 1634–35 | 3 | 3 | 5 | 4 | 2 | 4 | **3.50** | Block alphabet from 59 figures, then the nomenclator confirmed clause by clause against Wentworth's dispatches in Knowler 1739. The King's refusal of Kildare and the Crosby exchange for Ormonde's council seat. Two person-codes unidentified |
| 6 | **Louvois and Louis XIV → Catinat**, seven Grand Chiffre despatches | 1691 | 1 | 5 | 5 | 3 | 1 | 5 | **3.40** | No cryptanalysis: Bazeries' table applied to 12,362 groups from the MDZ hOCR. Ranks on content and volume alone: about 9,700 groups never in clear, including the King's 14 Sept decision to bring the army back over the Alps and abandon Piedmont. Controls 98–99 % against the two letters Bazeries printed |
| 7 | **Huang Xing → Lin Hu and Li Genyuan**, JACAR B03050731500 | 1916 | 3 | 3 | 5 | 3 | 1 | 4 | **3.30** | Kana-for-digit scheme identified and the telegram read from the frames. National Protection War correspondence; not on any list, a by-product of the Sun Yat-sen item |
| 8 | **Urquhart's Cyphral Octastich**, The Jewel 1652 | 1652 | 3 | 2 | 3 | 4 | 5 | 4 | **3.15** | A book cipher on the book itself, verified without the plaintext Vals AI published in Aug 2026: a new 285-number transcription from the 1983 photographs and 238/284 first-occurrence hits against 0.43 for controls. The highest-profile item solved (Schmeh Top 50 no. 28) but a royalist prayer, not news. Ten letters unread; the distich stays open |
| 9 | **Armstrong → Madison**, coded postscript | 1808 | 2 | 2 | 5 | 4 | 2 | 5 | **3.10** | Key rebuilt from pencil decodes on the NARA microfilm, found by scoring frames for faint pencil. 48 of 49 groups, the 49th a probable slip for *man*. The content is consular gossip. The separate 20 Feb 1808 letter is unsolved and the AFIO claim on it was rejected |
| 10 | **Warsaw, 24 Dec 1627**, DECODE R1408 | 1627 | 3 | 2 | 5 | 2 | 2 | 3 | **2.95** | Homophonic alphabet in plain order plus syllables, nulls and thirteen word codes, found by annealing from random starts. A promised canonry of Olmütz for a son of the Queen of Poland; addressee inferred. Word codes glossed from context only |
| 11 | **Richelieu → M. de Rancé**, BnF fr. 3829 ff. 87, 89 | 1629 | 4 | 3 | 1 | 2 | 2 | 5 | **2.85** | Clean ciphertext-only recovery of a homophonic alphabet and nomenclature, then found word for word in Avenel 1858. Cryptanalytically among the best pieces of work here; historically a verification of a 168-year-old reading the lists missed |
| 12 | **Charles I and Nicholas → Boswell**, TNA SP 84/157 | 1643 | 2 | 3 | 3 | 3 | 2 | 3 | **2.65** | Alphabet solved by R. Pitt (Sept 2026), verified here at z = 9.6. Added the four inline word-signs and the identification of the addressee as the Duke of Courland's envoy. A dozen word codes open |
| 13 | **Sir Richard Forster**, 13 May 1644 | 1644 | 3 | 2 | 1 | 2 | 2 | 4 | **2.25** | Found already read by Lasry, Biermann and Pitt. Value here is methodological: 31 of 34 symbols recovered blind from 207 tokens once word boundaries are used, six controls read |

Score = 0.25 D + 0.25 H + 0.20 N + 0.10 R + 0.10 F + 0.10 V.

### Provisional additions, 17 Sept 2026

Eight items read after the ranking above was compiled. Scored on the same axes and formula by the assistant
alone, not worked out in the appendix and not folded into the by-axis lists; Daniel is to check the scores
before the tables are merged. Where they would fall: Lanssac between Feuquières and Ormonde, Raince between Huang Xing and Urquhart,
the other four between Warsaw and Boswell, and Rennes 1563 (p42) beside Miranda/Sessa.

Not ranked: **Monsignor Giovanni Battista Pallotto (Vienna) → Barberini**, BAV Barb.lat. 6960, 1629 (catalogue 237). Its contents were
identified in Kiewning's 1897 edition and confirmed against the register. The key was found by others: it is the
Biermann–Bosbach key of Barb.lat. 6956 (2018, DECODE R215), which George Lasry matched to 6960. So there is no break
of this project's to score on these axes. See [SOLVED_CATALOGUE.md](SOLVED_CATALOGUE.md) §4 and
[pallotto1629/](pallotto1629/).

| # | Target | Date | D | H | N | R | F | V | Score | Why it sits here (provisional) |
|---|---|---|---|---|---|---|---|---|---|---|
| p1 | **Lanssac → Charles IX**, Warsaw, 26 Apr 1573, fr. 4735 f. 124, and ff. 160, 164, 174 | 1573 | 4 | 3 | 4 | 5 | 2 | 4 | **3.65** | Homophonic letter cipher with word signs, read from the Gallica images: key pinned from the glossed sibling f. 154v and the gutter-cut fragments, then confirmed by a pinned annealer against shuffled and blind controls; 96 of 100 signs; the same key reads three 1 and 9 May election letters. The Polish election bought by the Emperor and by France. Tomokiyo's table corrected |
| p2 | **Henri IV → Béthune**, Rome, 9, 10 and 22 Nov 1601, fr. 3484 nos. 7, 8, 12 | 1601 | 3 | 3 | 3 | 4 | 2 | 2 | **2.90** | 10 Nov read in full through its clear minute (f. 36), the key recovered by alignment and the 8 Nov and 10 Dec marginal decipherments; a Villeroy-office key of the design Bazeries printed for Béthune's brother. 9 Nov about six words in ten, 22 Nov open. Novelty limited because the minute already carried the 10 Nov text in clear |
| p3 | **Nevers → Pisany**, 8 Sept and 14 Oct 1593, fr. 3985 f. 209 and fr. 3986 f. 168 | 1593 | 2 | 3 | 4 | 4 | 2 | 2 | **2.85** | Tomokiyo's Nevers key no. 46 re-read at glyph level from fr. 3995 f. 87, checked against the office's decipherment of a Gondi letter, then applied: 8 Sept whole, 14 Oct in long stretches, both unread before. The five Revol letters are a separate key (no. 60) and stay open |
| p4 | **Philip II → Mendoza**, 7 Sept 1589, fr. 3641 ff. 10/14 and 12/76 | 1589 | 2 | 3 | 2 | 4 | 2 | 3 | **2.55** | Resolved rather than solved: f. 14 and f. 76 are the 1589 decipherer's fair copies of ff. 10 and 12, so the "second undeciphered letter" was never a cipher. Group-by-group alignment rebuilds part of Cg.13 (c. 70 syllables, c. 50 code groups), fills groups the decipherers left blank and corrects two readings. Fourteen groups open; needs Devos 1950 |
| p5 | **Jean du Bellay → Montmorency**, 16 June 1529, fr. 3078 no. 3 | 1529 | 2 | 3 | 3 | 3 | 2 | 2 | **2.55** | The residue of catalogue item 4, whose other letters proved to be in print (Le Grand 1688, Bourrilly 1905). Key re-derived on the leaf from the 22 June interlinear (B = o, the word signs *bien*, *fault*, *paix*), confirmed by reading the 17 Oct 1529 letter against Le Grand; about 60 % of the 16 June signs read in stretches. Divorce-negotiation news of 1529 |
| p7 | **BnF Espagnol 318** (BnF Espagnol 318 nos. 5, 92–95), nos. 92 and 95, the Catholic Monarchs' ciphered letters | 1497–1504 | 2 | 3 | 3 | 5 | 1 | 2 | **2.65** | Novelty lowered from 5 to 3 on 21 Sept 2026: cryptiana GL.htm says Lasry solved no. 95 itself in 2022 (alphabet published, no plaintext). Two keys found rather than broken: no. 92's is the *Cifra general* printed in 1994, proved against the glosses on its own leaf (eight hits, no misses) and transcribed; no. 95's is Lasry's 2022 alphabet, applied through segmentation and clustering to read about two thirds. High on novelty and research — five ciphered letters correctly mapped where the catalogue had four, one found already in print (Parisi 2020), and nos. 93–94 fingerprinted to the *Gran cifra* by the code-initial band of a one-part nomenclator. Low on difficulty and profile: nothing here was a cold break, and the volume is on no standard list. Held down on completeness — no. 92 is readable but not yet read out in full, and a third of no. 95 is beyond the scan |
| p6 | **Nicolas Raince → Montmorency**, Rome, 13 May and 20 Nov 1526, fr. 2984 pp. 29–31 and 105 | 1526 | 2 | 4 | 5 | 4 | 2 | 2 | **3.30** | The key was in print and useless, because reading which glyph sits under which letter in Tomokiyo's table image by eye slips a column: the first pass here had l, m and n each one place wrong. Re-measured off the image, the table resolves a control line glyph for glyph, and 86 of about 106 lines that exist in no edition were then read by hand off a microfilm. Low on difficulty (the system was published), high on novelty and content: the negotiation nine days before the League of Cognac, and the Medici pontificate as 'la totale ruine de sa maison' two months after the Colonna raid. Held down on completeness — 20 lines are machine-only and the read lines carry gaps |
| p7 | **Sormano and de Vaulx → François I**, Ferrara, Feb 1529, fr. 3096 nos. 63, 65, 66 | 1529 | 2 | 4 | 5 | 5 | 2 | 4 | **3.70** | Key in print (Lasry 2023) but never applied; the work was reading 18,000 signs from the scans by segmentation, clustering and a classifier with every line checked by eye, and finding the null and the nomenclator the table lacks. Two of three letters end to end, the third in stretches; the duplicate pair verifies the reading. Content: the duke of Ferrara refusing the crown of Naples and the French command before Cambrai, unread since 1529 |
| — | **Henri IV → Landgrave Maurice of Hesse-Kassel**, seven passages, 1602–09 | 1602–09 | 1 | 4 | 5 | 3 | 2 | 4 | **3.10** | Provisional. No cryptanalysis: Rommel's 1846 key applied to his 1840 figures, about 4,100 groups transcribed by eye. Never in clear before (Tomokiyo and the Lettres missives list them undeciphered). Content: the King's plan of a Protestant-German and Dutch front against the Spanish design on the Diet, 20 May 1606, and the two-million-livres subsidy, 22 Dec 1605 |

Arithmetic: p7 0.50 + 1.00 + 1.00 + 0.50 + 0.20 + 0.40; p6 0.50 + 1.00 + 1.00 + 0.40 + 0.20 + 0.20; p1 1.00 + 0.75 + 0.80 + 0.50 + 0.20 + 0.40; p2 0.75 + 0.75 + 0.60 + 0.40 + 0.20 + 0.20; p3 0.50 + 0.75 + 0.80 + 0.40 + 0.20 + 0.20;
p4 0.50 + 0.75 + 0.40 + 0.40 + 0.20 + 0.30; p5 0.50 + 0.75 + 0.60 + 0.30 + 0.20 + 0.20.

### Provisional additions, 18 Sept 2026

Ten more items, scored the same way and with the same caveat: the assistant's scores, for Daniel to check before merging.
Where they would fall: the Sun Yat-sen intercepts beside Lanssac, Toledo 1565 and Soglia 1848 beside Feuquières, Adams No. 88
just above Warsaw, Yard 1699 and Vich 1511–12 beside Béthune, Mary to Norfolk just above Adrian 1521, Adrian level with
Mendoza, and Erving 1807 below Forster. The Henrietta Maria letters of 1645–46 (p31, found already read by Lasry) sit just below Forster. Bay to Rákóczi 1706 (p96) sits beside Bizozola and Mantua 1590. D'Ewes's cipher log of 1635–36 (p97, 2.85) sits level with Bay: a private alphabet rebuilt by crib, a family record rather than state news. Kurz von Senftenau's Hamburg letters of 1639 (p33, key rebuilt, read in part) score 3.25. D'Affry's Hague letters of 1757–58 (p35, key rebuilt from Lyonet's decipherments) score 3.00. Kauderbach's Hague despatches of 1754–56 (p36, unseparated figures, key found by annealing onto a sibling key's vocabulary) score 3.55, level with Feuquières. Lope de Soria 1523 (p32) sits at the top of the provisional rows, just above Buda 1489. Bordeaux 1653 (p17, added later the same day) sits just below Huang Xing, Pelissier 1592 (p18, rescored after the calibrated re-reading) level with Louvois and Louis XIV, and Gramont 1529–37 (p19, rescored 2.90 on 21 Sept 2026: Lasry had decoded the texts at the time). Herbault 1626 (p20, contributed by Arya Sanketbhai Patel) sits just above Erving 1807; Conti 1649 (p21) beside Bordeaux 1653. Sadoleto 1482 (p26, added 19 Sept) sits just below Adams No. 88 and just above Warsaw. Ricasoli 1425 (p22) sits with Armstrong, just above Warsaw. Sessa 1524 (p23) sits among the lower partial reads, just above Herbault 1626. Charles VI to Windischgrätz 1720–22 (p24) sits beside Yard 1699, whose case it repeats: the key in the same papers, read straight off. The Acciaiuoli nunciature ciphers of 1758–60 (p34, 2.55) sit with Forster: a published key, but the first Italian text and code words for the attempt on José I. Barberini to Ceva 1632 (p37, 2.65) sits just above them: the key was already on the records and four of the eleven letters already read by Lasry, so the novelty is the two he left and the first six values of the dossier's nomenclator. Mondoucet 1572–73 (p95, 3.25) sits with Feuquières' neighbours: a key built by hand from the volume's crib, its 1573 passage then found in Didier's edition. The three KAA 4591 letters of 1531–37 (p100, 3.25) sit level with Mondoucet: two homophonic keys rebuilt from glosses, one letter still under the read bar.

| # | Target | Date | D | H | N | R | F | V | Score | Why it sits here (provisional) |
|---|---|---|---|---|---|---|---|---|---|---|
| p8 | **Sun Yat-sen's circle, intercepted telegrams**, JACAR B03050088300–B03050090200 | 1916–17 | 3 | 4 | 5 | 5 | 1 | 3 | **3.65** | The Swatow family applied across the Ministry of Communications' copies: keys found by search over a family already known, so 3 not 4, but each accepted on a telegram it was not fitted to, and rhyme-day dates check. About sixty telegrams from six files transcribed by hand from the forms. Content: the end of Yuan's monarchy seen from Sun's side, Chen Qimei's murder, and the Foreign Ministry's own advice relayed on a wire it could not read. On no list. Held down on completeness: most long telegrams keep [?] groups, two keys are tentative, and 文密 is open |
| p9 | **García de Toledo → Philip II**, Messina, 16 July 1565, AGS Estado leg. 1394 no. 247 (duplicado) | 1565 | 3 | 4 | 5 | 3 | 1 | 4 | **3.55** | No key in print and no decipherment on the leaf or in PARES, but an easy system once seen: two clear-text cribs (*seiscientos soldados*, *en tiera*) and the alphabetical order of the figures 12–43 gave the whole table, confirmed on predicted letters and on *Mosiur de Lenni*, a name not in the clear text. High on content: the viceroy's own account of the Piccolo Soccorso and of a second relief run waved off by La Valette's signals, plus the Sicilian finances. On no list (own PARES sweep). Held down on verification: the checks are internal; the original despatch has not been found |
| p10 | **J. Q. Adams → Secretary of State**, St Petersburg, No. 88, 25 June 1812, M35 reel 3 | 1812 | 2 | 3 | 5 | 4 | 2 | 2 | **3.05** | Code rebuilt from the clerk's interlinear decodes, not broken cold, after refuting the editorial premise that it was Armstrong's THE = 972. The nine lines Ford printed as not decyphered read, 124 of 134 groups with 27 by slot inference. Content: the Chancellor's strokes at Wilna on the eve of 1812, dated earlier than the standard accounts. Held down on completeness: one passage, ten groups unread, the rest of the despatch in threads |
| p11 | **Robert Yard → the Earl of Manchester**, Whitehall, 12 and 16 Oct 1699, Beinecke OSB MSS fc37 box 2/49, 2/51 | 1699 | 1 | 3 | 4 | 4 | 2 | 5 | **2.90** | No cryptanalysis: the key was a printed code sheet in the same Manchester papers at Yale, transcribed (1,456 slots) and validated on the 5 Oct sibling's contemporary decipherment. Both letters read end to end, 368 groups, five slips marked. Novelty held to 4 because Tomokiyo had named the code and decoded the first groups, and Cole's *Memoirs* (1733) was not re-checked. Content: intelligence traffic, the Dover watch for Mills and Lord Drummond's priest and reports of a design at Saint-Germain; no decision of state |
| p12 | **Adrian of Utrecht, the Admiral and the Constable → Charles V**, Vitoria, 30 Dec 1521, AGS Estado leg. 8 no. 150 | 1521 | 2 | 3 | 2 | 4 | 1 | 4 | **2.55** | Found in print (Pérez Gredilla's decipherment in Danvila, MHE 38, 1899), then used as a crib: ciphertext transcribed from PARES and aligned on `xif` = V. M., the nomenclator rebuilt with its alphabet-block code initials. Corrects the dead king from England to Manuel I of Portugal and reads or corrects about 17 of c. 25 unread groups. Low on difficulty and novelty (plaintext in print), on no list; held on completeness by about ten open groups and a rough sign alphabet at PARES resolution |
| p13 | **G. W. Erving → Madison**, Madrid, 24 Mar 1807, Pinckney's code | 1807 | 1 | 2 | 2 | 4 | 1 | 5 | **2.15** | Holes in a decode already in print closed from the two received copies and Pinckney's decoded despatches; the only loss is Erving's own. Low on difficulty (Madison had the key), novelty (the editors had suggested two of the corrections) and profile (on no list); high on verification and research (three microfilm and LoC sources collated) |
| p14 | **Ferdinand the Catholic → Jerónimo de Vich**, AHN Estado 8715 N.45, N.57, N.60, Apr 1511 – Sept 1512 | 1511–12 | 2 | 4 | 3 | 4 | 1 | 3 | **2.90** | Key rebuilt from two deciphered siblings, not broken cold, then read three letters it was not built from; about 22,500 signs and groups transcribed from PARES. High on content: Ferdinand's own account of how his army was pushed into Ravenna, the Sforza restoration and the call for spiritual war on Louis XII. Novelty held to 3 because Terrateig 1963 (not seen) prints Ferdinand's letters from this legajo and may include these. On no list. Held down on verification and completeness: the checks are internal, some groups unread, and the siblings N.41 and 8714 were not used |
| p15 | **Mary Queen of Scots → the Duke of Norfolk**, "the 20th" [Feb or Mar 1570], Cotton MS Caligula C II f. 74r | 1570 | 2 | 3 | 3 | 3 | 2 | 3 | **2.65** | Key in print (Tomokiyo, rebuilt from the deciphered siblings) and checked on f. 66r; no cryptanalysis beyond reading signs. Novelty is limited: Tomokiyo's overlay already had most of the letters, and what is new is the continuous reading, the gap fills, the names and the date. Content: the Norfolk marriage intrigue after Moray's murder, with Elizabeth blaming Mary for it. Five unkeyed signs and a few words open |
| p16 | **Cardinal Soglia → the nuncio Viale Prelà**, Rome 15 June 1848 (*L'Italia del Popolo*, 30 June 1848) | 1848 | 4 | 3 | 5 | 3 | 2 | 3 | **3.55** | Ciphertext-only recovery of a system nobody had described for this text: word separator, 64-cell table with syllables, alphabetical 8XXX code, and a synthetic control behind the negative. Never read before, and the paper offered a prize for it in 1848. Content: a papal counter-order to the nuncio that came a day late. Transcription supplied, one digit restored. On no list, only a Cipherbrain post. Ten code words read from context and checked by rank, eleven open |
| p17 | **Bordeaux → Brienne**, London, 30 May 1653, BL Add MS 4200 f. 88 | 1653 | 2 | 3 | 5 | 4 | 2 | 4 | **3.25** | Read with the Deciphering Branch's own key sheet (DECODE R7537), so 2 not higher, although the design had been identified and a solver built for it beforehand. Never read before: the English worksheets stop at frequency counts. Research: the DECODE key found, the transcription re-checked on the images and 21 faults fixed, the duplicates collated. Content: the envoy's precedence complaint after the Bordeaux deputies' reception and the advice to hold back French mediation, during the Fronde's last months. On Tomokiyo's list only. Held on completeness by six nomenclature codes and a dozen rare tokens |
| p18 | **A. Pelissier → Pierre Jeannin**, Burgos, 13 Sept 1592, BnF fr. 3982 no. 22 | 1592 | 2 | 4 | 4 | 5 | 2 | 4 | **3.40** | Read in part (93% of words); V kept at 4 for the calibration and glosses. Key in print (Tomokiyo, from Pelissier's later letters) and confirmed by the decipherer's glosses, so 2; the work was ~18,400 signs transcribed from the Gallica scans and beam-decoded. Never read before and weighty: Spanish policy toward the League and the Estates in the autumn of 1592, the two-army plan and its cost, the case for Navarre as argued in France. Research 5: the key calibrated on 1,764 signs of the sibling letters aligned with their decipherment. Completeness 4: 94% of the ciphered words read, 256 gaps marked |
| p19 | **Gramont, Mâcon and Langeac → Montmorency**, Venice and Rome, 1529–37, fr. 3083 no. 8, fr. 3091 no. 23, fr. 3071 nos. 4, 7 | 1529–37 | 2 | 4 | 2 | 4 | 2 | 4 | **2.90** | Keys in print (Lasry 2023), so 2. Lasry decoded all four texts at the time; Tomokiyo did not post the decipherments, so novelty is 2, not 5 (corrected 21 Sept 2026 on Lasry's note); the work was reading ~9,000 signs from the scans, six unlisted code signs, and dating. Content is the French line to Clement VII before Bologna (council, Florence, the Admiral's mission) and Paul III's Farnese marriage threat of 1537. Verification: a contemporary decipherment slip for the Mâcon f. 9v passage |
| p20 | **Phelipeaux d'Herbault → Philippe de Béthune**, Paris, 13 Feb 1626, BnF fr. 3669 no. 25 | 1626 | 1 | 3 | 2 | 3 | 1 | 4 | **2.20** | Resolved rather than solved, like Mendoza: the catalogue's one undeciphered letter is a copy of no. 26, which carries the 1626 decipherer's interlinear plaintext, so 1 on difficulty and 2 on novelty (read in 1626, never printed). The ciphered passages matter (the Valtelline, the reason for the Huguenot peace, Savoy pressing France towards war with Spain six weeks before Monzón); identity checked on the clear text, the run boundaries and matching groups. Only on the BnF harvest list. |
| p21 | **Prince de Conti → Laigue and Noirmoutier**, Paris, March 1649, BnF fr. 3854 nos. 41–43 | 1649 | 2 | 4 | 4 | 4 | 1 | 4 | **3.20** | Nos. 41–42 already read (Lasry 2023), so their share adds only corrections. No. 43's key was rebuilt from the clerk's glosses, not broken cold, hence D 2; but its opening had never been read and the body, though glossed in 1649, is unpublished. Content: the Frondeurs' secret line to the Archduke during Rueil, the conference as a stalling device and the promise to break it when Spain enters France. Not on any list (catalogue only). Four blotted places open |
| p22 | **Galeotto Fibindacci da Ricasoli → the Signoria of Florence**, Urbino, early 1425, ASF Dieci di Balìa, Responsive 2 no. 171 | 1425 | 3 | 3 | 4 | 4 | 1 | 3 | **3.10** | The oldest letter read in this repository. Gabbrielli's 1863 key and glosses did a third of the work; the three long runs he left unread were aligned sign by sign and his null list corrected. Never printed, so the text is new, though the key has been in print since 1902. Two word signs from context and five letter values on this letter only keep V at 3 |
| p23 | **Duke of Sessa (Luis Fernández de Córdoba) → Charles V**, Rome, 18 Apr 1524, RAH Salazar A-31 ff. 128–131 | 1524 | 2 | 2 | 4 | 5 | 1 | 3 | **2.70** | Key rebuilt from the court's decipherments of sibling letters, so 2. Routine embassy news, though never read: Bergenroth skipped the letter. Research 5: a century typo corrected, eight siblings aligned across three volumes, template matching over ~110 pages. Completeness 3: word-level reading, four groups open |
| p24 | **Charles VI → Count Windischgrätz**, Vienna, 1720–22, SOA Plzeň RA Windischgrätz (DECODE R5019–R5024) | 1720–22 | 1 | 4 | 4 | 4 | 1 | 4 | **2.95** | Both keys on DECODE beside the letters, so 1: the work was transcribing a 977-entry nomenclator and a sign key and reading 35 passages. Content weighs: the Emperor's own secret line on the peace after Alberoni's fall (France and Philip V, Sardinia, Montferrat, Portugal) and the first Spanish marriage feelers for his children. Novelty 4 because Mírka 2012 described the letters and keys without a plaintext. V 4: every passage reads, two cells uncertain |
| p25 | **Maffeo da Treviglio → Ludovico Sforza**, Buda, 22 Nov 1489 and 12 Jan 1490, ASMi Sforzesco 650 and 642/1, 4 | 1489–90 | 3 | 4 | 5 | 5 | 1 | 4 | **3.70** | The oldest text read in this repository, and the oldest previously unread ciphertext read here by any route. D 3: the key existed in print but only as numbers with no sign images, so it had to be re-anchored to the shapes through a cipher-and-clear pair, and about twenty signs were then recovered from the letters themselves. N 5: of the 1489 letter only its first two lines had ever been deciphered, and the 1490 letter not at all. H 4: Matthias Corvinus's peace with Frederick III and the Diet, the two rival marriages for John Corvinus, the queen's opposition, and a warning that intercepted cipher letters had been read. R 5: three archives' catalogues reconciled, three sibling records shown to be already deciphered and set aside. V 4: pp. 1–2 of 1489 read nearly throughout, p. 3 in patches |
| p26 | **Nicolò Sadoleto → Ercole I d'Este**, Pozsony, 16 July 1482, ASMo Ambasciatori Ungheria b. 1/9 no. 8 (DECODE R1102) | 1482 | 2 | 4 | 4 | 3 | 1 | 3 | **3.00** | Alphabet rebuilt from two sibling letters with contemporary clear copies, so D 2. The seven lines had no decipherment and carry real news: the Venetian counter-offer to Matthias at the start of the War of Ferrara (Veglia, a fleet command for János Corvin, 100,000 a year), the same sum Sadoleto later quotes as Matthias's price. Read in gist only, with a nomenclator group and a dozen signs open, so R 3; two of the four catalogue items were read at the time |
| p27 | **Marqués del Carpio (Rome) → Baltasar de Fuenmayor**, 1677, AGR Brussels SEG 2559 (DECODE R1002–R1011) | 1677 | 2 | 3 | 3 | 3 | 1 | 4 | **2.55** | The key was rebuilt from the cipher, but eight letters had marginal decipherments to align against, so D is 2. Two letters were catalogued as unread, though each proved to carry a faint margin, and no key had been published, so N is 3. Content: the Spanish ambassador's quarrel with Innocent XI, and the 1677 campaign seen from Rome (Messina, Charleroi, Freiburg, d'Estrées at Turin). V 4: the whole file reads, with three code words conjectural |
| p28 | **Unknown writer → "Monsieur"**, 17th c., TNA SP 106/10 ff. 241–243 (DECODE R927) | 17th c. | 4 | 4 | 1 | 2 | 1 | 3 | **2.80** | D 4: no key, no crib, no clear sibling; the pencil key on the flap was a false lead, and the homophonic system was recovered from a hand transcription by quadgram annealing. N 4: catalogued as undeciphered. H 1: a private client-to-patron letter, unnamed. R 2: writer and date unknown. V 3: last page nearly throughout, first page in fragments |
| p29 | **Cardinal Gian Francesco Morosini → Cardinal Montalto**, Blois–Moulins, 1588–89, AAV Segr. Stato Francia 22 (DECODE R18–R58) | 1588–89 | 1 | 5 | 4 | 3 | 1 | 4 | **3.10** | D 1: Meister printed the key in 1906; the only obstacle was cutting unseparated 1–3 digit homophones, done by a language-model beam search. H 5: the papal legate's own account of Blois, the Guise murders and the League's crisis. N 4: DECODE lists the file as partially decrypted and no plaintext or edition exists. R 3: 36 records sorted out of a mixed run, two keys. V 4: 34 of 36 read end to end, letter slips and a few dotted codes open |
| p30 | **Marqués de los Balbases (Nijmegen) → Baltasar de Fuenmayor**, 1677–78, AGR Brussels SEG 2559 (DECODE R985–R998) | 1677–78 | 3 | 3 | 4 | 3 | 1 | 3 | **3.00** | D 3: no key survives and none of the series keys fits; the table was recovered by anchoring and EM alignment against ten margin decipherments. N 4: four letters had never been deciphered. H 3: Spain's Nijmegen plenipotentiary on the northern war, Bremen, the Brunswick rank quarrel and the fall of Ghent. V 3: 97% of groups keyed, name codes and a few homophones open |
| p31 | **Henrietta Maria's household (St Germain, Paris) → Charles I**, 1645–46, TNA SP 106/10 ff. 213–247 (DECODE R785–R929) | 1645–46 | 1 | 4 | 1 | 2 | 2 | 3 | **2.15** | D 1: Lasry's keys applied, no cryptanalysis. H 4: the queen's circle on French, Lorraine and papal help in the last year of the first Civil War. N 1: read by Lasry on DECODE in 2020. F 2: on Tomokiyo's unsolved list. V 3: key checked on one letter; name codes open |
| p32 | **Lope de Soria → Charles V and Gattinara**, Genoa, June–Aug 1523, RAH Salazar A-28 (DECODE R9488–R9498) | 1523 | 4 | 4 | 5 | 4 | 1 | 3 | **3.80** | D 4: key A had no key, crib or sibling and was broken ciphertext-only by a substitution solver on a Castilian 4-gram model; key B came from a court decipherment. H 4: the Venetian league, a plan to seize Bergamo and Brescia, Siena, Andrea Doria's first approach to the Emperor. V 3: several code groups open, key-B passages graded C/M. |
| p33 | **Ferdinand Sigmund Kurz von Senftenau (Hamburg) → Trauttmansdorff**, Jan–Apr 1639, SOA Plzeň RA Trauttmansdorff inv. 200 (DECODE R3811–R4736) | 1639 | 3 | 4 | 4 | 4 | 1 | 2 | **3.25** | D 3: a contemporary gloss on one page; the syllable table was deduced from it and the rest solved with a structured annealer. H 4: the imperial vice-chancellor at the Hamburg peace preliminaries. N 4: Mírka read one letter (2012, unprinted); eight never read. R 4: 73 images transcribed, DECODE's 1638 date corrected. V 2: key complete, single-pass transcription leaves 20–45% garbled |
| p34 | **Filippo Acciaiuoli (Lisbon) → Secretariat of State**, 1758–60, AAV Segr. Stato Portogallo 117 (DECODE R25, R195–R201) | 1758–60 | 1 | 4 | 3 | 3 | 1 | 3 | **2.55** | D 1: Lasry's key and letter stream were on the records; the work was word division and fixing codes from three contemporary decipherments. H 4: the nuncio's secret account of the attempt on José I and of Carvalho's power. N 3: no Italian text or code identifications existed. R 3: eight records, 107 code words. V 3: all eight read, ~80 rare codes open |
| p35 | **Comte d'Affry (French ambassador, The Hague) → Rouillé and Bernis**, 1757–58, KHA Prins Willem V inv. 192 (DECODE R1054–R1076, R2067) | 1757–58 | 3 | 3 | 3 | 5 | 1 | 3 | **3.00** | Read in part (86% of groups; R1071 unread), V 3. D 3: no key; rebuilt by aligning Lyonet's decipherments, which DECODE said were not imaged. H 3: a year of French policy at The Hague (augmentation, convoys, Ostend, spies, a London loan), known in summary from Fruin's extracts. R 5: images, eight clear copies transcribed, DECODE digits corrected, one letter transcribed from scratch.
| p36 | **Johann Heinrich Kauderbach (Saxon-Polish resident, The Hague) → Dresden**, 1754–56, KHA Prins Willem V inv. 201 (DECODE R1043–R2082, ten records) | 1754–56 | 4 | 3 | 5 | 4 | 1 | 3 | **3.55** | D 4: unseparated figures, the Hague cabinet never broke them; nulls found by phase statistics, a homophonic attack failed, the key found by annealing a one-to-one assignment onto the vocabulary of a sibling key of 1761 whose numbers differ. H 3: the Dutch augmentation quarrel, the Saxon subsidy treaty and the Treaty of Versailles seen from a Saxon desk. N 5: never read. R 4: seven letters transcribed from the images. |
| p37 | **Cardinal Francesco Barberini (Rome) → Nuncio Ceva (Paris)**, two letters, AAV Segr. Stato Francia doss. 346 nos. 2 and 11 (DECODE R75, R84) | 1632 | 2 | 3 | 4 | 2 | 1 | 3 | **2.65** | D 2: Lasry's key was attached to the records, but it is unusable as it stands — the figures run on, and his own note misdescribes the nomenclator as four digits with prefix 4 when it is three; the work was the segmentation, done by beam search under a model built partly from the dossier. H 3: the papal reading of Lützen, a month on, and the fear of a France held disunited. N 4: never read in modern times, though R75 was deciphered on the leaf in 1632. R 2: DECODE's transcriptions, one source, images not re-checked. V 3: controlled at 77.5% against the contemporary interlinear; 117 nomenclator elements open. |
| p38 | **Lope Hurtado de Mendoza (Rome) → Charles V**, nine letters, RAH Salazar 9/26 (DECODE R9634, R9644–R9646, R9648–R9650, R9652, R9656) | 1522 | 4 | 4 | 5 | 3 | 5 | 3 | **3.95** | An unpublished cipher, not previously distinguished from Sánchez's among whose letters it is bound. D 4: the crib was bound with it, but had to be recognised as such and the key built from scratch — no published key exists for this correspondent. N 5: nothing of Hurtado's had been read; DECODE calls seven of the nine non-decrypted. H 3: Adrian VI temporising between Charles V and Francis I in the weeks before the French re-entry into Italy, with Adorno's intercepted letters and the Rhodes news. R 5: three ciphers of one chancery separated, two clear versions and a duplicate identified, and DECODE's status for R9652 corrected. V 3: four letters read complete as to content, the ciphered leaves in part, the five uncribbed records in substance only |
| p39 | **A Jacobean codebreaker's file of Italian intercepts**, TNA SP 106/10 ff. 128–195, 202–205 (DECODE R657, R660, R664, R704, R720–R722, key R725) | c. 1623–24 | 2 | 3 | 4 | 5 | 4 | 2 | **3.25** | D 2: no cryptanalysis was needed — the contemporary codebreaker had done it, and the work was to find the sheet he wrote it on and to read his hand. H 3: the Spanish Match and the Palatinate seen from inside the English government's postal attack, but no single despatch yet read through. N 4: nothing of SP 106/10 has a modern edition; the published SP 106 transcriptions stop at volume 4. R 5: seven catalogue records joined into one case, a sixty-seven-year date span narrowed to two years, three ciphers separated where the catalogue has one, one worksheet re-filed, and the key transcribed. V 2: the system is fully described and the first cipher's key complete, but only fragments of the letters are read |
| p40 | **Henri IV → Maisse**, BnF fr. 16093 ff. 370, 373, 406, 410 | 1592–93 | 2 | 4 | 5 | 4 | 3 | 5 | **3.85** | A published key that nobody had applied, recovered from image files a text dump hides, then checked letter-for-letter against a clear copy found by a separate route; low on difficulty, high on novelty and verification |
| p41 | **Conde de Miranda, duque de Sessa, Diego de Ibarra**, BnF fr. 3983 nos. 45, 79; fr. 3984 nos. 47, 68 | 1593 | 3 | 4 | 5 | 4 | 3 | 4 | **3.75** | The office's own key, with the nomenclature no published table has, recovered by following the catalogue's own DECODE step into a volume this repository already uses; high on novelty, held back because the letters are not yet transcribed |
| p42 | **Catherine de Médicis and the Court → the bishop of Rennes**, BnF fr. 3181 f. 55; Colbert 390 pp. 139, 357; Colbert 392 p. 231 | 1562–64 | 3 | 4 | 5 | 4 | 4 | 4 | **4.05** | Four letters never read: f. 55 printed by La Ferrière as an empty bracket, the other three listed undeciphered by Tomokiyo. Difficulty 3: the key was published but had to be fitted to four secretaries’ hands, each calibrated on glossed letters in the same hand. Novelty 5. Weight 4: Trent, the Habsburg marriage and its leak to Spain, the 1564 precedence quarrel. Fullness 4: ~87% of the signs, from 65% (the faint burn-after-reading note) to 99% |

Arithmetic: p8 0.75 + 1.00 + 1.00 + 0.50 + 0.10 + 0.30; p9 0.75 + 1.00 + 1.00 + 0.30 + 0.10 + 0.40; p10 0.50 + 0.75 + 1.00 + 0.40 + 0.20 + 0.20;
p11 0.25 + 0.75 + 0.80 + 0.40 + 0.20 + 0.50; p12 0.50 + 0.75 + 0.40 + 0.40 + 0.10 + 0.40; p13 0.25 + 0.50 + 0.40 + 0.40 + 0.10 + 0.50;
p14 0.50 + 1.00 + 0.60 + 0.40 + 0.10 + 0.30; p15 0.50 + 0.75 + 0.60 + 0.30 + 0.20 + 0.30; p16 1.00 + 0.75 + 1.00 + 0.30 + 0.20 + 0.30;
p17 0.50 + 0.75 + 1.00 + 0.40 + 0.20 + 0.40;
p18 0.50 + 1.00 + 0.80 + 0.50 + 0.20 + 0.40;
p19 0.50 + 1.00 + 0.40 + 0.40 + 0.20 + 0.40;
p20 0.25 + 0.75 + 0.40 + 0.30 + 0.10 + 0.40;
p21 0.50 + 1.00 + 0.80 + 0.40 + 0.10 + 0.40;
p26 0.50 + 1.00 + 0.80 + 0.30 + 0.10 + 0.30;
p22 0.75 + 0.75 + 0.80 + 0.40 + 0.10 + 0.30; p23 0.50 + 0.50 + 0.80 + 0.50 + 0.10 + 0.30;
p24 0.25 + 1.00 + 0.80 + 0.40 + 0.10 + 0.40;
p27 0.50 + 0.75 + 0.60 + 0.30 + 0.10 + 0.40;
p28 1.00 + 1.00 + 0.20 + 0.20 + 0.10 + 0.30;
p29 0.25 + 1.25 + 0.80 + 0.30 + 0.10 + 0.40;
p30 0.75 + 0.75 + 0.80 + 0.30 + 0.10 + 0.30;
p31 0.25 + 1.00 + 0.20 + 0.20 + 0.20 + 0.30;
p32 1.00 + 1.00 + 1.00 + 0.40 + 0.10 + 0.30;
p33 0.75 + 1.00 + 0.80 + 0.40 + 0.10 + 0.20;
p34 0.25 + 1.00 + 0.60 + 0.30 + 0.10 + 0.30;
p35 0.75 + 0.75 + 0.60 + 0.50 + 0.10 + 0.30;
p36 1.00 + 0.75 + 1.00 + 0.40 + 0.10 + 0.30.

### Provisional additions, 20 September 2026: Egmond and Groffey

Charles of Egmond (p43, rescored 2.95 on 21 Sept 2026) is an independent re-solution: Lasry had solved the cipher in 2023.
Groffey to Rákóczi (p44, 3.05) sits alongside Adams no. 88: a preserved key, but a new diplomatic reading and a catalogue reversal. Van Reede 1787 (p46, 2.85) sits just below it: an archive key again, with the transcription as the obstacle. De Swart 1782 (p45, 3.05) is the same kind of result: an archive key for a letter DECODE said had none. Alessandrino 1568 (p47, 2.90) sits between them: the key was already reconstructed and published, but decoding under a polyphonic key (two letters per digit) is itself ambiguous and difficult. The Ralph Boswell newsletter of 1627 (p49, 1.65, found already read by Mark Woodard) ranks lowest: a published key, with only the sender and date added. Lebel's three letters to Savoy of 1593 (p90, 3.10) sit with Hesse 1602–09: a published key, but letters nobody had read, on the crown at the Estates of the League. Bizozola's letter to Maximilian Sforza (p93, 2.60) sits below them: Lasry's published key applied to a letter nobody had read, dated here from its content. Mantua to Nevers 1590 (p94, 2.45) is the same kind: an archive key from the recipient's own papers, read unchanged, with the unseparated figures as the obstacle.

| # | Target | Date | D | H | N | R | F | V | Score | Why it sits here (provisional) |
|---|---|---|---|---|---|---|---|---|---|---|
| p43 | **Charles of Egmond → grand master of France**, BnF fr. 3015 no. 8 | 18 July (?), year unknown | 4 | 3 | 2 | 3 | 2 | 3 | **2.95** | Ciphertext-only graphic substitution with nulls, recovered from images after failed short probes. Full letter and address read with minor doubts. A request for support in war, without campaign year or personal names. Novelty 2: Lasry had already solved the cipher in 2023 (key on cryptiana GL.htm §2, no plaintext published; pointed out by Lasry, 21 Sept 2026), so this is an independent re-solution. Verification is internal. |
| p44 | **Philippe Groffey (?) → Ferenc Rákóczi II**, MNL OL G15 Caps. C. Fasc. 39 pp. 277–279 (DECODE R902) | 15 Oct 1707 | 1 | 4 | 5 | 4 | 1 | 3 | **3.05** | Preserved same-series key, independently controlled on two interlinear letters. New reading in substance and a reversal of the catalogue's direction; exact prose awaits fresh transcription and the unsigned writer remains a high-probability attribution. |
| p45 | **Johan Isaac de Swart (St Petersburg) → Pieter van Bleiswijk**, NA 3.01.25 inv. 610 (DECODE R1036) | 8 Mar 1782 | 2 | 3 | 5 | 4 | 1 | 3 | **3.05** | Archive key found for a letter DECODE called unidentified. Digit marks kept as separate groups; 34 values filled from context. 96.7% read, and the 1787 sibling read in part |
| p46 | **Arend Willem van Reede (Berlin) → Van de Spiegel**, NA 3.01.26 inv. 190 (DECODE R1026, R1027) | 29 Dec 1787, 4 Mar 1788 | 2 | 3 | 4 | 3 | 2 | 3 | **2.85** | Archive key (the 1782 Grand Chiffre, R1024) confirmed on a known-plaintext control; the work was the transcription, where one catch-all sign hid different digits and was resolved by a language model. New reading of the 1788 alliance negotiation; held down by the garbled stretches and the unread 1793 letter |
| p47 | **Cardinal Alessandrino → the nuncio in Spain**, AAV Segr. Stato Spagna 6/I and 6/II (DECODE R93–R102, R115) | 1568–69 | 3 | 3 | 3 | 4 | 1 | 3 | **2.90** | Published reconstructed key (Lasry 2020) with no plaintext; the work was choosing each digit's letter under a language model. Difficulty raised to 3 (21 Sept 2026): a polyphonic key is always ambiguous and hard to apply, and Lasry rates this above the cases with no key recovery or a purely external key search. Eleven papal letters of 1568–69 read for the first time online; held down because the key was already known and Serrano 1914 may print some in clear |
| p80 | **Cardinal Alessandrino → the nuncio in Spain**, AAV Segr. Stato Spagna 1 (DECODE R85–R90) | 1567 | 3 | 3 | 3 | 4 | 1 | 3 | **2.90** | The 1568 key and decoder applied unchanged; the new step was identifying the 'unknown sender' from the archive's volume description. Scored as its sibling p47. |
| p48 | **Conde de Hernán Núñez (Stockholm) → Baltasar de Fuenmayor**, AGR Brussels SEG 2559 (DECODE R1012–R1015) | Dec 1674 | 1 | 3 | 2 | 3 | 1 | 4 | **2.20** | Margins on every passage and a sibling key already rebuilt here (Balbases 1677), so D 1 and N 2; the work was recognising the key and checking the margins against it. Sweden on the eve of the Scanian War, verified group by group |
| p49 | **Sir Ralph Boswell → William Boswell**, TNA SP 106/5 ff. 20–21 (DECODE R413, catalogued as Charles I to Boswell) | 15 Dec 1627 | 1 | 2 | 2 | 1 | 1 | 3 | **1.65** | D 1: Woodard's 2021 monoalphabetic key applied. H 2: court news on Buckingham before the 1628 Parliament. N 2: read by Woodard; sender, date and two signs added here. F 1: a DECODE record only. V 3: key consistent on all 442 signs; one pair unread |
| p50 | **Bernardo de Salinas (London) and Pedro Ronquillo (Nijmegen) → Baltasar de Fuenmayor**, AGR Brussels SEG 2559 (DECODE R966–R984, R1001) | 1676–78 | 1 | 3 | 3 | 3 | 1 | 3 | **2.30** | A sibling key applied unchanged (D 1); the work was re-segmenting DECODE's transcriptions. Four letters with no margin, two catalogued as non-decrypted, read only in gist (read in part, 88%), so N 3, V 3 |
| p51 | **Antonio Sauli and Cardinal Riario (Portugal) → the papal Secretariat**, ASV Segr. Stato Portogallo 8 (DECODE R190–R194) | 1579–81 | 1 | 3 | 2 | 3 | 1 | 4 | **2.20** | Contemporary decipherments over nearly every passage and a published key (Lasry 2020), so D 1 and N 2; the work was transcribing R192–R194 and checking them against the glosses, which added five code words. Riario's legation on the Piedmont plot and the papal troops for Ireland |
| p52 | **János Pápai → Ferenc Rákóczi II**, MNL OL G15 (DECODE R731–R823) | 1706–10 | 1 | 3 | 4 | 3 | 1 | 4 | **2.60** | D 1: the envoy's own key, found among DECODE's key records and applied unchanged. N 4: eleven letters DECODE listed as undeciphered or partly deciphered, now read. H 3: Rákóczi's diplomacy at the Porte. V 4: 98.5% of groups keyed, continuous Hungarian and Latin. R731 (graphic signs) open. |
| p53 | **Archbishop of Bremen → Salvius**, Riksarkivet group (DECODE R4330–R4331) | 1631 | 2 | 2 | 3 | 3 | 1 | 3 | **2.30** | D 2: key rebuilt from the clerk's glosses, the grid order predicting the unglossed letters. N 3: DECODE listed them as partially decrypted; the unglossed fifth is new. H 3: Bremen's appeal to Sweden in the winter after Breitenfeld. V 3: every group reads; transcription slips remain. |
| p54 | **Charles Hémard de Denonville, cardinal de Mâcon (Rome, Orvieto) → Anne de Montmorency**, BnF fr. 3053, eight records (DECODE R4233–R4248) | 1536–37 | 1 | 4 | 3 | 3 | 1 | 3 | **2.50** | D 1: a published key (Tomokiyo/Lasry) applied, with corrections from a glossed line. H 4: the general council and the Germans, Doria's galleys, Milan refused to the Farnese, an estate in France for the Pope's son, in the year of the Emperor's entry into Rome. N 3: no plaintext existed anywhere and the sender was catalogued as unknown. F 3: BnF, via DECODE. V 1: six contemporary decipherments in the volume, three agreeing word for word. Held down by coverage: about half the cipher, and three quarters of the longest letter, are still unread |
| p55 | **Mihály Hentér → Ferenc Rákóczi II**, MNL OL G 15 Caps. D Fasc. 80 fol. 38 (DECODE R496) | 8 Jul 1707 | 1 | 2 | 3 | 1 | 1 | 3 | **1.85** | D 1: the decipherment was written between the lines at the time; the key was only checked on two sibling letters. H 2: an Ottoman offer of troops and grain and Rákóczi's wait for the grand vizier. N 3: DECODE listed it as non-decrypted, misdated. V 3: substance read, some clauses bracketed. |
| p56 | **The Cardinal of Como (papal Secretariat) → Anselmo Dandini, nuncio in France**, ASV Segr. Stato Francia 283C (DECODE R72–R73) | 1580 | 2 | 3 | 2 | 3 | 1 | 4 | **2.30** | D 2: a letter key rebuilt by annealing inside a published frame. H 3: Rome on Henri III and a nun. N 2: R73 was read by Lasry and R72 deciphered on the leaf. |
| p57 | **An Orange prince (son of William V) → an officer of the émigré troops**, KHA Prins Willem V inv. 339 (DECODE R1892) | c. 1795 | 3 | 3 | 5 | 4 | 1 | 3 | **3.30** | D 3: an unknown 6×6 square recovered ciphertext-only from images, but monoalphabetic. H 3: the Orange émigré corps' passage into British pay. N 5: DECODE non-decrypted, no reading known. V 3: word signs unread. |
| p58 | **The Windischgrätz brothers (Brussels) → Count Windischgrätz**, SOA Plzeň RA Windischgrätz inv. 1433 (DECODE R5029) | 18 Nov 1721 | 1 | 3 | 2 | 3 | 1 | 3 | **2.10** | D 1: a reconstructed key (Mírka 2023) applied without change. H 3: the Congress of Cambrai, the Emperor, Prince Eugene's plan and the succession, from inside the family. N 2: the key existed but no reading of this letter. V 1: every letter passage gives German at once. Held down by 23 open codes |
| p59 | **Sigismund Heusner von Wandersleben (Kassel) → Axel Oxenstierna**, Riksarkivet (DECODE R4332 = R3816) | 15 May 1637 | 1 | 3 | 1 | 2 | 1 | 3 | **1.80** | D 1: the published key applied. H 3: Hesse-Kassel turning from Sweden in 1637, secret gun-casting. N 1: read by Waldispühl & Kopal 2024. F 2: catalogued twice as open. |
| p60 | **Henry Brooke, Lord Cobham (Ostend) → [Walsingham]**, BL Harley MS 287 ff. 70–72 (DECODE R8482–R8487) | 20–22 Mar 1588 | 3 | 3 | 4 | 4 | 1 | 3 | **3.10** | D 3: no key, no glosses on these leaves; broken from clear-text cribs. H 3: the 1588 peace talks weeks before the Armada. N 4: catalogued unknown-to-unknown, not read before. R 4: every run read; 42 open. |
| p61 | **An Orangist correspondent (Basle) → Prince William V**, KHA inv. 339 (DECODE R2234) | 17 Aug 1796 | 1 | 3 | 4 | 2 | 1 | 4 | **2.50** | D 1: the key sheet was in the same file; only the line-by-line cycle had to be found. H 3: Orangist intelligence from Basle in 1796 (Salm, Barthélemy, Degelmann). N 4: no reading before. V 4: read end to end, a few words doubtful. |
| p62 | **Polish-court agents → Ferenc Rákóczi II; Rákóczi (Lwów)**, MNL OL (DECODE R483, R852, R912, R922; catalogued as "Ferenc Rákóczi II to unknown recipient") | 1706–11 | 2 | 3 | 4 | 3 | 1 | 3 | **2.75** | D 2: the sibling key corrected from its image and applied to new transcriptions; R483’s syllabic key rebuilt from the interlinear. H 3: Rákóczi’s Polish diplomacy in 1707 and his exile in 1711. N 4: three letters DECODE listed as undeciphered or partial, now read, and the direction corrected. |
| p63 | **Lord Cobham → Walsingham**, BL Harley MS 287 ff. 80–97 (DECODE R8490–R8496) | May–Jun 1588 | 2 | 3 | 3 | 4 | 1 | 2 | **2.60** | D 2: key rebuilt from glossed siblings, polyphonic signs, solver loop. H 3: Armada-year peace talks. N 4: never read. Read in part. |
| p64 | **Giuliano Caprile (Eger, Buda) → Ferrara**, ASMo Ambasciatori Ungheria b. 4 (DECODE R1136, R1139) | 1520–21 | 3 | 3 | 2 | 4 | 1 | 2 | **2.60** | D 3: key rebuilt from a printed decipherment by EM alignment over a noisy sign transcription. H 2: the bishop of Eger's estate. N 4: never read. Read in part. |
| p61 | **Cornelis Haga (Constantinople) → the States General**, NA The Hague 1.01.02 inv. 6894 (DECODE R2113, R2115) | 1 Feb – 4 May 1620 | 1 | 4 | 4 | 3 | 1 | 3 | **2.75** | D 1: the key for the series was filed with the letters (R2118) and fitted at first try. H 4: the Porte's position on the Bohemian revolt and on breaking the Spanish truce, from the Dutch ambassador. N 4: catalogued non-decrypted, no reading anywhere. R 3: four letters found in two records, their page order reconstructed, the key's missing m recovered. V 3: read in sense; code (50) and a few short words open |
| p65 | **Ferdinand I (Augsburg) → Johann Malvezzi (Constantinople)**, Hadtörténelmi Levéltár 1548/3 (DECODE R366) | 23 Jan 1548 | 1 | 4 | 3 | 3 | 1 | 3 | **2.50** | D 1: the key was filed on DECODE at the same shelfmark; the difficulty was the hand, not the system. H 4: the French working to break the Habsburg–Ottoman peace, and the envoy's finances at the Porte. N 3: no reading of this manuscript anywhere, but the text is probably in print in *Austro-Turcica* (1995). V 3: five passages read in substance, short stretches open. |
| p66 | **Arend Willem van Reede (Berlin) → Stadholder William V**, KHA Prins Willem V inv. 205 (DECODE R1057) | 4 Feb 1792 | 1 | 2 | 3 | 1 | 1 | 4 | **1.95** | D 1: archive key already in use; one transcription slip. H 2: the despatch itself was in invisible ink on the lost enclosure; this is the cover note. N 3: glossed at the time, DECODE gloss garbled, never read through. V 4: every message group read. |
| p67 | **Cesare Alberico Lucini (Madrid) → the Secretariat of State**, AAV Segr. Stato Spagna 304 (DECODE R120) | 13 Oct 1767 | 1 | 3 | 3 | 2 | 1 | 4 | **2.30** | D 1: Lasry's key was on the record. H 3: the nuncio's reading of Charles III's campaign against the clergy after the 1766 riots and the Jesuit expulsion. N 3: never decrypted, but the key existed. R 2: one sentence of 82 tokens. V 4: read in sense; one code open. |
| p68 | **Edward Wotton (Scotland) → Walsingham**, BL Add MS 32657 (DECODE R4841–R4843) | 25 Aug – 1 Sep 1585 | 1 | 3 | 3 | 2 | 1 | 4 | **2.30** | D 1: clear drafts, nothing to break; only a name code identified from context. H 3: Gray's plan with England to seize the King and bring down Arran, three months before Stirling. N 3: listed non-decrypted; probably calendared in CSP Scotland 8, not checked. R 2: twelve pages, eleven code numbers. V 4: drafts read in full; four codes open. |
| p69 | **Charles I (Oxford) → Prince Rupert**, BL Add MS 18983 f. 14 (DECODE R4921) | 29 Apr 1645 | 2 | 4 | 5 | 3 | 1 | 3 | **3.20** | D 2: a published key from a sibling cipher family, found by matching group shapes against a period tally. H 4: the King's own call on Rupert to march on Oxford, a week before the campaign that ended at Naseby. N 5: no reading anywhere before. V 3: about 15 code groups open. |
| p70 | **Sir Francis Walsingham → Edward Wotton (Scotland)**, BL Add MS 32657 (DECODE R4838–R4840, R4844) | 28 Jul – 10 Sep 1585 | 1 | 3 | 2 | 2 | 1 | 2 | **1.95** | D 1: clear letters; the name code came from the printed calendar's glosses, and the one real cipher (14 sign words) was not broken. H 3: Walsingham's handling of Gray and Arran before the lords' return. N 2: two of four already calendared. |
| p71 | **Paris nunciature (bishop of Bergamo, archbishop of Nazareth; Morosini) → the Secretariat**, AAV Francia 18 (DECODE R16–R17) | 1586–87 | 1 | 3 | 4 | 3 | 1 | 3 | **2.60** | D 1: published keys (Lasry, Meister) applied; the find was that DECODE's R16 decryption was R15's. H 3: Guise's price for the alienation of church property (Metz and money), the reiters of 1587. N 4: R16 and R17 had no reading anywhere. V 3: two name codes unconfirmed, ~23 groups open. |
| p72 | **Wolff (The Hague) → Princess Wilhelmina**, KHA Wilhelmina Prinses van Pruisen inv. 192 (DECODE R2232) | 25 Jul 1801 | 1 | 2 | 3 | 3 | 1 | 4 | **2.00** | D 1: the key was the next DECODE record, applied unchanged. H 2: a royalist's invasion plan and petition for half-pay; personal more than political. N 3: never read, key filed alongside. R 3: three pages, 1,065 groups. V 4: read in full; a few slips. |
| p73 | **Claude de La Guiche (Rome) → Montmorency**, BnF fr. 3138 no. 22 | 22 Nov 1551 | 3 | 3 | 5 | 2 | 2 | 2 | **3.10** | D 3: ciphertext-only break of a 22-sign substitution (406 signs) by annealing. H 3: Santa Fiora sounded for France before the Sienese rising. N 5: no decipherment anywhere. |
| p74 | **Champagne news-letters → the duc de Nevers**, BnF fr. 3623 nos. 23–25, 60 | Feb–Jun 1590 | 1 | 2 | 4 | 2 | 1 | 2 | **2.05** | D 1: one letter carried its own key; the other key rebuilt from interlinear glosses and alphabetical order. H 2: League news from Paris and Champagne, 1590. N 4: no reading anywhere before. V 2: short runs, several code numbers open. |
| p75 | **Sir Henry Norreys (Paris) → Cecil**, BL Add MS 4136 ff. 160–161 (DECODE R9251) | 1567–68 | 1 | 2 | 3 | 1 | 2 | 2 | **1.85** | D 1: a key reconstructed by Tomokiyo from *Cabala*, applied. H 2: ambassador's reports on the second civil war in France. N 3: no decipherment known for the Norreys side. R 1: a few dozen words. F 2: Forbes's copies, symbol shapes uncertain. V 2: checked against the Calendar's summaries. |
| p76 | **Thomas Spinelly (Brussels) → Henry VIII**, BL Cotton MS Galba B V ff. 40–41 (DECODE R8416) | 1 Feb 1517 | 2 | 3 | 4 | 2 | 2 | 3 | **2.75** | D 2: five lines (43 tokens) of a simple substitution of invented signs, broken from a crib in the letter's own clear text ("audensier"). Novelty 4: no decipherment on the leaf or in print; L&P II 2862 had only summarised the Cambrai clause. Short, and two word signs rest on context |
| p77 | **[Thomas Edmondes] → Burghley**, BL Stowe MS 166 (DECODE R7770–R7775) | 1592–94 | 2 | 3 | 4 | 2 | 2 | 2 | **2.65** | D 2: a symbol substitution with homophones and person signs, broken ciphertext-only from the clear context. H 3: Henri IV's words on his sister's marriage and his conversion politics. N 4: no decipherment on the leaves; Butler 1913 not checked. R 2: about 35 lines, four unread. |
| p78 | **Instructions for the cipher with Baron Stosch and Mr Walton**, TNA SP 106/7 f. 33 (DECODE R597) | c. 1731 | 1 | 1 | 2 | 1 | 3 | 4 | **1.70** | D 1: the syllables are written over every group by the writer. H 1: an instruction sheet, though it documents the cipher of Walpole's spy on the Pretender. N 2: DECODE had described it but called lines unsolved. R 1: 43 groups. F 3: clean hand. V 4: the plaintext is given in clear on the sheet. |
| p79 | **Lope Hurtado de Mendoza (Rome) → Charles V and Gattinara**, RAH Salazar 9/28, 9/30 (DECODE R9667–R9869) | 1523–24 | 3 | 3 | 4 | 2 | 2 | 2 | **2.90** | D 3: a known system with a changed key, rebuilt from a bound clear of one third of one letter, then applied to six letters with no crib. H 3: Clement VII between Charles V and Francis I, Beaurain's mission, Giberti. N 4: six letters not calendared and not read before; two in *CSP* 548, 617. R 2: letters read from a quarter to two thirds. F 2: cursive signs with look-alikes. V 2: exact-count runs, no control. |
| p80 | **Principe di Castelcicala (London, Paris) → Circello and Medici**, ASNa Esteri 2337 (DECODE R9553–R9589) | 1816–23 | 3 | 3 | 4 | 2 | 2 | 2 | **2.90** | D 3: a 2,450-group syllabic homophonic code with no key, rebuilt from four contemporary interlinear glosses. H 3: Decazes and Onís on the Floridas and Cuba (1816); France, Austria and the 1823 conclave. N 4: never read or printed. R 2: 45% of groups valued, no letter reads through. F 2: dense figures, blur and show-through on several pages. V 2: gloss cross-checks, no control. |
| p81 | **C. Ben. Schaeblin (The Hague) to Mr Jones**, BL Add MS 32256 f. 235 (DECODE R9218) | 1753 | 1 | 1 | 1 | 1 | 3 | 4 | **1.50** | D 1: nothing enciphered; the letter is in clear. H 1: a proposal for a French cipher, of interest for how the Hague office built codes. |
| p82 | **Count Visconti (Brussels) with Marquis Visconti (London)**, Italian cipher key, BL Add MS 32270 f. 42 (DECODE R7931) | 1727 | 1 | 1 | 2 | 1 | 3 | 4 | **1.70** | D 1: the record is the key; nothing to break. H 1: a reconstructed key, though for Walpole-era Brussels–London traffic. N 2: DECODE typed it as a ciphertext. R 1: 193 key places. F 3: clean fair copy. V 4: the endorsement and the draft on the next leaf confirm it. |
| p83 | **Mr Eichel → unknown**, TNA SP 106/7 image 0020 (DECODE R595) | 1758 | 2 | 1 | 3 | 1 | 3 | 3 | **1.95** | D 2: the right key had to be found among 22 records and its null rules applied. H 1: no message, a dummy sheet. N 3: DECODE listed it unsolved with the wrong key and "Russia" for Prussia. R 1: 139 groups, all void. F 3: clean hand, clear dockets. C 3: key on DECODE, nothing to transcribe beyond its record. |
| p84 | **Diego López de Ayala (Brussels) → Cardinal Cisneros**, AGS Estado leg. 496 fol. 22 (DECODE R9954) | 1516 | 1 | 3 | 1 | 2 | 1 | 2 | **1.70** | D 1: a published sibling key applied. H 3: the regency's agent on offices, Queen Germaine and Charles's voyage. N 1: printed in 1875 (Cartas de los secretarios XLIX, LIV), found after the reading. V 2: read, then checked against the print. |
| p85 | **Prince Frederick of Orange (London) → the Hereditary Prince, 7 May 1795**, KHA Koning Willem I inv. XVIII-3 (DECODE R2242) | 1795 | 1 | 3 | 5 | 3 | 1 | 3 | **2.70** | D 1: sibling key R1892 read it unchanged. H 3: Orange court-in-exile news, spring 1795. N 5: DECODE non-decrypted. V 3: word signs unread. |
| p86 | **The Hereditary Prince (Berlin) → Prince Frederik, 12 Mar 1796**, KHA Prins Willem V inv. 337 (DECODE R2239) | 1796 | 4 | 3 | 3 | 3 | 2 | 4 | **3.25** | D 4: the system and a 150-entry list rebuilt from a sibling's decipherment, then a printed crib found. H 3: the Prussian démarche in Paris for the Orange restoration, 1796. N 3: body in print since 1906, opening new. V 4: one word open. |
| p87 | **Francis Needham (before Sluys) → [Walsingham], 28 Jul 1587**, BL Harley MS 287 ff. 39–40 (DECODE R8479) | 1587 | 2 | 3 | 4 | 2 | 2 | 1 | **2.55** | D 2: pigpen with the alphabet in order, key from four glosses. H 3: the failed relief of Sluys, Leicester's campaign. N 4: DECODE partially decrypted, long runs unglossed, not in CSP. V 1: one word open. |
| p88 | **Nicholas Throckmorton (Paris) → Elizabeth I, 10 July 1559**, BL Add MS 4136 f. 32 (DECODE R2988) | 1559 | 2 | 3 | 5 | 2 | 2 | 3 | **2.95** | D 2: Tomokiyo's key with seven corrections. H 3: Throckmorton's report after Henry II's wounding. N 5: not in Forbes or CSP. V 3: 12 code signs and a few spans open. |
| p89 | **Łaski, King John, Bavarian agents → the Dukes of Bavaria, 1529–1583**, BayHStA Kurbayern Äußeres Archiv 4591 (DECODE R9291–R9427) | 1529–1583 | 4 | 3 | 5 | 3 | 3 | 5 | **3.85** | D 4: six systems; one broken ciphertext-only with a purpose-built period language model, one key rebuilt from a single faint gloss, two from keys filed in the volume. H 3: Hungary between Ferdinand and John Zápolya, the Turks, Rincon, Fulda 1576. N 5: no edition found. V 5: eight letters read in part, R9424 and R9319 open. |
| p90 | **Lebel (Paris) → Charles Emmanuel I of Savoy, Jan–Mar 1593**, BnF fr. 3983 nos. 11, 62, 100 | 1593 | 2 | 4 | 4 | 3 | 2 | 4 | **3.20** | D 2: Tomokiyo's key, a dozen sign corrections, code values aligned from three contemporary decipherments. H 4: Savoy, Mayenne and Spain over the crown at the Estates of 1593. N 4: key published, letters never read. V 4: read, ≈97% of enciphered tokens valued; M-grade codes and the no. 62 verso keep it from 5. |
| p91 | **Cardinal Marino Ascanio Caracciolo (Milan) → Charles V, 14 Nov 1537**, AGS Estado leg. 1184 fol. 110 (DECODE R9966) | 1537 | 1 | 3 | 3 | 2 | 1 | 1 | **2.00** | D 1: Luo's published key unchanged. H 3: imperial dealings with the Swiss and Grisons as the Dauphin crossed into Italy. N 3: Tomokiyo had read four lines. V 1: about ten signs doubtful. |
| p92 | **Cardinal Lorenzo Campeggio → Francis I, conclave articles, c. 1534**, BnF fr. 3081 f. 41 (DECODE R2322) | c. 1534 | 2 | 4 | 3 | 2 | 2 | 3 | **2.80** | D 2: Lasry's key with four sign re-valuations. H 4: a papabile's price for French support, Milan, Asti, Genoa. N 3: f. 41r read by Lasry 2022, f. 41v new. V 3: four sign groups, one code open, text breaks off. |
| p93 | **Ambrogio Bizozola → Maximilian Sforza, 1529**, BnF fr. 3034 ff. 156–157 (DECODE R4224) | 1529 | 1 | 3 | 4 | 2 | 2 | 4 | **2.60** | D 1: Lasry's published key, three homophones added. H 3: Bologna 1529, a partition of the Milanese state discussed in the Emperor's council. N 4: no text published. V 4: all four pages, 97% of signs, date numerals open. |
| p94 | **Vincenzo I Gonzaga (Mantua) → the duc de Nevers, 1590**, BnF fr. 3979 ff. 92–93 (DECODE R4176) | 1590 | 1 | 3 | 4 | 2 | 1 | 3 | **2.45** | D 1: archive key (fr. 3995 f. 64) applied unchanged, LM beam for look-alike figures. H 3: Sixtus V's death, Mantua's approach to Henri IV. N 4: never deciphered. V 3: 95.1% read (measured), four short stretches of writer's slips open. |
| p95 | **Claude de Mondoucet → Charles IX, 13 July 1572 and 4 Jan 1573**, BnF fr. 16127 ff. 60–61, 126v–127v | 1572–73 | 4 | 3 | 4 | 4 | 1 | 2 | **3.25** | D 4: key built by hand from the glossed 16 July crib after a segmenter artefact had defeated four aligners; 1573 key rebuilt from the 9 Sept alignment (α = r). H 3: Louis of Nassau's levies, English money at Hamburg, Alba and Ireland. N 4: 13 July 1572 unread anywhere; 4 Jan 1573 turned out to be printed by Didier 1891. V 2: 13 July only scattered words; 4 Jan ~60 % ciphertext-only, confirmed by the print. |
| p96 | **András Bay → Ferenc Rákóczi II, Jászvásár, 8 Mar 1706**, MNL OL G15 D 81/5 (DECODE R478) | 1706 | 2 | 3 | 4 | 3 | 1 | 4 | **2.85** | D 2: archive key found by scoring 94 G15 keys, applied unchanged. H 3: Muscovite–Swedish peace feelers, Rákóczi's Moldavian intelligence. N 4: never deciphered. V 4: 413/414 groups in key, ~10 without sense. |
| p97 | **Sir Simonds D'Ewes, cipher log of his son's fits, 1635–36**, BL Harley MS 286 f. 61 (DECODE R7759) | 1635–36 | 3 | 2 | 4 | 3 | 1 | 4 | **2.85** | D 3: private invented alphabet, no key in print, rebuilt by crib on recurring Latin words. H 2: a family record, the illness of an antiquary's son. N 4: never read. V 4: 96.5% of words, weekdays and moon phases check. |
| p98 | **Unknown writer → Hesse-Kassel**, HStAM 4 d Nr. 1218 no. 49 (DECODE R4500) | 1635–52 | 3 | 2 | 3 | 3 | 1 | 3 | **2.55** | D 3: no key in the volume; rebuilt by annealing and hand fixes, checked on the gloss. H 2: anonymous report on imperial-Bavarian matters. N 3: only lines 1–4 glossed at the time. V 4: ~97 %, nine signs open. |
| p99 | **Sir Edward Stafford (Paris) → [Walsingham], 20 Aug 1586**, BL Harley MS 1582 ff. 65–66 (DECODE R8500) | 1586 | 3 | 2 | 4 | 3 | 1 | 4 | **2.85** | D 3: letter key rebuilt from a sibling decipherment and glosses, 6 = e found. H 2: Junius, Cambrai and Balagny, a short postscript. N 4: never deciphered. V 4: all 61 signs read, four by context. |
| p100 | **Łaski, King John's side, a Bavarian at Wardein → the Bavarian court**, BayHStA KAA 4591 ff.226–261 (DECODE R9403, R9414, R9415) | 1531–37 | 4 | 3 | 4 | 3 | 1 | 3 | **3.25** | D 4: two new homophonic sign alphabets rebuilt from one-line glosses by annealing and beam search; Łaski's key with e/r swapped. H 3: King John's diplomacy with Bavaria, the Sultan's terms, the Pressburg diet, Turkish arming 1537. N 4: never read. V 3: 99.5% and 95.3%, but the German letter 91.3%. |
| p101 | **Sir Edward Stafford (Paris) → [Walsingham], 9 Nov 1586**, BL Harley MS 1582 ff. 76–77 (DECODE R8504) | 1586 | 1 | 1 | 4 | 3 | 1 | 4 | **1.95** | D 1: one word, sibling key applied. H 1: a single word, *princes*. N 4: not in print. |
| p102 | **Gottfried van Swieten (Bonn) → Count Cobenzl, 1757–59**, ARA Brussels SEG 1236 (DECODE R955–R957) | 1757–59 | 5 | 3 | 4 | 3 | 1 | 4 | **3.60** | D 5: 1759 syllabary rebuilt ciphertext-only by monotone annealing against an LM, then from context. H 3: French army finances and generals, the Gueldre convention. N 4: not in print. |
| p103 | **Robert Reade (Paris) → his cousin, 19 Apr 1641**, BL Harley MS 7001 ff. 148–149 (DECODE R7766) | 1641 | 2 | 3 | 4 | 3 | 1 | 3 | **2.60** | D 2: an archive key reconstruction found by correspondent and applied, blanks bracketed alphabetically. H 3: Windebank's exile and possible return, Strafford's trial year. N 4: not in print. V 3: 94% with 6% conjectured. |
| p104 | **Unknown sender → the King, BnF fr. 3029 ff. 134–135** (DECODE R3670) | c. 1521? | 1 | 3 | 4 | 3 | 1 | 4 | **2.35** | D 1: a published key applied unchanged. H 3: Toledo, the cardinals' pensions, a Church war and the Venetian league. N 4: not in print. |
| p105 | **Guise? → Mercœur, BnF fr. 15564 f. 78** (DECODE R4158) | 1587 | 2 | 3 | 4 | 3 | 1 | 4 | **2.60** | D 2: a published key extended by about 15 values. H 3: League strategy in Brittany, Parma's troops, Bellièvre. N 4: not in print. |

## By single axis

**Hardest cryptanalysis (D):** Ségur · Sun Yat-sen · Lucca · Feuquières · Richelieu. Ségur alone combined an
unknown system, transcription from images and a syllabary; the other four were known families attacked
ciphertext-only or with a partial crib. Catinat 1691 is last: the table was printed in 1893.

**Most important content (H):** Catinat 1691 · Ségur · Lucca · Sun Yat-sen · Ormonde, Feuquières, Huang Xing,
Boswell, Richelieu. Only Catinat 1691 records a decision of state (Louis XIV giving up Piedmont for 1692).
Ségur and Lucca are diplomacy at the level of armies and alliances. Urquhart and Armstrong are the weakest
here despite their prominence.

**First reading ever (N):** Ségur, Sun Yat-sen, Huang Xing, Lucca, Warsaw, Ormonde, Armstrong and Catinat's
five letters have no earlier reading that the notes could find*. Feuquières had an unpublished 1893 reading.
Urquhart and Boswell had readings weeks old. Richelieu and Forster were already in print.

**Most research (R):** Ségur · Feuquières · Ormonde · Urquhart · Armstrong. The Feuquières sibling letter was
found by searching the OCR of three volumes; the Ormonde nomenclator was confirmed from a 1739 edition; the
Urquhart numbers were re-transcribed from photographs on the HCPortal record.

**Highest profile (F):** Urquhart is the only Schmeh Top 50 entry among the solved. Everything else is from
Tomokiyo's list, and Catinat 1691 and Huang Xing are on no list at all.

## Second tier: explained, nothing to read

Ranked by how firmly the negative is established and how prominent the item was.

| # | Target | Date | Finding | Standing |
|---|---|---|---|---|
| 1 | Roosevelt cryptogram, number block | 1935 | A permutation of 1–52 written by hand; ordered-key readings fail while controls succeed. Ernst's doodle claim confirmed | Schmeh Top 50 no. 17. Reopen only with the original sheet |
| 2 | Chinese gold bar cryptograms | 1933 | Letter counts flatter than any cipher of a real text; no message | Schmeh Top 50; the top50 survey records independent corroboration |
| 3 | Hyde's ciphered superscriptions | 1659–60 | Dummy numbers, per the 1724 editor and the 1721 key | Tomokiyo entry; settled from print |
| 4 | Intercepted League and Spanish letters summarised for the duc de Nevers | 1589 | The summary is in clear; no ciphertext survives beside it; eleven deciphered intercepts found in the same volume | Catalogue 31; settled from the manuscript |
| 5 | D'Agapeyeff challenge | 1939 | Not enciphered English | Famous; the negative is a language test, not a full explanation |
| 6 | Beale Paper no. 1 | 1885 | Fabrication argued in the notes; book-cipher scan negative | Famous; the fabrication case is an argument, not a proof |
| 7 | Unknown sender → unknown recipient, BL Sloane MS 3188 ff. 109–169 (DECODE R8506–R8530) | 17th c. | 17th-century English stroke shorthand, not a cipher: notes on John Dee's spirit Actions and writings, attributed to William Shippen | Catalogue 138 + 139; settled from the images; shorthand unread |
| 8 | W. Loeschner → unknown, ÖStA HHStA Chiffrenschlüssel Kt. 20 (DECODE R2227) | 1816 | Not a cipher: a clear German memorandum amending the Staatskanzlei cipher instruction; its number groups are worked examples with the plaintext above them | Catalogue 269; settled from the images |

## Third tier: found already solved by others

**Queen Anne → the Earl of Peterborough (1712; catalogue 86)**: printed in clear by Parke (1798) from the office draft; every code run of the signed original aligned with the print, four anchors (him, he, himself, your) guessed from context before the print was found, and DECODE's "Turin embassy" subject corrected to the Saxon mission. Ranked as source identification, not a new cryptanalytic solve.

**Prospero Santa Croce (nuncio in France) → Cardinal del Monte (1553; catalogue 245)**: read at the time and printed deciphered (Lestocquoy 1972, ANG 9); Lasry's key on DECODE reproduces it. Only R9's cancelled postscript cipher is read here. Ranked as source identification, not as a solve. [Write-up](https://dbourdeau.github.io/cyphersolver/santacroce1552.html).

**Etienne Bourdeaux (Berlin) → Maarten van der Goes (1801; catalogue 228)** — read from the ministry’s contemporary clear copy, which DECODE had imaged under the neighbouring record R1946; no cryptanalysis, the code groups not aligned. Ranked as source identification, not as a solve. [Write-up](https://dbourdeau.github.io/cyphersolver/r1944.html).

**Sir Nicholas Throckmorton (Greenwich) → the Regent Moray (1569; catalogue 83)**: read at the time (interlinear, Bain no. 1103, Tomokiyo's key); the stain-faded passages read again from the cipher with the published key. Ranked as source identification and text recovery, not as a solve. [Write-up](https://dbourdeau.github.io/cyphersolver/throck1569.html).

**Mary Queen of Scots (Bolton) → Archbishop Hamilton (1569; catalogue 84)**: read at the time (decipherment bound as f. 74, Bain no. 966, Tomokiyo's key); the decipherment transcribed in full. Ranked as source identification, not as a solve. [Write-up](https://dbourdeau.github.io/cyphersolver/hamilton1569.html).

**Thomas Randolph (Edinburgh) → the Earl of Sussex (5 July 1570; catalogue 99)**: read at the time (decipherment on the next leaf, f. 278 = DECODE R4932; Boyd iii no. 339); a crib attack had read ~70% independently first. Ranked as source identification, not as a solve. [Write-up](https://dbourdeau.github.io/cyphersolver/randolph1570.html).

**C. A. graaf van Rechteren tot Borgbeuningen (St Petersburg) → the Griffier (1785; catalogue 232)**: read at the time. The Griffie's decipherment is on the record itself (DECODE R1039, images 5448–5449); key not rebuilt. Ranked as source identification, not as a solve. [Write-up](https://dbourdeau.github.io/cyphersolver/rechteren1785.html).

**Charles de Poupet, sieur de La Chaulx (Vitoria) → Charles V (1522; catalogue 150)**: read at the time. The contemporary decipherment is bound in with the letter (BNE 39/2); one line aligned, key not rebuilt. Ranked as source identification, not as a solve. [Write-up](https://dbourdeau.github.io/cyphersolver/poupet1522.html).

**Girolamo Ghinucci, Edward Lee and Sir Francis Poyntz (Valladolid) → Cardinal Wolsey (1527; catalogue 111)**: read at the time. Tuke's 1527 decipherment is interlinear and printed in *Letters and Papers* IV no. 3271; the record was identified from the calendar, the folio offset and the thumbnails, key not applied. Ranked as source identification, not as a solve. [Write-up](https://dbourdeau.github.io/cyphersolver/poyntz1527.html).

**Sir Edward Stafford (Paris) → Sir Francis Walsingham (1586; catalogue 118)**: read at the time. The four short cipher runs carry interlinear decipherments; re-read sign by sign and the letter values rebuilt, nothing new in content. Ranked as source identification, not as a solve. [Write-up](https://dbourdeau.github.io/cyphersolver/stafford1586.html).

**Alvise Mocenigo (Madrid) → Doge and Senate of Venice (1628; catalogue 266)**: read at the time. The chancery decipherment is imaged in the same DECODE record (R1874); tied to the cipher by paragraph marks and a repeated name run, key not rebuilt. Ranked as source identification, not as a solve. [Write-up](https://dbourdeau.github.io/cyphersolver/r1874.html).

**Sebastiano Foscarini (Escorial) → Doge and Senate of Venice (1761; catalogue 265)**: read at the time. The chancery decipherment is written on the despatch itself (DECODE R1875), the cipher barred out; key not rebuilt. Ranked as source identification, not as a solve. [Write-up](https://dbourdeau.github.io/cyphersolver/r1875.html).

**Dirk van Hogendorp (St Petersburg) → Maarten van der Goes (1803; catalogue 227)** — content identified from Sillem&rsquo;s 1890 account and its explicit footnote to ciphered dispatch no. 12; the matching archive codebook was found, but the 286 groups have not been aligned to a verbatim plaintext. This is ranked as source identification, not as a cryptanalytic solve. [Write-up](https://dbourdeau.github.io/cyphersolver/r1942.html).

**Beatrice d'Aragona (1482–1505; catalogue 160)** — source identification, not ranked as a new cryptanalytic solve. Four readings in MDE III–IV (1877–78); R1154 plain and dated 1505, with Berzeviczy (1914) no. CCCII as control. March editorial markers remain unverified. [Write-up](https://dbourdeau.github.io/cyphersolver/beatrice1482.html).

Ordered by how much this repo added.

1. **ADFGVX, Eastern Front 1918.** The 2017 thread consolidated, Lasry's sixteenth key rebuilt, Biermann's
   method reimplemented and re-deriving seven pages blind; the ten open messages shown to be garbles.
2. **Matthias Corvinus to Ercole I d'Este, Pozsony, 1 June 1482 (DECODE R1156).** Printed in 1877 and by Fraknói
   in 1895. The cipher runs re-read from the image and a working key rebuilt; four garbled passages of the print
   corrected (*valent*, *gentibus*, the closing *Speramus cito nos res nostras ita disposituros…*, and the "regest"
   shown to be the letter's own last sentence).
3. **Segreteria di Stato (Rome) to the Nuncio in Spain, 1718–1720, ASV Segr. Stato Spagna 364D (DECODE R154–R177).**
   Solved by George Lasry in October 2020; his reconstructed key and his segmented decipherment of the whole Spagna 364
   corpus are attached to every one of the 24 records, so the despatches were readable throughout. Measured here token by
   token at 97.6 % (33,408 of 34,243 groups). The unfinished part was the nomenclator: 189 of the 399 four-digit groups in
   use carried no value, 11.0 % of nomenclator tokens. Because the key is alphabetical in runs, each has a bracket, and 61
   were recovered against the 85,000-token corpus — *promozione*, *aggiustamento*, *giurisdizione*, *tribunale*,
   *vascelli*, *Vicerè*, *corriere*, *cifra*, *negoziato* — with the calendar block resolved into two parallel
   Gennaio–Dicembre runs and 4538 *Luglio* confirmed by the date of Alberoni's promotion. Unknown nomenclator usage
   3.4 % after. Two corrections to the filed key (4474 = *Vicerè*, 4535 = *Aprile*).
4. **Alonso Sánchez (Venice) to Charles V, 1522, RAH Salazar 9/23–9/26 (DECODE R9593–R9657).** Reconstructed
   and published by Tomokiyo on 6 Sept 2025. The catalogue entry corrected on three counts (four volumes not one;
   all of it 1522, so the July 1523 treaty is not in it; nine letters by Lope Hurtado de Mendoza), and the records
   shown to carry contemporary decipherments — unedited, not unread. The nomenclator shown to be alphabetically
   ordered, which fills the c-block numerals: `cab` = xv, `cef` = xxvi and `cif` = xxvii predicted and then confirmed
   in text. Two letters beyond Tomokiyo's list read in part here: R9653 (the siege of Rhodes in clear, a ciphered
   postscript) and R9635 (a whole page of cipher on the sums owed by the Signoria, "mas de xv mil ducados", with a
   patchy interlinear decipherment). Lope Hurtado's letters separated off as a third cipher.
5. **Alchymey teuczsch, Heidelberg Cod. Pal. germ. 597, 1426.** Read by Wattenbach in 1869. The compiler's struck
   24-sign alphabet (f. 1r) and the invocation alphabet (ff. 6v, 91v) recovered from the images and checked on his
   plaintexts; a third set fixed for eleven letters from the 2014 catalogue's reading of f. 93r; the "ff. 70–71"
   pointer shown to be Bischoff's item numbers. Ruled out as a record candidate.
6. **Letter to the King of Aragon, ACA Reserva 12, [1413–16].** Printed by Salas in 1931; the column-transposition
   rule checked on the archive's image.

Perwich, the Feynman ciphers, Ferdinand III, Milroy, the Confederate dictionary code and Mazarin–Bordeaux 1654 were found
solved by others with nothing added here and are no longer listed (removed 17 September 2026).

## Appendix: the scores worked out

Weights: D 0.25, H 0.25, N 0.20, R 0.10, F 0.10, V 0.10 (sum 1.00). Each entry below gives the reason for
every axis score, then the six weighted terms in that order and their sum. Scale anchors: 1 = the low
description in the axis table, 5 = the high one, 3 = a typical entry on Tomokiyo's list.

**1. Navarre → Ségur, 1585–86**
- D 5: no transcription existed; 461 figures and 25 letter-glyphs read from the Gallica images; the system (letters plus a 70-syllable table) was unknown until the mod-5 test exposed it; the key came from a structured annealer scored on a matched control at 96.6 %.
- H 4: instructions to the envoy raising a German army in the Wars of Religion, naming Casimir, Clervant's reiters and the invasion road; corrects the sender from Henry III to Navarre. Not a decision of state in itself, hence not 5.
- N 5: no reading anywhere before this work*; the letters were miscatalogued and unread.
- R 5: IIIF fetch, glyph-level transcription, whole-volume sweep of 440 canvases, an unlisted cipher leaf found (f. 366), Tomokiyo's sibling key shown to be this key shifted by eight.
- F 2: Tomokiyo list entry, no wider fame.
- V 4: 97 % on control, three letters read in substance; a dozen word-signs and f. 143 open.
- 0.25×5 + 0.25×4 + 0.20×5 + 0.10×5 + 0.10×2 + 0.10×4 = 1.25 + 1.00 + 1.00 + 0.50 + 0.20 + 0.40 = **4.35**

**2. Swatow telegram to Sun Yat-sen, 1916**
- D 4: the family (a code condenser over the standard telegraph code) was hypothesised, then 57,600 keys brute-forced with a Chinese character model. A known family narrowed by search, so 4 not 5.
- H 4: a field report of the Chaozhou rising and the fall of Swatow in the 1916 campaign against Yuan Shikai, addressed to Sun himself.
- N 5: no reading found before this work*.
- R 3: JACAR frames fetched; the tail re-checked on the sheet at 600 dpi.
- F 2: Tomokiyo entry.
- V 4: 41 of about 44 characters; the three lost codes are the operator's garble.
- 1.00 + 1.00 + 1.00 + 0.30 + 0.20 + 0.40 = **3.90**

**3. Fra Giovanni di Lucca → Ferdinand III, 1644**
- D 4: a polyphonic alphabet (two figures each standing for two letters) is harder than plain homophony; solved ciphertext-only after the supplied crib proved self-contradictory, with all seeds agreeing and shuffled controls failing. Not 5 because the transcription was supplied and the text is short.
- H 4: an offer to turn the Porte and Moldavia against Rákóczi and to supply 2,000 Cossacks, in the last year of the Thirty Years' War.
- N 5: DECODE still marks it non-decrypted; no reading found*.
- R 2: worked from Tomokiyo's transcription only.
- F 2: Tomokiyo entry.
- V 4: 231 groups read end to end; three spellings and the speaker's name need the images.
- 1.00 + 1.00 + 1.00 + 0.20 + 0.20 + 0.40 = **3.80**

**4. Feuquières → Catinat, 25 Jan 1691**
- D 4: a two-part code with no table in print cannot be annealed at 418 groups; it was read by aligning a second letter in the same code against its contemporary translation, by hand, after every automatic aligner failed. Heavy but partly known-plaintext, so 4.
- H 3: the tactical plan for the Veillane surprise; operational, not strategic.
- N 4: Bazeries read it in 1893 but never printed the reading.
- R 4: the Grand Chiffre table transcribed from Gallica and verified on four despatches; the sibling letter found by searching the OCR of three volumes.
- F 2: Tomokiyo entry.
- V 4: 586 of 601 tokens across the two letters; twelve singleton groups unread.
- 1.00 + 0.75 + 0.80 + 0.40 + 0.20 + 0.40 = **3.55**

**5. Maltravers → Ormonde, 1634–35**
- D 3: a regular block alphabet recovered from 59 figures through consecutive-figure doublets; short, and the alphabet is of a standard Stuart design.
- H 3: Wentworth's Irish administration, the King's refusal of Kildare, Ormonde's council seat in exchange for Crosby.
- N 5: no reading found before this work*.
- R 4: the nomenclator confirmed clause by clause against Knowler's 1739 edition of Wentworth's dispatches.
- F 2: Tomokiyo entry.
- V 4: every spelled word reads; two person-codes in one clause unidentified.
- 0.75 + 0.75 + 1.00 + 0.40 + 0.20 + 0.40 = **3.50**

**6. Louvois and Louis XIV → Catinat, seven despatches, 1691**
- D 1: Bazeries' 1893 table applied; no cryptanalysis.
- H 5: the King's 14 Sept decision to bring the army back over the Alps, fight defensively in 1692, hold and then burn Carmagnole, take Coni in winter. The only decision of state among the solved items.
- N 5: about 9,700 groups in five letters never before in clear*.
- R 3: MDZ hOCR of the volume, 137 doubtful stretches checked on the page images, seven OCR fixes.
- F 1: on no list; the by-product of the Feuquières item.
- V 5: 98.1 % and 99.1 % against the two letters Bazeries printed in clear.
- 0.25 + 1.25 + 1.00 + 0.30 + 0.10 + 0.50 = **3.40**

**7. Huang Xing → Lin Hu and Li Genyuan, 1916**
- D 3: the scheme (three kana per character, consonant row carrying the digit) identified by inspection and confirmed by reading.
- H 3: National Protection War correspondence between named commanders.
- N 5: no reading found before this work*.
- R 3: JACAR frames fetched and read.
- F 1: on no list; found beside the Sun Yat-sen telegram.
- V 4: read from the frames; not independently controlled beyond the reading itself.
- 0.75 + 0.75 + 1.00 + 0.30 + 0.10 + 0.40 = **3.30**

**8. Urquhart's Cyphral Octastich, 1652**
- D 3: a book cipher whose rule (number k → first word of the needed initial on physical page k) is simple once stated; the work was verifying it with a first-occurrence test, 238/284 against 0.43 for controls.
- H 2: a royalist prayer for Charles II in ottava rima; literary, not documentary.
- N 3: Vals AI published a plaintext in Aug 2026; this reading was made without it and extends the transcription, but is not first.
- R 4: 285 numbers re-transcribed from the 1983 edition's photographs on the HCPortal record (Schmeh's public 272 were 13 short); EEBO-TCP text aligned to physical pages.
- F 5: Schmeh Top 50 no. 28, with a live public dispute over the distich.
- V 4: ten letters of line 5 unread at a TCP text defect; the distich claim fails and stays open.
- 0.75 + 0.50 + 0.60 + 0.40 + 0.50 + 0.40 = **3.15**

**9. Armstrong → Madison, coded postscript, 1808**
- D 2: the key was read off pencil decodes on other despatches and completed by alphabetical-slot inference; little cryptanalysis.
- H 2: who should be consul; diplomatic gossip.
- N 5: no reading found before this work*.
- R 4: NARA microfilm frames fetched through the catalogue proxy and ranked by a script scoring faint pencil; 580-group table rebuilt.
- F 2: Tomokiyo entry.
- V 5: 48 of 49 groups determined, the 49th a probable slip for *man*; the reading is not in doubt.
- 0.50 + 0.50 + 1.00 + 0.40 + 0.20 + 0.50 = **3.10**

**10. Warsaw, 24 Dec 1627**
- D 3: a 5-gram plus dictionary annealer converged from random starts; the alphabet turned out to be in plain order, which made the problem easier than it looked but was not given to the solver.
- H 2: a promised canonry of Olmütz for a son of the Queen of Poland.
- N 5: DECODE still non-decrypted; no reading found*.
- R 2: Tomokiyo's transcription only.
- F 2: Tomokiyo entry.
- V 3: every spelled word reads; ten word codes and three groups glossed from context; addressee inferred.
- 0.75 + 0.50 + 1.00 + 0.20 + 0.20 + 0.30 = **2.95**

**11. Richelieu → M. de Rancé, 1629**
- D 4: homophonic alphabet plus nomenclature recovered ciphertext-only from a short text; clean cryptanalysis.
- H 3: Richelieu's own instructions in 1629; of interest, already used by historians since Avenel.
- N 1: printed word for word by Avenel in 1858.
- R 2: Tomokiyo's transcription; the Avenel match found afterwards.
- F 2: Tomokiyo entry.
- V 5: agrees word for word with the 1858 print.
- 1.00 + 0.75 + 0.20 + 0.20 + 0.20 + 0.50 = **2.85**

**12. Charles I and Nicholas → Boswell, 1643**
- D 2: the alphabet was solved by R. Pitt; this repo verified it (z = 9.6) and added the four word-signs.
- H 3: the King's letter to the Duke of Courland's envoy; Nicholas on the Dutch embassy of 1644.
- N 3: Pitt's reading is weeks old; the word-signs and addressee are new here.
- R 3: re-credentials traced to Simpson's 1893 print; the addressee identified.
- F 2: Tomokiyo entry.
- V 3: read in substance; a dozen single-occurrence codes open and the transcription needs the folios.
- 0.50 + 0.75 + 0.60 + 0.30 + 0.20 + 0.30 = **2.65**

**13. Sir Richard Forster, 13 May 1644**
- D 3: a mixed homophonic alphabet recovered blind, 31 of 34 symbols from 207 tokens, six controls read; good method on a small text.
- H 2: the content is not remarkable.
- N 1: already read by Lasry, Biermann and Pitt before this work.
- R 2: transcription only; four slips need the manuscript.
- F 2: Tomokiyo entry.
- V 4: permutation control z = 8.8; three symbols short of the full alphabet.
- 0.75 + 0.50 + 0.20 + 0.20 + 0.20 + 0.40 = **2.25**

**Sensitivity.** Three other weightings, same scores. With novelty dropped and its weight given to D and H (0.35 each): Ségur 4.25, Sun Yat-sen 3.70, Lucca 3.60, Feuquières 3.45, Richelieu 3.35, Ormonde 3.10, Urquhart 3.05, Catinat 1691 3.00, Huang Xing 2.90, Forster and Boswell 2.55, Armstrong 2.50, Warsaw 2.45. Richelieu climbs to fifth and Catinat 1691 falls to eighth, because both are carried by novelty in opposite directions. With list profile raised to 0.30 at the expense of D and H (0.15 each): Ségur 3.85, Urquhart 3.65, Sun Yat-sen 3.50, Lucca 3.40, Ormonde 3.30, Feuquières 3.25, Armstrong 3.10, Catinat 1691 3.00, Huang Xing 2.90, Warsaw 2.85, Richelieu and Boswell 2.55, Forster 2.15. Urquhart is the only item fame moves far. With all six axes equal (1/6 each): Ségur 4.17, Sun Yat-sen 3.67, then Urquhart, Ormonde, Lucca and Feuquières tied at 3.50, Catinat 1691 and Armstrong 3.33, Huang Xing 3.17, Warsaw and Richelieu 2.83, Boswell 2.67, Forster 2.33. Ségur is first and Forster last under every weighting tried; Sun Yat-sen is second in three of four; the middle six reorder freely.

## What this ranking does not settle

- **Novelty marked *:** "no earlier reading" means none was found in the printed editions, catalogues and
  DECODE records the notes cite. An archive decipherment sheet could exist for any of them, as it did for
  Richelieu. Confirming it would take the DECODE record and the archive's own finding aid for each.
- **Historical weight** is judged from the plaintext as read. For Ségur, Warsaw and Lucca the word-signs
  and names still open could raise or lower it.
- **Difficulty** compares finished work. Items closed as unsolved (SP 53, Ottobon, BLUME) were
  harder than anything here and are ranked in the tracker, not on this page.

Checked: every row against the Solved, Explained and Found-solved tables of README.md and the tracker rows of
TARGETS.md as of commit d1abee8; the five provisional rows against SOLVED_CATALOGUE.md and the per-target NOTES on 17 Sept 2026. Not checked: the per-target NOTES.md for facts beyond those tables; whether any
"first reading" has a prior in an archive finding aid. User must verify: the axis scores and weights, which are
editorial.


Nicholas Throckmorton (BL Add MS 4136, 1560–63; catalogue 88): **prior solution verified, unranked**, 20 Sept 2026. Two archive-key samples (42 tokens) and a twenty-record edition concordance; not counted as twenty new solves or a full transcription. See [evidence and limits](throckmorton/RESULT.md).

Sir Thomas Smith → Cecil and Elizabeth I (BL Add MS 4136 ff. 157–168, DECODE R9248–R9254, 1563–66; catalogue 89): **read at the time, re-read with the archived key, unranked**, 21 Sept 2026. Eighteen letters' cipher passages (Forbes's copies) read with Smith's key, Add MS 4136 f. 179 (DECODE R9261); the 1563 ones match Forbes's 1741 print, the 1564–66 ones were only summarised in CSP Foreign. R9236 (f. 140, catalogue 94, 21 Sept 2026) adds five letters of Oct 1562–Nov 1563 in the same key: four read and checked against Forbes/CSP; the 31 Jan 1563 advertisements fragmentary. [Write-up](https://dbourdeau.github.io/cyphersolver/smith1562.html).

Egmond provisional score: 0.25×4 + 0.25×3 + 0.20×2 + 0.10×3 + 0.10×2 + 0.10×3 = **2.95**.

Groffey provisional score: 0.25×1 + 0.25×4 + 0.20×5 + 0.10×4 + 0.10×1 + 0.10×3 = **3.05**.

De Swart provisional score: 0.25×2 + 0.25×3 + 0.20×5 + 0.10×4 + 0.10×1 + 0.10×3 = **3.05**.

Van Reede provisional score: 0.25×2 + 0.25×3 + 0.20×4 + 0.10×3 + 0.10×2 + 0.10×3 = **2.85**.

Alessandrino provisional score: 0.25×3 + 0.25×3 + 0.20×3 + 0.10×4 + 0.10×1 + 0.10×3 = **2.90**.

Alessandrino 1567 provisional score (p80): 0.25×3 + 0.25×3 + 0.20×3 + 0.10×4 + 0.10×1 + 0.10×3 = **2.90**, as its 1568 sibling.

Hernán Núñez provisional score: 0.25×1 + 0.25×3 + 0.20×2 + 0.10×3 + 0.10×1 + 0.10×4 = **2.20**. It sits at the foot of the provisional rows (p48): margins and a sibling key left little to break.

Ralph Boswell provisional score: 0.25×1 + 0.25×2 + 0.20×2 + 0.10×1 + 0.10×1 + 0.10×3 = **1.65**.

Salinas/Ronquillo provisional score: 0.25×1 + 0.25×3 + 0.20×3 + 0.10×3 + 0.10×1 + 0.10×3 = **2.30** (p50).
Sauli and Riario provisional score: 0.25×1 + 0.25×3 + 0.20×2 + 0.10×3 + 0.10×1 + 0.10×4 = **2.20**.
Pápai provisional score: 0.25×1 + 0.25×3 + 0.20×4 + 0.10×3 + 0.10×1 + 0.10×4 = **2.60** (p52), level with the other archive-key readings.

Bremen provisional score: 0.25×2 + 0.25×2 + 0.20×3 + 0.10×3 + 0.10×1 + 0.10×3 = **2.30** (p53): the glosses did most of the work.
Mâcon 1536–37 provisional score: 0.25×1 + 0.25×4 + 0.20×3 + 0.10×3 + 0.10×1 + 0.10×3 = **2.50** (p54).
Hentér 1707 provisional score: 0.25×1 + 0.25×2 + 0.20×3 + 0.10×1 + 0.10×1 + 0.10×3 = **1.85** (p55): the plaintext was already on the leaf.
Como to Dandini 1580 provisional score: 0.25×2 + 0.25×3 + 0.20×2 + 0.10×3 + 0.10×1 + 0.10×4 = **2.30** (p56): the leaf carried the plaintext; the new work was the R72 letter key.
Orange prince c. 1795 (R1892) provisional score: 0.25×3 + 0.25×3 + 0.20×5 + 0.10×4 + 0.10×1 + 0.10×3 = **3.30** (p57): a ciphertext-only break of an unknown square.
Windischgrätz 1721 provisional score: 0.25×1 + 0.25×3 + 0.20×2 + 0.10×3 + 0.10×1 + 0.10×3 = **2.10** (p58): the key was on the record; the new work was the transcription.
Heusner 1637 provisional score: 0.25×1 + 0.25×3 + 0.20×1 + 0.10×2 + 0.10×1 + 0.10×3 = **1.80** (p59): already in print; the new work was the duplicate record and the date.
Cobham at Ostend 1588 provisional score: 0.25×3 + 0.25×3 + 0.20×4 + 0.10×4 + 0.10×1 + 0.10×3 = **3.10** (p60): a cipher broken from its clear context and read.
Basle to William V 1796 (R2234) provisional score: 0.25×1 + 0.25×3 + 0.20×4 + 0.10×2 + 0.10×1 + 0.10×4 = **2.50** (p61): an archive key applied once the line cycle was found.
Rákóczi letters 1706–11 provisional score: 0.25×2 + 0.25×3 + 0.20×4 + 0.10×3 + 0.10×1 + 0.10×3 = **2.75** (p62): the R902 key corrected and reused; R483 key rebuilt.
Haga 1620 provisional score: 0.25×1 + 0.25×4 + 0.20×4 + 0.10×3 + 0.10×1 + 0.10×3 = **2.75** (p61): an archive key, but a text nobody had read.
Cobham to Walsingham May–June 1588 provisional score: 0.25×2 + 0.25×3 + 0.20×3 + 0.10×4 + 0.10×1 + 0.10×2 = **2.60** (p63): read in part from a sign inventory built on glossed siblings.
Caprile 1520–21 provisional score: 0.25×3 + 0.25×3 + 0.20×2 + 0.10×4 + 0.10×1 + 0.10×2 = **2.60** (p64): a homophonic key rebuilt from a 2025 crib and applied to two unread letters.
Ferdinand I to Malvezzi 1548 provisional score: 0.25×1 + 0.25×4 + 0.20×3 + 0.10×3 + 0.10×1 + 0.10×3 = **2.50** (p65): an archive key found among the siblings; the work was reading the signs.
Van Reede to William V 1792 provisional score: 0.25×1 + 0.25×2 + 0.20×3 + 0.10×1 + 0.10×1 + 0.10×4 = **1.95** (p66): an archive key on a glossed letter; its news was in lemon juice elsewhere.

Lucini 1767 provisional score: 0.25×1 + 0.25×3 + 0.20×3 + 0.10×2 + 0.10×1 + 0.10×4 = **2.30** (p67): a published key applied to one unread ciphered sentence, with one code corrected.
Wotton 1585 provisional score: 0.25×1 + 0.25×3 + 0.20×3 + 0.10×2 + 0.10×1 + 0.10×4 = **2.30** (p68): catalogued ciphers that turned out to be clear drafts; the work was naming the code numbers.

Charles I → Rupert 1645 provisional score: 0.25×2 + 0.25×4 + 0.20×5 + 0.10×3 + 0.10×1 + 0.10×3 = **3.20** (p69): Lasry's King–Queen key applied unchanged to a letter catalogued as unread.
Walsingham to Wotton 1585 provisional score: 0.25×1 + 0.25×3 + 0.20×2 + 0.10×2 + 0.10×1 + 0.10×2 = **1.95** (p70): clear letters with a name code; the sign words stayed unread.
Paris nunciature Francia 18 provisional score: 0.25×1 + 0.25×3 + 0.20×4 + 0.10×3 + 0.10×1 + 0.10×3 = **2.60** (p71): a misfiled DECODE decryption hid an unread letter; published keys read it.
Wolff 1801 provisional score: 0.25×1 + 0.25×2 + 0.20×3 + 0.10×3 + 0.10×1 + 0.10×4 = **2.00** (p72): the key Wolff sent six weeks later, filed next to the letter, read it at once.
La Guiche 1551 provisional score: 0.25×3 + 0.25×3 + 0.20×5 + 0.10×2 + 0.10×2 + 0.10×2 = **3.10** (p73): a symbol substitution with no decipherment, broken ciphertext-only.
Champagne news-letters 1590 provisional score: 0.25×1 + 0.25×2 + 0.20×4 + 0.10×2 + 0.10×1 + 0.10×2 = **2.05** (p74): a name code with its key bound in, and an alphabetical two-digit key rebuilt from glosses.
Norreys 1567–68 provisional score: 0.25×1 + 0.25×2 + 0.20×3 + 0.10×1 + 0.10×2 + 0.10×2 = **1.85** (p75): a reconstructed key from a printed decipherment reads Forbes's copies of the ciphered words.
Spinelly 1517 provisional score: 0.25×2 + 0.25×3 + 0.20×4 + 0.10×2 + 0.10×2 + 0.10×3 = **2.75** (p76): a short symbol substitution read from a clear-text crib.
Edmondes to Burghley 1592–94 provisional score: 0.25×2 + 0.25×3 + 0.20×4 + 0.10×2 + 0.10×2 + 0.10×2 = **2.65** (p77): a symbol substitution read from the clear text around it.
Stosch–Walton instructions c. 1731 provisional score: 0.25×1 + 0.25×1 + 0.20×2 + 0.10×1 + 0.10×3 + 0.10×4 = **1.70** (p78): an instruction sheet whose worked example carries its own decipherment.
Lope Hurtado 1523–24 provisional score: 0.25×3 + 0.25×3 + 0.20×4 + 0.10×2 + 0.10×2 + 0.10×2 = **2.90** (p79): a changed key rebuilt from one bound clear, six letters read in part.
Castelcicala 1816–23 provisional score: 0.25×3 + 0.25×3 + 0.20×4 + 0.10×2 + 0.10×2 + 0.10×2 = **2.90** (p80): a syllabic code rebuilt from four glossed letters, half the groups valued.
Schaeblin to Jones 1753 provisional score: 0.25×1 + 0.25×1 + 0.20×1 + 0.10×1 + 0.10×3 + 0.10×4 = **1.50** (p81): a clear letter about making a cipher, catalogued as a cipher.
Visconti 1727 provisional score: 0.25×1 + 0.25×1 + 0.20×2 + 0.10×1 + 0.10×3 + 0.10×4 = **1.70** (p82): a catalogued letter that is the Deciphering Branch's key.

Eichel 1758 provisional score: 0.25×2 + 0.25×1 + 0.20×3 + 0.10×1 + 0.10×3 + 0.10×3 = **1.95** (p83): a cipher sheet made only of nulls and blank cells of key R596.
Ayala to Cisneros 1516 provisional score: 0.25×1 + 0.25×3 + 0.20×1 + 0.10×2 + 0.10×1 + 0.10×2 = **1.70** (p84): a Non-decrypted DECODE letter read with a published sibling key, then found printed in 1875; novelty lowered from 5 to 1 on 21 Sept 2026.
Prince Frederick 1795 (R2242) provisional score: 0.25×1 + 0.25×3 + 0.20×5 + 0.10×3 + 0.10×1 + 0.10×3 = **2.70** (p85): the R1892 key read it unchanged.
Hereditary Prince 1796 (R2239) provisional score: 0.25×4 + 0.25×3 + 0.20×3 + 0.10×3 + 0.10×2 + 0.10×4 = **3.25** (p86): a word-list code rebuilt from its sibling's decipherment, then completed with a printed crib.
Needham 1587 provisional score: 0.25×2 + 0.25×3 + 0.20×4 + 0.10×2 + 0.10×2 + 0.10×1 = **2.55** (p87): a three-grid pigpen rebuilt from four contemporary glosses.
Throckmorton 10 July 1559 provisional score: 0.25×2 + 0.25×3 + 0.20×5 + 0.10×2 + 0.10×2 + 0.10×3 = **2.95** (p88): an unprinted letter read with a published key, corrected.
KAA 4591 (Bavarian key volume, 1529–1583) provisional score: 0.25×4 + 0.25×3 + 0.20×5 + 0.10×3 + 0.10×3 + 0.10×5 = **3.85** (p89): fourteen ciphertexts, twelve read or broken, most only in part.
Lebel to Savoy 1593 provisional score: 0.25×2 + 0.25×4 + 0.20×4 + 0.10×3 + 0.10×2 + 0.10×4 = **3.20** (p90): three unread letters read (≈97% of tokens) with a published key and harvested codes.
Caracciolo 14 Nov 1537 provisional score: 0.25×1 + 0.25×3 + 0.20×3 + 0.10×2 + 0.10×1 + 0.10×1 = **2.00** (p91): a published key read unchanged, past the four lines already read online.

Unsigned cipher slip, Brussels 1721 (DECODE R24, colonia1721): not ranked. Already read by Lasry and Bonavoglia on the DECODE record; only three key values added here.

Campeggio's conclave articles c. 1534 provisional score: 0.25×2 + 0.25×4 + 0.20×3 + 0.10×2 + 0.10×2 + 0.10×3 = **2.80** (p92): the unpublished second page of a letter Lasry half-read, read with his key.
Bizozola to Maximilian Sforza provisional score: 0.25×1 + 0.25×3 + 0.20×4 + 0.10×2 + 0.10×2 + 0.10×4 = **2.60** (p93): a published key applied to an unread letter, all four pages read.
Mantua to Nevers 1590 provisional score: 0.25×1 + 0.25×3 + 0.20×4 + 0.10×2 + 0.10×1 + 0.10×3 = **2.45** (p94): an archive key applied unchanged to an unread letter, read in part.
Mondoucet provisional score: 0.25×4 + 0.25×3 + 0.20×4 + 0.10×4 + 0.10×1 + 0.10×2 = **3.25** (p95): a hand-built key from the volume's own crib; the 1573 passage later found in Didier's edition.
Bay to Rákóczi 1706 provisional score: 0.25×2 + 0.25×3 + 0.20×4 + 0.10×3 + 0.10×1 + 0.10×4 = **2.85** (p96): an unlinked archive key identified by scoring and applied unchanged, read end to end.
D'Ewes's cipher log 1635–36 provisional score: 0.25×3 + 0.25×2 + 0.20×4 + 0.10×3 + 0.10×1 + 0.10×4 = **2.85** (p97): a private invented alphabet rebuilt by crib, read 96.5%.
Stafford August 1586 provisional score: 0.25×3 + 0.25×2 + 0.20×4 + 0.10×3 + 0.10×1 + 0.10×4 = **2.85** (p99): a key rebuilt from sibling letters' decipherment, applied to an unread postscript.
KAA 4591 letters 1531–37 provisional score: 0.25×4 + 0.25×3 + 0.20×4 + 0.10×3 + 0.10×1 + 0.10×3 = **3.25** (p100): Łaski's key adapted, two homophonic keys rebuilt from glosses, read 99.5%, 95.3% and 91.3%.
Stafford November 1586 provisional score: 0.25×1 + 0.25×1 + 0.20×4 + 0.10×3 + 0.10×1 + 0.10×4 = **1.95** (p101): one cipher word read with a sibling key.
Van Swieten to Cobenzl 1757–59 provisional score: 0.25×5 + 0.25×3 + 0.20×4 + 0.10×3 + 0.10×1 + 0.10×4 = **3.60** (p102): an alphabetical syllabary rebuilt from ciphertext alone, read 96%.
Reade to his cousin 1641 provisional score: 0.25×2 + 0.25×3 + 0.20×4 + 0.10×3 + 0.10×1 + 0.10×3 = **2.60** (p103): an archive key reconstruction applied to an unread letter, read in part.
Letter to the King, fr. 3029 f. 134 provisional score: 0.25×1 + 0.25×3 + 0.20×4 + 0.10×3 + 0.10×1 + 0.10×4 = **2.35** (p104): a published key applied unchanged to an unread letter, read end to end.
Guise to Mercœur 1587 provisional score: 0.25×2 + 0.25×3 + 0.20×4 + 0.10×3 + 0.10×1 + 0.10×4 = **2.60** (p105): a published key, extended, read an unread letter end to end.
