# Frozen plan: do the new upstream Mexican keys read our three federal telegrams?

Written by an AI agent (Claude Opus 5.5), 22 Nov 2026, 21:20 Eastern, before any decoding with these keys. Nobody has checked it.

## Question

Do any of the keys that appeared upstream from 6 to 22 Nov 2026 read our three telegrams in catalogue 1468 (CEHM DLXXIII.1.32.5-41, Rubio, 14 Oct 1913; DLXXIII.1.32.6-41, Rubio, 15 Oct 1913; DLXXIII.2.41.22-41, Blanquet, 19 May 1914)? Expected answer: no. These keys come from the other side (the Maderista junta of 1911, Villa's camp in 1914, Bernardo Reyes's circle in 1909) and differ in structure from our tables. The test is cheap and closes the question.

## Ciphertext (frozen; copies in `ext/`)

- `ext/oct14.runs`, `ext/oct15.runs`, `ext/may19.runs`: the transcriptions from our held patches (`output/codex_2026-11-17b/batch18d/held_bundle/mexico.patch` and `blanquet.patch`), unchanged. One cipher run per line. `?` = illegible group.

## Keys under test (no value added, changed or fitted)

1. **K-LIM**: `targets/limantour1909/key.tsv` (upstream main 7d9b91fb8), numbers to letters. The two phrase codes 77 and 79 are left out.
2. **K-VIL**: `ext/villa1914_key.tsv`, taken from pull request 865 (read with `gh pr diff`). Merge rule: use the March value. Where March has none, use the June pencil-aligned value. If two filled columns disagree, leave the number unassigned.
3. **K-SYL-RC** and **K-SYL-CR**: the two-digit syllabary card CMXV.16.1557.1 scan 3, as Daniel Jalkut set it out in `targets/duron1911/siblings/syl.py`. RC reads each group as row then column, CR as column then row. Only groups written with exactly two digits are mapped. Groups with one or three digits stay unassigned. No digit offsets are tried.

The letter-for-letter cards (Hernández swap, Clave G.A., Herrera Moreno, Dallas, the turning grille, Durón's shift) turn letters into letters. They cannot apply to number groups, so they are declared inapplicable and are not run.

## Positive controls (must pass, or the test is void)

- **P-OCT**: our frozen 78-entry October table `ext/candidate15.tsv`, applied to oct14 and oct15.
- **P-109**: upstream `targets/rubio1913/key.tsv` (Clave núm. 109), applied to may19.

## Statistic

- Spanish letter-trigram model from upstream `targets/esp318/lit/quijote.txt` (Gutenberg header and footer cut at the START/END markers). Alphabet a-z plus ñ, accents stripped, add-one smoothing.
- Decode each run group by group. An unassigned group or `?` breaks the run into separate stretches.
- Score = mean log-probability of the trigrams within stretches that cross at least one group boundary.
- At least 10 such trigrams per telegram, or that key/telegram pair is reported as "too little coverage to test".

## Controls

1,000 shuffles per key and telegram. Each shuffle permutes the plaintext values among that key's own numbers, so coverage stays the same. Random seed 20261122.

## Pass mark (all three needed, per key and telegram)

1. The observed score beats at least 999 of 1,000 shuffles. Ties count against.
2. At least 30% of the cipher positions are covered.
3. At least two different Spanish words of five or more letters, each spanning two or more groups, in different runs. Words are taken from the Quijote word list (seen at least 3 times). As a check, the same word count is also reported for the shuffled keys: the 99th-percentile control count must be lower than the observed count.

Twelve tests are run (4 keys × 3 telegrams). A single pass is a hit and is reported with its words. A pass only shows "decoded". It counts as "read" only if the output builds sentences.

Also reported, descriptively, without a pass mark: for each number that both keys share, whether the external key gives the same letter as our October table or Clave 109.

## What would change our conclusion

- A hit by any external key would mean shared key material across the factions. That would be surprising, and it would need a fresh second transcription before any use.
- A miss confirms that our readings stand on their own keys.
