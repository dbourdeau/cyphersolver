# graham1806/beling: the 2 Jan 1806 sibling against Weber's WE023

Andrew Beling (ajbeling), with AI agents. Transcription and first run 11 Nov 2026; this package and its rerun 22-23 Nov 2026.

## Source

Graham to Madison, New Orleans, 2 Jan 1806, the letter as received, with Jacob Wagner's interlinear words. National
Archives, RG 59, Territorial Papers of the United States, Orleans, microfilm T260 roll 8, file unit "Orleans: January
2, 1806 - December 31, 1806" ([naId 221215877](https://catalog.archives.gov/id/221215877)). Images are public and are
not committed. Frame N is
`https://catalog.archives.gov/medialz/dc-metro/rg-059/1226295/T260/T260-08/T260-08-000N.jpg`. The files fetched on
11 Nov 2026 have these SHA-256 values, which match the `x-amz-meta-sha256` header NARA sends:

| frame | page | SHA-256 |
|---|---|---|
| 0006 | p. 1 | 16afa86b680864706c6f1fdf4fbce407564b98030bd485f17751a1b55cb68347 |
| 0007 | p. 2 | 6e5d4ab9b72a969e29b5b7ac5c50ad3acd08474087cd57508054dd4f287db301 |
| 0008 | p. 3 | 83bc8dfed62c0798051570c6068af2f069623e7a4802354fde788d86d0dd2996 |
| 0009 | p. 4 | 4577d9073720aaa9560abc8be2a504426d3e33bf58ad90651c9b77e33d653b2d |
| 0010 | p. 4 verso | c0755522fffae61bdd29ecf41a99d50304c0a125122920447e6724e128adb334 |
| 0011 | p. 5, signed | f6ef8cf0a77a2c0f4c73645981cae6643f3a9c180f6bc65f7d9aabe2c2a24e2d |
| 0012 | docket | 4d34c54f0302413989959fc5691e8c50a3ad5e2b8add58cca1f4a655e068e98c |

The letter starts on frame 0006. Frame 0005 is a typed Library of Congress slip, not part of the letter.

## Files

- `transcription_2jan1806.txt`: 57 coded runs and 614 groups (275 distinct), each under the word Wagner wrote above
  it. The markup is explained in the file's header. Doubtful digits are marked `?` and unreadable groups `X`. Both are
  left out of every count.
- `PLAN.md`: what is measured and how. It also says what was and was not fixed before the first run.
- `verify.py`: the scorer, standard library only. `python3 verify.py` runs the parts that need no published table.
  `python3 verify.py --weber <file>` also runs the table test.
- `results.json`: the output of `python3 verify.py --weber` on our own transcription of Weber's tables. It holds counts
  only, and no element of any table.
- `key_direct.tsv`: the 124 groups that stand alone under one of Wagner's words, with that word. These values come from
  the 1806 manuscript, not from Weber.

## Weber's table is not here

WE023 is printed in Ralph E. Weber, *United States Diplomatic Codes and Ciphers, 1775-1938* (Chicago: Precedent,
1979), pp. 419-30. It is cited, not copied. The book is in many libraries and on the Internet Archive as a
print-disabled loan. **A reader without the book cannot rerun the table test.** That reader can rerun the held-out
test of Wagner's words and the statistics on the 22 Nov numbers. To rerun the table test, transcribe the tables you
want to try into a tab-separated file (header line; columns `code`, `number`, `element`) and pass it with `--weber`.
Our own file holds WE016-WE028. It was parsed from the text layer of an interlibrary-loan scan and was not corrected
by hand. Its SHA-256 is recorded in `results.json`. Several WE023 misses look like errors in that text layer (879, 1159, 967;
1593 is unreadable in it; see NOTES). The page images have not been checked, so a clean transcription may score a few
words higher.
