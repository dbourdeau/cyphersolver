#!/usr/bin/env python3
"""Build candidates.json and key_leads.json for the second MNL AdatbazisokOnline pass (11 Nov 2026, cloud).
Rows come from the item database of MNL OL G 15 (II. Rákóczi Ferenc fejedelem levéltára, Emigrációba vitt rész),
re-harvested per database with mnl_db_search.py; datasheets read with mnl_sheet.py; DECODE listed with decode_list.py
and decode_views.py. Notes are quoted as the archive gives them."""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
DB = "https://adatbazisokonline.mnl.gov.hu/adatbazis/ii_-rakoczi-ferenc-fejedelem-leveltara_-emigracioba-vitt-resz/adatlap/"
def L(pairs): return [{"label": "MNL AdatbazisokOnline, G 15 " + lab, "href": DB + str(i)} for lab, i in pairs]
SRC = "MNL AdatbazisokOnline second pass (G 15), 11 Nov 2026"
NOTE = "Scored from the archive's item description during the 11 Nov 2026 second MNL AdatbazisokOnline pass (research/sweep_2026-11-11_mnl_2/); not viewed (no images online)"
ACCESS = "No images in the MNL database (record text only); order scans of the folios from MNL OL, Budapest (G 15, II. Rákóczi Ferenc fejedelem levéltára, Emigrációba vitt rész)."
BY = "claude cloud sweep 11 Nov mnl_2"

def row(year, date, title, corr, place, lang, shelf, folio, cls, status, why, imp, sol, dif, verify, links, prior, vetting=None, decode_ids=None):
    r = {"year": year, "date": date, "title": title, "correspondents": corr, "place": place, "language": lang, "region": "Central Europe",
         "period": "1701-1800", "shelfmark": shelf, "folio_note": folio, "cls": cls, "status": status, "why": why, "importance": imp,
         "solvability": sol, "difficulty": dif, "score_note": NOTE, "verify": verify, "links": links, "seen": "catalogue", "source": SRC,
         "prior_art": prior, "needs_archive_scan": "yes", "access_note": ACCESS}
    if decode_ids: r["decode_ids"] = decode_ids
    if vetting: r["vetting"] = vetting
    return r
R = []

# 1. vetted -----------------------------------------------------------------------------------------------------
R.append(row(1707, "undated (the dated pieces of the fascicle run from 1705 to Feb 1708)",
 "Anonymous French letter partly in undeciphered secret signs, among the Lubomirski papers of Rákóczi's archive",
 "unknown → unknown", "unknown", "French",
 "MNL OL, G 15 (II. Rákóczi Ferenc fejedelem levéltára, Emigrációba vitt rész), Caps. C, Fasc. 39/b, fol. 20",
 "One leaf. Neighbours in the fascicle: fol. 14-19 and 21-28 are Latin letters of Theodor Lubomirski and his secretary Georgius Reyscher from Lubló and Podolin, 1705-1708, none with a cipher note.",
 "C", "MNL item record (adatlap 15835): language 'Francia', note 'részben megfejtetlen titkos jelekkel' (partly in undeciphered secret signs). Not on DECODE: DECODE's 97 records headed 'Caps. C. Fasc. 39' are the Polish-court letters of Fasc. 39/a (their page numbers 115-347 map onto 39/a fol. 76-212).",
 "A cipher of signs (not the number cipher of the Polish correspondence) in the file on Rákóczi's dealings with Lubomirski over the Szepes towns, 1707-08.",
 2, 1, 4, "Order a scan of Caps. C Fasc. 39/b fol. 20; compare the signs with the sign alphabets among DECODE's G 15 Caps. C Fasc. 43 keys (Láng T.Rak.63 is a key 'with signs').",
 L([("C Fasc. 39/b fol. 20", 15835), ("C Fasc. 39/b fol. 18-19 (Lubomirski, Podolin 7 Feb 1708; neighbour)", 15834)]),
 "open (checked 11 Nov 2026: DECODE full G15 list and record views, Láng 2015 repertory, Láng 2018, Tomokiyo unsolved list, web)",
 {"date": "2026-11-11", "by": BY,
  "seen": {"kind": "not online", "where": "MNL AdatbazisokOnline datasheets (record text only, no images), read 11 Nov 2026: adatlap 15835, with the neighbours 15832-15838.",
           "extent": "One leaf (fol. 20); the share in cipher is not stated beyond 'partly'.",
           "cipher": "Archive's note, verbatim: 'részben megfejtetlen titkos jelekkel' (Nyelv: Francia; Levélíró N. N.; Címzett N. N.; s.d.; s. l.). The same database writes 'megfejtett', 'egykorúlag megfejtett' or 'Thaly által megfejtett' where a decipherment is on or with the leaf, so 'megfejtetlen' records ciphertext without one."},
  "prior_art": {
   "decode": "decode_list.py 'G15' lists 290 DECODE records; the 97 from 'Caps. C. Fasc. 39' carry page numbers 115-347, and their dated records fall on Fasc. 39/a folios (three of 16 Jan 1705 at pp. 232-240 = 39/a fol. 145-150; R902 pp. 277-279 = 39/a fol. 171-172; R922 pp. 346-347 = 39/a fol. 212). None is an undated one-leaf French letter in signs; DECODE describes all of them as numerical.",
   "tomokiyo": "The repo copy of Tomokiyo's unsolved list (unsolved.htm) and the cryptiana index page (code/crypto.htm, fetched 11 Nov 2026) were searched for Lubomirski, Rakoczi and Podolin: no entry on either.",
   "lasry": "The repo copy of Lasry's publication list (targets/esp318/lit/crypt/GL.htm) was searched for Rakoczi, Lubomirski and Hungary: no Rakoczi or Lubomirski entry, and the web search below named no Lasry paper on this archive.",
   "edition": "No edition can be matched to an anonymous, undated leaf. Thaly's Archivum Rákóczianum is credited by this database on every leaf he deciphered ('Thaly által megfejtett'); this record carries no 'Kiadási információk' field and no such credit.",
   "literature": "Láng 2015 (real-d.mtak.hu/922, pdftotext): the repertory row C.Rak.260-360 covers 'MOL G 15 Caps. C Fasc 39 (214 fols, about 100 enciphered letters)', the number cipher of the Polish correspondence, 'solved above the ciphers, mostly'; grep for '39/b' and for Lubomirski in the repertory returns nothing. Láng 2018 (archive.org OCR) has no hit for 39/b either."},
  "searches": [
   {"query": "adatbazisokonline.mnl.gov.hu, G 15 database only: megfejtetlen; titkos*; jelekkel; jegyekkel",
    "result": "The G 15 database returned 97, 284, 3 and 24 records for these terms; fol. 20 is the only record of Fasc. 39/b with a cipher note, and its note is 'részben megfejtetlen titkos jelekkel'."},
   {"query": "DECODE RecordsList search 'G15' (all pages, decode_list.py) and the record views of the 213 non-key G15 records (decode_views.py)",
    "result": "DECODE holds 290 G15 records, 97 of them from Caps. C Fasc. 39; by date and position they are letters of Fasc. 39/a, and none is described with a symbol set other than 'Numerical'."},
   {"query": "grep of Láng 2015 (dc_758_13_doktori_mu.pdf) and Láng 2018 (1001507_djvu.txt) for '39/b', 'Fasc 39', 'Lubomirski'",
    "result": "Láng 2015 has one repertory row for Fasc. 39 (C.Rak.260-360, the French number-cipher letters) and no mention of 39/b or of a sign cipher in it; Láng 2018 has no hit."},
   {"query": "web: Rákóczi levéltára \"Fasc. 39\" Lubomirski Tódor 1707 1708 francia rejtjeles levél megfejtetlen titkos jelekkel",
    "result": "The search returned Thaly's Bercsényi volumes and general works on the Rákóczi archive; nothing on this fascicle or on a French letter in signs."}],
  "key_check": "Not tested, because the ciphertext was not seen. The sign alphabets among DECODE's key records from G 15 Caps. C Fasc. 43-44 are the first to compare.",
  "key_held": "DECODE holds 76 key records from G 15 Caps. C Fasc. 43-44 (between R549 and R646); which of them, if any, is this leaf's sign alphabet is not known. Not tested.",
  "duplicates": "known.py 'Fasc. 39/b' returned no hits; known.py 'Lubomirski' returned only the 1669 Radziwill letter (another collection). Catalogue 2475-2483 and 2485 and leads 2484, 2486-2490 hold no Caps. C Fasc. 39/b folio.",
  "verdict": "open"}))

# 2. lead ---------------------------------------------------------------------------------------------------------
R.append(row(1707, "undated (the cipher letters of this fascicle that carry dates are of 1704-1710)",
 "Two anonymous cipher items next to the undeciphered letters of catalogue 2479, language given only as '[rejtjeles]'",
 "unknown → unknown", "unknown", "unknown",
 "MNL OL, G 15 (II. Rákóczi Ferenc fejedelem levéltára, Emigrációba vitt rész), Caps. A1, Fasc. 11, fol. 61-61/a and fol. 62",
 "Two items, about three leaves. Fol. 60 before them is a clear Hungarian letter to 'jó Barátom' described as 'diplomáciai témáról, rejtjelezés továbbításáról szóló ... szándékosan homályosan (nevek és adatok nélkül) fogalmazott levél' (on forwarding an encipherment).",
 "C", "MNL item records 13650 and 13651: 'Nyelv: [rejtjeles]', writer and addressee N. N., no note and no decipherment recorded. The catalogued siblings fol. 36-37 and 46-47 (catalogue 2479) have the same language value with the note 'végig megfejtetlen rejtjeles levél'; these two were left out of the first pass because they have no note. DECODE has no record from Caps. A1 Fasc. 11.",
 "They belong to the same group of anonymous cipher letters in Rákóczi's private fascicle as catalogue 2479 and add ciphertext to it.",
 2, 1, 4, "Order the scans together with catalogue 2479 (A1 Fasc. 11 fol. 36-72) and check on the leaves that nothing is written over the cipher; no vetting block here because the record has no note saying 'megfejtetlen'.",
 L([("A1 Fasc. 11 fol. 61-61/a", 13650), ("A1 Fasc. 11 fol. 62", 13651), ("A1 Fasc. 11 fol. 60 (clear letter on forwarding an encipherment)", 13649)]),
 "not vetted (11 Nov 2026): DECODE's 290 G15 records include none from Caps. A1 Fasc. 11; Láng 2015 has no 'Caps. A' shelfmark; a web search for the shelfmark found nothing."))

# 3. lead ---------------------------------------------------------------------------------------------------------
R.append(row(1707, "21 Oct 1707, 10 Dec 1707 (two exemplars), 17 Dec 1707, 13 Jan 1708, 17 Feb 1708; and 4 Jan 1708",
 "Jakab Kray, Rákóczi's agent at Danzig: duplicates and triplicates of his number-cipher reports that were only partly deciphered",
 "Jakab Kray → Francis II Rákóczi (one as 'Pompeius Cettoni')", "Gdańsk (Danzig)", "Hungarian",
 "MNL OL, G 15 (II. Rákóczi Ferenc fejedelem levéltára, Emigrációba vitt rész), Caps. D, Fasc. 83, fol. 26-27, 57-58, 59-60, 71-72; Fasc. 84, fol. 17-18, 25-26; and Fasc. 84, fol. 7-12",
 "Seven items, about 18 leaves. Each of the first six has a same-date exemplar marked 'végig megfejtett számjelekkel': Fasc. 83 fol. 28-29 (21 Oct), 66-67 (10 Dec), 69-70 (17 Dec), 87-88 (13 Jan 1708), Fasc. 84 fol. 22-23 (17 Feb, with a transcript at fol. 33r-v). Fasc. 84 fol. 7-12 (4 Jan 1708) has no same-date sibling; its note 'kisebb részben megfejtett számjelekkel' may mean only that a lesser part of the letter is in cipher.",
 "A", "MNL item notes: fol. 26-27 and Fasc. 84 fol. 17-18 'csak részben megfejtett számjelekkel'; Fasc. 83 fol. 57-58 (triplicate, No. 25) 'csak részben megfejtett számjelekkel'; fol. 59-60 (duplicate, No. 24) and fol. 71-72 (duplicate, No. 28) 'csak kis részében megfejtett számjelekkel'; Fasc. 84 fol. 25-26 (duplicate, No. 45) 'csak a második szövegrészben megfejtett számjelekkel'. Not on DECODE (no record from Caps. D Fasc. 83-84; search 'Kray' 0).",
 "Kray ran Rákóczi's Baltic finance and correspondence; the deciphered exemplars of the same dates give the plaintext, so these leaves are key material for his number cipher more than unread text.",
 2, 2, 1, "Order the pairs (e.g. Fasc. 83 fol. 26-27 with 28-29) and check whether the partly deciphered exemplar has the same text as the fully deciphered one; if so close as read, and keep Fasc. 84 fol. 7-12 only if cipher stands undeciphered on it.",
 L([("D Fasc. 83 fol. 26-27 (21 Oct 1707)", 16741), ("D Fasc. 83 fol. 57-58 (10 Dec 1707, triplicate)", 16758), ("D Fasc. 83 fol. 59-60 (10 Dec 1707, duplicate)", 16759),
    ("D Fasc. 83 fol. 71-72 (17 Dec 1707, to Cettoni)", 16765), ("D Fasc. 84 fol. 17-18 (13 Jan 1708)", 16782), ("D Fasc. 84 fol. 25-26 (17 Feb 1708)", 16787), ("D Fasc. 84 fol. 7-12 (4 Jan 1708)", 16779)]),
 "not vetted (11 Nov 2026): DECODE search 'Kray' 0 records and no G15 record from Caps. D Fasc. 83-84; Láng 2015 names Kray only as a writer to Ráday (C.Rak.67 is Rákóczi to Kray, 12 Apr 1709, MOL G 19); two web searches for an edition of Kray's Danzig letters found none; the same-date deciphered exemplars in the fascicle were not compared (no images)."))

# 4. lead ---------------------------------------------------------------------------------------------------------
R.append(row(1706, "24 Jul 1706",
 "János Pápai and Ferenc Horváth to Rákóczi, Constantinople 24 July 1706: a separate slip in undeciphered number cipher",
 "János Pápai and Ferenc Horváth → Francis II Rákóczi", "Constantinople", "Hungarian",
 "MNL OL, G 15 (II. Rákóczi Ferenc fejedelem levéltára, Emigrációba vitt rész), Caps. C, Fasc. 33, fol. 44-49",
 "Six leaves; the letter is mostly deciphered, the undeciphered part is a separate slip (cédula). By date this is DECODE R814 ('Caps. C. Fasc. 33. 80-86', 24 Jul 1706, 7 images, status Decrypted).",
 "A", "MNL item note (adatlap 15654): 'nagyrészt megfejtett, külön cédulán megfejtetlen számjelekkel'. DECODE R814 is marked Decrypted with inline plaintext; whether the slip is among its seven images was not checked (images need a DECODE login).",
 "A postscript slip of the Constantinople envoys left unread by Rákóczi's chancery; the envoys' key (DECODE R580, used in targets/papai1706) should read it.",
 2, 4, 1, "Open DECODE R814 with a login, find the slip, decode it with the R580 key table of targets/papai1706; it belongs with that target rather than in the catalogue as a new entry.",
 L([("C Fasc. 33 fol. 44-49", 15654)]) + [{"label": "DECODE R814 (login for images)", "href": "https://de-crypt.org/decrypt-web/RecordsView/814"}],
 "not vetted (11 Nov 2026): DECODE R814 found by date and marked Decrypted; Láng 2015 C.Kov.23 (24 Jul 1706) says the solution is written above the numbers; targets/papai1706 does not include R814.",
 decode_ids=[814]))

# 5. lead ---------------------------------------------------------------------------------------------------------
R.append(row(1710, "26 Mar 1710",
 "Rákóczi to an unnamed correspondent, 26 March 1710: French copy with a few words in secret numerals",
 "Francis II Rákóczi → unknown", "unknown", "French",
 "MNL OL, G 15 (II. Rákóczi Ferenc fejedelem levéltára, Emigrációba vitt rész), Caps. H, Fasc. 229, fol. 186-187",
 "Two leaves, a contemporary copy; only a few words are in cipher.",
 "B", "MNL item record (adatlap 18322): 'Fennmaradási forma: Egykorú másolat', note 'néhány szó titkos számjegyekkel' (a few words in secret numerals); the note does not say whether they are deciphered. Not on DECODE (no record from Caps. H Fasc. 229).",
 "A few enciphered names in a letter of the prince from the last year of the war; Rákóczi's French keys survive (DECODE, G 15 Caps. C Fasc. 43-44), so this is a key lookup once seen.",
 2, 2, 1, "Order fol. 186-187 and read the numerals with Rákóczi's French keys on DECODE; no block because the note does not show that the words are undeciphered.",
 L([("H Fasc. 229 fol. 186-187", 18322)]),
 "not vetted (11 Nov 2026): no DECODE record from Caps. H Fasc. 229; lead 2489 lists other folios of the same fascicle (fol. 32-34)."))

json.dump(R, open(os.path.join(HERE, "candidates.json"), "w", encoding="utf8"), ensure_ascii=False, indent=1)

K = [
 {"title": "Gáspár Beniczky to Rákóczi, Warsaw 24 and 26 April 1712: enciphered Latin letters with their plaintext drafts, one with the encipherment written above the words",
  "shelfmark": "MNL OL, G 15, Caps. H, Fasc. 241, fol. 67-69 (24 Apr 1712, Hungarian and enciphered Latin), fol. 70-73 (26 Apr 1712, 'Rejtjelezett Latin'), fol. 74 (draft of the 26 Apr letter in Latin, 'fölé írva a rejtjelezés'), fol. 75-76 (draft of the 24 Apr letter)",
  "note": "Not a candidate: both cipher letters have their plaintext drafts in the same fascicle, and fol. 74 gives the cipher groups over the words, so the key of Rákóczi's secretary in 1712 can be rebuilt from it. Not on DECODE (search 'Beniczky' 0).",
  "links": L([("H Fasc. 241 fol. 70-73", 18758), ("H Fasc. 241 fol. 74 (draft with encipherment)", 18759), ("H Fasc. 241 fol. 67-69", 18757), ("H Fasc. 241 fol. 75-76", 18760)])},
 {"title": "Jakab Kray's cipher reports from Danzig with contemporary transcripts ('rejtjeles eredeti átírása')",
  "shelfmark": "MNL OL, G 15, Caps. D, Fasc. 84, fol. 33r-35 (transcripts of letters nos. 44-47 of 14, 17, 24 and 25 Feb 1708; the cipher originals are fol. 22-32)",
  "note": "Plaintext transcripts beside the cipher originals: material to rebuild Kray's number key for the partly deciphered duplicates (candidates row 3).",
  "links": L([("D Fasc. 84 fol. 33r (no. 44)", 16791), ("D Fasc. 84 fol. 33r-v (no. 45)", 16792), ("D Fasc. 84 fol. 34 (no. 46)", 16794), ("D Fasc. 84 fol. 35 (no. 47)", 16795)])},
 {"title": "János Pápai to Rákóczi, 2 June 1710: the contemporaneously deciphered exemplar of the letter that is DECODE R740",
  "shelfmark": "MNL OL, G 15, Caps. G, Fasc. 226, fol. 31-32 ('részben egykorúlag megfejtett számjelekkel', 2 Jun 1710; by position DECODE R734, pp. 55-57, Decrypted) and fol. 50-51 ('részben megfejtetlen számjelekkel', same date; by position DECODE R740, pp. 85-88, Non-decrypted)",
  "note": "For targets/papai1706: the MNL database dates both leaves 1710.06.02, while the target's notes date R740 '2 Jan 1710' and call its cipher passage 'decoded, not read, no key material'. If fol. 50-51 is a second exemplar of fol. 31-32, R734 carries the chancery's decipherment of the same passage. Not checked on the images (DECODE login).",
  "links": L([("G Fasc. 226 fol. 50-51", 18220), ("G Fasc. 226 fol. 31-32", 18211)])},
]
json.dump(K, open(os.path.join(HERE, "key_leads.json"), "w", encoding="utf8"), ensure_ascii=False, indent=1)
print(len(R), "rows;", sum(1 for r in R if "vetting" in r), "with a vetting block;", len(K), "key leads")
