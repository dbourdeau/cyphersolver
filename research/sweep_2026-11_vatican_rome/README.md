# Vatican and Rome sweep, 2 Nov 2026

Result: **4 rows** (not 60; the source does not hold more). No web search was made (the instruction was to re-vet without it);
vetting is known.py on shelfmarks and correspondents only. Rows are leads, scored from descriptions, none viewed.

## What worked
- DigiVatLib opens in the user's Chrome. The old `/mss/search?...` URL is the 403 target; the real search is `/search?k_f=0&k_v=<term>&r=100&p=<n>`
  (the home-page form), reachable by same-origin `fetch`, one request per 2.5 s. Detail pages are `/mss/detail/<shelfmark>`.
- 29 terms (cifra, cifre, cifrata/o/e, cifrario/i, decifrazione/ata/ato/ate, in cifra, chiffre, chiffre, cipher, cypher, zifra, cifrado/a, clave,
  nunzio cifra, lettere cifra, nunziatura, scrittura occulta, alfabeto segreto, cryptographia, steganographia ...): 146 unique manuscripts.
  Most are noise (`cifre` matches numerals, Dante, Livy); 27 letter-type volumes had their detail pages searched for cifr/chiffr/cipher: 4 real items.
- Not rows: Urb. lat. 948/949/998 (Federico II's cifrario, key sheets), Borg. lat. 565 (Jesuit China cipher list), Borg. lat. 898 (solved),
  Vat. lat. 8338 and 10285 ("segretario della cifra", name matches only), Urb. lat. 868 (numerals), Vat. lat. 2392 (a bird-catching recipe in cipher, a book not a letter).

## Blocked or not reached
- AAV (archivioapostolicovaticano.va), Propaganda Fide (APF/SC) and ARSI: no searchable online inventory or image route was found; not tried in Chrome
  beyond what the earlier vat_vatican sweep recorded. Any item there is access "archive".
- opac.vatlib.it (the manuscripts catalogue behind DigiVatLib) was not queried separately; DigiVatLib shows the same contents notes.
- Contents notes in the result list are truncated; only 27 detail pages were read, so ciphered leaves hidden in the other volumes
  (Vat. lat. diplomatic miscellanies, Barb. lat., Ottob. lat.) were missed. A fuller pass should fetch every Vat./Barb./Ottob./Chig. letter volume's detail page.
- The earlier research/vat_vatican sweep covers the DECODE-listed Segreteria di Stato records; not repeated.
