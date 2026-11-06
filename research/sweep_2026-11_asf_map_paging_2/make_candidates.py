"""Build candidates.json and keys.json for the second MAP whole-filza paging pass (6 Nov 2026).
Work list: ASF Mediceo avanti il Principato filza CXXXVII, docs 571-1058 (image positions 1217-2476), the part the first pass
(research/sweep_2026-11_asf_map_paging/) left unpaged. Every recto and verso was paged on 4-up contact sheets; flagged pages were
opened at the server maximum. Rows come from images viewed in this pass; see README.md. MAP leads/catalogue items 2307-2389 and
the rows of the three earlier ASF passes are not repeated."""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
B = 'https://archiviodistatofirenze.cultura.gov.it'
SCORE = 'Scored from the images viewed during the second MAP paging pass, 6 Nov 2026 (research/sweep_2026-11_asf_map_paging_2/)'

MAP_SRC = 'ASF Mediceo avanti il Principato (MAP) images, whole-filza paging pass 2 (CXXXVII docs 571-1058), Nov 2026'
MAP_ACCESS = ('scans public on the ASF MAP site, no login, curl works: /map/ricerca/ricerca-su-filza/?f=<filza>&d=<doc> and IIIF '
              '/iipsrv/iipsrv.fcgi?IIIF=/data/iip-data/asfi/mediceo_avanti_principato/00100137/A000NNNN.ptif (about 1272 px max); '
              'image id = 132517 + position - 1 for filza CXXXVII')
MAP_PRIOR = ('open as far as checked (6 Nov 2026): known.py finds nothing on the filza and document or on the writer; no lead or '
             'catalogue entry names the writer; DECODE dumps in the repo have no ASF MAP CXXXVII record except leads 2320/2321; '
             'Tomokiyo, Lasry and the printed editions not searched in this run.')


def maplinks(filza, doc, ids):
    out = [{'href': f'{B}/map/ricerca/ricerca-su-filza/?f={filza}&d={doc}&c=', 'label': f'MAP filza {filza}, doc. {doc}'}]
    out += [{'href': f'{B}/map/riproduzione/?id={i}', 'label': f'image id {i}'} for i in ids]
    return out


FIRST = {137: 132517}  # image id of position 1


def ids(filza, *positions):
    return [FIRST[filza] + p - 1 for p in positions]


def span(a, b):
    return list(range(a, b + 1))


MAP_ROWS = []
KEY_ROWS = []

# ---- rows are added below as each flagged page is checked at full size ----
# Paging: positions 1217-2476 on 4-up contact sheets (each page 390 px wide, contrast-stretched), doubtful pages at 800 px;
# every row below was then opened at the server maximum (1272-1411 px) unless its status says otherwise.

# ---- 1513-15: the Spanish embassy and other orators of the Medici restoration ----
MAP_ROWS += [
    dict(
        year=1513, date='27 Oct 1513 ("In Vagliadulit", closing on the verso)',
        title='Francesco Guicciardini, Florentine ambassador in Spain, Valladolid, 27 October 1513: about 40 lines of sign cipher in three long blocks, bare, endorsed as deciphered',
        correspondents="Francesco Guicciardini (signed \"Fr. de Guicciardinis Dr. Ambasciator\"), Valladolid -> Lorenzo di Piero de' Medici",
        place='Valladolid', language='Italian (sign cipher between clear passages)', region='Italy', period='1497-1559',
        shelfmark='Archivio di Stato di Firenze, Mediceo avanti il Principato, filza CXXXVII, doc. 619 (c. 627)',
        folio_note='c. 627r: clear opening (5 lines), then three blocks of dense sign cipher (Greek-like and Latin-like letters, E, C, ω, '
                   'with superscript digits 1-3 over many signs), about 40 lines in all, separated by clear sentences ("V. M.tia che '
                   'e prudentissima ...", "non voglio dire questo ..."); c. 627v: one cipher line at the top, clear closing, address. '
                   'Head of c. 627r in a contemporary hand, hard to read: "Decifrata ... la copia prec.te"?',
        cls='B',
        status='Bare (1272 px): no interlinear clear text. The head note seems to say it was deciphered, but the neighbours are not '
               'a decipherment (617 blank leaf, 618 a short clear letter of 4 Oct 1513; 620 Corsi\'s letter of the same day).',
        why='A cipher despatch of Guicciardini from his Spanish legation, written to Lorenzo the year the Medici returned. His '
            'legation letters are printed (Canestrini, Opere inedite VI, 1864; Jodogne, Le lettere), very probably from his own '
            'clear minutes in the Archivio Guicciardini, so the clear text may well be in print: check before any work.',
        importance=3, solvability=4, difficulty=2,
        verify='Look up the letter of 27 Oct 1513 to Lorenzo in Jodogne, Le lettere I-II, and Canestrini VI; if it is printed, the '
               'pair gives the key for the Corsi row; if not, transcribe and solve (homophonic sign cipher with superscript indices).',
        links=maplinks(137, 619, ids(137, 1325, 1326)),
        prior_art='Probably printed from Guicciardini\'s own minutes (not checked in this run). known.py: no hit on the document.',
    ),
    dict(
        year=1514, date='27 Oct 1513 - Apr 1514',
        title='Giovanni Corsi, Florentine orator at the court of Ferdinand the Catholic, Valladolid and Madrid, Oct 1513 - Apr 1514: four letters and three contemporary copies with bare letter-and-figure cipher',
        correspondents="Giovanni Corsi (signed \"Jo. Cursius or.\", \"Joannes Cursius or. apud Cath. M.tem\", \"Giovanni Corsi\") -> Lorenzo di Piero de' Medici",
        place='Valladolid, Madrid', language='Italian (letter/figure cipher with superscript indices between clear words)',
        region='Italy', period='1497-1559',
        shelfmark='Archivio di Stato di Firenze, Mediceo avanti il Principato, filza CXXXVII, docs. 620 (c. 628 bis), 621 (c. 629, copy of 620), 622 (c. 630, copy of a letter of 29 Jan 1514), 623 (c. 631 bis), 627 (c. 635?), 628 (copy of 627), 633 (c. 641, copy)',
        folio_note='620 (Valladolid 27 Oct 1513): about 16 cipher lines in two blocks on c. 628 bis r, one on the verso; 621: "Copia di '
                   'lettera de 27 oct. 1513 da Vagliadulit", the same cipher text (about 18 lines); 622: copy of a letter of 29 Jan 1514 '
                   '(about 11 lines); 623 (dated "xvi ... 1513", st. fior. = early 1514): about 22 lines in four blocks; 627 (Madrid, '
                   '25? Dec 1513): about 7 lines; 628: "Copia" of 627 with an added clear paragraph; 633 ("Copia", Madrid 9? Apr 1514): '
                   'about 15 lines. Signs are lower-case letters (a, b, d, e, f, g, k, m, o, t, x, y, z) and digits 3-9 with superscript '
                   'indices, some code groups (R, gg, aba, 1519, 1814) and repeated whole groups between clear words.',
        cls='A',
        status='Bare (1272 px on 620, 623, 627, 633; 800 px on the copies): no interlinear gloss and no filed decipherment beside '
               'any of them (the copies repeat the cipher, they do not decipher it).',
        why='A run of cipher despatches from the Florentine embassy to Spain in 1513-14 (the Holy League, the Swiss, the truce with '
            'France), with duplicate ciphertexts (620/621, 627/628) for checking a transcription; about 90 cipher lines in all. '
            'The same superscript-index style is glossed in CXXXVII 626 and 636 (keys.json) and in the 1513-15 MAP LXXII pairs '
            '(Acciaiuoli, Pandolfini).',
        importance=4, solvability=4, difficulty=3,
        verify='Transcribe 620 and 621 together; test the glossed 626/636 tables and the LXXII Acciaiuoli 190/191 and Pandolfini '
               'pairs; check the Guicciardini row for a printed clear text of the same week; then a homophonic solver on all seven.',
        links=maplinks(137, 620, ids(137, *span(1327, 1330))) + maplinks(137, 621, ids(137, *span(1331, 1334)))
              + maplinks(137, 622, ids(137, *span(1335, 1338))) + maplinks(137, 623, ids(137, *span(1339, 1342)))
              + maplinks(137, 627, ids(137, 1353, 1354)) + maplinks(137, 628, ids(137, 1355, 1356)) + maplinks(137, 633, ids(137, 1367, 1368)),
    ),
    dict(
        year=1514, date='26-27 [month?] 1514 ("a xxv del presente arrivai in corte del Re cath.co"; dated Valladolid ... MDXIIII on the verso)',
        title='A Florentine envoy newly arrived at the court of Ferdinand the Catholic, 1514: about 13 lines of letter-and-figure cipher, bare',
        correspondents="unidentified envoy (signature on the verso, read by the pager as \"Ant.o Pucci\"?, not checked) -> Lorenzo di Piero de' Medici",
        place='Valladolid', language='Italian (letter/figure cipher between clear words)', region='Italy', period='1497-1559',
        shelfmark='Archivio di Stato di Firenze, Mediceo avanti il Principato, filza CXXXVII, doc. 644 (cc. 652-652 bis)',
        folio_note='c. 652r: clear report of the audience, then about 13 lines of cipher (lower-case letters b, d, f, g, l, m, x and '
                   'digits, with numbers 22, 31, 42, 43, 92, 100 standing alone, probably code numbers) between clear words; the '
                   'lower third clear (a horse from the Count of Almazán, falcons, music); c. 652v: closing and signature; c. 652 bis: address to Lorenzo de\' Medici.',
        cls='B',
        status='Bare (1272 px on the recto, 800 px on the verso; neighbours 643 and 645 are clear).',
        why='Another cipher of the 1514 Spanish embassy, apparently a different hand and table from Corsi\'s.',
        importance=2, solvability=3, difficulty=3,
        verify='Read the signature and the month on c. 652v at full size; transcribe; compare with the Corsi table.',
        links=maplinks(137, 644, ids(137, *span(1399, 1402))),
    ),
    dict(
        year=1515, date='Sept 1515 (headed "6 sett.e 1515"?; closing "... septembre 1515", Vercelli?)',
        title='Francesco Pandolfini, Florentine orator, to the Otto di Pratica, September 1515 (contemporary copy): about 60 lines of sign cipher in a two-leaf letter, bare',
        correspondents='Francesco Pandolfini (signed "Franciscus Pandulphinus") -> the Otto di Pratica (copy for the Medici)',
        place='Vercelli? (with the papal orator and Raffaello Girolami)', language='Italian (sign cipher with superscript digits between clear words)',
        region='Italy', period='1497-1559',
        shelfmark='Archivio di Stato di Firenze, Mediceo avanti il Principato, filza CXXXVII, doc. 666 (cc. 674-674 bis)',
        folio_note='c. 674r headed "Copia della l(ette)ra del mag.co or(ato)re Franc.o Pandolphini a S(ignori) Otto di pratica": 9 clear '
                   'lines, then about 28 lines of sign cipher (3, y, g, t, 7, z, F, x with superscript digits 1-5 and bars); c. 674v: '
                   'about 17 lines, clear closing, clear postscript; c. 674 bis r-v: about 24 more cipher lines between clear passages '
                   '(Swiss, Milan, Lombardy).',
        cls='A',
        status='Bare (1392 px on c. 674r; 800 px on the rest). Neighbours 665 and 667 (a clear letter of 6 Sept 1515) are not a '
               'decipherment.',
        why='A long cipher despatch from the weeks before Marignano (13-14 Sept 1515). Pandolfini\'s 1514-15 French embassy '
            'cipher (catalogue: LXXII rows, superscript-index system) has plaintext pairs in LXXII 281-368: a direct key test.',
        importance=4, solvability=5, difficulty=2,
        verify='Test the Pandolfini table rebuilt from the LXXII pairs (334/332, 308/313); read; check whether the original is in '
               'the Otto di Pratica Responsive.',
        links=maplinks(137, 666, ids(137, *span(1463, 1466))),
        prior_art=MAP_PRIOR + ' The catalogued Pandolfini rows (MAP LXXII, Oct 1514 - Mar 1515) do not include this Sept 1515 copy.',
    ),
]

# ---- 1520-21: Galeotto de' Medici, orator in Rome, and Cardinal Giulio de' Medici ----
MAP_ROWS += [
    dict(
        year=1521, date='11 Jan 1521 ("Ex Urbe die xj Januarii MDXXI"; 1522 if Florentine style)',
        title="Galeotto de' Medici, Florentine orator in Rome, 11 January 1521: seven lines of sign cipher, bare",
        correspondents="Galeotto de' Medici (signed \"Galeottus de Medicis orator\"), Rome -> \"Magnifici domini\" (the Medici government in Florence)",
        place='Rome', language='Italian (sign cipher: Latin letters, digits, ÷, Δ, #, φ)', region='Italy', period='1497-1559',
        shelfmark='Archivio di Stato di Firenze, Mediceo avanti il Principato, filza CXXXVII, doc. 728 (cc. 736-736 bis)',
        folio_note='c. 736r: one clear line, then 7 lines of continuous cipher (z, #, 7, n, x, ÷, u, φ, Δ, 3, 4, 2, superscript o), '
                   'clear closing, date and signature; c. 736v blank; c. 736 bis v address "Mag.cis D.nis ... Florentie".',
        cls='B',
        status='Bare (1272 px). Neighbours 727 (a short clear letter with the same large signature as 733-734) and 729 (a clear letter of Feb 1521) '
               'are not a decipherment.',
        why='Short, but one of a correspondence between Galeotto in Rome and Cardinal Giulio de\' Medici in Florence that is '
            'in cipher both ways (next row).',
        importance=2, solvability=2, difficulty=3,
        verify='Transcribe; compare the sign set with the Card. Giulio letters 733-734.',
        links=maplinks(137, 728, ids(137, *span(1655, 1658))),
    ),
    dict(
        year=1521, date='Florence, May 152[0 or 1] (733: "Florentiae ... Maij M.D.XX."; 734: "Floren. xv Maij MDXX.", last numeral unclear)',
        title="Cardinal Giulio de' Medici (the future Clement VII) to Galeotto de' Medici in Rome, May 1520/21: two letters wholly in two different sign ciphers, bare",
        correspondents="Card. Giulio de' Medici, vice-chancellor (large autograph signature \"V. Jul. vicecancell.\"; the same as on doc. 735, Rome 19 July 1523) -> Galeotto de' Medici, Rome",
        place='Florence', language='Italian (two sign ciphers)', region='Italy', period='1497-1559',
        shelfmark='Archivio di Stato di Firenze, Mediceo avanti il Principato, filza CXXXVII, docs. 733 (c. 741) and 734 (c. 742)',
        folio_note='733 c. 741r: after "Ven. nobis dilect.", a whole page (about 28 lines) of geometric signs (squares, crosses, '
                   'T-shapes, circles, loops, dotted and double-dotted signs) evenly spaced; c. 741v: about 14 more lines, then clear '
                   'closing, date and signature. 734 c. 742r: after "Mag.ce vir amice mi char.me", about 14 lines of a different '
                   'alphabet (3, x, D, φ, square, U, B, 6, 8, z-like signs), "Ben valete Floren. xv Maij MDXX.", signature; '
                   'address on c. 742 bis v to Galeotto de\' Medici in Rome.',
        cls='A',
        status='Bare (1272 px on both rectos; 800 px on the versos). Neighbours 732 and 735 are clear letters; no decipherment '
               'filed beside them.',
        why='Outgoing cipher of Cardinal Giulio, who ran Florence and the Medici foreign policy for Leo X, to the family\'s orator '
            'in Rome, in the year of the imperial alliance (May 1521). About 55 lines in two systems, enough for a ciphertext-only '
            'attack on each; 734 is a plain-looking simple-substitution alphabet of about 20 signs.',
        importance=4, solvability=4, difficulty=2,
        verify='Read the year at full size (Giulio was vice-chancellor until Nov 1523); transcribe 734 first (short alphabet, word '
               'spacing absent) and solve as monoalphabetic with homophones; then 733.',
        links=maplinks(137, 733, ids(137, *span(1669, 1672))) + maplinks(137, 734, ids(137, *span(1673, 1676))),
    ),
    dict(
        year=1520, date='undated (filed among letters of 1520-23)',
        title='Two pages in a crude hand whose dot-separated words mostly do not read as Italian ("alpobbo", "farake", "z n s" for N.S.): possibly a word-preserving letter substitution, unglossed',
        correspondents='unidentified (signature on the next leaf read by the pager as "Fran.al ...", not checked)',
        place='not stated', language='Italian? (disguised words, word division kept)', region='Italy', period='1497-1559',
        shelfmark='Archivio di Stato di Firenze, Mediceo avanti il Principato, filza CXXXVII, doc. 747 (cc. 756-756 bis)',
        folio_note='c. 756r-v: two full pages, each word followed by a dot; many words are ordinary Italian ("amico", "molto", '
                   '"messo", "come", "papa"?), others are not ("alpobbo" repeated, "farake", "nasalji", "z n s" where "N. S." '
                   'would stand), so either a partial letter substitution or only a very corrupt phonetic hand.',
        cls='C',
        status='Unsure whether cipher at all (1272 px on the recto); no gloss, no clear copy beside it.',
        why='If it is a disguise, a cheap letter-substitution test settles it; otherwise it drops.',
        importance=1, solvability=3, difficulty=2,
        verify='Transcribe ten lines and test a simple letter substitution on the non-words (e.g. "z n s" = "N. S.", "alpobbo" = '
               '"el papa"?).',
        links=maplinks(137, 747, ids(137, *span(1719, 1722))),
    ),
]

# ---- key sources (cls K) ----
KEY_ROWS += [
    dict(
        year=1513, date='11 Dec 1513 (626, "Ex Turegho xi x.bris") and May 1514 (636)',
        title='Two glossed letters of 1513-14 in letter-and-figure cipher with interlinear decipherment: a Medici agent with the Swiss (Zurich) and "Raffaello ..." (Rome? 1514)',
        correspondents="626: an agent at Zurich (signature read by the pager as \"S.tor ... Ghorus?\") -> Lorenzo di Piero de' Medici; 636: Raffaello [surname not read] -> a Medici patron",
        place='Zurich; not stated', language='Italian', region='Italy', period='1497-1559',
        shelfmark='Archivio di Stato di Firenze, Mediceo avanti il Principato, filza CXXXVII, docs. 626 (cc. 634-634 bis) and 636 (c. 644)',
        folio_note='626 c. 634r: 4 cipher lines in the middle (lower-case letters, digits 2-9, H, KK, superscript indices) with '
                   'interlinear clear text in a second hand ("io ho ricercato cinque cantoni de suizeri"); c. 634v: '
                   'about 10 lines, glossed (Swiss, the Catholic king, the emperor, the king of England); c. 634 bis r: one glossed line. '
                   '636 c. 644r: about 16 lines in two blocks, glossed (the king of England, the Swiss); c. 644v: about 7 glossed lines.',
        cls='K', status='Glossed (1272 px on 634r and 644r).',
        why='Plaintext-aligned examples of the 1513-14 superscript-index ciphers: the first test for the bare Corsi letters and '
            'the Guicciardini letter (rows), and for the MAP LXXII 1513-15 family.', importance=3,
        verify='Record the sign/letter pairs of each and compare the tables with each other and with the Corsi ciphertext.',
        links=maplinks(137, 626, ids(137, *span(1349, 1352))) + maplinks(137, 636, ids(137, 1375, 1376)),
    ),
    dict(
        year=1495, date='undated (late 15th or early 16th century; names Orlando Pallavicino, Parma, Cremona?, Ferrara, Venice)',
        title='Two small code-word lists (numbered cover words and signs for persons and places), undated, unattributed',
        correspondents='unknown (Medici chancery or an agent); no address',
        place='not stated', language='Italian', region='Italy', period='15th-16th century',
        shelfmark='Archivio di Stato di Firenze, Mediceo avanti il Principato, filza CXXXVII, docs. 1053 (old nos. 643/551) and 1054 (old nos. 152/408)',
        folio_note='1053 r: a grid of 20 numbered entries, each a meaning above a cover word ("Lorenzo" 1, "la guerra"/"la nebia" 5, '
                   '"el papa"/"el fratello" 12, "la pratica"/"la fine" 18; "messer Pallo" 20?), some struck through. 1054 r: about 22 '
                   'entries, a name or term ("Vinegia", "Firenze", "Cardinale", "Orlando Palavicino", "Parma") with a cover word below '
                   'and a sign or number under each (3, 9, p, m, b, f, kh, L, then 1-22); 1054 v: two or three more entries.',
        cls='K', status='Key lists (1341-1411 px); not matched to any letter.',
        why='Two small nomenclators of cover words: keys for jargon letters (cover words in clear text) rather than for sign cipher; '
            'a date from the names would place them (an Orlando Pallavicino is active under the Ambrosian Republic, 1447-50, and another c. 1500).', importance=2,
        verify='Transcribe both lists; date from the persons named; search MAP for letters using the cover words ("la nebia", "el '
               'fratello", "la fine").',
        links=maplinks(137, 1053, ids(137, 2463, 2464)) + maplinks(137, 1054, ids(137, 2465, 2466)),
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
