# Arabic cryptology treatises and Eastern Christian secret scripts (24 Nov 2026)

Run by a Claude Code session for Daniel Bourdeau, with Claude in Chrome. Aim: targets like Penn LJS 51 f. 106v
(`targets/qaysarani1350`): enciphered text whose decipherment is missing, ideally inside a collection or manual that
solves most of its items. Two routes never swept before: (1) manuscript copies of the Arabic cryptology treatises and
the Mamluk chancery manuals; (2) secret-script colophons and notes in Syriac, Garshuni, Armenian and Ethiopic
manuscripts, through vHMML and the printed catalogues.

**State: not merged, nothing promoted.** A second pass over YEK, signed in with images viewable, is in the YEK section below. `candidates.json` holds 4 rows, none with a vetting block: no ciphertext was
seen on an image for any of them.

## Result

No new target of the LJS 51 kind was found. The treatise route gave the Istanbul and Bursa witnesses of Ibn
al-Durayhim, Ibn Dunaynir and Ibn 'Adlan from the YEK catalogue, but their images need a YEK account, so the question
of extra worked examples or practice ciphers beyond the Damascus edition stays open. vHMML can be searched from Chrome
by its own search box (the Turnstile token is issued to the page; a typed URL gets a 403), and its record JSON and the
IIIF images of "Unregistered" objects answer plain curl. Its catalogue has no Syriac or Garshuni cryptogram notes under
any English term tried; its "secret alphabet" hits are almost all magical alphabets and keys (Timbuktu, Lucknow, ZMT,
Harar). Two ÖNB manuscripts were opened and closed (N.F. 90a-d: pen trials and a decorative *ya Allah ya Muhammad*;
N.F. 303: passage not found on the opening the record names). The printed catalogues gave two Syriac secret-character
notes in the British Library (Wright) and an Armenian set of names in a cryptic alphabet with the plaintext beside it
(Conybeare).

## Findings

| Row | Item | Date | What is there | State |
|---|---|---|---|---|
| 0 | BL Add. MS 21580, fol. 198b (Wright no. DCCXXIII) | 15th-16th c. (notes of 1479, 1518, 1564) | "a signature in secret characters" after four Syriac verses | catalogue only |
| 1 | BL Add. MS 14471, colophon page (Wright no. LXXVII) | MS dated A.D. 615; line undated | "a line of writing in a secret character" on the outer margin | catalogue only; check the shelfmark on Wright's page |
| 2 | Beirut USJ MS 2/980, fol. 161r | 16th c. | "Poems in Turkish and secret alphabet" beside the colophon | vHMML, images need sign-in |
| 3 | ÖNB Cod. N.F. 303 (Ibn al-'Arabi, *'Anqa' mughrib*) | 16th c. (?) | "writing in a secret alphabet"; probably the author's own enigmatic letters | opening 70v-71r seen, passage not located |

Not rows:

- **Treatise witnesses (YEK catalogue, images behind login):** Ibn al-Durayhim, *Miftah al-kunuz fi idah al-marmuz*:
  Bursa İnebey, Genel 4808, and Süleymaniye, Esad Efendi 3558-006 (dated 10 Ramadan 114x AH, i.e. 1727-1737);
  Ibn Dunaynir, *Zubdat fusul* ... *fi hall al-tarajim*, Süleymaniye, Fatih 5300-003; Ibn 'Adlan, *al-Mu'allaf lil-Malik
  al-Ashraf fi hall al-tarajim*, Fatih 5300-004. Not checked: which of these the Damascus edition (Mrayati, Meer Alam,
  al-Tayyan 1987; English vol. 3, 2004) used. If it used one copy of the *Miftah*, the other is an uncollated witness
  that may carry extra examples. Worked examples in the treatises are solved in the treatises themselves (15 Nov sweep,
  part D).
- **Conybeare, Armenian MSS in the British Museum (1913):** names written "in a cryptic alphabet partly imitated from
  cuneiform" under a colophon of 1598 that gives the same names in clear (known plaintext, so read or readable); a
  colophon of 1606 whose ten dots stand for the scribe's name (Jacobus); an alphabet book with 75 specimens including
  cryptograms of Arabic alchemists (key material).
- **vHMML, magical and key items (excluded):** Timbuktu SAV BMH 23261, 16959, SAV ABS 958, 5319, 3853 ("On secret
  writing", 2 pp.); Harar EMIP 01770; Mahmudabad MS 545, 1020, 1087; ZMT 01189, 02959; USJ 1878; ÖNB A.F. 496 (abjad and
  secret alphabets with talismans); ÖNB Mixt. 1353 ("numerous letters from secret alphabets", not opened); ÖNB N.F. 412
  (secret alphabets, not opened); Melk 1086 (Rudolf IV alphabet, on-site only).
- **vHMML, Greek and Slavonic side hits:** ÖNB Phil. gr. 231, fol. 194v-195r, scribe's name "given in cryptography"
  (15th c.); ÖNB Phil. gr. 211, notes on cryptography; Lviv Ркк-650, fol. 356r, cryptography read backwards
  (17th c.); Mdina AIM Mem. 24, "Volume includes cipher" (18th c., Malta). Outside this sweep's scope; left for the
  Greek/Slavonic and Malta sweeps.

## Routes

| Route | Method | Result |
|---|---|---|
| vHMML Reading Room search | **Chrome**, typing in the page's own search box; a typed `search?keywordQuery=` URL returns 403 "Turnstile validation failed" | Works. Terms: cryptogram 0, "secret script" 1, "secret writing" 13, cryptographic 1, cryptography 4, cipher 1, ciphers 1, "secret alphabet" 19, encrypted 0, cryptic 0, "secret characters" 0 |
| vHMML record JSON | plain curl of `www.vhmml.org/readingRoom/view/<id>` (`selectedObjectJson` in the page) | Works, no bot check |
| vHMML IIIF (Unregistered objects) | plain curl: `www.vhmml.org/image/manifest/<id>?objectType=READING_ROOM`, images `.../image/READING_ROOM/<path>/<file>.jpg/full/<w>,/0/default.jpg` | Works; "Registered" objects need a sign-in (not done) |
| YEK (Türkiye Yazma Eserler Kurumu) | **Chrome**, `portal.yek.gov.tr/works/search/full?key=<term>&search_key_type=3&search_form_type=ALL_FIELDS`, fetched in page | Catalogue works; terms Düreyhim 11, Adlân 4, Dünaynir 0, "Halli't-Terâcim" 2, Ta'miye 1, Muammeyât 28 (Persian riddle verse), Mermûz 5. Images need login (not done); the page loads reCAPTCHA but showed no challenge |
| Qalamos / orient-digital | curl and Chrome | connection reset / Chrome error page (network refusal, not a CAPTCHA) |
| Gallica SRU | curl | 403 (not retried in Chrome; De Slane was grepped on 15 and 16 Nov) |
| QDL | curl | 403 (not retried) |
| Leiden digital collections | curl | home 200, search closed the connection; not retried in Chrome |
| Bodleian, Fihrist, Chester Beatty | curl | home pages 200; no search run |
| archive.org catalogue text | plain curl (`advancedsearch.php`, `_djvu.txt`) | Wright BM Syriac vols 1-3 (28 hits, 2 relevant), Wright BM Ethiopic 1877 (0), Conybeare BM Armenian 1913 (24, 3 relevant), Baronian-Conybeare Bodleian Armenian 1918 (4, none) |
| Web search | literature on Syriac cryptogram colophons; Ibn al-Durayhim manuscripts | Nothing specific: no list of Syriac cryptogram colophons read or unread was found; Kitzinger 2024 "Of colophons and cryptographs" is on Latin colophons |

No CAPTCHA was shown on any host in this sweep.

## YEK pass, signed in (24 Nov 2026, second session)

Türkiye Yazma Eserler Kurumu portal, 652,305 records, searched through Claude in Chrome in the owner's signed-in session. Route:
the search page sends a GET request (`/works/search/full?key=...&search_key_type=3&search_form_type=ALL_FIELDS`), and the same request works as a
same-origin `fetch()` from inside a portal tab. Results per page is a session setting (`rpp`, set once to 100 with the
page's own selector). Further pages are `/works/search/full/<offset>?key=...`. Every term with 600 hits or fewer
was paged to the end. The three larger terms (rumûz 744, الرموز 534, قلم 421) were read for their first 100 rows only. Record
pages are `/works/detail/<bib no>`. A "Görüntü" link opens the image viewer, which worked for every record tried. No CAPTCHA appeared.

**Hits per term (all fields):**

- **Ibn al-Durayhim:** Düreyhim 11, Dureyhim 11, الدريهم 11.
- **Miftah al-kunuz:** Miftâhu'l-künûz 40, Miftahu'l-kunuz 40, مفتاح الكنوز 15. Most of these are Ibn al-Qabaqibi's *Izah al-rumuz wa-miftah al-kunuz* (see below). merműz / mermûz 5.
- **Ibn Dunaynir and Ibn 'Adlan:** Düneynîr 1, Dunaynir 0, دنينير 0; Adlân 4, Adlan 4, عدلان 2.
- **Tarajim and mutarjam:** Halli't-Terâcim 2; Terâcim 448 (all biographies); hall-i mütercem 0; حل المترجم 0; mütercem 15 and المترجم 59 (all "translator").
- **Cryptography class:** Kriptografi 2, 652.8 2. The bare term "652" gives 342 hits, but these match other fields; only the two 652.8 records are cryptography.
- **Ta'miya:** ta'miye 1, tamiye 1, التعمية 0. تعمية gives 7, all glosses on Hayali where the word has a theological sense.
- **Mu'amma:** muammâ / muamma 176, Muammeyât 28, المعمى 25. These are Persian and Ottoman name-riddle verse and *mu'amma* treatises by Jami and others. استخراج المعمى 0.
- **Istikhraj:** istihrâc 122 (astronomy, fiqh).
- **Qalqashandi:** Subhu'l-a'şâ / Sübhü'l-a'şâ 47, Kalkaşendî 61. No copy of the *Subh* volume with the cipher chapter was identified by title. The hits are Qalqashandi's other works and unrelated titles that contain *a'sha*.
- **Old scripts:** aklâm 69, الأقلام 112, el-aklâmü'l-kadîme 0, hatt-ı kadîm 0, خط قديم 0.
- **Symbols:** rumûz 744, الرموز 534, remz 65.
- **Şifre:** şifre 6, şifreli 6, şifre usulü 0.
- **Secret writing:** kalem-i sırrî 0, sır yazısı 0, gizli yazı 0, kitâbet-i sırriye 0.
- **Ibn Wahshiyya:** İbn Vahşiyye 37, Vahşiyye 38 (agriculture and magic). No *Shawq al-mustaham* by title: Şevku'l-müstehâm 0, شوق المستهام 0.
- **Other:** Kenzü'l-esrâr 56 (alchemy, sufism); mukattaa 10 (the Qur'an's isolated letters); elifbâ 96; Kindî 218; Melikü'l-Eşref 5; cifr 148 (divination, screened by title only).
- **Ibn al-Qabaqibi:** Kabâkıbî / Kabakıbî / Kabâkibî 28, القباقبي 22.

**Records** (bib no. = YEK record):

| Bib no. | Library, collection, shelfmark | Item | Date | Folios | Images | Screened |
|---|---|---|---|---|---|---|
| 718705 | Süleymaniye, Esad Efendi 03558-006 | Ibn al-Durayhim, *Miftah al-kunuz fi idah al-marmuz* (652.8 Kriptografi) | copied 10 Ramadan 1149 (Jan 1737) | 47b-59a, 21 lines | yes (95 images, spreads) | Images 50-62 (ff. 47b-59a): plain naskh text. The worked examples are written out in letters and solved in the text. No sign alphabets, no marginal cipher. Ff. 66-67 (images 69-70, after the treatise) hold abjad letter-number tables and sums: numerology, not ciphertext |
| 30092 | Bursa İnebey, Genel 4808 | same work | not given | 13 ff., 23 lines | yes (13 images) | All 13 thumbnails, one spread at full size: text only, no tables or sign runs |
| 244314 | Süleymaniye, Fatih 05300-003 | Ibn Dunaynir, *Zubdat fusul Ibn Dunaynir fi hall al-tarajim* | not given | 54-88, varying lines | yes (192 images) | Images 55-93 as thumbnails, f. 59 (image 60) at full size: text, with one boxed letter example on f. 59r. No sign tables |
| 244315 | Süleymaniye, Fatih 05300-004 | Ibn 'Adlan, *al-Mu'allaf lil-Malik al-Ashraf fi hall al-tarajim* | not given | same volume | yes (same volume) | Only as far as image 93; later thumbnails did not load |
| 708867 | İstanbul Arkeoloji Müzeleri, Arkeoloji Yazmaları 01652 | *Şifre miftâhı defteri*: key to the cipher of the Fourth Army (Erzurum, Van); words and names as 3-digit groups | late 19th c. (undated) | 35 ff. | yes (91 images) | Image 8 seen: a code list (word = 3-digit group). Key material, no ciphertext |
| 708872 | İstanbul Arkeoloji Müzeleri, Arkeoloji Yazmaları 01660 | Register of cipher telegrams sent to the Seraskerlik and the army commands | 1305-1306 (1889-1891) | 112 ff. | yes (115 images) | Thumbnails 1-21, image 6 at full size: clear copies, no figures. A deciphered register that pairs with 01652 |
| 739481 | Süleymaniye, İsmail E. Erünsal 00035 | *Mecmû'a-i muharrerât*: Crete and western Thrace correspondence, with copies the catalogue calls "şifre" | 1293-1295 (1876-1878) | 26+V ff. | yes (34 images) | All thumbnails: clear copies in rik'a, no figure groups |
| 395111 | Millet, Ali Emiri Müteferrik 6001 | *Miftâh: Osmanlı şifre anahtarları* | not given | 2+101 pp. | not opened | Printed book (matbu) of cipher keys |
| 574079 | Beyazıt, BM11616 | *Şifre-i umûmî ta'rîfâtı* | not given | not given | no Görüntü link | Catalogue only; general cipher instructions (key material) |
| 721421 | Süleymaniye, Esad Efendi 03817-012 | Baha' al-Din al-'Amili, *Risala fi'l-alghaz wa'l-ta'miya* | 1074 (1663-64) | not given | no Görüntü link | Treatise on literary riddles (*lughz*, *mu'amma*) |

Other records with cipher words in their titles hold no ciphertext:

- 610668 *Şifre-i ma'arif* (Milli Kütüphane, 1898): by its title, a code book of the education ministry.
- 615407 *Şifreli Hamparsum nota defteri*: music in Hamparsum notation.
- 246937, 261404, 324857, 710802: "şifreli" is used in the sense of binding or a note.

The Persian *mu'amma* treatises are name-riddle verse and were not opened: Süleymaniye Ali Nihat Tarlan 115-009, 115-010 and 199-002; Giresun 180-017; Hacı Beşir Ağa 163; Kadızade Mehmed 381 (*Hulel-i mutarraz*, 866); Köprülü Hacı Ahmed Paşa 362-023; the Konya BY series.

**Findings.** No ciphertext of the LJS 51 kind was seen. The three treatise witnesses with images show only the treatise text.

Which copies the Damascus edition used could not be confirmed from the web. The English vol. 3 is on pdfcoffee.com, which returned 403 to a fetch, and it was not opened in Chrome.

The new items are Ottoman key material and one matching deciphered register:

- Keys: Arkeoloji 01652, Millet Ali Emiri Müteferrik 6001, Beyazıt BM11616.
- Deciphered register: Arkeoloji 01660.

None goes in `candidates.json`, because no ciphertext was seen. For a later sweep: these key books could read 1870s-1890s Ottoman cipher telegrams, if any turn up in the Ottoman state archive (BOA), which YEK does not hold.

**Ibn al-Qabaqibi (side check for `qaysarani1350`; that folder was not edited).**

- **YEK authority form:** İbnü'l-Kabâkıbî, Ebû Abdullah Şemseddin Muhammed b. Halil b. Ebû Bekir el-Halebî, d. 849/1445.
- **Life:** TDV İslâm Ansiklopedisi (islamansiklopedisi.org.tr/ibnul-kabakibi) gives birth in Aleppo in 777 or 778 (1375-76), blindness from 848, and death in Jerusalem on 20 Rajab 849 (22 Oct 1445). He taught the Qur'an readings at the Jawhariyya madrasa.
- **Works** (from TDV, Arabic Wikipedia via 3rabica.org, and YEK):
  - *Majma' al-surur wa-matla' al-shumus wa'l-budur*, a verse work on the 14 readings (Süleymaniye Bağdatlı Vehbi 31; Köprülü Fazıl Ahmed Paşa 27).
  - Its commentary, *Idah al-rumuz wa-miftah al-kunuz* (Kılıç Ali Paşa 23; Köprülü Fazıl Ahmed Paşa 19). 3rabica cites an edition by Dar 'Ammar, 2003.
  - *Taysir ma fi'l-Mustalah* (Esad Efendi 29).
  - *Urjuza fi'l-tajwid*.
  - *Zubdat al-muqtafa*, on the *Shifa'*, finished 815/1412 (Ayasofya 586).
  - *Takhmis al-Burda* and *Takhmis Banat Su'ad*.
  - A *badi'iyya* answering Safi al-Din al-Hilli.
  - *al-Zahr al-mukhtar min Rabi' al-abrar*.
  - *al-Qira'at al-sitta* and *Risala 'ala wujuh al-qira'at* (YEK titles).
- **No cipher works:** none of these sources lists a riddle, *mu'amma* or cipher-verse work, and none names al-Qaysarani.
- **Search trap:** his *Idah al-rumuz wa-miftah al-kunuz* shares title words with Ibn al-Durayhim's *Miftah al-kunuz fi idah al-marmuz*. It supplies most YEK hits for "Miftâhu'l-künûz".
- **Different person:** Burhan al-Din Ibrahim b. Muhammad al-Qabaqibi al-Halabi (d. c. 850) appears in web results and should not be confused with him.

**Still unswept in YEK:**

- The terms read for their first 100 rows only (rumûz, الرموز, قلم): rows past 100.
- Fatih 5300 after image 93 (Ibn 'Adlan's part), one image at a time.
- Detaylı Arama on the Tasnif field. The all-fields search for "Kriptografi" and "652.8" already returns the two 652.8 records.
- Millet Ali Emiri Müteferrik 6001 (printed), not opened.

## Still unswept

- YEK images of Bursa Genel 4808, Esad Efendi 3558 and Fatih 5300 (needs a YEK account held by the owner), and the
  Damascus edition's manuscript description, to see whether either *Miftah* copy is uncollated.
- Al-Qalqashandi, *Subh al-a'sha*, cipher section (vol. 9) in manuscript (BnF, Süleymaniye, Dar al-Kutub): not opened;
  the printed Cairo text has its worked examples solved.
- Mamluk chancery manuals (al-'Umari, *al-Ta'rif*; Ibn Nazir al-Jaysh, *Tathqif al-ta'rif*): not searched.
- Syriac: Payne Smith (Bodleian 1864), Zotenberg (BnF Syriac 1874), Assemani (Vatican), Scher (Seert, Diyarbakır),
  Vööbus's colophon collections, and the CFMM/Mardin collections on vHMML (whose records carry few notes) were not
  grepped or paged. Sachau and Mingana were grepped on 16 Nov.
- Ethiopic: Zotenberg (BnF 1877), Dillmann (Bodleian, Berlin), Conti Rossini (Abbadie) not grepped; EMML records on
  vHMML gave no cryptogram hits.
- Armenian: Matenadaran, Jerusalem St James, Venice and Vienna Mekhitarist catalogues not grepped.
- vHMML: ÖNB N.F. 303 images 5-72, ÖNB Mixt. 1353 and N.F. 412 not screened; "Registered" items (USJ 2/980) not seen.
