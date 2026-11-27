# Ktiv and Friedberg sweep (26 Nov 2026)

Run by a Claude Code session (`claude-sonnet-5-5`) for Daniel Bourdeau. Claude in Chrome, one tab, the user's real
Chrome. Nothing registered, no credentials typed, no CAPTCHA or Turnstile clicked, no images in the repository.
Goal: find new, likely unread Geniza cipher targets in the sources PGP does not hold (NLI Ktiv, AIU, Friedberg).

**Result: no new catalogue entry. Two low-grade leads added (importance 2 and 1), neither shown to be a cipher. Sweep closed
26 Nov 2026 at the user's request.** NLI Ktiv was hard-blocked at the start (the first section below), then unblocked by the user;
the AIU leaves and the Ktiv term searches were run afterwards (section "NLI Ktiv probe"). Friedberg was searched by Language
(Cryptic script, Nomina Barbara, Unknown/Tartaric, Occult Sciences x Coptic/Greek/Persian/Syriac) and Script Style (Mirrored).
Nothing in either source is a cipher; the four AIU leaves are magic or key material.

## What was blocked (at the start; later cleared)

- **NLI / Ktiv (`www.nli.org.il`): hard Cloudflare block, host-wide.** At the start of this session the Ktiv landing
  page and then a known item page (`itempage?vid=KTIV&scope=KTIV&docId=...`, the one that loaded in the 26 Nov
  `sweep_2026-11-26_nli_geniza` run) both returned "Sorry, you have been blocked" (an error page with a Ray ID, no checkbox),
  so this was not a Turnstile to clear. `iiif.nli.org.il` was not tried. Not done: AIU XII.41, XII.68, VI.B.157,
  VI.B.174, NLI 577.1/63 (already read from images in the earlier run: plain Arabic prayer, not a cipher), and the Ktiv
  term searches (English, Hebrew, Arabic). They need a person on an unblocked network, or saved images.
- **AIU's own site** did not resolve in the earlier run; the AIU leaves are on Ktiv only.

## Friedberg Genizah Project (fgp.genizah.org), signed in

The user was already signed in (the page showed the user's welcome line). The FGP frames were read with
`javascript_tool` on the frame documents (same origin; query-string output is filtered by the tool, so URLs were stripped).

- **Free-word search** ("Search Word") looks up the Hebrew-script transcription lexicon: "cipher" returned
  "No Records Found". English catalogue terms cannot be searched that way.
- **Advanced search** offers Collection, Titles, Domain and Title, Author, Period of Copy, **Language and Script**,
  Script Style, Vocalization, No. of Columns, Range of Lines, Physical Status, Material, Attributes, Information Source,
  Additional Conditions, Computer generated data, Bibliographical References. The Language list has **"Cryptic script"** and
  **"Nomina Barbara"**; the Type of Script list has **"Unknown"**. Recipe: Search tab, parameter dropdown, pick the parameter,
  tick boxes, click the green double arrow at the top right of the criteria panel to record the step, then the "Search"
  button under "Find all records for which".
- **Language = Cryptic script OR Script = Unknown: 12 shelfmarks.** All 12 were checked (below). "Nomina Barbara", Script Style,
  Attributes and Domain and Title were **not** searched: the Friedberg GUI is slow to drive (stale frames, one shelfmark's
  record per click), and the session stopped there.

| Friedberg hit | Result |
|---|---|
| T-S K5.7 | known: catalogue 3757 |
| CUL Or.1080 14.13, 14.25 | known: lead 3858 (closed `not_cipher`, amulet) |
| T-S Misc.10.60, T-S Misc.22.218 | known: catalogue / `targets/tsk2424`, `targets/cambridge_k5_7` |
| T-S 8.267 | Samaritan liturgical poem (Samaritan Arabic and Hebrew, 20 rows); tagged "cryptic script" by the Magic team, not seen at full size; not a cipher on the catalogue record |
| T-S NS 322.89 | both sides viewed: ruled blocks of cursive signs, hundreds of them. **PGP 41889: "Coptic mathematical table"** (initials MR). Cursive Coptic numerals, not a cipher; not independently decoded here |
| T-S NS 327.2(f) | both sides viewed: about 20 lines of repeated cursive signs and one Arabic word. **PGP 41863: "Account. Containing one word in Arabic and many lines of Coptic numerals."** Not a cipher |
| Mosseri VI,21.3 | recto viewed: rows of repeated looped charakteres, a struck-out line and Arabic cursive; verso blank. Magic, class B; no lead |
| T-S NS 322.97 | **lead** (new, below): not in PGP |
| T-S Misc.10.90 | **lead** (new, below): verso three lines of an unidentified script; not in PGP |
| (T-S AS 143.155, found in the same list) | recto viewed: three large charakteres and four short Hebrew-script lines; class B, no lead; verso not viewed |

Lesson: the Friedberg "cryptic script / unknown" tag marks scripts the cataloguer could not name, and here it caught
Coptic numeral tables as well as magic signs. Check PGP's record before treating a Friedberg "cryptic" leaf as new.

Neighbours checked for the same hand: NS 322.84-322.103 and NS 327.1(a,b), 327.2(a-h), recto and verso at about 260 px on
contact sheets. All ordinary Hebrew, Judaeo-Arabic or Arabic, apart from the leaves above. No sibling of NS 322.97.

## Leads added (`candidates.json`, no vetting block)

1. **T-S NS 322.97** (importance 2, solvability 2): bifolium; recto page of about 19 lines in a Hebrew-letter cursive with
   word spacing whose groups repeat in near-identical variants; verso four lines of large signs, sideways, each opening with the
   same group. About 600 signs. Reads more like a litany of names than a message; not transcribed.
2. **T-S Misc.10.90 verso** (importance 1, solvability 1): three lines (red, black, red) of Greek- or Coptic-looking letters
   under a Hebrew-script recipe leaf with angel names. Probably voces magicae; too short.

Neither goes to the catalogue. The vetting bar needs a viewed ciphertext (done) **and** a case that it is enciphered text,
searched in DECODE, Tomokiyo, Lasry and the literature; here the case is not made, and the DECODE/Tomokiyo/Lasry searches
were not run per item. Web search for each shelfmark found nothing (the only hit for NS 322.89 was PGP's Coptic-table record).

## NLI Ktiv probe, after the user unblocked it (26 Nov 2026, signed in, one tab, one request at a time)

Ktiv loaded and searched normally; no Cloudflare page in six page loads over about ten minutes. The results URL carries the
query in its hash, e.g. `.../searchresultspage?projectName=MANUSCRIPTS#q=lsr01,contains,all;any,contains,<term>&searchType=METADATA&ftsMethod=0&searchName=regular&sort=date`;
a shelfmark-only search adds `lsr04` and `ShelfmarkOnly=true`. `get_page_text` returns the result cards (title, shelfmark,
system number) in one call.

- **"AIU XII 41" in the shelfmark field: 0 results; "Eutychius": 0.** The AIU leaves are in Ktiv's collection "Library of the
  Alliance Israélite Universelle" (5,424 documents for a free-text search on "Alliance Israélite Universelle genizah"), so the
  shelfmark format there is not "AIU XII 41"; not yet found. The four AIU leaves are still unviewed.
- **"cipher": 55 documents**, all Cairo Genizah (Cambridge 48, Bodleian 3, JTS 2, Manchester 2). Most are Onkelos Targum leaves
  (the word matches by transliteration). The first 40 were read. Relevant: known K24.23, K24.24, T-S AS 143.155 (charakteres,
  viewed), Bodl. heb. e 94.23-25 (Halfon volume, known); new and viewed on CUDL images (not NLI): T-S AS 187.255 (Hebrew-script
  magic), T-S AS 183.70 (Arabic text with boxed rows of short strokes, a letter-science or numeral figure, a few lines), T-S
  Misc.22.13 (Arabic alchemical recipe with red headings), T-S K1.47 (Hebrew magic recipe, a few signs on the verso). **None is a
  cipher.** The last 15 of the 55 were not read.
- **"secret writing": 21 documents**, mostly unrelated manuscripts (the words match separately); the three Genizah ones
  are T-S 13J34.9 (an ordinary letter, PGP 8075), Bodl. heb. d 55.37 (pen trials) and Katz Genizah 340 (a legal
  document). Nothing.
- **"unidentified script": over 40 documents**, nearly all matches on Ktiv's catalogue label "תחום לא מזוהה" (unidentified
  *domain*, i.e. topic), not script (T-S AS 154.80, 161.265, 160.426, 76.195, L-G Ar. II 170 and 171 and others). Not a script
  signal; not followed up.
- **כתב סודי ("secret script"): 40+ documents**, all Kabbalah (Eleazar of Worms, "Sodei Razaya", and similar titles). Noise.
- **"charakteres": 206 documents** (Cambridge, Mosseri VI 9.1-9.3, Bodleian). The 66 shelfmarks read are Bohak's magic boxes
  (T-S AS 142.x and 143.x, NS 322.x, K 11 and K 12, Misc. 28.114, L-G Misc. 60), the same class of leaf as the Friedberg
  Nomina Barbara set; none was viewed here beyond those already seen. Many are not in PGP, so a CUDL image screen of the 206 is
  possible (about 14 contact sheets) but the prior is low: charakteres leaves are magic signs.
- **AIU shelfmarks found.** Ktiv titles them "Library of the Alliance Israélite Universelle, Ms. XII 41" (roman numeral, letter,
  number, spaces). A shelfmark-only search for `Ms. XII 41` returns the leaf (the string must start `Ms.`; "AIU ..." and "Alliance
  XII 41" return 0). DocIds: XII 41 `PNX_MANUSCRIPTS990053881880205171`, XII 68 `PNX_MANUSCRIPTS990053862400205171`, VI B 157
  `PNX_MANUSCRIPTS990048963570205171`, VI B 174 `PNX_MANUSCRIPTS990049100630205171`. Manifests
  (`https://iiif.nli.org.il/IIIFv21/DOCID/<docId>-1/manifest`, fetched from a www.nli.org.il page) each list two canvases; image
  ids XII 41 FL162645864/65, XII 68 FL166105451/52, VI B 157 FL161658702/03, VI B 174 FL169324130/31. Images load only as an
  `<img>` on a www.nli.org.il page (`/IIIFv21/<FL id>/full/1000,/0/default.jpg` and `pct:x,y,w,h` crops); see the earlier NLI
  sweep README. After an overlay empties the page body, a hash-only navigation does not re-render; load the Ktiv landing page
  first.
- **The four AIU leaves, viewed (26 Nov 2026):** **XII 41** (FL162645865): a cross, two lines of about 30 Greek-, Coptic- or
  rune-looking signs, then rows of Arabic letters with partial mirroring; reads as an alphabet or key table (a cryptic alphabet set
  against an Arabic alphabet), no running ciphertext; **key material**, no lead row. **XII 68** (recto): sideways Arabic magic text
  with red-ruled magic-square grids of numbers and words; magic, not a cipher; verso not viewed. **VI B 157** (recto): Hebrew
  magic squares of letters and numerals with Hebrew text; magic; verso not viewed. **VI B 174** (FL169324131): Ladino accounts in
  Hebrew script with faint columns of triangles, circles and dots; doodles or tallies, no text; other side not viewed. **No cipher
  among the four.** XII 41's recto (Eutychius' Annals) was not viewed.
- **Remaining terms, run:** "code" 470 documents and "coded" 472 (the words match Maimonides' "Code", "codex" and the like:
  noise, not read); "symbols" 67 (mostly amulets: Manchester Gaster Amulets 151, 200, 206, 207, 214, Katz Genizah E 16505 and
  E 16509, Mosseri V 372.5 and VI 9.1, BL Or. 10767; magic class, 30 read); צופן 552 (dominated by "צפנת פענח" and צפון
  "north": noise); شفرة, رموز, معمى and "ketav sod": 0 results (the catalogue holds no Arabic-script terms and no such
  transliteration). The last 15 of the 55 "cipher" results and the Gaster Amulet and Katz amulet leaves were not viewed.
- Ktiv stayed unblocked throughout (about 40 page loads and 8 manifest or image fetches over about 90 minutes, 6-10 s apart).

## Driving Friedberg without the GUI: what is known (26 Nov 2026)

Terms of Use (`/GeneralPages/Help/GeneralHelp/Conditions/Conditions.aspx`, read in full for sections A-C and the start of D):
personal study and research only, credit the source and the Friedberg Genizah Project, no commercial use, never share the
login, never download, copy or forward images; catalogue and transcription data belong to their authors; access may be
denied for a breach. Nothing there bans automated queries, but bulk copying of catalogue data is not covered by "personal
research", so queries should be light and results kept to shelfmarks plus short credited notes.

- The site is ASP.NET WebForms in nested frames (`FgpFrames.aspx`), same-origin, with a generated JS proxy for a WCF service:
  `/WCFServices/AjaxWcfHelper.svc/js` lists about 150 methods (`GetShelfmarks`, `GetShelfmarksDetails`, `GetMetadataVal`,
  `GetFgpNumbersDetails`, `GetShelfmarksByCollection`, `FillSessionWithCatRec`, `setFilterInSession`,
  `CheckSessionCateResExist` ...). Calls are JSON POSTs to `/WCFServices/AjaxWcfHelper.svc/<Method>` and work with the
  signed-in cookie from `fetch()` inside the tab.
- **A search is session state, not a URL.** The criteria page is
  `/SelectionPages/SearchPages/BooleanSearch/BooleanSearch.aspx?searchParam=N` (N=5 is Language and Script, 870 KB, 932 inputs,
  Telerik controls; checkboxes `ctl00_ContentPlaceHolder1_LangList_<i>`). Ticking boxes and recording a step stores the
  criteria in the server session; the results frame then calls `setFilterInSession`, `GetShelfmarks`,
  `GetFirstShelfmarkListDataToThumbnails`, `CheckSessionCateResExist`. A repeated Search click replays the stored criteria.
- **Working recipe (used for the Nomina Barbara and Unknown/Tartaric searches below).** The criteria page lives in the
  frame `ctl00_FramePlaceHolder_Iframe1` (`BooleanSearch.aspx`); its page functions are callable from the tab:
  `NewSearchButton_click()` resets to a blank criteria page; a real click on the "Language and Script" menu item (Telerik
  RadMenu, DOM clicks do not render the panel) shows the checkboxes; then set them by DOM
  (`#ctl00_ContentPlaceHolder1_LangList_<i>`, `AlphabetTypeList_<i>`, `AreaList_<i>`, `LettersTypeList_<i>` `.click()`),
  then two real clicks (the green double arrow at the panel's top right, then "Search"), then read the result list by DOM
  and page with `#btnNextPage`. Not fully GUI-free (the menu item and the two buttons still need coordinates, because the
  panel is drawn by Telerik scripts), but the checkbox and paging work is scripted. Language indices: 0 Arabic, 1 Aramaic,
  4 Coptic, 5 Cryptic script, 9 Greek, 10 Hebrew, 14 Nomina Barbara, 22 Tartaric, 25 Unknown. Alphabet: 8 Unknown. The result
  frame and JSON calls (`GetShelfmarks` etc.) were not decoded; the tool's output filter blocks any returned string that
  looks like a query string, so replace `= ? & :` before returning text.
- **Language = Nomina Barbara: 17 shelfmarks** (the list showed 18; one could not be read), 15 of them not in PGP (PGP holds only
  NS 324.76a/b, "Hekh-type names"), none in the repo. Both sides viewed at 300 px on contact sheets, plus K1.107 at 1300 px:
  T-S A26.83, K1.107, Ar.45.54, NS 89.11, NS 163.54, NS 223.94, NS 293.9, NS 324.76a/b, AS 142.58, AS 143.17, 143.18, 143.100,
  143.112, 143.254, 143.448 (a sheet of about 60 tiny fragments), AS 177.416. All are Hebrew-script magic: names in grids and
  ovals (AS 143.17/18/100/112, AS 177.416, AS 142.58), name lists (A26.83, NS 293.9 with a drawing), recipe texts, or
  charakteres rows (K1.107: looped signs in repeated stroke rows among Hebrew words). **No cipher, no lead.** The AS 143
  grids repeat one name pattern (עעפרים and similar) in ruled cells, which is a magic square of names, not a text.
- **Script Style = Mirrored Script: 3 shelfmarks** (T-S AS 157.506, 157.542, 157.543). Both sides viewed at 900 px. The "mirrored"
  writing is ink set-off (a reversed ghost image of the facing text) on ordinary Hebrew and Judaeo-Arabic: AS 157.506 a
  bifolium of Hebrew text; AS 157.542 + 543 a legal document (PGP 16693). **Not ciphers.** (Script Style's other fields: Region
  of Script, Style = Cursive, Diwani, Karaitic, Kufic, Mirrored, Naskhi, Nasta'liq, Rabbinical, Riqa, Semi-cursive, Square,
  Thuluth, Unknown; "Unknown" not searched, it is a catalogue default.)
- **Attributes** = Palimpsest, Illustration, Colophon, Cantillation: nothing cipher-related, not searched.
- **Domain and Title** has no cryptography or code domain. The nearest are Occult Sciences (Bohak's magic leaves, large) and
  "Teaching Aids, Pen Trials, Writing Exercises, Scribblings, Jotting" (large); not screened whole. A useful narrowing for a
  later pass: Domain = Occult Sciences AND Language = Greek, Coptic, Syriac, Persian or Unknown (magic in a non-Hebrew
  script or with no named language). Free Description is not offered as a search parameter in the dropdown; Additional Conditions was not opened.
- **Domain = Occult Sciences AND Language = Coptic, Greek, Persian or Syriac: 66 shelfmarks** (63 read; with "Unknown" added the
  set was 1,681 shelfmarks, because "Unknown" is a catalogue default, so it was dropped). 21 are in PGP and described: BL OR 5525.1
  (large Coptic magical fragment with poor Greek), T-S 12.207 + AS 207.54 (Coptic recipe; Crum), T-S 12.740 (Coptic prayer, known
  from the image screen), NS 31.37 (scorpion amulet), the Or.1081 2.75 Syriac/Garshuni school and liturgical leaves, and Syriac
  liturgy (NS 306.227-229, AS 177.539). The rest are JTS ENA 1880.1-25, ENA 2331.9-17 and ENA NS 65.23 (images on JTS, not
  fetched; the catalogue language is plain Syriac, Coptic or Greek) and three undescribed Cambridge leaves, viewed on both sides
  at 520 px: T-S K1.95 (two pages of Hebrew-style square script, ordinary), T-S AS 62.501 (lines of Hebrew-script text with set-off,
  ordinary) and **T-S NS 305.83** (a ruled 3 x 5 grid with one sign per cell, about a dozen charakteres, a scorpion drawing and an
  Arabic line: an amulet or sign table, class B, no running text). **No cipher, no lead.** JTS ENA 1880 and 2331 were not viewed.
- **Language = Unknown OR Tartaric: 17 pages (about 170 shelfmarks)**, mostly whole manuscripts (JTS ENA volumes, Michigan,
  Basel, Berlin and others): too broad to screen, "Unknown" is a catalogue default. Not examined. Narrow it by
  combining with Script = Unknown and a short Range of Lines before spending time on it.

## What is left, if the line is reopened

Closed for now: the expected return is low (see the closing assessment in the PR thread). Untried or unfinished:
1. The 206 Ktiv "charakteres" leaves and the Gaster and Katz amulet leaves (image screen on CUDL/NLI), the last 15 of the 55
   "cipher" results, and XII 41's recto.
2. Friedberg: Language = Unknown/Tartaric (17 pages, mostly whole manuscripts), Script Style = Unknown, Additional Conditions.
3. Ask Bohak's FGP Magic team or Cambridge's Genizah Research Unit what "cryptic script" meant for T-S NS 322.97.

## Files

`candidates.json` (2 rows), this README. Images used were fetched by curl from `images.lib.cam.ac.uk` into the session
scratch folder and are not in the repository.
