# Szent-Ivány to Rákóczi, Munkács, 14 May 1711 · catalogue 3910

Catalogue 3910 (#3674 in the draft of PR #910, before the gate gave it its id); removed from the catalogue at this write-up.

**Read in part.** The contemporary decipherment of Szent-Ivány's dispatch of 20 May supplies a key to his letter of 14 May. Szent-Ivány explains why he has held back from offensive action and asks the prince to send men to sustain morale. The four inserted cipher passages contain 56 groups. The evidence for the reading comes from two different letters.

The ciphertext is document 17, printed p. 1109. Document 24, pp. 1118–1120, is from the same sender to the same recipient. On p. 1119 Szent-Ivány himself discusses changing his keys after other officers surrendered theirs. On p. 1120 the editors tabulate values recovered from the chancery's decipherment of no. 24 and explain the first-digit rule in note 209. The archive identifies no. 17 as G 15, Caps. H, Fasc. 240, ff. 112–113. The present transcription was checked against the printed page image. The archival catalogue entry supplied no manuscript scan for comparison. [Edition, no. 17](https://epa.oszk.hu/00000/00018/00290/pdf/EPA00018_hadtortenelmi_2012_04_1087-1138.pdf#page=23) · [Sibling key, p. 1120](https://epa.oszk.hu/00000/00018/00290/pdf/EPA00018_hadtortenelmi_2012_04_1087-1138.pdf#page=34) · [Archival record](https://adatbazisokonline.mnl.gov.hu/adatbazis/ii_-rakoczi-ferenc-fejedelem-leveltara_-emigracioba-vitt-resz/adatlap/18712)

## Key and check

R619 comprises five tables. The one naming Szent Ivany, D2585, has only one three-digit entry, 131 for O. Direct lookup covers 0/19, 0/23, 0/7 and 0/7, even allowing a match on the number alone. [R619 transcription](../bay1706/keys/DOC_R619_D2585_2585.txt)

In the sibling key, the first digit selects a column and the mark selects a row. Thus plain 500 gives *e*, tilde 500 gives *n*, and apostrophe 5xx gives *v*. An underline across the middle digit of 2xx gives *sz*. The editors tentatively assign underlined 300 the whole word *hogy*. The published letter and digraph rows assign 52/56 groups. Extending the tentative whole-word value from underlined 300 to underlined 333 adds one proposed assignment. Three other signs remain without an assignment after that proposal. Value coverage measures lookup only. The entire third passage has values but its lexical reading remains uncertain.

## Four readings

| Passage | Mechanical output, with interpretive word spacing | Proposed sense in context |
|---|---|---|
| 1 | [hogy?] tülünk épen nem l[515;]hét | “Your Highness should know **that it is quite impossible for us**.” Read *lehet* with *e* for the semicolon-marked group. Plain 515 is explicitly *e* on p. 1120. The final vowel is enciphered as *é*. |
| 2 | ha modom lesz [214.]enne [4_10.] mutatom | “But **if I have the opportunity, I will [ … ] show it**.” Plain 2xx fits *b* between the attested alphabetic columns *a* and *c*, giving *benne*. Underlined 410 could stand for *meg*, giving *megmutatom*. This is a single occurrence with no confirming gloss. |
| 3 | é·sz·v·e·sz·c·ü | “But there are many **[? people out of their senses]**.” The historical word *észvesztő* fits the sentence and the first five groups. Plain 300 gives *c*, where 300 with an apostrophe would give *t*. The final underlined 100 gives *ü*, where the proposed modern form has *ő*. Both discrepancies remain open. |
| 4 | sz·i·v·e·k·e·t | “who did not uplift **the hearts**.” Modern *szíveket*, the accusative plural required after the verb. All seven values come from the sibling key. |

The historical dictionary records *észvesztő* in the sense ‘őrült’ in 1541. That supports the candidate's meaning, independently of its cipher spelling. [Új magyar etimológiai szótár, *eszeveszett*](https://uesz.nytud.hu/index.html?searchmode=lemma&searchstr=eszeveszett)

## Evidence from the neighboring letters

In his 15 May autograph Szent-Ivány writes *késűn* (modern *későn*, “late”). This independently documents his use of *ű* where modern Hungarian has *ő*. It makes the vowel at the end of the proposed *észvesztő* easier to account for. The same letter uses *megmutatja* (“it shows”), the verb proposed for passage 2 in a different person. Both are spelling or usage parallels. Neither supplies a cipher gloss, and plain 300 still gives *c*. [Document 20, p. 1114](https://epa.oszk.hu/00000/00018/00290/pdf/EPA00018_hadtortenelmi_2012_04_1087-1138.pdf#page=28)

On 22 May he reports sending new keys and says he will wait for the prince's acknowledgment before using them. That helps date the search for another letter in the May 14 system. Neither the May 15 nor the May 22 printed letter supplies another glossed occurrence of underlined 410. [Document 27, pp. 1124–1125](https://epa.oszk.hu/00000/00018/00290/pdf/EPA00018_hadtortenelmi_2012_04_1087-1138.pdf#page=38)

A search of 106 distinct local DECODE transcription filenames in the Bay, Eichel and Geertruidenberg key collections found no table with explicit three-digit assignments for all four of *e*, *n*, *v* in the 500s and *sz* in the 200s. The screen accepted any marks on the code, split alternatives on vertical bars, and compared plain letter labels case-insensitively. The two highest counts were two of four, both in French-language sheets (R596 D2339 and R587 D2735). This search tests explicit numbers in transcribed rows. A manuscript giving ranges, a diagram, or instructions in prose could escape it.

## Reproduction

Run `python targets/szentivany1711/decode.py` from the repository root. The script prints the direct R619 coverage and each printed group beside its sibling-key value. The underscore precedes the underlined digit. The semicolon remains distinct from a dot throughout. Contextual proposals in the table above are excluded from the decoder.

## Remaining gaps

- Underlined 333 and 410, plain 214 - blocker: no-key-material; the sibling table gives no direct whole-word gloss for either marked number and omits the b column.
- Semicolon after 515 and plain 300 in passage 3 - blocker: needs-physical-access; the printed signs are clear, while checking the manuscript may establish whether the marks changed in transcription.
- Final underlined 100 of passage 3 - blocker: too-short; the class gives ü, and the writer's spelling supports a vowel variant, but this is the only occurrence of the proposed word.

## Transcription doubts

- 515 (passage 1) - read: semicolon; checked: image, decode; plain 515 would give the expected e.
- 300 (passage 3) - read: dot alone; checked: image, decode; a following apostrophe would change c to t. The edition prints the dot alone.

## Escalation

- [x] siblings: no. 24 gave the working alphabet. Nos. 20 and 27 supplied spelling and key-change evidence.
- [x] clear-pages: the surviving May 14 catalogue entry supplies no scan or parallel decipherment.
- [x] known-keys: tried the Szent Ivany table of R619. Screened 106 transcription filenames for the sibling alphabet.
- [x] print: checked the 2012 edition, Rákóczi's outgoing letter book and the historical dictionary.
- [x] key-rebuild: the open alphabet column and sentence support b. Underlined 410 occurs only once, before mutatom.
- [x] retry: replayed all four passages and kept each contextual proposal marked in the reading.
