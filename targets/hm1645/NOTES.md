# Henrietta Maria's household (St Germain) to Charles I, September 1645 — Lasry's "TNA SP 106" key — TNA SP 106/10 — NOTES

Status: in progress. Re-read 22 Oct 2026 (b14): all three letters read from the key decode (texts/); the site page and ledgers are not updated yet.

**22 Oct 2026, reading audit** (George Lasry's test): Lasry's plaintexts of R785, R790 and R923 are on the DECODE records only; the git-ignored copies are no longer in any checkout, so nothing could be read. All three are *decoded, not read* in profile.json; class already solved is kept (his decipherment exists), fraction_read 0.9099 -> 0.

**22 Oct 2026, re-read (REREAD_BRIEF, batch b14).** Every file on the three DECODE records was fetched with the shared
cookie into the session scratchpad (Lasry's key, interlinear and plaintext files; Pettersson's transcriptions; 7
images); no contemporary decipherment or clear copy is on them. Each cipher line was decoded with Lasry's key beside his
plaintext (research/reading_audit/b14_hm.py). Two key values are corrected because every occurrence needs it: 292 = by
(Lasry "because") and 435 = next (Lasry "of"). The groups from 279 up are an alphabetical codebook, and band plus
context across the six letters of the key fixes 31 of the groups he left open (texts/hm1645_codes.tsv: 295 business,
330 dispatch, 340 foot, 405 master, 446 particular, 502 she, 518 those, 548 who, 392+498 lord+ship ...). On the images:
R923's "from the King this post" is 127 (the Queen; a 7 over a 6), and its "Lorrain support" is "forrain [succour]"
(341 r a 382 497). R785 is signed "A Cowley" and its f. 215 is a second letter in the same key. Readings, English
versions, corrections and the log are in texts/ (R785-R923_reread_log.md). _check_reading.py on the bodies (figures' spelling): R785
0.645, R790 0.542, R923 0.52 (0.841, 0.792, 0.84 in modern spelling: a word-list artefact); all three read; fraction_read 1.0. Lasry's own files stay out of the repository; the
readings here are built from the decode. Whether he wants the readings kept, and the 292/435 corrections, are for him.

Split on 14 Oct 2026 from the former `hm1645` under the one-key rule (George Lasry, 14 Oct 2026). The old entry
(catalogue 59) joined six letters in four of Lasry's reconstructed keys. This folder keeps the three letters in his
**"TNA SP 106"** key (R785, R790, R923). The others are different ciphers, each with its own entry and page:

- [`targets/sp106r787/`](../sp106r787/NOTES.md), R787 (ff. 216–217, July 1645, French), key SP106-2;
- [`targets/sp106r924/`](../sp106r924/NOTES.md), R924 (ff. 235–236, Paris, January 1646), key SP106-8;
- [`targets/sp106r929/`](../sp106r929/NOTES.md), R929 (f. 247, Paris, 26 January 1646), key SP106-5, the one
  letter where his key was applied here before his plaintext was compared.

**Outcome: read from existing decipherment.** George Lasry's key and his interlinear plaintext of ff. 207–234 are on
the DECODE records (uploaded 23 Oct 2020). Nothing about the text is added here. Sessions 2026-09-19 and 2026-10-14.

## What DECODE holds for these three letters

Each record page links four files (fetched with the shared cookie into `decode/`, git-ignored because they are
DECODE's and Lasry's work):

- `DOC_R785_D1809`, `DOC_R790_D1815`, `DOC_R923_D1816`: Sofia Pettersson's manual transcriptions ("SofPe"), Aug–Sept 2019;
- `DOC_R*_D3059/D3067/D3068` (one file): Lasry's reconstructed key "TNA SP 106", dated 1645-09;
- `DOC_R*_D3060/D3065/D3069` (one file): his interlinear cipher/plaintext for ff. 207–210, 211–212, 213–215,
  218–221, 230–232, 233–234;
- `DOC_R*_D3061/D3066/D3070` (one file): his plaintext with dating notes ("As all messages are from September and
  all under the same key, it can be assumed that everything is from Sept 1645").

| record | folios | date (Lasry) | language | groups (measured) |
|---|---|---|---|---|
| R785 | 213–215 | St Germain, 1 Sept 1645 ("the Queen is perfectly recovered"), signed 120 | English | 1882 (172 distinct) |
| R790 | 230–232 | St Germain, 22 Sept 1645 (penal laws, Sir Kenelm Digby at Rome) | English | 769 (121 distinct) |
| R923 | 233–234 | St Germains, 29 Sept 1645 (the Duke of Lorraine's "little remote hopes"), signed 120 | English | 722 (119 distinct) |

Counts: `python docs/_check_profile.py --measure targets/hm1645/decode/R<id>_ciphertext.txt` over the cipher lines
of Lasry's interlinear file (`decode/`, not committed).

Siblings in the same key, per Lasry's interlinear file: R752 (ff. 207–210, catalogue 54, the Queen's French letter
of 15 Sept), R754 (ff. 211–212), and R788 (ff. 218, 220–221; DECODE notes that f. 219 is in a second key, which
Lasry's files place in SP106-2). They were never documents of this entry and are not re-checked here.

DECODE's own "Hanoverian, based on the handwriting" dating in the record notes is superseded by Lasry's content
dating; DECODE's start dates already carry his days. R923's note "probably ... plaintext in French" is wrong
(English). Queued in `decode_updates/queue.json`.

## The key

Lasry's "TNA SP 106": one- and two-digit homophones (E 21|38|54|6|67, I 20|36|5|57|66, U 26|3|41|73|74, ...) and a
nomenclator of three-digit numbers (124 England?, 126 the King, 127 the Queen, 157 the Prince of Wales, 208 Prince
of Orange?, 279 and, ...), numbers separated by colons. His file says "There are no nulls".

## Check done here (14 Oct 2026)

`apply_key.py` applies the key group by group to the cipher lines of Lasry's interlinear file and compares with his
plaintext line:

```
python targets/hm1645/apply_key.py targets/hm1645/decode/DOC_R785_D3059_3059.txt 0213-0215 targets/hm1645/decode/DOC_R785_D3060_3060.txt
```

| letter | groups | given a value by the key | compared (lines whose columns line up) | agree |
|---|---|---|---|---|
| R785 | 1882 | 1718 (91.3%) | 1520 | 1520 |
| R790 | 769 | 693 (90.1%) | 585 | 585 |
| R923 | 722 | 658 (91.1%) | 607 | 607 |
| total | 3373 | 3069 (91.0%) | 2712 | 2712 |

On the 17 lines where his plaintext line has a different number of words from the cipher line, the columns shift and
no group-by-group comparison is made. The key reproduces his plaintext exactly; the reveal on the page is drawn from
this run (R785, the first 120 groups).

Groups with no value in the key: 58 distinct three-digit nomenclator numbers (99 tokens), which Lasry leaves in
brackets, and 11 one- and two-digit figures (205 tokens: 78 ×61, 77 ×49, 16 ×26, 49 ×20, 59 ×17, 39 ×16, 30 ×7,
79 ×5, ...), which he renders "_". In the text they fall between words ("PERTECTLY _ RECOUERED", "ST _ GERMAIN").
They look like word dividers or nulls, against the "no nulls" of his key file; not settled here.

## Remaining gaps

- three-figure nomenclator groups still open (28: 120, 148, 208, 212, 228, 234, 237, 257, 300, 334, 344, 348, 350, 353, 424, 469, 486, 488, 489, 500, 507, 522, 525, 529, 535, 541, 543, 545; 40 tokens in the three readings) and the two-figure 85 (a place) and 60 - blocker: no-key-material; seen once or twice in the six letters of the key, no context fixes them (31 others fixed on 22 Oct, texts/hm1645_codes.tsv)
- one- and two-digit figures with no value in the key (11 distinct, 205 tokens) - blocker: no-key-material; between words throughout, read as separators; nothing on the records says whether they are nulls

## Escalation

- [x] siblings: R752, R754, R788 are in the same key (Lasry's interlinear file); not documents of this entry
- [x] clear-pages: none; the records hold no clear copy
- [x] known-keys: Lasry's TNA SP 106 key is the key; applied here to all three letters (agrees with his plaintext)
- [x] print: Lasry's DECODE files are the decipherment; Tomokiyo's unsolved list still carries the SP 106 letters
- [x] key-rebuild: 22 Oct 2026, 31 nomenclator groups fixed from the codebook's alphabetical bands and context; 292 and 435 corrected
- [x] retry: 22 Oct 2026, all three re-read from the key decode, doubtful figures checked on the images (texts/hm1645_corrections.tsv)

## Open (not pursued)

- The writers: "120" at St Germain, probably of the queen's secretariat.
- Tomokiyo's unsolved list still carries the Henrietta Maria SP 106 letters; Lasry's DECODE readings answer it.

## Assumptions for George's review

- The key groups follow the CATALOG NAME headers of your DECODE files (23 Oct 2020): "TNA SP 106" for ff. 207-215,
  218, 220-221, 230-234; SP106-2 for 216-217 and 219; SP106-8 for 235-240; SP106-5 for 245-247. Your credit on each
  entry covers only the letters in that key.
- This entry (and sp106r787, sp106r924) is "read from existing decipherment": your plaintext is the reading; your key
  was applied here only as a check. Only sp106r929 counts as "read with known key", because the key was applied
  there before your plaintext was compared (19 Sept 2026).
- The low figures your key leaves without a value (78, 77, 16 ...) are treated as open, not as nulls, because they
  fall between words while your key file says "There are no nulls".

## 14 Nov 2026: full-texts pass, key file listed

`outcome.key_file` was missing although the contribution includes "key extended or corrected". It now points at
`texts/hm1645_codes.tsv`: the project's own key work of 22 Oct 2026 (292 = by and 435 = next corrected, and the
nomenclator values proposed from the codebook's alphabetical bands). This file is the extension only. George Lasry's
base key "TNA SP 106" is his DECODE record file (DOC_R785_D3059), which stays out of the repository as before, so
the folder still holds no complete key; nothing else changed.
