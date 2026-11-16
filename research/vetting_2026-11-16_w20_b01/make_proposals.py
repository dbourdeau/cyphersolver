"""Write proposals.json for wave 20 batch b01 (16 Nov 2026)."""
import json
D = "2026-11-16"
BY = "claude session 16 Nov 2026 (Claude Opus 5.5), wave 20 vetting"
TOMO = "Tomokiyo's unsolved.htm (fetched 15 Nov 2026) grepped, tags stripped, for {t}: no hit."
LAS = "Lasry's GL.htm list (fetched 15 Nov 2026) grepped for {t}: no hit on this item."
P429 = ("PARES (pares.cultura.gob.es) still answered HTTP 429 on 16 Nov 2026 to curl from this machine and to WebFetch from a "
        "different network, so the full record, its notes and any images were not reopened; the record text used is the one saved in "
        "research/pares_ags/hits.jsonl and research/sweep_2026-11_spain_nobility_aca/screen.json (27 Oct and 9 Nov 2026).")
P = {}

P["2711"] = {
 "verdict": "not_cipher", "confidence": "medium",
 "note": "The PARES description says the first document 'se compone fundamentalmente de una serie de cifras' with a marginal note 'Dos copias para Sánchez Román y otra para la demanda', beside a list of 1906 plenary dates: in this modern Michelena family fonds 'cifras' means figures (numbers) copied for a lawyer and a lawsuit, not a cipher. Images not seen because PARES answered 429.",
 "access": "online", "access_note": "PARES flags images for MICHELENA,C.18,D.142-143 (record 4025233); not viewable on 16 Nov 2026 (HTTP 429).",
 "correct_date": "c. 1906 (the companion list is of 1906 plenary sessions; the lead's year 1800 is a placeholder)",
 "vetting": {
  "date": D, "by": BY,
  "seen": {"kind": "not online",
   "where": "PARES record 4025233 (AHNOB, MICHELENA,C.18,D.142-143), description text as saved in research/pares_ags/hits.jsonl on 27 Oct 2026; " + P429,
   "extent": "Two undated documents; the first is described as mainly a series of figures with a marginal note, the second as a list of dates of plenary sessions held in 1906.",
   "cipher": "Archive description, verbatim: 'El primero se compone fundamentalmente de una serie de cifras y, en el margen del mismo, aparece una nota que dice: \"Dos copias para Sánchez Román y otra para la demanda (¿)\". El segundo es una lista de fechas en que se celebraron unos plenos (en 1906)'. Read in context this is a numeric list for a lawsuit (Felipe Sánchez Román was a Madrid jurist of that time), not ciphertext; no cipher system is described."},
  "prior_art": {
   "decode": "known.py on 'MICHELENA,C.18', 'Sánchez Román' and 'Sanchez Roman': no DECODE record, ledger, catalogue or target hit beyond this lead.",
   "tomokiyo": TOMO.format(t="Michelena and Sánchez Román"),
   "lasry": LAS.format(t="Michelena and Sánchez Román"),
   "edition": "No edition: an anonymous undated working paper of a late-modern family fonds; nothing printed was looked for beyond the web search.",
   "literature": "One web search (Michelena, Archivo Histórico de la Nobleza, Sánchez Román) found other MICHELENA records (papers of Pedro José Moreno Rodríguez, notes on public-debt securities, C.8 and C.10), consistent with a 19th-20th-century family and business fonds; nothing on this document."},
  "key_check": "No key concerned: the document is described as figures, not a cipher; no key in the fonds was looked for.",
  "duplicates": "known.py on the shelfmark and names found nothing; no other lead or catalogue entry cites MICHELENA,C.18.",
  "verdict": "not_cipher",
  "closed": "Closed as not a cipher: the archive's own description makes the 'cifras' a numeric list copied for a lawyer and a lawsuit in a 1906-era family fonds; reopen only if the PARES images show symbol or code groups."}}

P["2708"] = {
 "verdict": "open", "confidence": "medium",
 "note": "PARES describes FRIAS,C.1887,D.93-98 as 'Correspondencia cifrada remitida por el príncipe de Ligni [Claude Lamoral I] dirigida al conde de Oropesa', six documents 26 Sep-24 Oct 1670, no images and no decipherment mentioned; nothing on DECODE, Tomokiyo, Lasry or in print. Record error: Ligne was then viceroy of Sicily (Parliament, castles, Messina), so the place is Sicily -> Madrid, not Brussels -> Madrid.",
 "access": "archive", "access_note": "No images on PARES (hit-list flag false); needs an AHNOB (Toledo) reproduction order.",
 "correct_place": "Sicily (Palermo/Messina) -> Madrid",
 "vetting": {
  "date": D, "by": BY,
  "seen": {"kind": "not online",
   "where": "PARES record 13187073 (AHNOB, FRIAS,C.1887,D.93-98), description as saved 27 Oct and 9 Nov 2026; " + P429,
   "extent": "Six documents dated 26 Sep to 24 Oct 1670 described as cipher correspondence; how many lines or pages are in cipher is not stated.",
   "cipher": "Archive description, verbatim: 'Correspondencia cifrada remitida por el príncipe de Ligni [Claude Lamoral I] dirigida al conde de Oropesa [Duarte Fernando Álvarez de Toledo Portugal] relativa a la convocatoria que ha hecho del Parlamento para reforzar los castillos y plazas, el arrepentimiento de los Blancos y los negocios de Mesina.' No decipherment, translation or clear copy is mentioned; AHNOB titles in these fonds do name filed decipherments when present ('con sus traducciones', 'está descifrada')."},
  "prior_art": {
   "decode": "known.py on 'FRIAS,C.1887', 'Ligni', 'Ligne' and 'Oropesa': no DECODE record or catalogue entry for this unit; the 9 Nov spain_nobility_aca README lists it only as 'cipher letters, no images; not screened further'.",
   "tomokiyo": TOMO.format(t="Ligni, Ligne, Oropesa and FRIAS"),
   "lasry": "Lasry's GL.htm list (fetched 15 Nov 2026) grepped for Ligni, Ligne, Oropesa: only unrelated matches (the name 'Lignerac' and the word 'lignes' in French BnF items); nothing on this correspondence.",
   "edition": "No edition of Ligne's Sicilian viceregal letters to Oropesa found; the letters are not calendared with a text in any work turned up by the web search.",
   "literature": "Web search (príncipe de Ligne virrey Sicilia 1670 Oropesa cartas cifradas Mesina) found studies of Ligne's viceroyalty of Sicily 1670-74 (defence against the Ottomans, Merelli's atlas) and of Messina in 1674-78, none citing these cipher letters or a decipherment."},
  "key_check": "No Ligne or Oropesa key is held here or on DECODE as far as known.py shows; Spanish viceregal ciphers of the 1670s (e.g. targets/aragon1676) are a different correspondence and were not tried, since the letters are not online.",
  "duplicates": "known.py on the shelfmark, both correspondents and 'Oropesa' found only unrelated targets (aragon1676, battier1686) and this lead; no duplicate in the catalogue or leads.",
  "verdict": "open"}}

P["2709"] = {
 "verdict": "open", "confidence": "low",
 "note": "Open for FRIAS,C.635,D.33-41 only: PARES describes it as 'Felipe IV, por cédula y despacho cifrado, nombra Gobernador interino del Estado de Milán al Conde de Haro' (30 Sep 1647), no images, no decipherment mentioned. The second record cited, FRIAS,C.1389,D.28 (PARES 3949446), names no cipher in its title (the hit came from unseen text) and should be dropped from this entry until its record is read.",
 "access": "archive", "access_note": "No images on PARES for either record; AHNOB reproduction order needed.",
 "correct_shelfmark": "AHNOB, FRIAS,C.635,D.33-41 (drop FRIAS,C.1389,D.28 from the entry)",
 "vetting": {
  "date": D, "by": BY,
  "seen": {"kind": "not online",
   "where": "PARES record 3948294 (AHNOB, FRIAS,C.635,D.33-41) and 3949446 (FRIAS,C.1389,D.28), titles as saved in research/pares_ags/hits.jsonl and screen.json; " + P429,
   "extent": "Nine documents of 30 Sep 1647 including a royal cédula and a despatch described as in cipher; the cipher extent is not stated.",
   "cipher": "Archive description, verbatim: 'Felipe IV, por cédula y despacho cifrado, nombra Gobernador interino del Estado de Milán al Conde de Haro [Íñigo Melchor Fernández de Velasco].' No decipherment or clear copy is mentioned. For C.1389,D.28 the title ('Carta de Felipe IV al Conde de Haro sobre la pretensión del Conde Maserati del cargo de cuestor ...') says nothing of a cipher."},
  "prior_art": {
   "decode": "known.py on 'FRIAS,C.635', 'FRIAS,C.1389', 'Conde de Haro' and 'Haro': no DECODE record or catalogue entry for these units (the Haro hits are Luis Méndez de Haro and a Hungarian item, unrelated).",
   "tomokiyo": TOMO.format(t="Haro and FRIAS"),
   "lasry": LAS.format(t="Haro, Conde de Haro and FRIAS"),
   "edition": "No printed text of the 1647 appointment despatch found; no edition of the Frías-Haro Milan papers is known here.",
   "literature": "No separate web search beyond the sweep's; catalogue 844 (FRIAS,C.1442,D.2, Philip IV real cédula in cipher to the same man as duque de Frías, 1664) is the same recipient seventeen years later, not this document."},
  "key_check": "No key for Philip IV's 1647 despatches to Milan is held here; the 1664 cédula (catalogue 844) is unread, so it gives no key. A key would not block in any case.",
  "duplicates": "known.py on both shelfmarks and the names: no duplicate; catalogue 844 is a different document (1664, C.1442).",
  "verdict": "open"}}

P["2710"] = {
 "verdict": None, "confidence": "low",
 "note": "Not assessed; probably key material, not a ciphertext: PARES says Cárdenas's correspondence was 'remitiendo dos cifras' (sending two ciphers, i.e. key tables), and nothing describes cipher text in the nine documents (dated 1621-1775 as a unit). PARES 429 blocked reopening the record; refile in key_leads.json if the record confirms two key tables.",
 "access": "archive", "access_note": "No images on PARES (record 13363563); PARES answered 429 on 16 Nov 2026."}

ONLINE = ("2699", "2700", "2701", "2707", "2706", "2705")
for lid, s in (
 ("2699", "Titles of OSUNA,C.1634,D.127-132 and D.133 name no cipher; the 'cifrada' hit is from record text never seen, and the images (flagged online) could not be opened: PARES 429. The 14 Nov blocker stands."),
 ("2700", "Title of OSUNA,C.1634,D.124 names no cipher; hit 'cifrada' from unseen text; images flagged online but PARES answered 429. Blocker stands."),
 ("2701", "Titles of OSUNA,C.1635,D.130-134 and D.162-164 name no cipher; only D.88 (a servant asking the duke for a new cipher, 'nuevo código cifrado') names one, and it is a request, not ciphertext. Images flagged online, not viewable (PARES 429)."),
 ("2702", "Titles of OSUNA,CP.56,D.4 and D.8 (Osuna to Philip II, 1579) name no cipher; the 'carta cifrada' hit is from unseen record text and there are no images, so no archive description of the cipher can be quoted. Needs the PARES records reread."),
 ("2703", "Of the eight OSUNA,C.1977 records only D.8 ('respuesta cifrada del Monarca', 1624) and D.29 (letter to a cardinal 'además cifrada', Aug 1625) name a cipher in the title; D.17 holds a 'Copia carta cifrada, 14 de enero de 1625', most likely a decoded copy filed with it, and the same Osuna Rome-embassy fonds files plain copies with its cipher letters (CT.2/CT.7). Too likely to hold decipherments to call open unseen; needs the PARES records reread."),
 ("2704", "The PARES title 'Carta en parte cifrada del Marqués de Caracena a Antonio Ronquillo' (1651, no images) would pass as a not-online open lead, but a web search turned up a Spanish ministry exhibition page (www.mcu.es/ccbae/es/catalogo_imagenes/grupo.do?path=37756) with 'la carta parcialmente cifrada' of a Milan governor's spies shown with its decryption; that page answered 429 like PARES, so whether it is this letter is unknown. Held until that page and the PARES record are read."),
 ("2707", "Three writers in one lead (split before promotion). CT.15,D.5 (Galarreta, 18 Feb 1651) title ends 'Fragmento cifrado.'; CT.18,D.56 (Gradiñán, 20 Feb 1655) hit on 'no descifrada' in unseen text; CT.18,D.45 names no cipher. All have images flagged online, so a not-online acceptance does not apply; PARES 429 blocked them."),
 ("2706", "Title of OSUNA,CT.260,D.151-194 (44 Tercia letters 1668-76) names no cipher; 'carta cifrada' hit from unseen text; images flagged online, not viewable (PARES 429)."),
 ("2705", "Titles of OSUNA,CT.80,D.10-12 (Peña Zúñiga, Aug-Sep 1685, long news summaries) name no cipher; 'cifrado' hit from unseen text; images flagged online, not viewable (PARES 429)."),
):
    P[lid] = {"verdict": None, "confidence": "low", "note": "Not assessed. " + s,
              "access": "online" if lid in ONLINE else "archive",
              "access_note": "PARES (pares.cultura.gob.es) HTTP 429 on 16 Nov 2026 to curl and to WebFetch; record not reopened."}

for lid, s in (
 ("2930", "AHU OP16696: DigitArq API re-checked 16 Nov 2026, hasImages still false; the description 'Contém relatórios, e documentação cifrada' gives no count and does not say whether cipher groups or only decoded copies survive. The 14 Nov blocker stands: needs an AHU scan order."),
 ("2931", "AHU OP16752, OP16773, OP16774, OP16775: hasImages still false on all four (re-checked 16 Nov 2026); 'telegramas cifrados' listed among maps and reports, no count or sample. Blocker stands: AHU scan of one folder first."),
 ("2932", "AHU OP19560: hasImages still false (16 Nov 2026); 'Contém cifrados' in a mixed telegram register. Blocker stands."),
 ("2933", "AHU OP17197: hasImages still false (16 Nov 2026); one 'telegrama cifrado' in a correspondence folder. Blocker stands."),
 ("2935", "AHU MU-GM Teleg folders 1947-50: Mozambique 1947 record re-checked, hasImages false. A ministry series titled 'Telegramas cifrados recebidos' most likely holds the decoded texts as filed; system and key books unknown. Blocker stands; candidate for closure once one folder is seen."),
):
    P[lid] = {"verdict": None, "confidence": "low", "note": "Not assessed. " + s, "access": "archive",
              "access_note": "DigitArq API /api/docs/details: no digital objects; AHU Lisbon reading room or reproduction order."}

json.dump(P, open('proposals.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(P))
