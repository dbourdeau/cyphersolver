# Vetting wave 20, batch 12 (16 Nov 2026)

Claude Code session (Claude Opus 5.5). Leads 1221 1222 1223 1224 1225 2456 1286 2032 2507 1628 1196 2523 2522 2147 2548 2581 1938 1990.
Proposals only (`proposals.json`); nothing applied to `research/leads.json` or `catalogue.json`. Vetting blocks pass `vetting_problems`
apart from the verdict rule for closed leads. Tomokiyo and Lasry lists: the copies fetched 15 Nov 2026 (`prior.py`, `prior_out.txt`).

## Results

| lead | verdict | deciding fact |
|---|---|---|
| 1221 | partly_read | Türkei I Kt. 36-45: of 59 'no decipherment' dates, 47 have a same-date deciphered copy, clear copy or extract; 8 residual, unproven |
| 1222 | read | every 'no decipherment' item of Kt. 46-49 has its decipherment in the same Konvolut (49597, 49681, 49718-19, 49752, 49856, 49907, 49936) |
| 1223 | partly_read | Kt. 51-63: 31 of 41 dates resolved, 5 residual (the rest unclassified by the script); residue 51049 deciphered in the Ernst letter 51046 |
| 1224 | partly_read | Kt. 65-76: 34 of 53 dates resolved, 14 residual; 51863 sits beside the deciphered postscripts 51864 |
| 1225 | partly_read | Kt. 77-92: 12 of 22 dates resolved, 6 residual; Kreckwitz's parallel letters to Matthias deciphered |
| 2522 | key_lookup | Topelius's cipher (27 signs) solved by Vasenius, printed resolved in the SLS edition |
| 2581 | open (held: 1921) | only MHC 3352 is ciphertext (about 50 four-digit groups, nothing over them); 1186 = 3874, a clear 'suret'; 1830, 3284 clear notes |
| others | none | blockers in `proposals.json` notes |

**For the lead agent, outside this batch:** catalogue **2237** (Breuner 12 May 1583, Türkei I Kt. 48 Konv. 3 fol. 137-144, 147-151) is
Hungaricana regest 49853; regest 49856 is Breuner to Archduke Ernst of the same day, 'feloldás és sifrír', fol. 134-136, 158, **147-151**.
2237 looks read at the time and should be re-checked. The same pattern (cipher copy to Rudolf, deciphered parallel letter to the Archduke)
runs through the whole Constantinople series and probably affects catalogue 1226-1229 and 343 too.

## Routes found today

- **Hungaricana answers scripts from this machine** (plain urllib with a browser User-Agent, 16 Nov 2026), not a 403. `hsearch.py` pages the
  archives search (`/en/lear/search/results/?list=<base64 {"query": ...}>&per_page=100&page=N`); `regest.py` reads a regest in full.
  A quoted date string (`"1588.11.12"`) finds every regest of that day, but misses range-dated ones ('1588.11.11-12., 11.14.').
  `cluster.py`, `datecheck.py`, `datereport.py` build the Türkei I analysis; `raw/` holds the harvest (2,633 'sifrír*' regests).
- **Koç CONTENTdm and libdigitalcollections.ku.edu.tr reset the TLS connection** from here and from WebFetch; Europeana's thumbnail
  cache (`api.europeana.eu/thumbnail/v2/url.json?uri=<edmIsShownBy>&type=IMAGE&size=w400`) and record API (`wskey=api2demo`) work.
- **SLS digital editions** (Topelius and others): `POST api.sls.fi/digitaledition/topelius/search/elastic/topelius` takes a raw
  Elasticsearch query (use `highlight` on `text_data`).
- Calames answers curl again. Finna now shows a Cloudflare challenge; Kansas Memory a 202 with no body; Lambeth CalmView Record.aspx hangs;
  HOLLIS 403; Adam Matthew 403.
- HStAD D 4 185/3: all 414 images downloaded to `img/d4/` (git-ignored); `sheets.py` makes 6-up contact sheets.
