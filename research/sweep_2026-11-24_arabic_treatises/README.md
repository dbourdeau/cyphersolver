# Arabic cryptology treatises and Eastern Christian secret scripts (24 Nov 2026)

Run by a Claude Code session for Daniel Bourdeau, with Claude in Chrome. Aim: targets like Penn LJS 51 f. 106v
(`targets/qaysarani1350`): enciphered text whose decipherment is missing, ideally inside a collection or manual that
solves most of its items. Two routes never swept before: (1) manuscript copies of the Arabic cryptology treatises and
the Mamluk chancery manuals; (2) secret-script colophons and notes in Syriac, Garshuni, Armenian and Ethiopic
manuscripts, through vHMML and the printed catalogues.

**State: not merged, nothing promoted.** `candidates.json` holds 4 rows, none with a vetting block: no ciphertext was
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
