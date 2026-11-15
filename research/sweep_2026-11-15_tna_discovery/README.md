# TNA Discovery item-level cipher sweep (15 Nov 2026)

Output: `candidates.json` (**25 rows**, built by `make_candidates.py`, schema as the other 2026-11 sweeps; every region and
period is in merge.py's lists) and `key_leads.json` (9 bare-key groups). Nothing was merged, committed or edited in
`catalogue.json` / `leads.json`. Source key for a later merge: `tna_discovery_items` (not yet in merge.py's SWEEPS).

**Big raw files, keep out of git** (add a `.gitignore` rule or leave untracked): `raw.json`, `raw2.json`, `kept.json`,
`kept_tna.json`, `kept_tna_flag.json`, `review1-3.txt`, `sel*.txt`, `sib.txt`, `new2.txt`, `kerguelen.json`, `bho.html`.
The archive.org calendar OCR (about 270 volumes, 650 MB) was kept in the session scratchpad, not in the repo.

## Method

- **Discovery API** (`/API/search/records`, curl through `research/tna_discovery/tna.py`, 1 request per second, no block, no
  bot check, Chrome not needed). Pass 1 (`harvest.py`): one OR query (cipher, cypher, ciphers, "in cipher", "in cypher",
  ciphered, cyphered, deciphered, decypher, "cypher key", "key to the cipher", "in cyphers", cryptogram) per department
  (SP, FO, CO, WO, ADM, PRO, HO via `sps.departments`) and date window (25-year windows 1485-1699, 10-year windows
  1700-1919): 2,058 records, only 20 of them not in the 28 Oct / 2 Nov pools (all 1906-19 telegram administration).
  Pass 2 (`harvest2.py`): 36 more phrases (en chiffre, enciphered, "letter in cypher", "in characters", "in figures",
  interlinear, undeciphered, "invisible ink", ...) over 8 windows, no department filter: 1,092 records, 116 new to the pool
  and 15 usable (the Kerguelen letters, SP 87/24/89, SP 78/250/136, the Kitchener decodes).
- **Pool review.** The three pools (28 Oct `hits.jsonl`, 2 Nov `raw.json`, these two passes; 19,665 records) were filtered
  with `research/tna_discovery/filt.py` (drops royal cyphers, decipherment attached, etc.): 1,773 pre-1920 records, 1,086 at
  TNA. Each was flagged by exact reference and by volume against `known.py`'s corpus (`pool.py`): 667 are in neither, and
  those were read (`review2.txt`, `review3.txt`). Most are mentions of cipher telegrams (FO, CO, ADM 137 1914-18), not ciphertexts.
- **Calendar of State Papers.** `ia_list.py` found 662 archive.org items; the 351 domestic, foreign, Ireland, Scotland,
  Spanish and Venetian volumes were downloaded as `_djvu.txt` (273 at the time of the cut, the rest failing or still
  running). Paragraphs with "cipher/cypher" gave 3,606 hits (2,360 without a decipherment note); the narrower pattern
  "undeciphered / not deciphered / unknown cypher" gave 222 passages. Almost all of those are already catalogue or lead
  rows (Moody/Bristowe, Fowler, Fontenay, Roquet, Pickering/Morysine, Norton/Lee, Dr Walles, the 1655-59 royalist
  Nicholas/de Marces/Pile/Du Chastel letters, the Dumbarton 1571 intercept), so they were not repeated. Five were new:
  the last five rows. British History Online search is behind a challenge page (redirect to `/challenge`); BHO volume pages
  were not needed.
- **Dedupe.** `known.py` on shelfmark and names for every kept row; the removal file is searched by `known.py`.
  One key per entry: families with several correspondents were split or left to the one writer (see the Kerguelen and
  Raby rows, which each have a single correspondent pair).

## Result

25 rows: 7 pairs (ciphertext with a decipher or decode beside it: SP 87/2/49 and /51, ADM 1/1948/97, ADM 1/1665/176,
SP 46/146 Kerguelen, SP 32/14/51 extract, CSP Chas II 1663 nos. 17-18), the rest single ciphertexts with no decipher named.
Best by solvability or interest: ADM 1/1808/193 (three captured Batavia 1811 numerical-cipher letters, a sibling key
family in targets/batavia1800), SP 87/2/49 and /51 (Marlborough, interlinear decode), ADM 1/1948/97 (Hillyar 1813 pair),
SP 46/146 (Kerguelen), SP 54/41/27 (Gleneves code names with a partial key), PRO 30/24/7/505 (Shaftesbury 1682),
SP 46/97 f. 47 (Beverning 1653, sibling of targets/thurloe), the CSP Williams-Digby 1644 cipher letter, the Thorne-Lawrence
1663 pair.

## What the Discovery pool is

Discovery describes a cipher letter in a sentence, so the item-level catalogue is thin: FO, CO and WO items name cipher
telegrams as administration, not as ciphertext, and nothing before 1900 appears in them. The strong pre-1920 records are
concentrated in SP 87, SP 91, SP 105 (Whitworth, Stepney, Marlborough, Clavering/Prince Ferdinand), SP 35/36 (Atterbury, Newcastle),
PRO 30/11, 30/55, 30/57 and ADM 1 (captains' letters). Two further families were not turned into rows:

- **SP 87/37-45 (Holdernesse, Bute, Prince Ferdinand, Clavering 1760-63), about 90 "partly/mainly in cipher" letters.** The
  28 Oct sweep recorded that deciphers are written over them in the volumes, so they are solved at the time; not repeated.
- **Already tracked:** PRO 30/57/4 Kitchener (lead 1159), PRO 30/11 Cornwallis and PRO 30/55 Carleton (leads and catalogue),
  SP 91/5-6 Whitworth, SP 84/165, SP 105/60/121, SP 35/45-53 Atterbury (catalogue 860), SP 36/66 and SP 54/25, SP 55/13 Maclean
  letters, SP 95/136.

## Blocks and gaps

- No Discovery block; the API answered every request. British History Online search needs a challenge (not tried in Chrome;
  the calendars came from archive.org instead). About 80 of the 351 archive.org volumes failed or were not fetched at the
  cut (HTTP 500 stubs), so the CSP part is not exhaustive; the Venetian and Spanish volumes were barely reached.
- No image was seen for any row; none of the TNA State Papers pieces is digitised on Discovery (State Papers Online is paywalled).
- Calendar-derived rows give the SP number only where the calendar prints it; the others carry the printed volume number and a
  "not verified" note.
- Not done: item-level hunts inside WO 1, WO 32, FO 27 and CO 5 (colonial and army despatches), which Discovery describes
  by folio ranges without cipher words; CO 5 would need a per-volume approach.
