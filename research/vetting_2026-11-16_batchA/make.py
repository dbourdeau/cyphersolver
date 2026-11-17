"""Write proposals.json for vetting batch A (16 Nov 2026). Run: python -I -X utf8 make.py"""
import json, os

D = "2026-11-16"
BY = "claude session 16 Nov 2026 (Claude Opus 5.5), wave 19 vetting"
TOMO = ("cryptiana.web.fc2.com/code/unsolved.htm fetched 16 Nov 2026 and grepped for the correspondents, places and "
        "shelfmark: no entry for this item.")
LASRY = ("cryptiana.web.fc2.com/code/GL.htm (Lasry's BnF and other readings) fetched 16 Nov 2026 and grepped for the "
         "same terms: no entry for this item.")
MNL = "https://adatbazisokonline.mnl.gov.hu/adatbazis/ii_-rakoczi-ferenc-fejedelem-leveltara_-emigracioba-vitt-resz/adatlap/"
ASF = ("https://archiviodistatofirenze.cultura.gov.it/iipsrv/iipsrv.fcgi?IIIF=/data/iip-data/asfi/"
       "mediceo_avanti_principato/00100105/A0000NNN.ptif/full/1272,/0/default.jpg")


def block(seen, prior, key_check, duplicates, verdict, closed=None, **extra):
    v = {"date": D, "by": BY, "seen": seen, "prior_art": prior, "key_check": key_check, "duplicates": duplicates,
         "verdict": verdict}
    if closed:
        v["closed"] = closed
    v.update(extra)
    return v


P = {}

# ---------------------------------------------------------------- 2759 Vettori
P["2759"] = {
    "verdict": "read", "confidence": "high",
    "note": ("Both letters named by the Federal Archives (microfilm copies of ASF MAP filza CV) were seen on the ASF MAP "
             "IIIF server: doc. 27 (Lyon, 25 Feb 1515 s.f. = 1516) is interlined throughout with a contemporary "
             "decipherment, and doc. 31 (Lyon, 29 Jan) has its decipherment on c. 51v headed 'Deciferato della lra de 29'."),
    "access": "online",
    "access_note": ("ASF Mediceo avanti il Principato filza CV, IIIF images by curl: " + ASF + " (positions 091-094 = doc. 27, "
                    "095-098 = doc. 28, 099-100 = c. 43 decipherment, 113-114 = c. 51 decipherments, 117-119 = doc. 31). "
                    "The MAP filza listing page returned no image list on 16 Nov; the image folder 00100105 was found by trial."),
    "vetting": block(
        {"kind": "scan",
         "where": ("ASF MAP filza CV, IIIF positions 091-092 (doc. 27, c. 42, signed 'Franc.s Victorius', dated 'Lugduni die xxv "
                   "februarii MDXV'), 094 (address to Lorenzo de' Medici), 095-097 (doc. 28, Vienne, Feb 1515 s.f.), 099 (c. 43), "
                   "113-114 (c. 51r 'Deciferato della lra de 27', c. 51v 'Deciferato della lra de 29'), 117-119 (doc. 31, signed "
                   "Vettori, 'Lugduni die xxix Jan.'); inventory vol. 4 p. 27 (MAP site image 001A0004/A0000027) lists "
                   "'Franciscus Vectorius, orator. Lione, 1515 feb. 25, n. 27. Vienne, 1525 [sic] feb. 22, n. 28. Lugdunii, 1515 gen. 29, n. 31'."),
         "extent": ("Doc. 27: one full page of figure-and-sign cipher (c. 42r) and a few lines on c. 42v; doc. 31: about two pages of "
                    "cipher after a few clear lines; doc. 28 (not in the lead): clear opening and about a page and a half of cipher."),
         "cipher": ("Florentine homophonic cipher with nomenclator (figure groups such as 568, 808, 3qq and signs). Doc. 27 is "
                    "interlined line by line with the plaintext in a contemporary hand; doc. 31's plaintext is the slip at c. 51v "
                    "('Deciferato della lra de 29'); doc. 28's cipher continues in clear on the separate leaf c. 43 (it picks up "
                    "mid-sentence where the clear part of doc. 28 breaks off into cipher).")},
        {"decode": ("known.py on 'Vettori', 'Vectorius', 'filza 105', 'MAP CV': only this lead and its sibling 2760; the DECODE dumps "
                    "hold no MAP CV record."),
         "tomokiyo": TOMO, "lasry": LASRY,
         "edition": ("Not needed for the verdict: the decipherments are on file in the filza itself. The edition of Vettori's "
                     "1515-16 legation letters was not checked."),
         "literature": ("No web search made beyond the sweep's; the decipherments on the leaves settle the verdict.")},
        ("No key sought: both letters were deciphered at the time on or beside the leaf. The interlined doc. 27 and the c. 43 / c. 51 "
         "slips would rebuild the key if a sibling without decipherment turns up."),
        ("known.py on the shelfmark, the MAP filza and the names: no catalogue entry or target; lead 2760 (Tricarico/Cynthius, "
         "J1.58 #118) is the same microfilm deposit but a different letter."),
        "read",
        closed=("ASF MAP CV doc. 27 (Lyon 25 Feb 1516) is interlined with a contemporary decipherment and doc. 31 (Lyon 29 Jan 1516) "
                "has its decipherment on c. 51v; the sibling doc. 28 (Vienne, Feb 1516) is deciphered on c. 43."))}

# ---------------------------------------------------------------- 2625 OBA
P["2625"] = {
    "verdict": "read", "confidence": "medium",
    "note": ("The lead is defined as the Schönberg-Albrecht letters the finding aid describes with an Auflösung: for 8 of the 11 "
             "units the decipherment is filed with the cipher by the archive's own description, and OBA 26245 is printed in "
             "Joachim vol. 3 no. 110. Only 25324 and 25459 are not described in what was seen."),
    "access": "archive",
    "access_note": ("ACTApro records are a JSF shell to curl (16 Nov 2026: the archive.xhtml permalinks return the page frame "
                    "without the record); the sweep read them in Chrome. No images online."),
    "vetting": block(
        {"kind": "not online",
         "where": ("GStA PK ACTApro descriptions as quoted in the lead (14 Nov 2026 sweep): 22724 'Auflösung eines Chiffrebriefes', "
                   "22861 'Original in Chiffern; auch Auflösung', 22951 'Chiffernauflösungen', 22993 'wohl Auflösung eines "
                   "Chiffrenbriefes', 23072 'Auflösung eines Chiffers', 25292 'Beibrief in Chiffern mit Erläuterungen', 25331 'In "
                   "Chiffern; dabei Auflösung', 26268 the Grand Master's answer to a Chiffernbrief. Joachim, Politik des letzten "
                   "Hochmeisters vol. 3 (IA diepolitikdeslet03joac, OCR) p. 246 no. 110 'Chiffrirter Beibrief' (11 Jul 1523)."),
         "extent": "Eleven OBA units 1519-23; cipher extent per unit not described.",
         "cipher": ("The archive's descriptions say a decipherment (Auflösung) is filed with the cipher for most units, and OBA 26245 "
                    "is printed in clear by Joachim; this is the opposite of the bar's 'no decipherment on or with it'.")},
        {"decode": "known.py on the OBA numbers and Schönberg/Albrecht: only this lead, catalogue 553 and the GStA sweep files; no DECODE record.",
         "tomokiyo": TOMO, "lasry": LASRY,
         "edition": ("Joachim vols. 2 and 3 (IA OCR, downloaded 16 Nov 2026) searched for Chiffr/Ziffer: vol. 3 prints OBA 26245 as no. "
                     "110 'Chiffrirter Beibrief' with its German text and a 1524 'Zettel in Chiffren' in clear (p. 322); the 1522 "
                     "letters of 16 Jan and 12 Feb are cited in a source note (vol. 3 p. 23-24), and vol. 2 has a 1519 note on "
                     "cipher instructions (no. 36)."),
         "literature": "No study of the Schönberg-Albrecht cipher found by the earlier GStA pass; not repeated."},
        ("The Chiffrenbuch of Schönberg and the chancery is OBA 27584 (key_leads.json, GStA sweep); not seen, not tested. "
         "The filed Auflösungen are themselves plaintext for the cipher."),
        ("Catalogue 553 holds the Schönberg-Albrecht letters 'in Chiffern' with no Auflösung noted; this lead is its complement. "
         "known.py finds no other entry on these OBA numbers."),
        "read",
        closed=("By the GStA finding aid the decipherment (Auflösung) is filed with 8 of the 11 units and OBA 26245 is printed by "
                "Joachim (vol. 3 no. 110); 25324 and 25459, whose descriptions were cut off, can be added to catalogue 553 if their "
                "records show no Auflösung."))}

# ---------------------------------------------------------------- 1911 Nedeczky
P["1911"] = {
    "verdict": "partly_read", "confidence": "high",
    "note": ("Series-level row. The MNL item records of Nedeczky's G 15 reports (E Fasc. 113 and others) mark most of them "
             "'nagyrészt megfejtett számjelekkel' (largely deciphered); the undeciphered 1708 items are already lead 2484 "
             "(closed partly_read from the MTA copy Ms. 4958/2/II); Fogarasi's reports are not cipher."),
    "access": "archive",
    "access_note": "MNL AdatbazisokOnline G 15 item records (no images); originals in MNL OL, Budapest.",
    "vetting": block(
        {"kind": "not online",
         "where": ("MNL AdatbazisokOnline search 'Nedeczky' (807 hits) and 'Fogarasi' run 16 Nov 2026 (mnl_search.py; G 15 rows in "
                   "raw/g15_nedeczky_fogarasi.json): G 15 E Fasc. 113 fol. 13, 29, 30, 40, 42, 73-76, 77, 88-93 'nagyrészt "
                   "megfejtett számjelekkel' (adatlap 17424, 17430, 17431, 17436, 17438, 17460, 17461, 17466); A1 Fasc. 2 fol. 27-28 "
                   "'részben megfejtett'; H Fasc. 229 fol. 46-48 'nagyrészt megfejtett titkos írással'; E Fasc. 113 fol. 14+17, "
                   "15-16, 70, 78, 79, 80-84 'nagyrészt / szinte végig megfejtetlen' and fol. 94 'néhol megfejtetlen'."),
         "extent": "About 25 Nedeczky items 1707-1710 in G 15; about 7 of them marked mostly undeciphered.",
         "cipher": ("Number cipher with the signature group 441. Most reports carry the chancery's decipherment on the leaf; no "
                    "Fogarasi item in G 15 carries a cipher note.")},
        {"decode": ("Lead 2484's check stands (de-crypt.org 'Nedeczky', 11 Nov 2026): keys R613-R615 and R454-R455 only, no Nedeczky "
                    "ciphertext."),
         "tomokiyo": TOMO, "lasry": LASRY,
         "edition": ("Zsemlye 2025 (Belvedere Meridionale 37/3) quotes the 8 Apr, 24 Apr, 1 May and 8 May 1708 reports in clear from "
                     "MTA Ms. 4958/2/II (recorded under lead 2484); Ivanyi 1954 p. 134-135 is the source of this row."),
         "literature": "Lang 2018 pp. 64, 94 on the Rakoczi-Nedeczky clavis (earlier vetting); Révay 1974 on Rakoczi's ciphers not seen."},
        "Nedeczky keys on DECODE R613-R615, R454-R455 (Lang T.Rad.13, T.Rad.81, T.Rak.79); not tested here.",
        ("The undeciphered Nedeczky items (E Fasc. 113 fol. 14+17, 15-16, 70, 78, 79, 80-84, 94) are lead 2484 exactly; known.py "
         "'Fasc. 113', 'Nedeczky' finds only 2484, this row and the southeast sweep."),
        "partly_read",
        closed=("Series-level duplicate of lead 2484 for its only undeciphered items; the other Nedeczky reports in G 15 are marked "
                "deciphered on the leaf, and Fogarasi's reports are not described as cipher."))}

# ---------------------------------------------------------------- 2486 Karolyi
P["2486"] = {
    "verdict": "partly_read", "confidence": "medium",
    "note": ("Of the nine Károlyi letters, H Fasc. 239 fol. 24 and 25-26 (9 and 13 Jan 1711) are printed in Bánkúti, "
             "Dokumentumok a szatmári béke történetéhez (nos. 33, 34) by the MNL records themselves, and five others have only "
             "'egy-két szó' to 'két sor / pár sor' undeciphered. The one substantial piece, B Fasc. 22 fol. 86-87 (wholly in "
             "figures, writer only guessed), is proposed as a split ('2486-split')."),
    "access": "archive",
    "access_note": "MNL AdatbazisokOnline item records (no images); Hungaricana returns 403 to scripts (16 Nov 2026).",
    "vetting": block(
        {"kind": "not online",
         "where": ("MNL datasheets read 16 Nov 2026 (mnl_adatlap.py): " + MNL + "16263 (C 65 fol. 9-10, 9 Oct 1706, 'részben "
                   "megfejtetlen'), 18145 (G 218 fol. 28-29, 'két sor'), 18146 (fol. 30-31, 'két sor'), 18149 (fol. 36-37, 'pár sor'), "
                   "18150 (fol. 38, 'egy-két szó'), 18163 (fol. 63-64, 'egy-két szó'), 18642 (H 239 fol. 24, 9 Jan 1711, Kiadási "
                   "információk 'Bánkúti, Dok. 32. (No. 33.)'), 18643 (fol. 25-26, 13 Jan 1711, 'Bánkúti, Dok. 32. (No. 34.)'), "
                   "15393 (B 22 fol. 86-87, s.d., '[Károlyi Sándor?]', 'a külcímet kivéve végig megfejtetlen számjelekkel')."),
         "extent": "Nine letters; seven carry a word to a few lines of figures, one partly, one (B 22) wholly in figures.",
         "cipher": ("Number cipher in Károlyi's letters to Rakoczi; the archive marks the figures undeciphered, but two letters are "
                    "printed and most of the others are plain letters with a few figure groups.")},
        {"decode": "Earlier check (11 Nov): DECODE 'Károlyi' has no G 15 ciphertext record; not repeated.",
         "tomokiyo": TOMO, "lasry": LASRY,
         "edition": ("Lukinich, A szatmári béke története és okirattára (1925; MEK 23062, PDF text searched 16 Nov 2026): no cipher "
                     "words; it summarises Károlyi's 13 Jan 1711 report from the Aspremont archive (MNM), not the G 15 copy, and prints "
                     "Károlyi to Rakoczi 21 Feb 1711. Bánkúti 1991 (nos. 33-34) prints the 9 and 13 Jan 1711 letters per the MNL "
                     "records; not seen here, so whether the figures are resolved there is not checked. Archivum Rakoczianum (earlier check): no Károlyi letters."),
         "literature": "Lang 2015/2018 and the AETAS 2014 article treat the Károlyi-Bercsényi sign system (catalogue notes); no study of these letters found."},
        "Károlyi key sheets MNL OL P 396 nos. 379, 11345, 10543 (lead record); not seen or tested.",
        "known.py 'Károlyi', 'Fasc. 22, fol. 86': only this lead and the southeast sweep files; no catalogue entry for these folios.",
        "partly_read",
        closed=("Two of the nine letters are printed (Bánkúti nos. 33-34) and five have only a word to a few lines of figures; the "
                "row is closed and the one wholly ciphered piece, G 15 B Fasc. 22 fol. 86-87, is offered as its own lead."))}

P["2486-split"] = {
    "verdict": "open", "confidence": "low",
    "note": ("Proposed new lead split from 2486: G 15 Caps. B Fasc. 22 fol. 86-87, '[Károlyi Sándor?] -> Rákóczi Ferenc II', s.d., "
             "Hungarian, closing seal in red wax, 'a külcímet kivéve végig megfejtetlen számjelekkel'. No edition flag in the MNL record; "
             "but undated and the writer only guessed, so no edition can be searched by letter. Low confidence."),
    "access": "archive",
    "access_note": "MNL AdatbazisokOnline record " + MNL + "15393; no images; order a scan from MNL OL.",
    "vetting": block(
        {"kind": "not online",
         "where": MNL + "15393 (read 16 Nov 2026): G 15 Caps. B Fasc. 22 fol. 86-87, s.d., s.l., Nyelv Magyar, Pecsét 1 zárópecsét gyűrűs vörös viasz.",
         "extent": "One letter, two leaves, wholly in figures apart from the outer address.",
         "cipher": "Archive's note verbatim: 'a külcímet kivéve végig megfejtetlen számjelekkel' (in undeciphered figures throughout except the outer address); no decipherment noted."},
        {"decode": "DECODE 'Károlyi' (11 Nov check): no G 15 ciphertext record; known.py no hit on the folio.",
         "tomokiyo": TOMO, "lasry": LASRY,
         "edition": ("The MNL G 15 records give an edition field when a letter is printed (e.g. Bánkúti for H 239 fol. 24-26); this "
                     "record has none. Archivum Rakoczianum (earlier check) prints no Károlyi letters; Lukinich 1925 searched (no cipher words)."),
         "literature": "No study found; Lang's repertory has no row for G 15 Caps. B (earlier check)."},
        "Károlyi key sheets MNL OL P 396 nos. 379, 11345, 10543; not seen or tested. A key does not block the lead.",
        "Split from lead 2486; no catalogue entry or other lead on G 15 B Fasc. 22.",
        "open")}

# ---------------------------------------------------------------- 2488 split
P["2488-split"] = {
    "verdict": "open", "confidence": "low",
    "note": ("Proposed new lead split from 2488: Rakoczi to Theodor Korbe (secretary of the Wallachian voivode) and to Count "
             "Constantin Cantacuzino, G 15 A2 Fasc. 2 fol. 80-81 and 82-83, Latin, s.d., each sealed, 'az aláíráson kívül végig "
             "megfejtetlen titkos jegyekkel'. Cantacuzino to Rakoczi of 6 Dec 1709 (F Fasc. 189 fol. 47-48) is 'végig egykorúlag "
             "megfejtett' and may share the system. Undated, so no edition matched; low confidence."),
    "access": "archive",
    "access_note": "MNL records " + MNL + "14811, 14812 and 17947; no images.",
    "vetting": block(
        {"kind": "not online",
         "where": MNL + "14811 (fol. 80-81, to Korbe) and 14812 (fol. 82-83, to Cantacuzino), read 16 Nov 2026; sibling " + MNL + "17947.",
         "extent": "Two letters of two leaves each, wholly in secret signs apart from the signature.",
         "cipher": "Archive's notes verbatim: 'az aláíráson kívül végig megfejtetlen titkos jegyekkel'; no decipherment noted; the sibling 17947 is noted as deciphered at the time ('végig egykorúlag megfejtett titkosírással, a dátum azonban feloldatlan')."},
        {"decode": "Earlier check (11 Nov): DECODE 'Cantacuz', 'Korbe' 0 records; the Brâncoveanu/Cantacuzino key A of target sieniawski1708 is a different correspondence (not compared).",
         "tomokiyo": TOMO, "lasry": LASRY,
         "edition": "Archivum Rakoczianum (earlier check): no letter to Korbe or Cantacuzino matching; a note that a letter to 'Cantacuzeno' was never entered in the letter book. No edition field in the MNL records.",
         "literature": "No study found in the earlier web searches; Révay 1974 not seen."},
        "No key held; the deciphered Cantacuzino letter (F 189 fol. 47-48) could supply plaintext for the system. A key does not block.",
        "Split from lead 2488; target sieniawski1708 (Brâncoveanu and Cantacuzino) is a different sender pair and archive, not a duplicate as far as checked.",
        "open")}

# ---------------------------------------------------------------- 1598
P["1598"] = {
    "verdict": "read", "confidence": "low",
    "note": ("Not seen (BNE excluded by brief). Two independent signs that the letter is read: the DECODE record R1172 sets Inline "
             "Plaintext: Yes and Inline Cleartext: Yes, and Tomokiyo 2018 lists Ferdinand to John II, Córdoba, 4 Nov 1478 "
             "(MSS/20211/123) among the 1476-79 letters whose cipher he reconstructed (search-engine extract of the Academia "
             "paper, which itself returns 403). DECODE's 'Non-decrypted' status is contradicted by its own flags."),
    "access": "online",
    "access_note": "BNE Digital (not used, per brief; 403/Cloudflare to scripts on earlier tries); DECODE R1172 full images need a login.",
    "vetting": block(
        {"kind": "not online",
         "where": ("Not viewed. DECODE R1172 record (local dump research/catalogue_harvest/decode/views*.jsonl, name NLS_MSS_20211_123): "
                   "inline_cleartext True, inline_plaintext True, 2 pages, status 2, date 1478-11-04, receiver John II."),
         "extent": "One letter, two pages (DECODE).",
         "cipher": ("Homophonic substitution (DECODE). DECODE's own flag says plaintext is written on the leaf (interlinear), as on "
                    "the sibling MSS/20211/61 ('Notas interlineales', targets/ferdinand1473).")},
        {"decode": "R1172: Non-decrypted status but Inline Plaintext: Yes; the other nine BNE 1476-79 letters (R1170-R1184) carry solved statuses.",
         "tomokiyo": ("Tomokiyo, 'Spanish Ciphers before Accession of King Ferdinand: 1470-1479' (Academia 37751652, 2018): 403 to WebFetch; a "
                      "WebSearch extract of its text (16 Nov 2026) lists the Córdoba 4 Nov 1478 letter, MSS/20211/123, in the 1476-79 group whose "
                      "cipher (simple substitution with homophones, like the 1473 one) the author reconstructed. The blog post "
                      "cryptiana.blogspot.com/2018/11 gives no letter list. unsolved.htm has no entry."),
         "lasry": LASRY,
         "edition": "No printed edition of the letter found (targets/ferdinand1473 checked Galende 1994: none).",
         "literature": "Two web searches (16 Nov 2026) found only Tomokiyo's paper for this letter."},
        "Tomokiyo 2018 reconstructs the 1476-79 cipher; targets/ferdinand1473 holds key_1473 and key_1474 (earlier ciphers), not tested on this letter.",
        "targets/ferdinand1473 lists /123 as unchecked; no catalogue entry; known.py on '20211' and 'R1172' finds only this lead and Ferdinand-series notes.",
        "read",
        closed=("DECODE R1172 records an inline plaintext on the leaf and Tomokiyo 2018 reconstructs the cipher of this letter's "
                "1476-79 group naming MSS/20211/123; reopen only if an image shows no interlinear decipherment."))}

# ---------------------------------------------------------------- 2755 Courten
P["2755"] = {
    "verdict": "partly_read", "confidence": "medium",
    "note": ("The lead's core, d'Argenson's ciphered memoir of 13 Jan 1745 (Cn B 5/3/5), is filed with two units the AEV calls "
             "'mis en clair' (5/3/5bis, 19 Jan, and 5/3/5ter): a clear version on file. 5/3/6/6bis and the two partly ciphered "
             "letters of 28 Feb 1745 (5/3/8, 5/3/10) were not described further; the fonds is private, 'Consultation restreinte'."),
    "access": "archive",
    "access_note": ("AEV scopequery.vs.ch record pages (opened in Chrome on 15 Nov 2026); no images; owner's permission needed. "
                    "Not re-fetched by script here."),
    "vetting": block(
        {"kind": "not online",
         "where": ("AEV, fonds de Courten, Cn B 5/3/5 ('Mémoire chiffré pour le comte de Courten', Versailles 13 Jan 1745, cahier de 12 "
                   "pages), 5/3/5bis and 5/3/5ter ('mis en clair'), 5/3/6 and 6bis ('Mémoire militaire chiffré du ministre "
                   "d'Argenson', 17 Jan), 5/3/8 and 5/3/10 ('en partie chiffrée', 28 Feb 1745): descriptions as recorded by the 15 Nov sweep and vetting pass."),
         "extent": "Seven units; the memoir of 13 Jan is a 12-page cahier; the extent of cipher in the others is not described.",
         "cipher": "French ministry cipher of 1745 (not seen). A clear version ('mis en clair') of the 13 Jan memoir is filed beside it, so that unit fails the bar."},
        {"decode": "known.py 'Courten', 'Cn B 5/3': only the Austria/Swiss sweep files and this lead; no DECODE record found in the dumps.",
         "tomokiyo": TOMO, "lasry": LASRY,
         "edition": ("Frederick II's Politische Correspondenz / Oeuvres print his reply to d'Argenson's memoir of 29 Jan 1745 (web search "
                     "16 Nov 2026), not the 13 Jan memoir to Courten; not compared. The 1954 Valais article on Courten (doc.rero.ch "
                     "I-N177-1954-005) now resolves to the RERO DOC closure notice, not the text."),
         "literature": "One web search (Courten, d'Argenson, 1745, mémoire chiffré): HLS article on Courten, nothing on the cipher."},
        "No key held; the 'mis en clair' units are plaintext for the 1745 cipher. Not tested.",
        "known.py on the shelfmark and names: no catalogue entry or target; the 1757 Choiseul-Courten units (Cn B 5/11/6-8) are a separate lead.",
        "partly_read",
        closed=("The ciphered memoir Cn B 5/3/5 has its clear version filed beside it (5/3/5bis, 5/3/5ter 'mis en clair'); the other "
                "units are undescribed and restricted, so only a reading-room look at 5/3/6, 5/3/8 and 5/3/10 could make a new lead."))}

# ---------------------------------------------------------------- no verdict
P["2231"] = {"verdict": None, "confidence": None,
             "note": ("Not assessable: the blocker recorded on 11 Nov stands. Lang 2015 marks MNL OL E 190 43. doboz 5. tétel no. 597 "
                      "'nincs feltörve', but Szilágyi 1883 (pp. 667-674) prints the clear text of a Rakoczi-to-Rácz cipher letter of "
                      "19 Jan 1642 that Rácz could not read; if no. 597 is that letter it is read. Needs an image of no. 597. The 1883 "
                      "PDF (REAL-EOD 6176) did not open after download here (0 pages)."),
             "access": "archive", "access_note": "E 190 database, no images; MNL OL reading room or a scan order."}
P["2487"] = {"verdict": None, "confidence": None,
             "note": ("Not assessable as a row: eight letters of two writers. MNL records read 16 Nov: H Fasc. 233 fol. 6-7 (to Csúzi, "
                      "10 Feb 1710) and 8-9 (28 Feb 1710) 'nagyrészt megfejtetlen', 12-15 and 22-25 (31 Jan 1710, original and "
                      "duplicate) and 26-30 (Horváth's diary extract, Apr-May 1710) 'részben'; E Fasc. 108 fol. 13-16 (Pápai, 16 Mar "
                      "1708, duplicate) 'nagyrészt'; H Fasc. 234 fol. 13-14 (Pápai, 17 Jun 1710) 'pár sor'; D Fasc. 79 fol. 19-20 "
                      "deciphered later in pencil (drop). No edition field in any of these records. Benda 1963 and Thaly not reachable "
                      "(Hungaricana 403). Split Horváth's five 1710 pieces (with keys T.Rad.11/23 from DECODE's Horváth-Pápai sets) "
                      "from Pápai's two before vetting."),
             "access": "archive", "access_note": "MNL item records; no images."}
P["2488"] = {"verdict": None, "confidence": None,
             "note": ("Mixed row of seven writers; not assessable as one lead. MNL records read 16 Nov: H 240 fol. 112-113 (Szent-Ivány, "
                      "14 May 1711) is printed (Bánkúti-Mészáros, Már nem háború..., no. 17); fol. 78-83 (29 Apr 1711) 'részben'; "
                      "H 235 fol. 48-51 (Rosenau = Klement, London 18 Sep 1711, 'nagyrészt'); E 111 fol. 125 (Dániel, Foksány 23 Dec "
                      "1710, 'nagyrészt'); G 225 fol. 1-4 (Dániel, Jassy 4 Sep 1710, 'pár sor'); E 111 fol. 71-72 (Fierville, Danzig "
                      "14 Sep 1708, French, 'részben'); B 20 fol. 74 ([Bercsényi] to [Esterházy Dániel?], 'nagyrészt'). The two A2 "
                      "Fasc. 2 letters (Rakoczi to Korbe and to Cantacuzino, wholly cipher) are proposed as '2488-split'. Klement "
                      "(Fiedler, Actenstücke) and Bercsényi editions not opened."),
             "access": "archive", "access_note": "MNL item records; no images."}
P["2490"] = {"verdict": None, "confidence": None,
             "note": ("Not assessable. MNL record 13669 (read 16 Nov): György I Rákóczi to N.N., about 1646-47, Hungarian, 'részben "
                      "megfejtetlen számjelekkel', content note 'a követnek 1646. jún. 19-i levél célbaéréséről kell érdeklődnie' (an "
                      "instruction to an envoy to ask whether a letter of 19 Jun 1646 arrived). Beke-Barabás, I. Rákóczi György és a "
                      "porta (1888, MEK 20116, text searched) prints the 1645-48 Porte letters with cipher passages resolved in italics "
                      "('titkos jegyekkel', pp. 856-888) but no 19 Jun 1646 letter was found; Szilágyi 1875 (MEK 18041) and 1883 not "
                      "searched. Needs the scan (addressee) or a page-by-page check of those volumes for 1646-47 instructions."),
             "access": "archive", "access_note": "MNL item record; no images."}
P["2776"] = {"verdict": None, "confidence": None,
             "note": ("Not assessable: DAVEL (davel.vd.ch detail.aspx) returns 403 'Accès non autorisé' to curl (WAF), so the D 6/1 "
                      "sub-units could not be read to match Wrisberg's or Robethon's key; the row must first be narrowed to one "
                      "correspondent and key (one-key rule). One web search (16 Nov) found only the Wrisberg 1722 D 4 record, no "
                      "edition or study of the ciphers. Next pass in Chrome."),
             "access": "archive", "access_note": "ACV inventory (DAVEL) only; Chrome needed."}

# ---------------------------------------------------------------- Affry (filled by affry block below)
AFFRY = json.load(open("raw/affry_summary.json", encoding="utf8"))
FRIX = ("AEF friXplore (archives.fr.ch/search/results, server-rendered, curl) harvested 16 Nov 2026 for 'transcription chiffre', "
        "'transcription dépêche', 'décryptage', 'lettre chiffrée', 'Rouillé Affry', 'Bernis Affry', 'Estrées', 'Choiseul Affry', "
        "'chiffrée' (frixplore.py; 1,659 Affry pieces parsed to raw/affry_rows.json; pairing by affry_pairs.py, raw/affry_summary.json)")
AFF_DECODE = ("known.py 'Affry (de Boccard)', 'AEF Affry': only the French-Swiss sweep files and these leads. DECODE holds the "
              "Nationaal Archief intercepts of d'Affry's own letters (targets affry1757, affry1757c, R1064-R1076, R1071, R2067), "
              "not these incoming dispatches.")
AFF_ED = ("No edition of the Rouillé/Bernis/Choiseul-to-d'Affry dispatches found; the transcriptions filed in the fonds are the "
          "decipherments. The ministry's own minutes are in AMAE Correspondance politique Hollande (not checked).")
AFF_LIT = "One web search in the sweep; no study of these Fribourg pieces. targets/affry1757 NOTES cite only the Nationaal Archief and Lyonet."


def affry(ser_list, who, verdict, conf, note, extra_cipher, closed):
    s = [AFFRY[str(x)] for x in ser_list]
    ex = [e for x in s for e in x["transcription_examples"]][:4]
    return {
        "verdict": verdict, "confidence": conf, "note": note, "access": "archive",
        "access_note": "AEF Affry (de Boccard): no digital objects ('Multimedias: Sans'); reading room or reproduction order.",
        "vetting": block(
            {"kind": "not online",
             "where": FRIX + "; series " + ", ".join(map(str, ser_list)) + ". Examples: " +
                      "; ".join(f"{k} ({d}) '{t}'" for k, d, t in ex) + ".",
             "extent": (f"{sum(x['transcription_pieces'] for x in s)} transcription/décryptage pieces found in series "
                        + ", ".join(map(str, ser_list)) + f" for the dispatches of {who}; ciphered pieces are identified in the "
                        "inventory almost only through the transcription filed beside them."),
             "cipher": ("French ministry cipher (not seen). Each dispatch the inventory marks as ciphered has a 'Transcription du "
                        "chiffre' / 'Transcription de la dépêche chiffrée' / 'Décryptage' piece filed next to it with the same date "
                        "or number, i.e. the decipherment is with the text. " + extra_cipher)},
            {"decode": AFF_DECODE, "tomokiyo": TOMO, "lasry": LASRY, "edition": AFF_ED, "literature": AFF_LIT},
            ("No key in the fonds identified for these series; AEF Affry 280.209 'Chiffre avec Botteman' and 280.210 'Premier chiffre "
             "remis par le duc de Choiseul et le chancelier du Muy' are key sheets (not seen, not tested). The filed transcriptions "
             "would rebuild any key."),
            ("known.py on the AEF shelfmarks and names: no catalogue entry; related targets affry1757/affry1757c are d'Affry's outgoing "
             "letters (Nationaal Archief, Lyonet), and lead 2773 (Havrincourt, Affry 267) is the promoted residue of another series."),
            verdict, closed=closed)}


P["2766"] = affry([225], "Rouillé (1755-57)", "read", "medium",
                  ("Every Rouillé dispatch the AEF inventory marks as ciphered is followed by a 'Transcription de la dépêche chiffrée' "
                   "of the same date (30 found, Mar 1756 - Jun 1757); no ciphered Rouillé piece without one was found."),
                  "No piece in 225 is titled ciphered without a transcription.",
                  "The AEF inventory files a contemporary transcription beside each ciphered Rouillé dispatch in series 225.")
P["2767"] = affry([226], "Bernis (1757-58)", "read", "medium",
                  ("Series 226: 21 'Transcription de la dépêche ...' pieces beside Bernis's letters (Jul 1757 - Jun 1758); no "
                   "Bernis piece is described as ciphered without a transcription."),
                  "No piece in 226 is titled ciphered without a transcription.",
                  "The AEF inventory files a transcription beside each ciphered Bernis dispatch in series 226.")
P["2770"] = affry([238], "Marshal d'Estrées (1757)", "read", "medium",
                  ("Series 238: nine 'Transcription du chiffre de la lettre du maréchal d'Estrées du ...' pieces (6 May - 18 Jul 1757), "
                   "each beside the letter of the same date; the other Estrées letters are not described as ciphered."),
                  "Letters of 26 May, 17 and 26 Jun and later have no transcription and no cipher note in the inventory.",
                  "Each Estrées letter the inventory shows as ciphered has its 'Transcription du chiffre' filed beside it (238.10 to 238.54).")
P["2768"] = affry([227, 228], "Choiseul and Choiseul-Praslin (1759-62)", "partly_read", "medium",
                  ("Series 227-228: 27 transcription/décryptage pieces beside the numbered ciphered dispatches (e.g. 227.463/464 "
                   "no. 226, 228.50/51 no. 320). Four ciphered pieces had no transcription in the harvest: 227.287 'Lettre chiffrée' "
                   "8 Mar 1760, 227.465 'Document entièrement chiffré' (c. 1760), 227.516a 'Dépêche chiffrée n° 233' 13 Nov 1760 "
                   "(a '516b' may be its transcription, not surfaced) and 227.618 'Dépêche chiffrée n° 268' 7 Jun 1761: a possible "
                   "small residue lead, readable with a key rebuilt from the pairs; not seen."),
                  "Residue without a transcription in the harvest: 227.287, 227.465, 227.516a, 227.618.",
                  ("The ciphered Choiseul dispatches have transcriptions or décryptages filed beside them; at most four pieces (227.287, "
                   ".465, .516a, .618) lack one in the inventory and could be re-proposed as a residue lead after a look."))

json.dump(P, open("proposals.json", "w", encoding="utf8"), ensure_ascii=False, indent=1)
print(len(P), "proposals")
