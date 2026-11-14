# Cossit–Sumner correspondence to Sherwood: Entick dictionary code, 1783

Status: in progress — partial reading; the copied numbers are to be checked against British Library images of the originals (on order), and part of the modern literature is still unchecked.

Andrew Beling, with his own AI agents, 12–13 November 2026. **Read after matching with key from external sources, in part:** Nos. 1 and 4 are read in part. Nos. 2 and 3 are **decoded, not read**. This is not a first decipherment: Justus Sherwood himself read much of this in 1783 (most of Nos. 1 and 4 and some of No. 3), and his sketch was used as a crib from the outset. The credit for those readings is his.

## Documents and context

Four numbered messages from the Cossit–Sumner intelligence correspondence survive in British Library Add MS 21838, ff. 306r–307v. The witness used here is the **1880s Library and Archives Canada hand copy**, B.178 pp. 345–347, on Canadiana reel H-1737 frames 15–17. Earlier research confused copy page numbers 345–347 with British Library folios; the package corrects this. Stable transcription labels `f345/f346/f347` identify copy pages only. [Source links and witness table](SOURCES.md).

No. 4 is dated 16 February 1783, addressed C.S.L.B.H. (probably Captain Sherwood, Loyal Blockhouse), and endorsed from Mr Sum--r. Nos. 1–3 share the next sheet; individual authorship is not established. A passage after the word “three” on the reverse has been treated as the end of No. 3 because its letters left at St Johns and closing to Holland match the end of Sherwood's No. 3 sketch. Its date is 11 February 1783. This joining is an inference, not a separate fifth message proved by numbering.

Ranna Cossit and Benjamin Sumner were Loyalists associated with Claremont, New Hampshire. The letters belong to the Vermont negotiations/intelligence network around Haldimand, Sherwood and Smyth. No. 4 reports a march toward Oswego, feared instead to be directed against Vermont. Sherwood's separate 19 February report and “Plain Truth” of 2 March identify the contemporary expedition as Willett's; that contextual identification is not a codeword recovered here. Colonel Strong is likely John Strong of Dorset, but the cipher itself supplies only Strong. Holland's forename and the man described in No. 2 are not established by these messages.

Related but separate: Haldimand's headquarters also corresponded with Sir Henry Clinton in a line-column cipher. Brice Dudout's pointer in issue #359 (9 November 2026) covers Clinton to Haldimand, 22 October 1779 (British Library Add MS 21807, LAC transcript B.147), with its contemporary clear; the project recorded it on lead 1137. That is a different system from the Entick dictionary code and is not part of this folder.

## System and how the book was found

A group gives **printed page and printed line down either unmarked column** of John Entick's *New Spelling Dictionary*, London 1781, scanned as Internet Archive 11280377bsb. Continuation lines count. The market-town appendix supplies place names. Dictionary headwords can represent inflections, fragments or sound-alikes. See [KEY.md](KEY.md) and [key.tsv](key.tsv). No silent digit corrections or column choices have been passed off as a deterministic key.

Sherwood's sketch suggested member, new, the and related words; these fitted Entick pages. The pre-registered No. 4 test then compared a frozen lemma list from Sherwood's sketch with cipher page numbers. It scored 8; six shifted-page controls scored 1, 1, 0, 3, 1, 2, meeting the recorded rule. A packaging rerun on the original input files reproduced this exactly, and the frozen transcription hashes matched. This supports the book identification. It is **not** a blind recovery of the message, and it validates neither every numeral nor every proposed word. The OCR drops 17 of 30 lemmas and sometimes chooses an irrelevant first headword occurrence; the modest page-match test is reported as run, without improving it after the result.

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
| No. 2 |32|77.8%|decoded, not read|
| No. 3 plus probable continuation |81|63.8%|decoded, not read|
| No. 4 |47|70.2%|read in part|

The profile also records 169/216 (78.24%) direct dictionary-supported code groups, excluding all conjectural repairs; this is key-lookup coverage, not a sentence-reading claim.

There are 216 code groups under the declared counting rule. Counts use the repository's `_check_profile.py --measure` on normalised group-only files, excluding literal figures/words, cancelled figures and the dangling sign, but including the encoded month and each malformed written group as one unit. These files are measurement derivatives, not substitutes for the diplomatic transcription.

Strict reading shares are the repository `v2_score.py` explicit-hole measure over each `## Reading` body, including plain text; supplied endings and uncertain replacements count as holes. Earlier research figures that counted dictionary evidence rather than readable prose are superseded and not used. For comparison, direct dictionary/plain evidence covers 47/61 items in No. 1, 27/34 in No. 2, 63/86 in No. 3 combined after the correction and extra sign, and 38/50 in No. 4. Those counts include dates/plain text and do not test sentence sense. `measurements.json` and `verify.py` reproduce the package's actual measurements. A high token score does not turn No. 2 or No. 3 into readable prose.

The statistical validation (`docs/_validate.py`, pairs in `validation.tsv`, 13 November) is **underdetermined**: with about 1.3 occurrences per code group, a key fitted to shuffled groups scores better under the English letter model (-1.875 per letter) than the reading (-2.098), so the test can neither confirm nor refute a word-level dictionary code. The book identification rests on the frozen No. 4 page test and the edition row score above, not on this test.

Our own AI agent acting as coordinator reviewed the complete prose and decryption tables for Nos. 1 and 4 with LAC source-page inspection: No. 1 grade B (its first source/account/council clause remains raw), No. 4 grade A, both only read in part. This review checks prose/table consistency; it is not fresh validation of every Entick row, human verification, or outside-project independent verification. The separate two-reader numeral/headword check applies to 218-11. Nos. 2 and 3 receive no reading review and are not counted as coherent readings.

## Who read what, and when

Sherwood enclosed a sketch with his 2 March 1783 letter to Mathews, saying the cipher was badly written with frequent page-number mistakes. He understood most of No. 1 but not its thunder-damage clause, identified No. 2 as an advertisement without understanding it, summarised parts of No. 3, and read almost all No. 4. The sketch is commonly dated 16 February in the calendar, but that date belongs to the quoted No. 4; composition around 1–2 March is an inference from the covering letter. The copy's interlinear look-ups may be Sherwood's, but the copyist's hand cannot establish their original authorship.

The 1888 calendar lists and summarises the documents without giving a full decipherment. The 12 November research searched the calendar, Wilbur's *Ira Allen*, the Vermont Historical Society collections and Waite's *History of Claremont* without finding a later reading. Checked on 12–13 November, with no reading of these messages and no identification of Entick found:

- Ian C. B. Pemberton, *Justus Sherwood, Vermont Loyalist, 1747–1798* (PhD thesis, University of Western Ontario, September 1972; repository date 1973): all 373 pages screened by OCR for cipher, code, dictionary, Entick, Hoyt, Cossit and Sumner, with the relevant passages and the bibliography read.
- Pemberton, "The British Secret Service in the Champlain Valley During the Haldimand Negotiations, 1780–1783", *Vermont History* 44 (1976), pp. 129–140: full text read.
- Both instalments of "Sherwood's Journal", *Vermont History* 24 (April and July 1956): full text read; they cover 1780–81.
- Mathews to Sherwood, 9 January 1783 (LAC transcript B.179-2 pp. 162–169): read on the images; it approves the private correspondence but names no book or rule.

Not checked: Mary Beacock Fryer's *King's Men* (1980) and *Buckskin Pimpernel* (1981) were located in catalogues and libraries, but the relevant pages were not accessible; the intended Hoyt citation is unresolved; H. M. Jackson's 1958 Sherwood study was not seen; Ryan L. Wagner's 2026 thesis on Haldimand's intelligence operations was inaccessible (403). **Novelty is therefore not proven.** See [the follow-up](PRIOR_ART_2026-11-12.md). The contribution is the documented identification/testing of the dictionary setting, full transcriptions and transparent partial decodes, including portions Sherwood could not understand.

## Remaining gaps

- No. 1 repairs/source/logistics clauses and No. 2 415, 153-7, 237-31/sentence connections — blocker: needs-physical-access; dictionary and copy checked, original numeral images ordered to distinguish copying and encoder errors.
- No. 3 middle (262-36, 6-26 and sign, 272-8, 90-28, 303-22, 417-9, 224-4, 402-25), continuation 203-19 and plain words — blocker: needs-physical-access; bounded image/dictionary retry unsuccessful except corrected 218-11; originals ordered.
- No. 4 23-4-1 and 33-35 — blocker: needs-physical-access; copied figures do not yield Sherwood's closing clause; two holes retained.
- Prior art in Fryer 1980 and 1981, Jackson 1958 and Wagner 2026, and the intended Hoyt citation — blocker: needs-physical-access; Fryer located but relevant pages not accessible online, Jackson unseen, Wagner returned 403, Hoyt citation unresolved. Pemberton thesis and 1976 article, the 1956 journal instalments and the 9 January 1783 letter were checked (nothing found). Novelty not proven; the print step below stays unticked.
- Original authorship of glosses and comparison of original figures with the LAC copy — blocker: needs-physical-access; original images ordered. Coordinator AI prose reviews cover Nos. 1 and 4; no human_check or new inspection of every dictionary row is claimed.

## Escalation

- [x] clear-pages: Sherwood sketch and covering letter used and distinguished from a verbatim decipherment; nearby clear intelligence consulted for context.
- [x] siblings: research pass swept B.178 copy pp. 336–509 visually and additional B.177–178 material at thumbnail scale; no additional page of dictionary-code groups found; this was not an exhaustive archive sweep.
- [x] known-keys: Entick 1781 setting tested; formal gloss result left open; no surviving instructional key tied securely to these pairs.
- [ ] print: calendar, Pemberton's thesis and 1976 article, and the 1956 Sherwood journal checked; Fryer's two books, Jackson 1958, Wagner 2026 and the intended Hoyt citation remain unchecked.
- [x] key-rebuild: occurrence table includes both-column evidence, proposed readings and every repair; incomplete semantic recovery recorded.
- [x] retry: specified weak pairs inspected on copy/dictionary images with neighbouring rows and selected digit swaps; 218-11 corrected, other weak places remain.

The source frames used here are later copies. Andrew ordered British Library images of the originals on 12 November 2026: Add MS 21838 folios 306 recto and verso, 307 recto and verso, 324 verso and 379 recto. None has arrived. When they do, every copied number will be checked against them and the readings revised; the first four folios hold the messages. Generated website and catalogue files are left for the repository's contribution workflow.
