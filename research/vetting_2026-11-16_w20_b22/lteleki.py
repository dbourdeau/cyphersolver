import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *
base = ("Not assessed: the printed ciphertext in Teleki Mihály levelezése is still unseen. 16 Nov 2026: archive.org has no copy (advancedsearch on title 'teleki'); Hungaricana Library answers scripts but holds only citations of the edition, not the volumes; books.google.com page view returns a 403 'automated queries' page and the Books API quota is exhausted. The gdata feed does identify the Google Books volumes: {ids}, which a Chrome session could open at the page. Tomokiyo and Lasry (copies fetched 15 Nov 2026) have no entry for {names}; known.py finds no other row.")
put(2220, {"verdict": None, "confidence": "low",
 "note": base.format(ids="vol. II (1906) WM2_l3XbnwQC, iGHzUdDZ5SkC, jw0VAAAAYAAJ (its table of contents lists Kászoni's letters of 1663, matching no. 417)", names="Teleki, Kászoni, C.Tel.81") + " Lang's Real Life Cryptology (Google Books lMaLEQAAQBAJ) quotes Kászoni sending Teleki 'the new clavis' in 1663 (Teleki 2, pp. 660-661), so a Kászoni key is mentioned in the same volume; whether it is printed is unchecked.",
 "access": "archive", "access_note": "Printed edition (Gergely, Teleki Mihály levelezése II, 1906) not free online from this machine; library copy, Arcanum ADT, or Google Books in Chrome."})
put(2221, {"verdict": None, "confidence": "low",
 "note": base.format(ids="vol. IV (1908) dY_RAAAAMAAJ, cnDAdxVEDSgC", names="Kende, Teleki, C.Ken"),
 "access": "archive", "access_note": "Printed edition (Teleki Mihály levelezése IV, 1908) not free online from this machine; library copy, Arcanum ADT, or Google Books in Chrome."})
put(2219, {"verdict": None, "confidence": "low",
 "note": base.format(ids="vol. VIII (1926) FjzUAAAAMAAJ, -4l8XGKqC_4C", names="Rhédey, Teleki, C.Tel.30") + " The lead record itself says Rhédey's reply is printed partly resolved, so at best part of this row is open.",
 "access": "archive", "access_note": "Printed edition (Gergely 1926, Teleki Mihály levelezése VIII) not free online from this machine; library copy, Arcanum ADT, or Google Books in Chrome."})
