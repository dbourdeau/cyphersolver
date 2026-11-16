"""Chrome wave 7 (15 Nov 2026): Arxius en linia (Catalan archives portal) cipher sweep.
Writes candidates.json and key_leads.json."""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = "Arxius en linia (arxiusenlinia.cultura.gencat.cat) JSON backend in Chrome, wave 7, 15 Nov 2026"
URL = "https://arxiusenlinia.cultura.gencat.cat/#/cercabasica/detallunitat/"


def link(ref):
    return [{"href": URL + ref, "label": "Arxius en linia record " + ref}]


rows = []


def row(**kw):
    base = dict(language="Spanish", region="Spain", cls="B",
                score_note="Scored from the Arxius en linia record (15 Nov 2026, wave 7); the vetting block says what was viewed",
                links=[], source=SRC, ark="", needs_archive_scan="no")
    base.update(kw)
    rows.append(base)


# 1873 telegrams, digitised, ciphertext seen
for ref, date, sender, recv, clave, imp in [
    ("ANC1-700-T-412", "23 Apr 1873", "Governor of Zaragoza",
     "the civil governors of Lleida, Huesca, Tarragona, Barcelona, Valencia, Castellon, Granada and Jaen (received at Castellon, then Tarragona)",
     "no key name on the sheet; opens in clear ('Me dicen de Madrid'), then about 60 two-digit groups, with a clear 'tambien' inside", 2),
    ("ANC1-700-T-420", "15 Oct 1873", "Minister of the Interior (Gobernacion), Madrid", "the Governor of Tarragona",
     "sheet marked 'Clave L. 13': about 30 two-digit groups, then clear text", 2),
    ("ANC1-700-T-429", "10 Dec 1873", "Head of the Political Section of Gobernacion, Madrid", "the Governor of Tarragona",
     "sheet marked 'Clave N. 34': about 190 two-digit groups with a few clear words", 3)]:
    row(year=1873, date=date, period="1801-1900",
        title=f"Telegram in number cipher, {sender} to {recv.split(' (')[0].split(',')[0]}, {date} (Josep Anselm Clave papers)",
        correspondents=f"{sender} -> {recv}", place="Madrid / Zaragoza -> Tarragona",
        shelfmark=f"Arxiu Nacional de Catalunya, ANC1-700 Josep Anselm Clave, {ref.split('-', 1)[1]}",
        folio_note="1 unit, 1 leaf, 1 image (printed Despacho telegrafico form, manuscript); digitised on Arxius en linia",
        status=f"Online (1 image). Spanish telegraph cipher of the First Republic, 1873: {clave}. No decipherment on or with the sheet (viewed 15 Nov 2026). Catalogue: 'el contingut del telegrama esta xifrat'.",
        why="Short numeric telegrams of the Spanish Interior Ministry in 1873, with named keys (Clave 13, Clave 34) and clear word fragments inside the groups: a small code family for a rebuild by crib and frequency.",
        importance=imp, solvability=3, difficulty=3,
        verify="Check the other Clave telegrams of the same fonds and Spanish telegraph-code literature for a 1873 table.",
        links=link(ref), seen="image", needs_archive_scan="no")

# Carlist letters, not online
carl = [
    ("ANC1-1391-T-92", 1842, "7 Jul 1842", "Modena", "Rocaberti-Dameto (Modena) to Carlos Maria Isidro de Borbon (Carlist pretender)",
     "2 units: one letter on the journey, lodging, finance and suspected treachery of Carlist leaders, and 'una carta xifrada'"),
    ("ANC1-1391-T-115", 1842, "30 Dec 1842", "Vienna", "Rocaberti-Dameto (Vienna) to Carlos Maria Isidro de Borbon (Carlist pretender)",
     "1 unit: 'carta xifrada'"),
    ("ANC1-1391-T-421", 1835, "22 Feb 1835", "Cardona", "Pere Nolasc Bassa (Cardona) to Manuel Llauder, captain general of Catalonia",
     "1 unit: 'carta parcialment encriptada' on reports and sweeps in central Catalonia, First Carlist War"),
]
for ref, yr, date, place, corr, note in carl:
    row(year=yr, date=date, period="1801-1900", title=f"{corr}, cipher letter, {date}",
        correspondents=corr, place=place,
        shelfmark=f"Arxiu Nacional de Catalunya, ANC1-1391 Col.leccio documental sobre les guerres carlines, {ref.split('-', 1)[1]}",
        folio_note=note,
        status=f"Not online (Arxius en linia record, 15 Nov 2026; no digital object). {note}. No decipherment is mentioned. Spanish, manuscript (a draft in Rocaberti's file).",
        why="Carlist cipher letters of the 1830s-40s; the same collection holds the Alcudia cipher tables of 16 Jun 1840 (ANC1-1391-T-14), described as tables and instructions to decipher, a possible key.",
        importance=3, solvability=3, difficulty=3,
        verify="Order images from the ANC; read T-14 (the tables) first; check whether a clear copy of the draft exists in the same series.",
        links=link(ref), seen="catalogue", needs_archive_scan="yes")

row(year=1646, date="1640-1646", period="1611-1650",
    title="Saavedra Fajardo's peace negotiations: 'cartes xifrades' (ff. 174-329, 55 letters signed by Philip IV, mostly 1644), Blanes-Centelles i Saavedra family archive",
    correspondents="Philip IV (signed) -> Diego de Saavedra Fajardo, plenipotentiary at Munster and Ratisbon", place="Madrid / Zaragoza -> Munster",
    shelfmark="Arxiu Nacional de Catalunya, ANC1-53 Llinatge Blanes-Centelles i Saavedra, ANC1-53-T-702 (Especul d'escriptures, ff. 174-329)",
    folio_note="156 folios of a 534-folio parchment-bound book: 'Cartes xifrades relacionades amb les negociacions de pau (1640-1646): folis 174 a 329. Hi ha 55 cartes signades pel rei catolic (la majoria pertanyen al 1644)'; the volume needs restoration",
    status="Not online (Arxius en linia, 15 Nov 2026; no digital object). Description: cipher letters on the peace negotiations, 156 folios, 55 signed by the king. The description does not say a decipherment is filed. Spanish.",
    why="Philip IV's cipher letters to his plenipotentiary at Munster, mostly 1644: a long single-system corpus, a sibling of the Sarmiento and Cardinal-Infante cipher letters already in the ledger.",
    importance=4, solvability=3, difficulty=3,
    verify="ANC reading room: check whether the ciphers are paired with decipherments in the same book (an 'especul', a later compilation).",
    links=link("ANC1-53-T-702"), seen="catalogue", needs_archive_scan="yes")

row(year=1700, date="1681-1700", period="1651-1700",
    title="Manuel de Sentmenat Oms de Santapau, marquis of Castelldosrius: two cipher letters among the letters received from Charles II (1681-1700)",
    correspondents="Charles II of Spain and the court -> Manuel de Sentmenat Oms de Santapau i de Lanuza (marques de Castelldosrius)", place="Madrid",
    shelfmark="Arxiu Nacional de Catalunya, ANC1-167 Llinatge Sentmenat, marquesos de Castelldosrius, ANC1-167-T-3773 (old sig. 1242.19)",
    folio_note="composite unit of 478 documents: 'conte una carta autografa de Carles II sobre la successio al tron d'Espanya i dues cartes xifrades'",
    status="Not online (Arxius en linia, 15 Nov 2026; no digital object). Two cipher letters inside a 478-document unit of the Carles II correspondence; which two is not stated. Spanish.",
    why="Late-Habsburg court cipher letters to the diplomat who delivered Charles II's will.",
    importance=3, solvability=2, difficulty=3,
    verify="ANC reading room: find the two leaves; compare with the Spanish general cipher of the 1690s.",
    links=link("ANC1-167-T-3773"), seen="catalogue", needs_archive_scan="yes")

row(year=1936, date="11-18 Jul 1936", period="1901-1950", language="French",
    title="Narcis de Carreras i Guiteras: 10 enciphered telegrams, 11-18 Jul 1936, with keys",
    correspondents="unknown (telegrams to or from Narcis de Carreras, Barcelona)", place="Barcelona",
    shelfmark="Arxiu Nacional de Catalunya, ANC1-171 Narcis de Carreras i Guiteras, ANC1-171-T-183",
    folio_note="'Telegrames xifrats': 10 documents, typescript, French, 'Inclou claus'",
    status="Not online (Arxius en linia, 15 Nov 2026; no digital object). Ten typed enciphered telegrams of the week before the 1936 rising, in French, filed with their keys. No decipherment is mentioned.",
    why="A short typescript cipher series with its keys in the same unit, on the eve of the Spanish Civil War.",
    importance=2, solvability=4, difficulty=2, verify="ANC reading room; check whether the 'claus' are the keys or the plain texts.",
    links=link("ANC1-171-T-183"), seen="catalogue", needs_archive_scan="yes")

row(year=1937, date="1937 (copies made 1940-1945)", period="1901-1950",
    title="Josep Andreu i Abello: about 150 copies of enciphered telegrams, cables and radiograms of the Spanish Embassy in Mexico, 1937",
    correspondents="Spanish Embassy in Mexico (mostly Felix Gordon Ordas) -> members of the Republican government and Spanish consuls", place="Mexico City",
    shelfmark="Arxiu Nacional de Catalunya, ANC1-408 Josep Andreu i Abello, ANC1-408-T-1891",
    folio_note="'Correspondencia xifrada escrita entre l'01.01.1937 i el 31.12.1937': about 150 documents, 4 subfolders, Spanish, typescript copies",
    status="Not online (Arxius en linia, 15 Nov 2026; no digital object). Typescript copies of enciphered telegrams of 1937; whether the copies show the ciphertext or a clear text is not stated.",
    why="Republican diplomatic cable traffic of 1937, a large body from one embassy.",
    importance=2, solvability=2, difficulty=3, verify="Find out whether the copies are ciphertext; the Republican cipher keys are the open question.",
    links=link("ANC1-408-T-1891"), seen="catalogue", needs_archive_scan="yes", cls="C")

row(year=1937, date="09 Jun - 17 Dec 1937", period="1901-1950", language="Spanish / Catalan",
    title="Generalitat of Catalonia, file on competence conflicts with the Republican government 1937: enciphered telegrams among 30 documents (96 images online)",
    correspondents="Generalitat of Catalonia and the Government of the Republic (and the Basque government)", place="Barcelona / Valencia",
    shelfmark="Arxiu Nacional de Catalunya, ANC1-1 Generalitat de Catalunya (Segona Republica), ANC1-1-T-7519",
    folio_note="30 documents, 96 images online; 'telegrames xifrats, correspondencia, informes i resums de noticies'",
    status="Online (96 images, not viewed in full 15 Nov 2026). The description lists enciphered telegrams among the documents. Spanish/Catalan.",
    why="Civil War government telegrams with cipher among them; the 1938 sibling T-7499 has an agenda item on the use of a cipher key.",
    importance=2, solvability=2, difficulty=3, verify="Page through the 96 images for the cipher telegrams; check for a decipherment beside each.",
    links=link("ANC1-1-T-7519"), seen="catalogue", needs_archive_scan="no", cls="C")

json.dump(rows, open(os.path.join(HERE, "candidates.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)

keys = [
    {"title": "Arxiu del Palau-Requesens: 'Xifrat general' and 'xifrat particular' volumes of Philip II's correspondence, 1562-1576 (ANC1-960-T-891 to -895)",
     "shelfmark": "Arxiu Nacional de Catalunya, ANC1-960 Arxiu del Palau-Requesens, T-891, T-892, T-893, T-894, T-895",
     "note": "Five cipher volumes of Luis de Requesens y Zuniga: T-891 general cipher for Philip II, the Council and the viceroys of Naples and Sicily (1568); T-892 particular cipher Philip II-Requesens (10 units, 1568); T-893 with the duke of Arcos (1568-74); T-894 with Francisco de Alava, ambassador in France (1562-68); T-895 general cipher with Philip II's diplomats (3 units, 1562-76). Keys or cipher tables, not online. Arxius en linia 15 Nov 2026."},
    {"title": "Alcudia to Rocaberti-Dameto, Vienna 16 Jun 1840: cipher tables and instructions for the Carlist messages (ANC1-1391-T-14)",
     "shelfmark": "Arxiu Nacional de Catalunya, ANC1-1391 Col.leccio documental sobre les guerres carlines, T-14",
     "note": "'Carta que es tramet amb les taules i instruccions per desxifrar els missatges codificats. Inclou les taules.' 3 units, not online. A key for the cipher letters ANC1-1391-T-87, -92, -115 (1842)."},
    {"title": "Instruccions per cartes xifrades a Antonio Ximeno, 1487 (ACPS211-95-T2-242)",
     "shelfmark": "Arxiu Comarcal del Pallars Sobira, ACPS211-95 Archivo Ducal de Medinaceli, Casa Segorbe-Cardona, Seccion Pallars, T2-242",
     "note": "Instructions for cipher letters addressed to Antonio Ximeno, 1487, with a copy ('+ copia'); no further description, not online. Pre-1497: relevant to the oldest-cipher search."},
    {"title": "Valeria Weyler i Nicolau papers: 'Clau de xifrat' and 'Clau de xifrat numero 2' (ANC1-1458-T-62, -63)",
     "shelfmark": "Arxiu Nacional de Catalunya, ANC1-1458 Valeria Weyler i Nicolau, T-62 and T-63",
     "note": "Two undated cipher keys in Spanish, manuscript, one subfolder each; not online. The ciphers they serve are not identified."},
]
json.dump(keys, open(os.path.join(HERE, "key_leads.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(rows), "rows", len(keys), "keys")
