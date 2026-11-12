# PREREG — sanchez-1522, lot 2 (12 Nov 2026, fil 🔓, Claude Opus 5.5)

Frozen by SHA-256 (line added to HANDOFF.md) BEFORE any decoding of any lot-2 transcription and BEFORE the R9607 re-check.

## 1. Key: unchanged, so no new measure
Daniel's key for targets/sanchez1522 at origin/main 62b62c5b5 (unchanged at 3fc9defbb for this folder): key_codes.tsv
b81cc2266f5cbd23f4e69555c3f2d27dea43fa4a71ee0721dd1d68c9166bcb58, alpha.py 26dfe3f6…5739. Lot 1 (C02) established no
code value ("none was added"). **No code value and no sign value is added in this session.** Code groups absent from the
key stay unresolved (I) in every count; values suggested by context are listed as proposals only, not applied.
Consequently no new measure is run (the lot-1 measure on R9632 f. 200r ll. 7-25 stands; that passage is burnt and is not
reused for anything). If a key change were ever adopted later, it would need its own PREREG and a fresh held-out portion.

The sign table used for reading (`tools/decode_lot2.py`, SHA-256 bea96542…8ffa9) is the lot-1 measure table plus two
entries that are in Daniel's alpha.py and were missing from the lot-1 script: `mo` = h, `xo` = s. Declared look-alike
alternatives (resolved by sense, word then marked P): g = r|y ; q = s|t ; Yo = s|t ; P = f|s ; 3 = d|e ; Z = a|s|c ;
B = m|r ; tt = p|n (measure table p, alpha.py n). Everything else single-valued.

## 2. Letters read in this session
Blind shape transcriptions, each frozen by SHA-256 before decoding (HANDOFF lines):
- R9610 (2 June 1522, ff. 132r-134r), `transcriptions/R9610_signs.txt` 50c67271bf0d910fe8fe730b3a713216fc494bbff7b6ba23144eef641001c7de.
Further letters, if any, are frozen the same way and listed in HANDOFF before their decoding.

## 3. Re-check of R9607 (C02's unresolved words), declared now, before any re-count
Input: the frozen lot-1 transcription `transcriptions/R9607_signs.txt` (4276b855…7b39), not re-transcribed, and C02's
reading `transcriptions/R9607_reading.txt`. Tool: `tools/recheck_r9607.py` (SHA-256 1e7e4c08…95a0) with lexicon = words
seen ≥ 2 times in Don Quijote (`duran-1718/dl/corpus/quijote.txt`) + `tools/extra_words.txt` (79eda25c…51d: proper names
and chancery forms already read in R9607/R9605). For each run of single letter signs the tool enumerates the declared
alternatives (§1, plus adjacent `m o` read as the single sign `mo` = h) and keeps the segmentations into lexicon words
with the fewest words.
Rule: a word that C02 marked I (<…>) becomes P **only if** (a) the tool marks its run UNIQUE, or the run is ambiguous but
exactly one of the minimal segmentations fits the sentence by sense, (b) the result is a Spanish word in the context, and
(c) no code group value is invented. A word C02 marked S or P is never downgraded or upgraded by this re-check. Code
groups absent from the key remain I; for each, the lot-2 contexts (R9610 and any further letter) are listed, with the
value they suggest, as proposals only. The re-check is reported as before/after counts on the same 1,555 words.

## 4. Counting rule (unchanged from lot 1): Daniel's 95 % rule
Per letter: S (sure), P (probable), R (restored), I (unresolved); "read" iff (S+P)/(S+P+R+I) ≥ 95 %, else "read in part".
Clear-text words are not counted.
