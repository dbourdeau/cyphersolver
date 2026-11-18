"""Build candidates.json and key_leads.json for the Omont / Ancien-fonds 'avec chiffre' sweep (14 Nov 2026).

Rows are written by hand from the printed catalogue entries (parse_omont.py -> fixnum.py -> summarise.py output, read in
detail.txt); the Gallica arks come from ark_map.json (Gallica SRU queried from a Chrome tab, dc.source = 'Français N').
    python make_candidates.py
"""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
AM = json.load(open(os.path.join(HERE, 'ark_map.json'), encoding='utf-8')) if os.path.exists(os.path.join(HERE, 'ark_map.json')) else {}
CAT = ('Omont/Delisle printed Catalogue general des manuscrits francais, Ancien fonds (1868-1895; archive.org '
       'cataloguemanfran / p1cataloguegnr volumes, OCR)')


def links(frs, extra=None):
    out = []
    for n in frs:
        a = AM.get(str(n))
        if a:
            out.append({'label': f'Gallica, fr. {n}', 'href': f"https://gallica.bnf.fr/ark:/12148/{a['ark']}"})
            if a.get('cat'):
                out.append({'label': f'BnF Archives et manuscrits, fr. {n}', 'href': f"https://archivesetmanuscrits.bnf.fr/ark:/12148/{a['cat']}"})
    out.append({'label': 'Printed catalogue (archive.org OCR), Ancien fonds', 'href': 'https://archive.org/details/cataloguemanfran02bibluoft'})
    out += extra or []
    return out


def digit(frs):
    d = [n for n in frs if AM.get(str(n))]
    if len(d) == len(frs): return 'no', 'Gallica volume(s) online: ' + ', '.join(f'fr. {n}' for n in d) + '; openapi.bnf.fr IIIF works with curl'
    if d: return 'partly', 'Gallica has fr. ' + ', '.join(map(str, d)) + '; not found for the others'
    return 'yes', 'no Gallica ark found for ' + ', '.join(f'fr. {n}' for n in frs) + ' (Gallica SRU, dc.source "Français N"); microfilm or reading room, or a later digitisation'


ROWS = []


def row(frs, year, date, title, corr, place, lang, region, period, folio, why, imp, sol, dif, note='', cls='C', verify=None, prior=None):
    nas, acc = digit(frs)
    shelf = 'BnF Manuscrits, ' + ', '.join(f'fr. {n}' for n in frs)
    ROWS.append({
        'year': year, 'date': date, 'title': title, 'correspondents': corr, 'place': place, 'language': lang, 'region': region,
        'period': period, 'shelfmark': shelf, 'folio_note': folio, 'cls': cls,
        'status': ('Printed catalogue entry (' + CAT + ') lists these pieces as "avec chiffre" / "en chiffre" with no decipherment noted; '
                   'where the catalogue says "avec chiffre et dechiffrement" a decipherment is attached and the piece is not counted here. '
                   'Not viewed. ' + note).strip(),
        'why': why, 'importance': imp, 'solvability': sol, 'difficulty': dif,
        'score_note': 'Scored from the printed catalogue description during the 14 Nov 2026 Omont BnF sweep (research/sweep_2026-11-14_omont_bnf/); not viewed',
        'verify': verify or 'Open the volume on Gallica at the folios named, check that the cipher leaf has no contemporary decipherment on it or next to it; compare Tomokiyo and DECODE for the same folios.',
        'links': links(frs), 'seen': 'catalogue', 'source': 'Omont BnF catalogue sweep',
        'prior_art': prior or 'open as far as checked (14 Nov 2026): known.py on the shelfmark and the correspondents, grep of catalogue.json, leads.json, targets/*/NOTES.md and the Tomokiyo pages in research/gallica_sweep/src; no web search for this row',
        'needs_archive_scan': nas, 'access_note': acc,
    })


row([3231, 3232], 1571, 'Sep 1570 - Mar 1572',
    'Lodovico Birago (governor of Saluzzo) to the duke of Nevers, 14 Italian letters "avec chiffre"',
    'Lodovico Birago -> Louis de Gonzague, duke of Nevers', 'Saluzzo', 'Italian (a few French)', 'France', '1560-1589',
    'fr. 3231 nos. 6, 18, 42, 43, 63 ... (ff. 11, 35, 82, 87, 119 ...; 12 letters without decipherment, no. 20 f. 39 has one) and fr. 3232 nos. 30 (f. 47) and 77 (f. 117)',
    'Piedmont-Saluzzo governor reporting to Nevers during the 1570-72 war years; a run of 14 letters by one hand gives a long single-key sample, with the decipherments of nos. 20 (f. 39) and others as cribs.',
    3, 4, 2, cls='A',
    note='Same volume has Birago letters with decipherment (e.g. fr. 3231 f. 39), so a key is rebuildable. The repo has birago1571 (a different Birago piece, fr. 4702); fr. 3231/3232 are not in it.')
row([3057], 1590, '7 Sep 1589 - 26 Nov 1592',
    'Philip II, Mendoza and Ibarra, Spanish ciphered letters of the Paris embassy during the League (7 pieces)',
    'Philip II -> Bernardino de Mendoza; Mendoza -> Philip II and Idiaquez; Diego de Ibarra -> Philip II and the count of Olivares', 'San Lorenzo / Paris', 'Spanish', 'France', '1589-1598',
    'nos. 5 (f. 10), 27 (f. 58), 28 (f. 60), 43 (f. 91), 48 (f. 105) and two more "avec chiffre"; nos. 1-2 (Farnese to Philip II, Brussels 1588-89) carry a decipherment in the same volume',
    'Spanish diplomatic cipher of the League years, the Mendoza/Ibarra key family, with decipherments of the Farnese letters in the same volume as cribs.',
    4, 3, 3, cls='A',
    note='The printed entry opens with letters of Mary Stuart to the duchess of Nemours; the OCR heading reads 3057 and Gallica confirms fr. 3057 ("Recueil de lettres originales", 1501-1600). Catalogue 285 (Mary Stuart to Mauvissiere) is a different item.')
row([3652, 3339], 1612, 'Apr 1603; Nov 1611 - Mar 1613',
    'Henri IV (1603) and Marie de Medicis, Villeroy and Puysieulx (1611-13) to Savary de Breves, 22 letters "avec chiffre"',
    'Henri IV; Marie de Medicis; Nicolas de Neufville de Villeroy; Pierre Brulart de Puysieulx -> Francois Savary de Breves', 'Paris / Fontainebleau', 'French', 'France', '1611-1650',
    'fr. 3652 nos. 6, 8, 11, 12, 13 ... (ff. 10, 14, 20, 22, 26; 11 pieces) and fr. 3339 nos. 23-30 and more (ff. 60-75; 11 pieces), Breves as ambassador at Constantinople (1603) and Rome (1611-13)',
    'Royal and secretary-of-state despatches to one ambassador across ten years; Breves nomenclators are already worked in this repo (breves1603, catalogue 25), so keys exist for the early ones.',
    4, 4, 2, cls='B',
    note='Catalogue 25 (Marie de Medicis to Breves, 1610) and targets/breves1603 are the neighbouring items; the 1611-13 letters are not in either.')
row([3374, 4697, 4691], 1586, 'Jun 1585 - Dec 1586',
    'Louis de Gonzague, duke of Nevers, minutes "avec chiffre" to Scipione Gonzaga, Camillo Volta and others, 1585-86',
    'Louis de Gonzague, duke of Nevers -> Scipione Gonzaga (patriarch of Jerusalem), Camillo Volta; Guazzo -> Nevers', 'La Cassina / Chenonceau / Mirebeau / Cognac', 'Italian', 'France', '1560-1589',
    'fr. 3374 nos. 3, 61, 63 (ff. 4, 143, 145); fr. 4697 nos. 15-30 (ff. 14-49, copies and minutes marked "Chiffre"); fr. 4691 nos. 103-106 (ff. 179 ff., minutes with "Chiffre")',
    'Nevers wrote to his Gonzaga relatives in cipher; the minutes survive in his papers, so the plaintext intent is near the cipher text.',
    3, 3, 3,
    note='The catalogue marks several of these "Minute" or "Copie ... Chiffre", i.e. ciphered text or its clear original in the same hand; the nomenclator is not described.')
row([3422], 1589, '8 Apr - 18 Jun 1589',
    'Anonymous and initialled ciphered letters to the duke of Nevers during the war of the League, spring 1589 (6 pieces)',
    'signed "M...", "DE..." and unsigned -> Louis de Gonzague, duke of Nevers', 'France', 'French', 'France', '1560-1589',
    'fr. 3422 nos. 27 (f. 38 bis), 60 (f. 106), 62 (f. 108), 68 (f. 117), 69 (f. 118) and one more',
    'Ciphered news to Nevers from correspondents the catalogue could not name; a decipherment would identify them and the 1589 intelligence network.',
    3, 3, 3, note='Tomokiyo nevers.htm covers fr. 4702, 4712, 4715 only (README of research/gallica_sweep).')
row([3624, 3614, 3634, 3646], 1593, 'Apr 1589 - Jul 1593',
    'Ciphered letters to and from the duke of Nevers, 1589-93: Marchant, Lairiere, Montholon and others (12 pieces)',
    'Marchant; Lairiere; Nevers -> Montholon; unknown -> Nevers', 'France', 'French', 'France', '1589-1598',
    'fr. 3624 nos. 47, 51, 67 (Marchant, ff. 53, 57, 78) and 53 (Lairiere, f. 66); fr. 3614 nos. 58, 61, 64 (ff. 89, 94, 73); fr. 3634 nos. 4, 20, 60; fr. 3646 nos. 53, 67 (ff. 108, 129)',
    'Four volumes of the Nevers papers with ciphered intelligence letters from the League years; the nomenclators of the Nevers correspondence (nevers1587, nevers1594gondi, revol1593) are already in the repo.',
    3, 3, 3, cls='B', note='Neighbouring volumes fr. 3612, 3613, 3622, 3633 are already targets here (orbais, rondinelli1590, nevers1594gondi, blancmesnil).')
row([3329, 3409, 4717], 1578, 'Apr 1577 - Nov 1578',
    'Letters "avec chiffre" to the marquis de Humieres, governor of Peronne, 1577-78, with two cipher tables in fr. 3329',
    'Maineville; Pierre de Roncherolles; Philippe Laisne; unknown -> Jean de Humieres', 'Peronne / Chenonceaux', 'French', 'France', '1560-1589',
    'fr. 3329 nos. 1-2 (two "tables de chiffres"), 78 (f. 159), 81 (f. 104), 82 (f. 105); fr. 3409 no. 49 (f. 126, 21 Nov 1578); fr. 4717 no. 49 (f. 91, 2 Apr 1577)',
    'A governor of Peronne in the 1577 war of the League of Peronne; the cipher tables sit in the same collection as the letters, a rare case of key and ciphertext together.',
    3, 4, 2, cls='A', note='fr. 3329 also holds the "Nouvelles d\'Alencon, 3 May 1577, avec chiffre" (f. 159); not a Villeroi 1577 letter (that is already solved here).')
row([2986], 1526, '1526-27',
    'Hieronimo Ranzo and Nicolas Raince, ciphered letters from Rome, 1526-27 (27 pieces "en chiffre")',
    'Hieronimo Ranzo; Nicolas Raince -> grand master Anne de Montmorency', 'Rome', 'French / Italian', 'Papacy', '1497-1559',
    'fr. 2986 nos. 1, 2, 3, 7, 9 and 22 more ("lettre en chiffre", "piece en chiffre", "double de lettres escriptes en chiffre par Nicolas Raince"; ff. 1-60 and on)',
    'The largest single run of Rome ciphers in the Montmorency papers, from the same pair as the Raince and Ranzo targets already read here (fr. 2984, 2988).',
    3, 4, 2, cls='B',
    note='Raince (fr. 2984 f. 2) and Ranzo (fr. 2988 ff. 9-10, fr. 3022 no. 20) are targets here with keys, so this volume is a sibling run; the catalogue does not say which of the 27 have a decipherment.')
row([3027], 1530, 'c. 1525-1535',
    'Ciphered letters in the Montmorency papers, Bonnivet volume: "lettres en chiffre" ff. 67-202 (about 12 letters)',
    'unknown (volume opens with letters of admiral Bonnivet to the marshal of Montmorency)', 'unknown', 'French', 'France', '1497-1559',
    'fr. 3027 nos. 34 (f. 67), 49 (ff. 100, 102, 105), 70 (f. 182), 72 (ff. 186, 188, 190, 191, 193, 193, 197, 199, 202)',
    'Eight leaves of one run (ff. 186-202) in a single hand, sender unnamed by the cataloguer; likely a dispatch series from Italy or Switzerland.',
    2, 3, 3, note='Volume number printed as 5027 in the OCR; Gallica has fr. 3027 (Recueil de lettres et de pieces originales, 1501-1600), matching the Ane. 8554 note.')
row([2935], 1525, '16 Oct 1525',
    'Cardinal Giovanni Salviati, letter "en chiffres" in Italian, 16 Oct 1525',
    'Cardinal Giovanni Salviati -> unknown', 'unknown', 'Italian', 'Papacy', '1497-1559', 'fr. 2935 no. 11 (f. 34)',
    'One cipher letter (Italian) among clear ones; recipient not named in the entry.', 2, 3, 3)
row([2996, 3137], 1549, 'Jan 1546 (year garbled in OCR); 12 Nov 1549',
    'Jean de Morvillier (ambassador at Venice), two despatches "en chiffre" to the king',
    'Jean de Morvillier -> Francois I / Henri II', 'Venice', 'French', 'France', '1497-1559',
    'fr. 2996 no. 23 (f. 33, year printed 134(), read as 1546) and fr. 3137 no. 24 (f. 60, 12 Nov 1549)',
    'Venice despatches of a French ambassador whose Aug 1549 letter with its decipherment is in fr. 3138 f. 70 (noted in targets/guiche1551), giving a crib for the key.',
    2, 4, 2, cls='A')
row([3043], 1535, 'undated, 13 Oct',
    'Robert Cenalis, bishop of Avranches, despatch "avec chiffre" to the king from Venice',
    'Robert Cenalis -> Francois I', 'Venice', 'French', 'France', '1497-1559', 'fr. 3043 no. 29 (f. 36)',
    'One Venice despatch in the Montmorency papers.', 2, 3, 3)
row([3373, 3086], 1598, '22 Nov 1597; 14 Jun 1598',
    'Anne de Levis, duke of Ventadour, letters "avec chiffre" to the duke of Montmorency, Pezenas, 1597-98',
    'Anne de Levis, duc de Ventadour -> Henri de Montmorency', 'Pezenas', 'French', 'France', '1589-1598',
    'fr. 3086 no. 57 (f. 118, 22 Nov 1597, with a second letter no. 58; OCR heading 5086, Gallica has fr. 3086) and fr. 3373 no. 29 (f. 43, 14 Jun 1598); fr. 3373 no. 36 (f. 56) is a "Chiffre" (key)',
    'Letters from Pezenas to Montmorency; the key (fr. 3373 f. 56) sits in the same volume as one of the letters.',
    2, 4, 2, cls='A')
row([3638], 1617, '18 Oct 1617',
    'Duke of Monteleon (Spanish embassy, Paris), letter "avec chiffre" to Pedro de Toledo, copy',
    'Duque de Monteleon -> Pedro de Toledo', 'Paris', 'Spanish', 'France', '1611-1650', 'fr. 3638 no. 24 (f. 48)',
    'A Spanish ambassador\'s cipher letter in a French volume.', 3, 3, 3)
row([3689], 1623, '26-29 Aug 1623',
    'Daniel de La Mothe Houdancourt, bishop of Mende: "advis en chiffre" and ciphered letters to Richelieu, Aug 1623 (3 pieces)',
    'Daniel de La Mothe-Houdancourt, evesque de Mende -> Cardinal de Richelieu', 'France / Switzerland', 'French', 'France', '1611-1650',
    'fr. 3689 nos. 13, 22 ("advis en chiffre", no folio) and 26 (f. 15, "lettre en chiffre ... receue le 29 aoust 1623")',
    'Ciphered advice from the bishop of Mende to Richelieu in a volume otherwise on the Swiss embassy of 1625-26.',
    3, 3, 3)
row([3837, 3730, 3834], 1633, '19 Jun - 9 Jul 1633; 3 Aug 1633; 27 Mar 1649',
    'Bouthillier, Chatillon and the prince de Conti, ciphered memoirs and letters, 1633 and 1649 (4 pieces)',
    'Claude Bouthillier -> M. de Guron and others; marechal de Chatillon -> Servien; Armand de Bourbon, prince de Conti', 'Paris / Nijmegen', 'French / Latin', 'France', '1611-1650',
    'fr. 3837 nos. 15 (f. 25, Latin memoir), 18 (f. 30); fr. 3730 no. 104 (f. 123); fr. 3834 no. 42 (f. 115)',
    'Four short ciphered items of the Thirty Years War and Fronde years; low individual weight, grouped by volume only.',
    2, 3, 3, note='Grouped for convenience: separate sender/recipient pairs, would be split to one key per entry at vetting.')
row([3796], 1618, '28 Dec 1618',
    'Louis XIII to the duke of Nevers, letter "avec chiffre"', 'Louis XIII -> Charles de Gonzague, duke of Nevers', 'Paris', 'French', 'France', '1611-1650', 'fr. 3796 no. 38 (f. 61)',
    'A royal cipher letter to Nevers in the year of the Mantua negotiations.', 2, 3, 3)
row([4137], 1637, '3 Sep 1637',
    'Sabran, "memoire en chiffre" sent to Savoy, Bordeaux and Emery, 3 Sep 1637',
    'Sabran -> Duchess of Savoy (S. A.), the archbishop of Bordeaux and d\'Emery', 'Turin', 'French', 'Italy', '1611-1650', 'fr. 4137 no. 112 (f. 128)',
    'Sabran 1633 (Louis XIII to Sabran) is a target here; this is a different year and a memoir sent in cipher.', 3, 3, 3,
    note='The catalogue calls it "Livre des lettres et negociations de M. de Sabran, 1637-38"; the sabran1633 target is a different volume (fr. 4135).')
row([4733], 1573, '26 Apr 1573; 4 Oct 1586',
    'Lanssac (Warsaw, 1573) and an envoy at Edinburgh (1586): letters "avec chiffre"',
    'Lanssac -> Charles IX (1573); S. de "Colrcem-es" (name garbled in the OCR) -> Henri III (1586)', 'Warsaw / Edinburgh', 'French', 'Poland-Lithuania', '1560-1589',
    'fr. 4733 no. 51 (f. 124, Lanssac, Warsaw, 26 Apr 1573 "avec chiffre"); no. 141 (f. 363, envoy at Edinburgh, 4 Oct 1586 "avec chiffre et dechiffrement", so with a decipherment)',
    'Henri d\'Anjou\'s election as king of Poland: a French despatch from Warsaw in the Mantua-family papers.', 3, 3, 3,
    note='Only no. 51 lacks a decipherment; no. 141 is listed for context. The "Lanssac" and "Bouthillier" strings hit the ledgers 13 times each, not checked individually.')
row([3437], 1601, '1 May 1601',
    'Henri IV to Cardinal d\'Ossat, letter "avec chiffre"', 'Henri IV -> Arnaud d\'Ossat', 'Fontainebleau', 'French', 'Papacy', '1598-1610', 'fr. 3437 no. 2 (f. 8)',
    'Royal cipher letter to the ambassador at Rome; d\'Ossat\'s ciphers are known in print.', 3, 3, 2, cls='B')
row([3826, 3823, 3855], 1629, '14 Apr - 1 May 1629',
    'Richelieu to Denis Bouthillier de Rance and Marie de Medicis, Susa 1629: 10 letters "avec chiffre" in three volumes',
    'Cardinal de Richelieu -> Denis Bouthillier de Rance; -> Marie de Medicis', 'Suse', 'French', 'France', '1611-1650',
    'fr. 3826 nos. 8, 10, 17, 18, 19 and two more (ff. 24-54); fr. 3823 no. 28 (f. 77); fr. 3855 no. 15 (f. 46)',
    'Richelieu\'s own Susa letters; the repo already holds lead 1577 for fr. 3828/3835 and the solved fr. 3829 ff. 87, 89, so this adds the other volumes of the run.',
    4, 4, 2, cls='A',
    note='Overlaps lead 1577 (Richelieu to Rance, 7 letters) in subject; the folio sets here are in other volumes (fr. 3826, 3823, 3855), to be checked against 1577 at merge.')

json.dump(ROWS, open(os.path.join(HERE, 'candidates.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

KEYS = [
    {'shelfmark': 'fr. 3314 f. 12', 'what': 'Chiffre of the duke of Nevers sent to the duchess, Cracow, 26 Mar 1574 (and its double, no. 3)', 'use': 'Nevers 1574 letters'},
    {'shelfmark': 'fr. 3329 nos. 1-2', 'what': 'Two tables of chiffres in the Humieres papers', 'use': 'fr. 3329, 3409, 4717 Humieres letters 1577-78'},
    {'shelfmark': 'fr. 3336 f. 59; fr. 3361 ff. 57, 85; fr. 3411 ff. 109, 125, 137; fr. 3373 f. 56', 'what': 'Bare "Chiffre" leaves among Nevers and Montmorency papers (1580s-1590s)', 'use': 'neighbouring letters in the same volumes'},
    {'shelfmark': 'fr. 3454 f. 10', 'what': 'Chiffre given to Bethune going to Scotland, May 1599', 'use': 'Bethune Scotland mission 1599 (fr. 3484 nos. 1 ff.)'},
    {'shelfmark': 'fr. 3810 f. 1', 'what': 'Chiffre of M. de Chasteaurenault, 13 Sep 1617', 'use': 'Spanish/Netherlands letters of 1617'},
    {'shelfmark': 'fr. 4030 f. 1', 'what': 'Chiffre for Hotman (Villiers Hotman) going to the Cleves-Juliers duchies, plus Villeroy letter avec chiffre f. 166 (28 Apr 1612)', 'use': 'Villeroy to Hotman 1612'},
    {'shelfmark': 'fr. 4471 ff. 2, 17', 'what': '"Recueil de plusieurs chiffres": cardinal Du Bellay, the admiral, Saumaise (found in Sweden)', 'use': 'Du Bellay 1530s-40s, 17th-century Saumaise cipher'},
    {'shelfmark': 'fr. 4720 ff. 1, 68, 70, 78; fr. 4724 ff. 69, 136; fr. 4725 ff. 8, 50, 68; fr. 4727 f. 1; fr. 4703 f. 106', 'what': 'Nevers papers, 1619-23: chiffres with Du Coudray (Hollande), Deshays (Levant), count Scotti, marshal Brissac, Rusca, P. Yberois, M. Simon; name lists "a mettre en chiffre"', 'use': 'Milice chretienne and Levant correspondence of Charles de Gonzague'},
]
json.dump(KEYS, open(os.path.join(HERE, 'key_leads.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(ROWS), 'rows;', len(KEYS), 'key-only groups')
