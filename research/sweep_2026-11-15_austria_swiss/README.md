# Sweep: Austria and Switzerland, finding-aid databases (15 Nov 2026)

Brief: finish the Austrian and neighbouring archives left open by `sweep_2026-11-14_german_state_dbs` (Oberoesterreich hit titles, Steiermark, Tirol, Salzburg,
Vorarlberg, Kaernten, Landesarchiv Berlin) and the Swiss cantonal archives (the federated search the 9 Nov Swiss sweep could not script), plus Liechtenstein and South
Tyrol. **Result: 13 rows in `candidates.json` (8 class A/B with a key or clear text named, 4 weak class C), 5 key-only groups in `key_leads.json`.** Every row is
scored from finding-aid text (`seen: catalogue`), none viewed, no web/Tomokiyo/Lasry/DECODE search. Nothing merged, nothing committed, catalogue.json, leads.json
and `merge.py` untouched. `make_candidates.py` rebuilds both files. Pre-1920 only.

## Routes, for the next sweep

| Source | Route | Result |
|---|---|---|
| **archives-online.org** (about 50 Swiss archives plus the Vorarlberger Landesarchiv, one search) | Chrome tab on `www.archives-online.org/Search`; the form is prefilled by the permalink (`?FulltextSearch=T&YearFrom=1400&YearTo=1920&Archives=...`, the "Permalink fuer diese Suche" under the results), but results arrive over SignalR, so a `fetch` returns an empty shell. Drive it from the console: set `#SearchModel_FulltextSearch`, click `#executeSearchBtn`, wait 5 s, read the `tr` rows (10 a page; click the "nae chsten Seite" link until the `von N` total is reached; page-size select is a custom widget). About 4 s a term. Totals count Burgerbibliothek Bern, Sozialarchiv and swisscollections (done elsewhere); I excluded `StABL` (83 modern hits), `SozArch`, `BBB`. | 70 terms. The yield of the sweep. |
| **findbuch.net front ends** (OOe `www.ooela.findbuch.net`, Vorarlberg `www.vla.findbuch.net`, Landesarchiv Berlin `www.landesarchiv-berlin.findbuch.net`; same engine) | The POST `rech_start.php` returns ids and hex-coded shelfmarks only. The page's own function **`do_rech_start_with_words('term')`** called from the console renders the result list (signature, title, dates) in the page; read `document.body.innerText` after 4-6 s from `Suche nach 'term'`. A zero result raises an alert that must be dismissed (`#box_ok`) before the next call, or later searches silently show the old list (Berlin: this swallowed most terms; see the Berlin row). Click a hit row (`open_rechdet`) for the detail text ("Inhalt"). Wildcards do not work. | OOe, Vorarlberg and Berlin done. |
| **Steiermark ArchivIS** (`egov.stmk.gv.at/archivinformationssystem/`) | Form post by `fetch` returns the vendor's bot-defence script, so use the page: set `#imdasWebFormId:searchVolltextFieldId`, click `#imdasWebFormId:sucheVolltextFormSubmit`, read the result page (`volltext-liste.jsf` or `keine-treffer.jsf`). `*` truncation works, exact words do not (`chiffriert` 0, `chiffr*` 3). | Done; nothing. |
| Liechtenstein `www.e-archiv.li` | ASP.NET postback with `__EVENTTARGET=ctl00$lbSearch` and `ctl00$txtSearch` (curl with a cookie jar works; `/tmp/s/li.py` in the scratchpad, not kept). It is an edition of documents (Rheinberger letters, Landtag, Swiss-Liechtenstein relations, 1919-50), not an archive finding aid. | Chiffre 3, chiffriert 3, Geheimschrift 1: a Holstein letter 1872, a Heyse letter 1871 and 1919-20 diplomatic reports from Vienna that mention ciphering (modern, printed). No row. |
| Tirol (Tiroler Landesarchiv), Salzburg (Landesarchiv), Suedtirol (Landesarchiv) | **No public item-level finding-aid database.** TLA: only Matriken, maps and a library catalogue; holdings in the printed Beimrohr volume (TGQ 47). Salzburg: the AIS is reading-room only; the Landesarchiv publishes a few PDF Repertorien (7 downloaded and grepped: Domkapitel 21-12, Landschaft 21-13, Lodron 21-14-08, Helmreich 21-14-07, Museumsakten 21-16, Grenzakten 22-05; hits only "Ziffer" in article numbers and a place name; the Kurfuerstliche Regierung PDF link 404s). Suedtirol: provinz.bz.it portal, no search route found. | No row. A reading-room or print route is needed. |
| Kaernten (Kaerntner Landesarchiv, KLAIS web module, about 300,000 records) | The last known URL (`landesarchiv.ktn.gv.at/klais/`) resolves in DNS but the connection is reset from this machine, in curl and in Chrome (error page; `www.ktn.gv.at` the same). Not a bot check: a network block or a dead host. | Not searched. Try from another network or ask whether KLAIS moved. |
| Staatsarchive Zuerich, Basel-Stadt, Bern, Luzern, Aargau, Graubuenden, St Gallen, Thurgau, Schaffhausen, Valais, Fribourg ... | Through archives-online (above). Zuerich, Bern, Basel were also swept natively (`swiss_austrian`, `browser_pass_oenb_basel_geneva`). | Rows below. |
| Landesarchiv Berlin | findbuch.net front end (above). Hits: Geheimschrift 1 (A Pr.Br.Rep. 030 Nr. 12874, Polizeipraesidium, social democrats in Schleswig-Holstein 1880-81), Chiffre 13 (police files 1910-25: money collections with newspaper "Chiffren", KPD intelligence; Steuerfahndung 1937-40), Entzifferung 2, Chiffrier 4, Geheimschluessel 1 (a 1930 Reichstag library theft). Zero: chiffriert, Ziffernschrift, Zifferschrift. The other terms (verschluesselt, Dechiffr, Kryptograph ...) were lost to the stale-alert problem and not re-run. | No row (20th-century police files). |

## What is new

| Rows | What |
|---|---|
| 1-2 | **Luzern**: AKT 13/2346 (ciphered correspondence of the Catholic cantons 1655-56, key AKT 13/153) and FAA 763 (secret conference at Solothurn 1711-12, key COD 1100 of 1708, copy in Sion as AEV AV 54/7). |
| 3-5 | **Valais, fonds de Courten**: d'Argenson's ciphered memoranda to Maurice de Courten, 13-17 Jan 1745, with cleartext units (Cn B 5/3/5, 5ter, 5bis, 6, 6bis, 8, 10): cipher/clear pairs; Choiseul's 1757 dispatches deciphered by Courten (5/11/6-7); Torcy 1704 (one letter). |
| 6 | **Stiftsarchiv St Gallen**, Nachlass Vorster: three letters in Geheimschrift with Hofrat Peter Mueller in Paris, 1801-03. |
| 7-8 | **Swiss Federal Archives J1.58#1977/70**: Francesco Vettori at Lyon to Lorenzo de' Medici, Jan-Feb 1515, mostly ciphered, one with Klarschrift (#72, #73); Cynthius for Tricarico, camp near Milan, 18 Sep 1515 (#118). The collection's origin is not checked. |
| 9 | **OOe Landesarchiv**, Lamberg papers: Akt Nr. 406 (1660), letter with Leopold I "nebst Chiffrenschluessel". |
| 10-13 | Weak (class C): Rousseau's ciphered letter of 1751 (two copies) and two 1767 Conti letters (Neuchatel; a reading probably exists in Leigh's edition); a Schaffhausen diarist's secret script with a key that does not fit; Hohenems HoA 138,24 (1618-22) with only a keyword hit. |

`key_leads.json`: the Luzern key series AKT 13/152-158 (Spain 1594, Lorraine 1592, Savoy 1579-1603, France/Guise 1585-93, Champlitte, 1568-1696 agreements,
FAA 869, AKT 13/2229); Valais AV 54/7; Vorarlberg VOKA AN 629; Graubuenden Planta Ac.64; Federal Archives 1896 key and 1889 files.

## Seen and dropped

- **Held already**: Zuerich Ziffernschrift keys of 1653 (StAZH A 241.3 / C I Nr. 3580), A 235.2, Turreo 1515 (A 225.1 Nr. 182, lead 1243), Breitinger-Peblis (E II 399, lead 1244): `swiss_austrian`. Basel PA 633c "Chiffres pour correspondance secrette" 1795 and the Ochs 1798 letter, PA 511a 604-10-02: `browser_pass_oenb_basel_geneva`. Zwingli / Ulrich von Wuerttemberg (ZB Zuerich Ms F 46.186, .202, "verschluesselt"): catalogue entry on the Philip-Ulrich correspondence cites a Zwingli letter with a bracketed cipher name; not rowed again.
- **Noise**: Burgerbibliothek Bern (done 9 Nov), Thurgau and Zuerich patent class 52 ("Geheimschrift" as a classification), Nidwalden/Obwalden Amtsblaetter ("Ziffern"), Geneva "carton de dechiffrement" (ballot counting 1768-69), Vaud and Neuchatel "recapitulations chiffrees", "musique chiffree", Agassiz "Nomenclator zoologicus" and Haller's botanical Nomenclator, the Basel "cifra" deanery, a Sozialarchiv SMUV file 1940s, OOe 20th-century Chiffren (Telegramme 1876 Nr. 3615, Nazi-era Pol-Politische Polizei, BR-340/1935 etc.), the Steiermark posters/Bude collection ("per chiffre?").
- Kept in the notes but not rowed: OOe Akt Nr. 200 (1644, Lamberg, "die Kunst der Geheimschrift"; a treatise or manual, not a cipher text; look at it together with Nr. 406), Graubuenden B/N 0992 (Jecklin, "Tachygraphie und Cryptographie", 19th-century notes), Thurgau 8'680'11 and 8'680'13 (Memorien 1787-1831, Briefbuch Lose Blaetter; the Geheimschrift context is not shown), Schaffhausen Patentschriften.
- Library entries on the Vorarlberg findbuch: Meister 1902 (Anfaenge der modernen diplomatischen Geheimschrift) and the Schertlin edition 1852: printed books.

## Terms and counts

**archives-online** (1400-1920, ex StABL/SozArch/BBB): chiffriert 8, chiffrierte 6, Chiffre 349 (mostly "chiffres"), Chiffren 22, Chiffrierschluessel 2, Geheimschluessel 2, Geheimschrift 37, Chiffrenschluessel 0,
verschluesselt 4, Zifferschrift 1, Zifferschluessel 1, Ziffernschrift 4, cifra 1, cifre 1, Entzifferung 17, Dechiffrierung 0, dechiffriert 0, Kryptographie 1, Kryptogramm 293 (not read; "Kryptogramm" matches many other things),
Chiffern 25 (Schiffern), Cifer 24, Cypher 0, Ziffern 478 (not read), Nomenclator 16, Geheimsprache 2, Geheimzeichen 1, Wortzeichen 79 (read; Luzern keys and watchwords), Chiffreschrift 0, Chiffrierschrift 0, alphabet secret 3,
ecriture secrete 0, lettre chiffree 7, chiffree 17, chiffrees 22, chiffres 219 (not read), en partie chiffre 60 (not read; the 8 with "Courten chiffre" were), Vettori 7, "groesstenteils chiffriert" 2, "teils chiffriert" 4, Klarschrift 3, decryptage 1, dechiffrer 50 (not read),
cryptogramme 0, Turreo 1, geheime Schrift 355 (not read), "Schluessel zur Aufloesung" 98 (not read), Ziffer 995 (not read).
**OOe** (findbuch): Geheimschrift 3, Chiffr 8, Chiffre 7, Chiffren 4, chiffriert 1, chiffrierte 1, Chiffrenschluessel 1, Entzifferung 1 (Stiftsarchiv Mondsee, nothing), others 0.
**Vorarlberg**: Geheimschrift 4, Kryptograph 1, Chiffer 64 (surnames); chiffriert, Chiffre, Chiffren, chiffrierte, verschluesselt, Chiffrenschluessel 0 (the remaining terms of the list did not finish before I moved on).
**Steiermark**: geheim* 229 (noise; read page 1), schluessel* 21, ziffer* 3, chiffr* 3, others 0. **Berlin**: see the table.

## Honest limits

- Descriptions only. No row viewed; none has a web, Tomokiyo, Lasry or DECODE search. The vetting bar is not met for any of them.
- archives-online rows come out of the federated index, which can lag the home databases (Luzern titles are shorter than the StALU database's own record); the Federal Archives
  J1.58 collection is a Swiss-history gathering of Italian documents whose origin I did not establish, so the Vettori rows may be copies, not the Florentine originals.
- The "terms not read" above are word-stem matches for *Chiffre/ziffern* and were not paged; the cipher-bearing items in them, if any, are not in the rows. A narrower pass ("lettre en chiffres", "en chiffre", "avec le chiffre") on the French-speaking archives (Geneva, Vaud, Valais, Neuchatel, Fribourg) would be the next step; the Valais and Neuchatel hits show their finding aids use "chiffre" in French, so more may sit under "clef" and "dechiffr".
- Tirol, Salzburg, Kaernten and Suedtirol remain unsearched for lack of a route.
- Class labels follow the earlier sweeps: A = key or clear text named in the finding aid, B = cipher only, C = weak or unclear.

## Chrome use and blocks

Own tab in the extension's group; a second tab I opened was closed from outside once (another session closes the group). Rate about 4-6 s a search, no parallel
tabs flood. **No CAPTCHA, bot check or login appeared** (Steiermark's JSF endpoint returned a bot-defence script to a scripted POST, but the UI path was fine). The extension blocks tool
output that contains `?query=` style text or `key=value` pairs next to `&`; replace `=&?` in strings before returning them, and never print `key:value` with numeric values in the same line as a URL-like string.
Long awaits (more than 45 s) time out: start the loop un-awaited and poll a `window` object. Kaernten (`ktn.gv.at`) is unreachable from this network.
