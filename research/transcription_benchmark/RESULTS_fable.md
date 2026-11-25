# Transcription benchmark: Fable 5.2 rerun and three-model comparison (19 Nov 2026)

Same ten documents, tiles, references, scorer and three-blind-pass protocol as the Sonnet run (`RESULTS.md`,
`scores.json`) and the Opus run (`RESULTS_opus.md`), with the transcriber changed to Fable 5.2 (claude-fable-5-2; each
subagent reported that model ID). Raw passes: `passes_fable/`. Numbers: `scores_fable.json`, `analysis_fable.json`.

## Error rate, mean of three passes (alphanumeric for carpio and ferdinand)
| Document | Sonnet 5.5 | Opus 5.5 | Fable 5.2 | Fable consensus of 3 |
|---|---|---|---|---|
| hellen R1953 | 1.5% | 1.0% | 0.9% | 0.8% |
| santacroce R7 | 2.0% | 1.2% | 0.9% | 0.8% |
| santacroce R6 | 3.9% | 2.3% | 1.5% | 1.7% |
| kauderbach R2078 | 4.0% | 2.8% | 2.2% | 1.9% |
| ferdinand R1889 | 3.2% | 3.6% | 2.5% | 2.3% |
| dandini R72 | 4.4% | 3.9% | 2.8% | 2.8% |
| ferdinand R1890 | 3.0% | 3.5% | 2.8% | 2.9% |
| hellen R1049 | 9.6% | 4.8% | 4.6% | 4.5% |
| carpio R1009 | 18.0% | 17.1% | 14.0% | 14.2% |
| carpio R1010 | 15.9% | 17.7% | 14.1% | 13.5% |
| **All, pooled (30 passes)** | **5.1%** | **4.1%** | **3.3%** | |
| Digit-only documents, pooled | 4.0% | 2.5% | 2.0% | |
| Letter-and-digit documents, pooled | 8.7% | 9.0% | 7.2% | |

Pooled errors by type, as a share of reference characters: Sonnet 3.4% substitutions, 0.8% insertions, 1.0% deletions;
Opus 2.7%, 0.6%, 0.8%; Fable 2.1%, 0.5%, 0.7%.

Hellen exact groups (dot-separated numbers): R1049 Sonnet 60/82/74%, Opus 72/71/73%, Fable 90/89/72%; R1953 Sonnet
95/95/94%, Opus 97/96/97%, Fable 97/96/96%.

## What it shows
1. **Fable has the lowest mean error on all ten documents,** pooled 3.3% against 4.1% (Opus) and 5.1% (Sonnet). On the
   digit-only documents it is about 2.0%, i.e. about 98% accurate digit by digit.
2. **The gain over Opus is smaller than Opus over Sonnet, and for several documents is inside the spread between passes**
   (hellen R1049 4.6 against 4.8, ferdinand R1890 2.8 against 3.5 with overlapping ranges, dandini, kauderbach). The clearer
   differences are hellen R1953, both santacroce documents, ferdinand R1889 and carpio.
3. **Carpio improves for the first time, 14% against 17%, but remains the worst document by far.** Letters read as
   digits and the missed lines noted in `RESULTS.md` still dominate. Fable's top confusions are 1 read as 4, n as x,
   7 as 9, g as 7, f as 8.
4. **Hellen R1049 is now readable by both newer models (about 4.6%),** where Sonnet misread the open 4 as 2 systematically.
   Fable's exact-group rate there is 72 to 90%, the best of the three but the least stable between passes.
5. **Disagreement between passes remains a usable warning for every model.** For Fable the pass-1 character is wrong 31 to
   88% of the time where the passes disagree, against 0.5 to 9% where they agree. It catches 15 to 54% of pass-1 errors
   (least on hellen R1049 and R1953), and carpio's systematic letter/digit confusions are where agreement misleads most.
6. **The consensus vote barely matters for the newer models.** It helps Sonnet more because Sonnet's errors vary more between
   passes; Fable's consensus is within about 0.5 points of its single-pass mean on most documents.
7. **The models' own "unsure" flags are not comparable:** flagged lines per run were Sonnet 324, Opus 180, Fable 287 of
   about 1,086. They were not scored and should not be relied on.

## Limits
- Same limits as `RESULTS.md`: ten documents, not the frozen 41; one human reference each with its own errors; no expert
  check; the downstream solver test and the Pillon rerun not done.
- Three passes per model, so per-document differences between neighbouring models are often within noise. The pooled
  ordering Fable < Opus < Sonnet holds on every document's mean, but not every gap is clear.
- **Prompts were nearly identical but not byte-identical:** Sonnet's first-pass prompt (first four documents) had a looser
  flag instruction, and the Opus and Fable prompts asked for plain ASCII and the model ID. The Sonnet run came first and
  its ferdinand pass 1 read copies it had rotated itself.
- Model identity is the subagent's own report; the harness `model` option selected it.
- All transcribers saw the same pre-cut tiles. How each model would do on full pages, or on tiling it chose itself, was not tested.
