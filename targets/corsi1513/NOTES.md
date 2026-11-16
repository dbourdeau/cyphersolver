# Giovanni Corsi to Lorenzo de' Medici, 27 Oct and 16 Nov 1513 and April 1514 (ASF, Mediceo avanti il Principato CXXXVII, docs 620, 623 and 633; catalogue 2391)

Status: doc 620 (27 Oct 1513) decoded, not read: 74.7% of letter units read as sense (strict judge, first pass of record, above our own 65% line) but only 3 of 16 sentences clean by docs/_check_reading.py, so it is filed as decoded, not read; doc 623 (16 Nov 1513) decoded, not read, 55.4% strict; doc 633 (April 1514, a copy) decoded, not read: 74.2% strict (457/616) but 1 of 13 sentences clean by docs/_check_reading.py (0.077). Contributed, not yet written up.

Status: in progress

Contributed by Malcolm McBratney (Brisbane), working with Claude (Anthropic).

Giovanni Corsi was the Florentine orator at the court of Ferdinand the Catholic [stated: the contributor]. Catalogue entry 2391 covers Corsi's cipher letters to Lorenzo de' Medici in MAP CXXXVII. This folder holds three of them. The key comes from a fourth (doc 627), which carries a decipherment written at the foot of the page at the time.

Provenance tags: [measured] = counted or hashed from the files in this folder; [derived] = worked out from them; [sourced] = from a named source; [stated] = given by the contributor, not checked here; [unverified] = a guess from context.

## The documents

| | doc 620 | doc 623 | doc 633 |
|---|---|---|---|
| Shelfmark | ASF, Mediceo avanti il Principato, filza CXXXVII, doc 620 (c. 628 bis r-v) | the same, doc 623 (c. 631 bis r-v) | the same, doc 633 (c. 641r-v; "641" with "47" struck through), a contemporary copy headed "Copia" |
| Date | 27 Oct 1513 ("die xxvij octobris 1513", verso) | 16 Nov 1513 ("xvj nobr. 1513", verso; place read "In Madrilli(?)") | April 1514 ("In Madrid ... Aprilis MDXIIIJ", foot of recto; year reading not checked) |
| Images (ASF iipsrv) | A0001329 (recto), A0001330 (verso) | A0001341 (recto, cipher), A0001342 (verso, clear only) | A0001367 (recto, cipher), A0001368 (verso, address only) |
| Cipher | 9 runs inside clear text, 20 manuscript rows, 567 tokens | 4 runs inside clear text, 16 rows, 477 tokens | 2 runs inside clear text, 12 rows, 446 tokens |
| Decipherment on the sheet | none | none | none |

[sourced: blind/BLIND_NOTES.md, blind633/BLIND_NOTES.md; token counts measured with `docs/_check_profile.py --measure <file> --drop-first`]

Image URL pattern: `https://archiviodistatofirenze.cultura.gov.it/iipsrv/iipsrv.fcgi?FIF=/data/iip-data/asfi/mediceo_avanti_principato/00100137/<ID>.ptif&WID=1272&CVT=jpeg`. Fetched 2026-11-16T01:18Z. The images are not in the repository (ASF terms); fetch them by ID. MD5 of the files used [measured]:

| ID | md5 |
|---|---|
| A0001329 | 7a1375230a85db69dcea16a09ce3e637 |
| A0001330 | 15c5ca79387f3ba6be47e86264169337 |
| A0001341 | 10cd7211e6e8c420a237291b41aa4434 |
| A0001342 | ae67b27fdfa1cc1b3c0b625a2e9fc27f |
| A0001367 | d31b0ab052de907537b2a8817b9bc506 |
| A0001368 | eabca8f32a1f25e65cda9e7241e09258 |

The first requests to the ASF server (16 Nov, 00:39-00:48Z) failed with a connection reset; the fetch at 01:18Z worked [stated]. Doc 633 was found by thumbnails (A0001343, A0001361, A0001369, A0001367) and fetched at WID=1600 at 02:28Z, one request at a time (`blind633/FETCH_LOG.txt`) [sourced].

## The system

A syllabic substitution: a consonant sign with a small odd digit above it gives consonant plus vowel (1 = a, 3 = e, 5 = i, 7 = o, 9 = u). Bare letter-like signs give single letters, with several signs for some letters. Number groups stand for doubled consonants (11 rr, 12 ss, 13 tt) and, as codes, for persons and powers (23 = S.M.ta / questo Re, 22 = Francia). Some number groups and marks are nulls. No word division. [sourced: key_corsi_w17_frozen.json]

The nearest key in this repository is pandolfini1514. It is of the same family (consonant sign plus vowel digit) but has a different table: Pandolfini 1 = u, 2 = o, 3 = i, 4 = e, 5 = a. It is not one key with Corsi's [sourced: the 16 Nov collision check].

## Method

1. **Prior art first** (10 Nov, extended 16 Nov): `PRIOR_ART.md`. See "Prior art" below.
2. **Key** (10 Nov): built from the contemporary decipherment at the foot of doc 627 (c. 635r), extended by the syllabary rule and by context in 620 (`key_corsi_10nov_frozen.json`). Wave 17 (10 Nov) added five bare signs (P, Ko, sg, bt, Ri) and two number-table entries (#1 = x, "." = null). It changed no existing value (`key_corsi_w17_frozen.json`, the key of record; its `_w17` field gives the basis of each addition). Method: **key recovered based on adjacent plaintext**, extended by context. [sourced: the key's `_note` and `_w17` fields]
3. **Freeze** (16 Nov, 00:49:07Z): both keys hashed before any new transcription (`FREEZE.txt`).
4. **Blind transcription** (16 Nov): one reader had the four images and a name-only label sheet (`blind/SHEET.md`). The sheet lists the key's sign names with no values. The reader had no key and deciphered nothing. Output: `blind/BLIND.tsv`, with `blind/BLIND_NOTES.md`. Frozen at 2026-11-16T01:34:02Z together with the key hash (`blind/FREEZE_blind.txt`). Split by letter, unchanged, into `transcription_620.txt` and `transcription_623.txt`.
5. **One decode** (16 Nov): `blind/decode_once.py` ran once with the frozen key, with no edits (`blind/decode_once.txt`). It is split by letter into `decryption_620.txt` and `decryption_623.txt`. Re-run on a copy of the frozen inputs, it gives the same file byte for byte [measured, 16 Nov].
6. **Separate strict judge** (16 Nov): another session saw only `decode_once.txt` and a brief (`blind/JUDGE_BRIEF.txt`). It made one pass with no second tries. It segmented each row and marked every letter unit S (sense), E (wrong but a plausible one-letter slip) or N (no sense). Output: `blind/judge.tsv`, `blind/JUDGE_NOTES.md`. Each segmented row put back together equals its decode row (36 of 36 rows) [measured].
7. **Reading and translation**: `reading_620.md` and `reading_623.md` are the judge's segmented text. No word was improved and nothing was emended, so there is no emendation list. Marks: `[_]` = a sign with no key value; `[?word]` = N letters; `word*` = an E word, left as decoded. Words that the judge counted across a line break are joined. `translation_620.md` and `translation_623.md` were translated from these with the same holes, by Claude, and were not checked by a person.

8. **Doc 633** (16 Nov, after 620 and 623 were judged): the same pipeline with a new blind reader (`blind633/BLIND_PROMPT.txt`, the same label sheet, no key), two images, frozen 02:34:27Z with the key hash (`blind633/FREEZE_blind.txt`). One decode by `blind633/decode_once.py`, which refuses to run on a hash mismatch or over an existing output; re-run on a copy of the frozen inputs, it gives the same file byte for byte [measured, 16 Nov]. A separate strict judge (`blind633/JUDGE_BRIEF.txt`) made one pass; each segmented row put back together equals its decode row (12 of 12) [measured]. `reading_633.md` and `translation_633.md` are made as for 620 and 623 (stan + te and al + cuna joined across line breaks; translation by Claude, not checked by a person).

## Figures (first pass of record)

From `blind/judge.tsv` (row sums re-added, 16 Nov) [measured]:

**Doc 620** (A0001329 + A0001330, 20 rows)
- S = 43+44+40+8+29+22+25+11+50+57+20+37+56+3+13+45+18+35+36+41 = 633
- E = 11+16+26+0+0+0+0+0+0+10+0+0+13+34+0+0+2+0+28+0 = 140
- N = 15+7+2+0+13+5+0+4+4+2+8+2+1+1+7+1+0+0+1+1 = 74
- Strict share = 633 / (633+140+74) = 633/847 = **74.7%**. S+E = 773/847 = 91.3%.

**Doc 623** (A0001341, 16 rows)
- S = 9+23+8+22+36+31+9+8+51+31+17+10+34+35+32+14 = 370
- E = 5+17+0+10+2+0+3+6+3+28+10+0+12+12+24+4 = 136
- N = 0+13+4+18+15+17+16+8+11+10+16+0+18+10+4+2 = 162
- Strict share = 370 / (370+136+162) = 370/668 = **55.4%**. S+E = 506/668 = 75.7%.

The units are decoded letters (a syllable sign gives two). Each bracketed code counts as 1 unit and each `_` as 1 N unit. The two letters are not pooled.

**Doc 633** (A0001367, 12 rows; `blind633/judge.tsv`, `blind633/JUDGE_NOTES.md`)
- S = 40+33+44+35+55+26+53+51+51+12+40+17 = 457
- E = 0+18+0+10+4+9+0+0+4+0+19+0 = 64
- N = 2+8+13+16+3+20+5+11+8+0+0+9 = 95
- Units = 42+59+57+61+62+55+58+62+63+12+59+26 = 616 (= 457+64+95)
- Strict share = 457/616 = **74.2%**. S+E = 521/616 = 84.6%.

Doc 620 is above our own 65% line on letter units, but the repository's sentence check (below) gives 3 of 16 clean sentences, under the 0.60 for 'read in part', so it is filed as decoded, not read. Doc 623 is under 65% and is filed as decoded, not read. Doc 633 is above 65% on letter units but the sentence check gives 1 of 13 clean sentences (0.077), so it too is filed as decoded, not read.

Token classes of the decode by letter, from `blind/decode_once.py`'s rules [measured]: 620 has 567 tokens (524 with a letter value, 23 number entries, 13 holes, 7 nulls). 623 has 477 tokens (414 letter values, 35 number entries, 16 holes, 12 nulls). 633 has 446 tokens (381 letter values, 31 number entries, 23 holes, 11 nulls; 381+31+23+11 = 446), from `blind633/decode_once.py`'s own count.

**Repository sentence check** (`docs/_check_reading.py corsi1513`, 16 Nov) [measured]: `reading_620.md` has 3 of 16 sentences clean (0.188, hole rate 0.286), and the checker's verdict is "not a reading". `reading_623.md` has 0 of 16. `reading_633.md` has 1 of 13 (0.077, hole rate 0.367); `decryption_633.txt` 0 of 11. The readings have no punctuation, so the checker cuts long runs into 12-word windows. It also counts `word*` slips and Tuscan spellings outside its word list as holes. By the checker's sentence measure, doc 620 does not reach the 0.60 that the schema gives for "read in part". The 74.7% is a letter-unit figure from the strict judge, which is a different measure. This is not resolved here (see Remaining gaps).

## Non-blind figures of 10 Nov (not the figure of record)

On 10 Nov, first readers who knew the key gave these shares (firm tokens / all tokens): 633 95.7%, 620 93.8%, 623 90.3%, 627 89.9%. They predate the freeze and are kept only as history [stated: source NOTES].

## Controls

A dictionary-cover control: `blind/shuffle.py` and `blind/shuffle_out.txt` [measured: the output file]. The score is the share of the decode covered by words of three or more letters from an Ariosto/Dante word list, with codes left out. It is computed for the real key and for 5,000 keys shuffled within each table (bare, base, vowel), at seeds 20261112 and 7.

| | real | seed 20261112 | seed 7 |
|---|---|---|---|
| 620 | 0.6902 | 0 of 5,000 as good, max 0.6021 | 0 of 5,000, max 0.5838 |
| 623 | 0.573 | 2 of 5,000 as good, max 0.6 | 3 of 5,000, max 0.581 |
| 633 | 0.6507 | 0 of 5,000 as good, max 0.5943 | 0 of 5,000, max 0.5787 |

Doc 633's figures are from `blind633/shuffle.py` and `blind633/shuffle_out.txt` (same method, its own letter labelled C).

The word list (`wordlist_ariosto_dante.txt`, sha256 b88a1894...2829, 25,566 lines) is not in this folder, so `shuffle.py` will not run here as written. Its relative path `../suardino1524/` points to the contributor's working folder. The repository's `docs/_validate.py` was not run.

## Doc 623 and Flodden [unverified]

In doc 623 the key gives code 27 as "re di Scotia?" and code 24 as "Inghilterra?". Both question marks are in the key itself. The run reads "intesa la causa morte del [27] ... movessi partiti al [24]". If 27 is the King of Scots, this would be James IV, killed at Flodden on 9 Sept 1513. A letter of 16 Nov 1513 would then report the news reaching the Spanish court. This is a guess from context only, and nothing in this folder confirms either code value. (The 16 Nov source notes placed 623 in "early 1514"; the verso reads 16 Nov 1513.)

## Prior art

`PRIOR_ART.md` (copied unchanged; carried from 10 Nov plus the 16 Nov collision check). No earlier reading of 620, 623 or 633 was found. Doc 627 was deciphered at the time, on the page. Checked: this repository (catalogue 2391 "bare", no folder, no lead, no open PR at upstream ca48c89), Desjardins, *Négociations* II pp. 591-595 (clear extracts of Corsi only) and web searches. **Prior art is not complete.** The contributor's prior-art sheet lists what is still to search:

- Google Books / HathiTrust: "Giovanni Corsi" oratore 1513 Spagna; "cavargli della mente"; "sospettosissimo" 1514 Corsi.
- MAP printed inventory vol. 4 (filza CXXXVII), for a note of decipherment.
- Spanish-side editions (CSP Spain supplement, Zurita), for the same audiences.
- DECODE search for Corsi / Mediceo 137.

## Dating of the working files

The 10 Nov working files are dated on Zenodo, DOI 10.5281/zenodo.24267269 [stated; not checked in this folder].

## Sources (copied unchanged; sha256)

| File here | Source | sha256 |
|---|---|---|
| `blind/BLIND.tsv` | corsi1513/blind/BLIND.tsv | 8b4f93bad118ae0653b77c0571d0d7bf0453697c13977f69409395433f168221 |
| `blind/BLIND_NOTES.md` | the same folder | 08bad784a0b9484ef444dc784720ee229e3e56c7c5b426b85f00971d77f51154 |
| `blind/FREEZE_blind.txt` | the same folder | 598a59c9cad1a37b0a9b348acf3414666ba5b2001c2d097a86f8f0413a51872b |
| `blind/SHEET.md` | the blind reader's packet | bc4f17f2f6e21ea09deca06d4bde39bec95102118dca77df3414257dccc57968 |
| `blind/decode_once.py` | corsi1513/blind | 1af728c5c0cc6d88cc3aa08f2948e564a61434e4465238f146db1bc7024396a5 |
| `blind/decode_once.txt` | corsi1513/blind | cb2cb63941231cafa3efd993b72b654b4e27cb276668186b43450914af4bcf21 |
| `blind/JUDGE_BRIEF.txt` | the judge's packet | 3a76a21720977bb88ecdbcbd8b3174cda839a7d8b6261a92924be85202262a73 |
| `blind/judge.tsv` | corsi1513/blind | f14f6d0c07e3a1454ca88da1fe5430cfa8b5e1976eedeebd58ed6db2fff2c38b |
| `blind/JUDGE_NOTES.md` | corsi1513/blind | c18bc3de9d29bc190e50e6066b8ab42e2a4334479e83b8209727760dcfd64158 |
| `blind/shuffle.py` | corsi1513/blind | 72285ac2f3f84d24af36dfd25487a16445b54d2c4af36c4e465b7a34136c6395 |
| `blind/shuffle_out.txt` | corsi1513/blind | a6e74f17e24d2b8f50be94798f089587d4c5f94cfa85d4db20484bf628c0be30 |
| `blind633/BLIND.tsv` | corsi1513/blind633 | 401dd386104d1f25780de998dd763db353a91203c51bd05647540688d4777a59 |
| `blind633/BLIND_NOTES.md` | corsi1513/blind633 | 952d42547320dcc7f7a6d9f5146fca6aa756440bd72fe57cbbd30cb289f3e7ab |
| `blind633/BLIND_PROMPT.txt` | corsi1513/blind633 | 12f3ecc461ddf9c31420ccf1ae7b0ba0d43bbf277c684991823c9a71e81b1f19 |
| `blind633/FETCH_LOG.txt` | corsi1513/blind633 | a3a85c5336dab8fedeed80a203c12996c8456b2d2fec5bbbbfb0904b43f7b2a4 |
| `blind633/FREEZE_blind.txt` | corsi1513/blind633 | 155de2309703ce3516e4d23c8c9ca8d2f003f48132d736bf4c2352b5742b8f95 |
| `blind633/SHEET.md` | corsi1513/blind633 | bc4f17f2f6e21ea09deca06d4bde39bec95102118dca77df3414257dccc57968 |
| `blind633/decode_once.py` | corsi1513/blind633 | 0f24e16947fbe8388c3370733a787f009d9bfbf223657fd75a50441c5fb247ef |
| `blind633/decode_once.txt` | corsi1513/blind633 | df0da98dbf631429c8dd9131a7d2a5e47acc83e2d23a404b08f0553c9752da76 |
| `blind633/JUDGE_BRIEF.txt` | corsi1513/blind633 | bdc41b686669aa1407b7bb1b6994551f361a22a535503d11086c8cb3237e8c70 |
| `blind633/judge.tsv` | corsi1513/blind633 | e9f67976d19f98d9058f2b8c6771b6455cbe7044c0ea1c807a83f00cf408b14c |
| `blind633/JUDGE_NOTES.md` | corsi1513/blind633 | e3308897d519205e1f00920d60cfeea67427a83221a829e8bd217d915e5457d5 |
| `blind633/shuffle.py` | corsi1513/blind633 | 65cb4ea4e48f83171f324cff80149af68e274c4e928f09f96b44872bf1e39fc8 |
| `blind633/shuffle_out.txt` | corsi1513/blind633 | 4375bbfaa2e18466199e2ff6e3bcdf1940745e1045884c961c361fed0d89b537 |
| `key_corsi_w17_frozen.json` | corsi1513 (key of record) | 5f56ad5879c6d53d9c865d52096fde97fbe831e6fcca924efe83a5247c732940 |
| `key_corsi_10nov_frozen.json` | corsi1513 (history) | b574007fd6dc6d15fc806ad65a215e2b46392d6874c54ea6ff8964c63e5ed25e |
| `FREEZE.txt` | corsi1513 | 7742e828be986702b4baff0a0a13edb939394afb47cb69d7a61ad174ff71ec10 |
| `PRIOR_ART.md` | corsi1513 | b9c8e2d15a593079feb91a6c95c6f6d4dfc785b010c189d8422380e7bf0e478e |

The hashes of BLIND.tsv and of the key match `blind/FREEZE_blind.txt` and `FREEZE.txt`; `blind633/BLIND.tsv` matches `blind633/FREEZE_blind.txt` (401dd386...) [measured]. The scripts expect to run from this folder (`key_corsi_w17_frozen.json`, `blind/BLIND.tsv`).

Derived here (16 Nov): `transcription_620.txt`, `transcription_623.txt`, `decryption_620.txt`, `decryption_623.txt` (rows split out unchanged, with a header), `reading_620.md`, `reading_623.md` (the judge's segmentation with marks), `translation_620.md`, `translation_623.md`, `profile.json`; and for doc 633 `transcription_633.txt`, `decryption_633.txt`, `reading_633.md`, `translation_633.md`.

## Limits

- Model sessions did all the work: key, transcription, judge and translation. No person read the signs or the text without AI.
- One blind transcription per letter. No second reader, and no check of doubtful signs on the images after the decode.
- The judge was a model session, scoring sense by its own lights. E and N calls are its own.
- The key rests on the decipherment of doc 627 (c. 635r, IIIF A0001353). Since 16 Nov it is in `doc627/`: the image id and md5, the decipherment as written, the 10 Nov cipher-block transcription and the frozen key's decode of it. That transcription is not blind and the key was built from it, so it documents the source but is not a control. Catalogue 2391's 6 Nov vetting note (no decipherment on any leaf) missed it because it sits at the foot of the page, below the signature, not between the lines or in the margin.

## Remaining gaps

- Doc 627 as a blind control (fresh reader, name-only sheet, one decode, scored against its decipherment) has not been run; the key's source itself is now documented in `doc627/`. Blocker: not-attempted.
- The prior-art sheet (Google Books / HathiTrust phrases, MAP inventory vol. 4, Spanish-side editions, DECODE) is not yet searched. Blocker: not-attempted. Needs Malcolm for the HathiTrust and Google Books phrases.
- The code values 27 (re di Scotia?) and 24 (Inghilterra?) in 623 are unverified. The basis for 22 (Francia) is not recorded in the key note, and #161 in 623 has no value. Blocker: open-codes.
- "dunhtare" occurs twice in 623 (dubitare?, with nh for bi), and "coiono" and "coioborato" occur in 620 (rr written as i?). Repeated misreadings like these point to a key value or sign-label error, not a slip. Blocker: not-attempted. To check on the images against the key.
- By `docs/_check_reading.py`, reading_620.md is "not a reading" (3 of 16 sentences clean), and reading_633.md 1 of 13, so the target is classed "not read" (outcome.class), with the key method unchanged. Blocker: not-attempted. It would be settled by fixing the key or label errors above, then a new frozen pass.
- Doc 633: the shapes NEW1 (a flat 2-like sign, frequent) and NEW2 and the bare sign z have no key value, and superscript attribution was the blind reader's hardest point. 21 of 95 N units are holes. Blocker: not-attempted. To check against doc 627's decipherment and the images, then a new frozen pass.
- Copies 621, 622 and 628 are not collated. 621 gives clear equivalents for part of 620. 622 repeats at least one cipher block of 623 (one block compared, 10 Nov: "tra 51 et 52"); the catalogue calls 622 a copy of a letter of 29 Jan 1514. Which is right is not settled. Blocker: not-attempted.

## Escalation

- [ ] siblings: 633 done (decoded, not read, 74.2% strict); 627 source documented (doc627/), blind control not run; copies 621, 622, 628 not collated
- [x] clear-pages: versos A0001330 and A0001342 seen by the blind reader. Clear closings, dates and addresses; no decipherment on 620 or 623
- [x] known-keys: compared with pandolfini1514 (the same family, a different table); the key comes from doc 627's contemporary decipherment
- [ ] print: Desjardins II checked (clear extracts only); MAP inventory vol. 4, Spanish-side editions, Google Books / HathiTrust not reached
- [ ] key-rebuild: the dunhtare and coiono errors point to key or label fixes, not yet tried
- [ ] retry: no second frozen pass yet. The first pass stands as the figure of record

## Files

- `transcription_620.txt`, `transcription_623.txt`: the blind transcription, split by letter. `blind/BLIND.tsv`: the original, with the clear words before each run.
- `key_corsi_w17_frozen.json`: the key of record. `key_corsi_10nov_frozen.json`: the 10 Nov key, for history. `FREEZE.txt`: their hashes.
- `decryption_620.txt`, `decryption_623.txt`: cipher and decode, row by row.
- `reading_620.md`, `reading_623.md`, `translation_620.md`, `translation_623.md`.
- `transcription_633.txt`, `decryption_633.txt`, `reading_633.md`, `translation_633.md`: doc 633, laid out as 620 and 623.
- `blind633/`: doc 633's fetch log, reader brief, label sheet (identical to `blind/SHEET.md`), blind notes and freeze, decoder and output, judge's brief, table and notes, control script and output. No images.
- `blind/`: the label sheet, the blind notes and freeze, the decoder and its output, the judge's brief, table and notes, and the control script and output.
- `PRIOR_ART.md`, `profile.json`.
