"""Builds candidates.json and key_leads.json for the 15 Nov 2026 continental blocked-sources Chrome pass.
Routes: OeNB Primo (search.onb.ac.at, Chrome), Biblissima portal (Chrome), Alvin (Chrome). Rows scored from catalogue text, none viewed."""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
NOTE = 'Scored from catalogue text during the 15 Nov 2026 continental blocked-sources Chrome pass (research/sweep_2026-11-15_continental_blocked_chrome/); not viewed on an image'
SRC_ONB = 'OeNB Primo (search.onb.ac.at) in Chrome, continental blocked-sources pass, 15 Nov 2026'
SRC_BIB = 'Biblissima portal (portail.biblissima.fr) in Chrome, continental blocked-sources pass, 15 Nov 2026'
PRIOR = ('open as far as checked (15 Nov 2026): shelfmark and correspondent names searched with known.py (see README); '
         'no web, Tomokiyo, Lasry or DECODE search')
PRIMO = 'https://search.onb.ac.at/primo-explore/search?query=any,contains,{q}&tab=default_tab&search_scope=ONB_gesamtbestand&vid=ONB&facet=rtype,include,Korrespondenz&lang=de_DE&offset=0'


def onb(q, label='OeNB Primo search'):
    return {'href': PRIMO.format(q=q), 'label': label}


def rec(ac, label):
    return {'href': 'http://data.onb.ac.at/rec/' + ac, 'label': label}


rows = []


def add(**k):
    base = dict(score_note=NOTE, seen='catalogue', needs_archive_scan='yes', prior_art=PRIOR)
    base.update(k)
    rows.append(base)


# ---------------- OeNB Autographensammlung: single letters
add(year=1605, date='1605', language='German', region='Central Europe', period='1598-1610',
    title="Giorgio Basta to Seyfried von Kollonitz, letter in Geheimschrift with a German translation attached, Eperjes (Presov) 1605",
    correspondents='Giorgio Basta (imperial general, Upper Hungary) -> Seyfried (II.) von Kollonitz', place='Eperjes (Presov)',
    shelfmark='OeNB, Sammlung von Handschriften und alten Drucken, Autogr. 23/28-7',
    folio_note="1 Brief mit Unterschrift (Brief in Geheimschrift), 2 Blatt, 1 Seite; 'beigelegt ist dessen Uebersetzung auf Deutsch'; provenance Hofkriegsrat Registratur 1829-30; war news from the Bocskai rising",
    cls='A', status='Catalogue: the letter is written in a cipher and a German rendering is filed with it. No decipherment published that this pass found.',
    why='A cipher letter with its contemporary plaintext on the same shelfmark: a short key can be rebuilt from the pair. One sender-recipient key.',
    importance=3, solvability=5, difficulty=2,
    verify='Open the record, check that the translation is a full plaintext and the cipher is on a digitised image; search Basta in DECODE/Tomokiyo.',
    links=[rec('AC14096294', 'OeNB record'), onb('Geheimschrift')], source=SRC_ONB)
add(year=1570, date='6 Oct 1570', language='Italian', region='Italy', period='1560-1589',
    title="Marcantonio Bragadin, letter from Famagusta with the text in Geheimschrift, 6 Oct 1570 (the year before the siege fell)",
    correspondents='Marcantonio Bragadin (Venetian governor of Famagusta) -> unknown', place='Famagusta',
    shelfmark='OeNB, Sammlung von Handschriften und alten Drucken, Autogr. 4/6-1',
    folio_note="1 Brief mit Unterschrift (Brieftext in Geheimschrift), 1 Blatt, 2 Seiten; provenance Lombardisches Gubernium, Archiv der Republik Venedig, 1830",
    cls='B', status='Catalogue: the body text is in cipher; no plaintext or translation noted. No decipherment found in this pass.',
    why='A one-page ciphertext by a famous Venetian commander, 1570, from a Venetian archive. Solvable only by ciphertext-only methods unless a copy is found in the Venetian series (Dispacci da Cipro).',
    importance=4, solvability=2, difficulty=3,
    verify='Look at the page; try the Venetian chancery ciphers; check ASVe for a deciphered copy.',
    links=[onb('Geheimschrift', 'OeNB Primo search (Geheimschrift, correspondence facet, record 12)')], source=SRC_ONB)
add(year=1619, date='3 Feb 1619', language='German', region='Central Europe', period='1611-1650',
    title="Karl Bonaventura von Buquoy to Hans von Molart, letter 'in Geheimschrift', 3 Feb 1619",
    correspondents='Charles Bonaventure de Longueval, count of Buquoy -> Hans von Molart', place='unknown',
    shelfmark='OeNB, Sammlung von Handschriften und alten Drucken, Autogr. 18/15-1',
    folio_note='1 Brief mit Unterschrift (in Geheimschrift), 1 Blatt, 2 Seiten; provenance HHStA, given 1829. No translation noted',
    cls='B', status='Catalogue: cipher letter, no plaintext noted. Buquoy is in the repo through the Czech sweeps, not this letter.',
    why='A short ciphertext by the imperial commander just before the Bohemian war; Buquoy ciphers elsewhere may give the key.',
    importance=3, solvability=3, difficulty=3,
    verify='View; compare with the Buquoy cipher material named in sweep_2026-11_czech_chrome.',
    links=[rec('AC14029063', 'OeNB record')], source=SRC_ONB)
add(year=1635, date='12 Sep 1635', language='German', region='Central Europe', period='1611-1650',
    title="Rudolf von Colloredo to Emperor Ferdinand III, letter partly in Geheimschrift, 12 Sep 1635",
    correspondents='Rudolf von Colloredo-Waldsee -> Ferdinand III', place='unknown',
    shelfmark='OeNB, Sammlung von Handschriften und alten Drucken, Autogr. 23/80-2',
    folio_note='1 Brief mit Unterschrift (Text teilw. in Geheimschrift), 1 Blatt, 2 Seiten; provenance Hofkriegsrat Registratur 1829-30',
    cls='B', status='Catalogue: partly ciphered, no plaintext noted.',
    why='Short code passages in a military letter of the Thirty Years War, same Hofkriegsrat series as the Basta letter.',
    importance=2, solvability=2, difficulty=3,
    verify='View; see whether the cipher is a numeral code shared with the Hofkriegsrat ciphers.',
    links=[rec('AC14044264', 'OeNB record')], source=SRC_ONB)
add(year=1610, date='undated (before 1620)', language='German', region='Central Europe', period='unknown',
    title="Henri Duval de Dampierre to Siegfried von Kollonitsch, letter partly in Geheimschrift, undated",
    correspondents='Henri Duval, count of Dampierre (imperial general, d. 1620) -> Siegfried von Kollonitsch', place='unknown',
    shelfmark='OeNB, Sammlung von Handschriften und alten Drucken, Autogr. 32/69-6',
    folio_note='1 eigenhaendiger Brief (teilw. in Geheimschrift), 4 Blatt, 5 Seiten. Not the repo target dampierre1589 (a different Dampierre)',
    cls='B', status='Catalogue: partly ciphered, no plaintext noted, undated.',
    why='Five pages by hand, part in cipher; the Kollonitsch/Basta letters give a cipher family for comparison.',
    importance=2, solvability=2, difficulty=3,
    verify='View; date by content; compare with the Basta (23/28-7) key.',
    links=[rec('AC14116639', 'OeNB record')], source=SRC_ONB)
add(year=1862, date='1862 (22 telegrams)', language='German', region='Central Europe', period='1801-1900',
    title="Archduke Ferdinand Max (later Emperor Maximilian of Mexico) to Alphons Dupont, 22 telegrams with number-code passages 'von zeitgleicher Hand aufgeloest', 1862",
    correspondents='Ferdinand Max / Maximilian of Mexico -> Alphons Dupont (Teilnachlass Alphons Dupont)', place='Miramare -> Vienna',
    shelfmark='OeNB, Autogr. 1312/30-13 to 1312/30-34 (22 records; -16 read in full)',
    folio_note="Each record: Telegramm, 1 Blatt, 2 Seiten; 'Teile des Texts mit Zahlencode chiffriert, von zeitgleicher Hand aufgeloest'; e.g. 1312/30-16 of 9 Jul 1862 (budget for 1863). Found with the searches 'Zahlencode' (21 hits) and 'chiffriert'",
    cls='A', status='Catalogue: number-code passages, each with a contemporary solution written on the telegram. No study found in this pass.',
    why='Twenty-two telegrams of one correspondent pair with the plaintext inked in by a contemporary: a number code can be rebuilt from pairs and checked across the run.',
    importance=3, solvability=5, difficulty=2,
    verify='Open two records (one early, one late) and check the contemporary resolution is on the same sheet; look for the Dupont Nachlass code book.',
    links=[rec('AC13895947', 'OeNB record Autogr. 1312/30-16'), onb('Zahlencode', 'OeNB Primo search Zahlencode')], source=SRC_ONB)
for who, ac, n, extra, lang in [
    ('Johann David von Palm', 'AC13932091', '~22', "letters of 1707 from Vienna (e.g. 9 Apr 1707, fol. 97r-98v of Cod. Ser. n. 1698; 2 Mar and 5 Mar 1707 in 1697)", 'German'),
    ('Franz Colonna zu Fels', 'AC13931662', '2+', "letters from Grosswardein of 5 and 11 Dec 1705 (Cod. Ser. n. 1696, fol. 31r-32v and 54r-55v), 'Schreiben teilweise chiffriert'", 'German'),
    ('R. de Pesme de Saint-Saphorin', 'AC13932311', '2+', "French letters of 1707 (Cod. Ser. n. 1698, fol. 270r-272v); the Swiss pass of 15 Nov holds other Saint-Saphorin rows", 'French'),
    ('Emperor Joseph I', None, '2+', "two imperial letters in Cod. Ser. n. 1696", 'German'),
]:
    add(year=1706, date='1705-1707', language=lang, region='Central Europe', period='1701-1800',
        title=f"{who} to Count Leopold Schlik, partly ciphered letters, 1705-07 (Beilagen zur Oesterreichischen Staatsgeschichte, Bd. 13)",
        correspondents=f'{who} -> Leopold Schlik (imperial general in Hungary, Rakoczi war)', place='Vienna / Grosswardein',
        shelfmark='OeNB, Cod. Ser. n. 1696-1698 (documents of 1707; Beilagen Nr. 863-945 in Cod. Ser. n. 1698)',
        folio_note=f"{n} letters of this writer found by the search 'chiffriert' (49 correspondence hits, 28 to Schlik); {extra}. The volume note says 'Viele Originale, darunter mehrere chiffriert'",
        cls='B', status="Catalogue: 'Schreiben teilweise chiffriert' (record text); no key or plaintext noted; no study found. Each writer is a separate key.",
        why="A run of original letters of the Rakoczi war with ciphered passages, many by one correspondent, in volumes the OeNB catalogue (Mazal/Unterkircher 1963) treats as documents; enough text to attack one writer's code.",
        importance=3, solvability=3, difficulty=3,
        verify='View two letters of this writer; check how long the ciphered passages are and whether a deciphering is pencilled in; check Rakoczi-war ciphers in HHStA Ungarische Akten.',
        links=([rec(ac, 'OeNB record')] if ac else []) + [onb('chiffriert', 'OeNB Primo search chiffriert')], source=SRC_ONB)
add(year=1712, date='20 Apr 1712 - 23 Aug 1713', language='Italian', region='Italy', period='1701-1800',
    title="Vettor Zane at Vienna, 73 despatches to Carlo Rizzini, 1712-13, partly ciphered ('teilw. chiffriert')",
    correspondents='Vettor Zane (Venetian, at Vienna) -> Carlo Rizzini', place='Vienna',
    shelfmark='OeNB, Cod. Ser. n. 25702 (I+295 leaves)', folio_note='Volume of 73 despatches, paper, parchment binding; catalogue note H 67/82',
    cls='C', status="Catalogue title says 'teilw. chiffriert'; no key or plaintext noted; no study found.",
    why='A bound run of 73 Venetian despatches with cipher passages from the imperial court during the Utrecht negotiations; a clear copy may be in the Venetian archive.',
    importance=2, solvability=2, difficulty=3,
    verify='Page through; check the Venetian state archive for the same despatches (Senato Dispacci Germania).',
    links=[rec('AC13847637', 'OeNB record')], source=SRC_ONB)
add(year=1905, date='1898-1912 (5 groups, about 43 letters)', language='German', region='Central Europe', period='1901-1950',
    title="Adelgunde, Duchess of Bardi, to her sister Archduchess Maria Teresa, letters 1898-1912: description ends 'teilweis...' (cipher not confirmed)",
    correspondents='Adelgunde of Bavaria, Duchess of Bardi -> Maria Teresa of Austria', place='various',
    shelfmark='OeNB, Autogr. 1942/21 to 1942/25',
    folio_note="Five record groups of 8-9 letters or postcards each, found by the search 'Geheimschrift'; the description reads 'Briefe von ihrer Schwester Adelgunde, teilweis[...]' and the word after it was cut off in my read",
    cls='C', status='Weak: the search term matched, but the matching text was not read, so a cipher is unconfirmed.',
    why='If the family used a private cipher these are about 43 letters of one pair. Worth one record read.',
    importance=1, solvability=1, difficulty=3,
    verify='Open Autogr. 1942/25(1-8) and read the whole Beschreibung line.',
    links=[onb('Geheimschrift', 'OeNB Primo search Geheimschrift (records 4-6, 9-10)')], source=SRC_ONB)

# ---------------- Biblissima: BnF volumes with cipher letters and deciphering filed
BNF_NOTE = 'Biblissima shows the BnF Archives et manuscrits item list under "Titres attestes"'


def bib(year, date, lang, region, period, title, corr, place, sm, folio, status, why, imp, sol, diff, verify, mdata):
    add(year=year, date=date, language=lang, region=region, period=period, title=title, correspondents=corr, place=place,
        shelfmark=sm, folio_note=folio, cls='A', status=status, why=why, importance=imp, solvability=sol, difficulty=diff,
        verify=verify, links=[{'href': 'https://portail.biblissima.fr/fr/ark:/43093/' + mdata, 'label': 'Biblissima record'}],
        source=SRC_BIB, score_note=NOTE + '. ' + BNF_NOTE)


bib(1625, 'April 1625', 'French', 'France', '1611-1650',
    "Louis XIII and Raymond Phelypeaux d'Herbault to Philippe de Bethune (Rome), letters 'avec chiffre et dechiffrement', Apr 1625",
    "Louis XIII, R. Phelypeaux d'Herbault -> Philippe de Bethune", 'Paris -> Rome', 'BnF, Francais 3702',
    "31 catalogue lines with chiffr-; items 9-12 are the Apr 1625 letters, each 'avec chiffre et dechiffrement'",
    "Catalogue: each ciphered letter is filed with its deciphering. 'Francais 3702' is not a shelfmark in the repo ledgers (name-level overlap with Bethune and Phelypeaux entries is possible: check siblings).",
    'Cipher and plaintext on the same sheet over a run of one court-to-embassy channel: a key from pairs.', 4, 5, 2,
    'Check catalogue.json Bethune entries first (one key per entry: split by correspondent and year); open Francais 3702 on Gallica.',
    'mdataeac5338cc2f892332886cf79a0cfc1f510f1c7f9')
bib(1629, 'Jan-Mar 1629', 'French', 'France', '1611-1650',
    "Louis XIII and Phelypeaux d'Herbault to Bethune, letters 'avec chiffre et dechiffrement', Montluel and Suse, Jan-Mar 1629",
    "Louis XIII, R. Phelypeaux d'Herbault -> Philippe de Bethune", 'Montluel / camp of Suse -> Rome', 'BnF, Francais 3673',
    "28 catalogue lines with chiffr-; items 8-17 are the 1629 letters",
    "Catalogue: ciphered letters filed with their deciphering. Not a shelfmark in the repo ledgers (check siblings).",
    'Second Bethune volume, four years after Francais 3702, so the cipher change can be dated.', 4, 5, 2,
    'Check Bethune entries in catalogue.json; open the volume.', 'mdatac326b967e17b94058379ee339ba175f0d712a06b')
bib(1634, 'Mar-Jun 1634', 'French', 'France', '1611-1650',
    "French court memoires and letters to Feuquieres (ambassador in Germany) 'avec chiffre et dechiffrement', 1634",
    'French court -> Manasses de Pas de Feuquieres', 'Fontainebleau / Chantilly -> Germany', 'BnF, Francais 3703',
    "18 catalogue lines with chiffr-; items 9-12 are the Mar-Jun 1634 memoires",
    "Catalogue: ciphered with deciphering. 'Francais 3703' is not a shelfmark in the repo ledgers; Feuquieres is (17 hits by name: check which volumes and keys are already used).",
    'Same cipher/plaintext pairs, a further Feuquieres channel in 1634.', 3, 5, 2,
    'Check catalogue.json Feuquieres entries and targets/feuquieres; open the volume.', 'mdatae9067b505fc29feb1f7e06cbf547d49b37fc0e0c')
bib(1591, 'Sep-Nov 1591', 'French', 'France', '1589-1598',
    "Marshal Biron and the sieurs de Vivonne, Quitry and Salagnac to Henri IV, letters 'avec chiffre et dechiffrement', Normandy campaign, Sep-Nov 1591",
    "Armand de Gontaut, Marshal Biron; Vivonne, Quitry, Salagnac -> Henri IV", 'Normandy campaign', 'BnF, Francais 3645',
    "5 catalogue lines with chiffr-: items 9 (28 Sep), 20 (7 Oct) and 52 (11 Nov) among them",
    "Catalogue: ciphered with deciphering for Biron; item 52 'avec chiffre' only. Not a shelfmark in the repo ledgers.",
    'A few Biron cipher letters of the 1591 campaign with the deciphering beside them.', 3, 4, 2,
    'Search Biron in catalogue.json/DECODE; open the volume.', 'mdatae07c04ef36481313528e81b777e9443010e9e979')
bib(1592, '1592', 'Spanish', 'Spain', '1589-1598',
    "Duke of Sesso (Spanish ambassador at Rome) to the Duke of Parma, 9 Nov 1592, with deciphering; a further Italian dispatch deciphered; section 'Chiffres diplomatiques'",
    'Duque de Sesso -> Alessandro Farnese, duke of Parma', 'Rome -> Flanders', 'BnF, Francais 3362',
    "13 catalogue lines with chiffr-; item 10 'Lettre, avec chiffre et dechiffrement'; item 16 'Dechiffrement d'une depeche. En italien'",
    "Catalogue: ciphered with deciphering. Not a shelfmark in the repo ledgers.",
    'Spanish diplomatic cipher with plaintext, 1592, plus a "Chiffres diplomatiques" section that may hold keys.', 3, 4, 2,
    'Open the volume; see whether the Chiffres diplomatiques section holds Spanish keys (key lead).', 'mdatacdef8c2d28ed7b81828dd2ce42d2014c1d8dc8cc')
add(year=1713, date='1713 (pp. 91, 101, 115)', language='French', region='France', period='1701-1800',
    title="BnF Clairambault 528: letters on the Cardinal de Bouillon affair, the peace, England, the Low Countries and Spain, three marked '(lettre chiffree)'",
    correspondents='unknown', place='unknown', shelfmark='BnF, Clairambault 528, pp. 91, 101 and 115',
    folio_note='Biblissima: two catalogue lines with chiffr-; the text says only that the letters are ciphered, with no mention of a deciphering',
    cls='C', status='Weak: three ciphered letters in a miscellany, no deciphering noted. Not a shelfmark in the repo ledgers.',
    why='Three ciphered letters of the Utrecht period; correspondents unknown from this text.', importance=2, solvability=2, difficulty=3,
    verify='Open pages 91, 101, 115 on Gallica.',
    links=[{'href': 'https://portail.biblissima.fr/fr/ark:/43093/mdata705fd9ab9ddf24a686f7a247c5372e5271fae3c7', 'label': 'Biblissima record'}],
    source=SRC_BIB, score_note=NOTE + '. ' + BNF_NOTE)

json.dump(rows, open(os.path.join(HERE, 'candidates.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

keys = [
    {'title': "Uppsala UB H 355 a: 'Chiffer foer korrespondens mellan persiska gendarmeriets officerare', 1911-1915 (Hjalmarson)",
     'shelfmark': 'Uppsala universitetsbibliotek, H 355 a (Alvin)',
     'note': "A key (cipher table) for the Swedish officers of the Persian gendarmerie, 1911-15, with the same collector's 'Handlingar roerande persiska gendarmeriet 1911-1915'. Alvin search 'chiffer' (18 hits, same as the October sweep). Not in the repo ledgers (Hjalmarson: no hit)."},
    {'title': "Uppsala UB D 1601 a: 'Forborgad skrifkonst. Konst- och Underbook' (Alvin)", 'shelfmark': 'Uppsala universitetsbibliotek, D 1601 a',
     'note': "Alvin search 'hemlig skrift' (1 hit). A treatise on hidden writing, not a ciphertext; a method source only."},
    {'title': "BnF Francais 3362, section 'Chiffres diplomatiques' (Biblissima)", 'shelfmark': 'BnF, Francais 3362',
     'note': 'Biblissima lists a section headed Chiffres diplomatiques in the same volume as the Sesso 1592 letters; may hold keys of the period.'},
]
json.dump(keys, open(os.path.join(HERE, 'key_leads.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(rows), 'rows', len(keys), 'key leads')
