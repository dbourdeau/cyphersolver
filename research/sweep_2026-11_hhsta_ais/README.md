# HHStA / OeStA Archivinformationssystem sweep, 2 Nov 2026

Source: archivinformationssystem.at (scopeArchiv), the Staatenabteilung series Spanien, Frankreich, England, Italien/Rom,
Türkei, plus Kriegsakten, Haus-, Hof- und Familienakten, Staatskanzlei and Reichsakten where the same terms hit.
Output: `candidates.json` (70 rows, built by `make_candidates.py`). All rows are leads for `merge.py`, not catalogue entries.
Scripts: `ais_search.py` / `run_terms.py` (full-text postback and paging, copied from `research/aut_hhsta/`),
`fetch_b.py` (detail pages, all labelled fields incl. Bemerkungen, 2.5 s apart). Scratch data is in `_tmp/` (git-ignored).

## Method and counts

- Plain `requests`, one request every 2.5-3 s. No bot check, no login, no Chrome needed.
- Terms run this session (new): Chiffern 53, Ziffer 71 (mostly personal names), Klarschrift 55, Entzifferung 6, entziffert* 5,
  chiffrés 5, geheime Schrift 18, Chiffer* 14, Chiffres 5, ohne Klarschrift 55, Chifferbrief 2, Chiffre-Schlüssel 3,
  teilweise in Chiffern 12. Zero hits: chiffrirt*, verziffert*, Ziffernschrift, cifrado, cifrato, Chiffernbrief.
  Terms already run by `research/aut_hhsta/` (chiffriert*, chiffrierte*, dechiffriert*, Dechiffrierung, Geheimschrift, Ziffern,
  Chiffren, verschlüsselt*, Cifra, Zifra, Ziffernschlüssel) were re-crawled by a parallel run; union of 755 records.
- What is new against `aut_hhsta`: that sweep fetched only records with a scan icon. The Spanien Varia, Frankreich Varia,
  England Varia and Familienkorrespondenz records have no scan flag, but their **Bemerkungen** field says
  "teilweise/großteils/zur Gänze verschlüsselt" or "teilweise chiffriert". The detail pages were fetched for all of them
  (about 400) and read for that field and for any "dechiffriert", "interlinear", "Klarschrift" or "aufgelöst".
- Dedup: every candidate was checked by AIS id and by series+number against catalogue.json, research/leads.json and every other
  `research/*/candidates.json` (35 dropped as already tracked, mostly Pötting/Trautson/Harrach volumes, Frankreich Varia 2-8-104, 3-99, 3-125,
  Kriegsakten 129-133 and 90-104 groups). `known.py` run on the correspondents (Sepeville, Donzelot, Zamboni, Mailath, Blumendorf,
  Basserodes, Kromprich, Isabella Clara, Erzherzogin Anna, Chamoy): no hit outside this folder.
- Dropped as deciphered: records saying "chiffriert und dechiffriert", "interlinear", "in margine dechiffriert" (most of England
  Varia 3-x, England DiplKorr, Türkei I 1550-57 Vrančić/Zay/Cernovich, Frankreich Varia 45-20) and Kriegsakten items with
  "mit Klarschrift". They are sibling keys, not targets. One further item (Kriegsakten 131-1-66) was dropped for the same reason.

## Rows by series

Spanien (Varia, Diplomatische Korrespondenz) 42; Kriegsakten 10; Türkei I 5; Familienkorrespondenz 5; England 4; Frankreich 3;
Reichsakten 2; Toskana, Staatskanzlei Acta secreta, GKA Rom (Firmian 1755) 1 each; the rest by hand. Roughly 17 are class B
("großteils/zur Gänze verschlüsselt", or a whole letter); the Spanien Varia volume rows are class C: **a volume of mixed letters
where AIS says only "teilweise verschlüsselt", so the amount of cipher is unknown until a scan is seen.**

Best: Chapuys → Hannart, 13 Oct 1539 (England Varia 3-3-9, "großteils chiffriert", with a deciphered sibling at 3-2-3);
Spanien Varia 5-6-5, 5-6-27 (Khevenhüller/Eggenberg 1623, "großteils verschlüsselt"); Spanien Varia 20-4-3 ("zur Gänze
verschlüsselt"); the 61 letters of Archduchess Anna of Poland (Familienkorrespondenz A 40-3); England Varia 5-2-26 and 5-4-17 (Latin,
largely ciphered, 1667 and 1681).

## Not reached, caveats

- Fewer than 60 distinct Spanien/Rom/Venedig rows are possible: the **Venice and Rome series (Italienische Staaten Rom/Venedig Varia)
  gave only 2 hits** for any of these terms, and Venedig none. Nothing was padded.
- Scans were not viewed (no image fetch), so every row is scored from the AIS text only (`seen: catalogue`). Whether the ciphered
  part is a whole letter, a line or a post-script is unknown; the many "Einsichtsakten" rows are especially vague.
- Years of undated records in volumes with no dated sibling (Spanien Varia 47-4-32, 65-2-90, 66-2-55, 66-2-76, Dipl. Korr. 23-24,
  Kriegsakten 137-2-45) are estimates, flagged in `make_candidates.py` (`GUESS`).
- Titles and correspondents are kept as AIS gives them (German); some correspondents are only partly parsed.
- Not searched: Maximiliana and Fridericiana (done by `aut_hhsta`), Kriegsarchiv WWI, AVA, FHKA Hofkammer series, series-level
  browsing of the archive plan (Archivplansuche), which could list Varia volumes whose Bemerkungen do not use these words.
- A second process was running `details.py` in the same folder (writing `_tmp/details2.jsonl`) while this one ran; both outputs were merged.
