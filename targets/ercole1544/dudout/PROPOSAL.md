# Proposal for `targets/ercole1544` (cc. 78r-79r and 174r-175v), shape plate of 25 Nov 2026

For LcCompany / WAINUT (folder authors, PR #221), copy Daniel Bourdeau. Sent with Brice Dudout's agreement.

## Credit

The transcription, the table, the decryption and the reading are LcCompany/WAINUT's work. This proposal starts from
their files as they stand on cyphersolver `main` (unchanged from b13dd55072 to db211162a9) and changes signs only. The
working key `key.tsv` and the scripts are unchanged. Whether to take, change or decline any of it is the owners' choice.

## What was done

The folder's NOTES list places "Not settled on the image" in the two letters. Ten target signs among them were put on
a blind shape plate, answered by a human reader (Brice Dudout, 25 Nov 2026). Each question showed the line, the boxed
sign and real examples of each candidate shape, taken from sure places of the same hand, with no value or decoded text
shown. Three hidden controls of known answer were mixed in (a 3 in `30`, a b in `q b h`, an x in `h x a r`): 3 of 3
right. The selection rule and the integration rule were written and hashed before the plate was built (initial
SHA-256 762d8bf4…6959); one amendment, made after a contact sheet and before any answer, only re-cropped boxes (final
SHA-256 1421ffe3…cf22). The plate was built and scored by AI agents (Claude). Excluded from the plate: A03 (blot over
several signs), B03 (place not designated), the other unsettled signs of F08 (not located), the S/y g ligature at G06.

Images: Biblioteca Estense IIIF, 1900 px, CC BY-NC-SA, used for study only. No image, crop or derivative is included.

## Answers and changes (by shape; sense was not used to choose)

| place | question | answer | change |
|---|---|---|---|
| A05 `f n s ? e x` | 3 / g / z | **3** (digit) | `g` -> `3`. A lone 3 is not in the table: open code `[#3]`. The reading keeps `[...]` there |
| B01 `n x ? g x` | b / h | **h** | none: confirms "aiuti"; reserve lifted |
| B02 sign under the blot | r / n | **n** | `r` -> `n`: `y g e b f n 31` gives "dall'altro sa io", which does not read; `[?Se]` kept as a proposal from sense |
| B21 end, 3rd sign | a / n | **n** | `h x a b` -> `h ? n b`; the passage stays `[...]` |
| B21 end, 2nd sign | n / a / x | none of these | left `?` (see below) |
| C07 `q x 5 ?` | 9 / 7 / z | not counted | plate defect (see below); `59` kept, still not settled by shape. The answer was not 7 |
| E21 `a g r e ? r a r` | z / g | **g** | `z` -> `g`: "intertener" is now verbatim; the repair `intertener°` goes |
| F03 `t e n g x S x ? r` | z / g / q | **q** | `z` -> `q`: the signs give "gratissi**d**e"; "gratissime" becomes the repair `gratissime°` (value from sense only, so probable) |
| F08 `2?` after `s n e x e r` | q / 4 | **q** | `24` (null) -> `2 q`: "fari re [#2] drito"; new open code `[#2]`; the passage stays `[...]` |
| G06 `y 27 n ? n f` | z / g | **z** | none: confirms z |

So this settles seven of the places and one of the two open signs at B21. Two open codes are added, `[#3]` at A05 and
`[#2]` at F08.

**G06, "masca".** With z confirmed, the signs give "si cavara la **masca**" (would take off the mask), against the
repair `tasca°`. It may deserve a look; the patch keeps `tasca°` as it is.

**B21, 2nd sign.** The answer was "none / other shape", with the remark "r? or mis-framed?". On zooms the sign is
neither an r nor mis-framed: a caret-shaped sign with a thin left leg and a hooked foot, close to a. Left `?`.

## Plate defects, stated so they are not over-read

- **C07 (question not counted).** The example of the digit 9 and the example of z show the same sign in this hand (the
  "tailed 9" z), as the reader remarked ("forme 1 et 3 sont les mêmes ?"). The question decides nothing; `59` stays.
- **Control x/a/n (kept).** One example of the decoy a was framed about 5 px to the left and held the arm of the x
  (reader's remark: "forme 2 : mal cadrée ???"). The control was answered right, and it is kept as a valid control.

## Count (your `scripts/count_words.py`, unchanged)

Unchanged: cc. 78r-79r plain 718, no hole 385, clean 184, verbatim 148, repairs 3; cc. 174r-175v plain 1240, no hole
697, clean 260, verbatim 216, repairs 15. One word moves each way: "intertener" from repaired to verbatim,
"gratissime" from verbatim to repaired. No other word of the reading changes. This is a correction of the signs, not
a gain in reading; the status stays "read in part". Details in `RECOMPTE.md`.

Checks on the patched copy: `scripts/decode.py` with `key.tsv` regenerates both decryptions as in the patch (up to
CRLF line ends); `scripts/check_repairs.py` passes (0 unmarked differences); `check_repairs.py --table` regenerates
both `editorial_*.md` as in the patch.

## Files changed by the patch

`transcription_0078_0079.txt` (A05 `g`->`3`; B02 `r`->`n`; B21 end `x a`->`? n`), `transcription_0174_0175.txt` (E21
`z`->`g`; F03 `z`->`q`; F08 `24`->`2 q`), the two decryptions (regenerated), `reading_0174_0175.md`
(`intertener°`->`intertener`; `gratissime`->`gratissime°`) and `editorial_0174_0175.md` (regenerated).

Not in the patch, for the owners if they take it: NOTES.md "Not settled on the image" (strike B01, E21, F03, F08 now
`2 q`, G06; A05 and B02 decided by shape but not read; B21 2nd sign and C07 open), and a line per change in
`sign_changes.tsv`.

Shape check: Brice Dudout (blind plate, 25 Nov 2026), with Claude Opus 5.5. Transcription, table and reading:
LcCompany/WAINUT.
