"""Vetting of leads 2712-2723 (sweep_2026-11-14_dutch_own_sites) and lead 2538; writes vetting.json and applies it.

    python research/vetting_2026-11-14_dutch_own_sites/make.py          write vetting.json and apply to research/leads.json
Promotion and closing are then done with docs/_check_catalogue.py (--promote / --close)."""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
BY = "claude session 14 Nov 2026 (Claude Sonnet 5.5), Dutch own-sites sweep vetting"
D = "2026-11-14"
DEC = "decode_search.py (de-crypt.org RecordsList), 14 Nov 2026: %s"
TOMO = "Web search naming Tomokiyo/Cryptiana with %s (14 Nov 2026): no Cryptiana page on this material; hits were Mary Queen of Scots and Spanish-cipher pages."
LAS = "Web search for Lasry/HistoCrypt with %s (14 Nov 2026): nothing; GL.htm in targets/gramont1529 has no entry for it (known.py)."
out = {}

out["2538"] = {
    "date": D, "by": BY,
    "seen": {"kind": "not online",
        "where": "Tresoar (Leeuwarden), toegang 1 'Bestuur van de Saksische hertogen over Friesland (originelen in Dresden en Wenen)', item records read through archieven.tresoar.nl/api/search (titles and notes), 14 Nov 2026: scan_count 0 and no iiif for every item; microfilm of Saechsisches Hauptstaatsarchiv Dresden, Geheimes Archiv Loc. 8183 (1510-1514 and 1514-1515). No scan online at either archive.",
        "extent": "29 letters of Duke George of Saxony to Cesar Pflug, 14 Mar - 6 Dec 1514, each described as 'in geheimschrift' (nos. 1134-1136, 1141, 1148, 1171, 1174, 1178, 1179, 1368-1372, 1380, 1393-1397, 1402-1405, 1407, 1412, 1420, 1421, 1430, 1432). Counted from the Tresoar titles: 9 carry 'afschrift (ontcijfering)' beside the despatch (1369, 1371, 1380, 1394-1397, 1404, 1412); 1134 has a 'vertaling in normaalschrift'; 1148, 1171, 1174, 1178 have a clear-text copy or minute (14 despatches with a clear text in all); 15 are despatch only.",
        "cipher": "Tresoar titles verbatim, e.g. no. 1396: 'Brief in geheimschrift van hertog George van Saksen aan zijn stadhouder te Leipzig, Cesar Pflug. Gegeven te Leeuwarden op 6 mei 1514. Afschrift (ontcijfering) en expeditie in geheimschrift'; no. 1134: 'Afschrift (vertaling in normaalschrift) en expeditie in geheimschrift'. Cipher type not described. The clear copies are in the Dresden volume and are not transcribed in the finding aid, which only summarises each letter."},
    "prior_art": {
        "decode": DEC % "'Pflug', 'Georg von Sachsen', 'Cesar Pflug', 'Friesland': 0 records each.",
        "tomokiyo": TOMO % "Duke George of Saxony, Pflug and Friesland 1514",
        "lasry": LAS % "Saxon ciphers of 1514",
        "edition": "Gess's Akten und Briefe zur Kirchenpolitik Herzog Georgs (vol. 1-4) covers 1517-1539 only (SAW Leipzig page; sehepunkte 2015/4 review), so not 1514. The Reichstagsakten (RTA MR 1513 ch. 4.2.3, Georg against Edzard) cover the quarrel, not these letters. Tresoar cites 'Posse (1897)' at inv. 1405; not identified or opened. No edition of the 1514 Pflug letters found.",
        "literature": "Anne-Simone Rous, Geheimdiplomatie in der Fruehen Neuzeit: Spione und Chiffren in Sachsen 1500-1763 (Steiner 2022) has a section 4.1.1 on Geheimschrift in Duke George's external relations, and a search snippet says George wrote to Pflug in a secret script and used it for 34 letters from Friesland; the book's full text was not reachable (dokumen.pub 403, pageplace preview is front matter only), so whether she deciphers or prints any of these letters is unchecked. The Sehepunkte review does not mention them."},
    "searches": [
        {"query": "decode_search.py Pflug; Georg von Sachsen; Cesar Pflug; Friesland (de-crypt.org)", "result": "0 records for each."},
        {"query": "Gess 'Politische Correspondenz des Herzogs Georg von Sachsen' 1500-1517 Friesland Pflug Ziffern (web search)", "result": "No such title; Gess's Akten und Briefe zur Kirchenpolitik starts in 1517."},
        {"query": "Herzog Georg von Sachsen Friesland 1514 Pflug Geheimschrift Dresden Loc. 8183 entziffert (web search)", "result": "Only Rous 2022 (Geheimdiplomatie in Sachsen), which mentions the letters to Pflug in secret script; nothing on a decipherment."},
        {"query": "Rous Geheimdiplomatie Georg Pflug Friesland Chiffre 1514 Datenbank (web search)", "result": "Rous's cipher database covers more than 1,300 key tables in the Saxon HStA; one source says George used a cipher for 34 letters from Friesland; database not public."}],
    "key_check": "No key known. The Saxon HStA Dresden holds over 1,300 folded cipher keys (Rous 2022); one for George's 1514 correspondence with Pflug may be among them, not checked. The 14 despatch-plus-clear-copy pairs in the same volume give known plaintext. One key (George to Pflug), as in the lead.",
    "duplicates": "known.py on 'Pflug', 'Georg von Sachsen', 'Boner', 'Hasselaer' (14 Nov 2026): only this lead, sweep rows of 11 and 14 Nov (lead 2712 is the same bundle, closed as its duplicate) and the Dutch OAI README. No catalogue entry holds Loc. 8183 or Tresoar toegang 1.",
    "verdict": "open",
    "lead_updates": {"access": "archive",
        "access_note": "No scans at Tresoar (microfilm only) or online at Dresden; order the film from Tresoar or Loc. 8183 from the Saechsisches Hauptstaatsarchiv. Rous 2022 sect. 4.1.1 to be read for any key.",
        "folio_note": "29 letters described as in or partly in 'geheimschrift' (list in vetting.seen.extent). 14 have a contemporary clear copy or minute beside the despatch (9 headed 'afschrift (ontcijfering)': 1369, 1371, 1380, 1394-1397, 1404, 1412; plus 1134, 1148, 1171, 1174, 1178). 15 are despatch only (1135, 1136, 1179, 1368, 1372, 1402, 1403, 1405, 1407, 1420, 1421, 1430, 1432 and the two copies of 21 June, 1141/1393); of these 1432 (5 June), 1420 (10 July) and 1402 (6 Sept) carry almost no summary in the inventory.",
        "prior_art": "vetted 14 Nov 2026 (see vetting block): DECODE 0, no Cryptiana or Lasry page, Gess 1517-39 only; Rous 2022 sect. 4.1.1 not read"}}

out["2713"] = {
    "date": D, "by": BY,
    "seen": {"kind": "not online",
        "where": "Tresoar (Leeuwarden), fonds 323 Familie Van Eysinga-Vegelin van Claerbergen, inv. 5592.53-56 (API node 2160932) and 5592.52 (node 2160931), item records read through archieven.tresoar.nl/api/nodes, 14 Nov 2026: scan_count 0 and scan_aanvraagbaar False; not digitised.",
        "extent": "Four letters (5592.53, .54, .55, .56) of stadholder Willem Lodewijk to Albert Everts Boner and Epe Jacobs Juckema, 1593; plus, as the key, one sheet (5592.52, c. 1593).",
        "cipher": "Tresoar note on 5592.53-56 verbatim: 'Inv. nrs. 5592-53-56 zijn in geheimschrift. Zie ook inv. nrs. 5592-53-46, 50'; 5592.52: 'Lijst met verklaringen van het geheimschrift zoals dat door stadhouder Willem Lodewijk en Gedeputeerde Staten van Friesland is gebruikt' (1588-1598, ca. 1593). Unlike catalogue 2547 (5592.23, .45, .51, partly in cipher) these four are described as wholly in cipher. No decipherment is mentioned."},
    "prior_art": {
        "decode": DEC % "'Willem Lodewijk' returns only W.L. van Wassenaer (1780s, Russia); 'Boner', 'Juckema' 0; no record of these letters.",
        "tomokiyo": TOMO % "Willem Lodewijk, Friesland and Boner 1593",
        "lasry": LAS % "Willem Lodewijk and Frisian ciphers",
        "edition": "Groen van Prinsterer's Archives de la maison d'Orange-Nassau (2e serie I, 1584-1599) has none of Boner, Juckema or Bourtange (grepped in the 11 Nov vetting of catalogue 2547); no edition of the Eysinga bundle found.",
        "literature": "Web searches of 11 and 14 Nov 2026 on Willem Lodewijk, Boner and Juckema with geheimschrift: nothing on these letters. Tresoar's own cipher-keyword list (32 items) is the only source."},
    "searches": [
        {"query": "decode_search.py Willem Lodewijk; Boner; Juckema; Casimir (de-crypt.org)", "result": "Only W.L. van Wassenaer 1780s; Casimir gives a Rakoczi record; nothing for these letters."},
        {"query": "archieven.tresoar.nl/api/nodes 2160909-2160932 (5592.23-.56)", "result": "5592.53-56 'zijn in geheimschrift'; 5592.52 the cipher list; all 0 scans."},
        {"query": "Tomokiyo / Lasry web search (14 Nov 2026)", "result": "Nothing on Willem Lodewijk's 1593 ciphers."}],
    "key_check": "The key list is in the volume (5592.52) and is not seen or tested. It may also be the missing key of targets/casimir1618 scan 027 (Willem Lodewijk to an unnamed officer, 5 Apr 1594, which says 'onse laetste cyffer seer duncker' and so the old cipher was kept): same writer, same two years, the cipher 'used by the stadholder and the Frisian States'. Not tested because neither is scanned here.",
    "key_in_volume": "Tresoar fonds 323 inv. 5592.52, list explaining the cipher used by Willem Lodewijk and the Gedeputeerde Staten of Friesland; not seen (no scan), not tested.",
    "duplicates": "Narrowed from the sweep row to the four wholly ciphered letters 5592.53-56 so that it does not repeat catalogue 2547 (5592.23, .45, .51). known.py '5592' and 'Boner' (14 Nov 2026): lead 2713, catalogue 2547 and sweep rows only. Shares the key (5592.52) with 2547; one key per entry is kept because each entry lists different letters.",
    "verdict": "open",
    "lead_updates": {"access": "archive",
        "title": "Stadtholder Willem Lodewijk's four letters wholly in cipher to Albert Everts Boner and Epe Jacobs Juckema, 1593, with the list explaining the cipher he and the Frisian States used (same key list as catalogue 2547)",
        "year": 1593, "date": "1593",
        "shelfmark": "Tresoar (Leeuwarden), 323 Familie Van Eysinga-Vegelin van Claerbergen, inv. nrs. 5592.53-56 (key list 5592.52)",
        "folio_note": "Four pieces, 5592.53-56 (API node 2160932), 'zijn in geheimschrift'; the key list is 5592.52 (node 2160931), c. 1593",
        "status": "Finding aid read through Tresoar's API on 14 Nov 2026; Tresoar scan count 0, not digitised. Neither the letters nor the list were seen.",
        "prior_art": "vetted 14 Nov 2026 (see vetting block): DECODE, Cryptiana, Lasry, Groen van Prinsterer: nothing",
        "links": [{"label": "Tresoar 5592.53-56 (JSON)", "href": "https://archieven.tresoar.nl/api/nodes/2160932"},
                  {"label": "Tresoar cipher list 5592.52 (JSON)", "href": "https://archieven.tresoar.nl/api/nodes/2160931"}]}}

out["2716"] = {
    "date": D, "by": BY,
    "seen": {"kind": "not online",
        "where": "Tresoar (Leeuwarden), toegang 2 'Bestuur van Friesland (originelen in Brussel)', collective description node 1008815 read through archieven.tresoar.nl/api/nodes, 14 Nov 2026: scan_count 0, scan_aanvraagbaar False; Tresoar holds microfiche only (Inv. 588 ff. 1-416, 589 ff. 1-301); originals in Brussels.",
        "extent": "Parma's correspondence with the stadholder Rennenberg and others, 16 Mar 1579 - 16 Jul 1582 (Brussels inv. 588-589, about 717 folios); an unstated number of letters 'partly in cipher', from fiche 588 f. 20 onward.",
        "cipher": "Tresoar note verbatim: 'Sommige brieven zijn gedeeltelijk in geheimschrift (Fiche: Inv.nr. 588, f.20 en verder)'. No decipherment is mentioned. Not seen: no image online."},
    "prior_art": {
        "decode": DEC % "'Rennenberg' 0, 'Lalaing' 0, 'Parma Groningen' 0. 'Farnese' gives BnF records of 1579-1591 (e.g. R2017 BnF Espagnol 132 f.233-234, Maastricht 1579, decrypted) which are other letters of the same circle, not these.",
        "tomokiyo": TOMO % "Parma, Rennenberg and Groningen 1579",
        "lasry": LAS % "Rennenberg",
        "edition": "F.U. Ros, Rennenberg en de Groningse malcontenten (Nijmegen 1964) has a register of the Parma-Rennenberg-Groningen letters of 1579-81 (found by web search; the full text is blocked, 403 to curl and Chrome, so whether it reads or prints the cipher passages is not checked). Wagenaar, Vaderlandsche historie vol. 7, retells the affair. No Gachard edition of these letters found.",
        "literature": "Violet Soen, Vredehandel (2011) lists the Groningen and Rennenberg reconciliation file; none of the hits mentions a cipher."},
    "searches": [
        {"query": "decode_search.py Farnese; Alexander Farnese; Lalaing; Rennenberg (de-crypt.org)", "result": "No Rennenberg or Lalaing record; Farnese: BnF records of other letters."},
        {"query": "Parma Rennenberg Groningen 1579 1582 correspondentie chiffre uitgave (web search)", "result": "Ros 1964 dissertation (Radboud repository, 403), Soen 2011; nothing on a cipher edition."},
        {"query": "Tomokiyo/Lasry web search (14 Nov 2026)", "result": "Nothing."}],
    "key_check": "No key known. Farnese's 1579 chiffres are on DECODE for other letters (BnF Esp. 132) and might be the same family; not tested because no image of these letters exists online.",
    "duplicates": "known.py 'Lalaing' and 'Farnese' (14 Nov 2026): Farnese hits are other catalogue items (621, Tassis 1583, Doria Genoa legajos); nothing holds Tresoar toegang 2 or Brussels inv. 588-589.",
    "verdict": "open",
    "lead_updates": {"access": "archive",
        "prior_art": "vetted 14 Nov 2026 (see vetting block): DECODE 0 for Rennenberg; Ros 1964 register not opened (403)"}}

out["2717"] = {"verdict": "not_cipher",
    "closed": "Tresoar fonds 323 nos. 4036-4047 (Vegelin van Claerbergen journals 1707-16): the note says 'Voor een deel in geheimschrift, in het Grieks' (partly in secret writing, in Greek), i.e. a young man's private passages in the Greek language or alphabet, not a cipher system. Not seen (scan_count 0); judged from the finding aid on 14 Nov 2026; reopen if the pages show non-Greek signs."}
out["2715"] = {"verdict": "duplicate", "closed": "same folder as catalogue 1982 (KHA A24-8, 1640 letters partly in cipher to and from Hendrik Casimir I of Nassau-Dietz): Tresoar fonds 7-05 'De archieven in het Koninklijk Huisarchief: Hendrik Casimir I' no. 8 is the KHA A24-8 folder (14 Nov 2026)."}
out["2712"] = {"verdict": "duplicate", "closed": "same letters as lead 2538 (Duke George of Saxony to Cesar Pflug, 1514, Tresoar toegang 1 nos. 1134-1432 / Dresden Loc. 8183), which already lists them with their clear copies; 2538 carries the vetting (14 Nov 2026)."}

KEYS = "Key book or key sheet only; no ciphertext in the entry, so there is nothing to read until a letter in this cipher turns up. "
out["2714"] = {"unvetted": KEYS + "Viewed on the Amsterdam IIIF images on 14 Nov 2026 (two scans, one table of plain letters against numerals and signs). Hasselaer fonds 292 inv. 156; Pieter Vogelesangh (1616-63) and the date of the sheet not verified; DECODE 0 for Vogelesangh and Hasselaer. Kept as a lead for a matching ciphertext."}
out["2718"] = {"unvetted": "Only an introduction node (Tresoar 1009755, 'Formulaires et chiffres', inv. 646/2-646/6 of the original Brussels inventory, dated '1199-1221', a misprint) under 'Affaires diverses' of the Audience; no item description, 0 scans; 'chiffres' may mean figures. Nothing viewed."}
for i, s in (("2719", "Battier, Spanje: NA 1.10.110 inv. 2 sect. 2.11 nos. 184-186. Probably another copy of the key already held for targets/battier1686 (NA 1.10.29 Fagel inv. 1209, 'Voor den Heer Extraord. Envoye Battier'); 186 availability PHYSICAL, no scans (NA clevel API, 14 Nov 2026). DECODE R2794 is the Fagel Battier cipher."),
             ("2720", "Van Rechteren, Denemarken: NA 1.10.110 no. 187, codeboek; PHYSICAL, no scans (NA clevel API, 14 Nov 2026)."),
             ("2721", "Buijs, Denemarken: NA 1.10.110 no. 183, codeboek; no scans known (14 Nov 2026)."),
             ("2722", "Van Burmania, Wenen: NA 1.10.110 no. 179; no scans known (14 Nov 2026)."),
             ("2723", "Van Toulon, 'Sleutels voor geheimschriften': NA 2.21.227 no. 336, PHYSICAL, 0 scans (14 Nov 2026).")):
    out[i] = {"unvetted": KEYS + s}
json.dump(out, open(os.path.join(HERE, "vetting.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)

sys.path.insert(0, os.path.join(ROOT, "docs"))
import _check_catalogue as C
d, leads = C.load(C.LEADS, "leads")
byid = {str(l["id"]): l for l in leads}
for i, b in out.items():
    l = byid[i]
    if "unvetted" in b:
        l["vetting_note"] = b["unvetted"]; continue
    if b["verdict"] != "open":
        v = l.setdefault("vetting", {}); v.update(verdict=b["verdict"], closed=b["closed"], date=D); continue
    b = dict(b); l.update(b.pop("lead_updates", {})); l["vetting"] = b; l.pop("vetting_note", None)
C.save(C.LEADS, d)
print("applied", len(out))
