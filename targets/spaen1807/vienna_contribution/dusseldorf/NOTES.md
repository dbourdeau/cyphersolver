# Could Van Spaen's marked Vienna values be reused as bare numbers at Düsseldorf?

**Indeterminate on the known 15 January 1808 dispatch, No. 6.** Removing superscripts from the 93 frozen March 1807 candidates produced 89 bare numbers. Of these, 44 have one unambiguous whole-word value of two or more characters within that limited table. Only two predicted forms occur at eligible positions in No. 6. The plan required at least eight occurrences and four different words before any scoring. [Plan](PLAN.md) · [Dated hashes](FREEZE.txt) · [Result](result.json)

| No. 6 position | Bare number | Vienna source | Prospective form |
|---:|---:|---|---|
| 26 | 228 | cross-marked 228 | et |
| 71 | 502 | ring-marked 502 | pas |

A third bare number, 956 at position 58, has only an initial fragment in the Vienna table and supplies no whole word. The two proposed words above are **unverified projections**. The test stopped before the period French copy was consulted and before any shuffled keys were compared. [Every position](slots.tsv) · [Original types and exclusions](bare_numbers.tsv) · [Predictions](predictions.tsv)

## Inputs and order of work

The plan and its hashes were written at 22:21:19 UTC on 19 November 2026, before the overlap was computed. [FREEZE.txt](FREEZE.txt) lists four files by their paths in my working folders. All four are here, with the same hashes:

| Path in FREEZE.txt | In this repository |
|---|---|
| `output/codex_2026-11-17b/nov19_late/spaen1808_projection/PLAN.md` | [PLAN.md](PLAN.md) |
| `output/codex_2026-11-17b/nov19_late/shortlist/march/key.tsv` | [../march/key.tsv](../march/key.tsv) |
| `sources/research-repo/targets/spaen1808/annex_groups.txt` | [targets/spaen1808/annex_groups.txt](../../../spaen1808/annex_groups.txt), the repository's earlier transcription of the No. 6 annex |
| `output/spaen1808_2026-11-14/transcription/annex_pass2.txt` | [annex_pass2.txt](annex_pass2.txt), the second reading of No. 6 made on 14 November 2026 by a helper agent in my survey, from Nationaal Archief 2.01.08 inv. 281, scan 85 |

Both numeric witnesses to No. 6 contain 75 positions. Their first choices agree at 65; ten numbers differ, and one more position has the explicit alternative 553/555. The 14 November reading records four baseline strokes, one on a position already excluded for a numerical disagreement. This leaves 61 comparable positions with unqualified agreement and no stroke. My 14 November notes call the second reading independent. Whether its reader had seen neither key nor plaintext is not documented, so the coverage figure is an upper bound.

[screen.py](screen.py) is the script run at 22:21 UTC. Only its three input paths and its explicit encoding arguments have been changed; its four outputs here are the files written then, byte for byte, and `verify.py` regenerates and compares them.

This result supplies no evidence for applying a bare-number Vienna table to the unread Düsseldorf dispatch No. 4. No. 4 was not opened. Later changes of key, renumbering and the full historical vocabulary remain unresolved.

AI agents did this work; no person has checked it.
