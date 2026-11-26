# Durham, Abbas Hilmi II papers: HIL/202, HIL/203, HIL/49, HIL/99 screened in full (25 Nov 2026), plus Badator terms and Latin American probes

**Result: 0 new leads (`candidates.json` is `[]`). Every frame of the four volumes was looked at on a contact sheet and none carries ciphertext. Two key items in HIL/203 (already in the ledgers from wave 18) were seen again.**

Continues `research/sweep_2026-11-15_wave18_durham2/` (its "Left" line: HIL/202/94-543, the rest of HIL/203, HIL/49).
Run from a network that reaches Durham and the Basque Badator portal; Chrome (Claude in Chrome) for the Spanish and Latin American hosts.

## Why this area

The COVERAGE "Still unswept" rows for Valencia, Canarias, Madrid, Sardinia and Sicily could not be worked from this network (table below),
and the Spanish catalogues that open (Badator, Navarra, DARA, Arxius en linia) were already exhausted. Of the open items in the notes, the
Durham Abbas Hilmi II volumes were the one source with (a) images online and a script route that works (IIIF by curl), (b) a record of the
earlier waves finding bare cipher telegrams there (HIL/64, HIL/65, HIL/57: five promoted leads, 2899-2909, 2922), and (c) a named list of
volumes left. The volumes left were the best bet for another unread cipher item. The result is a clean negative, which is itself worth
keeping: **HIL/64 and HIL/65 are the only telegram volumes, and the cipher material in the rest of the collection is key sheets and code books.**

## Routes (all by script, Python urllib)

- Manifest: `https://iiif.durham.ac.uk/manifests/trifle/32150/<a[0:2]>/<a[2:4]>/<a[4:6]>/<ark>/manifest` (`man.py <tag> <ark>`), then every frame at
  1,024 px (`dl.py <tag> 1024`, one request a second; the server gave 5-40 frames a minute). Contact sheets of 12 frames (`sheet.py`, 400 px a
  frame): enough to tell a letter, a typed memorandum, a table or a number block apart; anything table-like was opened at full size. Images
  are in `img/` (not committed). Arks are in `units.tsv` (copy of the wave 18 table: ref, dates, title, ark).
- No block from Durham on any of 950 frames.

## Volumes screened

| Volume | Description | Frames | Labels | Verdict |
|---|---|---|---|---|
| HIL/202 | Dr Said Bey Kamil I, 1914-1921 (secret reports with Egypt, memoranda, letters) | 268 (frames 47-314; frames 0-46 were wave 18) | 94-543 | Clear. French legal memoranda and letters (Zurich, Lausanne, Geneva, 1915-16), Arabic memoranda 1919-21, French and Arabic press cuttings, a French notebook "Relations entre Abbas II et le gouvernement britannique". No figure groups, no telegram strips. |
| HIL/203 | Dr Said Bey Kamil II, 1914-1918 (Union des nationalites, Egyptian question, Oppenheim correspondence, Yeghen Pasha affair) | 504 (all) | 1-574 | Clear except the key material below. Typed French and Arabic, Egyptian-nationalist pamphlets, Swiss federal court papers (Yeghen Pasha, 1917), lawyers' letters, waqf account tables (frames 49-51, labels 58-60: Arabic tables of endowment figures, not a cipher), lists of enclosures (frame 411, label 465). Telegram forms (frames 5, 139, 416, 459, 471) carry clear French text. |
| HIL/49 | Political informants, 1901-1928 | 134 (all) | 1-249 | Clear. Arabic reports and letters to the Khedive (Cairo, Paris, Constantinople), a Credit Lyonnais account, press. No cipher. |
| HIL/99 | Political documents re Abbas Hilmi, 1916-1928 | 47 (all) | 1-92 | Clear. Typed telegram drafts from Hafiz Ramadan Bey (Neuilly) to governments and press, French memoranda, notes on the Anglo-Egyptian question (frames 5-7 are all-capital telegram text in plain French, opened at full size). No cipher. |

Not digitised, so not screened: HIL/88 and HIL/120 (the other "secret"/"intelligence" volumes named in wave 18 carry no digitised ark in the finding aid).

## Key material seen again (not leads; already recorded by wave 18)

| Item | What it is | Status |
|---|---|---|
| HIL/203/299-300 (frame 255) | A card with an Arabic letter-to-number table (letters over the numbers 11-38) and three lines of dash-separated number groups under it, with an Arabic gloss ("send us the answer of Khalid ...", 875 and a name struck through). A second small card is taped above with a smaller table. | A key sheet with its own sample lines; no separate ciphertext letter follows it in the volume. A reading of the sample lines with the table is a key lookup, not a lead. Frame 255 is wave 18's "203/299-300". |
| HIL/203/302 (frame 257) | Typed French "COPIE" of a telegram text (birthday greetings, regret at missing the Khedive in Vienna, request for Said Kamil as aide to Chafik Pasha on a short Syria trip), with an Arabic note: "copy of the translation of the telegram from Baron Oppenheim at Constantinople, May 1915, to the Khedive in Vienna". | The plaintext of a cipher telegram of May 1915; the cipher form is not in the volume (203/299-300 may be its key). Material for a crib if the Oppenheim telegram turns up elsewhere. |
| HIL/203/293-298, 301 (frames 250-256, 258) | File cover "Correspondance avec Baron Oppenheim", typed letters on ink formulae, ink-strip specimens, cover addresses. | As wave 18. |

Frame numbering note: wave 18 wrote "frames 246-258" for HIL/203/288-303; by this manifest those labels sit at frames 249-263 (0-based).

## Badator (RAH Salazar y Castro index and Basque archives), terms not yet run

Portal `https://www.artxibo.euskadi.eus/webartxi00-container/es/ad53aArchivoHistoricoWar/badator/maintSimple?locale=es`; type the term in the box
(click, type, Enter; wait about 3 s after the page loads or the typing is lost), read the result page. No export was downloaded.

| Term | Records | Verdict |
|---|---|---|
| criptograma | 0 | none |
| zifra | 0 | none |
| cifrista | 0 | none |
| cartilla de cifra | 0 | none |
| cifrar | 8 | Marino Caracciolo and Alonso Sanchez to Charles V, Venice 24 Mar 1525, "en cifra", decipherment not found (already in the Caracciolo family, lead 2868 and the Sanchez target); one 1827 Madrid letter (clear, a search hit on the verb); the 1869-70 telegram bundle; four 1936-37 items of the Basque government's finance department ("telegrama para cifrar" copies, Prieto to Aguirre, already viewed in wave 10: clear). Nothing new. |
| nomenclator | 98 | Census and place-name "nomenclator" lists (Legazpi, Busturia, Murelaga, Navarre judicial districts ...). First page of titles read; noise. |

## Hosts probed for the notes' unswept list (no yield; recorded so the next sweep skips them)

| Host | Result (25 Nov 2026) |
|---|---|
| Valencia ARV catalogue SAVEX (`savex.gva.es/flora/jsp/index_opac_es.jsp`, linked from `arv.gva.es/es/cataleg-savex`) | Error page in Chrome again (also dead on 15 Nov). The ARV site `arv.gva.es` itself loads. |
| Sardinia (`archiviodistatocagliari.cultura.gov.it`), Sicily (`archiviodistatopalermo.cultura.gov.it`) | DNS or connection error in Chrome and curl: needs another network line, as in wave 16. |
| SIUSA (`siusa-archivi.cultura.gov.it`), `archivioitaliano.sardegna.it`, `sian.an.gov.br` pages, `hr-dadu.hr`, `nationalarchives.gov.lk`, `portal.archivosdeandalucia.es`, `consulta.archivogeneral.gov.co`, `bvpb.mcu.es`, `anrb.gov.ph`, `catalogo.bn.gob.pe`, Brazilian BN | No connection from curl. |
| `pares.cultura.gob.es`, `hispana.mcu.es` | HTTP 429 on the first request. |
| `bdh.bne.es`, `europeana.eu`, `nationalarchives.gov.ph`, `bn.gov.br` | HTTP 403 to curl. (BNE Digital stays off limits without BNE's permission, per COVERAGE.) |
| Biblioteca Nacional Digital de Chile (`bibliotecanacionaldigital.gob.cl`, search is a script-drawn page; type the term in the box) | Opens. "carta en cifra" 1 hit (a Ricardo Palma letter of 1905, not cipher), cifra 13 (articles on Borges' "La cifra", the Palma letter, Aguirre Cerda mini-site), cifrado 4 (poetry, Memoria Chilena minisites), cifrada 1. Noise, as for Memoria Chilena. |
| Archivo Nacional de Chile (`archivonacional.gob.cl`) | Site opens; no item-level catalogue address found (`/sitio/Contenido/Catalogo` is a 404); the online catalogue named in its copy-request page was not located. |
| Biblioteca Digital de Castilla y Leon (`bibliotecadigital.jcyl.es`) | Opens; the search URL guessed (`catalogo_imagenes/busqueda_simple.do`) does not exist and the header box did not submit; not swept. |
| NAAIRS (South Africa) `www.national.archsrch.gov.za` | No response in 12 s from curl; `nationalarchives.gov.za` home (narssa) opens, no search form tried. |
| Argentina AGN, Costa Rica AN, Mexico AGN (gob.mx/agn), Uruguay, Peru AGN | Answer curl (200/301/404/406) with institutional pages only; no item-level search found in one request each. |

## Left

- Valencia, Madrid regional (ALTCHA box, needs the user), Canarias beyond the Omeka search, Sardinia and Sicily: same blockers as before.
- Latin America: the national archives open as sites but no item search was found on any of them; the next try should start from a named
  catalogue address (Chile ANH "Catalogo en linea", Brazil SIAN "Consulta", Colombia SIA) found through a library guide, not the home page.
- BDCYL search form (Castilla y Leon digital library) and NAAIRS: reachable, search not driven.
- Durham: nothing left that is described as cipher, telegram or code except the code books HIL/150, 152, 154 (sampled in wave 18, 40-130 frames each) and the
  HIL/64-65 dictionary-code telegrams (about 133, no ciphertext to read).
