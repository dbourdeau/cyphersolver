# TNA State Papers sweep (2 Nov 2026)

Source key `tna_state_papers`. Scope: State Papers Foreign and Domestic units in TNA Discovery whose description names a
cipher or cypher and gives no decipherment: SP 78, 84, 89, 92, 98, 104, 105, 106 first, then the other SP series.
Output: `candidates.json` (**31 rows**, built by `make_candidates.py`). Short of the 60 asked for: the source does not hold
more, and I did not pad it.

## Method

- Discovery's open JSON API (`research/tna_discovery/tna.py`, curl, one request every 2.5 s). No login, no bot check met,
  nothing solved or clicked through. Chrome was not needed.
- Three passes over the same catalogue: (1) the 15,121-record harvest of 28 Oct (`research/tna_discovery/hits.jsonl`),
  filtered locally to pre-1900 State Papers (1,348 records) and then to descriptions with "in cipher / undecoded / partly in
  cipher" and no "deciphered" (248 strong, 314 weaker mentions); (2) `harvest.py` here, a series-limited harvest with
  `sps.recordSeries` over 28 SP series x 9 terms (`raw.json`, 794 records, 11 not in the 28 Oct set, 5 of them usable);
  (3) 14 extra phrase queries ("undecoded cipher", "undecyphered", "in numerical cipher" ...), which added only five SP 84/165
  folios already covered by a catalogue entry.
- The pool is exhausted: a third independent pass adds nothing. The 28 Oct sweeps (`research/uk_tna`,
  `research/tna_discovery`) had already taken the best items, and `known.py` shows 100+ of the strong hits as existing leads or
  catalogue entries (SP 84/165 undecoded folios, SP 91/5-6 Whitworth, SP 35/45-53 Atterbury, SP 36/66 Blair letters,
  SP 78/111, SP 77/32/289, SP 99/24/251, SP 78/114, SP 34/10, SP 54/25-26, SP 105/60/121).
- Each row was checked with `research/archive_sweep_2026-10/known.py` (it searches the removal file too) on shelfmark and,
  where distinctive, on the correspondent. Rows keep the shelfmark and a Discovery link; none was viewed (no State Papers
  leaf is digitised on Discovery).

## What the 31 rows are

Individual letters or small groups with a cipher passage and no decipherment named: Walpole's Paris despatches of 1723
(undecoded paragraphs), Marlborough-era number-cipher letters (SP 87/4/133 with an extract as crib), Robinson/Hyndford/Villiers 1742,
the Lisbon series (Southwell 1666, Parry 1672, Methuen 1698, Worsley 1715), Danish and Hanoverian items in SP 8, a Forty-Five stray
near Leeds (SP 36/73/2 f. 125), Champigny's TNA copy (SP 42/27/73), and a few singletons. Best by solvability: SP 87/30/5 (twin
deciphered at f. 4), SP 87/4/133, SP 78/179/128 and /169, SP 87/8/65, SP 78/271/11, SP 36/73/2/125.

## Not rows (and why)

- **Decipherment on the leaf or in the volume:** SP 35/49/6, 35/50/23B, 35/53/17 (decypher in French written over); SP 36/73/3/71;
  SP 54/19/98B, 54/26/125; SP 87/36-45 Prince Ferdinand and Bute letters (read at the time); SP 94 and SP 97 "and decipher" items
  (Hopton, Taylor, Harborne, Barton, Roe) which carry a decipher by their own description.
- **Keys and instructions, not ciphertexts:** the whole of SP 106 (cipher/decipher sheets 1558-1759), SP 35/36, /37, /39, /40, /71,
  /73 key copies, SP 78 cipher distribution notes 1725-1773, SP 89/59, SP 90 and SP 91 "new cypher" notes. They are key leads;
  see `research/uk_tna/README.md`.
- **Mentions without a ciphertext:** letters that say a cipher letter was sent or received (SP 36/18/45, 36/22/53, 36/37/44,
  89/33/54, 91/13/276 ...), cypher-clerk appointments (SP 37), arithmetic or "a mere cipher" (SP 46/35, 78/287/46).
- **Foreign Office codebooks and telegrams** (FO 78, 335, 800): administrative mentions of cyphered telegrams, 19th century; no
  ciphertext, so no rows. The task text asked for codebooks; Discovery describes none as a document with undeciphered text.
- **Already tracked:** see the list above; also SP 78/114 (catalogue), SP 105/60/121 (lead), SP 84/165/134, /177, /181-183 (catalogue).

## What blocked, and what was not reached

- Nothing blocked: the API answered every request. No Chrome pass was made.
- Not reached: State Papers Online (Gale, paywalled), so no image was seen and every `seen` is `catalogue`; the CSP
  calendars were not searched per item, so some "undecoded" folios may have been read in print (prior art says "Discovery text only").
- Not reached: SP 104 (Foreign Entry Books) and SP 98 beyond f. 22, which return nothing with a cipher word; the `catalogueLevel`
  of many SP 87/89 items is item level but older SP 78 and SP 84 volumes are described by folio only where an archivist
  listed them (so a cipher letter inside an undescribed folio never shows).
- SP 94/3/221 (an intercepted portion with a key) was dropped because the volume date could not be fixed from the catalogue.
- The task asked for Foreign Office codebooks; none surfaced as a ciphertext (see above).
