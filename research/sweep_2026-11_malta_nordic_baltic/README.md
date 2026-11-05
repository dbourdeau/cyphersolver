# Malta, Finland, Norway, Iceland, Baltics sweep (2 Nov 2026)

Result: **0 rows** in `candidates.json` (empty list). Nothing was padded. Scripts first; Chrome once (vHMML), which
showed a Cloudflare Turnstile 403; no check was solved and the attempt stopped there.

| Source | Route | Terms | Result |
|---|---|---|---|
| Arkivportalen (Norway) | `GET https://www.arkivportalen.no/api/search?text=<term>&size=100&from=N` (JSON, no key; `query=`/`q=` are ignored) | 36 (chiffer/chiffre/ziffer/cifret/hemmelig skrift/kodet brev/dechiffr*/nøkkel/sympatetisk ...) | 6,405 units; 215 with a cipher word in title or note and start <= 1945. All are 20th-century signals/foreign-ministry administration (Chiffertjeneste, Hemmelig skrift instructions, WWII Chifferkorrespondanse), or "Cifferbog" = arithmetic/cipher-figure copybooks (1822, 1834, 1840). No pre-1900 cipher letter. `ap_hits.json` (cp1252-encoded; read with `errors='replace'`). |
| Astia (Kansallisarkisto, Finland) | `POST https://astia.narc.fi/uusiastia/ws/aineisto/read.php` (JSON, `endDate` filter) | 37 Finnish/Swedish/German/Russian/English | To 1920: one hit (`salakirjoitus`: 1906-14 prosecutor's seized papers, no cipher stated) and a personal name Siffer. Everything else is 1930-45 military "Salainen kirjeenvaihto". Astia searches descriptions only. |
| Finna API (Finland) | `api.finna.fi/v1/search` | - | Cloudflare challenge in curl. **Not swept** (Chrome not tried). |
| epaveldas.lt (Lithuania: LCVA, VUB, KRVA, museums) | `POST /vepis-api/internal/find` `{term,page,pageSize,filters}` | 65 in Lithuanian, Russian, Polish, German, French, Latin, Italian | 2,142 records; 96 matched a cipher stem. All noise: the Yiddish first name Šifra (Kaunas/Ukmergė registers), 1926-46 diplomatic telegram ciphers of the Lithuanian legations (LCVA 656, 648, 668), folklore "neiššifruotas", a 2014 insurgents' alphabet. No letter or document before 1900. Multi-word terms are OR-ed by the API. `lt_hits.json`. |
| Raduraksti (Latvia) | `/search?q=` | 6 | Returns an empty shell for every term, even "kods", so search needs a login or JS state. Not logged in (rule). **Not swept.** |
| Estonia AIS (ais.ra.ee) | - | - | DNS resolves (195.80.106.158), TLS handshake reset from this machine (curl and Python). **Not swept.** DEA/digar.ee and Muis reachable but not searched. |
| Iceland (handrit.is) | `/search?q=` | - | Security-check page (captcha). **Not swept.** Iceland's Lbs 946 8vo Napoleon key is already noted in `research/swiss_austrian`. |
| Malta: vHMML (Order of Malta archive, AOM series 9 letters 1586-1798; Mdina Lettere consolari) | `vhmml.org/readingRoom/search` | - | 403 "Turnstile validation failed", also in Chrome. **Not swept.** This is the most promising unreached source here. |
| Malta: Notarial Archives | notarialarchives.gov.mt | - | 403, redirects to notarytogovernment.gov.mt. Not swept. National Archives of Malta and Malta Library hosts did not answer. |

## Not reached / next steps

- vHMML Reading Room for Malta (needs a person to clear the Turnstile in a tab, then search `cifra`, `cifrato`, `chiffre`, `cipher` over AOM Arch. 1-1000s and Lettere consolari).
- Finna (Cloudflare), Raduraksti (login), Estonian AIS (network), handrit.is (captcha), Tartu/Vilnius university library catalogues (not probed).
- Sweden and Denmark are already in `research/scandinavia` and `sweep_2026-11_riksarkivet_volumes`.

Dedup: with zero rows, `known.py` was not needed.
