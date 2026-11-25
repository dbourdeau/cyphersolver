# METHOD: blind test of KEY_v2 on the Batavia letter of 9 Sep 1640 (inv. 1134). Written before any cipher value was viewed.

Inputs (frozen before the decode, md5 in FREEZE_blind.txt):
- ../trackB/keyv2/KEY_v2.tsv (frozen 2026-11-25T20:10:20Z, md5 037b8c7a022be05d332c259d2cc4ca36). Not changed.
- ../trackB/scripts/score.py (md5 e04f5aeb5129e24c96d9fba290fb6fd6). Not changed; used as a library: wordlist(), load_key(path),
  load_tokens(path), decode(), score(), norm().
- frozen/T1640_transcription.txt: cipher passages of the test letter, same sign convention as trackB T1623/T1634:
  ':' and '.' between numbers = space; '/' = word divider; clear words in [ ] are not tokens; a line break without '/' does not divide.
  Gutter or damaged groups supplied from the second copy are marked { } and listed. Illegible group = 0 (decodes as '?').
- frozen/BLIND2_*.txt: a second transcription of the same passages from the other copy, made from the image alone, aligned by script.

Steps:
1. Decode ONCE with KEY_v2 (scripts/run_blind.py). A number not in KEY_v2 decodes as '?'. This first pass is the figure of record.
2. Coverage = groups whose number is in KEY_v2 / all groups, full arithmetic. List the unkeyed numbers.
3. Score (score.py, unchanged): a token reads as sense only if it has no '?' and its normalised decode is in the 37,386-type
   wordlist (freq >= 2, VOC inv. 1068, 1120, 1132, 1151, 1156). NB inv. 1132 is a 1639-40 volume; it is not the source volume (1134)
   of the test letter. Score = tokens read / all tokens. Read bar >= 65%, strict.
4. Shuffle control: 5,000 keys at seed 20261112 and 5,000 at seed 7, each a random permutation of KEY_v2's values over its 60 keyed
   numbers. Count shuffles scoring >= the real score.
5. Second transcription aligned with difflib (matching groups / max length).
6. Only after 1-5 are written to RESULT: open the GM II printed text (pp. 101-109), any margin gloss, and compare. No change to key or score.
   Anything read afterwards (human reading, emendations) is reported separately and does not change the figure of record.
