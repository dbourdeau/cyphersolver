import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *
put(2785, {"verdict": "read", "confidence": "high",
 "note": "TNA's own description says both enciphered reports (ff. 251-252 and 253-254, not only 251-252) were 'deciphered at the Admiralty' and paraphrases the deciphered text at length; the plaintext is on file with the ciphertext.",
 "access": "archive", "access_note": "Not digitised on Discovery (digitised: false); ADM 1 is a Kew item.",
 "vetting": V(
  {"kind": "not online", "where": "TNA Discovery API record C12820601 (ADM 1/1948/97), read by script 16 Nov 2026 (raw/tna_C12820601.json): scope note for ff. 249-263.",
   "extent": "Two enciphered reports of Captain James Hillyar, HMS Phoebe: ff. 251-252 (entries 16 Jul - 14 Oct 1813) and ff. 253-254 (Guayaquil and Lima, late 1813), enclosures to his letter of 12 Jun 1813 (ff. 249-250).",
   "cipher": "The catalogue calls each an 'Enciphered report ... which has been deciphered at the Admiralty' and summarises the decipherment in detail (rendezvous at Juan Fernandez, Cocos Island; the Essex seen off Lima)."},
  {"decode": "known.py on 'Hillyar', 'ADM 1/1948', 'Phoebe', 'Essex' finds only this lead; no DECODE record for these reports.",
   "tomokiyo": tomo("'Hillyar', 'ADM 1/1948', 'Phoebe', 'Essex'"),
   "lasry": lasry("'Hillyar', 'ADM 1/1948', 'Phoebe', 'Essex'"),
   "edition": "No printed edition sought: the Admiralty decipherment on file, summarised in the TNA catalogue, already gives the plaintext.",
   "literature": "Not searched further; the decipherment filed with the piece settles the status."},
  "The cipher key is not named; the Admiralty decipher pairs with the ciphertext and would let a key be rebuilt, but nothing is left unread.",
  "known.py: no other row; ADM 1/1665/176 (lead 2786) is a separate 1813 Admiralty cipher letter.",
  "read",
  "Both enciphered Hillyar reports in ADM 1/1948/97 were deciphered at the Admiralty and the decipherment is filed and summarised in TNA's catalogue, so the text is read.")})
put(2786, {"verdict": "read", "confidence": "high",
 "note": "TNA's description of ADM 1/1665/176 (ff. 518-519) is 'Written in cypher code and decrypted': the decryption is part of the piece.",
 "access": "archive", "access_note": "Not digitised on Discovery (digitised: false); Kew item.",
 "vetting": V(
  {"kind": "not online", "where": "TNA Discovery API record C18550506 (ADM 1/1665/176, 4 Nov 1813), read by script 16 Nov 2026 (raw/tna_C18550506.json).",
   "extent": "Two folios (ff. 518-519): a letter of Captain Philip Carteret, HMS Pomone, off Cape Finisterre.",
   "cipher": "Catalogue: 'Written in cypher code and decrypted'. The ciphertext and its decryption are described together on these two folios."},
  {"decode": "known.py on 'Carteret', 'ADM 1/1665', 'Pomone' finds only this lead; no DECODE record.",
   "tomokiyo": tomo("'Carteret', 'ADM 1/1665', 'Pomone'"),
   "lasry": lasry("'Carteret', 'ADM 1/1665', 'Pomone'"),
   "edition": "No printed text sought: the archive describes the letter as decrypted on file.",
   "literature": "Not searched further; the filed decryption settles the status."},
  "No key named; the decryption on the leaves would give it.",
  "known.py: no duplicate; ADM 1/1948/97 (lead 2785) is a separate 1813 cipher.",
  "read",
  "TNA describes ADM 1/1665/176 as written in cipher and decrypted, so the decryption is filed with the letter.")})
put(2787, {"verdict": None, "confidence": "low",
 "note": "Not assessed to a verdict. TNA's description (C12835255) gives ff. 316-321 as a 'Letter (in code)' of 15 May 1799 and ff. 306-313 as Osborn forwarding 'extracts of a letter (which is in code)' of Rainier; it does not say whether the extracts are the coded text or a decoding, whether 'code' is a cipher or a naval signal code, nor what the two East India House papers (ff. 314-315) are. Needs an image of ADM 1/2253 ff. 306-321 (Kew only).",
 "access": "archive", "access_note": "Not digitised; ADM 1 is not in State Papers Online; Kew reading room or a copy order."})
