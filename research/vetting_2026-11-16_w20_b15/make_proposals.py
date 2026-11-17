"""Write this batch's proposals.json (wave 20, batch 15, 16 Nov 2026). Run: python -I -X utf8 make_proposals.py"""
import json, pathlib

BY = "claude session 16 Nov 2026 (Claude Opus 5.5), wave 20 vetting"
TL = ("Tomokiyo's unsolved list (cryptiana unsolved.htm, fetched 15 Nov 2026) searched for {t}: no entry.")
GL = ("Lasry's list (cryptiana GL.htm, fetched 15 Nov 2026) searched for {t}: no entry.")
AP403 = ("Abhilekh Patal answered HTTP 403 'Request blocked' (CloudFront) to curl on 16 Nov 2026 at the first request; "
         "not retried around it. Metadata taken from the October harvest (research/asia_india/details.jsonl).")
P = {}


def held(i, title, ident, kw, held_says, extra=""):
    """A lead whose leaf was read on 11 Nov through the withdrawn viewer route: no verdict from this batch."""
    P[i] = {
        "verdict": None, "confidence": "low",
        "note": (f"Not assessed: {title} ({ident}); the portal record gives only a title and OCR keywords ({kw}), which "
                 f"do not show ciphertext. The 11 Nov 2026 cloud pass read the file through the Abhilekh viewer and "
                 f"held '{held_says}' (vetting_held), but that route went round the WAF CAPTCHA and was withdrawn; "
                 f"nothing found today changes that block. {extra}").strip(),
        "access": "online",
        "access_note": AP403 + " The vetting_held block in leads.json stands pending Daniel's decision or a look "
                       "from his own logged-in Chrome session.",
    }


def unseen(i, title, ident, kw, why, extra=""):
    P[i] = {
        "verdict": None, "confidence": "low",
        "note": (f"Not assessed: {title} ({ident}); {why} No leaf seen and none was seen in earlier passes. {extra}").strip(),
        "access": "online",
        "access_note": AP403 + " Needs the pages opened from a logged-in Abhilekh Patal session (Daniel's Chrome).",
    }


held("1364", "Foreign Secret Cons. 1 Aug 1796 No. 5, 'Letter to Admiral G. K. Elphinstone ... dated 24 May recd 1 August', 5 pp.",
     "NAIDLF00945474", "Madras, Monarch, Forces, Cypher, Admiral", "not_cipher: plain covering letter naming two cipher enclosures not in the file")
held("1360", "Foreign Secret Cons. 8 Apr 1799 No. 29, 'Enclosed in a letter from Persian translator dated 21 march', 5 pp.",
     "NAIDLF00947849", "Little, Colonel, Cypher, Vieux", "not_cipher: plain copy of Mornington to Palmer, 19 Mar 1799",
     "Martin's Wellesley Despatches vol. I (archive.org india.history.resource.35304) was grepped: its list of letters to "
     "Palmer has 3 Mar, 3 Apr, 7 Apr and 2 May 1799, not 19 March, so the letter is not printed there; vol. I does print "
     "the Company's 'cypher, No. 11' being issued to the Mysore commissioners (Mornington to Harris, 1799), which fits the "
     "keywords but does not show what is on the leaf.")
P["1355"] = {
    "verdict": None, "confidence": "low",
    "note": ("Not assessed by sight: Foreign Secret Cons. 23 Jun 1802 Nos. 90-91 (NAIDLF01002013 and No. 91), the "
             "catalogue's own title says 'partly in cypher code'. The 11 Nov held block (withdrawn route) says every cipher "
             "run carries an interlined decipherment, which would make it 'read'; this batch could not re-see the leaf. "
             "Printed check: Poona Residency Correspondence vol. 7 (Close's Embassy, 1940) jumps from 7 Mar to 3 Sep 1802 "
             "and does not print these letters; Martin's Wellesley Despatches vol. III does not either."),
    "access": "online",
    "access_note": AP403 + " The catalogue title alone shows cipher but not whether the decipher is interlined, so "
                   "it cannot go in as 'open' on description; Daniel's look (or acceptance of the 11 Nov block) decides it.",
}
unseen("1365", "Foreign Secret Cons. 5 Oct 1807 No. 5, 'Letter to the Govt. of Bombay dated 5 October', 12 pp.",
       "NAIDLF00826189", "", "the record has only OCR keywords (Cypher, Naval, State, Expediency, Instructions, Resident), "
       "which show the word, not ciphertext; a Calcutta out-letter to Bombay is as likely to mention a cypher as to use one.")
unseen("1366", "Foreign Secret Cons. 1 Feb 1808 No. 2, 'Letter to the Secy. Prince of Wales Island dated 13 December', 4 pp.",
       "NAIDLF00829027", "", "the record has only OCR keywords (Secret, Original, Previous, Cypher, Supreme, Wishes); "
       "the 1813 Penang file (lead 1367) shows the same keyword pattern on a clear covering letter.")
unseen("1370", "Foreign, Persian Letters Received No. 327, issued 22 Feb 1808, 2 pp.",
       "NAIDLF02179604", "", "the portal 'title' is machine-translation noise ('The circle of the car s hand is "
       "overwhelmed ...') and 'Deciphe', 'Caccent', 'Broken' are OCR keywords from the same noisy pass; nothing says "
       "the letter is enciphered. The Calendar of Persian Correspondence stops at 1795, so there is no printed calendar "
       "for 1808.", "Likely not_cipher (same pattern as lead 1371), but unproven.")
held("1368", "Foreign Political Cons. 29 Jul 1809 No. 22, 4 pp.", "NAIDLF01546081", "Khan, Fermi, Resident, Seat, Cypher",
     "not_cipher: Edmonstone's plain note on a sealed letter that had names in cipher; that letter not in the file")
held("1367", "Foreign Secret Cons. 30 Apr 1813 No. 1, 'Letter to the Chief Secy. Prince of Wales Island ... dated 30 March', 4 pp.",
     "NAIDLF00824821", "April, Cypher, Letters, Understood, Requests",
     "not_cipher: clear covering letter forwarding two cipher letters from England that are not in the file")
held("1371", "Foreign, Persian Copies of Letters Received No. 26, issued 7 Jan 1828, 3 pp.", "NAIDLF02289159",
     "Point, Photographer, Lucian, Focal, Coherent, Cipher, Board",
     "not_cipher: an ordinary Persian letter; 'Cipher' is machine noise in the keyword list",
     "The record text itself supports that reading: the 'title' ('Ann CornIs my coherentTech ...') and keywords are "
     "machine output, not a description.")
unseen("1369", "Foreign Political Cons. 14 Oct 1853 No. 111, 'Letter to the Chief Secretary Bombay dated 19 Sept and Rec 1 Oct', 6 pp.",
       "NAIDLF01946321", "", "the record has only OCR keywords (Letters, Russian, Cypher, Bombay, Office, Secret, "
       "Commissioner); nothing says a passage is in cipher.")
unseen("1354", "Foreign Secret Progs. Nov 1879 Nos. 233-34 and 276-78 and Notes C-983",
       "NAIDLF02188873, NAIDLF02188881, NAIDLF03366898", "", "the titles show the Government of India watching and trying "
       "to decipher Mandalay-Italy telegrams ('Steps taken to decipher certain telegrams ...'; 'Exchange of Cipher "
       "Telegrams between Italy and Mandalay'; Viceroy's note naming the Genoa correspondent Durazzo Adorno), but the "
       "files are 2-3 pages each and whether any telegram text is copied in, or whether the attempt succeeded, is not "
       "stated. A web search (16 Nov 2026) on the Mandalay-Italy cipher telegrams of 1879 found nothing printed.",
       "Tomokiyo and Lasry lists: no Burma/Mandalay entry. If the pages show groups with no result, this becomes a real "
       "open candidate; the London side is IOR/L/PS (not checked).")
P["1354"]["access_note"] += " The London copies (IOR/L/PS/7 secret letters from India, 1879) are a second route, not tried."
unseen("1358", "Home Public Cons. 3 Jan 1812 No. 86, 'Undeciphered documents from early 19th century consultations', 3 pp.",
       "NAIDLF00330538", "", "the title is a cataloguer's label and is the only one of its kind in the 2026 harvest "
       "(details.jsonl has one 'Undeciphered' title); its OCR keywords are an archive stamp and names ('ES OF INDIA', "
       "'Suretary', 'William Pollency', 'Fullon'), which points to legible English papers the cataloguer could not "
       "identify rather than to cipher.", "Likely not_cipher, unproven.")

P["1916"] = {
    "verdict": "read", "confidence": "medium",
    "note": ("CADN 166PO/A-208 is Choiseul's correspondence with Tott for the Crimean mission (Aug 1767 - Apr 1769, "
             "'double', copies and ciphered originals) with Tott's drafts that the MNL abstract says match CP Turquie "
             "Suppl. 17/17bis and the Versailles copies; Tóth 2014 prints that correspondence (114 documents) from the "
             "Versailles volumes. The record's 'Vergennes-Fornetti' title is wrong: Fornetti is not in the contents."),
    "access": "archive",
    "access_note": "CADN Nantes volume not online; MNL OL holds an abstract only (read in Chrome in an earlier pass).",
    "correct_title": "Choiseul and the baron de Tott, Crimean mission correspondence (double), Aug 1767 - Apr 1769, CADN 166PO/A-208",
    "vetting": {
        "date": "2026-11-16", "by": BY,
        "seen": {
            "kind": "not online",
            "where": ("MNL OL abstract HK-CADN-166PO/A-208 (Archives Portal Europe, read in Chrome in an earlier pass and "
                      "quoted in the lead's vetting_note): 'Correspondance de Choiseul avec le baron de Tott - Crimée "
                      "(double) août 1767 - avril 1769 (másolatok és eredeti rejtjelezett levelek)'; fol. 185-412 drafts "
                      "of Tott-Choiseul letters, matching La Courneuve CP Turquie Suppl. 17 and 17bis and the Bibliothèque "
                      "de Versailles; fol. 413-428 Tott-Géraud (Warsaw). The CADN volume itself was not seen."),
            "extent": "One volume, at least 428 folios; how many pieces are ciphered is not stated in the abstract.",
            "cipher": ("The archive's abstract says the volume holds copies and original ciphered letters ('eredeti "
                       "rejtjelezett levelek'), alongside clear drafts of the same correspondence (fol. 185-412)."),
        },
        "prior_art": {
            "decode": "known.py on 'Fornetti', '166PO/A-208' and 'Tott': only this lead and the sibling Saint-Priest/Tott lead (vols. 151/153); no DECODE record of this volume or of Tott's Crimean letters.",
            "tomokiyo": TL.format(t="Tott, Crimée/Crimea, Choiseul"),
            "lasry": GL.format(t="Tott, Crimée/Crimea"),
            "edition": ("Ferenc Tóth (ed.), La correspondance consulaire de Crimée du baron de Tott (1767-1770), Istanbul, "
                        "Isis, 2014: per Kincses's review (Dix-huitième siècle 47, 2015, pp. 649-651, real.mtak.hu/124019, "
                        "read 16 Nov 2026) it prints 114 documents of the Crimean mission, with letters to and from "
                        "Choiseul and Vergennes, from Versailles BM Lebaudy Mss 4° 117-119, the copies the MNL abstract "
                        "says this volume matches. The book itself was not opened (REAL copy restricted)."),
            "literature": ("Tóth, 'Modernisation et tradition dans l'armée ottomane ... le cas du baron de Tott' (EPA "
                           "Toth_Ferenc.pdf) and Tóth's Hungarian survey of French archives (Mediterrán Tanulmányok) "
                           "grepped for chiffre/rejtjel/166PO: CADN Saint-Priest series cited, no cipher discussion."),
        },
        "key_check": "No key looked for: the clear drafts in the same volume and the printed Versailles copies give the text, so no key is needed to read the correspondence.",
        "duplicates": ("known.py on the shelfmark, Fornetti and Tott: the only related row is the Saint-Priest/Tott lead on "
                       "CADN vols. 151/153 (different volumes, 1769-70 despatches); no catalogue entry for this volume."),
        "verdict": "read",
        "closed": ("The volume pairs Tott's ciphered originals with clear drafts of the same Choiseul-Tott correspondence "
                   "(fol. 185-412, matching CP Turquie Suppl. 17/17bis and Versailles), and Tóth 2014 prints the "
                   "Versailles copies of that correspondence; the ciphered letters are read in clear in the archive and "
                   "in print. Medium confidence: no piece-by-piece check that every ciphered letter is among the 114 "
                   "printed documents."),
    },
}

KEYS = {
    "2719": ("NA 1.10.110 inv. 2 sect. 2.11 no. 186 'Battier, Spanje. Codeboeken' (API, PHYSICAL; nos. 184-185 answer 404 "
             "at the same API path)", "Battier's Madrid key is already held for targets/battier1686 (NA 1.10.29 Fagel "
             "inv. 1209) and on DECODE as R2794; these books are probably further copies."),
    "2720": ("NA 1.10.110 no. 187 'Van Rechteren, Denemarken, codeboek' (API, PHYSICAL)",
             "No DECODE or repo key for a Rechteren Copenhagen cipher (catalogue 232 is Rechteren at St Petersburg 1785, read)."),
    "2721": ("NA 1.10.110 no. 183 '(Cijffer voor de heer Buijs, extraordinaris Envoijé en Plenipotentiaris in "
             "Denenmarken) Codeboek' (API, PHYSICAL)", "No DECODE or repo key or letter for Buijs at Copenhagen."),
    "2722": ("NA 1.10.110 no. 179 'Van Burmania, Wenen: cijffer met de ministers te Stokholm, Weenen en Petersburg' "
             "(API, PHYSICAL)", "No DECODE or repo key; Burmania appears only among sibling letters without a cipher flag (siblings_nov9)."),
    "2723": ("NA 2.21.227 no. 336 'Sleutels voor geheimschriften, gedeeltelijk in het handschrift van Lodewijk van "
             "Toulon. Ongedateerd, ontwerpen (?)' (API, PHYSICAL)", "Next to no. 335, the Correspondentiecijffer that "
             "would read catalogue 230 (toulon1803, DECODE R2034); worth ordering with it."),
}
for i, (rec, ctx) in KEYS.items():
    P[i] = {
        "verdict": None, "confidence": "high",
        "note": (f"Key only, no ciphertext: {rec}, re-read from the NA clevel API 16 Nov 2026. {ctx} A key book has "
                 "no text to vet as open or closed; recommend moving it to the key leads (and a DECODE key-record queue "
                 "entry once scanned) rather than vetting it as a ciphertext lead. Not a BnF/Omont lead: the brief's "
                 "label for 2719-2723 does not fit these records."),
        "access": "archive",
        "access_note": "Nationaal Archief, physical only, scan on demand; known.py on the envoy names and the inventory number found only the sweep rows.",
    }

order = "1364 1360 1355 1365 1366 1370 1368 1367 1371 1369 1354 1358 1916 2719 2720 2721 2722 2723".split()
out = {i: P[i] for i in order}
pathlib.Path(__file__).with_name("proposals.json").write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(len(out), "proposals")
