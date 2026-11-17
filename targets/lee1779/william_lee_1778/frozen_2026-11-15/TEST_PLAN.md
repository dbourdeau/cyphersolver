# Test plan: two Lee letters of 1778 in the Entick dictionary code

Written 15 November 2026, about 03:55 EST, before any reader or look-up helper was started and before any group of
either letter was looked up in the dictionary by the worker. One run. A miss is reported as a miss.

Worker: one Fable agent (Claude Fable 5.2). Helpers: Fable only.

## What the worker had already seen when this was written (so that it is not mistaken for blind)

- Tonight's sweep notes (`output/sweeps_2026-11-15/sweep_2026-11-15_gap_paging/unread_william_lee_1778.md`): a single
  transcription of both letters and eleven of the faint words over Francis Lightfoot Lee's groups (Join, You, Junto,
  dupe, enemy, brother, Doctor, part, Deane, caution, before).
- Ford's printed text of William Lee's letter (1891, II 491-493) with his three guesses from the sense (Franklin,
  Deane, "Williams, nephew of Franklin").
- Edmund C. Burnett's typed partial key, filmed on roll 1 of the Lee Family Papers microfilm, as transcribed by an
  earlier agent (`output/push_2026-11-14/wt-lee1779/targets/lee1779/received/burnett_key_roll1.tsv`). It gives a
  value for ten of the twelve different groups of William Lee's letter (169bXXI in = frank[lin], 92bXXVII come,
  259bXXXII off, 110aXXVIII criticism, 426bXXVIII you, 177aXVI en = give(n), 415aX us, 39bII advice,
  373aXXXIV the?/their?, 253bXXI nephew) and for several of Francis Lightfoot Lee's (40bXXXIV against, 72aVII
  brother, 80bXI caution, 134aVI Doctor, 282bVIII plot, 426bXXVIII you, 115bXXVIII/XXXVIII Deane).
- Our own Arthur Lee key (`.../lee1779/key.tsv`): 115b38 Dean, 426b28 You, 415a10 Us, 218b3 Junto, 145a34 Enemy,
  134a6 Doctor.
- The full-size frames, while cutting the strips; the pencil word "He" beside the inserted numeral of the first
  group of Francis Lightfoot Lee's letter.
- In the machine-read text of the 1776 dictionary, the lines of p. 169 column b (an unreliable count; not used).

Because of this the worker does not read figures for the test, does not look anything up for the test, and does
not settle disagreements between readers for the test. Those steps are done by helpers who are shown none of the
above.

## The rule under test (frozen; from the Arthur Lee work, pull request 663, not changed here)

John Entick, *The New Spelling Dictionary*, London: Dilly, 1776 (Internet Archive
`bim_eighteenth-century_the-new-spelling-diction_entick-john_1776`; printed page p = image index p - 1). A group
"page, column, line" is the Nth headword entry counted from the top of that column; the running head, the letter
headings and the indented run-over lines of long entries are not counted. Pages 454-455 (Christian names) have
five columns a to e. An ending written after a group is added to the word.

## Step 1. Figures (blind double reading)

- Strips cut from the full-size frames (Internet Archive `.../page/n<N>.jpg`, 6,400 to 6,900 pixels wide): one
  line of writing each for Francis Lightfoot Lee's letter, cut to the band of the figures so that the pencil words
  above are left out (checked by the worker on check sheets; small specks at the strip edges removed by a filter
  that keeps ink strokes); for the first group, whose line numeral is inserted above the line beside a pencil
  word, a separate patch with the pencil word covered by a grey box. William Lee's letter has no words above; its
  strips show two or three lines.
- Readers A and B (Fable, separate agents, each confined to its own folder) transcribe page, column and line of
  every group, figure by figure, and freeze their files (sha256) before the worker opens them.
- Seeds, mixed in as sections of their own and not labelled: batch W (William Lee) carries the strip with
  332,b,XXVIII / 389,a,XVIII / 82,b,V-s; batch F (Francis Lightfoot Lee) the strip with 335,b,VI / 255,a,XX /
  96,b,XX (a fourth group on that strip, 348,b,XIII, is recorded but not required). Both strips come from Arthur
  Lee's letters used in the tests of the Arthur Lee package, where their values were settled. Required: page,
  column and line of all three groups. A batch that misses a seed is rejected and read again once by a fresh
  reader; if the second reader also misses, the batch is used and the failure is stated.
- Agreement is reported as the number of groups on which A and B give the same page, column and line.
- The figure used for the test: the reading A and B share. Where they differ, a third blind reader C reads those
  groups (not told the two readings) and the reading two of three share is used. If all three differ, the group
  has no settled figure and counts as a miss in step 3. The worker looks at the image for such groups only after
  the score, for the reading (step 4), and says so.

## Step 2. The words above the groups (Francis Lightfoot Lee's letter), afterwards

After A and B have frozen, a helper G is given crops that show the space above each group and transcribes what
is written there: a whole word, a few letters, or nothing legible. G is not given any look-up. G's file is frozen
before the look-up is compared with it. **Test groups = the groups over which G reads a whole word** (three or more
letters that make one identifiable word; a question mark after the word does not disqualify it). Groups with only
an initial or fragments are reported separately (does the look-up begin with that letter?) and are not in the score.
If G reads fewer than ten whole words, the worker says plainly that the glosses are too faint to carry an 80% test
and reports the count as it is.

## Step 3. Look-up and score

- A helper L, shown neither letter, nor any gloss, nor Burnett's key, nor our Arthur Lee key, looks up on the
  1776 page images every group (and both candidates where step 1 left two) by the frozen rule, and for the
  controls: the same column and line on page + 1, on page - 1, and the other column of the same page. L freezes its
  table before the worker compares anything.
- **Francis Lightfoot Lee, 12 August 1778.** Hit = the headword L finds is the word G read, or the same headword
  in another form (plural, tense, a spelling variant such as Dean / Deane, or the headword plus the ending written
  after the group). A different headword is a miss even if it is next to the right one (You / Your).
  **Pass mark: at least 80% of the test groups hit, and each of the three controls under 10%.**
- **William Lee, 15 October 1778** (no words above). What counts as a sound reading, fixed now:
  1. *Prior values.* Eleven of the twelve different groups have a value proposed before us and independent of our
     dictionary rule: Burnett's typed key (ten groups, listed above; he worked from the sense and a 1782-83
     edition that does not fit) and 115,b,XXXVIII = Deane (glossed at the time in other letters on the same roll;
     Ford's guess). L's headword must be that word (any alternative Burnett lists counts; "frank" + in for
     Franklin; give for give(n)) in **at least 9 of the 11**, with each control giving the prior word in **at most
     1 of 11**. If the double reading changes a page figure (for example 180 against Burnett's 110), the group is
     scored on the figure the readers settle, against Burnett's word.
  2. *Grammar.* Every one of the twelve groups must land on a real headword, and that headword must fit the
     slot in the clear text, by part of speech as written here in advance: 169b21+in a name or designation of a
     person; 115b38 a noun or name (subject of "will"); 92b27 a verb in its base form; 259b32 an adverb,
     preposition or noun completing the verb; 180/110a28 a noun or name after "with"; 426b28 a noun or pronoun
     (subject of "taken care"); 177a16 a verb in its base form after "to"; 415a10 a pronoun or noun (object);
     39b2 a noun after "timely"; 305b30 a noun after "of his"; 373a34 an article, possessive or adjective;
     253b21 a noun for a person ("... of [Frank]in ... has made £40,000"). **All twelve must fit; the controls
     must fit in at most 3 of 12 each.** Fit of the control words is judged by a helper J who is given the clear
     text with numbered blanks and, for each blank, the four candidate words (rule, page + 1, page - 1, other
     column) in shuffled order without labels.
  Both parts must hold for the reading to be called sound.
- **Other printings (information, not controls).** The folder holds page images of the 1776 printing only (24
  pages of 1772; none of 1773 or 1781), so the brief's condition for those controls is not met. The machine-read
  entry tables of 1773 and 1781 made on 14 November are looked up at the same coordinates and reported as
  information. The 1773 printing shares most page breaks with 1776 (it gave 44 of 71 in the Arthur Lee gloss
  test), so it is expected to score well above 10% and is not a control.

## Step 4. Reading (after the score)

Firm: at least two blind readings of the figure agree on page, column and line, and the headword fits the clear
text. Two candidates: the readers differ and both words are given. Unread: no settled figure, or a headword that
does not fit. Prior values (the pencil words, Burnett's key, Ford) are credited group by group.
