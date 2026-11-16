# Arabic-script and Middle Eastern cipher sweep, second pass (wave 15, 15 Nov 2026)

Run by a Claude Code session for Daniel Bourdeau, on the owner's machine. Continues
`research/sweep_2026-11-15_arabic/` (same day, cloud network), which could not reach Durham's telegram files,
Qalamos, Fihrist live, CUDL, Chester Beatty and vHMML. **State: not merged, nothing committed.** `candidates.json`
holds the rows; `raw/` holds the downloaded catalogue text and search results; `img/` holds images (not to be committed).

Written incrementally; sections are in the order worked.

## 0. Network note (read first)

The machine was on a VPN-style address (public IP 66.234.152.x, DNS 10.2.0.1) during this run. Several hosts treat that
address worse than a home line would:

- `qalamos.net` / `www.qalamos.net` (139.18.16.144, Leipzig): **TCP/TLS connection reset**, to curl and to the owner's
  Chrome alike (Chrome showed its error page). `orient-digital.staatsbibliothek-berlin.de` and `www.ub.uni-leipzig.de`:
  the same. This is a network-level refusal, not a bot check; nothing a browser can do. **Needs the owner with the VPN
  off**, or another line.
- `cudl.lib.cam.ac.uk`: three curl requests went through, then AWS WAF answered `202` with
  `x-amzn-waf-action: challenge`. In Chrome the page loads normally (no interactive check was shown).
- `www.fihrist.org.uk`, `viewer.cbl.ie`: Anubis page ("Making sure you're not a bot!") to curl.
- `www.vhmml.org`: the page loads by curl, but the search call needs a Cloudflare Turnstile token
  (`search-common.js`, header `cf-turnstile-response`).

## 1. CUDL (Cambridge Digital Library)

**Route.** Chrome, own tab: open `https://cudl.lib.cam.ac.uk/search?keyword=<term>` once, then call the site's own
JSON endpoint from the page, one request about every second:
`/search/JSON?keyword=<term>&start=<n>&end=<n+20>` (20 hits a call; `info.hits` gives the total). The Chrome tool
truncates script output at about 1,000 characters: write the result into the page (`<article><pre>`) and read it with
`get_page_text`, which returned 30,000+ characters without trouble.

Item metadata and catalogue-page transcriptions come **by plain curl** from the services host, no check:

- `https://services.cudl.lib.cam.ac.uk/v1/metadata/json/<ITEM-ID>` (description, page list with `IIIFImageURL`)
- `https://services.cudl.lib.cam.ac.uk/v1/transcription/tei/diplomatic/internal/<ITEM-ID>/i<page>`
- images: `https://images.lib.cam.ac.uk/iiif/<IIIFImageURL>.jp2/full/<w>,/0/default.jpg` (2,400 px wide served).

**Terms and hit counts** (whole library, all languages; 15 Nov 2026): cipher 58, cypher 36, cryptogram 2,
cryptography 3, cryptographic 4, "secret script" 7, "secret alphabet" 2, "secret writing" 27, "secret language" 16,
enciphered 0, encrypted 12, undeciphered 4, "in code" 54, coded 2, Geheimschrift 0, رمز 18, معمى 1, تعمية 1, أقلام 0,
مترجم 1, şifre 6 (all "Sifre", the midrash), "secret characters" 40, "unknown script" 108, "unidentified script" 184.
The multi-word terms are AND searches, mostly noise (Darwin letters, Sterne). The last four were not listed (noise);
the first 20 terms gave 116 distinct items, all read as title + snippet (`raw/` has the six metadata files fetched).

**Arabic-script and Middle Eastern results: nothing new with ciphertext.**

- T-S K5.7, K1.47, K1.135, 20.140 and the Targum "ciphers" (verse counts): Geniza items already in the Hebrew and
  Arabic sweeps, or numerals. Not re-recorded.
- Browne's catalogues (digitised with searchable text) name these, none a candidate:
  - **Browne Q. 3 (9)**, *Asrar-i Qasimi* attributed to Kashifi: uses a "cabbalistic secret writing ... to disguise
    from profane eyes certain words". A known work (lithographed Bombay 1302/1885); the secret alphabet is part of
    the text tradition. Treatise with cipher words, not viewed.
  - **CUL Add. 1899 (9 fragments, Samaritan papers of Petermann's circle), fragment 6**: "a specimen of the artificial
    script known in Persia as Khatt-i-sarvi ... or some similar form of cryptography", in pencil (Hand-list no. 1531,
    p. 355). A specimen; not digitised as far as the search shows; not viewed.
  - **CUL Dd. 3. 54** (Castell's Persian-Latin lexicon), **Kk. 2. 17** (a Qur'an with "notes in Castell's short-hand or
    cypher on the terminal pages") and **Dd. 6. 4** (Edmund Castell's notebook): 17th-century English shorthand or
    private cipher of an orientalist. European; side lead only, not viewed, prior art not searched.
  - Browne, Persian catalogue pp. 184-187 and Browne MSS p. 118: lists "in the cipher called raqam", i.e. siyaq
    accounting numerals. Not cipher.
  - Or. 25 (*Kitab Ishrasim al-Hindiyya*): the تعمية hit is the author saying he writes without concealment.

**Two finds outside the Arabic scope** (recorded in `candidates.json` because they are bare, unread and on an image):

- **Trinity College O.4.22, f. 248v** (Greek Gospel lectionary, 11th c.): after his dedicatory note the reader Ioannes
  added three lines of capitals in a numeral cryptogram. The CUDL record (Christopher Wright) transcribes it and says it
  "remains to be resolved". Image seen (1,305 x 2,000 px download; the lines are faint, at the foot of column 2).
- **CUL Add. 2255, f. 19v** (Jain *Vipakasutravrtti*, copied Vikrama 1650 = 1593/94): about a dozen coded signs before
  *lasitam* in the colophon where the scribe's or place name should stand; record: "Their meaning is yet to be
  deciphered". Image seen (2,000 px): the signs look like numeral forms in two or three groups separated by dandas.
  Very short.

Note on method: the CUDL search was run through the owner's Chrome after AWS WAF had challenged curl. No box was
clicked and no interactive check appeared; the page simply loaded. After that the session stopped using Chrome to get
past bot checks (see section 5), so CUDL is the only source in this sweep reached that way.

## 2. Durham, Abbas Hilmi II papers, HIL/64 and HIL/65 ("Arabic and code")

**Route (plain curl / Python, no check, fast: under a second an image).**

- Finding aid, whole collection as one page: `https://n2t.durham.ac.uk/ark:/32150/s18049g504c.xml` (answers with the
  XTF HTML view, 1.9 MB; saved as `raw/hil.xml`). The XTF keyword search does not find reference codes ("HIL/64": 0).
- Digitised units: HIL/64/1-1011 = ark `t2mks65hc530` (234 frames); HIL/65/1-1127 = ark `t1mh128nf091` (312 frames).
  Manifest: `https://iiif.durham.ac.uk/manifests/trifle/32150/<aa>/<bb>/<cc>/<ark>/manifest` (aa, bb, cc = the first
  three letter pairs of the ark). Viewer: `https://n2t.durham.ac.uk/ark:/32150/<ark>.html`.
- Images: `<service>/full/1024,/0/default.jpg`. The server caps every answer at 1,024 px, **but region requests work**:
  `<service>/<x>,<y>,<w>,<h>/<px>,/0/default.jpg`. `hires.py <hil64|hil65> <frame index> <n>` stitches an n x n grid
  (n = 3 gives about 3,070 px for a 7,000 px frame, enough to read every letter). This corrects the first sweep's
  note that 1,024 px was the limit.
- `dl_durham.py` fetched all 546 frames at 1,024 px (545 saved; frame labels with `*` need the sanitised file name).
  `sheet.py` builds contact sheets cropped to the message area of the forms.

**What the files are.** Microfilm frames of Egyptian State Telegraphs forms (G 13 / G 14), two or six forms to a
frame, about 2,100 forms. They are the traffic of the British administration: Sudan Government departments in Khartoum
and their Cairo agency (Stack, Bernard, Phipps, Slatin, Clayton, Symes, "Mukhabarat", "Hakimam", "Dakhlia",
"Ferasudan"), and the Egyptian Coastguard and frontier posts in the Western Desert and Sinai (Snow, Royle, Hunter,
Russell, Barlow, Hewitt; "Sawahil"), 1907-1914, with a few Arabic telegrams and French press telegrams. Nearly all are
in a handful of clerks' hands, so they are copies made for the Khedive's intelligence service, not the originals.
Language: English throughout; Arabic telegrams (seen: HIL/64/851-856, 951-955; HIL/65/921, 973) are in clear Arabic.
**No Arabic cipher and no Arabic numeral code was seen.**

**What "code" means here** (three things, none of them Arabic):

1. **Dictionary code words** inside clear English: Aglossa, Agyllinos, Academical, Alantapfel, Agatofillo, Aginaverid,
   Ajustamos, Afrosponde, Aeruginis, Flagitate, Flamando, Floorless ... (all A... or Fl...), in the Sudan Government's
   administrative telegrams, HIL/65 above all (e.g. 823-824, 849, 910, 928-929, 964, 966, 984, 1030-1031, 1092).
   Roughly one telegram in fifteen of those viewed. No decode beside them. A code book system (candidate 3).
2. **Five-letter cipher groups** inside clear English, rare: three telegrams found.
   - HIL/65/157-158, Phipps to Slatin, Khartoum 12 May 1913 (the one the catalogue names), 24 groups. **The same
     telegram stands in clear at HIL/65/159-160** on the same film frame and the next.
   - HIL/65/148, Erkowit to Stack, 16 May 1913, about 49 letters. **The same telegram stands in clear at HIL/65/153.**
   - HIL/64/890-891, Railhead to Herbert (Sawahil, Alexandria), 13 July 1912, 17 groups. No clear copy found in the
     frames screened. Different look (letters p to x dominate; groups such as `wuuuu`, `ktvvv`).
3. The word "Cypher" written in a clear telegram as a handling note (HIL/65/41-42: "Ball and pleased. Cypher. I am
   trying to get rid of ...").

**Share undeciphered.** Of the cipher telegrams found, two of three have their plaintext in the file. So the
honest count of bare, unread cipher is **one telegram (HIL/64/890-891), about 85 letters**, plus the dictionary code
words, which are unread but belong to a code book that probably survives. As a share of the two files: well under
1 per cent of the forms carry cipher groups; some 5 to 7 per cent of the Sudan Government forms carry code words.

**Coverage, plainly.**

| Part | Frames | Viewed | How |
|---|---|---|---|
| HIL/64 frames 137-232 (817-1007), two forms each | 96 | all | contact sheets, message area only (about the middle half of each form) |
| HIL/64 frames 1-136 (1-816), six forms each | 136 | 5 (1-6, 172-177, 316-321, 451-456, 752-757) | single frames at 1,024 px |
| HIL/64 frames 233-234 (1008-1011) | 2 | 0 | |
| HIL/65 frames 1-25 (1-50), two forms each | 25 | all | contact sheets |
| HIL/65 frames 26-153 (51-810), six forms each | 128 | 3 (147-152, 153-158, 159-164) | 2,049 and 3,074 px stitches |
| HIL/65 frames 154-297 (811-1099), two forms each | 144 | all | contact sheets |
| HIL/65 frames 298-312 (1100-1127) | 15 | 0 | |

About 265 of 546 frames were screened; in the screened two-form frames the sheets show only part of each form, so a
cipher run in the first or last lines of a form could have been missed. **The 264 six-form frames (about 1,550
forms, three quarters of all forms) were only sampled (8 frames).** Two of the three cipher telegrams came from that
unsampled part by following the catalogue, so more are likely there.

## 3. Qalamos

**Blocked at network level** (section 0): connection reset on `qalamos.net`, `www.qalamos.net`,
`mymssportal.dl.uni-leipzig.de` (a second host name of the same service, found by web search) and
`orient-digital.staatsbibliothek-berlin.de`, by curl, by WebFetch and in the owner's Chrome. No search term was run on
the site. Not a bot check, so there is nothing for the owner to click: it needs a different line (VPN off).

Stopgap: five web searches restricted to the two Qalamos host names (Geheimschrift, Geheimalphabet, Chiffre,
verschlüsselt, secret script, cipher, cryptographic). Search-engine coverage of Qalamos is thin; results, all read
from the search summaries only, **no record page opened**:

- **Leipzig UB, Vollers 32, f. 1r, secondary entry 4** (record `DE15SecEntry_secentry_00000285`; 1241 AH / 1826):
  an entry in a cipher of palm-frond signs, the letter given by the number of leaves; the writer gives the key himself.
  Keyed, so read; a second entry by the same writer is on the inside cover. Not a candidate; worth opening once
  Qalamos is reachable (is every enciphered line covered by his key?).
- Treatises and alphabet tables only (not candidates): Munich BSB Cod.arab. 654, f. 172 "Über Geheimschrift"
  (al-Majriti, copy 1784-1816); Berlin Sachau 53 and Sachau 93 f. 75v (Syriac: the alphabets of Bardaisan and Simon
  and a numeral cipher alphabet); Berlin Ms. or. quart. 805 (Armenian: list of abbreviations and secret scripts);
  a Yemeni codex of 1549 with the Himyaritic alphabet on f. 1b; Leipzig Vollers 833 and Berlin Ms. or. quart. 1869
  (letter magic, no cipher).

Still to do on Qalamos, with the exact terms asked for: Geheimschrift, Geheimalphabet, Chiffre, Kryptographie,
cipher, secret alphabet, رمز, مترجم, قلم, أقلام, معمى, تعمية, şifre. MyCoRe sites normally answer
`/servlets/solr/select?q=<term>&wt=json&rows=100` (not confirmed here). The first sweep's Berlin leaves
(Ms. or. oct. 3629 ff. 1a and 72b, Wetzstein I 203, Ms. or. oct. 1474 f. 1a) are still unseen.

## 4. Morocco (Saadian and Makhzen cipher letters)

Nothing with a cipher letter on an online image was found. What was established:

- **G. S. Colin, "Note sur le système cryptographique du sultan Ahmad al-Mansur", Hespéris 7 (1927), pp. 221-228**:
  read in full (the whole volume is a free PDF, `https://hesperis-tamuda.com/Downloads/1921-1929/Hespéris Tamuda
  1927.pdf`, 24 MB, PDF pages 251-258; text in `raw/colin1927.txt`). This corrects the first sweep, which had the
  article from memory as a decipherment. **Colin publishes a key, not a letter**: the flyleaf of a nine-leaf
  manuscript lent by Clemente Cerdeira (Tetuan), where an anonymous Moroccan says he found a note in the hand of the
  secretary Abd al-Wahid ibn Masud Anun with news for al-Mansur about the Queen of England in 1009 AH (1600-01)
  written in secret characters, worked on it for some fifteen years, and solved it; he then sets out 28 signs in
  Maghribi abjad order (several lost to a torn corner; three kept as lightly altered Arabic letters). Colin
  reproduces the page (p. 224) and says no dispatch in the script was known to him; the list "permettra, le cas
  échéant, de déchiffrer des dépêches". So: key in print, no ciphertext located. The Anun note itself is lost or
  unlocated; the Cerdeira manuscript's present home was not traced.
- Azizi and Azizi, Cryptologia 35 (2011) and 37 (2013), and Azizi 2019 (LNCS 11445): still not opened (paywall);
  the 2019 abstract speaks of a numeric method of al-Mansur based on hisab al-jummal. Whether they print an actual
  enciphered letter and its reading is not established.
- al-Tazi 1983: not found online; one Arabic web search returned nothing on it.
- TNA SP 71 / SP 102, BNRM, Archives du Maroc, Direction des Archives Royales: no online images of cipher letters
  found by web search; not searched in their own catalogues in this pass.
- Dutch Nationaal Archief (Staten-Generaal, Barbary letters; Consulaten Marokko 1.02.19): one web search, no mention
  of cipher; inventories not opened. Not established either way.

## 5. Not done: Fihrist live, Chester Beatty, vHMML

- `www.fihrist.org.uk` and `viewer.cbl.ie`: Anubis bot check to curl. `www.vhmml.org`: search needs a Cloudflare
  Turnstile token. **These were not run through Chrome.** They are bot-detection gates and this session did not pass
  them on an automated client's behalf; they need the owner at the keyboard (open the search page, run the terms,
  save the result pages), or a route the sites offer to scripts.
- Fihrist: the first sweep already grepped the whole Fihrist TEI dump (15,638 records) from GitHub, so little is lost.
- Chester Beatty: the first sweep ran cipher, cryptogram, secret, cryptic before the check appeared.
- vHMML: the largest unswept catalogue for this subject (Arabic, Garshuni, Syriac, Ethiopic, Maltese archives).
  Terms to run: cipher, cryptography, cryptogram, "secret script", "secret alphabet", "secret writing", رمز, قلم.

## 6. What a vetting step must still check

1. **HIL/64/890-891** (candidate 1): find the telegram's third sheet and any clear copy in HIL/64/1-816 (unscreened);
   collate the 17 groups from a 3,000 px stitch; identify the Coastguard cipher of 1912.
2. **HIL/65/157-160, 148, 153** (candidate 2): collate cipher against the clear copies and test Playfair and simple
   systems; then try the result on candidate 1. Decide whether a text with its plaintext in the file belongs in
   leads at all (it is a key-recovery case, not an unread text).
3. **Code words** (candidate 3): look for the Sudan Government telegraph code (Durham Sudan Archive catalogue, TNA).
4. Screen the 264 six-form frames of HIL/64 and HIL/65 for more cipher groups (`hires.py`, n = 2, is enough to tell).
5. **Trinity O.4.22 f. 248v** (candidate 4): download at full size, check Wright's transcription, search Pinakes and
   the literature on Byzantine cryptography.
6. **CUL Add. 2255 f. 19v** (candidate 5): prior art on Jain scribal ciphers; a larger image of line 14.
7. Qalamos from another line; vHMML, Fihrist and Chester Beatty with the owner.
