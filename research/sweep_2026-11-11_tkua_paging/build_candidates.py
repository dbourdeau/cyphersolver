"""Writes candidates.json for the TKUA paging pass (11 Nov 2026)."""
import json
V = "https://arkivalieronline.rigsarkivet.dk/da/billedviser?epid=%s#%s,%s"
rows = [
 {
  "year": 1651, "date": "1649 to 1655 (dated leaves seen: 20 Sep 1651, 6 Jun 1654, 1655)",
  "title": "Peder Vibe (Copenhagen) → Peder Juel (Danish resident in Stockholm): about twenty private-official letters with passages and whole leaves in a number cipher",
  "correspondents": "Peder Vibe → Peder Juel",
  "place": "Copenhagen", "language": "Danish", "region": "Scandinavia", "period": "1611-1650" if False else "1651-1700",
  "shelfmark": "Rigsarkivet (Copenhagen), Tyske Kancelli, Udenrigske Afdeling (TKUA), Speciel del, Sverige: Resident Peder Juels og Mogens Høegs gesandtskabsarkiver, Ordrer og breve m.m. 1648-55 (film label C.193; the Vibe leaves are stamped 'Ny kongl. Saml. Fol. 1299 e', their former Royal Library shelfmark)",
  "folio_note": "Arkivalieronline unit 261583 (95 images), images 57-93: letters signed 'Peder Wibe' numbered in an old hand (N. 317, 319, 330 ...). Cipher on images 57, 58, 60, 62, 63, 64, 65, 67-74, 77-79, 81, 83, 84, 87, 90, 91, 93. Whole leaves in cipher: image 71 (N. 317, 21 lines, ends 'Alias plura'), image 73 (slip), image 74 (N. 330, 20 Sep 1651, 13 cipher lines), image 77, image 78 (N. 319).",
  "cls": "A",
  "status": "Viewed 11 Nov 2026 (every image 57-95 on 8-up sheets; 64, 71, 74, 78, 87 at full size). Each cipher word is a string of numbers 1-23 opened by a number from 24 to 39, the numbers marked off by small ticks below the line; three-digit numbers (211, 228, 257, 370, 401, 422, 818, 873) stand between the words as code groups. Images 71 and 74 carry no decipherment at all. Image 78 has a faint interlinear decipherment over about a third of its groups ('des', 'sche', 'ambed...'), the only one seen; the rest of the letters have the ticks only. Not on DECODE; no edition of these letters found.",
  "why": "Vibe was the king's confidant and rentemester; these are the back-channel letters to the resident in Stockholm in the years of Queen Christina's abdication and the Ulfeldt affair, and the enciphered parts are exactly what he would not write in clear.",
  "importance": 3, "solvability": 4, "difficulty": 3,
  "score_note": "Scored from the scans during the 11 Nov 2026 TKUA paging pass (research/sweep_2026-11-11_tkua_paging/); five leaves read at full size",
  "verify": "Transcribe images 71, 74 and 78; use the interlinear letters on 78 as the crib (the opening number of each word may select the alphabet). Check KB NKS 1299 e fol. for the rest of the series and for Juel's replies.",
  "links": [{"label": "Arkivalieronline viewer, image 71 (leaf wholly in cipher)", "href": V % ("19852815", "261583", "48963828")},
            {"label": "Image 74 (20 Sep 1651)", "href": V % ("19852815", "261583", "48963831")},
            {"label": "Image 78 (partly deciphered between the lines)", "href": V % ("19852815", "261583", "48963835")},
            {"label": "Daisy series record", "href": "https://daisy.rigsarkivet.dk/arkivserie_detaljer?heid=11960015"}],
  "seen": "image", "source": "Rigsarkivet Arkivalieronline paging (TKUA envoys' archives)",
  "prior_art": "open (checked 11 Nov 2026: DECODE, Tomokiyo, Fridericia 1894, Gigas 1883, web)",
  "needs_archive_scan": "no",
  "access_note": "free on Arkivalieronline, no login; full-size JPEGs at api.rigsarkivet.dk/ao/v1/images/<id> (ao.py in this folder)",
  "vetting": {
   "date": "2026-11-11", "by": "claude cloud sweep 11 Nov tkua_paging",
   "seen": {"kind": "scan",
            "where": "Arkivalieronline epid 19852815, unit 261583: images 57-95 on contact sheets, images 64, 71, 74, 78, 87 downloaded at full size (api.rigsarkivet.dk/ao/v1/images/48963828 etc.)",
            "extent": "about twenty letters with cipher; five leaves wholly or mostly in cipher (image 71: 21 lines of about 5 groups; image 74: 13 lines); several hundred groups in all",
            "cipher": "Black-and-white microfilm scans. Words written as runs of numbers 1-23 after an opening number 24-39, separated by ticks under the line, with three-digit code groups between them; clear Danish around the cipher. No decipherment is written on images 71 or 74 or on the other leaves viewed; only image 78 has small letters over part of the groups."},
   "prior_art": {
    "decode": "Not on DECODE: live searches at de-crypt.org/decrypt-web/RecordsList?search= for Vibe, Wibe, Juel, 'Peder Juel', Rigsarkivet and TKUA each returned no record (a control search 'Denmark' returned records).",
    "tomokiyo": "Not in Tomokiyo's list: the repo copy unsolved.htm has no 'Vibe' or 'Wibe'; its Denmark/Juel mentions concern other material.",
    "lasry": "No Lasry or HistoCrypt paper on Danish 1650s ciphers found (web search 'Vibe Peder Juel resident Stockholm 1651 chifre dechifreret' returned only the Swedish Oxenstierna and unrelated papers).",
    "edition": "No edition of Vibe's letters to Juel found (web search 'Peder Vibe Peder Juel breve Stockholm 1649 1655 Danske Magazin': nothing; only Juel's own 1654 relation is printed, in Fryxell's Handlingar). Fridericia, Adelsvaeldens sidste Dage (1894, archive.org full text opened) cites 'Vibe til P. Juel, 1655 (Sverig, C)' from the manuscript and prints no text.",
    "literature": "Gigas, Grev Bernardino de Rebolledo (1883, full text opened) and Fridericia use Vibe's letters to Charisius and Juel as sources but say nothing of a cipher or a decipherment of these leaves."},
   "key_check": "No key for this system is held here. Rigsarkivet's TKUA 'Chiffer' series (Daisy heid 2132747) is dated 1670-1709, later than these letters, and was not viewed; KB NKS 1416 4to (key lead of the Nordic sweep) is untested. The partial interlinear decipherment on image 78 is the only key material seen.",
   "key_in_volume": "None as a table. Image 78 of the same unit carries a partial interlinear decipherment (letters over about a third of the groups): a crib, not tested.",
   "duplicates": "known.py 'Peder Vibe', 'Peder Juel', 'NKS 1299': only the Nordic sweep README (which lists the unit as not viewed); no catalogue, lead or target. DECODE searched by name as above.",
   "verdict": "open",
   "searches": [
    {"query": "de-crypt.org RecordsList?search=Vibe / Wibe / Juel / Peder Juel / Rigsarkivet / TKUA", "result": "0 records each (control 'Denmark': records listed)"},
    {"query": "WebSearch: \"Peder Vibe\" \"Peder Juel\" breve Stockholm 1649 1655 chiffer udgivet \"Danske Magazin\"", "result": "no edition; only Juel's 1654 relation in Fryxell and biographical pages"},
    {"query": "WebSearch: \"Vibe\" \"Peder Juel\" resident Stockholm 1651 breve \"Ny kgl. Saml.\" 1299 chifre dechifreret", "result": "nothing on these letters"},
    {"query": "grep 'Vibe til' in Fridericia 1894 full text (archive.org adelsvaeldenssid00frid)", "result": "manuscript citations only (Vibe til P. Juel 1655, Sverig C; Vibe til Charisius, Holland C)"},
    {"query": "known.py \"Peder Vibe\" \"Peder Juel\" \"NKS 1299\"", "result": "no catalogue entry, lead or target"}]}
 },
 {
  "year": 1673, "date": "25 May 1673",
  "title": "Christian V → envoys Jens Juel and Christoffer Lindenov in Stockholm: royal order in a three-digit code, closing passage without decipherment",
  "correspondents": "Christian V of Denmark (countersigned Griffenfeld) → Jens Juel and Christoffer Lindenov",
  "place": "Copenhagen", "language": "Danish", "region": "Scandinavia", "period": "1651-1700",
  "shelfmark": "Rigsarkivet (Copenhagen), TKUA, Speciel del, Sverige: Jens Juels gesandtskabsarkiv (Daisy 1664-69; the scanned unit holds the 1673-74 embassy of Juel and Lindenov: instruction 20 Apr 1673, orders 1673-74)",
  "folio_note": "Arkivalieronline unit 261588 (62 images). Order of 25 May 1673: images 7-11; cipher on image 8 right, image 9 left (about 45 lines), image 10 foot and image 11 (13 lines). A loose leaf with the chancery-hand decipherment lies at image 9 right and runs to the end of the image 9 cipher; its verso was not filmed. Orders of 1674 in the same code with full interlinear decipherment: images 33-37 (July 1674) and 39-43 (Oct 1674).",
  "cls": "A",
  "status": "Viewed 11 Nov 2026 (all 62 images on 8-up sheets; 8, 9, 10, 11, 33 at full size). Code of three-digit numbers 300-906 with letters and signs as syllables, clear Danish words left between. The first cipher block is deciphered on the loose leaf (the underlined words on it are the words left clear in the order); the closing block (image 10 foot and image 11, signed 25 May 1673) has no decipherment on the leaf, and the loose leaf as filmed ends before it. The 1674 orders give several hundred code groups with their meaning (512 = Eder, 747 = ordre, 309 = Holland ...).",
  "why": "Instructions on the Franco-Swedish alliance and the Dutch war at the opening of the negotiations that failed before the Scanian War; a short passage that the sibling orders should read almost completely.",
  "importance": 3, "solvability": 5, "difficulty": 2,
  "score_note": "Scored from the scans during the 11 Nov 2026 TKUA paging pass (research/sweep_2026-11-11_tkua_paging/); five images read at full size",
  "verify": "Not vetted as open: the verso of the decipherment leaf (image 9) is not on the film and may carry the rest; Danmark-Norges Traktater and Fridericia's 'Danmarks ydre politiske Historie' were not opened for this order. Build the code table from images 33-43 and read image 11; ask Rigsarkivet whether the loose leaf has a verso.",
  "links": [{"label": "Arkivalieronline viewer, image 11 (closing cipher passage)", "href": V % ("19852825", "261588", "48964499")},
            {"label": "Image 9 (cipher and the loose decipherment leaf)", "href": V % ("19852825", "261588", "48964497")},
            {"label": "Image 33 (1674 order, deciphered between the lines)", "href": V % ("19852825", "261588", "48964521")},
            {"label": "Daisy series record", "href": "https://daisy.rigsarkivet.dk/arkivserie_detaljer?heid=11960168"}],
  "seen": "image", "source": "Rigsarkivet Arkivalieronline paging (TKUA envoys' archives)",
  "prior_art": "largely read at the time (decipherment leaf in the unit); the closing 13 lines unchecked. DECODE searches 'Juel', 'Lindenov', 'Rigsarkivet': no record; editions not opened",
  "needs_archive_scan": "no",
  "access_note": "free on Arkivalieronline, no login (ao.py in this folder)"
 }
]
json.dump(rows, open("candidates.json", "w"), ensure_ascii=False, indent=1)
print(len(rows), "rows")
