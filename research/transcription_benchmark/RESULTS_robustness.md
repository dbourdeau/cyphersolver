# Transcription benchmark: robustness checks (19-20 Nov 2026)

Five checks run before writing the HistoCrypt paper, on the ten documents and 90 passes (Sonnet 5.5, Opus 5.5,
Fable 5.2; three blind passes each) reported in `RESULTS.md`, `RESULTS_opus.md` and `RESULTS_fable.md`.

## 1. Who is right when the AI and the human reference disagree? (`adjudicate.py`, `adjudication/`)
**Pipeline.** `extract` aligns every reference with all nine AI readings and takes the places where a majority of the
nine agree on something other than the reference (332 disputes after merging neighbours), plus a calibration sample of
60 places where only one or two readings differ. `batches` writes blind sheets: a crop of the page, the context, and
the two readings as A and B in random order. Each sheet was answered independently by an Opus 5.5 and a Fable 5.2
adjudicator (784 verdicts). `apply` counts a verdict only where both agree and re-scores all 90 passes against the
reference corrected where they sided with the AI. `review` writes a sheet for a person to check the adjudicators.
Re-running on new transcriptions is the same four commands.

**Adjudicator agreement:** 299 of 392 items (76%).

| | sided with the human reference | sided with the AI | split | neither |
|---|---|---|---|---|
| Disputes (332) | 116 | 127 | 86 | 3 |
| Calibration (60) | 52 | 1 | 7 | 0 |

- **The calibration sample is the control.** Where only one or two AI readings deviate, the adjudicators back the
  human reference 52 times to 1, so they do not simply side with the AI.
- **Where most AI readings agree against the reference, the reference is wrong about as often as the AI.** 127 agreed
  verdicts for the AI against 116 for the human. The corrections change 154 of 14,495 reference signs: **an estimated
  reference error rate of about 1.1%**, a lower bound (the 86 split items are not counted). It is highest for hellen
  R1049 (2.6%) and carpio (1.5% to 1.8%), lowest for santacroce R6 (0.4%).

**Error rate against the adjudicated reference** (pooled, with the 95% bootstrap interval):

| | original reference | adjudicated reference |
|---|---|---|
| Sonnet 5.5 | 5.1% | 4.2% (2.4 to 7.1) |
| Opus 5.5 | 4.1% | 3.1% (1.5 to 6.0) |
| Fable 5.2 | 3.3% | 2.4% (1.1 to 4.6) |
| Fable 5.2, digit-only documents | 2.0% | **1.1%** (0.6 to 1.7) |
| Fable 5.2, letter-and-digit documents | 7.2% | 6.3% (2.0 to 12.6) |

Per document (original / adjudicated): hellen R1049 Fable 4.6 / 2.1, Opus 4.8 / 2.3, Sonnet 9.6 / 7.4; hellen R1953 Fable
0.9 / 0.4; santacroce R7 Fable 0.9 / 0.4; carpio R1009 Fable 14.0 / 12.6 (`adjudication/summary.json`).

**What it would mean, if the adjudication held** (it did not survive the person's check in 1b): on the digit documents,
Fable's error against the adjudicated reference (about 1.1%) would be in the same range as the estimated error of the
human references themselves. Carpio stays the outlier at 12% to 16% for every model either way.

**Limits of this check.** The adjudicators are AI models of the same family as two of the transcribers; the
calibration control argues against a pro-AI bias but does not exclude a shared misreading. A person should check the
review sheet (`adjudicate.py review`, 40 random items with crops; it embeds DECODE images, so it is kept local).
Splits (22%) are left uncorrected. Only majority disputes were adjudicated; places where the AI readings disagree
among themselves were not, so the reference error rate is a lower bound.

### 1b. A person checked the adjudicators, and they did not hold up (20 Nov 2026)
The user answered a blind spot-check app (`adjudicate.py app`; answers `adjudication/person_answers.json`, key
`adjudication/person_check_key.json`, scored by `adjudicate.py score-app` into `adjudication/person_check.json`):
70 items, each showing a close-up of the page with the disputed sign outlined in red (the outline located by a vision
model from the surrounding signs only, never the readings; `adjudication/spot_boxes.jsonl`) and the two readings as A
and B, without saying which was human or AI.

- **40 items the two AI adjudicators had agreed on:** the person agreed on 13, disagreed on 14, could not tell on 13.
  On the 22 where the person chose one of the two readings: 13 agree (59%), 9 disagree (5 where the adjudicators had
  sided with the AI, 4 where they had sided with the human).
- **30 items the adjudicators split on:** the person sided with the human reference 13 times, the AI 6, neither 3,
  could not tell 8.
- Agreement with each adjudicator where the person decided: Fable 25 of 41, Opus 20 of 41.

**Conclusion: the AI adjudication is not validated.** Agreement with a person is little better than chance on the
decided items, and both the person (a third undecided) and the two models (a quarter split) find these places hard.
The adjudicated error rates in section 1 and the estimated reference error rate of about 1.1% must not be reported as
established; at most they show how much the numbers could move if part of the disputes are reference errors.
**The paper should report the error rates against the original DECODE reference** (section 2) and treat reference
error as an unmeasured limit that needs expert adjudication (a palaeographer or the DECODE transcribers).
Caveats on the check itself: one person, not a specialist in these hands; some "neither" answers (11) may come from
outlines that fell on a neighbouring sign; 70 items.

## 2. Confidence intervals and paired tests (`stats.py`, `stats.json`, `stats_adjudicated.json`)
Hierarchical bootstrap (documents resampled, then passes within each document; 10,000 draws), differences paired
by document, and a sign test over documents.

| Comparison (all ten documents) | difference, original ref. | 95% CI | documents where the second is lower | sign test |
|---|---|---|---|---|
| Sonnet minus Opus | +1.0 pts | +0.1 to +2.2 | 7 of 10 | p = 0.34 |
| Sonnet minus Fable | +1.8 pts | +1.0 to +3.0 | 10 of 10 | p = 0.002 |
| Opus minus Fable | +0.8 pts | +0.4 to +1.5 | 10 of 10 | p = 0.002 |

- Fable is lower than both other models on every one of the ten documents; that holds against the adjudicated
  reference too (same signs, same p).
- Opus beats Sonnet on all six digit-only documents (p = 0.03) but not on the letter documents (difference −0.4
  pts, CI −1.7 to +1.0, 1 of 4 documents).
- Intervals on pooled rates are wide (Fable 1.8% to 5.7% on the original reference) because ten documents vary a lot;
  the paired differences are tighter.

## 3. Human effort against AI time (`effort.py`, `effort.json`)
DECODE records how long each human transcription took: 30 minutes (dandini R72) to 4 h 40 (hellen R1049), **22.6 hours
for the ten documents** (one, santacroce R6, used speech recognition). For the eight documents with a recorded Sonnet
time, the AI took **5.7 minutes per pass against 1,035 human minutes, about 180 times faster**, at roughly 100,000 to
125,000 tokens per two-document agent. Opus and Fable timings were not recorded in this session. The comparison is
wall-clock only: the human also typed DECODE's conventions (marks, clear text), which the AI was not asked to do.

## 4. Does the setup move the score? (`prep_variants.py`, `sensitivity.py`, `runs_sensitivity/`)
One Fable pass per variant on santacroce R7, hellen R1049 and carpio R1009, against Fable's three baseline passes.

| Document | baseline, 3 passes (orig / adj) | full page | 600-px bands | reworded prompt |
|---|---|---|---|---|
| santacroce R7 | 0.7-1.1% / 0.2-0.6% | 0.8% / 0.4% | 1.3% / 0.7% | 1.4% / 0.8% |
| hellen R1049 | 4.4-4.7% / 2.0-2.2% | 5.4% / 3.1% | 4.8% / 2.4% | 4.8% / 2.2% |
| carpio R1009 | 12.3-15.4% / 10.9-13.9% | 12.9% / 12.2% | 16.8% / 15.5% | 15.0% / 13.7% |

Setup choices move a single pass by up to about 1.5 points on the hard documents and 0.5 on the clear one: less than
the Sonnet-to-Fable gap (about 2 points) but comparable to the Opus-to-Fable gap. Full-page images work about as well
as tiles at this resolution; narrower bands were worse on carpio. One pass per variant, three documents: indicative only.

## 5. Could the models have seen the references? (`contamination.json`)
All ten DECODE records are set to "Authentication required". Requested without a login, every reference
transcription returns DECODE's 17,947-byte forbidden placeholder; with the stored login cookie the same file opens
(R7: 4,202 bytes of text). An ordinary web crawl would not have collected these transcriptions. This lowers the
contamination risk; it does not exclude it (registered users can download them; parts may be quoted elsewhere).

## Sample selection (for the paper)
The ten documents are those with a clean pairing of a DECODE human transcription and page images of the same record,
chosen after an audit of a frozen 41-document sample whose frame turned out too loose (`RESULTS.md`, Limits). They are
a convenience sample: about six hands, mostly Italian and French, two letter-cipher hands, 1552 to 1754.
