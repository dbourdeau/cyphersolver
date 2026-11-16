import json
D = 'https://discovery.nationalarchives.gov.uk/details/r/'
IA = 'https://archive.org/details/'
SRC_D = 'TNA Discovery API (item-level cipher sweep, 15 Nov 2026)'
SRC_C = 'Calendar of State Papers, archive.org OCR (15 Nov 2026)'
PA_D = ('open as far as checked (15 Nov 2026: known.py and reference grep on shelfmark and correspondents; Discovery text only; '
        'no image seen; CSP, Tomokiyo, DECODE, Lasry and the literature not searched for this item)')
PA_C = ('open as far as checked (15 Nov 2026: known.py on names and shelfmark; calendar OCR only; the TNA original, '
        'State Papers Online and the literature not checked)')
SN_D = 'Scored from the TNA Discovery catalogue description only (item sweep, 15 Nov 2026; research/sweep_2026-11-15_tna_discovery/); not viewed'
SN_C = 'Scored from the printed calendar entry (archive.org OCR) only (research/sweep_2026-11-15_tna_discovery/); the TNA original not viewed'
rows = []


def add(links, csp=False, **k):
    base = dict(language='English', region='England', cls='C', difficulty=3, seen='catalogue',
                source=SRC_C if csp else SRC_D, prior_art=PA_C if csp else PA_D, needs_archive_scan='yes',
                access_note='not digitised on Discovery; State Papers Online (Gale, subscription) or a Kew visit',
                score_note=SN_C if csp else SN_D, folio_note='')
    base.update(k)
    base['links'] = [{'label': a, 'href': b} for a, b in links]
    rows.append(base)


add(year=1704, date='9 and 13 Jul 1704', period='1701-1800',
    title='Marlborough, Blenheim campaign: two enclosures "Cipher with interlinear decodement" (Wratislav and the elector of Bavaria)',
    correspondents='Marlborough -> Robert Harley (secretary of state)', place='Kinderkinge and Burcheim (Bavaria)',
    shelfmark='TNA SP 87/2/49 (f. 91) and SP 87/2/51 (f. 94)',
    folio_note='Covering letters SP 87/2/48 (ff. 89-90) and /50 (ff. 92-93) each refer to an enclosure in cipher; SP 87/2/70 (18 Aug 1704) is a deciphered copy in the same volume',
    cls='A', status='Catalogue: "Cipher with interlinear decodement" for both items; the plaintext is written over the ciphertext, so each is a ciphertext/plaintext pair. No edition of the decodement found.',
    why="A paired cipher/decode of Marlborough's number cipher in the Danube campaign; the interlinear decode is a crib for rebuilding the key and for the other Marlborough-era number letters in SP 87 (SP 87/4/133 is already a lead).",
    importance=3, solvability=5, difficulty=1,
    verify='Order SP 87/2 ff. 91 and 94; check the decode covers every group; compare with SP 87/4/133 and the Marlborough-Godolphin number cipher (catalogue 807 note).',
    links=[('TNA Discovery SP 87/2/49', D + 'C8950289'), ('TNA Discovery SP 87/2/51', D + 'C8950291')])
add(year=1811, date='1811 (letters undated; the ship left Batavia 7 Aug 1811)', period='1801-1900', language='French', region='Other',
    title='Governor-General of the Dutch East Indies to the French Minister of Marine: three "lettres en chiffre" captured with the corvette Le Comte Reynaud, 1811',
    correspondents='Governor-General of the Indies (Janssens, to be checked) -> Minister of Marine, Paris; captured by Justice Finley, HMS Rover', place='Batavia / Portsmouth',
    shelfmark='TNA ADM 1/1808/193 (ff. 517-526)',
    folio_note='"Original lettre en chiffre", numero un, deux, trois, ff. 521-522, 523-524, 525-526, each undated with an illegible signature; envelopes ff. 519-520',
    status='Catalogue: three original numerical-cipher letters; no decipherment mentioned.',
    why='Captured original French ciphertext from the last months of French rule in Java. targets/batavia1800 notes that the 1811 Janssens despatches (NA 2.01.27.05 inv. 12) use a numeric code, a possible key family.',
    importance=3, solvability=2, difficulty=3,
    verify='View ADM 1/1808/193; read targets/batavia1800/NOTES.md on the numeric code and test it on these letters; check whether the Admiralty kept a decipher.',
    links=[('TNA Discovery ADM 1/1808/193', D + 'C12759093')])
add(year=1813, date='1813 (report dated 16 Jul - 4 Oct 1813)', period='1801-1900',
    title='Captain James Hillyar (HMS Phoebe) enciphered report on the pursuit of the American frigate Essex, deciphered at the Admiralty',
    correspondents='James Hillyar -> Admiralty (enclosure to his letter of 12 Jun 1813)', place='South Atlantic / Pacific',
    shelfmark='TNA ADM 1/1948/97 (enclosure ff. 251-252)',
    folio_note='Cover letter ff. 249-250; the enciphered report and its Admiralty decipher are on ff. 251-252',
    cls='A', status='Catalogue: "Enciphered report ... which has been deciphered at the Admiralty"; the ciphertext and a contemporary decipher sit together.',
    why='A naval cipher/decipher pair from the War of 1812; the Admiralty decipher gives the plaintext, so a key can be rebuilt.',
    importance=3, solvability=4, difficulty=2,
    verify="Order ADM 1/1948 ff. 251-252; check the decipher is on the same leaves; look for other enciphered enclosures in the Captains' Letters H 1813 series.",
    links=[('TNA Discovery ADM 1/1948/97', D + 'C12820601')])
add(year=1813, date='4 Nov 1813', period='1801-1900', title='Captain Philip Carteret (HMS Pomone, off Finisterre) to the Admiralty: letter "written in cypher code and decrypted"',
    correspondents='Philip Carteret -> Admiralty', place='Cape Finisterre', shelfmark='TNA ADM 1/1665/176', folio_note='ff. 518-519',
    cls='A', status='Catalogue: "Written in cypher code and decrypted"; one-line description.',
    why='A short naval ciphertext with its decrypt, probably in the same folios; useful with ADM 1/1948/97 as a second Admiralty cipher of 1813.',
    importance=2, solvability=3, difficulty=2, verify='Order the two leaves; see whether the decrypt is written on the cipher.',
    links=[('TNA Discovery ADM 1/1665/176', D + 'C18550506')])
add(year=1799, date='15 May 1799', period='1701-1800', title='Rear Admiral Rainier (Asiatic Seas): letter and extracts "in code" sent by Captain Osborn, HMS Arrogant, from Bombay',
    correspondents='Peter Rainier / Edward Oliver Osborn -> Admiralty; enclosure from East India House', place='Bombay',
    shelfmark='TNA ADM 1/2253/132 (ff. 306-321)', folio_note='ff. 306-313 covering letter; ff. 316-321 "Letter (in code) dated 15 May 1799"',
    status='Catalogue: extracts of a letter "which is in code" and a letter in code; no decipherment named.',
    why="Late-18th-century naval code letters from the Indian station, in the Captains' Letters O series.",
    importance=2, solvability=2, difficulty=3, verify='View ADM 1/2253 ff. 306-321; check whether it is a code or a cipher and whether an Admiralty decode follows.',
    links=[('TNA Discovery ADM 1/2253/132', D + 'C12835255')])
add(year=1778, date='c. 1770-1786', period='1701-1800', language='French',
    title='Stapleton de Laurence to Kerguelen: six enciphered or partly enciphered love letters (one deciphered between the lines)',
    correspondents='Stapleton de Laurence ("Mimi") -> Yves-Joseph de Kerguelen (Saumur)', place='France',
    shelfmark='TNA SP 46/146/63-64, /65-66, /71-72, /89-90; SP 46/148/99-100, /196-197',
    folio_note="SP 46/146/63-64 is \"deciphered between the lines in Kerguelen's hand\" (first page missing); /71-72 partially enciphered; /89-90 and 148/196-197 partially encoded; 148/99-100 an enciphered love letter. SP 46/146/214 (1780) concerns difficulty reading Benyovszky's hand and is not a cipher",
    cls='A', status='Catalogue: one letter with an interlinear decipher, five more enciphered or partly encoded; no edition.',
    why='A small private-correspondence cipher family in the Kerguelen papers (SP 46), with one interlinear decipher as a crib; one key for the set.',
    importance=2, solvability=4, difficulty=2, verify='Order SP 46/146 ff. 63-66, 71-72, 89-90 and SP 46/148; build the key from ff. 63-64 and test on the others; check SP 46/146 for a key leaf.',
    links=[('TNA Discovery SP 46/146/63-64', D + 'C7712676'), ('TNA Discovery SP 46/146/71-72', D + 'C7712680'), ('TNA Discovery SP 46/148/99-100', D + 'C7713246')])
add(year=1751, date='28 Aug - 5 Sep 1751', period='1701-1800',
    title='Intercepted Jacobite letter (Andrew Clerck to Alexander Cameron of Gleneves) with a list of the names thought to be given in code',
    correspondents='Andrew Clerck -> Alexander Cameron of Gleneves; Lt-Gen Churchill -> Newcastle', place='Scotland',
    shelfmark='TNA SP 54/41/27A, 27B and 27C', folio_note='27A Churchill to Newcastle 5 Sep 1751; 27B the intercepted letter; 27C list of code names',
    cls='B', status='Catalogue: letter "thought to contain code names ... on the subject of the money left behind by the Young Pretender"; 27C is a partial key by the intercepting side.',
    why='A Forty-Five aftermath intercept with a contemporary partial key list; a nomenclator-style code that can be solved from the list plus context.',
    importance=3, solvability=3, difficulty=3, verify='Order SP 54/41 no. 27; compare with other Cameron of Gleneves letters; check the Cluny/Glengarry literature.',
    links=[('TNA Discovery SP 54/41/27C', D + 'C6820317')])
add(year=1695, date='1689-1702 (letter undated)', period='1651-1700', language='French',
    title='Ciphered letter on peace overtures (Ruvigny, Turenne, Sparr) with a plaintext extract at the front, Nine Years War',
    correspondents='unknown author -> "your Highness"', place='unknown', shelfmark='TNA SP 32/14/51 (ff. 99-101)',
    folio_note='f. 99 extract; ff. 100-101 the ciphered letter',
    cls='B', status='Catalogue: "Extract (folio 99) from a ciphered letter (folios 100-101)". The extract is a ready crib.',
    why='A plaintext extract beside the ciphered letter, in a volume of Secretary of State (Nottingham/Shrewsbury) papers; solvable from the extract.',
    importance=3, solvability=4, difficulty=2, verify='Order SP 32/14 ff. 99-101; align the extract with the cipher; check whether the volume has a key (Wallis deciphered letters in SP 32/2-3).',
    links=[('TNA Discovery SP 32/14/51', D + 'C17475303')])
add(year=1682, date='6 Jun 1682', period='1651-1700', title='Lord Shaftesbury: drafts of letters to Percivall, Perkins and Captain Fisher "in cypher"',
    correspondents='Anthony Ashley Cooper, 1st Earl of Shaftesbury -> Percivall, Perkins, Captain Fisher', place='London / exile',
    shelfmark='TNA PRO 30/24/7/505', folio_note="three drafts, indorsed \"These to be in my lord's book of letters, entered November 1682\"",
    status='Catalogue: drafts "in cypher"; no decipherment named.', why="Shaftesbury's own cypher letters at the time of his flight; the letter book may give plaintext.",
    importance=3, solvability=2, difficulty=3, verify='View PRO 30/24/7 no. 505; check the Shaftesbury letter-book entries of Nov 1682.',
    links=[('TNA Discovery PRO 30/24/7/505', D + 'C6756450')])
add(year=1687, date='5 Apr 1687', period='1651-1700', title='Letter in cipher from "PD" to William Benson, filed with a cryptic trade letter (James II)',
    correspondents='PD -> William Benson, Strand', place='London', shelfmark='TNA SP 31/3/117 (ff. 206-207)',
    folio_note='f. 206 cryptic plain letter; f. 207 "A letter in cipher", postscript "Cut off this and deliver it to my friend"',
    status='Catalogue: "A letter in cipher"; no decipherment.', why='A short cipher letter filed with a cryptic commercial letter, apparently a seized correspondence of 1687.',
    importance=2, solvability=1, difficulty=3, verify='View SP 31/3 ff. 206-207; check neighbours for the key.', links=[('TNA Discovery SP 31/3/117', D + 'C18485520')])
add(year=1704, date='1 Mar - 3 Jun 1704', period='1701-1800', title='Lord Raby (Berlin) to Hedges: cipher passages and "additions to cipher" in the Bavarian negotiation despatches',
    correspondents='Thomas Wentworth, Lord Raby -> Sir Charles Hedges', place='Berlin', shelfmark='TNA SP 90/2/107, /262, /335, /337, /356, /372',
    folio_note='/262 "Explains cipher of f.266"; /335 receipt of cipher; /356 "Additions to cipher"; /372 "Partly in cipher"',
    status='Catalogue: cipher passages and cipher explanations; no decipher named.',
    why="Raby's cipher with its explanation in the same volume; Raby is also the addressee in the Klement/Rakoczi number cipher already in leads.json.",
    importance=2, solvability=3, difficulty=3, verify='View SP 90/2 ff. 262-266, 335-337, 356; compare with the Fiedler key I match (Raby, princeps) in leads.json.',
    links=[('TNA Discovery SP 90/2/262', D + 'C6554786'), ('TNA Discovery SP 90/2/356', D + 'C6554815')])
add(year=1722, date='23 Oct 1722', period='1701-1800', title="George Kelly's pocket-book (Atterbury plot), \"various references, some in code\", three copies",
    correspondents='George Kelly (alias Johnson)', place='London', shelfmark='TNA SP 35/72/17', folio_note='copy of the pocket-book taken by the messenger Daniel Chandler; three copies; formerly E17',
    status='Catalogue: names, payments and meetings, some in code.', why='A code-name list inside the best-documented Jacobite plot; sibling of the SP 35/45-53 Atterbury ciphers (catalogue 860).',
    importance=3, solvability=2, difficulty=3, verify="Order SP 35/72 no. 17; compare with the cipher key SP 35/39/21 (BY1) and the three copies.",
    links=[('TNA Discovery SP 35/72/17', D + 'C15416206'), ('Key copy SP 35/39/21', D + 'C15416469')])
add(year=1722, date='12 Feb 1722', period='1701-1800', title='Letter from "R W" to a Monsieur, intercepted and translated; "all the names are still in cypher"',
    correspondents='R W -> [Monsieur]', place='unknown', shelfmark='TNA SP 35/30/31 (ff. 78-81)', folio_note='translation; names left in cypher',
    status='Catalogue: names still in cypher in the translation.', why='A name nomenclator in an Atterbury-era translation; the context (Whigs, Regent, Dubois, Czar) allows a name solution.',
    importance=2, solvability=3, difficulty=3, verify='View SP 35/30 ff. 78-81; check the original is in the volume.', links=[('TNA Discovery SP 35/30/31', D + 'C17209745')])
add(year=1743, date='31 May 1743', period='1701-1800', language='French', title='St Quentin (Paris) to the Pretender: French letter partly in cypher (Tencin, Amelot, northern nobility)',
    correspondents='St Quentin -> James Francis Edward Stuart (intercepted)', place='Paris', shelfmark='TNA SP 36/60/365', folio_note='f. 365',
    status='Catalogue: "French Partly in cypher".', why='Jacobite intercept of 1743 with a cipher portion and a clear context.',
    importance=3, solvability=2, difficulty=3, verify='View SP 36/60 f. 365; check the Stuart Papers for the sent copy.', links=[('TNA Discovery SP 36/60/365', D + 'C7768166')])
add(year=1653, date='12 Aug 1653', period='1651-1700', language='French', region='Low Countries',
    title='Beverning at Westminster to Newport at The Hague: report of a conversation "part in code", copy',
    correspondents='Hieronymus van Beverning -> Willem Nieupoort', place='Westminster', shelfmark='TNA SP 46/97/fo 47-47d', folio_note='copy; f. 47-47d',
    status='Catalogue: part in code, copy.', why='A sibling of the Beverning/Vande Perre ciphers already worked in targets/thurloe (22 Aug 1653) and targets/colbert; the same Dutch envoy cipher may open it.',
    importance=3, solvability=3, difficulty=2, verify='View SP 46/97 f. 47; test the thurloe/colbert Beverning key.', links=[('TNA Discovery SP 46/97/fo47', D + 'C7709925')])
add(year=1548, date='Nov 1548', period='1497-1559', title='Account "in code" on the back of a draft account for flax and wadmoll (Bronyng, Le, Hobson)',
    correspondents='Robert Bronyng; John a Le; Robert Hobson', place='London', shelfmark='TNA SP 46/124/fo 60d', folio_note='fo. 60d',
    status='Catalogue: "with an account in code on fo. 60d".', why='A rare English merchant code of 1548; short, but early.',
    importance=2, solvability=1, difficulty=3, verify='View SP 46/124 f. 60d; see the related SP 46/2 ff. 83-92.', links=[('TNA Discovery SP 46/124/fo60', D + 'C7694233')])
add(year=1670, date='Duke of York period (1660-85); undated in the catalogue', period='1651-1700',
    title='"Intercepted note in code from the Duke of York" (two pages), Braye MS.3, Parliamentary Archives',
    correspondents='James, Duke of York (later James II)', place='unknown', shelfmark='Parliamentary Archives, Braye MS.3 (Letters and State Papers 1648-1710); Discovery YPIC/P/301to399/374-375',
    folio_note='first and second page as two records',
    status='Catalogue: "Intercepted note in code". Discovery lists the two pages as records of a Parliamentary Archives item.',
    why='A code note by the future James II kept as two page records; a rare royal cipher of the Restoration period.',
    importance=3, solvability=2, difficulty=3, verify='Open the two Discovery records for images; check the HMC Braye report and the Parliamentary Archives catalogue for a decipher.',
    access_note='Parliamentary Archives; the two pages are listed on Discovery (image availability not checked)',
    links=[('Discovery YPIC/P/301to399/374', D + '90c45416-90f0-4557-bc4a-a27296025485'), ('Discovery YPIC/P/301to399/375', D + '64426b03-9179-492d-80d8-96666a75f191')])
add(year=1789, date='15 Jul 1789 (sent 12 Dec 1789)', period='1701-1800', title='Dead letter "to my dear George from M" with a section apparently in code (Weymouth, the king\'s stay)',
    correspondents='M -> George; forwarded by Anthony Todd (GPO)', place='Weymouth', shelfmark='TNA HO 42/15/21 (ff. 123A-125)',
    status='Catalogue: "a section apparently in code".', why='A short code section in a Home Office dead-letter file.', importance=2, solvability=1, difficulty=3,
    verify='View HO 42/15 ff. 123A-125.', links=[('TNA Discovery HO 42/15/21', D + 'C11805737')])
add(year=1803, date='8 Oct 1803', period='1801-1900', title='Pat McGuiness, Whitehaven: cryptic letter partly in code, headed "The moment is arrived"',
    correspondents='Pat McGuiness', place='Whitehaven', shelfmark='TNA HO 42/73/71 (f. 220)', status='Catalogue: partly in code.',
    why='Radical/Irish correspondence of the Despard period with a code portion.', importance=2, solvability=1, difficulty=3,
    verify='View HO 42/73 f. 220.', links=[('TNA Discovery HO 42/73/71', D + 'C17045965')])
add(year=1819, date='10 Apr 1819 (filed 28 May 1819)', period='1801-1900', title='Unsigned letter from Brentford to James Bateman, Birmingham: revolutionary plans, "places in code"',
    correspondents='unsigned -> James Bateman; forwarded by W Hicks, Returned Letter Office', place='Brentford / Birmingham', shelfmark='TNA HO 33/2/21 (ff. 74-77)',
    status='Catalogue: refers to places in code.', why='A Peterloo-period intercept with place names in code.', importance=2, solvability=2, difficulty=3,
    verify='View HO 33/2 ff. 74-77.', links=[('TNA Discovery HO 33/2/21', D + 'C9712187')])
# --- Calendar of State Papers (archive.org OCR) ---
add(csp=True, year=1645, date='1644-45 (calendar volume 1644; p. 690)', period='1611-1650',
    title='Cipher letter, ascribed by the editor to Archbishop John Williams of York, to Lord Digby in Ireland, intercepted by Parliament, "apparently not deciphered"',
    correspondents="Archbishop Williams (editor's reading) -> George, Lord Digby", place='Wales / Ireland', shelfmark='CSP Domestic, Charles I, 1644 (preface and p. 690); TNA SP 16 (volume not read)',
    folio_note='The editor says each symbol stands for a word and deduced the writer from the initial letters (W or Y, a Welsh place beginning C).',
    status='Calendar preface: intercepted, apparently not deciphered; the editor partly analysed the scheme.',
    why='A Royalist word-symbol cipher of 1644-45 with a published partial analysis; Digby/Nicholas/Goring keys of autumn 1645 are held (catalogue note, BL Add MS 32256).',
    importance=3, solvability=2, difficulty=4, seen='print',
    verify='Read the entry at CSP Dom. 1644 p. 690; find the SP 16 volume; test the Digby/Nicholas keys named in the catalogue.',
    links=[('CSP Dom. Charles I 1644 (archive.org)', IA + 'cu31924091770341')])
add(csp=True, year=1600, date='Oct 1600 (calendar vol. CCLXXV, p. 495)', period='1598-1610',
    title='Spy report with an inserted love letter (Donavillis to Feselaw): "the whole letter is in cipher"; italic passages and most of the love letters undeciphered',
    correspondents='report to Cecil by an agent; letter Donavillis -> Feselaw ("dear Bess")', place='England / Flanders', shelfmark='CSP Domestic Elizabeth 1598-1601 (p. 495); TNA SP 12/275 (printed vol. CCLXXV, not verified)',
    folio_note='23 pages; Weekes, Smith and George Kendal are named in the same report',
    status='Calendar: italics in the cipher "undeciphered, as well as the greater part of the love letters".',
    why='A long (23 page) report with unread cipher passages, in the Archduke spy-network period; the persons are known.',
    importance=3, solvability=2, difficulty=3, seen='print', verify='View SP 12/275 (or the volume holding Oct 1600); check whether the cipher is the Phelippes-era numeric nomenclator.',
    links=[('CSP Dom. Eliz. 1598-1601 (archive.org)', IA + 'sim_great-britain-public-record-mary-elizabeth-i-and-james-i_january-1598-february-1601')])
add(csp=True, year=1600, date='14 Oct 1600 (calendar vol. CCLXXV)', period='1598-1610',
    title='Wm. Holt to Hugh Owen and Rich. Bayley, Brussels: "the numbers are ciphers, undeciphered" (Parsons, Stanley, Thos. Gortz)',
    correspondents='William Holt (Jesuit) -> Hugh Owen and Richard Bayley', place='Rouen -> Brussels', shelfmark='CSP Domestic Elizabeth 1598-1601 item 79; TNA SP 12/275 (not verified)',
    folio_note='one page; numbers stand for persons', status='Calendar: "The numbers are ciphers, undeciphered."',
    why='A short Catholic exile letter with a number nomenclator; the persons are guessable (Parsons, Stanley).', importance=2, solvability=2, difficulty=3, seen='print',
    verify='View the original; compare with the Owen/Holt keys in the Spanish and Cecil papers.',
    links=[('CSP Dom. Eliz. 1598-1601 (archive.org)', IA + 'sim_great-britain-public-record-mary-elizabeth-i-and-james-i_january-1598-february-1601')])
add(csp=True, year=1620, date='9 Aug 1620 (calendar James I 1619-23, vol. CXVI)', period='1611-1650',
    title='Du Buisson brings letters from the Prince of Conde offering a daughter of France in marriage to the Prince: "partly in cipher, undeciphered"',
    correspondents='unknown (Dover) -> unknown', place='Dover', shelfmark='CSP Domestic James I 1619-23 (item before no. 60); TNA SP 14/116 (printed vol. CXVI)', status='Calendar: partly in cipher, undeciphered.',
    why='A marriage-negotiation note of 1620 with a cipher part; short.', importance=2, solvability=2, difficulty=3, seen='print',
    verify='View SP 14/116 near 4-9 Aug 1620.', links=[('CSP Dom. James I 1619-23 (archive.org)', IA + 'sim_great-britain-public-record-mary-elizabeth-i-and-james-i_1619-1623')])
add(csp=True, year=1663, date='1663 (Charles II calendar nos. 17-18)', period='1651-1700',
    title='Letter on the Thorne-Lawrence plot "partly in cypher", with a contemporary decypher as the next calendar item',
    correspondents='informer -> Sir Henry Bennet (Arlington)', place='Holland / England', shelfmark='CSP Domestic Charles II 1663-64 nos. 17-18; TNA SP 29 (volume not read)',
    folio_note='no. 17 the ciphered letter, no. 18 "Decypher of the preceding letter", endorsed by Bennet "Seize the armes in the Custom House"',
    cls='A', status='Calendar: partly in cypher with the decypher filed beside it, so a plaintext pair.',
    why="A ciphertext/decypher pair of 1663; the decypher gives the key for this informer's cipher.",
    importance=3, solvability=4, difficulty=2, seen='print', verify='Find the SP 29 volume (spring-summer 1663); order both leaves.',
    links=[('CSP Dom. Charles II 1663-64 (archive.org)', IA + 'sim_great-britain-public-record-papers-domestic-charles-ii_january-1663-august-1664')])
json.dump(rows, open('candidates.json', 'w', encoding='utf8'), ensure_ascii=False, indent=1)
print(len(rows))
