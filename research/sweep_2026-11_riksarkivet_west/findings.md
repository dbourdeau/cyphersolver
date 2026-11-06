# Running findings (rewritten after each volume)

Sheets: 15 images per volume from image 2 on, **600 px a tile, 3 columns** (`rik_sheet3.py`, `batch.py`); suspects
re-fetched at 900-1200 px (`rik_pick.py`); cipher pages zoomed to 2400-3200 px crops (`rik_zoom.py`) to look for faint
interlinear decipherments. A first pass at 300 px, 6 columns (`rik_sheet.py`) was dropped after Muscovitica 3/b/602: at that
size a page of mixed digit groups and words reads as dense handwriting (image 108 was missed on the 300-px sheet and seen
at 600 px). Every volume below was viewed on the 600-px sheet.

| Volume | Series id | Images | Seen | Verdict |
|---|---|---|---|---|
| Muscovitica 1/26/40 resident Jacob du Moulin 1649-50 | R0003224 | 30 | 600-px sheet | no cipher seen (Dutch/Swedish letters, clear) |
| Muscovitica 1/47/118 commissary Johan Bergenhielm 1698-1700 | R0003203 | 164 | sheet; 62, 96 at 900 px; 99 at 2200 px | no cipher seen (Swedish, clear; specks are show-through) |
| Muscovitica 1/76/538 Stedingk and Skjöldebrand, despatches 1809 | R0000475 | 114 | sheet | no cipher seen (French fair copies, Fredrikshamn peace) |
| Muscovitica 1/55/162 Cederhielm's report 1726 | R0003202 | 40 | 300-px sheet (all pages one fair-copy report) | no cipher seen |
| Muscovitica 1/55/157 Cederhielm to the Kanslipresident and Kanslikollegium 1725-26 | R0003201 | 274 | sheet; 92, 183 at 1100 px | no cipher seen (Swedish, clear) |
| Muscovitica 2/B/1/543 Teusina peace, border commissions 1595-96 | R0003613 | 377 | sheet | no cipher seen |
| Muscovitica 1/16/17 Boije, Horn, De la Gardie: Karl Filip's election as tsar 1613-15 | R0003435 | 173 | sheet; 150 at 2000 px | no cipher seen (German, Swedish; 150 has E.F.D. abbreviations, not code) |
| Muscovitica 3/b/602 commissary Adolf Ebers (Eberschildt), Moscow 1662-66 | R0003225 | 172 | sheet; 100-136 at 600 px; 44, 108 at 1000 px; 106, 108, 121, 138, 160 at 2400 px; 161 at 3200 px | **cipher, glossed**: German letters to the King with long runs of 2-digit groups (dot-separated, 15-95 and 2000) mixed with clear words; German decipherment written above the groups on every page zoomed (108 = Moscow 17 July 1664; 160 = Moscow 18 June 1665). 161 left is a faint duplicate of 160's ciphered page. Cipher also at 81, 103, 115, 124, 133 |
| Muscovitica 1/36/82 resident Johan von Lilienthal 1665-67 | R0000814 | 137 | sheet; 38, 47 at 2400 px | **cipher, glossed**: German letters with dense 2-3 digit code (groups 23-389), German decipherment between the lines (38, 47); cipher also at 11, 29, 65, 74, 83 |
| Muscovitica 1/76/539 Stedingk and Skjöldebrand, peace treaty drafts 1809 | R0000476 | 22 | 300-px sheet, all images | no cipher seen (Swedish/French drafts) |
| Muscovitica 6/638 conference protocols with Prontsichev 1683 | R0003599 | 44 | sheet | no cipher seen (Swedish protocol, fair copy) |
| Muscovitica 1/45/115 envoy Christoffer Kock (von Kochen) 1684-90 | R0003474 | 193 | sheet; 142, 155 at 2400 px | no cipher seen (German and Swedish, clear) |
| Gallica I/A/7/10 Hugo Grotius, embassy papers 1639-41 | R0003228 | 512 | sheet | no cipher seen (French, Latin, German, print; 15 of 512 images only) |
| Gallica I/A/8/11 correspondent Jonas Cling 1651 | R0003223 | 39 | sheet | no cipher seen (French newsletters from Paris) |
| Gallica I/A/11/15 resident Antoine de Courtin, embassy papers 1655-61 | R0003501 | 102 | sheet; 95 at 2400 px | no cipher seen (French, accounts) |
| Gallica I/A/7/8 letters to Hugo Grotius 1635-38 | R0003221 | 298 | sheet | no cipher seen (French, Latin) |
| Gallica I/A/9/12 chamberlain Matthias Palbitzky 1652-54 | R0003229 | 16 | sheet (all) | no cipher seen (French and Latin letters to the Queen) |
| Gallica I/A/7/9 Hugo Grotius, embassy papers 1636-38 | R0003222 | 447 | sheet; 299, 417 at 2400 px | no cipher seen (French drafts and notes, German and Dutch newsletters) |
| Gallica V/531 French embassies' memorials and notes 1738-48 | 40006082 | 325 | sheet | no cipher seen (French fair copies) |
| Gallica I/A/24/54 envoy Carl Bonde (with Lillieroot) 1674-78 | R0003797 | 557 | sheet; 113, 335, 446, 520 at 2400 px | **cipher, glossed**: Swedish despatches to the King with 2-3 digit number code (groups 10-997) between clear words; Swedish decipherment written above every coded run on all four pages zoomed (113, 335, 446 = f. 431, 520); cipher also in the margin of 76 |
| Italica I/5/5 Francesco Piranesi, despatches Jan-July 1797 | R0003430 | 611 | sheet | no cipher seen (Italian and French, print) |
| Italica I/5/6 a Piranesi, despatches Aug-Dec 1797 | R0003394 | 334 | sheet | no cipher seen (French and Italian, translations, print) |
| Italica I/5/4 Piranesi, despatches 1782-96 | R0003429 | 630 | sheet | no cipher seen (Italian, print) |
| Italica I/5/7 a Piranesi, embassy papers 1782-98 (I-IV) | R0003431 | 225 | sheet | no cipher seen (letters to Piranesi from Stockholm, French and Swedish) |
| Italica I/5/7 b Piranesi, embassy papers 1782-98 (V-XII) | R0003432 | 387 | sheet | no cipher seen |
| Italica I/5/6 b Piranesi, despatches Jan-June 1798 | R0003395 | 198 | sheet | no cipher seen (French, print, Roman Republic edicts) |
| Hollandica I/5/7 resident Ludwig Camerarius, letters to the King (and to Johan Skytte) 1626-28, 1630 | R0003234 | 535 | sheet; extra sheets 395-535 and 424-432 at 600 px; 109, 215, 426, 427, 428, 432, 442, 460, 498 at 2400 px; 428 at 3200 px | **cipher, partly bare**: Latin letters with a numeric nomenclator (2-4 digit groups 10-4000, halves such as 1114½, 2106½, single letters t., uu.) mixed with clear Latin. **Glossed** (Latin/German decipherment above): 109, 427, 498; 215 uses a second system (digits run together with signs π, Ψ, ⊠ and letters, `/q`, `/b` suffixes), also glossed. **Bare at 2400 px**: 426 (`Cl. vir, amice singularis`, image 16 of a run), 432 (`S.P. Vir amice obs.`, Sept 1630), 442 (`Serenissime Rex`, a full page of code), 460 (both pages); 428 is bare at 3200 px but is a duplicate of the glossed 427. More cipher letters at 73, 144, 423, 451 (not zoomed) |
| Hollandica I/26/301 envoy Johan Palmquist: letters from von Müllern 1710-15 | 40006086 | 189 | sheet; 152 at 2400 px | **cipher, glossed**: French and Swedish letters with number-code passages (89: `105.141.52.58.66...` with `le Comte de Welling` etc. above; 152: digits run together, `sentera` / `ingere` above). Von Müllern's field-chancery code (compare lead 2257, Bender) |
| Hollandica I/26/305 Palmquist: letters from governor-general Mauritz Vellingk 1711-12 | 40006087 | 817 | sheet | no cipher seen (French and German, clear) |
| Anglica I/26/214 resident Carl Gyllenborg: letters from von Müllern 1711-16 | 40006088 | 153 | sheet; 133 at 2400 px | **cipher, glossed**: Swedish letters with code passages in run-together digits (`216,180141924940...`), Swedish decipherment above (133: `en contre memorialet`, `projectant`, `Hanover`). Same practice as Hollandica 26/301 |
| Anglica Bihang/1 Scotica 1562-1650 | R0003219 | 73 | sheet | no cipher seen (French memorials, Latin royal letters) |
| Anglica IV/521 Parliament and Protectors' original letters 1645-60 | R0003220 | 95 | sheet | no cipher seen (formal Latin letters, Oliver P., Richard P.) |
| Danica 2/a/372 border commission, Trondheim county 1658 | R0003548 | 142 | sheet | no cipher seen (Swedish reports, tables) |
| Danica 2/a/370 Lapland-Norway border papers 1563, 1581-1603 | R0003227 | 384 | sheet | no cipher seen (registers, lists) |
| Germanica B/I/1/3/286 royal instruction for resident Schweder Kleihe 1655 | R0003547 | 21 | sheet (all) | no cipher seen (clear Swedish instruction; no key table) |
| Americana I/2 consuls Hallstedt, Gahn, Söderström 1784-1812 | R0003576 | 368 | sheet | no cipher seen (Swedish and English) |
| Americana I/1 consul Richard Söderström 1786-99 | R0003577 | 300 | sheet | no cipher seen |
| Americana II/5 miscellaneous papers 1783-1805 | R0003578 | 124 | sheet at half scale | no cipher seen (treaty drafts, French and Swedish) |
| Muscovitica 4/616 the tsars' original letters 1560-1649 | R0003534 | 28 | sheet at half scale | no cipher (formal charters) |
| Maroccana I/I lieutenant colonel Abraham von Stauden 1772-75 | R0003619 | 103 | sheet; 76 at 2400 px | **cipher, glossed**: Swedish reports to the Kanslipresident with 3-digit groups written run together with dot/comma marks (groups 180-599); image 76: decipherment written in the line beneath each ciphered line (left page) and above a ciphered run (right page: `bemälte Pass-Toppars förlovande`); two lines on the right page bare, set off by wavy rules |
| Maroccana II/I consul Peter Christian Wulff at Salé 1764-75 | R0003632 | 167 | sheet; extra sheets 3-47 and 48-167; 10, 11, 14 at 700 px; 12 at 3000 px; 13, 18, 24 at 2400 px | **cipher, bare**: Swedish letters with long unbroken digit strings (no separators), as Molinari's Tunis letters (lead 2260). 12 = two full pages of digits, 13 = one page, 11 = two blocks of digit rows, 14, 18, 24 = digit lines between clear lines of the letter. **No decipherment seen** (no writing above or below the digit rows at 2400-3000 px; the clear lines carry on the letter's own text). The same string `4471683745073806223843` stands before `presenterne` in 18 and 24 (a phrase about the peace presents): crib. Cipher seen only in 1764-66 letters (11-24); later letters (48-167) clear |
| Maroccana II/II-IX consul general Johan Magnus Wenström at Tangier 1775-87 | R0003633 | 281 | sheet | no cipher seen (15 of 281 images) |
| Maroccana II/X consul general Peter Wijk at Tangier 1787-1809 | R0003634 | 306 | sheet | no cipher seen (15 of 306 images) |
| Maroccana VII/b letters to and from Swedish missions and consuls 1766-98 | R0003642 | 210 | sheet | no cipher seen (accounts, letters to Wulff) |
| Maroccana I/II lieutenant colonel G. F. Strömfelt 1777 | R0003620 | 75 | sheet | no cipher seen |
| Maroccana I/III major Th. Kullenberg 1777-81 | R0003621 | 36 | sheet | no cipher seen |
| Maroccana I/IV major David Ankarloo 1779-80 | R0003622 | 45 | sheet | no cipher seen |
| Maroccana I/V lieutenant colonel Harald af Christiernin 1782-87 | R0003623 | 87 | sheet | no cipher seen |
| Maroccana I/VI colonel Måns von Rosenstein 1785, 1791 | R0003624 | 31 | sheet at half scale | no cipher seen |
| Maroccana I/VII lieutenant colonel P. G. Lagerstråle 1795 | R0003625 | 12 | sheet at half scale | no cipher seen |
| Maroccana VII/a accounts and memorials, peace presents 1761-65 | R0003641 | 233 | sheet | no cipher seen (accounts) |
| Maroccana VII/c, IX/a, IX/b, X/a, X/b, XI/a, VIII/a (petitions, accounts, drafts, ransom of seamen, convoy office, 1754-80) | R0003643, R0003645, R0003646, R0003647, R0003648, R0003649, R0003644 | 30, 88, 128, 30, 15, 16, 126 | sheets at half scale; IX/a 65 at 2000 px | no cipher seen |
| Stedingk E 6601 (86) drafts of despatches 1805 | 90003447 | 319 | sheet | no cipher (French drafts, St Petersburg). Image 108 is the draft of a `Très-humble Apostille en Chiffre du 24 Mars / 5 avril 1805`: the clear text of a ciphered postscript whose sent form (Muscovitica, not digitised) would be in cipher: crib source |
| Stedingk E 6627 (112) letters to Stedingk 1790-1807, Lachaux-Mörner | 90003529 | 580 | sheet | no cipher seen |
| Stedingk E 6703 (188) papers on the events of 1808-09 | 90003394 | 240 | sheet | no cipher seen (print, orders, copies) |
| Stedingk E 6644 (129) letters to Stedingk 1810-12 | 90003471 | 644 | sheet | no cipher seen |
| Stedingk E 6617 (102) letters from the kings (Gustaf IV Adolf, Carl XIII, Carl XIV Johan, Oscar) 1788-1828 | 90003463 | 216 | sheet | no cipher seen (autograph letters; image 45, Stockholm 28 Jan 1798, mentions a letter sent `tant en chiffre qu'en prose`) |
| Stedingk E 6588 (73) drafts of despatches 1790-91 | 90003434 | 293 | sheet at half scale | no cipher (drafts, incl. clear drafts of apostilles, e.g. 60 `Apostille du Comte Stedingk`, 29 Dec 1790): crib source |
| Stedingk E 6600 (85), E 6604 (89), E 6590 (75), E 6591 (76), E 6592 (77), E 6595 (80), E 6599 (84), E 6603 (88) drafts of despatches and letters 1793-1811 | 90003446, 90003450, 90003436, 90003437, 90003438, 90003441, 90003445, 90003449 | 428, 175, 336, 220, 297, 248, 172, 156 | sheets at half scale | no cipher (French drafts) |
| Stedingk E 6697 (182), E 6680 (165), E 6640 (125) royal letters and commissions, papers on 1788-90, letters from authorities | 90003388, 90003507, 90003542 | 248, 237, 144 | sheets at half scale | no cipher seen |
| Stedingk E 6622 (107), E 6623 (108), E 6628 (113), E 6632 (117) letters to Stedingk 1790-1807 | 90003524, 90003525, 90003530, 90003534 | 578, 659, 486, 656 | sheets at half scale | no cipher seen |
| Stedingk E 6642 (127), E 6643 (128), E 6645 (130) letters to Stedingk 1808-13 | 90003469, 90003470, 90003472 | 482, 248, 312 | sheets at half scale | no cipher seen |
| Stedingk E 6608 (93), E 6609 (94) family letters 1759-1812 | 90003454, 90003455 | 866, 553 | sheets at half scale | no cipher seen |
| Stedingk E 6704 (189) papers on the events of 1812-14 | 90003395 | 402 | sheet at half scale; 162 at 1400 px | no cipher (162 is a corrected French draft, 2 Oct 1813) |
| Stedingk E 6659 (144) consul general G. Sterky, Petersburg 1811-24; E 6709 (194), E 6710 (195) miscellaneous papers | 90003486, 90003400, 90003401 | 222, 543, 430 | sheets at half scale | no cipher seen |
| Stedingk E 6679 (164) Hastfer's papers taken in 1788; E 6585 (70) drafts 1801-06; E 6646 (131) papers 1814; E 6653 (138) Wehrtmann letters 1790-1811 | 90003506, 90003431, 90003473, 90003480 | 225, 274, 224, 214 | sheets at half scale | no cipher seen (136 in E 6679 is a strength return) |
| Stedingk E 6602 (87) drafts 1806-07; E 6624 (109), E 6625 (110) letters 1790-1807; E 6707 (192) mission to Russia 1826 | 90003448, 90003526, 90003527, 90003398 | 392, 569, 484, 208 | sheets at half scale | no cipher seen |
| Stedingk E 6597 (82) drafts 1800; E 6641 (126) letters 1808-09; E 6607 (92) drafts 1824-36; E 6635 (120) letters 1801-05 | 90003443, 90003468, 90003453, 90003537 | 237, 727, 200, 190 | sheets at half scale | no cipher seen |
| Stedingk E 6620 (105) letters Hamilton-Pollett; E 6705 (190) papers 1812-14 (print); E 6735 (220) Tersmeden letters 1816-41; E 6629 (114) letters 1790-1807 | 90003466, 90003396, 90003545, 90003531 | 492, 130, 297, 478 | sheets at half scale | no cipher seen |
| Stedingk E 6630 (115) letters 1790-1807; E 6702 (187) treaties 1790s-1805; E 6598 (83) drafts 1801; E 6647 (132) letters 1812-19 | 90003532, 90003393, 90003444, 90003474 | 474, 163, 274, 397 | sheets at half scale; E 6630 317 at 2000 px | no cipher seen |
| Stedingk E 6605 (90) drafts 1811-20; E 6658 (143) Hasselgren letters 1794-1814; E 6701 (186) border papers 1745-1804; E 6631 (116) letters 1790-1807 | 90003451, 90003485, 90003392, 90003533 | 191, 114, 533, 617 | sheets at half scale | no cipher seen |
| Stedingk E 6639 (124), E 6638 (123) letters from the State Office, supplications 1790-1807; E 6584 (69), E 6586 (71), E 6589 (74) drafts 1792-1809 | 90003541, 90003540, 90003430, 90003432, 90003435 | 306, 183, 295, 275, 221 | sheets at half scale; E 6638 88 at 1600 px | no cipher seen |

## Notes

- `rik_common.img` returns a white tile when a fetch fails three times; a few white tiles on the sheets may be failed fetches
  rather than blank pages (E 6638 image 88 was one: refetched, clear).
- Stedingk volumes were viewed at half scale (300-px tiles, 4 sheets to a composite): enough for whole pages of digits,
  not for a short run of code inside clear text. The Stedingk papers are drafts and letters received; his ciphered
  despatches as sent would be in Diplomatica Muscovitica 1790-1811, which has no digitised volumes for those years.
- known.py (6 Nov): no hit on any shelfmark above. Camerarius matches only the Munich target camerarius1621 and the
  docket on riksarkivet4284; Gyllenborg and Palmquist hits are other documents (the 1717 London affair, stade1710).
