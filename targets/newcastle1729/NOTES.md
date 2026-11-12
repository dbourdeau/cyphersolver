# newcastle1729: Port Sainte-Marie intelligence report in numerical code, 1729

Status: in progress

**Duplicate, found at the integration check (12 Nov 2026).** This target and [`../portstemarie1729/`](../portstemarie1729/) (page docs/portstemarie1729.html, catalogue 826, README row "complete", 134 of 141 groups) are the same document: Huntington mssBLA 191 p. 5 (HDL 61005), the report enclosed to Newcastle on 8 Aug 1729, in the same code, rebuilt from the same glossed sibling letters. One key, one entry: this folder must not get a page or a ledger row of its own; the checks below (the 4 Aug clear copy, mssBLA 194, the print search, the open-group proposals) belong to the portstemarie1729 target and are to be folded into it by the maintainer, with two consequences for its page. (a) Its 134 of 141 includes 15 groups filled from context and alphabetical order; by the strict read bar those are holes (116 groups valued directly = 0.823), so that page would read "read in part", not "complete". (b) It fills 1118 as "trouver" ("je lui ai fait trouver bon"); the mssBLA 194 gloss reads 1118 as "tain" (60893 L14, "reponse cer-tain", retouched ink), which this folder records and which contradicts that value. portstemarie1729 was not edited here (its page review is owed). Until then this folder stays `Status: in progress`; its own count here (121 of 141 firm, 0.858) is the strict one.

Catalogue #826. Huntington Library, William Blathwayt papers addenda, mssBLA 191 (HDL p15150coll7 id 61008), p. 5
(HDL page 61005): an undated report of about 140 dotted code groups from an unnamed British agent at Port
Sainte-Marie (El Puerto de Santa María), forwarded to the Duke of Newcastle on 8 Aug 1729. It has no decipherment on
the leaf. Contributed by johonn; the work was done by Claude Code under johonn's direction. **Unfinished work in
progress, saved on 28 Oct 2026 so a fresh session can continue.** Images are not committed: they are on
hdl.huntington.org (page ids below).

## Status

- **Key: partly recovered.** A 420-group code table (`codetable.tsv`) was rebuilt from the interlinear decipherments
  on five sibling letters in the same file (below), plus the glossed groups of three more items in the same code
  supplied by Michael Brackx (issue #189, `transcription/sibbrackx189.txt`). 1,127 glossed groups; 376 groups
  grade H, 44 grade M.
- **Text: decoded, not read.** Of the report's 141 groups, 121 have a firm value, 3 a doubtful one (974, 666, 122), 1 is a stop
  group, and 16 tokens (15 distinct groups) are open (88.7% with any value, 85.8% firm). The French in
  `decryption/report_61005_reading.txt` has 19 holes; `docs/_check_reading.py` finds 2 clean sentences of 9
  (hole rate 0.22), so it is not a reading, under the 95% bar.
- Outcome method (profile.json): key recovered based on adjacent plaintext; class not read; key partial; provenance
  contributed. Nothing is read or solved in the project's sense yet.
- Passages that already decode into sense: "l'[?obligation] que je vous ai, Milord, est bien grande pour votre lettre
  du [6]"; "j'y ai [?répondu] ce [?six] de [689]ars à la première adresse"; "Monsieur Kenne ne m'[65], mais il n'a
  aucun [?ordre] ..."; "je pouvois faire pour le mieux à l'accommodement"; "j'[?ig]nore [?vos] intentions et je serai
  inutile dans l'[?ig]norance. Mandés-moi donc quelque [?ordre] pour ma [?conduite]". The agent complains of being
  kept ignorant and asks for instructions; the names are Milord, Ken-ne (Keene, probably Benjamin Keene), Pa-ti-g-no
  (Patiño) and, in the siblings, Sta-no-pe (probably William Stanhope).

## Sources (HDL object -> pages)

| letter | HDL object | code pages used |
|---|---|---|
| mssBLA 191, 8 Aug 1729 (the target) | 61008 | p. 5 = 61005 (report) |
| mssBLA 187, 23 June 1729 (deciphered 19 July) | 60966 | 60963 |
| mssBLA 188, copies of 3 letters, 29 June 1729 | 60924 | 60917, 60918 (left leaf), 60919, 60920 |
| letter of 14 July 1729 | 60892 | 60887 (extracts); 60886 is the clear text of the same letter |
| letter of 4 Aug 1729 (enclosure "not sent") | 60914 | 60907, 60908, 60909 |
| mssBLA 194, 1729, undated (code letter with decipherment) | 60898 | 60893, 60894 (`beling/transcription/sib194_*.txt`) |

Images: `https://hdl.huntington.org/iiif/2/p15150coll7:<page id>/full/3000,/0/default.jpg` (wider than about 3000 px is
refused); region crops `.../pct:x,y,w,h/1800,/0/default.jpg`. Page lists:
`.../dmwebservices/index.php?q=dmGetCompoundObjectInfo/p15150coll7/<object id>/json`.

## Cipher type and key hypotheses

Numerical nomenclator of syllables and words, groups of 1 to 4 digits separated by dots, about 1 to 1370. It is
**roughly alphabetical**: syllables first, then words, per letter. Test (`slotsearch.py`): 273 of 330 adjacent
firm entries are in alphabetical order (82.7%) against 50.1% for shuffled orders, 20 sd above chance; the 57 breaks
are block restarts. Evidence from `codetable.tsv`:
208 comme, 217 concert, 224 confidence, 238 consideration, 242 continuation, 256 correspondance; 119 bi, 123 br;
S block 1013 s, 1014 sa, 1017 se, 1018 ser, 1020 si, 1022 so, 1032 su, 1033 sur, then words 1038 sçavoi, 1041 secours
... 1097 succède; numerals 8 vingt, 11 cinquante, 16 cent, 17 mille, 1206 deux, 1207 trois, 1209 cinq, 1211 sept,
1212 huit, 1213 neuf. The T block is not strictly ordered (1114 tout, then 1121 tache). Word division is by the
copyist's syllable hyphens. Unglossed "stop" groups (kept as `_`): 1233, 1240, 1243, 1250, 1252, 1255, 1261, 1268,
1290, 1324 (1370 doubtful); the report has one, 1250, which falls where a sentence ends ("à la première adresse.").

Best mapping: `codetable.tsv`. Names and numbers settled by the clean 4 Aug copy: 737 monsieur, 647 Ken, 756 ne,
822 Pa, 1109 ti, 506 g, 758 no (Pa-ti-g-no), 1028 Sta, 758 no, 825 pe, 697 665 941 270 mi-lo-r-d. Slot candidates for
open groups (bracketed by `slots.py`, all [?]): 285 do, 1152 vos, 1210 six, 222 conduite, 805 obligation, 816 ordre,
585 ig (ignore, ignorance), 689 m (m-ar-s), 122 bon. Homophones and variants seen: 735 and 737 both "monsieur"
(different copyists' hands, kept as two groups), 945 / 947 ri (945 also glossed re/ra), 1013 s, 289 du (one gloss
"Don"), 594 is (once "oit"), 1200 x (once "ze").

## Tried and ruled out (do not repeat)

- Aligning the 23 June page (60963) glosses to groups by position: the copyist's glosses are not under their groups
  and several words sit under one group. Every pair from that page is marked `?`; use it only as a check.
- 1152 = "traite" (from 60963): its slot (between vo 1150 and vous 1154) contradicts it; dropped, now [?vos].
- 1018 = "fer": the clean copies write "ser" (ser-ai, ser-oit, "je serai inutile"); table has ser.
- Merging 735 and 737: both read "monsieur" but the digits are different in two hands; kept apart.
- Reading 1210 and 6 as months or days without checking: 1210 sits between cinq and sept (so "six"); 689 + ar + s spells
  "mars", which does not fit a July date (the cover letter is 8 Aug): unresolved, see Open questions.
- Promoting the slot candidates to values: the slot lists (`decryption/slot_candidates.txt`) fit the proposals
  (vos at 1152, conduite at 222, comte/compte at 214, ordre at 805/816, bon at 122) but also many other words, so
  they stay [?]. A slot search that ignores the lexicon's j = i, v = u folding returns empty lists (fixed).
- `docs/_validate.py`: could not run here (Gutenberg unreachable); not a failure of the reading.
- Clear pages: the 21 July letter (61003-61004, trade, galleons, Patiño) and the clear text of 14 July (60886) do not
  contain the report; 60886 only repeats the 14 July extracts.

## Scripts and outputs (all in this folder)

| file | what it does |
|---|---|
| `transcription/report_61005.txt`, `report_61005_tokens.txt` | the report, 13 lines, 141 groups, with `?` marks / one token per group |
| `transcription/sib*.txt` | glossed code passages of the siblings, one passage per line, `group=value`; `?` doubtful, `{..}` struck, `_` no gloss |
| `build_table.py` | builds `codetable.tsv` (group, value, grade H/M, sources, count, other values) from `sib*.txt` |
| `decode.py` | applies the table to the report: `decryption/report_61005_decode.txt` (grouped), `report_61005_raw.txt` (word stream with [n] holes) |
| `decryption/report_61005_reading.txt` | the French reading, hand-made from the raw stream, holes in place |
| `reading.py` | checks that reading against the raw stream between holes (consonant skeletons) |
| `slots.py`, `decryption/open_groups_slots.txt` | brackets each open group between its nearest table neighbours |
| `slotsearch.py`, `decryption/slot_candidates.txt` | order test of the alphabetical hypothesis (82.7% vs 50.1% shuffled) and, per open group, the commonest French words that sort in its slot (v = u, j = i); slots, not readings |
| `validation.tsv` | token/reading pairs for `docs/_validate.py` (firm values only); test not yet run |
| `profile.json` | the profile (valid); `WORKLOG.md` the step-by-step log |

## Issue #189 (Michael Brackx), taken in 29 Oct 2026

Brackx's independent pass on p. 5 agrees with the transcription of the report. From his gist
(be7b2e6bf036ae898b5982936f5b32a6, rev 43cbfc4a, CC BY 4.0, credit Michael Brackx):

- three more items in the same code with interlinear decipherments, not used before: mssBLA 185 (Jan 1728, HDL 61081),
  194 (1729, HDL 60893-94) and 179 (Abbé G. B. Pareti, 7 June 1725, HDL 61122). Their glossed groups are entered in
  `transcription/sibbrackx189.txt` as he lists them (not re-transcribed here from the images). They give the report
  84 après, 65 aime and 816 ordre, and 666 lu (now doubtful: 188 has eu).
- two digit corrections in the 188 glosses, from his full-resolution crops: 60919 L11 737 -> 937 (*Monsieur*) and
  60920 L02 383 -> 387, 1017 -> 1019 (*et ... répon-se*). These give 937 and 1019 their values. Not re-checked on
  the images here.
- 122 bon and 1250 (full stop) were already in the table; 974 is glossed répondu on 60907 and répon(-se) on 60920.
- 65 avoit on 188 HDL 60918, which he also reports, is not in `sib188_60918.txt` and was not entered. He has since
  (2 Nov 2026, issue #189) withdrawn it: the group is on line 2, "Roy ge or ge premier [avoit] promis sur gi", and
  `sib188_60918.txt` already has it as 69 = avoit, which follows 68 avoit in the table's order; 65 is aime (194). So
  65 = aime stands and 69 = avoit stands. Not re-checked on the images here.

L05-L07 now give "comme je [285]is agir après le départ du [214], car Monsieur Kenne m'aime, mais il n'a aucun ordre
des se[711]s pour moi, Monsieur, dans l'affaire passée". Context proposals (805 obligation, 1210 six, 585 ig, 1152 vos,
222 conduite, 285 do) stay in the list above and in `decryption/open_groups_slots.txt`, not in the reading.

## Sibling pages read and a held-out check, 11 Nov 2026 (Andrew Beling, `beling/`)

Contributed by Andrew Beling with AI agents. Details in `beling/README.md`; the plan was written first in
`beling/PREREG.md`. [V] = checked on the image or in output, [I] = inference.

- The unread pages (60915, 60916, 60921, 60922, 60903-60906, 60910-60912, 60961, 60962, 60964) carry no new glossed
  code [V] (`beling/transcription/pages_survey.tsv`). 60916's code strip is the edge of 60917. None of the 15 open
  groups occurs in the five transcribed siblings (but see round 2: 1118 in mssBLA 194).
- **60903-60904 is the clear copy of the coded 4 Aug letter**: the passages coded on 60907-60908 are written out in
  square brackets [V] (`beling/transcription/clear_4aug_brackets.tsv`).
- Held-out check (pre-registered): the table rebuilt without the 4 Aug glosses, aligned to that clear copy, matches
  158 of 170 tokens (0.929); 200 shuffled tables best 0.171, margin 0.759: pass [V]. The full table: 205/214.
- Table values the clear copy settles [V], none in the report: 701 mo and 594 is ("j'aimois"), 191 c'est (60907 L19),
  791 ois ("faisois"), 869 perdu, 880 plustot, 829 pl, 169 com, 900 pris. 12 = a stands (60917 L14, a clear 2) [V].
  974 stands alone for "répondu" on 60907 L05, as in the report's "j'y ai [974] ce" [V there, I in the report].
- Dating: 60916 names Cesnok's letter "of the 5. of May", and 60917 L05 answers "votre lettre du cinq ma-y" [V];
  the report's "votre lettre du [6]" follows that style [I].
- Open groups, value-finding only, all [I] (`beling/results/open_group_values.md`): strong 585 ig, 1152 vos, 285 do,
  1210 six (1206-1213 run deux to neuf without a break); good 222 conduite, 805 obligation; fair 689 m (a second m,
  like the two l and l' groups), 1052 servi(ce), 836 pr ("à l'accommodement près"), 214 comte; weak 726 (the leaf
  reads 726 [V], the sense wants 926 que), 460, 1118 (see round 2); open 711, 6. Nothing is promoted; the report
  stays decoded, not read.
- Round 2 (plan in `beling/PREREG_round2.md`, inputs frozen first):
  - Print search: no clear text of the report or of any coded passage found. HMC *Polwarth* (Marchmont's papers)
    vols I-IV stop in 1725; vol. V (1725-80) searched inside on HathiTrust has no hit for "Port St. Mary", "cipher" or
    "Cadiz" (3 for "Pareti") [V]; Coxe's *Kings of Spain* and *Walpole* have nothing [V]. The covering letters from
    "Cesnok" are Marchmont's; his note of 8 Aug 1729 (61001) says the two letters he forwarded were of 14 and 21 July
    [V]. [I] The report is probably the coded part of the 21 July letter; the correspondent may be the Abbé Pareti.
  - mssBLA 194 (60893-60894), a code letter with full interlinear decipherment, transcribed in full
    (`beling/transcription/sib194_*.txt`). The table without any 194 gloss matches 89 of 93 firm 194 glosses
    (0.957; 200 shuffled tables best 0.065; pass) [V].
  - **1118 is glossed "tain"** in 194 (60893 L14, "974 163 1118" = "reponse cer-tain"; gloss retouched in darker
    ink) [V]: the only glossed occurrence of an open group. It was seen before the round-2 plan was written, so it is
    an observation, not a test. In the report it gives "je lui ai fait [tain] bon [?servi]ce", which does not read;
    "tant" is the nearest sense [I, weak].
  - 60917 L02 and L17 read **369** (e), not 869 [V, full-resolution crops]: the first figure has this hand's
    flat-topped 3, not its two-loop 8 (870, 1268 on the same lines). 869 = perdu is glossed in 194 too. 60917 L16
    "880" reads **830** (plus, "plus-ie-u-r-s") [V].
  - 60909 is the code part of a later letter dated 3 Nov 1729, on its own leaf, filed with the 4 Aug letter (whose
    catalogue entry counts 2 cipher pages, 60907-60908) [V leaf and catalogue; I placement]: it asks for 250 pounds,
    a bill drawn three months before having come back unaccepted, and the 4 Aug letter had asked on whom to draw.
    No letter of that date is in the Huntington file [V].
  - `beling/results/full_table.tsv`: the full construction, one row per group (439) with every gloss and
    clear-copy attestation and a conflict flag (20 rows); `codetable.tsv` is not changed.

## Integration check (12 Nov 2026)

- Re-run: both hash lists check; `check_4aug.py` 158 of 170 (0.9294, best shuffled 0.1706, margin 0.7588), `check_194.py`
  89 of 93 (0.957, best shuffled 0.0645), `full_table.py` (439 groups, 20 conflicts) and `open_groups.py` give the
  committed outputs. My own re-implementation of the 194 check (table built from every `sib*.txt` except the
  L194h60893 gloss lines, compared with the 194 transcription) gives 91 of 97 (0.938, 17 groups not in the table):
  same picture.
- These two checks show that the table agrees with a clear copy and with glosses on a letter it was not built from;
  they do not read the report. Huntington images were not fetched at the integration check: the transcriptions were not
  compared with the images.
- Order of events (checks pre-registered, inputs hashed first) is by the contributor's record. The 1118 = "tain" gloss is
  an observation, not a test (the gloss was seen before the round-2 plan was written).
- See the Duplicate note at the top: portstemarie1729 is the same document.

## Remaining gaps

- code groups 805, 6, 1210, 689, 460, 285, 214, 711, 1118, 1052, 726, 836, 585, 1152, 222 (16 tokens; 84, 65, 816, 937 and 1019 were filled from issue #189) - blocker: open-codes; only 1118 occurs elsewhere (mssBLA 194, glossed "tain", which does not give sense in the report); the unread sibling pages have no new code and no printed clear text was found (11 Nov 2026, `beling/`); slot-and-context proposals in `beling/results/open_group_values.md`, all [?]
- the 3 doubtful values 974 (répon-: répondu/répondez/réponse), 666 (lu/eu) and 122 (bon?) - blocker: open-codes
- the English translation of the reading is not written yet

## Escalation

- [x] siblings: five letters of the same file transcribed (187, 188, 14 July, 4 Aug); the remaining pages (188's 60915-60916, 60921-60922; 4 Aug 60903-60906, 60910-60912; 187's 60961-60962, 60964) read 11 Nov 2026: no new code; 60903-60904 is the clear copy of the 4 Aug code, used as a held-out check of the table (`beling/`)
- [x] clear-pages: 21 July letter and 14 July clear text checked; nothing from the report
- [n/a] known-keys: no other key of this series is known; the siblings are the key source
- [x] print: searched 11 Nov 2026 (`beling/README.md` section 5): HMC Polwarth I-V, Coxe (Kings of Spain, Walpole), TNA and BL catalogues; no clear text of the report or of any coded passage. Left: the 3 "Pareti" pages of HMC Polwarth V (search-only online), and the forwarded originals in SP 94 / the Newcastle papers (manuscript)
- [x] key-rebuild: alphabetical bracketing done (`slots.py`); no annealing run
- [x] retry: decode re-run after every table change; reading re-checked with `reading.py`

## Next steps (ranked)

1. Sanity check the saved state: `cd targets/newcastle1729 && python3 build_table.py && python3 decode.py && python3 reading.py`
   (expect: 121 firm, 3 doubtful, 16 open; "reading consistent with the table").
2. Re-zoom the doubtful digits on the scans (list below), then fix `transcription/*.txt` and re-run step 1.
3. Compare the clear 14 July text (HDL 60886) with the extracts on 60887 line by line, to promote glosses to firm.
4. Done 11 Nov 2026 (`beling/`): no new code on the unread pages.
5. Done 11 Nov 2026 (`beling/`): nothing printed found; next, HMC Polwarth V in a library (index: Pareti) and SP 94 for 1729.
6. Run the validation where the corpora are reachable: `PYTHONUTF8=1 python3 docs/_validate.py newcastle1729 --write`.
7. Write the English translation (`decryption/report_61005_en.txt`), add it to `outcome.texts[0].translation`, add the
   `decode_updates/queue.json` entry (report not on DECODE: `new_records`, key file `codetable.tsv`), then
   `PYTHONUTF8=1 python3 docs/_check_profile.py newcastle1729`, `python3 docs/_check_reading.py newcastle1729`,
   `python3 docs/_check_terms.py newcastle1729`. The maintainer does the docs/ write-up on merge.

Rules for this contribution: stage by explicit path; commit to branch `catalogue-826`; push only to origin (johonn's
fork); never to upstream or main; do not edit generated files in `docs/` or run the site rebuild; no PR from the
session (johonn opens it); mark unconfirmed values `[?word]`.

## Open questions and things to check against the scans

- Report L01 group 3 (386: first digit overwritten), L02 group 10 (1201: on a blot), L03 group 2 (163 or 103).
- 4 Aug p. 7 (60909): L03 `491` (r? for 941), L09 `045` (res? for 945), L13 `1015` (sans? for 1016), L04 `664` (ll).
- 4 Aug p. 5 (60907): L13 gloss "ai-mo-oit" under 26, 701, 594; L19 first group 191 or 791.
- 188 (60917): 596 on line 1 (overwritten); 1200 glossed "ze" on L10 (x elsewhere); 289 glossed "Don" on L12.
- Is the report earlier than July? 689 + ar + s spells "mars", but the covering letter is 8 Aug and the siblings
  are June to August. The date after "du [6]" and "ce [?six] de [689]ars" decides it.
- 945 vs 947: which is "ri" and which "re/ra" (adresse, mariage); the copyists' 5 and 7 are easily confused.
- 6 (single digit, numeral block): six? the date of the letter answered.
- [settled 11 Nov 2026] 60917 L02 and L17 read 369, not 869 (full-resolution crops; `beling/results/table_notes.md`).
  Proposed transcription fix: sib188_60917.txt L02 and L17 869=e -> 369=e; L16 880=plus -> 830=plus.
- [settled 11 Nov 2026, I] 60909 is the code part of a letter of 3 Nov 1729 on its own leaf, filed with the 4 Aug letter.
- 1118 is glossed "tain" in mssBLA 194 (L14, "cer-tain"; retouched): what does it mean in the report's "fait [1118] bon"?
- 60887 L15: a clear 880 glossed "plus"; 880 = plustot in the 4 Aug clear copy. Check against the clear 14 July text 60886.

## Checker output (docs/_check_writeup.py newcastle1729, 28 Oct 2026)

This work is unfinished, so a failing result is expected. The write-up surfaces in docs/ are left to the maintainer.

```
newcastle1729: write-up surfaces
  [MISS] docs/newcastle1729.html exists
  [MISS] PAGES entry in docs/_build_site.py (st=None)
  [MISS] IMAGES entry in docs/_build_site.py (None is allowed, a lead figure is better)
  [MISS] docs/_dates.json has the page (created by the first build)
  [MISS] README.md results row links https://dbourdeau.github.io/cyphersolver/newcastle1729.html
  [MISS] index.html Recent findings has a <li> linking the page
  [warn] writeups.html lists the page (regenerated by the build)
  [ok  ] catalogue.json no longer lists the target (read/resolved entries are removed, see the skill)
  [ok  ] newcastle1729/profile.json exists and is valid (/profile skill; python docs/_check_profile.py newcastle1729)
  [MISS] a correspondent portrait in docs/_portraits.json (python docs/_add_portrait.py), or the reason there is none in docs/_explore_skip.json "portrait"
  [MISS] no snip of the cipher on the page: crop one from the scans (IMAGES entry or a figure), or record why none can be had in docs/_explore_skip.json "snip"
  [MISS] a "watch it decipher" file docs/reveal/newcastle1729.json, or the reason there is none in docs/_explore_skip.json "reveal"
  [MISS] docs/keys.json links the key that read newcastle1729, or says why not in "unlinked" (its outcome or steps involve a key)
  [warn] docs/atlas.json maps the letters of newcastle1729 (1 documents have a route): give each document "places": {"from", "to"} with gazetteer names (tools/atlas_places.py) and rebuild
  result: INCOMPLETE - see MISS lines
```

Every MISS is a docs/ surface (page, manifest, README row, portrait, reveal, keys.json). The profile is valid. The
target itself is unfinished: key partly recovered, text decoded but not read.
