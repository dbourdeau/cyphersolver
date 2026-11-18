import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *
put(2688, {"verdict": "read", "confidence": "high",
 "note": "All four regests the row names say the cipher is deciphered on file (two interlinear, two on a separate sheet) and all four are printed in Károlyi, Fráter György levelezése, Történelmi Tár 1878. Record errors: 154594 (29 May 1542, Déva) is to Johann Wese, archbishop of Lund, not of Esztergom, and the four pieces sit at fol. 193-196, 205-207, 210-215 and 218.",
 "access": "archive", "access_note": "Regests only on Hungaricana (Vienna inventory); no images; the text is printed in Történelmi Tár 1878.",
 "vetting": V(
  {"kind": "not online", "where": "Hungaricana Vienna-inventory regests read in full by script on 16 Nov 2026: archives.hungaricana.hu/en/lear/BecsSeg/154594/, 154600/, 154603/, 154606/ (HHStA Ungarische Akten, Miscellanea Fasc. 431.A Konv. B, fol. 193-196, 205-207, 210-215, 218). No images online.",
   "extent": "Four letters of Frater Georgius (Martinuzzi) of 29 May, 17 Sep, 6 Oct and 12 Oct 1542; the ciphered share is not stated.",
   "cipher": "The regests call each 'orig. latin, sifrír/chiffrir' with 'sorközben feloldva' (154594, 154606: interlinear decipherment) or 'külön lapon feloldva' (154600, 154603: decipherment on a separate sheet)."},
  {"decode": "known.py on 'Martinuzzi', 'Fráter György', 'Frater Georg' and 'Fasc. 431' finds catalogue 503 (1543 enclosure) and 885 (1548 copies to Ibrahim Pasha) and leads 2462 (Gerendi 1529, same fascicle) but no row for these 1542 letters; no DECODE record found for them.",
   "tomokiyo": tomo("'Martinuzzi', 'Fráter György', 'Frater Georg', 'Fasc. 431'"),
   "lasry": lasry("'Martinuzzi', 'Fráter György', 'Frater Georg', 'Fasc. 431'"),
   "edition": "Each regest cites its printed text: Károlyi Árpád, Fráter György levelezése, Történelmi Tár 1878, pp. 260-264 (154594), 268-269 (154600), 501 (154603), 504-505 (154606). The edition prints the letters, so the 1542 texts have been read in print as well as at the time.",
   "literature": "A Hungaricana search for 'Fráter György sifrír' returns only these three Fasc. 431 regests plus 43464 (1550 credentials to Salm, also interlinear decipherment); no 1542 piece without a decipherment exists in the inventory."},
  "Each piece carries its own contemporary decipherment (interlinear or separate sheet), which gives the 1542 key; catalogue 885 / targets/ibrahim1548 hold a later Martinuzzi key. Not compared here because nothing is left to read.",
  "known.py on shelfmark and names: catalogue 503 and 885 are other years; no duplicate row for these four letters.",
  "read",
  "All four 1542 Martinuzzi letters carry a contemporary decipherment on file and are printed in Károlyi, Történelmi Tár 1878, so nothing is left unread.")})
