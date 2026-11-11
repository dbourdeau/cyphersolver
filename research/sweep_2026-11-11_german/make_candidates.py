"""Builds candidates.json and key_leads.json for the 11 Nov 2026 German sweep. Edit rows here, then run:
    python3 research/sweep_2026-11-11_german/make_candidates.py
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
GSTA = 'https://archive.spk-berlin.de/actaproweb/search.xhtml'
ACC = ('Not digitised. Description in the GStA PK database (archive.spk-berlin.de/actaproweb, search the Signatur); '
       'reading room in Berlin-Dahlem or a paid scan order.')
NOTE = 'Scored from the archive description during the 11 Nov 2026 German sweep (research/sweep_2026-11-11_german/); not viewed'
DEC = 'DECODE keyword search (de-crypt.org RecordsList, 11 Nov 2026) for %s: no matching record; DECODE lists no GStA PK holdings at all (searches "GStA", "Geheimes", "Dahlem", "Privy State" gave only Dresden and BL rows).'
TOM = 'Cryptiana german.htm and frederick.htm fetched 11 Nov 2026 and searched for %s: not mentioned.'


def row(year, date, title, corr, place, lang, period, shelf, folio, cls, status, why, imp, sol, dif, verify, prior, label=None,
        href=GSTA, scan='yes', access=ACC, region='Germany', vetting=None, note=NOTE):
    r = {'year': year, 'date': date, 'title': title, 'correspondents': corr, 'place': place, 'language': lang, 'region': region,
         'period': period, 'shelfmark': shelf, 'folio_note': folio, 'cls': cls, 'status': status, 'why': why,
         'importance': imp, 'solvability': sol, 'difficulty': dif, 'score_note': note, 'verify': verify,
         'links': [{'label': label or shelf, 'href': href}], 'seen': 'catalogue', 'source': 'GStA PK database / German portals sweep',
         'prior_art': prior, 'needs_archive_scan': scan, 'access_note': access}
    if vetting:
        r['vetting'] = vetting
    return r


ROWS = []

# 1. The one row with a block: the archive itself says the decipherment is partial.
ROWS.append(row(
    1758, 'Dec 1758', 'Martinet at Môtiers-Travers: ciphered message on the Neuchâtel officers affair, only partly deciphered',
    'Martinet (Môtiers, Val-de-Travers) → Prussian administration of Neuchâtel / Berlin', 'Môtiers-Travers', 'French',
    '1701-1800', 'GStA PK, I. HA Rep. 64 (Oranische Erbschaft / Neuchâtel), Nr. 828', 'one message in a file of 1758-1759; length not given',
    'C', 'GStA finding aid: "Empfehlungen diesbezüglich des Herrn Martinet (chiffrierte Mitteilung, teils entziffert, Môtiers-Travers, '
    'Dezember 1758)". Not on DECODE. Partial decipherment noted by the archive, so kept.',
    'A local informant\'s advice on the punishment of Vattel le cadet, Pury and Perregaux in the foreign-service affair of 1758.',
    2, 1, 3, 'Order a scan of the Martinet piece; compare with the Neuchâtel cipher table of 1703 in Rep. 64 Nr. 944 and the "Chiffrierung" notes in Nr. 777.',
    'open as far as checked 11 Nov 2026: DECODE, Cryptiana, two web searches, no edition of the 1758-59 Neuchâtel files found',
    vetting={
        'date': '2026-11-11', 'by': 'claude cloud sweep 11 Nov german',
        'seen': {'kind': 'not online', 'where': 'GStA PK database record I. HA Rep. 64, Nr. 828 (archive.spk-berlin.de/actaproweb), full record read 11 Nov 2026; no images attached',
                 'extent': 'one ciphered message of December 1758 inside the file; number of leaves not stated',
                 'cipher': 'Archive description: "Empfehlungen diesbezüglich des Herrn Martinet (chiffrierte Mitteilung, teils entziffert, Môtiers-Travers, Dezember 1758)": the ciphertext is in the file and the contemporary decipherment covers only part of it.'},
        'prior_art': {
            'decode': DEC % '"Martinet", "Travers", "Neuchâtel", "Neuchatel"' + ' The only Neuchâtel hit is a picture postcard (record 3490).',
            'tomokiyo': TOM % 'Neuch, Martinet, Metternich, Dupuy',
            'lasry': 'No Lasry paper on Prussian Neuchâtel ciphers turned up in the two web searches below; his own list was not opened.',
            'edition': 'No edition of the Neuchâtel administrative files of 1758-59 found. Bourgeois, Neuchâtel et la politique prussienne en Franche-Comté (1887, archive.org full text opened) stops at 1713. The Politische Correspondenz prints Frederick\'s own letters, not incoming notes of local informants; its 1758-59 volumes were not opened.',
            'literature': 'Web searches on Martinet, Môtiers, 1758 and the Vattel/Pury/Perregaux affair returned only HLS biographies and Rousseau material, nothing on this message or its cipher.'},
        'key_check': 'No key held in the repo. The archive files a Neuchâtel "dictionnaire chiffré" of 1703 in Rep. 64 Nr. 944 and cipher notes in Nr. 777 and 962; none could be tried because nothing is online.',
        'key_held': 'GStA PK I. HA Rep. 64 Nr. 944 (cipher table sent 8 Nov 1703) and Nr. 777 ("Handhabung der Chiffrierung", 1742-48); not tested, not online.',
        'duplicates': 'known.py "Rep. 64", "Martinet", "Môtiers", "Montmollin": no hits in catalogue, leads, targets or sweeps.',
        'verdict': 'open',
        'searches': [
            {'query': 'DECODE RecordsList search: Martinet; Travers; Neuchâtel; Neuchatel', 'result': 'Martinet 0, Travers 0, Neuchâtel/Neuchatel one postcard (3490); no GStA record on DECODE'},
            {'query': 'Martinet Môtiers Val-de-Travers 1758 Neuchâtel Vattel Pury Perregaux gouverneur lettre chiffrée Berlin Geheimes Staatsarchiv Rep. 64', 'result': 'HLS Vattel articles, Rousseau at Môtiers, BPUN periodicals; nothing on Martinet or a cipher'},
            {'query': 'Neuchâtel 1758 1759 principauté prussienne correspondance chiffrée déchiffrement "Martinet" Travers Frédéric II gouverneur Keith édition', 'result': 'General histories of Prussian Neuchâtel and the Gaudot affair; no edition or decipherment of the message'},
            {'query': 'cryptiana.web.fc2.com/code/german.htm and frederick.htm, text search Neuch / Martinet', 'result': 'no mention'},
        ]}))

P64 = 'not vetted: Bourgeois 1887 (archive.org, opened) cites ciphered pieces of this series by content (e.g. "Montmollin à Wartemberg, 23 mars 1705 (en chiffres)"), so decipherments probably lie in the files; DECODE and Cryptiana searched 11 Nov 2026, nothing'
ROWS.append(row(
    1703, 'Jul 1703 - Dec 1708', 'Prussian succession at Neuchâtel: partly ciphered reports of the agents, files with no decipherment noted',
    'Marc Dupuy (Bern), brothers Bondeli, Jean-Scipion de Peyrol, Emer de Montmollin, Ernst von Metternich, F. W. Duncker → Frederick I / Wartenberg',
    'Bern / Neuchâtel / Regensburg', 'French / German', '1701-1800',
    'GStA PK, I. HA Rep. 64, Nr. 692, 693, 694, 707, 708, 709, 710, 715, 717, 944, 995',
    'eleven files; "Berichterstattungen (teils chiffriert)"; amount of cipher not given',
    'A', 'GStA finding aid says "teils chiffriert" for these files and, for the sibling files Nr. 695-706, "teils chiffriert mit Entzifferung"; '
    'Nr. 995 has "chiffrierte Briefe mit Dechiffrierung zwischen den Zeilen" (Jul-Sep 1706) beside reports of Mar-Apr 1707 "teils chiffriert". '
    'Whether the files without the note really lack a decipherment is not known. Key table of 1703 in Nr. 944.',
    'The secret side of the Prussian acquisition of Neuchâtel in the War of the Spanish Succession.', 3, 1, 2,
    'Order sample scans of Nr. 692 and 717; the interlined siblings (Nr. 695-706, 995) and the table in Nr. 944 should read any piece left in cipher. No vetting block: needs the files.',
    P64))
ROWS.append(row(
    1699, 'Aug 1698 - Nov 1701', 'Vrijbergen at the French court and Lubières at Orange: partly ciphered reports on William III\'s Orange estates',
    'Marinus van Vrijbergen (Paris, Versailles, Compiègne) and Governor Lubières (Orange) → Portland, Robethon, William III', 'Paris / Orange',
    'French', '1651-1700', 'GStA PK, I. HA Rep. 64, Nr. 935', '"Korrespondenz, teils chiffriert"; Lubières "gelegentlich chiffriert"', 'C',
    'GStA finding aid as quoted; no decipherment mentioned. Papers of William III\'s Orange administration that came to Berlin with the Orange inheritance.',
    'Dutch-English diplomacy at Versailles after Rijswijk, in William III\'s own cipher.', 3, 1, 3,
    'Order scans; compare with the William III / Portland ciphers on DECODE and in targets. No vetting block: Japikse\'s Correspondentie van Willem III en Bentinck was not opened.',
    'not vetted: DECODE search "Vrijbergen" 0 (11 Nov 2026); known.py "Vrybergen" no hits; Japikse edition not opened'))
ROWS.append(row(
    1716, '1716-1717', 'Adam Otto von Viereck\'s reports from Paris, partly ciphered (Sellentin\'s Paris legation file)',
    'Adam Otto von Viereck → Frederick William I', 'Paris', 'French / German', '1701-1800', 'GStA PK, I. HA Rep. 64, Nr. 959',
    'ff. 131, 167ff., 180, 185ff., 194-205 "teils chiffriert"', 'C', 'GStA finding aid gives the folios; no decipherment mentioned.',
    'Prussian negotiation with the Regency over the Orange inheritance.', 2, 1, 3, 'Order ff. 194-205.',
    'not vetted: known.py "Viereck" no hits; no edition searched'))
ROWS.append(row(
    1761, '1761-1762', 'Ciphered correspondence about the envoy Haude, alias Karl Adolf von Rexin, at Constantinople',
    'Frederick II / Kabinettsministerium ↔ Gottfried Fabian Haude ("von Rexin")', 'Constantinople / Berlin', 'French / German', '1701-1800',
    'GStA PK, I. HA Rep. 11 Akten, Nr. 10646', 'one file; old shelfmark Rep. 11 Nr. 275 d Fasz. 20', 'B',
    'GStA title: "Chiffrierte Korrespondenz betr. den Gesandten [Gottfried Fabian] Haude unter dem Namen Karl Adolf von Rexin in Konstantinopel". No decipherment mentioned; the neighbouring files Nr. 10647-10650 are the ordinary correspondence.',
    'The Prussian-Ottoman alliance negotiation of the Seven Years War.', 4, 1, 3,
    'Open Politische Correspondenz vols. 20-22 (archive.org politischecorre20sybegoog etc.) for the Rexin letters and their source notes; then order the file. No vetting block: that edition was not opened (download cut off).',
    'not vetted: DECODE search "Rexin" 0 (11 Nov 2026); Politische Correspondenz not opened'))
ROWS.append(row(
    1756, '1756', 'Three ciphered letters of Queen Luise Ulrike of Sweden to her brother Prince August Wilhelm of Prussia',
    'Luise Ulrike of Sweden → August Wilhelm of Prussia', 'Stockholm', 'French', '1701-1800', 'GStA PK, BPH, Rep. 56 I, J, Nr. 23',
    'three letters, filed with August Wilhelm\'s letters to her', 'C',
    'GStA finding aid: "Enthält auch: Drei chiffrierte Briefe der Königin Ulrike von Schweden an ihren Bruder." Year of the failed royalist coup in Stockholm. Related: catalogue row with VI. HA Nl Schweden, U. v., Nr. 3 (Frederick to Ulrike).',
    'The queen\'s own account of the 1756 coup attempt to her favourite brother.', 4, 1, 3,
    'Open Arnheim, Luise Ulrike, die schwedische Schwester Friedrichs des Großen, vol. 2 (Gotha 1910): not on archive.org. No vetting block until it is checked.',
    'not vetted: DECODE search "Ulrike" 0 (11 Nov 2026); Arnheim 1909-10 could not be opened'))
ROWS.append(row(
    1743, '28 Sep 1743', 'Ciphered cabinet order of Frederick II to Count Finck von Finckenstein at Copenhagen',
    'Frederick II → Karl Wilhelm Finck von Finckenstein', 'Berlin / Potsdam → Copenhagen', 'French', '1701-1800',
    'GStA PK, I. HA Rep. 81 Kopenhagen, Nr. 254', 'one order', 'B',
    'GStA title: "Kabinettsordre (chiffriert) an Graf Karl Wilhelm von Finck von Finckenstein", 28 Sept. 1743. Legation copy as received; cipher keys for the legation in Rep. 81 Kopenhagen Nr. 1 (c. 1735).',
    'Short, dated, with a legation key of the same decade in the same fonds.', 2, 1, 2,
    'Open Politische Correspondenz vol. 2 at 28 Sept. 1743 (probably printed from the draft); order the leaf and Nr. 1.',
    'not vetted: Politische Correspondenz vol. 2 not opened'))
ROWS.append(row(
    1790, 'Aug-Nov 1790', 'Spiridion Count Lusi: ciphered reports of autumn 1790',
    'Spiridion von Lusi → Frederick William II / Hertzberg', 'unknown', 'French', '1701-1800', 'GStA PK, VI. HA, FA Lusi, v., Nr. 3',
    'file of reports, "(chiffriert)"', 'C', 'GStA finding aid: reports during his mission, Aug.-Nov. 1790, "(chiffriert)". Full record not opened (search list only).',
    'Prussian diplomacy at the time of Reichenbach and Sistova.', 3, 1, 3, 'Read the full record; order sample leaves.',
    'not vetted: DECODE search "Lusi" gives only unrelated BL and KHA rows (11 Nov 2026)'))
ROWS.append(row(
    1811, '1810-1812', 'Kingdom of Westphalia: partly ciphered copies of legation reports and ciphered reports to the envoy in Berlin',
    'Westphalian foreign ministry ↔ envoys (Berlin: Baron von Linden)', 'Kassel / Berlin', 'French', '1801-1900',
    'GStA PK, V. HA Königreich Westphalen, Nr. 304 and Nr. 393', 'Nr. 304 "enth. nur: z.T. chiffrierte Abschriften"; Nr. 393 "chiffrierte Berichte an den westphälischen Gesandten in Berlin"',
    'B', 'GStA finding aid as quoted. The same fonds holds a Westphalian "Chiffrierbuch (Chiffre chiffrant et déchiffrant)", Nr. 541, undated.',
    'Napoleonic satellite diplomacy; the code book is in the same fonds.', 2, 1, 2, 'Order Nr. 541 with a sample of Nr. 304.',
    'not vetted: DECODE search "Westphal" gives unrelated rows; no edition searched'))
ROWS.append(row(
    1811, '1810-1813', 'Scharnhorst to Boyen: seven ciphered letters',
    'Gerhard von Scharnhorst → Hermann von Boyen', 'unknown', 'German', '1801-1900', 'GStA PK, VI. HA, Nl Boyen, H. L. L. G. v., d. Ä., Nr. 648',
    '23 letters to Boyen, four drafts, "sieben chiffrierte Schreiben"', 'C', 'GStA title as quoted; no decipherment mentioned.',
    'The reformers\' private channel before 1813.', 3, 1, 3,
    'Check Scharnhorst, Private und dienstliche Schriften (ed. Kunisch), vols. 6-8, which should print them; not opened, so no vetting block.',
    'not vetted: DECODE search "Scharnhorst" gives two postcards; Kunisch edition not opened'))
ROWS.append(row(
    1808, '1798, 1808', 'Wittgenstein papers: ciphered instruction on Ansbach-Bayreuth (1798) and Wittgenstein\'s ciphered letters to Stein (22 Oct 1808)',
    'Hardenberg / Berlin → Rastatt; Wilhelm Ludwig zu Sayn-Wittgenstein → Freiherr vom Stein', 'Berlin / Hamburg / Königsberg', 'German / French',
    '1801-1900', 'GStA PK, BPH, Rep. 192 Nl Wittgenstein, W. L. G. zu, VI, Nr. 2, 2 and I, Nr. 1, 16',
    'single pieces inside two files', 'C', 'GStA finding aid: "... 2.3.1798 (chiffriert)"; "Wittgenstein an Stein: chiffrierte Briefe, 22.10.1808". Sibling of the Stein letters at Cappenberg (catalogue: Niebuhr to Stein 1808).',
    'The Stein-Wittgenstein affair that brought Stein down.', 3, 1, 3, 'Check Botzenhart/Hubatsch, Stein Briefe und amtliche Schriften, vol. 2/2; order the leaves.',
    'not vetted: Stein edition not opened'))
ROWS.append(row(
    1524, '9 Oct 1524', 'Georg Klingenbeck to Grand Master Albrecht, partly in cipher (extends the Ordensbriefarchiv group, catalogue 557)',
    'Georg Klingenbeck → Albrecht of Brandenburg-Ansbach', 'unknown', 'German', '1497-1559', 'GStA PK, XX. HA, OBA, Nr. 27275',
    'one letter, "teilweise Chiffern"', 'B', 'Joachim-Hubatsch regest: "König Christiern; das evangelische Wesen (teilweise Chiffern)". No Auflösung noted; many sibling OBA letters of 1519-25 carry one.',
    'Adds one piece to the Teutonic Order cipher group already in the catalogue.', 2, 1, 2, 'Treat with catalogue 557; order with the others.',
    'not vetted separately: same series and literature as catalogue 557'))
ROWS.append(row(
    1798, '1798', 'Attempt to decipher the inscription in a ring of the Polish revolutionaries (South Prussia)',
    'Prussian South Prussia administration', 'Posen / Warsaw', 'Polish (probably)', '1701-1800', 'GStA PK, I. HA Rep. 7 C (Südpreußen), Nr. 3144',
    'one file', 'B', 'GStA title: "Versuch der Entzifferung eines in einem Ringe der revolutionären Polen stehenden ..." (title cut in the list). Sibling Nr. 3145 holds keys to the Polish insurgents\' ciphers.',
    'A Prussian cryptanalytic attempt of 1798 with the target text and, next door, the insurgents\' keys.', 2, 1, 3,
    'Read the full record; order both files.', 'not vetted: outcome of the 1798 attempt unknown'))
ROWS.append(row(
    1640, '1626-1661', 'Landgrave Georg II of Hesse-Darmstadt: partly ciphered letter about an answer of Generalwachtmeister Otto Christoph Sparr',
    'Georg II of Hesse-Darmstadt → unknown', 'Darmstadt / Gießen', 'German', '1611-1650', 'HStAD (Hessisches Staatsarchiv Darmstadt), D 4, Nr. 185/3',
    '414 microfilm openings online; the cipher letter was not located', 'C',
    'Arcinsys: "Teilweise chiffriertes Schreiben Georgs II. über ein Antwortschreiben des Generalwachtmeisters Otto Christoph Sparr". '
    'All 414 images fetched 11 Nov 2026 and paged on contact sheets of 40; at that size no cipher could be told from the script (opening 107 viewed large: plain German).',
    'Thirty Years War, Hesse-Darmstadt between the Emperor and Sweden.', 2, 3, 3,
    'Page the unit at full size: https://digitalisate-he.arcinsys.de/hstad/d_4/185--3/hstad_d_4_nr_185--3_000.jpg to _413.jpg.',
    'not vetted: cipher leaf not found; known.py "D 4 Nr. 185" no hits',
    label='Arcinsys HStAD D 4 Nr. 185/3', href='https://arcinsys.hessen.de/arcinsys/showArchivalDescriptionDetails.action?archivalDescriptionId=4672681',
    scan='no', access='Images free on Arcinsys Hessen (microfilm scans, double pages).',
    note='Scored from the Arcinsys description during the 11 Nov 2026 German sweep; images paged on contact sheets, cipher leaf not located'))

KEYS = [
    {'shelfmark': 'GStA PK, I. HA Rep. 64, Nr. 944', 'what': 'Neuchâtel "dictionnaire chiffré / table de chiffrement", enclosure to the rescript of 8 Nov 1703 (41x33 cm)', 'reads': 'the Rep. 64 Neuchâtel reports 1703-08', 'online': 'no'},
    {'shelfmark': 'GStA PK, I. HA Rep. 64, Nr. 962', 'what': 'Marc Dupuy\'s notes on encipherment ("Verschlüsselungen für die Chiffrierung"), 1702-07', 'reads': 'Dupuy\'s reports in Rep. 64', 'online': 'no'},
    {'shelfmark': 'GStA PK, V. HA Königreich Westphalen, Nr. 541', 'what': 'Westphalian Chiffrierbuch (chiffre chiffrant et déchiffrant), undated', 'reads': 'V. HA Nr. 304, 393', 'online': 'no'},
    {'shelfmark': 'GStA PK, I. HA Rep. 7 C, Nr. 3145', 'what': 'keys to the ciphers of the Polish revolutionaries, 1798', 'reads': 'Rep. 7 C Nr. 3144 and Polish insurgent letters', 'online': 'no'},
    {'shelfmark': 'GStA PK, I. HA Rep. 81 Kopenhagen, Nr. 1 and Nr. 4', 'what': 'legation ciphers c. 1735 and for Vincke 1768', 'reads': 'Rep. 81 Kopenhagen Nr. 254; LAV NRW W, V 105 Nr. 797', 'online': 'no'},
    {'shelfmark': 'GStA PK, I. HA Rep. 81 Warschau Ges., I, Nr. 1; Rep. 81 Rastatt Nr. 18; VI. HA Nl Stein, J. F. v., Nr. 3; VI. HA Nl Lucchesini Nr. 41; I. HA Rep. 96 Nr. 90 G',
     'what': 'further Prussian legation cipher books 1759-1797 found only in the GStA database', 'reads': 'Prussian legation ciphers (catalogue 588 Stein at Mainz and others)', 'online': 'no'},
]

if __name__ == '__main__':
    json.dump(ROWS, open(os.path.join(HERE, 'candidates.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    json.dump(KEYS, open(os.path.join(HERE, 'key_leads.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(len(ROWS), 'rows;', sum(1 for r in ROWS if 'vetting' in r), 'with vetting;', len(KEYS), 'key leads')
