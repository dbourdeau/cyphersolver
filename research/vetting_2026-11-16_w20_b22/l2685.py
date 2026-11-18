import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *
put(2685, {"verdict": "not_cipher", "confidence": "medium",
 "note": "The full regest (145344) names the sender and recipient: Andreas Gembicki ('comes in Zabiszyn, capitaneus Tyggenoffensis') to Count Péter Zrínyi, Kraków 4 Oct 1669, 'orig. latin, mellékelve hozzá titkosíráskulcs is, legalább három különböző': a plain Latin letter with enclosed cipher keys (at least three), not a ciphertext. Lang's repertory lists the Zrínyi/Gembicki key at f. 77. This is key material to record (DECODE key record), not an open cipher; the related Fasc. 301 piece 145842 (Kassa 3 Jun 1670, to Nádasdy) has its two cipher lines deciphered above the line.",
 "access": "archive", "access_note": "Regest only on Hungaricana; HHStA Ungarische Akten, Specialia, Verschwörerakten III, Fasc. 296 Konv. B fol. 75-83 (copy order) for the keys.",
 "vetting": V(
  {"kind": "not online", "where": "Hungaricana regests 145338-145350 (Zrínyische Akten Fasc. 296 Konv. B-C) and 145842 (Fasc. 301 Konv. A) read in full by script on 16 Nov 2026: archives.hungaricana.hu/en/lear/BecsSeg/145344/ and 145842/. No images.",
   "extent": "One Latin letter with enclosures, fol. 75-83 (9 leaves).",
   "cipher": "Regest 145344: 'Andreas Gembicki ... – Zrínyi Péter gróf (orig. latin, mellékelve hozzá titkosíráskulcs is, legalább három különböző)': the letter is described as Latin original, with cipher keys (at least three different ones) enclosed; no ciphertext is mentioned. The neighbouring Palmerini/Bargilio pieces (145340-145343) are Italian originals and copies, not ciphered."},
  {"decode": "known.py on 'Zrínyi', 'Zrinyi', 'Gembicki', 'Fasc. 296' finds only this lead (catalogue 1230 is the Fasc. 327 key set, a different file); no DECODE record found for the Gembicki keys.",
   "tomokiyo": tomo("'Zrínyi', 'Zrinyi', 'Gembicki', 'Fasc. 296'"),
   "lasry": lasry("'Zrínyi', 'Zrinyi', 'Gembicki', 'Fasc. 296'"),
   "edition": "No edition cited in the regest; Lang 2015 lists the Zrínyi/Gembicki 1669 key at f. 77 (per the 9 Nov east-north sweep), i.e. it is known to the literature as a key.",
   "literature": "Not searched further; the regest settles that the item is a clear letter with keys."},
  "The item is itself key material: at least three cipher keys enclosed with Gembicki's letter (fol. 75-83; Lang: key at f. 77). Worth a DECODE key-record entry (decode_updates/queue.json) with this metadata.",
  "known.py: no other row for Fasc. 296; distinct from catalogue 1230 (Fasc. 327 keys).",
  "not_cipher",
  "Gembicki's letter of 4 Oct 1669 to Péter Zrínyi is a Latin original with cipher keys enclosed, not a ciphertext; it is key material for DECODE, not an open cipher.")})
