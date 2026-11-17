"""Write the closing proposals for 2790, 2795, 2927, 2921, 1158, 2551, 2918 as p/<id>.json."""
import json
T15 = "(cryptiana unsolved.htm, fetched 15 Nov 2026)"
L15 = "(GL.htm, fetched 15 Nov 2026)"


def tl(terms):
    return (f"Tomokiyo's unsolved list {T15} searched for {terms}: no hit.",
            f"Lasry's list {L15} searched for {terms}: no hit.")


P = []
t, l = tl("SP 32/14, Ruvigny and Sparr")
P.append({"id": 2790, "verdict": "partly_read", "confidence": "medium",
 "note": "TNA files a plaintext 'Extract (folio 99) from a ciphered letter (folios 100-101)' in front of the cipher, and the catalogue summarises the content from it (Ruvigny's silence on the peace overtures, Turenne's success, a Monsieur Sparr). At least part of the letter was deciphered on file; how much the extract covers is not stated.",
 "access": "archive", "access_note": "TNA SP 32/14/51, ff. 99-101, not digitised (Discovery API C17475303 read 16 Nov 2026); Kew or State Papers Online.",
 "vetting": {"seen": {"kind": "not online", "where": "TNA Discovery API record C17475303 (SP 32/14/51, ff. 99-101, dated 1689-1702, digitised false), read 16 Nov 2026. The leaves were not seen.",
  "extent": "A ciphered letter on two folios (ff. 100-101) with a one-folio plaintext extract (f. 99).",
  "cipher": "Catalogue: 'Extract (folio 99) from a ciphered letter (folios 100-101). Monsieur de Ruvigny [Earl of Galway] has not replied to the overtures for peace which your Highness told [the author] to make to the King...' The extract is a contemporary decipherment of at least part of the letter."},
  "prior_art": {"decode": "known.py on 'SP 32/14', 'Ruvigny' and 'Sparr': only this lead and the 15 Nov TNA sweep README (which already lists it among items with a decode beside them); no DECODE record.",
   "tomokiyo": t, "lasry": l,
   "edition": "No printed edition looked for beyond the catalogue; the extract on f. 99 is itself the contemporary reading.",
   "literature": "No literature search beyond the catalogue: the filed extract settles that the letter was deciphered at the time."},
  "key_check": "No key sought; the extract could serve as a crib if the remainder of ff. 100-101 is ever found unread.",
  "duplicates": "known.py on the shelfmark: only this lead; no catalogue entry for SP 32/14.",
  "verdict": "partly_read", "closed": "Closed as partly read: a contemporary plaintext extract of the ciphered letter is filed in front of it (f. 99)."}})

t, l = tl("SP 35/30, 'R W' (no relevant hit among the incidental matches of the two letters) and Atterbury")
P.append({"id": 2795, "verdict": "partly_read", "confidence": "high",
 "note": "The item is a letter 'intercepted and translated', with only the names left in cypher in the translation: the text was read in 1722 and only the name code is unresolved.",
 "access": "archive", "access_note": "TNA SP 35/30/31, ff. 78-81, not digitised (Discovery API C17209745 read 16 Nov 2026).",
 "vetting": {"seen": {"kind": "not online", "where": "TNA Discovery API record C17209745 (SP 35/30/31, ff. 78-81, 12 Feb 1722, digitised false), read 16 Nov 2026. The leaves were not seen.",
  "extent": "Four folios; whether the original cipher letter is among them besides the translation is not stated.",
  "cipher": "Catalogue: 'Letter from R W to [Monsieur], intercepted and translated. All the names are still in cypher.' The content (Whigs, Tories, the Regent, Dubois, the Czar) is summarised from the translation."},
  "prior_art": {"decode": "known.py on 'SP 35/30', 'R W' and 'Atterbury': no record of this item; Atterbury-era hits are other catalogue entries (e.g. 860, SP 35/46).",
   "tomokiyo": t, "lasry": l,
   "edition": "The filed translation is the contemporary reading; no printed edition was looked for beyond that.",
   "literature": "Not searched further: the translation on file decides the verdict."},
  "key_check": "Only the name code remains; Atterbury-plot name keys (Willes's decipherments) would be the place to look, not tested.",
  "duplicates": "known.py on the shelfmark: only this lead.",
  "verdict": "partly_read", "closed": "Closed as partly read: the letter was translated at interception and only the coded names remain unresolved."}})

t, l = tl("Pointis, Londonderry, SP 63/352 and 32499")
P.append({"id": 2927, "verdict": "partly_read", "confidence": "high",
 "note": "The calendar's own preface says the three Pointis letters in the 1689 Irish bundle 'have been deciphered by Dr. John Wallis of Oxford'; the 17 June letter is calendared from that decipherment with 'Part of the letter is undeciphered.' It is a deciphered letter with a gap, not an unread one; Wallis's copy (BL Add MS 32499, PRONI T582/2) may fill the gap.",
 "access": "archive", "access_note": "TNA SP 63/352 no. 5, not online; calendar on archive.org (calendarofstatep01grea_2).",
 "vetting": {"seen": {"kind": "transcription", "where": "CSP Domestic William and Mary 1689-90 (1895), archive.org calendarofstatep01grea_2 djvu.txt, read 16 Nov 2026: preface pp. ix-xii and the entries at pp. 147 (13 June), 154 (17 June) and 161 (22 June).",
  "extent": "One long letter; the calendar gives a detailed summary and notes an undeciphered portion of unstated length.",
  "cipher": "Preface: 'three very curious letters from Mons. Pointis ... which have been deciphered by Dr. John Wallis of Oxford.' Entry p. 154: 'The making of a second stockade is in hand. Part of the letter is undeciphered. [S.P. Dom., Ireland 352, No. 5.]'"},
  "prior_art": {"decode": "known.py on Pointis, Londonderry, SP 63/352 and 32499: the wave-18 sweep README and the 11 Nov US/UK leftovers README (PRONI T582/2, Pointis 1689 deciphered from BL Add MS 32499); no DECODE record.",
   "tomokiyo": t, "lasry": l,
   "edition": "Calendared in CSP Dom. W&M 1689-90 from Wallis's decipherment, with a passage noted as undeciphered.",
   "literature": "Wallis's decipherments of the Pointis letters are in BL Add MS 32499 and copied in PRONI T582/2 (recorded in research/sweep_2026-11-11_us_uk_leftovers); not opened."},
  "key_check": "Wallis recovered the key in 1689; his letter-book Add MS 32499 is the place for it, not opened.",
  "duplicates": "known.py: only this lead and the sweep notes; no catalogue entry for the Pointis letters.",
  "verdict": "partly_read", "closed": "Closed as partly read: deciphered by Wallis in 1689, with a passage noted as undeciphered in the calendar."}})

t, l = tl("Danett, SP 83/16 and Salcedo")
P.append({"id": 2921, "verdict": "partly_read", "confidence": "high",
 "note": "The letter is in plain English (calendared in full on BHO); only a handful of name numbers are coded and the editor notes there is no key. A clear letter with a few coded names, not a cipher text.",
 "access": "online", "access_note": "Calendar text on British History Online (CSP Foreign vol. 16, pp. 188-207, no. 189); original TNA SP 83/16 no. 79 not digitised.",
 "vetting": {"seen": {"kind": "transcription", "where": "CSP Foreign Elizabeth vol. 16 (1581-82), no. 189, on British History Online https://www.british-history.ac.uk/cal-state-papers/foreign/vol16/pp188-207, read 16 Nov 2026.",
  "extent": "One page; six number groups in an otherwise plain letter.",
  "cipher": "Money 'furnished by 10 out of 27, and by 81 out of 25'; 'the process and depositions are sent to 12, and 30 vehemently suspected of the practice'. The rest of the letter is plain English."},
  "prior_art": {"decode": "known.py on Danett, SP 83/16 and Salcedo: only the wave-16 sweep README; no DECODE record.",
   "tomokiyo": t, "lasry": l,
   "edition": "Printed in CSP Foreign 1581-82 no. 189; the editor's preface (p. xiii) says there is no key to Danett's numbers and offers guesses (12 = the French king, 30 = Guise?).",
   "literature": "Not searched further: six name numbers with editorial guesses."},
  "key_check": "No key known (editor's preface); other Danett letters in SP 83/16-17 might use the same numbers, not checked.",
  "duplicates": "known.py: no other row for Danett.",
  "verdict": "partly_read", "closed": "Closed as partly read: a plain letter printed in the calendar, with only six coded name numbers left unexplained."}})

t, l = tl("WO 1/923, WO 1/924, Bouillon (only unrelated 16th- and 17th-century hits) and Roznel")
P.append({"id": 1158, "verdict": "not_cipher", "confidence": "medium",
 "note": "Neither item is a cipher text: WO 1/923/115 is a plain report from Paris whose content TNA summarises in detail, only the signature being in cipher; WO 1/924/499 is Bouillon's plain letter to Cooke about an error in reading a cipher (troop figures at Brest reported at f. 495), i.e. a correction to a decipherment already made.",
 "access": "archive", "access_note": "TNA WO 1/923 ff. 115-118 and WO 1/924 ff. 499-502, not digitised (Discovery API C6240940 and C6241156 read 16 Nov 2026).",
 "vetting": {"seen": {"kind": "not online", "where": "TNA Discovery API records C6240940 (WO 1/923/115, 16 Jan 1800, Paris) and C6241156 (WO 1/924/499, 29 Nov 1804, Jersey), read 16 Nov 2026; a Discovery search of WO 1 for Bouillon with cipher/cypher returns only these two. The leaves were not seen.",
  "extent": "Four folios each; no ciphertext described beyond a signature.",
  "cipher": "WO 1/923/115: '[?Roznel] (signed in cipher) to Bouillon. Political events and expectations in Paris; Bonaparte's position...' (enclosed in ff. 111-114, French). WO 1/924/499: 'Bouillon to Cooke. An error in reading the cipher concerning previously reported numbers of troops embarked at Brest (See f.495).'"},
  "prior_art": {"decode": "known.py on WO 1/923, WO 1/924, Bouillon and Roznel: only the access_uncertain list and unrelated La Fin/Bouillon 1593 entries; no DECODE record.",
   "tomokiyo": t, "lasry": l,
   "edition": "No edition looked for: the content of both letters is given by the TNA description in plain terms.",
   "literature": "Not searched further: the descriptions show the texts are plain."},
  "key_check": "No key needed; Bouillon's correspondence ciphers elsewhere in WO 1/921-924 were not searched for this lead.",
  "duplicates": "known.py: no other row for these shelfmarks.",
  "verdict": "not_cipher", "closed": "Closed as not a cipher text: a plain report signed with a cipher name, and a plain letter correcting a decipherment."}})

t, l = tl("Padentiana, Harlingen and 273-03")
P.append({"id": 2551, "verdict": "read", "confidence": "medium",
 "note": "The Tresoar inventory gives the letter's content (an invitation from Sister Padentiana to the pastor to take tea with the mother superior in honour of St Clare), with the note 'De brief is gesteld in geheimschrift': the archivist read it. A trivial 19th-century convent piece filed under pastor J.J. Sletering (1872-1914).",
 "access": "archive", "access_note": "Tresoar 273-03 inv. 311, 1 piece, no scans (archieven.nl inventory text as harvested 11 Nov 2026 in research/sweep_2026-11-11_dutch_2/anl_det.jsonl).",
 "vetting": {"seen": {"kind": "not online", "where": "archieven.nl inventory of Tresoar 273-03 Rooms-Katholieke parochie Harlingen, section 09.2 (J.J. Sletering, pastoor 1872-1914), inv. 311, text as harvested 11 Nov 2026 (research/sweep_2026-11-11_dutch_2/anl_det.jsonl), re-read 16 Nov 2026. No scan.",
  "extent": "One piece, undated (19th century).",
  "cipher": "'Brief van zuster Padentiana, gericht aan de pastoor, met een uitnodiging om thee te komen drinken bij moeder (overste?), ter ere van St. Clara' with 'NB: De brief is gesteld in geheimschrift'."},
  "prior_art": {"decode": "known.py on Padentiana, Harlingen and 273-03: only the sweep READMEs; DECODE search 'Harlingen' gave 0 on 11 Nov.",
   "tomokiyo": t, "lasry": l,
   "edition": "No edition; the inventory summary is itself a reading of the letter.",
   "literature": "Not searched: a private convent note whose content the archivist has stated."},
  "key_check": "No key needed; presumably a simple substitution read by the inventory maker.",
  "duplicates": "known.py: only this lead.",
  "verdict": "read", "closed": "Closed as read: the archive's inventory gives the gist of the secret-script letter."}})

t, l = tl("Rebbe, Peter Gail, Trumbull and Downshire")
P.append({"id": 2918, "verdict": "partly_read", "confidence": "medium",
 "note": "HMC Downshire IV calendars the Rebbe and Gail letters at length in English (e.g. Gail 2 Nov 1613, Rebbe 1 Feb 1614 from Breda, Gail 28 Feb 1614), so the letters are read; the 'cipher symbols and allusions' the editor could not interpret are cover names and a few name signs (Alexander, the compere, the Alastores, Woletius/Velletius, a number '485'), not enciphered passages.",
 "access": "archive", "access_note": "Trumbull papers (BL Add MS 72242-72620, volume not identified; HMC refs Misc. v, 146; Misc. vi, 16 and 20; xxxii, 39); HMC Downshire IV on archive.org.",
 "vetting": {"seen": {"kind": "transcription", "where": "HMC Report on the Manuscripts of the Marquess of Downshire IV (1940), archive.org ReportOnTheManuscriptsOfTheMarquessOfDownshireV4, djvu.txt read 16 Nov 2026: introduction and the Rebbe/Gail entries at pp. 234-235, 288-290, 296-297 and about p. 303.",
  "extent": "Several letters of 1613-1614, each calendared in a paragraph or more.",
  "cipher": "Introduction: 'These are filled with cipher symbols and allusions to which there is no key. Their precise meaning is therefore obscure.' The calendared texts read as plain French letters (translated) using cover names; no undeciphered passage is marked in the entries read."},
  "prior_art": {"decode": "known.py on Rebbe, Peter Gail, Trumbull and Downshire: only the wave-16 sweep README and unrelated Trumbull entries; no DECODE record.",
   "tomokiyo": t, "lasry": l,
   "edition": "Calendared in HMC Downshire IV (1940) in English summary; the editor gives the sense of the letters but cannot interpret the cover names.",
   "literature": "Not searched further: the calendar shows the letters were read."},
  "key_check": "No key for the cover names exists per the editor; not a cipher key question.",
  "duplicates": "known.py: no other row for Rebbe or Gail.",
  "verdict": "partly_read", "closed": "Closed as partly read: the letters are calendared in full sense; only cover names and name signs remain uninterpreted."}})

for p in P:
    json.dump(p, open(f"p/{p['id']}.json", 'w', encoding='utf8'), ensure_ascii=False, indent=1)
print(len(P))
