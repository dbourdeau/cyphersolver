"""Build candidates.json for the ASF Florence sweep (6 Nov 2026).
Rows come from images viewed during the sweep (MAP site and the PAD digitised-archives site); see README.md.
Leads 2307-2312 (the italian_state_retry rows) are not repeated."""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
B = 'https://archiviodistatofirenze.cultura.gov.it'
SCORE = 'Scored from the images viewed during the ASF Florence sweep, 6 Nov 2026 (research/sweep_2026-11_asf_florence/)'

MAP_SRC = 'ASF Mediceo avanti il Principato (MAP) images + MAP printed inventory (archive.org OCR vols 1-3, ASF page images vol. 4), ASF Florence sweep, Nov 2026'
MAP_ACCESS = ('scans public on the ASF MAP site, no login, curl works: /map/ricerca/ricerca-su-filza/?f=<filza>&d=<doc> and IIIF '
              '/iipsrv/iipsrv.fcgi?IIIF=/data/iip-data/asfi/mediceo_avanti_principato/001000FF/A0000NNN.ptif (1600 px max)')
MAP_PRIOR = ('open as far as checked (6 Nov 2026): known.py finds nothing on the filza, document or correspondent; DECODE dumps in the repo '
             'have no ASF MAP ciphertext record; Tomokiyo and Lasry not searched in this run. Marco Vito (Vienna) works on encrypted MAP '
             'letters of 1486-1491 (research/medici_bia/README.md): check overlap for undated pieces.')

MDP_SRC = ('ASF Mediceo del Principato, Carteggio universale (PAD images) + Carteggio universale di Cosimo I inventory PDFs '
           '(ASF Inventari on-line), ASF Florence sweep, Nov 2026')
MDP_ACCESS = ('scans public on ASF PAD (archividigitali), no login, curl works: unit page /archividigitali/unita-archivistica/?id=<ua> lists '
              'carte; each /archividigitali/riproduzione/?id=<id>&ua=<ua> names the ptif; IIIF /iipsrv/iipsrv.fcgi?IIIF=/data/iip-data/asfi/'
              'mdp_carteggio_universale/<filza>/<seq>_C_<carta>_<R|V>.ptif (2000 px). PAD holds filze 330-460 only (1537-1557).')
MDP_PRIOR = ('open as far as checked (6 Nov 2026): known.py finds nothing on the filza, the carta or the correspondent; the inventory marks the '
             'piece "In cifra" with no decipherment noted, and none is written on the page; ASF holds the chancery keys '
             '(Cifrari II serie, "Chiavi delle cifre del Carteggio di Cosimo I dal 1536 al 1573", 3 filze), not online; DECODE\'s ASFi '
             '"Governo Mediceo - cifre" volumes (R5687-R7459) are 17th-18th c.; Tomokiyo and Lasry not searched in this run.')


def maplinks(filza, doc, ids):
    out = [{'href': f'{B}/map/ricerca/ricerca-su-filza/?f={filza}&d={doc}&c=', 'label': f'MAP filza {filza}, doc. {doc}'}]
    out += [{'href': f'{B}/map/riproduzione/?id={i}', 'label': f'image id {i}'} for i in ids]
    return out


def padlinks(ua, filza, pairs):
    out = [{'href': f'{B}/archividigitali/unita-archivistica/?id={ua}', 'label': f'PAD unit {ua} (Mediceo del Principato {filza})'}]
    out += [{'href': f'{B}/archividigitali/riproduzione/?id={i}&ua={ua}', 'label': lab} for i, lab in pairs]
    return out


def rng(first, labels):
    return [(first + k, lab) for k, lab in enumerate(labels)]


def cc(a, b):
    out = []
    for c in range(a, b + 1):
        out += [f'c. {c}r', f'c. {c}v']
    return out


MAP_ROWS = [
    dict(
        year=1478, date='13 Jan 1478 (as written; Florentine style would make it 1479)',
        title='Anonymous cipher letter of 13 January 1478 in the Mazzinghi cipher (lead 2307), bare; MAP 72/170 glosses the same system',
        correspondents='anonymous -> anonymous (Medici circle)', place='not stated (Rome likely, as for the sibling letters)',
        language='Italian (symbol cipher with clear words)', region='Italy', period='15th century',
        shelfmark='Archivio di Stato di Firenze, Mediceo avanti il Principato, filza CXXXVII, doc. 252',
        folio_note='One oblong leaf, recto: head "+ adì 13 di gennaio 1478", about 20 lines of cipher with clear words between runs; verso blank. '
                   'Inventory vol. 4 (filza CXXXVII, p. 281): "Lettera cifrata di anonimo ad anonimo. s. l., 1478 gen. 13, n. 252".',
        cls='A',
        status='Bare: no interlinear or marginal decipherment (checked at 1272 px). Same sign set (x, ‡, H, =, 5-like signs, "+" heads) and '
               'apparently the same hand as MAP LXXXIX 142 (Mazzinghi, 16 Jan 1478, lead 2307); MAP LXXII 170 (23 Jan 1478, lead 2308) '
               'carries a full interlinear decipherment of this system.',
        why='A third letter of the January 1478 Medici series, three days before the Mazzinghi letter: more ciphertext for the same key, '
            'with the glossed 72/170 as the key source.',
        importance=4, solvability=5, difficulty=2,
        verify='Fold into the Mazzinghi lead (2307) or keep as a sibling; transcribe and apply the key rebuilt from 72/170.',
        links=maplinks(137, 252, [133025, 133026]),
    ),
    dict(
        year=1478, date='undated (filza CXXXVII is a miscellany of 1430s-1470s papers)',
        title='"Poscritto cifrato anonimo": an 8-line postscript in what looks like the Mazzinghi 1478 sign set, bare',
        correspondents='anonymous', place='not stated', language='Italian (symbol cipher with clear words)', region='Italy',
        period='15th century',
        shelfmark='Archivio di Stato di Firenze, Mediceo avanti il Principato, filza CXXXVII, doc. 63',
        folio_note='One strip, recto: 8 lines mixing clear words and cipher runs; verso blank. Inventory vol. 4 (p. 280): '
                   '"Poscritto cifrato anonimo. s. l., s. d., n. 63".',
        cls='B',
        status='Bare (no gloss at 1000 px). Signs (x, ‡, H, dotted separators) resemble the January 1478 system of leads 2307/2308; not yet compared sign by sign.',
        why='A short sibling of the 1478 cipher letters; if the sign set matches, the 72/170 key reads it.',
        importance=2, solvability=4, difficulty=2,
        verify='Fetch at full size; compare signs with MAP 72/170 and 137/252; apply the rebuilt key.',
        links=maplinks(137, 63, [132645, 132646]),
    ),
    dict(
        year=1479, date='31 Aug 1479 (inventory); "1479" at the foot of the page',
        title='Cipher letter "de Spagna" of 31 August 1479 to Lorenzo de\' Medici (not flagged as cipher in the inventory), bare',
        correspondents="anonymous (from Spain, per the inventory) -> Lorenzo de' Medici (verso: 'Mag.co et generoso domino ... Florentie')",
        place='Spain (per the inventory)', language='Italian (symbol cipher with clear words)', region='Italy',
        period='15th century',
        shelfmark='Archivio di Stato di Firenze, Mediceo avanti il Principato, filza LXXII, doc. 171 (old c. 203)',
        folio_note='One leaf: recto a full page (about 40 lines) opening "Mag.co ...", cipher runs alternating with clear words, "1479" at the '
                   'foot; verso address to a Magnifico in Florence. Inventory vol. 3: "Anonimo, de Spagna, 1479 ago. 31" (no cipher mark). '
                   'Found by the vetting session of leads 2307-2312 and checked here.',
        cls='A',
        status='Bare: no interlinear or marginal decipherment (1000 px and full size). Its signs (Φ, ‡, H, =, dotted groups) are of the same '
               'family as the 1478 letters (leads 2307-2308); not yet compared sign by sign.',
        why='A dated pre-1500 Medici cipher letter from Spain, unread, with a possible key in the glossed 1478 letter.',
        importance=4, solvability=4, difficulty=3,
        verify='Transcribe; test the 72/170 key; if it does not fit, compare with the LXXII key sheets 178-188.',
        links=maplinks(72, 171, [79510, 79511]),
    ),
    dict(
        year=1480, date='undated (filza LXXII: papers of the 1460s-1520s)',
        title='Cipher letter to "Lionardo ... in Pisa" (not flagged in the inventory), bare',
        correspondents='unknown -> Lionardo ... in Pisa (verso address)', place='not stated', language='Italian (symbol cipher with clear words)',
        region='Italy', period='15th century',
        shelfmark='Archivio di Stato di Firenze, Mediceo avanti il Principato, filza LXXII, doc. 211',
        folio_note='One leaf: recto about 10 lines, cipher runs with clear words; verso address "D(omi)no Lionardo ... in Pisa" and two short '
                   'endorsements (not legible at 1272 px). Not flagged as cipher in the inventory; found by the vetting session.',
        cls='B',
        status='Bare (no gloss seen). Sign set differs from the 1478 letters and from 72/213-214 (lead 2310).',
        why='Short unread Laurentian-era cipher with clear words as cribs.',
        importance=2, solvability=3, difficulty=3,
        verify='Read the endorsements at full size for sender and date; compare with the key sheets LXXII 178-188.',
        links=maplinks(72, 211, [79616, 79617]),
    ),
    dict(
        year=1485, date='undated (opens "Magnifico Lorenzo"; news "da Napoli")',
        title='"Magnifico Lorenzo" cipher letter with news from Naples; scattered letters over a few signs, otherwise bare',
        correspondents="unknown -> Lorenzo de' Medici", place='not stated', language='Italian (symbol cipher with clear words)',
        region='Italy', period='15th century',
        shelfmark='Archivio di Stato di Firenze, Mediceo avanti il Principato, filza LXXII, doc. 216',
        folio_note='One leaf, recto and verso full (about 35 lines a side, heavy show-through): opens "Magnifico Lorenzo, a voi mi raccomando. '
                   'Questo dì ... lettere da Napoli continenti come le cose ..." then cipher runs (letters, digits, Greek-like signs) between clear words. '
                   'Not flagged in the inventory; found by the vetting session.',
        cls='B',
        status='Mostly bare: a later hand wrote single letters or pairs (e, o, t, so, an ...) over some signs, a partial or attempted '
               'decipherment, not a running gloss. Those pairs are a start for the key.',
        why='A long Laurentian cipher letter about Naples, unread, with a few sign values already noted on the page.',
        importance=3, solvability=4, difficulty=3,
        verify='Transcribe both sides at full size; collect the superscript values; solve the rest (homophonic substitution).',
        links=maplinks(72, 216, [79626, 79627]),
    ),
]

KEY_ROWS = [
    dict(
        year=1425, date='undated; nomenclator of the Romagna war of 1424-1425',
        title='Medici key with a Romagna nomenclator (Agnolo della Pergola, Piccinino, Faenza, Forlì, Oriolo ...): possible key for the Faenza 1425 letter',
        correspondents='unattributed ("Cifra"); Florentine commissioners in the Romagna (Averardo de\' Medici?)', place='Florence / Romagna',
        language='Italian (key)', region='Italy', period='15th century',
        shelfmark='Archivio di Stato di Firenze, Mediceo avanti il Principato, filza LXXII, doc. 180 (old c. 212)',
        folio_note='One leaf: alphabet with two homophones per letter, signs for da, se, si, et, non, con, per, che, quando, dove, come, del; '
                   'nomenclator of Visconti and papal captains (Agnolo della Pergola, Secco da Montagnana, Niccolò Guerrieri, Opicino d\'Alzate, '
                   'Cristoforo da Lavello, Taliano, Fornaino, messer Pandolfo [Malatesta], Niccolò Piccinino, Niccolò da Tolentino ...) and places '
                   '(Castrocaro, Oriolo, Forlì, Imola, Faenza, Cesena, Bologna) plus fanti a piè, gente d\'arme, cavalli. Inventory vol. 3: "« Cifra », n. 180".',
        cls='K',
        status='Key only, no ciphertext on the sheet. Agnolo della Pergola died in 1428; the names fit the Florentine-Milanese war in the '
               'Romagna of 1424-25, when Averardo de\' Medici was commissioner at Faenza.',
        why='The first candidate key for catalogue 337 / targets/medici1425 (Averardo de\' Medici and Piero Guicciardini, Faenza, 27 Oct 1425, '
            'cipher part unread; NOTES say "No key known"). Also a dated pre-1430 Florentine key for the Dieci commissioner family (florence1429).',
        importance=4,
        verify='Transcribe the table; compare with the Ricasoli 1424 key (targets/florence1429/key_extended.md); apply to the 1425 Faenza '
               'letter when its images are obtained; check MAP I nos. 89-207 (Averardo\'s Faenza file) for letters in this cipher.',
        links=maplinks(72, 180, [79530, 79531]),
    ),
    dict(
        year=1430, date='undated; nomenclator of the Lucca war of 1429-1433',
        title='"Cifra d\'Averardo con Astore": key of Averardo de\' Medici with Astorre (Gianni), Lucca war',
        correspondents="Averardo de' Medici <-> Astorre [Gianni] (commissioners)", place='Florence / Lucca front',
        language='Italian (key)', region='Italy', period='15th century',
        shelfmark='Archivio di Stato di Firenze, Mediceo avanti il Principato, filza LXXII, doc. 182 (old c. 214)',
        folio_note='One leaf: one-sign-per-letter alphabet; nomenclator: Dieci, fanti a piè, gente d\'arme, Berardino [della Carda], Ridolfo, '
                   'cavalli, Signore di Lucca, messer Ranaldo figliuolo del Signore di Lucca, Baldaccio d\'Anghiari, Duca di Milano, Niccolò '
                   'Piccinino, Genova, Tommaso da Campofregoso, Bartolomeo Orlandini, Rinaldo degli Albizzi, Cosimo, Pietrasanta, Motrone, '
                   'Castiglione di Garfagnana, Camaiore, Nozzano, Montecarlo, Lucca, amico, nimico, Signori, Averardo, Astore ... '
                   'Endorsed "Cifra d\'Averardo con Astore". Inventory vol. 3: n. 182.',
        cls='K',
        status='Key only, no ciphertext. The Lucca names date it c. 1430 (Averardo and Astorre Gianni were commissioners in the Lucca war).',
        why='An Averardo de\' Medici key five years after the Faenza letter (catalogue 337): a second candidate family for it, and the key '
            'for any Averardo/Astorre letter of 1430 in the Dieci Responsive or MAP.',
        importance=3,
        verify='Transcribe; test with lead 180 on the Faenza 1425 letter; look for Lucca-war cipher letters in MAP and Dieci Responsive 1430.',
        links=maplinks(72, 182, [79534, 79535]),
    ),
    dict(
        year=1485, date='undated (Laurentian chancery, c. 1470s-1490s)',
        title='Medici key sheets, MAP filza LXXII nos. 178-179, 181, 183-188 (Alamanni, ser Andrea da Bologna, Baccio Ugolini, Soderini, Biliotti, Cambini, "Diverse cifre")',
        correspondents="Lorenzo de' Medici's chancery <-> Piero Alamanni (178), ser Andrea da Bologna (179), Baccio Ugolini (181), Paolantonio "
                       "Soderini (183), Agostino Biliotti and Lionetto (184), Andrea Cambini (185); 186 'Cifra indiavolata'; 187 trial sheet; 188 'Diverse cifre'",
        place='Florence', language='Italian (keys)', region='Italy', period='15th century',
        shelfmark='Archivio di Stato di Firenze, Mediceo avanti il Principato, filza LXXII, docs. 178, 179, 181, 183-188 (old cc. 210-229)',
        folio_note='178: small alphabet with homophones and doubles (endorsed "Alamanni Piero"); 179: alphabet a-g = 1-9, h-y = Greek letters, '
                   'doubles, nomenclator (Papa, Reformando, Duca, Lorenzo, Sforza, Iacopo Pitti?, Firenze, popolo, Riformatori ...); 181: '
                   'nomenclator (Re Ferrando, Duca di Calabria, ... Piero di Lorenzo, Giuliano di Lorenzo); 183: alphabet with 3 homophones, '
                   'nulls, numbered nomenclator (Papa, Re di Napoli, Veneziani, Duca d\'Urbino ... Napoli, Siena, Arezzo); 184-185: alphabets, '
                   'doubles, "Nihil importantes", nomenclators (Duca di Ferrara, Bentivoglio, Gianfigliazzi, Sanseverino ...); 186 (cc. 218-219): '
                   'alphabet with 4-5 homophones; 187: scribbled trial sheet with a few cipher lines; 188 (cc. 222-229): alphabet, doubles, nulls '
                   'and a long code list.',
        cls='K',
        status='Keys only (187 has a few trial lines, no letter). None checked against the bare MAP leads yet.',
        why='The keys to try first on MAP leads 2309 (XLVIII 214), 2310 (LXXII 213-214: its digits-plus-Greek signs recall key 179), '
            '2311 (LXXIII 371), the LXXII 211/216 rows and any Laurentian cipher letter in MAP.',
        importance=3,
        verify='Transcribe each key; match sign inventories against the bare MAP letters; record matches.',
        links=maplinks(72, 178, [79526, 79528, 79532, 79536, 79538, 79540, 79542, 79546, 79548]),
    ),
]

MDP_ROWS = [
    dict(
        year=1549, date='23 Oct 1549 - 2 Jun 1554',
        title="Medoro Nucci d'Arezzo, Cosimo I's agent in Venice: all-figure cipher letters 1549-1554, bare",
        correspondents="Medoro Nucci d'Arezzo (Venice) -> Cosimo I / Cristiano Pagni", place='Venice', language='Italian (figure cipher)',
        region='Italy', period='1497-1559',
        shelfmark='Archivio di Stato di Firenze, Mediceo del Principato 394 A, cc. 1150-1151 and 1152-1153; 395, cc. 130-131; 401, cc. 177-178; '
                  '413, cc. 624-627; 427, cc. 37-38',
        folio_note='394 A cc. 1150 and 1152 (to Pagni, 23 Oct 1549): two letters, each about 30 lines of continuous figures closing in clear '
                   '("di Venetia ... 1549"), signed "D. V. S."; 395 c. 130 (to Cosimo, 8 Dec 1549) and 401 c. 177 (13 Jan 1551): full pages of figures; '
                   '413 cc. 624-625 (9 Feb 1552/3, "parzialmente in cifra") and cc. 626-627 ("Lettera in cifra", filed with them): figures; 427 '
                   'cc. 37-38 (2 Jun 1554): clear first page, full page of figures. Inventory vols. IV-VI mark them "In cifra" with no decipherment.',
        cls='A',
        status='Bare: no interlinear or marginal decipherment on any of these pages (checked at 1000-1600 px). Continuous figure cipher '
               '(two-figure groups, no separators), probably one key for the series.',
        why='A run of at least seven cipher letters from Cosimo I\'s Venice agent, 1549-1554, in one system: enough text for a '
            'ciphertext-only attack, and ASF\'s Cifrari II serie may hold the key.',
        importance=3, solvability=4, difficulty=3,
        verify='Transcribe two letters; test two-figure grouping and frequencies; look for the Nucci key in ASF Cifrari II serie '
               '(Chiavi delle cifre del Carteggio di Cosimo I 1536-1573) and on DECODE.',
        links=padlinks(982, '394 A', rng(528480, cc(1150, 1153))) + padlinks(983, '395', rng(528977, cc(130, 131)))
              + padlinks(989, '401', rng(537484, cc(177, 178))) + padlinks(1005, '413', rng(560558, cc(624, 627)))
              + padlinks(427, '427', rng(579078, cc(37, 38))),
    ),
    dict(
        year=1550, date='24 Nov 1550',
        title='Luigi Capponi, Florentine ambassador in France, to Cosimo I, Blois 24 Nov 1550: a full page of figure cipher, bare',
        correspondents='Luigi Capponi, ambassador -> Cosimo I', place='Blois', language='Italian (figure cipher)', region='Italy',
        period='1497-1559',
        shelfmark='Archivio di Stato di Firenze, Mediceo del Principato 400, cc. 311-312',
        folio_note='c. 311r clear (court news: the Cardinal of Ferrara, Tournon, Parma); c. 312r a full page (about 35 lines) of continuous figures. '
                   'Inventory vol. IV p. 209: "In cifra".',
        cls='A',
        status='Bare: no decipherment on or beside the page (checked at 1600 px).',
        why='A Florentine ambassador\'s cipher from the French court in 1550 (Parma war prelude), unread.',
        importance=3, solvability=3, difficulty=3,
        verify='Transcribe; look for Capponi\'s key in ASF Cifrari II serie and for other Capponi letters in filze 398-403 (vol. IV).',
        links=padlinks(988, '400', rng(536155, cc(311, 312))),
    ),
    dict(
        year=1551, date='December 1551 (filed between 16 and 18 Dec 1551)',
        title='"Cifra": a page of four-letter groups, filed in Cosimo I\'s correspondence, Dec 1551, bare',
        correspondents='unknown', place='not stated', language='unknown (letter cipher in four-letter groups)', region='Italy',
        period='1497-1559',
        shelfmark='Archivio di Stato di Firenze, Mediceo del Principato 406, c. 615',
        folio_note='One leaf, recto: about 20 lines of four-letter groups ("Bcam pdfe zxcb riab sdqz ..."), no clear word. Inventory vol. V p. 78: "Cifra., c. 615".',
        cls='A',
        status='Bare. A letter cipher in fixed four-letter groups, unlike the figure ciphers of the grand-ducal chancery.',
        why='An unusual system for the 1550s Medici archive (possibly polyalphabetic or a code); short and self-contained.',
        importance=3, solvability=3, difficulty=4,
        verify='Transcribe; frequency and IoC tests; check whether it is a key table rather than a text.',
        links=padlinks(997, '406', rng(547952, cc(615, 615))),
    ),
    dict(
        year=1552, date='January 1552 (filed with letters of 10-12 Jan 1552)',
        title='"Cifra": two pages of figure cipher filed in Cosimo I\'s correspondence, Jan 1552, bare',
        correspondents='unknown', place='not stated', language='Italian? (figure cipher)', region='Italy', period='1497-1559',
        shelfmark='Archivio di Stato di Firenze, Mediceo del Principato 407, cc. 86-87',
        folio_note='cc. 86r and 87r: full pages of continuous figures. Inventory vol. V p. 85: "Cifra., cc. 86-87".',
        cls='B',
        status='Bare (checked at 1600 px).',
        why='Unattributed grand-ducal cipher of 1552; sender may follow from neighbouring letters.',
        importance=2, solvability=3, difficulty=3,
        verify='Look at the versos and neighbours for an address; transcribe; compare with the Nucci series.',
        links=padlinks(998, '407', rng(548437, cc(86, 87))),
    ),
    dict(
        year=1550, date='18 Jul 1550 and Oct 1550',
        title='Two anonymous figure-cipher pieces to Cosimo I, 1550 (Mediceo 398 and 399), bare',
        correspondents='anonymous -> Cosimo I', place='Florence (398); not stated (399)', language='Italian (figure cipher)',
        region='Italy', period='1497-1559',
        shelfmark='Archivio di Stato di Firenze, Mediceo del Principato 398, cc. 191-192; 399, cc. 639-644',
        folio_note='398: c. 191r clear text under one line of figures, c. 192r a full page of figures with reader\'s dots under the groups; '
                   'inventory vol. IV p. 160 "*** a Cosimo I, Firenze 1550 luglio 18, In cifra". 399: cc. 639-643 clear, c. 644r about 12 lines '
                   'of figures; inventory p. 198 "*** a Cosimo I, s.l. s.d., cc. 639-644, In cifra".',
        cls='B',
        status='Bare: dots under figure groups on 398 c. 192 (segmentation marks), no letters written. Whether 398 c. 191 is a decipherment of c. 192 '
               'was not checked.',
        why='Unattributed cipher pieces in the 1550 run; low value until the sender is known.',
        importance=2, solvability=3, difficulty=3,
        verify='Read 398 c. 191 against c. 192 (a decipherment would make this a key source); transcribe 399 c. 644.',
        links=padlinks(986, '398', rng(532976, cc(191, 192))) + padlinks(987, '399', rng(535383, cc(639, 644))),
    ),
    dict(
        year=1554, date='May-June 1554',
        title='Three unattributed figure-cipher pieces of May-June 1554 (Mediceo 426-427: "Informazioni", "Biglietto", "Lettera in cifra"), bare',
        correspondents='unknown -> Cosimo I (Siena war)', place='not stated', language='Italian (figure cipher)', region='Italy',
        period='1497-1559',
        shelfmark='Archivio di Stato di Firenze, Mediceo del Principato 426, cc. 159-160; 427, c. 48; 427, c. 237',
        folio_note='426 c. 159 clear, c. 160 a page of figures ("Informazioni [in cifra]", s.l. s.d., vol. VI p. 113); 427 c. 48 "Biglietto in cifra" '
                   '(about 20 lines of figures with dots); 427 c. 237 "Lettera in cifra" (full page of figures). Inventory vol. VI pp. 113, 127, 129.',
        cls='B',
        status='Bare on all three (checked at 1600 px).',
        why='Unread cipher from the war of Siena; senders unknown, so value depends on attribution.',
        importance=2, solvability=3, difficulty=3,
        verify='Attribute from hands and neighbours; transcribe; compare figure systems with the Nucci series.',
        links=padlinks(426, '426', rng(577059, cc(159, 160))) + padlinks(427, '427', [(579100, 'c. 48r'), (579101, 'c. 48v'),
                                                                                      (579478, 'c. 237r'), (579479, 'c. 237v')]),
    ),
    dict(
        year=1557, date='30 Jan 1556 (Florentine style = 1557)',
        title='"Informazione" on Cardinal Rodolfo Pio da Carpi, Salvestro Aldobrandini and Carafa\'s demand on Venice, in the Gianfigliazzi-Orsini cipher, bare',
        correspondents='unknown informant -> Cosimo I', place='Rome?', language='Italian (figure cipher with marks)', region='Italy',
        period='1497-1559',
        shelfmark='Archivio di Stato di Firenze, Mediceo del Principato 457, c. 592',
        folio_note='One leaf: clear heading (date, 30 Jan), then two blocks of figures with superscript marks (about 25 lines). Inventory vol. VIII '
                   'p. 305 summarises the content and notes: "In cifra. Questa cifra viene usata ufficialmente da Bongianni Gianfigliazzi e '
                   'Giordano Orsini; cfr. A.S.F., Cifrari II serie, Chiavi delle cifre del Carteggio di Cosimo I dal 1536 al 1573; F. III."',
        cls='A',
        status='Bare on the page; the key is identified by the inventory and held in ASF (Cifrari II serie F. III), not online.',
        why='Key known and named, so a reading needs only the ASF key or a ciphertext-only solve; the inventory gives the topic as a crib.',
        importance=3, solvability=4, difficulty=2,
        verify='Ask for ASF Cifrari II serie F. III (Gianfigliazzi/Orsini table) or solve ciphertext-only using the inventory summary as crib.',
        links=padlinks(1016, '457', [(625000, 'c. 592r'), (625001, 'c. 592v')]),
    ),
]

rows = []
for r in MAP_ROWS:
    r.update(source=MAP_SRC, score_note=SCORE, access_note=MAP_ACCESS, prior_art=MAP_PRIOR, seen='image', needs_archive_scan='no')
    rows.append(r)
for r in MDP_ROWS:
    r.update(source=MDP_SRC, score_note=SCORE, access_note=MDP_ACCESS, prior_art=MDP_PRIOR, seen='image', needs_archive_scan='no')
    rows.append(r)
json.dump(rows, open(os.path.join(HERE, 'candidates.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(rows), 'rows')
# Key-only sheets (cls K): merge.py accepts only A/B/C rows, so they go to keys.json for the key ledger, not to leads.
keys = []
for r in KEY_ROWS:
    r.update(source=MAP_SRC, score_note=SCORE, access_note=MAP_ACCESS, prior_art=MAP_PRIOR, seen='image', needs_archive_scan='no')
    keys.append(r)
json.dump(keys, open(os.path.join(HERE, 'keys.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(keys), 'key sheets (keys.json)')
