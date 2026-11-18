import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *
put(2584, {"verdict": "key_lookup", "confidence": "low",
 "note": "New fact: the next regest in the same Konvolut, 47912 (Türkei I Kt. 34 Konv. 2 fol. 180-184, '1576?'), is 'Egy darab rejtjelkulcs' (a cipher key), filed two leaves after the one-page cipher of fol. 178; Ungnad's key is also on DECODE (R392). The page is undated and unattributed and may be a stray exemplar of one of the Dec 1576 Ungnad despatches deciphered in the same file (47884, 47888-47890, 47893, 47899), so it is not shown to be an undeciphered text; with two candidate keys at hand it is at most a key lookup, and a single folio inside lead 1220.",
 "access": "archive", "access_note": "Regest only on Hungaricana; HHStA Türkei I Kt. 34 Konv. 2 fol. 178-184 (cipher page and key) needs a copy order.",
 "vetting": V(
  {"kind": "not online", "where": "Hungaricana regests 47880-47915 (Türkei I Kt. 34 Konv. 2, 1576 XI-XII, fol. 52-193) read in full by script on 16 Nov 2026 (raw/kt34.txt), including archives.hungaricana.hu/en/lear/BecsSeg/47910/ (fol. 178) and 47912/ (fol. 180-184). No images.",
   "extent": "One page (fol. 178), undated ('1576?'), sender and language not stated.",
   "cipher": "Regest 47910: 'egy oldal csupa rejtjel' (one page entirely in cipher), no decipherment mentioned. 47912, fol. 180-184: 'Egy darab rejtjelkulcs' (one cipher key). The same Konvolut holds Ungnad's despatches of 2, 5, 8 and 19 Dec 1576, all ciphered with interlinear or separate decipherment."},
  {"decode": "known.py on 'Karton 34', 'Kt. 34', 'Ungnad', '47910' finds catalogue 342 (Ungnad 12 Mar 1576, key R392 transcribed in targets/ungnad1576/KEY.md) and lead 1220 (Türkei I Kt. 29-36); no row for fol. 178 or the fol. 180-184 key.",
   "tomokiyo": tomo("'Karton 34', 'Kt. 34', 'Ungnad', '47910'"),
   "lasry": lasry("'Karton 34', 'Kt. 34', 'Ungnad', '47910'"),
   "edition": "Not printed as far as the regests show (no edition cited for 47910 or 47912); the Lang 2015 repertory list of Ungnad pieces (C.Ung.*) was not re-read here.",
   "literature": "No web search for a one-line undated folio; the regest context is the deciding evidence."},
  "Two keys at hand: the 'rejtjelkulcs' at fol. 180-184 of the same Konvolut (Hungaricana 47912) and Ungnad's key R392 (OSZK Quart. Lat. 2254 f. 23, transcribed in targets/ungnad1576/KEY.md). Either would decipher the page if it is Ungnad's.",
  "A single folio within lead 1220 (Türkei I Kt. 29-36); possibly a duplicate of a deciphered Dec 1576 Ungnad despatch in the same Konvolut (not checkable without the image).",
  "key_lookup",
  "A one-page undated cipher filed beside a cipher key (fol. 180-184) in a Konvolut of deciphered Ungnad despatches, with Ungnad's key also on DECODE (R392): a key lookup and part of lead 1220, not a separate open target.")})
