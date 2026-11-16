# Wave 18 (16 Nov 2026): Durham, Abbas Hilmi II papers beyond HIL/64-65

Continues `research/sweep_2026-11-15_wave16_durham/` (HIL/64 and HIL/65 screened completely) and
`research/sweep_2026-11-15_wave15_arabic2/` section 2 (routes). Script access only (Python urllib, no browser).

## Route

- Finding aid: `raw/hil.xml` (copy of wave 15's, the XTF page of `https://n2t.durham.ac.uk/ark:/32150/s18049g504c.xml`).
  `units.py` splits it into 2,485 records (series, files and single photographs) -> `raw/units.json`, `units.tsv`
  (ref, dates, title, digitised ark). 517 records carry a "Digitised material" ark.
- `man.py <tag> <ark>`: manifest at `https://iiif.durham.ac.uk/manifests/trifle/32150/<a[0:2]>/<a[2:4]>/<a[4:6]>/<ark>/manifest`
  -> `raw/man_<tag>.json`. `dl.py <tag>`: every frame at 1,024 px -> `img/<tag>/<index>_<label>.jpg`, one request a second.
- Frame index = 0-based position in the manifest.

## Progress log

- 16 Nov: finding aid parsed. **HIL/66 is not a telegram file**: it is "Vicomte R. de St. Exupery" (HIL/66/1-35,
  1906-1916, letters in French). The telegram series "Telegrams Egypt and Sudan" is HIL/64 and HIL/65 only; there is
  no third telegram volume in the list. Units picked for screening by their descriptions (see the unit table below).
- 16 Nov: **HIL/274 (Ahmad Shauqi bey, 1904-1914, "a number of coded telegrams") screened completely**: 95 frames
  (HIL/274/1-187) at 1,024 px on contact sheets of six (about 520 px a frame), one hi-res region (274/97). All clear
  Arabic: letters, the Khedivial Diwan telegram drafts (form headed "Telegrafat Diwan Khidiwi"), Egyptian State
  Telegraphs forms in clear Arabic, press summaries ("Khulasat al-jara'id al-'arabiya"), a few English letters
  (Syrian Protestant College, 1905). **No figure groups, no letter groups, no cipher.** The "coded telegrams" of the
  description are the clear Diwan telegram drafts or clear copies; a few words in brackets (e.g. 274/27, 274/159,
  274/178) look like cover names but were not read. 274/97 "(sana thalitha inkilizi)" = school year, not code.
- 16 Nov: **HIL/57 (Crowned Heads, 1903-1939, "Language: ... code") screened completely**, 73 frames (57/1-117)
  on sheets of six. One code telegram, **HIL/57/77-80** (frames 47-50), the item the "code" in the description
  refers to; everything else is clear (French, German, English, Ottoman Turkish letters and clear telegrams; e.g.
  57/90-91 is a clear Arabic-in-Latin telegram from Ali, Sultan of Zanzibar). Details below.
- 16 Nov: **HIL/248 (Homer and Blakeney, 1931-1933)** screened completely, 46 frames: typescript and clear
  telegrams; the "importance of secrecy and of using code" letter (248/18) has no code in it. Nothing.
- 16 Nov: **HIL/203/288-303** (frames 246-258; Oppenheim correspondence, Constantinople April-May 1915) looked at:
  synthetic-ink formula (203/294-295, German and French), cover addresses (203/301), and **two cipher keys
  (203/299, 203/300)**, see key material below. The rest of HIL/203 (504 frames) was not screened.
- 16 Nov: **Codebooks HIL/150-155** (HIL/149 is not digitised): manifests fetched, HIL/151, 153, 155 downloaded in
  full and sampled; HIL/150, 152, 154 sampled (frames 1-2). See key material.
- 16 Nov: **HIL/51 (Loose papers, "codes")** screened completely, 86 frames: the "codes" are drafts of three open
  codes (51/108-125), see key material. No cipher text.
- 16 Nov: **HIL/202/1-93** (frames 0-46; "secret reports with Egypt", Vienna-Constantinople-Alexandria plan,
  1915-1916) screened: clear French and Arabic/Ottoman drafts and clear telegrams (Arif Pasha, Enver Pasha, Lucerne
  1915). The French plan "Organisation des rapports secrets avec l'Egypte" (202/13-31) prescribes a "code chiffré"
  and a "code conventionnel" for the Vienna-Constantinople-Alexandria link and how to get the code into Egypt
  (202/23-24): background for HIL/149-155 and HIL/51/108-125. No cipher text in these frames.

## Units of the finding aid (relevant ones; the full list is `units.tsv`)

2,485 records, 517 with a digitised ark. Units whose description points at code, cipher, telegrams or secret work:

| Unit | Title, dates | Digitised (ark, frames) | Screened here |
|---|---|---|---|
| HIL/64/1-1011 | Telegrams Egypt and Sudan I, 1907-1912 | t2mks65hc530, 234 | waves 15-16, complete |
| HIL/65/1-1127 | Telegrams Egypt and Sudan II, 1913-1914 | t1mh128nf091, 312 | waves 15-16, complete |
| HIL/66/1-35 | Vicomte R. de St. Exupery, 1906-1916 (letters, French) | t1mbn999718g | no (not telegrams) |
| HIL/274/1-187 | Ahmad Shauqi bey, 1904-1914, "a number of coded telegrams" | t2mf7623d13k, 95 | complete: no cipher |
| HIL/57/1-117 | Crowned Heads, 1903-1939, language "code" | t2m3f462569b, 73 | complete: 57/77-80 code telegram |
| HIL/248/1-79 | Dr Homer and Gen. Blakeney, 1931-1933 ("using code", 248/18) | t1mdn39x2118, 46 | complete: no cipher |
| HIL/51/1-126 | Loose papers, 1901-1943, "codes" | t2m5q47rp08z, 86 | complete: open-code drafts |
| HIL/202/1-543 | Dr Said Bey Kamil I, 1914-1921, secret reports | t2m4j03d016s, 315 | 202/1-93 only |
| HIL/203/1-574 | Dr Said bey Kamil II, 1914-1918, "cypher keys" 203/293-7 | t1mmw22v601r, 504 | 203/288-303 only |
| HIL/149/1-41 | Codebook 1914 (M.B.F., A.B.Ch., M.P.M.) | **not digitised** | - |
| HIL/150/1-82 | Turkish code book no. 75, printed Istanbul 1327-29 AH (c. 1910) | t2mjq085k39p, 43 | sampled |
| HIL/151/1-23 | Code for despatches of Shafiq Pasha | t1m9z9030418, 12 | complete |
| HIL/152/1-154 | 2 identical Arabic codebooks, numbered | t1m7s75dc88v, 78 | sampled |
| HIL/153/1-19 | Code Dalaman-Europe | t1m1r66j1741, 10 | complete |
| HIL/154/1-131 | Codebook of Izzat Pasha (Arabic, numbered) | t1mfq977v36q, 66 | sampled |
| HIL/155/1-101 | MS code-number book, "Chef du Cabinet de S.A. le Khédive" | t2m7w62f8727, 52 | all frames fetched, 6 pages read |
| HIL/49, 88, 45, 47, 78, 25, 1, 2, 4, 7, 10, 12, 24 ... | descriptions say "secret" / "intelligence" (reports) | yes | no |
| HIL/94, 103, 166, 195, 216, 230, 243, 279, 355, 351 ... | contain telegrams (no code mentioned) | yes | no |

## Bare code telegram (candidates.json)

**HIL/57/77-80** (man_hil57 frames 50, 49, 48, 47 = sheets I-IV; manifest
`https://iiif.durham.ac.uk/manifests/trifle/32150/t2/m3/f4/t2m3f462569b/manifest`). Received telegram on Austrian
form D.S. Nr. 759 (1/1910), typed tape strips: "D = SON ALTESSE KHEDIVE HOTEL IMPERIAL WIEN / SSS DDD PARIS
27597-153-14/10-18 =", then 143 four-figure groups, then clear "HOMMAGES DEVOUES = FOUAD =". Sheets II-IV are marked
in pencil "II/III/IV Blatt ad Nr 27597", sheet I "4 Blätter". Received stamp on each sheet: "P No 27 / 14 OCT 12 /
TEUFELBERGER" (stamp year read "12"; by the form's own legend the preamble gives office, number, word count,
day/month and hour, so "18" is the filing hour). **Date: 14 October, probably 1912** (stamp), filed Paris,
received Vienna. Word count 153 = 143 groups + address + 3 clear words, so the groups look complete.
Sender "Fouad": not identified (Prince Ahmad Fuad, the later king, is one possibility; "Kerim Fouad" is in the
name list of the open-code drafts HIL/51/122; neither checked).
Groups, read once from ~1,200 px regions, uncollated (also `raw/hil57_77-80_groups.txt`):

```
I   1932 4416 7706 1600 4101 0023 9252 8819 0124 / 5732 3063 1551 6555 7770 5737 6651 2132 4094 /
    3645 6699 9946 2424 0560 0191 4270 7568 9980 / 8262 6716 4093 5047 6633 0558 8723 8256 6350
II  3668 5737 6502 6892 4689 1366 0679 5869 8723 5737 / 1837 9320 0246 0560 4308 1316 3284 5731 4063 /
    1337 3645 4241 7662 4574 5732 6626 0679 7763 9756 / 6870 9403 8774 7568 7640 9980 0560 8494 9138
III 4982 3918 2424 5433 5416 1238 4094 3063 7771 / 5705 1316 3645 9225 5046 6626 1337 5879 /
    9943 7771 5705 0560 2474 9680 9014 1300 8293 / 9207 5083 2713 7596 5202 3063 0560 1316 0173
IV  9664 0818 5731 3063 9958 3645 5046 3391 3710 / 3095 9454 6863 0842 3063 6553 7710 0131 1655 /
    5532 7887 9276 1768 7706 3004 9276 2647 1308 / 0818 3661 5872 1366 3668 4274 6431  HOMMAGES DEVOUES = FOUAD
```

Repeats: 3063 x5, 0560 x5, 3645 x4, 5737 x3, 1316 x3, eighteen other groups twice. **Test against HIL/155
(direct lookup, no additive):** 0560 = "Arrivé", 3063 = "S'être entendu", 3645 = "Flatter"(?), 1316 =
"Cessionnaire", 5737 = "Motiver/Motivez", 0023 = "Vivre dans l'abondance": not a text, so the telegram is not
plain HIL/155 (another book, or HIL/155 with an additive or shift; not tried). HIL/150, 152 and 154 were not
tried. No clear copy or decode in HIL/57; the rest of the collection was not searched for one.

## Key material (not candidates)

- **HIL/203/300** (frame 255; file "II Correspondance avec Baron Oppenheim à Constantinople, avril et mai 1915"):
  Arabic letter-to-number substitution, 28 letters, odd numbers rising then even numbers falling: alif 11, ba 13,
  ta 15, tha 17, jim 19, ha 21, kha 23, dal 25, dhal 27, ra 29, zay 31, sin 33, shin 35, sad 37; dad 38, ta' 36,
  za' 34, ayn 32, ghayn 30, fa 28, qaf 26, kaf 24, lam 22, mim 20, nun 18, ha' 16, waw 14, ya 12. Worked examples
  beneath: "irsil lana jawab halan ..." = 11 29 33 22 - 22 18 11 - ... and "arsalna al-yawm 875 banadiq wa 12183
  khartusha" (875 rifles and 12,183 cartridges), numbers left in clear in brackets. Read from ~1,000 px regions;
  collate before use.
- **HIL/203/299** (same frame, slip above): Arabic letters to Latin letters, reversed alphabet (ba m, ta l, tha k,
  jim j, ha i, kha h, dal g, dhal f, ra e, zay d, sin c ...; second row runs on to z), example "rkg = xim" and
  letters under "irsil lana jawab halan". Read in part only.
- **HIL/203/301**: typescript "Deckadressen für Schafik Pascha" (cover addresses, Athens and Switzerland);
  203/294-295 synthetic (secret) ink formula, German and French.
- **HIL/155**: manuscript one-part French code, 0001 "A (lettre)" to about 9999, 100 numbers a page (page p holds
  (p-2)x100+1 ... ), label "... Pacha, Chef du Cabinet de S.A. le Khédive" (name not read). Words, phrases,
  syllables "(syll.)" and names. It does not decode 57/77-80 directly (above).
- **HIL/152, HIL/154**: Arabic one-part numbered codes (four figures; 152 begins 0001, 154 about 1111), with name and
  verb-tense sections (per the catalogue). **HIL/150**: printed Ottoman code book no. 75. Not read.
- **HIL/151**: "Code conventionnel pour les dépêches de et pour S.E. Chafik Pacha": numbered open-code phrases
  ("arrivé bonne santé", "Mohamed bien portant" ...) for the Prince's démarches with the King of Italy, the Duke of
  the Abruzzi etc., and for "Moheb" (Naples, Constantinople), with cover addresses (Mme Chafik, Izzeddine, Saddik).
  About 1914-1915.
- **HIL/153**: "Code conventionnel", part I Dalaman to Europe via Rhodes, part II Europe to Dalaman: French innocent
  phrases ("Reçu argent", "avons dix sacs pommes") = Arabic meanings. Open code.
- **HIL/51/108-125**: "Codes conventionnels - brouillons": drafts of the open codes for M.P.M., M.B.F. and A.B.Ch.
  (the drafts of the undigitised HIL/149); a "table chiffrée" of names (51/121) and a name list (51/122: Mohammed
  Fahmy, Midhat Faik, Kerim Fouad, Ahmed Chouckri). Open code.

No telegram in an open code (HIL/151, 153, 51) was recognised in the screened files; such telegrams read as clear
French and would not stand out on a contact sheet.

## Other Durham collections (catalogue search, script access)

Route: `search.py <keyword> ...` runs the XTF keyword search of `https://reed.dur.ac.uk/xtf/search?keyword=...` (all
result pages, one request a second; XTF stems, so "cipher" also finds "ciphers") and pulls the hit passages out of
each EAD finding aid -> `raw/search_<kw>.json`, log `raw/search_log.txt`. Keywords run: cipher, cypher, decipher,
decypher, cryptogram, codebook, "code book", "code telegram" (no hits), "in code", chiffre. Digitisation was checked by
the "Digitised material" ark links in each finding aid (`raw/ead_<name>.html`).

| Collection, item | What the catalogue says | Digitised | Status |
|---|---|---|---|
| Wingate, SAD.250/1/81 (Nile Campaign 1884-85) | "Table of cypher codes for senior army personnel" | yes, ark t1m6969z078q frame 34 | **looked at: key material** - letter-substitution alphabets in columns for named officers (Kitchener, Chermside, Rundle, Wortley ...) with number and Arabic-letter columns; 250/1/81v endorsed "Cyphers". Not read in detail. |
| Wingate, SAD.255/1/328-329 (1893) | "translation of a cypher telegram" Governor of Tripoli to Grand Vizier | yes, ark t1mgb19f592s frames 41-43 | looked at: Clare Ford (Constantinople) to Rosebery, 20 May 1893, with an English translation only; no cipher text |
| Wingate, SAD.246/7/54 (Nov 1883) | "Cypher telegram to London reporting the Hicks disaster" | SAD.246/7 not in the digitised list (246/9 is) | not seen |
| Wingate, SAD.141/3-4 (1916-17), SAD.223/2/1 (1915) | Hejaz cyphers discovered; cypher officer at Jiddah; Slatin's cypher books | not checked item by item | not seen |
| Hicks Pasha, SAD.866/5/1-46 and SAD.600/2/1-35 (1883) | registers of telegrams, "Language: English, Arabic and cypher" | no digitised links in the Hicks finding aid | **lead, not online** (not in candidates.json: not seen) |
| Slatin, SAD.451/124/73 (3 May 1909) | letter on "cipher amendments" | not checked | not seen |
| Leach, SAD.208/2/11-13 | Owen memo on "the ordinary word letter cypher" (Sudan) | only SAD.208/9/1 digitised | not seen |
| Clayton, SAD.694/1/21-22 (1920) | copy of cypher telegram (FO to Samuel) - a clear copy | not checked | not seen |
| Hill, SAD.969/15/86-87 (1937) | Sudan Railway Telegraphic Code Book | not checked | not seen |
| Elliott MS 9 (17 Mar 1547) | Francis I to Christophe Richer, in cipher, **with a modern decipherment by Pierre Bougé** | no | known reading; key material, not a lead |
| Elliott MS 10 (19 Sep 1646) | Mazarin to Henri Arnauld, number cipher **with the decipherment written in** | no | key material, not a lead |
| Ponsonby papers GRE/E481, GRE/E144 (1830, 1838) | Palmerston's instructions for ciphers; Colquhoun's "explanation and key to the cipher" | no | key material |
| 4th Earl Grey papers GRE/B181/5 (June 1896) | "6 coded telegrams ... decipher of 5 telegrams including 3 of the above" (Jameson raid) - so some coded telegrams may lack a decipher; also cipher/decipher pairs 1892-1913 | no digitised links | lead, not online |
| Wylde, WYL/76/1 (1877) | Gordon at Khartoum recommends a cipher to the F.O. | not checked | not seen |
| Cosin MS V.v.13 | fragment "in simple cipher: substitution of subsequent letters for vowels" (16th c. pen trial) | not checked | trivial, not seen |
| Sudan Archive personal papers (Aglen, Wood, Dingwall, Piper, Kenrick, Foley, Fouracres, Hebbert) | mention work as cypher clerks or officers, 1918-1953 | - | no cipher texts described |

"chiffre" returned no hits. The "in code" run was stopped part-way (it returns mostly Durham University Journal
volumes and unrelated finding aids); its partial log is in `raw/search_log.txt`.

## What was not looked at

- HIL/202/94-543 (frames 47-314) and HIL/203 apart from 288-303: WWI Khedivial secret-service files, the most
  likely place for further cipher or open-code telegrams (Arabic numeral code per HIL/203/300; open codes per
  HIL/151, 153, 51). Not screened.
- The HIL files described as "secret" or "intelligence" reports (HIL/49, 88, 45, 47, 78, 24, 25, 120 ...) and the
  other telegram-bearing files (HIL/10, 94, 103, 166, 195, 216, 230, 243, 279, 351, 355 ...). Not screened.
- HIL/150, 152, 154 beyond two frames each; HIL/155 beyond six pages. No attempt to decode 57/77-80 with them
  beyond the direct HIL/155 lookup.
- Sudan Archive items not digitised (Hicks telegram registers SAD.866/5, SAD.600/2; Wingate SAD.246/7/54) and the
  Wingate items not checked one by one (SAD.141/3-4, 223/2/1).
- Open-code telegrams in clear French or Arabic: they cannot be told from clear text on a contact sheet.

## Files

`units.py`, `man.py`, `dl.py`, `sheet.py`, `region.py`, `search.py` (scripts); `units.tsv`; `candidates.json`
(one row: HIL/57/77-80); `raw/` (finding aid, manifests, search results, `hil57_77-80_groups.txt`); `img/` (frames,
contact sheets `img/sheets/`, regions `img/v/`). `raw/` and `img/` are git-ignored.
