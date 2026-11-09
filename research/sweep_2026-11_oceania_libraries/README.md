# oceania_libraries sweep, 9 Nov 2026 (Australia and New Zealand holders beyond NAA)

Result: **0 candidate rows.** No Chrome (brief), no Trove key, so only public routes and web search.

## Routes
- **Worked:** DigitalNZ `api.digitalnz.org/records.json?text=...` (no key, `fields=` param). Aggregates NZ libraries,
  but returns almost only newspapers (3,600 of 3,899 unique hits for 13 terms, 5 pages each), Auckland Museum cenotaph
  records, bottles and stamps. Zero manuscripts or letters with cipher. Script: `dnz.py`, `dnz2.py`; output `dnz_hits.json`.
- **Blocked or JS-only (curl):** Trove (Anubis "Access Denied"), NLA catalogue (Anubis), SLNSW archival/search (Primo
  shell, connection reset), SLV Primo (JS shell) and SLV findingaids (403), Auckland ArchivesSpace (bot challenge page),
  Hocken recollect (403), natlib.govt.nz (redirect loop), digitalnz.org site (403), Archives NZ Archway (JS shell),
  PROV (202 empty), Tasmanian TMAG (Cloudflare), Te Papa (Next.js shell, not parsed), Auckland Libraries (406).
  These need Chrome; next sweep should go straight there for SLNSW, SLV, SLQ, SLSA, SLWA, PROV, natlib, Archway.

## Terms
DigitalNZ: "in cipher" (1 book), "in cypher", cipher/cypher/ciphered (5,853 matches, all newspapers), cryptogram (2),
"secret writing" (23), deciphered, undeciphered (38), "in code" (812), "written in code" (31), "secret code" (716),
"code letter" (32). Hits worth a glance: Otago `Charles Brasch's cipher` (a 20th-c. novel illustration, not a document).
Web searches (about 8, general web search): Mitchell Library, Turnbull, Grey Special Collections, convict diaries,
colonial governors' despatches, NZ Wars, Trove. No Australian or NZ 1788-1900 cipher letter described as undeciphered.

## Excluded
- Auckland MSS-92/1 Grey autograph letters: "Code for undetermined script" is ArchivesSpace boilerplate, not cipher.
- Turnbull ATLM-0009-24 "Letters from Unknown Writer, Camp Opotiki 1866": "difficult to decipher" means legibility.
- Yale R. Yard letter and other hits: not in the region.

## Remaining
All state library/archive catalogue term searches (cipher, cypher, "in cipher", cryptogram) are untried for lack of a
route. Needs Chrome pass: SLNSW Mitchell/Dixon catalogue, SLV, SLQ Colonial Secretary, SLSA, SLWA, PROV, Tasmania
(Libraries Tasmania Names Index/stors), natlib Tiaki, Archway, Hocken, Te Papa, Auckland Heritage.
