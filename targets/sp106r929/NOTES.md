# Henrietta Maria's household (Paris) to "Sir", 26 January 1646 — Lasry's "SP106-5" key — TNA SP 106/10 f. 247 (DECODE R929) — NOTES

Split on 14 Oct 2026 from `hm1645` under the one-key rule (George Lasry, 14 Oct 2026). The old entry (catalogue 59)
joined six letters of SP 106/10 in four of Lasry's reconstructed keys. This letter is the only one of the six in his
**"SP106-5"** key. The others are different ciphers, each with its own entry and page: [`targets/hm1645/`](../hm1645/NOTES.md)
(R785, R790, R923, key TNA SP 106), [`targets/sp106r787/`](../sp106r787/NOTES.md) (R787, SP106-2),
[`targets/sp106r924/`](../sp106r924/NOTES.md) (R924, SP106-8).

**Outcome: read with known key.** Lasry's SP106-5 key, on the DECODE record since 23 Oct 2020, was applied here to
Sofia Pettersson's transcription of f. 247 without his plaintext (19 Sept 2026), and then group by group to the whole
letter (14 Oct 2026). His plaintext existed first; the application reproduces it. Nothing about the text is new.

## The record

- DECODE R929 "TNA_SP106/10_UND_(0247)", one image (`decode/IMG_R929_I4926_P1.png`, git-ignored). The cipher is
  written sideways across the lower part of the leaf; the outer fold carries ":298:" and "from S.P. 106/10".
- Files on the record (in `decode/`, git-ignored, DECODE's and Lasry's work): `DOC_R929_D1821` Pettersson's
  transcription (29 Oct 2019); `D3085` Lasry's key "TNA SP106-5" (dated 1646-01); `D3084` his interlinear
  cipher/plaintext of ff. 245–246 and 247; `D3083` his plaintext with dating notes.
- 348 cipher groups, 93 distinct (`python docs/_check_profile.py --measure targets/sp106r929/decode/R929_ciphertext.txt`).
- Lasry's plaintext opens "PARIS JAN 26 SR THE <334> HAS THIS WEKE RECEIVED <425>S OF THE 26 OF DECEMB AND OF THE
  4 OF JANUARY". The writer thanks "Sir" for the continued weekly news of "the <241>'s affairs, how bad so ever",
  hopes they are not so desperate as not to subsist without further losses until "our endeavours" for relief take
  effect, and writes "likewise concerning the embassage and marriage" (Prince Charles's marriage treaty). Signed
  with numbers: <316> <440> <236>.
- Year: Lasry's notes on the SP106-5 letters prefer January 1646 (the marriage, not yet concluded, is also in
  Charles's letter to the Queen of 22 Jan 1646). DECODE already carries 26 Jan 1646.

## The key

Lasry's "TNA SP106-5": one- and two-digit homophones (A 14|15|16|17, E 1|2|3|4|5, ...) and a nomenclator written
as a letter and a digit (a1 and, a2 are, d5 his, e5 in, k1 of, n1 to, n3 the, n4 this, p5 with ...), with a few
three-digit numbers (105 with, 321 parti, 888 re). His file says "There are no nulls". It is also the
Charles I–Henrietta Maria key that read `rupert1645`. Same key on R928 (ff. 245–246, Dr Stephen Goffe at The Hague,
January 1646), per Lasry's interlinear file.

## Check done here

- 19 Sept 2026: the alphabet applied by hand to Pettersson's raw transcription, without the plaintext file, reads
  "…ARIS … IAN … SR … RECEIVED <425>S … DECEMB … IANVARY … THANKES … CONTINUATI[ON] … WEKLY ADVERTISEMENTS … STATE …
  AFFAIRES HOW BAD … EVER … DESPERATE … ABLE … SUBS[IS]T … WITHOUT FARTHER LOSSES … TILL OUR ENDEAVOURS … RELEIF …
  BROUGHT … EFFECT … LIKEWISE CONCERNING THE EMBASSAGE AND MARRIAGE", matching his plaintext.
- 14 Oct 2026: `apply_key.py` over the whole letter:

  ```
  python targets/sp106r929/apply_key.py targets/sp106r929/decode/DOC_R929_D3085_3085.txt 0247 targets/sp106r929/decode/DOC_R929_D3084_3084.txt
  ```

  348 groups; 293 (84.2%) get a value from the key; all 293 equal Lasry's plaintext (every line's columns line up).
  The reveal on the page is the first 120 groups of this run.

## Remaining gaps

- three-digit nomenclator numbers (17 distinct, 23 tokens: 425, 199, 429, 810, 241 ...) and the group e3 (2 tokens) - blocker: open-codes; not in Lasry's key, mostly names (241 probably the King); not reconstructed here
- the figures 81-90 (9 distinct, 30 tokens) - blocker: open-codes; not in the key, they fall between words ("HOW _ BAD _ SO EUER"), dividers or nulls against the "no nulls" of Lasry's key file; not settled

## Escalation

- [x] siblings: R928 (ff. 245-246) is in the same key per Lasry's file; the other SP 106/10 letters are in other keys
- [x] clear-pages: none; the record holds no clear copy
- [x] known-keys: Lasry's SP106-5 key applied; it also read rupert1645
- [x] print: Lasry's DECODE files are the only decipherment found; Tomokiyo's unsolved list still carries the letters
- [n/a] key-rebuild: rebuilding Lasry's nomenclator from the whole SP106-5 corpus (R928, Add MS 72438) is new work for a later session
- [n/a] retry: nothing beyond the key's values was read here, so there is nothing to regrade

## Open (not pursued)

- Who 316 440 is, and who "Sir" is. DECODE gives the receiver as "Henrietta-Maria ... and Charles I", but the letter
  is written from Paris, where the queen was, to "Sir", who sends weekly news of the King's affairs: someone at the
  King's side. Queued as a note, not as a field correction.

## Assumptions for George's review

- The key groups follow the CATALOG NAME headers of George Lasry's DECODE files (23 Oct 2020): "TNA SP 106" for
  ff. 207-215, 218, 220-221, 230-234 (hm1645); SP106-2 for 216-217 and 219 (sp106r787); SP106-8 for 235-240
  (sp106r924); SP106-5 for 245-247 (sp106r929). His credit on each entry covers only the letters in that key.
- Only sp106r929 counts as "read with known key" (his key applied before his plaintext was compared, 19 Sept 2026);
  the other three entries are "read from existing decipherment", the key applied only as a check.
- Figures his key leaves without a value are treated as open, not as nulls, although his key files say "There are
  no nulls".
