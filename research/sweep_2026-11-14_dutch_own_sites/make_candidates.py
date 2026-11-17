"""Builds candidates.json for the 14 Nov 2026 Dutch own-sites sweep (rows scored from finding-aid text; none opened except the Vogelesangh key)."""
import json
TS = 'https://archieven.tresoar.nl/api/nodes/'
SRC_T = "Tresoar's own archives site (archieven.tresoar.nl, open JSON API /api/search), 14 Nov 2026"
SRC_N = "Nationaal Archief inventory API (zvt.nationaalarchief.nl), spelling-variant re-run, 14 Nov 2026"
SRC_A = "Stadsarchief Amsterdam search API (id.archief.amsterdam /search/records, behind beta.archief.amsterdam), 14 Nov 2026"


def row(**k):
    base = dict(seen='catalogue', needs_archive_scan='yes')
    base.update(k)
    return base


rows = []
rows.append(row(
    year=1514, date="March-December 1514",
    title="Duke George of Saxony's ciphered letters to his governor Cesar Pflug at Leipzig, written in Friesland during the Saxon campaign, 1514 (about 30 letters, 9 with the contemporary decipherment copied beside them)",
    correspondents="Duke George of Saxony (in Friesland: Leeuwarden, Aduard, Appingedam, Schuettorf, Coevorden) -> Cesar Pflug, stadtholder at Leipzig; a few to Hugo von Leisnig",
    place="Friesland / Leipzig", language="German", region="Germany", period="1497-1559",
    shelfmark="portal repository NL-04-0041-000, fonds 1, nos. 1134-1136, 1141, 1148, 1171, 1174, 1178-1179, 1368-1372, 1380, 1393-1397, 1402-1405, 1407, 1412, 1420-1421, 1430, 1432 (originals Dresden, Loc. 8183)",
    folio_note="Tresoar toegang 1 'Bestuur van de Saksische hertogen over Friesland (originelen in Dresden en Wenen)'. Each regest gives the Dresden find-spot ('Vpl'), e.g. Loc. 8183 1510-1514 fol. 203-209 (Nov and Mar 1514) and Loc. 8183 1514-1515 fol. 17-170, with the film order. Nine items (inv. 1369, 1371, 1380, 1394-1397, 1404, 1412) carry 'afschrift (ontcijfering)' in the title, so cipher text and decipherment are both filed; inv. 1134, 1171, 1174 also list an expedition plus an afschrift. Many are 'Expeditie, opgedrukt zegel is verloren gegaan' (the sent original)",
    cls="A",
    status="Inventory regests only, read 14 Nov 2026 through Tresoar's JSON API (titles and notes). 31 items name 'geheimschrift'; the Dresden originals were not viewed and Tresoar's scan count is 0. No decipherment or edition of the cipher passages found (one WebSearch only).",
    why="Pairs of cipher letter and contemporary decipherment, 1514, from one sender to one recipient over eight months: a known-plaintext set from the first decades of the 16th century, earlier than almost anything else in the catalogue except the 15th-century items. The camp letters (Aduard, Appingedam) show the cipher in daily use. One key (George to Pflug); the Leisnig item is a different correspondent.",
    importance=4, solvability=4, difficulty=3,
    score_note="Scored from the Tresoar finding aid (research/sweep_2026-11-14_dutch_own_sites/); the originals were not viewed. Solvability assumes the Dresden ciphers can be photographed",
    verify="Order or fetch Dresden Loc. 8183 (1514-1515) fol. 65-66 and 160-162/1 (inv. 1393, text in clear and cipher) and fol. 74-77 (inv. 1396, decipherment and expedition); ask Tresoar for their film; check Gess's Politische Correspondenz des Herzogs Georg and Posse 1897 (cited at inv. 1405) for printed decipherments; look for digital images of Loc. 8183 in the Saxon State Archive's online finding aid.",
    links=[{"label": "Tresoar keyword Geheimschrift, 32 items (JSON)", "href": "https://archieven.tresoar.nl/api/nodes/by-trefwoord?field=twd&value=Geheimschrift&limit=100"}],
    source=SRC_T,
    prior_art="open as far as checked (14 Nov 2026): known.py on Pflug, Georg von Sachsen, Saxon, 'Bestuur van de Sak' finds nothing relevant; one German WebSearch found no decipherment; DECODE, Tomokiyo and Lasry not searched; Gess's edition not opened",
    access_note="Tresoar holds film and regests; the ciphertexts are in the Saechsisches Hauptstaatsarchiv Dresden (Loc. 8183, 8193); digitisation not checked"))

rows.append(row(
    year=1591, date="1588-1598 (letters 1589-1593)",
    title="Stadtholder Willem Lodewijk's ciphered letters to Albert Everts Boner and Epe Jacobs Juckema, with the list explaining the cipher he and the Frisian States used",
    correspondents="Willem Lodewijk of Nassau-Dillenburg -> Albert Everts Boner and Epe Jacobs Juckema (Frisian deputies)",
    place="Friesland", language="Dutch", region="Low Countries", period="1589-1598",
    shelfmark="portal repository NL-04-0041-000, fonds 323 (Van Eysinga-Vegelin van Claerbergen), no. 5592 (sub-items 5592-45, 5592-50, 5592-53 to -56 and the cipher list)",
    folio_note="Notes: '5592-53-56 zijn in geheimschrift. Zie ook 5592-50' and '5592-45 is voor een deel in geheimschrift'; four pieces each; the separate item 'Lijst met verklaringen van het geheimschrift zoals dat door stadhouder Willem Lodewijk en Gedeputeerde Staten van Friesland is gebruikt', 1588-1598",
    cls="A",
    status="Finding aid only (titles and notes read 14 Nov 2026); Tresoar scan count 0. Neither the ciphertexts nor the list were viewed.",
    why="Ciphertext and the cipher list of the same user sit in one fonds. The 1594 Willem Lodewijk letter in target casimir1618 lacks its key; this list (1588-98, 'used by the stadholder and the Frisian States') is a candidate for it, and 5592-53 to -56 are further ciphertexts in the same system.",
    importance=3, solvability=4, difficulty=3,
    score_note="Scored from the Tresoar finding aid; not viewed. Separate from catalogue 1950-1953 (fonds 7-02, the Nassau secretary's files)",
    verify="Request the scans of inv. 5592 at Tresoar; compare the list with the 1594 letter in targets/casimir1618 and with KHA A23-311 and A22-191, -195.",
    links=[{"label": "Tresoar cipher list (JSON)", "href": TS + "2160931"}, {"label": "Tresoar letters 1593 (JSON)", "href": TS + "2160925"}],
    source=SRC_T,
    prior_art="open as far as checked (14 Nov 2026): known.py on Boner, Juckema, Eysinga, 5592 finds nothing about this fonds; no DECODE, Tomokiyo or Lasry search",
    access_note="not digitised at Tresoar as far as its API shows (scan_count 0); order scans"))

rows.append(row(
    year=1660, date="undated, between about 1650 and 1663 (estimate)",
    title="Cipher key 'Cyffer tot de correspondentie te houden met de Heer Pensionaris Vogelsangh', Amsterdam Hasselaer family archive",
    correspondents="correspondents of the Pensionary Vogelesangh (the finding aid files it under Mr Pieter Vogelesangh, 1616-1663)",
    place="Amsterdam", language="Dutch", region="Low Countries", period="1651-1700",
    shelfmark="Stadsarchief Amsterdam, 292 (Archief van de familie Hasselaer en aanverwante families), inv. 156",
    folio_note="2 scans (KLAG03032000001, -2). Scan 1: the heading and a two-line table, the lower line the plain alphabet and the upper line numerals and flourished signs; scan 2 is blank except for a docket",
    cls="C",
    status="Viewed 14 Nov 2026 on the IIIF images. The finding-aid title says 'Opgaaf voor de ontcijfering van de correspondentie'. It is a key; no letter in this cipher found in the same file.",
    why="A real 17th-century Dutch cipher alphabet (numeral and sign substitution) from a named pensionary's correspondence, already digitised: a known key if a letter from or to Vogelesangh turns up (Amsterdam city archives, other Dutch cities, States General).",
    importance=2, solvability=3, difficulty=2,
    score_note="Scored from the viewed key page (research/sweep_2026-11-14_dutch_own_sites/); no ciphertext known",
    verify="Identify the Pensionary Vogelesangh and date the sheet; search the Hasselaer fonds and the Amsterdam city archives for letters 'in cijffer' to or from him; transcribe the table from the full-size image.",
    links=[{"label": "scan 1 (IIIF)", "href": "https://id.archief.amsterdam/resources/iiif/3/efd6ea45-2eae-4c3c-b40d-077498f16617/full/1000,/0/default.jpg"},
           {"label": "scan 2 (IIIF)", "href": "https://id.archief.amsterdam/resources/iiif/3/ce90beee-643b-4083-a0df-dface472f9db/full/1000,/0/default.jpg"}],
    source=SRC_A,
    prior_art="open as far as checked (14 Nov 2026): known.py on Vogelesangh, Vogelsangh, Hasselaer finds nothing; no DECODE, Tomokiyo or Lasry search; identity and date of the Pensionary not verified",
    needs_archive_scan="no", access_note="digitised; images open through the Stadsarchief IIIF service"))

rows.append(row(
    year=1640, date="1640 and undated",
    title="Letters to Hendrik Casimir I of Nassau-Dietz partly in cipher, 1640, with his draft replies partly in cipher; cipher 'partly deciphered'",
    correspondents="various correspondents -> Hendrik Casimir I of Nassau-Dietz (stadholder of Friesland); his minutes",
    place="Friesland / The Hague", language="Dutch", region="Low Countries", period="1611-1650",
    shelfmark="portal repository NL-04-0041-000, fonds 7-05, no. 8",
    folio_note="One folder; the note reads 'Geheimschrift gedeeltelijk ontcijferd'. Held in the Koninklijk Huisarchief, described in Tresoar's Stadhouderlijk archief 7-05",
    cls="B",
    status="Finding aid only (read 14 Nov 2026); not viewed. The KHA call number of the folder is not given by Tresoar.",
    why="Cipher letters of 1640 with a part decipherment on the same folder; the same stadholder family's ciphers as catalogue 1954-1956 (Zutphen 1629, Andreae 1645-53).",
    importance=3, solvability=3, difficulty=3,
    score_note="Scored from the finding aid; not viewed",
    verify="Find the KHA number (series A24, Hendrik Casimir I) and its scans on koninklijkeverzamelingen.nl; test the Zutphen 1629 key (A23-203) and the casimir1618 keys against it.",
    links=[{"label": "Tresoar record (JSON)", "href": TS + "947347"}],
    source=SRC_T,
    prior_art="open as far as checked (14 Nov 2026): known.py on 'Hendrik Casimir' finds only other files (catalogue 1954, 1955); this folder is not listed; no DECODE, Tomokiyo or Lasry search",
    access_note="KHA scans not checked"))

rows.append(row(
    year=1579, date="16 March 1579 - 16 July 1582",
    title="Parma, Rennenberg and others on the Groningen reconciliation, 1579-1582: some letters partly in cipher (microfiche of Brussels originals)",
    correspondents="Alexander Farnese, Duke of Parma; Georges de Lalaing, Count of Rennenberg; Groningen correspondents",
    place="Groningen / Brussels", language="French; Dutch; German; Italian", region="Low Countries", period="1560-1589",
    shelfmark="portal repository NL-04-0041-000, fonds 2 (Bestuur van Friesland, originelen in Brussel), original inv. 588-589, fiche inv. 588 f.20 ff.",
    folio_note="Tresoar note: 'Sommige brieven zijn gedeeltelijk in geheimschrift (Fiche: Inv.nr. 588, f.20 en verder)'; 588 runs 16 Mar 1579-26 Dec 1580 (ff.1-416), 589 2 Jan 1581-16 Jul 1582 (ff.1-301). Separately, fiche inv. 293 f.189v (1567, Leeuwarden agreement) is 'gedeeltelijk in geheimschrift'",
    cls="B",
    status="Description only (14 Nov 2026). The originals are in Brussels; Tresoar holds fiches. Whether a decipherment is filed with them is not stated.",
    why="A cipher of the governor-general's circle at the Groningen defection, with a fiche copy in the Netherlands.",
    importance=3, solvability=2, difficulty=4,
    score_note="Scored from the finding aid; the fiche was not seen",
    verify="Ask Tresoar for fiche 588 f.20 ff.; identify the Brussels call number; check Gachard and the Groningen sources for printed decipherments; check Parma's keys among DECODE's Farnese records.",
    links=[{"label": "Tresoar record (JSON)", "href": TS + "1008815"}],
    source=SRC_T,
    prior_art="open as far as checked (14 Nov 2026): known.py not run on Parma or Rennenberg (many Farnese hits expected from other leads); no DECODE, Tomokiyo or Lasry search",
    access_note="fiche at Tresoar; originals in Brussels, digitisation not checked"))

rows.append(row(
    year=1710, date="1707-1716",
    title="Johan Vegilin van Claerbergen's travel journals and letters to his father, partly in a secret script in Greek letters (inv. 4036-4047)",
    correspondents="Johan Vegilin van Claerbergen -> his father Hessel; his brother Philip Frederik travelled with him",
    place="Southern Netherlands (Maastricht, Dunkirk, 's-Hertogenbosch, Namur)", language="Dutch in Greek letters (note: 'in geheimschrift, in het Grieks')", region="Low Countries", period="1701-1800",
    shelfmark="portal repository NL-04-0041-000, fonds 323 (Van Eysinga-Vegelin van Claerbergen), nos. 4036-4047 (journals 1709-1715 at 4039-4046)",
    folio_note="At least seven yearly journals (1709 to 1715); the note says 'Voor een deel in geheimschrift, in het Grieks. Mogelijk voor een deel in functie opgesteld'",
    cls="C",
    status="Finding aid only; not viewed. 'Secret script in Greek' may mean Dutch written in the Greek alphabet, which would be quickly solvable.",
    why="Long private journals with a script cover for sensitive passages, early 18th century; probably a transliteration, so easy once scans exist.",
    importance=2, solvability=4, difficulty=1,
    score_note="Scored from the finding aid; not viewed",
    verify="Request scans of 4039-4046; read a Greek-letter passage; if it is a plain transliteration, decide whether this is a cipher target at all.",
    links=[{"label": "Tresoar record (JSON)", "href": TS + "1201591"}],
    source=SRC_T,
    prior_art="open as far as checked (14 Nov 2026): known.py on Vegelin, Eysinga finds nothing",
    access_note="scan_count 0 at Tresoar"))

rows.append(row(
    year=1600, date="given as 1199-1221 in the finding aid (obviously a misprint)",
    title="'Formulaires et chiffres' in the Brussels files on the administration of Friesland, inv. 646/2-646/6",
    correspondents="Habsburg administration of Friesland (Brussels originals)",
    place="Brussels", language="French", region="Low Countries", period="unknown",
    shelfmark="portal repository NL-04-0041-000, fonds 2 (Bestuur van Friesland, originelen in Brussel), original inv. 646/2-646/6",
    folio_note="Listed in the introduction as 'Formulaires et chiffres (Inv.nrs. 646/2-646/6, 1199-1221)'; the introduction also says some pieces are 'gesteld in geheimtaal (vrijwel altijd inclusief de ontcijfering)'",
    cls="C",
    status="Introduction text only (14 Nov 2026); no item-level description; not viewed. Date unreliable.",
    why="Key and form-book material for the Habsburg government's secret correspondence about Friesland; the same introduction says ciphered pieces nearly always come with their decipherment, which would make the Frisian files a plaintext and ciphertext source.",
    importance=2, solvability=2, difficulty=3,
    score_note="Scored from the introduction only",
    verify="Find the Brussels call numbers behind 646/2-646/6 and the date; check whether Tresoar's fiches cover them.",
    links=[{"label": "Tresoar introduction node (JSON)", "href": TS + "1009755"}],
    source=SRC_T,
    prior_art="open as far as checked (14 Nov 2026): known.py not run beyond the phrase; no DECODE, Tomokiyo or Lasry search",
    access_note="description only"))

NA = "Nationaal Archief, The Hague, 1.10.110 (Overige gezanten, 17e en 18e eeuw), inv. 2, section 2.11 'Cijfers', no. "
nal = [
    ("184-186", 1690, "Battier, Spanje: 'Chijffer voor den Heer extraordinaris Envoije Battier' and codeboeken (184-185, 186)", "Battier (Dutch envoy to Spain; sibling of target battier1686)", "Madrid", "2~2.11~186"),
    ("187", 1750, "Van Rechteren, Denemarken: codeboek", "Van Rechteren (Dutch envoy to Denmark; not catalogue 232, Rechteren at St Petersburg 1785)", "Copenhagen", "2~2.11~187"),
    ("183", 1750, "'Cijffer voor de heer Buijs, extraordinaris Envoije en Plenipotentiaris in Denenmarken': codeboek", "Buijs (Dutch envoy at Copenhagen)", "Copenhagen", "2~2.11~183"),
    ("179", 1750, "Van Burmania, Wenen: 'cijffer met de ministers te Stokholm, Weenen en Petersburg'", "Burmania (Dutch envoy at Vienna) with the ministers at Stockholm, Vienna and St Petersburg", "Vienna", "2~2.11~179"),
]
for nr, y, t, c, pl, cid in nal:
    rows.append(row(
        year=y, date="undated in the finding aid (17th-18th c. envoy papers)",
        title="Envoy cipher key: " + t, correspondents=c, place=pl, language="Dutch", region="Low Countries", period="unknown",
        shelfmark=NA + nr, folio_note="PHYSICAL only; 0 scans (NA API availability field)", cls="C",
        status="Inventory line only (NA API re-run with the spelling variants 'chijffer' and 'codeboek', 14 Nov 2026); not viewed.",
        why="Held key books of Dutch envoys; the key side for letters of the same envoys (Staten-Generaal Secrete kas, 1.01.02 section VI.C) and for DECODE records of the same senders. The year is a placeholder.",
        importance=2, solvability=2, difficulty=3,
        score_note="Scored from the NA inventory line; year is a placeholder",
        verify="Order a scan of the volume; establish the envoy's years and match them to letters in 1.01.02 or on DECODE.",
        links=[{"label": "NA clevel API", "href": "https://zvt.nationaalarchief.nl/api/eads/1.10.110/clevels/" + cid}],
        source=SRC_N,
        prior_art="open as far as checked (14 Nov 2026): known.py on 1.10.110 finds only the Oct 2026 NA sweep README (lead 4, '1619 Cijfers') and scan_requests; Burmania only in siblings_nov9; no DECODE, Tomokiyo or Lasry search",
        access_note="NA physical items; scan on demand"))

rows.append(row(
    year=1801, date="undated (about 1799-1803)",
    title="'Sleutels voor geheimschriften', partly in Lodewijk van Toulon's hand, Van Toulon family archive",
    correspondents="Lodewijk van Toulon (1767-1840), Batavian Republic foreign service", place="The Hague", language="Dutch", region="Low Countries", period="1801-1900",
    shelfmark="Nationaal Archief, The Hague, 2.21.227 (Van Toulon van der Koog), 2.5.2.2.1.4, no. 336",
    folio_note="'Ongedateerd, ontwerpen (?)'; next to no. 335, the Correspondentiecijffer already used in target toulon1803 (key physical at NA 2.21.045/34313)",
    cls="C", status="Inventory line only; PHYSICAL, 0 scans (NA API 14 Nov 2026).",
    why="Further Toulon key drafts that may bear on the open Toulon 1803 and Croiset-series letters (catalogue 230, DECODE R2034, R1942).",
    importance=2, solvability=2, difficulty=3, score_note="Scored from the NA inventory line",
    verify="Request a scan of no. 336 with no. 335 and the booklet NA 2.21.045/34313; compare with targets/toulon1803.",
    links=[{"label": "NA clevel API", "href": "https://zvt.nationaalarchief.nl/api/eads/2.21.227/clevels/2.~2.5.~2.5.2.~2.5.2.2.~2.5.2.2.1.~2.5.2.2.1.4.~336"}],
    source=SRC_N,
    prior_art="open as far as checked (14 Nov 2026): known.py 'Toulon' finds catalogue 230, targets/toulon1803 and the APE sweep, which names 2.21.227-336 but made no row",
    access_note="NA physical; scan on demand"))

json.dump(rows, open('candidates.json', 'w', encoding='utf8'), ensure_ascii=False, indent=1)
print(len(rows))
