# newcastle1729: the unread sibling pages, a held-out check of the code table, and the open groups

Contributed by Andrew Beling, with AI agents, 11 November 2026.
This folder adds to `targets/newcastle1729/`. It changes nothing in johonn's files or in the transcriptions taken in
from Michael Brackx (#189). The edits that go with it are in the same pull request (a dated NOTES.md section, the
Escalation and gap lines, and profile.json steps and a credit). The class and the read share are not changed:
`codetable.tsv` and the report's firm count (121 of 141) stay as they are.

[V] = checked on the image, the table or in output. [I] = inference.

## 1. What is here

| File | What it is |
|---|---|
| `PREREG.md` | the plan, written before any script or score |
| `transcription/pages_survey.tsv` | the 14 sibling pages NOTES lists as unread, page by page |
| `transcription/clear_4aug_brackets.tsv` | the bracketed passages of the 4 Aug clear copy (60903-60904), paired with the code lines of 60907-60908 |
| `scripts/check_4aug.py` | the held-out check (table without the 4 Aug glosses against the clear copy) |
| `scripts/open_groups.py` | table neighbours and report context of the 15 open groups, and the numeral groups |
| `results/check_4aug_result.json`, `check_4aug_output.txt` | the check, token by token |
| `results/open_groups_context.txt` | output of `open_groups.py` |
| `results/open_group_values.md` | proposed values for the 15 open groups, each with its evidence, and the reading they give |
| `results/table_notes.md` | eleven table values the clear copy and two re-zooms confirm or correct (none in the report) |
| `results/frozen_inputs.sha256` | hashes of the repo files and of this folder's inputs, taken before the check ran |
| `images.txt` | the HDL IIIF images and crops used |
| `CHECKS.txt` | script runs |
| **Round 2** | |
| `PREREG_round2.md` | the round-2 plan, written before either new script; `results/frozen_inputs_round2.sha256` |
| `transcription/sib194_60893.txt`, `sib194_60894.txt` | full transcription of mssBLA 194, a code letter with interlinear decipherment (Brackx listed 19 of its pairs) |
| `scripts/check_194.py`, `results/check_194_*` | the table, rebuilt without any 194 gloss, against the 194 glosses |
| `scripts/full_table.py`, `results/full_table.tsv` | full construction: one row per group, value, every gloss and clear-copy attestation, context proposal, conflict flag |

Scripts run from this folder with `python3 -I scripts/<name>.py` (`--target ..` is the default).

## 2. The unread pages [V]

None carries new glossed code (`pages_survey.tsv`). 60916 is the clear covering letter to Townshend, Cesnok 29 June
1729; the code at its edge is the next leaf (60917), already transcribed. 60910-60912, 60922 and 60964 are blank or
show-through; 60905 is the endorsement "not sent because not material and containing a complaint agt. Mr Keene".
60961-60962 are the clear 23 June letter with no brackets.

Two things are new:
- **60903-60904 is the clear copy of the coded 4 Aug letter**, with the coded passages written out in square
  brackets: about 220 code groups with an independent plaintext, unused until now.
- 60916 names the Cesnok letter "of the 5. of May"; the 188 code (60917 L05) answers "votre lettre du cinq ma-y".
  This is the dating style the report's "votre lettre du [6]" follows.

None of the 15 open groups occurs in these siblings, so no held-out test of them is possible (round 2 found
1118 in mssBLA 194, section 5).

## 3. Held-out check of the code table [V]

As registered: the table rebuilt without the 4 Aug glosses (345 groups) was aligned to the clear copy, 14 units.
**158 of 170 tokens with a value match (0.929); 200 shuffled tables: mean 0.111, best 0.171; margin 0.759. Pass.**
The full table (with the 4 Aug glosses) scores 205 of 214 (0.958). The misses are spelling (en/an, accez,
tacheoist) and conflicts between sources, set out in `table_notes.md`: 869 is perdu, not e; 880 plustot; 829 pl;
169 com; 900 pris; 791 ois; 701 mo; 191 c'est. This checks the key and the 4 Aug transcription. It says nothing
about the open groups.

## 4. The 15 open groups [I]

Value-finding only (`open_group_values.md`). Strong from slot and context: 585 ig, 1152 vos, 285 do, 1210 six (the
units 1206-1213 run deux to neuf without a break). Good: 222 conduite, 805 obligation. Fair: 689 m (a second m, like
the two l and l' groups), 1052 servi(ce), 836 pr (à l'accommodement près), 214 comte. Weak: 726 (the leaf reads 726
[V]; the sense wants 926 que), 460, 1118 (now glossed "tain", section 5). Open: 711, and 6 (a day number; 12 = a, so the low block does not fix it).

## 5. Round 2 (11 Nov 2026, evening)

Plan first in `PREREG_round2.md`; inputs frozen in `results/frozen_inputs_round2.sha256`.

**Print search: no clear text of the report or of any coded passage was found.**
- Who the correspondents are [V]: the Huntington item records and finding aid put mssBLA 176-195 among the papers of
  Alexander Hume-Campbell, 2nd Earl of Marchmont (with Whitworth, Townshend, Newcastle); "Cesnok" is Cessnock, the
  Campbell estate of Marchmont's wife, and the covering letters from there (188, 191) are his. His 8 Aug 1729 letter
  (61001) reads: "I have the Honour to transmitt to your Grace two letters from Port St. Maries which came to my hand
  together last post", and below: "Thir two letters of the 14. and 21. July I sent to the Duke of Newcastle of the
  date of the letter above" [V; the "14" could be read "19", but 189 is endorsed "In the letter of the 14 July. Sent to
  the D. of N. 8 Augt"].
- HMC *Report on the manuscripts of Lord Polwarth* (Marchmont's papers): vols I-IV are full text on archive.org and
  stop in 1725 [V]. Vol. IV prints Marchmont and Whitworth recommending "the Abbe Paretti, a gentleman of Genoa" for
  Spanish service (Cambrai, 1724) [V]. Vol. V (1725-80, 1961) is search-only on HathiTrust (osu.32435022299184): 0
  hits for "Port St. Mary", "Port Saint Mary", "Marys", "Sainte", "cipher", "decipher", "Cadiz", "galleons"; 3 for
  "Pareti", 2 for "Keene", 8 for "1729" [V hit counts; the pages are not shown]. So vol. V probably does not print
  the Port St Mary letters; its 3 Pareti pages are worth a look in a library copy.
- Coxe, *Memoirs of the Kings of Spain* (1813, 3 vols) and *Memoirs of Sir Robert Walpole* (1798-1800, 3 vols),
  archive.org full text: nothing on the correspondent [V grep]. TNA Discovery and the BL catalogue gave nothing at
  item level for 1729 (SP 94 is not calendared for these years).
- [I] The 1725 Pareti letter (179) is in this code (Brackx), and Marchmont had placed Pareti in Spain's service; the
  Port St Mary correspondent may be Pareti. Not tested.

**The full construction** (`results/full_table.tsv`, `scripts/full_table.py`): 439 groups. Basis: 136 gloss and 4 Aug
clear copy, 277 gloss only, 12 nulls, 14 context only (the open groups other than 1118). 20 rows carry a conflict
flag (glosses disagree or the clear copy differs); all are listed in `table_notes.md`. Nothing in `codetable.tsv` is
changed.

**mssBLA 194 transcribed in full** (`transcription/sib194_*.txt`) [V]: a code letter with a full interlinear
decipherment (Patiño well disposed; the garrisons in Italy; "mon projet du mariage"; Keene). Check with a shuffled
control (`check_194.py`, as registered): the table without any 194 gloss matches **89 of 93** firm 194 glosses
(0.957; 200 shuffled tables best 0.065; margin 0.893; pass). This confirms that 194 is in the same code and checks the
transcription; it says nothing about the open groups.

**1118 is glossed "tain"** in 194 L14 ("974 163 1118" = "reponse cer-tain") [V]. "tain" is written in darker ink over
an earlier gloss, and the first figure of the group is retouched in the same ink. It is the only glossed occurrence
of any of the 15 open groups, and it was seen while transcribing, before `PREREG_round2.md` was written, so it is an
observation, not a test. It rules out the round-1 guesses (toujours, très). In the report it gives "je lui ai fait
[tain] bon [?servi]ce", which does not read as French; the nearest sense is "tant" [I, weak]. 1118 is now glossed
but not read.

**60917 L02 and L17: 369, not 869** [V on full-resolution crops of 60917, 8708 px wide]. In both groups the first figure
has the flat top stroke this hand gives its 3 (as in 387 at the end of L17), not the two closed loops of its 8
(870 on L17, 1268 on L02). The gloss is "e" under both, and 869 is glossed "perdu" in 194 as well as in the 4 Aug
clear copy. Also seen: **60917 L16 "880" reads 830** (plus, in "plus-ie-u-r-s"): the middle figure is the flat-topped
3 of 438 on the same line [V].

**60909 is a separate code passage of 3 November 1729** [V image, I placement]. 60907-60908 are one leaf (60908 shows
60907 through the paper) and the catalogue counts "2 pages in cipher" for mssBLA 190 [V]; 60909-60910 is a second leaf,
in larger script and browner ink, probably the same decipherer [I]. Its text runs: I have given Mr Stanhope a letter
for you on affairs, going by the first courier, with another on my own interest; a bill of exchange sent three months
ago came back with no one to accept it; I am short of means; ask you for 250 pounds sterling and a rule of conduct;
dated "trois novembre mille sept cent vingt neuf" [V transcription]. The 4 Aug letter asks "marqués moi sur qui je puis
tirer au plustot" (60904) [V], so a bill drawn in early August that came back fits a letter of early November [I]. No
item of 3 Nov 1729 is in the Huntington file (175-195) [V list]. So 60909 is
the code part of a later letter of 3 Nov 1729, whose clear letter is not in this file, filed with 190 [I].

**Other gaps:**
- The report's date [I]: Marchmont sent the letters of 14 and 21 July on 8 Aug; the undated code report is filed in
  191 with the 21 July letter and is probably its coded part. That does not settle 689: "ce [?six] de [689]ars" would
  then refer to an earlier exchange, and stays a proposal.
- 1250 and the other stop groups: 194 adds 1260 (no gloss, at the end of the letter, after 1243).

## 6. What is left

- The report stays **decoded, not read**: 14 open groups have context proposals only; 1118 has a gloss ("tain") that
  does not yet give sense. Even with every proposal, 6, 711, 726 and 1118 give no usable value.
- No printed clear text was found. Remaining print leads: the 3 "Pareti" pages of HMC Polwarth V (library copy);
  SP 94 (Spain) for 1729 and the Newcastle papers (BL Add MS) for the originals Marchmont forwarded, which are
  manuscript, not print.
- 60887 L15 (880 glossed "plus"): compare with the clear 14 July text (60886).
- 194: 475 (favorable?), 433/438 and 389/387 need re-zooms; the 194 transcription is independent of Brackx's except
  where noted.
