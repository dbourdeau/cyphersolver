# Numerical probes, 23 September 2026

**All manuscript outputs are unsuccessful hypotheses, not plaintext.** No key file has been accepted.

## Inputs

`probe_input_initial.json` freezes the first 16 f65-right runs plus two May spans. `runs_digits.txt` is their digits-only projection used by `Segment.cs`. Later, `runs_dots.txt` supplies the expanded 31-span inventory to `PairNull.cs`, retaining points. `runs_draft.json` and `cipher_inventory.md` give sources and adjacent clear text. These are uncertain visual drafts: negative results cannot rule out models on an error-free transcription.

All language scoring comes from the shared `lang.lm` engine, model `fr-1600-letters`. `quad.bin` and `penta.bin` are regenerable binary exports of its order-4 and order-5 tables; `alphabet.txt` is the model alphabet.

## Tests

| Test | Implementation/output | Outcome |
|---|---|---|
| Greedy single/two-digit prefixes from 0–5; unrestricted homophones | `probe_segmentation.py`, `segmentation_results.json` | Degenerate repeated-letter outputs. Discarded; conditional language probability alone was insufficient. |
| Same prefix family, constrained letter swaps | `probe_swaps.py`, `segmentation_swap_results.json` | No coherent French. |
| Six pair/null variants | `probe_pairs.py`, `pair_results.json` | No coherent French. These remove or expand every six, or pair with/without point resets. |
| Forward and backward prefix parses over all ten digits | `Segment.cs`, `segment_sweep.tsv` | 1,566 retained configurations; filters exclude fewer than 19 or more than 55 symbols and more than eight dangling cases. Three restarts of 5,000 proposals each, constrained swaps and repeated-triple penalty. No reading. |
| Pair parsing reset at points; drop orphan single six; additionally try deleting terminal six | `PairNull.cs`, `pair_null.tsv` | 100 restarts × 25,000 proposals per model. Two runs impose *mais…jamais*, a third is unseeded. No independent coherent extension. |
| May-only order-5 scoring with literal *plusieurs* | `MayProbe.cs`, `may_probe_seeded.tsv` | 1,000 restarts × 25,000 proposals, imposed *mais…jamais* and *ne/ni*. No meaningful complete sentence; no key accepted. |
| Synthetic positive control | `PairNull.exe control 40000`, `control/result.tsv` | Unseeded model recovered **538/538** letters in the generated pair substitution. |

The initial `may_probe.tsv` predates a correction to duplicate literal-symbol handling and is **invalid as evidence**. The corrected program reuses symbols for repeated letters of *plusieurs*; `may_probe_seeded.tsv` is the corrected run. This still fails to read the manuscript.

## Reproduction

From the repository root, export the shared model using Python:

```python
from pathlib import Path
from lang import lm
r = Path('labbe1582')
for order, name in [(4, 'quad'), (5, 'penta')]:
    m = lm.load('fr-1600-letters', order=order, spaces=False)
    m.lp.tofile(r / (name + '.bin'))
    (r / 'alphabet.txt').write_text(m.alpha)
```

Compile each C# source **separately** with the available .NET Framework `csc.exe`; they intentionally use the same standalone class name:

```powershell
& C:\Windows\Microsoft.NET\Framework64\v4.0.30319\csc.exe /nologo /optimize+ /out:labbe1582\Segment.exe labbe1582\Segment.cs
& .\labbe1582\Segment.exe labbe1582 5000
```

Use the equivalent command for `PairNull.cs` (25,000 proposals) and `MayProbe.cs` (25,000). Run Python probes from the repository root. Frozen inputs preserve the initial tests separately from the expanded transcription.

The control input and known plaintext are saved in `control/`. It is synthetic text derived from clear French phrasing, not a reading of an encrypted passage. It tests a clean monoalphabetic pair substitution, with no claim that this is the manuscript’s system. The model alphabet excludes j/v; the fixed control file, rather than a modernized retyping, is the comparison standard.

## Interpretation

The restricted implementation works on its positive control. Its failure on the manuscript leaves several possibilities: incorrect grouping, transcription errors, null or syllabic conventions, multiple keys, or a model outside the tested family. Optimization scores across differently segmented models are not calibrated probabilities. A short plausible crib cannot be promoted to a key without a coherent independent extension.
