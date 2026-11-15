import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
BY = "claude session 14 Nov 2026 (Claude Sonnet 5.5), German state databases sweep vetting"
D = "2026-11-14"
out = {}

KOB_LINK = "Landesarchiv Thueringen Online-Findbuch (archive-in-thueringen.de), Staatsarchiv Meiningen, Geheimes Archiv Hildburghausen / Akten (4-11-2010): record text read in a Chrome tab on that origin in the 14 Nov 2026 sweep (same-origin fetch of the hit page); no image is attached to the record."
LASRY_GENERIC = "Web search naming Tomokiyo, Lasry, Cryptiana and the Thuringian courts (Hildburghausen, Meiningen, Sachsen-Weimar) (14 Nov 2026): Lasry/Tomokiyo/Biermann's Mary Stuart and 2025 TNA decipherments and a paper on the Saxon (Dresden) court ciphers of Augustus II; nothing on a Thuringian court cipher of any date."


def kob_pa(vol, edition_extra=""):
    return {
        "decode": "known.py (DECODE views dumps, HCPortal index, Cryptoole snapshot) on 'Hildburghausen', 'Kob', 'Seelig', 'Anton Ulrich' (14 Nov 2026): no DECODE record from the Geheimes Archiv Hildburghausen or any Kob correspondence (checked for " + vol + ").",
        "tomokiyo": "No Cryptiana page found for Hildburghausen, Meiningen or Kob in the web searches of 14 Nov 2026 (see searches); nothing that names " + vol + ".",
        "lasry": "No Lasry or HistoCrypt paper on a Hildburghausen or Meiningen cipher found (14 Nov 2026 web search); his Saxon-court work (Dresden, Augustus II) is a different court and period; nothing names " + vol + ".",
        "edition": "No edition of Kob's secret chancery found in the searches of 14 Nov 2026. " + edition_extra,
        "literature": "Web searches on Kob and on the Hildburghausen court of Ernst Friedrich III Carl (14 Nov 2026) returned local-history, Duke Friedrich and debt-commission material (the 1769 Kaiserliche Debitkommission) and no study of the cipher correspondence in " + vol + ".",
    }


# ---------------------------------------------------------------- 2652 Degenfeld
out["2652"] = {
    "date": D, "by": BY,
    "seen": {
        "kind": "not online",
        "where": "Archivportal-D / DDB Solr records of the Landesarchiv Baden-Wuerttemberg, Hauptstaatsarchiv Stuttgart (items DRBLDG3Q... for Bue 124 and DOIB6MTZ... for Bue 129), read in the 14 Nov 2026 sweep; no image or digital copy is attached to either record and the archive's own site was not checked for scans.",
        "extent": "Two volumes of one correspondence: Bue 124 (3 Jan - 22 Nov 1845) and Bue 129 (10 Jan - 19 Nov 1846); the records give no leaf counts.",
        "cipher": "Archive titles, verbatim: Bue 124 '(z. T. chiffriert, mit Aufl.)' and Bue 129 '(teilweise chiffriert, mit Dechiffrierung)'. Reports of the Wuerttemberg envoy Degenfeld-Schomburg at Munich; the legation's deciphering is filed in the same volumes. Leaf not seen: not digitised.",
    },
    "prior_art": {
        "decode": "known.py 'Degenfeld' and 'E 50/05' (14 Nov 2026): no DECODE record; the only earlier mention in the repo is a one-line note in research/archivportal_d/README.md and research/central_archives/README.md (no entry, no reading).",
        "tomokiyo": "Web search naming Tomokiyo, Cryptiana and Wuerttemberg legation ciphers of the 1840s (14 Nov 2026): no Cryptiana page on 19th-century Wuerttemberg diplomatic ciphers.",
        "lasry": "Same search for Lasry/HistoCrypt: nothing on Wuerttemberg legation ciphers of 1845-46; his German diplomatic work is 1900-15 (Kaiserreich), a different state and period.",
        "edition": "No edition of the Munich reports of 1845-46 found; Degenfeld's posting 1844-68 is in the Bavarian envoy database (gesandtendatenbank.bavarikon.de), which lists sources and no printed reports.",
        "literature": "Web search 'Degenfeld-Schomburg Gesandter Muenchen 1845 1846 Berichte chiffriert' (14 Nov 2026): Stuttgart E 50/05 finding-aid records for other years (Relationen 1855 Bue 173, Reskripte to Wintzingerode Bue 20) and no study of the cipher.",
    },
    "key_check": "No key is held here. The deciphering is filed in each volume (the key_in_volume). The Wuerttemberg legation cipher books of 1847 to about 1870 are in HStAS E 59 Bd. 232-242 (research/sweep_2026-11-14_german_state_dbs/key_leads.json), a key family for the following years; none is online and nothing was tried.",
    "key_in_volume": "The legation's contemporary deciphering ('Aufl.' / 'Dechiffrierung') is filed in the same volume per the archive titles; not seen, not tested.",
    "duplicates": "known.py 'Degenfeld', 'E 50/05', 'Dechiffrierung' (14 Nov 2026): no entry or lead other than 2652 holds E 50/05 Bue 124 or 129; E 59 key volumes are only in key_leads.json (not an entry). Both volumes are kept in one entry because the volumes are one correspondence and one legation cipher period (1845-46).",
    "searches": [
        {"query": "Degenfeld-Schomburg wuerttembergischer Gesandter Muenchen 1845 1846 Berichte chiffriert Chiffrierbuch Wuerttemberg Gesandtschaft Chiffre (web search)",
         "result": "Bavarian envoy database (Degenfeld-Schonburg, Muenchen 1844-68); HStAS E 50/05 records for Bue 173 (1855) and Bue 20; nothing on cipher books or on these two volumes."},
        {"query": "known.py 'Degenfeld' 'E 50/05' 'Dechiffrierung' against catalogue, leads, DECODE dumps, queue, READMEs (local)",
         "result": "Only the sweep rows and one-line mentions in archivportal_d and central_archives READMEs; no DECODE id; no catalogue entry."},
        {"query": "Tomokiyo Lasry cipher Wuerttemberg legation Munich 1840s Hauptstaatsarchiv Stuttgart E 50/05 (web search)",
         "result": "No result on 1840s Wuerttemberg ciphers; Lasry/Tomokiyo hits are Mary Stuart and 17th-century letters."},
    ],
    "verdict": "open",
    "lead_updates": {
        "folio_note": "Titles: '(z. T. chiffriert, mit Aufl.)' (Bue 124, 1845) and '(teilweise chiffriert, mit Dechiffrierung)' (Bue 129, 1846). Content note: Staendekammern, Minister Abel, dismissal of foreign minister Gise, church affairs. Other Bue of E 50/05 (other years) were not in the hit list.",
        "status": "Finding aid (14 Nov 2026): some reports ciphered, with the legation's deciphering filed in each volume. Not online; no decipherment or edition found. Key books of the next years are in HStAS E 59.",
        "needs_archive_scan": "yes",
    },
}

# ---------------------------------------------------------------- 2661 Kob-Seelig
out["2661"] = {
    "date": D, "by": BY,
    "seen": {
        "kind": "not online",
        "where": KOB_LINK,
        "extent": "One volume (Nr. 1006), 1750-1753; the record gives no leaf count.",
        "cipher": "Archive description: 'Enthaelt u.a.: Schluessel fuer die verwendeten Chiffres' in the secret correspondence of Hofrat Johann Sebastian Kob with Johann Georg Seelig at Frankfurt about the court of Duke Anton Ulrich of Sachsen-Meiningen; the key is filed with the letters. Leaf not seen: not digitised.",
    },
    "prior_art": kob_pa("Nr. 1006", "The Nr. 1006 volume is not among the printed sources the searches turned up."),
    "key_check": "A key 'fuer die verwendeten Chiffres' is described in the volume itself; not seen, not tested. No other key for Kob and Seelig is known; Kob's other correspondents have their own keys (Nr. 998 with Schneider in lead 2662, Nr. 368 with Fischer in lead 2663).",
    "key_in_volume": "'Schluessel fuer die verwendeten Chiffres' filed in Nr. 1006 per the Online-Findbuch; not seen, not tested.",
    "duplicates": "known.py 'Hildburghausen', 'Seelig', 'Kob' (14 Nov 2026): Nr. 1006 appears only in the sweep rows and lead 2661; no entry for the Geheimes Archiv Hildburghausen. One key per entry: Seelig kept apart from Schneider (2662) and Fischer (2663).",
    "searches": [
        {"query": "Hofrat Kob Hildburghausen Geheime Korrespondenz Chiffre Seelig Schneider Fischer Wien Herzog Ernst Friedrich (web search)",
         "result": "No result names Kob, Seelig or the correspondence; Hildburghausen ducal history, a Duke Johann Friedrich zodiac-sign cipher study and Dresden 'Chiffres' volumes only."},
        {"query": "known.py 'Hildburghausen' 'Seelig' against catalogue, leads, DECODE dumps, queue, READMEs (local)",
         "result": "Only the sweep rows (2661-2664) and unrelated 'Seeliger' (Volkelt, 1876) in the catalogue; no DECODE id."},
        {"query": "Tomokiyo Lasry cipher Hildburghausen Meiningen Sachsen-Weimar archive undeciphered 18th century German court cipher letters (web search)",
         "result": "Mary Stuart and 2025 TNA decipherments; a paper on the Dresden court ciphers of Augustus II; no Hildburghausen or Meiningen item."},
    ],
    "verdict": "open",
    "lead_updates": {
        "status": "Online-Findbuch text (14 Nov 2026): key and secret letters of 1750-53 in one volume. Not online; no decipherment, edition or study found.",
        "needs_archive_scan": "yes",
    },
}

# ---------------------------------------------------------------- 2662 Kob-Schneider
out["2662"] = {
    "date": D, "by": BY,
    "seen": {
        "kind": "not online",
        "where": KOB_LINK,
        "extent": "One volume (Nr. 998), 1753-1755; the record gives no leaf count.",
        "cipher": "Archive description: 'Enthaelt u.a.: Schluessel fuer die verwendeten Chiffres' in the secret correspondence of Hofrat Kob with the secretary Johann Caspar Schneider (Frankfurt and Meiningen; 'Hofrat Schrader?' is queried in the finding aid). Leaf not seen: not digitised.",
    },
    "prior_art": kob_pa("Nr. 998"),
    "key_check": "A key for the ciphers used is described in the volume; not seen, not tested. The Seelig volume (2661, Nr. 1006) is held separately; whether the two keys agree is untested.",
    "key_in_volume": "'Schluessel fuer die verwendeten Chiffres' filed in Nr. 998 per the Online-Findbuch; not seen, not tested.",
    "duplicates": "known.py 'Kob', 'Anton Ulrich' (14 Nov 2026): Nr. 998 appears only in the sweep rows and lead 2662; no entry for the Geheimes Archiv Hildburghausen. Kept apart from 2661 and 2663 under the one-key rule.",
    "searches": [
        {"query": "Johann Caspar Schneider Sekretaer Meiningen Anton Ulrich Frankfurt Hildburghausen Kob Hofrat Briefwechsel 1753 Chiffre Schluessel (web search)",
         "result": "Anton Ulrich died at Frankfurt 27 Jan 1763 (Sachsen-Anhalt file), a guardianship dispute print, a Meiningen cabinet secretary Wagner; nothing on Schneider, Kob or ciphers."},
        {"query": "Johann Sebastian Kob Hofrat Hildburghausen Geheimes Archiv Staatsarchiv Meiningen Geheimschrift Chiffre Korrespondenz 1750 (web search)",
         "result": "Footnote locating the military department of the Geheimes Archiv Hildburghausen at Meiningen; a Dresden 'Verschiedene Chiffres' volume; a Magdeburg 1708 cipher-key file; nothing on Kob."},
        {"query": "known.py 'Kob' 'Anton Ulrich' against catalogue, leads, DECODE dumps, queue, READMEs (local)",
         "result": "Only the sweep rows; catalogue hits for 'Anton Ulrich' are Brunswick's (Anna Ivanovna), unrelated."},
    ],
    "verdict": "open",
    "lead_updates": {
        "status": "Online-Findbuch text (14 Nov 2026): key and secret letters of 1753-55 in one volume. Not online; no decipherment, edition or study found.",
        "needs_archive_scan": "yes",
    },
}

# ---------------------------------------------------------------- 2663 Kob-Fischer
out["2663"] = {
    "date": D, "by": BY,
    "seen": {
        "kind": "not online",
        "where": KOB_LINK,
        "extent": "Nr. 368, 1749-1750, with its key sheet on Bl. 1-5; two or three neighbouring Kob-Fischer volumes (hits 3923377, 3923378, 3923380) were not all read and are not counted.",
        "cipher": "Archive description: 'Enthaelt auch: Schluessel der in der Korrespondenz mit Fischer gebrauchten Kuerzel (Bl. 1-5)'; the neighbouring volumes are titled 'Teilweise verschluesselte Korrespondenzen des Hofrats Kob'. Partly ciphered letters of Kob and the Geheimer Legationsrat von Fischer at Vienna. Leaf not seen: not digitised.",
    },
    "prior_art": kob_pa("Nr. 368"),
    "key_check": "A key to the abbreviations (Kuerzel) used with Fischer is on Bl. 1-5 of the volume, so the system may be a short nomenclator; not seen, not tested.",
    "key_in_volume": "Key of the abbreviations used in the Fischer correspondence on Bl. 1-5 of Nr. 368; not seen, not tested.",
    "duplicates": "known.py 'Sonnefeld', 'Hildburghausen', 'Kob' (14 Nov 2026): Nr. 368 appears only in the sweep rows and lead 2663. The neighbouring Kob-Fischer volumes are not given their own entries until their signatures are read; they belong to the same partner and key.",
    "searches": [
        {"query": "Hofrat Kob Hildburghausen Geheime Korrespondenz Chiffre Seelig Schneider Fischer Wien Herzog Ernst Friedrich (web search)",
         "result": "No result names Kob, Fischer or the Sonnefeld excess-charge matter."},
        {"query": "Johann Sebastian Kob Hofrat Hildburghausen Geheimes Archiv Staatsarchiv Meiningen Geheimschrift Chiffre Korrespondenz 1750 (web search)",
         "result": "A 1749-1750 Thuringian State Archive item with no title in the snippet; no cipher or Kob content confirmed."},
        {"query": "known.py 'Sonnefeld' 'Hildburghausen' against catalogue, leads, DECODE dumps, queue, READMEs (local)",
         "result": "Only the sweep rows and lead 2663; no DECODE id."},
    ],
    "verdict": "open",
    "lead_updates": {
        "status": "Online-Findbuch text (14 Nov 2026): partly ciphered Kob-Fischer correspondence of 1749-50 with a key sheet of abbreviations. Not online; no decipherment, edition or study found.",
        "needs_archive_scan": "yes",
    },
}

# ---------------------------------------------------------------- 2664 Radefeld
out["2664"] = {
    "date": D, "by": BY,
    "seen": {
        "kind": "not online",
        "where": KOB_LINK,
        "extent": "One volume (Nr. 1307), 1769-1770; the record gives no leaf count.",
        "cipher": "Archive description: 'Teilweise verschluesselte Korrespondenz' of Duke Ernst Friedrich III Carl and Assistenzrat Christoph Wilhelm Radefeld with the courts at Wertheim, Wuerzburg, Dresden and Vienna on the duke's debts and the imperial debt commission. No key is named. Leaf not seen: not digitised.",
    },
    "prior_art": {
        "decode": "known.py 'Radefeld', 'Hildburghausen' (14 Nov 2026): no DECODE record.",
        "tomokiyo": "No Cryptiana page on Hildburghausen or Radefeld found (14 Nov 2026 web searches).",
        "lasry": "No Lasry or HistoCrypt item on a Hildburghausen cipher of 1769-70 found.",
        "edition": "No edition of Radefeld's correspondence found; the web search returned only a Halle digitised pamphlet on the duke's conduct towards the debit commission (title and OCR fragments, no cipher).",
        "literature": "Web search on Radefeld and the Hildburghausen Schuldenkommission (14 Nov 2026): the 1769 Kaiserliche Debitkommission (active to 1826) is the context; no study of ciphered letters.",
    },
    "key_check": "No key is named for this volume; the Kob keys (Nr. 998, 1006, 368) are of 1749-55 and a different correspondence, so none is known to apply. Not tested.",
    "duplicates": "known.py 'Radefeld' (14 Nov 2026): Nr. 1307 appears only in the sweep rows and lead 2664; no entry for the Geheimes Archiv Hildburghausen.",
    "searches": [
        {"query": "Radefeld Assistenzrat Hildburghausen Schuldenkommission Reichshofrat Herzog Ernst Friedrich III Carl Schulden 1769 Chiffre (web search)",
         "result": "Debit commission of 1769 (Wikipedia, active to 1826); a Halle pamphlet on the duke's conduct towards the commission; nothing on Radefeld or ciphers."},
        {"query": "known.py 'Radefeld' against catalogue, leads, DECODE dumps, queue, READMEs (local)",
         "result": "Only the sweep rows and lead 2664."},
        {"query": "Tomokiyo Lasry cipher Hildburghausen Meiningen Sachsen-Weimar archive undeciphered 18th century German court cipher letters (web search)",
         "result": "Mary Stuart and TNA decipherments and a Dresden court-cipher paper; nothing on Thuringian courts."},
    ],
    "verdict": "open",
    "lead_updates": {
        "status": "Online-Findbuch text (14 Nov 2026): partly ciphered correspondence of 1769-70, no key named. Not online; no decipherment, edition or study found.",
        "needs_archive_scan": "yes",
    },
}

# ---------------------------------------------------------------- 2666 Wallenrodt
out["2666"] = {
    "date": D, "by": BY,
    "seen": {
        "kind": "not online",
        "where": "Landesarchiv Thueringen Online-Findbuch (archive-in-thueringen.de), Staatsarchiv Meiningen, Hennebergica Altenburg (4-10-1100) Nr. 310: record text read in a Chrome tab on that origin in the 14 Nov 2026 sweep; no image is attached.",
        "extent": "Two pieces inside a volume on the houses Coburg and Heldrungen 1546-52: the Denkzettel of August 1550 (Bl. 145-160) and one of September 1550; leaf count of the cipher parts not given.",
        "cipher": "Archive description, verbatim: 'Denkzettel des Matthias von Wallenrodt, 1550 Aug. (Bl. 145-160), Sept., z.T. in Geheimschrift'. No key is named. Leaf not seen: not digitised.",
    },
    "prior_art": {
        "decode": "known.py 'Wallenrodt', 'Hennebergica', 'Denkzettel' (14 Nov 2026): no DECODE record; Wallenrodt appears in catalogue 593 only as a recipient of Prussian orders of the 1740s, a different man.",
        "tomokiyo": "No Cryptiana page found on Wallenrodt or Ernestine-Saxon ciphers of 1550 (14 Nov 2026 web search).",
        "lasry": "No Lasry paper on a mid-16th-century Ernestine-Saxon cipher found.",
        "edition": "Mentz, Johann Friedrich der Grossmuetige vol. 3 (Internet Archive johannfriedrichd03ment, OCR searched 14 Nov 2026): no Denkzettel of Wallenrodt of 1550; the volume prints Wallenrod's 1541 instruction (Nr. 45) and nothing of 1550 from Nr. 310.",
        "literature": "Web search on Wallenrodt, Denkzettel 1550, Heldrungen and Hennebergica (14 Nov 2026): no result on the man or the piece; only a study of Geheimschrift in the Salzburg peasant uprisings of 1525-26 and Coburg exhibition catalogues.",
    },
    "key_check": "No key is named in the finding aid. Not tested.",
    "duplicates": "known.py 'Wallenrodt', 'Hennebergica', 'Denkzettel' (14 Nov 2026): Nr. 310 appears only in the sweep rows and lead 2666; no entry for the Hennebergica Altenburg.",
    "searches": [
        {"query": "Matthias von Wallenrodt Denkzettel 1550 Geheimschrift Coburg Heldrungen Johann Friedrich Gefangenschaft Henneberg Hennebergica Altenburg (web search)",
         "result": "Nothing on Wallenrodt or the Denkzettel; Salzburg 1525-26 Geheimschrift study, Coburg catalogues."},
        {"query": "Mentz vol. 3 OCR (johannfriedrichd03ment_djvu.txt): 'Wallenrod' near 1550, 'Heldrungen', 'Chiffr*'",
         "result": "Wallenrod occurs for 1541 (instruction to Duke Wilhelm of Juelich); Heldrungen only as a fortress; the many 'Chiffre' notes concern 1546-52 letters of other writers and none the 1550 Denkzettel."},
        {"query": "known.py 'Wallenrodt' 'Hennebergica' 'Denkzettel' against catalogue, leads, DECODE dumps, queue, READMEs (local)",
         "result": "Only the sweep rows and lead 2666 (and Wallenrodt in catalogue 593 as an unrelated Prussian name)."},
    ],
    "verdict": "open",
    "lead_updates": {
        "status": "Online-Findbuch text (14 Nov 2026): two Denkzettel of Aug-Sept 1550, partly in Geheimschrift, no key named. Not online; no decipherment, edition or study found.",
        "needs_archive_scan": "yes",
    },
}

# ---------------------------------------------------------------- 2668 Fritsch
out["2668"] = {
    "date": D, "by": BY,
    "seen": {
        "kind": "not online",
        "where": "Landesarchiv Thueringen Online-Findbuch (archive-in-thueringen.de), Hauptstaatsarchiv Weimar, Grossherzogliches Hausarchiv A XXVI (Carl Alexander) Nr. 269: record text read in a Chrome tab on that origin in the 14 Nov 2026 sweep; no image is attached.",
        "extent": "One volume of 135 Bl., 1845-1858; the share of the volume that is ciphered is not stated.",
        "cipher": "Archive description: 'Verschluesselte Berichte' (135 Bl.) of Carl Freiherr von Fritsch, Thuringian envoy to the Bundestag at Frankfurt, to Grand Duke Carl Alexander; the volume also holds the 1848 draft treaty of the Thuringian states and a dispatch of 19 March 1849. No key is named. Leaf not seen: not digitised.",
    },
    "prior_art": {
        "decode": "known.py 'Fritsch', 'Carl Alexander', 'Bundestag' (14 Nov 2026): no DECODE record; the catalogue's Bundestag entry is the Brunswick envoys' letters of 1828-30, another correspondence.",
        "tomokiyo": "No Cryptiana page on Saxe-Weimar Bundestag ciphers of the 1840s-50s found (14 Nov 2026 web search).",
        "lasry": "No Lasry or HistoCrypt item on Thuringian Bundestag ciphers found.",
        "edition": "No edition of Fritsch's Bundestag reports found; the search returned the Deutsche Biographie entries on Carl Wilhelm von Fritsch (1804-1892) and nothing on his Frankfurt reports.",
        "literature": "Web search 'Carl von Fritsch Bundestagsgesandter Frankfurt Sachsen-Weimar verschluesselte Berichte' (14 Nov 2026): biography only; no study of the ciphered reports.",
    },
    "key_check": "No key is named in the finding aid; the Weimar Hausarchiv A XXVI may hold one among the Carl Alexander correspondence (unseen). Not tested.",
    "duplicates": "known.py 'Fritsch', 'Carl Alexander', 'Bundestag' (14 Nov 2026): A XXVI Nr. 269 appears only in the sweep rows and lead 2668; catalogue's Bundestag entry is Brunswick's, not this.",
    "searches": [
        {"query": "Carl von Fritsch Bundestagsgesandter Frankfurt Sachsen-Weimar Carl Alexander verschluesselte Berichte 1848 Chiffre Briefwechsel Edition (web search)",
         "result": "Deutsche Biographie and Wikipedia entries on Carl von Fritsch (1804-1892); nothing on the reports, the cipher or an edition."},
        {"query": "known.py 'Fritsch' against catalogue, leads, DECODE dumps, queue, READMEs (local)",
         "result": "Only the sweep rows and lead 2668."},
        {"query": "known.py 'Carl Alexander' 'Bundestag' against catalogue, leads, DECODE dumps, queue, READMEs (local)",
         "result": "Catalogue entry of Brunswick envoys at the Bundestag 1828-30 and an AIS Schmalkalden lead of 1537, both unrelated; no DECODE id."},
    ],
    "verdict": "open",
    "lead_updates": {
        "status": "Online-Findbuch text (14 Nov 2026): 135 Bl. of 'Verschluesselte Berichte' of the Bundestag envoy Fritsch, no key named. Not online; no decipherment, edition or study found.",
        "needs_archive_scan": "yes",
    },
}

# ---------------------------------------------------------------- closes
out["2656"] = {
    "date": D, "by": BY, "verdict": "duplicate",
    "closed": "BayHStA Kurbayern Aeusseres Archiv 4591 is the volume the repo already works: catalogue entry 161 and targets/kaa4591 and targets/kaa4591b (Laski's cipher systems A' and B; DECODE R9322 ff. 121-122, R9323 f. 123, R9417 f. 264, R9403 ff. 226-228, R9318 key f. 95, R9367). The finding aid's '288 fol., Chiffrier- und Dechiffriertabellen, Korrespondenzschreiben in verschluesselter Schrift' describes that same volume; known.py on '4591' and 'Kurbayern' (14 Nov 2026) returns catalogue 161/162, the two target folders and the DECODE records.",
}
out["2665"] = {
    "date": D, "by": BY, "verdict": "partly_read",
    "seen": {
        "kind": "transcription",
        "where": "Georg Mentz, Johann Friedrich der Grossmuetige vol. 3 (Internet Archive johannfriedrichd03ment, OCR searched 14 Nov 2026), table of contents Nr. 43 and the printed piece with its apparatus; and the Online-Findbuch record of Reg. E Nr. 136 (read in a Chrome tab, 14 Nov 2026).",
    },
    "closed": "The headline cipher of the lead, the Elector's letter to Luther and Bugenhagen (Reg. E Nr. 136, fol. 394-400, 'z.T. verschluesselt, Schluessel fol. 393', May 1541), is printed in Mentz vol. 3 Nr. 43 with the ciphered words set in spaced type and the resolutions noted 'von Burchards Hand': the key was applied and the deciphered text is in print, so it is read from an existing decipherment, not an open ciphertext. The Findbuch's other ciphered pieces of the volume are in the councillors' reports to the Elector (1 June 1541, fol. 505-506 and 512 'verschluesselt'; the lead also quotes 26 May, fol. 300-302): a few leaves each, no key of their own named, not online, so no ciphertext was seen and no entry is made for them now; they stay in the lead's notes. The Speyer 1542 volume was not read.",
}

# ---------------------------------------------------------------- unvetted
UNV = {
    "2653": "GLA Karlsruhe 111 Nr. 304: one ciphered letter with its Dechiffrierung inside a Geroldseck file of 1779; sender, recipient and length are not given and the record has no image, so ciphertext not seen; no prior-art searches beyond the local known.py run. Needs an archive reply.",
    "2654": "NLA OS Rep 100 Abschnitt 256 Nr. 4: one ciphered report with its Aufloesung of 1630 inside a mixed volume; no image or length on the record; ciphertext not seen and prior art not searched beyond the local grep.",
    "2655": "Hessian Marburg 3 Nr. 712: the finding aid says only 'Dabei: Chiffrenalphabet' (a key filed with the envoys' letters); it does not say the letters are ciphered. Archivportal-D shows no image. Prior art: web search and known.py run (no result), but no ciphertext is named, so it is left until Marburg is asked or an LAGIS image is found.",
    "2657": "Saxon Loc. 03447/28 (de Vela): 'Dechiffrierte Briefe' of 1758-59, whether the cipher text is kept beside the plain copies is not stated; no digital copy found; not viewed.",
    "2658": "Saxon Loc. 00694/10 viewed on archiv.sachsen.de (7 microfilm frames: a 1893 title sheet by Dr. Krauske and a table of code numbers with French words, e.g. a numbered list of persons and places): this is a key table (Krauske's reconstruction), not ciphertext. The ciphertext sits in Loc. 694/08 (1712, digitised microfilm, French letters) and 694/09; the first 12 frames of 694/08 showed clear French letters with no numerals located, and the film is too coarse to find the ciphered passages without a page-by-page pass. Not promoted until the ciphered passages are found and a key-state note written.",
    "2659": "Saxon 10736 Nr. 00457/02 (Hitzschold, 1850) viewed on archiv.sachsen.de: the digital copy is 6 frames (cover and a few clear German leaves of the police file); no cipher sheet and no 'Entschluesselung' leaf is among them, so the cipher is not seen.",
    "2660": "BLHA Neuhardenberg Film 1563: the record carries only a title and a wildcard hit on chiffr*; the cipher word is not shown and the BLHA front end is broken; nothing seen.",
    "2667": "Henneberg-Brunswick papers Nr. 2661: 'Schreiben in Geheimschrift (Bl. 191-195)' only; no key named, not online, and prior-art searches stopped at known.py; left until Duke Albrecht of Prussia's key volumes (GStA PK, key_leads) are compared.",
}
for k, v in UNV.items():
    out[k] = {"unvetted": v}

with open(os.path.join(HERE, "vetting.json"), "w", encoding="utf-8") as fh:
    json.dump(out, fh, ensure_ascii=False, indent=1)
    fh.write("\n")
print(len(out))
