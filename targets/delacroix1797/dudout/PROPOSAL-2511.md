# delacroix1797: a person's look at the eight digit proposals (sign plate 2511, 25 Nov 2026)

The profile holds the eight digit changes of `beling2026/proposals/transcription_corrections.tsv` "until a person has
looked at NARA M30 roll 4 frames 0244-0245". Brice Dudout looked, on a blind shape plate: each doubtful digit boxed on
its line, options cut from clear digits of the same hand, no reading or value shown, three hidden controls.

- Controls: 3 of 3 passed.
- Read by the person: 808 -> **898**, 327 -> **527**, 381 -> **361**, 108 -> **100**; 257 ×3 -> **257** (as written);
  1024 -> **1084**.
- Applied under the rule hashed beforehand (`sign_check_2511/RULE-2511.md`): the four changes whose corrected group
  already carries the draft's letters (898 = con, 527 = d, 361 = del, 100 = sur).
- `delacroix1797-planche-2511.patch`: those four groups in `beling2026/key/alignment_by_group.txt`, and their four
  lines removed from `beling2026/proposals/transcription_corrections.tsv`. `ciphertext.txt` (Brackx's) is not touched;
  whether to record the four readings there is the maintainers' call.
- Effect (`RECOUNT-2511.md`): 27 -> 23 holes, read share 0.939 -> 0.948; still read in part.

Files: `sign_check_2511/answers-2511-delacroix1797.json` (answers as given), `key-2511-delacroix1797.json` (forme ->
digit, written with the plate), `results.tsv`, `REGLE-SELECTION.md` (the hashed rule, French) and `RULE-2511.md` (its translation). Checksums in `SHA256SUMS-2511`. No image is committed.
