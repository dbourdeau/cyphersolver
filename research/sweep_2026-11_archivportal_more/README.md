# Archivportal-D, more terms (2 Nov 2026)

Second sweep of Archivportal-D (archives sector of the Deutsche Digitale Bibliothek) after `research/archivportal_d/`
(26 Oct). `candidates.json` holds **82 rows**; every one is scored from the finding-aid text (`seen: "catalogue"`), none
viewed. `make_candidates.py` builds 78 from `harvest_filtered.json`; `add_rows.py` appends 4 from the last re-harvest.

## Method
- Public DDB Solr endpoint, no key, `fq=sector_fct:sec_01`, polite pace (1.5 s per page of 500). No bot check met; no
  Chrome used. `harvest.py` re-runs the harvest.
- Terms: Ziffer(n) (7,876 hits, almost all numerals), Schlüssel (5,181), Geheimschrift (384), Chiffern, Chiffre(n),
  Chiffrierung (121), chiffriert/-e/-en/-er, Entzifferung, Geheimschlüssel, Ziffernschlüssel, Ziffernschrift,
  Dechiffrierung, Dechiffrierschlüssel, Geheimzeichen, Geheimtinte, verschlüsselt, "mit Ziffern", "in Ziffern",
  "in Zahlen", Kryptographie, chifre and others (about 40 in all). The "first 200 chiffriert slots" of the central-archives
  sweep were already exhausted by the 26 Oct sweep, which paged every hit; this pass re-paged them anyway.
- Filter: cipher word (not Schiffer/Schiffrecht) in title or description, dated before 1920 or undated, minus
  Bundesarchiv/WWI-WWII/Stasi/Telchi noise, minus any item id already in a candidates file, leads.json or catalogue.json.
- Dedup: ids against all earlier sweeps (0 overlaps in the final file); `known.py` on shelfmarks of the added rows.

## Counts
Rows by period: 15th c. 5, 1497-1559 12, 1560-1589 2, 1589-1598 1, 1598-1610 2, 1611-1650 9, 1651-1700 13, 1701-1800 31,
1801-1900 7. Region: all Germany.

## Honest limits
- The 26 Oct sweep had taken almost everything that matches a cipher word; the last re-harvest (about 15,800 records in
  all) produced only **4 further rows**. The 78 earlier rows came from the first pass of this sweep through the
  looser terms ("Geheimschrift", "Chiffrierschlüssel", "mit Ziffern", "verschlüsselt").
- Many rows are key sheets or cipher instructions rather than ciphertext letters (classes B and C); the status field says
  which. Digitisation flags are per row (`needs_archive_scan`).
- Several finding aids give no sign of an Auflösung; rows with a decipherment noted were kept only when the key helps
  siblings.

## Not reached
- Archivportal-D items whose finding aid does not use any cipher word (a letter described only by its senders).
- Items where "Ziffer" appears with no other cipher term (7,876 records, numerals): not read.
- Kalliope, Hessian LAGIS and the Landesarchiv BW online finding aids directly (only what DDB carries).
- No scan viewed; no web search beyond `known.py`. Tomokiyo, Lasry, DECODE and edition literature not searched.
