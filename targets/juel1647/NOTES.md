# juel1647: Peder Juel's register of outgoing letters, Stockholm 1647-48 (catalogue 2553)

WAINUT, 12 Nov 2026. Work done with AI language-model agents viewing the images; no human palaeographer has checked the
signs or the readings. An independent AI language-model agent that took no part in the solve reviewed the folder blind
(it copied the cipher signs of pp. 5 and 115 from its own crops before opening the transcriptions); the changes made
after that review are listed under "Changes after the independent review".

Status: in progress (not yet written up). Read in part, 12 Nov 2026: the chancellor entry (p. 5) and the entry to Peder
Vibe (p. 115) are read in part; the p. 5 run to the King is not prose (one short run, read); the p. 6 entry to Hannibal
Sehested is not solved. No site page or README row.

## Documents

Rigsarkivet (Copenhagen), TKUA, Speciel del, Sverige, Peder Juels og Mogens Høegs gesandtskabsarkiver, Ekstraktprotokol
1647-49 (film C.195), Arkivalieronline epid 19852819, unit 261585. A secretary's register of Juel's outgoing letters; secret
passages are copied in as dotted number runs with no decipherment.

| doc | place | letter | system | state proposed |
|---|---|---|---|---|
| king | image 5, p. 5 top (3 lines) | to King Christian IV, 20 Nov 1647 | 8-64 table | not prose (one short run in clear text; all 3 cipher words read) |
| chancellor | image 5, p. 5, entry No. 4 (13 lines) | to the chancellor Christen Thomesen Sehested, 20 Nov 1647 | 8-64 table | read in part |
| hsehested | image 6, p. 6, entry No. 4 (3 lines) | to Hannibal Sehested, 20 Nov 1647 | 3-32 set, unknown | not solved |
| vibe | image 61, p. 115 (10 lines) | to Peder Vibe, 2 Sep 1648 | Vibe's old cipher (Dudout, PR #410) | read in part |

Note: the catalogue gives the p. 5 top run to the chancellor; the register puts it in the entry to the King of the same
day (the last entry on p. 4, "Till hans Kongl. Mtt. ... 20 9br 1647"). Image 7 (pp. 8-9) has no number runs; the p. 6
head carries only "8 ... 129" of the chancellor entry.

Images (no scans in git): viewer links
https://arkivalieronline.rigsarkivet.dk/da/billedviser?epid=19852819#261585,48964105 (p. 4-5), #261585,48964106 (p. 6),
#261585,48964161 (p. 115); full JPEGs api.rigsarkivet.dk/ao/v1/images/<id>. Key letters: unit 261575 images 117
(48962526), 118 (48962527), 121 (48962530). Fetched one at a time, 1.6 s apart (`scripts/ao_get.py`).

## System (8-64 table)

A homophonic number table for Danish. The glosses of the time on Juel's own letters of 1648 show four runs: 14-27 k..y
upward, 28-37 k..a downward, 38-49 a..m upward, 50-61 z..n downward, so most letters have two numbers (a 37/38, e 33/42,
n 17/61, r 21/57, s 22/56 ...). 8, 9, 10, 62, 63, 64 are unglossed nulls; they mostly stand between words, but in the
chancellor entry 63 and 64 also stand inside words ("wil.de", "gi.ern"). In the build glosses 19 = t,
20 = s and 24 = o, where the run pattern would give p, q and u; 11, 12, 13 are not glossed. Three-digit numbers (83-158 here;
396, 410, 486, 487 = "dennem", 545 = "Magnus" in the letters) are a nomenclator.

## Key source and held-out test

- Build: interlinear glosses of image 117 (letter of early March 1648) and image 121 (8 July 1648), 82 pairs
  (`pairs_build.tsv`). Values not glossed in the build set were filled from the run pattern (marked `s` in
  `key_frozen.tsv`). The glossed lines read e.g. "alle hendis ord ware med suck, taare i øynen" (121) and "trolofwelse ...
  mellom dennem och Magnus" (117).
- Frozen: `key_frozen.tsv` (= `key.tsv`; no value was changed after the test).
- Held out: Juel's letter of 11 March 1648 (image 118), 25 glossed numbers (`heldout_118.tsv`), e.g. 10.25.29.25.33.14.33 =
  "Wiweke" (Vibeke Kruse). **23 / 25 = 0.92** agree; misses 24 (gloss u, key o) and 41 (gloss g or d, key d).
  2000 random permutations of the key values: mean 1.1, best 7 of 25 (`scripts/heldout.py`, `work/heldout.out`).
- Caveat: image 118 was looked at before the freeze (its "Wiweke" gloss was read while the run pattern was being worked
  out), so the test is not blind in the strict sense.
- Of the 23 hits, three are values filled from the run pattern (30 h, 35 c, 39 b) and two are 25 = w, where the build
  glosses said u (or n); without the two 25 hits the score is 21 / 23. The two misses were left in the key, which was not
  tuned to the test.
- Statistical validation (Dan's `docs/_validate.py`, recorded in `profile.json`): `validation.tsv`, written by
  `scripts/validation_pairs.py` from the p. 5 transcriptions and the frozen key (holes, guesses, codes, open numbers and
  doubtful groups left out), gives 111 read tokens but only 63 letters: verdict **too short**. The p. 115 passage is not
  in the test, since Vibe's old cipher gives no fixed value per number.
- File times: `pairs_build.tsv` was last saved at 00:37 on 12 Nov, after `key_frozen.tsv` (00:29) and `work/heldout.out`
  (00:31). No version history of the work folder exists, so this cannot be proved from a diff. A re-check on 12 Nov
  found that the 82 pairs agree with every frozen value marked `g`, and that every conflict among the pairs (25 u,
  27 y/l, 35 e, 41 g, 53 w/u) is already named in the notes column of `key_frozen.tsv`, so no pair value differs from
  what the frozen key records. The 00:37 save falls in the same minute as the translations (00:37:12-14), which fits a
  layout pass.

## p. 115 (to Peder Vibe)

Not the 8-64 table. Brice Dudout's PR #410 (vibejuel1651, open, 11 Nov 2026) published Peder Vibe's old cipher ("gamle
Ciffres": opener 24-39 sets k = -(opener mod 3), body n -> letter n - k mod 23) and noted that register p. 115 is in it.
We applied his published table unchanged (`scripts/decrypt.py vibeold`); credit to him. It reads at once ("sagde nogle dage
til 212 at forrige 412 af 351 277 ... hende bort, nu skal 401 føre hende hid igien"). One word is a guess ("24 25" opener
pair, [?dragit]) and one is left open ("fogte"). The two slips of the first reading (bor{p/t}, s{f/k}al) went away when
the blind review read line 4 as "16 18 25" and "16 8 22" (probable; both passes had 14 and 4), so those words are now
verbatim. The other holes in this passage are nine unidentified codes and clear text of the register that is not yet
transcribed (see Remaining gaps), not failed decryption.

## p. 6 (to Hannibal Sehested): not solved

30 numbers, 3-32, two codes (86, 208). Tested (`scripts/test_332.py`, `work/test_332.out`): Vibe's old cipher, Vibe's new
alphabet, the 8-64 table shifted by -40..+40, and plain rank ciphers over 23- and 25-letter alphabets with all shifts.
None gives Danish (best: 8-64 table +10, "ak?ndinetkesiosembotstclirmsan"). Too short for a ciphertext-only attack; no
glossed sibling seen. Stop rule applied.

## Reading

Mechanical decryption with `scripts/decrypt.py`; every departure marked in `reading_<doc>.md`; `scripts/check_marks.py`
passes on king, chancellor and vibe.

Word counts (cipher words in letters; codes not counted as words):

| doc | verbatim | marked repair | from gloss only | guess | hole |
|---|---|---|---|---|---|
| king | 3 | 0 | 0 | 0 | 0 |
| chancellor | 14 | 4 | 0 | 3 | 5 |
| vibe | 23 | 0 | 0 | 1 | 1 |

Dan's `docs/_check_reading.py` clean share (`--file` on the plain reading, `work/plain_<doc>.txt`; codes count as holes):
king 0.0 (1 sentence, 20 words), chancellor 0.571 (7 sentences, 52 words), vibe 0.333 (6 sentences, 49 words). On the target (`python docs/_check_reading.py juel1647`): reading files king 0.5, chancellor 0.308, vibe 0.25; the raw
decryption files 0.0 each; target 0.305 (with the p. 6 trial decode, 0.0).
In the vibe passage the low share comes from the nine unidentified codes (13 occurrences) and from the clear text of the
register that is not transcribed (the "..." stretches), not from failed decryption: of its 25 cipher words 23 read
verbatim. The chancellor checker run picks German for some sentences; the profile gives `language: da` for every text.

## Prior art (12 Nov 2026)

- Catalogue vetting of 11 Nov 2026: not on DECODE, not in Tomokiyo, no Lasry/HistoCrypt paper; Fryxell 1836 prints a Swedish
  abstract of this register without the cipher passages.
- Web search (12 Nov 2026), "Peder Juel resident Stockholm 1647 1648 chiffer dechiffreret Vibeke Kruse brev": nothing on
  these passages; only Fryxell's abstracts and general pages.
- Brice Dudout, PR #410 (vibejuel1651): Vibe's two ciphers; points to register p. 115 but does not read it. No open PR or
  target covers unit 261585 or the 8-64 table (checked 11-12 Nov 2026: open PRs, issues, targets/ and research/ on
  origin/main 54c4ecc65).

## Changes after the independent review (12 Nov 2026)

The reviewer copied all cipher lines of p. 5 (entry No. 4) and p. 115 blind from its own crops of images 5 and 61
(about 153 of 156 and 147 of 150 numbers agree with the transcriptions), re-ran `decrypt.py` and `check_marks.py`, re-ran
the held-out test, and read both passages as Danish. Grades: chancellor read in part, B; vibe read in part, B. Changes
made from its image readings, and nothing else:

1. vibe, line 4: "16 14 25" is "16 18 25" and "16 4 22" is "16 8 22" (probable; the reviewer read 18 and 8 in its blind
   copy before it knew these were the repair points). The words read "bort" and "skal" verbatim; the repairs
   `bor{p/t}` and `s{f/k}al` are gone.
2. chancellor, line 11 ("48 56 55"): 50 is 56, so "holsten" reads verbatim (the `hol{z/s}ten` repair is gone).
   Line 2 ("62 50|56 55", "sterk") is now marked doubtful, `50|56`; the repair `{z/s}terk` stays. Line 10 ("31 33|53 20",
   in "trgese") is marked `33|53`. `scripts/decrypt.py` takes the first reading of a doubtful group.
3. The nulls: 63 and 64 also stand inside words ("wil.de", "gi.ern"), not only between words; System corrected.
4. Word counts: chancellor 14 verbatim, 4 repairs, 3 guesses, 5 holes (was 13, 5, 3, 5); vibe 23 verbatim, 0 repairs,
   1 guess, 1 hole (was 21, 2, 1, 1). `check_marks.py` passes on all three readings after the changes.
5. The held-out test notes now give the 21 / 23 figure without the two 25 hits and the file-time check of
   `pairs_build.tsv` (see Key source and held-out test).

Not done: the reviewer asked for the clear text of the register in the p. 115 entry to be transcribed in full, which
should lift the checker share of the vibe passage (0.333). It is not transcribed; see Remaining gaps. The reviewer also
advised against identifying the codes 124 and 158 without proof; they are left open.

## Remaining gaps

- 11, 12, 13 in the 8-64 table - blocker: no-key-material; no gloss in images 117-121; they stand in "12 19 37 27" and
  "13 19 37 27 20 29 44 61" (p. 5), which do not read, and in the chancellor repair `giern{[11]c/e}`, where two signs
  (11 unglossed, 35 = c) are replaced by one letter; the word is certain from context, the signs are not explained.
- 50 in "sterk" (p. 5, line 2, `50|56`) - blocker: illegible; a flourish from the line above crosses the digit where a
  6's ascender would be. Read as 56 the word is verbatim; read as 50 it decodes z by the run. With "holsten" now read as
  56, any claim that 50 = s rests on this one doubtful place.
- the chancellor entry's last two sentences - blocker: illegible; "trgese" (with `33|53`), "quartg[11]bb", "fyle" and
  "forlagrdit aggrop" do not read; copyist errors or unclear figures in the register; the original letter of
  20 Nov 1647 is not among images 115-135 of unit 261575.
- the vibe words "fogte" (hole) and "[?dragit]" (guess, 25 dropped as an opener) - blocker: needs-physical-access; the
  figures are clear but do not read under Vibe's old cipher; the original letter of 2 Sep 1648 would show a copyist slip.
- the clear text of the register in the p. 115 entry - blocker: illegible; a secretary hand on black-and-white
  microfilm. Only some words are made out ("och ... / ... da," and "gick hen aff / ... hos 446 som war dog ... af / 339");
  a reading by a palaeographer of Danish secretary hands is needed. These stretches are most of the holes the checker
  counts in the vibe passage.
- the nomenclator - blocker: open-codes; 83, 84, 123, 124, 129, 158 on p. 5 and 212, 277, 339, 351, 401, 412, 426, 442,
  446 on p. 115; no code list found. 124 (the man they would have as general) and 158 (where) are not identified; the context (winter 1647-48,
  Sweden seeking a generalissimo for the army in Germany) suggests candidates, but none is claimed.
- the signs TT, Θ, ∞, Ψ, Δ, Ш on p. 5 - blocker: open-codes; no list of these signs found.
- p. 6 (3-32 set, to Hannibal Sehested) - blocker: too-short; 30 numbers, no glossed sibling; the original letter to
  Hannibal Sehested would be needed.
- the held-out test is not strictly blind - blocker: too-short; image 118 was seen while the run pattern was worked
  out, and no other glossed letter of the 8-64 table was found among images 115-135.
- one blind AI review only; no human has checked the signs or the readings - blocker: needs-physical-access; a reader
  of Danish secretary hands with the originals or better images.

## Escalation

- [x] siblings: Juel's original letters to the chancellor in unit 261575, images 115-135, opened; images 117 and 121
  (glossed) gave the key, image 118 (glossed) the held-out test; the register pages next to the runs (pp. 4, 6, 8-9)
  checked for more runs
- [x] clear-pages: the register has no decipherment; the interlinear glosses of the time on the originals are the clear
  text used
- [x] known-keys: Peder Vibe's old and new ciphers (Dudout, PR #410) tried on p. 6 and the old cipher used for p. 115; the
  8-64 table and its shifts (-40..+40) and plain rank ciphers tried on p. 6 (`scripts/test_332.py`)
- [x] print: Fryxell, Handlingar rörande Sverges historia 1 (1836) prints an abstract without the cipher passages; DECODE,
  Tomokiyo and Lasry have nothing (catalogue vetting 11 Nov 2026); one web search on 12 Nov 2026 found nothing
- [x] key-rebuild: the four runs of the table rebuilt from the glosses and the unglossed values filled from the run
  pattern (marked `s`); 11, 12, 13 could not be rebuilt from what reads
- [x] retry: the doubtful groups were re-read on the image in the blind review (three corrected, two marked doubtful) and
  the readings regraded; the remaining holes are listed under Remaining gaps
