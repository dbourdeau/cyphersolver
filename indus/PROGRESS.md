# Decipherment progress: the metric and the loop log

Started 24 September 2026 at the owner's request: loops of registered hypothesis tests aimed at deciphering the texts,
with a progress metric measured the same way every loop (`progress.py`, log in `results/progress_log.tsv`).

## The metric

Decipherment happens in stages, so the metric is a vector, one component per stage:

| Component | What it measures | Direction |
|---|---|---|
| S structure | held-out bits per sign on a fixed 80/20 split (seed 2026) of the distinct lines, best registered model | lower |
| R roles | share of sign tokens whose job is fixed by a tested rule (numeral, ending, closer, marker, heading, name head, counted sign ...) | higher |
| M meanings | share of sign tokens whose sign has an externally anchored meaning (numeral values, copper-tablet sign = picture equations) | higher |
| P sound values | signs with a sound value that passed a registered held-out test (the prize) | higher |
| L language | candidate language families not yet excluded by registered tests | lower |

A component moves only when a registered set supports the change. S and R are the tractable parts; M needs outside
anchors; P and L need outside evidence, and a real decipherment would show first as P > 0 with S falling (a reading
makes the texts more predictable) and M rising.

## Log

| Loop | Sets | S bits (explained) | R roles | M meanings | P | L open | Note |
|---|---|---|---|---|---|---|---|
| baseline | 1-175 | 4.712 (24.9%) | 56.2% | 16.6% | 0 | 4 | model tri + pos + end, discounted (set 125) |
| 1 | 176 | 4.712 (24.9%) | 72.9% | 16.6% | 0 | 4 | role / class / numeral-value components add nothing to S; slot-based modifier role adopted in R |
