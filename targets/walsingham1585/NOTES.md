# Walsingham → Edward Wotton, 28 Jul – 10 Sep 1585 — BL Add MS 32657, DECODE R4838, R4839, R4840, R4844

Catalogue entry 82 ("Sir Francis Walsingham … to Edward Wotton, ambassador to Scotland, 4 ciphertexts", Tomokiyo
list, rule-scored). Worked 2026-09-21. **Outcome: read in part.** All four letters read. The name code is mostly
identified. About fourteen words in a sign alphabet in the 10 Sep letter stay unread.

Status: read in part (2026-09-21). Companion to [wotton1585](../wotton1585/NOTES.md), Wotton's own drafts to
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

## Remaining gaps
- R4844 sign words (~14 words, ~120 signs) - blocker: too-short; homophonic sign alphabet, no crib, no key, interlinear decipherment blotted out
- name codes 13, 14, 23, 30, 32, 37 - blocker: open-codes; not glossed in CSP or Wotton drafts; context too thin
- clear-text gaps [..] in reading_R4840/R4844 - blocker: illegible; second pass 14 Oct 2026 on the DECODE images (`clear_gaps_pass2.md`): of 46 places, 32 read H/C, 8 M, 6 illegible (blots, stains, struck interlinear words); nine transcription corrections found, not yet merged into the reading files

## Escalation
- [x] siblings: Wotton drafts R4841-R4843 in the same volume read for numbers and cribs
- [x] clear-pages: interlinear lines above the sign words examined; struck out, unreadable
- [x] known-keys: DECODE key records and Tomokiyo Elizabethan ciphers searched; no Wotton 1585 key
- [x] print: CSP Scotland viii checked page by page (nos. 40, 65, 106)
- [n/a] key-rebuild: the name code is a list of names with no internal order to bracket, and its open numbers occur once or twice in thin context; the sign alphabet is ~120 homophonic signs with nulls and no crib, below what an anneal can fix (a crib from SP 52/38 copies would be needed first)
- [x] retry: clear-text gaps re-read on the images 14 Oct 2026 (`clear_gaps_pass2.md`); name-code grades unchanged (the new words fix no open number)

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

