# Walsingham → Edward Wotton, 28 Jul – 10 Sep 1585 — BL Add MS 32657, DECODE R4838, R4839, R4840, R4844

Catalogue entry 82 ("Sir Francis Walsingham … to Edward Wotton, ambassador to Scotland, 4 ciphertexts", Tomokiyo
list, rule-scored). Worked 2026-09-21. **Outcome: read in part.** All four letters transcribed; R4844 is decoded, not read (reading audit, 22 Oct 2026). The name code is mostly
identified. About fourteen words in a sign alphabet in the 10 Sep letter stay unread.

Status: read in part (2026-09-21).

22 Oct 2026, reading audit (George Lasry's test: can sentences be built and translated?): R4840 (21 Aug) reads as
English sentences with its name codes glossed. **R4844 (10 Sep) is decoded, not read**: the unread sign-alphabet
words and open codes fall in nearly every sentence. Reading figure 0.43 (units in letters that read); the pooled 0.49
is withdrawn as a reading figure.

22 Oct 2026, re-read (REREAD_BRIEF, batch mix1, Claude Opus 5.5): R4844 checked again for an existing text (none:
Wotton's interlinear decipherment blotted, not in CSP Scotland viii, DECODE non-decrypted). The DECODE images are
behind the login and not in the checkout, so nothing new could be read on the page. The 14 Oct gap readings of
`clear_gaps_pass2.md` were merged into `reading_R4844_r2.txt` (sentence check 0.45 -> 0.50), but the sign words and
open name codes still fall in nearly every sentence: R4844 stays decoded, not read (`texts/R4844_reread_log.md`).

Companion to [wotton1585](../wotton1585/NOTES.md), Wotton's own drafts to
Walsingham in the same volume (R4841–R4843, catalogue 81), read by another session the same day.

Two ciphers, two results (one-key review, 14 Oct 2026): the two-digit name code of all four letters and the sign
alphabet of the 10 Sep letter are different systems, so the profile gives the outcome per part in `outcome.parts`
and README has one row per part, as soria1523 does. Name code: key recovered from the CSP glosses (external
plaintext), 34 of 46 occurrences read (12 of 18 numbers). Sign alphabet: not solved, too short. The pooled 0.49
(34 of 69 units) mixes the two and is kept only as a labelled total.

## 1. What the records are

Wotton's own papers from his 1585 embassy to James VI (Add MS 32657, "Hamilton papers" series of the BL). DECODE
(owner 22, 2023) lists each letter as "unknown; alphabet, graphic signs, numerical; Non-decrypted". The images were
fetched with the saved DECODE cookie (`targets/bordeaux/decode/cookie.txt`). They are BL images, not public domain, so
they stay git-ignored in `img/`.

| DECODE | ff. | date | place | what is in cipher |
|---|---|---|---|---|
| R4838 | 125–127 | 28 Jul 1585 | Nonsuch | nothing but name numbers (on f. 126, a slip: 13, 19, 37) |
| R4839 | 140–141 | 7 Aug 1585 | the Court | name numbers only (10, 19, 24, 28, 29, 30) |
| R4840 | 163–164 | 21 Aug 1585 | the Court | name numbers only (10, 11, 20, 27, 28, 29, 36, 39, 40) |
| R4844 | 194–195 | 10 Sep 1585 | the Court | name numbers **and ~14 words in a sign alphabet** |

The letters are in Walsingham's secretary's hand and signed by him, in plain English. The "cipher" is (a) a small
two-digit code for persons and countries, written in the line, and (b) in R4844 alone, a few words spelled in
signs (□, ⊿, =, ≠, ÷, f, ω, R, k, 4, dots and dashes). Wotton's reply drafts in the same volume (R4841, R4842,
R4843: 25 Aug, 30 Aug, 1 Sep) use the same numbers and are otherwise clear.

## 2. Prior art

- **CSP Scotland viii** (W. K. Boyd, 1914) calendars the 28 Jul letter as no. 40 and the 7 Aug letter as no. 65,
  from Walsingham's drafts and copies in the State Papers, which name the persons in clear. The 21 Aug and 10 Sep
  letters are **not calendared**: no Walsingham→Wotton entry for those dates. Checked page by page in the HathiTrust
  text (miun.abe1726.0008.001, seq. 20–230). BHO has the volume behind its paywall.
- The calendar glosses the numbers in Wotton's letters: Arran ["19"], the Master of Gray ["39"], Justice Clerk
  ["40"], Farnyhurst ["24"] (nos. 41 and later). No. 106 (Wotton, 1 Sep) calendars R4843's draft with "Morton" for 20.
- No key on DECODE (no key record mentions Wotton), none in Tomokiyo's *Ciphers during the Reign of Queen
  Elizabeth I* (his Wotton cipher is Nicholas Wotton's of 1548).

## 3. The name code

| no. | reading | grade | ground |
|---|---|---|---|
| 3 | France (or the French side) | M | R4841 draft: "divert him from 3 … convey him into Fr." |
| 10 | the King (James VI) | H | CSP 106 ("the King") for R4843's 10; sense in every letter |
| 11 | the French faction / party | C | "the party of 11 increaseth"; "the 11 course"; "devoted unto 11" |
| 13, 14 | persons at the Scottish court, not identified | I | "the meeting of 13 and 14"; "13 is affected to 19" |
| 19 | Earl of Arran | H | CSP 41 ["19"], 7 Aug letter (CSP 65) |
| 20 | John Lord Maxwell, styled Earl of Morton | H | CSP 106 "Morton" for R4843's 20 |
| 23 | not identified (a go-between with the Jesuits) | I | "23 is the principal dealer in 37 between 10 and the Jesuits" |
| 24 | Farnihurst (Sir Thomas Kerr) | H | CSP ["24"] |
| 27 | a councillor (the Secretary, Maitland?) | M | coupled with 40; "was greatly here", "no earnest friend to the Hamiltons" |
| 28, 29 | the banished lords (Angus and Mar?) | M | "yf 28 and 29 would come down to the Borders to join with 20" |
| 30 | not identified | I | |
| 32 | a place (Stirling or Dumbarton?) | I | "convey himself into 32" (R4843) |
| 36 | England / the Queen's side | M | "money out of 36", "10 carried away from 36" |
| 37 | not identified (a place?) | I | "at my being in 37"; "23 is the principal dealer in 37" |
| 39 | Master of Gray | H | CSP ["39"] |
| 40 | Justice Clerk (Sir Lewis Bellenden) | H | CSP ["40"] |

## 4. The sign words in R4844 (10 Sep 1585), unread

Each sign word has one line above it, heavily blotted: Wotton's interlinear decipherment, struck out on purpose.
Nothing of it can be read on the scan. Sign words as far as they can be copied (dots and dashes kept; `ω` a looped
w, `⊿` a triangle, `4` a crossed four):

1. f.194 l.3 "of the **□⊿=≠|–.⊥.f** set down by 39 than before" (the articles of the league?)
2. l.10 "will be **≠f–.÷≠f=** … as also 30 who is of best **ßkIω#fll–** … continent them"
3. l.14 "neither be **–.–==|÷–.□4** nor otherwise make **□4διωf÷ □δι÷f≠ω** a partie"
4. l.24 "that I would not … of any **□54Rhl≠dll–. □o ζlm÷–d** these great disorders"
5. f.194v l.3 "so as you shall be **⊿ϱ÷fll ⊿app⊿** at the **c–.–d#÷–**"
6. l.5 "ward your **(a)–.÷cr lld⊿4ꝙ** at **□⊿≠ ÷–.f÷≠gllω** & avoyde **–k÷.÷–…bll**"
7. postscript "a letter … from the **≠l÷.of ÷ψ÷lm=≠l**", "touching **Rh÷f ψ÷dc–. =≠l–**", "not carried with
   that **⊿4÷dψ–fcψτd**".

The words are short, homophones are likely (`□`, `⊿` and `≠` recur at word starts), and dots and dashes look like
nulls. About 120 signs in all, with no crib and no other text under the same alphabet, which is too little to
break. It would move with Wotton's cipher key (not found), or a decipherment of another letter in this alphabet
in SP 52/38.

## 5. Readings

`reading_R4840.txt` and `reading_R4844.txt` are working transcriptions of the two letters that are not in print,
with numbers glossed. R4838 and R4839 are left to CSP nos. 40 and 65, checked against the images (they match).

## 6. Steps

1. DECODE metadata via API; images fetched with the cookie (18 images).
2. Viewed all pages. The letters are clear English with a name code, not cipher letters; only R4844 has sign words.
3. CSP Scotland viii via the HathiTrust text-only view: nos. 40, 65 found; 21 Aug, 10 Sep absent.
4. Name code from the CSP glosses and Wotton's drafts R4841–R4843.
5. Sign words: looked for a key (DECODE, Tomokiyo) and for cribs (Wotton's drafts carry no sign text). Too little
   text to break without either. Closed unread.

**23 Oct 2026, v6 spelling check (research/reading_audit/v6_spelling_files.txt; REREAD_BRIEF step 3-4: no modern spelling in a reading)**: reading_R4840.txt and reading_R4844_r2.txt said 'spelling modernised (in part)'. There is no diplomatic transcription, so the DECODE images were fetched again with the project cookie (research/reading_audit/v6_fetch.py; scratchpad only, BL images) and re-read in strips; the words whose letters are clear in the secretary hand are now as written (dothe, complayne, wrytten, frende, knowe, countenaunce, towardes, yf, woold, ioyne, wyll, realme, iudge, therof, alwayes, then for than, Coorte; hathe bread, lykinge, doe bothe allowe of yt, untill, ben unmindfull, commyssion, Jesuites ...). Words not certain on the scan keep the earlier form, which the headers say; no hole was filled and no word changed. The R4840 marginal postscript (f. 163v) was not re-read. Explicit holes R4840 0.614 -> 0.667, R4844_r2 0.705 -> 0.736 (new header lines; no '## Reading' heading). States unchanged: R4840 read, R4844 decoded, not read.

## Read share over cipher words only (16 Nov 2026)

README Conventions now count the read share over the words written in cipher, holes by words, sure words only (probable
and grade-M words are holes; a word confirmed by an independent contemporary text is sure). The letters are clear
English; the cipher words are the two-digit name codes written in the line, and in R4844 the sign words. Recounted by
hand; the files do not mark them, so `v10_relabel.py` cannot reproduce these counts.

- **R4840** (21 Aug): 20 code occurrences, **15 sure**: 39, 40, 10, 24 (twice each), 20 and 19 on the calendar's glosses
  (grade H), and 27 (twice), 36 (twice) and 3 on the contemporary glosses of the deciphered pairs
  (`dudout/name_codes.md`: "the Secret[ary]", "Eng.", "the Q."), which are independent of this reading; **5 holes**:
  11 three times (grade C; its gloss in the pairs, "S. Fr.?", is uncertain), 28 and 29 (grade M, no gloss).
  **15 of 20 = 0.75**, from 0.957 (a figure over the whole letter, clear included, taken from `clear_gaps_pass2.md`).
  On the `texts/key.md` grades alone, without the pairs' glosses, it is 10 of 20 = 0.50. **State read -> read in part.**
  The clear words and their `[..]` gaps are not cipher and are not counted.
- **R4844 sign words** (Dudout; updated 20 Nov 2026 after sheets K and K2 and the review of #821, see Review of #821: 12 groups S, 4 P, 3 unresolved, **12 of 19 = 0.632**; sheet K alone 13 of 19, sheet K2 14 of 19). Count of 16 Nov 2026: 19 sign groups, **11 graded S (certain)**, 5 graded P (probable, one with a restored
  letter; holes) and 3 unresolved: **11 of 19 = 0.579**, from 0.86, which counted the sign letters with the probable
  and restored ones as read (certain letters about 69 of 116 = 0.59). Stays read in part. The reading file
  `dudout/reading_R4844_signs.md` is Dudout's and still carries its own 86% line.
- **R4844** (the whole letter) stays decoded, not read; **R4838, R4839** are in print as calendar abstracts and have no
  entry here.
- **Outcome fraction_read** 0.43 -> **0.36** (25 of 69 units: R4840 15, R4838/R4839 10 as before, R4844 none, as
  before); the 0.43 counted R4840's 20 whole. The 10 units of R4838/R4839 were not recounted.
- The class stays **read in part**; the part counts "34 of 46 name-code occurrences" and "12 of 18 numbers identified"
  count identified numbers, not sure occurrences, and are not recounted here.

## Remaining gaps
- R4844 as a whole decoded, not read (sign words or open codes in nearly every sentence; reading audit 22 Oct 2026) - blocker: too-short; see the sign-words and name-code lines below
- R4844 sign words (19 groups, ~120 signs) - blocker: too-short; homophonic sign alphabet, interlinear decipherment blotted out. A partial sign key now exists (`dudout/sign_key.tsv`, learnt on the glossed sign words of R4689, R4835, R4836; 0.646 vs 0.213 on held-out R4845), and two blind sign sheets (K, K2) were run: 12 of 19 groups certain, 4 probable, 3 unresolved (20 Nov 2026). Open: groups 2, 4, 10; the fifth sign of group 14; MP and ψ in group 16
- name codes 13, 14, 23, 30, 32, 37 - blocker: no-key-material; not glossed in CSP or Wotton drafts; context too thin
- clear-text gaps [..] in reading_R4840/R4844 - blocker: illegible; second pass 14 Oct 2026 on the DECODE images (`clear_gaps_pass2.md`): of 46 places, 32 read H/C, 8 M, 6 illegible (blots, stains, struck interlinear words); merged for R4844 into `reading_R4844_r2.txt` on 22 Oct 2026 (R4840's nine corrections still to merge into reading_R4840.txt)

## Escalation
- [x] siblings: Wotton drafts R4841-R4843 in the same volume read for numbers and cribs
- [x] clear-pages: interlinear lines above the sign words examined; struck out, unreadable
- [x] known-keys: DECODE key records and Tomokiyo Elizabethan ciphers searched; no Wotton 1585 key
- [x] print: CSP Scotland viii checked page by page (nos. 40, 65, 106)
- [n/a] key-rebuild: the name code is a list of names with no internal order to bracket, and its open numbers occur once or twice in thin context; the sign alphabet is ~120 homophonic signs with nulls and no crib, below what an anneal can fix (a crib from SP 52/38 copies would be needed first)
- [x] retry: clear-text gaps re-read on the images 14 Oct 2026 (`clear_gaps_pass2.md`); name-code grades unchanged (the new words fix no open number)
- [x] retry (22 Oct 2026): R4844 re-read under the reread brief; pass-2 readings merged (`reading_R4844_r2.txt`); images out of reach (DECODE login); sign words and open codes unchanged (`texts/R4844_reread_log.md`)
- [x] retry (19-20 Nov 2026): blind sign sheets K (10 signs) and K2 (3 signs) on the R4844 sign words, controls 2 of 2 on each, `dudout/sign_key.tsv` unchanged; sure groups 11 -> 13 -> 14 of 19, then 12 of 19 = 0.632 after the review of #821 (K and K2 disagree on group 14; group 16 rests on MP and ψ, not settled); read in part

## 2026-09-30 (quotation list for George Lasry)

- R4840 f. 163 ll. 4-9 re-read on the DECODE image (IMG_R4840_I28147_P1, fetched again with the cookie, 3-4x crops).
  The cut after "towards him" now reads: "with the [courage] to procure the practice of 27 and 40, which as he
  professeth doth greatly [abuse] you, being altogether bent to [ruin] 11 course; and for himself he voweth to be
  altogether at 3 devotion". Bracketed words are grade M (secretary hand: "couradge" with a crossed stroke; "abuse"
  runs into the gutter; "ruine" four or five minims). The old transcription's "overthrow 11" was wrong: the
  manuscript has a short word and "course" after 11. Wotton's reply of 30 Aug (R4842 f. 173) supports it: "I could
  never perceive cause to suspect them [27 and 40] in the 11 course". "at the devotion [..]" was "at 3 devotion":
  3 here is Gray's object of devotion, the Queen or England (M); Wotton's R4841 has both "divert him from 3" and
  "convey him towards 3 ... into Fr.", so the NOTES table's "France" for 3 is not settled either way.
- 28, 29, 36: CSP Scotland viii could not be rechecked (HathiTrust ssd view now behind a Cloudflare bot check;
  archive.org `calendarofstatep0008vari` lending-only, full-text search refused; the Google Books API is over quota).
  Wotton's R4842 pp. 1-2 were read for them: no use of 28, 29 or 36. They stay grade M.
- Quotation for the list: the continuous opening of R4840 ("Sir, 39 doth complain … bent to [ruin] 11 course"), with
  the numbers glossed.

## 2026-10-23: lead from the profile mining

Lead from research/patterns/DEEPER.md: Stafford's Walsingham cipher of 1586 (harley1582r8500/key.tsv) compared with the R4844 sign words. Only 35 of 131 signs (26%) have a Stafford sign label, and the frequent word-initial signs (□, ≠, ÷) are absent from that alphabet. Ruled out at the label level; a glyph-by-glyph check needs the R4844 images (DECODE login).

## Contribution, 9 Nov 2026 (Brice Dudout, with Claude): the sign alphabet and the name code from the deciphered pairs

See `dudout/README.md` (text only, no image). The same sign alphabet is deciphered at the time in DECODE R4689, R4835,
R4836, R4837 and R4845 (Add MS 32657). A key learnt on R4689, R4835 and R4836 scored 0.646 (best of 200 shuffled keys
0.213) on held-out R4845: partial by the protocol fixed in advance. With it the R4844 sign words read in part: 16 of 19
groups (plot, judgment, her selfe, violent course, absent, attempt, traine, Stirling, suspicion, Lorde, Scroupe, secreat,
plot, secrecy), 3 unresolved (`dudout/reading_R4844_signs.md`). Name code from the pairs' glosses
(`dudout/name_codes.md`): **3 = the Queen / England** (texts/key.md has "France", M), 14 = Earl of Leicester, 27 = the
Secretary, 37 = Scotland.

## 14 Nov 2026: full-texts pass, R4838-R4839 listed

`outcome.texts` had no entry for R4838-R4839. The folder holds no text of either letter: they were viewed on the
DECODE images on 21 Sept and compared with CSP Scotland viii nos. 40 and 65, and nothing was saved. Tried today:
the DECODE full images (refused without the login: "Insufficient permissions to see the full image"), and the
calendar (British History Online: premium content; HathiTrust: Cloudflare bot check; archive.org
`calendarofstatep0008vari`: lending only, HTTP 401). None reachable, so neither a transcription nor the calendar
abstracts could be added.

Done: `texts/R4838-R4839.md` lists the name numbers recorded for the two letters (section 1 above) with their values
from `texts/key.md` and `dudout/name_codes.md`; the entry is `not prose` with `transcription_missing`. Open: the
text of the two letters (blocker: needs the DECODE login, or a reachable copy of CSP Scotland viii).

Note on the count: `fraction_read_source` counts "R4838/R4839 10" name-code units as read, while section 1 lists
nine numbers for the two letters (3 and 6), two of them (13, 30) open in the key and 37 open until 9 Nov. The
count could not be re-made without the pages; it is left as it stands and flagged here.

## Sign check K, 19 Nov 2026 (R4844 sign words)

Level sought: "AI decipherment, human-checked on a sample of signs" (`outcome.sign_check`, held in `sign_check_pending.json`
until PR #789 adds the field to the schema; files in `sign_check/`). It checks how signs are written, not the key or the
reading, and it changes neither the class nor the state.

**Who did what.** The checker is Brice Dudout, the contributor of the sign-word reading (a project member, not an independent
reader). He answered blind: one boxed sign per question, shapes cut only from certain sign words of R4844 (same hand, same
letter), with "none / other shape", "illegible" and "not a sign"; no gloss (the struck interlinear masked), reading, place or
date was shown. An AI model (Claude Opus 5.5) wrote the rule, chose the signs by it, cut the thumbnails, built the sheet,
scored the answers and read the free-text remarks. The answer key stays private; its content for each question is in
`sign_check/sheet-K-results.tsv`. No image, crop or thumbnail is committed: the images are the DECODE study images of R4844,
not reproduced.

**Rule.** `sign_check/sheet-K-rule.md` (in French, as written), SHA-256
7d53c787b1a113a2e0ca586a66863c442b7cae534a1deba845adc5784a933ab5, written and hashed on 19 Nov 2026 before any thumbnail was
cut and before any answer. On the certain words, the dotted trait (DIV, read r or s) splits by the place of its dot: above =
r, below = s; dot after it on the line (TD) = t. Targets: ten dotted traits or barred signs in probable or unresolved groups
(4, 14, 12, 16, 2, 9), one sign per question, with the shape that makes the word named for each. Controls: the r of "course"
(group 8) and the k of "violent" (group 7). The rule was applied as written, with no change. **Declared deviation:** the
rule has no written integration clause. It was applied in the strictest way, as on the other sheets of this folder: a group
becomes certain only when every target in it gets the shape that makes it; "none / other shape" leaves the group at its
grade. That application was written after the answers; it adds nothing to the rule.

**Answers.** `sign_check/sheet-K-answers.json`, exported 2026-11-19T22:30:25Z (SHA-256
dc436bb4cecec6c6c18380315e5da10a233fd19c52ef53b9d3c7022e4a500c9f). Controls 2 of 2. Ten target signs: 2 corrected, 5 as
transcribed, 3 "none / other shape", each with a remark.
- Group 12 **traine**: the first trait has its dot after it (t): P -> **S**.
- Group 16 **Scroupe**: the barred sign is "=" (p): P -> **S**. Whether it names Lord Scrope is a separate question.
- Group 4 (candidate "supp...t"): the first sign has its dot below (s) and the fourth is "=" (p; remark: with a stroke
  through the middle), but the second is another shape ("a dot, then a trait"): stays unresolved.
- Group 14 suspition: the third and fourth signs have their dot below (s); the fifth is another shape ("an L with a stroke
  below"): stays probable.
- Group 9 [a]bsent: the sign after e is another shape ("a trait with a dot above and below"): stays probable.
- Group 2: the fifth sign has its dot below (s); the group stays unresolved.

The three new shapes are leads, not values: one case each, to be found elsewhere before any value is given.

**Effect.** `dudout/reading_R4844_signs.md`: grades of groups 12 and 16, and a paragraph on the sheet. Sure groups 11 -> 13
of 19 (0.579 -> **0.684**); 3 probable, 3 unresolved. A text under 40 words with 6 holes: still read in part. `fraction_read`
is unchanged (its units do not include the sign groups).

**Limits.** One checker, inside the project. Two controls show little on their own. The signs were chosen because they were
doubtful: a diagnostic, not a sample of the text. No person has audited the model's part. This is not a `human_check`.

## Sign check K2, 20 Nov 2026 (R4844 sign words)

Follow-up of sheet K, for its three new shapes. Same level and roles (checker: Brice Dudout, the contributor; an AI model,
Claude Opus 5.5, wrote the rule, chose the signs, cut the thumbnails, built and scored the sheet and read the remark). No
image, crop or thumbnail is committed: the images are the DECODE study images of R4844, not reproduced.

**Rule.** `sign_check/sheet-K2-rule.md` (in French, as written), SHA-256
de905a2656743a872a68e3d154bdb0a6f0ae6c72cef47dffdc5962f9acc803e4, written and hashed on 20 Nov 2026 before any thumbnail
and any answer. Unlike sheet K it has a written integration clause. The 19 sign groups were searched for other cases of the
three shapes: "an L with a stroke below" had a second possible case (the "=" of "attempt", where an upright reaches the
struck-out interlinear: perhaps the stem of a letter of the gloss); "dots above and below" a possible second case (group 2);
"a dot then a trait" none, so it was not asked. Three targets, two controls (the dotted r of "Sterling", the # of "attempt").

**Answers.** `sign_check/sheet-K2-answers.json`, exported 2026-11-19T23:31:13Z (SHA-256
130e58077cc9c911417400142ba956182ea508e39b9708c73c0486afe8b7951d); results `sign_check/sheet-K2-results.tsv`. Controls 2 of 2.
Group 14, fifth sign: "=", with the remark that the "L with a stroke below" he saw on sheet K was an error: the upright is a p
of the line above. Group 4, fourth sign: "=". Group 2, fifth sign: dot below.

**Effect.** By the clause, the fifth sign of group 14 is a p (as in "plot" and "attempt", certain words): it is relabelled EQ
(it was transcribed ⊥) and **suspition** becomes certain. The lead "L with a stroke below" is withdrawn, and with it the idea
of an "= with upright" variant (the upright in "attempt" is likewise outside the sign). Groups 2 and 4 stay unresolved.
Sure groups: 13 of 19 = 0.684 -> **14 of 19 = 0.737** (R4844 sign words, `dudout/reading_R4844_signs.md`). The target's
fraction_read (0.36) does not count R4844's units and is unchanged. Still read in part (fewer than 40 words, 5 holes).

**Limits.** One checker inside the project; two controls; signs chosen because doubtful. Not a `human_check`.

## Review of #821, 20 Nov 2026 (R4844 sign words)

Two groups go back to probable after the review of PR #821 (Daniel Bourdeau, 20 Nov 2026); no sign label or key value is
changed.
- Group 14, {suspition}: sheets K and K2 gave opposite answers on its fifth sign. Sheet K said "other shape, an L with a
  stroke below"; sheet K2, written knowing that answer, said "=". The group also has more s-signs than the word needs. It
  stays probable unless another checker settles that sign.
- Group 16, {Scroupe}: the sheet settled only ≡ = p. Sign by sign (`dudout/reading_R4844_signs.md`): DIV s/r, ψ (no row in
  `sign_key.tsv`; c only by context in groups 17, 19), DIV r, L o, m u, ≡ p, MP **l** (as in "plot" and "lorde" in the same
  postscript; "sometimes p" added after the measurement), d e. That is "s?rouple", perhaps "scrouple": eight signs for the
  seven letters of "Scroupe". It stays probable until MP and ψ are settled.

Sure groups: 14 of 19 -> **12 of 19 = 0.632** (12 S, 4 P, 3 unresolved). Still read in part. fraction_read (0.36) does not
count R4844's units and is unchanged.

## Integration of #821, 20 Nov 2026

Done at the integration of PR #821 (maintainer session, an AI agent; nothing here was checked on the DECODE images).
- `profile.json`: the `reading_review` of the sign-words entry is now the reviewer's (grade B), in place of the
  contributor's own of 9 Nov 2026. `outcome.gaps`, the sign part of `outcome.parts` and `outcome.notes` now give the state
  of the Remaining gaps section above: a partial sign key, sheets K and K2, 12 of 19 groups certain, 4 probable, 3
  unresolved; open: groups 2, 4, 10, the fifth sign of group 14, MP and ψ in group 16.
- The K2 relabel of the fifth sign of group 14 (⊥ -> EQ) stays in the sign column of `dudout/reading_R4844_signs.md`, but
  it was not accepted on review as a settled correction: sheets K and K2 disagree on that sign. `sign_check_pending.json`
  says so in its K2 entry, so the sign is not counted as corrected when the record moves to `outcome.sign_check` after #789.
- Not decided: the sign part of `outcome.parts` still has method "not solved" and extent "none", which record the project's
  own attempt of 21 Sept 2026 (section 4). Whether it is reclassed on the contributed sign key, with `outcome.provenance`
  and the README row to match, is left to the owner.
