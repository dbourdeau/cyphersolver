"""Builds candidates.json and key_leads.json for the Hungaricana sweep of 14 Nov 2026.

Source: the Hungaricana 'Becsi segedletek' (Vienna inventory, HHStA copies held by the Bécsi Magyar Levéltári
Kirendeltség) regests, harvested in a Claude in Chrome tab through the paging route in README.md, plus the
Hungaricana library-side full-text hits (published archival volumes). Every row is scored from regest text only
(seen: catalogue); none viewed. Regest ids are the numbers in archives.hungaricana.hu/hu/lear/BecsSeg/<id>/.
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = 'Hungaricana (archives.hungaricana.hu/hu/lear/BecsSeg, Vienna inventory regests), sweep of 14 Nov 2026'
SCORE = ('Scored from the Hungaricana regest text (Ugyleiras field) during the 14 Nov 2026 Hungaricana sweep '
         '(research/sweep_2026-11-14_hungaricana/); the leaf pages and images were not viewed')
PRIOR = ('open as far as checked (14 Nov 2026): known.py on the correspondent names and shelfmark finds no catalogue or '
         'lead row for this run (overlaps named in "status"); no web, Tomokiyo, DECODE or Lasry search made in this sweep')
ACCESS = ('regest only on Hungaricana (content provider Becsi Magyar Levéltári Kirendeltség); no images online; '
          'reproduction order from HHStA Wien (Haus-, Hof- und Staatsarchiv) needed, or a reading-room visit')

R = []


def bs(i, label):
    return {'href': 'https://archives.hungaricana.hu/hu/lear/BecsSeg/%s/' % i, 'label': label}


def add(**kw):
    kw.setdefault('source', SRC)
    kw.setdefault('score_note', SCORE)
    kw.setdefault('prior_art', PRIOR)
    kw.setdefault('seen', 'catalogue')
    kw.setdefault('needs_archive_scan', 'yes')
    kw.setdefault('access_note', ACCESS)
    R.append(kw)


LEAD_NOTE = ('Hungaricana regest wording: "sifrir" = a cipher text; "sorkozben feloldva" = contemporary interlinear '
             'decipherment on the same sheet; "kulon lapon feloldva" = decipherment on a separate sheet; "nincs feloldva" '
             '/ "feloldas nelkul" = no decipherment filed. ')

# ---------------------------------------------------------------- Konstantinopel, Tuerkei I Kt. 5-28 (1541-72)
add(year=1565, date='Apr 1562 - 1569 (Kt. 16-25)', language='Latin (some German, Italian)', region='Other',
    period='1560-1589',
    title="Albert de Wyss, imperial resident at Constantinople -> Ferdinand I, then Maximilian II: ciphered despatches 1562-69 (155 regests)",
    correspondents='Albert de Wyss -> Ferdinand I (1562-64) and Maximilian II (1564-69)',
    place='Constantinople', shelfmark='ÖStA HHStA Wien, Staatenabteilungen, Türkei I, Kt. 16-25 (Konv. as listed in the Hungaricana regests)',
    folio_note='155 regests name Wyss and a cipher: 117 say "sorkozben feloldva" (interlinear decipherment) and 17 say "nincs feloldva" (no decipherment, mostly duplicates and a few originals), e.g. ids 44944 (11 Feb 1564), 44956 (15 Mar 1564), 45199 (8 May 1565), 45536 (31 Aug 1566), 45649/45656 (Feb 1567), 45823 (11 Aug 1567); wholly ciphered pieces are marked in 45127, 45135 and 45098 (Nov 1564)',
    cls='A',
    status=LEAD_NOTE + 'Nothing in catalogue.json, leads.json or the targets names Wyss (known.py, 14 Nov 2026); lead 1220 starts at Kt. 29 (1573), so the 1562-69 run is not covered. Whether the Wyss cipher changed during the seven years is not stated in the regests.',
    why='The largest uncovered paired run in the Vienna inventory: seven years of one resident\'s despatches, a large majority with the contemporary interlinear decipherment in the same file. A key can be rebuilt from the paired sheets and then applied to the 17 pieces filed without decipherment. One key per correspondent (Wyss); a change of key would show as a break.',
    importance=4, solvability=5, difficulty=2,
    verify='Order Kt. 18 (Jan-Apr 1564) and Kt. 22 (Feb 1567); read one paired and one "nincs feloldva" sheet; check Nehring/Petritsch (Austro-Turcica 1541-1552 is earlier; look for the 1553-1578 volume), Lang 2015 and Lasry for the Wyss cipher; query DECODE for Wyss.',
    links=[bs(45050, 'Kt. 18 Konv. 4, 12 Aug 1564, Wyss to Ferdinand I'), bs(44944, 'Kt. 18, 11 Feb 1564, nincs feloldva'),
           bs(45536, 'Kt. 21, 31 Aug 1566, nincs feloldva')])

add(year=1571, date='Mar 1570 - Nov 1572 (Kt. 26-28)', language='Latin (some Italian)', region='Other', period='1560-1589',
    title="Carolus (Karl) Rym, imperial resident at Constantinople -> Maximilian II: ciphered despatches 1570-72 (about 75 regests)",
    correspondents='Carolus Rym -> Maximilian II (once to Johann Trautson)', place='Constantinople',
    shelfmark='ÖStA HHStA Wien, Staatenabteilungen, Türkei I, Kt. 26-28 (Konv. as listed in the Hungaricana regests)',
    folio_note='about 75 regests name Rym and a cipher, 12 of them "nincs feloldva" (ids 46741, 46529, 46398, 46351, 46680, 46667, 46408, 46719, 46410, 46717, 46413 and 46665/46723 for letters of other senders in the same volume); wholly ciphered pieces 46735, 46714, 46628, 46702 (maybe Ungnad and Provisionali); 46523 "only XVIII can be read out"',
    cls='A',
    status=LEAD_NOTE + 'Lead 1220 covers Rym only from 1573 (Kt. 29-30, 1573-74, with the deciphered pieces C.Ryu.01-08 in Lang); the 1570-72 run (Kt. 26-28) has no row. Same key as the 1573-74 Rym pieces is likely but not stated; a key held for 1573-74 would test it.',
    why='Interlinear decipherments for most of three years plus 12 unresolved originals and several wholly ciphered pages; the preceding run to catalogue lead 1220, so a key rebuilt here may carry over to 1573-74.',
    importance=4, solvability=5, difficulty=2,
    verify='Compare with the 1573-74 Rym pieces (Lang C.Ryu.*) and targets/ungnad1576 notes; order Kt. 27 (Sep-Oct 1570) and Kt. 28 (Jul-Sep 1572).',
    links=[bs(46348, 'Kt. 26, Rym to Maximilian, interlinear'), bs(46741, 'Kt. 28, 28 Sep 1572, nincs feloldva'),
           bs(46735, 'Kt. 28, wholly cipher, only the date solved')])

add(year=1558, date='Mar 1555 - Dec 1562 (Kt. 11-16)', language='Latin (some Italian, German)', region='Other', period='1497-1559',
    title="Augerius Ghislain de Busbecq -> Ferdinand I: ciphered despatches from Constantinople 1555-62 (53 regests)",
    correspondents='Augerius (Ogier Ghiselin de) Busbecq -> Ferdinand I', place='Constantinople / Amasya',
    shelfmark='ÖStA HHStA Wien, Staatenabteilungen, Türkei I, Kt. 11-16 (Konv. as listed in the Hungaricana regests)',
    folio_note='53 regests, 51 with "sorkozben feloldva"; none flagged unresolved; id 43971 (Kt. 11, 1555) is "csupa sifrir" (all cipher). Examples ids 44414 (6 Aug 1559), 44189 (17 Aug 1557)',
    cls='B',
    status=LEAD_NOTE + 'Catalogue 501 holds only the Amasya letter of 1555 (11-5-25); the Busbecq Paris reports 1581-88 (NLA Wolfenbuettel) are a different run. No row for the 1555-62 Constantinople series. The regests all report an interlinear decipherment, so the open question is the cipher itself, not the content.',
    why='Fifty-one paired sheets from a famous correspondent; useful for the cipher history of the Habsburg embassy before Wyss.',
    importance=4, solvability=4, difficulty=2,
    verify='Compare with the Busbecq letters printed in his Epistolae and with Austro-Turcica for the earlier period; order Kt. 13 (1557) and Kt. 14 (1559).',
    links=[bs(44414, 'Kt. 14 Konv. 3, 6 Aug 1559'), bs(44189, 'Kt. 13 Konv. 2, 17 Aug 1557'), bs(43971, 'Kt. 11, all cipher')])

add(year=1554, date='1553 - 1555 (Kt. 10-12)', language='Latin', region='Other', period='1497-1559',
    title="Ferenc Zay (with Antal Verancsics) -> Ferdinand I: ciphered reports from the Porte 1553-55 (24 regests)",
    correspondents='Ferenc Zay (and Antal Verancsics) -> Ferdinand I', place='Constantinople / Amasya',
    shelfmark='ÖStA HHStA Wien, Staatenabteilungen, Türkei I, Kt. 10-12 (Konv. as listed in the Hungaricana regests)',
    folio_note='24 regests, all "sorkozi feloldassal" (interlinear), ids from 43677, 43684, 43733, 43736 (MHHS IV 249), 43816',
    cls='B', status=LEAD_NOTE + 'Printed in part in Monumenta Habsburgica Hungariae (MHHS IV) per the regest; catalogue 501 is the 1555 Amasya letter without decipherment, a different piece.',
    why='Interlinear decipherments for a pair of envoys, with a printed edition cited for cross-checking.',
    importance=3, solvability=4, difficulty=2,
    verify='Check MHHS IV (Monumenta Habsburgica Hungariae) pp. cited in the regests for whether the cipher text is printed.',
    links=[bs(43816, 'Kt. 12, Zay to Ferdinand I')])

add(year=1569, date='Sep 1569 - 1570 (Kt. 25-26)', language='Latin', region='Other', period='1560-1589',
    title="Anselm Stöckl, Constantinople -> Maximilian II / Zasius: ciphered letters 1569-70 (12 regests)",
    correspondents='Anselm Stöckl -> Maximilian II (also to Johann Ulrich Zasius)', place='Constantinople',
    shelfmark='ÖStA HHStA Wien, Staatenabteilungen, Türkei I, Kt. 25-26 (Konv. as listed in the Hungaricana regests)',
    folio_note='12 regests, 8 interlinear; ids 46230 (18 Sep 1569, nincs feloldva, 3 duplicates) and 46258 (24 Dec 1569, nincs feloldva); id 46196 "feloldasa" of two letters\' cipher parts',
    cls='C', status=LEAD_NOTE + 'No row elsewhere (known.py "Stockl" no hits).',
    why='Small paired set from a lesser-known correspondent, with two unresolved originals.',
    importance=2, solvability=4, difficulty=2, verify='Order Kt. 25 Konv. (Sep-Dec 1569).', links=[bs(46230, 'Kt. 25, 18 Sep 1569'), bs(46258, 'Kt. 25, 24 Dec 1569')])

add(year=1571, date='1570 - 1572 (Kt. 26-28)', language='Italian / Latin', region='Other', period='1560-1589',
    title="Provisionali and Ungnad (?): ciphered Constantinople letters 1570-72 (8 regests)",
    correspondents='Provisionali -> Maximilian II; "csupa sifrir ... Ungnad es Provisionali" (id 46702)', place='Constantinople',
    shelfmark='ÖStA HHStA Wien, Staatenabteilungen, Türkei I, Kt. 26-28', folio_note='8 regests, 7 interlinear; 46702 wholly cipher',
    cls='C', status=LEAD_NOTE + 'No row elsewhere (known.py "Provisionali" no hits).', why='Small paired set; one all-cipher page.',
    importance=2, solvability=3, difficulty=2, verify='Order Kt. 28 Konv. 1 (1572).', links=[bs(46337, 'Kt. 26, 19 Jun 1570'), bs(46702, 'Kt. 28, all cipher')])

add(year=1560, date='1556 - 1565 (Kt. 12-20)', language='Latin / Italian', region='Other', period='1497-1559',
    title="Michael Czernovich (Cernovic), Constantinople -> Ferdinand I / Maximilian II: ciphered letters 1556-65 (10 regests)",
    correspondents='Michael Czernovich -> Ferdinand I / Maximilian II', place='Constantinople',
    shelfmark='ÖStA HHStA Wien, Staatenabteilungen, Türkei I, Kt. 12-20', folio_note='10 regests, 6 interlinear; id 45249 (11 Jul 1565) duplicate nincs feloldva; also 44093, 44098',
    cls='C', status=LEAD_NOTE + 'No row elsewhere (known.py "Czernovich" no hits).', why='Small spread-out set from a dragoman/envoy across a decade.',
    importance=2, solvability=3, difficulty=2, verify='Order Kt. 20 Konv. 1 (Jul-Sep 1565).', links=[bs(45249, 'Kt. 20, 11 Jul 1565')])

add(year=1550, date='1549 - 1550 (Kt. 8-9)', language='Latin / Italian', region='Other', period='1497-1559',
    title="Giovanni Maria Malvezzi, Constantinople: the Kt. 8-9 ciphered despatches 1549-50 beyond the ones in leads 891/892 (17 regests, Austro-Turcica pages cited)",
    correspondents='Giovanni Maria Malvezzi <-> Ferdinand I, Charles V; Sultan Suleyman letters in ciphered copy',
    place='Constantinople / Vienna', shelfmark='ÖStA HHStA Wien, Staatenabteilungen, Türkei I, Kt. 8-9 (Konv. 2)',
    folio_note='17 regests naming Malvezzi (11 interlinear, none unresolved), 30 more citing "Nehring" pages 418-571 (Austro-Turcica 1541-1552); ids 43471, 43485, 43483, 43498, 43394',
    cls='C', status=LEAD_NOTE + 'Leads 891 and 892 and targets/malvezzi1548 cover the 1548 and spring-autumn 1550 pieces; this row is the remainder of Kt. 8-9. The Austro-Turcica edition (Munich 1995) prints many with the decipherment; not opened.',
    why='Extends the Malvezzi key (targets/malvezzi1548) with more interlinear pairs.',
    importance=3, solvability=4, difficulty=2, verify='Match ids against lead 891/892 shelfmarks (8-2-22, 8-2-24, 8-3-10); check Austro-Turcica pp. 418-571.',
    links=[bs(43471, 'Kt. 8-9, Malvezzi to Charles V'), bs(43394, 'Kt. 8 Konv. 2, 25 Mar 1550')])

# ---------------------------------------------------------------- Ungarische Akten
add(year=1670, date='Mar 1668 - Sep 1670', language='Latin', region='Central Europe', period='1651-1700',
    title="Fr. Nicolaus Donellan O.Aug. -> Ferenc Nadasdy: the whole run of Latin ciphered letters with separate decipherment, 1668-70 (about 30 regests)",
    correspondents='Fr. Nicolaus Donellan O.Aug. -> Count Ferenc Nadasdy', place='unknown / Vienna',
    shelfmark='ÖStA HHStA Wien, Ungarische Akten, Specialia, Verschwörerakten IV (Nádasdysche Akten), Fasc. 311 Konv. C, 312 Konv. B, 313 Konv. A-B',
    folio_note='regests "orig. latin sifrir es kulon feloldasa" for Aug 1669 (146676, 146677) and Mar-Aug 1670: 146696, 146698, 146700, 146702, 146706, 146707, 146708, 146712, 146714, 146718, 146719, 146722, 146725, 146726, 146727, 146728, 146732-146734, 146739; 146748 (29 Aug 1670) "reszben sifrir nincs feloldasa"; 146623 (24 May 1668) a further piece',
    cls='A',
    status='Duplicate of lead 1232 (one letter, "no decipherment"): lead 1232\'s own vetting already notes that the Hungaricana series carries a separate decipherment; this row records the size of the run (about 30 letters), which the lead does not. ' + LEAD_NOTE,
    why='A key from a year and a half of one correspondent\'s letters, each with the decipherment on a separate sheet; the one piece without decipherment (146748) is the test.',
    importance=3, solvability=5, difficulty=2, verify='Merge into lead 1232 rather than add a new entry; see its vetting block.',
    links=[bs(146727, 'Fasc. 313 Konv. B, 22 Jul 1670'), bs(146748, 'Fasc. 313 Konv. B, 29 Aug 1670, nincs feloldasa')])

add(year=1659, date='Oct 1658 - Jul 1666', language='Latin / Hungarian', region='Central Europe', period='1651-1700',
    title="Letters to Ferenc Nadasdy (Fasc. 309-310), Latin and Hungarian cipher with separate or interlinear decipherment, 1658-66 (about 16 regests, senders not named in the list view)",
    correspondents='unnamed (regest list truncated) -> Count Ferenc Nadasdy', place='Vienna / Linz',
    shelfmark='ÖStA HHStA Wien, Ungarische Akten, Specialia, Verschwörerakten IV (Nádasdysche Akten), Fasc. 309 Konv. B-C, Fasc. 310 Konv. A-B',
    folio_note='ids 146454, 146455 (27 Nov 1658, Hungarian, interlinear), 146457, 146458, 146461, 146462, 146463, 146464 (Apr 1659), 146500 (24 Jul 1665), 146504 (3 Mar 1666), 146425 (7 Feb 1659, Hungarian, nincs feloldva), 146487/146488 (Oct-Nov 1663, Sztrecseny and Murany, largely cipher, nincs feloldva)',
    cls='B',
    status=LEAD_NOTE + 'The 1663 pair is catalogue 1231 (Wesselenyi to unknown); catalogue 2455 covers a 1659 Hungarian piece. The 1658-59 and 1665-66 pieces have no row. The sender is cut off in the list view and not read.',
    why='Interlinear and separate decipherments for a Hungarian magnate\'s correspondence; the unresolved 1659 and 1663 pieces fit a key rebuilt from the paired ones.',
    importance=3, solvability=4, difficulty=2, verify='Open the leaf pages to name each sender (one key per sender), then match to leads 1231 and 2455.',
    links=[bs(146455, 'Fasc. 309 Konv. B, 27 Nov 1658'), bs(146425, 'Fasc. 309 Konv. A, 7 Feb 1659, nincs feloldva')])

add(year=1669, date='4 Oct 1669', language='Latin', region='Central Europe', period='1651-1700',
    title="Zrinyi papers: Latin letter from Krakow, 4 Oct 1669, with a cipher key 'of at least three different ciphers'",
    correspondents='unnamed (regest) -> Zrinyi circle (Fasc. 296)', place='Krakow',
    shelfmark='ÖStA HHStA Wien, Ungarische Akten, Specialia, Verschwörerakten III (Zrínyische Akten), Fasc. 296 Konv. B (1668-69), fol. 75-83',
    folio_note='id 145344: "orig. latin ... mellekelve hozza titkosirasi kulcs is legalabb harom kulonbozo [...]"; related Fasc. 301 Konv. A (id 145842, Kassa 3 Jun 1670, two ciphered lines with interlinear solution)',
    cls='C', status='No row elsewhere for Fasc. 296 (known.py). Catalogue 1230 is the Fasc. 327 key set, a different file. The regest is truncated, so the sender and the ciphers are unnamed.',
    why='A letter with its key enclosed (three ciphers), from the Zrinyi-Frankopan conspiracy files.',
    importance=3, solvability=4, difficulty=2, verify='Open leaf 145344 for the full regest; order fol. 75-83.', links=[bs(145344, 'Fasc. 296 Konv. B fol. 75-83')])

add(year=1529, date='Feb 1529 - Jun 1529', language='Latin', region='Central Europe', period='1497-1559',
    title="Transylvanian bishop (Kolozsvar / Torda) -> Ferdinand I, ciphered reports with interlinear decipherment, Feb-Jun 1529 (about 8 regests; printed in Schuller)",
    correspondents='bishop (name cut off in the list view; catalogue 2462 names Bishop Gerendi) -> Ferdinand I, also Helytartotanacs (Lieutenancy)',
    place='Kolozsvar / Torda', shelfmark='ÖStA HHStA Wien, Ungarische Akten, Allgemeine Akten, Fasc. 10 Konv. B-C, Fasc. 11 Konv. A-C',
    folio_note='ids 142291 (15 Feb), 142482 (15 May), 142519 (31 May), 142525 (Torda, 1 Jun), 142389 (Kolozsvar, 1 Apr), 142388 (Ragusa?), 142318, 142319, 142344/142345 (spy report, deciphered), 142352 (Constantinople, Zapolya\'s envoy)',
    cls='B', status=LEAD_NOTE + 'Catalogue 2235/2457-2462 cover single 1529-30 pieces of Fasc. 10-16; this row is the Fasc. 10-11 run. Several regests cite "Schuller, Archiv f. siebenbuergische Landeskunde", so a printed edition exists; whether it prints the cipher text is not checked.',
    why='A run of paired reports from one sender in a short span, with a printed edition for checking.',
    importance=3, solvability=4, difficulty=2, verify='Open leaf pages for the sender; check Schuller in Archiv des Vereins fuer siebenbuergische Landeskunde.',
    links=[bs(142482, 'Fasc. 11 Konv. B, 15 May 1529'), bs(142525, 'Fasc. 11 Konv. C, 1 Jun 1529')])

add(year=1531, date='1530 - 1531', language='Latin', region='Central Europe', period='1497-1559',
    title="Nagyszeben (Hermannstadt) reports on Transylvania, Gritti and the Turkish war -> Ferdinand I, ciphered with interlinear decipherment, 1530-31 (about 14 regests; printed in Schuller)",
    correspondents='unnamed (Szeben authorities / agents) -> Ferdinand I', place='Nagyszeben / Szeben',
    shelfmark='ÖStA HHStA Wien, Ungarische Akten, Allgemeine Akten, Fasc. 15-19',
    folio_note='ids 143145 (1 May 1530), 143189 (1 Jun 1530), 161156 (22 Aug 1530), 164516 (15 Dec 1530), 164660 (11 Mar 1531, Ragusa and Gritti), 164749 (1 May 1531, siege of Vingard and Fogaras), 164752, 164963 and 164962 (28-29 Aug 1531, Brodarics), 165031 (2 Oct 1531), 165115 (12 Nov 1531), 165211',
    cls='B', status=LEAD_NOTE + 'No row elsewhere for Fasc. 15-19 (known.py). Catalogue 2459-2461 are neighbouring single items in Fasc. 10 and 16. Digits-over-letters decipherment ("a szamok folott") is mentioned for some pieces, so a numeric cipher is likely.',
    why='Fourteen paired reports; the regests say the decipherment sits above the numbers, i.e. a number cipher whose key is rebuilt from the pairs.',
    importance=3, solvability=4, difficulty=2, verify='Open leaf pages for senders; check Schuller.', links=[bs(164749, 'Fasc. 17 Konv. E, 1 May 1531'), bs(165031, 'Fasc. 18 Konv. E, 2 Oct 1531')])

add(year=1542, date='May - Oct 1542', language='Latin', region='Central Europe', period='1497-1559',
    title="Frater Georgius (Martinuzzi) -> Ferdinand I: ciphered letters of 1542 from Deva and Nagyvarad (4 regests)",
    correspondents='Frater Georgius Martinuzzi -> Ferdinand I (also to the archbishop of Esztergom)', place='Deva / Nagyvarad',
    shelfmark='ÖStA HHStA Wien, Ungarische Akten, Miscellanea, Fasc. 431 A (Einzuteilende Nachträge 1505-1575) Konv. B (1540-69), fol. 205-207 etc.',
    folio_note='ids 154594 (29 May 1542 Deva), 154600 (17 Sep 1542), 154603 (6 Oct 1542, decipherment on a separate sheet), 154606 (12 Oct 1542, interlinear)',
    cls='C', status=LEAD_NOTE + 'Catalogue 503 holds the 1543 letter (Fasc. 425), and catalogue 885 the 1548 Ibrahim Pasha copies (targets/ibrahim1548 has a key); the 1542 series has no row. One key per correspondent: Martinuzzi is the same hand as in 885.',
    why='Four paired letters that test the Martinuzzi cipher of 1543 and 1548 five years earlier.',
    importance=3, solvability=4, difficulty=2, verify='Check targets/ibrahim1548 key against 154603 and 154606.', links=[bs(154603, 'Fasc. 431 A Konv. B, 6 Oct 1542'), bs(154606, 'Fasc. 431 A Konv. B, 12 Oct 1542')])

add(year=1527, date='May 1527 - Oct 1528', language='Latin / German', region='Central Europe', period='1497-1559',
    title="Ferdinand I's first Hungarian files: ciphered letters from Olomouc, Krakow and Tarnow 1527-28, one with the cipher key sent on 12 Aug 1527 (about 8 regests)",
    correspondents='envoy at Krakow ("probably Laski") -> Ferdinand I; Lower Austrian government; Gianbattista Zuccarini; Logschan',
    place='Olomouc / Krakow / Tarnow / Piotrkow', shelfmark='ÖStA HHStA Wien, Ungarische Akten, Allgemeine Akten, Fasc. 4-9',
    folio_note='ids 141355 (Olomouc, 5 Jun 1527, cipher postscript), 141269 and 141270 (8 May 1527, Zuccarini, cipher and Latin decipherment), 141560 (Krakow, 12 Aug 1527, key sent), 141595 (22 Aug 1527, Lower Austrian government, nincs feloldva, key at hand), 141675 (Krakow, 11 Sep 1527), 141833 (Piotrkow, 10 Dec 1527, cipher additions on a separate sheet), 141936 (Tarnow, 4 Apr 1528), 142153',
    cls='B', status=LEAD_NOTE + 'Catalogue 1234 is Hanns Hofmann 1527 (Fasc. 5 Konv. B, fol. 133, key at 133/3); these are other pieces of the same files. No row for them (known.py).',
    why='The 1527 pieces include a key plus the letter that sends it, so the cipher of 141560 can be tested against 141595 (filed without decipherment).',
    importance=3, solvability=4, difficulty=2, verify='Open leaf 141560 and 141595; check whether 141560\'s key is the one at Fasc. 5 Konv. B fol. 133/3.',
    links=[bs(141560, 'Fasc. 5 Konv. B, 12 Aug 1527'), bs(141595, 'Fasc. 5 Konv. B, 22 Aug 1527')])

add(year=1530, date='18 Sep and 4 Oct 1530', language='Latin / Italian', region='Other', period='1497-1559',
    title="Naples letter of 18 Sep 1530, deliberately misdated, in cipher with decipherment alongside, and a 4 Oct 1530 piece (Tuerkei I Kt. 1)",
    correspondents='unnamed (regest cut off) -> Ferdinand I circle', place='Naples',
    shelfmark='ÖStA HHStA Wien, Türkei I, Kt. 1 Konv. 4 (1530), fol. 64-67 and 68-71',
    folio_note='id 42325 (18 Sep 1530, "titkosirassal es feloldas mellette", deliberately false date) and 42326 (4 Oct 1530, fol. 70-71 "titkosiras ... ehhez keszult [...]")',
    cls='C', status='No row elsewhere for Kt. 1 (known.py). Regest text is cut off, so the sender and the ciphered content are not read.',
    why='Two ciphered pieces of 1530 with decipherment, early in the Turcica series.',
    importance=2, solvability=4, difficulty=2, verify='Open leaf pages.', links=[bs(42325, 'Kt. 1 Konv. 4, 18 Sep 1530'), bs(42326, 'Kt. 1 Konv. 4, 4 Oct 1530')])

add(year=1540, date='21 Nov 1540 and 1540', language='German', region='Central Europe', period='1497-1559',
    title="Hoffinanz Ungarn 1540: German letters from the Szentandras camp and Visegrad, partly ciphered with interlinear decipherment",
    correspondents='unnamed -> Hofkammer (regest cut off)', place='Szentandras / Visegrad',
    shelfmark='ÖStA FHKA Wien, Hoffinanz Ungarn, RN 1, Konv. (fol. 22-23)',
    folio_note='ids 3799 (21 Nov 1540, Szentandras camp) and 3803 (Visegrad, 26 [month cut off] 1540); also id 156600 (Hoffinanz Ungarn 1654.08.14, Kt. 449, fol. 48-49: a six-line cipher writing and a seal) and id 179729 (Hoffinanz Ungarn 1670.12.07, Kt. 528: sending news by courier and in cipher in future)',
    cls='C', status='No row elsewhere for these FHKA items (known.py). Not HHStA but the Finanz- und Hofkammerarchiv inventory, also in the Vienna regests.',
    why='Two interlinear pairs from 1540; the 1654 and 1670 items are cipher mentions to check.',
    importance=2, solvability=3, difficulty=2, verify='Open leaf pages for the sender.', links=[bs(3799, 'Hoffinanz Ungarn RN 1, 21 Nov 1540'), bs(156600, 'Hoffinanz Ungarn 1654')])

add(year=1621, date='3 Dec 1621', language='Latin / German', region='Central Europe', period='1611-1650',
    title="Ferdinand II / Gerhard Questenberg: letter in Poland partly ciphered, with a cipher key ('Chiffrirschluessel Hungarica Nachtrag aus Fasc. 422')",
    correspondents='Ferdinand II and Gerhard Questenberg (signatures) -> Poland', place='Vienna',
    shelfmark='ÖStA HHStA Wien, Ungarische Akten, Miscellanea, Fasc. 422 (Aus der Hofbibliothek 1606-1629) Konv. A, fol. 72-81',
    folio_note='id 153758: "reszben sifrirban II Ferdinand es Gerhard Questenberg alairasaval ... fol. 75-76 sifrirkulccsal (Chiffrirschluessel)"',
    cls='C', status='No row elsewhere for Fasc. 422 (known.py); catalogue 1226/1227 cover Constantinople 1611-31, not this file.',
    why='A partly ciphered 1621 Habsburg letter with its key in the same fascicle.',
    importance=3, solvability=5, difficulty=1, verify='Open leaf 153758; order fol. 72-81.', links=[bs(153758, 'Fasc. 422 Konv. A fol. 72-81')])

add(year=1851, date='25 Mar 1851 (Kossuth) and Dec 1851 (Schwarzenberg)', language='French / Italian', region='Central Europe', period='1801-1900',
    title="Kossuth emigration: ciphered French text to Karoly Barics, Belgrade, 25 Mar 1851, with Kossuth's own interlinear decipherment (printed), and the Kossuth-Mazzini key 1849-51",
    correspondents='Lajos Kossuth -> Karoly Barics (Belgrade); Kossuth and Mazzini (alleged correspondence)', place='Italy / Belgrade',
    shelfmark='Straub, A Kossuth-emigracio olaszorszagi kapcsolatai (MOL kiadvanyai II/34), Dokumentumok p. 138ff, 25 Mar 1851; ÖStA HHStA, Ministerium des Äußern, Informationsbüro A-Akten 7657 (id 62045, Kossuth/Mazzini key 1849-51)',
    folio_note='the printed document text: original fair copy Italian, the ciphered part with Kossuth\'s decipherment above; id 65502 (Kabinettsarchiv, Acta secreta, Nachlass Schwarzenberg Karton 9, 8 Dec 1851): "the ciphered letter was deciphered"',
    cls='C', status='Prior art: the printed volume gives the decipherment (digital in Hungaricana library, MolDigiLib_MOLkiadv2_34). Not in the catalogue (known.py "Barics", "Kossuth" cipher no hit). Whether the cipher text is printed in full is not checked.',
    why='A mid-19th-century Kossuth cipher whose decipherment is printed and whose key sheet is catalogued in Vienna; also Kossuth-Mazzini key id 62045.',
    importance=3, solvability=4, difficulty=2, verify='Open the Hungaricana library PDF at p. 138ff; for 62045 order the Informationsbuero file.',
    links=[bs(62045, 'MdAe Informationsbüro A-Akten 7657, Kossuth/Mazzini key'), {'href': 'https://library.hungaricana.hu/hu/view/MolDigiLib_MOLkiadv2_34/', 'label': 'Straub, Kossuth-emigracio (Hungaricana library)'}])

with open(os.path.join(HERE, 'candidates.json'), 'w', encoding='utf8') as f:
    json.dump(R, f, ensure_ascii=False, indent=1)

K = [
    {'title': 'Key sheets "Titkosiraskulcsok, Sifre" in Kt. 28, 1571 (Constantinople embassy)',
     'shelfmark': 'ÖStA HHStA Wien, Türkei I, Kt. 28 Konv. 2 (1571 s.d.), fol. 171-180 (Hungaricana id 46649)',
     'note': 'Key-only item from the Rym years; test against the Rym series (candidate row) and the 1573-74 pieces.'},
    {'title': 'Frangepan, undated drafts in his hand c. 1670: "cipher key" (regest: "not 17 [...]")',
     'shelfmark': 'ÖStA HHStA Wien, Ungarische Akten, Specialia, Verschwörerakten V (Frangepanische Akten), Fasc. 317 Konv. D (id 147009)',
     'note': 'Key-only; Frangepan letters in cipher are not listed in the Hungaricana results, so no ciphertext yet.'},
    {'title': 'Chiffrirschluessel with the 1621 Questenberg letter (Fasc. 422)',
     'shelfmark': 'ÖStA HHStA Wien, Ungarische Akten, Miscellanea, Fasc. 422 Konv. A fol. 75-76 (id 153758)',
     'note': 'Key in the same fascicle as the ciphered letter.'},
    {'title': 'Key to a cipher alphabet of a correspondence between kings, 1528 ("Schluessel zum Geheimschrift Alphabet")',
     'shelfmark': 'ÖStA HHStA Wien, Ungarische Akten, Miscellanea, Fasc. 425 (id 154146)',
     'note': 'Key-only item; the correspondents are cut off in the list view.'},
    {'title': 'Cipher key sent by an envoy from Krakow, 12 Aug 1527',
     'shelfmark': 'ÖStA HHStA Wien, Ungarische Akten, Allgemeine Akten, Fasc. 5 Konv. B (id 141560)',
     'note': 'Key and the letter that sends it; test on id 141595 (22 Aug 1527, no decipherment).'},
    {'title': 'Key list "Titkosiraskulcs 178 Acharenten 179 Asia 180 [...]" with the Rome nuncius Grimaldi letters, 1644',
     'shelfmark': 'ÖStA HHStA Wien, Staatenabteilungen, Türkei I, Kt. 117 Konv. 2 (ids 60888, 60913, 60925)',
     'note': 'Key and Italian cipher copies of 1644; within lead 1229\'s range (Kt. 116-120) but this key and the Grimaldi cipher are not named there.'},
    {'title': 'Rejtjelkulcsok 1848-49 and 1850s: keys made to decipher intercepted papers; Klapka archive cipher keys (17 items 1848 onwards, "Table pour dechiffrer")',
     'shelfmark': 'MNL OL R 117 (Kossuth Lajos) and the Klapka archive (R 125 per Ivanyi 1968 Repertorium); Dávid Zoltán, Gyujtemenyek (Levéltári alapleltárak I), 1526 utáni gyűjtemény',
     'note': 'Found as inventory text in Hungaricana library volumes (MolDigiLib_LevLelt_67, MolDigiLib_LevAlapl_10, MolDigiLib_MOLfondjegy_1996_4); item numbers are not given in the snippets; ciphertexts to match are the Klapka and Eber (lead 1907) letters.'},
    {'title': 'Cipher keys 1758-59 and 1770-98 in a small family fonds (P section, "Rejtjelkulcsok Fasc. XL G No. 72-78" and "szam nelkul")',
     'shelfmark': 'MNL OL P (Bakacs, P szekcio: Kisebb családi és személyi fondok), áttekintő raktári jegyzékek p. 255',
     'note': 'Fonds name not read in the snippet; open MolDigiLib_LevLelt_53 p. 255.'},
    {'title': '18th-century cipher keys in the Danish Kingdom section of the Buda expugnata 1686 guide',
     'shelfmark': 'Buda expugnata 1686. Europa et Hungaria 1683-1718 (BFLV_LF_01_buda_01), Dán Királyság p. 283',
     'note': 'Pointer only; the Danish archive, fonds and shelfmark are not in the snippet.'},
]
with open(os.path.join(HERE, 'key_leads.json'), 'w', encoding='utf8') as f:
    json.dump(K, f, ensure_ascii=False, indent=1)
print(len(R), 'candidates', len(K), 'key leads')
