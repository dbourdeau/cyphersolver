# legation1788: key.tsv and transcription re-applied; the Carmichael read share recounted (Brice Dudout, Claude Opus 5.5, 14 Nov 2026)

`verify_dudout_20261114.py` reads `key.tsv`, `ct/*.txt`, `texts/*` and, for part 4 only,
`transcription/short_17920726_full.tsv`. Run it from `targets/legation1788/`. Part 3 imports `v10_relabel`, which
needs numpy.

## Decoder (Short, 26 Jul 1792, Code No. 10)

`ct/short_17920726.txt` has 674 groups, the same groups in the same order as `texts/short_17920726_decryption.txt`
(grades T 511, E 156, O 7). 471 groups carry a Jefferson value in `key.tsv`, and each of the 471 readings is the
`key.tsv` value or one of its `other_readings`. Another 99 groups are later parts of a word that spans several groups,
and 104 groups have no value in `key.tsv` (the editors' readings and the 7 open groups).

## Key: whole words credited to their first group

`make_key.py` credits a word that spans several groups to its first group. In a two-part code with syllables, this
gives one group several different values. The interlinear points to syllable values in these cases:

| group | key.tsv value | where the group stands | likely value |
|---|---|---|---|
| 1101 | accept (also acquainted, account) | 1101.660 accept, 1101.119.844 acquainted, 1101.1341 account | ac- |
| 689 | conspicuous (also consolation) | 689.957.158 conspicuous, 689.927.523 consolation, 689.1018 consider | con- |
| 562 | -forming (also forms) | 562 forms, 1093.562 inform, 1093.562.1165 in-forming | form |
| 1259 | re- (also remaining) | 1259.1361 re-medy, 1259.844 remaining | re- |
| 1093 | in (also les, in-, inform) | in x7, 1093.562 inform; "les" in 016_0999, over 1093 in the run 1184.1093.574.539.1005 "les intriguants" | in (in-triguants?) |
| 494 | from (also without) | 494.712 from, 494.1076 without; 1388.326 is also without | open |
| 534 | circumstan- | 534.31 circumstances, 1146.534 honourable (last digit of 534 blotted once) | open |

This changes no reading, since every word is still read from Jefferson's interlinear. It does change how `key.tsv`
should be read: as a list of Jefferson's words by first group, not as code values. 494 and 534 do not resolve to a
single value, and checking them would need the LoC images (frames 016_1006 and 016_1007). `key.tsv` is not changed
here.

## Read bar: Carmichael, 14 Apr 1788 (Code No. 13)

The recorded `read_share` of 0.0 counts only the 5 code items, none attested elsewhere. v10 measures
`texts/carmichael_17880414_reading.txt` at 0.974 (38 words, 1 hole) because `v2_score.holes` turns only lowercase or
"?" brackets into holes. The capitalised conjectures `[Maryland]` (twice) and `[Massachusetts]` therefore count as read,
and 597, a number, is not counted at all. The README rule counts supplied `[word]`s as holes. Counted that way (35 clear
words, the 4 conjectures and 597 as holes), the share is **0.875**, under 0.95, so "read in part" stands. The 0.974 is
a v10 artefact. 0.875 is the figure on the README rule if the maintainer prefers a word share to the item share.

Short's letter: v10 gives 0.996 and 0.99 is recorded; "read" is not in question.

## Not done

- No image check. LoC mtj1 009_0230 (597, the blotted 108) and 016_1006-1007 (494, 534) were not fetched.
- The split of Codes No. 10 and No. 13 into two entries (open in NOTES) was not done.
