# Cossit–Sumner correspondence to Sherwood: Entick dictionary code, 1783

Status: in progress — partial reading; the copied numbers are to be checked against British Library images of the originals (on order), and part of the modern literature is still unchecked.

Andrew Beling, with his own AI agents, 12–13 November 2026. **Read after matching with key from external sources, in part:** Nos. 1, 2 and 4 are read in part (for No. 2, its first half). No. 3 is **decoded, not read**. This is not a first decipherment: Justus Sherwood himself read much of this in 1783 (most of Nos. 1 and 4 and some of No. 3), and his sketch was used as a crib from the outset. The credit for those readings is his.

## Documents and context

Four numbered messages from the Cossit–Sumner intelligence correspondence survive in British Library Add MS 21838, ff. 306r–307v. The witness used here is the **1880s Library and Archives Canada hand copy**, B.178 pp. 345–347, on Canadiana reel H-1737 frames 15–17. Earlier research confused copy page numbers 345–347 with British Library folios; the package corrects this. Stable transcription labels `f345/f346/f347` identify copy pages only. [Source links and witness table](SOURCES.md).

No. 4 is dated 16 February 1783, addressed C.S.L.B.H. (probably Captain Sherwood, Loyal Blockhouse), and endorsed from Mr Sum--r. Nos. 1–3 share the next sheet; individual authorship is not established. A passage after the word “three” on the reverse has been treated as the end of No. 3 because its letters left at St Johns and closing to Holland match the end of Sherwood's No. 3 sketch. Its date is 11 February 1783. This joining is an inference, not a separate fifth message proved by numbering.

Ranna Cossit and Benjamin Sumner were Loyalists associated with Claremont, New Hampshire. The letters belong to the Vermont negotiations/intelligence network around Haldimand, Sherwood and Smyth. No. 4 reports a march toward Oswego, feared instead to be directed against Vermont. Sherwood's separate 19 February report and “Plain Truth” of 2 March identify the contemporary expedition as Willett's; that contextual identification is not a codeword recovered here. Colonel Strong is likely John Strong of Dorset, but the cipher itself supplies only Strong. Holland's forename and the man described in No. 2 are not established by these messages.

Related but separate: Haldimand's headquarters also corresponded with Sir Henry Clinton in a line-column cipher. Brice Dudout's pointer in issue #359 (9 November 2026) covers Clinton to Haldimand, 22 October 1779 (British Library Add MS 21807, LAC transcript B.147), with its contemporary clear; the project recorded it on lead 1137. That is a different system from the Entick dictionary code and is not part of this folder.

## System and how the book was found

A group gives **printed page and printed line down either unmarked column** of John Entick's *New Spelling Dictionary*, London 1781, scanned as Internet Archive 11280377bsb. Continuation lines count. The market-town appendix supplies place names. Dictionary headwords can represent inflections, fragments or sound-alikes. See [KEY.md](KEY.md) and [key.tsv](key.tsv). No silent digit corrections or column choices have been passed off as a deterministic key.

Sherwood's sketch suggested member, new, the and related words; these fitted Entick pages. The pre-registered No. 4 test then compared a frozen lemma list from Sherwood's sketch with cipher page numbers. It scored 8; six shifted-page controls scored 1, 1, 0, 3, 1, 2, meeting the recorded rule (8 or more, controls at most 3). The pass is narrow: one of the 8 hits, Say, counts only because the scan's text recognition places it on p. 315; without it the score is 7, below the frozen mark of 8, while recognition errors also cost three real hits. The frozen result is kept as it is. A packaging rerun on the original input files reproduced this exactly, and the frozen transcription hashes matched. This supports the book identification. It is **not** a blind recovery of the message, and it validates neither every numeral nor every proposed word. The OCR drops 17 of 30 lemmas and sometimes chooses an irrelevant first headword occurrence; the modest page-match test is reported as run, without improving it after the result.

The later pre-registered edition screen compared ten scanned printings. The 1781 copy scored 54/79 in the OCR page screen; the next best, 1772, scored 21/79 and did not pass the half-baseline threshold for visual row scoring. Visual counting of 1781 gave 77/79 in set A and 19/28 in set B: **96/107 exact or same-stem hits**. The other inspected printings do not share the matching page layout. Unexamined printings with an identical setting are not excluded. The gloss test gave only 3/9 exact, below its required 4 of 5 alphabetically possible glosses: **that separate question remains open**. Frozen rules and scores are in `evidence/`.

Apparent errors include swapped page digits (32-12 for 23-12, at; 64-12 for 46-12, by), a page one high (176-26 for 175-26, house), a wrong first digit (242-8 for 142-8, five), wrong-column glosses (formidably versus forward), and sound-alikes (Slay/sleigh, Inn/in). These could involve encoder, reader or nineteenth-century copyist mistakes; only the originals can separate their responsibility. The supposed word “Enticks” in Sherwood's private-correspondence letter remains unsettled, so it is not used as direct proof of the book's name.

## What this pass adds

The image retry corrects **No. 3 216-11 → 218-11 = Magnanimous**. Two of our own AI agents separately inspected the copied numeral and counted Entick p. 218 left row 11 from Magician = 1. Thus the former “name after the General” gap was a transcription error. The possessive in “the General['s] magnanimous clemency” remains supplied. No claim is made about the eighteenth-century original numeral until that arrives.

The retry inspected all nine specified No. 3 pairs, neighbours in both columns, selected digit swaps, and No. 4's ending. No supported connected reading emerged for the remaining gaps. The separate sign after 6-26 is retained as an extra hole; the earlier item tally omitted it. [RETRY.md](RETRY.md) records accepted and rejected possibilities.

## Full texts and measurements

Each message has a diplomatic transcription, a complete occurrence-by-occurrence decryption, a reading with every supplied ending or conjecture bracketed, and a summary. `transcription_all.txt` retains interlinear glosses, the repeated catchword and endorsements. The four per-document texts retain all message lines; addresses/endorsements are in the complete transcription. `lookup_occurrences.tsv` preserves every dictionary decision, including plain items, dates and the cancelled group. English originals need no separate translation.

| Message | Code groups | Strict reading share | Editorial state |
|---|---:|---:|---|
| No. 1 |56|64.5%|read in part|
| No. 2 |32|77.8%|read in part (first half)|
| No. 3 plus probable continuation |81|63.8%|decoded, not read|

The probable continuation on copy p. 347 is labelled No3 in `lookup_occurrences.tsv` and `key.tsv` (lines f347.*), matching these counts; an earlier draft labelled it P5.
| No. 4 |47|70.2%|read in part|

The profile also records 169/216 (78.24%) direct dictionary-supported code groups, excluding all conjectural repairs; this is key-lookup coverage, not a sentence-reading claim.

There are 216 code groups under the declared counting rule. Counts use the repository's `_check_profile.py --measure` on normalised group-only files, excluding literal figures/words, cancelled figures and the dangling sign, but including the encoded month and each malformed written group as one unit. These files are measurement derivatives, not substitutes for the diplomatic transcription.

Strict reading shares are the repository `v2_score.py` explicit-hole measure over each `## Reading` body, including plain text; supplied endings and uncertain replacements count as holes. Earlier research figures that counted dictionary evidence rather than readable prose are superseded and not used. For comparison, direct dictionary/plain evidence covers 47/61 items in No. 1, 27/34 in No. 2, 63/86 in No. 3 combined after the correction and extra sign, and 38/50 in No. 4. Those counts include dates/plain text and do not test sentence sense. `measurements.json` and `verify.py` reproduce the package's actual measurements. A high token score does not turn No. 2 or No. 3 into readable prose.

The statistical validation (`docs/_validate.py`, pairs in `validation.tsv`, 13 November) is **underdetermined**: with about 1.3 occurrences per code group, a key fitted to shuffled groups scores better under the English letter model (-1.875 per letter) than the reading (-2.098), so the test can neither confirm nor refute a word-level dictionary code. The book identification rests on the frozen No. 4 page test and the edition row score above, not on this test.

Our own AI agent acting as coordinator reviewed the complete prose and decryption tables for Nos. 1 and 4 with LAC source-page inspection: No. 1 grade B (its first source/account/council clause remains raw), No. 4 grade A, both only read in part. This review checks prose/table consistency; it is not fresh validation of every Entick row, human verification, or outside-project independent verification. The separate two-reader numeral/headword check applies to 218-11. On 13 November, after an independent check by another of our AI agents suggested it, a further AI agent of ours reread No. 2 and agreed that its first half is a coherent description of a man (thirty years old, five feet two, freckled, light or sandy hair, of New Haven, a spy and rebel, name unknown); No. 2 is now read in part with a grade B reading review that covers the first half only (the repository allows only A or B on a reading), and the words after "slipped through" and around York, trade and hemp remain unconnected. No. 3 receives no reading review and is not counted as a coherent reading.

## Who read what, and when

Sherwood enclosed a sketch with his 2 March 1783 letter to Mathews, saying the cipher was badly written with frequent page-number mistakes. He understood most of No. 1 but not its thunder-damage clause, identified No. 2 as an advertisement without understanding it, summarised parts of No. 3, and read almost all No. 4. The sketch is commonly dated 16 February in the calendar, but that date belongs to the quoted No. 4; composition around 1–2 March is an inference from the covering letter. The copy's interlinear look-ups may be Sherwood's, but the copyist's hand cannot establish their original authorship.

The 1888 calendar lists and summarises the documents without giving a full decipherment. The 12 November research searched the calendar, Wilbur's *Ira Allen*, the Vermont Historical Society collections and Waite's *History of Claremont* without finding a later reading. Checked on 12–13 November, with no reading of these messages and no identification of Entick found:

- Ian C. B. Pemberton, *Justus Sherwood, Vermont Loyalist, 1747–1798* (PhD thesis, University of Western Ontario, September 1972; repository date 1973): all 373 pages screened by OCR for cipher, code, dictionary, Entick, Hoyt, Cossit and Sumner, with the relevant passages and the bibliography read.
- Pemberton, "The British Secret Service in the Champlain Valley During the Haldimand Negotiations, 1780–1783", *Vermont History* 44 (1976), pp. 129–140: full text read.
- Both instalments of "Sherwood's Journal", *Vermont History* 24 (April and July 1956): full text read; they cover 1780–81.
- Mathews to Sherwood, 9 January 1783 (LAC transcript B.179-2 pp. 162–169): read on the images; it approves the private correspondence but names no book or rule.

Searched on 15 November (see "Follow-up on the PR #575 notes" below), with no reading of these messages and no identification of Entick found: Mary Beacock Fryer's *King's Men* (1980) and *Buckskin Pimpernel* (1981) and H. M. Jackson's *Justus Sherwood* (1958), by full-text search of the Internet Archive lending copies; Ryan L. Wagner's 2026 thesis, whole text searched. These were searches of a text layer, not page-by-page readings; the intended Hoyt citation is still unresolved. **Novelty is therefore not proven.** See [the follow-up](PRIOR_ART_2026-11-12.md). The contribution is the documented identification/testing of the dictionary setting, full transcriptions and transparent partial decodes, including portions Sherwood could not understand.

## Integration check (14 Nov 2026)

Verified from the files by the integrating reader (an AI reader, not a person) when PR #575 was merged.

- Reproduced: `verify.py` passes (56, 32, 81 and 47 code groups, 216 in all; the frozen No. 4 totals 8 against 1, 1, 0, 3, 1, 2; edition rows 96 of 107; gloss test 3 of 9; 218-11 present, 216-11 absent). `docs/_check_profile.py haldimand1783`: valid; `docs/_check_terms.py haldimand1783`: 0 hits. A second script, written from `key.tsv` and the `code_groups_no*.txt` files without the contributor's code, finds every one of the 216 groups in the key table in the order of `lookup_occurrences.tsv`, 169 distinct pairs, 169 occurrences with a direct headword (grade H), 39 inferred and 8 unresolved.
- Images. Canadiana reel H-1737 frame 15 (copy p. 345; file hash as in `evidence/image_sources.tsv`): all 47 groups of No. 4 compared with `transcription_no4.txt`, no disagreement. Frame 16 (p. 346): the ten lines of No. 3 on that page (f346.22-31, about 45 groups), no disagreement; 218=11 and 262-36 were looked at enlarged and are as transcribed, as far as the copyist's 8 and 6 can be told apart. Entick 1781 (Internet Archive 11280377bsb): p. 218 left column row 11 is Magnanimous and p. 220 right column row 30 is March v. with the continuation line counted, as the key says. Not compared: Nos. 1 and 2, the p. 347 continuation, and the other Entick rows.
- The tests, in plain words. The No. 4 page test passed its frozen rule (8 hits, bar 8, controls at most 3), narrowly: the hit *Say* is the text recognition placing a second lemma on p. 315, where *Saturday* already scores, so seven different cipher pages are hit. The edition comparison passed (54 of 79 against 21 for the next printing; 96 of 107 rows). **The gloss test failed** (3 of 9 exact against a bar of 4 of 5). The order of freezing and scoring is by the contributor's record. The statistical validation is underdetermined, as stated. What carries the book identification is the row-level fit (169 of 216 groups land on a fitting headword of this setting) and the two rows checked above.
- Strict read share. The profile figures (0.645, 0.778, 0.638, 0.702) are the repository's explicit-hole measure on the readings and are kept. Counted word by word by the integrating reader, with every word that carries a bracket (supplied ending, supplied word, guessed word, hole) as a hole: No. 1 40 of 63 (63.5%), No. 2 25 of 36 (69.4%), No. 3 59 of 93 (63.4%), No. 4 39 of 58 (67.2%). The classes do not change: Nos. 1, 2 and 4 read in part, No. 3 decoded, not read. The readings of Nos. 1 and 4 lean on Sherwood's 1783 sketch, as the notes say.
- `outcome.codes_open` filled: 8 of 169 distinct pairs have no value (8 occurrences).
- Duplicates: no other target, catalogue entry or lead holds these messages, and no other target uses an Entick dictionary. `targets/carleton1782` (PR #579) is the headquarters cipher of the same governor, a different system.
- Why no page yet: the contributor has ordered images of the originals and will check every number against them (a submission its author will refresh is held), the print step is open, and Nos. 1 and 2 and the p. 347 continuation have had no outside image check.

## Remaining gaps

- No. 1 repairs/source/logistics clauses and No. 2 415, 153-7, 237-31/sentence connections — blocker: needs-physical-access; dictionary and copy checked, original numeral images ordered to distinguish copying and encoder errors.
- No. 3 middle (262-36, 6-26 and sign, 272-8, 90-28, 303-22, 417-9, 224-4, 402-25), continuation 203-19 and plain words — blocker: needs-physical-access; bounded image/dictionary retry unsuccessful except corrected 218-11; originals ordered.
- No. 4 23-4-1 and 33-35 — blocker: needs-physical-access; copied figures do not yield Sherwood's closing clause; two holes retained.
- Prior art: the intended Hoyt citation, and a page-by-page reading of Fryer 1981 pp. 176-182 (the Cossitt and Sumner visit) — blocker: needs-physical-access; Fryer 1980 and 1981, Jackson 1958 and Wagner 2026 were text-searched on 15 Nov 2026 (no mention of the cipher, a code book or Entick), but the lending copies were not read page by page and the Hoyt citation is unresolved. Pemberton thesis and 1976 article, the 1956 journal instalments and the 9 January 1783 letter were checked (nothing found). Novelty not proven; the print step below stays unticked.
- Original authorship of glosses and comparison of original figures with the LAC copy — blocker: needs-physical-access; original images ordered. Coordinator AI prose reviews cover Nos. 1 and 4; no human_check or new inspection of every dictionary row is claimed.

## Escalation

- [x] clear-pages: Sherwood sketch and covering letter used and distinguished from a verbatim decipherment; nearby clear intelligence consulted for context.
- [x] siblings: research pass swept B.178 copy pp. 336–509 visually and additional B.177–178 material at thumbnail scale; no additional page of dictionary-code groups found; this was not an exhaustive archive sweep.
- [x] known-keys: Entick 1781 setting tested; formal gloss result left open; no surviving instructional key tied securely to these pairs.
- [ ] print: calendar, Pemberton's thesis and 1976 article, and the 1956 Sherwood journal checked; Fryer's two books, Jackson 1958 and Wagner 2026 text-searched on 15 Nov 2026 (nothing on the cipher); the intended Hoyt citation remains unchecked.
- [x] key-rebuild: occurrence table includes both-column evidence, proposed readings and every repair; incomplete semantic recovery recorded.
- [x] retry: specified weak pairs inspected on copy/dictionary images with neighbouring rows and selected digit swaps; 218-11 corrected, other weak places remain.

The source frames used here are later copies. Andrew ordered British Library images of the originals on 12 November 2026: Add MS 21838 folios 306 recto and verso, 307 recto and verso, 324 verso and 379 recto. None has arrived (15 November 2026). They are not online: the British Library's catalogue (searcharchives.bl.uk, record 040-002034298) marks Add MS 21838 as not digitised. When they do, every copied number will be checked against them and the readings revised; the first four folios hold the messages. Generated website and catalogue files are left for the repository's contribution workflow.

## Follow-up on the PR #575 notes (15 Nov 2026, Andrew Beling, with AI agents)

Searched by an AI agent (Claude); no person has read these books for this note. Nothing below changes a reading, a
number, a share or a class.

- **British Library images.** Not online. The catalogue (https://searcharchives.bl.uk, record `040-002034298`, Add MS
  21838, "Vol. III" of the Sherwood and Smyth letters, 1783-1784) gives "Digitised Content: No" for Add MS 21836-21838;
  the old Digitised Manuscripts address for Add MS 21838 now redirects to a general page. Its item list names Ranna
  Cossit to Sherwood, Grand Isle, 1 January 1783 (f. 2) and "B. Sumner; Jan. 1781 (?), f. 312" (letters to Sherwood and
  S. Holland), but no item at ff. 306-307. The images ordered on 12 Nov 2026 have not arrived; no delivery message was
  found on 15 Nov.
- **Fryer, *Buckskin Pimpernel* (1981)**, Internet Archive `buckskinpimperne0000frye` (lending copy), full-text search for
  cipher, cypher, code, dictionary, Entick, Cossit, Cossitt, Sumner, Hoyt, numbers, Claremont, Dartmouth. No hit for
  cipher (spelled so), Entick, dictionary (only Grose's slang dictionary in the bibliography) or Hoyt. "Cypher" occurs
  twice, for other papers: an extract of Haldimand to Clinton of 28 February 1781 "originally in cypher" (p. 132) and a
  message in cypher found on the courier Joseph Bettys in 1782 (p. 166). "Code" occurs only as "code name" of agents
  (Hudibras, Plain Truth). Pp. 176-182 tell of Cossitt and Sumner's visit to Sherwood on 30 December 1782 and of a later
  letter from Cossitt about Sherwood's son and Dartmouth College; the snippets give no numbered messages. Note 26 of that
  chapter cites "PAC Haldimand Papers B 175 pp. 185-186, Cossitt and Sumner to Haldimand, Dec. 30, 1782". In her notes
  on sources (p. 263) Fryer says she cited both the British Museum originals and the Public Archives of Canada B series.
- **Fryer, *King's Men* (1980)**, `kingsmensoldierf0000frye`, same terms: "cypher" once (a royal cypher on a uniform
  plate), "code" only as agents' code names, no hit for Entick, Cossitt, Sumner or Hoyt.
- **Jackson, *Justus Sherwood: Soldier, Loyalist and Negotiator* (1958)**, `justussherwoodso0000ltco`: no hit for cipher,
  cypher, code, dictionary or Entick. P. 58 has the December 1782 visit of Cossitt and Sumner (notes 73-74, B.175 pp.
  185-186).
- **Wagner, *The Security and Defense of This Province* (Liberty University PhD, February 2026)**, opened in Chrome
  from https://digitalcommons.liberty.edu/doctoral/7941/ (the PDF that curl had refused with 403), 262 pages, text layer
  searched: no hit for cipher, cypher, decipher, Entick, Cossit, Sumner, Hoyt or Add MS 21838; "code" only in general
  remarks on codes and invisible ink (pp. 228, 231, 238); Sherwood on ten pages. Wagner cites many Haldimand volumes by
  Add MS number, without image links.
- **What this changes.** The "not checked" literature is now searched, and none of it reads or identifies this code;
  the claim stays "novelty not proven" because these were text searches of lending copies, not readings, and the Hoyt
  citation is unresolved. The print step stays unticked.
- **A mistake in the search.** A first script asked the Internet Archive's search service for the three lending copies
  thirty times in a row and got 403 each time; it should have stopped at the first. The searches above were then made
  one at a time from the ordinary book pages in Chrome.
