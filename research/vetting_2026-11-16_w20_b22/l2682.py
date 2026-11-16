import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *
put(2682, {"verdict": "read", "confidence": "high",
 "note": "All 30 cipher-bearing Malvezzi regests in Türkei I Kt. 8-9 (1549-51) carry a decipherment on file (contemporary interlinear, or a 19th-century solution on a separate sheet; 43449 has its clear Latin draft) and 27 of them cite their printed text in Nehring, Austro-Turcica 1541-1552 (1995). No Kt. 8-9 piece lacks a decipherment.",
 "access": "archive", "access_note": "Regests only on Hungaricana; the texts are printed in Nehring, Austro-Turcica 1541-1552 (Munich 1995).",
 "vetting": V(
  {"kind": "not online", "where": "Hungaricana search 'Malvezzi' (249 regests) and the full regest of each of the 78 Türkei I Kt. 8-9 hits read by script on 16 Nov 2026 (raw/malv_full.txt in this folder), e.g. archives.hungaricana.hu/en/lear/BecsSeg/43471/, 43461/, 43483/, 43485/, 43498/, 43394/. No images online.",
   "extent": "30 regests mention cipher (sifrír, dechiffrirung): Malvezzi to Ferdinand I, Charles V and Jordanus 1549-51, Ferdinand to Malvezzi (43408, 43449, 43476, 43495), and two ciphered enclosures (43404 János Zsigmond, 43407 Sigismund of Poland to Süleyman).",
   "cipher": "Every one of the 30 is described with its decipherment: 'sorközi feloldással' / 'sorközben feloldva' (interlinear), 'XIX. századi feloldással' or 'desifrír a XIX. századból' (a 19th-century solution, 43346, 43358, 43362, 43363, 43408, 43476, 43495), or a later desifrírung (43443); 43449 has its clear Latin draft."},
  {"decode": "known.py on 'Malvezzi', 'Türkei I', 'Karton 8', 'Kt. 8' finds leads 891/892, catalogue 885 and targets/malvezzi1548 for the 1548 and 1550 groups; no other row for these pieces and no DECODE record for the remainder.",
   "tomokiyo": tomo("'Malvezzi', 'Türkei I', 'Karton 8', 'Kt. 8'"),
   "lasry": lasry("'Malvezzi', 'Türkei I', 'Karton 8', 'Kt. 8'"),
   "edition": "Nehring, Austro-Turcica 1541-1552 (Munich 1995): the regests cite its page for 27 of the 30 cipher pieces (e.g. 43471 pp. 509-510, 43461 pp. 504-509, 43483 pp. 525-529, 43498 pp. 568-571, 43511 pp. 613-615); the edition prints the despatches from the deciphered text. The three without a Nehring page are the enclosures 43404 and 43407 (interlinear decipherment) and the duplicate set 43443 (later desifrírung of the Venetian enclosure).",
   "literature": "No further search needed: the archive's own regests and the edition settle the status of each piece."},
  "The interlinear decipherments give the Malvezzi key; targets/malvezzi1548 already works it. Nothing remains to apply it to in Kt. 8-9.",
  "Overlaps leads 891/892 and targets/malvezzi1548 (1548 and spring-autumn 1550); the row is the remainder of the same boxes, all deciphered.",
  "read",
  "Every ciphered Malvezzi piece in Türkei I Kt. 8-9 carries a contemporary or 19th-century decipherment on file and is printed in Nehring's Austro-Turcica, so nothing is left unread.")})
