"""Build candidates.json and keys.json for the MAP whole-filza paging pass (6 Nov 2026).
Work list: ASF Mediceo avanti il Principato filze LXXII (docs not opened before: 1-159, 241-444), LXXIII, LXXIV, LXXV, paged
leaf by leaf (every recto and verso), flagged pages opened at the server maximum. Rows come from images viewed in this pass;
see README.md. Leads/catalogue items 2307-2312, 2320-2324, 2350-2353 and the asf_florence / asf_florence_2 rows are not repeated."""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
B = 'https://archiviodistatofirenze.cultura.gov.it'
SCORE = 'Scored from the images viewed during the MAP paging pass, 6 Nov 2026 (research/sweep_2026-11_asf_map_paging/)'

MAP_SRC = 'ASF Mediceo avanti il Principato (MAP) images, whole-filza paging pass, Nov 2026'
MAP_ACCESS = ('scans public on the ASF MAP site, no login, curl works: /map/ricerca/ricerca-su-filza/?f=<filza>&d=<doc> and IIIF '
              '/iipsrv/iipsrv.fcgi?IIIF=/data/iip-data/asfi/mediceo_avanti_principato/001000FF/A0000NNN.ptif (about 1272 px max); '
              'image id = first id of the filza + position - 1')
MAP_PRIOR = ('open as far as checked (6 Nov 2026): known.py finds nothing on the filza and document; not flagged as cipher in the MAP '
             'inventory (vol. 3, archive.org OCR); DECODE dumps in the repo have no ASF MAP ciphertext record; Tomokiyo and Lasry not '
             'searched in this run. Marco Vito (Vienna) works on encrypted MAP letters of 1486-1491 (research/medici_bia/README.md): '
             'check overlap.')


def maplinks(filza, doc, ids):
    out = [{'href': f'{B}/map/ricerca/ricerca-su-filza/?f={filza}&d={doc}&c=', 'label': f'MAP filza {filza}, doc. {doc}'}]
    out += [{'href': f'{B}/map/riproduzione/?id={i}', 'label': f'image id {i}'} for i in ids]
    return out


FIRST = {48: 59515, 72: 79110, 73: 80236, 74: 81295, 75: 81825, 137: 132517}  # image id of position 1 in each filza


def ids(filza, *positions):
    return [FIRST[filza] + p - 1 for p in positions]


def span(a, b):
    return list(range(a, b + 1))


MAP_ROWS = []
KEY_ROWS = []

# ---- rows are added below as each flagged page is checked at full size ----
# Paging: every recto and verso of each filza on 4-up contact sheets (each page about 390 px wide, contrast-stretched),
# doubtful pages at 800 px; every row below was then opened at the server maximum (1228-1465 px) and cropped, unless
# its status says "800 px".

MAP_ROWS += [
    dict(
        year=1445, date='19 Mar 144[3 or 7] (head "+ Al nome di dio adi 19 di marzo 144.", last digit unclear)',
        title='Florentine family letter of March 1443/1447 with short runs of digit-like cipher (3, z, 8, 7, g, t) among clear news, bare',
        correspondents='unsigned family letter (names Benedetto, the Tornabuoni, Albertaccio, Ricciardo; Medici circle) -> "Ricciardo"? (addressee on verso not read)',
        place='not stated (Florence?)', language='Italian (short cipher runs in clear text)', region='Italy', period='15th century',
        shelfmark='Archivio di Stato di Firenze, Mediceo avanti il Principato, filza CXXXVII, doc. 40 (pencil 49, old 23)',
        folio_note='One leaf, recto: about 20 lines of clear family news; at least four short cipher runs written in the same hand '
                   'with the same dot-separated layout: line 11 end ("... tu no(n) [3 signs] z3z3z4z3"), line 13 ("g3ttz1. 93 z3z3z4z3"), '
                   'line 14 ("a z3z4z3z3z#z3. 83z3. gttztt"), and a group at the end of line 18; signs are a small set of digit-like forms '
                   '(3, z, 8, 7, 4) and g/t letters, repeating like a vowel-and-number cipher. Verso not opened.',
        cls='B',
        status='Bare: no gloss over the runs; neighbours 39 and 41 not checked for a clear copy. Seen at 1382 px.',
        why='One of the oldest pieces of cipher found in the Medici archive (1440s), in a private letter; the runs are short and the '
            'sign set tiny, so the oldest-cipher question (pre-1497) is the main interest.',
        importance=4, solvability=2, difficulty=3,
        verify='Read the year (1443 or 1447) and the verso address at full size; transcribe the four runs; test a vowel/number '
               'substitution (the runs alternate 3 and z like vowel-consonant patterns); check docs 39 and 41.',
        links=maplinks(137, 40, ids(137, 83, 84)),
    ),
    dict(
        year=1477, date='Jun-Jul 1477 (docs 11-13 and 15 "Milano ... luglio 1477"; 14 "giugno 1477")',
        title='Tommaso Soderini, Milan, June-July 1477: five letters written in ordinary script whose words mostly do not read as Italian (possible word or letter substitution), unglossed',
        correspondents="Tommaso Soderini (signed \"Tomaso So...\"), Milan -> Lorenzo de' Medici", place='Milan',
        language='Italian? (disguised text in ordinary letters; uncertain)', region='Italy', period='15th century',
        shelfmark='Archivio di Stato di Firenze, Mediceo avanti il Principato, filza XLVIII, docs. 11-15',
        folio_note='Five leaves, rectos (versos addresses): each a full page in a fluent hand; some words read ("O magnifico ...", '
                   '"madonna", "aveva", "conforteranno", "tutti loro"), but many do not ("ezamonte", "zogo"), and scattered words are '
                   'heavily inked; the date lines are clear. Doc. 11 seen at 1272 px; 12-15 at 800 px.',
        cls='C',
        status='Unsure whether this is cipher at all (a jargon or letter-substitution disguise, or only a hard hand); no gloss and no '
               'clear copy seen beside it.',
        why='If it is a disguise, it is a 1477 Milan correspondence of Lorenzo\'s ambassador, before the Pazzi war; the same writer\'s '
            'August 1481 letter (row below) is in true sign cipher.',
        importance=2, solvability=2, difficulty=3,
        verify='Transcribe doc. 11 at full size and test for word substitution (cover names) versus a letter cipher in Latin letters.',
        links=maplinks(48, 11, ids(48, *span(23, 32))),
    ),
    dict(
        year=1481, date='Aug 1481 ("in Milano a di .. d\'agosto 1481")',
        title='Tommaso Soderini, Milan, August 1481: a full page of sign-and-figure cipher plus a ten-line cipher postscript, bare',
        correspondents="Tommaso Soderini (signed \"v. Tomaso ...\" on the verso), Milan -> Lorenzo de' Medici", place='Milan',
        language='Italian (sign cipher with digits; one clear date line)', region='Italy', period='15th century',
        shelfmark='Archivio di Stato di Firenze, Mediceo avanti il Principato, filza XLVIII, doc. 63 (c. 65)',
        folio_note='Recto: "Mag.ce v. et mag.re hon." then about 30 lines of dense continuous cipher (invented letter-like signs, '
                   'Greek-like forms, digits 6, 7, 8, 9, 3, with "=" and "+" as separators; no clear word), a clear dating line, and a '
                   'postscript "Dipoi scripta ..." of about 10 more cipher lines; verso: 4 cipher lines, then the signature and date.',
        cls='A',
        status='Bare (1272 px): no interlinear or marginal decipherment, no filed clear text beside it (docs 62 and 64 are clear letters).',
        why='A long, purely enciphered despatch of 1481 from Lorenzo\'s ambassador in Milan, two years after the Pazzi war; '
            'about 1,500 cipher symbols, enough for a ciphertext-only attack, and the 1480s Laurentian keys (LXXII 178-188, CXIX '
            '115-127) are the first test.',
        importance=4, solvability=4, difficulty=3,
        verify='Transcribe; count the sign set (homophones? "=" and "+" as word separators or nulls); test against LXXII 183 '
               '(Paolantonio Soderini, his son) and the CXIX keys; then a homophonic solver.',
        links=maplinks(48, 63, ids(48, 143, 144)),
    ),
    dict(
        year=1483, date='autumn 1482 - Feb 1485',
        title='Bernardo Rucellai, Florentine orator in Milan, 1482-85: the bare pieces of his sign cipher in MAP XLVIII (seven letters and slips), with dozens of glossed siblings and four filed decipherments in the same filza',
        correspondents="Bernardo Rucellai (Milan) -> Lorenzo de' Medici, and via \"Lionardo\" (Leonardo Spina / a cover address)", place='Milan',
        language='Italian (sign cipher with clear words)', region='Italy', period='15th century',
        shelfmark='Archivio di Stato di Firenze, Mediceo avanti il Principato, filza XLVIII, docs. 101, 158, 188, 189, 191, 196, 199',
        folio_note='101 (c. 102r): slip, top 11 lines solid sign/figure cipher with a few clear words, then clear text; 158 (c. 161r): clear '
                   'copy dated Dec 1482 with 3 cipher lines at the foot; 188 (c. 193r, endorsed 1483, "adi 14 d\'aprile"): about 20 sign runs '
                   'between clear words; 189 (Milan 17 Apr 1483, signed Bern.o Rucellai): runs in about 12 lines; 191 (c. 196r-v, Apr 1483): '
                   'long runs in most lines and in the postscript; 196 (10 May 1483): two-line cipher postscript below the signature; 199v '
                   '(17 May 1483): two-line cipher postscript beside the signature (199r is glossed).',
        cls='A',
        status='Bare on these pages (contact sheet and 800 px; 188-191 at 800 px): no clear text over the runs. The same filza holds the key '
               'material: interlinear glosses on about 60 Rucellai pages (docs 97-99, 102, 105-106, 116-117, 122, 125, 128, 135, 140, 142, '
               '153, 156, 159-161, 166, 182, 185, 190, 194-195, 198-201, 203-207, 211-213, 216-217, 219-223, 225-226, 230, 237-238, 245, '
               '266-279, 282, 288-293) and filed decipherments: 201 c. 208 bis (of 201), 220 c. 228 (of 220 c. 229), 241 (of 239 and '
               '240), 243 c. 254 (probably of 243 c. 253).',
        why='The bare Rucellai pieces can be read from the filza\'s own glossed letters; together with lead 2350 (LXXII 196-206, the 1482 '
            'Spina letters) they make one large Laurentian cipher corpus.',
        importance=3, solvability=5, difficulty=2,
        verify='Rebuild the sign table from the glossed pages and the four decipherment pairs; apply to the seven bare pieces; compare '
               'with LXXII 196-207 (lead 2350) and XLVIII 214 / 294 (see README: 294 is a cipher letter of February 1485 in the 214 sign '
               'family with its decipherment filed at c. 276).',
        links=maplinks(48, 101, ids(48, 235, 236)) + maplinks(48, 158, ids(48, 395)) + maplinks(48, 188, ids(48, *span(467, 478)))
              + maplinks(48, 196, ids(48, 497)) + maplinks(48, 199, ids(48, 503, 504)),
    ),
    dict(
        year=1486, date='20 Aug 1486 (verso: "1486 Copia A Baccio Ugolini adi 20 d\'agosto")',
        title="Lorenzo de' Medici to Baccio Ugolini, 20 August 1486 (copy in Lorenzo's hand, headed \"Abram\"): clear letter with about six code signs for persons, bare",
        correspondents="Lorenzo de' Medici -> Baccio Ugolini (Florentine agent, Naples/Rome)", place='Florence',
        language='Italian (clear with nomenclator signs)', region='Italy', period='15th century',
        shelfmark='Archivio di Stato di Firenze, Mediceo avanti il Principato, filza LXXII, doc. 403 (c. 513)',
        folio_note='Recto headed "Abram" (a cover name?), about 30 lines in Lorenzo\'s hand; in the second paragraph single signs stand for '
                   'persons: a box with a cross-stroke (three times), a cross, "B", a triangle, a circled cross; verso endorsed with the '
                   'same box sign. MAP inventory vol. 3: "A Baccio Ugolini. (Lorenzo il Magnifico) (Firenze), (1486 mar. 17), n. 358. '
                   '1486 ago. 20, n. 403".',
        cls='C',
        status='Bare (1272 px). The key sheet "Cifra col Baccio Ugolini" is in the same filza (LXXII 181: nomenclator of Re Ferrando, '
               'Duca di Calabria, Piero and Giuliano di Lorenzo ...).',
        why='A nomenclator-only cipher of Lorenzo himself, with the matching key in the same filza: a check of LXXII 181, not a text to solve.',
        importance=2, solvability=5, difficulty=1,
        verify='Match the six signs with key sheet LXXII 181; see also LXXII 358 (Lorenzo to Ugolini, 17 Mar 1486; not flagged on the sheets) '
               'and 434 ("Abraham" named twice).',
        links=maplinks(72, 403, ids(72, 1027, 1028)),
    ),
    dict(
        year=1488, date='c. 1488-89 (minute; signed on c. 509 bis "Lorenzo de Medici")',
        title="Lorenzo de' Medici to Giovanni Lanfredini, orator in Rome, c. 1488-89: autograph minute with about fourteen sign-cipher runs between clear words, bare",
        correspondents="Lorenzo de' Medici -> Giovanni Lanfredini, Florentine orator in Rome", place='Florence',
        language='Italian (sign cipher with clear words)', region='Italy', period='15th century',
        shelfmark='Archivio di Stato di Firenze, Mediceo avanti il Principato, filza CXXXVII, doc. 504 (cc. 509-510 bis)',
        folio_note='c. 509r: a dense clear minute (N.S. = the pope, Virginio Orsini?) with about 8 cipher runs of 10-40 signs (÷, π, +, 2, 3, '
                   '4, Latin-letter forms) in the middle and lower half; c. 509v: about 6 more runs; c. 509 bis r: signature; c. 510 bis v: '
                   'address to Lanfredini.',
        cls='A',
        status='Bare (1272 px on c. 509r, 800 px on the rest): no gloss; the cipher was written into the minute by Lorenzo\'s chancery.',
        why='An outgoing cipher letter of Lorenzo il Magnifico to his key ambassador in Rome in the years of the Innocent VIII alliance; '
            'Lanfredini\'s incoming cipher letters (and the Laurentian key sheets) are the obvious route to the key.',
        importance=4, solvability=4, difficulty=3,
        verify='Transcribe the runs; test the LXXII 178-188 and CXIX 115-127 keys (none is labelled Lanfredini); look for Lanfredini\'s '
               'own glossed letters of 1487-89 in MAP (e.g. filze L-LX).',
        links=maplinks(137, 504, ids(137, *span(1057, 1060))),
    ),
]

# ---- 1492-94: Piero di Lorenzo's ambassadors (LXXII-LXXV) ----
MAP_ROWS += [
    dict(
        year=1492, date='3 Aug 1492 - Jan 1493',
        title='Angelo Niccolini, Florentine envoy in Milan/Pavia, 1492-93: four short bare cipher passages (postscripts and single lines) among his glossed letters',
        correspondents="Angelo Niccolini (Milan, Pavia) -> Piero di Lorenzo de' Medici", place='Pavia, Milan',
        language='Italian (figure/sign cipher: H, HH, ÷, π, 11, 22 ...)', region='Italy', period='15th century',
        shelfmark='Archivio di Stato di Firenze, Mediceo avanti il Principato, filza LXXIV, docs. 42 (c. 90r), 49 (c. 104r), 81 (c. 177r), 90 (c. 200r)',
        folio_note='42 c. 90r (Pavia 3 Aug 1492): 5-line cipher postscript; 49 c. 104r (Pavia 20 Aug 1492): one run "sul papa HH x o q m 4 d '
                   'π c ÷ 11 ..."; 81 c. 177r (21 Dec 1492): one cipher line at the end; 90 c. 200r (postscript sheet, Jan 1493): one line.',
        cls='B',
        status='Bare (contact sheet and 800 px; 42 also at 1272 px). Niccolini\'s other letters in the filza (docs 6, 21, 32, 35-37, 59, '
               '62, 72, 78, 81 c. 176r, 97) carry interlinear decipherments of the same system (keys.json).',
        why='Short, but readable from the glossed siblings; useful only as part of the Milan embassy cipher of 1492-94.',
        importance=1, solvability=5, difficulty=2,
        verify='Build the table from the glossed Niccolini pages; read the four passages.',
        links=maplinks(74, 42, ids(74, 183)) + maplinks(74, 49, ids(74, 209)) + maplinks(74, 81, ids(74, 357)) + maplinks(74, 90, ids(74, 403)),
    ),
    dict(
        year=1494, date='25? Apr 1494',
        title='Piero Alamanni, Florentine orator in Milan, April 1494: two leaves with about 25 lines of mixed figure/sign cipher, bare',
        correspondents="Piero Alamanni (signed \"Petrus Alamannus eques\"), Milan -> Piero di Lorenzo de' Medici", place='Milan',
        language='Italian (figure/sign cipher between clear words)', region='Italy', period='15th century',
        shelfmark='Archivio di Stato di Firenze, Mediceo avanti il Principato, filza LXXIV, doc. 96 (cc. 220-221)',
        folio_note='c. 220r clear; c. 220v from line 6 to the foot: runs of figure/sign groups ("÷ 11 6 π b 7", "p π b v c q m", "v p y π", '
                   '"22 λ p ÷ 11 o v 11 4") between clear words; c. 221r: runs in lines 1-6, 9-14, 20-24; c. 221v: first lines, signature.',
        cls='A',
        status='Bare (1272 px): no interlinear clear text. The same sign family is glossed in Niccolini\'s and Ridolfi\'s letters of '
               '1492-94 in this filza; key sheet LXXII 178 is endorsed "Alamanni Piero" (his Naples cipher of 1489-92).',
        why='The orator\'s despatch from Ludovico Sforza\'s court on the eve of Charles VIII\'s descent (spring 1494), unread, with key '
            'material in the same and the next filza.',
        importance=3, solvability=5, difficulty=2,
        verify='Test LXXII 178 and the table rebuilt from the glossed LXXIV letters; read c. 220v-221v.',
        links=maplinks(74, 96, ids(74, *span(439, 442))),
    ),
    dict(
        year=1494, date='16-30 Oct 1494',
        title='Giovan Battista Ridolfi, Florentine envoy in Milan, October 1494: three letters with bare figure/sign cipher passages, beside eleven glossed letters of the same system',
        correspondents="Giovan Battista Ridolfi (Milan, Alessandria, Vigevano) -> Piero di Lorenzo de' Medici", place='Milan',
        language='Italian (figure/sign cipher between clear words)', region='Italy', period='15th century',
        shelfmark='Archivio di Stato di Firenze, Mediceo avanti il Principato, filza LXXIV, docs. 112 (c. 256), 113 (c. 257), 115 (c. 263)',
        folio_note='112 (Milan 16 Oct 1494): c. 256r about 17 lines of cipher runs in two blocks, c. 256v about 14 more, c. 261 the address; '
                   '113 (Milan 21 Oct 1494): c. 257r lower third 9 lines, c. 257v 2 lines; 115 (Milan 30 Oct 1494): c. 263r lines 4-13.',
        cls='A',
        status='Bare (1272 px on 112 and 113, 800 px on the versos and 115). Ridolfi\'s letters 101-110 and 114 (Sept-Oct 1494) carry '
               'interlinear decipherments of the same system (keys.json).',
        why='The Milan despatches of October 1494, during Charles VIII\'s march through Lombardy; readable from the glossed siblings.',
        importance=3, solvability=5, difficulty=2,
        verify='Rebuild the table from 101-110 and 114; read 112, 113, 115.',
        links=maplinks(74, 112, ids(74, *span(513, 516))) + maplinks(74, 113, ids(74, 517, 518)) + maplinks(74, 115, ids(74, 525)),
    ),
    dict(
        year=1494, date='26 Apr 1494',
        title='Guidantonio Vespucci and Piero Capponi, Florentine orators to France, en route ("urbe Taurina"?), 26 April 1494: four-line cipher postscript, bare',
        correspondents="Guidantonio Vespucci and Piero Capponi, orators -> Piero di Lorenzo de' Medici", place='Turin? (on the way to Lyon)',
        language='Italian (sign cipher with code numbers 764, 390, 86)', region='Italy', period='15th century',
        shelfmark='Archivio di Stato di Firenze, Mediceo avanti il Principato, filza LXXV, doc. 50 (c. 50v)',
        folio_note='c. 50r: clear letter with 5 glossed cipher lines at the foot; c. 50v: clear end, date "die xxvi aprilis MCCCCLXXXXIIII", '
                   'signatures "G.A. Vespuccius & Petrus Capponus ores", then a postscript whose 4 middle lines are sign cipher (letter-like '
                   'signs, crosses, code numbers 764 and 8611) without gloss.',
        cls='B',
        status='Bare (1272 px). Key material in the filza: the orators\' cipher letters with filed decipherments (27/29, 30/90, 32/31, 33/34, '
               '35/36, 37/46, 40/41, 42/43; keys.json) and the glossed 28 and 38; the key itself is also listed in Carte Strozziane I '
               'f. 23 (Guasti 1884, pp. 132-135: "Vespucci/Capponi in Francia").',
        why='Short, readable from the pairs; adds one unread passage to a well-keyed 1494 system.',
        importance=1, solvability=5, difficulty=1,
        verify='Rebuild the table from 27/29 and 37/46; read the postscript.',
        links=maplinks(75, 50, ids(75, 131, 132)),
    ),
    dict(
        year=1493, date='undated (filed with the Gentile Becchi / Piero Soderini embassy papers of 1493)',
        title='Cipher slip of 1493 in figures and signs (13 ÷ 327, 83, 77, 6300 ...): four cipher lines and a clear note, bare',
        correspondents="unsigned (Florentine embassy in France, 1493?) -> Piero di Lorenzo de' Medici", place='not stated',
        language='Italian (figure code mixed with letter-signs)', region='Italy', period='15th century',
        shelfmark='Archivio di Stato di Firenze, Mediceo avanti il Principato, filza LXXV, doc. 106 (old c. 166)',
        folio_note='Oblong slip: 4 lines of cipher, groups of figures (13, 327, 83, 77, 20, 300, 6300, 2627) and letter-like signs (÷, π, '
                   '+, "5ch6p800"), then 4 clear lines ("Galeasso viene da V.M. ... al Duca di Ferrara ... .L.").',
        cls='B',
        status='Bare (1364 px). Doc. 110 (old c. 171) is an unsigned clear slip ("Vuole aiuto da noi alla impresa del Reame ...") in the '
               'format of a decipherment, but at about 90 words it is longer than 106\'s four lines would give unless the figures are '
               'phrase codes; not matched.',
        why='A code-heavy system (three- and four-figure groups) of the 1493 French embassy; the numbered nomenclator of LXXII 183 '
            '(Paolantonio Soderini) and della Casa\'s "Arroge alla vostra cyfra" additions (LXXV 53-54, numbers 90-94) are candidates.',
        importance=2, solvability=3, difficulty=3,
        verify='Test whether 110 is the plaintext of 106 (names Re di Francia, Spagna, Napoli as code numbers); compare with LXXII 183 and '
               'LXXV 53-54.',
        links=maplinks(75, 106, ids(75, 327, 328)) + maplinks(75, 110, ids(75, 337)),
    ),
    dict(
        year=1494, date='[June 1494] (doc. 15, unsigned "Cosimo ..."; docs 14 and 17 are Sassetti\'s of 8 and 20 June 1494)',
        title='Cosimo Sassetti, June 1494: short note with two lines (about 25 signs) of sign cipher, bare; his glossed letters 14 and 17 beside it',
        correspondents="Cosimo Sassetti -> Piero di Lorenzo de' Medici", place='not stated (Lyon?)',
        language='Italian (sign cipher: Greek-like letters, crosses, circles)', region='Italy', period='15th century',
        shelfmark='Archivio di Stato di Firenze, Mediceo avanti il Principato, filza LXXV, doc. 15',
        folio_note='Short note; two lines of signs between clear words mid-page; signed "Cosimo ...".',
        cls='C',
        status='Bare (800 px). Docs 14 (8 June 1494) and 17 (20 June 1494), Sassetti\'s letters, carry the same kind of signs with interlinear glosses.',
        why='Too short alone; readable from 14 and 17.',
        importance=1, solvability=4, difficulty=2,
        verify='Read 14 and 17 glosses; apply to 15.',
        links=maplinks(75, 15, ids(75, 34)),
    ),
    dict(
        year=1494, date='4 Oct 1494 ("Ex Regiis Castris die 4 octobris")',
        title='Bernardo Dovizi da Bibbiena from the royal camp in Romagna, 4 October 1494: long clear letter with names spelled in a sign cipher (three groups, one of about 20 signs), bare; Piero de\' Medici\'s glossed letter of 28 October in the same signs',
        correspondents="Bernardo Dovizi da Bibbiena (\"B. ... Bib.\") -> Piero di Lorenzo de' Medici", place='camp of the duke of Calabria, Romagna',
        language='Italian (clear with sign-cipher names: x o u u + 8 π, x o u x o)', region='Italy', period='15th century',
        shelfmark='Archivio di Stato di Firenze, Mediceo avanti il Principato, filza LXXII, doc. 77 (cc. 83-88)',
        folio_note='Six sides of clear narrative (a "facto venereo" at the camp, Cesena); a name group "x o u u + 8 π" recurs (c. 84r-v, 86v), '
                   'a second group "x o u x o" recurs about ten times (cc. 86v-88v), and a lady\'s name is given in about 20 signs on c. 84v '
                   '("una nobilissima et bellissima Madonna chiamata ..."). Address c. 83v.',
        cls='B',
        status='Bare (1272 px on c. 84v; contact sheet and 800 px elsewhere). The sign set (x, ÷, π, u, h, 8, 3, +, 11) is the one '
               'glossed in LXXII 81 (Piero de\' Medici, Pietrasanta 28 Oct 1494, to ser Piero da Bibbiena), so the names should read '
               'directly. Moncallero\'s Epistolario di Bernardo Dovizi da Bibbiena (1955) prints his letters of 1490-94; whether this one '
               'and its names are deciphered there was not checked.',
        why='Small (three names) but readable at once from LXXII 81; low value except as a key check.',
        importance=1, solvability=5, difficulty=1,
        verify='Read the groups with the LXXII 81 glosses; check Moncallero 1955 for the letter of 4 Oct 1494.',
        links=maplinks(72, 77, ids(72, *span(171, 180))) + maplinks(72, 81, ids(72, 189, 190)),
    ),
    dict(
        year=1494, date='[1494] (head "+ Ex urbe Rome ... 1494")',
        title='Letter from Rome, 1494, signed "Iacobo ...": five lines of dot-separated words in ordinary letters that mostly do not read (possible letter cipher), unglossed',
        correspondents="\"Iacobo ...\" (Rome) -> [Piero di Lorenzo de' Medici's circle]", place='Rome',
        language='unknown (Latin-letter text with word divisions; uncertain cipher)', region='Italy', period='15th century',
        shelfmark='Archivio di Stato di Firenze, Mediceo avanti il Principato, filza LXXIII, doc. 3',
        folio_note='Recto: clear head and signature; 5 lines of words separated by dots, a few apparently Italian ("sono", "tre", "perche"), '
                   'most not; verso address only.',
        cls='C',
        status='Unsure (1272 px): could be a hard hand or a substitution in Latin letters; no gloss, no clear copy beside it.',
        why='Short; listed so that it is not paged again.',
        importance=1, solvability=2, difficulty=3,
        verify='Transcribe and test for simple substitution.',
        links=maplinks(73, 3, ids(73, 5, 6)),
    ),
]

# ---- 1512-15 ----
MAP_ROWS += [
    dict(
        year=1512, date='7 Mar 1512 and 6 Jun 1513 (inventory: 1512 mar. 7, n. 130; 1513 giu. 5-6, nn. 139-140)',
        title='Antonio Maria Bonanni of San Gimignano, Piacenza, 1512-13: two letters to ser Giovanni da Poppi with cipher runs (letters and digits with superscript index figures), bare',
        correspondents='Antonio Maria Bonanni (Bonannius geminianensis), Piacenza -> ser Giovanni da Poppi, Medici secretary', place='Piacenza',
        language='Italian (cipher runs: Latin letters and digits with superscript figures 1-4)', region='Italy', period='1497-1559',
        shelfmark='Archivio di Stato di Firenze, Mediceo avanti il Principato, filza LXXII, docs. 130 and 140',
        folio_note='130r ("Placentie die vij Martij XII", signed "Anto: maria Bonannus Gem."): five lines with four runs of 10-30 symbols '
                   '(e.g. "P4 5T8 Z584 3 5 X y d 6 3 d"), small figures 1-4 written above many symbols; 140r (Piacenza 6 June [1513]): about '
                   '2 lines (45 symbols) of the same kind. Versos: address "S. Iohanni de Puppio secretario Florentie".',
        cls='B',
        status='Bare (1228 px on 130, 800 px on 140): the superscript figures are index marks (homophone numbers), not a gloss. The '
               'same superscript-figure style is used in Acciaiuoli\'s 1513 cipher (LXXII 190-192) and Pandolfini\'s 1514-15 cipher (row below).',
        why='A Medici agent in Lombardy in the year of the Medici restoration; short, but the superscript-index system ties it to the '
            'better-keyed 1513-15 Medici ciphers.',
        importance=2, solvability=3, difficulty=3,
        verify='Transcribe both; test the Acciaiuoli 190/191 table and the Pandolfini table; look at doc. 139 (5 June 1513).',
        links=maplinks(72, 130, ids(72, 317, 318)) + maplinks(72, 140, ids(72, 337, 338)),
    ),
    dict(
        year=1515, date='Jan 1514 (st. fior.) - Feb 1515 and Sept-Dec 1514',
        title='Francesco Pandolfini, Florentine orator in France, 1514-15: seven cipher letters with no decipherment identified, beside about twelve cipher/decipherment pairs of the same system in MAP LXXII',
        correspondents="Francesco Pandolfini, orator at the French court -> the Otto di Pratica / Lorenzo de' Medici (duke of Urbino)", place='Paris',
        language='Italian (letter/digit cipher with superscript figures, between clear passages)', region='Italy', period='1497-1559',
        shelfmark='Archivio di Stato di Firenze, Mediceo avanti il Principato, filza LXXII, docs. 297, 307, 309, 310, 311, 322, 333',
        folio_note='297 (copy, Paris 22? Jan 1514 st. fior.): 8 cipher lines; 307 (c. 369, Feb 1514 st. fior.): almost a page; 309 (c. 378, to '
                   'Lorenzo, 26? Feb): 10 lines; 310 (cc. 380-381, 25 Feb-2 Mar): about 70 cipher lines in blocks; 311 (c. 382): nearly two '
                   'sides; 322 (copy of two chapters to Rome, Oct 1514): two 9-line blocks; 333 (c. 417, to Lorenzo, 27 Dec MDXIII or MDXIIII, read both ways): 3-5 lines.',
        cls='A',
        status='No gloss on these pages (contact sheet and 800 px), and the paging matched none of them with a filed clear text; some may '
               'be covered by the unheaded clear copies 284, 306, 316, 332, 337, 344, 347, 350, 365-366 and 419 (not aligned). Pairs in '
               'the filza: 281/285, 287/288, 290/291-292, 293/335, 308 (glossed)/313, 315/316, 317/348, 320/321, 330/331, 334/332, '
               '338/339, 340/341, 342/343, 346/345, 349/348; glossed 318, 319; decipherments 368 ("Decifrato ... a Lorenzo"), 366 ("tratti '
               'di cifra"). The first pass recorded 215 (1514, interlinear) as the key text of this system.',
        why='A full key can be rebuilt from the pairs, and the seven letters read; the embassy covers Louis XII\'s last months, Francis '
            'I\'s accession and the run-up to Marignano.',
        importance=3, solvability=5, difficulty=2,
        verify='Align 287 with 288 and 342 with 343 to rebuild the table (superscripts as homophone marks); read the seven; check each '
               'against the unheaded clear copies first.',
        links=maplinks(72, 297, ids(72, 719, 720)) + maplinks(72, 307, ids(72, 747, 748)) + maplinks(72, 309, ids(72, *span(755, 758)))
              + maplinks(72, 310, ids(72, *span(759, 762))) + maplinks(72, 311, ids(72, 763, 764)) + maplinks(72, 322, ids(72, 801, 802))
              + maplinks(72, 333, ids(72, *span(837, 840))),
    ),
]

# ---- key sources: glossed letters and cipher/decipherment pairs (keys.json) ----
KEY_ROWS += [
    dict(
        year=1494, date='28 Oct 1494',
        title="Piero di Lorenzo de' Medici to ser Piero da Bibbiena, Pietrasanta, 28 October 1494: sign-cipher runs with interlinear decipherment",
        correspondents="Piero di Lorenzo de' Medici -> ser Piero Dovizi da Bibbiena (Florence)", place='Pietrasanta', language='Italian',
        region='Italy', period='15th century',
        shelfmark='Archivio di Stato di Firenze, Mediceo avanti il Principato, filza LXXII, doc. 81 (c. 95, address c. 156)',
        folio_note='c. 95r-v: about 20 sign runs (π, ÷, u, 8, x, h, m, 3, +, 11) between clear words, clear text written above most '
                   '("provveder", "pietrasanta", "il castello" ...).',
        cls='K', status='Glossed (key source; 1272 px).', why='Key for LXXII 77 (row) and any 1494 Bibbiena-Medici sign letter.',
        importance=2, verify='Record the sign/letter pairs.', links=maplinks(72, 81, ids(72, *span(189, 192))),
    ),
    dict(
        year=1492, date='May 1492 - Oct 1494',
        title='Milan embassy cipher of 1492-94 (Angelo Niccolini, Giovan Battista Ridolfi): letters with interlinear decipherment, MAP LXXIV',
        correspondents="Angelo Niccolini; Giovan Battista Ridolfi (Milan, Pavia, Vigevano, Alessandria) -> Piero di Lorenzo de' Medici",
        place='Milan', language='Italian', region='Italy', period='15th century',
        shelfmark='Archivio di Stato di Firenze, Mediceo avanti il Principato, filza LXXIV, docs. 6, 7, 21, 32, 35-37, 59, 62, 72, 78, 81, 97 (Niccolini 1492-93); 101-107, 109, 110, 114 (Ridolfi 1494)',
        folio_note='Figure/sign runs (H, HH, ÷, π, 11, b 7 ii, 22, code numbers 48, 49, 69) between clear words with interlinear '
                   'decipherment; docs 105, 107, 110 almost entirely cipher, fully glossed. No separate decipherment slips in LXXIV.',
        cls='K', status='Glossed (contact sheet and 800 px).',
        why='Key for the bare Niccolini, Alamanni and Ridolfi rows.', importance=3,
        verify='Rebuild one table per writer and compare (one system or several).',
        links=maplinks(74, 6, ids(74, 19, 20, 21)) + maplinks(74, 105, ids(74, 475, 476, 477, 478)) + maplinks(74, 110, ids(74, *span(501, 508))),
    ),
    dict(
        year=1494, date='Apr-Jun 1494 (and della Casa 1493)',
        title='French embassy of 1493-94 (Vespucci and Capponi; Francesco della Casa; Sassetti): cipher letters with filed decipherments, glossed letters and nomenclator additions, MAP LXXV',
        correspondents="Guidantonio Vespucci and Piero Capponi; Francesco della Casa; Cosimo Sassetti; a \"V. P. ... Salviati\"? -> Piero di Lorenzo de' Medici",
        place='Lyon, Paris, Orléans', language='Italian', region='Italy', period='15th century',
        shelfmark='Archivio di Stato di Firenze, Mediceo avanti il Principato, filza LXXV, docs. 27/29, 30/90 ("Desifrata"), 32/31, 33/34, 35/36, 37/46, 40/41, 42/43, 51/47; glossed 14, 17, 28, 38, 45, 50r, 55, 61; nomenclator additions 53-54',
        folio_note='Pairs: cipher letter (sign cipher with code numbers 35, 46, 60, 63-65, 73-74, 86, "L." marks) and an unheaded clear slip '
                   'in one hand (90 headed "Desifrata"). 51 (Lyon?, 29 Apr 1493, signed "V. P. ...") is a two-level stacked system '
                   '(letters/digits written over a bar) whose working decipherment is 47 (with "nul" marks for nulls). 53 c. 72r and 54 '
                   'c. 75v (della Casa, Paris 17 July 1493): "Arroge alla vostra cyfra questi nomi": Generale di Linguadoca 90, Mons. di '
                   'Cordes 91, Principe di Salerno 92, Governatore di Borgogna 93, Conte Carlo [di Belgioioso?] 94.',
        cls='K', status='Read at the time (pairs) or glossed; 51/47 checked at 1400 px.',
        why='Keys for the LXXV rows (50v postscript, 106 slip, 15); the inventory\'s eight pairs confirmed and 51 added.', importance=3,
        verify='Rebuild the Vespucci-Capponi table from 37/46; record the 51 stacked system from 47.',
        links=maplinks(75, 27, ids(75, 63, 67)) + maplinks(75, 37, ids(75, *span(89, 92)) + ids(75, *span(117, 120)))
              + maplinks(75, 51, ids(75, 133, 121)) + maplinks(75, 53, ids(75, 141, 145)),
    ),
    dict(
        year=1482, date='1481-89',
        title='Laurentian ambassadors\' letters with interlinear decipherment in MAP LXXIII and CXXXVII (Tornabuoni 1481-82, Rome 1489, della Valle 1491, Soderini 1489 and 1494, Alamanni 1489, Capponi and Rucellai 1486, Vettori 1488)',
        correspondents="Giovanni Tornabuoni (Rome); Florentine orators in Rome; Antonio della Valle (Naples); Paolantonio Soderini (Naples, Venice); "
                       "Piero Alamanni (Pavia); Piero Capponi (camp); Bernardo Rucellai (Naples); Piero Vettori (Naples) -> Lorenzo / Piero de' Medici",
        place='Rome, Naples, Venice, Pavia', language='Italian', region='Italy', period='15th century',
        shelfmark='Archivio di Stato di Firenze, Mediceo avanti il Principato, filza LXXIII, docs. 117 (camp, 26 Aug 1494), 183-184 (Soderini, Venice 28 Oct 1494), 383, 387-389 (Tornabuoni and others, Rome 1481-82), 432 (Rome 5 Feb 1489), 437 (della Valle, Naples 25 Jan 1491), 354 and 356 (clear "Copia di cifrato"); filza CXXXVII, docs. 470 (Bracciano? 27 Jan 1482/3), 484 (Piero Capponi, 20 Aug 1486), 487 (Rucellai, Naples 26 Aug 1486), 499 (Piero Vettori, Naples 10 Jan 1488), 509-510 (Alamanni, Pavia 9 and 11 Jul 1489), 516 (Soderini, Naples 24 Nov 1489)',
        folio_note='Mixed figure/sign cipher runs (digits, H, x, π, =, +) between clear words, clear text written above most runs; LXXIII '
                   '183 and 184 almost entirely cipher, fully glossed.',
        cls='K', status='Glossed (contact sheet and 800 px); the cipher on 383, 389 and 432 needs a full-size check of the gloss coverage.',
        why='Worked examples of six or more Laurentian systems of 1481-94: tests for the LXXII 178-188 and CXIX 115-127 key sheets and keys '
            'for bare letters of the same writers (e.g. CXXXVII 504 to Lanfredini; XLVIII 63 Tommaso Soderini).', importance=3,
        verify='Match each against the LXXII and CXIX key sheets (Soderini: LXXII 183; Alamanni: LXXII 178; Tornabuoni: CXIX).',
        links=maplinks(73, 183, ids(73, 379, 380, 381, 382)) + maplinks(73, 389, ids(73, 822, 823)) + maplinks(73, 437, ids(73, 924))
              + maplinks(137, 509, ids(137, 1071, 1072)) + maplinks(137, 516, ids(137, 1091, 1092)),
    ),
    dict(
        year=1483, date='1482-86',
        title='MAP XLVIII cipher key sources: Bernardo Rucellai\'s glossed letters and decipherment pairs (Milan 1482-85), Jacopo Guicciardini (Ferrara 1483), F. Gaddi (Rome 1483), Pierfilippo Pandolfini (Milan 1484), N. Pandolfini? (1486)',
        correspondents="Bernardo Rucellai; Jacopo Guicciardini; Francesco Gaddi; Pierfilippo Pandolfini -> Lorenzo de' Medici",
        place='Milan, Ferrara, Rome', language='Italian', region='Italy', period='15th century',
        shelfmark='Archivio di Stato di Firenze, Mediceo avanti il Principato, filza XLVIII, Rucellai docs. 97-293 (glossed; list in the Rucellai row), pairs 201/c. 208 bis, 220 c. 229/c. 228, 239-240/241, 243 c. 253/c. 254, 294 c. 306/c. 276; Guicciardini docs. 307, 310, 314, 316, 317, 331; Gaddi doc. 5; Pandolfini doc. 53; doc. 354 c. 369 bis',
        folio_note='294 (Rucellai, Milan Feb 1484 st. fior. = 1485, signed "Bernardus Oricellarius"): three sides of cipher with "##" and '
                   'numerals 31, 87, 150, 18, the sign family of XLVIII 214 (catalogue 2309), with its clear text filed as c. 276 ("Scripsi '
                   'adi 22 et questa per fante ..."). 307-317, 331: Guicciardini\'s sign runs with numerals, glossed ("tu scrivi in cifera").',
        cls='K', status='Glossed / read at the time (contact sheet and 800 px).',
        why='294/276 is a plaintext pair in the sign family of the catalogued XLVIII 214 (2309); the rest key the Rucellai row and other '
            'War-of-Ferrara letters.', importance=4,
        verify='Align 294 c. 306 with c. 276 and compare the table with XLVIII 214 (catalogue 2309).',
        links=maplinks(48, 294, ids(48, 747, 748, 749, 751, 752)) + maplinks(48, 239, ids(48, 609, 611, 613)) + maplinks(48, 307, ids(48, 779, 780)),
    ),
]


rows = []
for r in MAP_ROWS:
    r.update(source=MAP_SRC, score_note=SCORE, access_note=MAP_ACCESS, seen='image', needs_archive_scan='no')
    r.setdefault('prior_art', MAP_PRIOR)
    rows.append(r)
json.dump(rows, open(os.path.join(HERE, 'candidates.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(rows), 'rows')
keys = []
for r in KEY_ROWS:
    r.update(source=MAP_SRC, score_note=SCORE, access_note=MAP_ACCESS, seen='image', needs_archive_scan='no')
    r.setdefault('prior_art', MAP_PRIOR)
    keys.append(r)
json.dump(keys, open(os.path.join(HERE, 'keys.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(keys), 'key items (keys.json)')
