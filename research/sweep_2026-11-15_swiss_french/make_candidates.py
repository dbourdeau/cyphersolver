"""Builds candidates.json and key_leads.json for the French-language Swiss pass of 15 Nov 2026.
Routes: Fribourg friXplore (archives.fr.ch, server-rendered results), Vaud DAVEL (davel.vd.ch, scopeArchiv form post),
BGE Geneve (archives.bge-geneve.ch), archives-online.org (Chrome console driving), e-manuscripta (fetch).
Every row is scored from finding-aid text (seen: catalogue); none viewed as an image."""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
NOTE = 'Scored from finding-aid text during the 15 Nov 2026 French Swiss pass (research/sweep_2026-11-15_swiss_french/); not viewed'
FR = {'href': 'https://archives.fr.ch/search/results', 'label': "friXplore, Archives de l'Etat de Fribourg (search 'lettre chiffree', cote Affry)"}
DV = {'href': 'https://davel.vd.ch/volltextsuche.aspx', 'label': 'DAVEL, Archives cantonales vaudoises (full text search)'}
BG = {'href': 'https://archives.bge-geneve.ch/archive/recherche/touslesfonds/n:96', 'label': 'Bibliotheque de Geneve, archives (search)'}
AO = {'href': 'https://www.archives-online.org/Search', 'label': 'archives-online.org (search the shelfmark)'}
PRIOR_AFFRY = ('open as far as checked (15 Nov 2026): "Affry (de Boccard)", "archives.fr.ch", "friXplore" and "AEF Affry" searched with known.py: no hit. '
               "Related targets affry1757 and affry1757c (d'Affry to Stainville, R1071) exist but cite only the Nationaal Archief and Lyonet decipherments; "
               'no web, Tomokiyo, Lasry or DECODE search made')


def dd(what):
    return ('open as far as checked (15 Nov 2026): ' + what + ' searched with known.py in the ledgers, leads, sweeps and targets: not found; '
            'no web, Tomokiyo, Lasry or DECODE search made in this sweep')


def row(**k):
    base = dict(score_note=NOTE, seen='catalogue', needs_archive_scan='yes', region='France')
    base.update(k)
    return base


def affry(year, date, series, title, corr, folio, cls, status, why, imp, sol, diff, verify, period='1701-1800'):
    return row(source='archives.fr.ch friXplore (Chrome), French Swiss pass, 15 Nov 2026', year=year, date=date, language='French',
               region='France', period=period, title=title, correspondents=corr, place='Versailles / Paris -> The Hague',
               shelfmark="Archives de l'Etat de Fribourg (AEF), Affry (de Boccard) " + series, folio_note=folio, cls=cls, status=status, why=why,
               importance=imp, solvability=sol, difficulty=diff, verify=verify, links=[FR], prior_art=PRIOR_AFFRY,
               access_note='friXplore lists no digital images for the Affry pieces (Multimedias: none); needs the AEF reading room or a reproduction order')


rows = []
rows.append(affry(1756, '1755-1757', '225.x', "Rouille's ciphered dispatches to d'Affry at The Hague with transcriptions, 1755-57 (42 units)",
    "Antoine-Louis Rouille (French foreign minister) -> Louis-Auguste Augustin d'Affry (French ambassador at The Hague)",
    'Series 225 (about 42 units, 1755-57): titles begin "Transcription de la depeche chiffree d\'Antoine-Louis Rouille ...". Dispatches and their transcriptions appear to be filed as separate pieces',
    'A', 'Finding aid: each unit is a transcription of a ciphered dispatch. No publication or decipherment of the series found in this sweep. Whether the transcription is contemporary or modern is not stated',
    "A long run of one minister's ciphered dispatches to one ambassador with transcriptions beside them: a key can be rebuilt from pairs. Same correspondent pair as the ten sibling d'Affry letters of inv. 192 (affry1757, deciphered in part with a key rebuilt from Lyonet), so a second source for that key",
    4, 4, 2, 'Open 225.1 and one transcription; check that cipher and transcription are both on file; compare the code with affry1757 (Rouille/Bernis 1757-58) and with Nationaal Archief 1.01.50 inv. 192'))
rows.append(affry(1758, '1757-1758', '226.x', "Bernis's dispatches to d'Affry at The Hague, 1757-58, ciphered with transcriptions (23 units)",
    "Abbe de Bernis (secretaire d'Etat des Affaires etrangeres) -> Louis-Auguste Augustin d'Affry",
    'Series 226 (23 units, 1757-58); the units surfaced for the terms chiffre / transcription; which are ciphered was not read',
    'A', 'Finding aid: letters of Bernis in the cipher series; transcriptions not read. No decipherment found',
    'Bernis succeeded Rouille in 1757; affry1757 holds Bernis letters of inv. 192 deciphered in part, so this series gives pairs for the same cipher period and a check on that key',
    4, 4, 2, 'Open 226.1 and 226.10; see which pieces are ciphered and whether transcriptions sit next to them; compare with affry1757'))
rows.append(affry(1760, '1759-1762', '227.x, 228.x', "Choiseul's ciphered dispatches to d'Affry at The Hague with 'Decryptage' and 'Transcription' pieces, 1759-62 (about 60 units)",
    "Duke of Choiseul (Stainville; Choiseul-Praslin 1762) -> Louis-Auguste Augustin d'Affry",
    '227.273 and 227.293 "Decryptage de la lettre chiffree du 17 fevrier / 17 mars 1760"; 227.339 "Decryptage de la depeche chiffree no 209 du duc de Choiseul" (24 Apr 1760); 227.302 (no 201), 227.362 (no 213, 10 May 1760); 227.465 "Document entierement chiffre" (c. 1760); 228 (1762, Choiseul-Praslin no 320). Dispatch numbers 201-261 are filed',
    'A', 'Finding aid names decipherments ("Decryptage") and transcriptions of numbered ciphered dispatches. No publication found',
    'Numbered dispatches (nos 201-320) with their decipherments in one fonds; the "Premier chiffre remis par le duc de Choiseul et le chancelier du Muy" (280.210) is filed in the same fonds and may be the key. A deciphered run in a Seven Years War code with the key probably on file',
    5, 4, 2, 'Open 227.273 (cipher and decryptage), 227.339 and 280.210; check whether 280.210 is the key to these dispatches; compare with Valais Cn B 5/11/6-8 (Choiseul to Courten, 1757)'))
rows.append(affry(1757, '1757-1760', '257.x, 259.x', "Stainville's (Choiseul's) ciphered dispatches from Vienna to d'Affry, 1757-60 (about 9 units)",
    "Comte de Stainville, later duke of Choiseul (French ambassador at Vienna) -> Louis-Auguste Augustin d'Affry",
    '257.6 "Depeche chiffree" 23 Sep 1757; 257.10 en partie chiffree 5 Nov 1757; 257.14, 257.18 (30 Jul 1758, clear), 257.28 (21 Oct 1758, Choiseul); 259 (1759-60, comte de Choiseul, en partie chiffree)',
    'A', "Finding aid: ciphered dispatches of Stainville to d'Affry; transcription status not stated. The catalogue holds d'Affry's 7 Aug 1757 intercept to Stainville (R1071, code C, no key): this is the reverse direction",
    "Stainville is the addressee of the unread d'Affry intercept of Aug 1757 (affry1757c); his own ciphered dispatches to d'Affry, perhaps with clear versions, may carry the code of that correspondence pair",
    4, 3, 3, 'Open 257.6 and 257.10; check for transcriptions and whether the code matches R1071 (affry1757c) or the Lyonet key (affry1757)'))
rows.append(affry(1757, '1757', '238.x', "Marshal d'Estrees's ciphered letters to d'Affry, May-June 1757, with transcriptions (20 units)",
    "Marshal Louis Le Tellier, duc d'Estrees (commander of the army of Germany, Hastenbeck campaign) -> Louis-Auguste Augustin d'Affry",
    '238.17 (15 May), 238.27 (30 May), 238.30 (1 Jun), 238.43 (24 Jun 1757) etc.: "Transcription du chiffre de la lettre du marechal d\'Estrees du ..."',
    'A', "Finding aid: transcriptions of the ciphered parts of Estrees's letters, dated one by one. No decipherment published found",
    'Army-commander cipher of the Hastenbeck campaign with the transcribed cipher parts filed in the same series; Richelieu (239), Clermont (240), Contades (241), Broglie (242), Soubise (243) follow in the same way (see key_leads.json)',
    4, 4, 2, 'Open 238.17 and its transcription; check whether the letters are cipher plus transcription pairs; the other commanders may share the war-office cipher'))
rows.append(affry(1759, '1759', '244.x', "Conflans d'Armentieres's letters to d'Affry, 1759, with transcriptions of the cipher (19 units)",
    "Louis de Conflans, marquis d'Armentieres -> Louis-Auguste Augustin d'Affry",
    'Series 244 (19 units, 1759): "Transcription du chiffre de la lettre de Louis de Conflans d\'Armentieres ..."',
    'A', 'Finding aid: transcriptions of the ciphered passages. Nothing published found',
    'One writer, 19 dated ciphered letters with transcriptions: the largest single-writer pair set after the ministers series',
    3, 4, 2, 'Open 244.1; check cipher and transcription are both on file'))
rows.append(affry(1759, '1758-1760', '266.x', "Ogier's partly ciphered letters to d'Affry, 1758-60 (28 units)",
    "M. Ogier -> Louis-Auguste Augustin d'Affry (Ogier's post is not named in the finding aid text read)",
    'Series 266 (28 units), "Lettre partiellement chiffree de M. Ogier a Louis-Auguste Augustin d\'Affry", 266.22 and 266.40 (18 Jul 1758) among them; the cipher passages are partial',
    'B', 'Finding aid: letters partly in cipher; no transcription named in these titles',
    'A diplomat-to-ambassador cipher over two years; a shared 1758-60 French diplomatic code may let the Choiseul/Affry pairs of series 227 and 257 act as the key',
    3, 3, 3, 'Open 266.22; see whether a transcription or key is filed; test the code against series 227 decipherments'))
rows.append(affry(1759, '1758-1760', '267.x', "Marquis d'Havrincourt's ciphered letters to d'Affry from Stockholm, 1758-60 (45 units)",
    "Louis de Cardevacque, marquis d'Havrincourt (French ambassador at Stockholm, as the finding aid names him) -> Louis-Auguste Augustin d'Affry",
    'Series 267 (45 units), e.g. 267.21 (20 Jun 1758): "Lettre chiffree du marquis d\'Havrincourt a d\'Affry"',
    'B', 'Finding aid: letters in cipher; no transcription named. 268.19 "Decryptage du chiffre de la lettre du 10 septembre 1758" sits next to this run and may belong to it',
    '45 ciphered letters from one writer in one code over 2 years: a good ciphertext-only target by length, and 268.19 is a decipherment filed beside them',
    4, 3, 3, 'Open 267.21 and 268.19; check whether 268.19 deciphers an Havrincourt letter; look for a key in 280.x'))
rows.append(row(source='davel.vd.ch DAVEL (Chrome fetch), French Swiss pass, 15 Nov 2026', year=1735, date='1730-1739', language='French',
    period='1701-1800', region='England',
    title='Comte de Marsay (British envoy) with members of the British Cabinet, 1730-39: some letters in cipher, "le code est dans le lot" (96 pieces)',
    correspondents='Armand-Louis de Saint-George, comte de Marsay (1680-1762), envoy of the King of Great Britain <-> members of the British Cabinet (Newcastle is not named in the finding aid)',
    place='unknown <-> London', shelfmark='Archives cantonales vaudoises (ACV), P de Mestral III 484 (davel.vd.ch, ID 723222)',
    folio_note='Dossier of 96 pieces in one envelope, 24 Aug 1730 - 18 Nov 1739; the finding aid: "Certaines lettres sont en code chiffre. Le code est dans le lot." Language field "Crypte; Francais"',
    cls='A', status='Finding aid names a code in the same lot. No publication found. TNA SP 78/205/95 (lead 1781, Waldegrave 1734) mentions a Newcastle-Marsay cypher copy: the same cipher system may be at issue',
    why="A British diplomat's ciphered correspondence with the key in the same dossier, 96 pieces: cipher, code and clear in one place. Links to catalogue lead 1781 (Newcastle to Marsay cypher, 1734)",
    importance=4, solvability=4, difficulty=2,
    verify='View the dossier (ACV may photograph); check how many letters are ciphered and the code format; compare with lead 1781 and the British cabinet cypher',
    links=[DV, AO], prior_art=dd('"Marsay", "Mestral", "Saint-Saphorin"') + '; "Marsay" hits only lead 1781',
    access_note='ACV inventory only; images not seen; reading room or reproduction'))
rows.append(row(source='davel.vd.ch DAVEL (Chrome fetch), French Swiss pass, 15 Nov 2026', year=1754, date='1746-1762', language='French',
    period='1701-1800', region='England',
    title='Comte de Marsay with members of the British Cabinet, 6 Oct 1746 - 28 Sep 1762, "avec une clef du chiffre" (145 pieces)',
    correspondents='Armand-Louis de Saint-George, comte de Marsay <-> members of the British Cabinet',
    place='unknown <-> London', shelfmark='ACV, P de Mestral III 486 (davel.vd.ch, ID 723224)',
    folio_note='Dossier of 145 pieces in one envelope; finding aid: "Avec une clef du chiffre - code pour dechiffrer"; descriptors codage, cryptage; Language "Crypte; Francais". A different period and a separate key from P de Mestral III 484',
    cls='A', status='Finding aid names a key. No publication found',
    why="145 pieces, a key filed with them, a later period (Seven Years War) than III 484; if the cipher is the British cabinet cipher of the period it also matters for the TNA SP series",
    importance=4, solvability=4, difficulty=2, verify='View III 486; count ciphered letters; check key; compare with III 484 (different key period)',
    links=[DV, AO], prior_art=dd('"Marsay", "Mestral"'), access_note='ACV inventory only; images not seen'))
rows.append(row(source='davel.vd.ch DAVEL (Chrome fetch), French Swiss pass, 15 Nov 2026', year=1722, date='1717-1726', language='French',
    period='1701-1800', region='Central Europe',
    title='Saint-Saphorin papers: ciphered letters from Robethon (1717), Wrisberg (Ratisbon 1720, 1724), Robinson (1726) and others, with per-correspondent ciphers in P de Mestral II D 6/1',
    correspondents="Letters filed in the Mestral family fonds (recipient is the Bernese general in British service Francois-Louis de Pesme de Saint-Saphorin by the fonds' context, not checked item by item): Jean de Robethon, Johann Rudolph von Wrisberg, G. Robinson; cipher sheets for Bothmer, Bernstorff, Buol, Hohenzollern, Fischer, Montmolin, Muralt, Prie, Salm, Schlick",
    place='Hanover / Regensburg / Vienna',
    shelfmark='ACV, P de Mestral II D 4 (letters received; Robethon, Wrisberg w/25/18 and w/26/28, Robinson) and II D 6/1 ("Divers chiffres, chiffrants et dechiffrants", 1670-1770, ID 726266) with sub-units D 6/1/b/2-4, f/1, h/1, m/1-2, p/2, s/1-2',
    folio_note='D 6/1 content: "Clef du chiffre, moyen avec lequel on peut lire, traduire ce qui est ecrit en langage chiffre"; 18 envelopes; each correspondent sub-unit marked "Chiffres". D 4: Wrisberg 19 Dec 1720 (w/25/18) and 6 Jun - 10 Sep 1724 (w/26/28, five letters from Ratisbon) flagged "Crypte". Ciphers of Salm (1680-1710), Schlick (1707), Prie (1658-)',
    cls='A', status='Finding aid: cipher letters and a keys series by correspondent in the same family fonds. No publication found',
    why="The Mestral fonds files ciphered letters of the Hanoverian/British diplomatic world around Saint-Saphorin with the keys of named correspondents, so letters and keys can be matched. Robethon's papers are lead 1663 (Huntington), a related set in a different archive",
    importance=4, solvability=4, difficulty=2,
    verify="Open II D 6/1/b/2 (Bernstorff) and II D 4 w/26/28 (Wrisberg 1724); match Wrisberg's ciphered letters against a D 6/1 sheet; confirm who the recipient is",
    links=[DV], prior_art=dd('"Mestral", "Saint-Saphorin", "Robethon" (lead 1663 only), "Wrisberg"'),
    access_note='ACV inventory only; images not seen'))
rows.append(row(source='archives-online.org (Chrome), French Swiss pass, 15 Nov 2026', year=1510, date='c. 1510', language='unknown',
    period='1497-1559', region='Central Europe',
    title='Letter in cipher addressed to Matthieu Schiner, count and prefect of the Valais and papal nuncio, c. 1510',
    correspondents='unknown -> Matthieu Schiner (bishop of Sion, later cardinal)', place='unknown',
    shelfmark="Archives de l'Etat du Valais (AEV), Supersaxo II, P 74 (via archives-online.org; native AEV database not searched)",
    folio_note='One document, "Lettre (en chiffres) adressee a [Matthieu Schiner], comte et prefet du Valais et nonce apostolique", dated approx. 1510 by the finding aid; sender not named',
    cls='B', status='Finding aid names the cipher letter only; no key. No publication found',
    why='An early (c. 1510) ciphered letter to the best-known Swiss cardinal-diplomat; the Supersaxo family papers may hold more',
    importance=3, solvability=2, difficulty=4, verify='View P 74; check the writer (Supersaxo, or a Milanese or imperial correspondent); look for sibling ciphered pieces in the Supersaxo fonds',
    links=[AO], prior_art=dd('"Supersaxo"'), access_note='AEV photography on request; images not seen'))
rows.append(row(source='archives-online.org (Chrome), French Swiss pass, 15 Nov 2026', year=1630, date='c. 1630', language='French',
    period='1611-1650', region='France',
    title='Letter partly in cipher from the court at Chambery, c. 1630 (FQ 238), and a letter of Silvio di Savoia to Antoine Quartery "contenu a dechiffrer", 22 Oct 163? (FQ 372)',
    correspondents='N.N. -> N.N. (FQ 238); Silvio di Savoia -> Antoine Quartery (FQ 372)', place='Chambery',
    shelfmark='AEV, fonds Jean Marclay, FQ 238 (c. 1630) and FQ 372 (22 Oct 163?, last digit not read)',
    folio_note='FQ 238 "Lettre (en partie chiffree)"; FQ 372 "contenu a dechiffrer". Two separate letters, two keys probable',
    cls='C', status='Finding-aid titles only; no key named', why='Savoyard letters of the Thirty Years War era in the Valais; weak until viewed',
    importance=2, solvability=2, difficulty=3,
    verify='View both; decide whether FQ 372 is a cipher or an illegible hand ("a dechiffrer" is ambiguous)', links=[AO],
    prior_art=dd('"Marclay", "Silvio di Savoia"'), access_note='AEV; images not seen'))
rows.append(row(source='archives-online.org (Chrome), French Swiss pass, 15 Nov 2026', year=1700, date='undated', language='French',
    period='unknown', region='Central Europe',
    title='List of ciphers to be used in a correspondence, Kalbermatten family papers, Valais',
    correspondents='Kalbermatten family (parties not stated)', place='Sion (probably)',
    shelfmark='AEV, de Kalbermatten, P 196',
    folio_note='Title: "Liste des chiffres a employer dans une correspondance touchant les affaires d..." (title cut in the listing; date not recorded)',
    cls='C', status='A cipher table; subject cut off in the listing; no ciphertext named', why='A key with no ciphertext; useful only if the matching letters are in the Kalbermatten fonds',
    importance=2, solvability=2, difficulty=3, verify='Read the full title and date; look for ciphered letters in the same fonds', links=[AO],
    prior_art=dd('"Kalbermatten"'), access_note='AEV; not viewed'))
rows.append(row(source='archives.bge-geneve.ch (Chrome fetch), French Swiss pass, 15 Nov 2026', year=1622, date='1620-1625', language='French',
    period='1611-1650', region='France',
    title="'Divers chiffres employes dans les guerres civiles': notebook of ciphers from Agrippa d'Aubigne's papers, 1620-25 (24 f.)",
    correspondents="Theodore Agrippa d'Aubigne and his secretaries (Huguenot party)", place="Geneva (d'Aubigne in exile)",
    shelfmark='Bibliotheque de Geneve, Arch. Tronchin 148/56, f. 138r-161r (notebook headed "No 56. 1620 a 1625. Chiffres employes dans les guerres civiles")',
    folio_note="24 f. with several ciphers for the Huguenot wars; the same notebook holds d'Aubigne correspondence; BGE shows 48 views (digitised)",
    cls='A', status='BGE finding aid describes a notebook of ciphers with correspondence in the same cahier. Not checked against editions or the Tronchin literature',
    why="A volume of ciphers of the French religious wars with correspondence in the same book, digitised on the BGE site: ciphers and clear letters can be paired. Arch. Tronchin 152 (d'Aubigne correspondence) is a neighbouring record",
    importance=4, solvability=3, difficulty=3,
    verify='Open the 48 views of Tronchin 148/56; check whether the letters on f. 138-161 are ciphered and have the clear beside them; check Tronchin 152',
    links=[BG], prior_art=dd('"Aubigne", "Tronchin 148"'), access_note='Digitised on BGE (48 views)'))
rows.append(row(source='archives.bge-geneve.ch (Chrome fetch), French Swiss pass, 15 Nov 2026', year=1814, date='1807-08; 1814-15; 1800-29', language='French',
    period='1801-1900', region='Central Europe',
    title="Ciphered correspondence in the papers of Jean-Gabriel Eynard and Francois d'Ivernois: Kleiber's cipher key (Eynard), Jacobi-Kloest letters with d'Ivernois's decipherment (1807-08), the key to d'Ivernois's Vienna Congress correspondence",
    correspondents="Eynard <-> Kleiber (Ms. suppl. 1879); Constans Philipp Wilhelm von Jacobi-Kloest -> Francois d'Ivernois (Ms. suppl. 976); d'Ivernois at the Congress of Vienna (Ms. suppl. 1004-1006)",
    place='Geneva / Vienna',
    shelfmark="BGE, Ms. suppl. 1879 f. 147 (Cle du chiffre de la main de Kleiber); Ms. suppl. 976 f. 270-272, 303-322 (lettres chiffrees avec dechiffrement de la main de d'Ivernois); Ms. suppl. 1004-1006 f. 113-114 (cle du chiffre de sa correspondance)",
    folio_note="Three separate sets, three keys; the Jacobi-Kloest lot is described as ciphered letters 'avec dechiffrement de la main de d'Ivernois', 1807-08; the d'Ivernois notebooks hold the key to his correspondence at the Congress (3 Oct 1814 - 29 Mar 1815)",
    cls='A', status='BGE finding aids name keys and a decipherment. No publication found; d\'Ivernois\'s Vienna correspondence may be in the diplomatic literature (not checked)',
    why='Napoleonic-era ciphers with keys and a contemporary decipherment named on the BGE catalogue; the 1814-15 set links to the Congress of Vienna. Three keys, so split on merge: Kleiber, Jacobi-Kloest, d\'Ivernois-Vienna',
    importance=3, solvability=4, difficulty=2,
    verify='Open Ms. suppl. 976 f. 303-322 first (cipher plus decipherment in one hand), then 1879 f. 147 and 1004-1006 f. 113-114; check the digitised views',
    links=[BG], prior_art=dd('"Ivernois", "Jacobi-Kl", "Eynard", "Kleiber"'), access_note='BGE records show views; images not opened'))
rows.append(row(source='archives.bge-geneve.ch (Chrome fetch), French Swiss pass, 15 Nov 2026', year=1700, date='undated', language='French',
    period='unknown', region='France',
    title='Rambaud: autograph letter "presque entierement chiffree" about a criminal case brought against him since his conversion',
    correspondents='Rambaud -> unknown', place='unknown',
    shelfmark='BGE, Ms. fr. 445 f. 116-117 (undated documents on church affairs; Compagnie des Pasteurs correspondence context)',
    folio_note='Item 116-117 within a volume of undated documents on church affairs; the record calls the letter "presque entierement chiffree"',
    cls='B', status='Finding aid only; Huguenot pastor context probable, not checked', why='A single almost fully ciphered letter of a convert; short; no key named',
    importance=2, solvability=2, difficulty=4, verify='View f. 116-117; identify Rambaud and date', links=[BG], prior_art=dd('"Rambaud"'), access_note='BGE; images not opened'))

json.dump(rows, open(os.path.join(HERE, 'candidates.json'), 'w', encoding='utf-8'), indent=1, ensure_ascii=False)

keys = [
 {'title': 'Fribourg: "Alphabeth conventionel et secret entre Lucerne, Fribourg et Soleure", 1708',
  'shelfmark': 'AEF, Legislation et varietes 52 (friXplore)',
  'note': 'Third copy of the 1708 three-canton code, with Luzern COD 1100 and Valais AV 54/7 (the Valais copy adds the Valais as fourth ally). Keys for the Luzern FAA 763 (1711-12) row of the Austria/Swiss sweep. One code, three archives; none seen as images.'},
 {'title': "Fribourg d'Affry fonds: key sheets 280.209 'Chiffre avec Botteman' and 280.210 'Premier chiffre remis par le duc de Choiseul et le chancelier du Muy' (undated)",
  'shelfmark': 'AEF, Affry (de Boccard) 280.209, 280.210',
  'note': 'Two keys in the same fonds as the Rouille / Bernis / Choiseul / Stainville ciphered dispatches (225-268). 280.210 probably keys the Choiseul dispatches of series 227 (not checked). Possible key for affry1757c (R1071).'},
 {'title': "Fribourg d'Affry fonds: other commanders' and envoys' ciphered letters with transcriptions, 1757-61",
  'shelfmark': "AEF, Affry (de Boccard) 239 (Richelieu 1757, 2), 240 (Clermont 1758, 5), 241 (Contades 1758, 7), 242 (Broglie 1761, 2), 243 (Rohan-Soubise 1761, 6), 253 (d'Aubigny 1757-58, 3), 255 (Michel 1761, 2), 256 (Chavigny 1758, 2), 262 (Monteil 1757), 264 (Bausset 1761), 265 (Broglie 1757-58, 4), 246 (Luce 1757, 2)",
  'note': 'Small groups of "Transcription du chiffre de la lettre ..." or "Depeche chiffree"; each writer may have a separate key, so each would be a separate small row if taken up. Companion to the 238 (Estrees) and 244 (Conflans) rows.'},
 {'title': 'Vaud: Mestral cipher series, ciphers by correspondent and undated sheets',
  'shelfmark': 'ACV, P de Mestral II D 6/1 (ID 726266), D 6/1/b/2-4, f/1, h/1, m/1-2, p/2, s/1-2; II D 6/2 (ID 726285, undated ciphers 1650-1750), 6/2/1 (ciphers on parchment, ID 726286), 6/2/2 (ID 726287, 13 pieces)',
  'note': 'Keys of named correspondents of Saint-Saphorin (Bothmer, Bernstorff, Buol, Hohenzollern, Fischer, Montmolin, Muralt, Prie, Salm, Schlick) and unlabelled cipher sheets. The labelled sub-units say only "Chiffres"; the sheets themselves not seen.'},
 {'title': "Valais: Courten Cn B 5/11/8 'Codes de chiffrage de Monsieur le comte de Stainville (duc de Choiseul)' and Cn B 5/10/8 (Bernis to Courten, promises ciphered letters)",
  'shelfmark': 'AEV, de Courten, Cn B 5/11/8 and 5/10/8',
  'note': "Stainville's code in the Courten fonds: the same Choiseul code period as the Fribourg Affry dispatches and the Choiseul-Courten 1757 row of the Austria/Swiss sweep. Link the three when any is read."},
 {'title': "Geneva BGE: Altamira archive, Coll. Edouard Favre (Archives de la maison d'Altamira, 15th-18th c., 6 m)",
  'shelfmark': 'BGE, Coll. Edouard Favre (fonds record); two boxes 83/1 and 83/2 (526 f.) not in the published Bulletin hispanique catalogue',
  'note': 'The fonds-level record surfaced under "alphabet secret" and "chiffree" but the matching lower-level item was not seen; Spanish noble house with diplomats. Look at the item list for the cipher item before taking it up. Not a row.'},
]
json.dump(keys, open(os.path.join(HERE, 'key_leads.json'), 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
print(len(rows), len(keys))
