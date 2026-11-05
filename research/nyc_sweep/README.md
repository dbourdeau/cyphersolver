# New York City archives (4 Nov 2026)

Question that started it: have we scanned archives in New York City? Before this pass: only indirectly. The Morgan, the
New-York Historical Society (N-YHS) and NYPL rows in `research/leads.json` came from ArchiveGrid and DPLA descriptions
(`sweep_2026-11_us_blocked`, `dpla_smithsonian`, `chi_riverbank`). No NYC catalogue had been searched directly.
Run in Claude in Chrome; the owner cleared each Cloudflare / WAF check, Claude clicked none.

## Morgan Library: CORSAIR works, the record pages add nothing

- `themorgan.org/literary-historical/<bibId>` opens after the check but repeats the ArchiveGrid description: call number,
  provenance, "3 p." No images, no notes beyond what ArchiveGrid had. Mary of Guise (bib 124981, MA 1346-177) is a
  description only. **No scan of any Morgan cipher letter is online** on these pages.
- **CORSAIR** (`corsair.themorgan.org/vwebv/search?searchArg=<term>&searchCode=GKEY^*&searchType=0&recCount=100`) is the
  Morgan's own catalogue and searches by keyword. "cipher" 148 records, "cypher" 48 more, "cryptogram" 10: 206 records, about
  45 of them manuscript letters. The rest are printed books, bindings and medieval folio records (noise).
  `holdingsInfo?bibId=<id>` gives the full record with Summary and Notes.
- **Cloudflare re-challenges after 2 to 4 requests.** An in-page `fetch` is challenged at once; `navigate` with 6 s between pages
  gets through a few more. Not run for lack of a clear tab: "chiffre", "cifra", "decipher", "in code".

### Morgan hits read on the record page (new beyond the 15 NYC leads)

| bib | Item | Verdict |
|---|---|---|
| 102337 | Grant to Sherman, 16 July 1864 | "Cipher" written top left: a telegram draft, clear text. Noise |
| 137632 | Seward to Thurlow Weed, 11 Oct 1864 | Annotation "Cipher" only; printed in Raymond. Noise |
| 126372 | W. Vans Murray to Gerry, 2 Nov 1797 | Says he sent no cipher. XYZ-affair set (MA 0157). Noise |
| 193594 | Maria Theresa to d'Aznares, 1861-63 | Adherents "designated in cipher" in the plain text; no ciphertext. Noise |
| 194958 | Marradas drafts, Vienna 1618-19 (Spear 176) | Drafts "some decoded from cipher"; a decipherment may be in the item. Spear gift 1985. Weak lead, not added |
| 128623 | Chase to Wheeler, 1783 | Matched on "cypher" in a long text; not cipher. Noise |

### Not read (bib ids kept): 118269 Sunderland to Bulstrode 1684 (check fired), 340340 Collings 1780, 79958 Kemble diary 1830-31,
415166 Coleridge 1812, 105545 Guicciardini 1513, 265325 Federico da Montefeltro 1478, 201066 Marlborough to Eugene 1711,
103655 Henry III to Mme de Montaigu, 130292 Beaton 1575, 120222 Webbe, 391215 Murray/Pulteney. Carroll's cipher poem,
cipher alphabets and alphabet-cipher (MA 6387, Houghton 352150) are well known. The King/Pickering XYZ letters (MA 0157) and
Lake/Webbe/Rawdon overlap leads 2074/2075.

## N-YHS and Center for Brooklyn History (NYU host)

- `findingaids.library.nyu.edu/nyhs/` (the bare root) answers `AccessDenied`, but collection pages
  (`/nyhs/<call-no-slug>/`, `/cbh/<id>/all/`) open in Chrome once the check is cleared.
- `specialcollections.library.nyu.edu/search/?q=<term>&per_page=100` shows an AWS WAF "Let's confirm you are human" page with a
  **Begin** button the first time; the owner pressed it and the search then worked for the rest of the pass. It covers N-YHS,
  Center for Brooklyn History, Fales, NYU Archives, Tamiment. The search stems: "cypher" gives the same 19 as "cipher".
  "cryptogram" none; the "in code / coded / cryptographic / secret writing" OR-query gave 5, all coding sheets (noise).
- **Result: 19 hits, almost all noise.** Real items: Beauregard's fan cipher with a worked sample (Chisolm papers, MS 670.5
  box 3; a key, not a text); Hitt's *Manual for the Solution of Military Ciphers* (1916, 7th Regiment); Brown Brothers cipher for
  partner names (1894); Philip Hamilton Hill diaries "Codes" (MS 3052, box 1 folder 4, not read); Pendleton Papers series VI
  (Hamilton, 1793-1813, matched inside, not read); and one lead:
- **Robert R. Livingston at Paris to his brother, 1803**, Louisiana-purchase negotiations, "partly in cipher handwriting"
  (Center for Brooklyn History, Mid-Atlantic early manuscripts collection 1974.002, box 1 folder 25; gift of Dr A. S. Hunt).
  The wording is ambiguous (cipher or cursive); Livingston's State Department cipher is known. Not added as a lead yet.

## Columbia (findingaids.library.columbia.edu)

Search works in Chrome with no check: `/archives?q=<term>&search_field=all_fields&per_page=100` (the old `/search` URL is a 404).
"cipher" 16 entries, "cypher" 24, "cryptogram" 1; most are novels, scores and surnames (Cypher). Real items, all Rare Book &
Manuscript Library, none digitised on the page and none read:

| Collection | Item | Note |
|---|---|---|
| Gouverneur Morris papers, 1768-1816 | Duportail 1794, transcription in Morris's hand of a cypher message sent through Thomas Pinckney (4 p.); Pinckney notes of May 1794 and 23 Aug 1794 "enclosing message in cypher"; Morris to Jay, Philadelphia, 1 Jan 1783 "and copy, partly in cypher"; Robert Morris 8 Aug 1790 "transcription ... of letter orig. in cypher" | Morris as minister in Paris 1792-94. Best group here: some items carry a decipherment, the 1794 ones may not. Papers of John Jay and Morris's *Diary of the French Revolution* to check |
| Henry White papers, 1876-1925 | John Hay to White: 4 telegrams in cypher, 15 Aug-13 Sep 1901; letter in cypher, 19 Apr 1902 | State Department code; likely in FRUS or White's decipherments. Low |
| Iosif Loris-Melikov papers | "Diplomatic Ciphers, 1914-1916" | Russian, key material. Not seen |
| (unnamed) | "Russian Consulate Key, 1920" | A bound booklet, the key to a cipher. Worth a look as key material |
| William J. Donovan papers, 1775-1790 | "Photostats of ciphers used for secret service" (research files) | Revolutionary-era ciphers copied by Donovan; origin unknown |
| Edward Morse Shepard papers | "Account Books Cipher Books" | Probably arithmetic "cipher books" (noise) |
| V. K. Wellington Koo; Liu-Chiang; Tsuyee Pei | Chinese telegraphic code books (printed) | Printed codebooks, not texts |

## Vetting and leads (4 Nov 2026)

`make_candidates.py` builds `candidates.json`; `research/archive_sweep_2026-10/merge.py --write` merged it (`nyc_sweep` added to
its sweep list); `apply_vetting.py` wrote the vetting blocks. Two leads, both `access: archive`, verdict `open`:

- **2249 Duportail to Gouverneur Morris, 1794, via Thomas Pinckney** (Columbia RBML, Morris papers Box 3, items 241, 1094,
  1099). Item 241 is Morris's transcription plus the cypher message itself, 4 p.; 1094 and 1099 each enclose a message in cypher.
  No edition or study found; the Morris diaries have a gap from Jan 1793 to Oct 1794. `_check_catalogue.py --lead 2249`: ready
  to promote. Whether Morris's "transcription" is cipher groups or a decipherment is the open question for the scan.
- **2250 Livingston to his brother, Paris 1803** (Brooklyn History 1974.002 box 1 f. 25). Weak: "partly in cipher handwriting"
  may mean cursive.

**Closed on the prior-art check, left out:** Gouverneur Morris to Jay, 1 Jan 1783 (printed with its decipherment in the Papers
of John Jay, Founders Online: Office of Finance Cypher No. 1, WE006; the Jay file copy is at Columbia); Robert Morris 8 Aug 1790
(Morris's transcription of the decoded text); Hay to White 1901-02 (State Department code; the 1903-04 telegrams are lead 1436);
"Russian Consulate Key, 1920" (already cited in the catalogue's RG 64 entry). Not taken up: Loris-Melikov "Diplomatic
Ciphers 1914-1916" (key material, unseen) and Donovan's "Photostats of ciphers used for secret service" (origin unknown).

## Still open

The NYPL archives catalogue (`archives.nypl.org`, Manuscripts and Archives Division), Hispanic Society, Center for Jewish
History, Brooklyn Public Library, Columbia terms beyond cipher/cypher/cryptogram ("in code", "secret writing", "chiffre",
"cifra"), the remaining Morgan terms and the unread Morgan bib ids above, and the unread N-YHS items (Hill diaries, Pendleton).
Nothing here is merged into `research/leads.json`; the Gouverneur Morris cypher items and the Livingston 1803 letter are the
candidates to vet first.
