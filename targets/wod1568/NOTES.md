# John Wood to Cecil, 6 September 1568: the cipher line on BL Add MS 4136 f. 33 (DECODE R2989; catalogue 97)

Attempted, not solved: closed unread on 21 Sept 2026 (39 symbols, no unique solution; the true crib is at Hatfield).
Write-up docs/wod1568.html.

Split on 14 Oct 2026 under the one-key rule (George Lasry, 14 Oct 2026): one entry per key. This folder held catalogue
entry 97 ("Unknown sender (Paris) to unknown recipient, 10 Jul – 8 Aug 1559"), the two items Tomokiyo lists as
unsolved on cryptiana `unsolved.htm` (Nicholas Throckmorton 1559 / John Wod 1568), together with Throckmorton's own
letter of 10 July 1559 on the same leaves. Three systems: it now keeps **John Wood's line** only. Throckmorton's 10 July
1559 letter in his Cipher 1 is a different cipher, with its own page ([`targets/throck1559/`](../throck1559/),
docs/throck1559.html), and so is the marginal word-sign code on f. 32
([`targets/throck1559margin/`](../throck1559margin/), docs/throck1559margin.html). The images (`img/`, git-ignored)
and Bain's OCR (`bain2.txt`, git-ignored) stay here, in the main checkout `targets/wod1568/`.

| record | leaf | the cipher here |
|---|---|---|
| R2989 | f. 33 (old 10), Throckmorton to Cecil, Paris, 8 Aug 1559 (read by Tomokiyo, Cipher 3; Forbes p. 195) | one line at the foot, docketed in the left margin "Mr John Wod to Secretary Cecil, 6 Sept 1568", with a traced signature "M. Jhone Wod" |

Images: `img/` (DECODE, git-ignored). Downloaded with the bordeaux cookie 2026-09-21.

## R2989: John Wood to Cecil, 6 September 1568

Transcription (`wood_line.txt`, my labels; 3x zoom on `IMG_R2989_I20715_P.jpg`):

    g x ob r3 Z pm x x x2 f x2 Z g D x2 e XX 3 · x zl x ob x3 x2 x x2 Z zl o d pm g x ob /  (J) o · Z D x2 zl

`x` plain saltire; `x2` saltire with a hooked stroke; `x3` inverted-v form; `ob` o with a flat bar; `r3` a reversed
curly 3; `Z` long-tailed ʒ; `3` a short numeral 3 followed by a point; `zl` z with a vertical (L over z);
`pm` a plus-minus sign; `D` triangle; `XX` a blotted x with a dotted x written above it. 34 signs on the main line
and 5 after the marker `(J)`, which may be an insertion or a separate item.

**Same family as the Moray→Wood cipher.** The symbol families (x with variants, ʒ/z with variants, g, o, e, f)
match Tomokiyo's transcription of Moray to Wood, 13 July 1568 (`../moray/`, unread after one session). Wood
was Moray's agent in London that summer, so this is very likely the same Scottish cipher, and a second sample
of it. Tomokiyo's labels cannot be aligned glyph-for-glyph without his image (`stewart.jpg`, 404), so the two
texts could not be pooled.

**Crib from Bain.** Bain, *Calendar of Scottish Papers* ii no. 804 (Wood to Cecil, Edinburgh, 6 Sept 1568,
Cecil Papers, holograph) prints one passage with the footnote "These words are in cipher": *"and says he must
neidis haif it be on meinis or uthir."* (42 letters). Tested against the line (`align3.py`, `align4.py`):
exhaustive alignment with each sign = one letter, a null, or a fixed string of up to 4 letters (up to 6 nulls and
12 multi-letter signs), with and without the `(J)` group, with *says/sayis*, forwards and reversed, and every
substring of the phrase of 8+ letters: **no consistent alignment**. The line opens and closes with the same
trigram `g x ob`, which the phrase cannot produce. Either the Add MS 4136 line is a different ciphered passage
of the letter (the copyist may have taken the last one; Bain's final sentence, with its garbled "sennwngist"
footnoted "Sinews", is a candidate), or Bain's footnote marks words that the original shows deciphered in a
form the copy does not reproduce. 39 signs is far below what a ciphertext-only attack on a ~30-sign homophonic
alphabet needs.

- HMC Salisbury (Hatfield) calendar vol. 1 (archive.org calendarmanuscr01giusgoog), checked 2026-09-21: no entry
  for Wood's letter of 6 Sept 1568 (Sept 1568 runs 1185-1187 with nothing from Wood). Bain ii 804 remains the
  only print, so no further crib exists in print for the Wood line.

**Non-uniqueness test (`nonunique.py`).** The 39 signs (16 distinct) were annealed with 200 random restarts
against a quadgram model of Bain ii, where each sign is one letter (homophones allowed). 185 of the 200 end
states score above the median of real 39-letter windows of Bain (−338), the best at −290, and 92 of them differ
from each other in more than a third of their letters. All the top solutions are gibberish (e.g.
"stereatththestherstateth…"). The model overfits: the line admits dozens of unrelated "English" readings that
fit better than real text. That makes the line undetermined, not just hard; ciphertext-only it cannot be read.
It can be read only with an external crib (the Hatfield original).

**Conclusion (2026-09-21): closed unread.** Shown to have no unique solution.

## Route in

1. The original Wood letter of 6 Sept 1568 in the Cecil Papers at Hatfield (Bain's "C.P., vol. I"). It should show
   where the cipher sits and whether it was deciphered, giving a true crib for the line and a second text for the
   Moray cipher.
2. Tomokiyo's image or glyph table for Add MS 32091 f. 213, to merge the Moray and Wood texts under one labelling.

## Files

`rec2989.htm` (DECODE record page) · `wood_line.txt` · `align*.py` (crib alignment) · `nonunique.py` ·
`bain2.txt` (Bain ii OCR, not committed) · `img/` (not committed).

## Log

- 2026-09-21: transcription, Bain crib alignment, HMC Salisbury check, non-uniqueness test; closed unread.
- 2026-10-14: split; the 10 July 1559 letter files moved to `../throck1559/`, the margin files to `../throck1559margin/`.

## Remaining gaps

- f. 33 John Wood line, 39 signs - blocker: too-short; no unique solution (nonunique.py); needs Hatfield, Cecil Papers vol. 1

## Escalation

- [x] siblings: Add MS 4136 key leaves ff. 173-185 (R9258-R9262) and the twenty targets/throckmorton/ records checked; no key for this cipher
- [x] clear-pages: no decipherment on the leaf; the Forbes copies have none for this line
- [x] known-keys: Tomokiyo Ciphers 1-3, Smith 1563, Cecil-Norris and Moray-Wood tried against the line
- [x] print: Bain II no. 804, HMC Salisbury I checked
- [x] key-rebuild: crib alignment (align3.py, align4.py) and identifiability test (nonunique.py)
- [n/a] retry: nothing reads, so there is no extended key to retry with
