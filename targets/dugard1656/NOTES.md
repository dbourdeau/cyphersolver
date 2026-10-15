# Du Gard to White, Brussels, 10 June 1656 (Thurloe State Papers v.78-79)

Attempted, not solved: a 27-token cover address in figures and letters; too short, no key fits.

Split on 14 Oct 2026 from `thurloe` under the one-key rule (George Lasry, 14 Oct 2026). Until then this piece was filed
with three other intercepts printed in Birch's *Thurloe State Papers* (cryptiana unsolved item #9) because they share
the printed source; each is in its own cipher. The others, each a different cipher with its own page:
[`targets/thurloe/`](../thurloe/NOTES.md) (Beverning 1653), [`targets/copinger1656/`](../copinger1656/NOTES.md)
(Brussels to Copinger, 12 Aug 1656), [`targets/waddall1656/`](../waddall1656/NOTES.md) (Waddall to "Vanyeare",
22 Aug 1656). The work below was done in the thurloe session of 15 Sept 2026 and is carried over from its NOTES; the
ciphertext file moved here on 14 Oct 2026. The shared scripts (`analyze.py`, `apply_keys.py`, the harvested keys) stay
in `targets/thurloe/`.

Work date: 2026-09-15.

## The document

- Thurloe State Papers (Birch 1742) vol. 5 pp. 78-79, "An intercepted letter of du Gard in a letter to White",
  Brussels, 10 June 1656 [N.S.]; MS Bodleian Rawlinson A vol. xxxviii p. 769 (not digitised). Birch prints the clear
  text in English translation from the French. Full text on British History Online (vol5/pp72-83); page image in the
  Internet Archive scan `collectionofstat05thur`, leaf n84 (p. 79).
- The writer thanks White for his letters (one brought by the footman of monsieur de Barrière, Condé's agent in
  London) and suspects others were intercepted. Then: "The enclosed paper is a new direction to write to me by the
  way" and the cipher, which is therefore a cover address.
- White is probably one of the White brothers (Richard, Ignatius, Andrew; cryptiana `thurloe.htm`, Richard White
  section). Du Gard is not identified.

## Transcription

`b_dugard_1656.txt`: two lines, `18, 15, 4, 20, 87, q, t, 20, y, 1.` and `12, m, 17, 24, 15, 8, 15, 17, f, 20, 18, 15,
9, 7, 6, 13, 20.` Figures with the letters q t y m f mixed in. Measured (`--skip '^(?!\d)'`): 27 tokens, 19 distinct.

## What was tried (15 Sept 2026)

- **Key matching** (`targets/thurloe/apply_keys.py`, output `apply_keys_out.txt`): every 1653-60 royalist and
  Commonwealth key on cryptiana (Marshall 1656-58, Barwick-Hyde 1659-60, Stamford 1655, Butler 1656, Charles II
  intercepted 1655, Kingston 1658, Westrope 1655, Hague agent/Blake) applied and scored by an English quadgram model.
  Nothing readable; the best gave strings like "edaewQTeYa" (Marshall).
- No statistical attack: 27 tokens of an address cannot carry one.

## Remaining gaps
- The cover address (27 tokens) - blocker: too-short; a name and place in a cipher of figures and letters, no key online; the Bruges/Brussels royalist ciphers of 1656 would be in the Clarendon MSS, not online

## Escalation
- [n/a] siblings: the original is in Bodleian Rawlinson A vol. xxxviii (not digitised); the sibling route (the Bruges court agents' ciphers of 1656, with White) would be the Clarendon MSS, not online
- [n/a] clear-pages: no images of the original, only Birch's 1742 print
- [x] known-keys: every 1653-60 key on cryptiana applied (apply_keys.py): none fits
- [x] print: Birch's TSP and cryptiana (Tomokiyo lists it as undeciphered) checked
- [n/a] key-rebuild: 27 tokens of an address are below any statistical attack
- [n/a] retry: nothing reads, so nothing to regrade
