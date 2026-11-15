# Test 1 (first reading, 14 Nov 2026)

A key built from the contemporary glosses on M332 images 9, 10 and 13 (`pairs.tsv`, 342 numbers, frozen in
`key_frozen.json`, hash recorded in `TEST_PLAN.md` before the run) was scored against the glosses on M332 image 20.
Result (`heldout_result.json`): 106 of 108 covered numbers agree after one transcription correction checked on the image
("519" is 515); 105 of 108 as first transcribed (`heldout_run1_as_transcribed.txt`). 200 shuffled keys: mean 7.9%,
max 14.8%. The two remaining disagreements are 250 (gloss alignment uncertain) and 545 (a real conflict between Dumas
and the decipherer). Not blind: one agent transcribed both the training pages and image 20.
`key_full.json` is the gloss key from all four pages, used by `../../key/build_key.py` to compare with the printed key.
