import json
P = 'https://pares.cultura.gob.es/ParesBusquedas20/catalogo/show/'
SRC = ('PARES (hit list research/pares_ags/hits.jsonl, 27 Oct 2026; records not reopened: PARES returned 429 to curl and '
       'to Chrome from 14 Nov 2026 18:20 on), 14 Nov 2026')


def row(year, date, title, corr, place, lang, period, shelf, folio, cls, status, why, imp, sol, dif, ids, img, verify):
    return dict(
        year=year, date=date, language=lang, region='Spain', period=period, title=title, correspondents=corr,
        place=place, shelfmark=shelf, folio_note=folio, cls=cls, status=status, why=why, importance=imp,
        solvability=sol, difficulty=dif, verify=verify,
        links=[{'href': P + i, 'label': 'PARES ' + i} for i in ids], source=SRC,
        score_note=('Scored from the PARES hit-list row (signatura, dates, title, hit term, image flag) on 14 Nov 2026; '
                    'the record and images were not opened this sweep'),
        prior_art=('open as far as checked (14 Nov 2026): known.py and a shelfmark grep against catalogue.json, leads.json, '
                   'every candidates.json / key_leads.json / sweep README and the targets find nothing on this shelfmark; '
                   'no web, Tomokiyo or Lasry search made in this sweep'),
        seen='catalogue', needs_archive_scan='no' if img else 'unknown',
        access_note=('PARES shows images for this unit (hit-list flag); not viewed' if img else
                     'PARES description only in the hit list (no image flag); digitisation not confirmed'))


R = []
R.append(row(1521, 'Jul-Sep 1521',
 'Condestable de Castilla (Iniguez Fernandez de Velasco) to Rodrigo Ponce de Leon, I duke of Arcos, on the war with France in Navarre: AHNOB Osuna C.1634 D.127-132, hit "cifrada"',
 'Inigo Fernandez de Velasco, constable of Castile -> Rodrigo Ponce de Leon, I duque de Arcos',
 'Castile / Andalusia (Navarre campaign)', 'Spanish', '1497-1559', 'AHNOB, OSUNA,C.1634,D.127-132',
 'Six documents, 5 Jul-23 Sep 1521; sibling D.133 (the constable, undated). The same box holds Arcos letters of many writers (D.124-347)',
 'A',
 'Description only (hit on "cifrada"); which letters carry cipher groups and whether a decipherment is filed was not seen. OSUNA,C.1634 was named in the 9 Nov spain_nobility_aca README as "not opened"; no row exists.',
 'A Castilian grandee writing to another in the Navarre war of 1521, one of the earliest private Spanish ciphers if the hit is a real cipher; images online; one writer, so one key per entry.',
 3, 3, 3, ['6063148', '6063155'], True,
 'Open 6063148 on PARES and look for cipher groups; compare with the Comunidades-era ciphers already in the catalogue.'))
R.append(row(1521, '24 Jul 1521',
 'Banuelos de Trevino to the duke of Arcos on government affairs: AHNOB Osuna C.1634 D.124, hit "cifrada"',
 'Banuelos de Trevino -> Rodrigo Ponce de Leon, I duque de Arcos', 'Castile', 'Spanish', '1497-1559',
 'AHNOB, OSUNA,C.1634,D.124', 'Single document dated 24 Jul 1521', 'B',
 'Description only; cipher extent not seen.',
 'A single 1521 letter flagged cipher with images; short, so mainly a probe of the box.',
 2, 2, 3, ['6063091'], True,
 'Open the images; if cipher, pair with the 1521 constable letters (D.127-132).'))
R.append(row(1521, '1520-21',
 'Pedro Munoz de Cordoba to the I duke of Arcos on the political and military situation, 1520-21: AHNOB Osuna C.1635 D.130-134, hit "cifrada"',
 'Pedro Munoz de Cordoba -> Rodrigo Ponce de Leon, I duque de Arcos', 'Andalusia / Castile', 'Spanish', '1497-1559',
 'AHNOB, OSUNA,C.1635,D.130-134',
 'Five documents; D.162-164 (unsigned letters of the same years, hit "cifrada") are neighbours; D.88 is a servant (Pedro de Castilla) asking the duke for a new cipher code',
 'B', 'Description only; cipher groups not seen.',
 'One writer, 1520-21, images online; D.88 shows the duke gave ciphers to correspondents, so a key may sit in the same box.',
 3, 3, 3, ['5608534', '5612014', '5596134'], True,
 'Open 5608534 and 5596134 (the request for a "nuevo codigo cifrado").'))
R.append(row(1579, '28 Jun and 7 Nov 1579',
 'Pedro Tellez Giron, I duke of Osuna, to Philip II on the succession of Portugal, two letters hit "carta cifrada": AHNOB Osuna CP.56 D.4 and D.8',
 'Pedro Tellez Giron, I duque de Osuna -> Philip II', 'Madrid / Osuna', 'Spanish', '1560-1589',
 'AHNOB, OSUNA,CP.56,D.4; OSUNA,CP.56,D.8', 'Two single-document records (D.4 28 Jun 1579, D.8 7 Nov 1579)', 'B',
 'Description only; no image flag in the hit list, so digitisation is not confirmed.',
 'A grandee-to-king cipher letter of 1579 at the start of the Portuguese succession crisis; a deciphered copy may sit in AGS Estado.',
 3, 3, 3, ['3911374', '3911378'], False,
 'Open both PARES records; check images and whether the text is a copy in clear.'))
R.append(row(1625, '1624-1626',
 'Philip IV to the duke of Pastrana, ambassador in Rome, short run of letters hit "carta cifrada": AHNOB Osuna C.1977 D.8, 11, 17, 18, 26, 28, 29, 33',
 'Philip IV -> Rodrigo Diaz de Vivar, duque de Pastrana (extraordinary ambassador at Rome)', 'Madrid -> Rome', 'Spanish',
 '1611-1650',
 'AHNOB, OSUNA,C.1977,D.8; D.11; D.17; D.18; D.26; D.28; D.29; D.33',
 'Eight records, Jan 1624-Dec 1626; the 1642-52 Rome-embassy letters of catalogue 747 are a separate run', 'B',
 'Description only; no image flag. The 1642-52 Osuna Rome letters carry contemporary plain copies, and these may too.',
 'Same king and Roman embassy a generation before the 69-item 1642-52 series already catalogued; a different cipher, so a separate key.',
 3, 2, 3, ['3941899', '3941903', '3942032', '3941896', '3941897', '3941971', '3942034', '3942039'], False,
 'Open 3942032 (12 Feb 1625) and check for a filed decipherment before listing as open.'))
R.append(row(1651, '1651',
 'Marques de Caracena to Antonio Ronquillo, letter in part cipher on the cavalry for Milan: AHNOB Osuna CT.535 D.30',
 'Luis de Benavides Carrillo, marques de Caracena -> Antonio Briceno Ronquillo', 'Milan / Rome', 'Spanish', '1651-1700',
 'AHNOB, OSUNA,CT.535,D.30', 'Single document, 1651', 'B',
 'Description only ("Carta en parte cifrada"); no image flag.',
 'Caracena wrote cipher letters in the Genoa family already in catalogue 755; this one sits in Osuna and may be another sample of his key.',
 2, 3, 3, ['3938963'], False,
 'Open the record; compare with the Caracena items EST,LEG,3637,33 and 39.'))
R.append(row(1685, '22 Aug-19 Sep 1685',
 'Antonio de la Pena Zuniga on Flanders and the Hungarian war, three letters hit "cifrado": AHNOB Osuna CT.80 D.10-12',
 'Antonio de la Pena Zuniga -> unknown (addressee not in the hit list)', 'Brussels / Madrid', 'Spanish', '1651-1700',
 'AHNOB, OSUNA,CT.80,D.10; D.11; D.12', 'Three single-document records dated 22 Aug, 5 Sep and 19 Sep 1685', 'B',
 'Description only; images flagged online, cipher extent not seen.',
 'Three consecutive letters of one writer in 1685, images online: enough to test whether the cipher is open.',
 2, 3, 3, ['3920970', '3920971', '3920972'], True,
 'Open the three records; if cipher groups, note the addressee.'))
R.append(row(1672, '1668-1676',
 'Antonio Navarrete, marques de la Tercia, to the duke of Pastrana and Infantado, 44 documents hit "carta cifrada": AHNOB Osuna CT.260 D.151-194',
 'Antonio Navarrete, marques de la Tercia -> duque de Pastrana y del Infantado', 'Spain', 'Spanish', '1651-1700',
 'AHNOB, OSUNA,CT.260,D.151-194', 'One record for 44 documents, 31 Mar 1668-4 Sep 1676', 'B',
 'Description only; images flagged online, no count of cipher letters.',
 'A long single-writer run with images: a good key-rebuild candidate if even a few are cipher.',
 3, 3, 3, ['3937262'], True,
 'Open 3937262 and count cipher letters.'))
R.append(row(1651, '1651-1655',
 'Letters to the duke of Infantado (Rome embassy, Sicily) and his secretary, hits "cifrado" / "no descifrada": AHNOB Osuna CT.15 D.5 (Galarreta), CT.18 D.45 and D.56',
 'Martin Galarreta Ocariz; Dionisio de Antequera Arteaga; Juan Jacinto Gradinan -> duque del Infantado / Francisco Trana',
 'Rome / Sicily', 'Spanish', '1651-1700',
 'AHNOB, OSUNA,CT.15,D.5; OSUNA,CT.18,D.45(1-2); OSUNA,CT.18,D.56(1-2)',
 'Three records, 1651-55; three writers, so three possible keys; split before vetting', 'C',
 'Description only; images flagged online; "no descifrada" means no deciphering copy is filed (the opposite of the CT.2/CT.7 Philip IV letters).',
 'Letters to the Infantado embassy where no decipherment is filed, so truly open, but short and by three writers.',
 2, 3, 3, ['3939375', '3935263', '3936479'], True,
 'Open each and pick the one with the longest cipher passage.'))
R.append(row(1670, '26 Sep-24 Oct 1670',
 'Prince of Ligne (Claude Lamoral I) to the conde de Oropesa, correspondence in cipher: AHNOB Frias C.1887 D.93-98',
 'Claude Lamoral I, prince of Ligne -> Duarte Fernando Alvarez de Toledo, conde de Oropesa', 'Brussels -> Madrid', 'Spanish',
 '1651-1700', 'AHNOB, FRIAS,C.1887,D.93-98', 'Six documents, 1670; PARES 13187073', 'B',
 'Description only ("Correspondencia cifrada"); no image flag. Listed unscreened in the 9 Nov spain_nobility_aca README ("cipher letters, no images; not screened further"), never made a row.',
 'Dated, signed, named correspondents, a clear cipher label; AHNOB can be asked for images.',
 3, 3, 3, ['13187073'], False,
 'Request images from AHNOB or reopen the PARES record.'))
R.append(row(1647, '30 Sep 1647',
 'Philip IV: cedula and cipher despatch naming the conde de Haro interim governor of Milan: AHNOB Frias C.635 D.33-41',
 'Philip IV -> Inigo Melchor Fernandez de Velasco, conde de Haro', 'Madrid -> Milan', 'Spanish', '1611-1650',
 'AHNOB, FRIAS,C.635,D.33-41',
 'Nine documents; plus Frias C.1389 D.28 (Philip IV to Haro, 31 Mar 1648, "carta cifrada", PARES 3949446)', 'B',
 'Description only; no image flag.',
 'Same duke as the Frias C.1442 cedula of 1664 already in the catalogue (844), earlier in his Milan appointment; a separate cipher.',
 2, 2, 3, ['3948294', '3949446'], False,
 'Open both PARES records.'))
R.append(row(1621, '1621-1775',
 'Alonso de Cardenas to the duke of Frias, "dos cifras" sent with news of a judge\'s stabbing: AHNOB Frias C.1815 D.98-106',
 'Alonso de Cardenas -> duke of Frias', 'Spain', 'Spanish', '1611-1650', 'AHNOB, FRIAS,C.1815,D.98-106',
 'Nine documents; the range 1621-1775 is the whole record, not the letters', 'C',
 'Description only: "remitiendo dos cifras" means the writer enclosed cipher tables, so this may be a key rather than a text.',
 'Possible key sheets for a Cardenas-Frias correspondence; no ciphertext confirmed.',
 2, 2, 3, ['13363563'], False,
 'Open the record; if two cipher tables, file as a key lead.'))
R.append(row(1800, 'undated',
 'Unattributed document made mainly of cipher figures with a marginal note: AHNOB Michelena C.18 D.142-143',
 'unknown', 'unknown', 'unknown', 'unknown', 'AHNOB, MICHELENA,C.18,D.142-143',
 'Two documents; first "se compone fundamentalmente de una serie de cifras"', 'C',
 'Description only; images flagged online; undated.',
 'Pure figure document with a note, anonymous, in a family archive; only worth an image look.',
 2, 2, 4, ['4025233'], True,
 'Open the images; read the note.'))
json.dump(R, open('candidates.json', 'w', encoding='utf8'), ensure_ascii=False, indent=1)
print(len(R))
