# French news letter forwarded to Henrietta Maria's household, 19/29 July 1645 — Lasry's "SP106-2" key — TNA SP 106/10 ff. 216–217 (DECODE R787) — NOTES

Split on 14 Oct 2026 from `hm1645` under the one-key rule (George Lasry, 14 Oct 2026). The old entry (catalogue 59)
joined six letters of SP 106/10 in four of Lasry's reconstructed keys. This letter is the only one of the six in his
**"SP106-2"** key. The others are different ciphers, each with its own entry and page: [`targets/hm1645/`](../hm1645/NOTES.md)
(R785, R790, R923, key TNA SP 106), [`targets/sp106r924/`](../sp106r924/NOTES.md) (R924, SP106-8),
[`targets/sp106r929/`](../sp106r929/NOTES.md) (R929, SP106-5).

**Outcome: read from existing decipherment.** Lasry's key and interlinear plaintext are on the DECODE record
(23 Oct 2020). Nothing about the text is added here. Sessions 2026-09-19 and 2026-10-14.

## The record

- DECODE R787 "TNA_SP106/10_UND_(0216-0217)", two images (`decode/IMG_R787_I4424_P1.png`, `_I4425_P2.png`,
  git-ignored). The cipher is written sideways on the leaves, numbers separated by commas.
- Files on the record (in `decode/`, git-ignored, DECODE's and Lasry's work): `DOC_R787_D1811` Pettersson's
  transcription (19 Aug 2019); `D3071` Lasry's key "TNA SP106-2" (dated 1645-07 to 1645-08); `D3073` his interlinear
  cipher/plaintext of ff. 216–217 and 219; `D3072` his plaintext with dating notes.
- 1569 cipher groups, 74 distinct (`python docs/_check_profile.py --measure targets/sp106r787/decode/R787_ciphertext.txt`).
- A duplicate ("DUPLICATA ENVOIE ... 19/29 JUILLET PAR AUTRE VOIE"), in French, signed with numbers "<103> <62> A <104>".
  Content: the Parlement de Paris and the duc d'Épernon, an envoy refusing to be heard except as an ambassador, the
  war news of summer 1645 (Enghien takes Heidelberg and pursues the Bavarians, the fort of Linck taken, Piccolomini
  entrenched round Dunkirk, a check to Montrose).
- Lasry's dating note: "Year 1645 - given in plaintext (July and August). In French but not from the King. Might be
  Goffe from Holland to the Queen, the letter being forwarded without change from France to the King." DECODE
  catalogues the author as "Assistant of Henrietta-Maria" and the receiver as the Queen and the King. Writer and
  receiver are left open here.
- Same key, in Lasry's file: f. 219, a letter of 30 Aug 1645 bound inside DECODE R788 (ff. 218–221; DECODE's own note
  says "two keys involved: 218, 220, 221 / 219"). Not a document of this entry.

## The key

Lasry's "TNA SP106-2": letter values on the numbers 1–60, two for most letters, four for A, E and O, nine for I
(25|26|29|37|38|57|58|59|60). His file says "Homophonic cipher with nomenclature" and "There are no nulls", but lists
no nomenclator values: the numbers above 60 stay open in his plaintext (bracketed or marked "?").

## Check done here (14 Oct 2026)

```
python targets/sp106r787/apply_key.py targets/sp106r787/decode/DOC_R787_D3071_3071.txt 0216-0217 targets/sp106r787/decode/DOC_R787_D3073_3073.txt
```

1569 groups; 1538 (98.0%) get a value from the key; all 1538 equal Lasry's plaintext (every line's columns line
up). The 31 others: 64 ×5, 103 ×3, 61 ×3, 62 ×3, 104 ×2, 116 ×2 and single 9, 06, 63, 71–75, 83, 97, 102, 105, 121.
The reveal on the page is the first 120 groups of this run.

## Remaining gaps

- nomenclator numbers above 60 and two stray figures (19 distinct, 31 tokens; 64, 103, 61, 62, 104, 116 ...) - blocker: open-codes; not in Lasry's key, his plaintext leaves them open; names and titles, one of them the writer's signature

## Escalation

- [x] siblings: f. 219 (inside R788) is in the same key per Lasry's file; the other SP 106/10 letters are in other keys
- [x] clear-pages: none; the record holds no clear copy
- [x] known-keys: Lasry's SP106-2 key is the key; applied here (agrees with his plaintext)
- [x] print: Lasry's DECODE files are the only decipherment found; Tomokiyo's unsolved list still carries the letters
- [n/a] key-rebuild: the entry is read from Lasry's existing decipherment; valuing his nomenclator (with f. 219) is new work for a later session
- [n/a] retry: nothing re-read; his decipherment taken as it is and checked with his key

## Assumptions for George's review

- The key groups follow the CATALOG NAME headers of George Lasry's DECODE files (23 Oct 2020): "TNA SP 106" for
  ff. 207-215, 218, 220-221, 230-234 (hm1645); SP106-2 for 216-217 and 219 (sp106r787); SP106-8 for 235-240
  (sp106r924); SP106-5 for 245-247 (sp106r929). His credit on each entry covers only the letters in that key.
- Only sp106r929 counts as "read with known key" (his key applied before his plaintext was compared, 19 Sept 2026);
  the other three entries are "read from existing decipherment", the key applied only as a check.
- Figures his key leaves without a value are treated as open, not as nulls, although his key files say "There are
  no nulls".
