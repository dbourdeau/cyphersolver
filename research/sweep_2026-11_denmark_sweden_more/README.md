# Denmark / Sweden, more (9 Nov 2026)

Result: **0 rows** in `candidates.json`; 2 key-only items in `key_leads.json`. Nothing padded.

## Routes

| Source | Route | Result |
|---|---|---|
| Libris (KB Stockholm, Swedish university/county libraries) | `https://libris.kb.se/xsearch?query=<t>&format=json&n=200&start=` works with curl (no bot check). `libris.py` | chiffer 396, chiffre 453, chiffrerad 4, ziffer 383, hemlig skrift 459, dechiffrering 16, cifferskrift 0. Almost all printed books, sound recordings and 20th-c. fiction. Only 7 manuscript records: Chifferlexikon D 1086a:1-2 (key), Görtz "Bref och handlingar 1717-21" (Görtz already in repo as R4350), Bonde on Sweden under Frederick I (not a cipher). No ciphered letter. |
| Det Kgl. Bibliotek, Copenhagen | Primo VE JSON API works with curl: `https://soeg.kb.dk/primaws/rest/pub/pnxs?...&inst=45KBDK_KGL&vid=45KBDK_KGL:KGL&scope=MyInstitution&q=any,contains,<t>` (`kbdk.py`). `www.kb.dk/search` is 403. | chiffer: 9 local records (one manuscript: Gøhr 1750 cipher samples with key, key-only); chiffre: royal monogram notes ("Christian IV's chiffre"), noise. Manuscript descriptions rarely mention cipher; I stopped the term loop after chiffer/chiffre/chiffrer/chiffreret (low yield, slow). |
| arkiv.dk, sa.dk, kb.dk home pages | reachable (200/301) but JS search; not pursued, Rigsarkivet itself was fully covered by `research/scandinavia` (Daisy + soeg API). | - |
| Riksarkivet NAD API | listed digitised units of Stedingk (273), Reuterholm, De la Gardie, Oxenstierna, Tessin (`nad_units.json`). Text terms are exhausted by `research/scandinavia` (1,074 records). | - |
| Riksarkivet images (lbiiif, Referer needed) | Manifests for Reuterholm volumes take 5 min each (use `probe.py`: info.json bisection gives the image count; ids are sequential, E 5134-5141 = R0003396-R0003403: 246, 499, 390, 581, 464, 580, 381, 339 images). Image server ran at 3-10 s an image. | Only Reuterholm E 5134 (1790-92) sampled, 1 image in 12 (21 openings): all clear French/Swedish letters, no number rows. The other seven Reuterholm volumes, Stedingk E 6616/6617 and the Gustav III/Karl XII letter volumes were **not sampled**: the server was too slow and I stopped. |
| Norway | Already swept (`sweep_2026-11_malta_nordic_baltic`: Arkivportalen 6,405 units, nothing pre-1900). | - |
| Uppsala Alvin | Not retried (Anubis). | - |

## Not reached (best next steps)

- Reuterholm E 5135-5141 (1793-97, letters from envoys; his key is at SE/RA/720741/~/28), Stedingk B b E 6616/6617
  (letters from royal persons 1788-1828), Ericsberg 720266/01 vol. 294 (Gustaf III to Tessin, Klingspor, Sophia
  Albertina), De la Gardie 720222/01/C/I (Moirous de Verrière 1662-68, Palm 1669-84). Sheet them at 1 in 10 with
  `sheet.py` when the image server is quicker (scripts: `sheet.py resolve|sheet`, `probe.py`, `rik_common.py` copied from the consuls sweep).
- KB Copenhagen: only a few terms run; Danish "Nye kgl. Samling" envoy copybooks are not described as cipher.
- Libris xsearch type filter for manuscripts (`&holdings`/`t=`) was not found; the 7 manuscript hits are all it showed.
