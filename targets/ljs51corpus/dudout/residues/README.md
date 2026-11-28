# LJS 51: residues of the partial by-eye keys (3x shape re-reading)

Contribution by dudout (re-reading at 3x of the sign classes that break, with shape plates). Images: University of Pennsylvania, LJS 51, OPenn (PDM 1.0), Penn IIIF, 2343 px.

**Prior work.** The keys, alignments and the list of breaks are Daniel Bourdeau's: `targets/ljs51corpus/keys_eye/REPORT.md` and `keys_eye/<chain>.json` (commit 44d521b44a, read at origin/main ff00dffd61). Nothing here re-derives a key. We only re-read, on the images, the sign classes Daniel reported as mixed, and re-labelled a sign only where the plate shows two different drawn forms. All other alignment rows are unchanged. `scripts/revise.py` checks this: 0 non-target rows changed.

**Criterion.** Sign-to-letter consistency over repeated shapes, as defined in REPORT.md. It is measured before and after, per chain. The compiler's plaintext is given and the chains are short, so there is no held-out portion. This is a descriptive consistency gain, **not** a frozen held-out validation.

## Results (`results.txt`, `results.json`)

| chain | before | after | what changed (plate) |
|---|---|---|---|
| 24v.6 | 67/76 = 88.2% | 71/73 = 97.3% | The lam-alif class has three distinct forms: plain (م ×5), hooked top bar (ب ×3) and looped head (ص ×1) (`24v6_LA`). The sign Daniel read as Sr in البلاغه is a different form, sin teeth on a ى body, read as غ. 'سا' is one sign (ق) in both الاقاليم and قمر; the "Al" in قمر is the end stroke of that sign. Still open: و for ر/م in قمر; ا for ن in نسل. |
| 33r.4 | 77/80 = 96.3% | 80/82 = 97.6% | Reader A sees a second cup form, with a tooth in its base, in فجي and at the end of الحاجري (ي). The blind reader B is undecided on these two cups, so the split is {probable} and not counted (`33r4_coupes`). In كنت the sign is the ت-triangle of وافيت, not the triangle of الدر. Two signs were missed in the count. An hourglass (ل) gives الحاجري its ال (U ⧗ ...). A ya-barree (م) opens l.11, so منكور is complete. 90 signs. |
| 101r.2 | 62/65 = 95.4% | 65/65 = 100% | The "open cross" has two forms: a cross with a descender (ه ×3) and a seated loop with no descender (ح ×3) (`101r2_S9`). |
| 103v.2 | 48/50 = 96.0% | 48/49 = 98.0% | The first "I" is intact. Both readers find the second sign (scraped) unclassable, so it is removed from the class, not read. The third sign is kept as Daniel has it, because the blind reader sees an "I" there. |
| 81r.5 | 61/62 | unchanged | The two "tables" in فلقد differ only by a curved left leg, which is not enough to split them. Open. |
| 92r.10 | 100% | unchanged | The key holds. The group read كييب (ring, two identical stemmed loops, double arch) is very probably **كئيب**, with the hamza seat written ي as elsewhere in the volume. This is a textual variant against the compiler's كيف, not a key break. Metre not checked. |
| 59r.2 | 100% | unchanged | ▱ is a long triangle with a flat, cut top. Its nearest form is the ◁ (ن). If it is a variant, the verse reads كنا نشا ... نشا ... نشا. This is a hypothesis and is not counted. |
| 88v.10 | 100% | unchanged | Not re-read (time). |

Total over the 8 chains, counting only the changes on which both readers agree: 461/479 = 96.2% → **471/477 = 98.7%** on repeated shapes. Reader A alone gave 99.4% (`results_readerA_only.txt`). The withdrawn changes are listed in `probable_not_counted.json`.

In 24v.6, the sign in البلاغه is a different form from the Sr sign for both readers. Reader B calls it a hybrid (F teeth, G tail), so its value غ is {probable}.

## Caveats

- Two readings of the plates (`plates/`: one framed sign per question, shape options only, no letter names). **Reader A** is Claude Opus 5.5, the plate author, who was not blind to the alignment. **Reader B** is Claude Opus, reading blind from the images only (`plates/READER-B-blind.md`). A change is counted only when both readers agree (see `reader_agreement_fr.md`, `probable_not_counted.json`). Both readers are LLMs, so a human blind pass would still strengthen the result.
- The 33r.4 additions put new occurrences into two non-target classes, the hourglass (ل) and the ya-barree (م). Both take the class's existing value.
- For الحاجري, the ya-barree with two dots (S23) cannot be told apart at 3x from the ya-barree class S1 (م), which also carries 0-2 dots. Daniel's separate label is kept. The long box (S24) is left as a surplus sign, so the group still has two unresolved signs.

## Files

- `baseline_consistency.txt`: Daniel's figures, recomputed.
- `revised/<chain>.json`: Daniel's JSON with the revised alignment, plus `revision.log`, which gives each changed row with its reason.
- `plates/*.jpg`, `plate_specs/*.json`: the plates and the questions behind them.
- `segments/*.json`: page coordinates of every segmented sign (2343 px IIIF images).
- `scripts/`: the scripts. `segment.py`, `plate.py` and `grid.py` expect the IIIF JPEGs at a local path, set in `IMG`. `revise.py` reads `keys_eye/` (or `$KEYS_EYE`).
