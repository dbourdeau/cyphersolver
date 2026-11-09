# Edward Wotton (Scotland) to Walsingham, 25 Aug – 1 Sep 1585 — DECODE R4841–R4843

Status: in progress (re-read 22 Oct 2026, batch b16: all three drafts transcribed and read; the write-up pages still describe the audit state).

**22 Oct 2026, reading audit** (George Lasry's test: can sentences be built and translated?): the repository holds only summaries of R4841-R4843 and the code table (texts/key.md); no draft is transcribed. Each image was checked (main checkout decode/s484x_1.jpg): all three are clear English drafts with numeric name codes. All three are *decoded, not read* in profile.json; class read -> not read, method -> not solved, fraction_read unknown -> 0. The code identifications stand.

**22 Oct 2026, re-read (REREAD_BRIEF, batch b16; texts/R4841-R4843_reread_log.md)**: the DECODE records were fetched
again (only the four page images each; nothing added since 21 Sept). CSP Scotland viii could not be reached for a text to
align with (HathiTrust Cloudflare check; archive.org lending-only, 401). The three drafts were **transcribed in full**
from the full-resolution images (texts/R484x_transcription.txt: struck words, interlineations, doubtful words marked,
plus Wotton's working notes at the head of f. 167r) and **read** in their last state with the name code glossed in place
(texts/R484x_reading.md) and rendered in modern English (R484x_en.md). Every reading word is carried by the
transcription or is a modernised spelling of a word in it (research/reading_audit/b16_wotton_align.py); supplied words
are bracketed. Clean-sentence share on the reading bodies (_check_reading.py): **R4841 0.98, R4842 0.89, R4843 0.91**
(before: no text). All three relabelled read; class not read -> read; method -> key recovered based on adjacent
plaintext; fraction_read 0 -> 1.0.
- **Code 3 = the Queen of England, not France** (flagged for review: sense only, but every occurrence fits): "divert 10
  from 3 ... or if that finding the K. constantly ^{affection} towarde 3 ... he wil not fail to convey him into Fr."
  (R4841 f. 167r) and "it can no way stand with 3 honor that I should be at that time in this contrey" (R4843 f. 175v,
  Wotton asking for his recall). 9 = England ("the 9 frendshippe", R4842) stays probable, sense only.
- New details read: the King was hunting on an island of the Duke of Lennox (25 Aug); Gray asks Elizabeth to "take
  the matter very highly" after Lord Russell's death and hold the King from the league; the 500 men are to be led by
  "L. of Arb:" (Lord John Hamilton, commendator of Arbroath), "the Erle Mo:" and "Master G." (Glamis); Gray asks money
  "out of 36" for 100 men to hold the King's house; Cuthbert Armorer and Sir William Stewart's report that the Lords
  are to be sent home "to shuffle the cards" (R4842 ticket to Leicester); Wotton's "My sworde can cutte as wel as an
  other mans".
- 27 is a Hamilton favourer kept from Gray's plot (R4843 ticket: "40 would reveale it to 27, whome wee esteeme no very
  great favorer of the LL"); still unidentified. 32 (a place the King might flee to, R4843), 36 (source of money, R4843)
  and 11 ("the 11 course", R4842) unidentified.

BL Add MS 32657, ff. 167-168 (R4841, 25 Aug), f. 173-174 (R4842, 30 Aug), f. 175-176 (R4843, 1 Sep).
DECODE lists them as "Non-decrypted, numerical, cipher type unknown".

Earlier status (before the 22 Oct 2026 reading audit): read (2026-09-21). Nothing needed breaking.

## What the records are
The images (fetched with the DECODE cookie, kept in `decode/`, git-ignored, BL copyright) are **Wotton's own
drafts, written in clear English**, headed "To Mr Secretary the 25th August", "... the 30th of August 1585", "... the
first of September". The only "cipher" is a small **numeric nomenclator of one- and two-digit code numbers for
persons and places**, written in the text in place of names ("39. came to me yesterday", "the enlargement of 19").
There is no letter cipher. The drafts can be read as they stand; the only task is to identify the code numbers.

## The code numbers, identified from context
| no. | reading | evidence |
|---|---|---|
| 19 | **James Stewart, Earl of Arran** | "the enlargement of 19" (Arran was warded after Lord Russell's murder, 27 Jul 1585); "19 yet remaineth at Kinneil" (Arran's house); "the Arranistes" |
| 39 | **Patrick, Master of Gray** | Wotton's informant who pushed Arran's fall; "complained to his friend in England" of Wotton's coldness; charged by the King to catch Hay and Dury |
| 10 | **King James VI** | "possess themselves of 10 and 19"; "the 10 house"; "hold the 10 from Stirling"; "his reconciliation with 10" (the drafts also write "the K." in clear) |
| 9 | Queen Elizabeth / England (probable) | "the K. ... very desirous of the 9 friendship" |
| 20 | a banished or disaffected lord seeking peace with the King through Arran; "20 make some incursion upon the L. of [Jo]hnstone with whom he hath a quarrel" → **Lord Maxwell** (probable) |
| 24 | a Catholic lord, suspected of a secret agreement with Arran and of a plan to take the King to France, paying his men with French crowns (the Jesuits' 6000 crowns) → ~~Earl of Huntly~~ **Sir Thomas Kerr of Ferniehirst** (CSP Scotland viii glosses "Farnyhurst"; see below) |
| 3 | France or the Guise party (probable) | "divert him from 3", "convey him towards 3 ... into France" |
| 27, 40 | two of Gray's associates at court ("39. 40. 27. [cannot] live safely in the court"); 27 "was greatly hers [Mary's] and is a great favourer of the Hamiltons" | unidentified (candidates: Secretary Maitland, Justice Clerk Bellenden) |
| 32 | a place into which the King (10) might "convey himself" rather than be taken (R4843 f. 175r: "if 10 would ... passe over the water into the Fife or seeke to convey himself into 32, he wil by force stay him"; corrected 22 Oct 2026 from "Arran") | unidentified |
| 36 | source of money for 39's hundred men ("money out of 36") | unidentified (the Queen's treasure?) |

## Content (summary)
- 25 Aug: Gray (39) urges that while Arran (19) is in favour with the King (10) the banished lords can never be
  restored or a league with England made safe; propose that Elizabeth fund the lords "to take 19 and seize 10's person".
  Rumours that Arran and 24 are agreed and that 24 may carry the King to France.
- 30 Aug: answers Walsingham's of the 21st about Gray's complaint; 27 and 40; Arran still at Kinneil under guard;
  Bothwell come to court "to the great grief of the Arranistes"; Hay and Dury (Jesuits) in the country.
- 1 Sep: the device of 39 and the Prior of Blantyre: the lords to join with 20 under colour of his feud, send 500 men
  to seize the King and Arran; 39 asks for money to hold the King's house; commissioners' meeting on the Borders.
  (This is the plan that became the lords' return and the fall of Arran at Stirling, Nov 1585.)

## Prior art
CSP Scotland vol. 8 (1914) calendars Wotton's despatches of these dates; the BHO text is paywalled and the archive.org
copy is lending-only, so whether the calendar prints these drafts' code numbers resolved was not checked. The
identifications above rest on the drafts' own context.

## Addendum (2026-09-21, from walsingham1585)
CSP Scotland viii *was* checked there, through the HathiTrust text-only view (miun.abe1726.0008.001). The calendar
glosses the numbers in Wotton's despatches: Arran ["19"], Master of Gray ["39"], Justice Clerk ["40"] and
**Farnyhurst ["24"]**, so 24 is Sir Thomas Kerr of Ferniehirst, not Huntly. No. 106 (1 Sep) calendars the R4843
draft with "Morton" for 20 (Maxwell, styled Earl of Morton). Walsingham's side of the correspondence (R4838–R4840,
R4844) is in [walsingham1585](../walsingham1585/NOTES.md).

**23 Oct 2026, v6 spelling check (research/reading_audit/v6_spelling_files.txt; REREAD_BRIEF step 3-4: no modern spelling in a reading)**: texts/R4841-R4843_reading.md said 'Spelling modernised'. Restored word by word to Wotton's spelling from his drafts as transcribed (texts/R484x_transcription.txt; v6_align.py): yland, forbeare, doinges, tyme, heere, wil, shal, frendes, contrey, therfore, Copie; abbreviations written out. No word changed. Explicit-hole shares unchanged (0.947-0.981); all keep read.

## Remaining gaps

- R4841, R4842, R4843: the drafts, not transcribed - closed 22 Oct 2026 (b16): transcribed in full and read (0.98, 0.89, 0.91)
- Codes 27, 32, 36, 11 unidentified - blocker: no-key-material; no key on DECODE or in Tomokiyo; CSP Scotland viii (which glosses 19, 24, 39, 40) unreachable on 22 Oct 2026 (HathiTrust Cloudflare check, archive.org lending-only)
- A few interlineations and struck-over phrases (R4842 p2.05-p2.09, R4843 p2.10-p2.17) - blocker: illegible; read in zooms at native resolution, left [..]

## Escalation

- [x] siblings: Walsingham's side (walsingham1585, R4838-R4840, R4844) checked
- [x] clear-pages: the drafts are clear text; not transcribed
- [x] known-keys: CSP Scotland viii glosses 19, 39, 40, 24
- [x] print: CSP Scotland viii calendars the despatches (no. 106 for 1 Sep)
- [n/a] key-rebuild: no cipher
- [x] retry: 22 Oct 2026 (b16) the three drafts transcribed in full and read; DECODE records re-fetched (nothing new); CSP viii retried (unreachable)

## Note, 9 Nov 2026 (Brice Dudout): name code 3

The deciphered pairs in Add MS 32657 (DECODE R4689, R4835, R4836) gloss **3 as the Queen / England** ("Her Ma^tie", "the Q.",
"Eng:"), not France; also 14 = Earl of Leicester, 27 = the Secretary, 37 = Scotland. Details in
`../walsingham1585/dudout/name_codes.md`; texts/key.md not edited.
