# Partial reconstruction of Van Spaen's Vienna code

A 93-entry candidate table fitted to G. C. van Spaen’s dispatch of 21 March 1807 made word predictions for two other dispatches. **32 of 43 predictions** matched the 28 March period decipherment within the prescribed position window. On the 14 March dispatch, **48 of 61 predictions** matched. The best of 1,000 shuffled tables scored 16 and 20, respectively. Both contemporary French decipherments survive. This local evidence draft concerns the reusable marked numerical code. [Nationaal Archief, Foreign Ministry, inventory 248](https://www.nationaalarchief.nl/onderzoeken/archief/2.01.08/invnr/248)

| Dispatch | Source scans in inventory 248 | Cipher positions accepted / all | Positions assigned a candidate | Prospective word matches | Best shuffled score |
|---|---|---:|---:|---:|---:|
| 21 March, No. 23, training | 2 right, 3 left, 5 right, 6 left; period copy on 3–5 | 721/745 | — | — | — |
| 28 March, No. 26 | 173 right and 174 left; period copy 174 right and 175 left | 329/355 | 72 | 32/43, 18 distinct forms | 16 |
| 14 March, No. 21 | 14–17; period copy 15–16 | 430/432 | 82 | 48/61, 20 distinct forms | 20 |

Two independent readers saw only cipher panels. Each type comprises the number, superscript and any trailing stroke. Each unresolved position remains in the count. Two monotone alignments of No. 23 to its French copy allowed whole words and fragments. A candidate needed the same unique most frequent segment under both settings, with at least two fit occurrences and support in at least two thirds of its occurrences under each. The table includes 53 whole-word values and 40 fragments. The test of No. 26 then froze all predictions before the scorer used its separately sealed reference. After that test, the exact same table went into a new prospective test on No. 21. Each custodian comparison used its own prepared French reference. The fitting investigator had previously seen a small spread of scan 174 while checking the date and layout, including the page bearing part of the French copy, without transcribing the body. [Fit and first transfer protocol](march/PLAN.md) · [Fixed-key second protocol](march14/PLAN.md)

The scoring program required exact normalized French tokens in order, allowing each reference token to be used once. The predicted and observed centers had to fall within four percentage points of document length. Apostrophes split tokens, so *qu* can count. Each test required eight predictions, five matches, four different matched forms and a score above every shuffled control. These are measures of prediction accuracy with a location tolerance. The tests did not determine a fraction of cipher words read. On 14 March there was one prospective complete word assembled from two fragments, *reront*. It missed. [28 March results](march/transfer_result.json) · [14 March results](march14/transfer_result.json)

## Individual candidates

| Marked number | Reading | Matches / predictions, 28 March | Matches / predictions, 14 March |
|---|---|---:|---:|
| 224, two dots | aussi | 2/2 | 1/1 |
| 293, cross | guerre | 2/2 | 1/1 |
| 723, two dots | cette | 2/2 | 3/3 |
| 82, cross | de | 2/2 | 1/2 |
| 859, ring | qu | 4/4 | no opportunity |
| 9, v-mark | que | 2/2 | 2/5 |

These six matched every predicted occurrence, with at least two nonoverlapping position windows, on the first held-out letter. The second letter supported *aussi*, *guerre* and *cette* at every opportunity, and weakened the case for *de* and *que* under the same rule. Short common words can match by accident. In No. 26, cipher positions 90–92 predicted *guerre, et, qu*, matching consecutive reference tokens 53–55. In No. 21, positions 246–248 predicted *que, pour, la*, matching consecutive tokens 157–159. The aggregate evidence supports transfer of the code; individual entries remain candidates for exact manual alignment. [Every prediction by code](march14/cross_letter_support.tsv) · [28 March matched positions](march/transfer_matches.tsv) · [14 March matched positions](march14/transfer_matches.tsv)

## January miss and prior work

No. 7 of 24 January 1807 is a different experiment on scans 105–106. Its within-letter position model proposed five tokens and matched just two occurrences of *de*. Of 1,000 shuffled controls, 226 equalled or exceeded that score; the highest was four. The investigator had seen the known French copy before this within-letter split. No January value entered the March table. [January protocol](january/VIENNA_PLAN.md) · [January result](january/vienna_result.json)

The project’s 14 November 2026 survey (Van Spaen 1808, inventory 248, “cipher survey,” and inventory 204A, “notes 211–274”) had already identified nine Vienna dispatches with period copies. It reported approximate group counts and samples. Two new cipher-only readings corrected seven of its first ten numbers for No. 7. The survey also dated No. 26 to 20 March. The manuscript dateline on scan 173 reads 28 March and the separate inventory 204A entry agrees. The 227 for *armée* attributed in the earlier summary to Vienna belongs to a Munich dispatch of 15 October 1807 lower on inventory 204A scan 254. The sparse 204A period corrections were excluded from fitting and scoring. [Inventory 248](https://www.nationaalarchief.nl/onderzoeken/archief/2.01.08/invnr/248) · [Inventory 204A](https://www.nationaalarchief.nl/onderzoeken/archief/2.01.08/invnr/204A)

The repository already has the distinct *spaen1808* target, the Düsseldorf correspondence using unmarked code groups in inventory 281. Its *batavia1800* target concerns Smissaert and a different cipher. The locally saved 19 November check included 902 target-directory names, with no *spaen1807*, and an issue/PR name search for “Spaen” returned zero. This bounded check does not establish historical priority. Neither the existing Düsseldorf key nor Van Kampen's different St Petersburg material provides an independent reading of the Vienna messages. [Existing Düsseldorf work](https://github.com/dbourdeau/cyphersolver/tree/fe637468dc7d728abca6bec06bfe8b8112508fef/targets/spaen1808) · [Separate Batavia example](https://github.com/dbourdeau/cyphersolver/tree/fe637468dc7d728abca6bec06bfe8b8112508fef/targets/batavia1800)

## Checks against the working decipherments

After scoring, two blind readers working independently on the annotation sheet examined the clerks’ marks in inventory 204A. On scan 253 right both favored cross-marked 238 below a struck word corrected to *on*. The number and word agree with both No. 23 training paths at position 309, where the predeclared rule had excluded the once-occurring code. On scan 254 left both preferred cross-marked 710 near *justement*; *du jour* is on the following line. The note withdraws the earlier attribution of *du* to cross-marked 718. The two other local annotations and the difference between *On donnera* and *on leur donnera* are described in the appendix. These checks took place after the two tests and did not alter either key or score. [Post-score manuscript appendix](appendix/NOTES_working_copy.md)

AI agents did this work; no person has checked it.
