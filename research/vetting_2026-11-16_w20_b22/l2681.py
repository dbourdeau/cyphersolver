import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *
put(2681, {"verdict": "partly_read", "confidence": "medium",
 "note": "The Czernovich ('explorator/amicus secretus') series is far larger than the row says: 153 regests naming him in Türkei I Kt. 12-21 (1556-66) mention cipher or decipherment, and all but four carry a contemporary decipherment (interlinear, beside, or on a separate sheet). Of the four, two duplicates have a deciphered twin of the same date (44170 = 44171, 16 Jul 1557; 45249 = 45250, 11 Jul 1565); the residue is 45148 (14 Feb 1565, 'csak részben feloldva', only partly deciphered) and 44618 (16 Aug 1562, a duplicate 'feloldás nélkül'; 44619 of 17 Aug is deciphered but may be a different letter).",
 "access": "archive", "access_note": "Regests only on Hungaricana; HHStA Türkei I Kt. 16 Konv. 1 fol. 49-50 and Kt. 19 Konv. 3 fol. 29-30 would need a copy order.",
 "vetting": V(
  {"kind": "not online", "where": "Hungaricana Vienna-inventory search 'Czernovich' (218 regests), 'Csernovics' (8), 'Cernovich' (1); every regest read in full by script on 16 Nov 2026 (raw/cz_full.txt), e.g. archives.hungaricana.hu/en/lear/BecsSeg/44093/, 44098/, 44170/, 44171/, 44618/, 44619/, 45148/, 45249/, 45250/. No images.",
   "extent": "About 153 cipher-bearing regests 1556-66 (Kt. 12: 8, Kt. 13: 60, Kt. 14: 39, Kt. 15-21: 46), mostly Italian reports of Michael Czernovich as secret informant, then as envoy to Maximilian II (1565).",
   "cipher": "Typical wording 'olasz orig. sorközi feloldással' (interlinear decipherment), 'sifrír, mellette feloldva', 'külön feloldás'. Without decipherment: 44170 and 45249 (duplicates, deciphered twins 44171 and 45250 of the same date), 44618 (16 Aug 1562, duplicate, 'feloldás nélkül'), and 45148 (14 Feb 1565, 'sifrír, csak részben feloldva')."},
  {"decode": "known.py on 'Czernovich', 'Cernovic', 'Csernovics', 'Czernović' finds only this lead; no DECODE record named for Czernovich (the 14 Nov Hungaricana vetting also found none in DECODE or Lang's repertory).",
   "tomokiyo": tomo("'Czernovich', 'Cernovic', 'Csernovics', 'Czernović'"),
   "lasry": lasry("'Czernovich', 'Cernovic', 'Csernovics', 'Czernović'"),
   "edition": "No edition checked for the residue; the 14 Nov vetting noted a web source describing his 1562 reports as Italian with interlinear decipherment, consistent with the regests. The two residual pieces are not shown to be printed.",
   "literature": "The regests themselves settle the status of the series; no separate literature search on the two residual pieces."},
  "The ~149 interlinear pairs give Czernovich's key(s) over 1556-65; the residual partly deciphered 45148 and the duplicate 44618 would be key lookups against them. No key sheet named.",
  "The row's count (10 regests) is far too small; no overlap with other leads or catalogue entries (known.py).",
  "partly_read",
  "Nearly all of Czernovich's ciphered reports 1556-65 carry a contemporary decipherment; only the undeciphered part of 45148 (14 Feb 1565) and the duplicate 44618 (16 Aug 1562) remain, both key lookups against the many interlinear pairs.")})
