# The marginal word-sign code on Throckmorton's leaf of 10 July 1559, BL Add MS 4136 f. 32 (DECODE R2988; catalogue 97)

Attempted, not solved: closed unread on 21 Sept 2026 (a word-sign code with half its tokens used once; no key or
verbatim crib). Write-up docs/throck1559margin.html.

Split on 14 Oct 2026 from `wod1568` under the one-key rule (George Lasry, 14 Oct 2026): one entry per key. The old entry
(catalogue 97) joined three systems on the leaves Add MS 4136 ff. 32–33. This folder keeps **the marginal text on
f. 32**, one of the two items Tomokiyo lists as unidentified (cryptiana `unsolved.htm`). Throckmorton's own letter on
the same leaf, in his Cipher 1, is a different cipher, with its own page ([`targets/throck1559/`](../throck1559/),
docs/throck1559.html), and so is John Wood's 1568 line on f. 33 ([`targets/wod1568/`](../wod1568/), docs/wod1568.html).
Shared material: the DECODE record page `../throck1559/rec2988.htm`; the images (`img/`, git-ignored) and Bain's OCR
(`bain2.txt`, used by `margin_stats.py`) stay in the main checkout `targets/wod1568/`.

## The margin

About 300 cursive signs in 12 lines (first estimate; the transcription counts about 405): strokes, hooks and loops
with points and superscript points, word-like clusters separated by spaces, `/` and `//`; a boxed group (read upright
something like `ʃro` with superscript points, once as `rel ʃro`) occurs several times; the clear year `1559` appears
in the date line. Mirroring and inverting the image do not give Latin script.

**A separate dated text.** It runs 10 lines under the letter, ends with a date line `ɥɾᵹ 8 ⅃.. 1559 / … //`, then a
3-line `*` block keyed to the star after "…" on main line 13 of the letter. The letter says Throckmorton wrote on "the
eight of this month" (by Gray, and again at midnight by Carew). So the margin is most likely his copy or abstract of
the **8 July** despatch, sent a second time with the 10 July letter. The printed abstracts are CSP For. i nos. 947
(to the Queen, on Lord Grey's ransom and Rochefoucauld) and 950 (to the Council; "portions in cipher, deciphered":
the French King's fever, d'Elbeuf and la Brosse for Scotland, galleys, Ruy Gomez, the Earl of Arran at Geneva, Anne
du Bourg). The boxed group is then probably a name; Lord Grey is the best candidate.

**System (line 1 at 4x).** The signs are small letter-like forms (o, θ, ϑ, ı, √, ɥ, 7, 6) that change value with
point position: points above, right, doubled (`o··`, `θ·`, `ɥ:`), and superscript letters. Groups are 1-4 signs
separated by spaces, with `/` and `//` as clause marks. This is the pattern of the dotted-letter word codes of the
period (Thomas Smith's 1563 cipher: "a letter with one or two dots to the left, right, above or below" stands for a
word beginning with that letter; the Cecil-Norris table also works this way).

**Transcribed and measured (`margin_transcription.txt`, first pass).** About 405 signs in 217 groups. There
are about 29 base shapes (22 occur 4 or more times) and about 80 shape+dot combinations. Mean group length is 1.87
(1 sign: 106 groups, 2: 60, 3: 30, 4: 14, 5: 5, 6: 2). One boxed group, `[y+r u']`, occurs 4 times (M00, M03, M04,
M06); `z+e+l'` occurs twice. English spelled letter by letter would give a mean word length of about 4.3, with
single-letter words under 5% of the total; here half the groups are one sign. So this is not a letter cipher.

**Identifiability test (`margin_stats.py`).** The groups match English words, not letters: 222 group tokens,
141 types, 113 hapaxes. 222-word windows of Bain give a median of 140 types and 107 hapaxes. So each group is
a word sign (a word code or shorthand), and 113 of 222 tokens (51%) are signs that occur only once. A sign seen
once has no internal evidence for its value. Without a key or a verbatim crib, at most the 109 tokens of repeated
signs (49%) can be pinned down ciphertext-only, and even those only up to guesses from context. **95% is
provably out of reach by any ciphertext-only method**. It needs the key or SP 70/5 (8 July 1559).

**Conclusion (2026-09-21): closed unread.**

## Route in

A clean high-resolution photograph of f. 32, and the R.O. originals SP 70/5 nos. 947/950 (TNA, State Papers Online)
with their deciphered cipher portions, aligned against a full margin transcription; or the code's key (not among the
Add MS 4136 key leaves ff. 173-185, R9258-R9262, which are Throckmorton's and Smith's letter ciphers).

## Log

- 2026-09-21: mirror/inversion test; first inventory attempt (failed); margin identified as a separate dated text;
  CSP Foreign checked; transcription and group statistics; identifiability test; closed unread.
- 2026-10-14: split from `wod1568`; `margin_transcription.txt` and `margin_stats.py` moved here.

## Remaining gaps

- f. 32 margin, ~405 signs in 222 groups - blocker: no-key-material; word-sign code, 113 of 141 types used once; needs its key or TNA SP 70/5 (CSP For. i 947, 950)

## Escalation

- [x] siblings: Add MS 4136 key leaves ff. 173-185 (R9258-R9262) and the twenty targets/throckmorton/ records checked; no word-code key
- [x] clear-pages: no decipherment on the leaf; the letter above it is Throckmorton's Cipher 1 text, not a gloss
- [x] known-keys: Tomokiyo Ciphers 1-3, Smith 1563, Cecil-Norris and Moray-Wood tried against the margin
- [x] print: Forbes I, CSP Foreign I (BHO) checked: abstracts of 8 July only
- [x] key-rebuild: identifiability test (margin_stats.py): no ciphertext-only route
- [n/a] retry: nothing reads, so there is no extended key to retry with
