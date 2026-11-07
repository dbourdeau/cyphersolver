# BAV letter volumes without item-level description, sweep of 6 Nov 2026

Result: **0 candidate rows** (`candidates.json` is `[]`), 2 key leads (`key_leads.json`), and a negative result for the
Chigi nunciature volumes. About 90 minutes; no Chrome needed.

## Route (same as research/sweep_2026-11_digivatlib/README.md, confirmed)
- OPAC `opac.vatlib.it/mss/search?k_f=0&k_v=<term>&r=100&p=<n>` with browser UA + cookie + Referer works from curl/urllib.
  `opac.py` (term harvest -> hits.jsonl), `items.py` (item records), `q.py` (print hits), `probe.py` (manifest status),
  `samp.py` (evenly spaced IIIF folios + contact sheet; needs Pillow).
- IIIF manifest `https://digi.vatlib.it/iiif/MSS_<Shelfmark>/manifest.json`: HEAD gives 405, so probing needs a full GET.
  **Rate limit: about 35 manifest GETs at 1 s intervals brought a 429 that lasted ~15 minutes** (it also hit the image
  server). Probe at 3 s intervals. A 429 body saved as a manifest breaks later reads: delete it.
- Contact sheets at 450-500 px are enough to tell clear text, cipher and drawings apart.

## Terms (new, on top of the earlier sweep)
`cifra con la decifrazione` 0, `lettere cifrate` 2, `cifrario` 4, `cifrari` 2, `cifrato` 0, `cifrata` 3, `decifrato` 7,
`cifre` 148, `cifra*` 51, `chiffre` 24, `cifras` 5, `en cifra` 0, `clave` 7, `lettere in cifra` 12, `cifrate` 2,
`alphabetum` 53, `litterae in notis` 90 (all liturgical/Greek/palaeographic), `nunziatura` 56, `scrittura cifrata` 0.
Every cipher hit among the letter volumes was already in the earlier sweep except two key volumes (below).
Nothing new for Ott. lat., Reg. lat. (letters), Ross., Ferr., Patetta, Boncompagni-Ludovisi: the OPAC returns no
item-level cipher notes for them, and no letter volume of those fondi surfaced.

## Findings
- **Barb. lat. 9914 and 9915, "Cifre antiche"**: cipher tables of Cardinals Antonio, Francesco and Carlo Barberini and of
  Carlo and Taddeo Barberini (OPAC ids 117953, 184209). Not digitised. Keys for the Barberini letters (the Revelo 1641
  row already in the catalogue names them as "key_held"). Not rows (no ciphertext).
- **Chig. A.I** (the Chigi nunciature and Münster papers, inventory of Incisa della Rocchetta; OPAC gives bibliography only):
  digitised are A.I.4, 6, 7, 8, 20, 21, 22, 23, 25 (manifest probe; 1-3, 5, 9-19 not, 35-60 not probed: 429).
  Contact sheets of A.I.20, 21, 22, 25, 8 (6 folios each): all clear Italian/Latin letter copies of Fabio Chigi's
  Münster/Cologne correspondence (1639-1651), no cipher seen. Cipher exchanges of the nunciature are in the
  Archivio Apostolico Vaticano (Nunz. Colonia, Germania), not here. A.I.4, 6, 7, 23 not sampled.
- **Barb. lat. 9848** (Mancini, Madrid 1648-54, "Cifre e decifrati"): sampled 6 folios; clear autograph letters that
  mention cipher letters ("in cifra de 6 d'Aprile"), no ciphertext on the sampled pages. Decipherments exist per OPAC,
  so not a row. 9846, 9812, 9845, 9857, 9889 OPAC records: mentions of ciphers only, not enciphered text.
- Barb. lat. 9812, 9840-9847, 9887-9899, 7633-7636, 8620, 9863, 9876: manifests 404 (undigitised).
  Barb. lat. 9900 is digitised but holds drawings.
- Vat. lat. 13471/13472 (Severoli, Vienna 1805-06): OPAC notes no cipher.

## Not reached
- Barb. lat. 6000-9800 letter volumes with no item description: digitisation status not mapped (the manifest rate limit
  stopped bulk probing) and content is invisible to OPAC search. A shelfmark-by-shelfmark probe at 3 s plus contact
  sheets is the only route; the Sala Cons. Mss. handwritten inventories are not read.
- Chig. A.I.35-60 (429), Ott. lat. letter volumes, Urb. lat. avvisi/ambassador volumes, Ross., Capponi (beyond Cappon. 164
  already closed), Ferr., Patetta, Boncompagni-Ludovisi: no handle in the OPAC.
- Prior art: web searches for Barberini/Chigi cipher decipherments (Tomokiyo, Lasry, APW, Nuntiaturberichte) returned
  nothing relevant; no rows, so none recorded per row.
