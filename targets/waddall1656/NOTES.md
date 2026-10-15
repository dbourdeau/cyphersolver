# Jo. Waddall (London) to "Vanyeare" at Bruges, 22 August 1656 (Thurloe State Papers v.337)

Attempted, not solved: 50 cipher groups (29 distinct, homophonic letters 7-86 plus codes 226 243) in a clear English
letter; too short to pin, no key fits.

Split on 14 Oct 2026 from `thurloe` under the one-key rule (George Lasry, 14 Oct 2026). Until then this piece was filed
with three other intercepts printed in Birch's *Thurloe State Papers* (cryptiana unsolved item #9) because they share
the printed source; each is in its own cipher. The others, each a different cipher with its own page:
[`targets/thurloe/`](../thurloe/NOTES.md) (Beverning 1653), [`targets/dugard1656/`](../dugard1656/NOTES.md) (du Gard
to White, 10 June 1656), [`targets/copinger1656/`](../copinger1656/NOTES.md) (Brussels to Copinger, 12 Aug 1656). The
work below was done in the thurloe session of 15 Sept 2026 and is carried over from its NOTES; the ciphertext file
moved here on 14 Oct 2026. The shared scripts (`analyze.py`, `apply_keys.py`, `solve_a2.py`, the harvested keys) stay
in `targets/thurloe/` and read this folder's file.

Work date: 2026-09-15.

## The document

- Thurloe State Papers (Birch 1742) vol. 5 p. 337, "An intercepted letter", the 22nd of August 1656; MS Bodleian
  Rawlinson A vol. xli p. 642 (not digitised). Signed "Jo. Waddall"; superscription "A mons. mons. Vanyeare marchant
  demeurant au logis de M. Robinson en Bruges, Flandres". Bruges was Charles II's court in 1656-58. Full text on
  British History Online (vol5/pp333-350); page image in the Internet Archive scan `collectionofstat05thur`, leaf n342.
- English in phonetic spelling, about the elections to the Second Protectorate Parliament (20 Aug 1656 OS) and the
  Westminster riot between Colonel Grosvenor's soldiers and Mr Latham's party. The cipher sits in the clear frame:
  "There is [6] of [3] sent to lie near [7] and six [6] of [243 226] are [3] to strengthen [3], and [8] is so far out
  of favour now, that [5] told me he had a greater mind to [3] him than [4]".

## Transcription

`d_waddall_1656.txt`. Measured with `--digits`, skipping all but the four cipher lines: 50 groups, 29 distinct.
Letters 7-86 plus the codes 226 243.

## What was tried (15 Sept 2026)

- **Key matching** (`targets/thurloe/apply_keys.py`, `apply_keys_out.txt`): every 1653-60 key on cryptiana (Marshall
  1656-58, Barwick-Hyde 1659-60, Stamford 1655, Butler 1656, Charles II intercepted 1655, Kingston 1658, Westrope 1655,
  Hague agent/Blake), scored by English quadgrams. The Marshall key covers 48 of 50 groups and gives "Theare is b s g n
  g m of i l m sent to lie nere k g c i k m d ...": noise.
- **Cribs** in the clear frame ("horse", "hang"): 27 distinct letter-symbols in 50 groups with homophones; every crib
  fits many assignments equally well.
- Not put through the matched control run on piece (a) (`targets/thurloe/control.py`): 29 distinct symbols in 50
  groups is fewer than two occurrences per symbol.

## Remaining gaps
- The eight cipher words (50 groups) and the code pair 243 226 - blocker: too-short; 29 distinct homophonic symbols in 50 groups, cribs fit many assignments; the key would be in the Clarendon MSS (the Bruges court's agents' ciphers), not online

## Escalation
- [n/a] siblings: the original is in Bodleian Rawlinson A vol. xli (not digitised); the Bruges court agents' ciphers of 1656 (Hyde/Nicholas with their agents) would be in the Clarendon MSS, not online
- [n/a] clear-pages: no images of the original, only Birch's 1742 print
- [x] known-keys: every 1653-60 key on cryptiana applied (apply_keys.py): none fits
- [x] print: Birch's TSP and cryptiana (Tomokiyo lists it as undeciphered) checked
- [n/a] key-rebuild: 50 groups over 29 homophonic symbols cannot be pinned; cribs fit many assignments
- [x] retry: the cribs were retried; nothing reads
