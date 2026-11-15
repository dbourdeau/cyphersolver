import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
BY = "claude session 14 Nov 2026 (Claude Sonnet 5.5), Koc/Ottoman deep-sweep vetting"
D = "2026-11-14"
out = {}

KOC = "https://cdm21054.contentdm.oclc.org/digital/collection/HPBK/id/%d"
HPBK_PA = {
    "decode": "known.py (DECODE views dumps, HCPortal index, Cryptoole snapshot) on 'HPBK', 'Hilmi', 'Mabeyn', 'Koc', 'Yemen', 'Morier' (14 Nov 2026): no DECODE record from Koc University, the Hilmi Pasa collection or Yildiz/Mabeyn telegrams.",
    "tomokiyo": "Web search naming Tomokiyo, Cryptiana, Ottoman telegraph cipher, Hilmi Pasha, Yemen (14 Nov 2026): no Cryptiana page on Ottoman palace or telegraph codes of 1896-1902; results were Bingol's Cryptologia papers and general telegraph-code pages.",
    "lasry": "Same search for Lasry and HistoCrypt: nothing on Yildiz/Mabeyn telegrams; the Ottoman item that turned up was Ben-Bassat's WWI telegrams to the yishuv (Haifa), a different series and period; no GL.htm entry found.",
    "edition": "No edition and no printed decipherment of any HPBK telegram found: the collection's own catalogue says 'content could not be deciphered' for most, and Turkish studies of Hilmi Pasa's Yemen governorship (Yesilyurt, OTAM 2013) and of the Yemen telegraph network (Cakilci, Turkiyat Mecmuasi 2022) do not print cipher text.",
    "literature": "Turkish literature searched 14 Nov 2026 (Hilmi Pasa Yemen sifreli telgraf, Yildiz Perakende sifre): Bingol's work (Cryptologia 2022/2023; the Turkish study of 'ozel amacli sifre ve kodlamalar' in the second half of the 19th century, CEEOL) and Karabacak Yilmaz (TTK) cover diplomatic and BOA ciphers, not the palace-to-Yemen traffic of 1896-1902.",
}


def pa(**kw):
    d = dict(HPBK_PA)
    d.update(kw)
    return d


# ------------------------------------------------------------------ 2628 system B
B_ITEMS = [495, 498, 518, 524, 527, 536, 541, 546, 562, 575, 577, 580, 583, 585, 587, 602, 623, 644, 652, 675, 1761]
out["2646"] = {
    "date": D, "by": BY,
    "seen": {
        "kind": "scan",
        "where": "Koc HPBK page images, viewed 14 Nov 2026 in the sweep (about 100 images from the CONTENTdm API) and in this pass; the 502-ing items 495, 498, 518, 524, 527, 536, 623 and 1761 were fetched through the image host the CONTENTdm record names (libdigitalcollections.ku.edu.tr IIIF, page id = item id minus 2). Example: " + KOC % 541 + ", " + KOC % 585 + ".",
        "extent": "21 single sheets, one telegram each, 1896(?)-1900: sheets of roughly 40 to 150 two-digit numerals in rows or in the form's printed grid (541, 495, 498, 524, 583, 536, 518 are grids); all viewed (a count of numerals per sheet was not made).",
        "cipher": "A stream of two-digit numerals (values about 44-49, 55-59, 64-71) with one Arabic letter written over or beside most numerals on 495, 498, 518, 524, 536, 541, 546, 562, 575, 577, 580, 583, 585, 623, 644, 652, 675; 587 and 602 are numerals with few or no letters. 527 and 688 (the latter in entry 2575) are free-line sheets with some clear Turkish words between the numerals; 1761 is a dense sheet of letters. The overwritten letters are the clerk's reading of each numeral, so every sheet with letters is a ciphertext with a partial reading on it; no full plaintext is written out, and no Turkish translation is filed with these sheets.",
    },
    "prior_art": pa(),
    "key_check": "No codebook or table is held or known. The clerk's letters over the numerals are a partial key carried on the sheets themselves (recorded in key_in_volume); they give one letter per numeral, not the Turkish text. Not tested here: no transcription was made, so whether the letter-per-numeral mapping is consistent across sheets is open. Sheets 587 and 602 carry the numerals without letters.",
    "key_in_volume": "The clerk's Arabic letters written over most numerals on 17 of the 21 sheets (a partial reading on the page); the printed grid sheets 541, 495, 498, 524, 583, 536, 518 show the letters in the cells.",
    "duplicates": "known.py on the shelfmarks and dates (14 Nov 2026): none of these 21 items is in an existing entry. Items of the same system B already sit in other entries and are not repeated here: 533 and 688 (entry 2575, whose 'five-digit groups' description fits only 772), and 483, 576, 578, 599 (entry 2577, which pools B with system A). Split from system A (entry 2647) on the one-key-per-entry rule: A is five-digit groups with Turkish words written over them, B is two-digit numerals with single letters over them.",
    "searches": [
        {"query": "Hilmi Pasa Yemen Yildiz sifreli telgraf sifre cozumu Mabeyn sifre katibi telgraf Yemen 1898 sifre sistemi (web search)",
         "result": "Koc library collection page, TDV Islam Ansiklopedisi 'Huseyin Hilmi Pasa', Yesilyurt OTAM 2013, Karabacak Yilmaz TTK; nothing on how these Mabeyn telegrams were enciphered or any printed cipher text."},
        {"query": "Ottoman Yildiz palace cipher telegrams Yemen 1900 codebook numeric code deciphered Cryptologia Tomokiyo Lasry (web search)",
         "result": "Bingol's Cryptologia papers (to 1877), Ben-Bassat WWI telegrams (Haifa), Cakilci on the Yemen telegraph network; no study of the 1896-1902 palace-to-Yemen codes and no Tomokiyo or Lasry item."},
        {"query": "known.py 'Hilmi', 'HPBK', 'Mabeyn', 'Yemen', 'Koc' against catalogue, leads, DECODE dumps, queue (local)",
         "result": "Only the sibling rows 2575-2581 of the 14 Nov sweeps; no DECODE id, no earlier entry."},
        {"query": "CONTENTdm API items 483, 495, 498, 518, 524, 527, 533, 536, 688, 1761 (record fields, image host)",
         "result": "Titles and dates confirm Yemen telegrams (Mehmed Kamil as clerk on 518, 477, 583); image host libdigitalcollections.ku.edu.tr serves the pages the cdm21054 image route 502s on."},
    ],
    "verdict": "open",
    "lead_updates": {
        "title": "Mabeyn to Yemen, system B: 21 telegrams in two-digit numerals with the clerk's Arabic letters over them, 1896(?)-1900 (HPBK, Hilmi Pasa collection)",
        "shelfmark": "Koc University (Istanbul), Hilmi Pasa Belgeleri Koleksiyonu (CONTENTdm HPBK), items 495, 498, 518, 524, 527, 536, 541, 546, 562, 575, 577, 580, 583, 585, 587, 602, 623, 644, 652, 675, 1761",
        "date": "Jun 1898 - Nov 1900 (580 and 587 are catalogued 8 Aug 1896; 583 and 585 undated)",
        "year": 1898,
        "correspondents": "Mabeyn-i Humayun cipher clerks (Mehmed Kamil named on 518 and 583) -> Yemen Province (Huseyin Hilmi Pasa)",
        "folio_note": "21 sheets, one telegram each. Dates as catalogued: 675 (20 Jun 1898), 644 (28 Jun), 652 (3 Jul), 623 (4 Jul), 602 (12 Jul), 498 (16 Aug), 541 (7 Sep), 495 (23 Sep), 562 (6 Feb 1899), 527 (24 Apr), 577 (30 Apr), 546 (4 May), 524 (20 Aug), 536 (21 Nov), 575 (6 Feb 1900), 518 (14 Nov 1900), 1761 (18 Jun 1898), 580 and 587 (8 Aug 1896 as titled; 587's date field says 1898), 583 and 585 undated. Not in this entry (other entries): 533 and 688 (2575, same system B), 483, 576, 578, 599 (2577). Clear sheets of the same days that serve as cribs: 725 and 748 (28 Apr 1901) and 726 and 764 (5 Jun 1901) against 578/599 and 576 (entry 2577); 1070 (6 Feb 1900) against 575 (this entry); the others of the 36 items of old lead 2578 are plain letters.",
        "status": "System B of the Mabeyn-Yemen telegrams. Seen on the page images (14 Nov 2026): two-digit numerals with one Arabic letter over most of them on 17 sheets; 587 and 602 numerals only. Catalogued as not deciphered; no reading, key or edition found. A partial reading (letters) is on the sheets; crib sheet for 575 is 1070.",
        "why": "Many sheets of one numeral system with the clerk's own letter-by-letter reading on the page: a ready training set for the numeral-to-letter mapping, and clear sheets of the same days for 575 and (in 2577) 576, 578, 599.",
        "importance": 4, "solvability": 4, "difficulty": 2,
        "verify": "Transcribe 541 (grid, 8 columns) and 585; tabulate numeral to letter; test the mapping on the other 17 sheets and on the six sheets of 2577; read the letters as Turkish (Arabic script) and compare 575 with the clear 1070.",
        "seen": "image",
        "needs_archive_scan": "no",
        "links": [{"href": KOC % i, "label": "HPBK item %d" % i} for i in B_ITEMS],
    },
}

# ------------------------------------------------------------------ 2629 system A
A_ITEMS = [542, 551, 560, 563, 565, 568, 569, 579, 581, 600, 656, 660]
out["2647"] = {
    "date": D, "by": BY,
    "seen": {
        "kind": "scan",
        "where": "Koc HPBK page images, viewed 14 Nov 2026 in the sweep and in this pass (e.g. " + KOC % 600 + ", " + KOC % 569 + ", " + KOC % 542 + "); 772 of entry 2575 was viewed in the earlier pass.",
        "extent": "12 single sheets, one telegram each, Dec 1898 - Oct 1902: five-digit groups in lines (the form of 600 gives 48 words) or in the printed grid (569, 568); all viewed, groups not counted per sheet.",
        "cipher": "Five-digit code groups with a Turkish word written over or beside many groups: on 600, 563, 579, 542, 551, 560, 568, 569, 565 and 581 most groups carry a word, 656 and 660 fewer. The words are the clerk's reading of each group; no full Turkish text is written out on the sheets, though the clear 'translations' 732 (9 Apr 1902), 766 (13 Apr 1902) and 727 (18 Dec 1898, vs 772) are filed in the collection as separate sheets.",
    },
    "prior_art": pa(
        tomokiyo="Web search naming Tomokiyo, Cryptiana, Ottoman palace codebook, five-digit code groups, Yildiz (14 Nov 2026): no Cryptiana page on Ottoman telegraph codebooks; general telegraph-code pages only.",
        literature="Bingol, 'Codes and codebooks' in Ottoman usage (Turkish study of a July 1881 archive sample) and his Cryptologia papers (to 1877) are the nearest work; they do not cover the 1898-1902 Mabeyn five-digit code. No study of the HPBK five-digit telegrams found (14 Nov 2026)."),
    "key_check": "No codebook is held or known. The Turkish words over the groups are a partial key carried on the sheets (key_in_volume); the clear sheets 732 and 766 of 9 and 13 Apr 1902 each appear to quote a five-digit number in a parenthesis in the clear text, which may tie them to the cipher telegrams of those days (542/579, 550/568): not tested, no transcription made. Not tested whether the 1898 sheet 772 (entry 2575) uses the same codebook as these 1900-02 sheets.",
    "key_in_volume": "Turkish words written over most five-digit groups on 10 of the 12 sheets (a partial reading on the page); clear same-day sheets 732, 766 (and 727 for 772 in entry 2575).",
    "duplicates": "known.py (14 Nov 2026): none of these 12 items is in an existing entry. Same-layout items already in other entries are not repeated: 772 (entry 2575, 18 Dec 1898, the same system A by layout) and 550 and 595 (entry 2577, pooled with system B). Kept separate from 2575 because whether 772 and these sheets share one codebook is untested (one key per entry); merge if a group-table comparison shows one codebook. 556 (17 Apr 1902) is on the sweep list but its sheet is a clear letter, not a cipher.",
    "searches": [
        {"query": "Ottoman telegraph codebook five-digit code groups Mabeyn Yildiz 1900 cipher Bingol codes and codebooks (web search)",
         "result": "Bingol's Ottoman diplomatic cryptography papers and his Turkish study of 19th-c. codes and codebooks (CEEOL); nothing on a five-digit Mabeyn code or on HPBK."},
        {"query": "Hilmi Pasa Yemen 1902 Italian warships Luhayye telegram Mabeyn sifre telgraf cozulmus (web search)",
         "result": "Studies of Hilmi Pasa's Yemen governorship and the telegraph network (OTAM 2013, Turkiyat Mecmuasi 2022) without cipher text; no printed reading of the 1901-02 telegrams."},
        {"query": "known.py 'HPBK', 'Luhayye', 'Italian', 'Mabeyn' and the item numbers 542, 551, 560, 568, 579, 600 (local)",
         "result": "Only the sibling rows 2575-2581; no DECODE record."},
        {"query": "CONTENTdm API field descriptions of HPBK 542, 551, 560, 568, 579, 600, 732, 766",
         "result": "Descriptions give subject and date (bandits and telegraph sabotage 9 Apr 1902; Italian ships 15 Oct 1902; 'encrypted document' for the clear 732 and 766); none says the cipher was solved."},
    ],
    "verdict": "open",
    "lead_updates": {
        "title": "Mabeyn to Yemen / 7th Army, system A: 12 telegrams in five-digit code groups with the clerk's Turkish words written over them, Dec 1898 - Oct 1902 (HPBK)",
        "shelfmark": "Koc University (Istanbul), Hilmi Pasa Belgeleri Koleksiyonu (CONTENTdm HPBK), items 542, 551, 560, 563, 565, 568, 569, 579, 581, 600, 656, 660",
        "date": "Dec 1898 - Oct 1902 (565 and 581 undated)",
        "year": 1901,
        "correspondents": "Mabeyn-i Humayun cipher clerks -> Yemen Province and 7th Army (Musir)",
        "folio_note": "12 sheets. Dates as catalogued: 660 (11 Dec 1898), 656 (12 Mar 1899), 563 and 569 (15 Feb 1900), 600 (21 Feb 1901), 560 (10 Dec 1901), 542 and 579 (9 Apr 1902), 568 (13 Apr 1902), 551 (15 Oct 1902), 565 and 581 undated. Not in this entry: 772 (2575, same layout), 550 and 595 (2577). Clear cribs on the same days: 732 (9 Apr 1902) for 542 and 579; 766 (13 Apr 1902) for 568 and 550; 447 and about 20 clear telegrams of 15-17 Oct 1902 for 551; 727 (18 Dec 1898) for 772. 556 (17 Apr 1902) is a clear sheet.",
        "status": "System A of the Mabeyn-Yemen telegrams. Seen on the page images (14 Nov 2026): five-digit groups with Turkish words written over most of them; catalogued as not deciphered; no reading, codebook or edition found. A partial reading (words) is on the sheets and clear same-day sheets exist for 9 and 13 Apr 1902.",
        "why": "Five-digit code groups with the clerk's own word-by-word reading on the page and clear same-day sheets: the raw material to rebuild a code table, from sheets that were never transcribed.",
        "importance": 4, "solvability": 4, "difficulty": 3,
        "verify": "Transcribe 600 (48 groups) and 569 (grid); list group -> word pairs; test them on 563/569, 542/579 and on 772 with the clear 727; compare the clear 732 and 766 with 542/579 and 568.",
        "seen": "image",
        "needs_archive_scan": "no",
        "links": [{"href": KOC % i, "label": "HPBK item %d" % i} for i in A_ITEMS],
    },
}

# ------------------------------------------------------------------ 2631 Morier 1808
out["2649"] = {
    "date": D, "by": BY,
    "seen": {
        "kind": "scan",
        "where": "Qatar Digital Library, IOR/L/PS/9/67/18 (https://www.qdl.qa/en/archive/81055/vdc_100038378586.0x000016), folio 2r (image 3 of 20) viewed in a Claude in Chrome tab on 14 Nov 2026 through the IIIF image iiif.qdl.qa/iiif/images/81055/vdc_100038378586.0x000016/IOR_L_PS_9_67_18_0003.jp2.",
        "extent": "One item of 10 folios (20 images), a copy of one letter; image 3 (f. 2r) is a column of about 15 lines of numerals; the other folios were not opened one by one.",
        "cipher": "Lines of two-digit and some single- and three-digit numerals separated by full stops (46. 50. 47. 33. 46. 37. 79 ... 65. 74. 40. ...), in one hand, with no letters, words or interlinear plaintext on the folio; the record says 'a copy of a letter written in numerical code' and gives no decipherment.",
    },
    "prior_art": {
        "decode": "known.py 'Morier', 'Harford Jones', 'Minto' and 'IOR/L/PS/9/67' (14 Nov 2026): no DECODE record; the repo has Harford Jones's 1798 Dundas code (catalogue, jones1802) and his 1805 cipher letter to Grant (lead 1993), different documents.",
        "tomokiyo": "Web search naming Tomokiyo, Cryptiana, Harford Jones and Morier (14 Nov 2026): no Cryptiana page on a British envoy to Persia's numerical code of 1808.",
        "lasry": "Same search for Lasry and HistoCrypt: nothing on Jones, Morier or Persia 1808 cipher.",
        "edition": "No edition: the British Library record (searcharchives.bl.uk 041-003356315) and the QDL record describe the letter as 'a copy of a letter written in numerical code' to Lord Minto from Bombay, 28 Apr 1808, enclosed in Jones's letter of 30 Apr to the Secret Committee, and give no deciphered text. The plain letter may be in the Bengal Secret Letters / Minto enclosures series (QDL 'Enclosures to Bengal Secret Letters of 21 December 1808, 20 January and 3 April 1809'): searched by title only, not opened.",
        "literature": "Web search 'Harford Jones 1808 Morier numerical code letter Minto' (14 Nov 2026) returned only the BL/QDL catalogue records of the series; no study of the code.",
    },
    "key_check": "No key is held or known. A decipherment or plain copy of this letter may exist in the Minto/Bengal Secret enclosures (not opened), which would make it a key lookup if found: unchecked.",
    "duplicates": "known.py on 'Morier', 'Harford Jones', 'IOR/L/PS/9/67' (14 Nov 2026): only the sweep row; Jones's 1798 Dundas code and the 1805 Grant letter are other documents. Narrowed to IOR/L/PS/9/67/18 (10 folios); /19 (4 images), /20 and /21 of the same series and dates are not part of this entry.",
    "searches": [
        {"query": "Harford Jones 1808 Morier numerical code letter Minto Persia cipher deciphered IOR/L/PS/9/67 (web search)",
         "result": "BL and QDL catalogue records of the IOR/L/PS/9/67 series (Jones to the Secret Committee, Minto to Jones); nothing says the numerical code was broken or gives a key."},
        {"query": "QDL record page of IOR/L/PS/9/67/18 and its IIIF manifest (Chrome, same-origin)",
         "result": "20 images, 10 folios, 'A copy of a letter written in numerical code'; Open Government Licence; no transcription field."},
        {"query": "known.py 'Morier' 'Harford Jones' 'Minto' 'IOR/L/PS/9/67' (local)",
         "result": "Only the sweep's row and the unrelated Jones 1798 Dundas and 1805 Grant items."},
    ],
    "verdict": "open",
    "lead_updates": {
        "title": "James Morier (for Sir Harford Jones) to Lord Minto, Bombay 28 Apr 1808: a letter in numerical code, copy of 10 folios (IOR/L/PS/9/67/18)",
        "shelfmark": "British Library IOR/L/PS/9/67/18 (20 images), Qatar Digital Library vdc_100038378586.0x000016",
        "folio_note": "IOR/L/PS/9/67/18 only (10 folios). Siblings of the same series and dates not in this entry: /19 (4 images), /20, /21 (QDL vdc_100038378586.0x000017 to .0x000019), not opened. Folio 2r seen: numerals only.",
        "status": "A copy of one numerical-code letter, Jones to Minto via Morier, 28-30 Apr 1808. Numerals only on the folio seen, no plaintext on it; no decipherment recorded in the BL or QDL record.",
        "seen": "image",
        "needs_archive_scan": "no",
    },
}

# ------------------------------------------------------------------ closes and unvetted
out["2648"] = {
    "date": D, "by": BY, "verdict": "not_cipher",
    "seen": {"kind": "scan", "where": "Koc HPBK 1791 (page id 1787), image fetched 14 Nov 2026 from libdigitalcollections.ku.edu.tr/iiif/2/HPBK:1787/full/1400,/0/default.jpg"},
    "closed": "The item is a single blank envelope or wrapper (2530 x 1451 px) with a few words in red ink; the record's description is only 'a document on special encryption book' and carries no cipher text or key. Not a cipher book and not a ciphertext.",
}
out["2651"] = {
    "date": D, "by": BY, "verdict": "duplicate",
    "closed": "Same five MHC items (1186, 3874, 1830, 3284, 3352) and the same 1921 telegrams as lead 2581 (Koc MHC War of Independence cipher sheets, 5 items, 3352 'not yet deciphered'); 2581 already carries them and is held as outside the pre-1920 scope.",
}
out["2650"] = {"unvetted": "Open Jerusalem (openjerusalem.org) did not open from Python, WebFetch or a Chrome tab in the 14 Nov sweep, so the six 1907 records were not seen; ciphertext not seen, prior art not searched beyond a search-engine snippet."}
out["2576"] = {
    "date": D, "by": BY, "verdict": "duplicate",
    "closed": "All 17 items are placed in entries 2646 (system B: 495, 498, 518, 524, 527, 536, 541, 546, 562, 575, 577, 580, 587, 602, 1761) and 2647 (system A: 563, 569), split by key after the 14 Nov 2026 viewing of every sheet; the old pooled row spanned two cipher systems.",
}
out["2578"] = {
    "date": D, "by": BY, "verdict": "duplicate",
    "closed": "All 36 sheets viewed 14 Nov 2026: six are ciphertext and now sit in entries 2646 (623, 644, 652, 675: system B) and 2647 (656, 660: system A); the other 30 (212, 733, 736, 737, 740, 751, 756, 760, 773, 782, 790, 1056-1058, 1068-1070, 1082, 1086, 1249, 1252, 1259, 1287, 1946, 1955, 1964-1966, 2227, 2268) are plain Ottoman letters or fair copies, not ciphertext.",
}
out["2579"] = {
    "date": D, "by": BY, "verdict": "duplicate",
    "closed": "All 37 sheets viewed 14 Nov 2026: ciphertext 542, 551, 560, 568, 579, 600 now sits in entry 2647 (system A); 556 and the other 30 (159, 188, 199, 248, 447, 641, 723, 725, 726, 729, 732, 742, 747, 748, 755, 763, 764, 766, 769, 775, 1039, 1040, 1055, 1067, 1083, 1087, 1282, 1816, 2279, 2294) are clear Ottoman letters, fair copies or telegram forms, not ciphertext; 725/748, 726/764, 732 and 766 are the cribs recorded on 2646, 2647 and entry 2577.",
}

with open(os.path.join(HERE, "vetting.json"), "w", encoding="utf-8") as fh:
    json.dump(out, fh, ensure_ascii=False, indent=1)
    fh.write("\n")
print(len(out))
