# Key v6b: a proposal for the sign "2" (pandolfini1514 and pandolfini1515)

Proposed on 19 Nov 2026 by Brice Dudout (L'Europe chiffrée), with Claude Opus 5.5 agents.

**Level: AI decipherment, human-checked on a sample of signs.** The keys v4 and v6 were derived after the only measurement and
were never measured. This proposal is not measured either. `key_v6.json` stays the key of record, unchanged
(sha256 a2f1c942...). The proposal is the separate file `key_v6b_proposal.json`.

## The change

In v6 the sign transcribed `2` reads c + vowel (`2^1` cu ... `2^5` ca). b is read only "by sense", as an alternative that
is not applied (bona, dubio, buon, bianca, bande...). On the images there are two shapes:

| shape | v6 | v6b |
|---|---|---|
| looped ʒ: the base runs down under the line in a curve, hook or loop; a long base running under the next sign also counts | c + vowel | **c + vowel** (unchanged) |
| flat 2: a small 2 whose short base sits on the line | c (b by sense) | **b + vowel** |
| bare 2 (no superscript) | o | **o**: its shape is ʒ (sheet X2) |

The machine rule "2^5 before y 3... = ba" (bande) is no longer needed: bande is written with a flat 2.

The transcriptions (`transcription_3xx.txt` here, and WAINUT's `transcription_666.txt`) write `2` for both shapes, so the rule
is applied occurrence by occurrence. The shapes are listed in `sign2_forms.tsv` here (193 occurrences in 307-333) and in
`../pandolfini1515/sign2_forms.tsv` (70 in 666).

## Evidence

1. **AI survey of every 2**: 263 occurrences on the ASF images. The criterion was written and hashed before the survey. There
   was one pass, with the shape noted before the expected value was joined.
   - It is not blind (the AI knew the readings) and has one observer.
   - Result: 152 ʒ, 45 flat, 66 doubtful.
   - 25 of 26 b-words were seen flat. 136 c-words were seen ʒ and 12 flat (all at medium confidence).
2. **Blind sheets checked by Brice Dudout**. Each sheet shows the boxed sign with reference shapes cut from the same letters,
   and no value or gloss. The sheets were prepared by AI agents; the choices are his alone.

| sheet | controls | targets | result |
|---|---|---|---|
| X2 (666) | 2/2 | 4 c-words + the bare 2 of "quatro o" | 4/4 ʒ; bare 2 ʒ |
| x3 (311, 322, 666) | 2/2 | 9 c-words the AI found doubtful (long straight base) | 9/9 ʒ |
| x4 (307-333, 666) | 2/2 | the 12 c-words the AI saw flat; bande (AI: ʒ); dubio, subito, bona | 11/12 ʒ; bande, dubio, subito, bona: 4/4 flat |
| X (666), not counted (one control wrong) | 1/2 | 5 b-words | 5/5 flat (indicative only) |

On the sheets that count, c-words were seen ʒ 24 times in 25, and b-words flat 4 times in 4.
- **Exception**: ricercare (311 A7, `2^5`) is a c-word written with a flat 2. It was already probable ({ricercare}), so no word
  is lost. It may be a slip of the cipher clerk.
- On x4, costì (333 L2) was answered "other shape: Z". It is taken as ʒ.
- The x3 sheet showed that the AI's "flat" class was too wide: a long base lying on the line is a ʒ to the human eye.

The sheets, rules and answers are not in the repository. No image or derivative is included (ASF images, study only).

## Recount with v6b (rule of #728: certain alone, and certain + probable)

Measured on our copy: the readings in this repository are not changed by v6b. A probable word {b...} whose 2 is flat becomes
certain. A c-word confirmed ʒ stays certain. Doubtful shapes keep the v6 value.

| letter | certain / probable / restored / unresolved (v6 -> v6b) | read by sense | certain alone (v6 -> v6b) |
|---|---|---|---|
| 666 (pandolfini1515; our count, 817 units) | 607/165/15/27 -> 613/159/15/27 | 94.5% | 74.3% -> 75.0% |
| 310 (3 words per unresolved group, 1,061) | 703/109/0/83 -> 707/105/0/83 | 76.5% | 66.3% -> 66.6% |
| 307 (291) | 205/57/0/29 -> 208/54/0/29 | 90.0% | 70.4% -> 71.5% |
| 309 (83) | 59/16/0/8, unchanged | 90.4% | 71.1% |
| 311 (533) | 424/42/1/66 -> 426/40/1/66 | 87.4% | 79.5% -> 79.9% |
| 322 (168) | 80/49/0/39 -> 81/48/0/39 | 76.8% | 47.6% -> 48.2% |
| 333 (29) | 28/1/0/0, unchanged | 100% | 96.6% |

The words that become certain are:
- 666: Bufaloro ×2, borgo, bastardo, bon, Binasco;
- 310: dubitatione, bona, bonissimo, dubitare;
- 307: buon, bon, dubio;
- 311: bono, bona;
- 322: ambasciadore.

The share read by sense does not change anywhere: v6b turns probable words into certain ones and adds no word read.
**Both targets stay "read in part".**
The 310 figures already include the four S -> 5 and two J? / J -> J# corrections of `transcription_310.txt` (sheet W, 18 Nov 2026); recounted 19 Nov 2026 from the marks of `reading_310.md` (895 units, 703/109/0/83).
