# Sweep: Süleymaniye Library via the YEK portal (27 Nov 2026)

**Duplicate of earlier work, found only when this was filed.** `sweep_2026-11-24_arabic_treatises` (YEK signed in, about 70 terms
paged to the end, images of Esad Efendi 3558-006, Bursa 4808, Fatih 5300 and others screened, no ciphertext),
`sweep_2026-11-25_yek_massive` and `sweep_2026-11-26_yek_scanned` had already covered YEK and Süleymaniye. This pass was
run from a checkout 807 commits behind and added nothing to them except the notes below (the 652.8 "Kriptografi" class has
two records; the title-matched "treatises" 199776, 248448, 203379, 208837, 194404 are hadith, Sufism, fiqh, jafr and riddle
texts; 721421 and 256465 are three-folio tracts). Read those folders first.

Result: **no unread ciphertext found; nothing promoted; no candidates.json.** Catalogue-level pass only, no images fetched.

## Route
`portal.yek.gov.tr` (Türkiye Yazma Eserler Kurumu union catalogue, 652,306 records, Süleymaniye among its libraries) works from
the user's machine in Chrome. curl gets an empty JS shell, so use `mcp__claude-in-chrome__javascript_tool` on
`https://portal.yek.gov.tr/works/search/full` and `fetch` the GET form: `?key=<term>&search_key_type=1&search_form_type=ALL_FIELDS&rpp=100`
(`rpp` 10/20/50/100 works; a `page` parameter was not found, so use terms specific enough to stay under 100 hits).
Multi-word keys match as OR (11,102 hits for "şifre kitabı"): use single words. Result blocks are `.marc-content-results-label` rows;
filter on "Süleymaniye Kütüphanesi". The harness blocks tool output that contains URLs with query strings.
YEK holds catalogue records only: images are on the Süleymaniye side (not reached, see below).

## Terms run (31)
şifre (15 hits), şifreli (6), şifre anahtarı (41), tamiye (8), kriptografi (2), kriptoloji (0), telgraf şifresi, rumuz (1,506),
remz (1,153), muamma (683), istihraç (281), cifr (250), miftah, تعمية (10), المعمى (27), شفرة (2), شفره (5), رموز, مفتاح,
ترجمان, استخراج المعمى and the multi-word ones. 2,446 unique records, 203 Süleymaniye records with a cipher-ish title.

## What Süleymaniye holds, by title
* **Only one Süleymaniye record is classed as cryptography.** YEK class 652.8 "Kriptografi" has 2 records in the whole union
  catalogue, both Ibn al-Durayhim, *Miftāḥ al-kunūz fī īḍāḥ al-marmūz*: 718705 (Süleymaniye, Esad Efendi 3558/6, ff. 47b-59a,
  copied 10 Ramaḍān 1149 = 1736) and 30092 (Bursa İnebey 4808, 13 ff., undated). The detail pages carry no image link
  (full record needs a member login).
* **Checked and not cryptology (my first pass listed them as treatises):** 199776 *Iṣlāḥ al-rumūz wa-Miftāḥ al-kunūz* is a
  hadith compilation (297.35); 248448 *Ḥall al-rumūz wa-mafātīḥ al-kunūz* (Ibn Ghānim, Sufism, copied 1017); 203379 *al-Ramz fī
  'ilm al-istibdāl* is fiqh (about substitution of endowments); 208837 *Rumūz al-kunūz fī'l-jafr* is jafr; 194404 *Ḥall al-ramz*
  is a riddle-solving text. 
* **Opened last (27 Nov):** 721421 *Risāla fī'l-alghāz wa't-ta'miya*, Bahā' al-Dīn al-'Āmilī (d. 1621), Esad Efendi 3817/12, ff. 86b-88b
  (3 folios), copied 1074 AH (1663/4), class 133 (occult), i.e. a short riddle-and-obscuring tract of a known author, no
  ciphertext indicated. 256465 *Hurūfīlere ait rumuzlar*, Hacı Mahmud Efendi 3359/4, ff. 69-71, Turkish, class 297.752 Hurūfiyya:
  three folios of Ḥurūfī signs ("various lines" per page), a sign table, not a message. Neither shows unread ciphertext on the
  record; images not seen.
* **Literature (step 2):** Mrayati, Meer Alam and Tayyan located and edited 15+ Arabic cryptology manuscripts, mostly from the
  Süleymaniye, from 1979 (Damascus 1987; English "Arabic Origins of Cryptology" vols 1-7, KACST). So the library's cryptology
  holdings were already collected and read; nothing suggests unread cipher text beyond the treatise examples.
* **Not cryptography:** the *mu'ammā* records (228572, 228573, 230491, 257650, 261943, 266547, 267714, 267805, 269246/7, 273569,
  319976, 324099, 330354, 533425) are the riddle/chronogram-poem genre; *Evzaḥ al-ramz 'alā naẓm al-kanz* (231207-10, 239477,
  274804-07) is a fiqh poem; *rumūz/künūz* titles are Sufi, alchemical or jafr; the 1927-ish *Telgraf* items are radio-telegraph textbooks;
  *cifr* records are jafr divination.
* **Checked, see above:** 256465 *Hurūfīlere ait rumuzlar* (Ḥurūfī sign alphabet; would be an alphabet, not a message).
  Also 385509 *Yazma kitaplar anahtarı* (a finding aid, not a key).
* No Ottoman diplomatic code book or telegram cipher sheet turned up at Süleymaniye: those sit in BOA and Koç (see
  `sweep_2026-11-14_koc_ottoman_deep`).

## Not done
Images: Süleymaniye's own digital library and the Yazma Eserler digital reader were not tried. 120 title-matched records were
read only for the 60 titles above; the remaining cipher-keyword hits (mostly noise) were not opened. Record-level notes (colophon,
"şifreli" remarks inside mecmua contents) are not searched: YEK full-text covers titles and content notes only.
