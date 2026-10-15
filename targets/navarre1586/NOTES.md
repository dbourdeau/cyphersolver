# Henry of Navarre, La Rochelle, 10 July 1586: news-sheet to Ségur in the f. 321 key (BnF 500 de Colbert 401 f. 333)

Read on 16 Sept 2026 in `targets/segur/`. Gallica ark:/12148/btv1b10035574w, f. 333 = canvas 369, f. 321 = canvas 359.

**Split on 14 Oct 2026 from `segur`** under the one-key rule (George Lasry): f. 333 was read with **Tomokiyo's f. 321
key**, not with the key recovered in `segur` for ff. 233, 239 and 288v (key A). Key A and the 1583 key of f. 143
(`segur1583`) are different ciphers, each with its own page. Moved here: `ct_333.txt`, `key_321.json`, `henryiii_figure.png`
(Tomokiyo's table, from cryptiana) and the controls of f. 333's size (`control4.txt`, `control4_key.txt`, `control5.txt`,
`control5_key.txt`). The scripts (`decode.py`, `solve.py`, `solve_mono.py`, `eval_mono.py`, `control.py`) stay in
`targets/segur/`; run them from there with the paths of these files. Full-resolution images are not committed.

## The key

S. Tomokiyo reconstructed the key from f. 321 (La Rochelle, 11 June 1586, Navarre to Clervant, Buhy(?) and Ségur as
*conseillers en mon conseil d'estat et surintendans de ma maison et finances*), where the decipherer struck through every
figure and wrote the clear text between the lines (cryptiana henryiii.htm, listed there as Henry III). Table in
`key_321.json`: letters 12-62 in alphabetical order with homophones (a 12-14 … u 53-55, x y z 56-59, et 60-62),
syllables ba-vu 63-142 in sixteen rows b c d f g h j l m n p q r s t v, names from 162 (162 = Le Roy de Navarre). It is the
design of key A with the letters shifted by eight and *h* and *j* rows added to the syllabary.

## f. 333

Transcribed at 2× (`ct_333.txt`, 108 numeric tokens by `_check_profile.py --measure --digits`, 62 distinct; superscript 31
after 52 in line 4). A news-sheet in the third person (*Le Roy de Navarre a envoyé … le Sr de Vesin de la Marsilliere à
Berne*) signed *Henry* at La Rochelle, 10 July 1586, and countersigned. Tomokiyo's table reads it almost completely:
*[162] desire fort d'avoir des nouvelles de [204] de [189] [190] … et leur advis sur le chemin [qu'i]l doit tenir et
comment. … [167] assurer qu'aussi tost que les reistres marcheront il montera à cheval; [166] et son frere sont de bonne
volonté; il fault avancer la levée et la faire marcher le plustost qu'on pourra.*

The reading forces three values Tomokiyo left blank, **24 = f** (*frere*), **34 = l** (*il*, *montera*), **36 = m**
(*comment*), and shows 61 = et as well as 62. Five figures disagree with the French and were confirmed at 2× as written
(55 in *advis*, 19 and 31 in *à cheval*, 88 in *fault*, 20 in *marcher*): the encipherer's slips, or homophones the
pattern does not predict. Measured 14 Oct 2026: 103 of the 108 numeric tokens have a value; the 5 open are the name codes
204, 189, 190, 166, 167.

## Blind checks (16 Sept 2026)

- **Free annealer on f. 333** (BLOCK0 = 63, NBLK = 16, 12 seeds × 300 000 steps, clear French as context): no two seeds
  agree; the best key has 35 of 58 letter tokens and 3 of 16 blocks right. A matched control of the same size
  (`control4.txt`) fails the same way (37.3 %, 3/16): f. 333 alone is below unicity for that method.
- **Design-constrained annealer** (`targets/segur/solve_mono.py`, homophones in alphabetical order, so the letter key is
  a vector of homophone counts): every seed converges; 54 of 58 letter tokens (93.1 %) against `key_321.json`, syllable
  rows weaker (7 of 16 blocks). Matched alphabetical control (`control5.txt`): 36 of 40 letter tokens (90 %). So the
  letter key of f. 321/333 can be re-derived from f. 333 alone once the chancery design is assumed. The reading itself is
  Tomokiyo's key applied and extended.

## f. 321

Every cipher figure is struck through by the decipherer's pen. At 2.4× and 3× the strike-through swaps 4/9 and 3/8
systematically, and removing the stroke removes the digit cores, so a figure-level transcription independent of the
interlinear reading is not obtainable from this image; one clean segment (`61 130 33 78 54 52` = *et si l fa u t*)
confirms the key. Not re-transcribed; Tomokiyo's table is the ground truth for it.

## Remaining gaps
- name codes 204, 189, 190, 166, 167 in f. 333 - blocker: no-key-material; Tomokiyo's table lists only 162, 302, 315, 317, 322, and each occurs once with no gloss
- f. 321 figure-level transcription - blocker: needs-physical-access; the decipherer's strike-through runs through every figure on the scan; the leaf or a raking-light image would be needed

## Escalation
- [x] siblings: the whole volume swept; f. 321 is the only other leaf in this key
- [x] clear-pages: the f. 321 interlinear decipherment is Tomokiyo's source
- [x] known-keys: Tomokiyo's f. 321 key applied; key A (segur) does not fit (figures below 12 are doubles and nulls here)
- [x] print: cryptiana henryiii.htm; no edition of the négociation found
- [x] key-rebuild: four values added from the reading; blind design-constrained re-derivation agrees on 93 % of letter tokens
- [x] retry: the five disputed figures re-read at 2×

## Assumptions for George's review
- No Lasry credit here: his saved decryptions of 15 Oct 2024 cover ff. 143, 233, 239 and 288v, not ff. 321 or 333.
