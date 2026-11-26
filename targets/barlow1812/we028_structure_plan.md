# barlow1812: test of the open numbers against the order of the surviving State Department sheet (plan)

Written 24 Nov 2026, 13:55 UTC, by an AI agent for the maintainers (write-up round 6), before any value was computed
for an open number. Seen before writing this: that 584 of the 623 values of `key.tsv` are entries of the State
Department code sheet at NARA M97 roll 13 (Weber's WE028, the = 1385; transcription in
`../morris1813/beling/key/codebook_M97_13_transcription.csv`), that no number has the same value in both codes, and the
WE028 numbers of the `key.tsv` values for Barlow numbers 100 to 330 (the difference between the two numbers stays the
same over short runs: 133 ti, 137 tin, 138 tion are 560, 564, 565 on the sheet). Not seen: the sheet entry any open
number would fall on.

Question. Both codes look like renumberings, run by run, of one alphabetical list. If so, an open Barlow number that
stands between two valued neighbours of the same run is the sheet entry at the same distance.

Rule, fixed here.

1. Anchors: the numbers of `key.tsv` with a value of grade P, C, D or W whose value (letters only, lower case) is the
   reading of exactly one sheet entry. Offset of an anchor = sheet number minus Barlow number.
2. For a number n, take the nearest anchor below and the nearest above, each at most 8 away. If both exist and have
   the same offset, the prediction is the sheet entry n + offset ("interpolated"). Otherwise the candidates from each
   side are listed ("one side" or "offsets differ") and no value is claimed.
3. Control: every anchor is left out in turn and predicted from the others by rule 2. The method is usable if at
   least 100 anchors get an interpolated prediction and at least 95% of those equal the value the anchor has in
   `key.tsv`.
4. The nine open numbers (815, 1567, 1404, 624, 706, 103, 163, 531, 537) are then run once. A value so found is
   grade I (inferred from position, README Conventions): it is kept out of `key.tsv`, does not change the read
   count, and is set beside the proposal from the sense in `proposals.tsv` as agrees / differs / no prediction.
