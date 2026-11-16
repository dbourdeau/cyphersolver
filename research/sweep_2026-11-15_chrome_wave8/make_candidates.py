"""Chrome wave 8 (15 Nov 2026): DARA (Documentos y Archivos de Aragon) and DigitArq non-ANTT archives.
Writes candidates.json (with a vetting block on the rows that meet the bar) and key_leads.json."""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = "DARA (dara.aragon.es) results and item pages, fetched same-origin in Chrome, wave 8, 15 Nov 2026"
BY = "claude session 15 Nov 2026 (Claude Sonnet 5.5), Chrome wave 8 vetting"
rows = []


def link(i, label):
    return [{"href": "https://dara.aragon.es/opac/app/item?i=" + str(i), "label": label}]


def vet(where, extent, cipher, decode, tomokiyo, lasry, edition, literature, key_check, duplicates):
    return {"date": "2026-11-15", "by": BY,
            "seen": {"kind": "scan", "where": where, "extent": extent, "cipher": cipher},
            "prior_art": {"decode": decode, "tomokiyo": tomokiyo, "lasry": lasry, "edition": edition, "literature": literature},
            "key_check": key_check, "duplicates": duplicates, "verdict": "open"}


DEC = ("known.py plus the DECODE dumps (research/catalogue_harvest/decode views.jsonl, views_b, views_c) and the Cryptoole snapshot, "
       "15 Nov 2026: no record for this shelfmark, fonds (Archivo del Reino de Aragon CRAR / Fundacion Alcort) or writers; the dumps are partial, "
       "so 'not on DECODE' is as far as they go.")
LAS = "GL.htm (Lasry's list) and Lasry's papers: not searched item by item on 15 Nov 2026; known.py over the repo's copies of the list found nothing for this shelfmark."
CRAR_TOM = ("Tomokiyo's 'Spanish Ciphers before Accession of King Ferdinand: 1470-1479' (Academia.edu, 2018) reconstructs four systems of Ferdinand's letters to John II "
            "(1470, 1473, 1474-76, 1476-79), sourced to BNE MSS/20211 (the 1470 letter is MSS/20211/56); web search 15 Nov 2026 found no mention of the Archivo del Reino de Aragon "
            "or of this letter. The paper's PDF could not be read (Academia login), so whether its 1476-79 system also reads this sheet is NOT checked.")
CRAR_EDN = ("None known: the CRAR volume (Cartas Reales del Archivo del Reino, collected by the chronicler Zurita) is catalogued in DARA with a one-line summary that does not mention the cipher; "
            "no edition of the cipher passages found by web search 15 Nov 2026.")
CRAR_LIT = ("Galende Diaz, 'La escritura cifrada durante el reinado de los Reyes Catolicos y Carlos V' is the standard survey; not seen. Web search 15 Nov 2026 "
            "(Archivo del Reino de Aragon cartas cifradas Fernando Juan II 1478): nothing on these letters.")


def crar(num, i, y, date, place, corr, title, status, extent, cipher_note, imp, sol):
    rows.append(dict(
        year=y, date=date, period="15th century" if y < 1497 else "1497-1559", language="Spanish", region="Spain", cls="B",
        title=title, correspondents=corr, place=place,
        shelfmark=f"Archivo Historico Provincial de Zaragoza (Archivo del Reino de Aragon), Coleccion Zurita, C_CRAR/000001/{num}",
        folio_note=extent,
        status=status, why=cipher_note, importance=imp, solvability=sol, difficulty=3,
        score_note="Scored from the DARA record and the thumbnail of the first leaf (15 Nov 2026, wave 8); the vetting block says what was viewed",
        verify="Open the record's PDF (DARA 'Archivo adjunto') for every leaf; compare with the Ferdinand-John II ciphers of Tomokiyo 2018 (BNE MSS/20211) and with targets/ferdinand1473.",
        links=link(i, "DARA record C_CRAR/000001/" + num), source=SRC, ark="", needs_archive_scan="no", seen="image"))
    return rows[-1]


# ---- Cartas Reales del Archivo del Reino (AHP Zaragoza): ciphers of 1477-79 and 1497
r = crar("0024", 1055720, 1478, "9 Jun 1478", "Seville", "Prince Ferdinand (Fernando II) -> John II of Aragon and Navarre",
         "Ferdinand to his father John II, Seville, 9 Jun 1478: a letter whose first page is entirely in cipher",
         "Online (PDF of the letter on DARA). The DARA summary ('Carta de Fernando II a su padre, el rey Juan II de Aragon y Navarra') does not mention cipher; the first page is written wholly in cipher signs (viewed 15 Nov 2026). No decipherment on the sheet.",
         "1 letter, bifolio; first page about 25 lines of cipher signs", "A full cipher letter of the future king to his father in 1478, uncatalogued as cipher: same correspondents and period as the BNE series of targets/ferdinand1473, pre-1497.", 4, 4)
r["vetting"] = vet("DARA record i=1055720 (C_CRAR/000001/0024), PDF at dara.aragon.es/opac/app/attachment?a=7a/9e/AHPZ_C_CRAR_000024.pdf, opened in the PDF viewer in Chrome 15 Nov 2026.",
                   "one letter; first page wholly in cipher signs, about 25 lines",
                   "Viewed in the PDF viewer 15 Nov 2026: page 1 is covered edge to edge by short lines of non-alphabetic cipher signs under the salutation; no interlinear decipherment and no clear copy on the leaf; the record's summary does not mention cipher.",
                   DEC, CRAR_TOM, LAS, CRAR_EDN, CRAR_LIT,
                   "No key held. The 1474-76 and 1476-79 systems reconstructed by Tomokiyo (BNE letters) are the first thing to test; targets/ferdinand1473 holds the 1473 and 1474 BNE keys, which were not tried on this sheet.",
                   "known.py 'CRAR', 'Archivo del Reino', 'C_CRAR', 'Zurita', 'Benasque' (15 Nov 2026): no hit in the ledgers; the BNE Ferdinand letters of targets/ferdinand1473 are siblings, not duplicates (different archive, different letters).")

r = crar("0026", 1055722, 1478, "16 Jul 1478", "Trapena", "Count of Cardona and Prades -> John II of Aragon",
         "Count of Cardona and Prades to John II, 16 Jul 1478: affairs of state, a parliament; long cipher passages",
         "Online (PDF on DARA). The summary ('explicando asuntos de estado, en relacion con un Parlamento; se menciona tambien al senor de Camarasa y a don Segimundo') does not mention cipher; the first page carries two large blocks of cipher signs (viewed 15 Nov 2026). No decipherment on the sheet.",
         "1 letter; two cipher blocks on the first page", "A magnate's cipher letter to the king in 1478, not Ferdinand's hand: a second writer in the same archive and year, so a different or shared system for comparison.", 4, 3)
r["vetting"] = vet("DARA record i=1055722 (C_CRAR/000001/0026); thumbnail of the first leaf viewed in Chrome 15 Nov 2026 (record PDF AHPZ_C_CRAR_000026.pdf).",
                   "one letter; two blocks of cipher signs on the first page (about 20 lines)",
                   "Viewed 15 Nov 2026 on the record's first-leaf image: the upper two thirds and a middle band of the page are cipher signs, with clear text only at the foot (signature); no decipherment on the leaf; the summary does not mention cipher.",
                   DEC, CRAR_TOM, LAS, CRAR_EDN, CRAR_LIT,
                   "No key held. Cardona's own system is unknown; Tomokiyo's Ferdinand systems are a first try.",
                   "known.py 'CRAR', 'Cardona', 'Archivo del Reino' (15 Nov 2026): no hit for this letter; the sibling is CRAR 0024 (Ferdinand, 1478).")

r = crar("0020", 1055638, 1477, "13 Jul 1477", "unknown (not given in the record)", "Prince Ferdinand (Fernando II) -> John II of Aragon",
         "Ferdinand to John II, 13 Jul 1477: affairs of the realm, Leonor princess of Navarre, Hermandad troops; a cipher passage",
         "Online (PDF on DARA). The summary ('sobre los asuntos del reino y la actuacion de Leonor, princesa de Navarra, con instrucciones y la promesa de ayuda de tropas de la Hermandad') does not mention cipher; the lower half of the first page is cipher signs (viewed 15 Nov 2026). No decipherment on the sheet.",
         "1 letter; about 10 lines of cipher signs below a clear opening", "A plain-plus-cipher letter of Ferdinand in 1477, with clear text on the same page that may state the cipher passage's content (a crib), on the sibling pattern of the BNE letters.", 4, 4)
r["vetting"] = vet("DARA record i=1055638 (C_CRAR/000001/0020); thumbnail of the first leaf viewed in Chrome 15 Nov 2026 (record PDF AHPZ_C_CRAR_000020.pdf).",
                   "one letter; about 10 lines of cipher signs at the foot of the first page",
                   "Viewed 15 Nov 2026: the top of the leaf is clear text in a chancery hand and the lower half is lines of cipher signs ending in the signature; no interlinear decipherment visible at thumbnail size (to be checked on the PDF).",
                   DEC, CRAR_TOM, LAS, CRAR_EDN, CRAR_LIT,
                   "No key held; the Tomokiyo 1476-79 system is the first candidate and was not tested.",
                   "known.py 'CRAR', 'Archivo del Reino' (15 Nov 2026): no hit; siblings CRAR 0024 and 0026.")

r = crar("0039", 1056536, 1497, "14 Apr 1497", "Genoa", "Juan Manuel (Spanish envoy) -> Catholic Monarchs",
         "Juan Manuel to the Catholic Monarchs, Genoa, 14 Apr 1497: Italian affairs, the truce, the risks to Genoa; half in cipher",
         "Online (PDF on DARA). DARA summary: 'la mitad de la cual esta escrita en codigo cifrado' (viewed 15 Nov 2026: a block of cipher signs below a clear head). No decipherment on the sheet.",
         "1 letter; about half the text in cipher (about 15 lines)", "A 1497 diplomatic cipher letter from Genoa to the Catholic Monarchs, the Almazan-era system; sibling of the Claver Milan letters of 1497 and 1500.", 3, 3)
r["vetting"] = vet("DARA record i=1056536 (C_CRAR/000001/0039); first-leaf image viewed in Chrome 15 Nov 2026 (record PDF AHPZ_C_CRAR_000039.pdf).",
                   "one letter; half the text in cipher, about 15 lines",
                   "Viewed 15 Nov 2026: three lines of clear text at the top, then a block of cipher signs of mixed shapes to the foot; the DARA summary says half of the letter is in code. No decipherment on the leaf.",
                   DEC,
                   "Tomokiyo's Ciphers-in-the-Reign-of-Ferdinand-and-Isabella page covers the 1480s-90s keys (Puebla, Simancas PTR); no entry for Juan Manuel at Genoa found by web search 15 Nov 2026.",
                   LAS, CRAR_EDN,
                   "Parisi, 'La decrittazione di cinque lettere cifrate di Juan Claver' (ASPN 2019) deciphers Claver's 1500-02 letters (ledger leads 1054, 1055); Juan Manuel is a different writer, so not covered.",
                   "Writer's system unknown; the Spanish 1490s keys (Simancas PTR 52/33 Roman-numeral code of 1495, Puebla ciphers) are candidates for a test.",
                   "known.py 'Juan Manuel', 'CRAR', 'Genova 1497' (15 Nov 2026): no hit for this letter; sibling CRAR 0040 (Claver, Milan, 19 Jun 1497) is kept as a lead.")

# lead-only rows (not promoted)
r = crar("0040", 1056537, 1497, "19 Jun 1497", "Milan", "Juan Claver (ambassador) -> Catholic Monarchs",
         "Juan Claver to the Catholic Monarchs, Milan, 19 Jun 1497: diplomatic news from France and Italy, cipher at the end",
         "Online (PDF on DARA). DARA summary: 'Escritura cifrada en la parte final del mensaje'. First-leaf image viewed 15 Nov 2026. Not vetted against lead 1048 (Claver to the Monarchs, Milan, 23 Jun 1497): the dates differ by four days, so it may be a draft, a duplicate or a different letter.",
         "1 letter, incomplete (torn); cipher at the end", "Same writer and place as lead 1048, 1497; Parisi deciphered Claver's later letters, so the key may be in print.", 3, 3)
r["verify"] = "Compare with lead 1048 (23 Jun 1497, Milan) and Parisi 2019 before promoting; check the last leaf of the PDF."

r = crar("0029", 1055725, 1479, "25 Jan 1479", "Guadalupe", "King Ferdinand -> John II of Aragon",
         "Ferdinand to John II, Guadalupe, 25 Jan 1479: answers four letters of the king, two in cipher and two in clear; one topic 'kept secret (cifrado)'",
         "Online (PDF on DARA). The summary says it answers four letters, two ciphered, and that one subject stays secret (cipher); the first leaf seen 15 Nov 2026 is clear text, so the cipher passage (if any) is on a later leaf that was not viewed.",
         "1 letter; cipher leaf not located", "Ferdinand's own mention of John II's cipher letters (the incoming ones are not in this volume) in 1479: the plain letter dates the ciphers of the 1476-79 system.", 3, 2)
r["cls"] = "C"
r["verify"] = "Page through the PDF for a cipher passage; look for the two cipher letters of John II it answers."

# Benasque / Fundacion Alcort
BEN_DEC = ("known.py plus the DECODE dumps and the Cryptoole snapshot, 15 Nov 2026: no record for Fundacion Hospital de Benasque / Alcort or this shelfmark; the dumps are partial.")
BEN_EDN = ("None known: the Alcort papers (Fundacion Hospital de Benasque, Valle de Benasque, CC BY-NC-SA images on DARA) are described item by item in DARA; no edition or study of the cipher "
           "sheets found by web search 15 Nov 2026 (not run beyond one query).")


def ben(sig, i, y, date, period, place, corr, title, status, extent, why, imp, sol, cipher, lang="Spanish"):
    rows.append(dict(
        year=y, date=date, period=period, language=lang, region="Spain", cls="B", title=title, correspondents=corr, place=place,
        shelfmark=f"Fundacion Hospital de Benasque, Fundacion Alcort, ES/FHB - CD/ALCORT/D/{sig} ('Documentos cifrados')",
        folio_note=extent, status=status, why=why, importance=imp, solvability=sol, difficulty=3,
        score_note="Scored from the DARA record and the thumbnail of the first leaf (15 Nov 2026, wave 8); the vetting block says what was viewed",
        verify="Page through the record's images for the cipher leaves and any clear copy filed beside them.",
        links=link(i, "DARA record ES/FHB - CD/ALCORT/D/" + sig), source=SRC, ark="", needs_archive_scan="no", seen="image"))
    return rows[-1]


r = ben("0055", 764905, 1600, "17th century (undated)", "unknown", "unknown", "unknown", "Letter in cipher, 6 leaves, Alcort papers (Benasque), 17th century",
        "Online on DARA (images, CC BY-NC-SA 4.0). DARA: 'Carta en lenguaje cifrado', 6 hojas, 'Encriptacion' among the subject terms. The first leaf is cipher signs top to bottom, with interlinear pencil marks (viewed 15 Nov 2026); no clear copy is filed beside it in the series 'Documentos cifrados'.",
        "6 leaves", "A long single-system cipher letter of the 17th century with no named writer or date in the record; the family papers are Italian (Alcort, Gonzaga) so a Spanish or Italian key is likely.", 3, 3, "")
r["vetting"] = vet("DARA record i=764905 (ES/FHB - CD/ALCORT/D/0055), first-leaf image viewed in Chrome 15 Nov 2026.",
                   "6 leaves; the first leaf is about 30 lines of cipher signs",
                   "Viewed 15 Nov 2026: the whole first leaf is dense lines of cipher signs of one hand; the record says 'Carta en lenguaje cifrado'; no decipherment on the leaf and none listed in the DARA series.",
                   BEN_DEC, "Tomokiyo's Cryptiana: no entry for the Benasque Alcort papers found by web search 15 Nov 2026.", LAS, BEN_EDN,
                   "Web search 15 Nov 2026 (Fundacion Alcort Benasque cartas cifradas): nothing on a decipherment of the sheets.",
                   "No key held; the series holds no key leaf.",
                   "known.py 'Benasque', 'Alcort' (15 Nov 2026): no hit; the Gonzaga cipher sheets of the same fonds (D/0040, 0043, 0047, 0051) are recorded in the wave 8 README, not promoted.")
r["language"] = "unknown"

r = ben("0056", 764906, 1575, "14 Apr 1575", "1560-1589", "Naples", "unknown writer -> Philip II",
        "Cipher letter to Philip II, Naples, 14 Apr 1575, completed with lines in Latin letters (Alcort papers, Benasque)",
        "Online on DARA (images). DARA: 'Carta cifrada dirigida al rey de Espana, que se completa con varias lineas en alfabeto latino' (2 leaves). The first leaf has clear text above and a cipher block below (viewed 15 Nov 2026).",
        "2 leaves; cipher block of about 10 lines plus lines in Latin letters", "A viceregal-period cipher letter from Naples to Philip II, with the cipher block completed by lines in plain letters (a crib).", 3, 4, "")
r["vetting"] = vet("DARA record i=764906 (ES/FHB - CD/ALCORT/D/0056), first-leaf image viewed in Chrome 15 Nov 2026.",
                   "2 leaves; cipher block of about 10 lines at the foot of the first leaf",
                   "Viewed 15 Nov 2026: clear text over the upper two thirds, then lines of cipher signs; DARA says the cipher is 'completed with several lines in Latin letters'; no decipherment on the leaf.",
                   BEN_DEC, "Tomokiyo's Cryptiana (Spanish ciphers of Philip II's reign): no entry for this letter found by web search 15 Nov 2026.", LAS, BEN_EDN,
                   "Web search 15 Nov 2026 (carta cifrada Napoles 1575 Felipe II Benasque): nothing.",
                   "No key held; the Naples cipher of 1575 is not known to be in print.",
                   "known.py 'Benasque', 'Alcort', 'Napoles 1575' (15 Nov 2026): no hit; D/0055 is the sibling.")

# Gonzaga of Guastalla cipher sheets: lead, decipherment probably filed
rows.append(dict(
    year=1683, date="Jan-Nov 1683, Aug 1685", period="1651-1700", language="Italian", region="Spain", cls="C",
    title="Vincenzo Gonzaga (Guastalla) to Vespasiano Gonzaga: letters with a cipher sheet, 1683-85 (Alcort papers, Benasque)",
    correspondents="Vincenzo Gonzaga -> Vespasiano Gonzaga", place="Guastalla",
    shelfmark="Fundacion Hospital de Benasque, Fundacion Alcort, ES/FHB - CD/ALCORT/D/0040, 0043, 0047 and 0051",
    folio_note="four letters of 3-4 leaves, each 'con una hoja cifrada'",
    status="Online on DARA (images). Each record says the letter contains a cipher sheet. The same series holds D/0041, 0045 and 0048, 'Noticia' records whose summaries match the content of the cipher sheets (rumours of a Venetian incursion, French and Venetians near Mantua, affairs of Milan, Genoa and France): probably the clear text or decipherment filed beside them, which would close the leads under the 15 Nov audit bar. Not viewed leaf by leaf.",
    why="Four cipher sheets of one correspondence in 1683-85.", importance=2, solvability=2, difficulty=3,
    score_note="Scored from the DARA records only (15 Nov 2026, wave 8)", verify="Open D/0041, 0045 and 0048 and see whether they are the decipherments of 0040, 0043 and 0047.",
    links=link(764879, "DARA record D/0040"), source=SRC, ark="", needs_archive_scan="no", seen="catalogue"))

# AHU
rows.append(dict(
    year=1897, date="1897-1898", period="1801-1900", language="Portuguese", region="Portugal", cls="C",
    title="AHU, Lourenco Marques railway arbitration of Berne 1897 (documentation in cipher) and the 1898 Cape railway conference (a cipher telegram)",
    correspondents="Portuguese government and Lourenco Marques railway case", place="Lisbon / Lourenco Marques / Cape",
    shelfmark="Arquivo Historico Ultramarino, PT/AHU/ID-OP/OP16696 and PT/AHU/ID-OP/OP17197",
    folio_note="OP16696: 'Contem relatorios, e documentacao cifrada'; OP17197: 'Correspondencia, contem telegrama cifrado'; no images on DigitArq",
    status="Not online (DigitArq, 15 Nov 2026, filesCount 0). AHU descriptions quoted in the folio note; no decipherment is mentioned.",
    why="Late-19th-century commercial and diplomatic cipher telegrams of a Portuguese colonial railway dispute; low priority.",
    importance=1, solvability=2, difficulty=3, score_note="Scored from the DigitArq records (15 Nov 2026, wave 8)",
    verify="AHU reading room or a scan request; the case files may hold the code book.",
    links=[{"href": "https://digitarq.arquivos.pt/documentDetails/0784fd2cc8f94abab559b8f14769abbe", "label": "DigitArq OP16696"},
           {"href": "https://digitarq.arquivos.pt/documentDetails/41745afa3bf64d2196a0f6cb0fe8054a", "label": "DigitArq OP17197"}],
    source="DigitArq JSON API (digitarq.arquivos.pt/api/docs/search, all archives except ANTT), wave 8, 15 Nov 2026", ark="", needs_archive_scan="yes", seen="catalogue"))

json.dump(rows, open(os.path.join(HERE, "candidates.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)

keys = [
    {"title": "AHU Angola 1760: Antonio de Vasconcelos sends the Jesuit cipher of General Aquaviva, 23 Mar 1587 (PT/AHU/CU/001/0047/04298)",
     "shelfmark": "Arquivo Historico Ultramarino, PT/AHU/CU/001/0047/04298 (Angola, 32 images online)",
     "note": "Oficio of the governor of Angola to the count of Oeiras remitting 'a cifra usada pelo padre [Claudio] Aquaviva, a 23 de Marco de 1587', reformed by the provincial Joao Correia. A Jesuit cipher table of 1587, online (32 images on DigitArq), a key for Jesuit cipher letters of the 1580s; not viewed in full."},
    {"title": "AHU Consulta of the Conselho Ultramarino, 1644: the viceroy count of Aveiras on sending a new cipher (PT/AHU/CU/034/0211/00028)",
     "shelfmark": "Arquivo Historico Ultramarino, PT/AHU/CU/034/0211/00028",
     "note": "Description only ('sobre se haver de mandar nova cifra'); not online. Evidence of a Portuguese India cipher in 1644."},
    {"title": "ACPS 1487 'Instruccions per cartes xifrades a Antonio Ximeno' (wave 7 key lead), checked in wave 8",
     "shelfmark": "Arxiu Comarcal del Pallars Sobira, ACPS211-95-T2-242",
     "note": "Rechecked on 15 Nov 2026: the Arxius en linia record has no digital object (objects endpoint returns an empty list) and the description is only 'Instruccions per cartes xifrades a Antonio Ximeno' with '+ copia'. Instructions, not a ciphertext, so no lead was made; it stays a pre-1497 pointer for the oldest-cipher search."},
]
json.dump(keys, open(os.path.join(HERE, "key_leads.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(rows), "rows", len(keys), "keys")
