# Post-submission research update: Foix table confirmation and A16 source correction

**Lawrence Beck, with the assistance of ChatGPT**  
Photographs, earlier transcriptions and prior source research: **Daniel Bourdeau**  
Comparative reconstructed Foix key: **Satoshi Tomokiyo**

Research continuation after PR #18, 3 October 2026.  
Target: British Library Add MS 4136, ff.148v-149, DECODE R9241, four encrypted extracts copied under 15 January 1563.

## Why this update matters

PR #18 froze the v0.9 / source-key v13 partial decipherment for review. Since that submission, the project has had one major external-key development and one further manuscript-level source correction.

The important change is not simply that a few more French words have been guessed. We obtained Satoshi Tomokiyo's reconstructed **Paul de Foix cipher table from 1565 correspondence**, compared it directly with the 1563 target, and found substantial reuse of both the alphabet and the numerical/nomenclator vocabulary.

That table materially strengthens and corrects the earlier reconstruction. A later native-image audit then found that one sign near the end of extract A had itself been misclassified: it is another occurrence of the already established **faire** word sign.

The public PR baseline remains useful as a record of the earlier independent reconstruction. This document records what changed after it.

## 1. Major post-PR result: the supplied Foix table substantially matches the reconstructed key

After PR #18, the actual image `CharlesIX_Foix.png` was supplied. Tomokiyo attributes the reconstruction to de Foix correspondence of 11 October 1565, BnF Français 15971, ff.21 and 26.

The comparison supports **substantial key reuse**, rather than merely a similar sixteenth-century cipher design.

Several distinctive entries already present in the PR reconstruction agree with the supplied table:

| Entry | PR / target reading | Foix reference |
|---|---|---|
| 30 | `est` | `est` |
| 31 | `pour` | `pour` |
| 50 / so-like group | `que` | `que` |
| 83 | `le` | `le` |
| 84 | `la` | `la` |
| crossed-h word sign | `faire` | `faire` |
| barred-E-like sign | `et` | compatible `et` entry |
| V-shaped / word-sign family | `ont` | compatible `ont` entry |

Numerous ordinary letter homophones also line up graphically: triangle/chevron=a, b-like=e, X=f, crossed/double-stroked 4=g, m=n, curved d=o, p-like=r, among others.

This is not a claim that the 1563 and 1565 tables are identical in every entry. The supplied table is a modern reconstruction, some small forms are ambiguous, and several target values remain target-derived rather than reference-confirmed. But the agreement is too extensive and too specific to treat the earlier decipherment as a free-standing language fit.

### New or corrected table-supported values

Applying the reference table changed **11 key-value assignments at 30 recorded occurrences** and supplied proposed table-supported values for **16 previously unassigned observations**.

The most useful changes were:

| Target item | Earlier state | Post-table treatment |
|---|---|---|
| 26 | unresolved | **bien** |
| 34 | unresolved | **tant**, where the source grouping is genuinely 34 |
| 40 | unresolved | **faict** |
| 52-like group | `qui` | **quil / qu'il** |
| 10 | earlier `sieur` guess | reference places **dict?** here; `sieur` is under 39 |
| 70 | unresolved / `tout` candidate | reference gives **toute** |
| N-like monogram | `ff` candidate | reference supports **f**, not ff |
| QF-like sign | `ss` | reference supports single **s** |

The B7 `34` grouping remains a source question because the second member is not as clear as the A15 numeral. Where that grouping is accepted, the table supplies `tant`; the grouping itself is not proved by the vocabulary entry.

Likewise, not every inherited proposal is reference-confirmed. In particular, the target-derived `nous` word sign remains useful but is not visibly listed as a `nous` entry in the supplied table.

## 2. What the table does to the plaintext

The table produces several materially stronger connected passages.

### Extract A

The previously unresolved 34 and 40 now give:

> **peust auoir tant de faueur**

> could have so much favour

and earlier:

> **aiant faict ...**

> having done/made ...

The surrounding long sentence is still not completely recovered.

### Extract B

Two graphical correspondences in the supplied alphabet improve the opening to:

> **Auecques grande abondance de langaige ...**

> With a great abundance of speech ...

The following damaged `acompain...` cluster remains unresolved. Later `cresin` is still literal; `credit` remains only a reconstruction candidate requiring unsupported changes.

### Extract C

The opening now reads much more continuously:

> **Dont ie ueoi bien qu'il seroit bien aise de faire son ...**

Approximately:

> From this I see clearly that he would be quite pleased to make/derive his ...

The following noun is still literal `proufice` and has not been silently normalized to profit.

Later the grouped 26 gives:

> **la lui feiz ie bien entendre pour lui oster ceste ...**

Approximately:

> I made him understand it clearly, in order to take this ... away from him.

The likely hope-word remains malformed in the literal source and is still marked as a reconstruction.

### Extract D

The main financial clause survives the reference-table comparison and becomes slightly cleaner because QF is single `s`:

> **que son but seroit de nous faire entrer en quelque deboursement de deniers dont nous n'avons nule intention**

> that his aim would be to draw us into some expenditure of money, which we have no intention of making

This remains the strongest long connected clause. The table supports a large fraction of the machinery around it, but the value `nous` itself is still target-derived rather than directly visible in the supplied reference vocabulary.

## 3. Further source correction after the table comparison: A16:29 = faire

The next positive result came from returning to the native manuscript rather than further smoothing the French.

At A16:29, a sign had been classified as ordinary `H=i`. On the full-size manuscript image it instead has the same construction as the crossed-h word sign already read as **faire** at C1:10 and D2:4:

- tall vertical stem;
- high horizontal crossbar;
- lower right-hand arch.

It also matches the `faire` entry in Tomokiyo's supplied table.

Importantly, Daniel's earlier second-pass transcription had independently distinguished this particular sign from ordinary H and recorded it as `t4`. That does not by itself establish the plaintext value, but it supports the conclusion that our later H classification was wrong.

Only this one observation was reclassified after checking all H / crossed-h occurrences.

The resulting source-supported ending is:

> **... il esperoit faire sortir promptement la reconciliation necesaire entre ces deux ...**

Approximately:

> ... he hoped to bring about promptly the reconciliation necessary between these two ...

The following literal text is still:

> `roiallmes`

The obvious historical sense may be `roiaulmes / royaulmes`, but the source does not yet justify silently replacing the literal form.

## 4. Latest native-source checks: two tempting shortcuts do not survive

The latest pass returned to Daniel's original 3,205 x 4,149 photographs and tested two unresolved signs immediately before the new `faire` passage.

These tests produced **no new plaintext**, but they narrowed what we should not claim.

### A16:1 is not simply the ordinary MM/null family

The first mark on A16 had been left as `MINIM_UNCERTAIN_A16`. If it emitted nothing, the final `i` on A15 and the first clear `l` on A16 could be divided as:

> `...moi, il auoit moien...`

The native image does not justify that shortcut.

The source mark is an m-like construction with a **separate cross above/right**. Daniel's second-pass transcription describes exactly this occurrence as:

> `m+` - m with a small cross above

It is a singleton in that transcription and is visibly different from the unmarked extended-MM forms previously treated as candidate nulls.

So the cross-line `il` remains **conditional**, not recovered text.

### A14 [82] is not the reference table's il code

The A14 group is genuinely 82/8z-like in the native photograph. Its first sign belongs visually to the same 8-like family seen in nearby 80/84 groups.

Tomokiyo's reference `il` entry is 35-like; an earlier reading of the tiny reference digits had suggested 25. Neither is a secure match to the target's 8-like first component.

Accordingly:

> **[82] remains unassigned.**

The convenient assignment `[82] = il` is not adopted.

### The malformed `roiallmes`

Native review also shows that the two adjacent literal `l` outputs in `roiallmes` come from **separate source signs across the A18/A19 physical line break**.

That makes a simple one-glyph reclassification less likely. `roialmes` or `roiaulmes` may still represent the intended historical word, but at present that is better treated as an editorial or copying-error hypothesis than as a decoded correction.

## 5. Current status relative to PR #18

| Question | PR #18 baseline | Current position |
|---|---|---|
| Relationship to known Foix key | no key had been obtained | supplied 1565 Foix reconstruction shows substantial reuse |
| 26 | unresolved | table-supported `bien` |
| 34 | unresolved | table-supported `tant`, conditional on grouping |
| 40 | unresolved | table-supported `faict` |
| 52 | `qui` proposal | table supports `quil / qu'il` |
| 10 | unresolved / `sieur` candidate | reference gives `dict?`; `sieur` is 39 |
| 70 | unresolved | reference gives `toute` |
| N monogram | unresolved / `ff` candidate | reference supports `f` |
| QF | `ss` | reference supports single `s` |
| A16:29 | ordinary H=i | manuscript reclassified as existing `faire` word sign |
| A16:1 | unresolved minim | marked singleton `m+`; not safely an ordinary null |
| A14 [82] | unresolved | remains unresolved; direct `il` transfer rejected |
| Completion status | partial | still partial; materially better constrained |

The current private source-key version is v17. The only source-level change from the preceding checkpoint is the A16:29 reclassification to the existing `faire` word-sign class.

## 6. What remains genuinely open

The major unresolved items are now fairly specific:

- A: `[82]`, `desineramoii`, marked A16:1, `luquel`, `roiallmes`, and the malformed verb around `uoulrigniuir`;
- B: damaged `acompain...` cluster and `cresin`;
- C: `proufice`, connector around `aiela`, and the malformed hope-word;
- D: opening irregularities, `aduertdrez`, `rfert`, and the final unread reference.

A historical proper-name hypothesis for the end of D was tested after the PR and rejected; it caused no source/key change and is not included in the critical reading.

## 7. What would be most useful to check independently

The most useful review questions now are narrow:

1. **A16:29** - do you agree that the sign you transcribed as `t4` is the same crossed-h / `faire` word sign as the C and D occurrences, rather than ordinary H?
2. **A16:1 `m+`** - have you seen this marked m-like sign in any related de Foix material or adjacent Add MS 4136 ciphers, and is there any evidence that the cross is a control/null instruction?
3. **A14 code 82** - does the same 82/8z-like group occur anywhere in related material with a readable context?
4. **Foix table reuse** - does the degree of overlap with Tomokiyo's 1565 reconstruction look consistent with what you have seen in other de Foix correspondence?

The native photographs are not committed here because their public redistribution permission has not been established. The full private evidence preserves the source crops and all comparison coordinates.

## Attribution and caution

The supplied 1565 reconstruction must be credited to **Satoshi Tomokiyo**. It is external prior work and materially changes how the post-PR progress should be described.

Daniel Bourdeau supplied the photographs, prior identification, earlier source research and the independent second-pass transcription used for several source checks.

Lawrence Beck directed the continuation. ChatGPT performed the recorded source comparisons, computation, reconstruction tests and drafting.

This remains an **unreviewed partial decipherment**. The new table support is significant, but it does not turn every current expansion into authenticated plaintext, and the later source audit deliberately leaves several attractive completions unresolved.

## Relevant files in this PR

- [Original preliminary report](REPORT.md)
- [Original French and English reading](FRENCH_AND_ENGLISH.txt)
- [Open questions from the submitted baseline](OPEN_QUESTIONS.md)

This update should be read as a post-submission research note. It does not rewrite the evidential state that PR #18 originally froze for review.
