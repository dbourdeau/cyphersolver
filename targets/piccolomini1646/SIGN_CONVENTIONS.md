# Sign conventions for 2358 (inv. 24874, 24876; control 24873)

Written before any value was applied to the bare frames. Shape names only; the values are in `key.tsv`.

The hand is one Italian chancery cursive. The cipher signs are ordinary letters and Arabic digits written in the
same cursive, so several digits look like letters of the same hand. The photographs are microfilm-screen photographs
(about 15-20 px per letter), so some fine distinctions cannot be seen. Where two shapes cannot be told apart on these
photographs, the transcription uses one class token, not a guess.

## Tokens

| token | shape |
|---|---|
| `1` | short minim with a dot above it (looks like a dotted i) |
| `3` | flat-topped three with a lower bowl, often with a short descender (like a z with a round belly) |
| `7` | seven: short top stroke and a long stroke descending to the left |
| `2` | small z-shape sitting on the line, no descender |
| `4` | four: open crossed stroke, the vertical runs below the line |
| `6` | six: bowl on the line with a stroke rising from it |
| `8` | figure eight, two stacked loops |
| `0` | small closed round loop sitting on the line, not joined (rare) |
| `S` | short s-shape with a flat or hooked top: in this hand the digit five and the short letter s are the same shape on these photographs (class token) |
| `5` | used by the solver where the s/5 shape was judged to be a five, without a written criterion; added to this table after the independent check, which found the rule unstated. The verifier wrote every such shape as `S`. Because the judgement is not secure at this resolution, the strict count in NOTES.md also gives the words with no `S`, `G` or `5` |
| `G` | closed bowl with a descender curving left: the digit nine, the letter g and the letter q have the same shape here (class token) |
| `f` | long s (tall, descends below the line) |
| `b c d h k l m n p r t v z` | the letter of that shape (z: a z with a descender loop, taller than `2`) |
| `x` | any other letter shape, written as itself |

## Marks in the transcription

- `?` after a token: the shape is doubtful at this resolution.
- `[?]` a sign that cannot be made out.
- `|` a line end inside a word is not marked; each frame line is one line of the file, `Lnn<TAB>` + space-separated words.
- Clear (uncoded) passages are not transcribed sign by sign; they are given in `NOTES.md` and the reading.

## Added after the independent check (6 Nov 2026)

The `5` row above. The first version of this file said that five and s are the same shape, while the transcriptions
and `key.tsv` also used a separate `5`; the verifier asked for the rule to be stated (VERIFY.md, fix 7). The
transcriptions were not re-tokenised: every `5` is the solver's judgement and is counted as such.

## Not used

No interlinear gloss exists on 24873, 24874 or 24876. Nothing between the lines was read into the sign copy.
