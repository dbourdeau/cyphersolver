# R9241 five-sign audit after PR #18 merge

**Lawrence Beck, with the assistance of ChatGPT**  
8 October 2026

This note answers Daniel Bourdeau's request on merged PR #18 to check the five apparent differences between the Beck working key and Feyseel Nur's independently derived 1565 de Foix key: **D, 3, 2, r, z**.

The main result is that comparison by mnemonic name alone was misleading. The Beck/private-v17 transcription and Daniel's public `qm2` transcription use several of the same ASCII labels for **different physical glyphs**.

No manuscript image is redistributed here. The comparisons were made against the original January photographs supplied by Daniel, Daniel's public `qm2_f148.txt` / `qm2_f149.txt`, and dated 1562 source material already examined in the continuing research.

## Result at a glance

| Beck/private label | Beck value | Physical qm2 counterpart | Feyseel K0 value for that physical counterpart | Result |
|---|---:|---|---:|---|
| `D` | t | `th` | t | **agreement; not a real conflict** |
| `3` | s | mostly `3`; one checked occurrence is `z3` | `3` = e/t; `Z3` = s | **mixed source class; plain-3 conflict remains open** |
| `2` | l | `2` | i | **genuine unresolved conflict** |
| `r` | u | `c` / `c'` | c = u | **agreement; not a real conflict** |
| `z` | i | `z` | p | **genuine chronological conflict; pre-1564 evidence supports i** |

## How the transcription crosswalk was checked

The private v17 source ledger and Daniel's second-pass public `qm2` transcription describe the same January manuscript lines but use different sign mnemonics. On manuscript rows where the two transcriptions have the same unit count, units can be compared position by position without plaintext fitting.

For the five requested private labels, the unambiguous equal-length-row subset gives:

| private label | qm2 labels at the same physical positions | checked positions |
|---|---|---:|
| `D` | `th` | 29 / 29 |
| `3` | `3` 29 times; `z3` once | 30 |
| `2` | `2` | 5 / 5 |
| `r` | `c` 23 times; `c'` once | 24 |
| `z` | `z` | 8 / 8 |

These are a conservative subset, not total occurrence counts. They are sufficient to show that `D` and `r` are mnemonic collisions rather than cryptographic disagreements.

### Example of the label collision

On the January line beginning the private A2 row, the same physical sequence is transcribed:

Private/v17:

`D p a THREE_CURL r f CH 50 FF 50 3 E ...`

Daniel qm2:

`th p a z3 c f ch so ff so 3 tb ...`

Thus private `D` is Daniel's `th`, and private `r` is Daniel's `c`. Comparing private `D` against Feyseel's `D`, or private `r` against Feyseel's `r`, compares different glyphs.

## 1. Private D = t

**Decision: retain t; apparent conflict removed.**

The private `D` class maps to qm2 `th` in all 29 unambiguous positionwise checks. Feyseel's independent K0 has `th=t`, so the two keys agree on the physical sign.

There is also direct earlier evidence. In the 6 June 1562 cipher with contemporary marginal decipher, the broad loop/sweep form in the bounded word `bruict` maps to final **t**. The January `D` / qm2-`th` construction is the same broad loop/sweep family.

The previously reported comparison `D: t versus a` resulted from comparing the private label `D` with qm2/K0 `D`, which is a different, delta-like physical sign.

**Conclusion:** no key disagreement for this January glyph.

## 2. Private r = u

**Decision: retain u; apparent conflict removed.**

Private `r` maps to qm2 `c` in 23 unambiguous positions and to the closely related `c'` once. Feyseel K0 gives qm2 `c=u`.

The 6 June 1562 bounded contemporary pair `bruict` also directly maps an open c-like sign to **u**.

The reported `r: u versus m` therefore compares private `r` with Feyseel's different physical qm2 `r` sign.

**Conclusion:** the two independent readings agree on the physical c-like January sign.

## 3. Private z = i

**Decision: retain i for the January target.**

Here the sign names really do refer to the same physical flat-z family: private `z` maps to qm2 `z` in all eight unambiguous checks.

Feyseel's 1565 K0 gives this sign as **p**, so this is a genuine historical/comparator conflict.

However, the continuing source work supplies direct pre-1564 evidence independent of R9241:

- 6 June 1562, bounded contemporary cipher/marginal-decipher pairing:
  - `ma derniere`: flat `z` = **i**
  - `bruict`: flat `z` = **i**
- the 1 July 1562 source analysis repeatedly aligns the same short zigzag family with **i**, although that broader alignment is less cleanly independent at the individual-sign level than the bounded 6 June pairs.

The 6 June pair is enough to retain **z=i** for the pre-1564 state. Potter also states that de Foix's cipher was significantly modified in early 1564. The Catherine letter is now identified as 15 January 1563/4, immediately before/around that transition, whereas Feyseel's comparator is from 1565.

This chronology makes a changed value plausible, but it does **not** by itself prove exactly when the value changed.

**Conclusion:** the directly paired 1562 evidence outweighs the later 1565 table for this January occurrence. Retain `z=i`; record `z=p` as a later-state conflict.

## 4. Private 3 = s

**Decision: split the morphology conceptually; plain-3 value remains unresolved against the 1565 key.**

The private `3` class is not perfectly homogeneous when checked against Daniel's later transcription:

- 29 checked positions correspond to qm2 plain `3`;
- A1:2 corresponds instead to qm2 `z3`, the descended 3-like form.

This matters because Feyseel K0 distinguishes them:

- `Z3=s`, which **agrees** with the private value at A1:2;
- plain `3` is assigned e/t in the 1565 comparison key.

So one part of the apparent conflict disappears after the source class is split, but the plain-3 majority remains a genuine disagreement.

The January plaintext supplies many replicated contexts for private plain-`3=s`, but that is target-internal evidence. No A/B-grade pre-1564 cipher/marginal pair for the exact plain-3 subtype has yet been established in the dated witness work.

**Conclusion:** do not overwrite plain `3=s` with the 1565 value, but do not call `3=s` independently established either. Future active source ledgers should separate A1:2/qm2-`z3` from the plain-`3` class. This bookkeeping split does not change A1:2's emitted **s**.

## 5. Private 2 = l

**Decision: unresolved; no key change.**

Private `2` maps to qm2 `2` in all five unambiguous positionwise checks, so this is a genuine comparison of the same sign family.

The current January reading uses **l**, while Feyseel's independent 1565 K0 gives **i**.

The January contexts strongly favor l in several places, including connected material such as `reconciliation` and the opening of `le intention`, but those are target-internal constraints. The current dated pre-1564 audit has not yet produced an independently paired occurrence of this exact `2` subtype.

Because the cipher was modified in early 1564, the 1565 value cannot automatically supersede the January value. Conversely, fluent January French is not enough to declare the later table wrong.

**Conclusion:** retain `2=l` provisionally in the frozen replay, mark the sign as an unresolved chronological/value conflict, and prioritize it in the next paired-witness search or the exact TNA SP 70/67 comparison.

## Net effect on the decipherment

This audit does **not** justify a wholesale key correction.

- Two of Daniel's five requested conflicts, private `D` and private `r`, disappear once the physical-glyph crosswalk is made.
- `z=i` gains direct dated 1562 support and should remain.
- private `3` needs a source-class split; the plain-3 value remains open.
- `2=l/i` remains open.

No plaintext output is changed by this audit.

The larger lesson is methodological: **compare physical glyphs first, then mnemonic labels**. The private and qm2 transcription namespaces are not interchangeable.

## Files and evidence used

- merged PR #18 contributor source/key package;
- Daniel Bourdeau, `qm2_f148.txt` and `qm2_f149.txt`;
- Feyseel Nur PR #21, especially `r9241_foix1565key/key_k0.json`;
- original January R9241 photographs supplied by Daniel;
- 6 June 1562 BnF fr.6612 f.54 cipher plus contemporary marginal decipher, bounded pairs `ma derniere` and `bruict`;
- 1 July 1562 BnF fr.6612 ff.84-85 comparison work as secondary dated support.

No restricted manuscript images are included in this Git contribution.
