# Bellièvre papers, BnF fr. 15890, 15894, 15897, 15898 on Gallica: page-by-page screen, 15 Nov 2026 (wave 15)

Continues `../sweep_2026-11-11_bellievre/` (which left these four volumes unscreened).

**Result: no ciphertext in any of the four volumes; `candidates.json` is `[]`.** All 3,570 canvases were fetched and
every one that carries writing was read on a contact sheet. One cipher key sheet was found (fr. 15890 f. 326r,
`key_leads.json`). One clear note with a few cover signs is described under fr. 15894 (f. 508r), not a candidate.

## Route
- Manifests: `https://openapi.bnf.fr/iiif/presentation/v3/ark:/12148/<ark>/manifest.json` (curl, 200).
- Images: `https://openapi.bnf.fr/iiif/image/v3/ark:/12148/<ark>/f<N>/full/800,/0/default.jpg`, one request at a time,
  about 3 s per image as served (`fetch_all.py`, resumable). No 429 so far. gallica.bnf.fr not used. Chrome not needed.

## Volumes
| fr. | ark | canvases | scan | contents (manifest title) |
|---|---|---|---|---|
| 15890 | btv1b105073513 | 988 | colour, one page per canvas, folio labels in manifest | I. Lettres et papiers divers (1566-1577); f. 1 title: letters of Bellièvre during his Swiss embassies, June 1566 - March 1573 |
| 15894 | btv1b525216318 | 1168 | colour, one page per canvas, folio labels | V. Lettres et papiers divers (1598-1606), 613 ff. |
| 15897 | btv1b9057357p | 580 | microfilm, two-page openings | VIII. Letters to the chancellor from prelates, princes, marshals (1599-1606), 569 ff. |
| 15898 | btv1b90643252 + btv1b9064324n | 422 + 412 | microfilm openings; two halves of one 810-f. volume | IX. Letters to the chancellor from presidents and councillors of the Parlements (1599-1606) |

## Method
- Every canvas fetched at 800 px. `ink.py` measures the ink fraction of each canvas; canvases under 0.0045 (blank pages,
  show-through only) are left off the sheets and listed in `img/<vol>_blank.json` (not viewed). Address panels and anything
  with a few lines of writing stay on.
- `sheets2.py`: contact sheets of 18 pages (6 x 3, 320 px per page) for the colour volumes; `sheets.py`: 20 openings
  (4 x 5, 480 px per opening) for the microfilm volumes. Every sheet was read; a suspect page is opened at 1200-1600 px.
- Limit, stated plainly: at 320 px per page a block of cipher (a line or more of figures or signs) is visible; a single
  code group or a few figures inside a cursive line would not be. "No cipher" below means no cipher block.

## Results per volume
### fr. 15890 (btv1b105073513, 988 canvases) - DONE, no ciphertext, one key sheet
- All 988 canvases fetched. 185 blank or show-through-only canvases left off the sheets (`img/15890_blank.json`); the
  other 803 read on 6 x 3 sheets, every sheet.
- Content: Bellièvre's letters from the Swiss embassy to the King, the Queen mother, Anjou, Morvillier (1566-1569, signed
  originals or secretary copies, views 11-420); a fair-copy register "Au Roy" Dec 1572 - Mar 1573 (views 427-497); his
  cursive drafts of 1572-73; Polish journey pieces 1573-74 (privilege of Henri as king of Poland, itineraries and expense
  journals of the journey out and of the return through Vienna and Venice, some on small leaves); drafts and letters of
  1575-76 on the reiters of Duke Casimir; discourses; a 1577 copy; Latin pieces.
- **Ciphertext: none seen.** No page with a block of figures or signs; the letters are all in clear.
- **Key sheet: f. 326r (view 659)**, verso (view 660) blank, no title, no date, no endorsement. One oblong leaf, seen at
  1600 px. Homophonic alphabet A-Z with three signs per letter (invented signs, some figures and letters), "Doubles"
  (PP, SS, MM, NN, CC, DD, FF, EE, TT, two signs each), "Monosilabes" (car, pour, quand, quel, que, faire, dire, de, la,
  les, encore, faut), "Nulles" (four groups), and a nomenclature of 21 names down the left margin as far as read: Le Roy
  Catholique, La Royne d'Angleterre, Dom Joan, L'Empereur, L'archiduc, Pays bas, Les Estatz, Le Prince d'Orange,
  Monseigneur, Le Duc Casimir, Allemans, Francoys, Espagnolz, Italiens, Le Pape, M. de Savoye, Le Roy de Navarre,
  Huguenotz, Anvers, Le Comte de Lalain, Bruxelles, Mons. The names (Dom Joan, the Estates, Orange, Lalaing, Mons,
  Monseigneur) point to the Netherlands affairs of about 1577-78, not to the Swiss or Polish pieces it is bound among
  (ff. 324-325 Gondi's 1573 Polish revenue contract, ff. 327-328 royal letters on parchment); the date is my inference
  from the names, not written on the sheet. No letter in this key was seen in fr. 15890. Bellièvre went to Monseigneur
  (Anjou) and the Estates at Mons in 1578: cipher letters in this key are to be looked for in the volumes for 1578
  (fr. 15891 was swept on 5 Nov; fr. 15905 and others). Not checked: whether Tomokiyo or DECODE list this key.
- The component detector (`det.py`, via `rank.py`) was tried as a second line and is useless on this colour scan (the key
  sheet itself scores 14 against a median of 17); no detector result is relied on.

### fr. 15894 (btv1b525216318, 1168 canvases) - DONE, no ciphertext, no key
- Views 1-400 (to f. 183) read on sheets: no cipher. Content: Bellièvre and Sillery's dispatches from Vervins to the King
  and to Villeroy, Jan - Aug 1598 (signed, in clear, with underlined passages and marginal crosses but no cipher signs),
  then the treaty articles, acts and ratifications of Vervins.
- Views 401-800 (ff. 185-465) read on sheets: no cipher. Content: Vervins acts and Savoy pieces 1598-1600, the memoirs
  on the dissolution of the King's marriage (1599, French and Latin), later fair copies of Bellièvre's letters to the King
  (1599-1601), his letters to Sillery at Rome (1600-01), drafts of edicts and financial memoirs (1602-04). All in clear.
- Views 801-1168 (ff. 466-613, covers) read on sheets: no cipher. Content: letters to the King and Villeroy 1602-05, the
  Biron trial papers of 1602 (interrogations, inventories of the exhibits, pieces in a large sloping hand at ff. 502-510),
  fair copies of letters of 1602-05, drafts of 1603-05.
- All 1168 canvases fetched (five transient HTTP 406/5xx, each fetched on retry). 181 blank canvases left off the sheets
  (`img/15894_blank.json`); the other 987 read, every sheet.
- **Ciphertext: none seen. Key sheets: none seen.**
- Noted, not a candidate: **f. 508r (view 909)**, among the Biron trial pieces, a nine-line note of credence in clear
  ("... vous pouves adjouter foy a ses parolles et parler franchement ... par ses caracteres vous cognoistres que c'est Z
  ... qui parle a 30 ... vous bruslerez ceste en sa presence ou elle me sera raportee", my reading from a 1600-px crop,
  several words uncertain). It names the parties by three or four cover signs (Z, 30, a sign like a barred o twice with 8
  between). That is a handful of cover names in a clear sentence, not ciphertext; no key seen. The hand matches the
  neighbouring ff. 502-510 pieces; whose hand it is I did not establish (the inventory at f. 534, view 973, lists papers
  "de la main" of the marshal, not compared).
- f. 92r (view 197) "A M. de Villeroy" looked odd on the sheet (a round upright hand with detached letters): opened at
  800 px, it is a clear French copy, not cipher.

### fr. 15897 (btv1b9057357p, 580 canvases) - DONE, no ciphertext, no key
- Microfilm, two-page openings; all 580 canvases fetched and all read on 4 x 5 sheets (480 px per opening), no canvas
  left out. Views 1-3 and 578-580 are film targets and covers.
- Content: original letters to the chancellor, 1599-1606, from cardinals (Joyeuse, Gondi, Givry, Sourdis, Ossat, Du
  Perron), bishops and chapters, princes and princesses (Catherine de Bourbon, Diane de France, the Lorraine and Guise
  houses, Montpensier, Conti), marshals and governors (Montmorency, Lesdiguieres, Ornano, Biron, Epernon and others).
  One or two pages each, signed, with address panels; petitions and recommendations. All in clear.
- **Ciphertext: none seen. Key sheets: none seen.**

### fr. 15898 (two arks) - DONE, no ciphertext, no key
- **btv1b90643252 (422 canvases) = ff. 401-810**, the second half of the volume (the first written leaf on view 3 is
  numbered 401, the last on view 416 is 810). Microfilm openings; all 422 canvases fetched and read on 4 x 5 sheets.
  Content: letters to the chancellor from the presidents, procureurs generaux and councillors of the provincial
  Parlements and Chambres des comptes (Grenoble, Aix, Rouen, Dijon, Rennes, Toulouse, Bordeaux as far as the signatures
  and place lines could be made out at sheet scale), 1600-1606. Petitions and reports, all in clear.
  **Ciphertext: none seen. Key sheets: none seen.** Views 393-395 (ff. 787-789) carry heavy ink bleed-through, which
  looks like rows of blots on the sheet; it is offset ink, not signs.
- **btv1b9064324n (412 canvases) = ff. 1-400**, the first half (flyleaf note on view 4: "Volume de 810 Feuillets";
  last numbered leaf on view 409 is 400). All 412 canvases fetched and read on 4 x 5 sheets. Content: letters of the
  gens du roi and presidents of the Parlement of Paris (with fair copies of letters patent and arrets of 1602 at
  ff. 11-20), then Toulouse, Bordeaux, Dijon, Aix, Rennes and other courts, 1599-1606. All in clear.
  **Ciphertext: none seen. Key sheets: none seen.**
- Note for the next reader: the two arks are in reverse order of their numbers (9064324n first, 90643252 second).

## What was not done, and limits
- Sheets were read at 320 px per page (colour volumes) and 480 px per two-page opening (microfilm volumes), so about
  240 px per page for fr. 15897 and 15898. A block of cipher (a line or more of figures or signs) shows at that size, as
  the key sheet and the f. 508r note did; isolated code groups or a few figures inside a cursive line would not, and no
  page was read line by line. "None seen" means no cipher block.
- Blank canvases of the two colour volumes (ink fraction under 0.0045: 123 in fr. 15890, 181 in fr. 15894) were not put
  on a sheet. The measure was checked on address panels and three-line pages, which stay above it.
- Only four pages were opened above 800 px: fr. 15890 views 659-660 (key sheet and its blank verso), fr. 15894 view 909
  (crop), and two fr. 15897 versos at 800 px (views 371, 522: show-through).
- The key sheet's sign values were not transcribed and its date is inferred from the names. Not checked for it: Tomokiyo's
  cryptiana pages, DECODE, and which Bellievre letters use it.
- Senders, dates and places in the content notes are what could be made out at sheet scale; they are orientation, not
  a calendar of the volumes.
- `research/COVERAGE.md` was not edited (this sweep writes only to its own folder): its rows naming fr. 15890, 15894,
  15897, 15898 as unscreened can now be closed.

## Files
- `fetch_all.py` (fetch), `sheets.py` (opening sheets), `sheets2.py` + `ink.py` (page sheets without blank pages),
  `det.py` + `rank.py` (component detector, tried on fr. 15890 and not relied on), `fetch.log`.
- `candidates.json` (`[]`), `key_leads.json` (the fr. 15890 f. 326r key).
- `img/` (not to be committed): 800-px canvases per volume, sheets, manifests, `hi/` close-ups.
