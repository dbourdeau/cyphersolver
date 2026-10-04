# Catherine de' Medici to Paul de Foix - current research status

**Substantial decipherment update, 4 October 2026**

**Lawrence Beck, with the assistance of ChatGPT**  
Photographs, earlier transcriptions and prior source research: **Daniel Bourdeau**  
Comparative reconstructed 1565 Foix key: **Satoshi Tomokiyo**  
Independent Foix cipher reconstruction and correspondence edition: **David Potter**

Target: British Library Add MS 4136, ff.148v-149, DECODE R9241, four encrypted extracts copied under the heading **15 January 1563**.

## Status at a glance

The position has moved materially beyond the preliminary state submitted in PR #18.

- **1,029 of 1,038 recorded source observations now have working assignments: 99.13%.**
- **Nine source observations remain unassigned.**
- Under a deliberately conservative connected-text measure, **827 of 1,157 known emitted letters form defensible connected French: 71.48%.**
- That 71.48% figure excludes malformed words and editorial repairs even when their intended reading is strongly suggested by context or by Potter's edition of the same letter. It is therefore a critical-edition measure, not a measure of how much of the letter's meaning can presently be understood.
- The cipher family is no longer unidentified. It is demonstrably related to the de Foix diplomatic cipher reconstructed independently by Tomokiyo and Potter, and several values have now been checked against dated 1562 manuscript cipher/plaintext evidence.
- An exact alternate archival witness of this letter has now been identified: **TNA SP 70/67, ff.82-84**, cited by Potter as a duplicate/intercept. Images of that witness have not yet been acquired, so it has not been used to alter the British Library literal reading.

This should now be described as a **substantial decipherment with a small number of unresolved signs and several malformed passages, some of which may reflect historical copying irregularities**, not as a fresh ciphertext-only target awaiting a first break.

## Why the original PR remains useful

PR #18 records an earlier stage of the work before the later comparative evidence was obtained. The long financial clause and a substantial portion of the mixed substitution/nomenclator system had already been reconstructed from the British Library copy and internal recurrence structure before Tomokiyo's table and Potter's exact-letter evidence were applied.

That chronology matters. The later sources validate, correct and extend the earlier work; they do not replace the fact that the initial substantial reading was developed independently from this target.

The original files in `beck-preliminary/` are therefore intentionally left unchanged as the frozen submission baseline. This document is the consolidated current-status update.

## 1. External Foix key comparison

After the original PR, Satoshi Tomokiyo's reconstructed 1565 Paul de Foix table was obtained and compared with the target. It substantially overlaps the working reconstruction.

Distinctive agreements include the numerical/nomenclator vocabulary around:

- `30 = est`
- `31 = pour`
- `50` / so-like form = `que`
- `83 = le`
- `84 = la`
- crossed-h word sign = `faire`
- `26 = bien`
- `34 = tant` where the grouping is genuinely 34
- `40 = faict`
- `52`-like group = `qu'il`

The comparison also exposed entries that required further source checking rather than blind adoption. In particular, the later work did **not** simply copy Tomokiyo's `70=toute` or N-like=`f` into the January target.

A subsequent native-image audit also corrected A16:29 from an ordinary i-valued H class to the already attested `faire` word sign, producing the source-supported sequence:

> il esperoit faire sortir promptement la reconciliation necesaire entre ces deux ...

The following kingdom word remains malformed in the literal replay (`roiallmes`) and is not silently normalized.

## 2. Dated 1562 primary-source evidence

The most important methodological advance after the first post-submission note was moving from reconstructed comparison tables to dated manuscript pairings.

The key witness is:

**Paul de Foix to Catherine de' Medici, London, 1 July 1562, BnF Français 6612, ff.84-85.**

This letter contains cipher together with a contemporary marginal decipher. Global sequence alignment was used because the margin and cipher wrap differently. The dated comparison supports a set of direct mappings and, critically, resolves several previous comparator conflicts.

Results relevant to the January target include:

- **`32 = par`**, confirmed in three dated occurrences. This supports the target reading and conflicts with Potter's composite `32=de` entry.
- **`10 = dict`**, directly confirmed.
- **RX-like sign = `mm`**, repeatedly confirmed.
- **`70 = tout`**, with the following `e` represented separately where `toute` is required. This shows that treating 70 itself as `toute` over-groups the dated evidence.
- the true angular N-like monogram represents **`ff`**, while visually similar b/pi-like forms must remain separate.

The earlier apparent July `82=ceulx` anchor did not survive source checking: the relevant July word is alphabetically encoded `celluy`. January `[82]` therefore remains unresolved.

The July alignment also produced successful held-out support on separate material, but those percentages are validation of the alignment procedure and are **not** presented as a percentage of the January letter deciphered.

## 3. January native-image transfers

The dated July evidence was then compared back to the full-resolution January photographs sign by sign. Values were transferred only where the physical sign construction was judged sufficiently close, rather than by transcription label alone.

Two January key entries changed:

### `70 = tout`

Both January occurrences were re-examined. The sign is the same uncrossed 7 + small oval construction seen in the dated witness. No separate e-valued sign belongs inside the code.

This makes the D instruction literally:

> ... alsi de tout ce ...

rather than the earlier malformed `de toute ce`.

### N monogram = `ff`

Both January N-monogram occurrences match the dated angular `ff` construction rather than the crossed b/pi-like forms.

This changes:

- C `proufice` -> literal **`prouffice`**
- D `rfert` -> literal **`rffert`**

Neither malformed word was then normalized by grammar. `prouffict` and `offert` remain editorial hypotheses pending better source evidence.

The existing January assignments `32=par`, `10=dict` and RX=`mm` were also upgraded by the dated comparison without changing their output.

## 4. Further dated alphabet evidence

A later survey of BnF Français 6612 identified additional 1562 cipher passages with contemporary marginal decipherment.

A bounded 6 June 1562 pairing gave:

- ten alphabetic signs corresponding to **`ma derniere`**
- six signs corresponding to **`bruict`**

From those directly paired sequences, thirteen graphical forms received new bounded contemporary support, including forms for:

`m, a, d, e, r, n, i, b, u, c, t`.

These do not produce a new January plaintext by themselves, because most broad alphabetic values were already provisionally reconstructed. Their importance is independent dated support for the underlying alphabet and for specific January morphology comparisons.

The same run located two credible numeral-82 forms in May 1562, but only in contexts where the corresponding reading comes from editorial text rather than a contemporary decipher. They are useful leads, not sufficient evidence to set January `82`.

## 5. Current reading

The complete literal replay is still intentionally rough because it preserves every unresolved or malformed output. Some of the strongest connected passages are now:

### Extract A

> Et en ceste visitation ... il esperoit faire sortir promptement la reconciliation necesaire entre ces deux ...

The middle of A still contains several malformed or unresolved stretches, including `[82]`, the marked `m+` sign, and damaged material.

### Extract B

The extract substantially reads as a description of someone speaking at length and trying to draw from the writer the means and expected support, while not being ignorant of what has happened. The literal noun currently emitted as `cresin` remains unresolved; `credit` is only an editorial candidate.

### Extract C

Current literal core:

> Dont ie ueoi bien qu'il seroit bien aise de faire son prouffice de ce roiaulme ...

`prouffice` is the literal output after the dated `ff` correction. The likely historical reading `prouffict` is not yet promoted into the source layer.

### Extract D

The strongest long clause remains:

> que son but seroit de nous faire entrer en quelque deboursement de deniers dont nous n'avons nule intention

Approximately:

> that his aim would be to draw us into some expenditure of money, which we have no intention of making

The following instruction now has:

> Vous uerez si la desus vous pourrez aprendre quelque chose et m'en [aduertdrez] alsi de tout ce qu'il se sera [rffert] depuis le partement du dict de [marisriuere].

The likely French sense is considerably clearer than the literal output, but `aduertirez`, `offert` and the final name are not counted as recovered words without source-level support.

## 6. Exact letter identified in Potter's edition

David Potter's edition changes the documentary context significantly.

Potter no.65 is the **same Catherine de' Medici to Paul de Foix letter**, dated Paris, **15 January 1563/4**. Potter cites:

**London, The National Archives, SP 70/67, ff.82-84 - duplicate/intercept.**

This corrects the project's earlier treatment of the copied heading as January 1563 in modern chronology. The relevant modern chronological year is **1564**.

Potter's edition supplies substantially reconstructed text for the same difficult passages and gives, among other editorial readings:

- `prouffict`
- `advertirez`
- `offert`
- `Mauvissiere`

Those forms are highly informative, but they have **not** been silently substituted into the British Library literal replay. Potter also notes that irregularities in the normal cipher appear to be associated with the copied intercept. That makes historical copying error a serious explanation for some of the remaining malformed output.

The decisive next source is therefore no longer speculative:

**TNA SP 70/67, ff.82-84.**

Until full-resolution images of those folios are inspected, the physical relationship between the TNA witness and BL Add MS 4136 remains undetermined, and no specific copyist error is claimed as proved.

## 7. What is firm, probable and still open

### Strong current results

- the target is a de Foix-family mixed substitution/nomenclator cipher;
- most of the alphabet and recurring nomenclator vocabulary are assigned;
- 1,029 / 1,038 source observations have working assignments;
- `70=tout` is source-supported in January;
- the January true N-like form is `ff`;
- `32=par`, `10=dict` and RX=`mm` have dated 1562 support;
- the A `faire sortir promptement...` passage is source-supported;
- the D financial clause is connected and reproducible;
- Potter no.65 establishes the exact letter and the January 1564 chronological context.

### Strongly suggested but not yet source-adopted

- `prouffice` -> `prouffict`
- `rffert` -> `offert`
- `aduertdrez` -> `aduertirez / advertirez`
- `marisriuere` -> `Mauvissiere`
- `roiallmes` -> historical kingdom spelling such as `royalmes / royaulmes`

These should be treated as editorial reconstructions until the source-sign discrepancies are demonstrated.

### Still genuinely unresolved

- nine source observations overall;
- the true value of January `[82]`;
- the marked A16 `m+` sign;
- several malformed/damaged stretches in extract A;
- the exact source explanation of `prouffice`, `rffert`, `aduertdrez` and the D8 name;
- the source genealogy between the TNA intercept and the later British Library facsimile/copy.

## 8. Current quantitative status

Two percentages should not be confused:

| Measure | Current result | Meaning |
|---|---:|---|
| Working source observations assigned | **1,029 / 1,038 = 99.13%** | coverage of the working key, including assigned nulls; not an accuracy claim |
| Conservative connected-readable letters | **827 / 1,157 = 71.48%** | letters inside defensible connected clauses/phrases; excludes editorial repairs and malformed words |

The second measure is intentionally severe. A substantial amount of the remaining 28.52% has an intelligible editorial reading, especially now that Potter's edition of the same letter is known, but this report does not convert that judgment into an unsupported solved-percentage claim.

## 9. Priority and attribution

This update does **not** claim discovery of an otherwise unknown de Foix cipher family. Tomokiyo and Potter independently reconstructed related de Foix material before this work.

The contribution claimed here is narrower and reproducible:

1. a substantial reading of the specific BL Add MS 4136 ff.148v-149 / DECODE R9241 extracts was developed before the later comparative keys were applied;
2. the target reconstruction was then tested and corrected against Tomokiyo's independent 1565 reconstruction;
3. dated 1562 manuscript cipher/plaintext pairings were used to establish or correct specific sign values rather than relying only on a composite table;
4. those dated forms were compared back to the January source photographs, producing the `70=tout` and N=`ff` target corrections and stronger support for several existing values;
5. Potter no.65 was identified as the same letter and TNA SP 70/67 ff.82-84 as the exact next source witness.

The cautious description at this stage is:

> **Substantial decipherment of the 15 January 1563/4 Catherine de' Medici to Paul de Foix cipher extracts, initially partially reconstructed independently and subsequently extended, corrected and validated using de Foix key evidence reconstructed by Satoshi Tomokiyo and David Potter and dated primary-source cipher/plaintext pairings from BnF Français 6612.**

Daniel Bourdeau supplied the manuscript photographs, source identification, prior transcriptions and public target framework that made the work possible. Satoshi Tomokiyo's reconstructed Foix table and David Potter's cipher reconstruction/correspondence edition are independent prior work and are credited accordingly.

## 10. Next verification step

The highest-value outstanding task is direct comparison with:

**TNA SP 70/67, ff.82-84.**

If that witness preserves clearer signs at the positions corresponding to `prouffice`, `rffert`, `aduertdrez` or `marisriuere`, it may allow the project to distinguish genuine historical cipher irregularities from errors introduced in later copying and convert several editorially obvious readings into source-supported plaintext.

Until those images are available, the literal replay is deliberately left conservative.

---

### Relationship to the earlier PR files

- `REPORT.md` remains the frozen original PR #18 report.
- `POST_SUBMISSION_UPDATE.md` records the first major post-PR Foix-table/source update.
- **This file is the consolidated current status as of 4 October 2026 and supersedes the earlier update for current conclusions.**

No manuscript photographs or restricted source images are committed here.
