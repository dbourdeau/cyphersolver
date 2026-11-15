# Sweep: Omont / Ancien-fonds "avec chiffre" pieces in BnF Manuscrits (14 Nov 2026)

Brief: take the BnF printed catalogue's "avec chiffre" / "en chiffre" pieces without a noted decipherment (COVERAGE.md "new sources" row:
"Omont's BnF catalogue, about 150 pieces, blocked only by finding Gallica arks"), find shelfmark, date, correspondents, Gallica ark, dedupe.
**Result: 21 rows in `candidates.json`, 8 key-only groups in `key_leads.json`.** Nothing merged; catalogue.json and leads.json untouched.
Every row is scored from the printed entry (`seen: catalogue`), none viewed.

## Source and counts

The cloud session's downloads were gone, so the OCR was fetched again from archive.org (`<id>_djvu.txt`, curl works):
the Ancien fonds volumes `p1cataloguegnr01-05bibluoft` (the 1868-1895 Catalogue des manuscrits francais, fr. 1-6170) and the Ancien
Supplement volumes `p2catalogue02/g02/g03` (fr. 6171-15369). The Omont NAF volumes (`CatalogueBnfNaf*`) and Ancien Saint-Germain III are not
at archive.org under those ids (404), so **nouvelles acquisitions francaises and Saint-Germain remain unswept**; the Supplement volumes
carry almost only binding "chiffre" hits (fr. 7199 "Recueil de chiffres diplomatiques 1688-1713" is the one real piece).

`parse_omont.py` (heading "NNNN." lines, items, `avec chiffre` counts) -> `fixnum.py` (OCR heading numbers repaired within the tome range, 3<->5 and
similar) -> `summarise.py` (per volume, items with and without "et dechiffrement"; output `summary.json`, read in `detail.txt`) -> `dedupe.py`
(fr. numbers against the ledgers and sweeps) -> `make_candidates.py` (the rows). The scripts read UTF-8 explicitly (the first pass did not and
lost every accented "dechiffrement"; the counts below are from the corrected run).

- 244 headings with a cipher word, 222 resolved volumes; **310 explicit "avec chiffre" items without decipherment** and about 358 items counting
  "en chiffre"/bare "Chiffre" leaves, in 186 volumes. About 1,200 further "avec chiffre" items are marked "et dechiffrement" (a decipherment sits
  with them) and are left out.
- Of 135 volumes with a plain item: 45 already appear in catalogue/leads/targets/README/DECODE queue (the Mascon 1536, Raince/Ranzo, Gramont,
  Nevers/League, Bethune 1601-05, Herbault 1626 families), 7 only in Tomokiyo pages, 83 not found; about 15 of those are noise (a binding
  "chiffre", an index, a sum). The rest are the 21 rows; the fr. numbers are in `cls.json`.
- **OCR heading numbers are unreliable** (3 and 5 swap, 0/6, 1/7). The repair is by the tome's range; where Gallica has the volume its title was
  checked (fr. 3057 and fr. 3086 corrected this way: the Mary Stuart / Philip II volume is fr. 3057, not 3657, and the Ventadour 1597 letter is
  in fr. 3086, not 3686). Every other shelfmark in a row is the OCR reading, confirmed only when a Gallica ark is given.

## Gallica arks

Route: a Claude in Chrome tab on `gallica.bnf.fr`, same-origin `fetch` of `/SRU?operation=searchRetrieve&version=1.2&query=(dc.source all "Departement des Manuscrits Francais N")`
(accents as in the catalogue: `Département des Manuscrits Français 3231`). **The path `/services/engine/search/sru` is blocked by Cloudflare ("Sorry, you have been blocked");
plain `/SRU` works.** Records carry `dc.source` = "...Departement des Manuscrits. Francais N" and `dc.relation` = the archivesetmanuscrits notice `cc...`, so one query
gives ark and notice. curl to gallica still gets 403; `catalogue.bnf.fr` SRU does not index manuscripts; archivesetmanuscrits.bnf.fr answers curl but its simple search finds no
"Francais N" shelfmark.

**Rate limit:** the `/SRU` path returns HTTP 429 after a few requests a second and the response is an empty record list, which looks like "not digitised". A first
pass over 184 volumes was wrong for that reason and was redone for the 63 volumes of the rows at 3 to 4 seconds a request, with the HTTP status checked; an empty list in the second pass is
a real "no record". No CAPTCHA appeared; nothing was solved or clicked through.

Digitised on Gallica (ark, notice): fr. 2986 btv1b90601395 (cc494409), 2996 btv1b9060087w, 3027 btv1b9060066q, 3043 btv1b90598808, 3057 btv1b9060031h, 3086 btv1b9060039t,
3093 btv1b9060128c, 3137 btv1b90598660, 3157 btv1b90598645, 3231 btv1b90602383, 3232 btv1b9060226w, 3314 btv1b9060078x, 3373 btv1b9059612r, 3374 btv1b9059610x, 3638 btv1b9059321p,
4102 btv1b9007662n, 4137 btv1b9060192j, 5212 btv1b525026901 (full list with notices: `ark_map.json`). Already-known arks from `research/gallica_sweep/ark_shelfmarks.json` (32 volumes) were not repeated.
**Not found on Gallica** (no record, so reading room or microfilm): fr. 2935, 3329, 3339, 3409, 3422, 3437, 3614, 3624, 3634, 3646, 3652, 3689, 3730, 3796, 3823, 3826, 3834, 3837, 3855,
4691, 4697, 4733 and the Nevers key volumes 3336, 3361, 3454, 3810, 4030, 4471, 4703, 4720, 4724, 4725, 4727. Their rows are `needs_archive_scan: yes`.

## Rows (best first)

Scores follow the BRIEF (importance / solvability / difficulty); cls A = a decipherment in the same volume.

1. **fr. 3231 + 3232, Birago (Saluzzo) to Nevers 1570-72**, 14 letters, A, 3/4/2, Gallica for both.
2. **fr. 3057, Philip II / Mendoza / Ibarra, Spanish League-years ciphers 1589-92**, 7 pieces, A, 4/3/3, Gallica.
3. **fr. 3826 + 3823 + 3855, Richelieu to Rance at Susa, April-May 1629**, 10 letters, A, 4/4/2, no ark found (overlaps lead 1577 in subject; check at merge).
4. **fr. 3652 + 3339, Henri IV 1603 and Marie de Medicis / Villeroy / Puysieulx 1611-13 to Breves**, 22 letters, B, 4/4/2, no ark (microfilm volumes).
5. **fr. 2986, Ranzo and Raince, Rome 1526-27**, 27 "en chiffre" pieces, B, 3/4/2, Gallica.
6. **fr. 3329 + 3409 + 4717, letters to Humieres (Peronne) 1577-78 with two cipher tables in 3329**, A, 3/4/2, no ark.
7. **fr. 3373 + 3086, Ventadour to Montmorency 1597-98, key in 3373 f. 56**, A, 2/4/2, Gallica.
8. **fr. 3374 + 4697 + 4691, Nevers' minutes "avec chiffre" to Scipione Gonzaga and Camillo Volta 1585-86**, 3/3/3, partly Gallica.
9. **fr. 3624 + 3614 + 3634 + 3646, Nevers' League-years intelligence 1589-93**, B, 12 pieces, no ark.
10. **fr. 2996 + 3137, Morvillier (Venice) 1546/1549**, A (the Aug 1549 letter with decipherment is in fr. 3138 f. 70), Gallica.
Further rows: fr. 3422 (anonymous 1589 letters to Nevers), 3027 (Bonnivet volume, ff. 186-202), Monteleon 1617 (fr. 3638), Mende to Richelieu 1623 (fr. 3689),
Bouthillier/Chatillon/Conti 1633-49, Sabran memoir 1637 (fr. 4137), Lanssac Warsaw 1573 (fr. 4733), d'Ossat 1601 (fr. 3437), Salviati 1525, Cenalis, Louis XIII to Nevers 1618.

## Already covered or left out

- **Withheld by request, not touched:** fr. 3029 and fr. 3092 (Lasry); fr. 3092 also appears in catalogue.json.
- Volumes whose number is already a target, lead or catalogue entry, or in Tomokiyo's Nevers/League/Henri III pages (fr. 3255, 3281, 3323, 3978, 3980, 3992, 3994 hit only there, so
  folios may be new but the volume is his), and the Bethune run fr. 3484-3490 (lead "Henri IV to Bethune, 15 letters 'avec chiffre'"), Beaumont/Harlay 1603 (fr. 3489, breves1603 notes).
- Not rows: fr. 3093 Sormano/Joachim de Vaulx, Ferrara 1529, 4 "avec chiffre" pieces (Sormano is a target family here), fr. 3668 f. 69 (the Herbault 1626 target), fr. 3606, 3662, 3670, 3699, 3702
  (Coeuvres/Herbault to Bethune 1623-26: almost all "avec chiffre et dechiffrement"), fr. 5188 (Rohan 1636, already catalogue), fr. 3157 and 5212 (only a stray word).
- `key_leads.json`: bare key leaves in the same volumes (Nevers 1574 Cracow key fr. 3314 f. 12, Humieres tables fr. 3329, Bethune Scotland 1599 fr. 3454 f. 10, Hotman fr. 4030 f. 1,
  Du Bellay / Saumaise fr. 4471, the 1619-23 Nevers chiffres fr. 4720 and neighbours).

## Not done

- Web search for prior art on each row: only the repo grep (`known.py`, ledgers, Tomokiyo source pages). Several family names hit the ledgers in other contexts (Lanssac, Bouthillier,
  Ibarra); not tracked down.
- DECODE lookup by R-number for these volumes (views dumps were grepped only by fr. number and name through `dedupe.py`).
- The NAF volumes (Omont's Nouvelles acquisitions francaises) and Ancien Saint-Germain are not at archive.org under the ids tried; Gallica's own catalogue copies (BnF "Catalogue general des
  manuscrits francais" on Gallica) were not looked for.
- No page was viewed on Gallica; every status is "printed catalogue says avec chiffre, no decipherment noted".

## Blocks (for COVERAGE)

- gallica.bnf.fr `/services/engine/search/sru`: Cloudflare block page in Chrome; `/SRU` fine. Same host 403 to curl. 429 under more than about one request per 3 seconds, silent as an empty result.
- archive.org NAF / Saint-Germain djvu ids: 404.
