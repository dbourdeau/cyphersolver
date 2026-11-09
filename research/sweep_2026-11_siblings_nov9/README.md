# Sibling sweep (9 Nov 2026), seeds = the promotions of 9 Nov

Idea: a promoted cipher item usually has siblings in the same fonds or series that no keyword search finds. Seeds:
catalogue 2415-2446 (AGR Merode Westerloo, AD Gironde G 919, PARES Carlist units, SOA Plzen family archives, Berleburg
Ber.A M 20, Hin.A.Ak / Alm.F.Ak, GWA Recklinghausen, HStA Dresden, Het Utrechts Archief Amerongen, Moreniana Libri).

Result: **2 candidate rows** (`candidates.json`, built by `make_candidates.py`, both class B from the finding aid) and
**4 key-only items** (`key_leads.json`, `make_keys.py`). Both rows are siblings of seed 2446 (Torck, Huis Amerongen).

## The route that worked: archieven.nl OAI-PMH (new for the project)

`https://harvest.archieven.nl/OAI/OAIHandler` (open data, no key, no bot check; plain GET; `verb=ListSets` lists about 40
sets, `Open_data_<n>` per archive: 39 Het Utrechts Archief, 37 Gelders Archief, 239 Zeeuws Archief, 59 Haags GA,
236 Noord-Hollands Archief, 141 HC Overijssel, 5 Groninger Archieven, 235 BHIC ...). `metadataPrefix=oai_ead` returns
complete EAD inventories with item-level notes (a single fonds is 4-10 MB; ListRecords pages of 3 records take about
10 s; `oai_dc` returns nothing for these sets). `GetRecord&identifier=<guid>` fetches one fonds. This replaces the Chrome-only
Het Utrechts Archief inventory pages (curl gets JavaScript shells there) that the earlier Netherlands sweeps could not read.
`oai_cipher.py` streams a set and writes every component whose title or note matches cipher words
(cijferschrift, cijfercode, in cijfer, geheimschrift, chiffr*, cipher, "in code", ...). Output `oai_hits.jsonl`
(stream 1, Het Utrechts Archief; the family archives have the low toegang numbers and come first, so they are covered;
the run was stopped at the point noted below) and `oai_hits2.jsonl` (stream 2, Gelders Archief first; its first page is
very large and the run was stopped before it got further). The regex also matches "gecodeerd"/"in code" in modern
classification-code notes (noise, ignored).

Huis Amerongen (1001) read in full from the EAD (`amerongen_rows.json` not kept; 6256 components): cipher components are
inv. 2883 (key, 1671/1685, digitised), 3486-3488 (Torck, already catalogue 2446), **3534** (Hyndford, Breslau 1742,
"grotendeels in code": row), **3577** (cipher tables plus a coded letter from Berlin, 13 Oct 1736, digitised: row), 131
(date illegible, noise). The sibling letters of the foreign envoys in 3517-3534 (Demeraet, Dickens, Hop, Rumpf, Swart,
Burmania, Hamel Bruijninx) carry no cipher flag.
Huis Hardenbroek (1010): inv. 1191 (1780 code table, Hardenbroek-Lesteve) and 4515 (Doublet van Groenevelt key, 1762) = key leads;
Doublet's letters (inv. 989, 990) are not flagged.

Coverage when the harvests were stopped (all processes killed; progress files `*.progress.json` allow a resume):
Het Utrechts Archief 567 of 1564 EADs (fonds 1001 to about 1651, i.e. all family and institutional archives with low toegang numbers;
later numbers are municipalities and 20th-century bodies), Gelders Archief 1 record (its open-data set holds one EAD), Zeeuws Archief
244 EADs (0 hits), EC Achterhoek-Liemers 196 (only modern "in cijfers"/"ongecodeerd" noise), BHIC and Eindhoven sets 0-1 EADs.
Outside Utrecht the only cipher components in these sets are modern. Not harvested: Haags GA (59), Noord-Hollands Archief (236), HC Overijssel (141),
Groninger Archieven (5), Rotterdam (184), Rivierenland (102), Amstel-Gooi-Vecht (142), Westfries (136), Rijnland (319) and the small sets.

## Other seeds, what was tried

| Seed | Route | Result |
|---|---|---|
| PARES Carlist units (2421, 2422, 2425) | `series.py` on the parent "Correspondencia carlista" (PARES 3735630, 61 units: DC 161 N.1-22, DC 168 N.1-40, DC 190 N.4), `descs.py` for all 61 descriptions, images of 161 N.3 (Gomez Labrador, Paris, 13 pp) viewed | Only 161 N.2 says cipher in its description; N.3 plain Spanish. The other 59 units are personal letters, memorials, empty envelopes. No sibling row. |
| PARES DC 195 N.14 (2423) | parent "Correspondencia isabelina" (PARES 3900022, 13 units) | Found DC 167 N.19 (59 reserved letters of the Army of Reserve of Andalusia, Nov 1837-1838; 134 images) whose description mentions "claves para documentos cifrados". Viewed images 1-8 and a 12-image sample: it holds a **music-staff cipher key** (note to letter table, 30 Nov 1837); letters sampled are plain. Key lead, not a row. |
| AHNOB TORENO C.71 (2424) | parent 4036163 (91 units), descriptions of C.71 D.30-32, C.76 D.61-234, C.48 D.216-223 | no other cipher; García Montes D.35-59 is the only one. |
| AD Gironde G 919 (2416) | Ligeo / archives.gironde.fr | **Blocked**: now answers with an Anubis proof-of-work page ("Making sure you're not a bot"). Not circumvented. |
| Landesarchiv NRW (2436, 2438-2440) | archive.nrw.de sufservice API | **Blocked** the same way (Anubis, 9 Nov afternoon; the morning sweep got through). Not circumvented, so Hin.A.Ak 2340-2350, Alm.F.Ak and GWA neighbours could not be listed. |
| Ber.A M 20 (2436) | LWL `mets.xml` titles for Ber.A_M 1-260 (`lwl_titles.py`, `lwl_ber_m.jsonl`) | Series M is a military/administrative bundle series (30 and 7 Years' War, Einquartierung, Muenzwesen). M 20 is the only cipher-titled one. Thirty Years' War correspondence bundles (M 31, 38, 41, 50 ...) have no cipher in the title; M 41 (28 images, microfilm) paged as a contact sheet: no number columns. |
| AGR Merode Westerloo (2415) | AGATHA EAD (14 MB) regex for code, clef, chiffre, cifra, cryptogr | Only no. 9750 itself; no sibling. |
| SOA Plzen Windischgraetz / Trauttmansdorff / Nostitz (2427-2433) | aron.soaplzen.cz API with klic, cifr*, Ziffer*, Schluessel, kryptogr*, chyfr*, tajn* | 0 new (cifr*/Ziffer*/kryptogr*/chyfr* 0). Item records are one-line titles; the cipher flag exists only where the earlier sweep's sifr* search found it. |
| HStA Dresden Loc. 02814 (2441) | archiv.sachsen.de search "Sackens" | fuzzy search (1708 hits of Sack*), no neighbour found; word searches already exhausted by the earlier sweep. |
| Moreniana Libri (2445) | Manus harvest copy (`research/sweep_2026-11_manus_italian_libs/_dl/detail.jsonl`) | Other Libri inserts (Palagi Libri 432 ins. 27, 59, 68, Carte Libri 9, 42, 46, 133) are ordinary letters; one (record 696696) mentions "decifrare" and numbers standing for names but no cipher text. Nothing new. |
| BNE Gayangos (1270, 1271) | off limits (no BNE Digital) | not done |

## Not done / what remains

- Finish the OAI harvest of the other archieven.nl sets (Gelders Archief, Zeeuws, Haags GA, Noord-Hollands, Overijssel, Groningen, BHIC ...):
  `PYTHONUTF8=1 python oai_cipher.py oai_hits.jsonl Open_data_37 Open_data_239 ...` resumes from `oai_hits.jsonl.progress.json`.
  This is the cheapest new route into Dutch regional family archives (Huis Bergh, Twickel, Zeeland and Holland regents) and should
  be a sweep of its own; the Nationaal Archief is not in these sets.
- Open Amerongen inv. 3577 in the Het Utrechts Archief viewer (digitised): decipher the Berlin letter of 13 Oct 1736.
- Retry archive.nrw.de and Ligeo later (Anubis) for the Westphalian and Gironde neighbours; or ask for Chrome access.
