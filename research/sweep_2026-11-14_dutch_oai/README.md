# Dutch archives OAI-PMH harvest, remaining sets (14 Nov 2026)

Brief: finish the archieven.nl OAI-PMH harvest begun in `sweep_2026-11_siblings_nov9` (COVERAGE: "Noord-Hollands 430 of 2726,
Groninger 450 of 2794"). **Result: 5 rows in `candidates.json` (built by `make_candidates.py`), all scored from the inventory line,
none viewed; no strong lead.** The Dutch regional archives hold almost no flagged early-modern cipher items outside the
Utrecht Amerongen family (already catalogue 2446 and the Nov 9 rows).

## Route and recipe
`https://harvest.archieven.nl/OAI/OAIHandler`, `verb=ListRecords&metadataPrefix=oai_ead&set=Open_data_<n>`; `oai_cipher.py`
(copied from siblings_nov9) streams a set and keeps every component whose title/note matches the cipher regex (cijfer*, geheimschrift,
in cijfer, ontcijfer*, chiffr*, cipher, in code, cifra ...); `show2.py` filters noise (classification codes "gecodeerd met de letter",
"ontcijferd" = illegible, statistics "in cijfers"). Resumed from the Nov 9 resumption tokens (token = base64 `oai_ead|||SET|count|last-id`; the
count part is not checked, the id is the cursor). Up to six streams at once, each ~1 request per 3 s to 10 s; no 403/429 at any point.
Westfries's old token had been marked "done" in error and was rejected (badArgument); rebuilding it as `...|3|160655` resumed it.
Raw hits per stream: `hB` (Haags GA), `hD` (Rivierenland), `hE` (Westfries), `hF` (Noord-Hollands), `hG` (Groninger), `hX` (small sets).

## Coverage now (EADs read)
| Set | Result |
|---|---|
| Noord-Hollands Archief (236) | complete (to the end of the feed, about 2,700 EADs). 160 raw hits, nearly all 19th-20th-century notarial/domain deed codes. One cipher item: Penninck Hoofd (3248) inv. 141, undated note "in geheimschrift (met codering)" |
| Groninger Archieven (5) | complete (about 2,800). Rows below; also Menkemaborg 623 inv. 1597 "Datering in geheimschrift" (undated schoolbook), Fraeylemaborg 2393 inv. 353 (1866 notes "betreffende geheimschrift?", Thomassen), Systeemkaarten 2183 "Sleutel op de gecodeerde namen in het rapport van Bilkes" (WWII resistance, out of period) |
| Haags GA (59) | complete; 4 hits, all modern |
| Westfries Archief (136) | complete; 3 hits, none cipher in period (Wognum house numbering code, etc.) |
| RA Rivierenland (102) | complete; 0 hits |
| NIMH (2231), Dordrecht (46), Deventer (45), Roermond (103), Rijckheyt (62), Domijnen (111), HC Het Archief (2557), Rijnland (319), Waterlands (131), Noordwest Utrecht (386), Eemland (28) | complete; Dordrecht gives the 1783 Patriot letter and the lodge papers; NIMH only 1940-45 Japanese/Dutch resistance cipher material |
| GA Zaanstad (137) | part (about 430 records; hits are statistics "in cijfers") |
| Alphen (105), Voorne-Putten (126), Schieland (150), Goeree-Overflakkee (1950), Langstraat (128), Flevoland (35), NoVA (434), onbekend (2803, 2801), Kerkrade (72), Landgraaf (1949) | **not harvested** (stream stopped; all are municipal archives, 19th-20th c.) |

Het Utrechts Archief, Gelders, Zeeuws, HC Overijssel, BHIC, Eindhoven, EC Achterhoek-Liemers, Amstel-Gooi-Vecht, Rotterdam were done
in `siblings_nov9`. Not on the feed at all (no OAI route here): Tresoar, Drents Archief, Stadsarchief Amsterdam, Erfgoed Leiden, Nationaal
Archief (own sweep `nationaal_archief`; its API was not re-run here), so those need the Chrome route.

## Rows
1. Dordrecht, 'De Vrijheid' patriot society, toegang 325 inv. 44: J. van Meeteren (Dinther), 14 Oct 1783, "gedeeltelijk in geheimschrift" (B; best of the five)
2. Groningen, Catalogus 1032 inv. 735: copy of a 25 May 1594 report, "gedeeltelijk in cijfers" (C; a copy, original unidentified)
3. Groningen, Catalogus 835 inv. 256: Julsing diary 1589-94, already deciphered by Boeles and edited 2006 (C; duplicate guard, probably script mixing not a cipher)
4. Dordrecht, lodge 'La Flamboyante' 383 inv. 803 and 847: Masonic cipher papers, undated (C; pigpen-type)
5. Groningen, Nanninga 561 inv. 439: 1871 shift-alphabet tableau by J. M. Sijtsma (C)

Not rows: Penninck Hoofd inv. 141 (undated brief note), Menkemaborg inv. 1597 (a school-book date), Fraeylemaborg inv. 353 (1866 notes with
question mark), Groningen toegang 1109 inv. 487 and 3089 inv. 277 (Nov 9 sweep, already judged), the Nut van 't Algemeen "oud letterschrift" plates (script primer).
Dedupe: `known.py` on Julsing, Exercitiegenootschap, Buerenston, Nanninga, Flamboyante, Menkemaborg, Fraeylemaborg, Van Meeteren, Dinther: no hits (Penninck matches only Schimmelpenninck).
No DECODE, Tomokiyo or Lasry search was run for these rows.
