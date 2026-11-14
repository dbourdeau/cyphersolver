# Fresh manuscript review, 18 September 2026

**Still not securely solved.** The visual evidence favours `?nau?is` over the
published `te a ? o i s` interpretation. *Knauis* remains a conjecture because
it does not account for all seven visible signs. The surrounding phrase now
has a linguistically supported, but cryptographically unproved, interpretation.

## Source and numbering

Re-examined original DECODE R8345 P4, both halves of all three long cipher
lines, L4, and the existing focus sheets. No generated or reconstructed image
was used. The authoritative token sequence for this review is the published
`moray-1568/transcription.txt`: line counts **46 / 43 / 38 / 7** = 134.
The old automated contact-sheet labels identify image components, not cipher
tokens: some components merge neighbouring signs. In particular, sheet
“3.24” is token **L3.26**, and sheet “4.3” includes tokens **L4.4–5**.
All positions below use actual token numbering.

## Visual comparison, before choosing words

| Position | Comparison elsewhere | Assessment |
|---|---|---|
| L4.1, large curled 3 | L3.3–4, the doubled sign in `la??is` | Same sign family; does not independently decide k versus t. |
| L4.2, curved x | Curved n-sign in *remane* (L1.17), *sending*, *freindis* (L3.35); angular e-sign in those same words | Visually favours **n**. Earlier x3=e is poorly supported. This is an allograph judgement, not a new plaintext witness. |
| L4.3, triangle | Numerous a-signs | Retain a. |
| L4.4, crossed/starred x | u-sign in *cummis* (L2.30) and *oure* (L3.28) | Visually favours **u**; cannot establish that the extra strokes cancel an e instead. |
| L4.5, z with long descending-left stroke | o-signs in *of* (L1.40) and *to* (L3.14), which have short upward-left stems; slashed y in *haym* (L1.38) | Do not treat the equality with ordinary Z2=o as certain. Distinct stroke geometry, but no independently known value. |
| L4.6–7 | i/s signs in *freindis*, *cummis*, etc. | Retain is. |
| L3.25–26 | Angular e-sign followed by a unique t-shaped sign | e is supported; the second value is not. Its resemblance to a literal t never established plaintext t. |

L4.4–5 have two recognisable sign bodies. The long stroke does not clearly
strike through either body. Combining them into one compound w-symbol, or
declaring either cancelled/null, is possible but **not demonstrated**.
There is no clearly exceptional internal word gap that resolves this.

## An actual flaw in the earlier corpus evidence

Rechecking the original OCR contexts gives eight standalone `lattis` tokens
across the local corpus and eight downloaded OCR volumes (a ninth download was an HTTP error page). **Six are broken forms
of *prelattis*, “prelates”**, split at a line-end hyphen (including OCR
*Prc-* and *Pro-*). Only two are genuine verb uses, both in “lets … know.”
The previous “eight attestations versus zero” argument should be withdrawn.
The eight saved contexts and source hashes are in `review-evidence.json`;
`fresh_review.py` recounts those contexts and reproduces `fresh-review-results.json`.

This does not disprove *lattis*: [DOST Lat v.2](https://dsl.ac.uk/entry/dost/lat_v_2)
independently attests it. [DOST Lak v.](https://dsl.ac.uk/entry/dost/lak_v)
also independently attests *lakkis*. The dictionary evidence, rather than raw
OCR counts, leaves both alternatives open.

## Surrounding phrase and boundaries

[DOST As](https://dsl.ac.uk/entry/dost/as_adv_conj) explicitly lists **es** as
a spelling of *as*. Consequently `haill e? oure freindis` could be:

> haill es oure freindis …

This requires assigning the singleton t-shaped sign at L3.26 the value **s**.
It retains the securely read e. It is a linguistic conjecture, not an
independent decipherment of that sign.

There is another possible division: `haille [as] oure freindis`, treating
L3.26 as a word-sign. [DOST Hale](https://www.dsl.ac.uk/entry/dost/hale_adj_n)
lists *haille*. This alternative has no independent key evidence either;
it shows why spacing alone cannot fix the singleton.

With *lakkis*, *es*, and conjectural *knauis*, the sentence would mean:

> If [the Queen] comes home, nothing more is needed to ruin the whole,
> as our friends know.

Queen identification, normalisation of literal *haom* to “home,” singleton
values, and the treatment of the extra final sign remain explicit assumptions.
[DOST Knaw](https://dsl.ac.uk/entry/dost21033) attests *knauis*, but does not
establish that this manuscript says it.

All 64 boundary patterns were checked for each strict reading `knauois` and
`tnauois` using the local corpus. Raw OCR produces artificial partitions such
as `kna uois`: inspected contexts show truncated *kna…* and French `j a uois`.
No satisfactory multiword reading emerged. The raw hits are retained; this is
not proof that no historical reading exists.

## What remains necessary to make the conjecture a decipherment

Under the visually preferred n/u assignments and contextual k, keeping the
fifth sign as o yields **knauois**, not *knauis*. Omitting it yields *knauis*;
omitting the fourth sign and assigning the fifth w yields *knawis*. A compound
w or a uu spelling is another unverified possibility. None is established
by repetition or an identifiable correction mark. No matching historical
attestation of *knauois* was located in this bounded check.

The defensible outcome is a clearer conjectural sentence and corrections to
the evidence, **not a completed solution**. Published key values and transcription are preserved as the baseline; key
annotations now flag the withdrawn evidence and visual alternatives. Do not promote the t-shaped singleton to s, or the final sign to
null, merely because this makes a fluent sentence.

Reproduce the saved-context counts, boundary enumeration and conditional literal outputs
with `python3 moray-1568/fresh_review.py` from the repository root. This checks
the evidence snapshot, not an independent rescan of the full corpus. Supply
`--corpus-dir PATH` to repeat the full scan against the original local corpus
layout (`scots_corpus.txt` and `lexicon/*.txt`); source hashes must match.
The snapshot includes counts of every substring relevant to these boundary
tests, including zero counts. Raw OCR hits are not validated dictionary words.
The archived first audit in `LAST-WORD-AUDIT.md` predates the *es* finding here.
