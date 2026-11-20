# Transcription benchmark: Opus 5.5 rerun (19 Nov 2026)

Same ten documents, same tiles, same references, same scorer and same three-blind-pass protocol as the Sonnet run
(`RESULTS.md`, `scores.json`), with the transcriber changed to Opus 5.5 (claude-opus-5-5; each subagent reported that
model ID). Raw passes: `passes_opus/`. Numbers: `scores_opus.json`, `analysis_opus.json`.

## Digit error rate (alphanumeric for carpio and ferdinand), mean of three passes
| Document | Sonnet 5.5 | Opus 5.5 | Opus consensus of 3 |
|---|---|---|---|
| hellen R1953 | 1.5% | 1.0% | 1.1% |
| santacroce R7 | 2.0% | 1.2% | 1.0% |
| santacroce R6 | 3.9% | 2.3% | 2.0% |
| kauderbach R2078 | 4.0% | 2.8% | 2.5% |
| dandini R72 | 4.4% | 3.9% | 3.3% |
| hellen R1049 | 9.6% | 4.8% | 4.6% |
| ferdinand R1889 | 3.2% | 3.6% | 3.5% |
| ferdinand R1890 | 3.0% | 3.5% | 3.1% |
| carpio R1009 | 18.0% | 17.1% | 17.2% |
| carpio R1010 | 15.9% | 17.7% | 17.4% |
| **All, pooled (30 passes)** | **5.1%** | **4.1%** | |
| Digit-only documents, pooled | 4.0% | 2.5% | |
| Letter-and-digit documents, pooled | 8.7% | 9.0% | |

Hellen exact groups (dot-separated numbers): R1049 Sonnet 60/82/74%, Opus 72/71/73%; R1953 Sonnet 95/95/94%, Opus
97/96/97%.

## What it shows
1. **Opus is better on digit-only hands, about 2.5% against 4.0% pooled.** The biggest gain is hellen R1049 (9.6% to
   4.8%), the hand where Sonnet misread 4 as 2 systematically. Opus's main hellen confusions are different (4 read as 9,
   1 as 4), so the systematic misreading was reduced, not removed.
2. **No gain on letters mixed with digits.** Carpio is about 17% for both models (Opus worse on R1010 and on its passes 2
   and 3), ferdinand slightly worse for Opus (3.5% against 3.1%). Letters read as digits (o as 0, b as 6) persist; Opus
   adds h read as k.
3. **Opus's passes agree with each other more where it matters, but disagreement catches fewer errors.** Where passes
   disagreed the pass-1 character was wrong 23-81% of the time, against 0.5-7% where they agreed (Sonnet: 34-81% and
   0.8-12%).
4. **Opus flagged fewer lines as unsure (180 of 1,087 against 324 of 1,086),** the flags remain unscored and should not be
   relied on.

## Limits
- Same limits as `RESULTS.md`: ten documents (not the frozen 41), one human reference each with its own errors, no expert
  check, the downstream solver test and the Pillon rerun not done.
- **Three passes each, so single-document differences are noisy.** Per-document ranges overlap in places (carpio, ferdinand,
  dandini); the pooled digit-only gap and hellen R1049 are the differences clearly larger than the spread between passes.
- **The prompts were nearly identical but not byte-identical to the Sonnet run:** Sonnet pass 1 of the first four documents
  used a looser flag instruction (flags are not scored), and the Opus prompts asked for plain ASCII and the model ID.
- Opus transcribed from the same tiles; Sonnet's ferdinand pass 1 read copies it had rotated itself. Neither affects the scorer.
- Opus 5.5 came from the subagent `model` option; the only check is each agent's own report of its model ID.
