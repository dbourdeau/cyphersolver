# Basel UB AN V 9 (baselanv9): pass 3, 25 Nov 2026 evening

**Bottom line**

1. **Tried:** the brief asked for "pass 2", but pass 2 (key leaf, 62 first-series rims, separate judge) was already done, pushed and commented on PR #957 at 13:43-13:52 AEST today, with H1 still at 62.04% [measured: `wt-basel/targets/baselanv9/keyleaf/RUN_RECORD.tsv`]. This job is therefore a declared **pass 3**: key leaf re-checked (no value changed), decoder rules corrected and frozen as key v3, H1 re-read from the full-size image, a fresh held-out passage H4 (f. 25r lines 1-12), 11 second-series rims (ff. 52r-53r), one decode after the freeze (07:55:17Z).
2. **Figures (solver's own strict count, NOT a separate judge; pass 1 stays the figure of record at 65.6% pooled, H1 62.4%):** H1 re-read 394/405 = **97.28%**; H4 held out 379/415 = **91.33%**; second-series rims 468/521 = 89.83%, 10 of 11 rims at or over 65%, S2-05 at 4/17 = 23.5% (names) [measured: `SCORE_P3.tsv`].
3. **Does H1 clear 65%? Yes on the re-read, with two limits.** It is not held out (decoded twice before; I had seen its clear copy), and no separate judge has scored it. The check that does not depend on my judgement: the H1 decode matches 399 of 425 letters of the clear copy f. 109v = 93.9% [measured]. Controls 0/5000 at both seeds for H1r, H4, the rims as a section and each of the 11 rims [measured: `CONTROL_P3.txt`].
4. **Blocked:** nothing by a site. Not done: a separate judge (this agent cannot launch one; `judge/BRIEF.txt` + `judge/decode.txt` are ready, the brief was written after the decode); the three two-ring figures on f. 54r, f. 97r-v and the texts inside the circles; H4 against its clear copy; the printed Key of Solomon pentacle legends.
5. **Next step:** launch the separate judge on `judge/`; if it confirms, Malcolm decides whether pass 3 goes to #957 as a follow-up. Nothing was pushed, posted or sent.

## What changed against pass 2, and why H1 moved

- **The key did not change.** All 73 token values, 5 pairs and 2 word forms of pass 2's `KEY_LEAF.tsv` were re-checked against the leaf image f. 99r; none differs (`KEY_V3.tsv`, `RULES_V3.md`) [measured].
- **The decoder changed in five declared places** (`RULES_V3.md`): C1 mark order (`Tk^@` = rum, a pass-2 fault); C2 a nasal dot on a vowel + consonant group sign goes after the vowel (et_ = ent; ground: leaf wording and the training leaf f. 4r, ruebant, fiebant); C3 two-dot fallback widened; **C4 `Cl Tq` = rte and C5 x = ch in the chi-rho-iota abbreviation are NOT on the leaf**. H1 without C5: 379/405 = 93.58%; without C4 and C5: 374/404 = 92.57% [measured].
- **H1's failure in passes 1 and 2 was transcription, not key** [derived]. At native size the lambda (a) is a thin leg plus a thick hook; passes 1-2 often wrote it as `1` (b) or as `Lm 1` (a + b): sabctorem, bgnia, gbudi, qubcuque. Nasal dots were on the wrong sign, and the leaf's ligatures ia, io, tio, tia, ur, pt, te were not used. Every change is in `DOUBTS_P3.md`.

## Per-section figures [measured: `SCORE_P3.tsv`, full arithmetic per line there]

| unit | status | S | E | N | S/(S+E+N) | controls, seeds 20261112 / 7 |
|---|---|---|---|---|---|---|
| H1r, f. 15r l. 1-12 | re-read, not held out | 394 | 5 | 6 | 394/405 = 97.28% | 0/5000, 0/5000 (z 11.7 / 11.7) |
| H4, f. 25r l. 1-12 | **held out**, first decode | 379 | 7 | 29 | 379/415 = 91.33% | 0/5000, 0/5000 (z 9.8 / 9.8) |
| S2 rims, 11 | new text, no clear copy | 468 | 8 | 45 | 468/521 = 89.83% | 0/5000, 0/5000 (z 12.6 / 12.6) |

Per rim: S2-02 49/50 = 98.0%; S2-03 39/40 = 97.5%; S2-04 38/39 = 97.4%; **S2-05 4/17 = 23.5% (under)**; S2-06 40/40 = 100%; S2-07 50/50 = 100%; S2-08 47/49 = 95.9%; S2-09 54/62 = 87.1%; S2-10 52/60 = 86.7%; S2-11 51/58 = 87.9%; S2-12 44/56 = 78.6%. Each rim 0/5000 at both seeds; lowest z 4.6 / 4.5 (S2-05). H4's lowest lines: L09 24/33 = 72.7%, L10 25/33 = 75.8%. Signs with no value: H1r 0, H4 5, S2 0.

## The plaintext (no emendation; `DECODE_P3.txt`)

H4, f. 25r [measured decode; sense unverified]:
```
post hac sugit et aperit brachia sua ac si uellet amplexari aere dicendo [?]
per nooen iestius libri et per omnes eius uirtu=tes [?] tortuosi ne[?] deformes sed in oni man=
sueta forma ad nos ueniatis et per nomen et in nomine adonai sabaoth emloo eloi sadai
iod he uau aleph tetragrammaton ineffabale eius uidelichet qui est deus uirtut~um deus
exel[?]us deus ueus ter imsrael qui super t[?]= rar gerum habitat et in coelo sedes eius
per nomen eius qui dixit et facta sunt et stare fecit omnia et ipse super omnia dominatur et
```
Rims: S2-02 hoc signum triumphatoris dni~ nostri iesu ch~ri mesteriosum. S2-03 cum hoc signo erus gratus omnibus et fortunatus. S2-04 iesus autem trasiens per medium ipsorum abiit (Luke 4:30). S2-05 caraton amen mathoi. S2-06 deposuit potentes de sede et exaltauit humiles (Luke 1:52). S2-07 hoc signum reddit hominem uirtuosum et a periculo defendit. S2-08 hoc est ineffabale nomen dei quo aron usus est in periculus. S2-09 ad amorem ingribe hos caracteres in crusta panis et praebe ad commedendum. S2-10 hoc signum in sinu aut uestibus portatum auget hominem gratia mirabala. S2-11 gribe hoc cum manu sinistra sanguine digiti tui die iouus in aurgento. S2-12 contra ligaturam positum in uestibus ligati statim liberabiutur.

## Known texts compared (`PRIOR_ART_P3.md`)

The rims are use-captions of the late-medieval pseudo-Solomonic amulet-seal kind ("hoc signum ...", "qui hoc signum portat ..."), as in BL Stowe MS 16 ff. 151r-152r [sourced: Drieshen, BL blog 2019], plus Gospel and psalm verses. Two web searches found no page with the Basel wording. Not compared with the Hebrew or Latin legends of the printed Key of Solomon [unverified].

## Limits, stated plainly

- No person and no separate judge has checked any of pass 3. The S/E/N tags are mine; all 34 non-S words are listed with reasons in `SCORE_P3.tsv`.
- The reader knows the key leaf, so no transcription here is shape-blind. H4 is held out in the sense that its text was never transcribed or decoded before the freeze and its clear copy was not looked for.
- Two labels I would change by sense were left as first written (S2-09, S2-11 `5` where a hook-sign gives inscribe / scribe); they count as N.
- Rule C3 gives a for i in -bili- words (ineffabale, mirabala) where the x's inner dot cannot be seen.
- The pass-2 count "62 + 38 = 100" covers first-series nos. 11-110; with these 11 rims, 73 cipher rims are decoded. The "~112" in the brief counts circles, not inscribed rims [derived].

## Files (all in `/home/claude/fable25/basel_p2/`)

`RUN_RECORD.tsv`, `SPLIT_P3.md`, `FREEZE_P3.txt`, `KEY_V3.tsv`, `RULES_V3.md`, `DOUBTS_P3.md`, `tx/f015r_p3.txt`, `tx/f025r_H4.txt`, `tx/PENT_S2.txt`, `DECODE_P3.txt`, `SCORE_P3.tsv`, `CONTROL_P3.txt`, `PRIOR_ART_P3.md`, `BLOCKED.tsv`, `judge/`, `scripts/`. No project check tool was run: the repo checkers are repo scripts, which this brief bars.
