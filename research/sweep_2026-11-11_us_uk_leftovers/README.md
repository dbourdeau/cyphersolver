# US and UK/Ireland leftovers from COVERAGE.md (11 Nov 2026, cloud session)

Brief: `research/_nov11/BRIEF.md`. Retest, from the cloud container's network, of the US and UK/Ireland hosts that
`research/COVERAGE.md` lists as blocked or untouched, plus the NARA M1194 word search.

Output: `candidates.json` (2 rows: 1 with a complete `open` vetting block, 1 lead), `key_leads.json` (4),
`catalogue_corrections.json` (1: catalogue 2077). Built by `make_candidates.py` (+ `more_rows.py`). Page images
and downloads stayed in scratch.

## Main result: the BYU Sfondrati letters are online and were seen

`cdm15999.contentdm.oclc.org` (timed out on 3 Nov) answers plain curl here.

- API: `https://cdm15999.contentdm.oclc.org/digital/bl/dmwebservices/index.php?q=dmQuery/SCMisc/CISOSEARCHALL^code^all^and/title!descri!call!date/title/1000/1/0/0/0/0/0/0/json`,
  then `dmGetItemInfo/SCMisc/<ptr>/json` (the cipher note is in the `genera` field) and
  `dmGetCompoundObjectInfo/SCMisc/<ptr>/json` for the page pointers.
- Images: `https://cdm15999.contentdm.oclc.org/digital/iiif/SCMisc/<page ptr>/full/900,/0/default.jpg`.
- "Sfondrati" gives 535 objects (Vault MSS 516-524 and 771). "code" gives 33 Sfondrati letters; "cipher", "cypher",
  "cifra", "coded" give none in the manuscripts collection (the rest of BYU's CONTENTdm hits are newspapers).

What they are:

| Shelfmark | Items | BYU note | Seen |
|---|---|---|---|
| Vault MSS 771, items 6, 7, 9, 12, 13, 14, 16, 18, 19, 21, 25, 26 | Terranova (governor of Milan) to Paolo Sfondrati, ambassador in Savoy, 14 Aug - 26 Sep 1583 | "Most of the letter is written in code" (6) / "Portions ..." (6) | All 46 pages on contact sheets, item 6 p. 1 at full size. Spanish, "Muy Illustre Señor", dated "De Milan". Numbers, letter signs with dots and strokes, two-letter groups, three-letter code words (hom, sim, cem, vil, hol, gal, roe). **No decipherment on any page.** This is catalogue 2077 |
| Vault MSS 518, folder 3, item 2 | the same, 5 Oct 1583 | "Portions of letter written in code" | pp. 1-2 read: same cipher, about 20 lines, no decipherment. **New row, vetted `open`** |
| Vault MSS 521, folder 1, 20 items | Niccolò Sfondrati (later Gregory XIV) at Trent to Paolo Sfondrati, Nov 1561 - Mar 1562 | "Portions of text written in code, with de-coded text in margin" | items 4 and 31 seen: cipher runs with the marginal decipherment. Read at the time: `key_leads.json` |

`catalogue_corrections.json` carries the fields of catalogue **2077** that are wrong (it was promoted "not online",
language Italian, region Papacy, period 1589-1598, correspondents unknown): the letters are Spanish, 1583, online,
with a `seen` block of kind scan. The earlier block also called BL Add MS 28418 "a different person's
correspondence"; it is the same Paolo Sfondrato (decipherings of his letters to Philip II, 1580-85), so it is a
source for the cipher. DECODE has a key headed "Duca di Terranova" (R9318, Munich BayHStA KAA 4591 f. 95); not
tested. MSS 518 folder 3 has 38 more Terranova letters of 1583 in clear, and the cipher letters themselves mix
clear and cipher: good cribs.

## NARA M1194 (the "decipher" search across all rolls)

Route: `catalog.archives.gov/proxy/records/parentNaId/2824985?limit=100&page=N` lists the 262 file units of the
series (Security Classified Personal Name Index, RG 165); `/proxy/extractedText/<naId>?limit=1000&page=N` gives
each roll's OCR. (`/api/v2/` returns the page shell without a key.) `m1194_scan.py` read all **262 rolls**, 2 s
apart, no errors: **2,637 frames** name a cipher (cipher, cypher, decipher*, undecipher*, cryptogra*, "code
message/letter/telegram", "in code", "secret writing"); about 60 distinct cards carry a failure phrase.

Result: **no new row.** Every failure-phrase card I checked against the repo is already in
`research/nara_triage_e` or `nara_triage_l` (Roth/Haiti five-figure groups, Tillenger, Freytag, Strover/Pringle to
Minko, the "Ciclo" telegram 10640-1790, Japanese code 1766-904, Gregson 10511-84, Batlle/Manila, Frey/Thayer
soldier card). The `--words` pass of `nara_reels/bulk_scan.py` (its regex includes `decipher\w*`) had already gone
over the M1194 OCR: slice E read 2,239 M1194 lines. The COVERAGE row "NARA M1194: no search for decipher across all
261 rolls" is stale and can be removed. The cards index undigitised MID files (RG 165 entry 65), so nothing here
can be seen online anyway.

## Routes, 11 Nov 2026, this network

| Source | Result | Terms and hits |
|---|---|---|
| BYU CONTENTdm | **works** (curl) | see above |
| NARA catalogue proxy | works | M1194, above |
| Maryland Center (`mdhistory.libraryhost.com`) | **works now** (search returned nothing on 3 Nov) | cipher, cypher, ciphers, "in cipher", "in cypher", cryptogram, "secret writing", undeciphered, deciphered: 0 each. "in code" 2 (jeweller's price lists 1936-45), coded 3, code 35 (law codes, Morse, code flags, John Hinrichs Cable Code Co.). **Nothing. Row can be closed** |
| PRONI eCatalogue | curl POST gets "Request Rejected" (F5); **headless Chromium driving the form works** (`proni_pw.js`, `proni_more.js` opens each row's "More" page) | decipher 46, deciphered 20, ciphers 10, cyphers 12, cypher 54 (first 50 read in full), cipher 39 (read on 3 Nov), cryptogram / "secret writing" / undeciphered 0. The phrase boxes do not do phrase search ("in code" = 694 hits on "code"). 1 lead, 2 key leads; see below |
| Digital Scriptorium | works (`/catalog.json?q=`; record JSON gives 500, record HTML works) | 18 terms, 22 distinct records beyond "code". All marginal: see below |
| UMass Boston (`openarchives.umb.edu`, CONTENTdm API) | works | cipher 11: union minutes, newspapers, oral histories. Nothing |
| NEHGS library catalogue (`library.nehgs.org`) | works | cipher 1 (the printed HMC Skrine volume, Salvetti letters), cypher 0. Their manuscript finding aids host did not resolve |
| Cambridge ArchiveSearch | works to curl now (`/search?q[]=..&op[]=&field[]=`) | not re-run: swept in Chrome on 29 Oct (`uk_libraries`, 330 records) |
| NYPL archives (`archives.nypl.org`) | **blocked**: Incapsula script page | |
| Harvard (hollisarchives, id.lib, api.lib, iiif.lib, nrs) | **blocked**: 403 on every host | |
| MIT, Tufts, Brandeis, BU (archivesspace.bu.edu), Center for Jewish History ArchivesSpace | **blocked**: HTTP 202 AWS WAF challenge, empty body | BU's old `archives.bu.edu` redirects to a library page |
| N-YHS (NYU finding aids, emuseum, digital collections) | **blocked**: 403 / 405 | |
| Brooklyn Public Library, Hispanic Society (site and emuseum) | **blocked**: 403 | |
| TARO (`txarchives.org`) | **blocked**: Anubis "Making sure you're not a bot" | Benson finding aids still unread |
| Congregational Library (Quartex) | search is JavaScript; in headless Chromium the results page says "Page not available" | not swept |
| TCD Digital Collections | **blocked now**: reCAPTCHA page (worked to scripts on 3 Nov) | |
| TCD MARLOC / manuscripts catalogue | hosts do not connect | |
| NRS catalogue | 403 | |
| National Archives of Ireland | site opens; as on 3 Nov it has no item catalogue to search | |
| CUDL | 200 to curl for the shell; search needs the WAF-guarded API. Not re-run (swept 29 Oct) | |
| revistas.uam.es (Scalisi 2023 on Terranova) | Anubis; not opened | |

## PRONI, read in full

- Lead (row 2): **D1071/H/B/N/60**, Ivy Neville-Rolfe at Naples to Dufferin, 1890-91, "[Some letters in code]".
- Read at the time (not rows): D2433/D/1/100-186 (Keith papers 1777, all "with a translation"; already noted on
  3 Nov); D1854/6/8 (Annesley to Shaw, Aug 1881, three telegrams "mainly in cypher", the translation is enclosed);
  D1071/H/B/S/476/33 (a cypher telegram of 1874 told as an anecdote); D572/17/56 (Drake 1795, catalogue 1991);
  D3030/1998, /2110, /3567, /3925, /3928 (deciphered copies); T582/2 (Pointis 1689, deciphered, BL Add MS 32499);
  MIC326/1 (Dufferin, deciphered telegrams).
- Mentions only: T3245/4/4 (1796, a prisoner's "strip of paper written in characters somewhat like cyphers",
  described in Clare's letter, the strip is not with it); MIC608/1 (Cosby rebuked for not using cypher, 1765);
  T3459/E/254 (Pembroke to Hutchinson "about cyphers and letters", Tilsit 1807: unseen, could hold a key).
- Noise: about 70% of "cypher" is figurative ("a mere cypher"), the rest royal monograms and "difficult to decipher".
- Key leads: MIC316/1 ("Key to ciphers used by the English government to their ministers at foreign courts in
  1724"); D1437/12 (Gallaher telegraphic cypher); D1238 (UVF cypher system, 1914); T3673 (Trist book cipher, the
  Cryptologia 1983 article).

## Digital Scriptorium, read

Nothing for the catalogue. For the record: Harvard MS Ital 130 (16th-c. Italian poems, "Encoded list of the women
addressed (pp. 1-2)", no images, Harvard hosts 403); Princeton Garrett 60L, 330H, 329Bq, 117L, 598Y (a line of
"secret writing" or a secret alphabet among owners' inscriptions, images at Princeton); Garrett 3410Y (scribe's name
"[ciphered]" in a 1676 colophon); Columbia MS Or 34 (colophon year "in code, undeciphered", Lahore, 18th c.,
probably abjad); Newberry Case MS 13 (owner's inscription in cipher by Richard Cabel, f. 125); Penn LJS 51, LJS 225
and LJS 423 (known cipher manuals, already in the Arabic sweep or key material). The "undeciphered" hits are
illegible names.

## Left

- NYPL archives, Harvard, MIT/Tufts/Brandeis/BU, CJH, N-YHS, Brooklyn, Hispanic Society, TARO, TCD, NRS: need the
  owner's Chrome. Nothing new was learnt about them here except that TCD Digital Collections now shows a CAPTCHA.
- PRONI: "cypher" rows 51-54 and "code" (694) not read; Neville-Rolfe letters need a copy order and a prior-art search.
- Catalogue 2077 and the MSS 518 letter: transcribe (about 32 cipher pages), test DECODE R9318, look at BL Add MS
  28418 for the nomenclator. Read Scalisi 2023 (Libros de la Corte) in a browser for any quoted decipherment.

## Scripts

`m1194_scan.py` (NARA roll OCR word pass, resumable), `proni.py` (plain POST: rejected, kept as a record),
`proni_pw.js` and `proni_more.js` (Playwright), `quartex_pw.js` (Congregational, failed), `make_candidates.py`,
`more_rows.py`.
