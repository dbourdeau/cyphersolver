"""Builds proposals.json for wave 20 batch b17 (16 Nov 2026)."""
import json, pathlib
HERE = pathlib.Path(__file__).resolve().parent
BY = "claude session 16 Nov 2026 (Claude Opus 5.5), wave 20 vetting"
D = "2026-11-16"
TOMO = "Tomokiyo's unsolved.htm (fetched 15 Nov 2026) searched, tags stripped, for %s: no hit."
LASRY = "Lasry's GL.htm list (fetched 15 Nov 2026) searched, tags stripped, for %s: no hit."
P = {}


def V(seen, prior, key, dup, verdict, closed=None):
    v = {"date": D, "by": BY, "seen": seen, "prior_art": prior, "key_check": key, "duplicates": dup, "verdict": verdict}
    if closed:
        v["closed"] = closed
    return v


# ---------------- 2813 Gaelic scribal cipher ----------------
P["2813"] = {
 "verdict": "read", "confidence": "high",
 "note": "The NLS (Black) description of Adv.MS.72.2.10, read from the Wayback copy of 6 May 2025, prints Angus Beaton's cipher colophons with their readings: p. 302 'Misi bhdlnghfts mbhc fscbhrcbhngr' (Aonghus mac Fearchair), p. 333 'bhdlinghfts mbhc fscr chair', p. 348 'Misi bhdlnghfts', p. 401 'mngsng bhdlnghfts mbhc fsebhrcair' (misi Aonghus mac Fearcair), and p. 16 likewise. 'Donnchadh's cipher' is a vowel-for-consonant-group substitution of the scribe's own name formula, read by the cataloguer; close as read. Adv.MS.72.1.33 and 72.1.5 were not seen (no Wayback copy) but are described as the same kind of colophon cipher.",
 "access": "archive",
 "access_note": "NLS Advocates Gaelic manuscripts; manuscripts.nls.uk answers 403 to scripts (16 Nov 2026); the Adv.MS.72.2.10 record was read from web.archive.org/web/20250506071941id_/https://manuscripts.nls.uk/repositories/2/resources/20198; no Wayback copy of the 72.1.33 record (resources/21663). Adv.MS.72.1.33 images are said (15 Nov note) to be on Irish Script on Screen; not opened.",
 "vetting": V(
  {"kind": "transcription",
   "where": "NLS Archives and Manuscripts catalogue record of Adv.MS.72.2.10 (Black's description), Wayback copy https://web.archive.org/web/20250506071941id_/https://manuscripts.nls.uk/repositories/2/resources/20198 (saved as raw/nls20198.txt), read 16 Nov 2026; the record transcribes Angus Beaton's colophons and notes page by page.",
   "extent": "Short scribal colophons: in Adv.MS.72.2.10 the name formula on pp. 16, 302, 333, 348 and 401 (one line or less each); Adv.MS.72.1.33 fol. 1v colophon and Adv.MS.72.1.5 'florid form of cipher' are of the same kind (described, not seen).",
   "cipher": "The catalogue says Angus 'even uses Donnchadh's cipher (pages 302, 333, 348, 401; cf. Adv.MS.73.1.22, folio 310 recto)' and gives each cipher colophon with its reading in brackets, e.g. p. 401 'mngsng bhdlnghfts mbhc fsebhrcair' (misi Aonghus mac Fearcair): vowels are replaced by consonant groups (a = bh, o = dl, u = ft, e = s, i = ng), so the cipher is a known name-formula substitution, read in the catalogue itself."},
  {"decode": "known.py on 72.1.33, 72.2.10, 72.1.5, Beaton, Fithcheallaigh and Donnchadh (DECODE dumps, catalogue, leads, targets) 16 Nov 2026: only this lead and its sweep rows; no DECODE record.",
   "tomokiyo": TOMO % "Gaelic, Beaton, Donnchadh",
   "lasry": LASRY % "Gaelic and Beaton",
   "edition": "The cataloguer's description (Black's catalogue text as used on manuscripts.nls.uk) prints the colophons with readings; that is the published reading.",
   "literature": "No further web search needed: the published catalogue reading decides the verdict. The device (vowels written as consonant groups) is the familiar Gaelic scribal name cipher."},
  "No key needed: the substitution can be read off the catalogue's paired cipher and plain forms (a = bh, o = dl, u = ft, i = ng, e = s, consonants mostly kept).",
  "known.py on the three shelfmarks and scribe names: no other lead or catalogue entry. Adv.MS.73.1.22 f. 310r (Donnchadh O Conchubhair) uses the same cipher and is not a lead.",
  "read",
  "The NLS catalogue transcribes and reads the cipher colophons (the scribe's name formula in a vowel-substitution cipher), so the cipher was read in print.")}

# ---------------- 1929 Tweeddale cypher tables (key only) ----------------
P["1929"] = {
 "verdict": None, "confidence": "medium",
 "note": "Key only, no ciphertext shown: the full NLS record (Wayback copy of 14 Sep 2024) shows MS.14496 is 'Legal, financial and miscellaneous papers of the 2nd Marquess of Tweeddale, 1669-1712' (Hays of Yester papers), item (iv) 'Cypher tables, 1707-1711 (folio 105)', among bonds, discharges and executry papers; no ciphered letter is named. Record correction: the owner is John Hay, 2nd Marquess of Tweeddale, not 'the 2nd Hay'. Not assessable as a ciphertext lead; useful as key material for Tweeddale or Squadrone letters of 1707-11 if any turn up.",
 "access": "archive",
 "access_note": "NLS MS.14496 (143 leaves); manuscripts.nls.uk 403 to scripts; record read at https://web.archive.org/web/20240914080947id_/https://manuscripts.nls.uk/repositories/2/archival_objects/35956. Not digitised as far as the record shows.",
 "correct_title": "Papers of the 2nd Marquess of Tweeddale: cypher tables 1707-1711 (MS.14496, f. 105 ff.)"}

# ---------------- 1932 Currie cypher systems ----------------
P["1932"] = {
 "verdict": None, "confidence": "low",
 "note": "Not assessed: the full NLS record (Wayback copy of 20 May 2024) places MS.11732 (38 leaves) in the papers of the 1st Earl of Minto as Governor-General of India: 'Letters and papers of D Currie, 8 Duke's Row, Tavistock Square, London, concerning various cypher systems, 1805-1807'. It describes proposals about cipher systems sent to Minto, not ciphered correspondence; whether specimen ciphertexts are among them needs the leaves. Record correction: the file is in the 1st Earl of Minto's India papers (MSS.11001-13496).",
 "access": "archive",
 "access_note": "NLS MS.11732; manuscripts.nls.uk 403 to scripts; record read at https://web.archive.org/web/20240519230937id_/https://manuscripts.nls.uk/repositories/2/archival_objects/52358."}

# ---------------- 1935 Minto telegram book ----------------
P["1935"] = {
 "verdict": None, "confidence": "low",
 "note": "Not assessed; the blocker stands. The full NLS record (Wayback copy of 19 May 2024) adds only context: MS.12551 (73 leaves, oblong octavo) is among the 4th Earl of Minto's papers as Military Secretary to Lansdowne, Governor-General of Canada, 1883-86 (North-West Rebellion), 'some in cipher'. Whether the book holds coded telegrams without their plain text cannot be told from the record, and the Morton and Roy edition (archive.org telegramsofnorth0000unse and legramsofnorthwe0000desm) is lending-only: its full-text search returns 'Item not available'.",
 "access": "archive",
 "access_note": "NLS MS.12551; manuscripts.nls.uk 403 to scripts; record read at https://web.archive.org/web/20240519225809id_/https://manuscripts.nls.uk/repositories/2/archival_objects/53544."}

# ---------------- 1996 Melfort ----------------
P["1996"] = {
 "verdict": None, "confidence": "low",
 "note": "Not assessed; the blocker stands. manuscripts.nls.uk answers 403 to scripts and there is no Wayback copy of archival_objects/38177; a web search found only the catalogue snippet. Whether the 'excerpts ... partly in code' are the Rome letters Macpherson printed with decyphered passages still needs the NLS leaves.",
 "access": "archive",
 "access_note": "NLS MS.3836 ff. 3-8; catalogue blocked to scripts (403), no Wayback snapshot."}

# ---------------- 2809 NLW 9235A ----------------
P["2809"] = {
 "verdict": "open", "confidence": "medium",
 "note": "The NLW catalogue (also on Archives Hub) says of this 17th-century book of medical recipes, astrological notes and diagrams and a list of Christian names: 'Some of the recipes and notes are in cipher. The monogram M.L. occurs twice in the manuscript.' No decipherment is noted and none is published; no DECODE, Tomokiyo or Lasry record. Open as an archive item; the cipher is probably a short private substitution, and its extent is unknown.",
 "access": "archive",
 "access_note": "NLW MS 9235A; archives.library.wales answers 403 to scripts on 16 Nov 2026 and Archives Hub reset the connection; no digital object is mentioned in the description. Needs NLW images or a visit.",
 "vetting": V(
  {"kind": "not online",
   "where": "NLW archives catalogue record 'File NLW MS 9235A - Medical recipes and astrology' (https://archives.library.wales/index.php/medical-recipes-and-astrology), read in Chrome in the 15 Nov 2026 sweep (research/sweep_2026-11-15_uk_blocked_chrome/), and the Archives Hub copy (archiveshub.ac.uk record 2a54ecb3-c3ec-37fe-b2db-37089c173598) as summarised by a web search on 16 Nov 2026; no images.",
   "extent": "Not stated: 'some of the recipes and notes' in a small-format (A) 17th-century volume.",
   "cipher": "Archive description: 'Some of the recipes and notes are in cipher. The monogram M.L. occurs twice in the manuscript.' No decipherment, key or translation is mentioned."},
  {"decode": "known.py on '9235A' (DECODE dumps, catalogue, leads, targets) 16 Nov 2026: only this lead and its sweep README; no DECODE record.",
   "tomokiyo": TOMO % "recipe, Wales, astrology",
   "lasry": "Lasry's GL.htm list (fetched 15 Nov 2026) searched for recipe and Wales: the only 'recipe' hit is BnF fr. 14765 (an alchemical recipe), unrelated.",
   "edition": "No edition known: the manuscript is described only in the NLW catalogue; a web search found no printed text.",
   "literature": "Web search '\"9235A\" National Library of Wales medical recipes astrology cipher' (16 Nov 2026): only the NLW and Archives Hub records; the cipher hits are about BL Sloane MS 1902 (read via HistoCrypt), a different manuscript."},
  "No key is held or named in the description; the monogram M. L. is the only clue to the owner. Nothing was tested because no ciphertext was seen.",
  "known.py on '9235A' and a web search: no other lead or catalogue entry for this volume; NLW MS 23075A 'Astrology & medicine' is a different manuscript with no cipher noted.",
  "open")}

# ---------------- NRS four ----------------
NRS = "catalogue.nrscotland.gov.uk answers 403 to scripts (16 Nov 2026) and no Wayback snapshot exists; TNA Discovery's API does not mirror NRS records (searches for the item wording returned nothing)."
P["1261"] = {"verdict": None, "confidence": "low",
 "note": "Not assessed; the 28 Oct blocker stands: NRS CH12/12/1877 'copy of cipher, possibly Prince Charles to his father' does not say whether it is ciphertext or a key, and no scan is online. " + NRS,
 "access": "archive", "access_note": "NRS CH12/12/1877, on site only."}
P["1259"] = {"verdict": None, "confidence": "low",
 "note": "Not assessed; the blocker stands: NRS GD16/34/1 'copies of letters addressed in cypher' may mean only the addresses are in cipher, and the copies are not online. " + NRS,
 "access": "archive", "access_note": "NRS GD16/34/1, on site only."}
P["1262"] = {"verdict": None, "confidence": "low",
 "note": "Not assessed; the blocker stands: a cluster of Breadalbane items whose NRS records say only 'note in cipher' or 'names in numerical cipher' (name-code letters), no scans; should be split per item when the records can be read. " + NRS,
 "access": "archive", "access_note": "NRS GD112/39/..., on site only."}
P["1260"] = {"verdict": None, "confidence": "low",
 "note": "Not assessed; the blocker stands. The NRS summary of GD124/15/1256 (read in Chrome earlier) gives the letter's content ('calumnies were loaded on Manley'), which suggests a cant-name letter the cataloguer could read, and a 'note of the cipher used' is filed with it; that points away from open, but the scan is needed to decide. " + NRS,
 "access": "archive", "access_note": "NRS GD124/15/1256, 2 documents, on site only."}

# ---------------- 2761 Lamberg OOeLA ----------------
P["2761"] = {"verdict": None, "confidence": "low",
 "note": "Not assessed: the OOeLA findbuch (ooela.findbuch.net) is reached only through its JavaScript search in Chrome (15 Nov sweep); nothing new is reachable by script. The regest 'Brief an/von Kaiser Leopold I. nebst Chiffrenschluessel' (2 Stueck, 1660) reads most naturally as a cover letter with a cipher key, not a ciphered letter, so it may be key only; needs Akt Nr. 406 opened.",
 "access": "archive", "access_note": "OOe Landesarchiv, Herrschaftsarchive 06.S06.04.01, Akt Nr. 406; no digitisation stated."}

# ---------------- OeNB common ----------------
SRU = "OeNB Alma SRU (https://obv-at-oenb.alma.exlibrisgroup.com/view/sru/43ACC_ONB, open to scripts 16 Nov 2026; script onbsru.py)"
MAZAL = "Mazal and Unterkircher, Katalog der abendlaendischen Handschriften der OeNB, Series nova Teil 2 (1963), pp. 60-61 (manuscripta-mediaevalia.de HSK0752a_b0060-b0061), read as images 16 Nov 2026"


def schlik_prior(names):
    return {"decode": "known.py on 'Ser. n. 169', Schlik, Palm, Colonna, Saphorin (DECODE dumps, catalogue, leads, targets) 16 Nov 2026: no DECODE record for these letters; the only Palm hits are catalogue palm1727 (a different Palm, imperial resident in London 1727) and the only Schlick hit is lead 1619 (Mathias Schlick, 16th century).",
            "tomokiyo": TOMO % ("Schlik, Schlick, %s, 1705, 1707, Rakoczi" % names),
            "lasry": LASRY % ("Schlik, %s, 1705, 1707" % names),
            "edition": "No edition found: the letters are Wassenaer's 'Beilagen zur Oesterreichischen Staatsgeschichte' (1798), described in Mazal-Unterkircher 1963 without any decipherment; the OeNB SRU records carry no decipherment note (SRU searches Schlik + dechiffriert / Dechiffrierung / entziffert / Aufloesung: 0 records each).",
            "literature": "Web search 'Johann David Palm Schlik 1707 chiffriert Briefe Wassenaer Staatsgeschichte Rakoczi' (16 Nov 2026): nothing on these letters; hits were general Rakoczi-cipher items (Bercsenyi, Sieniawska)."}


SCHLIK_DUP = "SRU search Schlik + chiffriert lists 28 records: 22 Palm, 2 Colonna zu Fels, 2 Pesme de Saint-Saphorin, 2 Joseph I; each writer is its own lead (2820-2823). known.py: no other lead or catalogue entry for these volumes."
SCHLIK_KEY = "No key for Schlik's correspondents of 1705-07 is held in the repo or on DECODE (known.py); Schlik's own letterbooks in Cod. Ser. n. 1697 (ff. 2-146: to Joseph I, and to Andrezel, Clifford, Pesme de Saint-Saphorin, Salm, Schoenborn, Sutton, Theilliere, Wratislaw, Jan-Jun 1707) are clear outgoing copies that may give context, not a decipherment. Nothing tested."

P["2820"] = {
 "verdict": "open", "confidence": "medium",
 "note": "OeNB SRU lists 22 records of Hofkammerrat Johann David Palm to Count Leopold Schlik, Vienna, 12 Jan - 2 Jun 1707 (25 letters), each 'Brief grossteils chiffriert' or 'teilweise chiffriert', with no decipherment noted; Mazal-Unterkircher 1963 confirms 'Groesstenteils chiffriert'. No DECODE, Tomokiyo, Lasry or edition. Record correction: the Palm letters are in Cod. Ser. n. 1697 (Bd. 12, Beilagen 802-849, Jan-Mar 1707) and Cod. Ser. n. 1698 (Bd. 13, Beilagen 873-927, Apr-Jun 1707), none in 1696; in 1707 Schlik commanded in Italy, so the context is the Italian campaign, not the Rakoczi war.",
 "access": "archive",
 "access_note": "OeNB Sammlung von Handschriften, Cod. Ser. n. 1697-1698; the ONB image routes (onb.digital, api.onb.ac.at IIIF) failed on 15 Nov; no Digitalisat link in the SRU records. Needs an OeNB reproduction.",
 "correct_shelfmark": "OeNB, Cod. Ser. n. 1697 (fol. 147-299) and Cod. Ser. n. 1698 (fol. 50-211) [Palm letters]",
 "vetting": V(
  {"kind": "not online",
   "where": SRU + ": query 'alma.all_for_ui=\"Schlik\" and alma.all_for_ui=\"chiffriert\"' (raw/sru_schlik_chiff.txt) and parent records AC13931942 (Bd. 12) and AC13932064 (Bd. 13) (raw/sru_parents.txt); " + MAZAL + ". No image.",
   "extent": "22 records, 25 letters, 12 Jan - 2 Jun 1707, 2 to 12 leaves each (e.g. fol. 147r-152v, 159r-164v, 111r-122v); 15 marked 'grossteils chiffriert', the rest 'teilweise chiffriert'.",
   "cipher": "Archive description per letter, e.g. AC13931945 'Beilage Nr. 802. Brief grossteils chiffriert.', AC13932091 'Brief teilweise chiffriert. - Beilage Nr. 890'; volume note 'Zahlreiche chiffrierte Berichte' (Bd. 12). No decipherment, translation or key is noted in any record."},
  schlik_prior("Palm"), SCHLIK_KEY, SCHLIK_DUP, "open")}

P["2821"] = {
 "verdict": "open", "confidence": "medium",
 "note": "Two letters of Franz Colonna zu Fels to Schlik, Grosswardein 5 and 11 Dec 1705 (Cod. Ser. n. 1696, fol. 31r-32v and 54r-55v, Beilagen 639 and 652), each 'teilweise chiffriert' per the OeNB SRU records; no decipherment noted, no prior art found. Small (two letters), but open as described. Record correction: only these two letters carry the cipher note, both in Cod. Ser. n. 1696 (Bd. 11, documents of 1705-06), not 1697-98.",
 "access": "archive",
 "access_note": "OeNB Cod. Ser. n. 1696; no Digitalisat link; ONB image routes failed on 15 Nov.",
 "correct_shelfmark": "OeNB, Cod. Ser. n. 1696, fol. 31r-32v and 54r-55v [Colonna zu Fels letters]",
 "vetting": V(
  {"kind": "not online",
   "where": SRU + ": records AC13931651 and AC13931662 (raw/sru_schlik_chiff.txt), parent AC13931595 (Cod. Ser. n. 1696); no image.",
   "extent": "Two letters of two leaves each (fol. 31r-32v, 322 x 200 mm; fol. 54r-55v, 317 x 195 mm); part of each in cipher.",
   "cipher": "Archive description: AC13931651 'Brief teilweise chiffriert. - Beilage Nr. 639'; AC13931662 'Schreiben teilweise chiffriert. - Beilage Nr. 652'. No decipherment, translation or key is noted."},
  schlik_prior("Colonna"), SCHLIK_KEY, SCHLIK_DUP, "open")}

P["2822"] = {
 "verdict": "open", "confidence": "medium",
 "note": "Two letters of R. de Pesme de Saint-Saphorin to Schlik in Cod. Ser. n. 1698: Berne, 6 Apr 1707 (fol. 78r-80r, Beilage 883) and undated 1707 without place (fol. 270r-272v, Beilage 945), both 'Brief teilweise chiffriert' per OeNB SRU; no decipherment noted, no prior art found. Record correction: written from Berne (and o. O.), not Vienna or Grosswardein; his letter from Schaffhausen, 22 Jan 1707 (Ser. n. 1697 fol. 167) has no cipher note. Schlik's outgoing letterbook (Ser. n. 1697 ff. 67-146) includes letters to Saint-Saphorin, Feb-Jun 1707, which may help as context.",
 "access": "archive",
 "access_note": "OeNB Cod. Ser. n. 1698; no Digitalisat link; ONB image routes failed on 15 Nov.",
 "correct_shelfmark": "OeNB, Cod. Ser. n. 1698, fol. 78r-80r and 270r-272v [Saint-Saphorin letters]",
 "vetting": V(
  {"kind": "not online",
   "where": SRU + ": records AC13932084 and AC13932311 (raw/sru_schlik_chiff.txt), parent AC13932064 (Bd. 13 = Cod. Ser. n. 1698); " + MAZAL + " for his unciphered Schaffhausen letter and Schlik's letterbook. No image.",
   "extent": "Two French letters, three leaves each (fol. 78r-80r, 340 x 227 mm, fol. 80v blank; fol. 270r-272v, 340 x 220 mm); part in cipher.",
   "cipher": "Archive description: AC13932084 'Brief teilweise chiffriert. - fol. 80v leer. - Beilage Nr. 883'; AC13932311 'Brief teilweise chiffriert. - Beilage Nr. 945'. No decipherment, translation or key is noted."},
  schlik_prior("Saphorin, Pesme"), SCHLIK_KEY, SCHLIK_DUP + " The 15 Nov Swiss pass holds other Saint-Saphorin rows (different letters and recipients).", "open")}

P["2823"] = {
 "verdict": "open", "confidence": "medium",
 "note": "Two rescripts of Emperor Joseph I to Schlik, Vienna 5 Dec 1705 (fol. 34r-35v, Beilage 641) and 19 Dec 1705 (fol. 91r-93v, Beilage 673), Cod. Ser. n. 1696, sealed originals 'teilweise chiffriert' per OeNB SRU; no decipherment noted, no prior art found. A chancery cipher sent to a field commander may carry the recipient's interlinear solution, which the catalogue would not necessarily note; check on the scan.",
 "access": "archive",
 "access_note": "OeNB Cod. Ser. n. 1696; no Digitalisat link; ONB image routes failed on 15 Nov.",
 "correct_shelfmark": "OeNB, Cod. Ser. n. 1696, fol. 34r-35v and 91r-93v [Joseph I rescripts]",
 "vetting": V(
  {"kind": "not online",
   "where": SRU + ": records AC13931652 and AC13931816 (raw/sru_schlik_chiff.txt), parent AC13931595 (Cod. Ser. n. 1696); no image.",
   "extent": "Two rescripts, 2 and 3 leaves (fol. 34r-35v, 315 x 205 mm; fol. 91r-93v, 337 x 215 mm); part in cipher.",
   "cipher": "Archive description: AC13931652 'Mit teilweise zerstoertem Siegel. Schreiben teilweise chiffriert. - Beilage Nr. 641'; AC13931816 'Siegel in Resten vorhanden. Teilweise chiffriert.- Beilage Nr. 673'. No decipherment, translation or key is noted."},
  schlik_prior("Joseph"), SCHLIK_KEY + " No imperial chancery key of 1705 for Hungary is among the repo's DECODE notes.", SCHLIK_DUP, "open")}

P["2824"] = {
 "verdict": "open", "confidence": "low",
 "note": "OeNB SRU record AC13847637: Vettor Zane, '73 Depeschen an Carlo Rizzini vom 20.4.1712 bis 23.8.1713, teilw. chiffriert', Vienna, I+295 leaves, parchment binding with ex libris; no decipherment noted and none found in print. The recipient is evidently Carlo Ruzzini, Venetian plenipotentiary at the Utrecht congress (record and lead spell 'Rizzini'), so these are received letters bound in the recipient's set, where an interlinear decipherment would be usual but is not recorded; hence low confidence. Ruzzini's outgoing Utrecht despatches (173, 1 Apr 1712 - 22 Aug 1713) are described in a catalogue reached only through SNAC (bot check), not seen.",
 "access": "archive",
 "access_note": "OeNB Cod. Ser. n. 25702; no Digitalisat link in the SRU record; ONB image routes failed on 15 Nov.",
 "correct_title": "Vettor Zane at Vienna, 73 despatches to Carlo Ruzzini (Venetian plenipotentiary at Utrecht), 1712-13, partly ciphered",
 "vetting": V(
  {"kind": "not online",
   "where": SRU + ": record AC13847637 (raw/sru_zane.txt), 16 Nov 2026; no image.",
   "extent": "One bound volume, I+295 leaves, 73 despatches, 20 Apr 1712 - 23 Aug 1713; how many carry cipher is not stated.",
   "cipher": "Archive title: '73 Depeschen an Carlo Rizzini vom 20.4.1712 bis 23.8.1713, teilw. chiffriert'. No decipherment, translation or key is noted."},
  {"decode": "known.py on '25702', Zane and Rizzini 16 Nov 2026: only this lead and the oenb_deep README; no DECODE record.",
   "tomokiyo": TOMO % "Zane, Ruzzini, Rizzini",
   "lasry": LASRY % "Zane, Ruzzini, Rizzini",
   "edition": "No edition of Zane's letters to Ruzzini found; Frigo's essay on Ruzzini at Utrecht (arts.units.it 11368/2932547) uses his correspondence with the Senate (web search summary, not opened). Venetian Senato, Dispacci Germania would hold Zane's official despatches; not checked.",
   "literature": "Web searches '\"Vettor Zane\" Vienna 1712 Rizzini dispacci' and 'Ruzzini dispatches 1712-1713 Utrecht Venetian representatives London Vienna manuscript cipher' (16 Nov 2026): no study of the cipher; a catalogue (via SNAC, bot check) lists Ruzzini's own 173 outgoing despatches and Grimani's 'coded letters, and transcriptions' to Ruzzini, which suggests Ruzzini's office kept separate transcriptions."},
  "No Venetian key of 1712-13 is held in the repo or found on DECODE by known.py; nothing tested.",
  "known.py on '25702', Zane, Rizzini: no other lead or catalogue entry. Grimani's coded letters to Ruzzini (via SNAC) are a different correspondent.",
  "open")}

P["2825"] = {
 "verdict": "open", "confidence": "medium",
 "note": "The cut-off word is now read: five OeNB SRU records (AC16563068, AC16566212, AC16566438, AC16566267, AC16571699) each say 'Briefe von ihrer Schwester Adelgunde, teilweise in Geheimschrift', 43 autograph letters and postcards, 116 leaves, 12 Feb 1898 - 1912, Adelgunde Duchess of Bardi to Archduchess Maria Teresa; some letters are addressed to 'Monica' or 'Andrea' and signed 'Clara' (family cover names). No decipherment noted; no prior art found. Open, but low importance; the 'Geheimschrift' could also be a private shorthand, to check on the scan.",
 "access": "archive",
 "access_note": "OeNB Autogr. 1942/21-25; no Digitalisat link in the SRU records.",
 "vetting": V(
  {"kind": "not online",
   "where": SRU + ": query 'alma.all_for_ui=\"Adelgunde\" and alma.all_for_ui=\"Geheimschrift\"' (5 records, raw/sru_bardi.txt), 16 Nov 2026; no image.",
   "extent": "Five groups: 9 items/21 leaves (1898-1911), 9/34 (1911-12), 9/23 (1911-12), 8/22 (1912), 8/16 (1912); part of the letters in cipher, amount not stated.",
   "cipher": "Archive description (field 520) in each record: 'Briefe von ihrer Schwester Adelgunde, teilweise in Geheimschrift.' Two add 'Teilweise sind die Briefe an \"Monica\" adressiert' and 'an \"Andrea\" adressiert, teilweise mit \"Clara\" unterschrieben'. No decipherment or key is noted."},
  {"decode": "known.py on 'Autogr. 1942', Adelgunde and Bardi 16 Nov 2026: only this lead and the oenb_deep README; no DECODE record.",
   "tomokiyo": TOMO % "Bardi and Adelgunde",
   "lasry": LASRY % "Bardi and Adelgunde",
   "edition": "No edition of Adelgunde of Bardi's letters to Maria Teresa found.",
   "literature": "Web search 'Adelgunde Herzogin von Bardi Briefe Erzherzogin Maria Theresa Geheimschrift' (16 Nov 2026): nothing on these letters (hits were Adelgunde of Modena's letters to Wiltrud and Empress Maria Theresa's ciphers)."},
  "No key held or known; nothing tested.",
  "known.py on the shelfmark and names: no other lead or catalogue entry (the oenb_deep README's 'known, 2816-2818' refers loosely to this sweep's rows; catalogue 2816-2818 are Buquoy, Colloredo and Dampierre, unrelated).",
  "open")}

P["2834"] = {
 "verdict": "not_cipher", "confidence": "medium",
 "note": "The OeNB card catalogue (KAT-ZOOM Autographenkatalog card 79173, image read 16 Nov 2026) reads '1) L.s.(Chiffern).av.adr. 1 f, 1 p. 7.8.1517, Augsburg; an Bernhard von Cles', i.e. a letter signed, the signature in 'Chiffern'; card 79174 has 6) 'L.s.(Chiffre)' for the Traunstein 1508 letter, the monogram-signature case the lead names. 'Chiffern' qualifies the signature, not the text, so this is a signed chancery letter, not a cipher letter. Record correction: written at Augsburg to Bernhard von Cles (Bernardo Clesio), not 'Tyrol chancery, recipient not given'.",
 "access": "archive",
 "access_note": "OeNB Autogr. 15/28-1; SRU record AC14166923 (parent AC15074034); card image https://katzoom.onb.ac.at/DB4/hnl/m001/z008/h092/g0079173.gif.",
 "vetting": V(
  {"kind": "transcription",
   "where": SRU + ": record AC14166923 ('1 Brief mit Unterschrift (Chiffern), mit Anschrift, 1 Blatt, 1 Seite'; recipient Clesio, Bernardo; place Augsburg; provenance Tiroler Gubernium 1831) and the OeNB Autographenkatalog cards 79173-79174 (https://katzoom.onb.ac.at/cgi-bin/katadmin/hnlview.pl?katalog=7&kz=1&start=0079173, images img/kz79173.png and img/kz79174.png), read 16 Nov 2026. The letter itself was not seen.",
   "extent": "One leaf, one page, with address.",
   "cipher": "The card's formula 'L.s.(Chiffern)' puts 'Chiffern' in brackets after 'L.s.' (letter signed), describing the signature, as in item 6 'L.s.(Chiffre)'; no card or record says the text is in cipher."},
  {"decode": "known.py on '15/28', Cles, Clesio and 'Maximilian I' 16 Nov 2026: no DECODE record for this letter; Maximilian I hits are other items (Moronus to Maximilian, catalogue).",
   "tomokiyo": TOMO % "Cles, 1517, Maximilian",
   "lasry": LASRY % "Cles, 1517",
   "edition": "Not searched in the Regesta Imperii (Maximilian I) for 7 Aug 1517: not needed once the card shows the 'Chiffern' note belongs to the signature.",
   "literature": "No web search: the archive's own card decides the question."},
  "No key applies: no ciphertext is described.",
  "known.py: no other lead; the series 15/28(1-11) holds other Maximilian letters, of which 15/28-6 carries the same '(Chiffre)' signature note.",
  "not_cipher",
  "The OeNB card catalogue's 'L.s.(Chiffern)' describes the signature (a sign-manual or monogram), not an enciphered text; the letter is a signed chancery letter to Bernhard von Cles, Augsburg, 7 Aug 1517.")}

ORDER = "2813 1929 1932 1935 1996 2809 1261 1259 1262 1260 2761 2825 2820 2821 2822 2823 2824 2834".split()
out = {k: P[k] for k in ORDER}
(HERE / 'proposals.json').write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print(len(out), {k: v['verdict'] for k, v in out.items()})
