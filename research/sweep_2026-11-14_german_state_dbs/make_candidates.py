"""Builds candidates.json and key_leads.json for the German state databases sweep of 14 Nov 2026.

Sources: Archivportal-D / DDB Solr (ddb_harvest2.py -> raw2.jsonl, triage.py, short.py), Archivportal Thueringen
(archive-in-thueringen.de, Chrome same-origin fetch), BLHA (blha-recherche.brandenburg.de /rest/search, Chrome), OOe Landesarchiv
findbuch.net, Steiermark ArchivIS. Every row is scored from the finding-aid text (seen: catalogue); none viewed.
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = {}
for line in open(os.path.join(HERE, '_tmp', 'raw2.jsonl'), encoding='utf-8'):
    r = json.loads(line)
    RAW[r['id']] = r


def ap(prefix, label):
    ids = [i for i in RAW if i.startswith(prefix)]
    assert len(ids) == 1, (prefix, ids)
    return {'href': 'https://www.archivportal-d.de/item/' + ids[0], 'label': label}


def th(path, label):
    return {'href': 'https://www.archive-in-thueringen.de/de/findbuch/view/bestand/' + path, 'label': label}


SRC_AP = 'Archivportal-D (DDB Solr), German state archives sweep, 14 Nov 2026'
SRC_TH = 'Archivportal Thueringen (archive-in-thueringen.de), German state databases sweep, 14 Nov 2026'
SCORE = ('Scored from the finding-aid text during the 14 Nov 2026 German state databases sweep '
         '(research/sweep_2026-11-14_german_state_dbs/); not viewed')
PRIOR = ('open as far as checked (14 Nov 2026): the shelfmark, fonds series and correspondent were searched in catalogue.json, '
         'leads.json, every candidates.json / key_leads.json and the targets (known.py-style grep) and found nowhere; '
         'no web, Tomokiyo, Lasry or DECODE search made in this sweep')
ACCESS_AP = ('description only on Archivportal-D; no images found on the item page of the portal; order from the archive or '
             'use the reading room (digitisation not checked on the archive\'s own site)')
ACCESS_TH = ('index text only in Archivportal Thueringen (Online-Findbuch); digitisation not checked; order through the '
             'Landesarchiv Thueringen reading room or reproduction service')
R = []
K = []


def add(**kw):
    kw.setdefault('source', SRC_AP)
    kw.setdefault('score_note', SCORE)
    kw.setdefault('prior_art', PRIOR)
    kw.setdefault('seen', 'catalogue')
    kw.setdefault('needs_archive_scan', 'yes')
    kw.setdefault('access_note', ACCESS_AP)
    kw.setdefault('language', 'German')
    kw.setdefault('region', 'Germany')
    R.append(kw)


# ------------------------------------------------------------------ Archivportal-D rows
add(year=1845, date='1845-1846', period='1801-1900', cls='A',
    title='Reports of the Wuerttemberg envoy Degenfeld-Schomburg at Munich to the foreign minister, "teilweise chiffriert, mit Dechiffrierung" (2 volumes)',
    correspondents='Ferdinand Christoph Graf von Degenfeld-Schomburg (Wuerttemberg envoy at Munich) -> Minister of foreign affairs, Stuttgart',
    place='Munich / Stuttgart',
    shelfmark='Landesarchiv Baden-Wuerttemberg, Hauptstaatsarchiv Stuttgart, E 50/05 Bue 124 (3 Jan - 22 Nov 1845) and Bue 129 (10 Jan - 19 Nov 1846)',
    folio_note='Titles: "(z. T. chiffriert, mit Aufl.)" (Bue 124) and "(teilweise chiffriert, mit Dechiffrierung)" (Bue 129). Content note: Staendekammern, Minister Abel, dismissal of foreign minister Gise, church affairs. Other Bue of E 50/05 (other years) were not in the hit list; their titles may use no cipher word',
    status='Finding aid: some reports ciphered, with the legation\'s deciphering filed in the same volume. No decipherment or edition found in this sweep. The Wuerttemberg key books of the same years are in E 59 (Chiffrierbuecher 1847-um 1870, Bd. 232-242, see key_leads.json), so the key family is traceable.',
    why='A paired cipher/plaintext set of a small German court\'s diplomatic reports of 1845-46, with the Wuerttemberg legation cipher books (E 59, 1847 onward) listed next door: a key can be rebuilt from the pairs and checked against the books.',
    importance=2, solvability=4, difficulty=2,
    verify='Order Bue 124 and 129 (or ask HStAS for scans); check whether the Dechiffrierung is interlinear or a separate sheet; compare with E 59 Bd. 238-241 (Munich cipher books VII-X).',
    links=[ap('DRBLDG3Q', 'E 50/05 Bue 124'), ap('DOIB6MTZ', 'E 50/05 Bue 129')])

add(year=1779, date='1779', period='1701-1800', cls='A',
    title='Reichshofrat opinion in the Baden v. von der Leyen lawsuit with a "chiffriertes Schreiben mit Dechiffrierung"',
    correspondents='unknown (letter inside a Baden Geheimer Rat file on the Geroldseck claims)', place='unknown',
    shelfmark='Landesarchiv Baden-Wuerttemberg, Generallandesarchiv Karlsruhe, 111 Nr. 304 (Geroldseck, 03 Ansprueche)',
    folio_note='1 Fasz.; the description says "Enthaelt u.a.: Chiffriertes Schreiben mit Dechiffrierung". Sender, recipient and length of the cipher are not given',
    status='Finding aid says a ciphered letter is filed with its deciphering. Not found in any ledger; no web search made.',
    why='A single short ciphered letter with its plaintext in a Baden legal file: probably too short to carry a key, but a clean crib for the Baden chancery cipher of 1779 if the Karlsruhe key volumes (GLA 48) cover it.',
    importance=2, solvability=3, difficulty=2,
    verify='Ask GLA Karlsruhe for the folio; check length (a few lines is a class C) and compare with GLA 48 Nr. 65-84.',
    links=[ap('F55HIYVM', 'GLA 111 Nr. 304')])

add(year=1630, date='1630', period='1611-1650', cls='A',
    title='Report on the troops of Rittmeister Maudt before Lemgo (1630), "verschluesselt und Aufloesung", in the correspondence of Bishop Franz Wilhelm of Osnabrueck with his chancellor and councillors',
    correspondents='unknown (report, sender not named in the description) -> Osnabrueck chancery', place='Osnabrueck / Lemgo',
    shelfmark='Niedersaechsisches Landesarchiv, Standort Osnabrueck, NLA OS Rep 100 Abschnitt 256 Nr. 4',
    folio_note='One item inside a mixed volume (letters of 1626-30; others named: Wiedenbrueck 1626, Lingen commander Micault 1630, contributions). "verschluesselt und Aufloesung" = ciphered report with a resolution',
    status='Finding aid names one ciphered report with its resolution. Franz Wilhelm of Osnabrueck is held in catalogue.json for other files; this volume is not. No decipherment found.',
    why='Thirty Years\' War field intelligence in a bishop\'s chancery cipher with the key resolution beside it: small, but dated and placed (Lemgo 1630).',
    importance=2, solvability=3, difficulty=2,
    verify='Order or request the volume; find the folio; check if the Aufloesung is a full transcription.',
    links=[ap('KZ76GT37', 'NLA OS Rep 100 Abschnitt 256 Nr. 4')])

add(year=1544, date='Jul-Aug 1544', period='1497-1559', cls='B',
    title='Hessian envoys Tilemann Guenterode and Johann Keudel at the imperial court: letters to Landgrave Philip, with a "Chiffrenalphabet"',
    correspondents='Dr. Tilemann Guenterode and Lic. Johann Keudel -> Landgrave Philip of Hesse; also letters of Wolfgang Rehlinger (Strasbourg) and to Duke Moritz of Saxony', place='imperial court / Speyer period',
    shelfmark='Hessisches Staatsarchiv Marburg, 3 (Politisches Archiv Landgraf Philipps des Grossmuetigen), Nr. 712 (2.19 Ereignisse 1542-1545)',
    folio_note='"Dabei: Chiffrenalphabet": the cipher alphabet is filed with the letters. Whether the letters themselves are ciphered is not said',
    status='Finding aid lists a cipher alphabet inside the envoys\' file. Philip\'s Politisches Archiv has other keyed volumes in this repo\'s ledgers (e.g. Feige); this number is not held.',
    why='A cipher alphabet filed with the actual letters of 1544 diplomats in Philip of Hesse\'s service: key and ciphertext from one volume, in the generation of the Schmalkaldic League ciphers.',
    importance=3, solvability=3, difficulty=3,
    verify='Look at the images at Archivportal-D / LAGIS if digitised (Marburg 3 is partly online); check whether the letters use the alphabet.',
    links=[ap('FOL5BKWF', 'Marburg 3, 712')])

add(year=1500, date='late 15th to early 17th century', period='1497-1559', cls='B',
    title='Munich: "Chiffrier- und Dechiffriertabellen, Korrespondenzschreiben in verschluesselter Schrift" (288 fol.), Kurbayern Aeusseres Archiv, correspondence files, Verschiedenes',
    correspondents='unknown', place='Munich',
    shelfmark='Bayerisches Hauptstaatsarchiv, Kurbayern Aeusseres Archiv 4591 (Kasten schwarz 13478), 39 Korrespondenzakten, 39.22 Verschiedenes',
    folio_note='288 fol. Dated "Ende 15.-Anfang 17. Jh." Keyword on the record: Chiffre. Both cipher tables and ciphered letters in one volume',
    status='Finding aid names both tables and ciphered letters in one miscellany. The Bavarian 30 Years\' War key collection (Kurbayern Aeusseres Archiv 2681) is already in catalogue.json; this volume is not.',
    why='A 288-folio miscellany of ciphers from the late 15th to early 17th century with tables beside ciphered letters, so keys can be matched to texts across a century; the earliest material could be among the oldest German ciphers.',
    importance=4, solvability=2, difficulty=4,
    verify='Order the volume; check the first folios for 15th-century material; the portal gives a gda.bayern.de record, no scans noted.',
    links=[ap('OZNIU4QQ', 'BayHStA KAeA 4591')])

add(year=1758, date='1758-1759', period='1701-1800', cls='A', language='German or French (not stated)',
    title='"Dechiffrierte Briefe, meist aus der Zeit des Siebenjaehrigen Krieges, unter anderm vom Feldwachtmeister de Vela an den saechsischen Kurprinzen"',
    correspondents='Feldwachtmeister de Vela -> Saxon Electoral Prince', place='Saxony / Dresden',
    shelfmark='Saechsisches Staatsarchiv, Hauptstaatsarchiv Dresden, 10026 Geheimes Kabinett, Loc. 03447/28 (039.303 Vela, de)',
    folio_note='Title says the letters are deciphered ("dechiffriert"); whether the ciphertext is kept beside the plaintext is not stated',
    status='Finding aid: deciphered letters of 1758-59 (Seven Years\' War), Saxon cabinet. No other row or ledger has this Loc. number. "Vela" matches other families in the ledgers, not this correspondence.',
    why='Seven Years\' War letters to the Saxon Electoral Prince with their contemporary deciphering: the plaintext side of a possible cipher pair of the Saxon court.',
    importance=3, solvability=3, difficulty=2,
    verify='Request scans from HStA Dresden; check if cipher sheets survive beside the plain copies.',
    source='Archivportal-D / Saechsisches Staatsarchiv sweep, 14 Nov 2026',
    links=[ap('DSKEZ6L4', 'Loc. 03447/28')])

add(year=1712, date='1712-1713', period='1701-1800', cls='A',
    title='Manteuffel\'s reports to Flemming, 1712-13: Chiffre resolutions made by Dr. Krauske in 1893 for Loc. 694/08 and 694/09',
    correspondents='Manteuffel -> Flemming (first names and offices are not in the description)', place='unknown',
    shelfmark='Saechsisches Staatsarchiv, Hauptstaatsarchiv Dresden, 10026 Geheimes Kabinett, Loc. 00694/10 (035.001 Gesandtschaften, Allgemeines); the reports are Loc. 694/08 and 694/09',
    folio_note='"Einige Chiffre-Aufloesungen zu den Berichten Manteuffels an Flemming 1712 und 1713": a 1893 modern decipherment of parts of two ciphered report volumes. A digital copy link is shown for this record on the Saxon site',
    status='Finding aid: partial modern decipherment (1893) of two report volumes, so a Saxon cipher for 1712-13 is partly keyed. The Flemming correspondence has other rows in the ledgers; Loc. 694/08-10 are not named in any of them.',
    why='Saxon diplomatic reports of 1712-13 with a scholar\'s partial decipherment, giving a crib to complete the Manteuffel-Flemming cipher (the "Graefl. Flemmingsche Chiffres" key volumes are listed in the Saxon sweeps).',
    importance=3, solvability=4, difficulty=2,
    verify='Open the digital copy link on archiv.sachsen.de for Loc. 694/10 and look for 694/08-09 scans; judge the 1893 resolutions.',
    needs_archive_scan='partly',
    access_note='the Saxon archive page for Loc. 694/10 shows a digital copy link ("digitalisat"); the report volumes 694/08-09 were not checked',
    source='Archivportal-D / Saechsisches Staatsarchiv sweep, 14 Nov 2026',
    links=[ap('HJGLVTUA', 'Loc. 00694/10')])

add(year=1850, date='1850', period='1801-1900', cls='B',
    title='Saxon Ministry of the Interior police file on Carl Heinrich Hitzschold, former Justizamtmann at Wolkenstein: "Entschluesselung chiffrierter Schreiben"',
    correspondents='Hitzschold (person under police watch) and unknown correspondents', place='Wolkenstein / Dresden',
    shelfmark='Saechsisches Staatsarchiv, Hauptstaatsarchiv Dresden, 10736 Ministerium des Innern, Nr. 00457/02 (09.02.06 Ueberwachung von Einzelpersonen)',
    folio_note='Content note: "Enthaelt u. a.: Entschluesselung chiffrierter Schreiben". A digital copy link is shown on the Saxon site',
    status='Finding aid says police-deciphered letters of a person under surveillance in 1850 (year only, no context given). Unclear whether ciphertext and decipherment are both kept.',
    why='A Saxon police decipherment of a private (not diplomatic) cipher of 1850, probably a simple substitution; useful for the private-cipher side of the corpus.',
    importance=2, solvability=4, difficulty=1,
    verify='Open the digital copy link; look for the cipher sheets and the police reading.',
    needs_archive_scan='no',
    access_note='the Saxon archive page for this record shows a digital copy link ("digitalisat"); not opened',
    source='Archivportal-D / Saechsisches Staatsarchiv sweep, 14 Nov 2026',
    links=[ap('NA6LUEJG', 'Ministerium des Innern 00457/02')])

add(year=1759, date='1759', period='1701-1800', cls='C', language='German and French',
    title='Military papers of General Christian Ludwig von Hardenberg in the Seven Years\' War on the English-Hanoverian side: microfilm record that matched "chiffr*"',
    correspondents='Christian Ludwig von Hardenberg and unknown correspondents', place='Hanover / Westphalia theatre',
    shelfmark='Brandenburgisches Landeshauptarchiv, 37 Neuhardenberg, Film 1563',
    folio_note='The record text shown by the portal is the title only ("dt. frz."); the matched cipher word is in a field not displayed by the search API. Film = microfilm',
    status='Hit on the wildcard chiffr* (also chiffer*, Chiffrierung) with no visible cipher text. Weak: could be an incidental word in a long contents note.',
    why='Hardenberg commanded Hanoverian troops in 1759; if ciphered orders or reports are among the papers they could pair with Hanoverian chancery keys.',
    importance=2, solvability=2, difficulty=3,
    verify='Open the record at blha-recherche.brandenburg.de (pk 1097847) and read the full contents field.',
    source='BLHA (blha-recherche.brandenburg.de /rest/search), German state databases sweep, 14 Nov 2026',
    access_note='microfilm in the BLHA; the online record lists no images',
    links=[{'href': 'https://blha-recherche.brandenburg.de/de/#/search?query=Neuhardenberg%20Film%201563', 'label': 'BLHA 37 Neuhardenberg Film 1563 (search)'}])

# ------------------------------------------------------------------ Archivportal Thueringen rows
KOBNOTE = ('Kob\'s secret chancery of Hildburghausen, volumes in the "Geheimes Archiv Hildburghausen / Akten" (Bestand 4-11-2010). '
           'Each correspondence has its own cipher: one key per entry.')

add(year=1751, date='1750-1753', period='1701-1800', cls='B', source=SRC_TH, access_note=ACCESS_TH,
    title='Secret correspondence of Hofrat Johann Sebastian Kob with Johann Georg Seelig at Frankfurt about the court of Duke Anton Ulrich of Sachsen-Meiningen, with the key "fuer die verwendeten Chiffres"',
    correspondents='Johann Sebastian Kob (Hildburghausen) <-> Johann Georg Seelig (Frankfurt)', place='Hildburghausen / Frankfurt am Main',
    shelfmark='Landesarchiv Thueringen, Staatsarchiv Meiningen, Geheimes Archiv Hildburghausen / Akten (4-11-2010), Nr. 1006',
    folio_note='"Enthaelt u.a.: Schluessel fuer die verwendeten Chiffres" plus the Duke\'s marriage and the births of princesses. ' + KOBNOTE,
    status='Index text of the Online-Findbuch: key and secret letters of 1750-53 in one volume. Not in any ledger.',
    why='A small German princely spy correspondence with its own key in the same volume, a rare complete (key + letters) 18th-century secret chancery set from Thuringia.',
    importance=2, solvability=4, difficulty=2,
    verify='Order Nr. 1006 at Staatsarchiv Meiningen; check if the letters are in number cipher and the key complete.',
    links=[th('23365/systematik/156459/archivgut/3924631', 'Nr. 1006 (Online-Findbuch)')])

add(year=1754, date='1753-1755', period='1701-1800', cls='B', source=SRC_TH, access_note=ACCESS_TH,
    title='Secret correspondence of Hofrat Kob with the secretary Johann Caspar Schneider (Meiningen court of Duke Anton Ulrich) at Frankfurt and Meiningen, with the key for the ciphers used',
    correspondents='Johann Sebastian Kob (Hildburghausen) <-> Johann Caspar Schneider (secretary, Frankfurt / Meiningen); "Hofrat Schrader?" queried in the finding aid', place='Frankfurt am Main / Meiningen / Hildburghausen',
    shelfmark='Landesarchiv Thueringen, Staatsarchiv Meiningen, Geheimes Archiv Hildburghausen / Akten (4-11-2010), Nr. 998',
    folio_note='"Enthaelt u.a.: Schluessel fuer die verwendeten Chiffres". ' + KOBNOTE,
    status='Index text of the Online-Findbuch: key and secret letters of 1753-55 in one volume. Not in any ledger.',
    why='Second Kob correspondence with its own key; a different cipher from Nr. 1006 (different partner), so a pair of cipher systems from one chancery within five years.',
    importance=2, solvability=4, difficulty=2,
    verify='Order Nr. 998 together with Nr. 1006; compare the two keys.',
    links=[th('23365/systematik/156459/archivgut/3924632', 'Nr. 998 (Online-Findbuch)')])

add(year=1750, date='1749-1750', period='1701-1800', cls='B', source=SRC_TH, access_note=ACCESS_TH,
    title='Partly ciphered correspondence of Hofrat Kob with the Geheimer Legationsrat von Fischer at Vienna about the excess charge on the Amt Sonnefeld, with a key to the abbreviations used (Bl. 1-5)',
    correspondents='Johann Sebastian Kob (Hildburghausen) <-> von Fischer (Geheimer Legationsrat, Vienna)', place='Hildburghausen / Vienna',
    shelfmark='Landesarchiv Thueringen, Staatsarchiv Meiningen, Geheimes Archiv Hildburghausen / Akten (4-11-2010), Nr. 368 (further Kob-Fischer volumes in the same run: three hits 3923377, 3923378, 3923380; their signatures were not all read)',
    folio_note='"Enthaelt auch: Schluessel der in der Korrespondenz mit Fischer gebrauchten Kuerzel (Bl. 1-5)": the key is described as abbreviations (Kuerzel), so the cipher may be a nomenclator',
    status='Index text only; two or three neighbouring volumes of the same correspondence are titled "Teilweise verschluesselte Korrespondenzen des Hofrats Kob". Not in any ledger.',
    why='Hildburghausen\'s Vienna agent correspondence in a partial nomenclator with a key sheet in Bl. 1-5, 1749-50 (court and Reichshofrat business).',
    importance=2, solvability=3, difficulty=2,
    verify='Order Nr. 368 and its neighbours; read the Kuerzel key and count how much of each letter is ciphered.',
    links=[th('23365/systematik/156419/archivgut/3923377', 'Nr. 368 (Online-Findbuch)'),
           th('23365/systematik/156419/archivgut/3923378', 'Kob-Fischer volume (hit 2)'),
           th('23365/systematik/156419/archivgut/3923380', 'Kob-Fischer volume (hit 3)')])

add(year=1769, date='1769-1770', period='1701-1800', cls='C', source=SRC_TH, access_note=ACCESS_TH,
    title='Partly ciphered correspondence of Duke Ernst Friedrich III Carl of Hildburghausen and Assistenzrat Christoph Wilhelm Radefeld with the courts at Wertheim, Wuerzburg, Dresden and Vienna on the duke\'s debts and the imperial debt commission',
    correspondents='Duke Ernst Friedrich III Carl / C. W. Radefeld <-> courts at Wertheim, Wuerzburg, Dresden and Vienna', place='Hildburghausen / Vienna',
    shelfmark='Landesarchiv Thueringen, Staatsarchiv Meiningen, Geheimes Archiv Hildburghausen / Akten (4-11-2010), Nr. 1307',
    folio_note='"Teilweise verschluesselte Korrespondenz" listed with the Absendung Radefelds to Vienna; no key mentioned for this volume',
    status='Index text only; no key named. Class C: ciphertext in a debts file without a stated key.',
    why='Reichshofrat debt-commission politics of a small Thuringian duchy, partly ciphered; might share a key with the Kob volumes.',
    importance=2, solvability=2, difficulty=3,
    verify='Order Nr. 1307; check the proportion ciphered; compare with the Kob keys (Nr. 998, 1006, 368).',
    links=[th('23365/systematik/156454/archivgut/3924282', 'Nr. 1307 (Online-Findbuch)')])

add(year=1541, date='1541-1542', period='1497-1559', cls='B', source=SRC_TH, access_note=ACCESS_TH,
    title='Saxon electoral councillors at the Diets of Regensburg 1541 and Speyer 1542: reports "z.T. verschluesselt, Schluessel fol. 393", in the Ernestine Reichstag acts',
    correspondents='Saxon electoral councillors -> the Elector (Torgau, per the instruction)', place='Regensburg / Speyer',
    shelfmark='Landesarchiv Thueringen, Hauptstaatsarchiv Weimar, Ernestinisches Gesamtarchiv, Reg. E (Reichstage), Nr. 136 (Regensburg 1541, 1539-1541; Bl. incl. fol. 393 key); the Speyer 1542 volume is a neighbouring number not read',
    folio_note='Quoted: "Regensburg 1541., z.T. verschluesselt, Schluessel fol. 393 ... Mai 26, verschluesselt (fol. 300-302)" and "Speyer 1542 ... Raete an Kurfuerst, z.T. verschluesselt: Febr. 23". The finding aid cites a printed edition for part of the volume: "Druck: Mentz 3 Nr. 43" (not checked)',
    status='Index text of the Online-Findbuch: ciphered letters and the key (fol. 393) in the same Reichstag volume. Some pieces are in print (Mentz), which gives plaintext for part.',
    why='A 1541-42 Saxon electoral cipher with its key on fol. 393 and printed plaintext for parts, inside the major Reichstag series; a good Schmalkaldic-era pair.',
    importance=3, solvability=4, difficulty=2,
    verify='Order Reg. E Nr. 136 at ThHStAW or check for scans; locate fol. 300-302 and fol. 393; compare with the printed Mentz edition cited in the finding aid.',
    links=[th('24595/systematik/142619/archivgut/3604089', 'Reg. E Nr. 136 (hit 1)'),
           th('24595/systematik/142619/archivgut/3604093', 'Reg. E Nr. 136 (hit 2)'),
           th('24595/systematik/142619/archivgut/3604097', 'Speyer 1542 (hit 3)')])

add(year=1550, date='1546-1552', period='1497-1559', cls='C', source=SRC_TH, access_note=ACCESS_TH,
    title='Correspondence about the houses Coburg and Heldrungen, 1546-52, incl. the "Denkzettel des Matthias von Wallenrodt, 1550 Aug. (Bl. 145-160), Sept., z.T. in Geheimschrift"',
    correspondents='Matthias von Wallenrodt and others (Ernestine Saxon court, Coburg)', place='Coburg / Heldrungen',
    shelfmark='Landesarchiv Thueringen, Staatsarchiv Meiningen, Hennebergica Altenburg (4-10-1100), Nr. 310',
    folio_note='Cipher parts given as Aug.-Sept. 1550 pieces (Bl. 145-160); no key named',
    status='Index text only; no key named.',
    why='Mid-16th-century Saxon cipher in a Thuringian family archive, with no key listed: a class C item, but dated to a few weeks.',
    importance=2, solvability=2, difficulty=4,
    verify='Order Nr. 310; check for a key or a plaintext copy of the Denkzettel.',
    links=[th('23482/systematik/27100/archivgut/569849', 'Hennebergica Altenburg Nr. 310')])

add(year=1557, date='1550-1568', period='1497-1559', cls='C', source=SRC_TH, access_note=ACCESS_TH,
    title='Dowry affairs of Anna Maria of Brunswick, wife of Duke Albrecht of Prussia: "Schreiben in Geheimschrift (Bl. 191-195)" among the Henneberg-Brunswick papers',
    correspondents='unknown (Brunswick / Prussian side, Count Poppo of Henneberg)', place='Henneberg / Brunswick / Prussia',
    shelfmark='Landesarchiv Thueringen, Staatsarchiv Meiningen, Gemeinschaftlich Hennebergisches Archiv, Sektion I (4-10-1010), Nr. 2661',
    folio_note='Bl. 191-195 in Geheimschrift; no key named',
    status='Index text only. Duke Albrecht of Prussia\'s own chancery ciphers are in the GStA PK Teutonic Order / EM key leads (OBA 27584, EM 19 a Nr. 68), so a key family may exist.',
    why='A Henneberg-Brunswick-Prussia cipher of the 1550s-60s that might use the Prussian ducal alphabet.',
    importance=2, solvability=2, difficulty=4,
    verify='Order Nr. 2661; check Bl. 191-195 against the Prussian key books in GStA PK.',
    links=[th('27769/systematik/265688/archivgut/5622708', 'Hennebergisches Archiv Nr. 2661')])

add(year=1850, date='1845-1858', period='1801-1900', cls='C', source=SRC_TH, access_note=ACCESS_TH,
    title='Correspondence of Grand Duke Carl Alexander with Carl Freiherr von Fritsch, Thuringian envoy to the Bundestag at Frankfurt: "Verschluesselte Berichte" (135 Bl.)',
    correspondents='Carl von Fritsch (Frankfurt) -> Carl Alexander / Watzdorf (Weimar)', place='Frankfurt am Main / Weimar',
    shelfmark='Landesarchiv Thueringen, Hauptstaatsarchiv Weimar, Grossherzogliches Hausarchiv A XXVI (Carl Alexander, 6-14-1260), Nr. 269',
    folio_note='135 Bl.; contents also include the 1848 draft treaty of Thuringian states and a dispatch of 19 March 1849; no key named',
    status='Index text only; whether the "verschluesselte Berichte" are a few pages or most of the volume is not stated.',
    why='Reports of a Thuringian envoy to the Bundestag at Frankfurt, partly ciphered: a mid-19th-century diplomatic cipher.',
    importance=2, solvability=2, difficulty=3,
    verify='Order Nr. 269; look for the key in Weimar Hausarchiv A XXVI correspondence.',
    links=[th('27234/systematik/279167/archivgut/6143554', 'Hausarchiv A XXVI Nr. 269')])

# ------------------------------------------------------------------ key-only groups
K.append({
    'title': 'Baden key volumes "Chiffren": markgravial and grand-ducal ciphers 1600s-1890s (GLA 48 Nr. 65-84, plus GLA 49 Nr. 1958)',
    'shelfmark': 'Landesarchiv BW, Generallandesarchiv Karlsruhe, 48 Nr. 65-84 (Chiffren 1-3 and Zugang 1893/1908), 49 Nr. 1958 (Chiffre-Buch der Gesandtschaft)',
    'note': '20 volumes: Baden-Durlach and Baden-Baden margraves (Nr. 65-77, mostly 1600s-1700s by the portal\'s date fields), Karl Friedrich with Edelsheim (Nr. 67, 75), Grand Duke Karl\'s period (Nr. 76) and ministry keys 1860-1893 (Nr. 78-84). None of these numbers is in any ledger. They key the Baden letters in GLA 46, 47, 50 (see catalogue 576, 2036) and the Hennenhofer papers (GLA 52).'})
K.append({
    'title': 'Wuerttemberg Chiffrierbuecher 1847-um 1870 (HStAS E 59 Bd. 232-242) and legation cipher files E 51, E 50/03, E 50/12',
    'shelfmark': 'HStAS E 59 Bd. 232-237 (5-figure German cipher for the Berlin legation), Bd. 238-240 (German ciphers Munich VII-IX, dated 1847), Bd. 241 (French cipher Munich X), Bd. 242 (St Petersburg XI, 1857, with "Observations sur le Chiffre"); E 51 Bue 215, 258, 483, 503; E 50/03 Bue 87 (Kaufmann\'s draft of a new cipher for Berlin, 1810-14); E 50/12 Bue 30 (French cipher used at the Munich legation)',
    'note': 'Key side for the Degenfeld-Schomburg reports from Munich 1845-46 (candidates.json row 1) and for later Wuerttemberg legation traffic. Not in any ledger.'})
K.append({
    'title': 'Nassau-Dillenburg and Nassau-Oranien keys: HHStAW 171 A 615 (1578), 171 K 569 (16th c.), 172 Nr. 354 (172 C.220, 1754-91)',
    'shelfmark': 'Hessisches Hauptstaatsarchiv Wiesbaden, 171 A 615; 171 K 569 "Chiffren des nassauischen Schriftverkehrs"; 172 Nr. 354 "Chiffrierung der diplomatischen Korrespondenz"',
    'note': '171 A 615 holds a "Schluessel fuer chiffrierte Schreiben, 1578" in a Memoriale for the government of the Nassau lands in the absence of Count John VI. Related Nassau-Siegen files are in catalogue.json; these numbers are not.'})
K.append({
    'title': 'Nuremberg 1633: "Schluessel zu einer geheimen Zahlen-Korrespondenz" (Reichsstadt Nuernberg, Schwedische Kriegsakten 80); Hohenlohe Oe 1 Bue 18778 number key',
    'shelfmark': 'Staatsarchiv Nuernberg, Reichsstadt Nuernberg, Schwedische Kriegsakten 80 (1633); Hohenlohe-Zentralarchiv Neuenstein, Oe 1 Bue 18778 (undated number key for French words, "aus der Kanzlei des fraenkischen Kreises?")',
    'note': 'Other Nuernberg Schwedische Kriegsakten volumes are in catalogue.json (Poemer / Pirna); the key volume 80 is not. Oe 1 Bue 18778: 2- to 4-figure numbers for French words and for courts and princes of South Germany.'})
K.append({
    'title': 'Saxon and Thuringian private and chancery keys not held: Roetha Nr. 2423 (um 1640-70), Gotha Geheimer Rat Nr. 3476 and 5129, Loc. 00663/01 and 02684/08',
    'shelfmark': 'Saechsisches Staatsarchiv Leipzig, 20532 Rittergut Roetha Nr. 2423 ("Schluessel fuer Chiffre-Schrift", Carl von Friesen); Staatsarchiv Gotha, Geheimer Rat (2-13-0021) Nr. 3476 (1700, "Dechiffrierschluessel" with the Spanish Succession treaty papers) and Nr. 5129 (1667-83, "Chiffreschluessel fuer Geheimschriften"); HStA Dresden 10026 Geheimes Kabinett Loc. 00663/01 (Debrose, tables with Aufloesung, 1721ff.) and Loc. 02684/08 (Bruehl, 1770)',
    'note': 'Key-only or key-first items; Loc. 00663/01 has a digital copy link on the Saxon site. The Saxon Geheimes Kabinett Chiffres volumes Loc. 03233-03234 are already in the catalogue.'})

json.dump(R, open(os.path.join(HERE, 'candidates.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump(K, open(os.path.join(HERE, 'key_leads.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), 'candidates;', len(K), 'key groups')
