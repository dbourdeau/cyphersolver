# lima1909: decode re-run and read share recounted (Brice Dudout, Claude Opus 5.5, 14 Nov 2026)

`verify_dudout_20261114.py` reads only `code_values.tsv` and the eight `m*_transcription.txt` files, then compares
with `m*_decryption.txt` and `m*_reading.md`. Run it from `targets/lima1909/`. Part 2 imports
`research/reading_audit/v10_relabel.py`, which needs numpy.

## Decoder

The transcriptions give 409 code items (4 + 30 + 40 + 47 + 101 + 31 + 91 + 65). They are the same groups, in the same
order, as the group column of the eight decryption files. Each group is in `code_values.tsv`, and each value is the
gloss given in the decryption: 409 of 409 agree. The code table and the decodes agree throughout.

## Read bar: why the recorded and measured shares differ

The `read_share` recorded for each telegram is a share of code items: items with a gloss divided by all items. For
example, m0011 is 97/101 = 0.960, m0009 45/47 = 0.957 and m0014 31/31 = 1.0. These figures date from 27 Oct 2026, after
the v10 pass of 24 Oct, so v10 was never run on this target. v10 counts words in `m*_reading.md` instead. Two kinds of
bracket count as holes there although no code item is unread:

- 31 editorial supplements: articles and prepositions the telegraphic style leaves out, such as `[o]`, `[a]`, `[da]`
  and `[vá]`; the restored signature `[Lima]` (m0005); and the expansions `Pres[idente da]`, `G[rã-]C[ruz da]`,
  `[de Honra]` and `P[residente da]`;
- doubt marks written as `[?]` after a word that has a gloss (m0011 "combinação [?]", "Aguardando [?]"). v10 counts
  each of these as a hole and does not count it as a doubtful word.

| doc | recorded | v10 as published | v10 without the editorial supplements | real holes in the reading |
|---|---|---|---|---|
| m0001 | 1.0 | 0.973 | 1.0 | 0 |
| m0005 | 1.0 | 0.950 | 1.0 | 0 |
| m0007 | 0.975 | 0.973 | 0.991 | 50667 |
| m0009 | 0.957 | 0.926 | 0.970 | 18703, 10586 |
| m0011 | 0.96 | 0.904 | **0.937** | 595191, 85178, 70706, 43243, 48696 Hen[daya?], plus 2 doubt marks |
| m0014 | 1.0 | 0.868 | 1.0 | 0 |
| m0018 | 0.989 | 0.935 | 0.981 | 33125, plus "jantar" doubtful |
| m0020 | 0.985 | 0.878 | 0.963 | 83636, 05068 and 19313 doubtful |

With the supplements left out, seven telegrams are at 0.963 or higher. **m0011 stays under 0.95 (0.937).** It has
4 open groups and the doubtful "Hen[daya?]", and its decryption marks 8 more glosses "?". By the word rule it would be
read in part; by the item count it is at 0.950-0.960. The class is unchanged here; that is the maintainer's decision.
Mid-word brackets such as `G[rã-]C[ruz da]` are counted by v10 as part-word holes, the known v10 artefact for
expanded abbreviations.

## Not done

- Image check: the DigitArq scans of the faint glosses (m0009 18703 and 10586, m0011 line 7, m0020 83636) were not
  fetched.
- No new readings were made for the open groups.
