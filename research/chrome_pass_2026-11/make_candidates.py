# Builds candidates.json for the Chrome pass of 2 Nov 2026 (see README.md). Rows were read in the user's Chrome.
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
SZ = 'https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/'
BN = 'https://bnedigital.bne.es/bd/es/card?id='
POL = 'open as far as checked (2 Nov 2026: known.py; one web search on the correspondents found nothing on this cipher; Tomokiyo, Lasry, edition not searched)'
ESP = 'open as far as checked (2 Nov 2026: known.py, Cryptoole snapshot; one web search; Tomokiyo, Lasry, edition not searched)'


def sz(label, *ids):
    return [{'label': f'{label} {i}' if len(ids) > 1 else label, 'href': SZ + str(i)} for i in ids]


def row(year, date, title, corr, place, lang, region, period, shelf, folio, cls, status, why, imp, sol, dif, links,
        seen='catalogue', scan='no', access='scans public on szukajwarchiwach.gov.pl, no login', prior=POL, portal='szukajwarchiwach', **kw):
    note = 'viewed' if seen == 'image' else 'not viewed'
    r = dict(year=year, date=date, title=title, correspondents=corr, place=place, language=lang, region=region,
             period=period, shelfmark=shelf, folio_note=folio, cls=cls, status=status, why=why, importance=imp,
             solvability=sol, difficulty=dif,
             score_note=f'Scored from the {"image" if seen == "image" else "archive description"} during the Nov 2026 Chrome pass (research/chrome_pass_2026-11/); {note}',
             verify=kw.pop('verify', 'View the scans; measure the cipher; look for a decipherment or key in the same fonds.'),
             links=links, seen=seen, source=f'Chrome pass, {portal}', prior_art=prior, needs_archive_scan=scan, access_note=access)
    r.update(kw)
    return r


PL = 'Poland-Lithuania'
NOSCAN = dict(scan='yes', access='catalogue record only; no scans flagged on szukajwarchiwach, AGAD order needed')
R = [
    row(1757, '1757 (dateline on the letter, not read closely)', 'Jan Klemens Branicki → Antoni Potocki, voivode of Bełz: letter mostly in cipher, catalogued unsolved',
        'Jan Klemens Branicki → Antoni Potocki', 'unknown', 'French (clear opening)', PL, '1701-1800',
        'AGAD, Zbiór Anny z Potockich Ksawerowej Branickiej (zesp. 338), 1/338/0/1/446', '5 scans; scan 2 has about 10 lines of letter cipher after 3 clear lines',
        'C', "Catalogue: 'List w większej części szyfrowany nierozwiązany'. Scan 2 viewed: clear French opening, then a neat run of lower-case letters and some digits with no interlinear decipherment.",
        'Hetman Branicki was the head of the anti-Czartoryski party during the Seven Years War; his cipher can open the rest of this fonds.', 4, 5, 2, sz('scans', 28224155), seen='image',
        verify='Transcribe scans 2-5; try a monoalphabetic and small-homophonic solve in French.'),
    row(1750, 'undated (fonds range 1691-1838)', 'Unknown → unknown (one perhaps to Branicka): four letters in cipher, three catalogued unsolved',
        'unknown', 'unknown', 'unknown (no. 1401 partly Polish)', PL, 'unknown',
        'AGAD, zesp. 338, 1/338/0/1/1398, 1399, 1400, 1401', 'scans online; no. 1398 scan 2 is a full page of dense mixed letters and numbers',
        'C', "Catalogue: 'List cyfrowany, nierozwiązany' (1398-1400), 'List cyfrowany, częściowo po polsku, może do Branickiej' (1401). Scan of 1398 viewed; no decipherment on that page.",
        'Whole-page ciphertext in a family archive, explicitly left unsolved by the cataloguer.', 3, 4, 3, sz('no.', 28225111, 28225112, 28225113, 28225114), seen='image'),
    row(1765, '1757-1771', "Letters to Father Betański, partly in cipher: some solved between the lines, some not", 'unknown; Bouden (1757), perhaps Betański → J. K. Branicki (1771)',
        'Wilno (no. 131), others unknown', 'Polish', PL, '1701-1800',
        'AGAD, zesp. 338, 1/338/0/1/128, 130, 131, 143 (no decipherment noted); siblings 129, 132-136, 138, 140-142 (solved)', 'scans online',
        'A', "Catalogue: nos. 135-142 'z interlinearnem rozwiązaniem', 129 'szyfr rozwiązany', 132 'z rozwiązaniem szyfru'; 131 'nierozszyfrowany', 143 'częściowo szyfr nierozwiązany'.",
        'Interlinear siblings give a key directly, which may read the unsolved letters and the Branicki family ciphers.', 3, 5, 2,
        sz('no.', 28223835, 28223837, 28223838, 28223850, 28223842, 28223848), verify='Rebuild the key from the interlinear letters and apply it to 128, 130, 131, 143.'),
    row(1715, '1715', 'Dahku → unknown: part of a letter in cipher, catalogued unsolved', 'Dahku → unknown', 'unknown', 'Polish (clear part)', PL, '1701-1800',
        'AGAD, zesp. 338, 1/338/0/1/682', '5 scans; the one page viewed was the clear part', 'C',
        "Catalogue: 'Część listu pisana szyfrem, nierozwiązanym'. The cipher itself not seen yet.", 'Great Northern War era; the sender is not identified.', 2, 4, 3, sz('scans', 28224391)),
    row(1768, '1768', 'Janowa Branicka (catalogued née Szembek) → unknown: two letters with unsolved cipher', 'Janowa Klemensowa Branicka née Szembek, as catalogued → unknown, perhaps F. K. Branicki',
        'unknown', 'unknown', PL, '1701-1800', 'AGAD, zesp. 338, 1/338/0/1/541, 544', 'scans online', 'B',
        "Catalogue: 541 'List szyfrowany, częściowo nierozwiązany'; 544 'List ma pozycje pisane szyfrem'.", 'Bar Confederation year. The catalogue name needs checking: Branicki was by then married to Izabela Poniatowska.', 3, 4, 3, sz('no.', 28224250, 28224253)),
    row(1757, '1757', 'Beck: letter partly in cipher on political and military events', 'Beck → unknown', 'unknown', 'unknown', PL, '1701-1800', 'AGAD, zesp. 338, 1/338/0/1/83', 'scans online', 'B',
        "Catalogue: 'List częściowo szyfrowany'; no decipherment noted.", 'Seven Years War news in the Branicki circle.', 2, 4, 3, sz('scans', 28223790)),
    row(1713, '1713-1714', "Chomętowski's embassy to the Porte: ciphered letters and reports with their solutions and code", 'A. M. Sieniawski, J. Potocki, Augustus II and others ↔ Stanisław Chomętowski',
        'Poland; Istanbul', 'Polish', PL, '1701-1800', 'AGAD, Archiwum Koronne Warszawskie, 1/3/0/33/79, teczki 542, 545, 591, 601, 602',
        'at least 13 cipher items; solutions nr 881, 1041, 1044, 1057; code nr 1062', 'A',
        "Catalogue: 'Szyfrowany list', 'Kopia szyfrowanego listu', 'Urywek' (nr 902, 970, 1019, 1035, 1040, 1043, 1052, 1053, 1056, 1058, 1060, 1061) beside 'Rozwiązanie szyfru' sheets and 'Kod szyfrowy' (nr 1062). Several letters have no solution listed.",
        'A Polish embassy at the Ottoman court during the Bender crisis, with its own code preserved.', 4, 2, 2,
        sz('nr', 17709747, 17709763, 17709768, 17709769, 17709790), **NOSCAN, verify='Order teczki 601-602 from AGAD; compare nr 1062 with the Sieniawski keys in targets/sieniawski1708 and potocka1714.'),
    row(1711, '1711', 'Unknown → unknown: three ciphered letters on Augustus II and the Porte', 'unknown', 'unknown', 'Polish', PL, '1701-1800',
        'AGAD, Archiwum Koronne Warszawskie, 1/3/0/33/79, teczka 544, nr 884, 885, 887', 'not seen', 'C',
        "Catalogue: 'Szyfrowany list nieznanego nadawcy do nieznanego adresata'; no solution listed.", 'Secret news of the marriage plans of the Saxon prince and the hospodar of Wallachia.', 3, 1, 3, sz('nr', 17709604, 17709605, 17709607), **NOSCAN),
    row(1744, '4 May - 24 Oct 1744', "Franciszek Giuliani, interpreter in Turkey → probably Bishop Załuski: letters in cipher, with cipher tables", 'Franciszek Giuliani → A. S. Załuski (probably)',
        'Turkey', 'Polish or Italian', PL, '1701-1800', 'AGAD, Archiwum Koronne Warszawskie, 1/3/0/33/80, teczki 726-739', 'nr 1381-1389; solutions nr 1377, 1380, 1382, 1384, 1392, 1394; tables nr 1373-1375', 'A',
        "Catalogue: 'Wiadomości polityczne (pisane szyfrem)'. Solution sheets exist for some letters; 1385-1389 appear to have none. Cipher tables (teczka 726) were sent to him from Dresden on 21 Mar 1742.",
        'Polish reporting from the Ottoman court during the War of the Austrian Succession, with its keys.', 3, 2, 2, sz('nr', 17710087, 17710091, 17710092, 17710093, 17710094, 17710095, 17710081), **NOSCAN),
    row(1788, '9 Sept 1788', 'Kajetan Chrzanowski, Polish resident at Constantinople → Department of Foreign Interests: letter in an unsolved cipher', 'Kajetan Chrzanowski → Departament Interesów Cudzoziemskich',
        'Constantinople', 'unknown', PL, '1701-1800', 'AGAD, Archiwum Koronne Warszawskie, 1/3/0/33/80, teczka 758, nr 1443', 'not seen', 'B',
        "Catalogue: 'Pisany nie rozwiązanym szyfrem, zapewne różne wiadomości polityczne'.", 'Russo-Turkish war of 1787-92, at the start of the Four-Year Sejm; the cabinet keys in Zbiór Popielów are candidates.', 4, 1, 3, sz('record', 17710151), **NOSCAN,
        verify='Order the letter; test Zbiór Popielów 450 (Constantinople chiffre).'),
    row(1633, '1 June 1633', 'Officials and citizens of the Smolensk palatinate, besieged in Smolensk → Krzysztof Radziwiłł: ciphered letter', 'Besieged at Smolensk → Krzysztof Radziwiłł, Lithuanian field hetman',
        'Smolensk', 'Polish', PL, '1611-1650', 'AGAD, Archiwum Warszawskie Radziwiłłów (zesp. 354), 1/354/0/2.1/1116', '7 microfilm scans online; the page viewed is the film card, cipher not seen', 'C',
        "Catalogue: 'Szyfrowany list ... zawierający informacje o rozwoju wydarzeń'.", 'Sent out of the city during the Muscovite siege of the Smolensk War.', 5, 3, 3, sz('scans', 29638410)),
    row(1627, '1626-1627', 'Stanisław Radziejowski, voivode of Rawa → Tomasz Zamoyski: three letters apparently in cipher', 'Stanisław Radziejowski → Tomasz Zamoyski', 'unknown', 'Polish', PL, '1611-1650',
        'AGAD, Archiwum Zamoyskich (zesp. 358), 1/358/0/-/363', '16 scans online; the volume holds many letters', 'C',
        "Catalogue: 'w tym trzy listy pi[sane ...]' was cut off in my export; the search term matched cipher, so confirm the wording.", 'Polish-Swedish war in Prussia.', 3, 3, 3, sz('volume', 17916623)),
    row(1659, '23 May 1659', 'Hieronim Pinocci, royal resident → Bishop of Łuck, Crown Chancellor: cipher on the war with Sweden and Muscovy and possible peace', 'Hieronim Pinocci → Mikołaj Prażmowski (the then chancellor; to confirm)',
        'unknown', 'Italian or Polish', PL, '1651-1700', 'AGAD, Archiwum Koronne Warszawskie, 1/3/0/10/38/54', 'not seen', 'C', "Catalogue: 'szyfr w sprawie wojny ze Szwecją i Moskwą'.", 'Peace of Oliva preliminaries.', 4, 1, 3, sz('record', 17707003), **NOSCAN),
    row(1662, 'Aug 1662', 'Unknown → Jerzy Lubomirski: three ciphered letters', 'unknown → Jerzy Sebastian Lubomirski', 'unknown', 'unknown', PL, '1651-1700',
        'Archiwum Narodowe w Krakowie, Archiwum Sanguszków (zesp. 637), 29/637/0/1.3/9071', 'not seen; cat. 441 (Morsztyn → Lubomirski) is the possible sibling', 'B', "Catalogue: 'Lubomirski. List szyfrowany'; '(trzy szyfrowane listy)'.", 'Lubomirski rebellion prelude.', 3, 2, 3, sz('record', 41961320),
        scan='yes', access='unit page shows 0 scans (2 Nov 2026); order from AN Kraków'),
    row(1791, '29 Dec 1791', 'Jan Nepomucen Małachowski, envoy in Saxony → unknown: letter half in cipher on the Polish succession', 'J. N. Małachowski → unknown', 'Dresden', 'unknown', PL, '1701-1800',
        'Archiwum Państwowe w Lublinie, Akta ze zbiorów Muzeum KUL (zesp. 94), 35/94/0/-/32', 'not seen', 'B', "Catalogue: 'list pisany w połowie szyfrem'.", 'The Saxon succession under the 3 May Constitution; the cat. 433 Dresden correspondence is related.', 4, 2, 3, sz('record', 979249),
        scan='yes', access='unit page shows 0 scans (2 Nov 2026); order from AP Lublin'),
    row(1760, 'undated', "Unknown → Forbes, secretary to Crown Treasurer Teodor Wessel: letter partly in cipher", 'unknown → Forbes', 'unknown', 'unknown', PL, 'unknown', 'Archiwum Państwowe w Łodzi, Archiwum rodziny Bartoszewiczów (zesp. 592), 39/592/0/1.7/363', '4 scans online', 'C',
        "Catalogue: 'częściowo pisany szyfrem'.", 'Saxon-era court finance.', 2, 4, 3, sz('scans', 6537648)),
    row(1656, '13 Mar 1656; Dec 1769', 'Radziwiłł archive: ciphered postscript of 1656 and ciphered addition of 1769', 'unknown', 'unknown', 'unknown', PL, 'unknown', 'AGAD, Archiwum Warszawskie Radziwiłłów (zesp. 354), 1/354/0/4/46/16 and 1/354/0/4/261/17', 'two object-level items; the 1656 unit has 76 scans, the item inside it not located', 'C',
        "Catalogue: '\"Post scriptum\" cyfrowane do…', 'dodatek cyfrowany'. Two different ciphers are likely; split if both are worked.", 'The Deluge (1656) and the Bar Confederation (1769).', 3, 2, 3, sz('item', 17873460, 17873661), scan='partly', access='1656 unit: 76 scans on szukajwarchiwach; 1769 unit not checked'),
    row(1787, '1787', 'Antoni Augustyn Deboli → Warsaw: ciphered despatch, numbers and a small French fragment', 'A. A. Deboli → Warsaw', 'St Petersburg', 'French', PL, '1701-1800', 'AGAD, Archiwum Koronne Warszawskie, 1/3/0/2/58/1', 'not seen', 'B',
        "Catalogue: 'same liczby i mały fragment po francusku'. Not the Zbiór Popielów series worked in targets/deboli1788-1791.", 'May be read with the key in targets/deboli1789.', 3, 1, 1, sz('record', 17706097), **NOSCAN, verify='Order it; apply the deboli1788/1789 key.'),
    row(1800, '1771; 1790-1812', "M. T. Tyszkiewiczowa's correspondence, including letters catalogued 'nie rozszyfrowana'", 'various ↔ Maria Teresa Tyszkiewiczowa', 'unknown', 'French or Polish', PL, '1801-1900', 'AGAD, Archiwum ks. Józefa Poniatowskiego i Marii Teresy z Poniatowskich Tyszkiewiczowej (zesp. 346), 1/346/0/-/1066', 'not seen', 'C',
        "Catalogue: 'w tym również nie rozszyfrowana'. May mean unidentified writers or an illegible hand rather than cipher; confirm first.", "Poniatowski's sister in the Napoleonic period; weak until seen.", 2, 1, 3, sz('record', 17870468), **NOSCAN),

    row(1470, '7 Oct 1470', 'Mosén Pedro Vara → Ferdinand, king of Sicily: letter from Dueñas in mixed clear and cipher with interlinear glosses', 'Pedro de Vara → Ferdinand II of Aragon', 'Dueñas', 'Spanish', 'Spain', '15th century',
        'BNE, MSS/20215/36', '1 leaf, 2 images; cipher runs on most lines of the page viewed; glosses between the lines', 'A',
        'BNE card: firma autógrafa, notas marginales. Viewer page 1 seen: signs and digits inside a clear Spanish text, later interlinear glosses in another hand that seem to cover part of it. Not on DECODE; not in the repo. Same place and weeks as Ferdinand → John II, Dueñas 12 Nov 1470 (MSS/20211/56, R9530 solved, targets/ferdinand1473 d56).',
        "Ferdinand's own circle in the first year of the marriage to Isabella; a 1470 sibling and possible key source for ferdinand1473.", 5, 5, 2,
        [{'label': 'BNE card', 'href': BN + '3ec1dafd-40d2-4e42-90c2-a66ba335e0f9'}], seen='image', access='BNE Digital viewer, free; CC BY 4.0', prior=ESP, portal='BNE Digital', cls_note='',
        verify='Compare its signs with d56, d64 and d73; align the glosses; read the rest.'),
    row(1477, '1476-1479', 'Ferdinand → John II of Aragon: at least ten more letters that BNE matches as cipher', 'Ferdinand II of Aragon → John II of Aragon', 'Bilbao, Madrigal, Medina del Campo, Madrid, Córdoba, Trujillo', 'Spanish', 'Spain', '15th century',
        'BNE, MSS/20211/98, 109, 114, 115, 123 (others in the series: shelfmark not read before BNE slowed me)', 'dated 5 Aug 1476, 30 Apr 1476, 6 Jul 1477, 9 and 18 Apr 1478 (two), 4 Nov and 4 Dec 1478, 22 Jan 1479', 'B',
        "All returned by BNE's field search for 'cifrada' (the matching field not seen). None viewed. This is the open item in targets/ferdinand1473 NOTES (Next steps 2). Letters /56, /64, /73 are excluded: already that target.",
        'The war of succession and the last years of John II, from Ferdinand himself.', 5, 5, 2,
        [{'label': d, 'href': BN + i} for d, i in [('Bilbao 1476', '1d2558fe-3e2e-469a-884f-4e8827b66610'), ('1477', '957ce7b2-d446-40a9-abae-3549355d3dd7'), ('9 Apr 1478', '19f9674b-c52e-48cc-ab6e-63f210f30182'), ('18 Apr 1478', '46115f93-986a-4cb5-9ac3-a37b34f3604f'), ('18 Apr 1478 b', '8fad26d6-2c4e-4bb5-b5b0-117c68d25319'), ('4 Nov 1478', 'efc87815-5336-44c7-930c-ad2af9bb5609'), ('Madrigal 1476', '7cc11f17-b68a-40fa-8169-fb57d094f48f'), ('Medina 1477', 'a85eb2e0-6882-4ac3-865b-a70ee107ab7e'), ('Trujillo 4 Dec 1478', 'b64ed2f0-e1f2-4f58-a1f6-6dceba27c00a'), ('Trujillo 1479', '24287df5-48b3-4dc1-b4e1-d35ea262bde9')]],
        access='BNE Digital viewer, free; CC BY 4.0', prior=ESP, portal='BNE Digital', verify='Open each in the viewer and test the d64 and d73 alphabets. Work inside targets/ferdinand1473 if they fit.'),
    row(1680, '14 Apr 1680', 'Emperor Leopold I → Charles II of Spain: autograph cipher letter from Prague', 'Leopold I → Charles II of Spain', 'Prague', 'Spanish or Italian', 'Central Europe', '1651-1700', 'BNE, RES/261/58', '[I, 3] leaves', 'C',
        "BNE title: 'Carta cifrada del Emperador Leopoldo I a Carlos II de España'; autograph, wax seal. No decipherment noted on the card. Not on DECODE. Not viewed.", "A ruler's own cipher letter inside the Habsburg family, after Nijmegen.", 5, 4, 3,
        [{'label': 'BNE card', 'href': BN + '29736cc9-91f0-4f84-b38e-93bb5f93f932'}], access='BNE Digital viewer, free; CC BY 4.0', prior=ESP + '; SNAC mirrors the BNE title', portal='BNE Digital'),
    row(1548, '12 May 1548', 'Diego Hurtado de Mendoza → Cardinal Granvelle: cipher letter from Rome', 'Diego Hurtado de Mendoza → Antoine Perrenot de Granvelle', 'Rome', 'Spanish', 'Spain', '1497-1559', 'BNE, RES/261/73', '[I, 2] leaves', 'B',
        "BNE title: 'Carta cifrada'. A separate item from the five Gayangos letters the bne_hispana sweep listed. Not viewed.", 'The Farnese crisis after the murder of Pier Luigi; same family as Tomokiyo\'s Granvelle keys.', 4, 4, 2,
        [{'label': 'BNE card', 'href': BN + 'fd34a0af-aca4-4122-92ae-02a7b7012a0f'}], access='BNE Digital viewer, free; CC BY 4.0', prior=ESP, portal='BNE Digital', verify='View it; test the Hurtado and Granvelle keys listed in spanish2C.htm.'),
    row(1622, '8 Dec 1622', 'Marquis of Mirabel → Carlos Coloma, ambassador in England: cipher letter from Lyon', 'Antonio de Zúñiga, marquis of Mirabel → Carlos Coloma', 'Lyon', 'Spanish', 'Spain', '1611-1650', 'BNE, RES/227/122', '[2] leaves; signature and postscript autograph', 'B',
        "BNE title: 'Carta cifrada'. Not viewed. Mirabel → Gondomar (Mss/18…) is an earlier bne_hispana lead, perhaps with a related key.", 'Spanish Match diplomacy.', 4, 4, 3,
        [{'label': 'BNE card', 'href': BN + '0c7ab8a3-f444-4a54-a356-e07f50dc525d'}], access='BNE Digital viewer, free; CC BY 4.0', prior=ESP, portal='BNE Digital'),
    row(1622, 'Aug - 23 Nov 1622', 'Duke of Feria, governor of Milan → Carlos Coloma: letters, some in cipher', 'Gómez Suárez de Figueroa, duke of Feria → Carlos Coloma', 'Milan', 'Spanish', 'Spain', '1611-1650', 'BNE, RES/227/120-121 and a further Aug-Sept 1622 item (shelfmark not read)', '2 letters + further set', 'C',
        "BNE: 'La primera carta, cifrada en parte'; 26 Oct and 23 Nov 1622. Not viewed.", 'Valtelline and the Spanish Match.', 3, 4, 3,
        [{'label': 'RES/227/120-121', 'href': BN + 'fd72f368-47a6-45d9-96cf-0d7a71f3ccc9'}, {'label': 'Aug-Sept 1622', 'href': BN + 'ce09330d-dffc-4e3d-8ed8-4f2ccd37dcac'}], access='BNE Digital viewer, free; CC BY 4.0', prior=ESP, portal='BNE Digital'),
    row(1548, '30 June 1548', 'Ferrante Gonzaga → Cardinal Granvelle: letter from Mantua matched as cipher', 'Ferrante Gonzaga → Antoine Perrenot de Granvelle', 'Mantua', 'Spanish or Italian', 'Spain', '1497-1559', 'BNE, shelfmark not read (see card)', 'not seen', 'B',
        "Returned by BNE's search for 'cifrada'; card blocked by BNE's security check before I could read it.", 'Milan and Piacenza in the aftermath of 1547.', 3, 3, 3,
        [{'label': 'BNE card', 'href': BN + 'f5cf9a8e-f67d-4193-a130-ca4a994f3c96'}], access='BNE Digital viewer, free; CC BY 4.0', prior=ESP, portal='BNE Digital'),
    row(1548, '5 July 1548', 'Jean de Saint-Mauris → Cardinal Granvelle: letter from Dijon, cipher', 'Jean de Saint-Mauris → Antoine Perrenot de Granvelle', 'Dijon', 'French or Spanish', 'France', '1497-1559', 'BNE, MSS/7913/127', 'marginal notes in another hand', 'B',
        "On DECODE as R1185 (Cryptoole status open). Returned by BNE's search for 'cifrada'. Not viewed. DECODE record not opened.", 'Tomokiyo records a Granvelle-Saint Mauris cipher of 1547-48 (PP1), which should fit.', 3, 4, 1,
        [{'label': 'BNE card', 'href': BN + 'dfaf8047-c3c5-400a-851e-02c291cc9a92'}], access='BNE Digital viewer, free; CC BY 4.0', prior='not fully open: key family known to Tomokiyo; read status of this letter not checked (2 Nov 2026)', portal='BNE Digital', decode_ids=[1185],
        verify='Open R1185; apply the Granvelle-Saint Mauris key.'),
    row(1684, '1670s-1690s', 'Antonio de Mendoza Caamaño y Sotomayor, marquis of Villagarcía: diplomatic correspondence, volumes matched as cipher by BNE', 'Antonio de Mendoza Caamaño, II marquis of Villagarcía ↔ various', 'Genoa, Venice', 'Spanish', 'Spain', '1651-1700',
        'BNE, Correspondencia diplomática de Antonio de Mendoza Caamaño y Sotomayor, tomos 3, 4, 8, 9, 11, 13, 14, 17, 18 (shelfmarks not read)', 'nine volumes; extent of cipher unknown', 'C',
        "All nine returned by BNE's field search for 'cifrado'; the matching field was not seen. The volume notes on Europeana contain no cipher word, so the cipher is unconfirmed. Per BNE and the DBE this is the II marquis (1638-1714), at Genoa from 1672 and Venice 1677-91. Not viewed: BNE blocked access on 2 Nov 2026.",
        'Spanish embassy files at Venice during the War of the Holy League, if they do hold cipher.', 3, 2, 3,
        [{'label': f'tomo {t}', 'href': BN + i} for t, i in [(3, 'bafe8c96-2090-4c14-a48d-e265723b5f32'), (4, '49480a9a-9249-4eca-811e-9fe2d2657e01'), (8, 'e2aecac4-24ea-4525-a17e-f56db008bacd'), (9, '0a5fd854-799e-428b-bab0-99e9306913e7'), (11, '3b205f2d-243c-494a-a773-e66c5ac7a531'), (13, '8e3d9ad8-7a2f-41de-9c2b-b6c711e842a0'), (14, '8d019cc7-d63c-4892-a91d-ec34e16e773b'), (17, '48145573-3de8-4e82-a386-7e04a21ce27c'), (18, '15628d19-22c9-43e6-b119-12b2a2e70ab3')]],
        access='BNE Digital viewer, free; BNE blocked this session', prior=ESP, portal='BNE Digital', verify='Open each card to see why it matched; sample the volumes for cipher.'),
    row(1681, '12 Jan 1681', 'Diego Crolope → uncertain recipient: letter matched as cipher by BNE', 'Diego Crolope (name doubtful) → unknown', 'unknown', 'Spanish', 'Spain', '1651-1700', 'BNE, bdh0000173166 (shelfmark not read)', 'not seen', 'C',
        "Returned by BNE's field search on a cipher term; the matching field was not seen. Its Europeana record does not mention cipher (notes: 'Nombre de remitente dudoso', 'Manchas de humedad'). Weak. Not viewed: BNE blocked access on 2 Nov 2026.",
        'Unknown until seen.', 1, 2, 3, [{'label': 'BNE card', 'href': BN + '8b0f5fc5-5240-4104-8392-76cf341135c4'}],
        access='BNE Digital viewer, free; BNE blocked this session', prior=ESP, portal='BNE Digital', verify='Open the card and the leaf; drop this row if there is no cipher.'),
]
for r in R:
    r.pop('cls_note', None)
with open(os.path.join(HERE, 'candidates.json'), 'w', encoding='utf-8') as f:
    json.dump(R, f, ensure_ascii=False, indent=1)
print(len(R))
