"""Build candidates.json and keys.json for the second ASF Florence pass (6 Nov 2026).
Work list: the Mediceo del Principato (Carteggio universale) items marked "in cifra" / "parzialmente in cifra" on PAD that the
first pass (research/sweep_2026-11_asf_florence/) did not open, plus MAP filza LXXII paging. Rows come from images viewed
in this pass; see README.md. Leads 2307-2312 and 2320-2331 are not repeated."""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
B = 'https://archiviodistatofirenze.cultura.gov.it'
SCORE = 'Scored from the images viewed during the second ASF Florence pass, 6 Nov 2026 (research/sweep_2026-11_asf_florence_2/)'

MDP_SRC = ('ASF Mediceo del Principato, Carteggio universale (PAD images) + Carteggio universale di Cosimo I inventory PDFs '
           '(ASF Inventari on-line), second ASF Florence pass, Nov 2026')
MDP_ACCESS = ('scans public on ASF PAD (archividigitali), no login, curl works: unit page /archividigitali/unita-archivistica/?id=<ua> lists '
              'carte; each /archividigitali/riproduzione/?id=<id>&ua=<ua> names the ptif; IIIF /iipsrv/iipsrv.fcgi?IIIF=/data/iip-data/asfi/'
              'mdp_carteggio_universale/<filza>/<seq>_C_<carta>_<R|V>.ptif (2000 px). PAD holds filze 330-460 only (1537-1557).')
MDP_PRIOR = ('open as far as checked (6 Nov 2026): known.py finds nothing on the filza, the carta or the correspondent; the inventory notes '
             'no decipherment and none is written on or beside the page (neighbouring carte checked); ASF holds the chancery keys '
             '(Cifrari II serie, "Chiavi delle cifre del Carteggio di Cosimo I dal 1536 al 1573", 3 filze), not online; DECODE\'s ASFi '
             '"Governo Mediceo - cifre" volumes (R5687-R7459) are 17th-18th c.; Tomokiyo and Lasry not searched in this run.')

MAP_SRC = 'ASF Mediceo avanti il Principato (MAP) images, second ASF Florence pass, Nov 2026'
MAP_ACCESS = ('scans public on the ASF MAP site, no login, curl works: /map/ricerca/ricerca-su-filza/?f=<filza>&d=<doc> and IIIF '
              '/iipsrv/iipsrv.fcgi?IIIF=/data/iip-data/asfi/mediceo_avanti_principato/001000FF/A0000NNN.ptif (1600 px max)')
MAP_PRIOR = ('open as far as checked (6 Nov 2026): known.py finds nothing on the filza or document; not flagged as cipher in the MAP '
             'inventory; DECODE dumps in the repo have no ASF MAP ciphertext record; Tomokiyo and Lasry not searched in this run. Marco '
             'Vito (Vienna) works on encrypted MAP letters of 1486-1491 (research/medici_bia/README.md): check overlap.')


def padlinks(ua, filza, pairs):
    out = [{'href': f'{B}/archividigitali/unita-archivistica/?id={ua}', 'label': f'PAD unit {ua} (Mediceo del Principato {filza})'}]
    out += [{'href': f'{B}/archividigitali/riproduzione/?id={i}&ua={ua}', 'label': lab} for i, lab in pairs]
    return out


def maplinks(filza, doc, ids):
    out = [{'href': f'{B}/map/ricerca/ricerca-su-filza/?f={filza}&d={doc}&c=', 'label': f'MAP filza {filza}, doc. {doc}'}]
    out += [{'href': f'{B}/map/riproduzione/?id={i}', 'label': f'image id {i}'} for i in ids]
    return out


def rng(first, labels):
    return [(first + k, lab) for k, lab in enumerate(labels)]


def cc(a, b):
    out = []
    for c in range(a, b + 1):
        out += [f'c. {c}r', f'c. {c}v']
    return out


MDP_ROWS = []
MAP_ROWS = []
KEY_ROWS = []

# ---- Mediceo del Principato rows (one per correspondent/system); verdicts from images viewed at 900 px (2000 px where noted),
# with the carte on both sides checked ----

MDP_ROWS += [
    dict(
        year=1537, date='[May 1537] (annexed to Noceto\'s letter of 2 May 1537)',
        title='"Informazione" for Giovanni Noceto: a full page of figure cipher annexed to his letter to Francesco Campana, May 1537, bare',
        correspondents='Giovanni Noceto (Bagnone, Lunigiana) -> Francesco Campana, first secretary of Cosimo I',
        place='Bagnone', language='Italian? (figure cipher)', region='Italy', period='1497-1559',
        shelfmark='Archivio di Stato di Firenze, Mediceo del Principato 331, cc. 70-71',
        folio_note='c. 70r: Noceto\'s clear covering letter to Campana (Bagnone, 2 May 1537); c. 71r: about 25 lines of continuous figures, '
                   'no clear word; versos blank. Inventory vol. I p. 30: c. 70 "In allegato c. 71"; c. 71 "Informazione [per Giovanni '
                   'Noceto], [1537]", note "Cifra allegata a c. 70".',
        cls='A',
        status='Bare: no gloss on c. 71r; c. 70 is the covering letter and c. 72 an unrelated letter (Annibale da Napoli, Mantua). '
               'Seen at 900 px.',
        why='The earliest cipher piece found in the Carteggio universale (first year of Cosimo I), a self-contained page from the '
            'Lunigiana frontier, unread.',
        importance=3, solvability=3, difficulty=3,
        verify='Transcribe c. 71r at full size; test two-figure grouping; look for Noceto/Campana keys in ASF Cifrari II serie.',
        links=padlinks(373, '331', rng(472017, cc(70, 71))),
    ),
    dict(
        year=1537, date='4 Aug 1537',
        title='Giovanni Lanfredini, Lyon, 4 August 1537: letter with about twelve lines of cipher (figures and letter-signs) among clear text, bare',
        correspondents='Giovanni Lanfredini (Lyon) -> *** (addressee not named; Medici chancery)',
        place='Lyon', language='Italian (mixed figure and sign cipher with clear text)', region='Italy', period='1497-1559',
        shelfmark='Archivio di Stato di Firenze, Mediceo del Principato 333, c. 225',
        folio_note='c. 225r: clear letter (news from the French court) with two cipher blocks in the lower third (about 12 lines, '
                   'digits mixed with letter-like signs), c. 225v continues in clear, signed "Gio. Lan." and dated Lyon 4 Aug 1537. '
                   'Inventory vol. I p. 58: "Giovanni Lanfredini, Lione, 1537 agosto 4, c. 225", note "Parzialmente in cifra".',
        cls='B',
        status='Bare: no interlinear or marginal decipherment (cipher block cropped and checked at 900 px); cc. 224 and 226 are unrelated clear letters.',
        why='A Florentine in Lyon reporting to Cosimo I\'s chancery in the first months of the reign, in a mixed sign cipher.',
        importance=2, solvability=3, difficulty=3,
        verify='Transcribe at full size; look for other Lanfredini letters in filze 331-335 for more ciphertext.',
        links=padlinks(375, '333', rng(473753, cc(225, 225))),
    ),
    dict(
        year=1538, date='25 May 1538',
        title='Cardinal Innocenzo Cibo to Cosimo I from Nice, 25 May 1538 (the Nice congress): five sides mostly in figure cipher, bare',
        correspondents='Cardinal Innocenzo Cibo (Nice) -> Cosimo I', place='Nice', language='Italian (figure cipher with clear passages)',
        region='Italy', period='1497-1559',
        shelfmark='Archivio di Stato di Firenze, Mediceo del Principato 335, cc. 181-183',
        folio_note='c. 181r opens in clear ("Illmo et Eccmo S.re ... ") then runs into continuous figures; cc. 181v-183r almost all figures '
                   '(about 30 lines a side) with short clear passages; c. 183v ends in clear, dated Nice. c. 180 is a wrapper ("Lettera '
                   '... del Card.le Cibo ... da Nizza"). Inventory vol. I p. 79: "Card. Innocenzo Cibo, Nizza, 1538 maggio 25, cc. 181-183", '
                   'note "Prevalentemente in cifra. Duplicato."',
        cls='A',
        status='Bare: no gloss on any side; c. 180 is a wrapper and c. 184 an unrelated letter (Bastiano Bindi). The inventory calls it '
               'a duplicate; the first copy was not located.',
        why='A long cipher despatch from the papal-imperial-French congress of Nice (May-June 1538) by Cosimo I\'s kinsman and protector, unread.',
        importance=4, solvability=4, difficulty=3,
        verify='Transcribe; frequency test of the figure groups; search filze 335-336 for the original of the duplicate and for a decipherment.',
        links=padlinks(377, '335', rng(475175, cc(180, 183))),
    ),
    dict(
        year=1538, date='23 Mar 1538',
        title='Averardo Serristori, Florentine envoy at Barcelona, 23 March 1538: letter with figure-cipher passages, bare',
        correspondents='Averardo Serristori (Barcelona) -> Cosimo I', place='Barcelona', language='Italian (figure cipher with clear text)',
        region='Italy', period='1497-1559',
        shelfmark='Archivio di Stato di Firenze, Mediceo del Principato 335, cc. 132, 139',
        folio_note='c. 132r-v: clear despatch with several figure runs (about 15 lines of figures in all), water-stained in the middle; c. 139 '
                   'the clear postscript. Inventory vol. I p. 77: "Averardo Serristori, Barcellona, 1538 marzo 23, cc. 132,139", note '
                   '"Parzialmente in cifra".',
        cls='B',
        status='Bare: no gloss seen at 900 px; cc. 131 and 133 are unrelated clear letters. Water damage affects part of the figures.',
        why='Cipher of Cosimo I\'s envoy to Charles V\'s court in Spain in 1538, unread.',
        importance=2, solvability=3, difficulty=3,
        verify='Transcribe at full size; compare with Serristori\'s Rome cipher of 1554 (Mediceo 425, row below) and the interlinear-glossed 410 c. 1006.',
        links=padlinks(377, '335', rng(475079, cc(132, 132)) + rng(475093, cc(139, 139))),
    ),
    dict(
        year=1538, date='24 Dec 1538',
        title='Luzio Calvelli to Gaspare Masolini, chancellor of Prato, 24 December 1538: about eight lines of figures among clear text, bare',
        correspondents='Luzio Calvelli -> Gaspare Masolini, cancelliere di Prato (Florence)', place='not stated',
        language='Italian (figure cipher with clear text)', region='Italy', period='1497-1559',
        shelfmark='Archivio di Stato di Firenze, Mediceo del Principato 335, c. 570',
        folio_note='c. 570r: four lines of figures, six clear lines, three more lines of figures, dated 24 Dec 1538, signed "Lutio Calvelli"; '
                   'c. 570v address. Inventory vol. I p. 89: note "Parzialmente in cifra".',
        cls='B',
        status='Bare (900 px); c. 569 is an unrelated clear letter.',
        why='Short private figure cipher in the Medici chancery papers; low value until the context is known.',
        importance=1, solvability=3, difficulty=3,
        verify='Transcribe; compare with the Campana-network figures (row below).',
        links=padlinks(377, '335', rng(475959, cc(570, 570))),
    ),
    dict(
        year=1540, date='20 Dec 1539 - 4 Feb 1541 (and June 1542, not digitised)',
        title='Gerolamo del Vezzo and Niccolò Campana: the Medici intelligence correspondence from Modena, Piacenza and Bologna, 1539-1541, with figure runs and letter-pair codes, bare',
        correspondents='Gerolamo del Vezzo (secretary of Lucrezia Pico Rangoni, Modena; writing as from "Barzalona") -> Lorenzo Pagni and '
                       'Niccolò Campana (Bologna) -> Lorenzo Pagni, secretary of Cosimo I',
        place='Modena (as "Barzalona"), Piacenza, Bologna', language='Italian (figure groups and letter-pair codes such as EE, DD, KK, ZZ in clear text)',
        region='Italy', period='1497-1559',
        shelfmark='Archivio di Stato di Firenze, Mediceo del Principato 337, c. 330; 347, c. 597; 349, c. 42; 353, c. 337',
        folio_note='337 c. 330r-v (del Vezzo, "Barzalona" = Modena, 20 Dec 1539, to [Lorenzo Pagni], annexed to Campana\'s c. 335): a full '
                   'page with many figure runs and code pairs (EE, DD, KK, &&); 347 c. 597 (Campana, Bologna, 22 Nov 1540, to Pagni): two '
                   'figure passages; 349 c. 42 (del Vezzo, Piacenza, 4 Feb 1541, to Campana, annexed to c. 12): six figure runs; 353 c. 337 '
                   '(del Vezzo, "Barzalona", 27 Aug 1540, to Campana): mostly clear with codes ZZ, KK, HS and one figure run. Inventory '
                   'vol. I pp. 112, 209, 224, 279 note each "Parzialmente in cifra" (with "luogo di emissione: Barzalona" for 337 and 353). '
                   'The same network\'s June 1542 pieces (357 c. 558 "Cifra", an avviso of Bernardino Duretti; c. 564 del Vezzo "In codice") '
                   'are in 357 parte II, which PAD lists without images.',
        cls='A',
        status='Bare on all four: no interlinear or marginal decipherment; the adjacent carte (337 cc. 329, 331, 335; 347 cc. 596, 598; '
               '349 cc. 41, 43, 12; 353 cc. 336, 338) are clear letters of the network, none a decipherment.',
        why='A cover-name intelligence network run by Cosimo I\'s secretaries into Farnese and Este territory (1539-42), with a shared '
            'figure code: several letters for one system, unread.',
        importance=3, solvability=3, difficulty=3,
        verify='Transcribe the four letters; build the figure-group inventory; the clear context names many persons (Farnese, Rangoni, '
               'the "Marchese"), useful as cribs; check 357 parte II at ASF.',
        links=padlinks(379, '337', rng(477367, cc(330, 330)) + rng(477377, cc(335, 335))) + padlinks(1028, '347', [(642575, 'c. 597r'), (642576, 'c. 597v')])
              + padlinks(1030, '349', [(643545, 'c. 42r'), (643546, 'c. 42v'), (643485, 'c. 12r'), (643486, 'c. 12v')])
              + padlinks(386, '353', rng(481121, cc(336, 338))),
    ),
    dict(
        year=1544, date='4 Jun 1544',
        title='Cristiano Pagni, Tortona, 4 June 1544: four lines of figure cipher closing a clear despatch on the Piedmont campaign, bare',
        correspondents='Cristiano Pagni (with the imperial army, Tortona) -> Cosimo I', place='Tortona',
        language='Italian (figure cipher)', region='Italy', period='1497-1559',
        shelfmark='Archivio di Stato di Firenze, Mediceo del Principato 366, cc. 39-40, 42',
        folio_note='cc. 39r-42r clear (the Florentine infantry at Tortona, Count of Santa Fiora); c. 42v, after the date "Da Tortona alli iiii di '
                   'Giugno MDXLIIII", four lines of continuous figures (about 200 digits), then the subscription. Inventory vol. II p. 245: '
                   'note "Parzialmente in cifra".',
        cls='B',
        status='Bare (900 px). Short.',
        why='Short cipher postscript by the future first secretary of Cosimo I; only useful with other Pagni ciphertext.',
        importance=1, solvability=2, difficulty=3,
        verify='Transcribe; compare with the figure systems of the 1540s rows here.',
        links=padlinks(399, '366', rng(494478, cc(39, 42))),
    ),
    dict(
        year=1547, date='[Aug 1547] (filed with letters of 3-23 Aug 1547)',
        title='Copy of a cipher letter of Cardinal Alessandro Farnese (to Pier Luigi Farnese), intercepted, August 1547: a full page of figures, bare',
        correspondents='Cardinal Alessandro Farnese -> [Pier Luigi Farnese, duke of Parma and Piacenza] (copy made in Cosimo I\'s chancery)',
        place='not stated (Rome?)', language='Italian (figure cipher)', region='Italy', period='1497-1559',
        shelfmark='Archivio di Stato di Firenze, Mediceo del Principato 384, c. 78',
        folio_note='c. 78r headed "Copia / D\'una littera del card.le Farnese", then about 35 lines of continuous figures, a few clear words at the '
                   'foot. Inventory vol. III p. 103: "(Alessandro Farnese) a (Pier Luigi Farnese), s.l., s.d., c. 78", note "Copia di una lettera in cifra".',
        cls='A',
        status='Bare (checked at 2000 px). Its neighbours are glossed: c. 70 (Valerio Amanio to Pier Luigi Farnese, Venice) has its '
               'decipherment at c. 71 ("Deciferato di M. Valerio"), and c. 76 (copy of a chapter of the French ambassador\'s letter, Rome '
               '10 Aug 1547) has its decipherment at c. 79 (same heading); c. 78 has none (c. 80 is an unrelated letter).',
        why='An intercepted Farnese cipher of the weeks before Pier Luigi\'s murder (Sept 1547), unread; a Farnese family key of 1541-42 '
            'is already worked in this repo (targets/vatican5), and the glossed Amanio and French-ambassador copies in the same gathering '
            'show the chancery was reading Farnese traffic.',
        importance=4, solvability=4, difficulty=3,
        verify='Transcribe; test against the vatican5 Farnese key family; read cc. 70-71 and 76-79 to see which systems the chancery had broken.',
        links=padlinks(969, '384', rng(513450, cc(70, 71)) + rng(513462, cc(76, 79))),
    ),
    dict(
        year=1549, date='26 Dec 1548 - 18 Apr 1549',
        title='Giovanni Girolamo de\' Rossi, bishop of Pavia, Milan, to Cosimo I, 1548-49: figure cipher with "+" separators (full-page insert of 7 March 1549), bare',
        correspondents="Giovanni Girolamo de' Rossi, bishop of Pavia (Milan) -> Cosimo I", place='Milan',
        language='Italian (figure cipher, groups divided by "+")', region='Italy', period='1497-1559',
        shelfmark='Archivio di Stato di Firenze, Mediceo del Principato 391, c. 287; 392, cc. 47-49; 393, cc. 261-263',
        folio_note='391 c. 287 (26 Dec 1548): two lines of figures, struck through, in a clear letter (cc. 298-299 the opening, clear); '
                   '392 c. 49 (7 Mar 1549), headed "Inserto": a full page (about 30 lines) of figures in groups joined by "+", one line '
                   'repeated at the foot of cc. 47-48; 393 c. 263 (18 Apr 1549): about nine lines of the same "+" figures after a clear '
                   'letter (cc. 261-262). Inventory vol. III p. 181 and vol. IV pp. 5, 20 note "Parzialmente in cifra". The inventory\'s '
                   'other de\' Rossi cipher pieces, 391 A c. 601 ("Lettera in cifra", 25 Jan 1549, vol. III plate list) and cc. 926-927 '
                   '(20 Feb 1549), are beyond PAD\'s 391 A, which stops at c. 517.',
        cls='A',
        status='Bare: no decipherment on the pages or on the adjacent carte (391 cc. 286, 288; 392 cc. 46, 50; 393 cc. 260, 264 are clear letters).',
        why='A run of cipher from Cosimo I\'s informant in imperial Milan (Ferrante Gonzaga\'s government), 1548-49; the full-page insert '
            'gives enough text for an attack. Lead 2329 (399 cc. 643-644, pencil "V.o di Pavia (?)") may belong to the same bishop, but its '
            'figures have no "+" separators.',
        importance=3, solvability=4, difficulty=3,
        verify='Transcribe 392 c. 49 and 393 c. 263; compare group structure with lead 2329; obtain 391 A cc. 601, 926-927 from ASF.',
        links=padlinks(977, '391', rng(522608, cc(287, 287)) + rng(522629, cc(298, 299))) + padlinks(979, '392', rng(524143, cc(47, 49)))
              + padlinks(980, '393', rng(525134, cc(261, 263))),
    ),
    dict(
        year=1554, date='9 Apr 1554',
        title='Averardo Serristori, ambassador in Rome, 9 April 1554 (duplicate): a full-page figure-cipher "Inserto" and cipher lines, bare',
        correspondents='Averardo Serristori, Florentine ambassador (Rome) -> Cosimo I', place='Rome', language='Italian (figure cipher)',
        region='Italy', period='1497-1559',
        shelfmark='Archivio di Stato di Firenze, Mediceo del Principato 425, cc. 192-195',
        folio_note='c. 192r clear despatch; c. 193r headed "Inserto": a full page (about 30 lines) of continuous figures; c. 194r ends with three '
                   'lines of figures; c. 195r clear with a few figure groups. Inventory vol. VI p. 108 (note 56): "Duplicato, parzialmente '
                   'in cifra. In allegato cc. 175-176, 173" (c. 173 a short letter, cc. 175-176 a clear "Memoriale" of 7 April).',
        cls='A',
        status='Bare (c. 193 checked at 2000 px): no decipherment on the page; c. 191 is blank, c. 196 an unrelated letter, and the annexed '
               'memoriale (cc. 175-176) is a separate clear text, not a decipherment of c. 193.',
        why='The Florentine ambassador\'s cipher from Julius III\'s court during the war of Siena, unread; ASF\'s 410 c. 1006 (Serristori, '
            'interlinear decipherment, per the inventory) may give the key.',
        importance=3, solvability=4, difficulty=3,
        verify='Transcribe c. 193; open 410 c. 1006 (glossed Serristori informazione) and test its key; look for the original of this duplicate.',
        links=padlinks(425, '425', rng(576334, cc(173, 176)) + rng(576372, cc(192, 195))),
    ),
    dict(
        year=1554, date='s.d. [June 1554]',
        title='"Brano di lettera" apparently to the pope (Ferrara, Parma, the duke of Ferrara named), about five lines of figure cipher, bare',
        correspondents='unknown -> the pope (Julius III?), per the inventory', place='not stated', language='Italian (figure cipher with clear text)',
        region='Italy', period='1497-1559',
        shelfmark='Archivio di Stato di Firenze, Mediceo del Principato 427, c. 521',
        folio_note='c. 521r: clear text (fragment, beginning lost) then about five lines of figures. Inventory vol. VI p. 132: "Brano di lettera '
                   'in parte in cifra, mancante della parte iniziale. Sembra indirizzata al Papa (Giulio III?) ...", s.l., s.d.',
        cls='B',
        status='Bare (900 px); cc. 520 and 522 are unrelated clear letters.',
        why='Short; value depends on identifying the writer.',
        importance=1, solvability=2, difficulty=3,
        verify='Transcribe; compare with the other 1554 figure systems (leads 2330, 2325).',
        links=padlinks(427, '427', rng(579984, cc(521, 521))),
    ),
    dict(
        year=1554, date='[late July 1554]',
        title='"Brano di lettera": a slip with four lines of figure cipher among clear lines, July 1554, bare',
        correspondents='unknown', place='not stated', language='Italian (figure cipher with clear text)', region='Italy', period='1497-1559',
        shelfmark='Archivio di Stato di Firenze, Mediceo del Principato 433, c. 797',
        folio_note='c. 797: a cut slip, clear lines alternating with about four lines of figures. Inventory vol. VII p. 126: "Brano di lettera", note 91 "Parzialmente in cifra".',
        cls='B',
        status='Bare (900 px); cc. 796 (Roberto Strozzi) and 798 are unrelated clear letters.',
        why='Short fragment from the war of Siena.',
        importance=1, solvability=2, difficulty=3,
        verify='Transcribe; compare with other 1554 figure systems.',
        links=padlinks(433, '433', rng(590730, cc(797, 797))),
    ),
    dict(
        year=1554, date='[c. 24 Dec 1554]',
        title='"Avviso" on contacts in Switzerland between Gualtiero Rollo and the French ambassador: about eight lines of figure cipher, bare',
        correspondents='unknown informant -> Cosimo I', place='not stated', language='Italian (figure cipher with clear text)',
        region='Italy', period='1497-1559',
        shelfmark='Archivio di Stato di Firenze, Mediceo del Principato 436, c. 900',
        folio_note='c. 900r: about eight lines of figures, then five clear lines on the Swiss. Inventory vol. VII p. 218: "Avviso sui contatti in '
                   'Svizzera tra Gualtiero Rollo e l\'Ambasciatore di Francia", note 125 "Parzialmente in cifra".',
        cls='B',
        status='Bare (900 px); cc. 899 and 901 are unrelated clear letters.',
        why='Short intelligence report on French recruiting in Switzerland during the war of Siena.',
        importance=2, solvability=2, difficulty=3,
        verify='Transcribe; compare with the Babbi and Griffoli figure systems.',
        links=padlinks(436, '436', rng(595075, cc(900, 900))),
    ),
    dict(
        year=1555, date='14 Mar 1555',
        title='Baldovino del Monte, Rome, 14 March 1555: cipher passages in his sign cipher, bare, with a decipherment of the same system in Mediceo 436',
        correspondents="Baldovino Ciocchi del Monte (brother of Julius III), Rome -> Cosimo I", place='Rome',
        language='Italian (letter-sign cipher)', region='Italy', period='1497-1559',
        shelfmark='Archivio di Stato di Firenze, Mediceo del Principato 443, cc. 678-679',
        folio_note='c. 678r clear; c. 679r: about eight lines of cipher at the top and ten at the foot, in small letter-like signs, signed '
                   '"S. Bal(dovino)"; dated Rome 14 Mar 1555. Inventory vol. VII p. 376, note 89 "Parzialmente in cifra".',
        cls='A',
        status='Bare (900 px); c. 677 (Leonida Malatesta) and c. 680 are unrelated. Key material for this system: Mediceo 436 cc. 849-850 '
               '(Baldovino, 21 Dec 1554, same sign set) with its decipherment at c. 851 (inventory note 117), and 443 c. 78 (6 Jan 1555, '
               'full page) followed by c. 79, a clear unsigned "Informazione sull\'atteggiamento del Papa" that is very likely its decipherment.',
        why='The pope\'s brother writing to Cosimo I in cipher in the last weeks of Julius III; a key can be rebuilt from the two glossed '
            'letters and this one read.',
        importance=3, solvability=5, difficulty=2,
        verify='Build the key from 436 cc. 849-851 (and 443 cc. 78-79); apply to c. 679; ASF Cifrari II serie F. III has a key attributed '
               'to Baldovino that the inventory says does not fit 443 c. 78.',
        links=padlinks(443, '443', rng(602630, cc(678, 679)) + rng(601430, cc(78, 78))) + padlinks(436, '436', rng(594973, cc(849, 851))),
    ),
    dict(
        year=1555, date='1 Feb 1555 - 3 Jan 1556',
        title='Marcello Griffoli, Cosimo I\'s commissioner in Siena, in his figure cipher, 1555-56: a full page and a long block, bare; a decipherment of the system exists',
        correspondents='Marcello Griffoli (Siena) -> Cosimo I', place='Siena', language='Italian (figure cipher)', region='Italy', period='1497-1559',
        shelfmark='Archivio di Stato di Firenze, Mediceo del Principato 443, c. 315; 451, cc. 25-26',
        folio_note='443 c. 315r (1 Feb 1555): a full page (about 30 lines) of figures; inventory vol. VII p. 362, note 40: "In cifra. Questa '
                   'cifra viene usata ufficialmente da Marcello Griffoli, cfr. A.S.F., Cifrari II serie ... F. III". 451 c. 25r (3 Jan 1556): '
                   'about 30 lines of figures after the salutation, c. 26r clear; inventory vol. VIII p. 137, note 3 "Parzialmente in cifra".',
        cls='A',
        status='Bare (900 px); adjacent carte (443 c. 314; 451 cc. 24, 27) are other writers\' clear letters. Key material: 443 cc. 316-318 '
               '(Griffoli, 2 Feb 1555), partly in cipher, with its decipherment at c. 317 (inventory note 41); the key itself in ASF Cifrari II serie F. III.',
        why='Griffoli governed Siena for Cosimo I after its surrender (1555); his figure cipher is keyed in the archive and a decipherment '
            'of the same system survives, so these pieces are readable.',
        importance=3, solvability=5, difficulty=2,
        verify='Rebuild the key from 443 cc. 316-318 (cipher and decipherment); apply to 443 c. 315 and 451 c. 25.',
        links=padlinks(443, '443', rng(601904, cc(315, 318))) + padlinks(1010, '451', rng(614508, cc(25, 26))),
    ),
    dict(
        year=1555, date='[May 1551] - [Apr 1555]',
        title='Francesco Babbi\'s cipher avvisi from Ferrara, 1551-1555: three full pages of figures, bare; a decipherment of his system exists',
        correspondents='Francesco Babbi, Florentine agent at Ferrara -> Cosimo I', place='Ferrara', language='Italian (figure cipher)',
        region='Italy', period='1497-1559',
        shelfmark='Archivio di Stato di Firenze, Mediceo del Principato 402 A, c. 675; 444, c. 127; 445, c. 386',
        folio_note='402 A c. 675r (s.d., filed 9 May 1551, to ***): a full page of figures (vol. IV p. 271); 444 c. 127r ("Avviso in cifra di '
                   '[Francesco Babbi]", [1555], filed with Babbi\'s letters of 18-19 Mar 1555): a full page; 445 c. 386r (same title, filed '
                   'inside Babbi\'s letter of 14 Apr 1555, cc. 385, 387): a full page. Inventory vol. VII pp. 389, 412 and index: "Babbi '
                   'Francesco, avviso in cifra, 1555: 444, 127; 445, 368; 386".',
        cls='A',
        status='Bare: no gloss on the three pages; neighbours are clear (402 A c. 674, c. 676 Ferrari; 444 cc. 126, 128 avvisi; 445 cc. 385, 387 '
               'Babbi\'s covering letter). Key material: 445 c. 368 (Babbi avviso) with its decipherment at c. 367 (inventory note 52, '
               '"Questa cifra è usata ufficialmente da Francesco Babbi ... La decifrazione è a c. 367"), 444 c. 113 (Babbi, 18 Mar 1555, '
               'interlinear decipherment, note 9), and the key in ASF Cifrari II serie F. III.',
        why='A series in one keyed system from the Este court during the war of Siena; the glossed siblings let the key be rebuilt and the bare avvisi read.',
        importance=3, solvability=5, difficulty=2,
        verify='Rebuild the key from 445 cc. 367-368 and 444 c. 113; apply to the three bare pages; check 402 A c. 845 (Babbi insert sent '
               'via "il Sarto", not found on the PAD carte 845-846).',
        links=padlinks(991, '402 A', rng(540096, cc(675, 675))) + padlinks(444, '444', rng(603167, cc(127, 127)))
              + padlinks(445, '445', rng(604330, cc(367, 368)) + rng(604368, cc(386, 386))),
    ),
    dict(
        year=1555, date='s.d. [late March 1555]',
        title='Anonymous full-page cipher to Cristiano Pagni, March 1555: mixed figures and letters (A, S, x as markers), bare',
        correspondents='[...] -> Cristiano Pagni, secretary, Florence', place='[...]',
        language='unknown (cipher of digits mixed with letters and signs)', region='Italy', period='1497-1559',
        shelfmark='Archivio di Stato di Firenze, Mediceo del Principato 444, c. 315',
        folio_note='c. 315r: about 30 lines of cipher mixing digits with letters (A, S, x, Q-like signs) and a short clear opening line; '
                   'c. 315v address to Cristiano Pagni. Inventory vol. VII p. 396: "[...] a Cristiano Pagni segr., Firenze, [...], s.d., c. 315", note 38 "In cifra".',
        cls='A',
        status='Bare (900 px); cc. 314 and 316 are unrelated clear letters. The system differs from the figure ciphers of Babbi, Griffoli and Nucci.',
        why='A full page in a distinct mixed cipher addressed to Cosimo I\'s first secretary, sender suppressed; unread.',
        importance=2, solvability=3, difficulty=3,
        verify='Transcribe at full size; read the verso for any endorsement; compare with 427 c. 237 / c. 48 (lead 2330).',
        links=padlinks(444, '444', rng(603543, cc(315, 315))),
    ),
    dict(
        year=1555, date='27 Nov 1555',
        title='Mario Sforza, Santa Fiora, to his brother Sforza Sforza, 27 November 1555: about ten lines of figure cipher among clear text, bare',
        correspondents='Mario Sforza (Santa Fiora) -> Sforza Sforza, count of Santa Fiora', place='Santa Fiora',
        language='Italian (figure cipher with clear text)', region='Italy', period='1497-1559',
        shelfmark='Archivio di Stato di Firenze, Mediceo del Principato 448, cc. 549-550',
        folio_note='c. 549r: clear opening, then about ten lines of figures with clear words, clear close; c. 550 a clear slip. Inventory '
                   'vol. VIII p. 63, note 63 "Parzialmente in cifra. Allegata a c. 557 e con c. 557 allegata a cc. 560-561".',
        cls='B',
        status='Bare (900 px); c. 548 (Cornelio Bentivoglio) and c. 551 are unrelated.',
        why='A family cipher of the Sforza di Santa Fiora (imperial commanders in the Siena war), forwarded to Cosimo I.',
        importance=2, solvability=3, difficulty=3,
        verify='Transcribe; open cc. 557, 560-561 (the covering letters).',
        links=padlinks(448, '448', rng(609695, cc(549, 550))),
    ),
]

KEY_ROWS += [
    dict(
        year=1555, date='10 Sep 1555',
        title='Cifrario of Cosimo I\'s chancery with don Bernardino de Mendoza at Naples, 10 September 1555',
        correspondents='Cosimo I\'s chancery <-> don Bernardino de Mendoza (Naples)', place='Florence / Naples',
        language='Italian (key)', region='Italy', period='1497-1559',
        shelfmark='Archivio di Stato di Firenze, Mediceo del Principato 448, c. 277',
        folio_note='One leaf headed "1555 ... Con il S. Don Ber.no di Mendozza a Napoli": alphabet with one or two figure values per letter, '
                   'nulls, and a nomenclator in three columns numbered to about 900 (Papa, Imperatore, Re, Francesi, Siena, Roma, Napoli, '
                   'Milano, Piombino, Orbetello ...). Inventory vol. VIII p. 41 and index: "cifrario usato a Napoli con Bernardino de Mendoza, '
                   '1555 settembre 10, 448, 277".',
        cls='K',
        status='Key only. Not checked against any letter; Mendoza\'s Naples letters of 1555-57 in filze 448-460 are the place to look.',
        why='A dated key of the Siena-war chancery: any bare Mendoza letter in Mediceo 448-470 can be read with it.',
        importance=3,
        verify='Transcribe the table; search filze 448-470 (vol. VIII-IX inventory) for Mendoza letters in cipher.',
        links=padlinks(448, '448', rng(609151, cc(277, 277))),
    ),
]

# ---- MAP filza LXXII, docs. 160-240 paged leaf by leaf at 900 px (rectos and versos) ----
MAP_ROWS += [
    dict(
        year=1482, date='3 Jul - 4 Sep 1482',
        title='Bernardo Rucellai, Florentine orator in Milan, July-September 1482: four bare letters in his sign cipher, with three glossed siblings in the same filza',
        correspondents="Bernardo Rucellai, orator in Milan -> Lorenzo de' Medici", place='Milan',
        language='Italian (sign cipher with clear words)', region='Italy', period='15th century',
        shelfmark='Archivio di Stato di Firenze, Mediceo avanti il Principato, filza LXXII, docs. 196, 200, 202, 206',
        folio_note='Each a single leaf, recto, opening in clear and running into long sign-cipher passages between clear words: 196 '
                   '(old c. 238; inventory "(Milano, 1482 lug. 3)", about 20 lines), 200 (c. 243; "lug. 19", about 15 lines), 202 '
                   '(c. 245; "lug. 11", about 15 lines), 206 (c. 249; "set. 4", about 8 lines with dotted gaps). MAP inventory vol. 3, '
                   'filza LXXII: "(Bernardo Rucellai). (Milano, 1482 lug. 3), n. 196; (lug. 15), n. 201; lug. 19, n. 200; (lug. 11), n. 202; '
                   '(ago. 30), n. 204; n. 205; (set. 4), n. 206; (giu. 3), n. 211"; none flagged as cipher.',
        cls='A',
        status='Bare: no interlinear or marginal decipherment on 196, 200, 202 or 206 (900 px, crops). Key material in the same run: 201 '
               '(15 Jul) carries interlinear glosses over many cipher groups; 205 is the clear text of 204 (30 Aug; it opens with the '
               'same words, "Noi diremo che noi contraffacciamo ..."); 208 is the decipherment of 207 (inventory "Decifrato della n. 207"). '
               'Lead 2323 (LXXII 211) is the 3 June 1482 letter of this series (inventory attribution to Rucellai).',
        why='A run of cipher despatches from Milan in the War of Ferrara (1482), with three glossed letters of the same system beside '
            'them: a key can be rebuilt and the four bare letters (and lead 2323) read.',
        importance=4, solvability=5, difficulty=2,
        verify='Rebuild the sign table from 204/205, 207/208 and the glosses on 201; apply to 196, 200, 202, 206 and lead 2323 (211); '
               'compare with the 1483 Rucellai cipher of XLVIII 214 (catalogue), said to use a different sign set.',
        links=maplinks(72, 196, [79582, 79583]) + maplinks(72, 200, [79594, 79595]) + maplinks(72, 202, [79598, 79599])
              + maplinks(72, 206, [79606, 79607]) + maplinks(72, 201, [79596, 79597]) + maplinks(72, 204, [79602, 79603, 79604, 79605])
              + maplinks(72, 207, [79608, 79609, 79610, 79611]),
    ),
    dict(
        year=1513, date='23 Oct 1513',
        title='Roberto Acciaiuoli, Florentine orator in France, Amiens 23 October 1513: two sides of homophonic cipher, bare; a glossed letter of the same day gives the key',
        correspondents="Roberto Acciaiuoli, orator at the French court -> [Giuliano de' Medici / the Medici in Florence]", place='Amiens',
        language='Italian (sign cipher with superscript homophone marks)', region='Italy', period='1497-1559',
        shelfmark='Archivio di Stato di Firenze, Mediceo avanti il Principato, filza LXXII, doc. 192 (old c. 234)',
        folio_note='One leaf: recto opens "Mag.ce Vir" then about 15 lines of letter-signs, many with small superscript digits (3, 4, 5); the '
                   'verso about 14 more lines of the same. MAP inventory vol. 3: "Robertus Acciarolus, orator. Ex Amiens, 1513 ott. 23, n. 192" '
                   '(no cipher flag).',
        cls='A',
        status='Bare (900 px, recto and verso). Key material: doc. 190 (c. 232), Acciaiuoli\'s cipher letter of the same day in the same '
               'system (signed "Robertus Acciarolus", "Ex Amiens die xxiii Octobris MDXIII"), and doc. 191 (c. 233), "Copia di lettera di '
               'Ruberto Acciaioli da Amiens ...", which repeats the text of 190 in clear ("Oltre alle lettere publiche ... Sanseverino ... '
               'arrivò adì xx la sera"): a full plaintext for 190.',
        why='The Florentine ambassador at Louis XII\'s court in the year after the Medici restoration; the key can be rebuilt from 190/191 '
            'and 192 read.',
        importance=3, solvability=5, difficulty=2,
        verify='Align 190 with 191 to rebuild the homophonic table (superscripts included); apply to 192 r-v.',
        links=maplinks(72, 192, [79574, 79575]) + maplinks(72, 190, [79570, 79571, 79572, 79573]),
    ),
    dict(
        year=1512, date='8 Sep 1512',
        title='Piero Dovizi da Bibbiena, Venice, 8 September 1512: two sides of clear text with many sign-cipher runs, bare',
        correspondents="Piero Dovizi da Bibbiena (Venice) -> [the Medici: Cardinal Giovanni or Giuliano de' Medici]", place='Venice',
        language='Italian (sign cipher with clear words)', region='Italy', period='1497-1559',
        shelfmark='Archivio di Stato di Firenze, Mediceo avanti il Principato, filza LXXII, doc. 189 (old cc. 230-231)',
        folio_note='cc. 230r-231r: a long letter in clear with frequent cipher runs in single letter-like signs (several runs a line, some '
                   'underlined), naming Bernardo Rucellai and ser Giovanni di ser Bartolomeo in clear. MAP inventory vol. 3: "Petrus (Dovizi '
                   'da) Bibiena. Venetiis, 1512 set. 8, n. 189". A separate strip, doc. 189 bis, is a partial cipher alphabet (keys.json).',
        cls='A',
        status='Bare (900 px; crops of both sides): no interlinear gloss; 190-191 are Acciaiuoli\'s 1513 pair, not a decipherment of this '
               'letter. The 189 bis alphabet strip was not matched against these signs.',
        why='A Medici agent in Venice writing in cipher a week after the Medici returned to Florence (Sept 1512); many short runs between '
            'clear words make it a good crib target.',
        importance=3, solvability=4, difficulty=3,
        verify='Transcribe; compare the sign set with the 189 bis strip and the LXXII key sheets 178-188; solve from the clear context.',
        links=maplinks(72, 189, [79564, 79565, 79566, 79567]),
    ),
]

KEY_ROWS += [
    dict(
        year=1481, date='24 Aug 1481',
        title='Cipher letter of 24 August 1481 with its own letter-by-letter interlinear decipherment (digits and Greek-like signs)',
        correspondents='unsigned (initial only) -> Medici circle', place='not stated', language='Italian (cipher with interlinear decipherment)',
        region='Italy', period='15th century',
        shelfmark='Archivio di Stato di Firenze, Mediceo avanti il Principato, filza LXXII, doc. 172 (old c. 204)',
        folio_note='One small leaf: two clear lines, then about six lines of cipher in digits and Greek-like signs with a clear letter written '
                   'over each sign; dated "xxiiii augusti 1481". MAP inventory vol. 3: "... 1481 ago. 24, n. 172".',
        cls='K',
        status='Key source (glossed), flagged by vetting batch n10. Its digits-plus-Greek style recalls key sheet LXXII 179 (ser Andrea da '
               'Bologna: a-g = 1-9, h-y Greek letters) and lead 2310 (LXXII 213-214).',
        why='A worked example of a 1481 Medici cipher: the sign values can be read directly and tested on lead 2310 and on key sheet 179.',
        importance=3,
        verify='Transcribe sign/letter pairs; compare with key sheet 179 and the slips of lead 2310.',
        links=maplinks(72, 172, [79512, 79513]),
    ),
    dict(
        year=1492, date='24 Jan 1492',
        title='Piero Alamanni, Naples, 24 January 1492: postscript in cipher with interlinear decipherment, the test text for key sheet LXXII 178 ("Alamanni Piero")',
        correspondents="Piero Alamanni, Florentine orator in Naples -> Lorenzo de' Medici", place='Naples',
        language='Italian (sign cipher with interlinear decipherment)', region='Italy', period='15th century',
        shelfmark='Archivio di Stato di Firenze, Mediceo avanti il Principato, filza LXXII, doc. 177 (old c. 209)',
        folio_note='One leaf: clear text, then about 20 lines of sign cipher in the lower half with clear words written above most cipher '
                   'runs. MAP inventory vol. 3: "Poscritto alla lettera n. 176 (Napoli, 1492 gen. 24), n. 177" (176: "Petrus de Alamannis, '
                   'eques et orator ... Neapoli, 1492 gen. 24").',
        cls='K',
        status='Glossed (key source). Not yet compared with key sheet LXXII 178 (endorsed "Alamanni Piero").',
        why='Confirms or completes the Alamanni key (178) and gives the key for any bare Alamanni letter of 1489-92 in MAP.',
        importance=3,
        verify='Compare its sign/letter pairs with key sheet 178; then search MAP for bare Alamanni letters.',
        links=maplinks(72, 177, [79524, 79525]),
    ),
    dict(
        year=1500, date='undated',
        title='Partial cipher alphabet on a strip filed as LXXII doc. 189 bis',
        correspondents='unattributed', place='not stated', language='Italian (key fragment)', region='Italy', period='unknown',
        shelfmark='Archivio di Stato di Firenze, Mediceo avanti il Principato, filza LXXII, doc. 189 bis',
        folio_note='A narrow strip: the alphabet a-x in one line with one to three cipher values under some letters (+, II, C under a; m, f, '
                   'circled-dot signs, 7, 8, a division sign, pi, 6, 9, o, p and q-like signs under others).',
        cls='K',
        status='Key fragment only; filed after Bibbiena\'s 1512 letter (doc. 189), whose signs it does not obviously match.',
        why='A small key that may belong to one of the bare sign-cipher letters of LXXII or LXXIII.',
        importance=1,
        verify='Compare with the sign sets of LXXII 189, 196-211 and leads 2310-2311.',
        links=maplinks(72, 189, [79568, 79569]),
    ),
    dict(
        year=1482, date='1482 (inventory: Bernardo Rucellai, Milan, 28 Mar [1482]; vetting n10: endorsed June 1482)',
        title='Cipher slip LXXII 209 with its clear decipherment 210 (Bernardo Rucellai, 1482), a second Rucellai system',
        correspondents="Bernardo Rucellai (Milan) -> Lorenzo de' Medici", place='Milan', language='Italian (cipher slip and decipherment)',
        region='Italy', period='15th century',
        shelfmark='Archivio di Stato di Firenze, Mediceo avanti il Principato, filza LXXII, docs. 209-210 (old cc. 252-253)',
        folio_note='209: an oblong slip of about 17 lines of dense signs (slashes, crosses, digits, Greek-like letters), no clear word; 210: a '
                   'clear text of matching length (vetting n10). Inventory: "Bernardo Rucellai, or(ator). Mediolani, 1482 lug. 12, n. 175; ago. '
                   '27, n. 203; mar. 28, n. 209".',
        cls='K',
        status='Read by its filed decipherment (210); key material. Its sign set differs from the 196-207 Rucellai system.',
        why='Gives a second Rucellai table of 1482 for any bare letter in that system.',
        importance=2,
        verify='Align 209 with 210 and record the table.',
        links=maplinks(72, 209, [79612, 79613, 79614, 79615]),
    ),
]

# ---- MAP filza CXIX, docs. 115-127: the Laurentian key sheets (opened at 900 px) ----
MAP_ROWS += [
    dict(
        year=1485, date='undated (filed among the key sheets of Lorenzo de\' Medici\'s chancery, c. 1478-1492)',
        title='A full page of sign cipher filed among Lorenzo de\' Medici\'s key sheets (MAP CXIX 126), bare',
        correspondents='unknown (Laurentian chancery correspondence)', place='not stated', language='unknown (sign cipher, no clear word)',
        region='Italy', period='15th century',
        shelfmark='Archivio di Stato di Firenze, Mediceo avanti il Principato, filza CXIX, doc. 126 (old c. 127)',
        folio_note='One leaf, recto: about 28 lines of continuous letter-like signs (Latin letters, crosses, Greek-like forms), no clear word, '
                   'no address; verso blank. MAP inventory vol. 4 lists CXIX 115-127 together as "Cifre della segreteria di Lorenzo il '
                   'Magnifico col duca di Urbino, col duca di Calabria, con Giovanni Tornabuoni, con l\'ambasciatore di Venezia, Paolo '
                   'Antonio Soderini, con Lodovico Sforza, con Piero Medici, con Costanzo Sforza, con Dionigi Mortellas, con Giovan Battista '
                   'Centurioni, con Pellegrino (Rossi) da Forlì, con Ranuccio (Farnese)": twelve keys named for thirteen documents; 126 is '
                   'the one that is a text, not a table.',
        cls='A',
        status='Bare (900 px). The twelve key sheets beside it (CXIX 115-125, 127; keys.json) are the obvious first test.',
        why='An unread Laurentian cipher text filed with twelve keys of the same chancery: very likely readable with one of them.',
        importance=3, solvability=5, difficulty=2,
        verify='Build the sign inventory of 126; match it against the alphabets of CXIX 115-125, 127 and LXXII 178-188.',
        links=maplinks(119, 126, [118042, 118043]),
    ),
]
KEY_ROWS += [
    dict(
        year=1485, date='c. 1478-1492 (116 endorsed "Cum duca Calabriae 1485"; 117 pencil "1492-1498")',
        title='Twelve key sheets of Lorenzo de\' Medici\'s chancery, MAP CXIX 115-125 and 127 (Urbino, Calabria, Tornabuoni, Soderini, Lodovico Sforza, Piero de\' Medici, Costanzo Sforza, Mortellas, Centurioni, Pellegrino da Forlì, Ranuccio Farnese)',
        correspondents="Lorenzo de' Medici's chancery <-> the duke of Urbino, the duke of Calabria, Giovanni Tornabuoni, the Venetian ambassador, "
                       "Paolantonio Soderini, Lodovico Sforza, Piero de' Medici, Costanzo Sforza, Dionigi Mortellas, Giovan Battista "
                       "Centurioni, Pellegrino (Rossi) da Forlì, Ranuccio (Farnese) (per the inventory, not matched sheet by sheet)",
        place='Florence', language='Italian (keys)', region='Italy', period='15th century',
        shelfmark='Archivio di Stato di Firenze, Mediceo avanti il Principato, filza CXIX, docs. 115-125, 127 (old cc. 116-126, 128)',
        folio_note='115 (c. 116, with blank 116 bis): alphabet with three values, nulls, doubles, nomenclator (Papa, Re de Sicilia, Signoria '
                   'de Genova, Duca de Milano, Fiorentini, Duca de Ferrara, Duca de Urbino, Conte Hieronymo, Roberto Malatesta, Costanzo, '
                   'Signore de Faenza ...), so c. 1478-82; 116 (c. 117; 117 bis a list of sign words: Arcadi, Danari, Gente d\'arme, Fanti, '
                   'Vettovaglia, Alloggiamenti ...) "Cum duca Calabriae 1485": alphabet, doubles, "Nihil importantes", nomenclator '
                   '(Papa, Re, Duca di Calabria, Cardinals Orsini, Savello, Colonna, Duca d\'Andria, Fabrizio Colonna ...); 117: alphabet, '
                   'doubles, nulls, long nomenclator, pencil "1492-1498"; 118: alphabet, nulls, doubles, numbered nomenclator 20-54 '
                   '(Veneziani, Duce, Turco, Armata, Papa, Re Ferrando ...); 119: alphabet with three values, doubles, nulls, long '
                   'nomenclator; 120: small alphabet and numbered names (Papa, S. Francesco, Lorenzo ... Cardinali); 121: alphabet, doubles, '
                   'nulls and particles; 122: alphabet over a short covering letter ("ho fatta la cifra per potervi meglio informare ..."); '
                   '123: alphabet with homophones and a two-column nomenclator (Roma, Napoli, Venezia, Re di Spagna, Genova, Savona, '
                   'Spinola, Fregosi, Adorni ...); 124: alphabet and a few names (Siena, Bentivoglio?, Ducati, Roma, Milano, Napoli, '
                   'Veneziani, Duca di Ferrara); 125: alphabet with homophones, doubles, "nihil importantes" phrases, nomenclator; 127 '
                   '"Cum ... Ranuccio": alphabet with digits and a numbered nomenclator (Papa, Cardinali, Roma, Conte Hieronymo, Duca di '
                   'Calabria ...). 126 is a cipher text (row in candidates.json).',
        cls='K',
        status='Keys only; individual attribution to the inventory\'s twelve names not done (only 116 Calabria 1485 and 127 Ranuccio are '
               'endorsed legibly at 900 px). None tested yet.',
        why='With LXXII 178-188, the second Laurentian key set: first test for CXIX 126 and for the bare MAP letters (leads 2309-2311, '
            '2320-2324 and the LXXII rows of this pass).',
        importance=4,
        verify='Transcribe each table at full size (1600 px); attribute each to the inventory names; match sign sets against CXIX 126 and '
               'the bare MAP letters.',
        links=maplinks(119, 115, [118016, 118017, 118018, 118019, 118020, 118021, 118022, 118023, 118024, 118026, 118028, 118030,
                                  118032, 118034, 118036, 118038, 118040, 118044]),
    ),
]

rows = []
for r in MDP_ROWS:
    r.update(source=MDP_SRC, score_note=SCORE, access_note=MDP_ACCESS, seen='image', needs_archive_scan='no')
    r.setdefault('prior_art', MDP_PRIOR)
    rows.append(r)
for r in MAP_ROWS:
    r.update(source=MAP_SRC, score_note=SCORE, access_note=MAP_ACCESS, seen='image', needs_archive_scan='no')
    r.setdefault('prior_art', MAP_PRIOR)
    rows.append(r)
json.dump(rows, open(os.path.join(HERE, 'candidates.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(rows), 'rows')
keys = []
for r in KEY_ROWS:
    src, acc, pri = (MAP_SRC, MAP_ACCESS, MAP_PRIOR) if 'avanti' in r['shelfmark'] else (MDP_SRC, MDP_ACCESS, MDP_PRIOR)
    r.update(source=src, score_note=SCORE, access_note=acc, seen='image', needs_archive_scan='no')
    r.setdefault('prior_art', pri)
    keys.append(r)
json.dump(keys, open(os.path.join(HERE, 'keys.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(keys), 'key items (keys.json)')
