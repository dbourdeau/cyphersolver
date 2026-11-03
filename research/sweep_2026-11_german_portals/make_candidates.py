"""Build candidates.json for the German-portals sweep (2 Nov 2026) from the shortlists in labw_selected.md,
arcinsys_ni_selected.md and the Arcinsys Hessen harvest in README.md. Rows are leads scored from descriptions."""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
TODAY = '2 Nov 2026'
SRC = {
    'labw': ('Landesarchiv BW sweep', 'Landesarchiv BW online finding aids (www2.landesarchiv-bw.de/ofs21)',
             'https://www2.landesarchiv-bw.de/ofs21/olf/druckansicht.php?id_titlaufn=%s'),
    'ni': ('Arcinsys Niedersachsen sweep', 'Arcinsys Niedersachsen',
           'https://www.arcinsys.niedersachsen.de/arcinsys/showArchivalDescriptionDetails.action?archivalDescriptionId=%s'),
    'he': ('Arcinsys Hessen sweep', 'Arcinsys Hessen',
           'https://arcinsys.hessen.de/arcinsys/showArchivalDescriptionDetails.action?archivalDescriptionId=%s'),
}
PRIOR = ('open as far as checked (%s: known.py on shelfmark and names, repo catalogue, leads and sweep files; '
         'DECODE, Tomokiyo, Lasry, the edition and the literature not yet searched)' % TODAY)

rows = []


def add(src, ids, year, date, title, corr, place, lang, region, period, shelf, note, status, why, imp, sol, dif, verify,
        cls='C', digital='unknown', access=''):
    name, site, url = SRC[src]
    rows.append({
        'year': year, 'date': date, 'title': title, 'correspondents': corr, 'place': place, 'language': lang,
        'region': region, 'period': period, 'shelfmark': shelf, 'folio_note': note, 'cls': cls,
        'status': status + ' No decipherment mentioned in the description.', 'why': why,
        'importance': imp, 'solvability': sol, 'difficulty': dif,
        'score_note': 'Scored from the finding-aid description during the Nov 2026 German portals sweep '
                      '(research/sweep_2026-11_german_portals/); not viewed',
        'verify': verify,
        'links': [{'label': '%s %s' % (site.split(' (')[0], i), 'href': url % i} for i in ids],
        'seen': 'catalogue', 'source': name, 'prior_art': PRIOR, 'needs_archive_scan': digital,
        'access_note': access or 'whether the unit is digitised is not shown in the finding-aid text; check "Digitalisate" on the unit page',
    })


add('labw', [8406631], 1546, 'Jun 1546', 'Schmalkaldic War: letters to and from Duke Ulrich of Württemberg, newsletters and warnings, with an alphabet of cipher signs (Nr. 132 d)',
    'Duke Ulrich of Württemberg and correspondents', 'various', 'German', 'Germany', '1497-1559',
    'Hauptstaatsarchiv Stuttgart, H 55 Bü 20', 'Nr. 81-140; Nr. 132 d carries an "Alphabet mit Zeichen als Verschlüsselung"',
    'Landesarchiv BW: the file contains an alphabet of signs used as encipherment, so some letters in it are probably enciphered with it.',
    'A key sheet inside a Schmalkaldic War file can read the ciphered warnings of June 1546.', 3, 3, 2,
    'Open the unit, find the ciphered letters near Nr. 132 d, and test the alphabet on them.', cls='B')
add('labw', [10752199], 1621, '1621', 'Enciphered letter to Weikersheim (sender and recipient not named)',
    'unknown → Weikersheim (?)', 'unknown', 'German', 'Germany', '1611-1650', 'Hohenlohe-Zentralarchiv Neuenstein, We 5 Bü 1105',
    'one letter', 'Landesarchiv BW: "Verschlüsseltes Schreiben nach Weikersheim(?)", 1621.',
    'A single 1621 Hohenlohe letter in a cipher of the first Thirty Years\' War year.', 2, 2, 3,
    'View the unit; check length and whether a key sits in the Weikersheim Schlossarchiv.')
add('labw', [10753127], 1621, '1621-1634', 'Letters of a commander of the Franconian Circle and governor of Augsburg, using secret codes or a secret script',
    'unknown (Franconian Circle commander) → Hohenlohe', 'Augsburg / Franconia', 'German', 'Germany', '1611-1650',
    'Hohenlohe-Zentralarchiv Neuenstein, We 5 Bü 2955', 'a bundle of letters 1621-1634',
    'Landesarchiv BW: letters "in geheime Codes oder eine Geheimschrift benutzendes Schreiben".',
    'Military letters of the Franconian Circle in the early Thirty Years\' War.', 3, 3, 3,
    'View the unit; identify the commander (Hohenlohe Weikersheim papers) and the cipher type.')
add('labw', [2951408], 1707, '1707-1726', 'Grävenitz trial: ciphered correspondence of the Württemberg missions to Vienna and Paris',
    'Württemberg envoys ↔ court', 'Stuttgart / Vienna / Paris', 'German; French', 'Germany', '1701-1800',
    'Hauptstaatsarchiv Stuttgart, A 48/05 Bü 51', 'item 5: "Chiffrierter Schriftverkehr mit ..."',
    'Landesarchiv BW: general evidence file of the Grävenitz and Würben trials lists ciphered correspondence 1707 and 1709/10.',
    'Evidence file for the fall of Württemberg\'s favourite Grävenitz; the cipher letters were used as proof.', 3, 3, 3,
    'View the file for the ciphered items and whether a key is bound in; possible overlap with the lead already merged from Archivportal-D (merge row 52).')
add('ni', [5544081], 1553, '1553', 'Duke Heinrich the Younger of Brunswick-Wolfenbüttel and his son Philipp Magnus: war affairs, partly ciphered',
    'Heinrich d. J. ↔ Philipp Magnus', 'Wolfenbüttel', 'German', 'Germany', '1497-1559',
    'NLA Wolfenbüttel, 1 Alt 22 Nr. 42', 'one unit; letters of 1553',
    'Arcinsys: "welche besonders die damaligen Kriegshändel betreffen und z. T. chiffriert sind".',
    'Letters of a Catholic prince in the year of Sievershausen, 1553, with the cipher he used with his son.', 3, 3, 3,
    'View the digitised unit if any; compare with the Heinrich der Jüngere ciphers (BU L 1 Nr. 548, 562) already in the repo.')
add('ni', [11492288], 1641, '1641', 'Colonel Rauschenberg, commandant of Wolfenbüttel, to an Elector (partly ciphered)',
    'Oberst von Rauschenberg → an Elector', 'Wolfenbüttel', 'German', 'Germany', '1611-1650',
    'NLA Wolfenbüttel, 250 N Nr. 1148', 'one letter',
    'Arcinsys: "teilweise chiffriert", on the stance towards the Swedes.',
    'A commandant\'s letter at the time of the Wolfenbüttel occupation (1641).', 2, 3, 3,
    'View the unit; Rauschenberg appears in the Brunswick cipher files.')
add('ni', [5542497], 1657, '1657-1660', 'Chancellor Johann von Schwartzkopf: affairs in Celle, Hanover, Magdeburg, Peine, Berlin; negotiations with the prince',
    'Johann von Schwartzkopf and the Brunswick-Lüneburg courts', 'Celle / Hanover / Berlin', 'German', 'Germany', '1651-1700',
    'NLA Wolfenbüttel, 1 Alt 12 Nr. 1 Bd. 1', 'volume 1',
    'Arcinsys description mentions ciphered parts (truncated in the search view).',
    'Correspondence of a Guelph chancellor in the years after Westphalia.', 2, 2, 3,
    'Open the unit page for the full description before scoring further.')
add('ni', [3049208], 1671, '1671-1674', 'Otto Grote to the envoy Statz Victor von Mandelsloh at Stockholm: drafts of reports, cipher',
    'Otto Grote → Mandelsloh', 'Hanover / Stockholm', 'German', 'Germany', '1651-1700',
    'NLA Hannover, Cal. Br. 24 Nr. 7480', 'one unit',
    'Arcinsys: drafts of individual reports, "Chiffre..." (truncated).',
    'Hanoverian diplomacy at Stockholm during the Franco-Dutch war.', 3, 3, 3,
    'Open the unit page; the Cal. Br. 24 volume also holds ciphers (Nr. 62, 5084, 5094).')
add('ni', [3048570], 1711, '1711', 'Privy legation councillor von Fabrice: reports from Mecklenburg and Pütt near Stralsund to Minister Bernstorff, partly ciphered',
    'von Fabrice → Bernstorff', 'Pütt near Stralsund', 'German', 'Germany', '1701-1800',
    'NLA Hannover, Cal. Br. 24 Nr. 6801', 'one unit',
    'Arcinsys: reports "zum Teil" in cipher (truncated); Celle Br. 92 Nr. 119 holds a Chiffre for Fabrice.',
    'Hanoverian reports from the Great Northern War front at Stralsund, 1711.', 3, 4, 2,
    'Open the unit; the Fabrice cipher (Celle Br. 92 Nr. 119) is a held-key candidate, so check that first.', cls='B')
add('ni', [3960235, 3960234, 3960246, 3960247, 3960248, 3960260, 3960259, 3960258, 3960257, 3960256], 1727, '1727-1749',
    'Reports "partly ciphered" of a Blankenburg court councillor, later Reichshofrat and Wolfenbüttel privy justice councillor (ten volumes)',
    'Georg Ch... (Reichshofrat) → Wolfenbüttel / Blankenburg court', 'Vienna', 'German', 'Germany', '1701-1800',
    'NLA Wolfenbüttel, 2 Alt Nr. 580-589', 'ten units, one per year or two',
    'Arcinsys: every title says "Berichte (zum Teil chiffriert)"; the full name is cut off in the search view.',
    'A long run of Vienna reports with one agent\'s cipher, enough text for a statistical solve.', 3, 4, 2,
    'Open Nr. 580 for the full name and digitisation; look for the key in the same fonds (2 Alt Nr. 2838 holds Chiffern of 1675-1725).')
add('ni', [1680530, 1684901], 1738, '1738-1739', 'Reichshofrat Knorre: report on his conversion to Catholicism (partly in cipher) and a gift of 1,000 ducats',
    'Hanover court ↔ Reichshofrat Knorre', 'Vienna / Hanover', 'German', 'Germany', '1701-1800',
    'NLA Hannover, Cal. Br. 15 Nr. 2225, 2233', 'two units',
    'Arcinsys: "z.T. in Chiffre verfaßt".',
    'A confessional affair of a Hanoverian Reichshofrat, 1738.', 2, 3, 3,
    'Open the units; look for ciphertext length.')
add('ni', [3411478, 3411492, 3411582, 3411441], 1808, '1808-1814', 'Münster papers: reports and letters partly in cipher from Canning, Nugent, Bremer, Dörnberg (Russia, Austria, plans to free Germany)',
    'Count Münster ↔ Nugent, Bremer, Dörnberg, Canning', 'London / St Petersburg / Vienna', 'German; French', 'Germany', '1801-1900',
    'NLA Hannover, Dep. 110 A Nr. 105, 113, 228, 66', 'four units',
    'Arcinsys: "Berichte (meist chiffriert)", "teils chiffriert", "einzelne Briefe chiffriert".',
    'Hanoverian-British conspiracy letters of the Napoleonic wars, in ciphers that may match the Hanoverian legation keys in NLA HA Dep. 103 VIII.', 4, 4, 2,
    'The legation Chiffren are in Dep. 103 VIII (Nr. 458-476, 1805-30); that is a held-key route if the ciphers match. View the units.', cls='B')
add('ni', [7168843, 7145076], 1828, '1828-1830', 'Brunswick envoys at the Frankfurt Bundestag: letters of Ludwig von Cramm and others, partly ciphered',
    'von Cramm; von Thielau; von Hohnhorst; Marschall', 'Frankfurt / Celle / Wiesbaden', 'German', 'Germany', '1801-1900',
    'NLA Wolfenbüttel, 242 N Nr. 823, 347', 'two units',
    'Arcinsys: "z.T. chiffriert".', 'Brunswick politics under Duke Charles II before the 1830 revolution.', 2, 3, 3,
    'View the units.')
add('ni', [5536294], 1750, '18th c. (mid)', 'Brunswick places: assorted papers, partly in secret script, concerning a Wolfenbüttel affair of the mid-18th century',
    'unknown', 'Wolfenbüttel', 'German', 'Germany', '1701-1800',
    'NLA Wolfenbüttel, VI Hs 15 Nr. 143', 'one unit',
    'Arcinsys: "zum Teil in Geheimschrift geschrieben".', 'Small miscellany of a local scholar\'s papers.', 1, 2, 3,
    'View the unit.')
add('he', [5797116, 5797121, 5914472, 5914474, 5914463, 5914464, 5914475, 5914466, 5914476, 5914468, 5797195, 5914477], 1666, '1666-1687',
    'Chancellor Vigelius: reports from Vienna and Constantinople to the Counts of Nassau-Idstein / Nassau-Usingen, "Briefe chiffriert" (fourteen volumes)',
    'Chancellor Vigelius → Count Walrad of Nassau-Usingen', 'Vienna / Constantinople', 'German', 'Germany', '1651-1700',
    'Hessisches Hauptstaatsarchiv Wiesbaden, 130 I Nr. 400-412, 463', 'about 14 volumes; Nr. 400 notes "Briefe chiffriert"',
    'Arcinsys: Nr. 400 (1666-75) carries the note "Briefe chiffriert"; the other volumes belong to the same series of embassy reports.',
    'A long, single-agent run of Habsburg-court reports on the imperial princely rank of Nassau, a good statistical target.', 3, 4, 2,
    'Open Nr. 400 and a later volume; no digital copy shown on the unit page, so likely archive-only.', digital='unknown')
add('he', [4174856, 2372085, 1745074], 1640, '1629-1653', 'Letters to the Counts of Nassau-Diez, partly in secret script (Zutphen 1629, Friesland deputies 1645-53, 1640 letters)',
    'various → Counts Ernst Kasimir, Heinrich Kasimir, Wilhelm Friedrich of Nassau-Diez', 'Zutphen / Friesland', 'Dutch; German', 'Low Countries', '1611-1650',
    'Hessisches Hauptstaatsarchiv Wiesbaden, 3036 (Koninklijk Huisarchief inventory) A 23 Nr. 223; A 24 Nr. 8; A 25 Nr. 347', 'three units',
    'Arcinsys: "teils in Geheimschrift", "z. T. in Geheimschrift", "zum Teil in Geheimschrift"; the originals are in The Hague, Wiesbaden holds the inventory.',
    'Dutch stadholder-family letters; the Hague holds the documents, so check there.', 3, 2, 3,
    'Check whether the Koninklijk Huisarchief (The Hague) holds scans; the Wiesbaden entry is the finding aid only.', digital='yes',
    access='the finding aid is in Arcinsys Hessen (HHStAW 3036), the documents belong to the Koninklijk Huisarchief; scans not shown')
add('he', [3646744], 1640, '1640', 'Reports on the junction of Lüneburg and Lower Hessian troops with Weimar and French forces (partly enciphered)',
    'Hessian field officers → Landgrave Georg II', 'Hesse', 'German', 'Germany', '1611-1650',
    'Hessisches Staatsarchiv Darmstadt, E 8 A Nr. 150/2', 'one unit',
    'Arcinsys: "teilweise verschlüsselt". Same series as the Georg II letters already in the catalogue (E 8 A 217/1, 227/2).',
    'Darmstadt military correspondence of 1640; likely the same cipher family as the other E 8 A units.', 3, 4, 2,
    'View the unit; compare with the catalogue entry for the Georg II ciphers.', cls='B')
add('he', [3352629], 1672, '1672', 'Secretary Linker, from Hamburg, on his treatment at the Danish court and Brandenburg\'s envoy',
    'Linker (Hesse-Kassel) → Kassel', 'Hamburg / Copenhagen', 'German', 'Germany', '1651-1700',
    'Hessisches Staatsarchiv Marburg, 4 f Staaten D, Dänemark 125', 'one unit',
    'Arcinsys hit on "Chiffre"; the search view shows no further description.', 'Minor Hesse-Kassel diplomatic dispatch.', 1, 2, 3,
    'Open the unit page to see why it matched.')
add('he', [4131421], 1744, '1744', 'Military news for Prince Carl August Friedrich, in cipher',
    'unknown → Prince Carl August Friedrich of Waldeck', 'unknown', 'German', 'Germany', '1701-1800',
    'Hessisches Staatsarchiv Marburg, 118 a Nr. 3954', 'one unit',
    'Arcinsys: "in Chiffre", military news of 1744 (War of the Austrian Succession).', 'A Waldeck newsletter in cipher.', 2, 3, 3,
    'View the unit.')
add('he', [186282], 1776, '1776-1795', 'Reports of the Hesse-Homburg legation councillor Reckert at Berlin',
    'Reckert → Landgrave of Hesse-Homburg', 'Berlin', 'German', 'Germany', '1701-1800',
    'Hessisches Staatsarchiv Darmstadt, D 11 Nr. 111/20', 'one unit',
    'Arcinsys hit on a cipher word; the description in the search view does not show it.', 'Minor court reports under Frederick II.', 2, 3, 3,
    'Open the unit page to see where the cipher is mentioned.')
add('he', [5062992], 1775, '1775-1777', 'Eleven letters from Ansbach, "Adelaide" to "Eugenie" (names in quotation marks)',
    '"Adelaide" → "Eugenie"', 'Ansbach', 'French; German', 'Germany', '1701-1800',
    'Hessisches Staatsarchiv Darmstadt, F 27 G Nr. 427', 'eleven letters',
    'Arcinsys hit on a cipher word; the quoted pseudonyms suggest a code or cover names.', 'Private letters in cover names.', 1, 2, 4,
    'Open the unit page to see why it matched.')

json.dump(rows, open(os.path.join(HERE, 'candidates.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(rows), 'rows')
