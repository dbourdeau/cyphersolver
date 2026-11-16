# Audit: shelfmarks of the Omont-derived leads and catalogue entries (16 Nov 2026)

Brief: the 16 Nov batch-B vetting found that the Omont printed-catalogue sweeps paired items with the wrong volume heading
(Omont prints "(Anc. N.)" at the end of an entry, so an OCR pass that reads the next heading can attach items to the wrong
volume). Check every Omont-derived row against the BnF Archives et manuscrits notice of the volume it names.
Read-only for `catalogue.json` and `research/leads.json`; nothing merged or committed. fr. 3029 and fr. 3092 not touched.

## Rows in scope (step 1)

Selected by grepping `catalogue.json` and `research/leads.json` for Omont / "Catalogue general" / the Omont sweep folders,
then reading the sweep READMEs:

- `research/sweep_2026-11-14_omont_bnf` (Ancien fonds, 21 rows) -> ids 2724-2744. 2726 and 2732 are now catalogue entries
  (2726 in this worktree's uncommitted catalogue.json, rescoped to fr. 3654 by batch B); the other 19 are leads.
- `research/sweep_2026-11-15_omont_naf` (NAF, Saint-Germain, Petits fonds, 8 rows) -> ids 2745-2752. 2746 is a catalogue entry; 7 leads.
- `research/sweep_2026-11-15_gallica_omont_wave6` (Omont Saint-Germain leftovers, located on Gallica images) -> catalogue 2838-2842.
- Not counted as Omont-derived (they cite Omont only in passing, shelfmarks from other sources): catalogue 363 (issue #81),
  1129 (Besancon), 2916 (Stieve print); lead 1195 (BULAC).

Total in scope: **34 rows: 8 catalogue entries (2726, 2732, 2746, 2838-2842) and 26 leads (2724, 2725, 2727-2731, 2733-2745, 2747-2752).**
All 34 were checked; none left unreached.

## Route (step 2)

- Notice: `https://archivesetmanuscrits.bnf.fr/ark:/12148/cc<n><check>` by curl (NOID check character, `am.py`).
  `find_fr(N)` walks cc ids from a guess until the notice's "Cote" is "Français N".
- **The notice page lists only the first 30 sub-units.** The rest are reached by the IR's own full-text search ("loupe"):
  `affichageDetailsComposants.html?eadCid=FRBNFEAD<9-digit n>&typeIndex=TEXTE_LIBRE_LOCAL&val=<word>`; one component's full
  display (with folio) is `ajaxGetCompDisplay.html?eadCompId=<id>`. The search matches whole tokens, accent-insensitive
  ("chiffre" finds "chiffré" and "avec chiffre et déchiffrement", but not "chiffres"), so `ciph()` queries chiffre, chiffres,
  chiffrée, chiffrées.
- **Folio trap on the notice page:** the page prints each item's folio *before* the item (after the previous one). Read naively,
  every folio is shifted one item down. Checked against Omont's printed "(Fol. N.)" and the component display for fr. 3654 and
  fr. 3657. Catalogue 2726 carries the shifted folios (it has no. 6 at f. 12; the right folio is f. 10). `am.parse` corrects for it.
- **Group notices:** some volumes sit inside one notice for a run (fr. 4133-4138, 4734-4736, 3693-3694, 15540-15584,
  20500-20576, 23210-23229). The volume is a component of that notice, found with the loupe.
- **cc ids are not in shelfmark order across the fonds.** Inside a sub-range they run in *string* order ("15597, 156, 1560, 15601").
  `find_fr` walks from a guess, `interp` handles the ranges, and some volumes were found by stepping through the ids.
- **NAF 10001+ are outside that numbering** (NAF 22330 = cc4087, NAF 11238 = cc5902). They were found with the site's simple search:
  POST `resultatRechercheSimple.html` with `TEXTE_LIBRE_INPUT=<word>`. It works by curl and returns `./ark:/12148/cc...` links.
  This search also contradicts an earlier sweep note that said it does not work.
- One request at a time, at least 1.1 s apart. Responses are cached outside the repo (scratchpad `amcache/`). No bot check was met.
- The Omont OCR was fetched again from archive.org (`p1cataloguegnr01-04bibluoft_djvu.txt`, outside the repo) for re-identifying volumes.
  The pattern holds for every wrong row: the items belong to the entry that **closes** with the "(Anc. N.)" printed after them.
  The OCR heading above them is often misread (3/5 and 0/6 swaps), and a heading the OCR missed merges two entries.
  `ocrctx.py` and `ocrwin.py` print the heading above a hit and the next "(Anc. N.)" below it. The Anc. number then gives the fr. volume through its notice's "Ancienne cote".

Scripts: `am.py` (notice fetch/parse, loupe, component, finders), `dump_vols.py` (cipher items of named volumes),
`items.py` (given items of a volume), `ocrctx.py` / `ocrwin.py` (Omont OCR context), `make_findings.py` (writes `findings.json`).

## Results (34 rows checked: 17 ok, 15 shelfmark_wrong, 2 decipherment_filed, 0 not_found)

### Catalogue entries (public)

| id | status | finding |
|---|---|---|
| 2726 | ok, folios wrong | fr. 3654 nos. 6, 8, 11-19 is right, but the folios are shifted one item: they should be ff. 10, 14, 20, 22, 26, 28, 32, 34, 37, 40, 43 |
| 2732 | **shelfmark_wrong** | Omont nos. 34, 49, 70, 72 ("lettre(s) en chiffre", ff. 67-202) are in the entry closing "(Anc. 8554.)", the volume after fr. 3028 (Anc. 8553). By sequence that is **fr. 3029, which is withheld**. Its notice was not opened. fr. 3027 (Anc. 8552) lists no cipher item, and its f. 67 is a Bonnivet letter. The cipher leaf seen on Gallica fr. 3027 view 69 is real but is a different, unlisted piece. Rescope the entry and ask about fr. 3029 |
| 2746 | ok | fr. 20140 f. 16, Danzay "en partie chiffree" |
| 2838-2841 | ok | fr. 15567 f. 24 and f. 158 ff.; fr. 15568 f. 151 and f. 207. The notice names Matignon as the writer of 15567 f. 24 and 15568 f. 151, where the entries say "unknown" |
| 2842 | ok | fr. 15571 confirmed. The notice lists only f. 34 (Chasteauneuf); f. 37 was seen on the image |

### Leads

- **Wrong volume (13 leads):**

| lead | where the pieces actually are |
|---|---|
| 2724 | fr. 3251 and fr. 3252 (Birago) |
| 2725 | fr. 3641 (Philip II / Mendoza / Ibarra; on Gallica) |
| 2727 | fr. 3375 replaces fr. 3374 |
| 2729 | Lauriere letter in fr. 3625 no. 55; item numbers fixed |
| 2731 | fr. 2988 (Ranzo / Raince, on DECODE) |
| 2733 | fr. 2933 no. 11 (Salviati 1525; on Gallica) |
| 2735 | fr. 3045 no. 29 (Cenalis; probably DECODE R4231, decrypted) |
| 2736 | fr. 3586 no. 57 and fr. 3575 nos. 29, 36 (Ventadour) |
| 2737 | fr. 3659 no. 24 (Monteleon) |
| 2738 | fr. 3693 nos. 13, 22, 26 (Mende, England, 1625 not 1623) |
| 2739 | fr. 3758 nos. 100, 104 (1635 not 1633) and fr. 3854 nos. 41-42; fr. 3837 right |
| 2742 | fr. 4734 no. 51 (Lanssac) |
| 2743 | fr. 3457 no. 2 (Ossat) |

- **Wrong volume, already closed:** 2744 (fr. 3828, 3825, 3835), as batch B found.
- **Decipherment recorded:**
  - 2734: the 1549 Morvillier despatch is fr. 3138 no. 24, "avec chiffre et dechiffrement".
  - 2752: the fr. 20506 notice cites the Lasry-Biermann-Tomokiyo 2023 decipherment of the Mary Stuart letters in that volume.
- **ok:** 2728, 2730 (folio fixes: 3329 nos. 81-82 are ff. 164-165), 2740, 2741, 2745, 2747, 2748, 2749, 2750, 2751.

Sibling cipher items found in passing, none checked against the ledgers:

| volume | items | content |
|---|---|---|
| fr. 3138 | no. 22 | La Guiche, Rome 1551, no decipherment |
| fr. 3634 | nos. 45, 80 | |
| fr. 3329 | no. 107 | |
| fr. 3045 | nos. 24, 31 | |
| fr. 3641 | nos. 3, 6, 50, 58 | |
| fr. 4697 | no. 70 | |
| fr. 4691 | nos. 20-21 | |

## Not done

- No leaf was viewed in this audit; every verdict is from the BnF notice, with the Omont OCR used only to locate entries.
- fr. 3029 (and fr. 3092) were not opened. The fr. 3029 attribution in 2732 is inferred from the Anc. sequence (8552 = fr. 3027,
  8553 = fr. 3028, next = 8554) and is not confirmed.
- DECODE was not re-queried. The R-numbers quoted come from the earlier vetting notes.
- Only the rows named in step 1 were checked. Other rows of these sweeps were not checked: the `key_leads.json` groups, unless they were merged
  under another id. Nor were rows of other sweeps that cite Omont only for context (catalogue 363, 1129, 2916; lead 1195).
