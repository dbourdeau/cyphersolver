# Held-out test of key MAP LXXII 183 on Ridolfi, MAP LXXIV doc. 114 (22 Oct 1494)

Written 14 November 2026, before any image of the cipher leaves of doc. 114 (c. 258v, 259r, 259v), and before the
printed text (Desjardins, Négociations diplomatiques, t. I, 1859, pp. 585-586), was opened by the session that
writes this file and runs the scoring. That session has seen c. 258r (clear text only) and the two plaintext
fragments quoted in cyphersolver issue #589.

## Fixed inputs
- Key: `milan-1494/key.json` at commit 46dec7b, sha256 91472a7f7d59eb71836fbb74da29f98bc65e4eafaa298d77a37f86c230eb13d4.
  No value is added or changed for this test.
- Transcription: made by an agent that sees only gloss-masked line crops of doc. 114, the label and shape inventory
  with all values removed, and Ridolfi's bare letters 112, 113, 115 with their label sequences as shape exemplars.
  It does not see the gloss, the key values, the issue, the README, or the printed text. A different agent locates
  the cipher lines and paints out the interlinear gloss. The transcription file is frozen and its sha256 appended
  below before the decoder is run on it. No re-transcription after scoring.
- Reference: the printed text of the ciphered passages (Desjardins), fetched after the freeze. Which printed words
  are cipher is decided from the clear words that bound each cipher block on the leaf.

## One measurement
Character agreement between key output and reference, per the rules below, over all cipher blocks together.

- Normalisation, both sides: lower case, letters only, accents stripped, j = i, v = u. Editorial expansions printed
  by Desjardins stay as printed (they count against the key if the cipher abbreviates).
- Key output: each sign gives its value(s) in key.json; nulls give nothing; code signs give their word; person signs,
  name numbers and unidentified signs give one wildcard character that never matches.
- Multi-valued signs (÷ = n/c, the d/l class, and the others listed with several values): the sign matches if the
  aligned reference letter is any of its values.
- Alignment: global alignment (unit cost for substitution, insertion, deletion) of the output sequence against the
  reference, per cipher block. Agreement = matched positions / max(output length, reference length), summed over blocks.
- Null distribution: 1,000 shuffles in which the value sets are permuted among the sign labels that occur in the
  transcription and carry at least one letter (so a multi-valued set stays a set and gets the same any-of rule).
  Report the best and the mean shuffle.
- Bar: 0.85, the figure Brice Dudout used for the same letter. Reported whatever it is.

Secondary, descriptive only: the same agreement with every multi-valued sign forced to its first listed value; and
the count of words that come out exact.

## After the measurement
Doc. 114's gloss is then used as an exemplar set (d against l, ÷ for n against c, the doubled-consonant signs). From
that point 114 is no longer held out.

## Frozen transcription
(appended at freeze)
- transcription-frozen.tsv sha256 98f1ec21e6a1ae01b8dace0923195d225d44684d174d98f5086a2d7ad8828c96 (865 signs, 14 Nov 2026), frozen before the printed text was fetched or the decoder run.
- score.py sha256 439bd0eae873ee9038f70e1f5d6f1a125533595d583970ed205d667a03bc5401.
- Alternatives in braces and ? marks in the transcription are ignored by the scorer: the first shape reading is used.
