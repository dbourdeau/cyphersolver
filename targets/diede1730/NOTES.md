# diede1730: Hanoverian envoys Diede and Reck at Regensburg, 1730 (NLA Hannover, Hann. 9g Nr. 1687 and Hann. 92 Nr. 1149/1), key of the type A letter cipher

Status: read in part (key recovered from the chancery's plaintext and validated; Brice Dudout, 11 Nov 2026; Hann. 92 Nr. 1149/1 aufn 0004: 145 of the 160 measured groups read by the key, 12 restored, 3 unresolved; Hann. 9g Nr. 1687 read in part, about 3,600 of an estimated 6,000 type A groups transcribed, no word count).

Contributed by Brice Dudout (Europe chiffrée), with Claude Opus 5.5 agents. **Role: key reconstructed (credited as
transcription + verification), not a solution.** The key was learned from the chancery's own plaintext of 1730 (the clear
text of a postscript and the interlinear decipherments written at the time); much of what the key reads was therefore read in
1730 already. What is new: the key as a reusable table, validated on a held-out page that has no gloss, and a new source.

## Daniel's ids

- **Lead 1659** (Huldenberg and Regensburg, "NLA Hannover, Hann. 9g Nr. 1687, 1691"), closed 2 Nov 2026 as a duplicate of
  catalogue **598** ("same Hann. 9g Mecklenburg-commission series ... Caveat: Nr. 1687 and 1691 were not opened on a cipher
  page"). This target opens Nr. 1687. Two corrections to the lead: Nr. 1687 is dated 1730 (Relat. 9-25, January-March 1730),
  as the finding aid says, not 1735-37; and its cipher is **not** the system of `targets/mecklenburg1734` (WAINUT, #104:
  undivided runs of figures, a code). Nr. 1687 uses dotted groups of 2-4 digits, about one group per letter.
- **Lead 1658** (Diede, Hann. 9g Nr. 1424, 1491, 1673, 1676; catalogue only): Nr. 1687 holds Diede's Regensburg relations of
  1730, so it is where his cipher is found; we did not open 1424, 1491, 1673 or 1676.
- Hann. 92 Nr. 1149/1 is not in the catalogue or the leads: a **new source** (below).

## Documents

Niedersächsisches Landesarchiv, Abteilung Hannover (NLA HA). Images: Public Domain Mark, no login (Arcinsys,
`https://www.arcinsys-digitalisate.niedersachsen.de/nla_ha/hann._9g/nr._1687/m_ha_hann._9g_nr._1687_aufn_NNN.jpg`;
`.../nla_ha/hann._92/nr._1149--1/m_ha_hann._92_nr._1149_1_aufn_NNNN.jpg`). No images are included; pages are cited by
`aufn` number. Credit: "NLA Hannover, Hann. 9g Nr. 1687" / "NLA Hannover, Hann. 92 Nr. 1149/1".

| file / aufn | piece | role here |
|---|---|---|
| 9g 1687 / 060-065 | Relat. 16, Regensburg, Feb 1730, cipher without gloss (1,467 groups) | key training (cipher side) |
| 9g 1687 / 065R-068L | "P.S. ad Relat: Regensp: 16tam", clear text of the time, another hand (about 430 words) | key training (clear side) |
| 9g 1687 / 004, 025-031, 056-057 | Relat. 3, 8, 15 and the relation of 027-036, cipher with partial glosses of the time | transcribed; checks only |
| 9g 1687 / 033-036 | glossed runs | held-out set of measurement 1 (failed) |
| 92 1149/1 / 0003 | P.S. ad Relat. 1, Regensburg 2 Jan 1730, 5 cipher lines, full interlinear gloss | not used (declared context) |
| 92 1149/1 / 0004 | same P.S., about 24 lines / 242 groups, **no gloss** | held-out set of measurement 2 (validated); text |

## System and key (`key.tsv`, CC BY 4.0)

Homophonic substitution of German letters: groups of 2-4 digits (5-1497) separated by dots, written in lines inside clear
relations, about one group per letter, 3-6 homophones for the frequent letters (e = 63, 227, 293, 416, 1043, 1419...; n = 110,
205, 270, 464, 1125...), plus a few word or syllable codes (Chur Mayntz 216.123.53, Chur Cölln 270.333; 841 = ich is
probably one). The glosses of the time are written as continuous text under the line they translate, which is why early
line-by-line alignments failed. The key has 166 rows: 83 sure, 66 probable, 17 doubtful (doubtful rows never used in a
measurement). It was learned only from the 13 cipher/clear segments of Relat. 16 and its clear P.S. (EM letter alignment,
`frozen/1687/scripts/lalign2.py`, `frozen/1687/UNITS-PS16.tsv`) and frozen by SHA-256 before any held-out page was opened.

## Validation (`validation.txt`, `frozen/`): one failure, then one pass

1. **Measurement 1, Nr. 1687 aufn 033-036: FAILED.** Pre-registered (PREREG, PREREG-2/3/4): one Smith-Waterman alignment
   of the decode against the gloss of the time, characters, thresholds >= 0.85 and margin >= 0.30. Result 0.244 against 0.050
   for the best of 200 shuffled keys. The 160 groups are 24 separate runs and a single local alignment counts only the longest
   common stretch (about 40 letters): a flaw of the measure. Post hoc, run by run and without verdict value: 0.738 against
   0.412. The portion is spent.
2. **Measurement 2, Hann. 92 Nr. 1149/1 aufn 0004: VALIDATED.** The single re-test allowed for the unchanged key. Protocol
   and amendment hashed before the page was viewed; the 160 first groups transcribed without the key and hashed. Measure M5:
   dictionary coverage of the decode (lexicon of 1730 chancery prose from Nr. 1687 plus German Gutenberg texts, nothing from
   1149/1), thresholds calibrated beforehand on Nr. 1687 and hashed (coverage >= 0.60 and margin >= 0.30). Result 0.656
   against 0.325 for the best of 200 shuffled keys (mean 0.196), margin 0.331.

M5 is a dictionary-coverage measure, not the 0.85 character-agreement criterion: aufn 0004 has no gloss or clear twin to
compare with. It shows that the key turns an unseen page into German words far better than chance; it is not a measure of
character accuracy.

## Texts

`transcription.txt`, `decryption.txt`, `reading.md`, `translation.md`: Hann. 92 Nr. 1149/1 aufn 0004, groups 1-160.
Reading: "... dessen gute und vertrauliche Freundschaft es wohl im Churfürstlichen Collegio als auch im Evangelischen Corpore
wie alle Zeit, also vornehmlich anietzo von nicht geringer [...] ist, und es täglich Gelegen(heit) ..." It agrees word for word
with the gloss of the time on aufn 0003, which was not used.

Daniel's count on the 160 groups: **sure 106 / probable 39 / restored 12 / unresolved 3** (157 of 160 resolved = 98%; read by
the key alone 145 of 160 = 91%): read in part. Groups 161-242 of the same page are **unmeasured exploration** (raw decode in
`decryption.txt` and `reading.md`), not counted and not claimed.

## How much of Nr. 1687 is read

Nr. 1687 (252 images) holds type A cipher in Relat. 3 (aufn 004), Relat. 8 (025-026), the relation of aufn 027-036, Relat. 15 (056-057) and Relat. 16 (060-065) (about 3,600 groups,
all transcribed here in `frozen/1687/transcr/`) and in Relat. 17, 21 and 25 (aufn 119-123, 142-144, 158-159; about 240 lines,
roughly 2,400 groups by line count, not transcribed). Of the transcribed groups:
- Relat. 16 (1,467 groups) has its clear text of the time (the P.S., aufn 065R-068L): existing, the key's source.
- the other transcribed runs carry partial glosses of the time; we decoded only checks (056: "wie der graf von toring meldet
  so werden ihro churfurstl durchl in baiern nachste tagen einen der ministrorum nach mainz absenden...", 027, and 033-036).
- the frozen key gives a value to 94% of the transcribed groups (3,431 of 3,636), which is coverage, not reading.
No word-by-word count has been made on Nr. 1687, and roughly 40% of its type A cipher is not transcribed, so Nr. 1687 is
**read in part**, well under 95%. Relat. 17, 21 and 25 (almost without gloss) are the obvious next use of the key.
A second system in Nr. 1687, the Copenhagen letters of Schütz (aufn 150-153, 165-166: dotted 4-digit groups 2000-4100, dense
interlinear gloss), was not attacked.

## New source: Hann. 92 Nr. 1149/1 (pointer for leads 1658/1659)

NLA Hannover, Hann. 92 Nr. 1149/1, "Einzelne Relationen aus Regensburg 1730-1731" (605 images, Public Domain Mark): the
London copies (Deutsche Kanzlei) of the relations and postscripts of the same envoys to George II. All 605 images were
surveyed; cipher only in four pieces of 1730:
- **Type A** (this key): P.S. ad Relat. 1, 2 Jan 1730 (aufn 0003 glossed, 0004 not), Relatio 2, 5 Jan 1730 (0006-0008,
  decipherment in the margin), P.S. ad Relat. 14, Feb 1730 (0102-0103, partly glossed): about 975 groups, about 685 of them
  glossed. The frozen key reads aufn 0003 unchanged ("weil der ... bey dem ... übel gebrauch davon machen könte").
- **Type B**: a piece to the King of 3 Aug 1730 (0129-0132): 4-digit groups 1000-3400, not dotted, written continuously, about
  900 groups, with a pale interlinear gloss on most lines. A different system; inventory only, **not attacked**.
- P.S. ad Relat. 16 is not in 1149/1 (Nr. 1687 holds the only copy found).
Likely the same series and cipher, digitised, not opened by us: Hann. 92 Nr. 1146/2 (1728), 1146/3 (1729), 1149/2 (1731).

## Prior work

- The chancery's clear P.S. and interlinear decipherments of 1730 (credited `contemporary`, prior solution).
- Lead 1659's vetting (2 Nov 2026): nothing on DECODE, Cryptiana or Lasry's lists for Hanover, Huldenberg or Regensburg; no
  edition known. `targets/mecklenburg1734`: a different system; no key there to apply.
- No target, branch or PR for Nr. 1687, Nr. 1149/1, Diede or Regensburg 1730 in this repository (checked on main 6a94e2f0e,
  11 Nov 2026).

## Integration check (Daniel's session, 11 Nov 2026)

- `frozen/1149-1/scripts/m5.py` re-run on `frozen/1687/KEY.tsv` (SHA-256 matches `KEY.sha256`) and `H-0004.codes`:
  coverage 0.656, controls mean 0.196, best 0.325, margin 0.331. The reported result reproduces exactly.
- `decode1687.py` (added here) applies `key.tsv` (sure + probable rows) to every transcribed type A run of Nr. 1687 and
  writes `decryption-1687.txt`: 3,630 groups parsed, 3,426 with a value (the contributor counted 3,431 of 3,636; the
  small difference is parsing). Spot check on the unglossed lines R7-R16 of aufn 056: "nechst tagen einen der ministrorum
  nach mainz absenden umb daselbst unter andern in der mecklenburgischen sache", consistent with the gloss over R1-R6.
  This file is a raw decode, not a reading.
- Escalation was stopped by access: the Arcinsys image host and Wikimedia Commons were both refused by this session's
  network policy, so Relat. 17, 21, 25 could not be transcribed, no crop of the cipher could be made, and no portrait
  could be searched.

## Remaining gaps
- Nr. 1687 Relat. 17, 21, 25 (aufn 119-123, 142-144, 158-159; roughly 2,400 groups) not transcribed - blocker: needs-physical-access; the Arcinsys images were refused by the integrating session's network policy; the frozen key applies once they are transcribed
- Nr. 1149/1 aufn 0006-0008 and 0102-0103 not transcribed; aufn 0004 groups 161-242 only raw exploration - blocker: needs-physical-access; groups 161-242 need a re-check of the transcription on the image; Arcinsys unreachable from the integrating session
- transcribed runs of Nr. 1687 (aufn 004, 025-036, 056-057) decoded but not read word by word - blocker: needs-physical-access; doubtful digits and the partial glosses must be settled on the images; Arcinsys unreachable from the integrating session
- 17 doubtful key rows; word codes 281, 26, 279 (Nr. 1149/1 aufn 0003) and others - blocker: open-codes; too few occurrences in the transcribed material to fix them

Other ciphers met here are separate systems, not gaps of this key (one key, one entry): the type B 4-digit system of
Nr. 1149/1 aufn 0129-0132 and the Copenhagen letters of Schütz in Nr. 1687 (aufn 150-153, 165-166). They are recorded in
the lead notes (leads 1658, 1659) for a later target.

## Escalation
- [x] siblings: all 605 images of Hann. 92 Nr. 1149/1 surveyed (contributor); type A in aufn 0003-0004, 0006-0008, 0102-0103. Hann. 92 Nr. 1146/2, 1146/3, 1149/2 and Hann. 9g Nr. 1424, 1491, 1673, 1676, 1691 not opened (Arcinsys unreachable from the integrating session); noted on the leads
- [x] clear-pages: the clear P.S. ad Relat. 16 (aufn 065R-068L) is the key's source; aufn 0003 gloss checked against the decode
- [x] known-keys: targets/mecklenburg1734 (WAINUT, #104) is a different system (a code); no other Hanoverian key of 1730 in the repository
- [x] print: no edition known; nothing on DECODE, Cryptiana or Lasry's lists (lead 1659 vetting, 2 Nov 2026)
- [x] key-rebuild: key rebuilt by EM alignment from the clear P.S. (166 rows), frozen and validated on aufn 0004
- [x] retry: the frozen key re-applied to all 3,630 transcribed groups of Nr. 1687 at integration (decryption-1687.txt); further reading needs the images

## Limits

- One reader (an agent) per transcription, on full-resolution images; no human palaeographic check.
- Key from one long clear/cipher pair; 17 doubtful rows; word codes 281, 26, 279 (aufn 0003) not in the table.
- Measurement 2 is a dictionary measure on 160 groups; the lexicon includes the gloss of the spent measurement 1 (declared).
- Working files in `frozen/` are in French and kept as hashed; three local file paths were redacted for publication
  (PREREG-1730.md, PREREG.sha256 image lines, mklex.py), so those copies do not match their recorded hashes.
