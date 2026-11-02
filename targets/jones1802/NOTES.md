# Harford Jones's Baghdad code, 1798-1802 (IOR/L/PS/9/76/49, 51, 212, 217)

Status: in progress

British Library India Office Records, Political and Secret, IOR/L/PS/9/76: papers of Harford Jones, East India
Company Resident at Baghdad. Free IIIF images on the Qatar Digital Library (found by the QDL sweep,
`research/qdl/`). Viewed and transcribed 29 Oct 2026.

| item | QDL record | what |
|---|---|---|
| /49 | vdc_100109378677.0x000001 | Jones to Henry Dundas, Bagdad 17 Dec 1798, "true Copy" in code (2 pp.) |
| /51 | vdc_100109378680.0x000001 | "Copy - Original in Cypher. Secret." The same letter in clear |
| /212 | vdc_100109378870.0x000001 | "Translation ad Sensum" of a letter from KARAP[ET] dated Erzeroum 20 Nov, received 6 Jan; docketed "Enclosed in Sir Har[ford Jones's letter] to the Chairman ... 20 Jany 1802" (6 pp.) |
| /217 | vdc_100109378875.0x000001 | "Translation ad Sensum" of a letter from KARAPET dated Erzeroum 19 Dec, received 12 Feb (2 pp.) |

## The system

An English one-part code. Each group is `page,word`, and the pages run roughly in alphabetical order. A group
stands for a whole word, or for a letter when a word is spelled out. Letter groups sit at the start of their letter
in the book: A 1,1; B 28,1; C 29,10; D 93,66; E 123,1; F 141,67; G 161,70; I 187,63; K 213,8; L 215,23; M 228,45;
N 229,28; O 256,12; P 266,63; R 305,25; S 327,1; T 376,56; U/V 398,16; Y 439,66; Z 440,72. Second codes: C 49,10;
N 249,48 / 249,45; O 256,10; A 56,11; L 215,3; H 147,7 and 174,7; P 265,63. Pages 442-443 hold personal names,
past Z.

- Clear words are left in the text ("he had", "on the", "into"). The code is applied to the sensitive words only.
- Inflections are suffixes after the group (`230,1 ing` making, `373,52 ed` astonished, `129,70 es` enemies), or a
  third number (`177,12` have, `177,12,2` had; `13,71,7` is, `13,71,5` are).
- Function words (the, of, to, a) take groups ending `,2` on many different pages. These may be homophones, or
  "word 2 of any page" may be a rule. The pairs do not settle which.
- The alphabetical order is only rough between M and W: me 235, measure 235, would 238, with 236, while N is at 229.

## 1798 key from the pair 49/51

`ct_49.txt` holds /49 (326 groups by `align.py`'s tokens) and `pt_51.txt` holds /51 (308 words). `align.py` aligns
them by dynamic programming over (group, word, letter-in-word):
- 221 groups line up with one word each, and 104 are letters of spelled names (Constantinople ×4, Russians ×2,
  Russian, England, India).
- 74 clear words match. 4 moves are skips: "would", "if" and "Government" are not in the code copy, and one group
  `230,1` falls out where `230,1,2,2` stands for "make a".
- Output: `table_1798.tsv` (group to word) and `align_1798.tsv`.
- Nine groups get two words. The `,2` function-word groups cause most of these, plus two places where the clear copy
  paraphrases ("this Question, and a" against `302,19. 15,65. 15,65 a`).

## Test: do the 1798 values read the 1802 letters? Yes, same code book

`apply.py` applies the 1798 table to `ct_212.txt` and `ct_217.txt` and writes `decode_212.txt` and `decode_217.txt`.

| letter | groups | 1798 word value | 1798 letter value | letter fixed by a 1802 name | no value |
|---|---|---|---|---|---|
| 217 | 128 | 3 (2%) | 62 (48%) | 22 (17%) | 41 (32%), 32 distinct |
| 212 | 580 | 16 (3%) | 315 (54%) | 119 (21%) | 130 (22%), 85 distinct |

- Every 1798 group that recurs in 1802 gives sense in place:
  - `309,26` received (both headings)
  - `31,7` Bacha
  - `169,25` Government ("belonging partly to the Government of SEFLIS")
  - `271,10` party ("depart in small parties")
  - `302,31` put ("will soon put an `129,40` [end]")
  - `382,28` then
  - `353,5` some
- The spelled names read with the 1798 letters plus the new ones:
  - KARAPET; ERZEROUM; ABDULLAH × AGA; MERDIN; BAGDAD; CONSTAN(tinople); DEARBEKIR; MOOSHA; BAYEZEED; MADAN
  - PHILIPOOS × AMEREK; ARMENIANS; ASTRACHAN; EECH × MIASIN (Etchmiadzin); ERIUAN (Erivan)
  - PUMBEC (Pambak); SEFLIS (Teflis, spelled with S); KARS; ALCALZIKEH (Akhaltsikhe); TOMANS; RUSSIA(N); PERSIA
  - DAMAR × CAPI (Demir Kapı), i.e. DERBEND
- Few 1798 *word* groups recur (2-3% of the 1802 groups), because the 1802 letters are about other things. Most
  open groups are content words. The page alone places them in the alphabet:
  - `95,32` D-E, the heading formula: "dated"
  - `96,75` D-E: "December"
  - `145,56` E-I: "February"
  - `188,31` I-L: "January"
  - `255,4` N-O: "November"
  - `221,15`/`221,25` L-N: "letter"
  - `378,44` T-U: "Tartar"
  - `164,30` E-I: "General", after RUSSIAN
  - `272,17` P-R: "Patriarch"
  - `128,21` E-I: "Emperor"
  - `149,56` E-I: "Firman"
  - `262,35` O-P: "Ottoman"
  - `169,74 404,67` G / V: "Grand Vizier"
  - `394,37/38` T-U: "troops"
  - `95,50` D-E: "days"
  - `205,70` I-L: "intelligence"

  These readings are proposals from context and alphabet position. None is in `table_1798.tsv`.

## Content (proposed, not a reading yet)

The informant, an Armenian (KARAPET), writes to Jones from Erzeroum in Nov-Dec [1801]. He went in the suite of
Abdullah Aga to Merdin, then Dearbekir and Madan, and reached Erzeroum.

He reports the disputed succession to the Armenian Patriarchate (Catholicos) at Etchmiadzin:
- The Armenians at Astrachan back `442,56`. The Khan of Erivan backs `442,55`, who pays him 400 tomans and holds
  the convent.
- A Russian firman and an Ottoman firman favour `442,56`.
- A Russian General is at Teflis, with troops at Pambak, 12,000 according to /212.

He also reports:
- The Pasha of Akhaltsikhe has fled to Teflis.
- The Grand Vizier has given Madan and Erzeroum to `443,48` Pasha, who served in Egypt.
- The Russians threaten Erivan.

`442,55`/`442,56` are presumably David and Daniel, the rival Catholicoi of 1801. That is not yet checked.

## Siblings and retry (29 Oct 2026, second pass)

- **Siblings opened.**
  - /214 (Rickards/Manesty, 1801-02) uses a different system, a homophonic two-digit alphabet only for dates and a
    few words, with the body in clear: A 9/37, E 8/40, N 70, I/J 75, S 39, R 23, H 5, D 30, O 36, V 33, M 4. It
    gives "dated R-E-S-H-E-D", "the 12th N-O-V", "received the 12th J-A-N" and "made public to all the
    A-R-M-E-N-I-A-N-S".
  - /243 and /244 (May 1802) are in clear.
  - /274 (Erzeroum, 7 Aug 1802, same informant?) is in clear and names Pumbec, the Khan of Erivan, the Pasha of
    Kars and the Russian commander "Shebkatoor at Teflis".
  - /211 (interrogation of the Armenian Stephan, 8 Jan 1802) confirms the Pasha who fled Akhaltsikhe to Teflis.
  - /213 (Jones to Wellesley, 13 Jan 1802) does not paraphrase the code.
  - None is a clear copy of a coded letter, so the siblings add context, not values.
- **Key rebuild.** `proposals.tsv` gives values for 98 of the open groups, from their page position in the
  alphabet plus context, graded H/M/L. Examples:
  - ALTOON IAAK = Turkish *altun ayak*, "golden leg": "so called from having lost a leg in war and wears a golden
    or gilt [one] in the place of it".
  - "the convent of the three churches" = Uch Kilise, Etchmiadzin.
  - "not in command of the troops who are commanded by a Russian General".
  - Three misreadings resolve to 1798 values: `148,76` = 128,76 find; `160,30` = 164,30; `87,63` = 187,63.
  - DE-A-RBEND has a second A, `1,45`.
- **1798 table correction.** The DP had shifted "Government (said he emphatically)", giving `169,25` = said. It is
  now Government, with `327,66` = said (`align.py` OVERRIDES).
- **Retry** (`apply.py --retry`, `reading_212.txt`, `reading_217.txt`): 645 of 708 code groups (91%) read from the
  1798 key, the 1802 letters or a grade-H proposal. Another 32 are grade M, 25 grade L, and 6 are open.
- **Statistical test** (`docs/_validate.py`, en-modern, H values only): underdetermined. Most read stretches are
  spelled foreign names or single code words between clear words, which a letter model cannot separate from a
  fitted key.
- **Names.** `442,55`/`442,56` are presumably the rival Catholicoi David and Daniel. The two letters disagree on
  which one arrives at Erzeroum to be escorted, so both are graded L.
- Work stopped here at the user's request (29 Oct 2026): the session turned to logging the sweep.

## Remaining gaps

- 212/217 groups with only an M or L value (57 tokens) and 6 open tokens (443,48 x3, 48,75,3, 239,69, 53,36) - blocker: open-codes; workable from context, set aside on 29 Oct 2026 when the session turned to logging the QDL sweep
- The `,2` function-word groups (homophones or a rule) - blocker: open-codes; untested
- Name groups 442,55 / 442,56 (which Catholicos) - blocker: open-codes; the two letters conflict, needs a history of the 1801-02 succession
- Transcription doubts (/49 superscript over `187,3`, blotted `179,7`; /217 `213,7` vs `213,8`; /212 SGUSGEG after DERBEND) - blocker: open-codes; re-read at higher zoom

## Escalation

- [x] siblings: /214, /243, /244, /274, /211, /213 opened 29 Oct 2026 (see above). None is a clear copy of a coded letter; /214 uses another system.
- [x] clear-pages: /51 is the clear copy of /49 and gave the 1798 table. /212 and /217 are themselves English "translations ad sensum" with no clear version of the coded words on their leaves (all six and two pages viewed 29 Oct 2026).
- [x] known-keys: the 1798 table from 49/51 applied to 212/217 (apply.py). The code book itself is not identified; it may be a printed vocabulary of about 445 pages with names after Z.
- [x] print: web search 29 Oct 2026 found no edition or study of these letters or of Jones's cipher.
- [x] key-rebuild: proposals.tsv, 98 groups bracketed by page and context, graded H/M/L.
- [x] retry: apply.py --retry, 91% at grade H or better; validation underdetermined.

## Files

- `ct_49.txt`, `pt_51.txt`, `ct_212.txt`, `ct_217.txt`: transcriptions from QDL IIIF crops.
- `align.py`: builds the 1798 key and writes `table_1798.tsv` and `align_1798.tsv`.
- `apply.py`: applies the 1798 key to 1802 and writes `decode_212.txt` and `decode_217.txt`. `--retry` adds
  `proposals.tsv` and writes `reading_212.txt` and `reading_217.txt`.
- `proposals.tsv`: graded values for the groups with no 1798 value. `validation.tsv`: pairs for `docs/_validate.py`.

## Dudout corrections, 29 Oct 2026
- Held-out check of the 1798 table (ct_49/pt_51/align_1798.tsv): table from /49 f. 1r only (129 rows), tested on f. 1v: letters 0.959 (70/73, 0 wrong) against witnesses max 0.329. Groups x,2 are not fixed values. New sibling leads: IOR/L/PS/9/76/134 (Malcolm to Jones, Shiraz Aug 1800, partly in cypher) and BL Add MS 41767-41768 (Jones papers).
(Brice Dudout, research/dudout_2026-10-29/; his findings, not re-checked here.)
