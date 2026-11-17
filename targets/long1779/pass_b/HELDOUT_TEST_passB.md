# Clean held-out test, pass B (written 13 Nov 2026 before running)

Key: the first agent's `key_frozen.json`, unaltered (sha256 aaafa6c11f174bed54228fdfea8e2b4b6af32a94111f24c0cdab6c9b2803df9e), built from images 11, 13R, 14L, 14R.
Text: my blind transcription `passB.tsv` (sha256 in FREEZE_passB.txt, frozen before I opened the first agent's folder), cipher words of System A pages the key was not built from: images 15L, 15R, 16L, 18R, 19L, 22L, 29. Words of two or more signs; plain words, struck words and the second-alphabet pages excluded.
Sign correspondence (my shape code -> first agent's glyphs), fixed in step 4 from the glyph descriptions, not from readings: z->{=,3}; i->{1,.,\}; o->{o,A}; - ->{-}; t->{t}; h->{t\} (two signs); g->{g}; l->{l}; . ->{.}; w->{~}; r->{v,\}; 8->{B,d,c}; f->{y}; + ->{+}; L->{t}; v->{^,j}; F->{+,p}; a->{A}; p->{p}; s->{j}; c->{c}; u->{A}; 2->{=,3}; other codes -> unknown.
Because my codes merge some signs, a word counts as English if any of its expansions under the key is in the lexicon (repository `lang/lexicons/en.json.gz` plus: molly, kimball, newbury, bartlett, bartletts, tivertown, sergt, corpl, inst, capt). Words with more than 4096 expansions count as misses.
Null: 200 keys made by shuffling the frozen key's letter values among its glyphs (seed 1780), scored the same way, with the same expansions.
Pass, stated in advance: frozen-key share at least 35% AND above the 99th percentile of the 200 shuffled shares. Expected: the expansions raise the shuffled scores too, so the margin, not the raw share, is the result.
