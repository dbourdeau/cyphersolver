# Arabic-script cryptology sweep (6 Nov 2026)

Aim: the oldest real ciphertext (not treatise, not key) in Arabic script (Arabic, Persian, Ottoman, Maghribi, Mamluk,
Andalusi; Judaeo-Arabic at the edge) that this project could read, 1000-1400 CE first, to 1500 second.
Nothing written to `catalogue.json`, `docs/` or git. No `candidates.json`: nothing qualifies as an unread lead (see below).
Overlap: `research/sweep_2026-11_hebrew/` already tabulated the Geniza ciphers (same PGP search); not repeated here.

## Result in one paragraph

No unread Arabic-script ciphertext of text length dated before 1500 was found online. The oldest real enciphered
Arabic-script texts found are (a) Penn LJS 51, 15th c. Syria, cipher letters in ~150 alphabets WITH Arabic
transcriptions by the compiler (so read, and a key/plaintext corpus, not a target), and (b) Cairo Geniza Judaeo-Arabic
cipher letters (T-S NS 70.1, T-S AS 205.186, ENA 4100.7b, T-S NS J479), undated 11th-13th c., most read or about to be
read by Bohak/Zinger/Elbaum. Everything else is treatises, riddle-poems (mu'amma = Persian enigma verse, not cipher),
fiscal "cipher" signs (siyaq/raqam, Coptic numerals) or 16th c. and later.

## Findings table

| Item | Date | Length | Images | Read? | Verdict |
|---|---|---|---|---|---|
| Penn LJS 51, "Collection of alphabets and encoded correspondence" (Schoenberg), Arabic, naskh, 106 ff., 13 lines | "14--"/15th c., Syria? | cipher letters in ~150 alphabets, ~13 lines/page, ciphertext lines seen on image (word separators present) | OPenn, public: `https://openn.library.upenn.edu/Data/0001/ljs51/data/web/0084_NNNN_web.jpg` (NNNN = 0000..; throttled, 16 KB/s bursts), page https://openn.library.upenn.edu/Data/0001/html/ljs51.html, Digital Scriptorium DS738, Colenda 81431-p3br8mg9s | Catalogue: letters "accompanied by transcriptions of the letters in Arabic"; red Arabic equivalents above some alphabets. Only a Voynich Ninja thread (thread-4685) looks at the glyphs; no scholarly study found (Transformation of Knowledge 2006 p.43 only) | Oldest real Arabic-script ciphertext online, but already paired with plaintext. Use as key/control corpus; check whether EVERY letter has its transcription (not done: needs ~100 page views) |
| CUL T-S NS 70.1 verso (PGP 26158) | undated Geniza | one letter | CUDL via PGP | Cracked by Bohak 2025, edition by Bohak/Zinger/Elbaum forthcoming | read, unpublished |
| CUL T-S AS 205.186 (PGP 42291) | undated | damaged fragment, alef-tet + dot x10/x100 numeral cipher | `images.lib.cam.ac.uk/iiif/MS-TS-AS-00205-00186-000-00001.jp2` | deciphered by Elbaum 2026 | read |
| JTS ENA 4100.7b recto (PGP 11951) | undated | 6 lines in a son-to-mother letter, Qus | PGP / JTS | tag "cipher to examine", unread | too short (6 lines) |
| CUL T-S NS J479 (PGP 8804) | after c.1250 | one folio both sides | CUDL, blog images | ~22 symbols mapped by Elbaum, not read | Hebrew sweep's lead; erotic jottings |
| SOAS MS 12217, Qur'an in ta'miya (ring-letter) cipher | date uncertain | Surahs 2-6 fragment | SOAS digital | decoded by D'Ottone, JIM 11 (2020) 133-176 | read (text predictable) |
| Mashhad, Astan-i Quds, Babur Shah's coded Qur'an | 10th/16th c. | full Qur'an | n/a | D'Ottone, JIM 16 (2025) 125-162 | read, 16th c. |
| Penn LJS 409 (alchemy, partial code, key f.3r) | 16th-17th c.? | occasional | OPenn | key present | out of range |
| Princeton Islamic MSS Third Series 223 "Risalat al-mu'amma" | 1510-1600 | treatise | DS13827 | n/a | treatise, out of range |
| Wellcome MS Arabic 259 "Miftah al-kunuz" | 1850s | Persian/Arabic medical | Wellcome | n/a | NOT Ibn al-Durayhim (same title only). Negative |
| Borg cipher (Vatican, 17th c.) | 17th c. | long | Vatican | read 2016 (Aldarrab, Knight, Megyesi) | out of range |

## Treatises (task item 2)

Al-Kindi (c.850), Ibn 'Adlan (d.1268), Ibn al-Durayhim (d.1361, Miftah al-kunuz fi idah al-marmuz), Ibn Dunaynir, al-Qalqashandi
(Subh al-a'sha, 1412) survive through the Istanbul (Suleymaniye) manuscripts edited by Mrayati/Meer Alam/at-Tayyan (Damascus
1987 ff.; English "Arabic Origins of Cryptology" vols 1-7) and Al-Kadi, Cryptologia 16 (1992). Their worked examples are in the
editions. Not followed to the manuscripts: Suleymaniye is not digitised for scripts. No source says any contains unread ciphertext
beyond the printed examples. Schwartz, Cryptologia 33 (2009) covers Ayyubid/Mamluk chancery cryptology: no surviving
chancery cryptogram named.

## Sources tried

| Source | Route | Result |
|---|---|---|
| Princeton Geniza Project `?q=cipher` (39 hits) | curl works | table above; rest fiscal signs. Other queries (cryptogram, encoded) 0 hits |
| Cambridge Genizah blog 2022 (Elbaum) | WebFetch | J479, Zinger letter (words mostly begin with alef, not simple substitution, unlocated), India Book Coptic-numeral code |
| Fihrist (UK Islamicate union catalogue), live site | Anubis proof-of-work page for curl; **needs a real browser** | Instead cloned github.com/fihristorg/fihrist-mss (15,638 TEI records, 338 MB, scratch only) and grepped cipher/mu'amma/ta'miya/Wahshiyya/Shams al-Ma'arif/"unknown script": only Persian mu'amma riddle treatises (BL Delhi Pers. 1210-1213, Cambridge Or. 14, Add. 3674-5, T 2, Oxford Selden sup. 32, SOAS 46438), raqam/siyaq number tables (CUL Add. 304 of 1220; Bodl. Or. 76; Rawlinson Or. 22), Shams al-Ma'arif copies, Tipu Sultan ciphers (1790s). No Arabic-script ciphertext before 1500 |
| DECODE (repo dump research/catalogue_harvest/decode/views*.jsonl, 2,351 records) | local grep | 0 Arabic/Persian/Turkish-script records; Ottoman items are Dutch/Hungarian/French cipher letters from Constantinople, 1548+ |
| Wellcome catalogue API | curl | 0 relevant (MS Arabic 259 is medical) |
| Digital Scriptorium | curl works, search is fuzzy | surfaced LJS 51 (DS738), Princeton 223; Princeton Islamic, Vassar, Newberry hits are generic, not screened individually |
| QDL (qdl.qa), Chrome same-origin fetch | 503 "Backend fetch failed" / 403 on every query today | not swept for Arabic terms; retry later (BL Arabic scientific MSS are the only relevant QDL part) |
| Gallica SRU, Library of Congress search, Princeton catalog JSON, University of Rome IRIS | curl: Cloudflare 403 / empty | not swept; Chrome needed (Gallica/Calames "arabe" + chiffre/ecriture secrete) |
| WebSearch: Nasrid/Marinid/Hafsid letters at ACA | | the 200+ Arabic documents at ACA studied for diplomatics (Labarta, Potthast, Viladrich): none described as ciphered |
| WebSearch: Persian/Ilkhanid/Seljuk chancery ciphers, HistoCrypt Arabic papers | | nothing found |

## Needs Chrome or a human

- Fihrist live search, Gallica/Calames (BnF Arabe), British Library Or. catalogue, Digital Bodleian, Staatsbibliothek Berlin
  (Ahlwardt catalogue lists the Arabic cryptology treatises under "Geheimschrift"), Escorial Arabic MSS, Suleymaniye,
  Princeton Islamic catalogue (curl blocked).
- LJS 51: complete the page-by-page check (download all ~210 images from OPenn with long timeouts; the host trickles).
- Ask Zinger/Bohak (Geniza) for the unlocated alef-initial cipher letter and the T-S NS 70.1 edition.

## Chrome pass, QDL (6 Nov 2026)

qdl.qa opens in Chrome without a check (curl and scripts get 503/403). English "cipher": 3,927 matches in 516 records, but the
date facets are 1600-99 (5), 1700-99 (1), 1800-99 (59), 1900-99 (3,870): nothing before 1600, all India Office / Gulf
Residency files (letters "in cipher" of 1852, 1868, 1875; censorship and code files of 1913-46). The Arabic term تعمية returns
no results (QDL descriptions are English). Same-origin `fetch` from the tab returned 403 on about half of 12 further terms
(rate or bot rules), so only the browser navigation route works. No Arabic-script cipher text before 1600 found on QDL.
Dead end for the 1000-1400 goal. Not reached: BnF Arabe, British Library Or., Berlin, Escorial, Suleymaniye, Princeton Islamic.

## Chrome pass, other Arabic sources (6 Nov 2026)

- **Qalamos** (qalamos.net, German Islamic manuscripts union catalogue): both navigations (a search URL and the home page) were
  redirected to another domain and the extension refused to read the tab ("page navigated to a different domain"). Not swept.
  Needs the user to open it by hand, or a different entry route.
- **Fihrist** (fihrist.org.uk; UK Arabic/Persian/Turkish MSS): the old `/search` URL is a 404, `/catalog?q=` works in Chrome (and
  same-origin fetch, 3 s apart, returned 200 throughout). Terms tried: cipher, cryptogram, cryptography, "secret alphabet", encrypted,
  mu'amma, ta'miya, "cipher alphabet", "secret script", "in cipher", istikhraj, tashfir, "hidden writing", coded. Hits are
  only mu'amma riddle-poems (Nishapuri d. 904 AH, Or 6836, Rylands Persian 134), miscellanies on divination and riddles
  (Delhi Persian 853, 1212), astronomical istikhraj texts and translations of Persian letters (IO Islamic 4225-4232). No ciphertext.
- **BnF archives et manuscrits**: the guessed results URL returned "page n'existe pas"; the real search form was not driven
  (cookie banner, form). Not swept. Calames/BnF Arabe still open.
- Not reached: British Library Or. catalogue, Staatsbibliothek Berlin (Ahlwardt), Escorial, Suleymaniye, Princeton Islamic.

## Chrome pass, BnF archives et manuscrits (6 Nov 2026)

Route: archivesetmanuscrits.bnf.fr; the simple-search form is a POST to `/resultatRechercheSimple.html` (fields `TEXTE_LIBRE_INPUT`,
`DOC_NUMERISE_INPUT_RADIO=all_docs`); filling the box and submitting the form in the tab works, `get_page_text` then reads the
list. A background `fetch` loop is slow (several seconds per term; the tool call times out at 45 s, so start it into
`window.__out` and poll). The guessed GET URL with `mots=` is wrong. Cookie banner declined (non-essential).
Counts (all collections): cryptographie 16, cryptogramme 2, écriture chiffrée 12, écriture secrète 25, alphabet secret 8
(other terms not finished). Read lists for cryptographie and écriture secrète: Latin MSS with cryptic marginalia (Latin 974, 1993,
2335, 3236, 3277, 3528, 3713, 3719, Dupuy 661/673), tironian notes (Latin 8777-8780), NAF 10760 and 11238 (17th-18th c.), and
**Hébreu 881** (Postel-circle Kabbalah miscellany, c. 1600; ff. including a Latin text "en caractères cryptés", digitised with Ktiv):
out of range. The two Arabe hits for écriture secrète (Arabe 1966, a Prophet biography; Arabe 97, Roman Mass prayers) look incidental,
not opened. No Arabic- or Hebrew-script cipher text before 1500 on BnF Archives et manuscrits.

## Chrome pass, British Library and Qalamos (6 Nov 2026)

- **Qalamos**: third failed attempt (search URL in a fresh tab): the tab fell back to a blank page and the extension refuses to read a
  tab that changes domain. Not swept; the user would have to open it by hand.
- **British Library Archives and Manuscripts Catalogue** (searcharchives.bl.uk, interim catalogue of records made before Oct 2023;
  works in Chrome): `/?search_field=all_fields&q=...&page=N` returns 10 records a page; same-origin fetch, 2.5 s apart, ran as a
  background loop into `window.__r` (the tool call itself times out at 45 s). Queries: cipher, cryptogram, cryptic, "secret
  alphabet", "secret script", encoded, cryptography, "in code" (146 unique records over up to 4 pages each). Oriental Manuscripts hits:
  Or 7243 (Turkish/Arabic, early 18th c.), Or 9861 (Hebrew magical texts, 1500-1599), IO Islamic 3965 (Persian, 1800), Delhi Persian 853
  (1844). Pre-1500 Western hits are cryptic marginalia or notes in Latin/English books (Cotton Titus D XXVI-XXVII, Add MS 29250
  Chaucer Astrolabe, Burney 160 and 183, Add MS 31913 and 21917, Harley 3542; Harley 2874 is already read here). Others are India Office
  cipher files, 1753-1920. No Arabic- or Hebrew-script cipher text before 1500. Caveat: a catalogue record that does not say "cipher"
  hides its cipher; the search covers 2-4 result pages per term only.
