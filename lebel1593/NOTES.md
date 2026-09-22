# Lebel, Savoyard ambassador in Paris, to Charles Emmanuel I — BnF fr. 3983 nos. 11, 62, 100 (1593)

Catalogue entry "Lebel, Savoyard ambassador, to the Duke of Savoy, three letters" (class C). Opened 21 Sept 2026.

Status: read (all three letters; ~98% of enciphered tokens; see section 8). Written up as `docs/lebel1593.html`.

## 1. Prior art: the key is published, the three letters are not read

- The catalogue said "no decipherment noted; Lebel is named on Tomokiyo's League page". The League page
  (cryptiana `league.htm`, saved as `src/t_league.htm`) lists all four Lebel letters in fr. 3983 (nos. 11, 62, 80,
  100) and points to a separate article, **`savoy.htm`** ("Reading Undeciphered Letters to the Duke of Savoy
  (1593)", S. Tomokiyo, 2017, rev. 2023; `src/t_savoy.htm`).
- Tomokiyo reconstructed the key (`src/savoy.png`) from the two letters deciphered at the time: **fr. 3983 no. 80,
  f. 166-169, 13 March 1593**, deciphered on a separate sheet (f. 167, canvas 295, checked here), and fr. 3984 f. 182
  (24 July 1593, interlinear), plus fr. 3985 f. 23 (5 Aug 1593, interlinear).
- For our three letters he gives **only the images**, "many code groups yet undeciphered". A commented-out draft in
  the HTML of `league.htm` lists his guesses for about 90 code numbers from f. 130 (no. 62). There is no reading of
  nos. 11, 62 or 100 there or in print as far as checked. So the key is prior art, and a reading of these three
  letters would be new. Per Lasry's rule ([[cryptiana-undeciphered-meaning]]), "undeciphered" on cryptiana means
  that no decipherment was made at the time. Here Tomokiyo says in so many words that he did not read these letters.
- Also in the same key, not in this entry: BnF esp. 336 nos. 79-81 (2 March, 18 May, 4 July 1593), fr. 3984 no. 86,
  fr. 3985 no. 9.

- DECODE has no record of these letters: the full record list (10,106 records, `catalogue_harvest/decode/list.json`,
  18 Sept 2026) has no BnF fr. 3983/3984/3985 holding and no Lebel, so there is nothing to queue.

## 2. The leaves (fr. 3983 = btv1b9059406b)

The folio numbers in the BnF notice (`src/notice_3983.html`) are two higher than Tomokiyo's, because the notice
foliates the piece and he gives the first leaf.

| no. | date | notice fol. | leaf | canvases |
|---|---|---|---|---|
| 11 | 17 Jan 1593 | 28 | f. 26r-v | 49-50 |
| 62 | 10 Mar 1593 | 132 | f. 130r-v | 233-234 |
| 80 | 13 Mar 1593 (deciphered at the time) | 169 | f. 166; decipherment f. 167 | 293-295 |
| 100 | 27 Mar 1593 | 196 | f. 194r-195r | 333-335 |

## 3. The system

A homophonic substitution of 1-2 signs per letter (a: pp/12, e: ɱ/g, o: #/✱, s: ooo/4t, t: λ/4→ ...), three nulls
(4+, X, o-f), a sign for *et*, and a nomenclator of about 300 numbers set off by dots, with an alphabetical
addendum above 300 introduced later in 1593. Words run on without division. The "vm" pair is a second *d* and
never stands alone (Tomokiyo's note, confirmed on no. 62: *conduysant*, *de droict*).

## 4. Readings

- `reading11.md`: no. 11, read in this session (letter level). Mayenne is recovering his standing on the crown;
  the Pope and the King of Spain want a Catholic king elected; Mayenne will favour whichever candidate brings the
  most advantage; the Cardinal de Bourbon; the secret council of three (…, Villeroy, président Jeannin).
- `reading62_full.md`: no. 62, read sign by sign. Recto about 94% of letter signs, verso about 55% (the recto's
  ink bleeds through it). Mayenne's discontent was bought off: 40,000 écus down, and assignations in [69] and in
  Spain up to 260,000 écus. Philip II's ministers persist; Feria brings "ung docteur qui veult disputter la
  couronne par poincts de droict, dont l'on se mocque tout ouvertemant". The Spanish army is smaller than any
  before it. Those around Mayenne, seeing no chance of the crown for him or for the house of Bourbon, will propose
  a [255], and someone will soon come to Savoy on Mayenne's behalf. Lebel advises courting Mayenne.
- `reading100_full.md`: no. 100, read sign by sign, about 85%. Lebel's approach to someone (Villeroy?): if Philip
  II's designs fail, Savoy could "avec plus de raison que aultre [163 prince]" hope from the Estates. Money for his
  "compagnon" and président Jeannin, to be paid through Zamet. Feria's and Commandeur Tassis's letters raise hopes
  that Spain, failing, will turn to Savoy. Good offices at Rome with the Pope. The Provence governorship and
  Vaudemont. The château of Miolans.
- Taken together: the three letters follow Savoy's candidacy for the crown at the Estates of the League, from
  January to March 1593.

## 4b. Codes recovered from the letters deciphered at the time (`codes_harvest.tsv`, `codes_harvest.md`)

Sources: fr. 3983 no. 80 (cipher f. 166r-v = canvases 293-294, decipherment sheet f. 167 = canvas 295); fr. 3984
no. 86 f. 182r-v = canvases 339-340 (interlinear); fr. 3985 no. 9 f. 23r = canvas 47 of ark btv1b90606498
(interlinear). Glossed directly (H): 24 l'Infante, 84 negotiation, 98 affaires, 250 tout, 255 tresve, 257
parvenir, 297 catholiques, 71 (Cardinal de) Pelvé, 192 choisir, 254 paix, 327 Espagnols, 369 mandé. By alignment
(C): 94 pratiques/menées, 100 condescendre, 102 aller, 104 dire, 115 celuy, 129 donner, 133 incontinant, 134 tost,
142 affectionné/serviteur, 164 filz, 190 argent, 191 the jurist (Feria's "docteur"), 236 capitaines, 221 mariage.

Applied to the three readings:
- no. 62: "sur ses pretantions ... le [292] soit pour luy *et l'Infante* [24]"; "tascheront de faire proposer une
  *tresve* [255]"; "[236] *capitaines* de Mayenne"; "le [190] *argent* plus court que jamays"; "[100 condescendre]
  [102 aller] ... bien tost"; Feria's "[191] jurist". Tomokiyo's 100 is right after all.
- no. 100: "les desseins du Roy d'Espaigne pour *l'Infante* [24] ... sont pleins de toutte impossibilité"; "faire
  [257] *parvenir* [la couronne] a V. A."; "[71] = *Pelvé*": "Sera ledict Cardinal de Pelvé"; "[84] *negotiation*";
  "[115] *celuy*"; "[142] *affectionné*"; "[164] filz"; "[133] *incontinant*".
- no. 11: "les [297] *catholiques* principaulx qui suivent le party du Roy de Navarre"; "le Roy d'Espaigne luy
  [250] *tout* presenter"?, so 250 there is still uneasy; "[106] *non*" and "[235] *président*" by context.
- Still open after the harvest: 22, 27, 30, 49, 50, 64, 69, 85, 103, 130, 150, 153, 161, 163, 227, 230, 240, 241,
  247, 253, 258, 260, 274, 275, 283, 302, 305. 64/50 in no. 11 = probably *l'archevesque de Lyon* (Épinac, the
  third member of Mayenne's council), by history only.

## 5. Key corrections found here

- ∇ also stands for y. δ with a cross stands for d and also for i/j. X is not always a null (it is an i in
  *remedié*). o→ is sometimes h. The long h stands for both n and l. ∠ and a barred λ are further s forms. An α-like
  sign stands for z (*Zamet*). A barred T or □ stands for b. □ stands for u or v. "bm"/"vm" is d.
- Code values proposed from context (not in Tomokiyo): 240 maison, 250 tout, 154 sieur, 161 ses mains, 163 prince,
  164 Commandeur, 235 président, 241 chasteau, 283 lettres, 142 ministres?, 275 offre?, 253 trouver?, 257
  plaisir/service?. Tomokiyo's 100 "condescendre" does not fit.

## 8. Final pass (third pass, 21 Sept 2026): read

Files: `reading11_final.md`, `reading62_final.md`, `reading100_final.md` (built on the `*_full.md` sign-by-sign
passes with every value of `codes_harvest.tsv` re-applied); `reading_esp336.md` (context reading of the unglossed
BnF esp. 336 nos. 79-80, ark btv1b100325613 canvases 268-273).

- New code values: 283 lettres, 163 prince(s), 227 seigneur(s) (C, from esp. 336 nos. 79-80); 103 venir, 257
  faveur(s), 142 serviteur, 115 bon, 404 puis, 344 dire, 439 besoing, 24 l'Infante; 100 = pour in no. 62
  ('condescendre' elsewhere).
- no. 11: every cipher passage reads in sense; ~720 letter signs, ~714 valued (~6 open in four short spans);
  58 code tokens all valued (41 H, 11 C, 6 M: 305 pretendre, 130 avoir, 292 couronne x2, 106 non, 50 Lyon).
  "le [64] de [50]" re-read at full resolution = "le [archevesque] de Lyon", Épinac, with Villeroy and Jeannin.
- no. 62: recto 617 enciphered tokens, 607 valued (98%), every passage in sense, all 62 codes valued (36 H, 13 C,
  13 M); verso three cipher lines ~101 tokens, ~70 valued.
- no. 100: 1000 enciphered tokens, all valued; codes 65 H, 26 C, 19 M (13 of the M are context guesses: 22, 27,
  49, 50, 150, 153, 230, 274, 278, 302, 305, XC, 104).
- Overall ≈ 97% of enciphered tokens valued. What remains is physical (no. 62 verso bleed/blot) and graded
  single-context inferences.

## Remaining gaps

- no. 62 f. 130v: ~6 signs under the recto's ink before code 46, and one blot (= 1 sign, probably i) - blocker: illegible; bleed-through and blot, dense on both sides.
- no. 62 f. 130v codes 223 and 247, and the 8-sign run on line 1 (a e n l/s t s o o m a) that does not segment - blocker: open-codes; no gloss, single context under bleed.
- no. 62 recto, 10 letter signs (4 after the clear "que" at the head, 1-2 in l. 8, a stray "11" in l. 3) - blocker: illegible.
- no. 11, ~6 letter signs in four short spans (l. 4 a(i)lles, l. 6 second? under a smudge, l. 20 au(?), v10 entre(m)ettant) - blocker: illegible.
- M-grade code values: no. 11 305, 130, 292, 106, 50; no. 62 275, 69, 292, 109, 137, 278, 240, 100, 253, 30, ⅅX; no. 100 22, 27, 49, 50, 104, 150, 153, 154, 161, 230, 235, 241, 258, 260, 274, 278, 302, 305, XC - blocker: open-codes; no surviving gloss (every decipherment in this key harvested), only the office nomenclator would confirm.

## Escalation

- [x] siblings: fr. 3983 no. 80 (and its decipherment f. 167), fr. 3984 f. 182, fr. 3985 f. 23 opened and harvested (section 4b). Still to open: BnF esp. 336 nos. 79-81, same key.
- [x] clear-pages: f. 167 (no. 80's decipherment sheet) checked; no clear copy of nos. 11, 62, 100 found in fr. 3983-3985 near the letters.
- [x] known-keys: Tomokiyo's savoy.htm key (the key of this series); his commented-out league.htm guesses for ~90 codes of f. 130 compared.
- [x] print: Tomokiyo (savoy.htm, league.htm) read; no printed reading of these letters found as far as checked.
- [x] key-rebuild: letter-sign corrections (section 5) and code values by alignment with the contemporary decipherments and by context.
- [x] retry: second sign-by-sign pass on all three letters with the corrected key and the harvested codes; codes regraded H/C/M/I.
- [x] second harvest (21 Sept): fr. 3984 f. 182r-v re-read at higher resolution, ~40 more values (85 Monsieur, 64 le, 113 celuy, 114 eulx, 331 disoit, 349 estoit, 400 promettre ...; 257 glossed "en la faveur de" once, so ambiguous; the old "115 celuy" was 113). BnF esp. 336 (ark btv1b100325613): nos. 79 (canvases 268-269), 80 (272-273), 81 (270-271); only no. 81 is glossed (368 ma, 408 part, 359 ils, 383 ne). fr. 3985 f. 23v/24 blank/address.
- [x] image-processing: f. 130v bleed-through removed by registering the mirrored recto (patch-wise warp, ~1 px) and whitening bleed-level pixels.
- Result: 26 codes (22, 27, 30, 49, 50, 69, 103, 106, 130, 150, 153, 161, 163, 227, 230, 240, 241, 247, 253, 258, 260, 274, 275, 283, 302, 305) occur in NO surviving glossed decipherment. They can be closed only by the office key itself (not known to survive) or context; esp. 336 nos. 79-80 carry some of them unglossed (227, 163) and could give context values after a letter-key reading.
