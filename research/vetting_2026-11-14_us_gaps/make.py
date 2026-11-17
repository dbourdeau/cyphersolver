import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
BY = "claude session 14 Nov 2026 (Claude Sonnet 5.5), US gaps sweep vetting"
D = "2026-11-14"
out = {}

out["2670"] = {
    "date": D, "by": BY,
    "seen": {
        "kind": "not online",
        "where": "Penn finding aid, Henry Dundas papers, Ms. Coll. 888, Series I, Box 11 Folder 26 (findingaids.library.upenn.edu/records/UPENN_RBML_PUSP.MS.COLL.888, inventory text read 14 Nov 2026); the record has no digital object and Kislak holds the folder in the reading room only.",
        "extent": "One folder: Malcolm's memorandum of 2 Dec 1798 (clear) and 'a second copy of the same in cypher' with Dundas's enclosing letter of 19 Aug 1800; no leaf count is given.",
        "cipher": "Archive text, verbatim: 'Memorandum relative to the late French Corps in the Deccan, from Captain Malcolm, 2 December 1798; also a second copy of the same in cypher with an enclosing letter by Henry Dundas, dated 19 August 1800'. Leaf not seen: the cipher system (numerical or nomenclator) is not stated; the clear copy of the same text is in the same folder, which is a crib.",
    },
    "prior_art": {
        "decode": "known.py 'Dundas', 'Malcolm' (14 Nov 2026): no DECODE record; the only Dundas cipher entries are catalogue 1921 (Dundas of Dundas accounts, 1688) and the Harford Jones to Dundas code of 1798 (catalogue), both different items.",
        "tomokiyo": "Web search naming Tomokiyo, Cryptiana, Dundas, Board of Control and Wellesley cyphers (14 Nov 2026): no Cryptiana page for this folder or for a Malcolm cypher of 1798-1800.",
        "lasry": "Same search for Lasry and DECODE: nothing on Dundas/Malcolm cyphers; the hits are BL Wellesley despatches 'some in cipher' and Qatar Digital Library enclosures of 1808, none a decipherment.",
        "edition": "Web search for the memorandum's title (14 Nov 2026) found no printed edition; Wellesley Despatches (Martin) and Kaye's Life of Malcolm were not searched in full text, so a print of the clear text is not excluded (it would give the plaintext, not the key).",
        "literature": "Web searches (14 Nov 2026) returned DNB and history-of-India material on the disbandment of the French corps and no study of a Malcolm-Dundas cypher.",
    },
    "key_check": "No key is held here. The cypher copy is a copy of the clear memorandum in the same folder, so the folder itself carries the crib; whether the code is the Board of Control's of 1800 (compare the Harford Jones code of 1798 in the catalogue) is unknown.",
    "duplicates": "known.py 'Dundas', 'Malcolm', 'Deccan', shelfmark 'Ms. Coll. 888' (14 Nov 2026): no entry or lead holds Penn Ms. Coll. 888; the Harford Jones to Dundas code (catalogue) is a different writer, place and year.",
    "searches": [
        {"query": "Malcolm memorandum French corps Deccan 1798 cypher Dundas papers Penn Ms. Coll. 888 (web search)",
         "result": "Penn finding aid of the collection (no item level in the summary); DNB on Malcolm and the disbandment of the French corps; Huntington Dundas records of other collections; nothing on a cypher copy."},
        {"query": "Tomokiyo cryptiana OR DECODE OR Lasry Henry Dundas Board of Control cypher 1800 Wellesley Malcolm cipher letter India (web search)",
         "result": "BL Wellesley to Dundas despatches 'some in cipher', Qatar Digital Library Malcolm Persia enclosures of 1808; no Tomokiyo, DECODE or Lasry hit."},
        {"query": "\"Memorandum relative to the late French Corps in the Deccan\" Malcolm 1798 printed (web search)",
         "result": "No catalogue record or print of the memorandum; background on the disbandment (DNB) and Bengal Secret Letter enclosures at TNA."},
        {"query": "known.py 'Dundas' 'Malcolm' 'Deccan' against catalogue, leads, DECODE dumps (local)",
         "result": "Only the sweep row, catalogue 1921 and the Harford Jones code; no overlap."},
    ],
    "verdict": "open",
    "lead_updates": {
        "status": "Finding aid (Penn, read 14 Nov 2026): a clear copy and a cypher copy of one memorandum in Box 11 Folder 26, with Dundas's enclosing letter of 19 Aug 1800. Not online; no edition or decipherment found; scan request to Kislak (rbml@pobox.upenn.edu) is the next step.",
    },
}

out["2669"] = {
    "date": D, "by": BY, "verdict": "read",
    "seen": {
        "kind": "transcription",
        "where": "Penn PACSCL finding aid of the Free Library of Philadelphia Historical manuscripts collection (findingaids.library.upenn.edu/records/FLP_FLP.RBD.HISTMSS, inventory text read 14 Nov 2026): items 'Deane, Silas. Autograph letter to James Wilson. Paris, 1780 October 9' and 'Paris, 1780 December 1'.",
    },
    "closed": "The finding aid describes both items as deciphered letters, one on the recto and one on the verso of one sheet, 'said to be in James Wilson's hand' (Julian P. Boyd, March 1937), with a modern transcription laid in; one carries Wilson's note about Deane's letters being shown to the minister of France. The decipherment is on the sheet, so the item is a decipherment, not an open ciphertext; the finding aid does not say the cipher sheets survive. No image online.",
}

out["2671"] = {
    "date": D, "by": BY, "verdict": "not_cipher",
    "seen": {
        "kind": "transcription",
        "where": "Columbia finding aid for Imre Forbath Diaries and Photographs, Journal 8 (record text quoted in lead 2671, 14 Nov 2026); no image.",
    },
    "closed": "The finding aid's own words: 'written in German stenography and is not deciphered'. German stenography (Gabelsberger or Stolze-Schrey) is a published shorthand system read by any stenographer, not a cipher; 'not deciphered' means the library has not had it transcribed. Out of scope for a cipher catalogue.",
}

out["2673"] = {
    "date": D, "by": BY, "verdict": "not_cipher",
    "seen": {
        "kind": "transcription",
        "where": "Morgan CORSAIR record 190797 (read in a Chrome tab, 14 Nov 2026): MA 3990, Misc English (Strickland), Macdonald's autograph letter to Agnes Strickland, 3 p., dated 1 Mar 1850 (the record's '1950' is a typo).",
    },
    "closed": "The item held is Macdonald's covering letter, not a ciphertext. Its summary says it acknowledges receipt of four original Mary Queen of Scots letters, 'one in code, of which he sends transcriptions': the decipherment went to Strickland in 1850. No ciphertext is in the Morgan record; the code letter itself belongs to the Register House (now National Records of Scotland), and Mary Stuart's cipher letters are among the most worked ciphers (Lasry et al. 2023).",
}

UNV = {
    "2672": "Bryn Mawr BMC-M25 Box 13 Object Diaries 9-13 (TriCollege ArchivesSpace read in a Chrome tab, 14 Nov 2026; the Cloudflare check passed by itself, nothing clicked): Diary 9 (22 May-27 Jul 1918) 'Primarily in Greek. I resolve to keep my diary in cipher again'; later diaries to June 1919 'Primarily in Greek'. The record says most materials are not digitized. It is not stated whether the Greek is Greek words or English in Greek letters, so whether it is a cipher at all is open; no leaf seen and one web search (no hit). Needs a scan from Bryn Mawr Special Collections.",
    "2674": "Columbia Devoiants Papers (finding aid cul-4077451, blocked to WebFetch; abstract known from search): 15 items, 'texts of telegrams (1919-20) ... deciphered by Armenian military intelligence', on-site only; whether any ciphertext is kept beside the decipherments is not stated; no image; Hovannisian not checked. Needs a Columbia RBML reply.",
}
for k, v in UNV.items():
    out[k] = {"unvetted": v}

with open(os.path.join(HERE, "vetting.json"), "w", encoding="utf-8") as fh:
    json.dump(out, fh, ensure_ascii=False, indent=1)
    fh.write("\n")
print(len(out))
