import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *
put(2684, {"verdict": "duplicate", "confidence": "high",
 "note": "The regests name the senders the list view cut off: the 1658-66 pieces are Fr. Nicolaus Donellanus OSA (9 letters, Latin, cipher deciphered on a separate sheet) and Jónás Mednyánszky (27 Nov 1658, Hungarian, interlinear decipherment), all read at the time. The only undeciphered pieces are 146425 (7 Feb 1659, 'Gróf ? György', no decipherment), already catalogue 2455, and 146487/146488 (Wesselényi, Oct-Nov 1663), already catalogue 1231. Nothing new is left for this row.",
 "access": "archive", "access_note": "Regests only on Hungaricana; no images.",
 "vetting": V(
  {"kind": "not online", "where": "Hungaricana regests 146415-146510 (HHStA Ungarische Akten, Specialia, Verschwörerakten IV, Nádasdysche Akten Fasc. 309 Konv. A-C and Fasc. 310 Konv. A-B) read in full by script on 16 Nov 2026 (raw/nad.txt), including archives.hungaricana.hu/en/lear/BecsSeg/146425/, 146454/, 146455/, 146457/, 146458/, 146461/-146464/, 146487/, 146488/, 146500/, 146504/. No images.",
   "extent": "13 cipher-bearing letters 1658-66 in the Nádasdy papers.",
   "cipher": "Donellanus to Nádasdy (146454, 146457, 146458, 146461, 146462, 146463, 146464, 146500, 146504): 'orig. latin, (részben) sifrír, amely külön lapon került feloldásra' (deciphered on a separate sheet). Mednyánszky to Nádasdy 27 Nov 1658 (146455): 'orig. magyar, sifrír sorközben feloldva'. Without decipherment: 146425 (Count ? György to unknown, 7 Feb 1659?) and 146487/146488 (Wesselényi to unknown, 10 Oct and 20 Nov 1663)."},
  {"decode": "known.py on 'Nádasdy', 'Nadasdy', 'Fasc. 309', 'Fasc. 310' finds catalogue 2455 (Fasc. 309 Konv. A fol. 1-2 = regest 146425) and catalogue 1231 (Fasc. 310 Konv. A fol. 32-37 = 146487/146488); DECODE Nádasdy keys R686/696/697/648 are the key side (per the 14 Nov vetting).",
   "tomokiyo": tomo("'Nádasdy', 'Nadasdy', 'Fasc. 309', 'Fasc. 310'"),
   "lasry": lasry("'Nádasdy', 'Nadasdy', 'Fasc. 309', 'Fasc. 310'"),
   "edition": "No edition cited in the regests; the Donellanus and Mednyánszky letters carry their contemporary decipherments, so print is not needed to settle them.",
   "literature": "Not searched further; the regests settle the status."},
  "Contemporary decipherments of the Donellanus and Mednyánszky letters give their keys; DECODE R686/696/697/648 hold Nádasdy keys. The open pieces are handled in catalogue 2455 and 1231.",
  "The undeciphered residue duplicates catalogue 2455 (146425) and catalogue 1231 (146487, 146488); no other lead overlaps.",
  "duplicate",
  "All new pieces in this row (Donellanus 1658-66, Mednyánszky 1658) carry contemporary decipherments, and the undeciphered ones are already catalogue 2455 and 1231.")})
