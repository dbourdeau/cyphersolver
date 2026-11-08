# The second reading

The notebook was transcribed twice. The first transcription (`data/transcription/` in this
repository) was made by Anthropic Claude. The second was made by a different reader that was given
nothing but the page images — no key, no values, and no sight of the first transcription.

## What the second reader was given

Every run received one page image at a time (the full-size image, 2,800–3,900 px on the long side)
and the same instruction sheet. The sheet describes the letter shapes of this hand (the digit 1 is a
short slanted stroke that can look like a small s; 9 has a descender like g; 2 can look like z; 4 is
open at the top; the long ſ is a tall letter with a descender). **It carries no key, no values and no
part of the first reading.** The reader was told to use only the image it was given and to open no
other file.

## The runs

| Run | Reader | Images | Role |
|---|---|---|---|
| R1 | OpenAI Codex CLI (gpt-6-astra, reasoning high) | 36 | comparison (below) |
| R2 | same | 17 (stopped by a usage limit) | comparison (below) |
| S2 | Anthropic Claude Sonnet | 36 | **independent second reading, reader A** |
| R3 | OpenAI Codex CLI (gpt-6-astra, reasoning high) | 35 (image 70 lost to a usage limit) | **independent second reading, reader B** |
| C2 | Anthropic Claude Sonnet | image 70 only | **second reading of image 70, with the column rule** |
| C3 | Anthropic Claude Fable | image 70 only | the same |
| C1 | OpenAI Codex CLI (gpt-6-astra, reasoning high) | image 70 only | the same (taken later, once the R3 limit had lifted) |

Two second readings were taken against the corrected transcription, by readers from different
families (S2 and R3). Both sets of figures are given below; the lowest is the one the judgement
rests on.

## R1 and R2 are a comparison record, not the independent second reading

R1 and R2 were set against the first transcription, and where they disagreed, **seven words were
corrected after checking the letter shapes in the full-size image** (`data/verified.tsv`):

| Image | Before | After | What the image showed |
|---|---|---|---|
| 21 | `44`, four places | `t4` | the same shape as `t4` elsewhere on the page; reads "to" |
| 21 | `w3thg5t` | `w3th45t` | the same 4 as in `45t` (out) on the same line; reads "without" |
| 40 | `p2;t29` | `p22t29` | "oyle of peeter" (saltpetre) |
| 45 | `F2y2tary` | `F272tary` | the third letter is 7, shaped unlike the final y; "femetary" (fumitory) |
| 66 | `d3ss46;2`, `d3s46;2d` | `d3ſ4652`, `d3ſ4652d` | "disolue" / "disolued" |

**Once the first reading has been corrected in the light of a comparison, that comparison is no
longer independent.** R1 and R2 are therefore kept only as a record of agreement, and fresh runs
(S2 and R3) were made against the corrected reading and used as the independent second reading.

Agreement of R1 and R2 with the reading as it stood before those corrections (compared on decoded
values, per page, by edit distance):

| Run | Images | Characters in reading 1 | Matched | Share |
|---|---|---|---|---|
| R1 | 36 | 12,468 | 11,278 | 90.5% |
| R1, excluding lines covered by a pasted slip | 36 | 12,343 | 11,262 | 91.2% |
| R2 | 17 | 5,812 | 5,300 | 91.2% |
| R1 against R2 | 17 | — | — | 95.3% |

R2 covers only 17 images because the Codex runs hit a usage limit ("try again at 5:25 PM").

## Independent second reading, reader A (S2, Claude Sonnet)

Anthropic Claude Sonnet read all 36 images against the corrected transcription (its transcriptions
are in `../second/sonnet/`, the instruction sheet it was given in `../second/PROMPT.md`). It was run four
times, each run given only the images it was to read. The run logs were examined afterwards and
**no run opened the first transcription, the key, the word lists or the Codex output.**

| Scope | Characters in reading 1 | Matched | Share |
|---|---|---|---|
| All 36 images | 12,465 | 11,249 | **90.2%** |
| The 35 images whose reading is published (image 70 excluded) | 12,201 | 11,073 | **90.8%** |
| Lines covered by a pasted slip excluded (36 images) | 12,340 | 11,140 | 90.3% |

Per image the range is 66.7% (image 70 — see "Measuring a page laid out in columns" below) to 98.0%
(image 56); setting image 70 aside, the lowest is 76.8% (image 51).

### The pages that agree least

- **Image 70: see "Measuring a page laid out in columns" below.** Under the first instruction sheet
  it came to 66.7%, but the gap was not a disagreement about letters — it was a disagreement about
  which way to walk the columns. With one line added to the sheet, the same models give 87.5% and
  89.0%, and the reading is published.
- **Image 31 (69.9%): its reading is published.** This page carries a note written vertically in the
  left margin. The first transcription puts it last, the second puts it first. **That is a
  difference of placement, not of reading**: align the marginal block and the same comparison gives
  90.9%. Both figures are given here.
- Setting image 70 aside, the next lowest are image 51 (76.8%), 53 (79.1%) and 54 (86.1%), all pages heavy with struck-through
  lines and ink bleed. Their readings are published; the symbols that remain doubtful are listed in
  `OPEN.en.md`.

### The part that was redone

In the first attempt at S2, 18 of the 36 images were handed to a single reader. That reader lost
sight of the images part-way through (of 234 image reads, 79 came back with the image dropped) and
said in its own report that it had written from guesswork. **Those 18 were discarded** and redone
with each image opened exactly once. In the two runs that redid them, images were dropped only four
times, each after the transcription was already written, and both readers reported that no page had
been unreadable.

## Independent second reading, reader B (R3, Codex)

The same instruction sheet and the same delivery (one page image per call) were given to the OpenAI
Codex CLI for the same 36 images (its transcriptions are in `../second/codex/`). Image 70 was lost
to a Codex usage limit ("try again at 10:33 PM"), so **the 35 images it did return are exactly the
35 whose reading is published.** Image 70 was taken afterwards, once the limit had lifted, under the
same delivery and the instruction sheet with the column rule added (C1, below). The runs were made
in a read-only ephemeral sandbox, and the run
logs were examined: no run used a shell (`command_execution`, 0 occurrences).

| Scope | Characters in reading 1 | Matched | Share |
|---|---|---|---|
| The 35 images returned (= the 35 published) | 12,201 | 11,137 | **91.3%** |
| Lines covered by a pasted slip excluded (same 35) | 12,076 | 11,120 | 92.1% |

Per image the range is 41.5% (image 25) to 99.0% (image 57). **The 41.5% on image 25 is not a
disagreement about reading.** The upper half of that page is covered by a pasted slip, and Codex
wrote out only the five lines below the slip, leaving the fragments around it untranscribed. With
the slip-covered lines excluded, image 25 gives 74.6% and the lowest page becomes image 27 at 70.6%.

### The two readers side by side

| | Claude Sonnet | OpenAI Codex |
|---|---|---|
| The 35 images other than 70 | 90.8% | 91.3% |
| Slip-covered lines excluded | 90.3% (36 images) | 92.1% (35 images) |
| All 36 images (image 70 from the column-rule run) | **90.7%** | **91.3%** (11,379 of 12,465) |

**The figure the judgement rests on is the lowest of these, 90.7%.** For comparison, keeping image
70 at its first-sheet run instead gives 90.2% (11,249 of 12,465); either way the figure stays above 90%.

## Measuring a page laid out in columns (image 70)

Image 70 is not a recipe. It is a page of practice writing — names, strings of figures, a table of
single letters — set down **in two columns**. The first instruction sheet said only "one manuscript
line per output line, top to bottom", so one reader took the left column from top to bottom and
then moved to the right, while another read across the two. **Two readers can agree on every letter
and still score badly**, because the strings are then aligned in different orders. That, and not a
disagreement about letters, is what the 66.7% was.

One line was therefore added to the sheet (`../second/PROMPT_columns.md`) and the page was taken
again, **with the same models and the same image**:

> If the page is laid out in two or more columns side by side, do not read across them. Transcribe
> each column in full, top to bottom, beginning with the leftmost, and output a line containing
> only === between one column and the next.

The first transcription was reordered to the same convention. **Not one character was changed**: the
characters before and after were counted and compared — none added, and the only ones removed were
the five that made up a working note which had never been part of the manuscript.

| Reader | First sheet | With the column rule |
|---|---|---|
| Claude Sonnet | 66.7% | **87.5%** (`../second/columns/sonnet/f70.txt`) |
| Claude Fable | 62.1% | **89.0%** (`../second/columns/fable/f70.txt`) |
| OpenAI Codex | (lost to a usage limit) | **91.7%** (`../second/columns/codex/f70.txt`) |

Changing the model did not help under the first sheet (62.1%); changing one line of the sheet took
the same model to 89.0%. Under the sheet with the column rule, three readers of different lineage
cluster at 87.5%, 89.0% and 91.7%. The figure this page is judged on is the lowest of them, 87.5%.

The two runs made under the first sheet are recorded here but are not used for the judgement: their
disagreement is what prompted the reordering and the removal of the working note, so they are no
longer independent, exactly as R1 and R2 are not. The judgement rests on C2 and C3, taken after the
first reading was put right.

The defect those runs exposed — a working note written on one line of image 70 and counted as five
characters of transcription — was searched for across all 36 images; there is no other instance.

## How agreement is counted

Each page of both transcriptions is decoded with the key, reduced to its alphanumeric characters,
and the two strings are aligned by edit distance; the matched characters are divided by the length
of the first reading. Lines are not paired up beforehand. Because the comparison is on decoded
values, two names for one letter (9 and g, which the key sends to the same value) count as
agreement.

Every figure given here can be recomputed from the files in this repository:

```
python3 src/agreement.py second/sonnet      # 90.2% over 36 images (image 70 from the first sheet)
python3 src/agreement.py second/codex       # 91.3% over 35 images
python3 src/agreement.py second/columns/sonnet p70   # 87.5%, image 70 alone
python3 src/agreement.py second/columns/fable p70    # 89.0%, image 70 alone
python3 src/agreement.py second/columns/codex p70    # 91.7%, image 70 alone
```

The script prints both the figure that keeps the written order and the figure that ignores line
order. On ordinary pages the two are nearly the same; they part only where the page is laid out in
interleaving columns.

## What the disagreements are

The largest single class is not a disagreement about letters but about how to write them down. The
first transcription expands the superscript e as `ye`; the second writes `y` (82 places). The rest
are of the same kind: the period spellings `giue` and `fiue` written as `give` and `five`, the long
ſ written as s.

## Limits

**No human has checked this transcription.** Two AI readers agreeing on a letter does not make the
letter right. Letters that both can misread the same way — above all 9 against g, and 1 against the
long ſ — remain a real possibility. One of the two second readings (R3) comes from a reader built by
a different maker than the first, which makes a shared error inherited from the same training that
much less likely, but not impossible.
