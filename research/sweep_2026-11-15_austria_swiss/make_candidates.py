"""Builds candidates.json and key_leads.json for the Austria / Switzerland sweep of 15 Nov 2026.

Routes: archives-online.org (Chrome tab, form + SignalR results, 10 rows a page; date 1400-1920), findbuch.net front ends
(ooela, vla, landesarchiv-berlin: call the page's own do_rech_start_with_words(term) from the console and read the result tab),
Steiermark ArchivIS (UI form). Every row is scored from finding-aid text (seen: catalogue); none viewed.
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
SRC_AO = 'archives-online.org federated search (Chrome), Austria/Swiss sweep, 15 Nov 2026'
NOTE = ('Scored from the finding-aid text during the 15 Nov 2026 Austria/Swiss sweep '
        '(research/sweep_2026-11-15_austria_swiss/); not viewed')
AO_LINK = {'href': 'https://www.archives-online.org/Search', 'label': 'archives-online.org (search the shelfmark)'}


def dedupe(what):
    return ('open as far as checked (15 Nov 2026): ' + what + ' searched with known.py in catalogue.json, leads.json, decode_updates, '
            'every candidates.json / key_leads.json and the targets: not found; no web, Tomokiyo, Lasry or DECODE search made in this sweep')


def row(**k):
    base = dict(source=SRC_AO, score_note=NOTE, seen='catalogue', needs_archive_scan='yes', region='Central Europe')
    base.update(k)
    return base


C = []

C.append(row(
    year=1656, date='10 Dec 1655 - 15 Feb 1656', language='German', period='1651-1700',
    title="Ciphered correspondence between Luzern, Fribourg and Solothurn, Dec 1655 - Feb 1656 (key: the Catholic cantons' agreements on secret signs and ciphers, AKT 13/153)",
    correspondents='Luzern <-> Fribourg <-> Solothurn (Catholic cantons, in the run-up to the First Villmergen War)',
    place='Luzern / Fribourg / Solothurn',
    shelfmark='Staatsarchiv Luzern, AKT 13/2346 (key volume: AKT 13/153, 1568-1696)',
    folio_note="Title as indexed: 'Chiffrierte Korrespondenz zwischen den Orten Luzern, Freiburg und Solothurn (Schluessel siehe AKT 13/153)'. AKT 13/153 is 'Verabredungen der katholischen Orte ueber die geheimen Wortzeichen und Chiffren 1568-1696'",
    cls='A',
    status='Finding aid names the key volume. No edition or decipherment found in the sweep.',
    why="A ciphered letter file of 1655-56 with its key named in the same archive, from the Swiss Catholic cantons' diplomacy just before 1656. Same system as the Luzern key series AKT 13/152-158 (see key_leads.json).",
    importance=3, solvability=4, difficulty=3,
    verify='Open AKT 13/2346 and 13/153 at the Staatsarchiv Luzern (query database or reading room); check whether the key of 13/153 covers 1655 or only the earlier agreements; compare the Zurich Ziffernschrift keys of 1653 (swiss_austrian) and StAZH A 235.2 (1655, "mit 3 Chiffrierschluesseln").',
    links=[AO_LINK], prior_art=dedupe('AKT 13/2346, AKT 13/153, Luzern, Geheimkonferenz'),
    access_note='description on archives-online.org (federated StALU data); no image route found (query.staatsarchiv.lu.ch does not resolve from this machine); order from the archive'))

C.append(row(
    year=1712, date='1711-1712 (key made 1708)', language='German / French', period='1701-1800',
    title="Secret conference of Luzern, Fribourg, Solothurn and the Valais at Solothurn, 1711-12, 'teilweise chiffriert' (key: Geheimschluessel of 1708, Luzern COD 1100; same code in the Valais as 'Alphabet secret')",
    correspondents='Luzern, Fribourg, Solothurn, Valais (Catholic cantons and the Valais, Toggenburg War period)',
    place='Solothurn',
    shelfmark='Staatsarchiv Luzern, FAA 763 (key: COD 1100, 9 folios, 1708; Valais copy AEV AV 54/7)',
    folio_note="FAA 763: 'Abschied einer Geheimkonferenz ... zu Solothurn (teilweise chiffriert) 1711-1712'. COD 1100: 'Geheimschluessel zwecks Aufloesung von chiffrierten Dokumenten militaerischen Charakters ... geltend fuer die Staende Luzern, Freiburg und Solothurn. Angefertigt 1708 (Villmergerkriege?)', 1-9 fol. AEV AV 54/7: 'Alphabet secret (code) partage par les cantons catholiques de Lucerne, Fribourg, Soleure et par la Republique du Valais', frontispiece with the arms of the four allies",
    cls='A',
    status='Finding aids name three copies of one code. No decipherment found in the sweep.',
    why='A short 1711-12 ciphered conference record with a dated key (1708) held in the same archive, and a second key copy in Sion: a clean key-plus-ciphertext pair, small enough to read.',
    importance=3, solvability=4, difficulty=2,
    verify='Order FAA 763 and COD 1100 (Luzern); look at AEV AV 54/7 on the Valais site; check the key covers the 1711 Abschied (the key was made for war-time military papers).',
    links=[AO_LINK], prior_art=dedupe('FAA 763, COD 1100, AV 54/7, Alphabet secret, Geheimschluessel'),
    access_note='descriptions only (archives-online.org); Luzern and Sion images not checked'))

C.append(row(
    year=1745, date='Jan - Feb 1745', language='French', region='France', period='1701-1800',
    title="Minister d'Argenson to Maurice de Courten: ciphered memoranda on his mission to Frederick II of Prussia, 13-17 Jan 1745, several 'mis en clair' (7 units)",
    correspondents="Marc-Pierre d'Argenson (French minister of war) -> Maurice de Courten (Swiss colonel in French service, mission to the King of Prussia)",
    place='Versailles -> Prussia',
    shelfmark='Archives de l\'Etat du Valais (AEV), fonds de Courten, Cn B 5/3/5, 5/3/5bis, 5/3/5ter, 5/3/6, 5/3/6bis, 5/3/8, 5/3/10',
    folio_note="'Memoire chiffre pour le comte de Courten' (5/3/5, 13 Jan 1745) with two cleartext units ('mis en clair', 5/3/5bis and 5/3/5ter); 'Memoire militaire chiffre du ministre d'Argenson' (5/3/6, 17 Jan, and 5/3/6bis); two letters 'en partie chiffree' (5/3/8, 5/3/10, 28 Feb 1745)",
    cls='A',
    status='Finding aid lists cipher/clear pairs. No publication of the pairs found in the sweep.',
    why="Three ciphered memoranda each filed beside its cleartext, from one correspondent to one recipient in one month: the pairs give the French 1745 cipher directly, with no outside key needed. The same fonds holds the 1757 Choiseul dispatches (next row).",
    importance=4, solvability=5, difficulty=2,
    verify='Look at Cn B 5/3/5, 5/3/5bis and 5/3/5ter first (cipher and two clear versions); check whether the clear is a contemporary decipherment or a draft; check whether the French ministry cipher of 1745 is known from DECODE keys.',
    links=[AO_LINK], prior_art=dedupe('de Courten, Cn B 5/3, Argenson'),
    access_note='descriptions on archives-online.org (AEV data); images not checked; the fonds is described on the AEV site'))

C.append(row(
    year=1757, date='Dec 1757', language='French', region='France', period='1701-1800',
    title="Duke of Choiseul's ciphered dispatches to Maurice de Courten, 1757, deciphered by Courten (partly) (2 units)",
    correspondents='duc de Choiseul (as indexed; which Choiseul is not stated) -> comte Maurice de Courten',
    place='unknown -> Valais',
    shelfmark='AEV, fonds de Courten, Cn B 5/11/6 (4 Dec 1757) and Cn B 5/11/7 (first part missing)',
    folio_note="5/11/6: 'Depeche chiffree du duc de Choiseul et en partie dechiffree par le comte Maurice de Courten' (content: Prussian king weakened by the loss of Bevern, Breslau and 16,000 men, i.e. 4 Dec 1757); 5/11/7: 'Depeche chiffree ... dont la premiere partie manque, et dechiffree par le comte ...'",
    cls='A',
    status='Finding aid says a contemporary (partial) decipherment is on the sheet.',
    why='Seven Years War ciphered dispatches with the recipient\'s own decipherment, giving a crib per dispatch; the cipher of Choiseul in 1757 is not a standard ministry table.',
    importance=3, solvability=4, difficulty=2,
    verify="Open both units; see whether the decipherment is interlinear; compare Choiseul's cipher with the Bernis letter of the same period (Cn B 5/10/8, not described as ciphered).",
    links=[AO_LINK], prior_art=dedupe('de Courten, Cn B 5/11, Choiseul'),
    access_note='descriptions only; images not checked'))

C.append(row(
    year=1704, date='9 Jan 1704', language='French', region='France', period='1701-1800',
    title="Marquis de Torcy to Jean Etienne de Courten: letter 'en partie chiffree' about Colonel Reding's proposals from the Duke of Savoy, 1704",
    correspondents='Jean-Baptiste Colbert, marquis de Torcy -> Jean Etienne de Courten (1653-1723, Swiss colonel in French service)',
    place='Versailles -> Valais', shelfmark='AEV, fonds de Courten, Cn B 10/1/8',
    folio_note='One letter, partly ciphered; no key or cleartext mentioned in the finding aid',
    cls='B', status='Single partial-cipher letter.',
    why='A second French ministry hand (Torcy) in the Courten fonds; weak alone, useful with the 1745 and 1757 pairs for French cipher habits.',
    importance=2, solvability=2, difficulty=3,
    verify='View the letter; check whether a decipherment is written between the lines.',
    links=[AO_LINK], prior_art=dedupe('Cn B 10/1/8, Torcy Courten'),
    access_note='description only'))

C.append(row(
    year=1802, date='1801-1803', language='German / French', region='Central Europe', period='1801-1900',
    title="Abbot Pankraz Vorster of St Gallen and Hofrat Peter Mueller (Paris): letters 'in Geheimschrift', 1801-03 (3 units)",
    correspondents='Fuerstabt Pankraz Vorster <-> Hofrat Peter Mueller (agent of the abbey in Paris)',
    place='St Gallen / Paris',
    shelfmark='Stiftsarchiv St. Gallen, Nachlass Pankraz Vorster, Nr. 203-002 (19 Sep 1801), 358-002 (26 Dec 1801), 868-001 (9 Mar 1803)',
    folio_note="Titles: 'Hofrat Peter Mueller an Fuerstabt Pankraz Vorster (in Geheimschrift)' (203-002), 'Brief in Geheimschrift von Hofrat Peter Mueller an Fuerstabt Pankraz Vorster' (358-002), 'Abt Pankraz an Hofrat Mueller in Paris (in Geheimschrift)' (868-001); Nr. 70 'Directorium S. Gallense' 1798 also hit 'Entzifferung'",
    cls='B', status='Three letters in secret writing, both directions; no key in the finding aid.',
    why="The St Gallen abbot's correspondence with his Paris agent after the abbey's 1798 dissolution, letters in both directions, so a two-way key can be tested; the Vorster Nachlass is digitised at the Stiftsarchiv in part.",
    importance=3, solvability=3, difficulty=3,
    verify='Check whether the Stiftsarchiv images exist for Nr. 203, 358 and 868; look for plaintext copies in the same Nachlass (Mueller\'s letters may exist in clear in the Directorium files); search the Vorster key in the Nachlass.',
    links=[AO_LINK], prior_art=dedupe('Vorster, Peter Mueller, Geheimschrift St. Gallen'),
    access_note='description on archives-online.org (Stiftsarchiv St. Gallen); image availability not checked'))

C.append(row(
    year=1515, date='Jan-Feb 1515 (dated 1515 [1516])', language='Italian', region='Italy', period='1497-1559',
    title="Francesco Vettori, Florentine ambassador at Lyon, to Lorenzo de' Medici: two letters 'groesstenteils chiffriert', one with Klarschrift, 1515 (Swiss Federal Archives copies)",
    correspondents="Francesco Vettori -> Lorenzo de' Medici (the younger)",
    place='Lyon -> Florence',
    shelfmark='Schweizerisches Bundesarchiv, J1.58#1977/70#72 (25 Feb 1515, mit Klarschrift) and #73 (29 Jan 1515, ohne Klarschrift)',
    folio_note="'Orig., ital., groesstenteils chiffriert [mit Klarschrift], vgl. unten' (#72) and '[ohne Klarschrift]' (#73); the same J1.58 collection also has #118, Jo. Cynthius for Tricarico to Lorenzo, 18 Sep 1515, teils chiffriert (next row). The finding aid says 'Orig.' but the collection is probably a Swiss-history gathering of Italian documents; its provenance is not checked",
    cls='A',
    status='Cipher plus an accompanying clear version for one of the two letters; the collection is a Swiss-history gathering, not the Florentine Mediceo, so the physical origin is unclear.',
    why="Vettori's Lyon letters of 1515 (the Marignano year) in cipher, one with its Klarschrift, so the Medici cipher of that legation can be rebuilt from the pair and tested on the second letter.",
    importance=4, solvability=4, difficulty=2,
    verify="Open J1.58#1977/70 #72 and #73 on the Federal Archives' scopeArchiv; check what J1.58 is; compare Vettori's Medici-letter editions (Legazione in Francia) and ASF Mediceo avanti il Principato ciphers (leads 1243 and Medici 1515 keys).",
    links=[{'href': 'https://www.recherche.bar.admin.ch/', 'label': 'Swiss Federal Archives search (J1.58#1977/70#72, #73)'}, AO_LINK],
    prior_art=dedupe('Vettori, J1.58, 1977/70, Cynthius, Tricarico'),
    access_note='description via archives-online.org; the Federal Archives site not checked for scans'))

C.append(row(
    year=1515, date='18 Sep 1515', language='Italian', region='Italy', period='1497-1559',
    title="Jo. Cynthius for Tricarico to Lorenzo de' Medici: letter from the French camp near Milan, 18 Sep 1515, 'teils chiffriert'",
    correspondents="Jo. Cynthius (for Tricarico) -> Lorenzo de' Medici",
    place='camp near Milan (Marignano) -> Florence',
    shelfmark='Schweizerisches Bundesarchiv, J1.58#1977/70#118',
    folio_note="'ex castris Christianissime maiestatis prope Mediolanum ad tria miliaria', 'Orig., ital., teils chiffriert'",
    cls='B', status='Single partly ciphered letter written days after the battle of Marignano.',
    why='A cipher letter from the French camp in the week of Marignano; companion of the Vettori pair in the same collection (different correspondent, own key).',
    importance=3, solvability=2, difficulty=3,
    verify='View the letter; check whether Tricarico (Neapolitan) used a Medici key already known.',
    links=[AO_LINK], prior_art=dedupe('J1.58, Cynthius'),
    access_note='description only'))

C.append(row(
    year=1660, date='1660', language='German', region='Central Europe', period='1651-1700',
    title="Johann Maximilian Graf von Lamberg: letter to/from Emperor Leopold I 'nebst Chiffrenschluessel', 1660 (2 pieces)",
    correspondents='Johann Maximilian von Lamberg (1608-1682, imperial envoy) <-> Emperor Leopold I',
    place='Vienna / Steyr area (Lamberg estate)',
    shelfmark='Oberoesterreichisches Landesarchiv Linz, Herrschaftsarchive, Bestand 06.S06.04.01 (Korrespondenz und diverse Schriften), Akt Nr. 406 (Faszikel 24, Schachtel 1235)',
    folio_note="'Brief an/von Kaiser Leopold I. nebst Chiffrenschluessel', 2 Stueck, 1660. The same Bestand: Akt Nr. 200 (1644, 21 Stueck, Faszikel 12): 'die Kunst der Geheimschrift' (probably a treatise, not a cipher letter)",
    cls='A', status='Key filed with the letter in the finding aid. Lamberg\'s Madrid reports (1656-60) are catalogue entries; this family-estate file is not held.',
    why='A letter between the Emperor and a diplomat with the cipher key attached, in the Lamberg family papers: a key and ciphertext pair in a private Herrschaft archive, in the year of the Peace of the Pyrenees aftermath. Two pieces only, so quick to read.',
    importance=3, solvability=4, difficulty=2,
    verify="Order Akt Nr. 406 (Linz, Digitalisate not stated); compare the key with the Lamberg conclave nomenclator DECODE R1270 and the Lamberg-to-Poetting letters of 1666-67 in AIS (catalogue); check whether Nr. 200 holds a cipher manual of the same hand.",
    links=[{'href': 'https://www.ooela.findbuch.net/php/main.php', 'label': 'OOe Landesarchiv findbuch (search Chiffrenschluessel; result 06.S06.04.01 : 406)'}],
    prior_art=dedupe('Lamberg, Chiffrenschluessel, 06.S06.04.01'),
    source='ooela.findbuch.net (Chrome console call of do_rech_start_with_words), Austria/Swiss sweep, 15 Nov 2026',
    access_note='description on the OOeLA findbuch; no scan indicated'))

C.append(row(
    year=1751, date='1751', language='French', region='France', period='1701-1800',
    title="Jean-Jacques Rousseau to Mme Dupin de Francueil: two copies of a ciphered letter, 1751",
    correspondents='J.-J. Rousseau -> Suzanne Dupin de Francueil (nee Bollioud de Saint-Julien)',
    place='Paris', shelfmark='Bibliotheque publique et universitaire / Bibliotheque de Neuchatel (Fonds Rousseau), 102MsR-172.1 and 102MsR-172.2',
    folio_note="'Copie d'une lettre chiffree de Jean-Jacques Rousseau a Suzanne Dupin de Francueil': two copies of one letter; the edition (Leigh, Correspondance complete) may print a decipherment, not checked",
    cls='C', status='Copies of a ciphered letter; a published reading is likely (Rousseau letters are heavily edited) but was not checked.',
    why='A cipher letter of a famous correspondent in a well-catalogued fonds; weak because a reading probably exists in the Leigh edition.',
    importance=2, solvability=3, difficulty=2,
    verify="Search Leigh's Correspondance complete (1751 letter to Mme Dupin de Francueil) for the cipher and any decipherment note before anything else.",
    links=[AO_LINK], prior_art='not checked beyond the ledgers (15 Nov 2026): known.py Rousseau, Dupin and Francueil found nothing; the Leigh edition and Rousseau scholarship were not searched',
    access_note='description only'))

C.append(row(
    year=1767, date='1767', language='French', region='France', period='1701-1800',
    title="Jean-Jacques Rousseau to Louis-Francois de Bourbon, prince de Conti: two letters of 1767 indexed with 'dechiffrement' (Fonds Rousseau, Neuchatel)",
    correspondents='J.-J. Rousseau -> Prince de Conti',
    place='Trye / Paris', shelfmark='Neuchatel public library, 102MsR-101.15 and 102MsR-101.16',
    folio_note="Hit on 'dechiffrement'; the title shown is only 'Lettre de Jean-Jacques Rousseau a Louis-Francois de Bourbon prince de Conti, 1767'. Whether the letters are ciphered or a clear text was read is not shown",
    cls='C', status='Unclear; probably a note that Conti\'s office deciphered or that Rousseau used a cipher name.',
    why='Rousseau and Conti exchanged letters under cover in 1767 (Trye); if the letters are ciphered, there may be a key in the same fonds.',
    importance=2, solvability=2, difficulty=3,
    verify='Open the two records in the Neuchatel catalogue; read the notes field for "dechiffrement".',
    links=[AO_LINK], prior_art='not checked (15 Nov 2026): no ledger mention of Rousseau-Conti; Leigh edition not searched',
    access_note='description only'))

C.append(row(
    year=1850, date='c. 1850s', language='German', region='Central Europe', period='1801-1900',
    title="Schaffhausen: key to a secret writing of identical letter symbols, with examples, found with a diarist's papers (the key does not fit the diaries' own secret writing)",
    correspondents='unknown diarist (Schaffhausen)', place='Schaffhausen',
    shelfmark='Staatsarchiv Schaffhausen, Kultur II 67/246',
    folio_note="'Schluessel zu einer auf zumeist identischen Buchstabensymbolen basierender Geheimschrift, mit Beispielen; der Schluessel scheint jedoch nicht auf die Geheimschrift in den Tagebuechern anwendbar, da dort andere Symbole verwendet werden'",
    cls='C', status="Archivist's note: the diaries are in a different secret script from the key's.",
    why="Secret-script diaries (19th century) whose own key is lost: a diary of unknown length in an unrecorded symbol cipher, and a separate key for another script.",
    importance=2, solvability=2, difficulty=4,
    verify='Find the diary series next to Kultur II 67 and see how many pages are in the secret script; look for a clear fair copy.',
    links=[AO_LINK], prior_art=dedupe('Kultur II 67, Schaffhausen Geheimschrift'),
    access_note='description only; diary volume numbers not read'))

C.append(row(
    year=1620, date='5 Jun 1618 - 30 Aug 1622', language='German', region='Central Europe', period='1611-1650',
    title="Hohenems archive: Graubuenden affairs 1618-22 (Ulrich von Ramschwag, Kaspar von Hohenems), a hit on 'Geheimschrift' in a very long summary",
    correspondents='Ulrich von Ramschwag; Kaspar Graf zu Hohenems; the Three Leagues; Glarus; Zurich',
    place='Hohenems / Graubuenden', shelfmark='Vorarlberger Landesarchiv, Herrschaftsarchiv Hohenems (A.05 - HoA), HoA 138,24',
    folio_note="The word 'Geheimschrift' occurs somewhere in a summary of about 1,500 characters (not read in full); the context (a cipher letter, a key, or a report of a secret script) was not seen",
    cls='C', status='Hit on a keyword in a long regest; no cipher text confirmed.',
    why='Hohenems correspondence in the Bundner Wirren (1618-22); a cipher letter here would be tied to the Spanish-Austrian side and could use the Hohenems key.',
    importance=2, solvability=2, difficulty=3,
    verify='Read the whole regest on vla.findbuch.net (search Geheimschrift, result HoA 138,24) and see which letter is meant.',
    links=[{'href': 'https://www.vla.findbuch.net/php/main.php', 'label': 'Vorarlberger Landesarchiv findbuch (search Geheimschrift)'}],
    prior_art=dedupe('HoA 138,24, Hohenems, Ramschwag'),
    source='vla.findbuch.net (Chrome console call of do_rech_start_with_words), Austria/Swiss sweep, 15 Nov 2026',
    access_note='description on the VLA findbuch'))

# the three Courten pair/1745 etc. already single rows. Key-only leads follow.
K = [
    dict(title="Luzern key series of the Catholic cantons: 'Chiffren' for Spain (1594), Lorraine (1592), Savoy (1579-1603), France and the Duke of Guise (1585-93), the Count of Champlitte (before 1600), plus the 1568-1696 agreements on secret signs",
         shelfmark="Staatsarchiv Luzern, AKT 13/152 (Verschleierungen, Abkommen Luzern-Freiburg-Solothurn), 13/153 (1568-1696), 13/154 (Lorraine 1592), 13/155 (France/Guise 1585-93), 13/156 (Savoy, Chabod and Lambert 1579-1603), 13/157 (Spain 1594), 13/158 (Champlitte); AKT 13/2229 (1609 renewal); FAA 869 (c. 1700); COD 1100 (1708 Geheimschluessel)",
         note="Seven consecutive AKT 13 units that are cipher keys, each for a named correspondent. None of these numbers is in any ledger. They would key Luzern's letters to the Spanish, Lorraine, Savoyard and French envoys in AKT 13 and the Savoy/Spain correspondence held elsewhere (Simancas Estado Suiza; Savoy archives). Found through archives-online.org (Chiffren, Wortzeichen)."),
    dict(title="Valais 'Alphabet secret (code)' shared by Luzern, Fribourg, Solothurn and the Valais, 1708",
         shelfmark='Archives de l\'Etat du Valais, AEV AV 54/7',
         note="Copy of the 1708 four-canton code with a frontispiece of the allies' arms and the Latin motto 'Nodus iste nec gladio...'. Pairs with Luzern COD 1100 (same year). Key for the 1711-12 FAA 763 row."),
    dict(title="Vorarlberg 'Geheimschrift, Arkana, Chiffrierungsschluessel' (undated bundle)",
         shelfmark='Vorarlberger Landesarchiv, A.03 VOKA AN 629',
         note="Undated bundle in the Vorarlberg Kreisamt (VOKA) holdings, title only. Not seen; could be a key set for the Austrian administration of the Vorlande."),
    dict(title="Graubuenden: Chiffrierschluessel (list and code names) in French, written by Friedrich Planta, 18th century",
         shelfmark='Staatsarchiv Graubuenden, Familienstiftung von Planta, D III S/II Ac.64 (1 sheet)',
         note="A French cipher list with code names, 18th century. Planta correspondence (Chur, Salis) is not in the ledgers; key only."),
    dict(title="Swiss Federal Archives: 'Chiffrierschluessel fuer die schweizerischen Auslandvertretungen' 1896; 'Drucksachen betr. Geheimschrift' 1889; 'chiffrierte Passeintragungen' 1889",
         shelfmark='Schweizerisches Bundesarchiv, E2001A#1000/45#61; E27#1000/721#10043; E2200.257A#1000/400#32',
         note="Late 19th-century key and regulation files of the Swiss foreign service. Possible key for Swiss legation telegrams; the files may be closed or unscanned (not checked)."),
]

with open(os.path.join(HERE, 'candidates.json'), 'w', encoding='utf-8') as f:
    json.dump(C, f, ensure_ascii=False, indent=1)
with open(os.path.join(HERE, 'key_leads.json'), 'w', encoding='utf-8') as f:
    json.dump(K, f, ensure_ascii=False, indent=1)
print(len(C), 'candidates', len(K), 'key leads')
