# UK and Ireland retest (3 Nov 2026)

Source key `uk_retest`. Retest of the portals blocked in `research/uk_libraries` and `research/sweep_2026-11_uk_ireland`, run with
the user's VPN on. `candidates.json` holds **8 rows** (built by `make_candidates.py`). All are leads scored from catalogue
descriptions; none was viewed, so none passes the vetting bar and none was promoted.

**The VPN exit was Dublin, not the UK** (ipinfo in both the shell and Chrome: IE, AS9009 M247). So this does not test a UK exit.

## Access

| Source | Result 3 Nov 2026 |
|---|---|
| PRONI | **Newly reached.** The eCatalogue moved to `apps.proni.gov.uk/eCatNI_IE/SearchPage.aspx`; the old path 404s. Works in Chrome, driving the form. A same-origin POST of the form returned nothing; "More" POSTs from the results page work. Searched "cipher" (39 records) and "cypher" (first 50 of 54). A later any-word query listing several terms got an F5-style "Request Rejected"; not pushed. Single terms "decipher", "ciphers" and "in code" not run |
| Lambeth (CalmView) | Opens to scripts and Chrome. **"cypher" newly run: 10 records**, read in full. Use `advanced.aspx`, because the `Overview.aspx` URL with dsqSearch returns an empty list |
| NLS | 403 to scripts; Cloudflare clears by itself in Chrome. Search needs `/repositories/2/search?q[]=...&op[]=&field[]=&from_year[]=&to_year[]=`; a bare `/search?q[]=` gives an error page. "cipher key" (fuzzy, 57) and "in code" (2) run; "key to cipher", "secret writing", "cipher alphabet" give 0 |
| TCD Digital Collections | Opens to scripts: `/catalog?q=...&search_field=all_fields`. "cipher" 7 records, all code lists or MS 509. "cypher" 0 parsed from curl. **The Manuscripts & Archives catalogue host (`manuscripts.catalogue.tcd.ie`) times out to scripts and left the domain in Chrome, so the main TCD catalogue is still not swept** |
| NRS | 403 to scripts; opens in Chrome. Not re-crawled: 528 records were taken over 11 terms on 29 Oct (`research/uk_libraries`) |
| National Archives of Ireland | Site opens. It has no item catalogue of early papers; site search for "cipher" gives one DMP report (Sept 1915). Nothing to sweep |
| National Library of Wales | Cloudflare clears in Chrome, then the site says the catalogue is unavailable ("Website Not Available"). **Still not swept.** On 2 Nov the page said it was unavailable outside the Library building, so this looks like an outage or restriction, not geography |

## What the rows are

Best: Lambeth MS 649 ff. 490-5, cipher letters to Anthony Bacon (Essex's network, not in `known.py`, no entry in Tomokiyo); PRONI
D572/17 Drake at Genoa 1795, with Macartney's partial decipherment as a crib; and an RMG Drake letter of 1796 in cipher, found while
checking those. Weak rows are marked in `verify`: D3030/2109 is cited to a printed volume and may close at once.

## Left out

Read at the time, so not open: PRONI D2433/D/1 (Keith papers 1777, "in cypher with translation": Elliot, Stormont, Stepney, Ainslie,
Eden), T3765/H/6/1 (Harrington to Granard 1733-34, decoded on slips folded in), D3030/P/61 and /P/148 (cipher passages with the words
given); Lambeth MS 645, 646 (Charles II's own decipherings, Birch), MS 930 nos. 4, 5, 8-10 (Blencowe's decipherments, 1702).

Most PRONI "cypher"/"cipher" hits use the word figuratively ("a mere cypher") or as a monogram.

## Key leads (keys and code lists without ciphertext)

Lambeth MS 930 no. 6 (French numeric code table, partly reconstructed by Blencowe, c. 1701: test on Louis XIV 1702 intercepts);
Lambeth MS 646 no. 60 (Ceffis's cipher device, with diagram); NLS MS.5720 (Sir Robert Liston, "a diplomatic cipher", 1794-1807);
PRONI HA/32/1/311 (RIC secret cipher 1922), D2744/U/1 (Lombard General Code and Whitehall Secret Cipher c. 1930), T2593/44-45 (John
MacDonald's cipher table, 1820); TCD MS 9383/1196, MS 9385/1254, MS 9501/5307 (Davitt and Parnell Commission code lists, 1891-1903).

## Next

MIC/438/5-6 (PRONI) and the MS 649 images decide the two best leads. Still unreached: the TCD manuscripts catalogue and NLW. A UK
exit is untested.

## Vetting, 3 Nov 2026 (`vet_2026-11-03.py`)

Promoted as archive-only, no ciphertext seen: 1989 (Bacon, MS 649), 1991 (Drake, PRONI), 1992 (Drake, RMG CRK/4/136).
Closed as read: 1993 (printed in Castlereagh Correspondence v, 428), 1994 (clear draft is D3030/4980).
Held as leads, with `vetting_note`: 1990 (extent unknown), 1995 (T-series copy), 1996 (probably readable from the Lansdowne 1163 register).
Not checked: FO 28 copies of Drake, Nicolas's Nelson vol. 2, Tosh's thesis, Birch's folio notes (poor OCR).
