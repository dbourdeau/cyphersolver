# UK and Ireland catalogue sweep (2 Nov 2026)

Source key `uk_ireland`. Output: `candidates.json`, **18 rows**, built by `make_candidates.py`. Far short of the 60 asked for:
the reachable catalogues hold few letters with cipher and no decipherment, and I did not pad it. Leads only; no row was viewed
(all scored from catalogue descriptions). Vetting used `research/archive_sweep_2026-10/known.py` only; no web search was run,
as instructed ("re-vet without web search"), so Tomokiyo, Lasry, DECODE on the web and printed editions are unchecked.

## What was reached

| Source | Result |
|---|---|
| NLS Archives and Manuscripts Catalogue (manuscripts.nls.uk, ArchivesSpace) | Opened in Chrome after a Cloudflare interstitial cleared on its own (nothing solved or clicked). Same-origin `fetch` of `/search`, one request per 2.5 s. Terms: cipher (3 pages), cypher, ciphers, cyphers, decipher, deciphered, "in cipher", "in cypher", encoded, cryptic. 91 distinct records; about 70 are ownership marks or monograms (Balfour of Denmilne's "cipher", royal cipher GR, armorial ciphers) and were dropped. 15 rows kept |
| Lambeth Palace Library (CalmView) | Opens. "cipher" gives 27 records: Carew MSS 597/615/624 (Pelham 1579-80, Mountjoy and Carew 1602), MS 647 f. 218, MS 3193. 1 row kept (Casenowe, MS 647 f. 218); the Pelham and Carew items are already tracked (`research/uk_tna`, catalogue entry on Pelham's cipher, calendared in Carew MSS) so were dropped. "cypher" not searched at Lambeth |

## What blocked, and what is not reached

- **NLW** (archives.library.wales): Cloudflare check, then the Welsh redirect page says the Archives and Manuscripts catalogue is
  unavailable outside the Library building. Not swept.
- **TCD** (manuscripts.catalogue.tcd.ie): the tab did not reach a TCD catalogue (the session stayed on the NLS host); not swept.
  TCD Digital Collections and MARLOC not tried.
- **PRONI**: `apps.proni.gov.uk/eCatalogue/` returns a 404 (the eCatalogue has moved); new address not found without web search. Not swept.
- **NAI** (National Archives of Ireland): not tried; catalogue mostly not online by item.
- **Archives Hub**: not touched (already swept elsewhere; no `research/archiveshub` folder exists here).
- Lambeth "cypher", Lambeth page 1 beyond the first 20 results were read only in part; NLS terms "code" and "secret" were not run (too noisy).

## What the 18 rows are

Mostly Scottish private papers at NLS with cipher passages and keys together, which make closed test sets: the Andrew Fletcher,
Lord Milton volumes (MS.16962, 17018, 16914, 16980, 17891, 17605: accounts and journals with cypher and keys, 1737-1756), the
Dundas of Dundas account books and notes in cipher (Adv.MS.80.3.48-50, 80.7.7, 1688-1701), Hay cypher tables 1707-11 (MS.14496),
Balcarres papers with keys of cyphers (Adv.MSS.29.2), D. Currie on cypher systems 1805-07 (MS.11732), Carstares letters partly in
cipher 1694-1700 (MS.3471, 19th-century copies, probably printed 1774), Mary Queen of Scots copies with cipher letters (MS.6135,
probably in Bain or Labanoff), plus small items. Weak or likely printed rows are marked in `verify`. One Lambeth row.

## Next

Check the Carstares State Papers and Bain for MS.3471 and MS.6135 before any work. Best by solvability: Milton MS.16962 and
MS.16980 (keys in the volume). A search of NLS for "key" and "alphabet" and for the Milton correspondence series, TCD, and a new
PRONI address would add rows.
