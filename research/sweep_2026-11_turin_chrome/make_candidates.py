"""Build candidates.json and key_leads.json for the Turin / Archivi Nazionali / Milan ICAR browser sweep (6 Nov 2026).
Rows come from the ASTo online database (seal database "Documenti" records) and the Archivi Nazionali guide records; see README.md."""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = 'ASTo online database (seal database and item-level inventories) + Archivi Nazionali search, Turin browser sweep, Nov 2026'
SCORE = ('Scored from catalogue descriptions read during the Turin browser sweep, 6 Nov 2026 '
         '(research/sweep_2026-11_turin_chrome/); no ciphertext seen')
AST = 'https://archiviodistatotorino.cultura.gov.it'
AST_ACCESS = ('ASTo database: the "Verifica del browser" page only sets a cookie (asto_v, value printed in the page); Chrome passes it, '
              'and curl passes it by resending that cookie. No login. The seal photo shows the seal and a strip of the sheet, not the text. '
              'The letters themselves are not digitised (fonds marked "Digitalizzato: No"); order scans from ASTo (Sala studio online).')

ROWS = [
    dict(
        year=1612, date='16 Oct 1612 and 21 Jul 1613',
        title="Charles Emmanuel I of Savoy's cipher letters to his ambassador in London, Giovanni Battista Gabaleone (Infanta Maria - Prince Henry match)",
        correspondents='Charles Emmanuel I, Duke of Savoy -> Giovanni Battista Gabaleone, Savoyard ambassador in London',
        place='Turin -> London', language='Italian (expected)',
        region='Italy', period='1611-1650',
        shelfmark=("Archivio di Stato di Torino, Corte, Materie politiche per rapporto all'interno, Matrimoni della Real Casa di Savoia, "
                   "mazzo 25, fasc. 7 (seal database); inventory n. 102 lists mazzo 25 fasc. 4 \"Lettere diverse del Duca ... al Caval.e Gabaleone, "
                   "Ambasciadore ... in Londra\", 1612-1619"),
        folio_note=('Two letters described in the ASTo seal database as "Lettera cifrata di Carlo Emanuele I duca di Savoia indirizzata a Giovanni '
                    'Battista Gabaleone ambasciatore a Londra": did=490 (16/10/1612, red wax seal under paper, endorsement "... 9bre" visible on the '
                    'seal photo, i.e. the letter as received and brought back) and did=1197 (21/7/1613). File title: "Matrimonio progettato tra '
                    "l'Infanta Maria ... ed il principe di Galles Enrico Federico\"."),
        cls='C',
        status=('Description only: the catalogue calls both letters "lettera cifrata"; the seal photos show no text. Whether a decipherment is '
                'written on them (as received copies often have) is not known.'),
        why=('Savoyard ducal cipher of 1612-13 on the English marriage negotiation, from the received originals; Gabaleone\'s own despatches '
             'survive (ASTo Lettere Ministri Gran Bretagna m. 1; BL Add MS 32023 A-B transcripts), which may give the clear text or the key.'),
        importance=3, solvability=3, difficulty=3,
        verify=('Order scans of did=490 and did=1197 (mazzo 25 fasc. 7 / fasc. 4); check for an interlinear decipherment; look for the '
                "Gabaleone cipher in Lettere Ministri Gran Bretagna m. 1 and in BL Add MS 32023 A-B."),
        links=[{'href': f'{AST}/sigdtl/?did=490', 'label': 'ASTo seal database, letter of 16/10/1612'},
               {'href': f'{AST}/sigdtl/?did=1197', 'label': 'ASTo seal database, letter of 21/7/1613'},
               {'href': f'{AST}/inventari/?id=484745', 'label': 'ASTo inventory n. 102, mazzo 25 fasc. 4'},
               {'href': 'https://searcharchives.bl.uk/catalog/032-002025751', 'label': 'BL Add MS 32023 A-B (Gabaleone despatches, transcripts)'}],
        access_note=AST_ACCESS,
        prior_art=('known.py: no hit for Gabaleone, Matrimoni della Real Casa or mazzo 25. Web search (6 Nov 2026): Gabaleone\'s mission and the '
                   'BL transcripts are cited, nothing on cipher letters. DECODE, Tomokiyo, Lasry not searched.'),
    ),
    dict(
        year=1640, date='7 Jul 1640',
        title="Cardinal Maurizio of Savoy's cipher letter to abate Buschetti, ambassador of the 'principi cognati' at Milan (Savoyard civil war)",
        correspondents="Cardinal Maurizio of Savoy -> abate Buschetti, envoy of the princes Maurizio and Tommaso to the Spanish governor of Milan",
        place='Nice -> Milan', language='Italian (expected)',
        region='Italy', period='1611-1650',
        shelfmark=("Archivio di Stato di Torino, Corte, Materie politiche per rapporto all'interno, Tutele, reggenze e luogotenenze generali, mazzo 4"),
        folio_note=('ASTo seal database did=1388: "Lettera cifrata del cardinale Maurizio di Savoia all\'abate Buschetti", Nice, 7/7/1640, '
                    'Maurizio\'s seal (red wax under paper). The same database lists clear letters to Buschetti of 1 Jul 1640 (did=714, Maurizio) '
                    'and five from Prince Tommaso (did=1382-1386): the Buschetti file of the princes\' party.'),
        cls='C',
        status=('Description only: the catalogue calls it "lettera cifrata"; the seal photo (1630 px) shows only faint show-through of a few signs, '
                'too faint to say whether they are cipher figures. Gloss unknown.'),
        why=('A cipher of the princes\' party in the Savoyard civil war (1639-42), with clear sibling letters to the same envoy in the same file '
             'for cribs.'),
        importance=3, solvability=3, difficulty=3,
        verify='Order scans of mazzo 4 (did=1388 and siblings did=714, 1382-1386); check for a decipherment on the leaf or among the siblings.',
        links=[{'href': f'{AST}/sigdtl/?did=1388', 'label': 'ASTo seal database, cipher letter 7/7/1640'},
               {'href': f'{AST}/sigdtl/?did=714', 'label': 'ASTo seal database, clear sibling 1/7/1640'}],
        access_note=AST_ACCESS,
        prior_art='known.py: no hit for Buschetti, Maurizio di Savoia or Tutele. DECODE, Tomokiyo, Lasry and the literature not searched.',
    ),
    dict(
        year=1590, date='1589-1597',
        title='Venetian "Lettere in cifra" to the Provveditori alle biave from the bailo at Constantinople (1589-97) and the ambassador in Spain (1590)',
        correspondents='Venetian bailo at Constantinople; Venetian ambassador in Spain -> Provveditori alle biave (grain magistracy), Venice',
        place='Constantinople, Madrid -> Venice', language='Italian (expected)',
        region='Italy', period='1589-1598',
        shelfmark=('Archivio di Stato di Venezia, "Secreta, lettere in cifra ai provveditori alle biave" (per the 1991 inventory; series number '
                   'not given in the portal), inventory "Lettere in cifra indirizzate prevalentemente ai Provveditori alle biave dal bailo di '
                   'Costantinopoli (1589-1597) e dall\'ambasciatore veneto in Spagna (1590)"'),
        folio_note=('Archivi Nazionali guide record sdr 43087032 (inventory compiled 1991, ASVe general series). Its note: "CONTROLLARE: fondo '
                    'collegato «Secreta, lettere in cifra ai provveditori alle biave»? così nell\'inv. ma senza riscontro di SE relativa nel DB".'),
        cls='C',
        status='Description only: a small fonds of cipher letters named by an ASVe inventory; extent, busta numbers and any decipherments unknown.',
        why=('Bailo cipher letters on grain supply in the 1590s, sent to a magistracy outside the Senate\'s Deciferazioni series, so possibly '
             'never deciphered into the Senate registers.'),
        importance=3, solvability=3, difficulty=3,
        verify=('Ask ASVe for the 1991 inventory and the busta numbers; check against Senato, Dispacci Costantinopoli and Deciferazioni for '
                'the same dates; the CX key books (Cifre, chiavi e scontri di cifra) hold the 1578-87/1590s ambassadors\' cipher.'),
        links=[{'href': 'https://archivinazionali.cultura.gov.it/it/guida-ed-inventario/-/sdr/view/43087032', 'label': 'Archivi Nazionali guide record'}],
        access_note='Not digitised; the portal gives only the inventory title. ASVe reading room or a reference enquiry.',
        prior_art=('known.py: no hit for "biave" or "bailo di Costantinopoli". Web search (6 Nov 2026) found nothing on these letters. '
                   'DECODE, Tomokiyo, Lasry not searched.'),
    ),
]

AN = 'https://archivinazionali.cultura.gov.it/it/unita-archivistica/-/ua/view/'
SG_ACCESS = ('Not digitised (no Mirador tab on Archivi Nazionali). Description from the ASGe San Giorgio inventory as loaded into Archivi '
             'Nazionali; the portal gives no numeric shelfmark, so the filza is cited by cancelliere, cover title and ARK. ASGe reading room / '
             'photo order.')
SG_PRIOR = ('known.py: no hit for San Giorgio, Cancelleria dei Protettori, Montebruni, Lasania. Not in DECODE dumps. Tomokiyo, Lasry and '
            'the literature not searched.')
SG = 'Archivio di Stato di Genova, Casa di San Giorgio, Affari generali, Cancelleria dei Protettori'
ROWS += [
    dict(
        year=1561, date='6 Jun 1560 - 2 Jan 1570 (mostly Jun 1560 - Jun 1562)',
        title="Banco di San Giorgio: Corsican commissioners' letters 'often partly in cipher', filed with 'several' of their keys (Montebruni filza 1560)",
        correspondents=('Commissari generali of Corsica Andrea Imperiale, Pellegro Giustiniano, Gaspare Cattaneo, Nicolò Grimaldi and local '
                        'officials -> Protettori of the Casa di San Giorgio, Genoa'),
        place='Bastia, Ajaccio, Balagna, Capraia, Calvi -> Genoa', language='Italian (expected)',
        region='Italy', period='1560-1589',
        shelfmark=f'{SG}, cancelliere Francesco Montebrunus Cybo, filza "[...] ebruni [...] 1560" / "Anno 1560. Francesco Cibo M..." (ARK ark:/22580/ua_25838904)',
        folio_note=('Filza of 111 unnumbered cc. and fascicles. Inventory: "a) lettere, spesso parzialmente in cifra, dei commissari generali ... '
                    'copie di dispacci provenienti dall\'estero e di missive di privati intercettate ...; parecchi cifrari dei funzionari di stanza '
                    'in Corsica (commissario generale e commissari locali, vicario e luogotenenti)".'),
        cls='C',
        status='Description only. Keys of the same officials are in the same filza, so the cipher passages should be readable from them.',
        why=('Genoese colonial cipher of the Corsican war years (after the 1559 return of Corsica to San Giorgio), with the senders\' keys in '
             'the same filza: a key-plus-ciphertext set from an archive not yet in the catalogue.'),
        importance=3, solvability=4, difficulty=2,
        verify='Order photos of the cipher letters and the cifrari in the filza; pair each letter with its commissioner\'s key.',
        links=[{'href': AN + '25838904', 'label': 'Archivi Nazionali record (ASGe inventory text)'}],
        access_note=SG_ACCESS, prior_art=SG_PRIOR,
    ),
    dict(
        year=1562, date='7 Jan 1561 - 9 Apr 1565 (mostly Jan 1561 - Feb 1563)',
        title="Banco di San Giorgio: letters 'sometimes partly in cipher' of the Corsican commissioners Cattaneo, Grimaldi and Fiesco (Montebruni filza 1561-65)",
        correspondents=('Commissari generali of Corsica Gaspare Cattaneo, Nicolò Grimaldi, Paolo Gregorio Fiesco and local officials -> '
                        'Protettori of the Casa di San Giorgio, Genoa'),
        place='Bastia, Bonifacio, Ajaccio, Calvi, Corte, Balagna -> Genoa', language='Italian (expected)',
        region='Italy', period='1560-1589',
        shelfmark=f'{SG}, cancelliere Francesco Montebrunus Cybo, filza "1561 in 156[.]. Actorum Francisci Cybo Montebruni cancellarii" (ARK ark:/22580/ua_25838898)',
        folio_note=('Filza of 367 unnumbered cc. and fascicles, 315 x 115 mm. Inventory: "a) lettere, talvolta parzialmente in cifra, dei commissari '
                    'generali Gaspare Cattaneo, Nicolò Grimaldi e Paolo Gregorio Fiesco ... sullo stato dei presidi, dispiegamento delle forze militari, '
                    'costruzione delle nuove fortificazioni ...".'),
        cls='C',
        status=('Description only. Keys for these officials: the 1560 Montebruni filza (row above) and the Officium Corsice filza 1559-66 '
                '(ARK ua_25838907, "istruzioni, cifrari e fideiussioni dei neoeletti").'),
        why='Same system as the row above, a later run (1561-63); keys for the same commissioners sit in sibling filze of the same chancellor.',
        importance=3, solvability=4, difficulty=2,
        verify='Order photos; take the keys from ua_25838904 / ua_25838907 / ua_25838922.',
        links=[{'href': AN + '25838898', 'label': 'Archivi Nazionali record (ASGe inventory text)'},
               {'href': AN + '25838907', 'label': 'sibling filza with cifrari, 1559-66'}],
        access_note=SG_ACCESS, prior_art=SG_PRIOR,
    ),
    dict(
        year=1519, date='11 Jan - 25 Dec 1519',
        title="Banco di San Giorgio: reports 'sometimes in cipher' from Genoese ambassadors, consuls and envoys at the papal court (Lasagna filza 1519)",
        correspondents='Genoese ambassadors, consuls and envoys at the Roman curia, and others resident in Rome -> Protettori of San Giorgio',
        place='Rome -> Genoa', language='Italian (expected)',
        region='Italy', period='1497-1559',
        shelfmark=f'{SG}, cancelliere Ieronimus Lasania, filza "1519. Hieronimi Lazanie" / "M°DXVIIII. Lazanie Ieronimi ..." (ARK ark:/22580/ua_25840020)',
        folio_note=('Filza of 309 unnumbered cc., 295 x 104 mm. Inventory: "missive dell\'inviato genovese a Milano Laurentius Parrisola e relazioni, '
                    'talvolta in cifra, sia di ambasciatori, consoli ed inviati a vario titolo presso la curia pontificia in Roma, sia di altri soggetti '
                    'residenti nell\'urbe".'),
        cls='C',
        status=('Description only. San Giorgio filze of these years hold many cifrari issued to officials (e.g. 1517-18 Lasagna, 1519-20 Porta), '
                'but none named for Rome envoys.'),
        why='Genoese diplomatic cipher from Rome under Leo X, 1519; early-16th-century Genoese ciphers are scarce in the catalogue.',
        importance=3, solvability=3, difficulty=3,
        verify='Order photos of the Rome reports; check the 1517-1520 San Giorgio filze for a matching cifrario.',
        links=[{'href': AN + '25840020', 'label': 'Archivi Nazionali record (ASGe inventory text)'}],
        access_note=SG_ACCESS, prior_art=SG_PRIOR,
    ),
]

KEY_LEADS = [
    dict(year=1520, date='1466-1570',
         title='About 99 filze of the Cancelleria dei Protettori of San Giorgio holding "istruzioni e cifrari" for newly elected officials (Corsica, the Rivieras, Sarzana, Capraia ...)',
         shelfmark='Archivio di Stato di Genova, Casa di San Giorgio, Affari generali, Cancelleria dei Protettori (filze of the chancellors Gallo, Compiano, Lasagna, Porta, Terrili, Borlasca, Lomellini, Spinola de Caneto, Raimondi, Sorba, de Franchis, Montebruni ...)',
         note=('Archivi Nazionali search "cifrari" returns the ASGe San Giorgio inventory: almost every chancellor\'s filza of 1466-1570 lists '
               '"promesse di buon servizio con relative cauzioni, istruzioni e cifrari per i nuovi eletti alle cariche vacanti". Named ones: '
               'Nicolaus Spinula castellan of Bonifacio 1492 (ua_25840002/25840056); captain of Sarzana Luquinus Stella 1524 (ua_25839279); '
               'castellan of Pieve di Teco Adam de Arquata 1526 (ua_25839846); castellan of Sarzanello Lucas Salvaigus 1542 (ua_25839867); '
               'captain Lazaro Sauli 1543 (ua_25840773); Stephanus Vadesturla, fort of San Paolo, Ventimiglia (ua_25840266). Not digitised. '
               'Keys for the cipher letters of the three San Giorgio rows; full list in the sweep scratch file sg2.json (not committed).'),
         links=[{'href': AN + '25840002', 'label': 'example: Lasagna filza 1491-94 (Spinola cifrario 1492)'}]),
    dict(year=1546, date='1546-1550s',
         title="17 cipher keys of Cardinal Cristoforo Madruzzo's chancery (Trent), digitised",
         shelfmark='Archivio di Stato di Trento, Capitolo del Duomo di Trento, N1303p2 = N1303_06 to N1303_22',
         note=('Archivi Nazionali (under AS Varese/Trento), images in the Mirador viewer: duke of Florence (10 Jul 1546), "miser Traiano" (23 Dec 1546), '
               'don Diego (20 Apr 1547), cardinal of Coria Francisco de Mendoza (6 Sep 1547), prince of Sul[mo]na, Fabrizio Colonna, Maurice of Saxony, '
               'cardinal of Augsburg Otto Truchsess, cardinal Carpi, "Cifra con Turca", Maximilian II, "Stropp", cardinal Farnese, cardinal Salviati, '
               'mons. de Fanno, cardinal of Ravenna, one unnamed. Trasselli, "Su alcuni dispacci in cifra della Biblioteca comunale di Trento", '
               'Studi Trentini XXII (1941) 183-192, edits related material (BCT manoscritti; AS Trento Corrispondenza madruzziana, 8 bb., 1539-67). '
               'Keys for Madruzzo cipher letters elsewhere (cf. catalogue entry 627, Charles V to Madruzzo 1546, AGS).'),
         links=[{'href': 'https://archivinazionali.cultura.gov.it/it/unita-documentaria/-/ud/view/18355515', 'label': 'N1303p2 parent record'},
                {'href': 'https://archivinazionali.cultura.gov.it/it/unita-documentaria/-/ud/view/18355521', 'label': 'N1303_06, key with the duke of Florence 1546'}]),
    dict(year=1716, date='1716-1717',
         title='Cipher of the Conte della Perosa (two copies), Savoyard envoy in London',
         shelfmark="Archivio di Stato di Torino, Corte, Materie politiche per rapporto all'estero, Lettere Ministri, Gran Bretagna, mazzo 23",
         note=('Inventory n. 151 vol. I (PDF): "Perosa (Conte della) - Contiene anche il cifrario del Conte della Perosa in 2 copie, 1716 e 1717", '
               'with a "Registro di lettere di S.M. e del Ministro al Conte della Perosa 1716 in 1719". Possible key for catalogue entry 1962 '
               '(Perosa letters, Archives de Savoie 1J 164).'),
         links=[{'href': f'{AST}/upload/LETTERE-MINISTRI-Vol_I.pdf', 'label': 'ASTo inventory n. 151 vol. I (PDF)'}]),
    dict(year=1830, date='1816-1849',
         title='Sardinian legation registers "Copia dei cifrati" (Paris, Munich, Naples): copies of the ciphered enclosures, probably in clear',
         shelfmark=("Archivio di Stato di Torino, Corte, Lettere Ministri: Francia mazzo 340 (cifrati sent from Turin to the envoy in Paris, 2 registers, "
                    "1816-1844) and mazzo 343 (cifrati sent to Turin, 2 registers, 1816-1832); Baviera mazzo 41 (1823-1827); Due Sicilie mazzo 68 "
                    "(1836-1849, both directions)"),
         note=('Inventory n. 151 vol. I and the fonds descriptions ("copia dei cifrati annessi ai dispacci ordinari"). Legation-side registers, so most '
               'likely the plaintext of what was sent in cipher: cribs or plaintext for any ciphered Sardinian despatch of 1816-49 in the Turin '
               'or legation files. Not digitised; whether they hold cipher or clear text is not stated.'),
         links=[{'href': f'{AST}/fondi/?id=273937', 'label': 'ASTo Lettere Ministri Francia (fonds description)'},
                {'href': f'{AST}/fondi/?id=273935', 'label': 'ASTo Lettere Ministri Due Sicilie'},
                {'href': f'{AST}/fondi/?id=273927', 'label': 'ASTo Lettere Ministri Baviera'}]),
    dict(year=1691, date='1691-1692',
         title='Savoyard cipher for the Holland mission (Della Torre, 1690-97)',
         shelfmark="Archivio di Stato di Torino, Corte, Materie politiche per rapporto all'estero, Lettere Ministri, Olanda, mazzo 1",
         note='Inventory n. 151 vol. II (poor OCR): "OLANDA ... CIFRARIO 1691 e 1692" next to the Conte/Presidente Della Torre entries (1690 in 1697).',
         links=[{'href': f'{AST}/upload/LETTERE%20MINISTRI_Vol.II.pdf', 'label': 'ASTo inventory n. 151 vol. II (PDF)'}]),
    dict(year=1729, date='1729-1731',
         title='Ciphers sent to the Conte di Chiusano, Savoyard minister in Holland',
         shelfmark="Archivio di Stato di Torino, Corte, Negoziazioni con Inghilterra e Olanda (inv. n. 94), Olanda, mazzo 2, fasc. 1",
         note='"ISTRUZIONE al Conte di Chiusano Ministro in Ollanda ... con le Memorie relative ad altri Affari, e Ciffre al med.o state rimesse. 1729 in 1731".',
         links=[{'href': f'{AST}/inventari/?id=459637', 'label': 'ASTo inventory record'}]),
    dict(year=1742, date='12 Feb 1742',
         title='Cipher given to the Marchese Mossi, Savoyard ambassador extraordinary at Venice',
         shelfmark="Archivio di Stato di Torino, Corte, Negoziazioni colla Repubblica di Venezia (inv. n. 98), Venezia, mazzo 1, fasc. 18",
         note='"Istruzione originale di S. M. al Marchese Mossi ... 12 feb.ro 1742 ... Con la Ciffra al medesimo rimessa".',
         links=[{'href': f'{AST}/inventari/?id=359609', 'label': 'ASTo inventory record'}]),
    dict(year=1770, date='second half of the 18th century',
         title='"Ciffre della Corte di Roma" copied from an old Vatican manuscript, with reflections on them',
         shelfmark="Archivio di Stato di Torino, Corte, Scritture relative alle corti straniere (inv. n. 100.2), Roma, mazzo 1, fasc. 9",
         note='Papal keys (age not stated) copied in Turin with a commentary; may duplicate known Vatican key collections.',
         links=[{'href': f'{AST}/inventari/?id=461868', 'label': 'ASTo inventory record'}]),
    dict(year=1765, date="1760s",
         title='"Ciffre, e Controcifre" of the Sardinian viceroyalty',
         shelfmark="Archivio di Stato di Torino, Corte, Sardegna, Materie politiche (inv. n. 57), Cat. IV (Vicerè, Governatori ...), mazzo 2, fasc. 48",
         note='Keys and counter-keys of the viceroys / Segreteria for Sardinia, 1760s.',
         links=[{'href': f'{AST}/inventari/?id=336055', 'label': 'ASTo inventory record'}]),
    dict(year=1810, date='1810-1811',
         title='"Cifra per la Corrispondenza" in the file on Mgr Ruopoli, vicar apostolic of Fondi, arrested in Sardinia',
         shelfmark='Archivio di Stato di Cagliari, Segreteria di Stato e di guerra del Regno di Sardegna, Serie II, Cat. I Affari esteri, unità 00021',
         note='Archivi Nazionali unit 44037159: "Lettere relative all\'arrivo in Sardegna di Monsignor Ruopoli ... ed al di lui seguito arresto: 1810-1811. Cifra per la Corrispondenza." No images.',
         links=[{'href': 'https://archivinazionali.cultura.gov.it/it/unita-archivistica/-/ua/view/44037159', 'label': 'Archivi Nazionali record'}]),
    dict(year=1924, date='1924 (exhibit of the 1927 trial)',
         title='Codebook ("cifrario") of the newspaper Corriere italiano, seized for the Matteotti murder trial',
         shelfmark='Archivio di Stato di Roma, Corte di assise di Roma, fascicolo 2 del 1927 (processo Matteotti), documenti sequestrati ed esibiti, vol. 18',
         note=('Archivi Nazionali unit 18875997 "Cifrario del «Corriere italiano» e busta", digitised (Mirador viewer). The same trial file has '
               'several police "trascrizione del telegramma cifrato" items of 1924 (clear transcriptions, not ciphertext).'),
         links=[{'href': 'https://archivinazionali.cultura.gov.it/it/unita-documentaria/-/ud/view/18875997', 'label': 'Archivi Nazionali record (images)'}]),
]

rows = []
for r in ROWS:
    r.update(source=SRC, score_note=SCORE, seen='description', needs_archive_scan='yes')
    rows.append(r)
json.dump(rows, open(os.path.join(HERE, 'candidates.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump(KEY_LEADS, open(os.path.join(HERE, 'key_leads.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(rows), 'rows,', len(KEY_LEADS), 'key leads')
