# Chrome pass over blocked portals (2 Nov 2026)

Five portals that earlier sweeps recorded as blocked, retried in the user's own Chrome (Claude in Chrome) as same-origin
`fetch` calls, about one request a second. No check was solved or clicked by Claude. Candidates are in `candidates.json`,
built by `make_candidates.py`; all rows are leads, not catalogue entries. Most are scored from descriptions.

## Result by portal

| Portal | Earlier | This pass | Result |
|---|---|---|---|
| szukajwarchiwach.gov.pl | Imperva check, not one search (`polish_archives`) | Opens. 67 terms (Polish, French, German, Latin, Italian, Russian), 1,883 records to 1950, 843 with a cipher word in title or note | 19 rows |
| BNE Digital (bnedigital.bne.es) | WAF, Cloudflare (`bne_hispana`) | Opens. 51 terms on `f=ficha`, 851+ records, about 80 manuscripts | 8 rows. **Partial, see below** |
| RAH Biblioteca Digital | Anubis check | Opens. 30 terms | 0 new: only Morillo and Isabel II records, already leads |
| Internet Culturale | TLS failure, CAPTCHA | Opens. 56 terms, manuscripts filter, 179 records | 0 new rows: Dudout's sweep already holds the real ones |
| DigiVatLib, opac.vatlib.it | 403 | `ERR_CONNECTION_RESET` in Chrome; TLS error 35 in curl | **Not swept.** Network-level from this machine; try another network |
| Archives Hub | Cloudflare | Check cleared in one tab, not by Claude. That tab then stopped answering the tools, and a fresh tab was challenged again | **Not swept.** Stopped after three tries |

## Best leads

1. **Pedro Vara → Ferdinand, Dueñas, 7 Oct 1470 (BNE MSS/20215/36).** Image seen: mixed clear and cipher with interlinear
   glosses. Not on DECODE or in the repo. Weeks from `targets/ferdinand1473` d56.
2. **Ferdinand → John II, 1476-79 (BNE MSS/20211).** At least ten more letters match "cifrada". This answers Next steps 2
   in `targets/ferdinand1473/NOTES.md`. Not viewed.
3. **Branicki → Potocki, 1757 (AGAD 1/338/0/1/446).** Image seen: clear French opening, then about ten lines of neat letter
   cipher. Catalogued "nierozwiązany".
4. **Betański letters (AGAD 1/338/0/1/128-143).** Interlinear solutions on some, none on others: the best key route here.
5. **Leopold I → Charles II, Prague, 14 Apr 1680 (BNE RES/261/58).** Autograph "carta cifrada". Not viewed.
6. **Besieged Smolensk → Krzysztof Radziwiłł, 1 June 1633 (AGAD 1/354/0/2.1/1116).** Scans online; cipher not seen yet.

Also **AGAD 1/338/0/1/1398-1401**: image of 1398 seen, a full page of dense cipher.

## Catalogue corrections to make (not done here)

The Polish portal shows scans for these Zbiór Popielów and Nabytki units, but catalogue entries about them carry
`access: archive` or say the portal is behind a bot check. Open one unit per entry before changing it:
sygn. 63 (cat. 430), 84 (434), 90 (431), 423 (Zabłocki, probably 425), 424 (432), and 1/420/0/-/125 (436). The other
entries from 412 to 433 were not checked against scan flags.

## Key leads (bare keys, no ciphertext; not rows)

AGAD 1/338/0/1/1196 (cipher and decipher key, scans); 1/3/0/1/08a nr 49 (numeric cipher key, 1750-95); 1/3/0/2/55b/33
(Keyserling, congress with the Turks); 1/3/0/1/08b nr 043 (Morsztyn at Stockholm, 1655, solution written above);
1/15/0/-/968 (Ghigiotti's keys, 1768, 1789-91); 1/8/0/3/III.150 (key among Kamera papers, scans); 1/3/0/33/77 teczka 461
nr 774-775 (Wysocki, 1668); 1/3/0/33/80 teczka 684 nr 1273-1275 (Łopuski, Benoe, 1742); 1/11/0/-/394 (Jakubowski, French
ministry, 1759-69, tables, scans); 1/244/0/9/148 (January Uprising, War Department key, scans). AN Kraków 29/637/0/1.3/6575
(Paweł Karol Sanguszko keys); 29/650/0/1.1/13 (Cieciszewski cipher, 17th c.). 10/300/0/22/300,31/9h (intercepted
Schlippenbach and Courtin papers 1655-56, chancery cipher). 1/12/0/-/445-452 (Kwilecki and Deboli chiffres, already noted
in catalogue entries, scans online). BNE MSS/20212/34/1-5: Pacheco (Jaén) → Granvelle, 1551-54, cipher with the decipherment in
the margin, so excluded as a target but a usable key source.

## Excluded as already held

Listy multańskie and Wołoszczyzna (29/677/0/2/185/62, 72): DECODE R7483 and `sieniawski1708`. Zbiór Popielów letters: catalogue
412-434. Kinner 1728: 437. Garnysz: 436. BNE: Sessa, Carpi, Mary of Hungary, Hurtado (five letters), Leyva, Juan Manuel,
Nájera, Mirabel → Gondomar, Dormer in `bne_hispana`; Savoia 1555, Cardona, Moncada in the catalogue; Herrera 1526 on Cryptoole;
Poupet, Lope Hurtado, Niño in targets. Internet Culturale: Carte Machiavelli I/3, IV/83, V/139-140, Autografi Palatini IV/77,
VI/38, VI/62 are leads 1548-1559. New to the repo but not added, because read at the time or single name-words: Machiavelli III/21,
V/63, V/64, V/123.

## Not finished

- **BNE:** "cifrado" (123 hits) and "descifrada" were never read. "cifra" stopped at offset 500 of 790, "cifras" at 100 of
  177. Most shelfmarks in the Ferdinand series and the MSS/2408-15 (Villahermosa), MSS/8695 (Fuentes), MSS/20212/37 (Juan José),
  MSS/20210/36 (Colonna) matches were not checked for cipher. BNE began serving "Verificación de Seguridad" after about 25
  card fetches, so I stopped. Resume gently, by hand-paced navigation.
- **Polish portal:** only pre-1900 rows were read: 564 keyword records from 1900-1950 and 115 Radom records (58/387) were
  not triaged, and the harvest sits in that Chrome profile's localStorage (`szh`), not on disk. Rows with no scan flag need AGAD.
  "Szyfrowe" lost a re-search after a tab freeze, but its counts and pages were taken on the first run. Letter-level prior art is
  a single web search per family: Tomokiyo, Lasry and the printed editions have not been searched, so no row is vetted.
- **RAH:** `resultados_ocr.do` returned the same hits as the catalogue search, so OCR text was probably not searched. The
  Salazar index was not reached; it does not appear to be in this search.
- **Internet Culturale:** only the manuscripts filter. Full-text (28,624 hits for "cifra") not read.
- Hispana, BVPB and BDCyL were not tried in this pass.

## Practical notes for the next pass

- Background tabs freeze in Chrome and the tab id can change. Run one portal at a time, in short calls of under 30 seconds,
  saving to `localStorage`. Batches of more than four such calls time out.
- szukajwarchiwach keeps the search in the session and a `fetch` POST does not change it: submit the advanced form in a
  same-origin iframe, then page `/wyszukiwarka?...&_Result_delta=40&_Result_cur=N`.
- BNE: `results?o=&w=<term>&f=ficha&l=100&s=<offset>`. `c` is the page number, not a size. An empty `w` loads the whole
  catalogue and hangs the tab. Card: `card?id=<uuid>`.
- RAH: POST `busq_general` to `/es/consulta/resultados_busqueda.do`.
- Internet Culturale: `/it/16/search?q=<term>&__meta_typeTipo=manoscritto&pag=N`.
