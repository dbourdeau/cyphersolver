# Wave 15: libraries and regional portals (15 Nov 2026)

Script access only (curl / Python / WebSearch); no browser. Sources: KBR, BnL, Royal Danish Library manuscripts, HStA Dresden,
regional portals (Canarias, Madrid, Veneto, Sardinia, Sicily, Dutch leftovers). Rows: `candidates.json`. Raw output: `raw/` (not committed).

Note for COVERAGE.md: the "Not looked at, though reachable" rows for KBR/BnL, Danish KB manuscripts and HStA Dresden were stale.
Earlier sweeps had already run them in part: `sweep_2026-11_belgium_kbr_arch` (KBR, Van den Gheyn full text),
`sweep_2026-11_denmark_sweden_more`, `sweep_2026-11-11_nordic` and `wainut_leads_2026-11-03` (soeg.kb.dk Primo API),
`sweep_2026-11_austria_german_states` (archiv.sachsen.de `cps/suche.html`). This wave filled what they left.

## 1. KBR (Royal Library of Belgium)

- `https://opac.kbr.be/` and `https://belgica.kbr.be/`: **connection reset** to curl (TLS 1.2 and 1.3, HTTP/1.1, browser User-Agent) and to
  Python urllib ("Remote end closed connection without response"); plain http times out. Not a CAPTCHA page, the server drops scripted
  clients. `https://www.kbr.be/en/` answers 200. **Needs Chrome**: `https://opac.kbr.be/Library/search.aspx?SC=DEFAULT&QUERY=chiffre`
  (9 Nov note: results render by JavaScript after about 8 s, and the catalogue holds printed matter, not manuscript items).
- Nothing new from KBR in this wave. Van den Gheyn t. 1-13 was grepped on 9 Nov (see `sweep_2026-11_belgium_kbr_arch`).

## 3. Royal Danish Library manuscripts (soeg.kb.dk)

Route: Primo VE public API, no token needed (`primo.py kb ...`):
`https://soeg.kb.dk/primaws/rest/pub/pnxs?inst=45KBDK_KGL&vid=45KBDK_KGL:KGL&scope=MyInstitution&tab=Everything&q=any,contains,<term>&qInclude=facet_rtype,exact,manuscripts&limit=50&offset=N`
(the `qInclude` manuscripts facet removes the printed-book noise; wildcards work, e.g. `chiff*`). The shelfmark is in `display.lds01`,
the notes in `display.lds25`, provenance `lds03`. `www5.kb.dk/manus` does not connect; the old Gigas catalogue pages answer at
`https://permalink.kb.dk/permalink/2006/manus/719/dan/<page>/` (719 = Gigas I, 722 = Gigas II, 723 = Gigas III:1). Gigas I-II full text:
`https://archive.org/download/katalogoverdetst12kong/katalogoverdetst12kong_djvu.txt` (grepped for chiff/ciffer/ciffre/Ziffer/lønskrift:
only NKS 775 4to and NKS 1416 4to are cipher; the rest are royal monograms on bindings).

Terms (manuscripts facet, hits): chiffer 2, chiffre 3, chiffré 3, "i chiffer" 2, ciffer 1, cifferskrift 2, chifferskrift 1, lønskrift 4, Ziffern 1,
cifra 1, déchiffrement 1, chiffernøgle 1, "med chiffre" 2, steganographia 1, "secret writing" 4; wildcards chiff* 9, chif* 9, ciff* 16, cifr* 3,
dechif* 2, déchif* 2, ziff* 4, krypt* 3, crypt* 1, lønskr* 5, geheim* 573 (filtered to lines with schrift/chif/ziff/alphabet), hemmelig* 83
(same filter), karakterer 6, code 12, kode 3, stenograf* 8; zero: chiffrer, chiffreret, chifre, chiffres, chiffrée(s), "en chiffres", Chiffern,
chiffriert, chiffrirt, Chiffren, Geheimschrift, cipher, cypher, "hemmelig skrift", dechiffreret, dechiffrering, déchiffré, chiffreskrift,
Zifferschrift, kryptografi, zifr*, ciph*, cyph*, tegnskrift.

Result:
- **Row: NKS 775 4to**, J. F. Tautte (1697-1777, colonel, Platz-Major of Copenhagen), "Der Staat von dem Königreiche Dännemarck, oder
  Zuverlässiger und unpartheyischer Entwurf von dem Caracter verschiedener Generals, Ministers und anderer Königlichen Bedienten",
  570 pp. + index, "Autograf; skrevet i chiffre" (Gigas I p. 270-271: "Autogr., skreven i Ciffre"). Not in any repo ledger; the 9 and 11 Nov
  KB passes missed it. No image seen; no digital copy linked from the record. Two web searches found no edition or decipherment.
- Keys and decipherments (no row): NKS 1416 4to (key list, already a key lead); NKS 2003 g 4to "C. C. Erlund's Nøgle til hans Cifferskrift"
  (120 pp.; already a key lead; Erlund is the decipherer in `targets/stenbock1713`); Thott 2186 4to "Ciffre de anno 1700 ... Jacob Schmidz in
  Hambourg vor Baron Görtz" (key, already a key lead); Thott 844 4to "Von Ziffern, d. i. von Cantzeley- und andern verborgenen Schriften"
  (treatise); Additamenta 163 4to Gøhr 1750 (already in the catalogue).
- New for vetting, not rows: **[NKS 637 folio], now in Rigsarkivet (handed over 1888)**: "Copiæ Schwedischer und Andrer mit Ciffres
  geschriebenen Brieffen, so in diesen letzten Kriegen in den Jahren 1657, 1658, 1659, 1660, intercipiret ... undt auf Befehl d. K. M. zu
  Dannemarcken deciffriret worden, von Zach. Lundius" (Gigas III:1 p. 148): the Danish decipherments of intercepted Swedish cipher letters,
  1657-60; a crib and key source for any Swedish cipher letter of the Karl X Gustav wars. **Kall 436 4to**: "Neun eigenhändige, durch Hülfe
  J. R. Temlers dechiffrirte Briefe Christ. IV an den Kanzl. Chr. Friis in J. 1625-1626" (Schlegel's hand; deciphered). **NKS 1299 e folio
  nr. 273**: Molbech's copy of the cipher list attached to Christian IV's letter of 30 May 1627 to Christian Friis ("Dii Nye Characterer paa
  Danske"; the two originals went to Rigsarkivet in 1889). **GKS 510 folio item s**: "Lettera in cifra al S. Cardinale Bichi, Nontio in
  Francia, intercetta" in a 17th-c. Italian tract volume (most likely a clear copy of a deciphered intercept; not seen).
- Noise: Kloge Søren's Cyprianus and the rune/"lønskrift" alphabets (Nordic sweep rows already), royal monograms ("Chr. IV's chiffre"),
  Ziffer song notation, Vilhelm Thomsen's Orkhon decipherment papers.

## 2. Bibliothèque nationale de Luxembourg (a-z.lu)

Route: the same Primo VE API answers without a token (`primo.py bnl ...`):
`https://www.a-z.lu/primaws/rest/pub/pnxs?inst=352LUX_BIBNET_NETWORK&vid=352LUX_BIBNET_NETWORK:BIBNET_UNION&scope=DN_and_CI&tab=DiscoveryNetwork&q=any,contains,<term>`.
It is the union catalogue of printed and audiovisual holdings. The `facet_rtype,exact,manuscripts` filter returns only music manuscripts
("lettre" 4, all `bnl_music_manuscript`); "chiffre" with that filter 0. Unfiltered local counts: chiffre 34,944, chiffré 33,759 (stemmed;
"chiffre d'affaires", statistics, films), "lettre chiffrée" 87, "lettres chiffrées" 59, Geheimschrift 222, chiffriert 100, cryptogramme 14,
"déchiffrement lettre" 12: first 50 of each read by type, no manuscript or archive record among them. **No item-level catalogue of BnL
manuscript letters is exposed there; 0 rows.** `eluxemburgensia.lu` (newspapers and printed matter) was not searched again.

## 4. Sächsisches Hauptstaatsarchiv Dresden (archiv.sachsen.de)

Route (as on 9 Nov): `https://www.archiv.sachsen.de/cps/suche.html?q=<term>&offset=N&pagesize=10`, plain GET, 10 per page (`sax_harvest.py`).
The search is fuzzy and unquoted: "geheime Schrift" returns 2,243 records (any of the words), "Ziffer", "Ziffern" and "in Ziffern" all return
the same 318 **fonds-level** descriptions (links `bestand.jsp?oid=..&bestandid=..`, no `guid`), which the 9 Nov harvester skipped; they were
paged here (`raw/sax_ziffer.jsonl`) and hold one cipher item (Loc. 08485/04, a key volume already known).
Terms new in this wave (hits): Ziffernschrift 0, Chiffern 1, chiffrirt 0, chiffrirte 0, "in Chiffern" 1, Chiffreschrift 1, Zifferschrift 0,
Ziffer 318, entziffert 0, Entzifferung 3, Dechiffrierung 1, Chiffres 56, Chiffrierung 1, Chiffreschlüssel 0, Zifferschlüssel 0, Geheimschriften 23,
"geheime Schrift" 2,243 (all paged, filtered to cipher words), Kryptographie 0, Chiffrebriefe 0, Chiffrendepeschen 0, Nomenklator 0,
Ziffren 0, Ziphern 0, "Chiffre-Schlüssel" 1, Chiffrierschlüssel 0, dechiffrierte 6, Chifferschrift 0, Geheimchiffre 0.
2,281 unique records; 100 with a cipher word (`raw/sax_new.txt`); nearly all are the key volumes and items already in the ledgers.

New:
- **Row: 10026 Geheimes Kabinett, Loc. 03234/06** (1692ff.): "Chiffren (wahrscheinlich von der französischen Gesandtschaft zu Warschau und aus
  den Jahren 1692-1697 herrührend; Chiffres avec Monseigneur le Cardinal Albani de S. Clement avec Lagnasco à Rome et Lomaca, **avec une
  feuille non dechiffrée**; zwei Pakete Chiffen, von der Gesandtschaft zu Wien herrührend)". The volume was known as a key lead; the
  undeciphered sheet lying with its own keys was not noted. No scan icon.
- **Row: 11237 Geheimes Kriegsratskollegium, Loc. 10922/01** (1724-25): arrest of Captain von Löwenburg at Naumburg for his ties to Stanisław
  Leszczyński, "Enthält u. a.: Haftbedingungen.- Verhörprotokoll.- Zettel mit Chiffren." No scan icon.
- Decipherments (no row): 10026 Loc. 03422/13 and 03422/14 (1735), "Konzepte zu Briefen (des Grafen von Wackerbarth), meist an Kardinäle und
  andere Geistliche, und dechiffrierte Briefe in italienischer Sprache".
- Context (no row): 12527 Nachlass Friedrich Christian Nr. 266, Brühl to the Electoral Prince 1739-52, "Verwendung von Geheimschrift" among
  the subjects, with a letter of Father Breinl (cf. catalogue 595, Breinl 1749). 12561 Nachlass Johann Nr. 012r, 1828 "Übungen in
  Chiffreschrift" (a prince's exercise). Flemming correspondence 1714-27 (digitised), "Leib, Entwurf einer Chiffren-Schrift, 1725" (a
  cipher design).
- For vetting: many of the Saxon key volumes now carry a digital copy ("#digitalisat" in the hit link), which the 9 Nov pass did not find:
  "Charaktere und verborgene Ziffern" (10024 Loc. 08485/04), "Fürstlich hessen-darmstädtisches Alphabet" 1640, "Paket: Allerhand Chiffren"
  1630ff., "Notiz über einige alte Chiffren" 1510-1573, "Allerhand Chiffren, so nicht mehr gebraucht worden (Bose)", "Verschiedene Chiffren
  in einer Mappe", "Des Geheimen Rates Chiffre", "Schlüssel für Chiffre-Schrift" um 1640-1670, "Chiffres [der Gesandtschaften]" 1701-1799,
  "Instructions et Chiffres pour Monsieur de Debrose" 1721ff., "Konzepte, Chiffren, Manifeste" 1706-09, August II's own draft of a cipher.
  Links are in `raw/sax_new.txt` (the viewer itself needs a browser, per `vetting_2026-11-14_german_state_dbs`).

## 5. Regional portals

### Veneto: SIAR (Sistema Informativo Archivistico Regionale)

Route found in the page script: `GET https://siar.regione.veneto.it/serverSiar/json/searchMetadata?request=<url-encoded JSON>` with
`{"caseInsensitive":true,"text":"<term>","actorId":"","archivi":{"tipo":["descrizione","unita","lettera","cartografia"],"denominazione":"",
"archiviFotografici":false,"conAlberoArchivistico":false,"conInventarioDigitale":false,"conDocumentoDigitalizzato":false,"conImmagini":false,
"conFilmati":false,"progetto":""}}` (`tipo` must be a list; that list is the "fino al livello delle unità" setting). `siar.py`.
Terms: cifra 7, cifre 9 (only series and fonds titles come back: tax registers "Estimi", "Campatico", "Gravezze", protocol registers, a poorhouse, fonds de Lazara, Secco, Zaccaria Demetrio; the records were not opened, the titles point to amounts and numerals),
and 0 for cifrato/a/e/i, cifrario, cifrari, "in cifra", decifrato/a, decifrazione, crittografia, crittografato, zifra, ziffra, cifera,
"scrittura segreta", "codice segreto", "linguaggio convenzionale", chiffre, crittogramma, cifrante. **0 rows.** SIAR describes municipal,
charity and family archives of the region; the state archives of Padua, Verona, Vicenza, Treviso, Belluno and Rovigo are not in it.

### Dutch regional leftovers

`sweep_2026-11-14_dutch_oai`, `sweep_2026-11-14_dutch_own_sites` and `sweep_2026-11-11_dutch_2` (archieven.nl site search, about 80 terms)
cover nearly everything. Tried here:
- **Regionaal Archief Tilburg**: the site embeds its Memorix endpoint and public key in the search page; finding aids answer at
  `https://webservices8.memorix.nl/archives/findingaids?apiKey=<key from the page>&keywords=<term>&lang=nl_NL&requestSolr=0&start=0&limit=30&flimit=1&view=context`.
  geheimschrift 1 (Plaatsingslijst collectie documentatie Tilburg; not opened), cijferschrift 0; "in cijfers", gecodeerd, "in code",
  ontcijferd, chiffre returned no matching text. 0 rows.
- **Open Archieven** (`https://api.openarch.nl/1.1/records/search.json?name=cijferschrift`): 0; it indexes persons, not file descriptions.
- West-Brabants Archief (`westbrabantsarchief.nl/collectie/archieven/zoeken?q=`): same Memorix widget, no key in the static page (loaded
  by script); not searched.
- Regionaal Archief Nijmegen `studiezaal.nijmegen.nl`: **403** to curl. Drents Archief and archieven.nl load (200) but draw results by
  script (as noted on 14 Nov). `www.rhcl.nl` redirects to `historischcentrumlimburg.nl` (home page only). Erfgoed Leiden: home page 200,
  search not reachable (as on 14 Nov).

### Canarias, Madrid, Sardinia, Sicily: nothing reachable by script

| Source | URL tried | Result |
|---|---|---|
| Memoria digital de Canarias (ULPGC) | `https://mdc.ulpgc.es/digital/search/searchterm/cifra`, `https://mdc.ulpgc.es/` | 200 with an Anubis page ("Making sure you're not a bot!"). **Needs Chrome.** |
| Archivo de la ULPGC (AtoM) | `https://atom.ulpgc.es/index.php/informationobject/browse?topLod=0&query=cifra` | answers; a 20th-c. university archive; no result line read for "cifra"; not pursued |
| Gobierno de Canarias archives | `www.gobiernodecanarias.org/cultura/archivos/` 404; `archivoshistoricos.gobiernodecanarias.org`, `archivostenerife.es`, `catalogoarchivo.tenerife.es`, `archivo.lalaguna.es` gave no connection (guessed hosts) | no catalogue address found for the two Archivos Históricos Provinciales; El Museo Canario (`www.elmuseocanario.com/archivo-2/`, Inquisition archive): no online item search found |
| Comunidad de Madrid, Archivo Regional (AtoM) | `https://gestiona.comunidad.madrid/archivos_atom/index.php/informationobject/browse?topLod=0&query=cifra` | **403, "Verificación de Seguridad" page. Needs Chrome.** |
| Memoria de Madrid (Archivo de Villa) | `https://www.memoriademadrid.es/buscador.php` | **403 Access Denied.** Needs Chrome. `archivodelavilla.madrid.es` gave no connection |
| Archivio di Stato di Cagliari, Soprintendenza archivistica della Sardegna | `https://sa-sardegna.cultura.gov.it/`, `https://archiviostatocagliari.org/`, `https://archivi.cultura.gov.it/`, `https://sias-archivi.cultura.gov.it/` | **connection reset** on every one (TLS handshake dropped, as earlier sweeps met at ASNa). Needs Chrome. `www.sardegnaarchiviovirtuale.it` does not resolve |
| Sardegna Digital Library, SardegnaCultura | `https://www.sardegnadigitallibrary.it/search?q=cifra`, `https://www.sardegnacultura.it/` | 200, but a photo/audiovisual library whose results are drawn by script; no archive descriptions; not pursued |
| Sicilian state archives (Catania, Messina, Siracusa, Trapani) | `asct.cultura.gov.it`, `archiviodistatomessina.cultura.gov.it`, `archiviodistatocatania.cultura.gov.it` | no DNS answer or reset; inventory PDFs exist under `asmessina.cultura.gov.it/fileadmin/...` and `archiviodistatotrapani.cultura.gov.it/fileadmin/...` (found by web search, not fetched). Needs Chrome or Wayback |
| Regione Siciliana | `https://www.regione.sicilia.it/` | 200, an administrative site with no archive catalogue; `bibliotecacentraleregionesiciliana.it` is a parked domain; `cricd.it` gave no connection |

Three web searches (Canarias "carta cifrada"; Cagliari "in cifra"/cifrario; Catania/Messina/Siracusa/Trapani "lettere in cifra") returned no
cipher item in these archives. **0 rows from these regions; they are not swept, only shown to be closed to scripts.**

## Needs Chrome (exact URLs)

- `https://opac.kbr.be/Library/search.aspx?SC=DEFAULT&QUERY=chiffre` and `https://belgica.kbr.be/` (connection reset to scripts)
- `https://mdc.ulpgc.es/digital/search/searchterm/cifra` (Anubis)
- `https://gestiona.comunidad.madrid/archivos_atom/index.php/informationobject/browse?topLod=0&query=cifra` (403 security check)
- `https://www.memoriademadrid.es/buscador.php` (403)
- `https://sa-sardegna.cultura.gov.it/`, `https://archiviostatocagliari.org/`, `https://sias-archivi.cultura.gov.it/` and the Sicilian
  `*.cultura.gov.it` archive hosts (connection reset or no DNS from this machine)
- `https://studiezaal.nijmegen.nl/` (403)

## What is left

- NKS 775 4to: view or order a few pages (letters, signs or numbers; is the title page in clear; is the whole text in cipher); check the
  Danish literature on Tautte (Dansk biografisk Lexikon, Fund og Forskning, Danske Magazin) for an edition or a decipherment; NKS 1416 4to
  and Erlund's NKS 2003 g 4to are keys of the same decades in the same library and should be tried against it.
- Dresden Loc. 03234/06: the undeciphered sheet needs a scan order; date Lagnasco's Rome mission and find the Albani key in the bundle.
- Dresden Loc. 10922/01: how many slips, ciphertext or key, and whether the interrogation record explains them.
- KB Copenhagen letter volumes (NKS, Thott, GKS envoy letters) are described without cipher words; only images would find more.
- KBR and BnL manuscript letters have no item-level online catalogue reachable by script (a-z.lu holds none at all).

## Files

`primo.py` (Primo VE harvest, KB and BnL), `sax_harvest.py` (the 9 Nov harvester with a shorter pause), `siar.py` (SIAR Veneto),
`make_candidates.py` -> `candidates.json` (3 rows, all class B). Raw, not for commit: `raw/primo_kb.jsonl`, `raw/primo_bnl.jsonl`,
`raw/kb_run1.txt`, `raw/kb_run2.txt`, `raw/gigas12_djvu.txt`, `raw/sax.jsonl`, `raw/sax_ziffer.jsonl`, `raw/sax_new.txt`, `raw/siar.jsonl`.
No image was fetched: none of the three rows has an image online.
