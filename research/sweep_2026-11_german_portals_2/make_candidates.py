"""Build candidates.json for the second German-portals sweep (3 Nov 2026) from the harvests in this folder.

Only records whose shelfmark is not yet in catalogue.json, research/leads.json or SOLVED_CATALOGUE.md (newcheck.py). Rows are leads
scored from the archive's description unless a vetting block says the scan was viewed."""
import json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
TODAY = '3 Nov 2026'
ISO = '2026-11-03'
BY = 'Claude session, German portals sweep 2'
GDA = json.load(open(os.path.join(HERE, 'gda_selected.json'), encoding='utf-8'))
ARC = json.load(open(os.path.join(HERE, 'arcinsys_detail.json'), encoding='utf-8'))
PRIOR = ('open as far as checked (%s: known.py on shelfmark and names, repo catalogue, leads and the DECODE list; '
         'Tomokiyo, Lasry, the edition and the literature not yet searched)' % TODAY)
AP = {'he': 'https://arcinsys.hessen.de/arcinsys/showArchivalDescriptionDetails.action?archivalDescriptionId=%s',
      'ni': 'https://www.arcinsys.niedersachsen.de/arcinsys/showArchivalDescriptionDetails.action?archivalDescriptionId=%s'}
LABW = 'https://www2.landesarchiv-bw.de/ofs21/olf/druckansicht.php?id_titlaufn=%s'
rows = []


def period(y):
    for hi, name in [(1496, '15th century'), (1559, '1497-1559'), (1589, '1560-1589'), (1598, '1589-1598'), (1610, '1598-1610'),
                     (1650, '1611-1650'), (1700, '1651-1700'), (1800, '1701-1800'), (1900, '1801-1900'), (1950, '1901-1950')]:
        if y <= hi:
            return name
    return 'unknown'


def gda(prefix):
    for v in GDA.values():
        if v['head'].startswith(prefix):
            return v['url']
    raise KeyError(prefix)


def arc(*sigs):
    out = []
    for s in sigs:
        hit = [(k, v) for k, v in ARC.items() if v['sig'].endswith(s)]
        if not hit:
            raise KeyError(s)
        k, v = hit[0]
        out.append({'label': 'Arcinsys ' + v['sig'], 'href': AP[k[:2]] % k.split(':v')[1]})
    return out


def add(portal, links, year, date, title, corr, place, lang, region, shelf, note, status, why, imp, sol, dif, verify,
        cls='C', scan='yes', access='', seen='catalogue', vetting=None):
    row = {'year': year, 'date': date, 'title': title, 'correspondents': corr, 'place': place, 'language': lang, 'region': region,
           'period': period(year), 'shelfmark': shelf, 'folio_note': note, 'cls': cls, 'status': status, 'why': why,
           'importance': imp, 'solvability': sol, 'difficulty': dif,
           'score_note': 'Scored from the finding-aid description during the Nov 2026 German portals sweep 2 '
                         '(research/sweep_2026-11_german_portals_2/); ' + ('scan viewed' if seen == 'image' else 'not viewed'),
           'verify': verify, 'links': links, 'seen': seen, 'source': portal + ' sweep', 'prior_art': PRIOR,
           'needs_archive_scan': scan,
           'access_note': access or ('finding aid online; the archive shows no scan of this unit, so a scan order or a reading-room visit is needed')}
    if vetting:
        row['vetting'] = vetting
        row['prior_art'] = 'open (checked %s: see vetting block)' % TODAY
    rows.append(row)


def V(kind, where, extent, cipher, decode, tomokiyo, lasry, edition, literature, key_check, dups):
    return {'date': ISO, 'by': BY, 'seen': {'kind': kind, 'where': where, 'extent': extent, 'cipher': cipher},
            'prior_art': {'decode': decode, 'tomokiyo': tomokiyo, 'lasry': lasry, 'edition': edition, 'literature': literature},
            'key_check': key_check, 'duplicates': dups, 'verdict': 'open'}


NOD = 'not on DECODE: known.py on the shelfmark and the names has no hit in the list of 10,106 records (3 Nov 2026)'
NOT = 'nothing on cryptiana for these correspondents (web search 3 Nov 2026; known.py finds no Tomokiyo reference in the repo)'
NOL = 'no paper or GL.htm key for these correspondents found (web search and known.py, 3 Nov 2026)'
BG = 'gda.bayern.de'
A = 'Arcinsys'

# ---- gda.bayern.de: Staatliche Archive Bayerns. Every unit is "A = Analoges Archivale": no scans online.
add(BG, [{'label': 'Kurbayern GehR Archivalien 889', 'href': gda('889 - ')}], 1536, '23 Jan 1536',
    'Francis I of France to Dukes Wilhelm IV and Ludwig X of Bavaria, a parchment letter partly in cipher',
    'Francis I → Wilhelm IV and Ludwig X of Bavaria', 'France', 'unknown', 'France', 'BayHStA, Kurbayern GehR Archivalien 889', '114 Bl.; one letter dated 23 January',
    'Finding aid: "Teilweise chiffriertes Schreiben des Königs Franz I. von Frankreich auf Pergament vom 23. Januar". No decipherment mentioned.',
    'French royal cipher sent to the Bavarian dukes in the run-up to the 1536 war.', 4, 2, 3, 'Order a scan of the letter; try the French royal ciphers of 1536 held here (rome1536).', cls='B')
add(BG, [{'label': 'Hochstift Bamberg 892', 'href': gda('892 - ')}, {'label': 'Hochstift Bamberg 893', 'href': gda('893 - ')}], 1553, 'May-June 1553',
    'Second Margrave War: reports and correspondence of the Franconian League against Albrecht Alcibiades, letters partly in secret script',
    'Franconian League (Bamberg) and correspondents', 'Bamberg', 'German', 'Germany', 'Staatsarchiv Bamberg, Hochstift Bamberg, Archiv, Akten 892 and 893', 'two collective files, May and June 1553',
    'Finding aid: "Schreiben teilweise in Geheimschrift".', 'War letters of the campaign that ended at Sievershausen.', 3, 2, 3, 'Order scans; compare with Zasius 1553 (catalogue 565) and NLA WO 1 Alt 8 Nr. 407.')
add(BG, [{'label': 'Pfalz-Neuburg Akten 793/II', 'href': gda('793/II')}], 1612, '1612', 'Pistorius in Prague: reports and ciphered correspondence to Pfalz-Neuburg',
    'Pistorius → Pfalz-Neuburg chancery', 'Prague', 'German', 'Central Europe', 'BayHStA, Pfalz-Neuburg Akten 793/II', 'file of reports',
    'Finding aid: "Berichte, weitergeleitete Nachrichten und chiffrierte Korrespondenz des Korrespondenten Pistorius aus Prag".',
    "Court news from Prague in the last year of Rudolf II's reign.", 3, 2, 3, 'Order a scan; look for the key in Pfalz-Neuburg Akten.')
add(BG, [{'label': 'Pfalz-Neuburg Akten 6286', 'href': gda('6286 - ')}, {'label': 'Pfalz-Neuburg Akten 1346', 'href': gda('1346 - ')}], 1614, '1614',
    'Wolfgang Wilhelm of Pfalz-Neuburg: two letters to Maximilian of Bavaria with many passages in cipher, and his personal notes on his conversion, partly ciphered',
    'Wolfgang Wilhelm of Pfalz-Neuburg → Maximilian I of Bavaria; his own notes', 'Neuburg', 'German', 'Germany', 'BayHStA, Pfalz-Neuburg Akten, Neuburger Abgabe 1989, 6286; Pfalz-Neuburg Akten 1346', 'two copies of letters; personal notes',
    'Finding aid: "zahlreiche Passagen in Geheimschrift"; "Persönliche Notizen Wolfgang Wilhelms, teilweise chiffriert".',
    "The Count Palatine's secret conversion to Catholicism in 1613-14, in his own cipher.", 4, 2, 3, 'Order scans of both; the notes should give word lengths for the same system.')
add(BG, [{'label': 'Pfalz-Neuburg Akten 1450/1', 'href': gda('1450/1')}], 1623, '1623-30 (report undated)', 'Fabriani: a ciphered Italian report among Pfalz-Neuburg government papers',
    'Fabriani → Pfalz-Neuburg', 'unknown', 'Italian', 'Germany', 'BayHStA, Pfalz-Neuburg Akten 1450/1', 'one report', 'Finding aid: "chiffrierter italienischer Bericht Fabrianis (undatiert)".',
    'An Italian agent writing to Neuburg in the Thirty Years War.', 2, 2, 3, 'Order a scan.')
add(BG, [{'label': 'Kasten blau 61/3', 'href': gda('61/3 - ')}], 1639, '1639-51', 'Correspondence with Johann Wippermann, Pfalz-Neuburg privy councillor and marshal, with ciphers noted as not resolved',
    'Johann Wippermann ↔ Pfalz-Neuburg court', 'Düsseldorf; Vlotho', 'German', 'Germany', 'BayHStA, Kasten blau 61/3', 'file 1639-51',
    'Finding aid: "Enthält u.a.: nicht aufgelöste Chiffren". The archive itself says these ciphers are unresolved.',
    'Pfalz-Neuburg diplomacy in Jülich-Berg at the end of the Thirty Years War.', 3, 2, 3, 'Order a scan; length and system unknown.',
    vetting=V('not online', 'https://www.gda.bayern.de/gvl/archive.xhtml (record BayHStA, Kasten blau 61/3, read 3 Nov 2026); unit is "A = Analoges Archivale", no image',
              'not known: a correspondence file 1639-51 holding an unstated number of ciphered passages',
              'Finding aid quoted: "Enthält u.a.: nicht aufgelöste Chiffren". The archive states they are not resolved; no decipherment is noted.',
              NOD, NOT, NOL, 'no edition of the Wippermann correspondence found; the Kaiserin Eleonora edition (oeaw) uses Kasten blau 44-45 for the 1680s only',
              'Gángó 2019 on the Polish crown bid does not treat ciphers; no literature on these letters found',
              'No key held here. The file has not been seen, so the Kasten blau 61 siblings with "Chiffren" (61/25, 61/30) cannot yet be tried on it.',
              'known.py on "Wippermann" and "Kasten blau 61": no hit; newcheck.py on the shelfmark: new.'))
add(BG, [{'label': 'Kasten blau 61/25', 'href': gda('61/25')}], 1664, '1664-73', 'Correspondence with Wilhelm von Schröder, secret secretary at the imperial court, with ciphers',
    'Wilhelm von Schröder ↔ Philipp Wilhelm of Pfalz-Neuburg', 'Vienna', 'German', 'Central Europe', 'BayHStA, Kasten blau 61/25', 'file 1664-73', 'Finding aid: "Enthält u.a.: Chiffren". May be keys rather than ciphertext.',
    'Pfalz-Neuburg intelligence from the Vienna court.', 3, 2, 3, 'Order a scan; find out whether "Chiffren" means letters or keys.', cls='A')
add(BG, [{'label': 'Kasten blau 61/30', 'href': gda('61/30')}], 1671, '1671-74', 'Correspondence with Oberkanzler Franz von Gise, with several ciphers and letters of Louis de Verjus',
    'Franz von Gise ↔ Philipp Wilhelm of Pfalz-Neuburg', 'unknown', 'German; French', 'Germany', 'BayHStA, Kasten blau 61/30', 'file 1671-74', 'Finding aid: "Enthält auch: verschiedene Chiffren, Briefe von dem französischen Diplomaten Louis de Verjus".',
    'Neuburg and French diplomacy before the Dutch War; may hold keys for Gise letters.', 3, 2, 3, 'Order a scan; try against Grassegger-Sammlung 15280.', cls='A')
add(BG, [{'label': 'Kasten blau 61/32 a', 'href': gda('61/32 a')}, {'label': 'Kasten blau 61/32 b', 'href': gda('61/32 b')}], 1670, '1670-76', 'Correspondence with Electoral Cologne and Franz Egon von Fürstenberg, bishop of Strasbourg, with ciphers (also Galen, Pomponne)',
    'Franz Egon von Fürstenberg, Christoph Bernhard von Galen ↔ Philipp Wilhelm of Pfalz-Neuburg', 'Cologne; Strasbourg', 'German; French', 'Germany', 'BayHStA, Kasten blau 61/32 a and 61/32 b', 'two files', 'Finding aid: "Chiffren" in both, with letters of Galen and Pomponne.',
    "The Fürstenberg brothers were France's agents in the Empire before the Dutch War.", 4, 2, 3, 'Order scans; the Fürstenberg letters are the point.', cls='A')
add(BG, [{'label': 'Kasten blau 61/42', 'href': gda('61/42')}], 1677, '1677', 'Monthly correspondence with Andreas Schellerer, Pfalz-Neuburg resident in Vienna, with ciphers',
    'Andreas Schellerer → Philipp Wilhelm of Pfalz-Neuburg', 'Vienna', 'German', 'Central Europe', 'BayHStA, Kasten blau 61/42', 'file 1677', 'Finding aid: "Enthält auch: Chiffren".', 'Vienna reports during the Dutch War.', 3, 2, 3, 'Order a scan.', cls='A')
add(BG, [{'label': 'Kasten blau 59/3', 'href': gda('59/3')}, {'label': 'Kasten blau 59/5', 'href': gda('59/5')}], 1677, '1677-89', 'Correspondence with General von Louvignies of Osnabrück and with the brothers Nesselrode, with ciphers',
    'General von Louvignies; Philipp Wilhelm and Wilhelm Franz Joseph Bertram von Nesselrode ↔ Pfalz court', 'unknown', 'German; French', 'Germany', 'BayHStA, Kasten blau 59/3 and 59/5', 'two files', 'Finding aid: "Enthält u.a.: Chiffren" in both.', 'Military and Rhenish politics 1677-89.', 2, 2, 3, 'Order scans.', cls='A')
add(BG, [{'label': 'Kasten blau 62/1 a', 'href': gda('62/1 a')}], 1673, '1673-88', 'Correspondence with the agent Heiss in Paris, with ciphers', 'Heiss → Philipp Wilhelm of Pfalz-Neuburg', 'Paris', 'German; French', 'France',
    'BayHStA, Kasten blau 62/1 a', 'file 1673-88', 'Finding aid: "Enthält u.a.: Chiffren, La Gazette (4. Mai 1686)".', "A Neuburg agent's reports from Louis XIV's Paris.", 3, 2, 3, 'Order a scan.', cls='A')
add(BG, [{'label': 'Grassegger-Sammlung 15280', 'href': gda('15280')}], 1667, '1667', 'Partly ciphered letter to Oberstkanzler Franz von Gise, in Poland to negotiate for the Polish crown',
    'unknown (Pfalz-Neuburg court?) → Franz von Gise', 'unknown → Poland', 'German', 'Poland-Lithuania', 'BayHStA, Grassegger-Sammlung 15280', 'one letter',
    'Finding aid: "Teilweise Chiffriertes Schreiben an den vermutlich zu Verhandlungen wegen Erlangung der polnischen Königskrone in Polen weilenden Oberstkanzler Franz von Gise". No decipherment noted.',
    "A cipher passage from Philipp Wilhelm's bid for the Polish crown, the campaign Leibniz wrote for in 1669.", 4, 2, 3, 'Order a scan; try keys in Kasten blau 61/30 (Gise).', cls='B',
    vetting=V('not online', 'https://www.gda.bayern.de/gvl/archive.xhtml (record BayHStA, Grassegger-Sammlung 15280, read 3 Nov 2026); unit is "A = Analoges Archivale", no image',
              'one letter of 1667, partly in cipher; length not stated',
              'Finding aid quoted: "Teilweise Chiffriertes Schreiben an den ... Oberstkanzler Franz von Gise". No decipherment is mentioned.',
              NOD, NOT, NOL, 'no edition printing this letter found; Gángó 2019 (Philipp Wilhelm and the Specimen Polonorum) gives no text of it',
              'Gángó 2019 and the DDB file AA 0031 3713 on the bid; nothing on the cipher',
              'No key held here. BayHStA, Kasten blau 61/30 (Gise, "verschiedene Chiffren") may hold one but is also not online.',
              'known.py on "15280", "Gise", "Philipp Wilhelm": only catalogue entries on Virmond, a different correspondent; newcheck.py: new.'))
add(BG, [{'label': 'Fechenbach 2189', 'href': gda('2189 - ')}], 1746, '18 June 1746', 'Ciphered letter from Rome on politics, in a Fechenbach family miscellany', 'unknown → Fechenbach', 'Rome', 'unknown', 'Papacy',
    'Staatsarchiv Würzburg (Kitzingen), Adelsarchiv Fechenbach zu Laudenbach, 2189, Bl. 417-418', '2 leaves', 'Finding aid: "chiffriertes Schreiben, Rom, 18. Juni 1746 (betrifft Politisches) (Bl. 417-418)".',
    'A short Roman political cipher, possibly tied to catalogue 586 (Seiz in Rome, same years).', 2, 2, 3, 'Order Bl. 417-418; compare with Geistliche Sachen 1455.')
add(BG, [{'label': 'Geheimes Archiv Ansbach 99', 'href': gda('99 - ')}], 1748, '1748-52', "Acta secretissima on Margrave Carl Wilhelm Friedrich of Ansbach's will and the heir's education, partly encrypted letters from the Hanover ministry",
    'Hanover ministry and others → Ansbach', 'Hanover; Ansbach', 'German', 'Germany', 'Staatsarchiv Nürnberg, Fürstentum Ansbach, Geheimes Archiv, Fürstliche Testamente 99', 'file', 'Finding aid: "(teilweise verschlüsselt)".', "A dynastic secret between Ansbach and George II's ministers.", 3, 2, 3, 'Order a scan.')
add(BG, [{'label': 'Geheimer Rat 16091', 'href': gda('16091')}], 1778, '1778', 'Ansbach-Bayreuth reports on the Bavarian succession, with a ciphered letter and cipher tables (Prod. 75)',
    'Ansbach Geheimer Rat ↔ Prussian ministry', 'Ansbach', 'German', 'Germany', 'Staatsarchiv Nürnberg, Fürstentum Ansbach, Geheimer Rat 16091, Prod. 75', 'one letter and tables', 'Finding aid: "Darin: Chiffrierter Brief und Chiffretabellen (Prod. 75)". The tables probably read the letter.',
    'War of the Bavarian Succession seen from Ansbach.', 3, 2, 2, 'Order Prod. 75; likely a key alignment.', cls='A')
add(BG, [{'label': 'Reichswesen 125', 'href': gda('125 - ')}], 1802, '1802-03', 'Knightly canton Rhön-Werra at the Reichsdeputation: reports of envoy von Gemmingen, with encrypted texts', 'Freiherr von Gemmingen → Ritterkanton Rhön-Werra', 'Regensburg', 'German', 'Germany',
    'Staatsarchiv Würzburg (Kitzingen), Mischbestände, Reichswesen 125', 'file', 'Finding aid: "Enthält auch: Verschlüsselte Texte".', 'The Imperial Knights fighting for survival in 1803.', 2, 2, 3, 'Order a scan.')
add(BG, [{'label': 'Ortenburg 4509', 'href': gda('4509')}], 1804, '1804-05', "Karl von Wöllwarth's mission for the Imperial Knights to the Vienna court: ciphered letters with code key", 'Karl von Wöllwarth ↔ Reichsritterschaft', 'Vienna', 'German', 'Central Europe',
    'Staatsarchiv Würzburg (Kitzingen), Gräflich Ortenburg\'sches Schlossarchiv, Bi-Ort 4509', 'file', 'Finding aid: "unter anderem auch chiffrierte Briefe (mit Codeschlüssel)".', 'Key filed with the letters, so readable from a scan.', 2, 2, 1, 'Order a scan.', cls='A')
add(BG, [{'label': 'MA Politisches Archiv 9', 'href': gda("9 - 'Mission")}], 1805, '1 Sept - 31 Dec 1805', "Gravenreuth's extraordinary mission to Napoleon's headquarters in the 1805 campaign, ciphers resolved and not resolved",
    'Karl Ernst von Gravenreuth ↔ Max IV Joseph and Montgelas', 'French imperial headquarters', 'French', 'Germany', 'BayHStA, MA Politisches Archiv (Rep. Bd. 1, 5) 9', 'file with an added bundle of letters to Mieg in Vienna',
    'Finding aid: "überwiegend in französischer Sprache, teilweise Chiffren (aufgelöst und nicht aufgelöst)".',
    "Bavaria's envoy at Napoleon's side during Ulm and Austerlitz, the talks that made Bavaria a kingdom.", 5, 2, 3, 'Order a scan; the resolved passages give a crib for the unresolved ones.', cls='A',
    vetting=V('not online', 'https://www.gda.bayern.de/gvl/archive.xhtml (record BayHStA, MA Politisches Archiv 9, read 3 Nov 2026); unit is "A = Analoges Archivale", no image',
              'not known: a file of Sept-Dec 1805 in which some cipher passages are resolved and some not',
              'Finding aid quoted: "teilweise Chiffren (aufgelöst und nicht aufgelöst)". The archive says part of the cipher has no decipherment.',
              NOD, NOT, NOL, 'no edition of the Gravenreuth reports found (search 3 Nov 2026)',
              'A Ferdinandeum article (zobodat.at VeroeffFerd 78) cites Gravenreuth on the Tyrol and a book chapter is titled "Gravenreuth gegen Montgelas"; neither was read in full, and the searches returned nothing on the cipher',
              'No key held here. The Bavarian archives list a file "Die Chiffern und Chiffriersysteme" 1799-1917 (signature 633), not online, not tried.',
              'known.py on "Gravenreuth": no hit; newcheck.py: new. Catalogue 584 (NL Montgelas 74) is a different file.'))
add(BG, [{'label': 'MA Politisches Archiv 13', 'href': gda("13 - 'Affaire")}], 1806, '1806-08', 'The Posch affair: proceedings against Baron von Posch for breach of duty, mostly French, partly in cipher', 'Baron von Posch; Bavarian foreign ministry', 'Ulm; Munich', 'French', 'Germany',
    'BayHStA, MA Politisches Archiv (Rep. Bd. 1, 5) 13', 'file', 'Finding aid: "Überwiegend in französischer Sprache, teilweise Chiffren".', "An envoy's disgrace under Montgelas.", 2, 2, 3, 'Order a scan.')
add(BG, [{'label': 'MA 41 Postwesen 16', 'href': gda('16 - Guerre')}], 1811, '1811-13', 'Guerre contre la Russie: Bavarian file on the 1812 campaign with cipher tables and ciphers noted as not resolved', 'Bavarian foreign ministry and field post', 'Russia; Munich', 'French; German', 'Germany',
    'BayHStA, MA Politisches Archiv 5 (I. Reihe) 16, bound', 'bound volume', 'Finding aid: "Chiffriertabellen (a) alphabetisch, b) numerisch) (teilweise in französischer Sprache, teilweise Chiffren (nicht aufgelöst))". The tables in the same volume probably read them.',
    "Bavaria's corps in Napoleon's Russian campaign.", 4, 2, 2, 'Order a scan; try the tables on the ciphers first.', cls='A')
add(BG, [{'label': 'Gesandtschaft Bern 59', 'href': gda('59 - Gesandtschaftsberichte')}], 1822, '19 June - 22 Dec 1822', 'Legation reports from Switzerland with a partly ciphered letter of King Max Joseph', 'Max I Joseph → Bavarian legation in Bern', 'Munich → Bern', 'German', 'Germany',
    'BayHStA, Gesandtschaft Bern 59', 'file', 'Finding aid: "Schreiben des Königs Max Josef, z.T. chiffriert".', 'Restoration diplomacy; short.', 2, 2, 3, 'Order a scan.')
add(BG, [{'label': 'Landesarchiv Coburg 7174', 'href': gda('7174')}], 1854, '1854-55', 'Letters of Prince Chimay to Duke Ernst II of Saxe-Coburg, secret script partly transcribed', 'Prince de Chimay → Ernst II of Saxe-Coburg-Gotha', 'unknown', 'unknown', 'Low Countries',
    'Staatsarchiv Coburg, Landesarchiv, Lokat A 7174', 'Bd. 1, paper', 'Finding aid: "Geheimschrift (teilweise Transkripiert)". The transcribed part is a crib.', 'Letters of the Crimean War years in a partly glossed cipher.', 3, 3, 2, 'Order a scan.', cls='A')

# ---- Arcinsys Niedersachsen
Vd = V('scan', 'https://www.arcinsys-digitalisate.niedersachsen.de/nla_ha/dep._110/a_nr._111/m_ha_dep._110_a_nr._111_aufn_0159.jpg (with aufn_0158 and aufn_0160, viewed 3 Nov 2026; also aufn_0040, 0080, 0198 as a sample of the 277 images)',
       'at least three full openings, ff. 141-143, about 20 lines a page of unbroken digits; other pieces in the file are clear or carry interlinear decipherment (aufn_0198)',
       'Continuous undivided numeric cipher with no plaintext, no gloss and no decipherment on ff. 141-143. The finding aid says "teils chiffriert (ein Teil nicht dechiffriert)".',
       NOD, NOT, NOL, 'no edition found (search 3 Nov 2026); the 1978 Haase Findbuch to Dep. 110 and Hormayr\'s Lebensbilder aus dem Befreiungskriege appear in the search but were not read for this',
       'no study of Münster\'s ciphers found; lead 1978 records Dep. 110 A Nr. 105 as read interlinearly, a different file',
       'No key held here. The interlined pieces of this same file (aufn_0198) are a likely crib; not yet tried.',
       'known.py on "Dep. 110 A Nr. 111": no hit; lead 1978 covers Nr. 105, 113, 228, 66 only; newcheck.py: new.')
add(A, arc('Dep. 110, A Nr. 111'), 1810, '1810-13', "Count Münster's papers on the war between Russia and France: reports from Göteborg, Kolberg, St Petersburg, Dresden and Lisbon, part ciphered and part never deciphered",
    "Hanoverian agents (Dörnberg and others) → Count Ernst zu Münster", 'Göteborg; Kolberg; St Petersburg; Dresden; Lisbon', 'French; German', 'Germany', 'NLA Hannover, Dep. 110 A Nr. 111', '277 images; undivided numeric cipher on ff. 141-143 (aufn_0158-0160)',
    'Finding aid: "teils chiffriert (ein Teil nicht dechiffriert)". Viewed: ff. 141-143 are unbroken digits with nothing written over them; aufn_0198 has decipherment between the lines.',
    "Anglo-Hanoverian secret intelligence against Napoleon in 1810-13, the network behind the German rising.", 5, 4, 3, 'Find all undeciphered pieces; align with the interlined ones for a crib.', cls='A', scan='no',
    access='scans free on Arcinsys Niedersachsen', seen='image', vetting=Vd)
add(A, arc('Dep. 110, A Nr. 116', 'Dep. 110, A Nr. 64'), 1809, '1809-12; 1827', "Count Münster's papers: Waldstein's letters on the 1809 alliance, teils chiffriert; Dörnberg's reports from St Petersburg 1827, teils chiffriert",
    'Graf Waldstein; General von Dörnberg → Count Münster', 'Vienna; St Petersburg', 'French; German', 'Germany', 'NLA Hannover, Dep. 110 A Nr. 116 and Nr. 64', 'digitised on Arcinsys',
    'Finding aid: "teils chiffriert" in both. Not viewed. Other files of this fonds are usually deciphered between the lines.', 'Same network as Dep. 110 A Nr. 111.', 3, 3, 3, 'Sample the scans for undeciphered pieces.', cls='B', scan='no', access='scans free on Arcinsys Niedersachsen')
Vg = V('not online', 'https://www.arcinsys.niedersachsen.de/arcinsys/showArchivalDescriptionDetails.action?archivalDescriptionId=5544978 (NLA WO 1 Alt 22 Nr. 786, read 3 Nov 2026, with Nr. 787 and 788); the unit shows original, safety film and fiche, no scans',
       '404 reports in three volumes, 1731-40, "in Chiffern"; share in cipher not stated',
       'Finding aid quoted: "404 Berichte des Legationssekretärs Christoph Friedrich Gross aus Moskau (1731) u. St. Petersburg (seit 1732) an den Geheimrat A. A. v. Cramm, z. T. mit Anlagen, in Chiffern". No decipherment is mentioned.',
       NOD, NOT, NOL, 'no edition found (search 3 Nov 2026)',
       'A Ural Federal University article (elar.urfu.ru 10995/141632) treats Gross (1696?-1742) as Osterman\'s secretary and part of the Brunswick mission (search snippet only; not read in full)',
       'No key held here. NLA WO 2 Alt Nr. 2841 "Chiffern" (1735) may hold the Petersburg key, and the Arcinsys title of 2 Alt Nr. 2837-2842 names envoys at the courts; not online, not tried.',
       'known.py on "Gross Moskau", "Cramm" and "1 Alt 22": only the unrelated 1 Alt 22 Nr. 42 and a Ludwig von Cramm of 1828; newcheck.py: new.')
add(A, arc('1 Alt 22, Nr. 786', '1 Alt 22, Nr. 787', '1 Alt 22, Nr. 788'), 1731, '1731-40', "Christoph Friedrich Gross's 404 reports from Moscow and St Petersburg to Privy Councillor von Cramm, in cipher",
    'Christoph Friedrich Gross → A. A. von Cramm (Brunswick-Wolfenbüttel)', 'Moscow; St Petersburg', 'German; French', 'Other', 'NLA Wolfenbüttel, 1 Alt 22 Nr. 786-788', '3 volumes, 404 reports with enclosures',
    'Finding aid as quoted. Not digitised. No decipherment noted.', "Secret reports from the court of Anna Ivanovna: Brunswick's Anton Ulrich was married into the Russian succession in these years.", 5, 2, 3, 'Order a sample scan; test key units 2 Alt Nr. 2840-2841.', cls='B', vetting=Vg)
add(A, arc('1 Alt 8, Nr. 549'), 1540, '1540-42', 'Duke Heinrich the Younger with his councillors on Brunswick and Goslar, the Rammelsberg and the libel against Saxony and Hesse: large parts in cipher',
    'Heinrich the Younger of Brunswick-Wolfenbüttel ↔ his councillors', 'Wolfenbüttel; Regensburg', 'German', 'Germany', 'NLA Wolfenbüttel, 1 Alt 8 Nr. 549', 'file; "Große Teile chiffriert"',
    'Finding aid as quoted. Not digitised. A printed study (https://www.sav.sk/journals/uploads/0307161001500opt.pdf, search snippet only) reproduces a single-letter cipher of Heinrich c. 1540 from 1 Alt 8 Nr. 490, so this may be a key lookup; not promoted.',
    "The feud with the Schmalkaldic League that cost Heinrich his duchy in 1542.", 4, 3, 2, 'Read the sav.sk article; order a scan; try the Nr. 490 key.', cls='B')
add(A, arc('1 Alt 8, Nr. 505'), 1544, '1544-45', "Heinrich the Younger's arming to recover his duchy: pieces in cipher and a cipher key (f. 68)", 'Heinrich the Younger and agents', 'unknown', 'German', 'Germany', 'NLA Wolfenbüttel, 1 Alt 8 Nr. 505', 'key at f. 68',
    'Finding aid: "darunter Chiffreteile und Chiffreschlüssel (f. 68)".', 'The 1545 attempt that ended in his capture at Kalefeld.', 3, 3, 1, 'Order a scan; key is in the file.', cls='A')
add(A, arc('1 Alt 8, Nr. 407', '1 Alt 8, Nr. 408'), 1553, '1553', 'Second Margrave War: letters between Philipp Magnus and Heinrich the Younger in code, to June 1553', 'Philipp Magnus ↔ Heinrich the Younger', 'unknown', 'German', 'Germany', 'NLA Wolfenbüttel, 1 Alt 8 Nr. 407 and 408', 'Bd. 2 and sibling',
    'Finding aid: "Schreiben von Herzog Philipp Magnus mit Herzog Heinrich d.J. in Geheimcode [bis Juni 1553]". Same hands as catalogue 1971 (1 Alt 22 Nr. 42).', 'Father and son writing weeks before Philipp Magnus died at Sievershausen.', 3, 2, 3, 'Order a scan; pair with 1 Alt 22 Nr. 42.', cls='B')
add(A, arc('1 Alt 22, Nr. 204a'), 1620, '1620-30', "Duke August the Younger with Dr Thomas Lindemann of Rostock, including partly ciphered letters of Wallenstein's chancellor Johann Eberhard Sohn",
    'Johann Eberhard Sohn; Thomas Lindemann → August the Younger', 'Rostock; Güstrow', 'German', 'Germany', 'NLA Wolfenbüttel, 1 Alt 22 Nr. 204a', 'several letters', 'Finding aid: "Mehrere, z. T. chiffrierte Schreiben des friedländischen Kanzlers Johann Eberhard Sohn".',
    "Wallenstein's Mecklenburg chancery writing to the later author of Cryptomenytices (1624).", 4, 2, 3, 'Order a scan; try the systems in Selenus 1624.', cls='B')
add(A, arc('2 Alt, Nr. 560'), 1727, '1727-41', "Knörr's reports to Prime Minister Münchhausen, with ciphered passages (series 2 Alt Nr. 560-579, sibling of catalogue 1976)", 'Georg Christian von Knörr → Hieronymus von Münchhausen', 'Vienna', 'German', 'Central Europe', 'NLA Wolfenbüttel, 2 Alt Nr. 560-579', '20 volumes',
    'Finding aid: "[mit chiffrierten Stellen]". Same writer and years as catalogue 1976 (Nr. 580-589), a different series.', 'Twenty more volumes from the same Vienna agent.', 3, 2, 3, 'Treat with catalogue 1976; order a sample.', cls='B')
add(A, arc('2 Alt, Nr. 3565'), 1673, '1673-75', 'Letters of Duke Rudolf August to a legation councillor, some with ciphered lines', 'Rudolf August of Brunswick-Wolfenbüttel → legation councillor', 'Wolfenbüttel', 'German', 'Germany', 'NLA Wolfenbüttel, 2 Alt Nr. 3565', 'Bd. 6; film 5064', 'Finding aid: "Chiffrierte Zeilen in einigen Schreiben".', 'Short ducal cipher in the Dutch War.', 2, 2, 3, 'Order a scan; try keys in 2 Alt Nr. 2838.', cls='B')
add(A, arc('Cal. Br. 15, Nr. 3805'), 1636, '1636-37', 'Seizure of the ciphered correspondence of Dr Wilhelm Burchhard Sixtinus with his brother at Kassel', 'Wilhelm Burchhard Sixtinus ↔ his brother at Kassel', 'Calenberg; Kassel', 'German', 'Germany', 'NLA Hannover, Cal. Br. 15 Nr. 3805', 'Criminalia file', 'Finding aid: "Beschlagnahme von chiffrierter Korrespondenz". Not viewed. targets/malsburg1637 holds a Hesse-Kassel Sixtinus key of Dec 1635.',
    'Intercepted letters in a spy case, possibly readable with a held key.', 3, 3, 2, 'Order a scan; try the Sixtinus key in targets/malsburg1637.', cls='B')
add(A, arc('Ballati Nr. 23', 'Ballati Nr. 24'), 1683, '1683; 1691', "Letters to Abbé Luigi Ballati, partly ciphered, and the anonymous or ciphered letters of the French diplomat Benoît d'Asfeldt from Hamburg", "Paolo de Rinavola, Diego Nunez da Costa, Benoît d'Asfeldt → Abbé Luigi Ballati", 'Hannover; Hamburg', 'French; Italian', 'Germany',
    'NLA Hannover, Hann. 91 Ballati Nr. 23 and 24', 'two files', 'Finding aid: "zum Teil anonyme oder chiffrierte Korrespondenzen". Not digitised.', "Hanover's Catholic envoy and Louis XIV's man in the north, in Leibniz's circle.", 3, 2, 3, 'Order scans.')
add(A, arc('Best. 100, - 135 Nr. 91'), 1641, '11 Mar 1641', 'Dr Abraham Kayser to the Hildesheim council from the Regensburg Diet, partly in cipher', 'Abraham Kayser → Rat der Stadt Hildesheim', 'Regensburg', 'German', 'Germany', 'Stadtarchiv Hildesheim, Best. 100-135 Nr. 91', 'one report', 'Finding aid: "zum Teil in Chiffern".', 'A town agent at the 1640-41 Diet.', 2, 2, 3, 'Order a scan.')
add(A, arc('Rep. 32, Nr. 194'), 1581, 'Jan-Feb 1581 (to 1588)', "Anger de Busbeck's reports from Paris, ciphered and deciphered", 'Ogier Ghiselin de Busbecq (imperial envoy in Paris) → unknown', 'Paris', 'unknown', 'France', 'NLA Stade, Rep. 32 Nr. 194', 'part of a run to 1588', 'Finding aid: "Chiffrierte und dechiffrierte Berichte". Probably read at the time; kept as a sibling for the Busbecq ciphers.', 'Busbecq in Paris; a key source if the pairs are there.', 3, 3, 1, 'Check the pairs; useful as a crib rather than a target.', cls='A')
add(A, arc('1 Alt 3, Nr. 27'), 1726, '1726-27', 'Partly ciphered and deciphered French letters of the envoy to Vienna on the Wolfenbüttel-Blankenburg talks', 'Envoy extraordinary → Brunswick-Wolfenbüttel', 'Vienna', 'French', 'Central Europe', 'NLA Wolfenbüttel, 1 Alt 3 Nr. 27', 'file', 'Finding aid: "Zum Teil chiffrierte und dechiffrierte Schreiben". Probably read at the time.', 'Crib for the Knörr series (catalogue 1976).', 2, 3, 1, 'Check whether every piece has its decipherment.', cls='A')

# ---- Arcinsys Hessen
add(A, arc('170 III, 29'), 1523, '1523', 'Nassau-Dillenburg correspondence of 1523 with partly ciphered letters (sibling of catalogue 561, 170 III Nr. 30)', 'Landgrave Philipp of Hesse, Count Philipp of Solms and others', 'unknown', 'German', 'Germany', 'HHStAW, 170 III Nr. 29', 'digitised on Arcinsys', 'Finding aid: "Z. T. chiffrierte Korrespondenz". Not viewed.', 'The year of the Sickingen feud.', 3, 3, 3, 'Find the cipher pieces in the scans; pair with Nr. 30.', cls='B', scan='no', access='scans free on Arcinsys Hessen')
add(A, arc('4 h, 1815'), 1645, '1645', 'Ciphered instruction of Landgravine Amalie Elisabeth on quarters and the state of the cavalry', 'Amalie Elisabeth of Hesse-Kassel → commander', 'Kassel', 'German', 'Germany', 'HStAM, 4 h Nr. 1815', 'one instruction', 'Finding aid: "Chiffrierte Anweisung". Not viewed. targets/malsburg1637 studied Hesse-Kassel keys of these years.', 'Regent of Hesse-Kassel directing the last war years in her own cipher.', 3, 3, 2, 'Order a scan; try the Hesse-Kassel keys in targets/malsburg1637.', cls='B')
add(A, arc('D 4, 245/1'), 1644, '1644-70', 'Landgravine Sophie Eleonore to her son Ludwig VI, 220 letters, some in cipher', 'Sophie Eleonore of Hesse-Darmstadt → Ludwig VI', 'Darmstadt', 'German', 'Germany', 'HStAD, D 4 Nr. 245/1', '233 images; 220 letters', 'Finding aid: "Enthält zum Teil chiffrierte Briefe". Eight images sampled 3 Nov 2026 at low resolution; cipher pieces not located.', 'A mother and son writing privately over 26 years.', 2, 3, 3, 'Page through the scans for the cipher letters.', scan='no', access='scans free on Arcinsys Hessen')
add(A, arc('D 4, 409/1'), 1736, '1736-40', 'Correspondence of Landgrave Ludwig VIII, with partly encrypted reports on the imperial court and Regensburg', 'Correspondents → Ludwig VIII of Hesse-Darmstadt', 'Vienna; Regensburg', 'German', 'Germany', 'HStAD, D 4 Nr. 409/1', '426 images; 196 letters', 'Finding aid: "Teilweise verschlüsselte Berichte über politischen Entwicklungen am Kaiserhof und in Regensburg". Not located in the scans yet.', 'Darmstadt\'s information from the imperial court before the Austrian Succession.', 3, 3, 3, 'Page through the scans.', scan='no', access='scans free on Arcinsys Hessen')
add(A, arc('D 4, 487/4', 'D 4, 487/6'), 1788, '1788-97', 'Hofrat Jähring to Landgrave Georg Karl, letters including ciphered ones', 'Hofrat Jähring → Georg Karl of Hesse-Darmstadt', 'unknown', 'German', 'Germany', 'HStAD, D 4 Nr. 487/4 and 487/6', '226 images in 487/4; 93 and 196 letters', 'Finding aid: "Chiffrierte Briefe". Eight images of 487/4 sampled 3 Nov 2026; no whole cipher letter located.', 'Revolutionary-era reports to a Hessian prince.', 2, 3, 3, 'Page through the scans.', scan='no', access='scans free on Arcinsys Hessen')
add(A, arc('E 8 A, 208/3'), 1643, 'Oct 1643', 'Ciphered report from Vienna among letters on the European situation, Georg II of Hesse-Darmstadt', 'unknown → Georg II', 'Vienna', 'German', 'Central Europe', 'HStAD, E 8 A Nr. 208/3', 'Konvolut 143', 'Finding aid: "verschlüsselter Bericht aus Wien, Oktober 1643". Not in catalogue 568\'s list of E 8 A units. Key candidate D 4 Nr. 141/2.', 'Adds a Vienna report to the Georg II group.', 3, 2, 2, 'Order a scan; treat with catalogue 568.', cls='B')
add(A, arc('E 1 M, 54/1', 'E 1 M, 54/2', 'E 1 M, 54/3', 'E 1 M, 54/4'), 1673, '1673-76', "Nikolaus Martin Drach, Hesse-Darmstadt's agent in Vienna, to Ludwig VI, with a key to diplomatic ciphers", 'Nikolaus Martin Drach → Ludwig VI of Hesse-Darmstadt', 'Vienna', 'German', 'Central Europe', 'HStAD, E 1 M Nr. 54/1-54/4', '4 files', 'Finding aid: "mit Schlüssel zur Entzifferung diplomatischer Geheimschriften". Key in the file.', 'Vienna reporting in the Dutch War with its key to hand.', 3, 3, 1, 'Order scans; align the key.', cls='A')
add(A, arc('KHA Inv. A 22 Nr. 191', 'KHA Inv. A 22 Nr. 195', 'KHA Inv. A 22 Nr. 197'), 1590, '1590-1608', 'Letters to and from the Nassau councillor and secretary Erasmus Stöver, Count Wilhelm Ludwig and Johann VII, partly in secret script', 'Erasmus Stöver ↔ Wilhelm Ludwig and Johann VII of Nassau', 'Dillenburg; Leeuwarden', 'German', 'Low Countries', 'Koninklijk Huisarchief inventory A 22 Nr. 191, 195, 197 (HHStAW 3036 lists it)', 'held at The Hague', 'Finding aid: "z. T. in Geheimschrift / deels in geheimschrift". Listed in the HHStAW finding aid; originals in the Koninklijk Huisarchief. Same family as catalogue 566 (171 S 995).', 'The Nassau inner circle during the Dutch reforms.', 3, 2, 3, 'Ask the KHA for scans; compare with HHStAW 171 S 995 and C 667.', cls='B')
add(A, arc('KHA Inv. A 23 Nr. 203'), 1629, '1629', 'Letters of the Deventer town government to Ernst Casimir of Nassau-Diez, a draft reply mostly in secret script', 'Stadsbestuur Deventer ↔ Ernst Casimir of Nassau-Diez', 'Deventer', 'Dutch', 'Low Countries', 'Koninklijk Huisarchief inventory A 23 Nr. 203 (HHStAW 3036 lists it)', 'held at The Hague', 'Finding aid: "überwiegend in Geheimschrift / grotendeels in geheimschrift". Sibling of lead 1982.', 'The 1629 Spanish invasion of the Veluwe.', 3, 2, 3, 'Ask the KHA for scans; A 23 Nr. 311 holds keys for this correspondence.', cls='A')

# ---- Landesarchiv BW
add('Landesarchiv BW', [{'label': 'HStA Stuttgart J 1 Nr. 219', 'href': LABW % 7431511}], 1635, 'to 1635', "Johann Leonhard Beringer's collectanea, 692 leaves on the events of his time, with encrypted passages partly resolved in the margin", 'Johann Leonhard Beringer (own compilation)', 'Württemberg', 'German', 'Germany', 'Hauptstaatsarchiv Stuttgart, J 1 Nr. 219', 'X, 692 Bl.; digitised', 'Finding aid: "zum Zeitgeschehen, mit verschlüsselten (teilweise am Rand auf[gelösten])" passages. Partly glossed, so a crib is on the page. Not viewed.', 'A contemporary notebook of the Thirty Years War with its own glosses.', 3, 4, 2, 'Open the LABW viewer (Digitalisate einsehen); locate the cipher passages.', cls='A', scan='no', access='scans free on the Landesarchiv BW viewer')
add('Landesarchiv BW', [{'label': 'GLA 50 Nr. 933 a (Stockmayer 1778-79)', 'href': LABW % 7909469}, {'label': 'GLA 50 Nr. 1291 (1774)', 'href': LABW % 7910034}, {'label': 'GLA 50 Nr. 734 (1776)', 'href': LABW % 7909140}], 1774, '1774-79', "Baden-Durlach's reports from the Diet, partly ciphered, and Jakob Friedrich von Stockmayer's ciphered reports from Vienna", 'Baden-Durlach envoys, J. F. von Stockmayer → Margrave Karl Friedrich', 'Regensburg; Vienna', 'German', 'Germany', 'Generallandesarchiv Karlsruhe, 50 Nr. 933 a, 1291, 734', 'three files 1774-79 (siblings of catalogue 576, GLA 50 Nr. 924 and 924 a)', 'Finding aid: "Reichstagsberichte, zum Teil chiffrirt", "chiffrirte Berichte Jakob Friedrich von Stockmayers aus Wien", "chiffrirter Bericht aus Wien". GLA 48 Chiffren units 66-70 (lead 1671) hold keys.', 'The Bavarian Succession from a small Protestant court.', 3, 2, 2, 'Order a sample; try GLA 48 Chiffren 1 Nr. 3 and Chiffren 2 Nr. 7a.', cls='A')
add('Landesarchiv BW', [{'label': 'Abel 1797', 'href': LABW % 13119616}, {'label': 'Abel 1798', 'href': LABW % 13119619}, {'label': 'Abel 1799', 'href': LABW % 13119621}, {'label': 'Normann 1801', 'href': LABW % 13119626}], 1797, '1797-1801', 'Reports of the Württemberg envoys Abel and Normann from Paris during Rastatt and Lunéville, some in cipher', 'Christoph Konrad Abel, Philipp Christian von Normann → Duke of Württemberg', 'Paris', 'German; French', 'France', 'Hauptstaatsarchiv Stuttgart, A 16 a Bü 696, 699, 701, 706', 'see A 74 i Bü. 24', 'Finding aid: "Einige Berichte sind chiffriert; vgl. auch A 74 i Bü. 24".', 'Paris diplomacy of a German court through the Directory.', 3, 2, 3, 'Order a sample; A 74 i Bü. 24 may hold the deciphered copies.', cls='A')
add('Landesarchiv BW', [{'label': 'Rheinbund 1806', 'href': LABW % 2944401}], 1806, 'July-Aug 1806', "Württemberg's resistance to the Confederation of the Rhine: encrypted secret correspondence", 'Württemberg foreign ministry', 'Stuttgart', 'German; French', 'Germany', 'Hauptstaatsarchiv Stuttgart, E 40/11 Bü 243', 'file with list of acts', 'Finding aid: "verschlüsselte Geheimkorrespondenz".', 'The weeks Bavaria and Württemberg tried to refuse Napoleon.', 4, 2, 3, 'Order a scan.')
add('Landesarchiv BW', [{'label': 'Petersburg 1834', 'href': LABW % 1505239}], 1834, '4 Jan - 25 June 1834', 'Relations of the Württemberg envoy in St Petersburg, Prince Hohenlohe-Kirchberg, with ciphered texts (the 1835 volumes add deciphering)', 'Heinrich Prince of Hohenlohe-Kirchberg → Württemberg foreign ministry', 'St Petersburg', 'German; French', 'Other', 'Hauptstaatsarchiv Stuttgart, E 50/11 Bü 44', 'file', 'Finding aid: "chiffrierte Texte" in 1834; "chiffrierte Texte mit Dechiffrierung" in the 1835 units, which give a crib.', 'Nicholas I\'s Russia from a German envoy.', 2, 3, 2, 'Order 1834 and a 1835 unit together.', cls='A')
add('Landesarchiv BW', [{'label': 'Mentzingen 1785-95', 'href': LABW % 3395768}], 1785, '1785-95', 'Sale of Gondelsheim by the Mentzingen family to Baden, with texts encrypted in a number code', 'Family von Mentzingen; Baden', 'Gondelsheim', 'German', 'Germany', 'Generallandesarchiv Karlsruhe, 72 Nr. 6372', '5 cm file', 'Finding aid: "Einige mit Zahlencode verschlüsselte Texte".', 'A private number code in a land sale.', 1, 2, 3, 'Order a scan.')

json.dump(rows, open(os.path.join(HERE, 'candidates.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(rows), sum(1 for r in rows if r.get('vetting')))
