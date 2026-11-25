# YEK massive sweep (25 Nov 2026): stopped early, partial

Run by a Claude Code session with Claude in Chrome (owner signed in to portal.yek.gov.tr). **Stopped at the coordinator's request
after the harvest phase was about 40% through.** Nothing was screened on an image, nothing was promoted, no `candidates.json`
(no ciphertext seen). State of the work, so it can resume:

## How the portal's search works (the part that was worked out)

- **Detaylı Arama** is a query builder at `/works/advancedsearch/full`. Its URL carries `key=&search_key_type=3&search_form_type=ALL_FIELDS&rule=<JSON>`,
  `rule = {"condition":"AND"|"OR","rules":[{"id":F,"field":F,"type":"string","input":"text","operator":"in","value":V}]}`.
  The HTML of that URL holds **no results**: the page's script calls the xajax function `xajaxSetFilter(rule, false)` and the results
  come back as JSON, `xjxobj[?]` with `id == "data_result"` and `data` = HTML.
- **Plain route (works from a fetch inside any portal tab):** `POST <same URL> ` with body
  `xjxfun=xajaxSetFilter&xjxr=<ms>&xjxargs[]=<rule JSON, urlencoded>&xjxargs[]=Bfalse`, content type form-urlencoded. Response JSON ->
  `xjxobj.find(c=>c.id=='data_result').data` -> parse; rows are `.biblio_result_row`, labels `.marc-content-results-label` (value in the next
  sibling), title `.summary_title`, an `a` reading "Görüntü" = images exist, bib no. from "Bibliyografik kayıt no.". 0 hits: no `data_result`.
- **Paging:** POST to `/works/advancedsearch/full/<offset>?<same query string>` (offset 0, 100, 200 ...; 100 per page after the session's `rpp`
  is 100). The `/works/search/full/<offset>` route ignores the advanced rule.
- **Date filter is in the URL, and is lexicographic on a string field.** Append `&filter_options_date_type%5Bistinsah_yil%5D=0&istinsah_yil=[a,b]`
  (type 0 = between; 2 = before; the field is Hijri year). Ranges compare **as strings**: [1,904] returns 126,085 records, because "1000"-"1999"
  sort inside it. Only same-length ranges are safe: [200,299] ... [800,899] are correct (3-digit years), [1000,1110] is correct for 4-digit years,
  single years via [y,y]. Facet filters (language, library, material) are session state (`setFiltering` -> `xajaxSetLefBarFilter`) and were not used.
- **Field ids** in the builder: AllFields, title, author, konu_tasnif_no, collections, collection_no, alfabe_yazi_turu, baskı_bildirimi,
  baslangic_satirlari, biblionumber, bitis_satirlari, kagit_boyutu, cilt_*, arap_harfli_notlar, kayitlar_muhurler, dil_notu_portal, eser_turu,
  eserin_ozgun_dili, genel_notlar, istinsah_kaydi, istinsah_basim_tarihi, istinsah_basim_yeri, kaynak_referans_portal, collection, Subject,
  yazar_olum, muhurler, diger_yazarlar, terim_iliski, ozet_icerik, siniflama_numarasi_portal, telif_*, temelluk_vakif, tezhip_*, publisher,
  yazim_sekli. Operators: in (contains), not_in, equal, is_empty.
- **Search semantics learned:** the analyser folds diacritics (şifre = sifre = ŞİFRE) and splits on apostrophes and spaces, and **a multi-word
  value is an OR of its tokens** ("şifre ile" = 79,903 hits). Use one token per rule with `condition: AND`. "mu'amma" and "muʿamma" therefore
  match on "mu"/"amma". `AllFields` finds more than the old all-fields URL (şifre: 15 vs 6).
- **Speed:** about 2.5 s per 100-row page; two loops in one tab ran fine. The page's JS calls time out at 45 s, so run harvests as a background loop
  in the page and poll a status object. Data cannot leave the page except as tool output (about 1,000 characters per call), and fetches from the
  portal to `http://127.0.0.1` hung (Chrome local-network prompt, not answered), so the harvest lives in the **browser's IndexedDB** (db
  `yekharvest`, store `kv`, key `db`, portal origin, JSON `{rows, log, t}`). Helper code: `harvest.js`.

## What was done

Harvest, 20,476 distinct records in the last IndexedDB snapshot (taken at 303 completed query records):

| Harvest | State | Result |
|---|---|---|
| A: all records with istinsah year 200-904 AH, by 100-year slice and single years 1-199 | **done** | 200-299: 0; 300-399: 14; 400-499: 66; 500-599: 298; 600-699: 1,107; 700-799: 3,170; 800-899: 5,940; 900-904: 311 (total 10,906). Years 1-199: 1 record (year 20); years 94 and 95 returned a server error (HTML) and were not retried. Includes printed books with early-looking dates only if the field says so |
| D: description-field terms, Latin, fields AllFields / title / Subject / genel_notlar / ozet_icerik / arap_harfli_notlar | **partial** | done in this order: şifre, şifreli, "şifre ile" (junk, OR of tokens), rumûz, remz, ramz, muammâ, mütercem, müterceme, hall, hurûf, cifr, ebced, gizli, sırlı (all fields), esrâr title (11,576 hits, split; E1 not reached). Counts per query in `query_counts.tsv`. Large terms (over 1,500) were re-run as istinsah slices [200,999] and [1000,1110] |
| D: Latin terms after esrâr, all Arabic-script terms, AND-phrases | **not started** | queue was built (about 545 jobs) but the tab closed |
| B: classes (652.8 etc.), Subject terms | **not started** | counts only: see below |
| C: mecmua / kunnâş / münşeât / inşâ / rasâ'il types before 1111 AH | **not started** | |
| E: Ottoman şifre defteri, cetveli, miftahı | **not started** | the two known records (Arkeoloji 01652, 01660) are in the A/D harvest |

Class counts (konu_tasnif_no "in", whole portal): 652.8: 2; 652: 26; 133: 3,528; 133.3: 595; 133.4: 103; 135: 542; 153: 101; 509: 124; 510: 2,502;
400: 197; 410: 1,443; 811: 5,539; 891: 13,770; 070: 162; 090: 64; 955: 415; 956: 10,309; 351: 454; 003: 40; 001: 4,961; 297: 269,528; 298: 12;
492.7: 49,340; 929: 636; 475: 5. 003.54, 001.54 and 135.4 return nothing. Whole portal: 652,305 records; the facet counts on the landing page
were 375,082 manuscripts, 277,222 printed.

Triage: a scoring script over the snapshot (title, author, class, date, tags from the note-field searches) gave 531 rows scoring 3 or more; the top
rows are in `shortlist.tsv`. Scores here are on catalogue lines only; none has been looked at on an image.

## Shortlist (from the partial harvest; screened: none)

`shortlist.tsv` holds 61 rows. Reading of it:

- **Not what the sweep is after, but now catalogued with shelfmarks:** about 45 Persian and Ottoman *mu'amma* (name-riddle verse) items, in
  Süleymaniye (Ali Nihat Tarlan 52, 60, 75, 115, 122; Ayasofya 3993, 4009, 4209, 4219, 4274; Esad Efendi 3817), Manisa İl Halk 2968-2992,
  Millet Ali Emiri, Beyazıt, Bursa İnebey. These are literary riddles solved in their own commentaries; Hall-i mu'amma items are the commentary.
- **Treatise witnesses newly seen:** *Izah al-rumuz wa-miftah al-kunuz* (Ibn al-Qabaqibi) in Bursa Haraççıoğlu 727, 746; Manisa 4537/2;
  Köprülü Fazıl Ahmed Paşa 19; Hacı Selim Ağa 24-002; Samsun 55 Hk 271; Kılıç Ali Paşa 23; *Keşf rumuz* of Ibn Wahshiyya, Konya Yusuf Ağa
  YY00004887/3 (dated 707 AH); *al-Tiraz al-asma 'ala kanz al-asma fi'l-lughz wa'l-mu'amma* (Ibn al-Bukka'), Manisa 2976/8 and Ankara Adnan
  Ötüken 06 Hk 1108; Kenz al-asma fi 'ilm al-mu'amma (Nahrawali), Manisa 2976/9, Süleymaniye Hafid Efendi 296; *al-Mermuzat al-'ishrun*
  (Sadr al-Din Muzaffar, 705 AH, Reisülküttab 1197-001); *Mermuzat-i Asadi* (Najm al-Din Daya, 735 AH, Esad Efendi 1704).
- **Not previously seen, worth the first image look:** *Rumuz al-kunuz* (Shuja' al-Din Ilyas, 1047 AH), Arkeoloji Yazmaları 00557, class 133.3
  with "cifr" in the notes; *al-Jafr al-jami'*, Millet Ali Emiri Arabi 2844; *Remz min al-'ilm al-maknun wa-l-sirr al-masun*, Laleli 2147-004
  (900 AH); *al-Durr al-munazzam fi'l-sirr al-a'zam* (Ibn Talha), Hüseyin Şemsi-Fa 78-001 and Esad Efendi 1984-001, class 133.3, notes mention
  rumuz and cifr; *Risale fi'l-lughz wa'l-ta'miya* (Baha' al-Din al-'Amili), Esad Efendi 3817-012 (already seen as catalogue line); *Teshil
  al-majaz ila fann al-mu'amma wa'l-algaz* (Cezairi), Millet Ali Emiri Arabi 3566, 3567, Beyazıt BM5452, Hazreti Nasuhi D 535.
- Noise to expect: authors scored only by name (Safadi, Ibn Nubata, Suyuti, Ibn Hijja) and the tag "rumûz"/"sırlı" in the note field (Hanafi and
  hadith books use *rumuz* for sigla and *sırlı* for glazed binding). Treat those as 0.

Not found in the part harvested: any copy of Ibn Dunaynir, Ibn 'Adlan, al-Kindi's *Risala fi istikhraj al-mu'amma* or al-Qalqashandi's *Subh* by
title beyond what the earlier sweep listed (Fatih 5300-003/004). `query_counts.tsv` shows the term-level counts so a gap is visible.

## Not done

- Everything marked "not started" above; the Arabic-script term list in particular (المعمى, التعمية, خط سري, القلم المشجر ...).
- Screening on images (none opened). The first looks to make: Arkeoloji 00557, Ali Emiri Arabi 2844, Laleli 2147-004, Hüseyin Şemsi-Fa 78-001.
- Prior-art check of any item (web, DECODE, edition). Only one web search ran (Damascus edition: no manuscript list found).
- Harvest of authors' death date (yazar_hicri <= 905) and of the 905-1110 AH mecmua slice.
- The snapshot is only in the owner's Chrome. `harvest.js` rebuilds it (about 40 minutes for A and D). The old sweep tab (id from the first session)
  had its body replaced by a text dump of the log during wrap-up; reload it.
- No `leads.json`, `catalogue.json`, `targets/` or `docs/` edits.
