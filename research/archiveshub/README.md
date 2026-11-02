# Archives Hub sweep (2 Nov 2026)

Scope: archiveshub.jisc.ac.uk, cipher/cypher/code material before about 1950. `candidates.json` holds 6 rows
(built by `make_candidates.py`, hand-written from the hits; none viewed on an image).

## Method

- The Hub sat behind a Cloudflare check for scripts and the in-app browser. With the check cleared in the user's Chrome,
  the Hub works from Claude in Chrome with a tab of our own. A search page fetched from inside that tab
  (`fetch('/search/?terms=...&page=N')`, DOM-parsed, 20 hits per page, `sort=date.asc`; the `limit` parameter is ignored)
  worked without any new challenge. About 0.5 s between requests; no CAPTCHA appeared.
- The hit list is component-level (`ul.results > li.hit`): title, date, reference, repository. A component's own page is
  `/search/archives/<collection-uuid>?component=<uuid>`; the stable address is `archiveshub.jisc.ac.uk/data/<ref-slug>`.
- 84 distinct queries (cipher, cypher, ciphers, ciphered, decipher/decypher variants, "in cipher", "in cypher",
  "code letters", cryptogram, cryptography, secret writing, code book, coded, encoded, invisible ink, nomenclator,
  Walsingham, Thurloe, Jacobite, Cecil, and phrase variants). Many phrase queries return 0 to 7 hits: the Hub's phrase search
  is strict, so the single words `cipher` (about 440 hits) and `cypher` (about 50) carry the sweep.
- About 1,280 distinct hits were pulled and filtered locally on year < 1951 plus a cipher word in the title; the Hub
  collections matched in their full text were opened for the context of the word (Senate House MS300, Loseley, Talbot,
  Bray/Nicholas, Brodrick, Aske, Elphinstone, Howard, Frankland and the like: all noise, cipher word in a biography
  or "decipher" of handwriting).

## What it found

The Hub is overwhelmingly 20th-century (Auchinleck cipher messages 1941-47, Golden Dawn "Cipher Manuscript" ritual
(Hebrew cipher; Westcott's translation), India Office cypher-clerk files, Bletchley personal papers, telegraph code books).
Pre-1800 diplomatic cipher is almost absent: **Hatfield, Longleat, Lambeth Palace and the Cecil and Walsingham
papers are not on the Hub at the item level** (searches for "Hatfield cipher", "Longleat cipher", "Lambeth cipher" return 0).
The Hub does not list Lambeth item-level cipher letters; `Walsingham` and `Thurloe` hit only collection descriptions.

Candidates (6): Clive/Watts Plassey letters 1757 (BL Mss Eur G37), Francis to Clive, CUL MS Add.110 law reports
in cipher, Hotham papers (Reichenbach's cypher, c. 1730), Rastrick private cipher, Mackinnon telegrams in code.

## Excluded, with reason

- **Henry VIII to Gardiner and Knyvet, Ratisbon, 17 June 1541** (Borthwick CMAY/6/1/1): cipher, but "Pd. with facsimile,
  deciphered and ed. by Christine J. Black and C.E. Challis (York, 1968)": already read in print.
- Clive Mss Eur G37/8/4 ff.70-72 (Select Committee to Clive, 23 Jun 1757): decryption attached.
- Golden Dawn "Cipher Manuscripts" (Museum of Freemasonry GD/1/1, c. 1870-85, Trithemius-type cipher, Westcott read it in 1887); 
  twentieth century material (Auchinleck, Ramsay MacDonald telegram decypher 1935, Swire 1942, Burma Office, India Office).
- Telegraph code books (African Lakes Corporation, Dundee, Crossley, Baxter, Alec-Smith "Codliver Code"): commercial
  codes, no ciphertext.
- Noise: ship "Cypher" (Swansea), oak "cyphers" (timber), royal cypher monograms, "cryptic" cards, "decipher" of handwriting.

## Key leads (keys or key-like items without ciphertext)

- Chatsworth CS1/5.0: "Cipher devised by Henry Wriothesley, 3rd Earl of Southampton", c. 1590, 1 sheet.
- Senate House MS 289 (c. 1850): copy of a cypher used for a letter of Queen Elizabeth to Nicholas Throckmorton, 1 July 1559.
- BL Mss Eur G37/7/20 ff.1-13: Clive's lists of cyphers 1757 (with the candidate above).
- SOAS PP MS 14/002/069/084: Charles Addis on cyphers in London telegrams, 1897.
- Orkney D1/431: Cypher log, HMS Royal Oak, 1939 (naval, out of scope).

## Blocked or not done

- Nothing blocked in this pass. No CAPTCHA. Tab 1987532794 was opened for this sweep and closed afterwards.
- Not done: viewing any image; the literature and web check for each candidate (the `prior_art` fields say so);
  expanding the Clive hit to every ciphered item of the Mss Eur G37 file (only the items the Hub returned were read).
- merge.py's `SWEEPS` list did not include this folder, so `archiveshub` was added there (one-line edit). Dry run:
  `archiveshub: 6 rows, 6 new`.
