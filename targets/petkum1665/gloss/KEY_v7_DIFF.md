# key_v6.tsv (PR #646) -> key_v7.tsv (16 Nov 2026)

`key_v6.tsv` of PR #646 md5 b4156072b5c6ac8f2389222780e90af0 (key_v5 + nine values of Brice Dudout's T2 seen under a
gloss, 88 corrected). `key_v7.tsv` md5 d1ee7e3094e1643bfb0f58b39e9d0052 = that file, unchanged except: one header line
added at the top, row 164 changed, five rows appended under a `# Additions for KEY v7` line. Built by a script from
#646's file (md5 checked first). Nothing has been decoded with key v7; no figure of record changes; no frozen blind,
decode or judge file was touched.

This replaces the key_v6.tsv first filed with PR #689 (md5 9bce330ab3116ec3ae32946bb05df093), which was built on
key_v5 and collided in name and content with #646's key_v6.tsv. The rows below are the same readings, renamed v7 and
moved onto #646's file. The gloss files are renamed with them (`KEY_v6_*` -> `KEY_v7_*`, content unchanged).

Evidence: `KEY_v7_glosses_261294.tsv` (one row per gloss: code or sign, gloss word, image, page, line, cipher context).
Coverage and resolution per image: `KEY_v7_coverage_261294.tsv`. Fetches: `KEY_v7_FETCH_LOG_261294.txt` (Rigsarkivet
image API, plain GET, one at a time, 2 s pause, all HTTP 200, no bot check). Read by an AI reader (Claude): 119 images of
unit 261294 not read in full for v5 (11-16, 22, and 26-141 except 30, 33, 50, 71), the unread halves of 17, 23, 24, 25,
and 574R (unit 261267) re-read. Images 26-28 were read as full pages (about 1300 px) with zooms; the rest as two-page
spreads of about 1560 px after contact-sheet triage, lower than v5's 2400 px copies.

Brice Dudout's T2 was not used to find or choose any value below. Agreements with it are remarks only.

## Rows added or changed, with their basis

| row | v6 (#646) | v7 | tier | glosses | basis | flag |
|---|---|---|---|---|---|---|
| 164 | alliance (A2, 574R) | amitie | G | 21 | 7R, 17R, 21R, 24R x2 (seen for v5); 24L, 27L, 27R, 34R x2, 44R, 52R, 54R, 70L, 73L, 79R, 86R, 88L, 89L, 90L, 95R | changed |
| 151 | none | François | G2 | 1 | 23R, spread + zoom: "les François aussy bien que les Anglois" | single gloss, 1560 px spread |
| 181 | none | bruit | G2? | 1 | 27L, full page + zooms: 'bruit' over 181 where the sense wants contre; margin corrects to 185 | single gloss; doubtful (dispute below) |
| 248 | none | hommes | G? | 3 | 113L "d'hommes et d'Argant", 124R "huict mille hommes et", 127R "d'hommes", all spreads + zooms | doubtful (dispute below) |
| 346 | none | ratification | G | 2 | 113R "des Ratifications du traitte de Commerce", 141L "des dites ratifications", spreads + zooms | |
| DB (crossed d) | none | g | A | 4 | 112L "grand", 115L "Allemagne", 15L "signe", "signer", spreads | a sign, not a code number |

Tiers: G = code word glossed twice or more (counts E, never S); G2 = code word glossed once (counts E); A = spelled value.
A tier ending in `?` marks a doubtful row: `scripts/count_v7.py` counts it N, like tier C.

164: 163 = alliance stands beside it (24R "alliances et amities", 163.31.38.164.31). 574R re-read: its gloss is "de
l'alliance" over X.164, one chancery reading against 21, kept in the source note. #646's NOTES add that T2's held-out leaf
has "l'amitie" over x.164 (remark; agrees).

## Disputed: which number is 'bruit' (248 or 181)? Not settled, both rows marked doubtful

What #646 records (`NOTES.md` Remaining gaps, `key_v6.tsv` additions comment, `profile.json` gap): 248 is glossed 'bruit'
on image 541 left of unit 261267, by Brice Dudout's reading. His file `dudout/transcriptions/H2.txt` (PR #622), section
541 L, has the groups `lambda.4 | 248 | 356.253.2 | 14 | 182.lambda.366.313` glossed "un | bruit | sujet | a | caution":
"un bruit sujet a caution". #646's integration compared "the head of 541 left" with his file by eye and reports no
disagreement there; it does not say whether that comparison reached this group.

What our glosses show (`KEY_v7_glosses_261294.tsv`, unit 261294):

- 248 = hommes, three glosses in three different relations: 113L line ~13, "d'hommes et d'Argant" (17.248.31 100
  17.166: d + 248 + s, et, d + argent, neighbours valued); 124R line ~7, "avec huict mille hommes et" (381.Y 245.22.Y.32
  278.24.267 248.31 100); 127R line ~13, "(le nombre) d'hommes" (17.248.31). In each the plural s (31) follows 248.
- 181 = bruit, one gloss: 27L line ~22, 'bruit' over 181 in `181.26.340`, where the sense wants contre; the margin
  corrects it to "co n t re 185,26,32,340". The cipher clerk wrote 181 for 185 and the decipherer wrote his key value
  for 181 over it. One gloss, over a slip.
- In the bare letters #646 cites "mille 248s" and "cet 248 la" (NOTES, Remaining gaps). [derived, not tested] "cet"
  before the word fits hommes (h mute) better than bruit.

Possible readings of the conflict, none tested: (a) on 541L the cipher clerk wrote 248 where 181 was meant and the
decipherer glossed by sense; (b) the 541L figure is 181 or another number read as 248; (c) the code gives bruit two
numbers, or 27L's gloss is the decipherer's error. Image 541 left was not looked at again for this file.

Decision for v7: both values are kept with the evidence above and marked doubtful (tiers `G?` and `G2?`), counted N.
Neither is preferred. To settle: look at 541 left at full resolution for the figure under 'bruit', and search the
glossed leaves for a second gloss of 181.

## Agreements with #646, no change

- 88 = le Roy d'Espagne: #646 corrected 88 from 561R. Our reading of unit 261294 had proposed the same value from three
  Sehested glosses (86R "avec l'Empereur et le Roy d'Espagne", ct.381.Y.74.100.88.38.353.31; 117R twice "au Roy
  d'Espagne", ct.LAM.88). #646's row is kept as it stands; these glosses are further support (glosses file, kind NOTE88).
- 134 = Stockholm (#646, from T2): not met in our reading; kept.
- Row T = y stands: a single small T is glossed y at least 11 times (26R x3, 52R, 53L, 88R, 132R, 133L, 136L x2, and in
  luy, payer, j'ay). The 'T T' of the 16 Nov Paulmyer blind files (filed in the passages pull request) is one cursive #
  sign, HSH = o (113R "ou" = HSH.LAM; 111L "obtenir"): a transcription error there, not a key fault.

## Proposed, not applied

- Tier upgrades C -> A2 (one gloss each): 245 = hu (124R "huict"), 252 = ja (27L "j'avois"; also 52R, 132R), 256 = ju
  (35 "juge", 140R "justice").
- 82 = Brandebourg: a second attestation (88R); the row stands.
- Sign 9 (Sehested's hand) = b in "subsides" and "obtenir": not checked against row 9.

## Not adopted

- 40: 112L, inside the gloss "plus" over G.26.40.270.31: no word for 40 alone; possibly a null. Open.
- 235 and 399: clerk's slips corrected in the margin (26L 235 for 253 je; 34R 399 for 339 ra). No value.
- 351: 17L spells rupture out (343.G.368.340), so no evidence for 351 there.

## Open numbers (counted by `scripts/count_v7.py`, output `counts_v7.txt`)

Of the 21 numbers open after key v5 (40, 108, 134, 135, 151, 181, 197, 198, 235, 248, 330, 344, 346, 351, 370, 374,
376, 388, 390, 394, 399): 21 - 1 (#646: 134) - 4 (v7: 151, 181, 248, 346) = 16 with no value (40, 108, 135, 197, 198,
235, 330, 344, 351, 370, 374, 376, 388, 390, 394, 399); 16 + 2 doubtful (181, 248) = 18 without a settled value.

Over every code number in the first-reader transcriptions (175 distinct numbers, 1,856 occurrences): no value under v5
35 numbers (68 occurrences); under v6 35 - 5 = 30 (55); under v7 30 - 4 = 26 (42); with the 2 doubtful rows, 28.

Per letter (section 3 of `counts_v7.txt`, not a count of record): 14 word units move, 11 N to E (151 x4, 346 x7) and 3 N
to S (DB = g in 24 Mar 1665, 10 Dec 1665, 13 Apr 1666). The doubtful 181 and 248 move nothing.

## Limit

Images 29-141 were triaged on contact sheets and read as 1560 px spreads; a target number written small could have been
missed, and the single-gloss row 151 rests on one such reading.
