# Second held-out test (written 14 Nov 2026 before running)

Key under test: `key/key_positions.json`, sha256 `36276e0a73f3dd58d8940202b7c97033fb706bb576317083a083a2808744ae74`
(from the printed Vattel passage, Dumas's line totals and Tomokiyo's transcription of the Committee's table; NOT built from any gloss).

Held-out page: PCC item 93 vol. 1 (naId 502964761) image 0173, "Copie de ma Lettre ... 27 Juillet 1778" with the reply of 31 July:
a contemporary decipherer's letter written over nearly every number. This page was not used in the first test (which used M332 images
9, 10, 13 to build a key and 20 to test it) and is a different letter. Gloss data: pass A transcription `transcriptions/R3_A/img0173.txt`
(the only pass that recorded glosses on every number), taken as transcribed, glosses marked `?` included and flagged.

Score: share of glossed numbers whose key character equals the gloss letter (accents ignored; a gloss "=" counts as the hyphen; x is
scored as a miss). Report all, and separately excluding glosses marked "?".
Null: 200 keys made by shuffling the 682 key characters among the positions (random seed 20261114); same score for each.
Pass criterion stated in advance: real score >= 90% and above the maximum of the 200 shuffled scores.
Caveat stated in advance: the G2 reading agent had already decoded image 173 with this key before this plan was written (it reported 100%
read); what is new here is the number-by-number comparison of the key with the 1778 decipherer's glosses, and the shuffle null.
