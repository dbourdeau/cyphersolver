# Africa and eastern-US remainder sweep (9 Nov 2026)

Result: **0 candidate rows** (`candidates.json` is `[]`), 0 key leads. Nothing was viewed on an image.

## Routes that worked
- Penn / PACSCL finding aids (`findingaids.library.upenn.edu/?q=`, plain curl, Blacklight; covers HSP, Haverford, Swarthmore, Bryn Mawr, Temple, Lehigh, Drexel, Chester Co., Germantown ...). Terms (hits): cipher 36, cypher 17, cryptogram 0, "in cipher" 36, decipher 33, "secret writing" 1. `bl_harvest.py`, `hits_library.jsonl`.
- Princeton finding aids (`findingaids.princeton.edu/?q=`, curl). cipher 44, cypher 10, "in cipher" 4, decipher 16, "in code" 110 (noise). `hits_princeton.jsonl` (title and snippet; urls carry tracking suffixes).
- UCT AtoM (`atom.lib.uct.ac.za/index.php/informationobject/browse?query=`): cipher 0, cypher 1 (Sir B. Walker papers, not opened beyond the reference code; not cipher evidence).
- `ctx.py` fetches a record and prints cipher contexts.

## Blocked or unreachable from this network
- Anubis proof-of-work: Duke (`archives.lib.duke.edu`), Massachusetts Historical Society search page is JS-only; UConn and Hagley show a challenge page. Yale 403, SOVA 403, Archives Hub 403. Not tried in Chrome (the ArchiveGrid sweep already reached Duke, Connecticut, Yale).
- No answer (connect failure): Wits Historical Papers AtoM, Cory Library, South African National Archives eAHRA / search host, UNC finding aids (404), UMass finding aids, Mission 21 archive. nationalarchives.gov.za site has no usable search (404 on search paths).
- Not reached: Cornell RMC (static page list only), UVA / Library of Virginia / Maryland State Archives / Colonial Williamsburg / Delaware / Rhode Island searches, Egypt Dar al-Kutub, AHU Lisbon, Basel Mission (baslerafrika.ch front page only), Nationaal Archief VOC Kaap (1.04.02 is inventory-level; no cipher search done).

## What the hits were, and why none became a row
- Penn Ms. Coll. 579 Torcy to Gaultier 1711-14: already a lead (known.py).
- Princeton De Coppet (C0063): Greene 1782 and Humphreys/Short 1790-91 / Barlow 1812 already leads or read; Monroe-era Paris 1796 (Box 26 f.13) and Committee of Correspondence 1778 (Box 20 f.3) carry interlinear decipherment ("with deciphering above", "deciphered"), so not unread. Grant/Stanton/Ord City Point telegrams 1865 are marked "Cipher" but are clear texts.
- Princeton Tallmadge, Beauharnais military reports 1814, Cliosophic Secret Cipher (c.1820), Rush Code or Cypher: in `research/us_societies` as key/material leads.
- Haverford Joel Cadbury 1856 and Lehigh Archibald Johnston 1912: already in the catalogue.
- Keyser "cipher book 1823" (Germantown), Gratz "Arnaut's Cipher", Ross "Cyphering Book": arithmetic ciphering books, not cryptography. Waln, Wister, Dundas, Mickley, Sharples-Paschall: no cipher text in the record.
- Most other hits: 20th-c. Bloomsbury cipher clerks, Bacon-cipher literature, a surname Cypher, Princeton Bundy "Signal Corps" noise.
- Web searches for African cipher letters (Cape, Zanzibar, Gold Coast, Abyssinia, Boer War) found only copies of War Office telegrams (Liddell Hart at KCL, Kitchener at Kew), already-solved Livingstone (faded ink, not cipher) and Biafra ciphers (cryptocellar, 1960s).

## What remains
Africa is still essentially unswept: South African archives need either their own hosts to answer (they did not) or Chrome; Basel Mission (Mission 21), Cory, Wits, Dar al-Kutub, AHU Lisbon (digitarq-style search for "cifra" with ultramar fonds) and Nationaal Archief Kaap/Elmina (WIC Elmina series) remain. East-US: Anubis-gated Duke, UConn and Hagley need a Chrome pass; UVA, LVA, Maryland, Delaware, RI, Cornell, UNC, Colonial Williamsburg were not searched. Most eastern holders were already hit through ArchiveGrid (`sweep_2026-11_us_blocked`), so expected yield is low.
