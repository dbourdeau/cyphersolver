# German portals sweep (2 Nov 2026)

Berlin SBB, Wolfenbüttel (HAB and the state archive), bavarikon, Arcinsys Hessen, Arcinsys Niedersachsen, Landesarchiv
Baden-Württemberg. Earlier sweeps reached these only through Archivportal-D and Kalliope; this pass used each portal's
own search in Claude in Chrome (same-origin requests, about one a second; no check solved or clicked by Claude).
`make_candidates.py` builds `candidates.json` (21 rows); merged into `research/leads.json` as ids 1967-1987.

## Result by portal

| Portal | Result |
|---|---|
| Landesarchiv BW (OFS) | Works. POST to `suche/ergebnis1.php` with the form's fields, `suche=<term>`, `trefferausgabe=500`. 28 terms, 1,162 unique hits, 292 dated to 1900 with a cipher word; 92 before 1750. Shortlist in `labw_selected.md`. Most of the real ones were already in the repo (Peasants' War 1525, Schertel, Osiander, Reichenau, Hatzfeldt, Gyllenstierna). New: H 55 Bü 20, We 5 Bü 1105/2955, A 48/05 Bü 51. |
| Arcinsys Niedersachsen | Works through the page: fill `filter.searchTerm` on `simpleSearch.action`, submit, read the server-side DataTable `#searchResultList` (`page.len(50)`, then each page). 6 terms, 190 unique records, 173 to 1900. Shortlist in `arcinsys_ni_selected.md`. |
| Arcinsys Hessen | Same software; **use `arcinsys.hessen.de` without `www`** (www gives 403). 6 terms, 108 unique, 97 kept. |
| bavarikon | Anubis proof-of-work passes by itself in about 5 s. Search field is `terms` (not `q`). Hits are printed-book full text and Neue Deutsche Biographie entries; nothing to add. Posthius to Eysenmenger letters (UB Erlangen, 1614, 1618) carry the key on the same sheet, so not targets. |
| Berlin SBB digital collections | Meteor app; read results from the rendered page after about 4 s. "Geheimschrift" 195 hits, one a manuscript (oriental); "chiffriert" and "Chiffre" 0. Manuscripts and Nachlässe are in Kalliope, swept earlier. Nothing to add. |
| Wolfenbüttel HAB (diglib.hab.de) | **Not reached**: browser error page in Chrome, TLS error 35 in curl, same as DigiVatLib. Try another network. The state archive (NLA Wolfenbüttel) is covered through Arcinsys NI. |

## Leads and vetting

21 leads merged, scored from descriptions. Two were vetted and promoted to the catalogue (archive-only, kind "not online",
prior art searched 2 Nov 2026): **Knörr's Vienna reports, NLA WO 2 Alt Nr. 580-589, 1727-49** (cat. entry from lead 1976) and
**Chancellor Vigelius's Vienna reports, HHStAW 130 I Nr. 400-412, 463, 1666-87** (from lead 1981). The other 19 stay in
`research/leads.json`.

Second pass (same day, "Vet more"): looked at every digitised unit and read the full archive description of the
ambiguous ones. Outcome by lead:

| Lead | Outcome |
|---|---|
| 1971 Heinrich the Younger and Philipp Magnus, 1553 (NLA WO 1 Alt 22 Nr. 42); 1972 Reuschenberg to an Elector, 1641 (NLA WO 250 N Nr. 1148); 1973 Schwartzkopf's partly ciphered reports 1657-60 (NLA WO 1 Alt 12 Nr. 1) | Vetted ("not online", prior art searched) and **promoted** |
| 1978 Münster papers, NLA HA Dep. 110 A Nr. 105 | **Closed, read at the time**: viewed aufn_085 and aufn_100 at full resolution; numeric code with French plaintext interlinear. Nr. 66, 113, 228 not checked (Nr. 113 aufn_030 is a clear English memorandum) |
| 1975 Fabrice reports 1711 (Cal. Br. 24 Nr. 6801) | **Closed, read**: archive title says "zum Teil d'chiffriert von Robethon" |
| 1984 Linker 1672, 1985 Waldeck 1744 | **Closed, duplicates** of catalogue 341 (`targets/hesse1672`) and 339 (`targets/waldeck1744`). Viewed 118 a Nr. 3954: dotted-number code, 8 images, no plaintext. The first duplicate check missed both because of "Nr." in the shelfmark |
| 1987 Ansbach "Adelaide/Eugenie" letters | **Closed, not a cipher**: plain French under society cover names (L'ordre de l'Énigme) |
| 1974 Grote to Mandelsloh; 1979 Cramm | Left open as leads: 1974's unit contains the cipher itself, 1979's Nr. 823 lists a Chiffreschlüssel (likely key lookups) |
| 1967, 1968, 1969, 1970, 1977, 1980, 1982, 1983, 1986 | Still unvetted leads |

Cautions from the sweep:

- **Hanoverian chancery material (NLA HA Cal. Br. 15/24, Dep. 110, Hann. 9g) is usually deciphered interlinearly**
  (`targets/mecklenburg1734`; confirmed again for Dep. 110 A Nr. 105), so lead 1977 (Knorre 1738) is probably read at the time too.
- Duplicate checks must ignore "Nr." in shelfmarks (`HStAM 118 a Nr. 3954` against `118 a 3954`); a norm() that drops
  the token "nr" found three duplicates the first pass missed.
- NLA HA full-size images follow `https://www.arcinsys-digitalisate.niedersachsen.de/nla_ha/dep._110/a_nr._<n>/m_ha_dep._110_a_nr._<n>_aufn_<NNN>.jpg`
  (curl works, 3175 px wide); the Arcinsys viewer's page box stalls, use `selectId` URLs or the image pattern.
- The Nassau-Diez row (lead 1982) is a finding aid of the Koninklijk Huisarchief papers held in The Hague.
- Landesarchiv BW print view per item works with curl: `ofs21/olf/druckansicht.php?id_titlaufn=<id>`.

## Tool notes

- The JS tool of Claude in Chrome truncates output at about 700 characters and blocks anything that looks like a query
  string; write rows into the page body and read them with `get_page_text`, and store harvests in `sessionStorage`
  across navigations.
- A POST from an https page to `http://127.0.0.1` hangs (local network access blocked); do not try a local receiver.
- Dropped as noise: Wertheim notarial "Chiffre" (45 parchments 1420-45), royal-monogram snuffboxes, bare key units
  (GLA 48 Nr. 65-84, NLA HA Dep. 103 VIII, StAB 2-Dd 8, HStAD D 4 141/2, HStAM 1 Nr. 2123).

## Key leads (bare keys, not rows)

NLA WO 2 Alt Nr. 2838 (Chiffern 1675-1725); NLA HA Celle Br. 92 Nr. 116-125 (Chiffren for Bothmer, Fabrice, Schrader);
NLA HA Dep. 103 VIII Nr. 1, 51, 118, 458-476, 500 (Hanoverian legation ciphers 1769-1870); NLA AU Rep. 241 E 16/17;
HHStAW 171 C 667, 171 Z 1807, 150 Nr. 787, 130 I Nr. 1576; HStAM 4 f Schweden 116, 253, 271; HStAD D 4 141/2, D 4 588/5.
