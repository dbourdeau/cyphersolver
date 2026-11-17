# Independent review of Milan 1494, second pass

14 November 2026. Reviewed `46dec7b..20263c46b073dc2a1df9361bf5da02f58d395358`, limited to the requested paths. No network was used. All retained review artifacts are under `out/`; the repository's tracked files are unchanged.

The shape discoveries substantially hold up. The published substitution and tier arithmetic reproduce. The principal corrections concern the definition and description of the held-out measurement, some retained strict classifications, and several inaccurate statements about the evidence. This is **not** a finding that the cipher identification or the newly identified ll sign fails.

| Item | Verdict | Reason |
|---|---|---|
| **1. Shape rules and sorts** | **holds with corrections** | The key's c/n distinction is visible; the sampled hook/arm and left-bowl/right-bowl distinctions are real. Perfect agreement with previously forced readings is reproducible, but is not independent blind validation. Some shapes remain genuinely uncertain. |
| **2. Changed readings** | **holds with corrections** | Exact substitution and counts reproduce, all fourteen Ridolfi LL shapes and Alamanni's mantello support ll, and the gloss supports C for LL, BB and Re. RD should remain I. Two already-strict words retain low-confidence stem readings; several notes are stale. |
| **3. Held-out test** | **holds with corrections** | The frozen inputs and scorer reproduce 0.8382 versus 0.3790. The main scoring rule follows the written protocol. The claimed exact-word secondary result is missing, block 5 has reference-boundary defects, chronology is asserted rather than independently timestamped, and “blind” and the explanation of 0.886 need qualification. **A claim that the 0.85 criterion was met does not hold.** |

## 1. Shape evidence

### 1a. Key sheet: H is justified

I inspected the whole sheet and separately enlarged its c and n cells. Under c, the dash has a definite lower dot and no definite upper dot. Under n, the upper example has dots on both sides; the lower example has a definite upper dot. The contrast is visible in the supplied pixels, not merely inferred from words. See `key-c.png` and `key-n.png`.

**Retain H for Na/Nb and /a, /b as value provenance.** This does not make every individual occurrence H-quality handwriting. A lost or doubtful upper tick must still be represented as uncertainty at that occurrence. “Below only” requires inspecting the space above, especially to the right of the dash; a tick need not be centered or round.

The sheet's l is a crossed **b-like, right-bowl** form; the proposed LL is a crossed **d-like, left-bowl** form. A top bar by itself is insufficient to distinguish ll from l/p. Bowl side and the open-versus-closed lower part matter. The provided Gabbrielli 25 frame reinforces this distinction.

### 1b. Sample and findings

The ledger contains **191 sign observations**. Its core requested sample is 55 Ridolfi dot signs, 70 Ridolfi stem signs, and all 31 Alamanni dot signs. I additionally recorded the 34 supplied Alamanni stem cutouts and its mantello LL directly from the source. `j` is the zero-based token index within the transcription unit; thus `112r:4.13/j5` is one sign, not a whole word. Tables supplied with the cutouts match the committed shape tables after TSV parsing.

| Leaf | Dot signs checked | Stem signs checked |
|---|---:|---:|
| 112r | 13 | 22 |
| 113r | 18 | 20 |
| 113v | 6 | 8 |
| 115r | 18 | 20 |
| 220v | 13 | 12, including mantello |
| 221r | 12 | 16 |
| 221v | 6 | 7 |

The selection deliberately includes all fourteen Ridolfi B5/LL instances, the B0 outlier, low-confidence cases, and all the sparse 113v dot signs. It is not a random sample or an accuracy estimate. I inspected the cutouts on newly assembled sheets, the source-leaf overviews, and direct source crops for disputed passages. I did not independently relocate every cutout from scratch. I already knew the proposed readings; this review is independent of the authors' reasoning, **not blind to their conclusions**.

The ledger records **186 compatible and 5 unclear**, with no definite incompatible label. That is a compatibility assessment, not 191 confirmations of correct reading. The material exceptions/limits are:

- **113r:2.15/j2:** cropped by the scan edge. An upper mark is visible, but the complete dot configuration is not. Keeping the unsplit N is right.
- **113r:9.2/j0 and 113r:9.10/j1:** brown stains compromise the upper-dot area. I cannot certify a unique class. The unsplit labels appropriately remain.
- **113r:6.4/j5, 113r:9.10/j4, 115r:10.7/j3:** upper ticks are remote or faint. They illustrate why the upper-right space matters. The last is compatible with Na, though much less crisp than the usual examples.
- **113v:2.4/j4:** upper dot is clear; the lower smudge is not securely ink. This does not undermine n, but it prevents an unqualified claim about both dots.
- **115r:7.4/j0:** the remote mark below belongs plausibly to the following line, not to this dash. Upper-dot n remains compatible.
- **112r:5.8/j2, sala:** crossed stem/short foot, not an ordinary open hook or clear closed bowl. The existing alternatives should remain; this is not an LL counterexample.
- **112r:10.6/j1, al:** heavy ink at the foot; an arm is plausible but the sorter itself calls the shape low confidence. See item 2c.
- **115r:12.5/j0, di:** very faint. I see no distinct baseline arm and accept compatibility with Zh, but do not regard the image as a strong isolated exemplar.
- **Alamanni 220v:20.1/j0:** lower dot is visible, but the long dash may continue a preceding clear-text flourish. Keeping the older ambiguous token is sensible.
- **Alamanni 220v:21.4/j2:** faint upper-right tick; mantello's n remains a choice. The word has correctly not become strict.

In the sample, LL's left bowl consistently separates it from the sheet's l and the target's pb/right-bowl forms. The arm criterion for Zh/Za also works well on clear examples. The borderline is a short notch or ink knot at the junction, not an arbitrary difference in stem height or top-bar length. Avoid treating every unsorted or blotted stem as uniquely determined by these rules.

### 1c. “No disagreement” is arithmetically true, but its evidential description needs repair

I joined the shape tables to the **46dec7b** transcriptions, not to the relabelled outputs. The pre-existing forced subset gives:

| Subset | n/d | c/l | Disagreements |
|---|---:|---:|---:|
| Ridolfi dot signs | 34 n | 20 c | 0/54 |
| Ridolfi hook/arm signs | 24 d | 8 l | 0/32 |
| Alamanni dot signs | 12 n | 6 c | 0/18 |

These are the README's stated forced-subset counts. “No disagreement with any word-forced value” is fair **as a description of this join**. It is too strong if read as an independent validation experiment. The same sorter first located signs using the old label sequences, then sorted them; tile identities retained the unit IDs. Those sequences carry prior segmentation and classification decisions, and some labels are mnemonic. Also, “forced” itself means forced within the admitted transcription choices and vocabulary, not historically necessary.

The Ridolfi sorter notes already disclose this unusually well. Bring that disclosure into the main README: **“The sorts agree with the previously selected values in all 54/32/18 forced cases. The sorter had used the original label sequences to locate the signs, so this is a consistency check, not independent blind confirmation.”**

This is not wholly circular: old N and Z classes really do split into visibly different forms, and a sheet/gloss provides external values. Conversely, agreements such as old pb → right-bowl barred form have much less independence. The 114 confusion counts also use a key-assisted alignment to a known reference; they are not all manually established, independent sign/gloss pairings.

## 2. Readings and tiers

### 2a. Substitution and counts

`PYTHONDONTWRITEBYTECODE=1 python3 milan-1494/verify.py` passed from `repo/`, without `--write`. `build_audit.py` independently parsed the TSVs, counted tiers, checked strict-token syntax, and compared normalized readings with substitution output.

| Corpus | Strict | Forced | Lenient | Doubt | Unread | Total | Through forced | Through lenient |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Ridolfi | 194 | 54 | 31 | 2 | 2 | 283 | 248 (87.6%) | 279 (98.6%) |
| Alamanni | 53 | 11 | 16 | 2 | 9 | 91 | 64 (70.3%) | 80 (87.9%) |

Strict coverage is 68.6% and 58.2%, respectively. The verifier's grades are **98 H / 89 C / 55 S / 37 M / 4 I** and **45 H / 6 C / 13 S / 24 M / 3 I**. These match the main README, root README, TARGETS rows and generated reading tables. I had no offline copy of the GitHub PR body, so I cannot certify an additional table existing only there.

“82 proposed, two doubtful” for Alamanni and “80 read through lenient” are consistent accounting conventions, not conflicting totals. Likewise, Ridolfi has 281 proposals if doubt is included, but 279 through lenient. State the inclusion rule whenever comparing them.

All ordinary, read words spell the committed key output under the stated normalization. **Do not paraphrase this as verification of every expansion or identity:** bracketed text is removed, unread words are not tested, and the verifier bypasses equality for grade-I words. Re/Duca/name-number expansions and the supplied p in a[p]resentarsi therefore are not authenticated by a passing verifier. Syntax enforcement is also not image verification.

### 2b. Every LL occurrence

All fourteen Ridolfi signs below have the left-bowl, barred-ascender form. In each, **ll is better supported than retaining the old single-l label**. The spelling is a key inference from this distinct class plus the gloss, not something read as two literal l strokes in the cipher.

| Unit | Sign index | Reading | Image judgment |
|---|---:|---|---|
| 112r:4.13 | 5 | castello | Clear LL; wraps to physical line 5. |
| 112r:6.8 | 0 | a + lla camera | Clear left bowl and bar. |
| 112r:7.3 | 0 | ne + lletto | Clear LL; supports nel letto. |
| 112r:9.7 | 2 | della | LL clear; the word's first sign retains a separate alternative. |
| 112r:9.9 | 3 | quelli | Clear LL. |
| 112r:12.11 | 3 | quello | Clear LL. |
| 112r:17.3 | 3 | quella | Clear LL. |
| 113r:3.11 | 2 | della | Clear LL. |
| 113r:4.6 | 5 | Isabella | Clear LL. |
| 113r:4.9 | 2 | uolle | Clear LL. |
| 113r:9.2 | 4 | cauallaro | LL compatible; other signs remain doubtful/ambiguous. |
| 113r:9.9 | 3 | quello | Small partly filled left bowl, still LL rather than pb. |
| 115r:7.5 | 0 | ne + lla città | Clear LL. |
| 115r:12.3 | 0 | a + lla corte | Clear LL. |
| 220v:21.4 | 5 | mantello | Clear barred left-bowl form; differs from Alamanni's ordinary open l. Upper dot in the earlier n-sign remains faint. |

**Non volle is sound.** The sequence is `p P LL m`, hence u-o-ll-e, normalized volle. The earlier review's objection depended on identifying that sign as ordinary l; the newly established shape class supplies the missing evidence. This changes the tense legitimately, rather than silently inserting a consonant to suit context. I do not propose an alternative historical paraphrase of “dice non volle.”

### 2c. Promotions: consistent algorithm, incomplete transfer of uncertainty

I replayed `apply_shapes.py` against copies of the base-commit files in `out/replay/`. It reports **203 Ridolfi signs relabelled / 86 words promoted** and **28 Alamanni signs relabelled / 16 words promoted**. Comparing final TSVs to the base instead gives **90** newly strict Ridolfi words: the difference is the four RC words changed separately. Alamanni's final increase is 16. Thus 86/16 is accurate for the script; it is not the final complete Ridolfi tier delta.

No current strict row contains a multi-valued token, brace alternative or `?`. I found no newly promoted sampled word whose image clearly demands reversing the new value. In particular, Alamanni `221v:2.6` has an open hook without an arm; its promotion to strict di is visually reasonable despite its stale “not individually checked” note.

However, **two low-confidence sorts remain strict because they were already strict**:

- `112r:10.6` al, `11 5`; stem `j1` is low confidence in ridolfi-B.tsv.
- `221v:4.6` la, `5 11`; stem `j0` is low confidence in alamanni-B.tsv, with a heavy knot where a small loop cannot be excluded.

Both remain plausible readings. The image and sorter record do not justify claiming that their sign identity has no uncertainty without an explicit adjudication. Add an occurrence-level uncertainty marker and an appropriate non-strict tier, or explain why the recorded doubt does not affect the value. Do not mechanically demote every “low” field: for some signs it concerns a feature irrelevant to n/c or d/l. These two deserve attention because the doubtful feature is the stem-foot classification itself.

A further pre-existing inconsistency is `220v:10.2` questo: the note still admits “could be a slanted 11,” while the token is unqualified `a`. The source favors a joined, open a-like sign over two separate strokes, but does not make the old reservation disappear by itself. Explicitly resolve the note or retain the alternative. This is **not** one of the 16 promotions.

### 2d. Re and Duca

**RC = Re at C holds.** I inspected the five cited cipher forms on c259v, including direct crops of lines 3, 8, 12, 16 and 20, and the gloss runs/sequence. The raised c is clearest on 8 and 20, weaker on 16. Re is well supported by the repeated gloss and position. The article in **[il Re]** is editorial: the key correctly stores `[Re]`, and the gloss does not consistently contain an article within the sign's value.

**RD = [il Duca] at I is fair, not C.** The three 112r signs on lines 6, 10 and 11 share a long-tailed base and a raised hooked stem. In 114, line 3 has the same base but a 3-like raised sign; line 4 has an h-like raised sign whose top may overlap gloss ink. The gloss/scene gives a persuasive title comparison, but I cannot establish identity of all raised forms from these pixels. Keeping the inference and the Lodovico caveat is appropriate.

There is a concrete error in the argument: **the 9-null follows 114's line-3 Duke sign but precedes the line-4 sign**. It follows 112's first two RD occurrences; the third goes straight into rispose. “Each followed by the same 9-shaped null as in 112” is false and exaggerates the match. `gloss/signs.md` itself describes the positions correctly.

### 2e. Alamanni 221v:3–4

The lower-only dots in the opening signs of `ce la` and `calera` are visible; the remaining letter forms support c-e-l-a and c-a-l-e-r-a. **Doubt is the right tier for the phrase**, because word division, accent and the sense of “ce la calerà” depend on the unread material. It should not become a confident translation of the second threat.

The preceding run remains unread. At its third sign I see a loop/cup with a descending stroke and rightward crossing; `4{PSI}` is a reasonable record of uncertainty. I cannot establish the open-cup tt form rather than r. Substituting tt gives something like **acttesima**, not an independently persuasive word. “A [qua]resima” still supplies signs/letters the image does not provide. I offer **no new resolved reading**. The final x c of this unit are at the start of line 4; the displayed “acresima” should not be mistaken for a secure word or a single-line group.

### 2f. LL and BB grades

**C for both is justified**, with a narrower assertion than “all exact spellings independently legible.” In the c258v line-16 gloss, alla has two distinguishable l ascenders; q[ue]lla on line 15 is compressed but compatible with the same doubling. The corresponding cipher forms have left bowls and crossed ascenders. In c258v line 20, giouerebbe shows two b ascenders/bowls; c259v line 19 passerebbe supplies a second compatible example. These are stronger than merely choosing conventional Italian double consonants in an unglossed word.

The gloss is compressed horizontally: these are sequence-based correspondences, not a literal “word directly above its sign” lookup. I did not independently certify every one of the nine LL pairings or all four BB gloss spellings. The clear cited examples suffice for provenance C; uncertain target occurrences still need their own uncertainty markers.

## 3. Held-out measurement

### 3a. Reproduction and protocol

All three recorded SHA-256 values match the current frozen files. The frozen key is byte-identical to `git show 46dec7b:milan-1494/key.json`. The requested full 1,000-shuffle run completes successfully and reproduces the committed output:

| Quantity | Reproduced value |
|---|---:|
| Transcribed signs | 865 |
| Used labels absent from key | 0 |
| Reference letters | 988 |
| Agreement, any-of | **0.8382** |
| Agreement, first value | **0.7745** |
| Best of 1,000 shuffles | **0.3790** |
| Mean shuffle | **0.2859** |

The any-of numerator is **829**, and the sum of per-block maximum lengths is **989**, not 988: block 4 has 28 output characters against 27 reference characters. Per-block results are in `protocol-checks.txt`.

The scorer implements the written main rule: normalize, use first shape alternative, expand code values, keep nulls empty and person/unidentified signs as never-matching wildcards, then use global unit-cost alignment. Equal-cost alignments are resolved in favor of more matches. That tie-break is sensible and disclosed in the function docstring, but should also be stated in the protocol. No used value set has unequal-length alternatives, so the scorer's fallback for that unregistered edge case does not affect this run.

**The alignment metric is sound for the stated character-compatibility question.** It is not exact-word accuracy, nor simply one minus normalized edit distance. Spaces and word boundaries are discarded, gaps are optimized, and each occurrence of a multi-valued sign can match a different permitted value. An 0.838 result therefore does not mean 83.8% of words, signs, or uniquely deciphered letters are correct.

**The null is fair for a conditional random-key comparison.** The same any-of advantage applies to observed and shuffled value sets; the sets themselves remain intact. It does not establish transcription independence, the correctness of a particular word, or performance of a single-valued decipherment. Permuting sets among labels also changes which frequent labels receive broad or multi-letter values, so it does not preserve the occurrence-weighted ambiguity budget or output length. That limits its interpretation, but does not make the large observed separation disappear. No formal probability of “the reading is true” should be attached to it.

Two qualifications prevent saying “everything was run as preregistered”:

1. The promised **count of exact words** (`PREREGISTRATION.md:35–36`) is neither implemented nor reported. Add a clearly specified secondary word-comparison rule/result, or acknowledge that this part was not performed. Do not invent one after the fact and call it preregistered.
2. The commits contain protocol, frozen inputs and results together. Their hashes verify file identity, **not the claimed temporal order of writing, viewing and scoring**. The recorded workflow is consistent with preregistration, and I found no evidence of changed frozen inputs; I cannot independently prove the chronology or the authors' lack of earlier image exposure from these files alone.

### 3b. Block boundaries

Blocks 1–4 and the beginning/end of block 6 are broadly consistent with the clear/cipher transitions and quoted reference. In particular the stand-alone clear Certamente correctly separates blocks 2 and 3.

**Block 5 is not cleanly delimited.**

- At its start, the abbreviated **che quando** after “E m'ha affermato” looks like clear text, and the gloss starts with Re. The transcriber's own notes say the three marks were counted as cipher because the boundary instructions said so. The README already acknowledges this probable error; it is partly a masking/boundary instruction error, not merely a transcriber error.
- At its end, **si is clear**, written in the margin before the clear trovava at the beginning of line 6. It should not be in the cipher reference. This is already admitted in `gloss/NOTES.md`, but not in the main held-out account or reference annotation.
- The final line-5 group around x1020–1200 is also strikingly clear-script-like (“el quale”), and the blind notes explicitly flag its unusual appearance. The gloss reader treats it as accounted for in the gloss. I would have a palaeographer adjudicate this boundary before claiming a fully corrected cipher-only score; I have not silently excluded the group or claimed a definitive additional correction.

Preserve the frozen measurement as the historical result and publish a separately labelled sensitivity calculation. With the frozen transcription unchanged, removing final si from the printed reference yields **0.838906**. Additionally removing initial chequando from the reference and the first three transcribed marks yields **0.843558**. These are **post hoc diagnostics, not replacement preregistered scores**; the latter is still below 0.85 and does not adjudicate the final “el quale” group. I did not run new shuffle distributions for these diagnostic variants.

### 3c. Blindness

“Gloss-masked transcription with partial blinding” is defensible. “Blind” without nearby qualifications is too broad. The held-out README discloses mnemonic labels, but should also say directly that:

- the transcriber received **label sequences**, not only images of 112/113/115;
- the masker necessarily saw gloss and selected the boundaries;
- the scorer had seen **two plaintext fragments**, as the protocol explicitly says;
- the blind notes record an instruction to omit three undecided raised groups, later identified as cipher superscript ta, despite the masking manifest saying those groups were kept;
- the original images had already been downloaded, and “working notes record no use” is weaker than proof that nobody had seen them.

I inspected three masked crops against their source regions. They remove readable interlinear gloss in those sampled spans, but also trim nearby ink and leave some stubs. I did not audit every mask pixel or every possible residual cue. These limitations concern the transcriber/masker workflow; they do not show that the frozen key was trained on 114.

### 3d. Secondary gloss score and the bar

The full secondary rerun also reproduces the committed result: **0.8855 any-of, 0.8162 first-value, best shuffle 0.3784, mean 0.2873**. Both saved rerun outputs match their committed result files byte for byte. The warning that 0.886 is post hoc and partly circular is welcome. The phrase **“only to show how much of the shortfall is the printed text” still overclaims**. That difference mixes spelling modernization, abbreviation conventions, different reference boundaries, and spellings chosen with help from the cipher. It is not an identified causal estimate of modernization's cost. Prefer: **“a post hoc sensitivity comparison to a partly cipher-assisted gloss transcription; not independent validation or an estimate of accuracy.”**

The main run missed the threshold by about **0.0118**, or 1.18 percentage points. “Just under the bar” is arithmetically fair if immediately accompanied by **“did not meet the preregistered criterion.”** It should not imply practical passage, statistical equivalence to 0.85, or that the gloss comparison rescues the result. The current headline table correctly leaves 0.838 as the primary number.

### 3e. Gabbrielli

The supplied frames support the substantive comparison. No. 25 is headed Alamannis (de) Petrus, 1492, filza 39; its alphabet matches the distinctive families of sheet 183, and its doppie visibly give **ll, nn, rr, tt**, including the left-bowl barred LL. B, G and Z have no entries. No. 34, headed Johannes Batta de Rydolphis, 1495, has a visibly different substitution alphabet and its own double-letter and name/number material.

“Same alphabet as far as recovered” is a fair summary; “a subset that would necessarily read everything the sheet reads” would be too literal, since this is a later copy/reconstruction and not a comprehensive occurrence test. “No. 34 does not supply this October 1494 alphabet” is better than the absolute “does not bear on the letters.” The images alone do not independently establish how Gabbrielli reconstructed the tables or when this project first noticed LL.

## Concrete corrections

Locations below are relative to `repo/`. “High” means the file/image evidence directly establishes the correction; “medium” marks an interpretation or a recommended qualification.

| File | Location | What it says | What it should say/do | Certainty |
|---|---|---|---|---|
| `milan-1494/held-out-114/README.md`; `milan-1494/key.json` | Person signs, item 5; RD basis | Both Duke signs are each followed by the same 9-null as in 112. | 114 L3: null after; L4: null before. 112: after the first two occurrences, absent after the third. Use adjacency only as supporting evidence. | High |
| `milan-1494/held-out-114/reference-desjardins.tsv`; `blocks.md`; held-out README | Block 5 endpoint / measurement caveats | Block 5 ends “… il quale si”; only trovava is excluded. | Annotate that si is clear before trovava. Preserve frozen result; provide a separately identified boundary sensitivity. | High |
| Same | Block 5 start | Cipher begins after affermato, including che quando. | Identify likely clear ch[e] q[ua]n[do], and distinguish boundary-instruction error from pure sign-reading error. | High for needed qualification; medium-high for exact clear expansion |
| `milan-1494/held-out-114/PREREGISTRATION.md`; `score.py`; results | Lines 35–36 / secondary results | Promises a count of exact words. | Report that this secondary check was not performed; optionally add a separately specified post hoc word metric. | High |
| `milan-1494/held-out-114/README.md` | Measurement opening / “blind” | Names shape exemplars, but not their label sequences; scorer exposure only discoverable through protocol. | State exemplar label sequences, mnemonic labels, gloss-aware masker, and scorer's two known plaintext fragments in one nearby disclosure. | High |
| Same; `blocks.md` | Raised groups on c259v L4, L13, L16 | Masker kept undecided groups; transcriber notes say omit them per instructions. | Explain that the frozen transcript omitted these kept groups and that later inspection identified cipher superscript ta. | High |
| `milan-1494/README.md`; `AUDIT.md` | Forced-shape agreement | Classes agree with every word-forced value. | Keep counts, explicitly call it consistency with earlier lexical choices after label-assisted locating, not independent blind confirmation. | High |
| `milan-1494/held-out-114/README.md` | Secondary 0.886 paragraph | Shows “how much of the shortfall is the printed text.” | Post hoc comparison to partly cipher-assisted gloss; difference does not isolate modernization. | High |
| Same | “What costs agreement” | abbia versus habbi offered as a scored mismatch. | Remove that example: neither occurs in the scored references; habbi is in the clear lead-in before block 1. Use an actual scored difference, e.g. dilezione/dilectione. | High |
| Same; `ridolfi-reading.md`; `docs/_build_site.py` and generated pages | “just under” / “falls just short” | Near-threshold wording. | Retain numerical proximity but explicitly say the preregistered 0.85 criterion was not met. | High |
| `milan-1494/ridolfi-transcription.tsv` | `112r:10.6`, j1 | Strict al, unqualified `5`; sorter confidence low. | Record/resolve the foot/arm uncertainty. If retained, add `?` or an alternative and assign a non-strict tier; rerun counts. | High conflict; medium on demotion pending adjudication |
| `milan-1494/alamanni-transcription.tsv` | `221v:4.6`, j0 | Strict la, unqualified `5`; sorter calls heavy knot low confidence. | Explicitly adjudicate open-arm versus filled-loop uncertainty or retain an occurrence-level doubt and non-strict tier. | High conflict; medium on demotion pending adjudication |
| Same | `220v:10.2` | Strict questo; note still says first sign could be 11. | Either document rejection of the old alternative on shape grounds or serialize it and cease calling the word strict. | High internal inconsistency |
| Same | `221v:2.6` | “d/l form not individually checked.” | Replace with the actual high-confidence shape-sort result and this review's compatible no-arm observation. | High |
| `milan-1494/ridolfi-transcription.tsv` | `112r:9.8` and other n/c, d/l notes | “n/c twice: dazio de la macine”; other unresolved-looking notes remain on newly strict words. | Distinguish historical ambiguity from current labels; update phrase to della, or identify these explicitly as old audit notes. | High |
| `milan-1494/AUDIT.md` | Table “Handling here” | non vuole restored; bb S; mante[?]o; all mantello/other listed words lenient. | Mark these as 13-November handling and append the 14-November state: volle, BB C, mantello forced. The sequence section alone does not resolve the table's present tense. | High |
| `milan-1494/README.md` | Opening “Two letters”; first table | Calls one Alamanni letter plus three Ridolfi despatches “two letters.” | “Two correspondents/four letters” or “two transcription corpora.” | High |
| `milan-1494/README.md`; reading pages | “secure parts are … H or C” | Risks equating evidence provenance with certain ink/transcription. | “Values supported by a key or contemporary gloss; individual transcriptions can still be wrong.” | High as methodological qualification |
| `milan-1494/held-out-114/README.md` | Gabbrielli no. 34 | “It does not bear on the October 1494 letters.” | “It is not the alphabet used in these October 1494 passages.” | Medium; wording precision |
| Public summaries of promotions | Wherever 86/16 is compared with final tiers | Could imply full final increase. | “86/16 by script; final Ridolfi increase 90, including four separately promoted RC words.” | High; no incorrect committed headline count found |

Corrections to tiers would require regenerated grade totals and reading tables; the numbers above are the **verified current counts**, not silently amended ones. I have not prescribed a new total before the two low-confidence occurrences and questo note are adjudicated.

## What a skeptical reader would attack first

First, the phrase “blind test” spans several actors with different exposures, and the frozen hash cannot certify that history. Second, a reference-optimized any-of character score is readily mistaken for accuracy of the newly strict readings, although it tested the **old** key on a different transcript. Third, the attractive zero-disagreement shape result comes after locating with the old labels in hand. Fourth, the higher gloss score uses partly cipher-assisted spellings and changed reference conventions. These should be disclosed in the main account, not only in linked notes.

The most concrete factual defect is the 9-null argument; the most concrete scoring defect is block 5's inclusion of clear si. Neither invalidates the underlying alphabet match. The strongest positive evidence is the visible key-sheet dot distinction and the repeated, distinct LL form with legible contemporary doubling and corroboration in Gabbrielli 25.

## Scope and artifacts

- `spot_checks.tsv`: all 191 image observations, including unclear cases. `selected-*.tsv` preserves sample-to-cutout mapping; `check-*.jpg` are the inspected sheets.
- `build_audit.py`: independent TSV counts/substitution checks, base-to-final promotions, frozen hashes, sample selection and key-cell enlargements. Output: `independent-counts.txt`.
- `test_protocol.py`: frozen-key comparison to Git, per-block score components, boundary sensitivity, shape-script replay under `out/`, and old forced-value joins. Output: `protocol-checks.txt`.
- `make_crops.py`: source-coordinate crops for the cited disputed passages. `write_ledger.py`: entered visual observations serialized to TSV.
- `score-rerun.txt`: full requested primary rerun. `score-gloss-rerun.txt`: secondary rerun. `verify-rerun.txt`: normal verifier output.

I did not consult the live PR, print scans, catalogue, outside historical references, or any network source. Consequently I checked the supplied printed quotation and its manuscript boundaries, not the accuracy of its transcription from the printed edition. I did not certify the initial key-discovery history, recheck unavailable 107/110 images, re-run language-model permutations, re-transcribe all words, independently sort all of doc. 114, or certify every masking boundary. I inspected the unrelated site/favicon changes in the requested diff as code/content changes, not as a browser rendering audit; no substantive cipher claim depends on them.

The prior Codex review was read as historical context; this review's visual verdicts come from the supplied images. Enlargements add no detail. The proposed shape corrections are well supported within those limits, and the primary test remains useful evidence of nonrandom compatibility, with a documented failure to meet its chosen bar.
