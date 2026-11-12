# Pre-registration, round 2: the rest of sande1660 cipher A as new held-out material for key.txt

Written 11 Nov 2026, before any transcription of the pages below exists and before any round-2 script exists.
The coordinator has looked at these pages only as whole-page thumbnails and one 2x crop of the top of m0272 (to set
the crop size); nothing was transcribed or decrypted.

## Material
New transcriptions from the DigitArq scans (`images.txt`), one line of the page per line of the file, physical line
numbers counted from the first cipher line of the page:

| File | Page and lines |
|---|---|
| `transcription/m0272.txt` | m0272, every cipher line |
| `transcription/m0265_rest.txt` | m0265, line 19 to the end |
| `transcription/m0266_rest.txt` | m0266, line 1 and line 6 to the end |
| `transcription/m0267.txt` | m0267, every cipher line |
| `transcription/m0269_rest.txt` | m0269, lines 1-2 and line 12 to the line before the last |
| `transcription/m0273_top.txt` | m0273, line 1 down to the line before the last 12 |

Secondary file (not part of the pass/fail): `transcription/m0271_r2.txt`, a second reading of m0271.

**Who transcribes.** Each file is made by a separate AI agent (same model family as the first reader; separate
context). The agents are given only the scan, a crop recipe and the glyph notes of NOTES.md section 3 (27 is a 2
with a reversed hook; the hook alone is 7; 13 has a two-bowl 3; 19 ends in a reversed hook). They are not given
key.txt, transcription.txt, NOTES.md, any decryption, or (for m0271_r2) the first transcription or reading of
m0271. So, unlike round 1, these transcriptions are blind to the key table as well as to any decryption.

**Format.** As `transcription/m0271.txt`: numbers separated by dots, word gaps by `|`, `?` for a sign not read
(one `?` per sign, estimated where a line runs into the gutter), `*` after a doubtful reading. Words in clear are
written in braces `{...}` and count as a break, like a code group. Comment lines start with `#`.

**Freezing.** The coordinator may change the agents' files before hashing only in layout (tags, spacing, comment
lines); any such change is shown by a diff in CHECKS.txt. The files, this PREREG and the four round-1 inputs it
reuses (key/key.txt, key/transcription_build.txt, lexicon/pt.json.gz, PREREG.md) are hashed into
`results/frozen_inputs_round2.sha256` before `scripts/test_round2.py` exists. Corrections found later (collation,
second looks) go into the reading and a separate file; the scored text is not changed.

## Score
Exactly the rule of `PREREG.md`, code unchanged where possible: decrypt with key.txt (26 numbers, nothing added);
numbers of 60 and up, `?` and `{clear}` break the string; a number below 60 that the key lacks is one letter that
cannot be covered; same normalisation (ç → s); coverage by lexicon words of 3+ letters, best parse per line; word
gaps ignored.

- Exclusion: a new line that shares a run of 6 or more consecutive tokens with a line of transcription_build.txt is
  left out of the score and listed (it is already build material).
- S_new = coverage of all six files together, after the exclusion.
- S_build = coverage of transcription_build.txt (0.7393 in round 1; recomputed).
- Null: 200 keys made by permuting key.txt's 26 letter values over its 26 numbers, random.Random(1660); S_new
  under each.

**Pass** if S_new ≥ 0.85 × S_build and S_new − best shuffled ≥ 0.30. "Too small" if fewer than 600 decrypted
letters. One run of the scoring script; any later run only checks that the output is identical.

Reported but not pass/fail: S per file; S of `m0271_r2.txt`; counts of tokens, code groups, unread signs and
numbers below 60 the key lacks.

## Not part of the test (reading, checked by eye)
- Collation of m0271 (first reading against m0271_r2), each disagreement settled on the image where possible.
- The numbers below 60 not in key.txt (23, 25, 26, 31, 38, 42 on m0271, and any new ones): called a homophone only
  if read clearly on the image in two or more places where one value fits and no keyed number in its place fits;
  otherwise left as a probable misreading. key.txt is not changed either way.
- Code groups: a proposed value counts as "good" only if it fits in more than one place; the places are recorded.
- Cipher B (m0063 glosses): any table built from the glosses is reported with the share of m0063 it reads; there
  is no held-out test for it in this round.
