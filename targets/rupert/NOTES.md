# Prince Rupert / Royalist ciphers 1645-46 — cryptiana unsolved items #5 and #6

Status: read in part, written up 9 Oct 2026 (docs/rupert.html). Cryptiana #5 (Maurice) and #6 (f. 9/f. 10) not solved: no key in Add MS 72438 fits; f. 104 and R8433 not solved; f. 107 (R8728) deciphered 95.3% of words with the f. 106 alphabet. Profile: primary method 'read with known key' (f. 107), parts 'not solved' for the rest; fraction_read 122/1,412 = 8.6%.

## #5 Maurice -> Rupert, Worcester, 7 July 1645 (Warburton, *Memoirs of Prince Rupert*, iii. 133)
Ciphertext (full, from the 1849 print; `maurice1645.py`): 93 groups, 63 distinct, max 398; 18 distinct groups < 100
(letters), 45 >= 100 (words). Repeats: 148 x5, 15 x4, 229 x4, 293 x4, 26/84/150 x3. Clear words interleaved:
"By your cipher, you may observe, that ... Garrison, ... Accordingly, ...". Context: the Scots army under Leven
was four miles from Worcester; Maurice is explaining why he cannot bring his regiments to Rupert at Bristol.

Known keys tested (ranges only, by Tomokiyo and here): Charles I-Rupert-Digby-Ormonde 1644-45 (has letter+digit codes
a1..p5, words to 421) and Nicholas-Rupert July 1645 (words 98-373 and 427-616) do not fit. "By your cipher" = a
cipher Rupert issued to his brother; no copy is known in print.

### Where the key would be — all located, none reachable online (2026-09-15)
- **BL Add MS 18980-18982** (Rupert Correspondence 1642-45, Warburton's source): all three volumes are digitised
  (ark:/81055/vdc_100163595876, vdc_100176984506, vdc_100165006764) but the catalogue says *"digital images
  currently unavailable"* — offline since the October 2023 BL cyber-attack; IIIF manifests return 403.
  The 18982 contents list (searcharchives.bl.uk/catalog/040-002095608) shows Maurice->Rupert 29 Jan 1645 at
  ff. 27-28 but no cipher-key item; the 7 July letter is not itemised there (Warburton may have used another volume).
- **DECODE** has 47 records from Add MS 18980-82 (R8429-R8454, mostly "Decrypted" 1645 letters with interlinear
  decipherment) and 81 from Add MS 72438 — images require an account and are flagged private (BL permission needed
  to publish). Public thumbnails are 200 px, unreadable.
- Cryptanalysis on 93 groups of a ~400-entry nomenclator: not feasible.
**Status: offline-only** (needs BL images back online, or a DECODE account + BL permission).

## #6 Intercepted royalist letters, BL Add MS 72438 ff. 9-10 (DECODE R8623, R8624), May 1646
Add MS 72438 = Trumbull Papers vol. 197, Weckherlin's cipher-keys and intercepts, incl. the 49 keys taken from
Digby's coach at Sherburn (Oct 1645). Catalogue (searcharchives.bl.uk/catalog/040-001967027): f. 9r "Intercepted
letter, addressed to 'My Lord' ... 21 May 1646. Largely in (undecoded) cipher"; f. 10r "Intercepted letter to King
Charles I, 13 May 1646. Largely in (undecoded) cipher". Also f. 104r and f. 171r undecoded.
- Full ciphertext is **not available anywhere online**: cryptiana prints only the first two lines of f. 9
  ("My lord your Lo^p being not a little beholding to 309 for y^e 500 44 66 24 21 107 195 155 212 well 32 66 25 155
  151 12 38 35 26 81 38 122 ..."; letters as 2-digit, words 107-500); DECODE records are "Private Ciphertext: True",
  authentication required; the BL digitisation (vdc_100162920089) is offline (403).
- The "cf. Biermann & Brown 2021" idea (their Isle-of-Wight key: letters 1-106, words 142-615) cannot even be
  tested on 40 groups of excerpt with the key table living in Cipherbrain comments; it is a 1648 key for a
  different correspondent in any case.
- The same volume holds 49+ keys (ff. 25-99, 100-109, 151-170) that would very likely read f. 9/f. 10 by simple
  trial once images are accessible — this is a "key in the same box" situation like Hamilton, not a cryptanalysis
  problem.
**Status: offline-only** (BL images offline; DECODE login + permission).

## Files
- `maurice1645.py` — the Warburton ciphertext and structure stats.
- `get_warburton.py`, `find_letter.py` — fetch/locate the letter in the archive.org OCR (`warburton3.txt`, not tracked).
- `thumbsize.py` — confirms DECODE public thumbnails are 200 px.

## If resumed
BL restores Add MS 72438 / 18982 images (check the catalogue "Digitised Content" field) -> pull IIIF manifests,
OCR-free eyeballing of the 49 Digby keys for one with words <= 398 and no letter-digit codes (Maurice), and run the
f. 9/f. 10 texts against every key in ff. 25-109.

## 9 Oct 2026 — DECODE access works; records listed, f. 9 and f. 10 transcribed
- `decode_fetch.py` (cookie from targets/bordeaux) saves record pages + API views in `decode/` (git-ignored: pages
  embed a session token); `decode_list.py` writes **`decode_records.tsv`**: 115 records, Add MS 72438 (R8619-R8745,
  81 = 8 ciphertexts + 73 keys, plus the ct f. 104 R8725, f. 107 R8728), Add MS 18982 (R8428-R8454, 27 ciphertexts)
  and Add MS 18983 (R4916-R4922). **No DOC transcription files on any of them.** Add MS 18980 and 18981 have no
  DECODE records at all. The gap ids R8659-R8718 between the keys are Add MS 20443 (Italian), not this volume.
- No Maurice letter in the 18982 records (authors are Digby, Nicholas, "P. R.", Charles R.); the 7 July 1645 letter
  is not on DECODE.
- **f. 9r (R8623)**: one slip, verso blank; `f9_transcription.txt`. Clear words + ~130 groups: letters 3-81, words
  100-343 (155 and 212 frequent); signature "36 54 3 222 6 9 44 34 3". Tomokiyo's excerpt "500 44 66" is "100 44 66"
  on the image, "195" is "105".
- **f. 10r-v (R8624)**: letter to the King, endorsed "Quadrupl." (fourth copy), right edge of the recto and left edge
  of the verso torn, water stain on the verso; `f10_transcription.txt`, ~600 groups: letters 1-99, words 100-697
  (360/361 very frequent, "430 543" x6, "resolved to expect 430 543"); signed "555 697 496", dated 13 May 1646.
  The two letters use different keys (f. 9 has no 360/361 and no group above 343).
- **f. 25r (R8627) is the index "Cyphers taken in the L. Digbys [coach]"**, keys numbered 80-139 (ff. 25v-26v blank):
  80 Countess of Cork; 84 Mr Bennet with L. Digby; 85 Lady Goring; 86 Lady Elizabeth; 87 with M. G. B.; 88 Sr John
  Nor[?]; 89 with Major Digby; 90 with the Governor of Pontefract; 100 Lady Kat.; 101 Lord Traquair & Digby;
  102 miscarried, Col. Gerrard; 103 E. Antrim; 104 Thom. Killigrew; 105 Ld Culpeper & Sr L. Dives; 106 Col. Barry;
  107 Mar. E. B., Capt. Digby, M. Jo. Fe. & T. K.; 108 Sr George Hamilton; 109 Mr Whorewood; 110 Col. Leigh;
  111 Col. Frood; 112 Lord Taaffe; 113 Sr W. Vavasour; 114 Doctor Rutherford & John Digby; 115 Sr W. Ogle;
  116 Kirkby, Sr Ph. Musgrave, John Lamplugh; 117 E. Bristol, L. Digby, Col. J. Digby, Sr Richard Greenvill & Doctor Cox;
  118 Ormond & Pr. Rupert; 119 Ld Inchiquin & L. Digby; 120 Ld Culpeper; 121 Saint Nicholas; 122 Carbury;
  123 His Majesty's cipher with the Queene; 124 Col. Cockram; 125 Mr Browne; 126 Newark; 127 Boisivon; 128 Doctor
  Johnson; 129 without name, from Queen's Court; 130 Col. Hurliston; 131 Lord Goring; 132 S. Kenelm Digby; 133 Col.
  Blague; 134 Mr Neile; 135 E. of Newport; 136 Harcourt; 137 Heenfleets; 138 many sheets, De Vic's hand; 139 Dr Isola.
- Key screen by range (f. 9 needs letters to ~81 and words 100-343 with no letter+digit codes; f. 10 letters 1-99,
  words 100-697), from the 1600-px previews:
  R8628 (Preston) letters 1-35, words 36-200: no. R8629 (80 Cork) words to 144: no. R8630 (84 Bennet) syllabary with
  letter+digit codes: no. R8631 (85 Lady Goring) letters only. R8632 (86 Princess Elizabeth) small, symbols: no.
  R8633 (87 M.G.B.) words 61-91, 100-106, 200-212, 300-316, 400-419: no. R8634 (88) words 79-152; R8635 (89) words
  71-99; R8636 (L. Digby) words 55-109; R8637 (100 Lady Kat.) sparse; R8638 (101 Traquair) letters 1-129, words
  128-305; R8639 words 79-127; R8640 (103 Antrim) letters 1-89, words 95-274; R8641 (104 Killigrew) small; R8642
  letters + letter-digit codes; R8643 (108?) one-part alphabetical, words to 293; R8644 (107) fragment to 155; R8645
  (Hamilton) words to ~200; R8646 (109 Whorewood) 64-161; R8647 (110 Leigh) letters only; R8648 77-105; R8649
  (112 Taaffe) letters only; R8650 letter-digit codes, words 200-239; R8653 (116 Kirkby/Musgrave) graphic letters;
  R8654 (117) letters to ~105, words 104-278; R8657 (120 Culpeper) 80-165: all no.
  **R8655 (118 Ormond & Pr. Rupert, ff. 59-60)**: letters 1-80, nulls 81-90, one-part alphabetical words 91-434,
  letter+digit small words (a1 and ... p6): transcribed letter table into `keys.py`. Read against f. 9: "100 44 66 24
  21 107" = Aurange Prince, o, r, m, b, Anglesey: no. Against Maurice 1645: letters fit the range (82/84 = nulls) but
  "15 26 342 148 136 13" = a m [342 blank] Design Dungarvon c: no.
  R8656 (119 Inchiquin & Digby): letters 1-89 with scattered nulls, words 100-~323 + letter-digit small words: range
  fits f. 9 only loosely (f. 9 has no letter-digit groups); R8651 (f. 53-54) letters to ~105, words to ~560 and
  R8658 (f. 64-65) letters to ~124, words to 845: f. 10 range candidates, to check.
- More screening: R8686 (122 Carbury) supplement 77-106; R8687 (123 King with Queen, ff. 67-68) letters 1-79 (4, 21,
  34, 44 unassigned), words to 575: applied to f. 9 and f. 10 (`test_letters.py`), gibberish. R8723 (ff. 100-101, "King
  and Queen") is a decipherer's worksheet of the same key 123 (1 w, 2 k, 3 p, 4 nul ...). R8690 (124) letters only;
  R8694 (125 Mr Browne) letters 2-79, words 80-371, names 402-~698: f. 10 range fits but applied it is gibberish.
  R8696 (126 Newark) to 179; R8697 (127 Boisivon), R8719 (136 Harcourt), R8720 (137 Heenfleets) French; R8700 to 195;
  R8701 a 559-580 names fragment; R8704 (130 Hurliston) syllabary codes; R8709-R8716 small (words < 110);
  R8721 (ff. 90-97) four-digit code to ~3000. **R8724 (ff. 102-103) endorsed "Cypher betwixt the L. Digby & his
  servant Walsingham (now at Modlen College)"**: letters 1-75 (61-75 partly), words 76ff (reverse alphabetical: 76
  your, 77 you, 81 worke, 82 without, 83 with, 86 why, 87 which ...): applied to f. 9 and f. 10, gibberish. It should
  be the key of the Walsingham ciphertexts R8625/R8626 (1647, already "Decrypted").
- Remaining box keys: R8722 (ff. 98-99), R8731 (Weckherlin, French), R8732 (Latin), R8733, R8734 (Sackville Crow,
  Constantinople 1638), R8736, R8738 (Weckherlin-Augier French syllabary), R8739, R8740-R8742 (Parliament
  syllabaries, words to 1161), R8743-R8745 (Parliament key, words 200-487 reversed; letter table applied: gibberish):
  none is a royalist 1646 key of f. 9/f. 10 shape. R8658 (f. 64-65) letters 14-125 + a1-type codes: f. 10 uses 1-13
  heavily, so no. **No key in Add MS 72438 fits f. 9 or f. 10.** The coach keys were taken in Oct 1645; these
  intercepts are May 1646, so their keys were probably never captured with them.
- Letter runs: f. 9 108 letter groups in 28 runs, f. 10 300 in 117 runs (mean 2.6): too little homophonic text
  (~80-99 letter values) for a ciphertext-only key rebuild.

## #5 Maurice 1645 — 9 Oct 2026
- No Maurice letter in the DECODE 18982/18983 records; Add MS 18980/18981 are not on DECODE. Tested: key 118
  (Ormond-Rupert, R8655) letter table -> nonsense; Tomokiyo's partial Nicholas-Rupert May 1645 key (from his notes on
  R8430/R8432) -> nonsense.
- **Lead**: R8433 (Add MS 18982 ff. 51-52, DECODE "Bristoll", non-decrypted) is **Arthur Trevor to Rupert, Bristol
  8 April 1645** (signed "Ar: Trevor"), clear text with ~60 cipher groups of Maurice's shape (letters 4-76, words
  110-222). Context cribs: "Sr Vivian Molineux, Sr Bryan O'Neile ... were by ill weather forced 137 26 50 30 12 45 7
  32 67 5 147 ... from thence by night marches they recovered 67 24 43 9 31 52 39" (7 letters, no repeats: e.g.
  Chester). Not broken; whether it shares Maurice's key is unknown.

## 9 Oct 2026 (follow-up) — R8433 Trevor, f. 104, f. 107
- **R8433 transcribed** (`trevor1645_transcription.txt`): 62 groups, of which 54 letter groups in 4 runs (36 distinct,
  4-76) and 8 word groups (110-222). Date: the loss of "Sir Tho. Coghill's house" (Bletchingdon, 24 April 1645) puts
  it at 28 April 1645, not 8 April. Not in Warburton iii (grep of the OCR: no Trevor letter of April 1645, no
  Molyneux/O'Neill passage); a web search found nothing on the Molyneux/O'Neill landing.
- Crib attempts (`trevor_anneal.py`, en-1640s 4-gram, homophonic annealing over the runs): with "chester" or
  "bristol" fixed on the 7-letter run, and with no crib, each restart gives a different English-looking string
  (e.g. "...husbanda | kplac | iuwereach..." vs "...ioward | orcollenc"): 54 letter groups over 36 homophones are far
  below unicity; **no stable solution, so no letter table recovered**. The box letter tables (118, 123, 125, Digby-
  Walsingham, R8744) applied to R8433: nonsense. So test (a) on Maurice / other 18982 letters could not be run.
- **f. 104r (R8725)**: DECODE says "Decrypted", but the sheet carries **no decipherment**: an all-numeric letter, 19
  lines, 253 groups + 3 in the endorsement (`f104_transcription.txt`, `f104_groups.txt`), letters 1-99, words 100-859 (342 most frequent),
  endorsed "The direction endorst 347: 313: 364". Letter tables 118, 123, 125, R8744 and the Parliament key R8741
  (letters 10-72, nulls 1-9, 73-75, 776-779) applied: nonsense; key 123's 342 = Broughton, so not that key either.
  Unread.
- **f. 107 (R8728) read** (`f107_reading.txt`): graphic-sign English letter, 10 lines + a 4-sign header, partial
  interlinear gloss by a contemporary decipherer. The **lower alphabet of f. 106 (R8727)** is its key, unchanged
  except for homophones it does not list (plain-e shape = e, Ʈ = h, ɣ = r, 7 = y, plain α = t); signs that look like
  letters are key signs (circle = i, stroke = o). Checked against every glossed word ("I hoped for some comfortable
  lynes but tis in vaine to expect" = 0 Ʈ1ŧ≡= +1X S1:≡ -1:+1XȺ∧Ꝛ≡ɩ ɩıı:≡S ...). Measured 129 words, 6 unread or
  conjectural = **95.3%** (write-up recount: 128 cipher words, the editorial "[one]" excluded, 122 read = 95.3%). Text: "if I may cal you so without offence, I rese[ave] few lynes, so much as your affection
  would give you leave. God knowes how ioyfull I was to heare you got safe to the King. It was reported heare you were
  al kild [..] and taken, which made me almost besides myselfe and could never be satisfied til I heard from you. I
  hoped for some comfortable lynes but tis in vaine to expect one where there is [..] my heart. It is not the condision
  of honest men and woman that after [so] many yeares acquaintance should make them hate and neglect one another. I
  shal in loving you, that it hath as good an heart to [dye] for you as it hath a mind and ..." Writer: a woman, an
  old acquaintance, to a royalist officer who reached the King after being reported killed or taken; no names,
  date or place in the text. The f. 106 sheet is filed with the coach keys, so presumably to Digby or one of his
  correspondents, before Oct 1645 (not provable from the text).

## Remaining gaps
- f. 9 (R8623), whole cipher text: - blocker: no-key-material; none of the 73 Add MS 72438 keys fits, and 108 letter
  groups are too few for a ciphertext-only rebuild.
- f. 10 (R8624), whole cipher text: - blocker: no-key-material; no Add MS 72438 key fits; 300 letter groups over
  ~99 homophones, short runs.
- Maurice 7 July 1645: - blocker: no-key-material; key not in Add MS 72438 or on DECODE; 93 groups.
- f. 104r (R8725), whole letter: - blocker: no-key-material; no Add MS 72438 key tested fits; 253 groups + 3 in the endorsement (256 measured).
- R8433 Trevor 1645, 54 letter groups: - blocker: too-short; no stable key from cribs/annealing, no print found.
- f. 107 (R8728), 6 words (header "=≡↑ŧ̥", "≡≡=" after kild, ":≡0" before my heart, the blotted word, "=7L" before for you, the end of "rese.."): - blocker: illegible; blot and writer slips, the gloss skips them, no second copy.

## Escalation
- [x] siblings: all 115 DECODE records of Add MS 72438 / 18982 / 18983 listed; all 73 keys of Add MS 72438 screened by range; 6 letter tables applied; f. 106 (R8727) next to f. 107 proved to be its key; R8433 (Trevor, 18982 ff. 51-52) transcribed.
- [x] clear-pages: none with the intercepts f. 9/f. 10 or f. 104; f. 25r index read (keys 80-139 with correspondents); f. 107's interlinear gloss used as crib.
- [x] known-keys: keys 118, 123, 125, the Digby-Walsingham key, R8744/R8745, the Parliament key R8741, Tomokiyo's 1644-45 royalist keys (Ormond-Rupert, Nicholas-Rupert May/July 1645): no fit on f. 9, f. 10, f. 104, R8433 or Maurice; f. 106 lower alphabet reads f. 107.
- [x] print: Warburton iii (Maurice; no Trevor letter of the week), cryptiana, web search; no decipherment in print for f. 9/f. 10/f. 104/R8433.
- [x] key-rebuild: homophonic annealing on R8433 with and without cribs (chester/bristol) does not converge (54 letter groups over 36 values); f. 9 (108 letter groups) and f. 10 (300) too short for ciphertext-only over ~80-99 homophones; f. 107 homophones added to the f. 106 alphabet.
- [x] retry: f. 107 re-read with the extended alphabet (95.3%); remaining six words are blots or conjectures. The others need a 1646 royalist key that is not in the volume.

## DECODE queue
- R8627 (f. 25r): it is the index "Cyphers taken in the L. Digbys [coach]", keys numbered 80-139 with
  correspondents (list above); add it to the record description; the key records R8628-R8745 can carry these numbers
  (written on each sheet's dorse, e.g. 118 = Ormond & Prince Rupert, 123 = King & Queen, 107 = Capt. Digby &c.).
- R8724 (ff. 102-103): endorsed "Cypher betwixt the L. Digby & his servant Walsingham (now at Modlen College)";
  link to the Walsingham ciphertexts R8625/R8626.
- R8723 (ff. 100-101) is a decipherer's worksheet of key 123 (R8687), not a separate key.
- R8433 (Add MS 18982 ff. 51-52): author Arthur Trevor, Bristol, [28] April 1645, to Prince Rupert; add transcription.
- R8728 (f. 107): add the reading (f107_reading.txt) and key = R8727 (f. 106) lower alphabet; writer a woman, recipient a royalist officer.
- R8727 (f. 106): note that the lower alphabet is the key of R8728.
- R8725 (f. 104): status should be Non-decrypted (no decipherment on the sheet); add f104_transcription.txt.
- R8623 / R8624: add transcriptions (f9_transcription.txt, f10_transcription.txt); R8624 endorsed "Quadrupl.";
  R8623 f. 9v blank.

## Write-up, 9 Oct 2026
- Page `docs/rupert.html` (slug `rupert`): hero and title say #5 and #6 remain unread and that f. 107 is what was
  deciphered. Crops of f. 107r (lead + full), f. 106r and f. 9r from the DECODE images; portraits Maurice
  (Honthorst) and Rupert (Lely); reveal = line 6 of f. 107 sign by sign (`f107_decode.py`, transcribed from the
  image and decoded with the f. 106 key; the r sign used for x in "expect" marked uncertain).
- Counts measured: maurice1645_groups.txt 93, f9 152, f10 721, f104 256, trevor 62 (--digits), f107_reading.txt
  129 tokens (--drop-first) = 128 cipher words + the editorial "[one]". fraction_read = 122/1,412 = 0.086, f. 107 in
  words, the rest in figure groups (a lower bound; #5 and #6 are at 0).
- Outcome framing: Lasry's split rule (primary achievement): the only achievement is f. 107, so outcome.method is
  "read with known key" (the key sheet filed beside it), with parts "not solved" for Maurice, f. 9/f. 10 and
  f. 104/R8433. f. 107's part is "complete" (95.3%, read bar met). Note for the paper: `_analysis.py` counts one
  method per target, so this target counts as a known-key success although the items as posed failed.
- README rows under Read with known key (f. 107) and Not solved (the rest); the old Not applicable row removed.
  SOLVED_CATALOGUE 138, SOLVED_RANKING provisional 2.80. DECODE queue: R8623, R8624, R8433, R8725 (status ->
  Non-decrypted), R8728 (reading R8728.txt, key R8727), R8727, R8627 (index), R8724, R8723.
