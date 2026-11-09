# oceania_chrome sweep, 9 Nov 2026 (Chrome pass over the sources blocked to scripts in oceania_libraries)

Result: **0 candidate rows.** No Australian or NZ 1788-1900 letter or diary with an undeciphered cipher passage found.

## Routes
- **Worked (Chrome):** Trove web search, category "Diaries, Letters & Archives" (`trove.nla.gov.au/search/category/correspondence?keyword=...&sortBy=dateAsc`).
  Anubis check cleared by itself in about 10 s; results render only after a further 8-10 s wait. This one route aggregates SLNSW,
  SLV, SLSA, SLWA, NLA, Libraries Tasmania, QLD State Archives, AJCP. Clicking a result (not reading link hrefs: the JS tool
  blocks query-string URLs) opens the work record.
- **PROV** (`prov.vic.gov.au/search_journey/select?keywords=`): works; "cipher" 0, "cypher" 7 (all people/passenger names).
- **Blocked in Chrome:** SLNSW `collection.sl.nsw.gov.au` ("Human Verification", needs a click; not cleared, left), natlib.govt.nz
  (Imperva "Error 15"), Archives NZ `collections.archives.govt.nz` ("security check" page, did not clear in 20 s).
  SLQ OneSearch (`onesearch.slq.qld.gov.au/nde/search`) renders and text can be read with `document.body.innerText`, but a
  query for "in cipher" returns only journal articles and books (Rohonc, Qur'an in cipher, etc.), no manuscripts.
- **Not tried:** SLV findingaids, SLSA, SLWA native catalogues, Tasmanian Archives native, Hocken, Auckland Heritage, Te Papa
  (Trove already surfaces SLV/SLSA/SLWA/Libraries Tas items; the NZ native catalogues are the remaining gap, all behind
  bot checks that did not clear).

## Terms (Trove, correspondence category, hit counts)
"in cipher" 46; cypher 415; cipher 365; cryptogram 24; "secret writing" 9; decipher/deciphered/undeciphered 359.
Read in full: first pages of cypher (earliest first), cipher (earliest first), "secret writing", decipher (earliest first).

## Excluded
- Wellington to Sir Home Popham 1812, partly in cipher (SLV): "interlinear translation" given, already deciphered.
- Flinders letters to Capt. Jacques Bergeret/Pellew 1806-08 (SLNSW Safe 1/56, subject tag "Ciphers"): Flinders' own letterbook
  copies in English; tag not seen with any ciphertext. SLNSW record page blocked, so not opened.
- John Ussher to J. S. McCord, Montreal 1829 (Kassler papers, NLA MS 10371 item 309): music-symbol rebus letter, content
  summarised (dinner invitation), not a cipher puzzle.
- Burr Conspiracy collection (US material, "some material in cipher", Library of Congress microfilm): outside the region.
- Many "ciphering book" (arithmetic), telegraph-code, Colonial Office cypher administration, Monash/Menzies papers, "undeciphered
  addressee" (illegible name) hits.
- Tasmania Convict Department "Code of Signals" 1844/1860, Sydney Railway Company telegraph cipher 1848-55: signal/telegraph
  code lists, not letters.

## Remaining
SLNSW native catalogue (needs a human to pass the verification), natlib/Turnbull, Archives NZ, Hocken, Te Papa and Auckland
Heritage are still untested for lack of a route. Prior: Australia/NZ holdings of pre-1900 cipher letters look sparse.
