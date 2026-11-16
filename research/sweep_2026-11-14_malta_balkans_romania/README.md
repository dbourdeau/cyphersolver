# Malta, Balkans, Romania sweep (14 Nov 2026): 0 rows

`candidates.json` is empty on purpose. Nothing found met the bar (a ciphertext item that exists, with a shelfmark or
record URL, unread, not already in `catalogue.json` / `leads.json`). Not padded.

## What was searched
- **Europeana API** (`api2demo`, `eu.py`, 2.5 s between requests, `YEAR:[1200 TO 1919]`, no country filter): 30 terms in
  Romanian (scriere secretă/cifrată, scrisoare cifrată, cifru), Hungarian (titkosírás, rejtjel*, cifrált levél), Croatian/Serbian
  (cifrirano/šifrirano pismo, tajnopis), Italian/Latin (lettera in cifra, litterae cifratae), German (chiffrierter Brief,
  Geheimschrift, Chiffrenschlüssel), Greek and Bulgarian phrases, plus "cifra Malta/Dubrovnik/Ragusa". 47 distinct records
  (`europeana_raw.json`): all noise, namely Romanian medals ("cifru" = monogram), and 1518-1881 printed cryptography treatises
  (ONB, BSB) matched by "Geheimschrift". No manuscript letter.
- **Web searches** (about 14, English, Italian, Croatian, Serbian, Romanian, Hungarian, German, Greek): Dubrovnik/Ragusa,
  Order of St John / AOM / NLM, Cluj, Sibiu, Brukenthal, Batthyaneum, Hurmuzaki, Mihai Viteazul/Brâncoveanu, Filiki Eteria,
  Arhiv Srbije/Cetinje, Zrinski-Frankopan/HDA. No item-level cipher record surfaced in any of them.
- Known.py checks (Teleki, Vrančić, Dubrovnik, Ragusa, Brâncoveanu, Wallachia, Révay, Vadai, Brukenthal): see below.

## Why nothing was added
- **Teleki Mihály to Rhédey Ferenc, 23 Jan 1678** (mostly numeric code, letter-book copy; Gergely, *Teleki Mihály levelezése*
  VIII, 1926, p. 40): Hegedüs Gyula, *Nyelv és Világ* 23 (2020), pp. 60ff, "Teleki Mihály titka", works on it (a cracking
  attempt, with the numbers printed); the 1666 Teleki to Széchy Mária letter was solved on kripto.blog.hu (2016). The Teleki
  edition's other code letters are already leads (c32 batch, Láng C.Bor.02). Not new; not a fresh row. Possible same-key
  sibling note if someone wants one: `https://publikaciotar.uni-bge.hu/1711/1/Hegedus_Nyelvvilag23.pdf`.
- Vrančić (Šibenik, Paris, OSZK code books), Levski (BIA fonds 85), Brâncoveanu/Cantacuzino to Sieniawski, Ferducci/Ragusa:
  already in the catalogue, leads or targets.
- Dubrovnik, Malta: previous sweeps (`sweep_2026-11_B_unswept_south`, `sweep_2026-11_malta_nordic_baltic`,
  `sweep_2026-11_balkans_greek`) reached the same wall; this pass added nothing.

## Blocks
| Source | Result |
|---|---|
| vHMML Reading Room search (Malta AOM series 9, NLM) | 403 "Turnstile validation failed" in Claude in Chrome (own tab, tab closed). Not solved or clicked through. A person has to clear it, then search cifra / cifrato / chiffre / cipher over NLM AOM. Record view pages are volume-level only. |
| nlmalta.gov.mt, nam.gov.mt | no connection from this machine (curl code 000) |
| arhivelenationale.ro | HTTP 503; cluj.arhivelenationale.ro: no connection |
| dacoromanica.ro, restitutio.bcub.ro | search URL guesses 404 (JS front ends; not driven in Chrome) |
| dad.hr / arhiv.hr | redirect only, no item catalogue |
| hrcak.srce.hr, doaj.org | bot checks on full texts (not opened) |
| No CAPTCHA was solved. | |

## Next steps (outside what this run could do)
1. Person clears the vHMML Turnstile, then search the Malta series by term (the only item-level route to AOM ciphers).
2. Chrome pass on Dacoromanica and the Romanian archives' search pages (JS) with cifru / scriere cifrată / cifrat; ask
   Arhivele Naționale Cluj and Sibiu whether any finding aid lists "scriere cifrată".
3. Read by hand: Láng Benedek, *Real Life Cryptology* (2018) for Transylvanian items; Révay 1974; Polic Bobic, "Tajna
   diplomacija u Dubrovniku u XVI. stoljecu" (2011) for Ragusan cipher series shelfmarks.
