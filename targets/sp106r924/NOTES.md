# A member of Henrietta Maria's household (Paris) to Charles I, January 1646 — Lasry's "SP106-8" key — TNA SP 106/10 ff. 235–236 (DECODE R924) — NOTES

Split on 14 Oct 2026 from `hm1645` under the one-key rule (George Lasry, 14 Oct 2026). The old entry (catalogue 59)
joined six letters of SP 106/10 in four of Lasry's reconstructed keys. This letter is the only one of the six in his
**"SP106-8"** key. The others are different ciphers, each with its own entry and page: [`targets/hm1645/`](../hm1645/NOTES.md)
(R785, R790, R923, key TNA SP 106), [`targets/sp106r787/`](../sp106r787/NOTES.md) (R787, SP106-2),
[`targets/sp106r929/`](../sp106r929/NOTES.md) (R929, SP106-5).

**Outcome: read from existing decipherment.** Lasry's key and interlinear plaintext are on the DECODE record
(23 Oct 2020). Nothing about the text is added here. Sessions 2026-09-19 and 2026-10-14.

## The record

- DECODE R924 "TNA_SP106/10_UND_(0235-0236)", two images (`decode/IMG_R924_I4915_P1.png`, `_I4916_P2.png`,
  git-ignored). The cipher runs sideways on the leaves, numbers separated by colons.
- Files on the record (in `decode/`, git-ignored, DECODE's and Lasry's work): `DOC_R924_D1817` Pettersson's
  transcription (2019); `D3089` Lasry's key "TNA SP106-8" (dated 1646-01); `D3091` his interlinear cipher/plaintext of
  ff. 235–236 and 238–240; `D3090` his plaintext with dating notes.
- 2012 cipher groups, 214 distinct (`python docs/_check_profile.py --measure targets/sp106r924/decode/R924_ciphertext.txt`).
- Lasry's plaintext opens "PARIS JAN <DATE E> <207> IT PLEAS YOUR MAJESTY YOU HAVE SO MUCH <797> <320> HANDS ...":
  a writer at Paris to the King against Sir H. Compton's journey and the treaty for Prince Charles's marriage with
  Portugal, on Montreuil's mission, the frost that stopped the river traffic, levies in hand to send over "a body of
  5 or 6 thousand men". "The Queen sends ..." and "the Queen desires your Majesty ..." show the writer is not the
  Queen. Signed "I AM YOUR MAJESTY S <219> OBEDIENT <SERVANT> <385>".
- Lasry's dating note: "First letter dated January ... Montreuil - French emissary ... Also mentions frost like
  0245-0246 so either both collections are from Jan 1645, or from 1646 (more likely)". His note on the sibling
  R925 puts Henry Compton's embassy to Portugal in 1646–48.
- DECODE's start date is 26 June 1646; the letter says "Paris Jan". Queued as a correction (`decode_updates/queue.json`).
- Same key, in Lasry's file: R925 (ff. 238–240), a letter of the Queen (his "Second Letter from Queen": the marriage,
  Compton). Not a document of this entry.

## The key

Lasry's "TNA SP106-8": one- and two-digit homophones (A 15|23|25|5, E 11|2|22|26, ...) and a numbered word list from
100 up, roughly alphabetical (100 all, 101 are, 102 as, 103 at, 108 and, 109 be, 141 for, 173 I, 174 in, 176 ing ...).
His file says "There are no nulls".

## Check done here (14 Oct 2026)

```
python targets/sp106r924/apply_key.py targets/sp106r924/decode/DOC_R924_D3089_3089.txt 0235-0236 targets/sp106r924/decode/DOC_R924_D3091_3091.txt
```

2012 groups; 1850 (91.9%) get a value from the key. On 11 lines Lasry's plaintext line has a different number of
words from the cipher line and the columns shift; on the others (1604 keyed groups) every value equals his
plaintext. 162 groups have no value: 58 distinct three-digit numbers (85 tokens: 324 ×4, 428 ×4, 321 ×3, 532 ×3,
208 ×3 ...) and 11 low figures (77 tokens: 21 ×24, 30 ×15, 42 ×12, 50 ×9, 16 ×7 ...), which Lasry renders "_".
The reveal on the page is the first 120 groups of this run.

## Remaining gaps

- three-digit word-list numbers not in Lasry's key (58 distinct, 85 tokens) - blocker: open-codes; he leaves them in brackets; names and words of the numbered list, not reconstructed here
- low figures with no key value (11 distinct, 77 tokens; 21, 30, 42, 50, 16 ...) - blocker: open-codes; rendered "_" by Lasry; dividers, nulls or values missing from his alphabet, not settled

## Escalation

- [x] siblings: R925 (ff. 238-240) is in the same key per Lasry's file; the other SP 106/10 letters are in other keys
- [x] clear-pages: none; the record holds no clear copy
- [x] known-keys: Lasry's SP106-8 key is the key; applied here (agrees with his plaintext)
- [x] print: Lasry's DECODE files are the only decipherment found; Tomokiyo's unsolved list still carries the letters
- [n/a] key-rebuild: the entry is read from Lasry's existing decipherment; filling his word list (with R925) is new work for a later session
- [n/a] retry: nothing re-read; his decipherment taken as it is and checked with his key

## Assumptions for George's review

- The key groups follow the CATALOG NAME headers of George Lasry's DECODE files (23 Oct 2020): "TNA SP 106" for
  ff. 207-215, 218, 220-221, 230-234 (hm1645); SP106-2 for 216-217 and 219 (sp106r787); SP106-8 for 235-240
  (sp106r924); SP106-5 for 245-247 (sp106r929). His credit on each entry covers only the letters in that key.
- Only sp106r929 counts as "read with known key" (his key applied before his plaintext was compared, 19 Sept 2026);
  the other three entries are "read from existing decipherment", the key applied only as a check.
- Figures his key leaves without a value are treated as open, not as nulls, although his key files say "There are
  no nulls".
