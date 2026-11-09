# Baltic + Hungary + Slovenia sweep in Chrome (9 Nov 2026)

Result: 2 weak rows in `candidates.json` (cls B, regest only, not viewed). Tab closed at the end.

| Source | Route | Result |
|---|---|---|
| raduraksti.lv, arhivi.lv (Latvia) | Chrome navigation falls back to the new-tab page (host unreachable from this machine, same as curl) | not swept |
| dspace.ut.ee (Tartu) | same: redirected away, unreachable | not swept |
| dea.digar.ee | Cloudflare "Just a moment..." did not clear in ~25 s | not swept, left alone |
| periodika.lv, gramatas.lndb.lv | load, but are printed books/newspapers (viewer app), no manuscripts | not searched; not letter sources |
| dlib.si | works: same-origin `fetch('/results/?query=...')` returns server-rendered results | `'keywords=šifra'` 7 (all modern, pseudo-random generators etc.), šifrirano/šifrirana 0, šifrirani 1 (a 2020s paper), kriptogram 3 (modern), tajnopis 1 (Presek 1995). No manuscript hit. |
| Hungaricana Levéltári iratgyűjtemények (`archives.hungaricana.hu/hu/lear/search/results/?query=...`) | works; results are server-rendered, page 2+ via `fetch(...&list=<base64 {"query":...}>&page=n)` (use ASCII `\uXXXX` escapes in the JSON for accented terms) | rejtjeles 2, rejtjel* 9, `titkosír* OR chiffr* OR cifr* OR zifr* OR kriptogram*` 83, `feloldás nélkül` 419 (353 cipher-related). These are the "Bécsi segédletek" (HHStA, Vienna delegation aids). |

## What the 419 "feloldás nélkül" hits are
Almost all are HHStA Türkei I (Turcica) boxes 13-120: already covered by the earlier Türkei I range sweeps (Kt. 13-20, 29-36, 36-45, 46-49, 51-63, 65-76, 77-92, 93-120 in catalogue/leads/swiss_austrian). Ungarische Akten items were also covered: Fasc. 327 Konv. C/D (catalogue 1664-68 + Thököly 1682), Fasc. 310 (catalogue), Fasc. 425 Fráter György 1543 (swiss_austrian), Allgemeine Akten Fasc. 5 Hofmann 1527 (catalogue 1234), Misc. 427 Rákóczi to Klement 1710 (catalogue). Only two items were new to known.py: Fasc. 309 Konv. A fol. 1-2 (1659) and Misc. Fasc. 418 fol. 188-191 (1549).

Excluded as deciphered at the time or key-only: Fasc. 311 Konv. B (Nádasdy's chest letters, Latin translation), Fasc. 286 (Nagy of Leszenye "paria ... in ciffra", Latin copy), Fasc. 296 Gembicki to Zrínyi 1669 (keys, already in D_east_north), Fasc. 314 Donellan 1671 (key; letter 1670 already in leads), Fasc. 431 Fráter 1542 (deciphered on a separate sheet), Allgemeine Fasc. 4 1527 (Latin decipherment filed), Türkei I Kt. 1 (1530 key/decipherment), Kt. 28 (keys), Kt. 78 Konv. 3 (annexe cipher, Kt. 78 in swiss_austrian), Kt. 84 (1600: only cipher half-sentences in a postscript), Fasc. 327 Konv. D key leaves.
Non-lead hits: BFL 1919 criminal files (Popov, Odescalchi), a cipher-device deposit (Ágoston Lajos), Informationsbüro 1849-51 Kossuth-Mazzini key.

## Not done
Latvian State Historical Archive, Riga city archive, Academic Library of Latvia, Tartu University Library/ester.ee, DIGAR: host unreachable or Cloudflare. MNL OL archive.hungaricana.hu "Levéltár" databases beyond the Bécsi segédletek, and library.hungaricana.hu, were done by the 2 Nov Hungary sweep. Next try for Latvia: a different network (the LVVA hosts do not answer from here).
