# claiborne1806: William C. C. Claiborne's State Department code, 1805-1806 ("key not found")

Status: in progress (integration check of PR #564, 14 Nov 2026: the code is the State Department code WE028 with its blocks of 100 reversed, the same copy order as Anthony Morris's in `../morris1813`; see Integration check below. Gaps are workable: images of 0226 to finish, 1077, the LoC letters, the Founders notes behind a bot check, and the one-key-one-entry decision with morris1813. No page yet.)

Contributor's status line, kept: read (existing: Wagner's decipherments of the time); key partial (261 of about 1 600 values). Contributed by Brice Dudout, Europe chiffree, with a Claude Opus 5.5 agent (27 Oct 2026). The texts are EXISTING (Wagner's decipherments); what is new is the structure of the code and 261 of about 1 600 values. Not in catalogue.json, leads.json or targets (checked 12 Nov 2026: no hit for Claiborne).

## Documents
National Archives, RG 59, Territorial Papers, Orleans, microfilm T260: roll 7 images 0224-0226 (Claiborne to Madison, 24 Oct 1805, about 270 groups), roll 8 image 0045 (13 Jan 1806, about 75) and image 0409 (25 Nov 1806, about 45). The two letters of 18-19 Nov 1806 are in the Library of Congress (Burr Conspiracy Collection), not accessible: not used. Roll 9 (1807-08, 437 images) was scanned in contact sheets: no other ciphered page. Public domain; no image is reproduced here.

## System and key
Code of about 1 600 numbers, one-and-a-half-part type: vocabulary (letters, syllables, words, a few names) in alphabetical order by segments of variable length, the segments in permuted order (start of a segment often at x01 = a single letter: 1 a, 51 o, 101 i, 201 b, 301 g ...). I/J and U/V merged. Final hook (L) = -s, triangle = -ed. The structure matches the 1 700-element State Department codes described by Weber (Masked Dispatches, pp. 66-67). Segment map in frozen/RESULTATS-C01.md section 3. key.tsv = number, value, S/P/D, attestations.

## Validation
See validation.txt: 96 % alphabetical order in pages of 50 (controls <= 57 %), and 22 of 23 held-out groups on the 25 Nov 1806 letter fall at their place.

## Prior art
PJM-SS (Madison, Secretary of State series) lists the code as "State Department code; key not found" for five despatches (24 Oct 1805; 13 Jan, 18, 19 and 25 Nov 1806). No reconstruction published that we found; Weber 1979 (restricted lending) not consulted, Weber's Masked Dispatches does not cite Claiborne.

## Integration check (14 Nov 2026, PR #564)

Done on the integration branch with scripts of our own (`we028_check.py` in this folder; the order and held-out checks in the
session scratchpad). The contributor's files are unchanged except this section, the status line, `profile.json`, and the two
added files `we028_check.py` and `transcription_corrections.tsv`.

**The code is WE028 with reversed blocks.** The contributor's key was compared with every State Department key in the
repository. King's code (`../king1797`, the = 769), the Pinckney/legation codes (`../erving1807aug`, `../legation1788`,
`../pinckney1793`), the JQA table read directly (`../jqa`, WE028, the = 1385), Armstrong's 972 code and Mountflorence's code
give no agreement. Under the block reversal found for Anthony Morris's copy (`../morris1813`: Morris/Claiborne 100*i + r =
WE028 100*(15-i) + r), Beling's transcription of the surviving WE028 copy (NARA M97 roll 13 frames 1056-1057,
`../morris1813/beling/key/codebook_M97_13_transcription.csv`) gives the contributor's value for 223 of the 261 numbers
(I/J and U/V merged): sure 85 of 89, probable 125 of 145, doubtful 13 of 27. The four sure values that differ are spellings
(101 I.J., 223 ben, 981 are/arc conflict in the sheet, 1582 missisipi). The JQA table under the same reversal gives 169 of 237
against at most 63 for 1,000 random block orders. The 1805 code sent by Wagner to Claiborne is therefore WE028 in the
reversed-block copy order. The Madison editors' "key not found" is explained by the reversal. The contributor's
"alphabetical segments of variable length, permuted" is that table seen through the reversal: one-and-a-half-part blocks
of 100.

**Key coverage, counted.** `python targets/claiborne1806/we028_check.py` applies WE028 reversed unchanged to the 328 aligned
words. 294 give Wagner's word under a mechanical rule (89.6%; groups 478 of 550): 227 of 250 in the letter of 24 Oct 1805,
40 of 51 on 13 Jan 1806, 27 of 27 on 25 Nov 1806. Of the 34 others, 23 fit by hand: Mobille x3 (mo-bil-e), frontier
(fro-n-ti-ers), attack (at-tact-k), defence (def-ence and 364 = a full stop), Mississippi x2 (the sheet's missisipi),
speedy (sp-e-dy), cannon (cant-non), been (ben), are (981, the sheet's two halves read are/arc), the numerals of 13 Jan 1806
(653 659 651 = 2 8 0, 657 651 = 6 0, four words), compliance (comply-ance), Col. (colon-el), orders (285 611 567 = the
order-s), and the re-split of "General Wilkinson" (308 | 484 152 149 1101 1351 = general | wi-l-ki-n-son) and "General
binding" (308 | 232 1101 743 301 = general | bi-n-din-g), four words. That re-split removes the contributor's doubtful 149,
232 and 484. 317 of 328 words (96.6%) are then reproduced by an external key used unchanged. Three words are encoder
slips where the code is right and the clerk erred: 611 order in "information", 235 bil for "the", and "John" encoded 101 51
(I-O). Three are 1077 = tra for tro- in troops (clerk, copy variant or a misread of the sheet). Five are unsettled on the
image or in the alignment: arrival, leather, the second Lakes, and "the collecting". The contributor's own key, counted
strictly (sure values only), covers 326 of 550 groups (59.3%; 24 Oct 1805 252/389, 13 Jan 1806 47/99, 25 Nov 1806 27/62)
and 202 of 328 words with every group sure (61.6%). The probable and doubtful values are holes in that count, and 15 of
them differ in substance from WE028 (e.g. 232 ne = bi, 484 ner = wi, 813 ger = r, 186 r = ro, 1116 d = nd, 1262 ins = notify).

**Reproduced.** Order test (own script on key.tsv): 96.4% of 197 adjacent sure/probable pairs in order within pages of 50;
1,000 shuffles median 49.7%, max 56.9% (contributor: 96%, median 50%, max 57%). 28 groups occur only in the held-out letter of
25 Nov 1806 (the contributor's 23 testable + 5 not testable); by page bounds from the other two letters 27 fit, 1116 does not.
That the letter was held out rests on the contributor's record (one commit; the protocol hash in validation.txt is not an
external timestamp). The held-out test is superseded by the external key.

**Images.** NARA catalogue (script-friendly: `catalog.archives.gov/medialz/dc-metro/rg-059/1226295/T260/T260-0R/T260-0R-NNNN.jpg`,
file unit 218518480, roll 8 naId 221215877). All 62 groups of 25 Nov 1806 (0409) and all 99 of 13 Jan 1806 (0045) agree with
`transcription.txt`. On 24 Oct 1805 (0224, top of 0225) about 150 groups were compared. Two are misreads, corrected in
`transcription_corrections.tsv` and applied by the script: learn 1087 135 -> 1087 185, and lakes 153 1482L -> 153 148L
(the final hook was read as a 2, as in "its" 140L, which the contributor flagged as "lu 1402"). Two places are unsettled:
arrival 980 1?0 35, where 980 is overwritten and the middle digit is a 3 or an 8 (130 inter and 180 rive both fit badly,
179 riv would fit), and leather 1?37, where Wagner's gloss covers the second digit (1087 lea would fit; 1037 is elm). Image
0226 (the end of the letter: the second Lakes, the struck groups before "of", 489 wise) was not compared.

**Prior art.** Founders Online answers scripts with an AWS WAF challenge (HTTP 202, empty body), and this session had no
browser. Web-search snippets of Founders confirm the editors' note for 24 Oct 1805 and 13 Jan 1806: italic words encoded in
"a State Department code; key not found"; copy-text is Wagner's interlinear decoding. The 18 and 19 Nov 1806 notes and
PJM-SS volume and page numbers are by the contributor's record. No one seems to have connected Claiborne's code with WE028
before. The texts were read in 1805-1806; the new things are the identification of the code, the partial key, and three
small corrections to the printed text (489 wise, 235 slip, 611 slip), which the WE028 values confirm (489 wise, 235 bil,
611 order).

**One key, one entry.** The number-to-value map is morris1813's (reversed WE028), not jqa's (direct). Precedent keeps jqa
and morris1813 apart because their maps differ. Claiborne's map is the same as Morris's, so by the rule this folder
belongs with morris1813 (one entry for the reversed-block copies of WE028) unless the owner keeps correspondences apart.
That is the owner's call, and is one reason there is no page yet. `../graham1806` (Graham, 1806, catalogue 482) is in a
different code: the editors' conjectures there do not fit the reversed table (e.g. 73 = od, 67 = obtain).

**Method and class.** The texts are Wagner's (class "already solved"). The key that reproduces them was matched from
external sources (WE028 and the reversal from morris1813), method "read after matching with key from external sources".
The contributor's own partial rebuild from Wagner's interlinear decipherments ("key recovered based on adjacent plaintext")
is kept as a step and in the credits.

## Remaining gaps
- 261 of about 1 600 numbers; the letters of 18-19 Nov 1806 (LoC) not accessible: Wagner's decipherments there could be checked with this key.
- Doubtful zones: 135, 143, 149 (Wilkinson), 362, 364 (defen-ce), 484, 1037/1087.
- Weber 1979 not consulted.

- (14 Nov 2026) 1077 = tra against tro- in troops x3: re-read the M97 r13 sheet at 1077 (WE028 577) or accept a clerk/copy variant.
- (14 Nov 2026) arrival (1?0) and leather (1?37) unsettled on the image (illegible under the gloss); image 0226 not compared (second Lakes, the struck groups before "of"): workable.
- (14 Nov 2026) the LoC letters of 18 and 19 Nov 1806: check whether the Burr Conspiracy Collection is online (LoC digital collections) before calling them blocked.
- (14 Nov 2026) PJM-SS notes read through search snippets only (Founders WAF challenge; use Claude in Chrome).
- (14 Nov 2026) one key, one entry with morris1813: owner's decision.

## Escalation
Siblings: the Mississippi (Sargent) code differs. Print: PJM-SS and Rowland used as the clear. Key rebuild: partial, done. Next: other holders of the same 1805 code (the same list may have been issued to other officers).

(14 Nov 2026) Known key found: WE028 with reversed blocks (morris1813), applied unchanged; done. Next: image 0226, the 1077 sheet entry, the LoC letters, the Founders notes in a browser, then the one-key-one-entry decision and a write-up. Other holders of the reversed-block copy: Morris at Cadiz 1813-15 is one; the rest of T260 rolls 7-8 (Claiborne's despatches of 1805-06 not yet scanned for code) is the next sweep.
