import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *
put(2679, {"verdict": "partly_read", "confidence": "medium",
 "note": "Of the Stöckl cipher pieces 1569-70 (and 1573), every original carries an interlinear or separate decipherment, and the second 'nincs feloldva' item the row names, 46258 (24 Dec 1569), has its clear Latin copy at Kt. 26 Konv. 4 fol. 17-20 (regest 46363, one of a run of clear copies 'Beilage zum 6. August 1570'). The only undeciphered piece left is 46230 (18 Sep 1569, to Zasius?, 'sifrír, de nincs feloldva, 3 duplikátum'), a short request for 35 ducats, which is a key lookup against the many pairs and is probably printed in the Fazekas-Fodor edition (2025, not seen).",
 "access": "archive", "access_note": "Regests only on Hungaricana; 46230 is HHStA Türkei I Kt. 25 Konv. 3 fol. 151-152 (copy order).",
 "vetting": V(
  {"kind": "not online", "where": "Hungaricana searches 'Stöckl', 'Stöckel', 'Stoeckl', 'Anselm', 'Anselmus' and 43 Stöckl regests read in full by script on 16 Nov 2026 (raw/st_full.txt): archives.hungaricana.hu/en/lear/BecsSeg/46195/, 46196/, 46230/, 46240/, 46241/, 46246/, 46253/, 46258/, 46266/, 46271/, 46277/, 46293/, 46297/, 46298/, 46301/, 46304/, 46314/, 46361/-46378/, 46884/. No images.",
   "extent": "About 18 cipher-bearing Stöckl letters to Maximilian II and Zasius, May 1569 - Apr 1570 (Kt. 25-26), plus one of 28 Jul 1573 (46884), and a run of 18 clear Latin copies of his letters 26 Nov 1569 - 12 Jul 1570 (46361-46378).",
   "cipher": "Originals 'sifrír, sorközben feloldva' (46240, 46241, 46246, 46253, 46266, 46271, 46277, 46297, 46298, 46304, 46314, 46884), 'külön papíron feloldva' (46195; 46196 is the decipherment of two letters of 29 May and 3 Jun), 'külön egy feloldott másolat' (46301). Undeciphered: duplicates beside deciphered originals (46246, 46293, 46304), 46258 (clear copy 46363), and 46230 alone with no decipherment or clear copy found."},
  {"decode": "known.py on 'Stöckl', 'Stoeckl', 'Stockl', 'Zasius' finds only this lead; the 14 Nov vetting found no Stöckl record in DECODE or Lang's repertory.",
   "tomokiyo": tomo("'Stöckl', 'Stoeckl', 'Stockl', 'Zasius'"),
   "lasry": lasry("'Stöckl', 'Stoeckl', 'Stockl', 'Zasius'"),
   "edition": "The Fazekas-Fodor edition of the Constantinople embassy reports (2025) covers Stöckl 1569-70 (per the 14 Nov vetting); its text is not online and was not seen, so whether it prints 46230 is unchecked.",
   "literature": "The archive's regests settle the status of every piece but 46230; no further literature search."},
  "The interlinear pairs and clear copies give Stöckl's 1569-70 cipher (inherited from ambassador Wyss, per 46240); 46230 is a key lookup against them.",
  "known.py: no other row. 46258's clear copy 46363 and the duplicates 46246/46293/46304 are internal duplicates resolved here.",
  "partly_read",
  "All Stöckl ciphers of 1569-70 are deciphered on file or have clear copies except the short letter 46230 of 18 Sep 1569, a key lookup against the many pairs.")})
