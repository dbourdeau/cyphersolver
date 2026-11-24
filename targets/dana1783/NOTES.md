# Francis Dana to Robert R. Livingston, St Petersburg, 6 Apr 1783 (O.S.), No. 23: the eight cipher lines

Status: in progress. Next step: try the key and Dana's word list on the other despatches of PCC item 89 vol. 2 (the retry step). Dana's own table of October 1782 (PCC 89 vol. II p. 656, found by Brice Dudout) was viewed on 24 Nov 2026 and agrees with the break; see "24 Nov 2026" below.
Contributed by WAINUT (27 Oct 2026). Key recovered from the ciphertext alone; the three word codes 31, 137 and 168
are read with Dana's own table. The text is read in part: 47 of 52 words sure (0.904), with one group (29) open and
four words that carry an enciphering slip. The site page and the ledger rows are left to the maintainer; no page
exists yet.

Catalogue 485. Contributed by WAINUT (https://github.com/WAINUTAI). The work was done with AI language-model agents.
Every number was read twice from the NARA scan, the second time independently, and the decryption was checked
against the image.

## 1. The document

- **Source.** NARA RG 360, Papers of the Continental Congress, item 89 vol. 2 (microfilm M247), catalogue
  [naId 502963402](https://catalog.archives.gov/id/502963402), "Letters from Ralph Izard, Henry Laurens, John Jay and
  Francis W. Dana 1777-84: Volume 2". The letter runs from MS p. 727 (digital object 312, heading
  "St Petersbourg April 6th 1783. O.S.", docket "(Tript. No. 23)") to p. 730 (object 315,
  [scan](https://catalog.archives.gov/medialz/partners/dc-metro/rg-360/M247/pcc_404461_0001/407507.jp2)), where the
  cipher stands.
- **Which copy.** The docket says this is the **triplicate** of No. 23. The original and the duplicate were not looked
  for.
- **Date.** 6 April 1783 Old Style is 17 April 1783 New Style. Wharton, *Revolutionary Diplomatic Correspondence*
  VI (1889), pp. 381-383, prints the same letter as "No. 23. St. Petersburgh, April 17, 1783". The catalogue entry
  gives 6 Apr 1783; both dates are right.
- **Context.** Dana had told the vice-chancellor of his mission on 7 March and had no answer. The clear text ends:
  "I have only to pray Congress would be pleased to suspend their judgment upon this matter ... All may yet end as we
  wish; it may end otherwise." Then come eight lines of numbers. Wharton prints "(Here follow eight lines of cipher.)".
- **The cipher is Dana's own.** P.S. in clear: "I make use of the Cypher I sent you by Mr. Adams's Son, having laid
  yours aside for the reason there mentioned." On 23 Sept 1782 (Wharton V, pp. 752-754) Dana had written that
  Livingston's cipher was "intolerably tedious and so liable to errors" and that he would "prepare another scheme"
  and send it to Holland by Mr. Adams' son, John Quincy Adams, then his secretary.
- **A difference from Wharton.** The P.S. on the scan reads "Your printed one has come to hand with your letter".
  Wharton prints "has not come to hand". No "not" is visible on the scan.

## 2. The system and the key

Periodic numerical table of the type James Lovell used. The alphabet has 27 signs, a..z and &. A letter p under key
letter K is written (p - K) mod 27 + 1, so the key letter itself is 1. The key word is **WIN**, used letter by letter
in a cycle of three. The full table is in `key.txt`. Numbers above 27 (29, 31, 137, 168) are code groups. Their
meanings were not known on 27 Oct 2026, when this section was written; 31, 137 and 168 are now read from Dana's own
table (sections below), and 29 is in neither its alphabets nor its word list.

How it was found: the numbers run 1-27 apart from four groups, which suggests a 27-sign table. An index-of-coincidence
test over periods (in the solver's working scripts, not included) pointed to alphabet size 27 and period 3, but the
signal is weak (period-3 IC 1.30 x 27, against 1.12-1.23 for other periods). What finds the key is the bigram ranking
of all period-3 keys (section 5), not the IC. The key letters then followed from the best shifts. `decrypt.py` reproduces the decryption from `transcription.txt`.

## 3. Transcription and interventions

`transcription.txt` gives 212 tokens (measured): 204 fully visible letter numbers, 4 code groups, and 4 numbers cut by
the edge of the microfilm frame (lines 1, 3, 4 and 6) with only their first digit visible.
Line 5 ends with a third "1" stroke at the edge. The ink blot in line 3 is not a number.

The decryption needs these interventions. All are written into the working text in `decrypt.py`, which checks that,
with the annotations removed, it gives back the transcription.

- **Three slips by Dana**, each in a W position: line 1 "23" and line 2 "12" (in "any") were enciphered with N; line 6
  "24" (in "influence") with I. With W they would give r, g and s.
- **One skipped key position** in line 5, after "irresistab". Without the skip the next letters are g/w; with it, "le".
- **Four cut numbers completed**, each matching its visible first digit: 1| = 11 (s), 1| = 15 (a), 2| = 27 (m),
  2| = 26 (l).
- **Three letters supplied** at line ends where nothing is visible: o (20) at the end of line 2, f (11) at the end of
  line 5 (a partial stroke is visible there), n (1) at the end of line 7. The key phase of the next line requires
  exactly one position in each case. Line 2 shows no cut, so there Dana may simply have left the letter out.
- **Code groups and the key.** After each of 31, 137 and 168 the next letter is under **N** (on the raw numbers:
  "liketh...", "adopti...", "herehe..."; W and I give nonsense). In `decrypt.py` terms, after 137 the key continues
  and after 31 and 168 it moves two places on, but the simpler description is that every code group in the body
  resets the key to N. Dana's earlier key sheet "No. 1" (section 6) carries exactly such a rule on its back:
  "N.B. When you come to an arbitrary character begin [the] key word again." After the opening 29 the text starts
  under W, which the reset does not explain. It changes no letter. Because of this, the opening "[29]n an [31]" is
  not confirmed: the letters n, a, n decode directly, but how they join the groups is open.

Of 211 letter positions, 201 decode directly and 10 need one of the interventions above.

## 4. The reading

Line by line in `decryption.txt` (output of `python decrypt.py`), as sentences in `reading.md`:

> [29]n an [31] like this, which is not guided by any settled principles or system, you can be certain of no
> measure. What the [137] adopt in this hour may be opposed by an irresistible influence in the next. In short,
> properly speaking, there is no [168] here. Hence my present difficulty.

The plaintext is English. Dana writes "irresistable"; the reading normalises the spelling. Context suggests readings
for the code groups ("In an [empire? court?] like this", "what the [ministers? court?] adopt", "there is no
[system? ministry?] here"), but none is proposed as a value.

What the passage says: Dana explains why he cannot predict the answer to his mission. At the Russian court nothing is
settled by principle, and what one party adopts may be overturned by another influence the next hour. The letter
dates from the weeks when Catherine II gave no answer to Dana and had just accepted the invitation to mediate the
definitive peace.

## 5. Controls (`python decrypt.py --controls`)

Scores are mean letter-bigram log-probabilities, with bigrams counted from the repository's English word list
(`lang/lexicons/en.json.gz`).

- The decryption with the interventions scores **-2.739**.
- 200 random wrong period-3 keys with the same alignment: best -4.431, mean -6.102.
- All 19,683 period-3 keys on the raw stream (the 204 fully visible letter numbers, no corrections, key running
  straight on): WIN ranks second (-4.680) and its rotation NWI tenth. The best key, WIP (-4.652), differs only in the
  third letter: the uncorrected phase breaks at the code groups shift the third position. The median key scores
  -6.167.
- 200 shuffles of the raw stream under WIN: best -4.874, mean -5.513.

An independent check of 27 Oct 2026 (separate re-reading of the scan, separate decryption script, Federalist bigram
model) gave the same plaintext and the same controls pattern: blind search over all period-3 keys on the raw stream
put the rotations of WIN at ranks 0 and 8.

## 6. Prior work

- Wharton VI (1889), pp. 381-383, prints No. 23 with "(Here follow eight lines of cipher.)" and no decipherment.
- The Madison Papers (note to JM to TJ, 11 Aug 1783, Founders Online Madison/01-07-02-0151, quoted in the catalogue)
  say only 8 lines were encoded and that the passage is not decoded in Wharton.
- Wharton VI, p. 464, has the footnote "The key to Mr. Dana's cipher is missing." It belongs to a **different**
  letter, Dana to John Adams, St Petersburg, 1 June 1783, and to the figures 121 and 134.571 in it ("Most probably the
  figures stand for Dr. Franklin and the French ministry"). It says nothing about No. 23.
- Two web searches for phrases of the plaintext found no printed decipherment. The Papers of John Adams (vol. 13)
  describe a separate Livingston nomenclator endorsed "Mr Dana's Papers"; Dana's P.S. says he did not use
  Livingston's cipher here.
- **Dana's key sheet in PCC item 59 vol. 1** (pp. 137-138, naId 475671573 images 107-108, Fold3 172700-172701; listed
  in `targets/pcc1780`), checked after the break on a reviewer's lead. It is headed "No. 1": a 25-sign table (a..z
  without j and v, plus &) in three columns that are not the W, I, N alphabets, and a word list numbered 26-52
  (Washington 40, Congress 26, America 27, England 29, France 30, Holland 31, ... Russia 51, Court 52). It is not the
  27-sign WIN scheme of No. 23: 137 and 168 are not on it, and England / Holland do not fit "[29]n an [31] like
  this". So the WIN key was not available from it, and the method stays ciphertext-only. The sheet is probably the
  cipher Dana took to Russia in 1781; the 1782 scheme sent by J. Q. Adams was not found (27 Oct; it is the sheet at
  PCC 89 vol. II p. 656, below). The verso has the restart rule quoted in section 3.
- The Papers of John Adams vol. 13 (Dana to John Adams, 4 Oct 1782, and the editors' notes) describe Dana's cipher;
  not checked.
- Checked on 24 Nov 2026 (Andrew Beling, issue #898, and the integration review): the Hawkins transcripts, PCC item
  109 (naId 2316037), for Dana's table (objects 103-104) and for No. 23 (object 207). The transcript of No. 23 gives
  the cipher numbers, not a decipherment. The rest of that volume was not searched.
- Not checked: the original and duplicate of No. 23 elsewhere in the PCC (one may carry a decipherment), Giunta's
  *The Emerging Nation*, and the Dana Papers at the Massachusetts Historical Society. **No earlier solution was
  found, but the search was not exhaustive.**

## Dana's own table and Brice Dudout's parallel reading (27 Oct 2026)

Brice Dudout (Europe chiffrée, `https://bdudout.github.io/europe-chiffree/en/documents.html#dana-1783`) read the same
eight lines on the same day, independently. He first broke the three shifted alphabets blind (letter frequencies and
English 4-grams), as was done here, then found **Dana's table of October 1782 in the same volume, PCC 89 vol. II
p. 656** by leafing through it: three shifted alphabets of 27 signs (a-z and &) starting at n, w and i, used in turn; a
nomenclator of words and names numbered 30 to 305, three numbers per word; the keyword starts again after every
number above 27. Its three columns coincide with the shifts of his blind break, and it reproduces its own example
("When the Army of America go"). Dana's note on the sheet: he sends it "only because I have probable grounds to
suppose yours is in the hands of the Ministry here"; it went by John Quincy Adams. (Correction, 24 Nov 2026: the
bearer's name is not on the sheet, which says "This goes by a private & safe hand by whom I write to you". That it
went by John Quincy Adams comes from Dana's letters: p. 648 of the volume, where he will forward the new scheme "to
Holland by Mr Adams's Son", and the P.S. of No. 23.) This is the 1782 code list that section 6 looked for; the PCC 59
"No. 1" sheet is the earlier scheme.

Values for the four open groups, from his reading: **31 = Administration; 137 and 168 = Minister** (two of its three
numbers); **29 is Dana's slip for i** ("In an Administration like this"). So: "What the Minister adopt in this hour
may be opposed by an irresistable influence in the next. In short, properly speaking, there is no Minister here.
Hence my present difficulty." He counts 213 visible groups and 2 lost in the gutter, and four enciphering slips, each
the value of the letter in a neighbouring column; reading about 98%. On the sentences compared (lines 1-5), his
text and the reading here are the same wherever both give a value. Not checked here against p. 656 itself on
27 Oct; done on 24 Nov 2026 (next section). Catalogue 485 was removed on 27 Oct 2026 as read.

## 24 Nov 2026: Dana's sheet viewed, and the transcript copy in PCC item 109 (Andrew Beling, issue #898)

Andrew Beling (@ajbeling), with AI agents, found a transcript copy of Dana's table and of No. 23 in **PCC item 109**,
"Transcripts of Letters from Francis Dana, Henry Laurens, and John Laurens" (naId 2316037, 489 objects). The
integration review of 24 Nov 2026 (an AI agent, for the maintainers) opened the NARA images and also Dana's own sheet.
All of these are AI readings, his and ours; no person has checked an image.

- **Dana's own sheet, PCC 89 vol. II p. 656** (naId 502963402, object 262, file 407345, a wide frame with
  pp. 656-658), viewed on 24 Nov 2026, one AI reading at reduced size. It has the alphabet columns with a = 15, 6, 20
  and n = 1, 19, 6 (the N, W and I alphabets of `key.txt`, in that order); "Adams 30 61 92" and "Administration 1 2 3"
  (the list gives the last figure of each number, so 31, 62, 93); "Franklin 123 154 185" and "Minister 7 8 9"
  (137, 168, 199); the example "When the Army of America go" = 10. 13. 24. 1. 25. 27. 19. 35. 2. 11. 33. 21. 20; the
  N.B. on blank spaces; and "This goes by a private & safe hand by whom I write to you." It agrees with the break and
  with Brice Dudout's reading of it. Not checked: the whole sheet number by number, and the other words of each block.
- **The numbers go with the word before them.** The example has Army 35 and America 33 (Adams 30 + 5 and + 3), and
  the rule line of the copy gives "America. 33. 64. 95". So 137 and 168 are Minister, not the next word.
- **The example also gives the order of the key word: N, W, I**, and it starts again at N after a word number. That
  is the reset to N seen after 31, 137 and 168 in section 3. Rule on the copy: "When you come to an arbitrary
  character, begin your Key word anew. # Or to a Cypher above 27".
- **The item 109 copy of the table** (objects 103 and 104, files 418136 and 418140; transcript p. 102, margin
  "Mr Dana's Cypher"; NARA's description dates it 14 Oct 1782) has the same alphabets, the same two word lines and
  the same example, and "N.B. The blank spaces may be filled up with any words you may think proper to add".
- **216-263 have words.** On p. 656 the column "216 -" stands beside sixteen words: Spanish, State, Stockholm,
  Sweden, Swedish, Tartars, Treaty, Troops, Turkish, Turkey, United Provinces, United States, Vergennes (Count),
  Versailles, Vienna, Warontzow (Count), from Spanish 216, 232, 248 to Warontzow 231, 247, 263. A rule follows, and
  264-305 (fourteen rows of three) are the blanks. The item 109 copyist put the 216-305 columns on the next page,
  away from their words, which is why issue #898 took 216-305 to have no words. This does not touch No. 23.
- **No. 23 in item 109** (object 207, file 418502, transcript p. 202) is a clerk's letter-book copy that gives the
  cipher numbers in full: eleven lines, 215 numbers. Laid beside `transcription.txt`: all 208 fully read numbers
  agree; the four cut numbers are 11, 15, 27, 26, as completed in section 3; the three line ends supplied on the key
  phase are there, 20 after "24. 6." (line 2), 11 after "10. 1. 1." (line 5), 1 after "13. 24." (line 7). 29, 31, 137
  and 168 stand as in our text. 212 + 3 = 215. This is a clerk's transcript, so it confirms the seven numbers from
  another copy of the despatch, not from the triplicate's own sheet; which copy of No. 23 the clerk had is not known.
- **29** is in neither the alphabets (1-27) nor the word list (which starts at Adams 30). It stands in both copies.
  It is read as a slip for i from the sentence only. Worked out in this edit from `key.txt`, not seen on any image as
  a slip: 29 stands in the N position, where i is 23, so it is one figure from the letter the sense wants. It stays
  the one open group.

**Recount** (README rule: only sure words count, a marked letter makes its word a hole). `reading.md` now has 52
words. Holes: "In" (29), and the four words with one of Dana's slips or the skipped key position (is, any,
irresistable, influence). **47 of 52 = 0.904**, so read in part; a text of 52 words is above the short-text floor. If
the seven numbers taken from the clerk's copy were counted as supplied, five more words (or, measure, may, properly,
hence) would be holes: 42 of 52 = 0.808. Either way the class is the same. `python docs/_check_reading.py dana1783`
on `reading.md`: readable, clean share 0.8 (4 of 5 sentences as the checker cuts them), hole rate 0.07 (its own
word-list count, not the read bar).

## Remaining gaps

- Group 29 (1 of 215 tokens): not in Dana's table; read as a slip for i from the sentence - blocker: open-codes; one occurrence, and the retry on the other despatches is the only way left to see it again. (31, 137 and 168 are read with the writer's own key, seen on p. 656 and in the item 109 copy.)

Not a gap to work on, but counted as holes: four words carry an enciphering slip of Dana's or the skipped key position
(is, any, irresistable, influence). The numbers are as written and the correction is ours; they are the writer's
errors and stay marked.

Closed on 24 Nov 2026: the four cut numbers and the three line ends. The item 109 transcript of No. 23 (object 207)
gives the cut numbers as 11, 15, 27, 26 and has 20, 11 and 1 at the three line ends. It is a clerk's copy of the
despatch, not the triplicate's own sheet; the original and duplicate of No. 23 were not looked for.

## Escalation

- [x] siblings: the clear P.S. and Dana's letter of 23 Sept 1782 identify the cipher as his own scheme; other letters
  in it were not decrypted (next step). 24 Nov 2026: the clerk's transcript of No. 23 in PCC item 109 (object 207)
  opened; it gives the seven cut or missing numbers
- [x] clear-pages: the clear text of No. 23 (Wharton VI) frames the passage; it gives no crib for the code groups
- [x] known-keys: Livingston's cipher is ruled out by Dana's own P.S.; Dana's earlier "No. 1" sheet (PCC 59 vol. 1
  pp. 137-138) checked: a different, 25-sign scheme without 137 or 168; the key was recovered from the ciphertext.
  24 Nov 2026: Dana's own table of October 1782 (PCC 89 vol. II p. 656; copy in PCC item 109) viewed: it is the WIN
  table and gives 31, 137 and 168
- [x] print: Wharton V-VI read; the "key missing" footnote traced to the 1 June 1783 letter to Adams
- [x] key-rebuild: the letter table is complete (WIN); the code groups have one occurrence each
- [ ] retry: Dana's other 1783 despatches in PCC item 89 vol. 2 may use the same scheme and repeat the code groups

## Files

- `transcription.txt`: the eight lines as read from the scan
- `decrypt.py`: working text with the interventions, decryption and controls (standard library)
- `decryption.txt`: output of `python decrypt.py`
- `reading.md`: the reading as sentences (24 Nov 2026: word codes from Dana's table, slips marked)
- `key.txt`: the WIN table, and the words of Dana's list seen on p. 656
- `validation.tsv`: token-by-token pairs for `docs/_validate.py` (cipher type = key letter + number); verdict pass

## Independent reading by Brice Dudout (27 Oct 2026)

Same letters, read separately the same day; the three word codes are identified (31 Administration, 137 and 168 Minister). See `dudout/README.md`.

## 14 Nov 2026: reading review recorded

(Superseded in part on 24 Nov 2026: the sheet has been viewed, 31, 137 and 168 are read, and `reading.md` is
recounted at 0.904; see the 24 Nov section above.)

Both readings of No. 23 were read as sentences against their decryptions (Claude, session of 14 Nov 2026): `reading.md`
(read in part, read_share 0.855, four code groups open) and `dudout/reading.md` (word codes filled from Dana's table as
Brice Dudout reports). Each is four coherent sentences with its completions marked; `reading_review` grade A recorded on
each in `profile.json`. States unchanged. Dana's table sheet (PCC 89 vol. II p. 656) was not viewed here, so the first
gap in Remaining gaps stays as it is.
