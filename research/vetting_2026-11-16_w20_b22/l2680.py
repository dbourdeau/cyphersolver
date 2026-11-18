import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *
put(2680, {"verdict": "read", "confidence": "medium",
 "note": "The all-cipher item 46702 (18 Jun 1572, Kt. 28 Konv. 4 fol. 218-219, 'probably a copy of a letter of Ungnad and Provisionali') sits directly before 46703, the Ungnad-Provisionali letter of the same day (fol. 220-229, 'olasz orig., sifrír, sorközben feloldva, és külön másolat'), so it is a duplicate of a deciphered letter. Every other Provisionali cipher piece 1570-72 (about 25 regests) is deciphered interlinearly or separately; the only undeciphered duplicates (46346, 46347 of 14 Jul 1570; 46294, 46316, 46344) each have a deciphered original or a copy ('másolat') filed with them.",
 "access": "archive", "access_note": "Regests only on Hungaricana; no images.",
 "vetting": V(
  {"kind": "not online", "where": "Hungaricana search 'Provisionali' (75 regests) read in full by script on 16 Nov 2026 (raw/prov_full.txt), plus 46700-46704 and 46345 around the all-cipher piece: archives.hungaricana.hu/en/lear/BecsSeg/46702/, 46703/, 46337/, 46346/, 46347/, 46711/, 46712/. No images.",
   "extent": "About 25 Provisionali cipher pieces, Jan 1570 - Jun 1572 (Kt. 26-28): his own reports, joint letters with Stöckl (1570) and with David Ungnad (1572).",
   "cipher": "Wording 'olasz orig., sifrír, sorközben feloldva' throughout (46269, 46278 'külön feloldása', 46294-46296, 46302-46306, 46316-46318, 46323, 46327-46328, 46334, 46337, 46344, 46692, 46703, 46711, 46712). 46702 'csupa sifrír' is a second exemplar of 46703. 46346 and 46347 (14 Jul 1570) are duplicates 'nincs feloldva' filed with a copy each."},
  {"decode": "known.py on 'Provisionali', 'Karton 28', 'Kt. 28' finds only this lead; Provisionali's key sheet is DECODE R388 / Lang T.Gev.16 (per the 14 Nov vetting).",
   "tomokiyo": tomo("'Provisionali', 'Karton 28', 'Kt. 28'"),
   "lasry": lasry("'Provisionali', 'Karton 28', 'Kt. 28'"),
   "edition": "The Fazekas-Fodor edition (2025) covers Provisionali 1569-70 (per the 14 Nov vetting); not seen. 46345 (Selim to Tsar Ivan, ciphered Italian translation, interlinear decipherment) is printed in Petritsch I no. 614.",
   "literature": "The archive's regests settle the status; no further search."},
  "Key on DECODE as R388 (Lang T.Gev.16, 1570); the interlinear decipherments also give it. Not applied because nothing is left unread.",
  "46702 duplicates 46703; 46346/46347 duplicate a letter of 14 Jul 1570 with copies filed. Joint Provisionali-Stöckl letters overlap lead 2679.",
  "read",
  "Every Provisionali cipher piece of 1570-72 is deciphered on file or is a duplicate of a deciphered letter; the all-cipher 46702 is a second exemplar of the deciphered 46703 of the same day.")})
