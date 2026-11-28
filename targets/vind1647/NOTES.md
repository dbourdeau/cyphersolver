# vind1647: Holger Vind, Copenhagen, 17 March 1647: a Danish letter in a reciprocal letter cipher, with its Latin close in clear

Status: **read in part: 65 of 74 cipher words (87.8%), 9 holes; 64 of 74 if the first sign of line 07 is l.** The
key is recovered from the ciphertext alone. The registered held-out test (Latin) missed and the plan's 95% read bar is
not met; everything that reads came after the plan and is labelled so.

Contributed by Andrew Beling, with AI agents. Transcription, solve, controls and this write-up are by AI agents
(Claude Opus 5.5, Anthropic) on 26 Nov 2026, 01:10-02:35 UTC, with two AI helper agents of ours (Claude, model Opus):
a blind second transcriber and a cold reviewer (02:20-02:27 UTC). **No person has checked the reading.** All times
are from the local shell clock; the order of plan and runs rests on local file times only (no external timestamp).
Revised on 27 Nov 2026 (local date; 28 Nov 02:52-02:59 UTC) after an independent AI review of ours (Claude Opus 5.5,
27 Nov 2026, about 18:55-19:30 EST): two more holes, the order of results 4 and 5, the German held-out file refiled.

## Source

- Rigsarkivet (Danish National Archives, Copenhagen), Tyske Kancelli, Udenrigske Afdeling (TKUA), Almindelig del 3
  nr. 112 "Chiffer", Arkivalieronline unit 260610, image 126, right-hand leaf.
  - Image: `https://api.rigsarkivet.dk/ao/v1/images/48691601`.
  - Viewer: `https://arkivalieronline.rigsarkivet.dk/da/billedviser?epid=19852193#260610,48691601`. The epid is taken
    from `targets/biermann1675/NOTES.md`; the viewer link itself was not opened.
- The left-hand leaf of the same image is part of the "Nomina propria" register sheet (names to 359, "Nationer").
- The leaf has:
  - a heading in clear, "Mitto tibi navem sine prora puppique" (the riddle for AVE);
  - 12 lines of cipher;
  - five lines of Latin in clear;
  - the place, date and signature: "Hafn: raptim 17 Martij 1647 Holger Vind". The year's 6 is written like a 5. Holger
    Vind lived 1623-1683, so the year is read as 1647.
- **Conditions.** The image is free on Arkivalieronline, with no sign-in. It was fetched by plain GET on 26 Nov 2026,
  00:05-00:26 UTC, with the rest of unit 260610; the SHA-256 is in the contributor's local fetch log.
  - Andrew Beling's recorded words of 25 Nov 2026, on Rigsarkivet and CEHM-Carso images: "I agree with your plans and
    the image use for item 2".
  - The licence for reuse of the image itself was not checked, so no image or crop is filed here.
- **Prior art.** Listed, not deciphered, in `targets/biermann1675/keyhunt.md` (see below). Not in `catalogue.json` or
  `research/leads.json` of 25 Nov 2026 (searched for "Holger Vind", "Mitto tibi", "navem sine"). Two web searches on 26 Nov 2026 found no
  edition or decipherment. Danish printed sources (Danske Magazin, letter editions) were not searched.
- **How it was found.** The leaf was noticed during a paging of unit 260610 on 26 Nov 2026 for catalogue 2542. The unit
  had been paged before for `targets/biermann1675/keyhunt.md`, and this leaf is listed there: Daniel Bourdeau's line 84
  (27 Oct 2026) names a "small letter on 126 'Mitto tibi navem sine prora puppique' with a letter cipher". That is a
  mention only; no decipherment is given there.

## The system

A simple substitution in ordinary letters. **The key is reciprocal**: plain and cipher letters swap in pairs.

- The pairs are a-x, b-y, c-z, d-h, e-p, f-o, g-n, i-m, k-l, q-r, t-u and s-w.
- The writer uses a capital and a small form of the cipher letter w; both stand for s.
- `key.tsv` gives every value.
- Reciprocity, checked after the solve: the signs a, c and r occur once each and e twice; all four were given their values by
  the pairing, so they are left out. Of the 12 remaining signs whose partner is also a sign in the text, 12 are reciprocal;
  in 100,000 random one-to-one keys over the same 17 signs, the most was 10 (`count_words.py`).
- No word of the repository's da, de and la lexicons (167,876 words), used as a keyword and folded on itself or set
  in two rows, reproduces the pairs; the best gives 9 of 12 (`work/scripts/keyword_fold.py`,
  `work/runs/keyword_fold.txt`). Keywords outside those lexicons, and other constructions, were not tried.
- The plain text is **Danish** in 17th-century spelling, with the Latin words ingenium, exercer[e] and quasi.

## Results, in order

Registered (`work/PLAN.md`, frozen 2026-11-26 01:23:11 UTC by the local clock; SHA-256 in `work/PLAN.sha256`; the
frozen transcription is `transcription_frozen.txt`, SHA-256 also in `work/PLAN.sha256`. PLAN.md says its hash is in
WORKLOG.md: that is the contributor's local work log, not filed here):

1. **Held-out test: missed.** The plan assumed the language was Latin (the first inventory line had guessed Latin).
   A key built by the solver from lines 1-6 alone decodes lines 7-12 to 9 of 33 Latin lexicon words (27%, bar 80%);
   0 of 1,000 shuffled keys scored at or above it (`work/runs/heldout_registered_la.txt`).
2. **Second control: passed.** The solver on 20 random permutations of the cipher letters (word lengths kept) scored
   -8.82 to -8.61 per letter with the Latin model and -8.88 to -8.58 with the Danish model, against -7.75 and -7.39 for
   the true text (`work/runs/permcontrol.txt`).
3. **Read bar (95% of cipher words): not met.** 65 of 74 (87.8%), below.
   - **Departure from plan step 3.** After the Latin miss the plan said to try homophones, then the keyword alphabets
     of the same file. Instead the language was switched (result 4). Homophones and those keyword alphabets were not
     tried; the keyword-fold test (The system, above) is a different test.

After the plan (labelled):

4. **Held-out with the Danish lexicon**, run at 01:27 UTC by the local clock (these minute times are the file times of
   the contributor's local work folder, which is not filed), beside the registered Latin run (01:26:53)
   and a German one (01:27:12) (`work/runs/heldout_afterplan_da.txt`, `heldout_afterplan_de.txt`): 12 of 33 held-out
   words in the repository's Danish lexicon (36%; the lexicon is modern and lacks forms such as uille, udi, skee, ieg); 0
   of 1,000 shuffled keys at or above it. German gave 13 of 33 lexicon words, and its decode of lines 7-12 comes out
   close to the same Danish ("din uille der udi hand thee ieg forundrer ..."); the text was read as Danish from these
   decodes. (`heldout_afterplan_de.txt` as first filed held only the JSON line; on 28 Nov 2026 UTC (27 Nov local) it was replaced by a
   rerun whose first line is byte-identical and whose second line is the decode the script also prints.) The key from lines 1-6 alone decodes 162 of 171 held-out letters exactly as the final key
   does; 18 of its 21 values equal the final key; the three that differ (a, w, z) occur 1, 1 and 3 times in lines 1-6
   (`work/scripts/agreement.py`, `work/runs/heldout_afterplan_da_agreement.txt`, written at 01:29 UTC).
5. **Whole-text comparison of languages**, run at 02:30 UTC, after the cold review (02:20-02:27) and after the key was
   set, as a record asked for by that review: the solver on the whole frozen text with Latin, Danish, German and Dutch
   models (seed 2, 12 restarts; `work/scripts/whole_text.sh`, `work/runs/whole_text.txt`). The Danish run gives readable
   Danish ("ieg ... dit ... min moder udi ... som det shal uere giort mit ingenium"). It did not choose the language;
   result 4 did.
6. **The final key** (`key.tsv`) was set by hand from the whole text after the runs of results 1-4. The Danish whole-text run's key
   differs from it in 7 of 23 signs (a, c, d, l, o, w, y); those values were set from the sense and the pairing.
7. **Reading** (`reading.md`, `translation.md`): 74 cipher words, **65 read, 9 holes (87.8%)**, by `count_words.py`.
   - The nine holes:
     - `yqfhpq` decodes to "broder": its second sign was re-read y to q after the solve, on the sense alone (the
       frozen reader had y, the blind reader g or q).
     - `xkkp` decodes to "alle": its second sign was re-read d to k after the solve, on the sense alone (the frozen
       reader had d or k, the blind reader h, k or d).
     - These two are the same kind of change as the withdrawn line-12 re-reading (e to o), so they are holes too.
     - `papqzpq` decodes to "exercer": "exercere" wants a supplied final e.
     - `hmlu` decodes to "dikt": the third sign is doubtful (l or z); "dict" (= dit, your)?
     - `nqpghp` decodes to "grende": "trende" (three) is wanted.
     - `fzh` decodes to "ocd": "och" is wanted.
     - `Wuxootpd` decodes to "staffueh": "staffued" (stavet, spelt) is wanted.
     - `yfnWuxeotpq` decodes to "bogstapfuer": "bogstaffuer" wants f where both readers saw an e-like sign (= p).
     - `mgofqh` decodes to "inford": perhaps "indført"; not settled.
   - Two of the holes swap d and h, which are a pair in the key.
   - One read word carries a doubt: "udi" in line 7 (first sign t or l; with l it would be a hole, 64 of 74).
8. **What the letter says.** Vind thanks his "[brother]" for a letter received through his mother that evening. He says
   the puzzle was too easy to need much thought, and that he is surprised it was not subtler, since [three] chancery
   clerks had worked on it and had neither [spelt] right nor [put in] [all] the [letters]. Words in square brackets
   rest on holes. The Latin close calls this the
   solution of the reader's "Gordian knot", untied "not in Alexander's way but in a very simple one".
   - So the cipher is Vind's answer to a cipher puzzle, written in the puzzle's own cipher.
   - The puzzle itself was not looked for. Who the "[broder]" is was not checked.

## Method

Key recovered from ciphertext only: a hill-climbing substitution solver with letter 4-gram models built from the
repository's lexicons (`work/scripts/solve.py`, `common.py`).
- The language was found from the held-out runs made right after the Latin miss (result 4): the Danish decode reads.
- The rare signs were fixed by the reciprocal pairing and the sense.
- The scripts use the Python standard library only, and read `lang/lexicons/*.json.gz`.

## Transcription

- **`transcription_frozen.txt`.** Its "Raw copy" line names the contributor's local copy of the image, which is not
  in the repository; the file is under the plan hash, so it is left as it was. Transcribed by an AI agent (Claude Opus 5.5), 26 Nov 2026, from full-scale and 2x
  crops of the image, before any solving; one reader; hashed with the plan at 01:23:11 UTC. Its header says "c.
  01:15-01:25": the end time was an estimate written into the file before it was hashed.
- **`review/blind_transcription.txt`.** A blind second transcription by an AI helper agent of ours (Claude, model
  Opus), 26 Nov 2026 01:29:56-01:34 UTC. It worked from a crop of the leaf only, was told not to decipher, and was not
  shown the first transcription. Its image line, which named a local file path, was replaced by a description; nothing
  else in it was changed.
- **`transcription.txt`.** The frozen file with eight signs re-read after the solve, listed in its header. Three of
  them follow the blind reading and were confirmed on 4x crops: xooupg (afften), ipg (men) and mgofqh. Two rest on the
  sense alone and are counted as holes: yqfhpq (broder) and xkkp (alle). The other three: dtpqzlpg (huercken), a
  re-reading of the image that the blind reader also has; imn (mig), the n written above the g, read as the writer's
  own correction; hmlu (dikt), a hole in any case. The rule used: a re-read word is counted read when the change rests
  on the image and an independent blind reading agrees, and a hole when it rests on the sense alone. Counted strictly,
  with every re-read word a hole (afften, men, huercken and mig too), the share would be 61 of 74. A ninth
  re-reading (line 12, e to o, giving "bogstaffuer") was withdrawn after the cold review: both readers had e before the
  solve, and the change rested on the sense only.
- **Agreement** (`review/compare_blind.py`, output in `review/compare_blind.txt`; W and w are merged there, as they
  are one cipher letter):
  - frozen against blind: 327 of 336 letters in words of equal length;
  - `transcription.txt` against blind: 334 of 339.
- **Cold review.** An AI helper agent of ours (Claude Opus, 26 Nov 2026 02:20-02:27 UTC) that had not built the folder checked it against the
  image, re-applied the key with its own code and reran the scripts (26 Nov 2026 02:20-02:27 UTC). Its findings were
  taken in: "exercer" and "bogstapfuer" counted as holes, line 12 kept as e, the reciprocity count made non-circular,
  the sign counts of result 5 corrected, the whole-text runs filed, wider claims narrowed.

## Transcription doubts

- [y/q/g] (line 01, `yqfhpq`, second sign) - read: q; checked: image, decode, transcription; the frozen reading has y, the blind reading g (or q); q gives "broder"; re-read after the solve on the sense alone, so a hole.
- [l/z] (line 06, `hmlu`, third sign) - read: l; checked: image, decode, transcription; the blind reading has `hmle`; l gives "dikt", z would give "dict"; a hole either way.
- [t/l] (line 07, `thm`, first sign) - read: t; checked: image, decode, transcription; the first reading has t (a stroke at the foot runs into the h), the blind reading and the cold reviewer l (`lhm`, "kdi"); t gives "udi", as in lines 02 and 06; counted read, so the count is 64 of 74 if l is right.
- [g/n] (line 08, `imn`, third sign) - read: n; checked: image, decode, transcription; an n is written above the g of `img` ("min"), read as the writer's correction to "mig"; the blind reading gives img[n].
- [=/z] (line 09, `zxgu=`, end) - read: = (word goes on); checked: image, decode, transcription; the blind reading has a final z; with = the word is "cantzelister".
- [k/h/d] (line 11, `xkkp`, second sign) - read: k; checked: image, decode, transcription; the sign is heavy, perhaps written over another; the frozen reading has d (d-like with a loop, d or k), the blind reading h, k or d; k gives "alle"; re-read after the solve on the sense alone, so a hole.
- [d/h] (line 11, `Wuxootpd`, last sign) - read: d (cipher d = h); checked: image, decode, transcription; both readings agree on the d form; "staffued" wants the h form, so a hole (the writer's slip).
- [e/o] (line 12, `eotpq`, first sign) - read: e; checked: image, decode, transcription; both readings have e (blind: e or c); o would give "bogstaffuer"; with e the word is a hole.
- [q/g] (line 12, `mgofqh`, fifth sign) - read: q; checked: image, decode, transcription; straight descender; the blind reading gives q (or g); a hole either way ("inford" / "infond").

- [n/rr] (line 03, `nmfqu`, first sign) - read: n; checked: image, decode, transcription; rr-like in the first reading, n in the blind one; n gives "giort".
- [q/g] (line 02, `oqx`, second sign) - read: q; checked: image, decode, transcription; the blind reading notes g; q gives "fra".
- [z/e] (line 02, `fzd`, second sign) - read: z; checked: image, decode, transcription; the blind reading notes e; z gives "och".
- [w/u] (line 06, `kphmw`, last sign) - read: w; checked: image, decode, transcription; the blind reading notes u; w gives "(ander)ledis".
- [p/r] (line 06, `ofqpgh`, fourth sign) - read: p; checked: image, decode, transcription; the blind reading notes r; p gives "forend".
- [x/q/p] (line 08, `exx`, second sign) - read: x; checked: image, decode, transcription; blotted; the blind reading gives x, q or p; x gives "paa".
- [x/p/z] (line 08, `txq`, second sign) - read: x; checked: image, decode, transcription; the first reading noted p, the blind one z; x gives "uar".
- [c/e] (line 10, `cpkmwupq`, first sign) - read: c; checked: image, decode, transcription; the blind reading notes e; c gives "(cant)zelister".
- [y/v] (line 11, `yfnWux=`, first sign) - read: y; checked: image, decode, transcription; the blind reading notes v; y gives "bog-".
- [word division] (line 02, `xooupg`; line 09, `pooupqWfi`) - read: one word each; checked: image, decode, transcription; the first reading noted a possible gap in each; one word gives "afften", "efftersom".
- [W/w] (line 03 `Wfi`, line 04 `rtxWm`, line 09 `pooupqWfi`, line 11 `yfnWux`) - read: W; checked: image, decode, transcription; the blind reading has the small form w in these four; both forms are s, so the reading does not change.
## Remaining gaps

One line per piece that is not read letter for letter from the key, with its blocker.

- Line 06, `hmlu` ("dikt") - blocker: illegible; the third sign is l or z on the microfilm image, and neither gives a sure word ("dict" = dit, your, is possible).
- Line 12, `mgofqh` ("inford") - blocker: illegible; the fifth sign is q or g on the image, and neither reading gives a sure word ("indført", entered, is possible).
- Lines 09-12, the four writer's slips "grende" (trende), "ocd" (och), "staffueh" (staffued), "bogstapfuer" (bogstaffuer) - blocker: needs-physical-access; they read from the sense and stand in both transcriptions; only the original (or a colour image) could show a correction the black-and-white film loses.
- Line 01, `yqfhpq` ("broder") and line 11, `xkkp` ("alle") - blocker: illegible; the second sign of each was re-read after the solve on the sense alone (frozen y and d, blind g and h); the image does not settle it.
- Line 04, "exercer" (exercere) - blocker: illegible; no final e is written on the image; the word wants a supplied letter, so it is a hole by the counting rule.

Not gaps in the reading, but open: who the "[broder]" is, and the puzzle letter Vind answers; neither was looked for.

## Escalation

- [x] siblings: an AI helper paged all 309 images of the unit at overview scale on 26 Nov 2026, looking for sign
  alphabets for catalogue 2542. It was not asked to look for this hand or this cipher, and its report names no other leaf
  in this cipher. The left-hand leaf of the image is a name register. The Vind family papers were not searched.
- [x] clear-pages: the heading and the Latin close on the same leaf are in clear; they say what the cipher is (the
  solution of the reader's "Gordian knot") but do not give its text.
- [x] known-keys: every word of the repository's da, de and la lexicons was tried as a keyword, folded or in two rows
  (`work/scripts/keyword_fold.py`): best 9 of 12 pairs. The keyword alphabets of the same unit ("Danus ...", images
  133-137) are known here only from the unit's inventory; the sheets themselves were not compared with this key.
- [x] print: catalogue.json, research/leads.json and two web searches (26 Nov 2026): no decipherment. The leaf is
  listed, not deciphered, in `targets/biermann1675/keyhunt.md` line 84 (Daniel Bourdeau, 27 Oct 2026). Danish printed sources
  (Danske Magazin, letter editions) were not searched.
- [x] key-rebuild: the key gives a value to every sign in the text (23 signs); the reciprocal pairing fixes the rare
  signs a, c, e and r; y has no partner sign in the text, so its pair b-y rests on "breff", "blød", "subtiler", the
  "bog-" of line 11 and "broder" (a hole).
- [x] retry: every hole and doubtful sign was re-read on 2x-4x crops after the solve and against the blind
  transcription (26 Nov); no hole closes.

## Conditions of the source

The image is Rigsarkivet's, free on Arkivalieronline with no sign-in, fetched by plain GET. No licence or other
conditions came with it, and its reuse terms were not checked, so no image or crop is filed here. AI agents working for
Andrew Beling read the image. Andrew Beling's recorded words of 25 Nov 2026 on these images: "I agree with your plans
and the image use for item 2". Andrew Beling decided on 25 Nov 2026 that Rigsarkivet images may be used with AI
readers.

## Rebuild

From the repository root, with the Python standard library:
- `python3 -I targets/vind1647/decrypt.py --check`
- `python3 -I targets/vind1647/count_words.py`
- `python3 -I targets/vind1647/review/compare_blind.py`
- `VIND_LANG=la python3 -I targets/vind1647/work/scripts/heldout.py` (and `da`, `de`), about 1 minute each
- `python3 -I targets/vind1647/work/scripts/agreement.py`
- `sh targets/vind1647/work/scripts/whole_text.sh`, about 1 minute
- `sh targets/vind1647/work/scripts/permcontrol.sh`, about 4 minutes
- `python3 -I targets/vind1647/work/scripts/keyword_fold.py`

Each was run twice and gave the filed output both times. All were rerun again on 28 Nov 2026 UTC (27 Nov local), 02:52-02:58 UTC, after
rebasing onto the repository's main branch of that day, and gave byte-identical output; the one exception is
`heldout_afterplan_de.txt`, which had been filed without its decode line and was refiled whole (result 4).

`validation.tsv` (one cipher letter per line with its value, model da-modern) is filed for `docs/_validate.py`. It could
not be run on 26 Nov 2026: the da-modern corpus fetch from gutenberg.org returned HTTP 503.

## Not checked

- Danish printed sources and the Vind family papers, for an edition or the puzzle.
- The viewer link (only the image API URL was fetched).
- Whether the leaf's year is 1647 or a slip for another year; 1647 rests on Vind's dates.
