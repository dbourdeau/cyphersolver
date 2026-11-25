# YEK portal, records with scans online (26 Nov 2026): catalogue pass done, image screening blocked by sign-in

Run by a Claude Code session with Claude in Chrome. Follows `sweep_2026-11-25_yek_massive` (partial harvest, nothing screened) and
`sweep_2026-11-24_arabic_treatises`. Aim: finish the YEK harvest for records that have scans, rank it, screen the top 60 on the images.

**State.** Steps 1, 2 and 4 (the filter, the re-run queries, the catalogue side of the four loose items) are done. **Step 3, the
screening on images, was not done: this Chrome profile is not signed in to portal.yek.gov.tr** (the header shows "Giris", detail pages say
"Daha fazla bilgi icin lutfen uye girisi yapiniz", and no "Goruntu" link is shown on any record). Signing in needs the owner's credentials,
which an agent must not enter. Nothing was screened, so `candidates.json` has two rows and no `vetting` block. Nothing promoted; no
`catalogue.json`, `leads.json`, `targets/` or `docs/` edits.

To finish: the owner signs in to YEK in this Chrome, then a session opens the 60 records of `ranked_top60.tsv` (and the extra list below)
with the viewer. The harvest is in the portal origin's IndexedDB (db `yekharvest`, store `kv`, key `db2`, JSON `{rows, log, t}`, 38,952 rows with
images, all queries below); `ranked_top60.tsv` is the top of it.

## 1. How the portal marks records with scans

- **The list-view "Goruntu" link is only shown to a signed-in session.** Signed out, 10 of 10 rows of a query had no such link although
  the records have images. The 25 Nov `i` flag in `harvest.js` is therefore unreliable unless signed in (the old IndexedDB snapshot has `i = 0`
  on all 20,476 rows).
- **The reliable flag is the facet "Goruntu Durumu" (Goruntusu Olanlar 488,054 / Goruntusu Olmayanlar 164,246 of 652,300),** a field called
  `dkym_status` (1 = images, 0 = none). Clicking it calls `setFiltering('1','dkym_status')`, which redirects the page to the same search URL
  with `&dkym_status=1`. **It is a plain URL parameter** that the `xajaxSetFilter` POST of the harvest accepts, like the `istinsah_yil` date filter.
  Append `&dkym_status=1` (images) or `=0` (none) to any query of `harvest.js`. Check: title "rumuz" 824 hits = 639 (1) + 185 (0).
  It works signed out, so the filter does not need a login.
- **Results per page** is a session setting: `xajaxPagination('100')` (what `change_rpp(100)` calls) reset itself to 10 in the fresh tab and
  was set again (a display preference only).
- **Single-record check:** an `AllFields`-free lookup by `biblionumber` with operator `equal` plus `&dkym_status=1` returns 1 hit if the record
  has scans and none if not.
- **The filter barely thins the early records.** Images by Hijri istinsah year: 300-399 13 of 14; 400-499 47 of 66 (A harvest of 25 Nov);
  500-599 262 of 298; 600-699 1,052 of 1,107; 700-799 3,071 of 3,170; 800-899 5,786 of 5,940; 900-904 306 of 311. About 96% of the pre-905 AH
  records have images, so the facet saves little there and is decisive only for the terms and classes.

## 2. Queries re-run with `&dkym_status=1` (counts in `query_counts.tsv`, 164 rows)

Every row is hits with images. Terms are AllFields unless noted. Multi-word terms are one rule per token joined by AND (the 25 Nov OR-of-tokens trap).

- **Arabic script, single:** الرموز 475, المرموز 11, المترجم 68, المعمى 23, التعمية 0, الأقلام 125, الكنوز 259, الألغاز 72, اللغز 21, المعمّى 1, الترجمة 76,
  كتابة 955; حل (title) 0.
- **Arabic, AND:** خط+سري 11, القلم+المشجر 0, حل+التراجم 3, حل+الرموز 70, علم+التعمية 0, استخراج+المعمى 1, مفتاح+الكنوز 20, كشف+الرموز 137, صبح+الأعشى 19,
  شوق+المستهام 0, إيضاح+الرموز 8, مفتاح+الرموز 17, القلم+الأقلام 19, كتابة+سرية 1, حل+الألغاز 8, الجفر+الجامع 2. "حل المترجم" 0.
- **Latin AND-phrases:** miftahu+kunuz 46, miftah+kunuz 56, hall+mutercem 0, halli+teracim 3, hall+teracim 7, kalem+sirri 109, sir+yazisi 432,
  gizli+yazi 73, kitabet+sirriye 0, istihrac+muamma 2, ilm+cifr 31, hatt+kadim 13, aklam+kadime 2, sevku+mustehâm 0, subhu+asa 27, duneynir 1, dureyhim 10,
  adlan 243, kalkasendi 34, halli+tercüme 44, kriptografi 2, kriptoloji 0, tamiye 5, taamiye 2, muamma+hall 25, muamma+istihrac 2, lugaz+muamma 52,
  mukattaat 74. (Several of these AND pairs match tokens in different fields of a record, so they are loose: kalem+sirri, sir+yazisi, ilm+cifr.)
- **Latin singles:** rumuz 1,295 (images), remz 693, sifre 12, sifreli 6, muamma 642, mutercem 12, muterceme 7, cifr 60, ebced 363, hurufu 46, gizli 172,
  sirli 2,545, esrar 10,247 (first 1,500 rows kept), kunuz 467, kenz 2,387, kenzu 1,354; title rumuz 639, title muamma 436.
- **Classes with images:** 652.8: 2; 652: 19; 133.3: 66; 133.4: 22; 135: 444; 153: 62; 509: 87; 003: 24; 070: 50; 090: 38; 133: 268; 410: 583; 811: 3,503;
  891: 11,262; 956: 4,854 (first 3,000 rows kept).
- **Record types, istinsah 905-1110 AH with images:** mecmu 20 + 83, mecmua 18 + 81, munseat 12 + 12, insa 53 + 50, mektubat 1 + 6, resail 1 + 13,
  rasail 0, kunnas 1 + 0, mektup 0 + 2, nameler 0 + 3, muharrerat 0, munsea 12 + 12; Arabic title words مجموع 18 + 80, مجموعة 12 + 55, رسائل 1 + 12,
  منشآت 11 + 12, إنشاء 8 + 7, مكاتبات 0 + 2, مجاميع 0 (each pair is 905-999 and 1000-1110 AH). Before 905 AH the date slices above (all records with images, 10,000+ rows) hold every record type.
- **Ottoman register and key terms (list collections and counts):** sifre+defteri 2; sifre+cetveli 0; rumuz+cetveli 15 (noise: Qur'an-reading
  commentaries called *Jami' al-rumuz*, *Kenz al-rumuz*); sifreli+telgraf 1; sifre+miftahi 1; sifre+telgraf 3; sifre+telgrafname 1; sifre+kitabi 1;
  sifre+usulu, talimatnamesi, lugati, kodu, cifr+defteri 0; rumuz+defteri 1; sifre+mektup 3; sifre+muharrerat 1; sifre+muhabere 1; sifreli+mektup 1.
  The 21 distinct rows (images only): Arkeoloji Yazmalari 01652 and 01660, Suleymaniye Ismail E. Erunsal 35, Milli Kutuphane 06 Mil Yz A 10377
  (*Sifreli Hamparsum nota defteri*, music) and 17 Qur'an-reading, hadith and Sufi titles with "rumuz" or "kenz". **No other Ottoman cipher register or
  key book with images exists in YEK** under these terms. Only these four are Ottoman cipher material; the 12-sample screen was not needed.

Not done: the full 811/891/956 class sets beyond the caps, and `esrar`, which is noise.

## 3. Ranking and the screen

Local score (title, author and class fields only): cipher word in the title 3; rumuz, remz, muamma, kunuz and similar 1.5; Arabic cipher words 2;
class 652/133.3/003 2; date up to 905 AH 2, up to 1110 AH 1; up to 40 pages +1; mecmua type +1; a part number +0.5. Of 38,952 harvested rows,
4,239 score 3 or more, 480 score 5 or more, 167 score 6 or more. `ranked_top60.tsv` holds the top 60.

**Reading of the list: it is noise.** The top is full of *Kunuz al-rumuz* / *Izah al-rumuz wa-miftah al-kunuz* (Ibn al-Qabaqibi, commentary on Qur'an
readings), Sufi *rumuz* and *kunuz* books and riddle compendia (*al-Zaha'ir al-Ashrafiyya fi'l-alghaz*, *Hall al-rumuz*). Only the Ibn al-Durayhim
*Miftah* (718705, 30092) and the 01652 / 01660 pair are cipher texts by title. The one unplaced item is Arkeoloji 00557 *Rumuz al-kunuz* (Shuja' al-Din
Ilyas, 1047 AH, class 133.3 with "cifr" in the notes), probably occult; same box as 706146 *Sirr al-asrar*.

**Images screened: none (sign-in).** For the record, items the facet says have **no scans** (so the 25 Nov "first image look" cannot be done at
all): Millet Ali Emiri Arabi 3566 (151508, *Teshil al-majaz*), Beyazit BM5452 (578636), Laleli 2147-004 (300372, *Remz min al-ilm al-maknun*),
Beyazit BM11443 (573905, *Jafr*) and the three loose items of step 4 below. Items that **have scans** and are worth a first image look once signed in:
Arkeoloji 00557; Bagdat 1592 (209748, *Teshil al-majaz*); Reisulkuttab 1197-001 (*al-Mermuzat al-ishrun*); Esad Efendi 1704; Konya Yusuf Aga 4887/3
(*Kashf rumuz*); Ankara Adnan Otuken 06 Hk 1108 and Manisa 2976/8, /9 (Ibn al-Bukka', *al-Tiraz*, *Kenz al-asma*); Suleymaniye Hafid Efendi 296 (261943);
Hacı Selim Ağa 487 (364122, *al-Durr al-munazzam* family; 48 copies with images).

### Ibn al-Durayhim, Ibn Dunaynir, Ibn 'Adlan

- Copies with scans: Esad Efendi 3558-006 (718705; 95 images), Bursa Genel 4808 (30092), Fatih 5300-003/-004 (244314/244315; one volume, 192 images). Same four as
  24 Nov; the image-filtered term runs (duneynir, dureyhim, adlan, kalkasendi, miftahu+kunuz) found no additional copy with scans.
- **Not screened further** (sign-in): Fatih 5300-004 beyond image 93 stays unseen; no worked example beyond the printed text was found in any copy.
- **Which copies the Damascus edition used.** Not stated by the edition's own front matter, which could not be reached. An islamonline article on
  the rediscovery of the *ta'miya* manuscripts (the page named the copyist of Esad 3558 as Sidqi Mustafa b. Salih, dated Friday 10 Ramadan 1149, and
  the Fatih 5300 composite, dated by Sezgin to the 6th century AH) reports the first volume (al-Kindi, Ibn 'Adlan, Ibn al-Durayhim, with a preface by
  Shakir al-Fahham, 1987) but, as summarised by the fetch tool, no shelfmark of a base text. The article's subject being the Istanbul copies
  suggests, but does not prove, that the edition used them. Not checked: the edition's apparatus (Mrayati, Meer Alam, Tayyan 1987; English vol. 3 2004).
  If it used Esad 3558 and Fatih 5300, the Bursa Genel 4808 copy is the one uncollated witness with scans.

## 4. The four loose items

| Item | YEK record | Scans | Result |
|---|---|---|---|
| Millet Ali Emiri Muteferrik 6001, *Miftah: Osmanli sifre anahtarlari* | 395111 | **none** | Printed book (matbu, 2+101 pp.). Cannot be checked on a scan |
| Beyazit BM11616, *Sifre-i umumi ta'rifati* | 574079 | **none** | Catalogue only |
| Esad Efendi 03817-012, Baha' al-Din al-'Amili, *Risala fi'l-alghaz wa'l-ta'miya* | 721421 | **none** | Literary riddles and *ta'miya*; no scan to check |
| Arkeoloji Yazmalari 01652 (708867) and 01660 (708872) | both | yes (91 and 115 images) | Catalogue: 01652 *Sifre miftahi defteri*, 35 ff., the Fourth Army cipher (Erzurum, Van), words and names as 3-digit groups; 01660 *Makam-i Seraskeri ve Ordu-yi Humayunlar Musiriyyet-i Celilelerine yazilan sifreli telgrafnameler*, 112 ff., 1305-1306 AH. **Whether the telegrams in 01660 are ciphered text with a matching key in 01652 or only decoded copies is not settled by this sweep.** The 24 Nov session saw thumbnails 1-21 and image 6 of 01660 (clear copies, no figures) and image 8 of 01652 (a code list); this session could not open images. The portal title of 01660 says "sifreli telgrafnameler" (ciphered telegrams), which the early thumbnails did not bear out. Extents: 112 ff. (about 224 pp.) against 115 images. The remaining 94 images of 01660 are unseen |

Ottoman prior art found by web search (not read in full, titles and abstracts only): Sedat Bingol, "The changes in Ottoman diplomatic cryptography and its
methods during the 19th century (1811-1877)", Cryptologia 2023, pp. 541-569; Anadolu University record "Methods for encryption in early 19th-century Ottoman
diplomatic correspondence"; Melike Karabacak Yilmaz, special-purpose ciphers and codes of the second half of the 19th century (TTK); an English translation of
the Ottoman government's 1907 cipher instructions (consonant groups keyed to months) in the literature. The telegraph-era key books and registers of the
Fourth Army are not known to be covered by them; not checked in their text. DECODE (`research/catalogue_harvest/decode`) and the 24 Nov notes
carry no Arkeoloji 01652 / 01660 record (grep: none).

## Routes learned

- `&dkym_status=1` on the `xajaxSetFilter` POST: the images-only filter, works signed out. Use it in every YEK query.
- Chrome tool output is capped at about 1,300 characters per call and blocks anything that looks like a URL or query string; the harvest therefore stays in
  IndexedDB and is read out as short compact lines. A 100-row page takes 2.5-3 s; 39,000 rows took about 75 minutes of polling.
- Signed-out sessions show truncated detail pages and no image links. A session that needs images must start with the owner signed in.

## Remaining

1. Sign-in, then the top-60 first-image look, the Arkeoloji 01660 / 01652 comparison (check a telegram against the key) and Fatih 5300-004 images 94-192.
2. The 811/891/956 sets beyond the caps and the mecmua titles dated 905-1110 AH that carry no cipher word in the title (screen by sampling contents).
3. The Damascus edition's apparatus.
