# Arabic cipher sweep 2, part B: Egypt and Sudan, 1880-1940, Durham first (16 Nov 2026)

Run by a Claude Code session (Claude Opus 5.5) for Daniel Bourdeau. Nothing solved, merged, promoted or committed.
Rows: `candidates_B.json` (1 row, no vetting block). Scripts, downloads, contact sheets and crops stayed in the session
scratch directory (`.../scratchpad/s2B/`), not in the repository.

## Result in one paragraph

**HIL/64 and HIL/65 are now paged in full and hold no Arabic cipher or Arabic numeric code.** All 546 canvases were
looked at: the 264 six-form canvases (the part the 15 Nov wave-15 sweep only sampled) as 2 x 2 region stitches of about
2,000 px a frame, with native-resolution crops of every form that looked like cipher. The rest were looked at as whole
frames at 1,024 px. The Arabic telegrams in the two files are all in clear. The cipher that is there is English
five-letter groups in Sudan Government and Coastguard telegrams. In every case checked, the same telegram stands in
clear elsewhere in the file. Six more such pairs were found (list below). They are out of scope here, and none is bare.
The one Arabic find of this part came from the Sudan Archive catalogue: **SAD.250/1/550, a note from Gordon to the Mudir
of Dongola written mostly in two-digit Eastern Arabic numerals.** It was found among Dongola papers in 1886 and sent to
Grenfell, who said he held the key. No translation is filed with it. It is written up as a lead, without a vetting
block, because a possible contemporary translation at TNA (PRO 30/57/4/26) could not be opened.

## Routes (from this network, 16 Nov 2026)

| Source | Route | Result |
|---|---|---|
| Durham IIIF manifests | `https://iiif.durham.ac.uk/manifests/trifle/32150/<aa>/<bb>/<cc>/<ark>/manifest` | curl works. HIL/64 = ark `t2mks65hc530` (234 canvases), HIL/65 = `t1mh128nf091` (312) |
| Durham IIIF collection tree | `https://iiif.durham.ac.uk/manifests/trifle/collection/32150/t1crx913p91b` (Abbas Hilmi II files; 28 sub-collections) | works; 412 digitised HIL manifests listed by label (`bin/tree.py` in scratch) |
| Durham image server | `<service>/full/1024,/0/default.jpg`; regions `<service>/x,y,w,h/<px>,/0/default.jpg` | **every answer is capped at 1,024 px on the long side, regions included.** Native resolution comes from regions no larger than 1,024 px. A 2 x 2 grid of a six-form frame gives about 2,000 px; one form body in 2 x 2 regions comes back at 1:1 (about 1,600 px for one form). About 1,600 requests at 2.5 s, no 403 or 429 |
| Durham catalogue (XTF) | `reed.dur.ac.uk`; `n2t.durham.ac.uk/ark:/32150/<id>.xml` redirects to reed | **not used**: this session's permission layer refused requests to reed.dur.ac.uk. `collections.durham.ac.uk/schmit/ark:/32150/s18049g504c.pdf` gave 404 |
| Durham Primo (Discovery), the working catalogue route | guest token `GET https://durham.primo.exlibrisgroup.com/primaws/rest/pub/institution/44DUR_INST/guestJwt?isGuest=true&lang=en&targetUrl=x&viewId=44DUR_INST:VU1`, then `GET .../primaws/rest/pub/pnxs?q=any,contains,<term>&qInclude=facet_rtype,exact,manuscripts&scope=MyInst_and_CI&tab=Everything&vid=44DUR_INST:VU1&limit=50&offset=<n>` with `Authorization: Bearer <token>` | works (these are the calls the public search page makes; no bot check). The manuscripts facet holds the EAD records of the Sudan Archive and the Abbas Hilmi II papers, with full descriptions and the digitised-object ark (`bin/primo.py`) |
| Durham Alma OAI-PMH | `https://durham.alma.exlibrisgroup.com/view/oai/44DUR_INST/request` (reached from the manifest's `seeAlso` through palimpsest.dur.ac.uk) | works; used for single records only |
| St Antony's, Middle East Centre Archive | guide PDFs at `www.sant.ox.ac.uk/wp-content/uploads/` (main guide 2025, Egypt guide, Sudan guide) | curl works |
| Internet Archive | full text `archive.org/services/search/beta/page_production/?service_backend=fts&user_query=`; `archive.org/download/<id>/<file>_djvu.txt` | works |
| TNA Discovery | `beta.nationalarchives.gov.uk/catalogue/id/C6686738` | 403 to WebFetch; not opened |
| DECODE | `research/sweep_2026-11-11_german/decode_search.py` | works (shallow) |

## Searches and counts

**Durham Primo, manuscripts facet (whole library):** cypher 31, cipher 30, ciphered 11, cyphered 20, "in cypher" 31,
"in cipher" 30, "arabic cypher" 1, "arabic cipher" 1 (both HIL/203, Oppenheim "cypher keys"), decypher 1, decipher 9,
decyphered 2, deciphered 13, "arabic code" 5, "in code" 172, coded 145, "code telegram" 6, chiffre 0, "secret writing"
11, "secret code" 0, cryptogram 0, "cypher Mahdi" 0, "cipher Mahdi" 0, "cypher Arabic" 1, "code Arabic" 5, "cypher
Slatin" 2, "cypher Wingate" 6, "cypher Gordon" 1, "code Khedive" 2, codebook 7, "code book" 27 (235 distinct records,
all titles read; every one touching Egypt, Sudan, Arabic or a code read in full). Second pass: "Said bey Kamil" 3,
"Shafiq telegrams" 2, "telegrams Khedive" 46, "telegram arabic" 40. Third: "telegrams Hilmi" 43, "telegram Hilmi" 43,
"code Hilmi" 8, "chiffre Hilmi" 0, "chiffrés Hilmi" 0, "secret Hilmi" 8. Fourth: "Gordon code" 3, "Gordon figures" 11,
"Gordon Arabic note" 3, "Gordon message Khartoum Arabic" 2, "Mahdi cypher" 0, "Mudir Dongola Gordon" 0.

**Internet Archive full text:** "Arabic code telegram" 0; "telegram in Arabic code" 0; "in Arabic cipher" Khartoum 2
(the 1884 quill facsimile, already in part D of the 15 Nov sweep); "Arabic cypher" telegram Mahdi 25; "Arabic cipher"
Senussi 62 and "Arabic cipher" Sherif 82 (dictionaries, the "zero" sense; one hit: Kedourie, *In the Anglo-Arab
labyrinth* 1976, "a telegram in an Arabic cipher from his father [1919] ... The cipher was broken by the ...": Sharifian,
side lead); "Mudir of Dongola" Gordon cypher 217; "Mudir of Dongola" "Arabic cypher" 19; "Gordon" "Mudir of Dongola" "in
Arabic cypher" November 2; "Arabic cypher" "Mudir" "could not be deciphered" 0; "Gordon" cypher "Mustafa Yawar" 8. Gordon's
*Journals* (Hake 1885, `journalsofmajorg00gorduoft`) and FO 407/60-66 (Confidential Print, 1884-85) downloaded as text and
grepped.

**DECODE:** Durham 1 (BL Egerton, unrelated), "Abbas Hilmi" 0, Sudan 0, Egypt 0, Khedive 0, Mahdi 0, Wingate 0, Slatin 0,
Cairo 0, Khartoum 0, Arabic 0, telegram 5 (Naples, unrelated), Gordon 0, Dongola 0, "Durham University" 0, "Sudan
Archive" 0.

**MEC guides (St Antony's):** cipher, cypher, ciphered, "in code", "code book", codebook, decipher, decypher: 0 in each of
the main guide (33,477 words), the Egypt guide (7,245) and the Sudan guide (1,397). "secret" 14 / 0 / 4, none about cipher.

**Web searches (5):** Abbas Hilmi coded telegrams (no study found); MEC guides; Gordon / Mudir of Dongola / cipher; Tomokiyo
/ Gordon; Gordon Arabic numeral cipher / Grenfell / Durham. None names SAD.250/1/550 or a decipherment of it.

## Durham HIL/64 and HIL/65: what was paged

| File | Canvases | Forms | How |
|---|---|---|---|
| HIL/64 | 0-135 (HIL/64/1-816), six forms each (two at 2 forms) | about 800 | every canvas as a 2 x 2 region stitch (about 2,000 px), read in 4-up sheets; suspect forms cropped at 0.44-1.0 of native |
| HIL/64 | 136-233 (HIL/64/817-1011), two forms each | about 195 | every canvas at 1,024 px, 16-up re-screen (wave 15 had read the message areas); 232-233 for the first time |
| HIL/65 | 25-152 (HIL/65/51-810), six forms each | about 760 | as HIL/64 0-135 |
| HIL/65 | 0-24, 153-311 (HIL/65/1-50, 811-1127) | about 370 | every canvas at 1,024 px; 297-311 (HIL/65/1100-1127) for the first time |

Caveat: the 1,024 px whole-frame re-screen of the two-form canvases is enough to tell numeral groups or five-letter runs
from clear handwriting. It is not a reading of every word.

**What is in them.** As wave 15 found: Egyptian State Telegraphs forms copied for the Khedive's service. They carry
English traffic of the Sudan Government and its Cairo agency, the Coastguard ("Sawahil") and the frontier posts,
1907-1914. Mixed in are French press and diplomatic telegrams, a few Ottoman Turkish (HIL/64/700, 29 Aug 1912) and clear
Arabic telegrams. The Arabic ones seen: HIL/64 canvases 0, 2, 98 (HIL/64/593-595, al-Tur to the Interior, Dec 1911),
111-115 (Dec 1912, with numbered lists of tribal names), 135, 154-155, 172, 203-205 (HIL/64/951-956, Suez and Matruh to
the Interior and the Coastguard, Feb 1912), 232-233; HIL/65 canvases 34, 67, 79, 207, 233. All are in clear Arabic with
ordinary figures for numbers, and none has code groups. **No Arabic numeric code, no Arabic cipher.** No telegram in
these files fits the Arabic codebooks HIL/152 or HIL/154.

**English cipher in the six-form canvases (out of scope; each with its clear copy in the same file):**

| Cipher form | What | Clear copy |
|---|---|---|
| HIL/64/214 (canvas 36, form 1) | Khartoum to Mulki Cairo, no. 458, 26 Sep 1908, 129 words: clear opening, then about 44 five-letter groups | HIL/64/62 (canvas 10, form 6) |
| HIL/64/239 (canvas 40, form 2) | sheet 2 of a Governor-General's telegram, about 14 groups in English | HIL/64/118 (canvas 20, form 1) |
| HIL/64/240 (canvas 40, form 3) | Khartoum to Bernard, "Your 2308 & 2309 and 2310", about 25 groups | HIL/64/119 (canvas 20, form 2) |
| HIL/64/402 (canvas 68, form 2) | Khartoum to Stack, no. 1656, 3 Jan 1909: "... with regard to VB u xp. cupum xpfub xpgnw spcov and suspend action" | HIL/64/403 (same frame): "... with regard to Muralia Ibrahim Ragis wall ..." |
| HIL/64/758-761 (canvas 126) | Ferasudan Cairo to Port Sudan, no. 1295, 19 Nov 1912, 139 words in 3 sheets, about 80 groups (Bank of Abyssinia) | HIL/64/764-766 (canvas 127) |
| HIL/65/~142 (canvas 41, form 2) | Khartoum to Stack, no. 168, about 10 groups | canvas 42, form 1 |
| HIL/65/~273 (canvas 62, form 2) | Baqbaq to Sawahil, June 1913, about 6 groups | not looked for |

These add to the two pairs wave 15 recorded (HIL/65/157-160, 148/153). They are key-recovery material for the Sudan
Government's English cipher of 1908-1913. The candidate rows of wave 15 should say that HIL/64/1-816 is now screened:
HIL/64/890-891 has no clear copy in HIL/64/1-816 that turned up in this screening, but the screening was not a collation.
Handling notes ("Decypher following telegram", "decypher yourself", "am not in possession of your Cypher", "my arabic
no 176") occur in clear. Dictionary code words (Aglossa, Alantapfel, Flaccidity, Afocherde ...) recur in HIL/64 as well
as HIL/65.

## Finds

1. **SAD.250/1/550 (Wingate papers): Gordon to Mustafa Pasha Yawar, Mudir of Dongola, Arabic note mostly in two-digit
   numerals, dated 16 M[uharram] 1302 [about 5 Nov 1884].** Seen on the image: canvas 35 of 96 of SAD.250/1/528-606,
   native size 2,107 x 3,264 px, read as two region crops at 0.97 of native. Address in clear, then 15 lines of about 8
   Eastern Arabic two-digit numbers each (about 120 numerals), with Arabic words in clear among them. Then 3 lines mostly
   in clear, the date, and the signature "Ghurdun" with "bi-khatmihi". The covering letter SAD.250/1/549 (Palmer to
   Grenfell, 15 Nov 1886) says a scrap "containing figures signed by Gordon" was found in papers from Dongola, and that
   "The figures are in Arabic". Grenfell answers on 549v: "I have the key ... I will translate & send back to you". No
   translation is filed with it (folios 543-548 and 551-556 viewed at 500 px). `known.py` ("SAD.250", "Mudir of
   Dongola", "Yawar", "Gordon") finds only the catalogue line in the 15 Nov sweep's parts C and D and unrelated Gordon
   rows. It is not in `leads.json` or `catalogue.json`, and not on DECODE. Gordon's *Journals* print two other notes
   from Gordon to the Mudir of Dongola (15 Shawwal 1301, 7 Dhu'l-hijja 1301), both in clear. The Confidential Print (FO
   407/62-63) records "Arabic cypher" letters from Gordon arriving at Dongola and Debba in Nov 1884 and translations of
   some. A note to the Mudir of 16 Muharram was not found in the OCR text. TNA PRO 30/57/4/26 (Kitchener papers) is
   catalogued, by a web search summary, as a "translation from Arabic script cipher respecting repayment of a loan" (see
   also PRO 30/57/3/11). It was not opened, and it could be this note's decode or a sibling's. **No vetting block**
   because of that open question and because FO 407/63 was only grepped, not read. cls B (key said to exist in 1886;
   clear words in the text).

## Closed (looked at, not leads)

- **HIL/64 and HIL/65** in full, as above: no Arabic cipher. English cipher pairs all have clear copies.
- **HIL/203/291-298** (Said Kamil, Oppenheim correspondence "with formula and ?sample of synthetic ink and cypher keys"):
  canvases 249-254 at 1,024 px. Folder cover "Correspondance avec Baron Oppenheim a Constantinople avril et mai 1915",
  a list in Arabic, the typed German "Synthetische Tinte" formula (203/294), the French "Formule encre synthetique"
  (203/295), Pera Palace and visiting cards. No cipher table or key was seen on these canvases.
- **HIL/166/212-276** (Ahmad Shafiq, including the "series of telegrams in Arabic during 1908-1909", HIL/166/235-239):
  canvases 112-143 at 1,024 px, 16-up. Clear Arabic letters and telegram copies, with French translations of letters
  from the Melkite patriarch. No numeral groups at this size. The rest of HIL/166 (516 canvases) was not paged; 149
  were downloaded.
- **SAD.916/15-16** (Gordon's scrap smuggled in a young man's hair, 1884): catalogue describes clear Arabic with a
  contemporary translation and a 2006 translation. Not cipher.
- **SAD.101/19** (Sharif Husayn, Abdallah, Sayyid Ali: Arabic telegrams to Wingate, 1916): catalogued as Arabic telegrams,
  not as cipher; not digitised (no ark in the Primo records). Not opened.
- **SAD.451/124/73** (Slatin papers, "cipher amendments", 1909), **SAD.208/2/11-13** (Owen, "ordinary word letter cypher"),
  **SAD.246/7/54**, **SAD.694/1/21-22**, **SAD.141/3-4**, **SAD.138/10, 12** (Arab Bureau on Sharif-Faruqi coded
  messages, English): English, catalogue only.
- **SAD.252/1/936** "Translation of a telegram in Arabic, said to be a copy of one written by Gordon on 29 December
  1884": a translation only, not cipher.
- **HIL/248/18** (Homer to Azmi "on the importance of secrecy and of using code", 1931-33): catalogue only; English.

## Key leads (keys with no ciphertext)

| Item | Seen | What |
|---|---|---|
| Durham HIL/153/1-19, "Dalaman to Europe, Europe to Dalaman" | canvas 3 of 10 (HIL/153/6-7) at 1,024 px of 3,879 | pocket notebook: "Conventions" (French cover phrases, numbered: "Avons 25 sacs pommes", "Cabby nouvelles santé", "lettre suit", "santé bonne" ...) against "Signification" in Arabic (government troops, the inspection, the mudir). A jargon (open) code for the Khedive's Dalaman estate: French cover text, Arabic meaning |
| Durham HIL/155/1-101, code book for the Khedive's cabinet chief | canvas 10 of 52 (HIL/155/19-20) at 1,024 px of 6,329 | French numeric code: four-digit numbers (1701-1900 on this opening) against French words in alphabetical order |
| Durham HIL/152, HIL/154 | not reopened (see 15 Nov part D) | Arabic numeric codebooks; nothing in HIL/64-65 to try them on |
| Grenfell's key to Gordon's Arabic figure cipher (1886) | mentioned on SAD.250/1/549v | not located; would read SAD.250/1/550 |

## Side leads (one line each)

- Ottoman Turkish: HIL/64/700 (canvas 116, form 3), a clear Ottoman telegram of 29 Aug 1912. Not cipher.
- Sharifian Arabic cipher of 1919 broken by the British (Kedourie 1976, IA full text): sources for the groups not traced.
- Persian: none met.

## What is left

1. **TNA PRO 30/57/4/26 and PRO 30/57/3/11** (Kitchener papers): open them to see whether one is the translation of
   SAD.250/1/550. Then vet the row, or close it as read.
2. **FO 407/63** (Confidential Print, Nov-Dec 1884): read the "Arabic cypher" letters forwarded from Dongola page by page
   (the OCR is poor) for a translation of a note of 16 Muharram 1302 to the Mudir.
3. **Durham catalogue in XTF** (reed.dur.ac.uk) was not reachable from this session. The Primo route covers the same
   records, but finding-aid context (series headings) was not read.
4. **HIL/166** (516 canvases) beyond canvases 112-143, **HIL/23** beyond what part D screened, **HIL/51** (codes among the
   loose papers; manifest fetched, not paged), **HIL/248**: not paged.
5. **Sudan Archive Arabic files** (SAD.101/19 and the Mahdist Arabic collections) are mostly not digitised; ask Durham for
   scans if a cipher is suspected. The Sudan Archive's other digitised Gordon papers were not searched frame by frame.
6. Sudan Memory, EAP, QDL: not retried here (blocked in the 15 Nov sweep; no Chrome in this session).
