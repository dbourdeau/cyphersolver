# Delacroix to Létombe, Paris, 25 Messidor an V (13 July 1797): despatch No. 5 in a French numeric code (catalogue 649)

Status: read in part (key recovered from external plaintext: the ministry's clear draft found by Andrew Beling, PR #884; owner's decision of 23 Nov 2026; written up 24 Nov 2026, `docs/delacroix1797.html`)

**State, 24 Nov 2026.** Method: key recovered from external plaintext (`outcome.method` "key recovered based on
plaintext from external sources"). Class: read in part. Key: partial. Owner's decision of 23 Nov 2026 on PR #884. The
ministry's clear draft of the despatch survives in Paris (Archives diplomatiques, CP États-Unis vol. 48, ff. 41r-42r);
Andrew Beling, with AI agents, found it, laid it on Brackx's 653 groups and built a partial table of the code
(`beling2026/`). Read share 0.948 since 25 Nov 2026 (23 holes; 444 cipher words by the contributor's script, 442 by our
reviewer's count, 419 of 442), after Brice Dudout's look at four doubtful digits on the film (sign plate 2511, PR #990);
0.939 and 27 holes before. Strict share 0.671: 298 of 444 words rest only on values confirmed by two or more agreeing
uses; 123 words rest on at least one of the 148 single-use values and count as probable (`strict_share.py`). See
"Integration of PR #884", "Write-up steps, 24 Nov 2026" and "Sign plate 2511" below.

The sections from "What the numbers show" to "Second round" record the ciphertext-only attempt of 2 Nov 2026, which
established no value: what they say about the meaning of groups is hypothesis, and most of it is now replaced by the
table. The structural findings in "What the numbers show" are measured.

## The document

- NARA RG 59, Despatches from US Ministers to Great Britain, vol. 5 = microfilm M30 roll 4, frames 0244 right, 0245 left
  and right (catalog naId 188512917). A clerk's copy marked "Dup.", "(Copy)", "No. 5 Duplicata". Enclosed in Rufus King's
  No. 53, London, 12 Nov 1797, which says: "I have no means of decyphering it."
- Heading in clear: "Le Ministre des relations extérieures au citoyen Letombe consul à Philadelphie, exerçant
  provisoirement le consulat général de la République Française aux États Unis". Close in clear: "Salut et fraternité",
  "Ch. Delacroix".
- Transcription by Michael Brackx (issue #122, 27 Oct 2026), `ciphertext.txt`: 653 groups, 297 distinct, values 2-1198
  (`_check_profile.py --measure`). His doubtful readings are listed in the issue. Frames viewed here at reduced size to
  confirm layout and page-foot catchwords; the transcription was not re-collated digit by digit in this session.

## Context

Létombe's reply No. 42, 22 Brumaire an VI, is printed in Turner, *Correspondence of the French Ministers* (1904), pp.
1076-77, from the ministry's decipherment (États-Unis vol. 48, f. 355). He admits having mixed consular and political
matters in his letters since the minister's departure, says he dictates the figures of his political letters himself,
and promises more attention to "ce qui m'a été prescrit par la dépêche du 25 Messidor dernier". So part of No. 5 probably
concerns how that correspondence is kept. This is a likely subject, not a crib with known wording.

## What the numbers show (measured)

1. **Neighbouring numbers cluster.** Summing min(f(n), f(n+1)) over adjacent values gives 162; 3,000 random
   reassignments of the same frequencies onto 2-1198 average 98, and none reached 162.
2. **Near-repeats vary by small steps** (`solver` session output; a search for aligned passages differing by at most 3):
   - `263 267 705 806 711 405 81 973 486` / `326 265 705 806 711 405 83 972 485` / `416 268 705 806 711 405 81 973 82`
   - `383 338 439 958 235 39 1083 489 1052` / `262 338 440 958 234 39 1083 489 1052`
   - `500 235 689 124 152 882 755 240` / `1163 234 689 123 151 882 755 247`
   - `310 174 973 266` / `1031 174 971 268`; `379 973 1122 317` / `596 973 1122 316`
   - `540 327 799 350 39` / `498 326 800 350 39`; `715 417 269 705 806` / `494 416 268 705 806`

   Inference: at least some entries own several consecutive numbers (homophones in small blocks), for instance 971-973,
   265-269, 81-83, 416-417, 326-327, 799-800, 234-235, 123-124, 151-152. Blocks are inferred from context, and their edges
   are unknown. The earlier reading of 972/973 and 81/82 as evidence for a one-part alphabetical code is not supported:
   a calibrated test found no alphabetical order ("Second round" below), and these pairs are better explained as homophones.
3. **711 and 400 fill one slot** in `705 806 _ 405` (5 and 2 times), so homophones also sit far apart.

Comparable in kind to the numeric syllabic nomenclators with homophones in `bouille1778`, but that is a comparison, not a
proof of the system.

## What was tried (2 Nov 2026)

1. **Annealing with the numbers in alphabetical order** (`solver/solve1.py`, Turner 5-gram). Degenerate: favours long words.
2. **Homophonic syllable annealing with a character model** (`solver/solve2.py`), with a length cap and overuse penalty.
   French-looking output, no agreement between seeds. Calibration on synthetic letters of the same size, with known keys
   and Turner text (`solver/calib.py`): true key scored 802-1338, annealed junk 1692-1789, token accuracy at most 0.037. This
   objective cannot find the key, and its outputs carry no information.
3. **Word-bigram Viterbi objective** (`solver/wsa.py`, `wordscore.py`). It separates true from junk on the synthetic
   letters (about -0.9 to -1.5 against -2.3 per character, with the test text inside the training corpus, which flatters the
   truth), but the search cannot reach the truth: at 300,000 iterations token accuracy stayed at or below 0.037 unpinned
   (`calib3.py`), 0.34-0.40 with 30-33% of tokens pinned correctly, and 0.60-0.65 with 51-53% pinned (`calib4.py`), which is
   only about 8-12 points above the pinned share. A tenfold-longer unpinned run (3,000,000 iterations) reached at most 0.028.
4. **Competing cribs on the real text** (`solver/realtest.py`, 4 seeds, 300,000 iterations): `705 806 711 405` + `265-269`
   as *la République* -2152 to -2128, as *le gouvernement* -2146 to -2100, nonsense control -2311 to -2232. Both beat a
   control whose pins are not French, which says little. They do not separate from each other. No output reads.
5. **Hand phrase matching.** Unverified ideas: `705 806 711 405` = République or gouvernement; `338 439 958 235 39 1083 489
   1052` = correspondance politique, or indépendance plus two groups; `1031 782 315 39` = confiance; `327 799 350 39` =
   puissance. None survives a check on all its other occurrences, and I retracted several while testing them. In particular
   405 was first taken as *ment*, then *que*. See `cribs.tsv`.
6. **Known keys** (`solver/keyscan.py`, each against 50 permuted copies of itself): Bouillé K6, Damas, the Martinique
   table, Mercier 1761, Ennery 1765, d'Affry code X, Champigny 1744. All within their own null range (for example Bouillé
   -2.900, null max -2.711; Ennery -3.005, null max -2.798). Ruled out. None is a Foreign Ministry key of the 1790s; no such
   key is held here or was found on DECODE metadata.
7. **Print and web.** Turner does not print No. 5. Searches found no edition or quotation of it. Schnakenbourg, "Un conflit
   sans grief ?", *AHRF* 2026/3 (no. 425), pp. 71-90, cites Létombe's letters in the États-Unis series, but only the abstract
   is open (Cairn, paywalled; read via Chrome after a 403). A search-result excerpt places Létombe to Delacroix, 29 Messidor
   an V, at CP États-Unis vol. 48, f. 73. Not checked: whether this article cites No. 5; Nasatir and Monell's calendar (1967).

## Second round (2 Nov 2026, at Daniel's request to keep attacking)

All on the word-bigram objective, after adding a limit of 5 values per entry, a reward for distinct entries and a penalty on
immediate word repeats. Synthetic letters here are held out of the language model unless stated.

| test | synthetic letters | real text | scrambled numbers |
|---|---|---|---|
| Strict one-part, homophones in blocks (`solver/mono.py`, 150,000 iterations) | -1818 to -2096, token accuracy 0.49-0.50 | -2527 to -2719 | -2596 to -2810 |
| Alphabetical inside blocks of 100 (`solver/blocks.py`, 120,000) | not run | -2220 to -2364 | -2235 to -2365 |
| Alphabetical inside blocks of 25 | not run | -2199 to -2230 | -2188 to -2218 |
| Two-part with consecutive numbers merged, word-placement moves (`solver/tied.py`, 300,000) | -2230 to -2504, accuracy at most 0.017; model not held out | -2179 to -2252 | not run |

- **One-part is the useful negative.** The method breaks about half of a synthetic one-part letter from scratch, so it would very
  probably have shown a one-part code here. The real text stays about 600 below those letters and overlaps the scrambled control
  (5 seeds each, so the comparison is rough). Strict alphabetical order is not supported, nor is order inside blocks of 100 or
  25, though those two tests were not calibrated.
- **Word-placement moves** (`solver/wsa2.py`, `calib5.py`) gave accuracy at most 0.031 from scratch, and pinning the top 20, 40
  or 80 groups gave only 3-6 points above the pinned share (`calib6.py`).
- **All real-text outputs here are noise.** Fragments such as "re pu bli que" or "de part est au" appear because the search can
  assemble common words on any input. The scrambled control does the same. They are not readings.

Conclusion so far: this search can only break a code with the alphabetical constraint. For a code without it, 653 tokens leave
the search unable to reach the true key even when the objective ranks that key first, so an outside crib of real length is
needed.

## What would move it

(Written 2 Nov 2026. The second item was met on 21 Nov 2026: the minute is in vol. 48, ff. 41r-42r. Vol. 47 was only
spot checked by the contributor; the CADN article is still unseen.)

- **CADN Nantes, Philadelphia consulate, 519PO/1, article 1** ("Correspondance avec le ministère des affaires étrangères,
  Arrivée: mars 1793-février 1798 ...", finding aid on archivesdiplomatiques.diplomatie.gouv.fr). New lead: this is where
  the received No. 5 or a deciphered copy would be, if kept. The finding aid has no entry naming a cipher table.
- **La Courneuve, CP États-Unis vols. 47-48**: the minute of 25 Messidor an V, or Létombe's ciphered originals beside the
  decipherments Turner printed, which would give pairs to rebuild the code.
- Any of Schnakenbourg's footnotes that cite the despatch.

## Remaining gaps

23 words of the reading are holes (25 marked groups), and 123 more words are probable only (since sign plate 2511,
25 Nov 2026; 27 holes, 29 marked groups and 121 probable before).

- 4 places where a digit change to Brackx's transcription is still proposed (257 three times, 1024) - blocker: illegible; a person (Brice Dudout, sign plate 2511, controls 3 of 3) read 7 at all three 257 places, as Brackx wrote it, so they stay holes: the plate settles the shape, not the value, and "ai" for 257 is found only at these three places; token 413 was read 1084, which is not in the table, so the hole stays. The other four proposals (108, 808, 327, 381) were read by the same look and applied (see "Sign plate 2511")
- 17 groups with an unsure (class C) value: 383, 496, 526, 571, 1122, 1126, 347 - blocker: no-key-material; each stands for different draft letters at different places, and only this one letter in the code is known
- 4 groups whose table value differs from the draft's letters (175 ses/se, 855 pres/pre, 355 iez/es, once ez, 20 ay/ai) - blocker: no-key-material; the draft is the minute, not the copy that was enciphered, and the sent wording is not held
- the 148 single-use values, on which 123 words of the reading rest (121 before 25 Nov 2026) - blocker: no-key-material; untested outside this letter, and no second text in this code is known: none on NARA frames 0236-0252, none among the targets, catalogue and leads searched again on 24 Nov 2026 (the only French diplomatic texts of these years there, `astrea1799`, Rozier to Talleyrand 1798, and catalogue 521, Rivals to Sieyès 1798, are not online), none in 39CP/48 (paged in full by the contributor); 39CP/47 was spot checked by the contributor only
- the received No. 5 or a deciphered copy in CADN 519PO/1 art. 1 - blocker: needs-physical-access; the article is not digitised as far as found

Open lead, not an unread piece: 39CP/47 (January to June 1797, 938 images online) has not been paged in full for a text
in numbers, and the other volumes of the series have not been looked at. The contributor's spot check of 39CP/47 and
full paging of 39CP/48 found the ministry's decipherments of Létombe's despatches and no numbers. On 24 Nov 2026 the
paging was not done here: the archive's viewer opens with a notice of its conditions of reuse that the reader must
accept, and that is the owner's to accept, not a session's ("Write-up steps" below).

## Transcription doubts

The digits are Brackx's (`ciphertext.txt`), unchanged; since 25 Nov 2026 four of them carry a correction from a
person's look on the film, kept as a separate layer in `ciphertext_corrections.tsv` (108 -> 100, 808 -> 898,
327 -> 527, 381 -> 361; "Sign plate 2511" below). The doubts below are the contributor's, each read blind on the
film (NARA M30 roll 4, frames 0244-0245) by three AI readers. Brackx's issue #122 lists several of the same places
(808, 1024, 381, 108, 1105) among the readings he checked twice at full resolution when he transcribed; since then no
person has looked at the film for them, and the project only at 300 and 1105 (below). Full list with the readers' answers: `beling2026/proposals/transcription_corrections.tsv` and
`beling2026/README.md`, "Transcription doubts".

- 808 (245 left, line 12, 8th group) - read: 898 with "80" written above (3 of 3 readers); checked: image, decode (898 = con four times; le-con); read 898 by a person (plate 2511); applied
- 1024 (245 left, line 13, 1st) - read: 1034 (2 of 3; the third 1084); checked: image, decode (1033, 1035 = e; pri-e); read 1084 by a person (plate 2511), not in the table; unresolved, hole kept
- 327 (245 left, line 25, 8th) - read: 527 (2 of 3; the third 327); checked: image, decode (527 = d three times); read 527 by a person (plate 2511); applied
- 257 at three places where the text has "ai" (244 right line 11, 9th; line 17, 6th; 245 left line 15, 4th) - read: 257 by most readers, and 257 by a person at all three (plate 2511); checked: image, decode; unresolved: the clerk wrote 257 for 251, or the code has something not understood
- 108 (244 right, line 19, 1st) - read: 108 or 128, no reader 100; read 100 by a person (plate 2511, both digits asked); checked: image, decode; applied (sur)
- 381 (245 left, line 25, 11th) - read: 381 (3 of 3, blotted); read 361 by a person (plate 2511); checked: image, decode; applied (del)
- 383 (244 right, line 7, 3rd) - read: 383 (one second choice 363); checked: image, decode; unresolved, the text wants "de la" (363)
- 300 (244 right, line 5, 10th) and 1105 (245 left, line 20, 1st) - read: 300 or 308 (308 by two of the contributor's readers), and 1105, 1185 or 1195; checked: image, decode; seen in passing by the contributor; looked at again on the frames at twice their size on 24 Nov 2026 (an AI reading for the maintainers, not a person): the last digit of 300 has the same looped form as the last digit of 630 two groups on, and the third digit of 1105 is a filled loop over show-through; each number occurs once, so the decode gives the draft's letters (the l of fédéral; France) under any of these readings and cannot decide; unresolved, Brackx's digits kept

## Escalation

- [x] siblings: frames 0236-0252 have no decipherment (Brackx); catalogue and leads searched for Létombe, Delacroix, Talleyrand, Adet, Fauchet: `astrea1799` (Rozier 1798, ciphertext not online) only, and no shared key shown; the contributor paged 39CP/48 in full and spot checked 39CP/47: the ministry's decipherments of Létombe's despatches, no second text in numbers; searched again 24 Nov 2026 over the catalogue, the leads and every target profile of 1789-1803: nothing new online (catalogue 521, Rivals to Sieyès 1798, is in the Archives nationales, not online)
- [x] clear-pages: heading and close only on the NARA copy; King's No. 53 has no decipherment; the clear draft found in Paris, CP États-Unis vol. 48, ff. 41r-42r (Beling, 21 Nov 2026)
- [x] known-keys: seven French numeric keys in the repo tried, all within chance; 24 Nov 2026, the table compared number by number with every key file under `targets/` (`key_compare.py`): the seven French keys agree on 0 of their 39 to 209 shared numbers, and no file of the 174 compared agrees on more than 3
- [x] print: Turner 1904, web searches; Schnakenbourg 2026 paywalled; Nasatir and Monell not seen; 24 Nov 2026, four web searches on the draft's wording, on King's No. 53 and on the ministry's cipher: no printed or quoted text of No. 5 and no table
- [x] key-rebuild: 2 Nov annealers and hand phrase matching gave no key; 21 Nov the contributor's table from the draft: 297 numbers, 136 confirmed by two or more uses
- [x] retry: 24 Nov 2026, the table applied again to all 653 groups and compared with the reading by `docs/_replay.py` (`replay.py`): no difference that the reading leaves unmarked; every group already has a table value, so the 29 marked groups need a person on the film or a second text in the code, not another run; 25 Nov 2026, a person's look (sign plate 2511) settled four of them, and the replay rerun with those digits leaves 22 marked words and none unmarked

## Files

`ciphertext.txt` (Brackx's transcription), `ciphertext_corrections.tsv` (four digits read by a person on sign plate 2511, a layer over Brackx's), `dudout/` (Brice Dudout's sign plate 2511, PR #990), `cribs.tsv` (unverified hypotheses of 2 Nov, superseded by the table),
`solver/` (scripts; the Turner text, model tables and logs are in the untracked local `.work/delacroix1797/`), `img/`
(NARA frames 0243-0245, not to be committed), `beling2026/` (the contribution of PR #884: draft transcription,
alignment, partial table, decryption, reading, translation, tests), `strict_share.py` (the strict share),
`key_compare.py` (the table against every key file in the repository), `replay.py`, `replay.tsv`, `replay.json` (the
key replay), `mk_validation.py`, `validation.tsv` (the pairs for `docs/_validate.py`), `mk_reveal.py` (the passage
shown on the page, `docs/reveal/delacroix1797.json`).

## Order of events in `beling2026/` (Andrew Beling, with AI agents)

The claim that the test plan came before the draft was read rests on local file times and SHA-256 sums only (no
outside timestamp). The draft (CP États-Unis vol. 48, f. 41r) was first opened on 21 Nov 2026 at 00:52:04 EST, by the
AI agent that found it (its request log); two blind AI readers transcribed it 01:07-01:13 EST; the plan was written and
hashed (with the scripts and the ciphertext) at 01:31 EST and the test text fixed at 01:32 EST
(`plan/FREEZE_before_reading_draft.txt`), by an agent that, by its own record, had seen the two readers' short reports
(line counts and hard spots such as "[facilité?]", "Boston") but not the draft's wording. (This line read "hashed at
01:32" until the claims review of 24 Nov 2026.) See
`beling2026/README.md`, "The test".

## Integration of PR #884 (maintainers, 23-24 Nov 2026)

Owner's decision, 23 Nov 2026: method key recovered from external plaintext, class read in part, and the words that
rest on the 148 single-use values count as probable, with a strict share beside the contributor's 0.939.

- **What was checked at review** (two rounds, an AI agent for the maintainers; not a person): the table rebuilds from
  the alignment to `beling2026/key/code_table_F_partial.tsv` exactly; a decode of `ciphertext.txt` with it equals the
  filed decryption; the contributor's second scorer for the held-out test gives 36 of 43 predictions on the last 85
  groups (1,000 shuffled keys: mean 12.3, at most 18); the frozen hashes match.
- **Not checked by us:** the draft against the archive's images (the viewer needs JavaScript), the NARA film, and
  tests 1, 2a and 2b by rerun. Who read what (corrected after the claims review of 24 Nov 2026; this line read "Every
  reader of the draft and of the film is an AI agent; no person has looked", which the profile's transcription record
  contradicts): the 653 groups were transcribed from the film by Michael Brackx, recorded in `profile.json` as a
  person's transcription (issue #122, where he lists the doubtful readings he checked twice); the draft was read only
  by AI agents (two readers and a third that merged them), and no person has read it; the eight digit proposals rest
  on the contributor's AI readers; no person has compared the reading with the film.
- **Read share** (at that date; 0.948 since 25 Nov 2026, "Sign plate 2511"). 27 words carry a mark: 0.939 (444 cipher words by `beling2026/scripts/make_reading.py`, 442 by our
  reviewer's count, 415 of 442). The reading is the draft laid on the groups, so this share is circular by design: it
  says how consistently the table gives the draft.
- **Strict share** (`python strict_share.py`, same word division and marking rule as `make_reading.py`): 296 of 444
  words rest only on class A values (two or more uses that agree), 0.667; 121 words touch a class B or B2 value (one
  use) and are probable; 27 are holes. Tokens: 481 A, 103 B, 45 B2, 24 C. Marked groups 29: 17 with a class C value, 8
  at proposal places, 4 where the table value differs from the draft's letters.
- **Reading review**, grade B, 24 Nov 2026: the reading read in full as sentences; coherent French throughout, the
  holes are short words or parts of words. Recorded in `profile.json`.
- **Digit proposals.** The eight changes in `beling2026/proposals/transcription_corrections.tsv` are proposed, not
  applied. `ciphertext.txt` is Brackx's, unchanged.
- **The draft is not the sent text.** One clause has no groups in the American copy ("est arrivé à Paris, il y a
  quinze jours: Il"); the groups carry "utilité" where the draft's overwritten word reads "facilité".
- **Old attempt.** `outcome.parts` keeps the ciphertext-only attempt of 2 Nov as its own part, not solved.
- **Owed at that date, done on 24 Nov 2026** (next section): the write-up page, catalogue 649 known/open, the README
  row, and the DECODE queue entry (held until Brackx and Beling agree). The page's claims review is the coordinator's.

## Write-up steps, 24 Nov 2026 (an AI agent for the maintainers; not a person)

Stopping point by the six escalation steps: every marked group and every single-use value waits on a person looking
at the film or on a second text in this code, and no second text is known. One lead stays open (39CP/47 in full, see
"Remaining gaps").

- **Siblings.** The catalogue, `research/leads.json` and every target profile of 1789-1803 searched again for French
  diplomatic texts in numbers: `astrea1799` (Rozier, whom this despatch names, to Talleyrand, 1798; the numbers are
  on a Massachusetts Historical Society microfilm, not online) and catalogue 521 (Rivals to Sieyès, 1798, Archives
  nationales 284AP/12, not online). Nothing to apply the table to.
- **Known keys, direct comparison** (`python key_compare.py`). With the table in hand the 2 Nov scan can be made
  exact: for each key file under `targets/` that lists numbers with values, the numbers this letter uses that carry
  the same value in both. 174 key files compared. The seven French keys of the 2 Nov scan agree on none of their
  shared numbers (Bouillé K6 0 of 129, Damas 0 of 131, the Martinique table 0 of 130, Mercier 1761 0 of 50, Ennery
  1765 0 of 209, d'Affry code X 0 of 39, Champigny 1744 0 of 81). The most any file reaches is 3 of 47 (the Danish
  chancery's French syllabary of `petkum1665`). No key held here is this code or an edition of it.
- **Print.** Four web searches (the draft's wording "hazards de la mer", "mauvaise foi des porteurs", "recours au
  chiffre"; Rozier, Mozard and Hauterive with Létombe; King's No. 53 and "no means of decyphering"; the ministry's
  cipher of 1797): no printed or quoted text of No. 5 and no table of the code.
- **Key replay** (`python docs/_replay.py delacroix1797`; adapter `replay.py`). The table applied to Brackx's 653
  groups and compared with the reading: 441 words by the tool's division (it does not divide at hyphens, so New-yorck
  twice and Etats-unis once count as one word each, which is the 444 of `make_reading.py` less 3); 414 exact (93.9%),
  27 marked in the reading (the tool lists 26 as marked and one, `[ay]ent`, as an i/y difference), none unmarked.
  Where the table lists two values for a number the listed one that the alignment has is taken; the adapter's header
  says how class C numbers and the proposal places are handled.
- **Statistical validation** (`python mk_validation.py`, then `python docs/_validate.py delacroix1797 --write`):
  underdetermined. 622 groups read, 285 numbers, 2.18 uses per number. The reading scores -1.938 per letter on the
  `fr-modern` model; random keys of the same shape -2.514 on average (z 10.1); but a key of the same shape fitted to
  the shuffled groups reaches -1.935 on average and -1.927 at best, and the fitting search on the real groups reaches
  -1.911. So the letter model cannot tell this table from a fitted one on a text this short; the test neither confirms
  nor refutes it. The reading is real French by construction (it is the draft). The evidence that the draft is the
  text behind the groups stays the contributor's held-out test.
- **Two doubtful numbers looked at on the frames** (300 and 1105, "Transcription doubts"): not settled.
- **The Paris volumes.** The archive's record pages and its search are plain pages (a search for 39CP/47 gives the
  record `ark:/14366/dg3f7hv6c1bq`, "1797, janv.-juin", 938 images; 39CP/48 is `ark:/14366/bg45qmrw70n9`, 841
  images). The images open only in its viewer, a JavaScript application: use Chrome for it. Opened in Chrome, the
  viewer shows a notice, "Conditions de réutilisation", with one button to accept the ministry's conditions of
  reproduction and reuse. Accepting terms is the owner's act, so the session stopped there: the draft was not seen on
  the images and 39CP/47 was not paged. A scripted call to the viewer's own interface was refused by the session's
  permission rules after one answer (record metadata only, no image) and was not tried again.
- **Catalogue 649** is taken out of `catalogue.json`, as the write-up skill says for a target written up, and listed
  in `CATALOGUE.md` under "Read or resolved here, and removed"; the README row carries what the entry held, the
  offline key material included. **DECODE:** no record of this despatch is known (none in the notes, the
  profile, the vetting of 2 Nov or the local DECODE harvest); the queue entry is a skip with a hold: Brackx's
  transcription and Beling's draft transcription, table and decryption are not sent before they agree.
- **Image.** The page's crop is cut from NARA frame 0244 (right page, heading and first five lines). No image of the
  Paris draft is used.

## Sign plate 2511 (Brice Dudout, 25 Nov 2026, PR #990)

The person's look at the film that the eight digit proposals waited for. Brice Dudout answered a blind shape plate
made from NARA M30 roll 4 frames 0244 right and 0245 left (`dudout/sign_check_2511/`): each doubtful digit boxed on
its line and enlarged, options cut from clear digits of the same hand, no reading, value or meaning shown, three
hidden controls. The rule (`REGLE-SELECTION.md`, English `RULE-2511.md`, sha256 0bc3ef05...51ed58) was hashed before
the vignettes and the answers, and says which outcomes are applied: only a change whose corrected group already
carries the draft's letters in the table.

- **Controls** 3 of 3. **Read:** 808 -> 898, 327 -> 527, 381 -> 361, 108 -> 100 (both digits asked); 257 as written at
  all three places; 1024 -> 1084. 9 target digits: 5 corrected against Brackx, 4 as transcribed. Recorded as
  `outcome.sign_check`. Model roles not stated by the contributor; recorded from the files (the PR is signed "Brice
  Dudout (with Claude)", so all five roles are listed).
- **Applied** (the plate's patch, `dudout/delacroix1797-planche-2511.patch`): the four groups 898, 527, 361, 100 in
  `beling2026/key/alignment_by_group.txt`, and their four lines removed from
  `beling2026/proposals/transcription_corrections.tsv`. Brackx's `ciphertext.txt` is not changed; the four digits are
  recorded as a correction from this look in the new `ciphertext_corrections.tsv`, which `replay.py` and
  `mk_validation.py` apply, so that the transcription and the alignment agree.
- **Counts before -> after** (`python strict_share.py`): holes 27 -> 23 (marked groups 29 -> 25, proposal places
  8 -> 4); sure 296 -> 298; probable 121 -> 123; read share 0.939 -> 0.948 (419 of 442 on the reviewer's count);
  strict share 0.667 -> 0.671. Words that leave the holes: [sur] tout, le[çon], [d]'envoyer, [dél]ai. The filed
  reading file (`beling2026/readings/reading_1797-07-13.md`, the contributor's) still marks these four places.
- **Key replay** rerun (`python docs/_replay.py delacroix1797`): 418 of 441 words exact (94.8%; 414 before), 22 marked,
  no unmarked difference. The statistical validation of 24 Nov 2026 was not rerun (`validation.tsv` unchanged).
- **257.** The three places stay holes, as the contributor's rule has it. The plate settles the shape (a 7), not the
  value: "ai" for 257 is found only at these three places, whose reading was in doubt, so counting it would take the
  value from the sense. Counting it would give 422 of 444 = 0.950. A sign check does not change a class.
- **Token 413** read 1084 (the third reader's choice), neither Brackx's 1024 nor the proposed 1034; 1084 is not in the
  table, so the hole stays.
- **Class** stays read in part: 421 of 444, and 95% needs 422.
- **Not checked:** the digits on the film frames (the plate's crops are not filed). The option order was fixed in the
  rule, not shuffled; the chosen option was the first on 6 of 12 questions, including 4 of the 5 digits behind the
  changes, while the controls passed at other positions. Rule, key and answers are in one commit, so the order of
  events rests on the contributor's record.
