# Intercepted letter from Brussels to Mr Copinger, 12 August 1656 (Thurloe State Papers v.267)

Attempted, not solved: 16 single digits (a 12-sign name and a 4-sign word) in a clear English letter; too short, no key fits.

Split on 14 Oct 2026 from `thurloe` under the one-key rule (George Lasry, 14 Oct 2026). Until then this piece was filed
with three other intercepts printed in Birch's *Thurloe State Papers* (cryptiana unsolved item #9) because they share
the printed source; each is in its own cipher. The others, each a different cipher with its own page:
[`targets/thurloe/`](../thurloe/NOTES.md) (Beverning 1653), [`targets/dugard1656/`](../dugard1656/NOTES.md) (du Gard
to White, 10 June 1656), [`targets/waddall1656/`](../waddall1656/NOTES.md) (Waddall to "Vanyeare", 22 Aug 1656). The
work below was done in the thurloe session of 15 Sept 2026 and is carried over from its NOTES; the ciphertext file
moved here on 14 Oct 2026. The shared scripts (`analyze.py`, `apply_keys.py`, the harvested keys) stay in
`targets/thurloe/`.

Work date: 2026-09-15.

## The document

- Thurloe State Papers (Birch 1742) vol. 5 p. 267, "An intercepted letter", Brussels, 12 Aug. 1656 [N.S.]; MS
  Bodleian Rawlinson A vol. xli p. 78 (not digitised). Addressed "To Mr. Copinger, at the widow Andrews, in
  Bedford-bury in Covent-garden". Full text on British History Online (vol5/pp258-271); page image in the Internet
  Archive scan `collectionofstat05thur`, leaf n272.
- Clear English news: the Spanish siege of Valenciennes, the Swedish war in Poland. Then: "2 3 1 4 7 4 6 4 9 7 2 3 is
  come with a great train to visit the 0 9 3 7. What his occasion is, is not yet known. God grant it be for good, for
  he is in a good way to gain his process."

## Transcription

`c_brussels_12aug1656.txt`. Measured: 16 tokens, 8 distinct (single digits).

## What was tried (15 Sept 2026)

- **Pattern and crib**: the name is ABCDEDFDGEAB, the word HGBE (sharing 9, 3, 7 with the name). Brussels, August
  1656: the arrival of Don Juan José of Austria as governor, or a visit to Charles II's court at Bruges, are the
  obvious contexts. "the king" (k-i-n-g) for the word would force the name to read ?n?dgdfdig?n, impossible, so
  either the digits are not simple letters or the word is not "king". Unresolvable at 16 symbols.
- **Key matching** (`targets/thurloe/apply_keys.py`, `apply_keys_out.txt`): every 1653-60 key on cryptiana (Marshall,
  Barwick-Hyde, Stamford, Butler, Charles II intercepted 1655, Kingston, Westrope, Hague agent/Blake) applied: none
  gives a name.

## Remaining gaps
- The name (12 digits) and the word (4 digits) - blocker: too-short; 16 single digits with 8 distinct, a ten-symbol cipher that the name pattern shows is not a plain letter alphabet for "the king"; no key online

## Escalation
- [n/a] siblings: the original is in Bodleian Rawlinson A vol. xli (not digitised); the Bruges court agents' ciphers of 1656 would be in the Clarendon MSS, not online
- [n/a] clear-pages: no images of the original, only Birch's 1742 print
- [x] known-keys: every 1653-60 key on cryptiana applied (apply_keys.py): none fits
- [x] print: Birch's TSP and cryptiana (Tomokiyo lists it as undeciphered) checked
- [n/a] key-rebuild: 16 digits are below any statistical attack; the crib "the king" was tested and fails
- [x] retry: the cribs were retried; nothing reads
