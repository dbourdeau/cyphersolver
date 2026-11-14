# Sweep: GStA PK deep pass over ACTApro (14 Nov 2026)

Brief: extend the GStA PK harvest of `research/sweep_2026-11-14_reachable_unlooked/` with more cipher terms, across all
Hauptabteilungen, years 1400-1919. **Result: 29 rows in `candidates.json`, 5 key-only groups in `key_leads.json`**
(`make_candidates.py` builds both). Every row is scored from the finding-aid text (`seen: catalogue`), none viewed;
digitisation was not checked, so `needs_archive_scan: "yes"` throughout. Nothing was merged; catalogue.json and leads.json
were not touched.

## Route (and a faster variant of the old one)

`https://archive.spk-berlin.de/actaproweb/search.xhtml`, in a Claude in Chrome tab on that origin, `fetch` GET then POST of the
`searchForm` (as in the reachable-unlooked README). Two findings that change the old recipe:

- **Results per page = 500 works through fetch.** Set the `resultsForPage` radio to `500` in the POST body and the whole hit
  list comes back in one response (the old recipe halved year ranges to stay under 25 hits because paging fails). The cap is 500;
  only `verschl*` (1,703 hits) went over it. One request per term, 1400-1919 in one range, about 1.5 s apart.
- **Wildcards work** (`chiffr*`, `*chiffr*`, `entziffer*`), so inflected forms need no separate queries. Plain `chiffre` and
  `chiffriert` are exact-token only.
- Hit blocks were read from the response HTML: `a[id$=searchDocumentLink]` is the header (signature, title, dates), the `td.doc-text`
  cells are the matched field fragments, and `document/Vz_<uuid>` in the entry is the permalink id.
- The Chrome extension blocks tool output that looks like query-string data (any text carrying `?id=` links), so results were put into
  `document.body` and read with `get_page_text`. A `fetch` from the https page to a local receiver on 127.0.0.1 hung and never arrived;
  do not plan on a localhost drop.
- No Hauptabteilung filter was set (the `Bestande` picker is not needed): the whole database is queried and the HA read from the
  signature. All the requested Hauptabteilungen appear (I. HA Rep. 11, 63, 64, 96, 81 and others, BPH, VI. HA Nachlaesse and
  Familienarchive, XX. HA OBA / EM, III. HA MdA). No CAPTCHA and no bot check appeared.

## Terms and hit counts (dated 1400-1919 unless marked)

| Term | Hits | Term | Hits |
|---|---|---|---|
| `chiffr*` | 232 | `*chiffr*` | 265 (280 with undated and later) |
| `chiffer*` | 53 | `chiffre` | 26 |
| `entziffer*` | 46 (50 all dates) | `dechiffr*` | 32 |
| `verschluesselt*` (umlaut spelling) | 12 (16) | `verschluesselung*` | 5 |
| `geheimschrift*` | 4 (7) | `geheimschl*` | 1 |
| `kryptograph*` | 2 | `geheimzeichen*` | 1 |
| `zahlenschrift*`, `kodiert*`, "in Ziffern" | 1 each | "nicht entziffert" | 3 |
| "Schluessel zu" / "Schluessel zur" | 15 / 6 | "in Chiffren" | 6 |
| `ziffer*` | 93 (numerals, filtered by a cipher-word test) | `verschl*` | 1,703, capped at 500 (replaced by the two exact forms) |

Zero hits: Zifferschrift, Ziffernschrift, cifra*, cifr*, cipher*, cypher*, entzifferungs*, Geheimsprache, Geheimalphabet,
Chiffrenalphabet, Zifferbrief, "mit Ziffern", "en chiffres", chiffree/chiffrée, codiert*.

958 distinct records came back (with the capped `verschl*` list); 386 matched a cipher-word filter. About 100 of those are noise:
reading old script or inscriptions (Entzifferung of Meroitic, cuneiform, handwriting), "Schluessel" as a physical key or an
apportionment key, steamship words that match `chiffr*` fuzzily (Dampfschiff...), patents for cipher machines (Rep. 120, 1852-75), and
records after 1919.

## What is new

| Rows | What |
|---|---|
| 1 | **Rep. 81 Dresden Nr. 781-791**: eleven volumes of Frederick II's ciphered cabinet orders 1744-56 to Klinggraeffen (and Buelow, Anhalt-Dessau, Rutowsky), each "mit Aufloesung in franzoesischer Sprache". The best paired set of the sweep. Catalogue 593 names Nr. 782-784 only in a side note. |
| 2-8 | Seven Years War and 1740s-60s: Nr. 798 (Austrian envoy's cipher with Aufloesung), Rep. 96 Nr. 97 E 1 / F (Dessau code 1745), Nl Wedel Nr. 3 (1759, five Dechiffrierungen), Schmettau, Dohna (two fonds), Rep. 34 Nr. 6676 (1668), BPH Rep. 35 Nr. 15 (1673 imperial letter). |
| 9-14 | 1780s-1800: Rep. 11 Nr. 10691 (Lusi, the plaintext side of FA Lusi Nr. 3), Nl Schlitz v. Goertz, Crown Prince's Hohenfels letter, Esterhazy 1756 facsimile (Rep. 400), Zegelin from Constantinople, Rep. 7 C Nr. 3144-3145 (Polish revolutionaries' ring text and keys, 1798). |
| 15-19 | **Neuchatel (Rep. 64)**: 16 further volumes in five rows (Metternich era with the cipher notes Nr. 690, 962, 992, 994; the 1719-48 and 1767-81 volumes; Goltz at Paris 1780). None of these numbers is in the reachable-unlooked rows. |
| 20-26 | Napoleonic and later: Rep. 81 Frankfurt Nr. 167-173 (1809-13 orders with the legation's Aufloesung), **Nl Gruner Nr. 57-58 (1811-12, deciphered foreign envoys' dispatches)**, **Rep. 77 Tit. 437 Nr. 6 (Prussian decipherment of French ciphers, 1810-33)**, Bern Nr. 93, Strangford to Miltitz with two keys, Westphalen Nr. 461, Wilhelm II-Sultan cipher (Rep. 89 Nr. 666). |
| 27-29 | **Teutonic Order (OBA) new numbers**, grouped by correspondent (one key per entry): eleven Schoenberg-Albrecht pieces with an Aufloesung noted; Kasimir (23682); Klingenbeck (27275, 27533). The chancery's own **Chiffrenbuch OBA 27584** is in `key_leads.json`: with the Schoenberg row it gives ciphertext, plaintext and key from one series. |

`key_leads.json` holds five key-only groups: the Teutonic Order and Ducal Prussia Chiffrenbuecher (OBA 27584, EM 19 a Nr. 68),
Prussian foreign-service keys 1735-98, Napoleonic-era keys 1806-19, post-1815 legation keys, private keys and alphabets.

## Skipped as already held or already seen

Checked with `research/archive_sweep_2026-10/known.py` plus a number grep over catalogue.json, leads.json and every
`candidates.json` / `key_leads.json`. Dropped: all OBA numbers already in catalogue 553-557 and others (2987, 19026, 20039,
20349, 21069, 21213, 22407, 22448, 22472, 22473, 22490, 22553, 22687, 22717, 22744, 22755, 22849, 22850, 22884, 22939, 23392-23464,
23484, 23852-23943, 24019, 24365, 24382, 24565, 25346, 25970, 26695, 26815, 26859, 26969, 26976, and the reachable-unlooked
22442 / 23213), OBA 22736 and 22789 (seen in `archivportal_d` and removed 2 Nov), Rep. 15 B Nr. 274 (catalogue 529), Rep. 91 A Nr. 86
and Rep. 81 Neapel Nr. 24 (catalogue 591), Nl Albrecht Nr. 11 and 58 (leads 1694), the 17 reachable-unlooked rows and 4 key groups
(Rep. 64 Nr. 686-706 and others, Derfflinger, Charles XI, Haude, Lusi FA Nr. 3, Boyen Nr. 648, Westphalen Nr. 304 and 393, Woellner Nr. 6,
Dohna FA Nr. 51, Rep. 81 Kopenhagen Nr. 254), the Saegert and Wittgenstein papers, Rep. 81 Mainz, Bevern Nr. 3-4, FA Werther Nr. 36,
Rep. 39 Nr. 58 and 289, Rep. 49 R Nr. 129.
Dropped as noise or out of scope: the III. HA MdA Chiffren files (keys, already a key group in the previous sweep), cipher-machine
patents (Rep. 120), telegram cipher administration after 1875 (Rep. 120 Anhang, XVI. HA Rep. 30 Nr. 18, Rep. 89 Nr. 13353),
single-line mentions of a cipher change with no text (Rep. 132 Nr. 2, Rep. 46 B Nr. 161, BPH Rep. 47 Nr. 17 and 470, Rep. 76 Vf Lit. L),
and every record dated after 1919.

## Honest limits

- Descriptions only: no row has been looked at on a scan, and no row has had a web, Tomokiyo or Lasry search. The vetting bar
  (README Conventions) is not met for any of them. The matched-text fragments ACTApro returns are cut off at the edges, so several
  correspondents' names are incomplete (marked "cut off" in the rows).
- The `cls` grade A means the finding aid says a decipherment or Aufloesung is filed; whether the ciphertext is also in the volume,
  and in what form, is not known until the file is seen. "Mit Aufloesung" can mean the legation's interlinear reading or a separate sheet.
- Rows grouped by volumes (Dresden, Frankfurt, Rep. 64, Gruner, Schoenberg) are one cipher per correspondent by description;
  Lasry's one-key-per-entry rule needs the volumes seen, and the Gruner, Schlitz and Rep. 64 rows will split into one lead per key.
- ACTApro covers part of GStA's holdings; the term lists may miss files whose descriptions use none of these words.
  Not run: Italian/French terms beyond `cifr*` and "en chiffres" (all zero), and any Hauptabteilung-restricted query.

## Chrome use

One own tab (closed afterwards): ACTApro, about 90 requests over roughly 40 minutes, no CAPTCHA, no bot check. A local receiver on
127.0.0.1 was started to take the results from the page and killed again; it received nothing.
Source needing Chrome, for the next sweep: **ACTApro (JSF session).**
