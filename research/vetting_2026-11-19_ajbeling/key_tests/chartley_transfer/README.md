# January controls and the September comparison

Charles Paget’s letter to Mary of 4 January 1585 has both a cipher at SP 53/15 f. 6r and a period decipher on f. 7r. Tomokiyo identifies SP 53/22 f. 47 as the key. The shorter old 97a sheet preserves much of the same alphabet. The first, strict short-key control missed at eight of 109 positions. A subsequent descriptive audit of those recordings found 55 identical tile choices and 30 adjacent pairs after admitting medium-confidence choices. Distinct tiles with equal values added zero placements. The strict result stands. [Original control](../january_control/README.md) · [Cipher](https://link.gale.com/apps/doc/MC4307883976/SPOL) · [Decipher](https://link.gale.com/apps/doc/MC4307883977/SPOL) · [Key](https://link.gale.com/apps/doc/MC4322680002/SPOL)

On the next January row, two readers independently compared an entire row with 84 anonymously permuted specimens from the fuller Chartley manuscript. Usable values required agreement on the historical entry’s kind and value at medium or high confidence. Agreement on null and doubling signs left a break. Of 110 aligned positions, 86 supplied usable values, yielding 69 adjacent pairs. An independent transcription of the first eight lines of the period decipher covered the salutation and body. The reference maker had previously seen the opening three lines. The sign assignments on row two remained withheld when the plan was frozen. Eight ordered, nonoverlapping fragments of four or more characters matched 49 reference characters. The highest of 1,000 shuffled tables matched 15. The fragments include the five letters of “he did” and the nine-letter fragment “thcatholi” spanning parts of “wth Catholikes”. Spelling, holes and sign boundaries were preserved. This passed the January control. [Plan](january/PLAN.md) · [Exact boundaries and fragments](january/excerpts.tsv) · [Results](january/reference_results.json)

The September letter lacks an independent decipher. The test therefore asked how well the historical assignments predicted the first letter of the next adjacent unit using an independent sixteenth-century English corpus. Whole-word entries earned no points from letters inside them. Two known January rows passed this language check. Three September comparisons using earlier and fresh sign readings are shown below. The minimum usable coverage was 40%, with at least ten adjacent pairs and six different ordered pairs. A September score also had to exceed all 1,000 randomized keys. Randomization preserved homophones and shuffled word and letter entries separately.

| Row sample | Usable / all positions | Adjacent pairs | Shuffles equal or better |
|---|---:|---:|---:|
| January, short table | 55/109 | 30 | 0 |
| January, fuller table | 86/110 | 69 | 0 |
| September, short table, three strips | 22/136 | 3 | 608 |
| September, short table, fourteen rows via sign atlas | 94/579 | 10 | 378 |
| September, fuller table, newly matched lower row four | 22/57 | 9 | 10 |

The fourth row of the lower block was chosen before language calibration because it had the most positions in the earlier coordinate union. In the fresh reading, one reader marked 57 centers and the other 52. Of 25 exact tile agreements, three represented special signs and 22 supplied usable values. This gives 38.6% coverage. The nine adjacent pairs were all different. The language score was −3.202, against −2.649 for the strongest shuffled key. The study had already tried several comparisons on this manuscript. The rank of this nine-pair result does not establish the table or any September word. [Plan](september/PLAN.md) · [January language results](january/language_results.json) · [Earlier September readings](september/legacy_results.json) · [Fresh September result](september/result.json)

## Reproduction

From the repository root, run the command below. The Python standard library rebuilds the English probabilities from the repository’s copy of the Unton correspondence, validates its SHA-256 digest, and reruns the six 1,000-key comparisons. It checks the reference fragments and all five language scores, coverages and permutation ranks. The anonymous lookup tables give each specimen’s source center and crop dimensions in the working table image. The manuscript links identify the originals. The holding service supplies the source images. [Plan timestamps and specimen hashes](TIMESTAMPS.txt)

```sh
python3 -I -B research/vetting_2026-11-19_ajbeling/key_tests/chartley_transfer/verify.py
```

AI agents did this work; no person has checked it.
