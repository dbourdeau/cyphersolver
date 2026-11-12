# Port Sainte-Marie spy report, c. July 1729 (catalogue 826)

Status: read in part (116 of 141 groups directly valued, 0.823; 18 more filled from the sense, 7 without a value), key rebuilt from the glossed siblings in the same file. Recounted strictly on 12 Nov 2026; earlier "134 of 141, 95%, read" counted the 18 context-filled groups as read.

Huntington Library, William Blathwayt papers addenda, mssBLA 191, p. 5 (HDL p15150coll7 id 61005;
compound object 61008). Enclosure to a covering letter to the Duke of Newcastle of 8 Aug 1729. French,
numerical one-part code (groups 1-1370), alphabetical: syllables, words and names in one sorted list
(18 a, 278 de, 580 je, 581 ie, 585 ig, 1154 vous ...). 1240-1370 unglossed separators/nulls.

## Method

1. Transcribed p. 5 from the HDL image (`ct_p5.txt`, 141 groups, 13 lines).
2. Transcribed the glossed siblings in the same series (`pairs_A.tsv`, `pairs_B.tsv`, running texts in
   `pairs_*_text.md`): mssBLA 187 p. 3 (HDL 60963, cipher of the letter of 23 June, deciphered 19 July 1729),
   the 29 June letter (60917-60920), the 14 July letter (60887) and the letters on 60907-60909
   (incl. 3 Nov 1729). 1,055 glossed pairs in the two files (first reported as 942; recounted 12 Nov 2026), 364 distinct codes.
3. `decode.py` applied the table: 116/141 groups valued directly (strict count; `decode.py` now prints the inferred ones as `[?word]`).
4. Filled 15 more codes (18 tokens) from context plus the alphabetical order of the code (`pairs_zinf.tsv`); under the read bar (README Conventions) a value given by the sense or by position alone is a hole, so these are not counted:
   585 ig (ig-no-re, ig-no-ra-n-ce), 275 dans, 222 conduite, 816 ordre, 666 lu, 1118 trouver, 689 m (de m-ar-s),
   460 fe (fe-re-z), 84 apres, 1152 vos, 1210 six (between 1209 cinq and 1211 sept), 805 obligation,
   285 di, 711 maine (se-maine-s), 1250 separator.

## Reading (`texts/p5_reading.md`, strict marking)

L'[?obligation] que je vous ai, Milord, est bien grande pour votre lettre du [6]. J'y ai répondu ce [?six] de [?m]ars
à la première adresse. Quand vous me [?fe]rez sçavoir, comme je [?di]s, [il s']agit [?après] le départ du [274], car
Monsieur Keene ne m'avoit [rien dit], mais il [254] a aucun [?ordre] des [?maine]s pour moi [937] [?dans] l'affaire
passée. Je [?lu]i ai fait [?trouver / ?tain] bon [1052] ce, sans qu'il m'ait jamais dit ce [726] je pouvois faire pour le
mieux à l'accommodement. [836]es je [?ig]nore [?vos] intentions, et je serai inutile [?dans] l'[?ig]norance. Mandez-moi
donc quelque [?ordre] pour ma [?conduite] ...

English (words in [?...] are filled from the sense only and count as unread): The [?obligation] I owe you, my Lord, is
very great for your letter of the [?]. I answered it this [?sixth] of [?M]arch at the first address. When you let me know,
as I say, it concerns [what follows] [?after] the departure of [?], for Mr Keene had [told] me nothing, and there has been no
order for me for [?weeks] [?] in the past affair. I [?got him] to [?find / ?"tain"] good [?] this, without his ever telling
me what I could do for the best towards the accommodation. [?] I do not know your intentions, and I shall be useless in [?]
ignorance. Send me then some [?order] for my [?conduct] ...

The agent complains that Benjamin Keene (British envoy in Madrid) leaves him without orders during the
accommodation (the Treaty of Seville talks) and asks Newcastle for instructions. Same agent and code as the
29 June letter, which asks for a new cipher, an address and money.

## Group 1118: two values on record

- Here 1118 was filled as "trouver" from the sense ("je lui ai fait trouver bon"), with no gloss behind it; the alphabetical
  bracketing does not help (neighbours 1114 tout, 1121 tache; a tr- word is no better placed than a ta- word).
- `../newcastle1729/` (the duplicate folder, Beling's checks) records the one glossed occurrence of 1118 anywhere in the file:
  mssBLA 194 (HDL 60893, line 14), "974 163 1118" glossed "reponse cer-tain", the gloss "tain" in darker ink written over an
  earlier one and the first figure of 1118 retouched in the same ink (`../newcastle1729/beling/transcription/sib194_60893.txt`).
  Checked here on the HDL image (12 Nov 2026): the last line of 60893 carries a gloss ending "-tain" under 163 1118, with the
  overwriting visible; I did not settle what stood under it before.
- "tain" has a gloss behind it; "trouver" has the sense only. But "tain" does not make "fait [1118] bon" read, and the
  retouching leaves open that the clerk corrected the gloss. Neither is adopted: 1118 is a hole, marked `[?trouver / ?tain]`
  in the reading. The files support "tain" better as a value of the code, "trouver" better as the word of this sentence; the
  conflict is unresolved (the same group may even be misread in the report).

## Other evidence in the duplicate folder (not adopted here)

`../newcastle1729/` rebuilt a table of 420 groups from the same five siblings plus glossed groups of mssBLA 185, 194 and 179
supplied by Michael Brackx (issue #189, not re-checked on the images there), and a 4 Aug clear copy (60903-60904) used as a
held-out check (158 of 170 tokens, 0.929) and mssBLA 194 (89 of 93, 0.957). It gives glosses for 84 apres and 816 ordre (mssBLA 185, 179, Brackx's
transcription) and, by reading two digits of the 188 lines differently (275 dans where this folder has 255; 937 monsieur
where this folder has 737, 60919 L11), for 275 and 937; 666 lu is blotted on 60918 L18 and doubtful there. On the Huntington
images (60917 L4, 60919 L11, seen 12 Nov 2026) those two digits cannot be settled at this resolution. It keeps 805, 6, 1210, 689, 460, 285, 711, 1152, 222, 585, 1052, 726, 836 open ("context only"). Those
glosses are not in this folder's pairs_*.tsv, so they are not counted here. If the digits of 275 (2 tokens) and 937 (1 token)
are as newcastle1729 reads them, 119 of 141 would be valued (0.844); folding in 84, 816 and 666 as well would give about 122
(0.865): not the bar either way.

## Remaining gaps

- 18 tokens (15 codes) filled from context only, counted as holes: 805 obligation, 585 ig (2), 275 dans (2), 222 conduite, 816 ordre (2), 666 lu, 1118 (trouver or tain, see above), 689 m, 460 fe, 84 apres, 1152 vos, 1210 six, 285 di, 711 maine, and 1250 as separator - blocker: open-codes; none is glossed in the siblings transcribed here; the duplicate folder finds glosses for 84 and 816 in other letters (not re-checked on the images), for 275 and 666 by reading a digit differently or from a blotted group, and none for the others
- 7 groups with no value: 6 (a number, date of Newcastle's letter), 274 (a name or d-word after "départ du"), 254, 937, 1052, 726, 836 - blocker: open-codes; not glossed in any sibling here, alphabetical neighbours narrow them only to a letter range (the duplicate folder reads the digits of 60919 L11 as 937 = monsieur, which this folder reads 737; not settled on the image), mssBLA 184 and 186 are unglossed

## Escalation

- [x] siblings: all glossed letters in mssBLA 187-191 used here (60887, 60907-60909, 60917-60920, 60963); mssBLA 185, 194 and 179 are glossed too and are used in `../newcastle1729/` only
- [x] clear-pages: the 21 July clear letter and the 4 Aug clear copy (60903-60904, `../newcastle1729/`) checked; nothing from the report
- [x] known-keys: no other key of this series is known (not on DECODE); the siblings are the key source
- [x] print: none found, no printed edition; the duplicate folder searched HMC Polwarth, Coxe's Kings of Spain and Walpole and the TNA and BL catalogues, 11 Nov 2026
- [x] key-rebuild: alphabetical bracketing of every gap (`pairs_zinf.tsv`; `../newcastle1729/slots.py`); it gives the 18 context-filled tokens, which count as holes
- [x] retry: decode re-run on the strict count 12 Nov 2026 (116 of 141); retry possible if further Port Sainte-Marie letters are digitised (mssBLA 185-195 not all)

## Duplicate folder

`../newcastle1729/` (johonn's folder with Andrew Beling's checks, PR #448) covers the same document and key; it stays
`Status: in progress` and has no page. Its sibling checks are recorded there.

## Correction of 12 Nov 2026

Found while verifying PR #448: (1) the status "read, 134 of 141 (95%)" counted 18 tokens filled from the sense and the
alphabetical order; by the read bar those are holes: 116 of 141 = 0.823, read in part. (2) 1118 "trouver" conflicts with the
mssBLA 194 gloss "tain" (above). `decode.py`, `texts/p5_*`, `texts/key.md`, the profile, the page and the ledgers were changed
to the strict count; the credit is unchanged.

## Prior solution

None: catalogue says undeciphered; the leaf has no gloss (checked 28 Oct 2026).
