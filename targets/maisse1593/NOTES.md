# Henri IV to Maisse (Venice), 8 February and 27 April 1593, in Maisse's Cipher (1592-1593) — BnF fr. 16093 ff. 406, 410

Status: in progress. Partial, 0.908 of the cipher (12 Nov 2026): both cipher blocks transcribed sign by sign (6,238 signs, Andrew Beling, `beling/`) and decrypted with a key rebuilt from the clear Brienne 13 copies of the same letters; it gives 0.908 of the decrypted letters as the copy's letters (the strict figure, under the 95% of the cipher that gives sense), 0.894 on 84 lines held out from the rebuild. Tomokiyo's own key failed the same kind of test (0.818 against 0.85, round 1). Method: key recovered from external plaintext (the copy). Next step: a second reading of the cipher lines (one blind reading each).

History: 22 Oct 2026 reading audit, both letters decoded, not read (no text in the repository). 27 Oct 2026 (WAINUT): the Brienne copies transcribed except fol. 173r and most of fol. 194v, Tomokiyo's key applied to six stretches (128 signs), read in part.

**22 Oct 2026, reading audit** (George Lasry's test): no text of f. 406 or f. 410 is in the repository, only links to the cipher leaves and to the Brienne 13 copies. Both are *decoded, not read*; class read -> not read, method read from existing decipherment -> not solved until the copies are transcribed; fraction_read 1.0 -> 0.

Earlier status (before the 22 Oct 2026 reading audit): read from the contemporary clear copies (Brienne 13); the cipher itself not deciphered on these leaves. Written up as docs/maisse1593.html.

Split on 14 Oct 2026 from `maisse1592` under the one-key rule (George Lasry, 14 Oct 2026): one entry per key. The old
entry (catalogue 17) joined four leaves of fr. 16093 that Tomokiyo assigns to two different ciphers. ff. 370 and 373
(November 1592) are in Maisse's Cipher (1592), a numerical cipher, which is a different cipher, with its own page
([`targets/maisse1592/`](../maisse1592/), docs/maisse1592.html). This folder keeps **ff. 406 and 410** in
**Maisse's Cipher (1592-1593)**, with their twins f. 404 (partial interlinear decipherment) and f. 412. The full
working record of the catalogue item (folio and canvas maps, the pièce-number route, the scripts) stays in
`../maisse1592/NOTES.md`; the fetch scripts (`fetch.py`, `fetchr.py`, `fetchb.py`) and the git-ignored images are there.
Tomokiyo's key image for this cipher is `src/henryiv_Maisse2.png` (moved here).

This entry was contributed (Arya Sanketbhai Patel, PR #7) as part of maisse1592.

## The leaves

| target | date on the original | pièce | Brienne 13 (NAF 6984) | canvas / page | confirmed by |
|---|---|---|---|---|---|
| **f. 406** (canvas 457) | Chartres, 8 Feb 1593 | 247 | fol. **171r** | 176 right | heading *"Coppie de lettre du Roy audict sieur de Maisse de Chartres le huictiesme febvrier 1593, receue le viii.e d'Avril"*; preamble identical |
| **f. 410** (canvas 461) | Mantes, 27 Apr 1593 | 251 | fol. **193v** | 199 left | heading *"Mante le vingt huictiesme Avril 1593, receue le vingt douxiesme May"* |

Twins: **f. 404** (canvas 455) is the same despatch of 8 Feb 1593 as f. 406, sent by the other route ("double voye"),
with a partial interlinear decipherment; Brienne 13 copies the letter once, at fol. 171r, under pièce 247. **f. 412**
is the duplicate of f. 410 (Tomokiyo). The four leaves of catalogue 17 are four despatches in two ciphers; f. 404 is
not one of the four (corrected 22 Sept 2026 in the maisse1592 notes).

## The cipher

Observed on f. 404 at native resolution: letter-shaped symbols (w, d, l, p, b, y, g, z, long-s and others) carry the
letters, two-digit figures carry the nomenclator; 27, 10, 26, 23, 19, 21, 22, 24 and 8 are the commonest figures on
f. 404. Tomokiyo's key, *"Maisse' Cipher 2 (BnF fr.16093, f.344 etc.)"* (`src/henryiv_Maisse2.png`), is homophonic and
carries word codes (*vous, ceulx, est, faict, de, des, fort, par, pour, que, qui, advis, ces, comme, bon, avec, et,
jay, les, luy, moy*). This is the key Henri IV calls "le double du chiffre que j'ay envoyé aud. de Brèves" in the clear
text of f. 404 itself, which is why Tomokiyo finds the same cipher in the Savary de Brèves correspondence of
1593-1596 and again between Brèves and Beaumont in 1602.

## What the letters say

- **f. 406 / f. 404** (8 Feb 1593, Chartres). The King has answered every despatch and docketed the dates so Maisse can
  tell what is lost; the Spanish insolence and the Pope; Pisany and Cardinal Gondi should not leave Rome; their going
  would be of importance, and their entry among those of the League could breed division.
- **f. 410** (27/28 Apr 1593, Mantes). Acknowledges Maisse's letters of 20 Feb, 7 and 23 Mar; the duc de Nevers held
  one courier in Champagne; warm assurance that Maisse's absence will cost him nothing in the King's favour; and that
  experience has proved Maisse's long-standing judgement of "les affaires de Rome" right.

## What is not done

Both cipher blocks are transcribed sign by sign (one blind reader per part) and decrypted (`beling/`). Not done: a
second reading of the cipher lines; the twins f. 404 and f. 412 (duplicates) are not transcribed past WAINUT's lines;
the doubtful signs listed under Remaining gaps.

## Log

- 2026-09-19: Brienne copies located through the pièce numbers (PR #7, as part of maisse1592); f. 406 = f. 404.
- 2026-10-14: split from `maisse1592`.
- 2026-11-11/12: both cipher blocks transcribed and tested; copies finished and read twice (Andrew Beling, `beling/`).

## Assumptions for George's review

- 12 Nov 2026 (`beling/`): the cipher itself is now deciphered sign by sign, so the read bar can be judged on the
  leaves: 99% of the 6,238 cipher signs take a value (0.989 by the mechanical rule alone), and the decrypted text
  matches the clear copies (0.908 of letters; most of the rest are single-sign misreadings and real wording variants).
  Decided at the integration check (12 Nov 2026): class partial (profile: read in part), by the README rule as written. The contributor
  proposed class read, counting 0.989 (signs that take a value); the strict figure is 0.908 (letters equal to the
  copy). The whole-letter readings and translations exist (`beling/reading_f406.md`, `reading_f410.md`,
  `translation_f406.md`, `translation_f410.md`); the French of the part that is in cipher is the clear copy, not a
  reading made from the cipher alone.

## 11-12 Nov 2026: both cipher blocks transcribed, Tomokiyo's key tested, a key rebuilt and passed, the copies read twice (Andrew Beling, `beling/`)

- The cipher is far longer than this file says: f. 406 has 54 cipher lines (leaf ll. 23-43 of the recto and ll. 1-33
  of the verso), ff. 410-411 have 93 (410r ll. 10-31, all of 410v and 411r, 411v ll. 1-3). WAINUT's f. 406 line
  numbers are 7 lower than the leaf's. Both blocks run from the copy's "Le surplus" / "L'experience" to the end of the
  letter; the clear closes follow. All 6,238 cipher signs are transcribed, blind to the copies, by six readers (one per
  part), with one shared sign catalogue (`beling/catalogue/`).
- Round 1 (`beling/PREREG.md`): Tomokiyo's key, frozen from his image, on 58 lines (2,501 signs): 0.818 against a bar
  of 0.85, margin 0.589 over 200 shuffled keys. A fail by the rule; the cause was sign naming and one key value.
- Round 2 (`beling/PREREG_round2.md`): a key rebuilt mechanically from the round-1 lines by a fixed rule, frozen, then
  tested on the 84 lines nobody had transcribed (3,543 signs, three new blind readers): 0.894, best of 200 shuffled
  keys 0.149, margin 0.745. Pass. Tomokiyo's key on the same signs: 0.801.
- Full construction (after the test): `beling/key/key_full.tsv`. Tomokiyo's key is right for 43 signs; `pi` is o
  (not r, 269 places), which settles the "rrme" hole (Rome); the ζ-sign is "et" (not y); 13 signs not in his key get
  values from the copies (`k` a, 238 places; `6~` ss; `La` faire; `va` ll; `Cloop` g; and others), and nine
  judged values [I] (`III a~` rr, `III` moy, `H` bien, `tt` grand ...). 99% of signs get a value; 0.908 of the decrypted
  letters match the copies (`beling/results/full_decryption.txt`, line by line).
- The cipher is not word for word the copy: e.g. f. 411v "il est possible que Dieu pourra amener" against the copy's
  "peut estre que Dieu amenera". The short run on f. 406r l. 13 reads "pour [le] regard des presens", where the copy
  has "pour le regard du pape" [I].
- Brienne 13 fol. 173r-v and 194v-196r transcribed; fol. 172r-173v and 193v-196r read a second time, blind
  (`beling/transcription/second_reading/`): 66 disagreements, 63 settled on the image. Corrections that change the
  sense: fol. 195r "aux presens de Leuant" (not "pensions de Pisani") and "secours" (not "service"); fol. 194v "Je
  croy ... d'en faire enleuer Lancosme"; fol. 195v "Gien-ne" (not "bien-tost"); fol. 194r "luy veullent persuader",
  "le grand duc luy enuoiera", "Au moings"; fol. 172v "Aiant neantm."; fol. 173r "le terme", "Orez que"; fol. 173v
  "Apres l'ouuerture". WAINUT's `f406_brienne_copy.txt` and `f410_brienne_copy.txt` are not edited; the settled
  readings are in `beling/transcription/second_reading/collation.tsv`.

## Integration check (12 Nov 2026)

- Re-run: both hash lists check; `test_key.py` 0.8184 (fail), `test_key_v2.py` 0.8939 (best shuffled 0.1492, margin
  0.7448), `build_key_v2.py` (with and without `--all`), `make_copy_round2.py` and `full_decrypt.py` give the
  committed outputs byte for byte. An independent decoder written from `key/key_v2.tsv` and the round-2 transcription
  files gives 0.8939 (f. 406 0.9048, ff. 410-411 0.8923, 63 unknown tokens).
- Images (Gallica `openapi.bnf.fr` IIIF, canvas 462): f. 410v ll. 5-6 and f. 411r ll. 20-21, about 100 groups, compared
  with the transcription: no clear disagreement (the doubtful `4?` is marked as such). The sign names were not
  re-derived from the catalogue exemplars (not committed).
- Round 1 is a failed pre-registered test and stays published as failed. That key v2 was frozen before round 2 was
  transcribed is by the contributor's record (hashes and self-declared times in `beling/CHECKS.txt`).
- Corrections made here: the Status line (it mixed three states) and the Assumptions item that still carried
  `fraction_read` 1.0; class stays partial with the strict figure 0.908; method changed from "read from existing
  decipherment" to key recovered from external plaintext (the key was rebuilt against the copy in another volume);
  `beling/README.md` section 7 says 6,223 signs where 6,238 is right (`build_key_v2.tokens`); the PR text's "no
  translation of the whole letters" is out of date (the translations were added in its second commit).
- `validation.tsv` (written here from `key/key_full.tsv` plus the overrides applied to the 6,238 signs) and `python docs/_validate.py maisse1593 --write`: reading score -2.119 against random keys -4.660 (max -3.775, z 7.1) and the shuffled-text refit -2.835: verdict pass. The key was fitted to these same signs, so this shows that the letters read as French, not that the key is held-out.
- Overlap: no other target holds ff. 406 or 410; `mayenne1586*` and `matignon1586*` are different ciphers.

## Remaining gaps

- the cipher lines of ff. 406 and 410-411 have one blind reading each - blocker: not-attempted; next step, a second reading (the catalogue and line crops make it quick)
- signs the readers could not separate reliably: `y` (o) from Tomokiyo's y-sign, `a~` alone, `1`, `4` (about 200 signs, 3%) - blocker: illegible; values come from the copies
- three copy readings open (fol. 172v l. 24, 193v l. 24, 194v l. 24); "Gien-ne" (fol. 195v) not identified - blocker: illegible

## Escalation

- [x] siblings: f. 404 (twin of f. 406, partial interlinear) and f. 412 (twin of f. 410) identified
- [x] clear-pages: Brienne 13 fol. 171r and 193v located
- [x] known-keys: Tomokiyo's key for this cipher (src/henryiv_Maisse2.png) applied unchanged to six stretches (128 signs) of ff. 404, 406, 410 on 27 Oct 2026; it gives the copies' text (wainut/decode_check.py). The rest of the cipher is not yet transcribed; 11-12 Nov 2026 tested on both whole blocks (`beling/`)
- [x] print: Berger de Xivrey used to locate the copies
- [n/a] key-rebuild: the key exists (Tomokiyo); corrected and extended from the leaves (`beling/key/key_full.tsv`, 12 Nov 2026)
- [x] retry: 11-12 Nov 2026, both blocks transcribed; Tomokiyo's key 0.818 (fail); rebuilt key 0.894 on held-out lines (pass)

## Contribution by WAINUT (27 Oct 2026)

Contributed by WAINUT (https://github.com/WAINUTAI), a Dutch AI company. The work was done with AI language-model
agents, and the key lines were checked against the Gallica images a second time, independently; what rests on one
reading only is said below. The target and the Brienne 13 copies were found by Arya Sanketbhai Patel (PR #7); this
section builds on that. The text above is unchanged except the Status line, Remaining gaps and Escalation (review of PR #106). The new files are in
`wainut/`. In `profile.json` the two WAINUT `outcome.texts` entries replace the earlier f406/f410 entries (images only, decoded,
not read; the image links are kept in their notes), and `documents[].read`, class, method, gaps, credits and dated solution steps
are brought in line. The texts carry no `reading_review` grade: grading is left to a reviewer.

**Outcome: read in part, work in progress** (not a stopping point: the remaining pieces have no outside blocker). The two clear copies in Brienne 13 are transcribed through the enciphered passages, and
the start of each cipher block is decrypted with Tomokiyo's key against them. The cipher itself is not transcribed
in full: only six stretches (128 signs) of ff. 404, 406 and 410.

### Files

- `wainut/f406_brienne_copy.txt`, `wainut/f410_brienne_copy.txt`: the contemporary clear copies, line by line
  (Brienne 13 = NAF 6984 fol. 171r lower part to 172v; fol. 193v, 194r and the first lines of 194v).
- `wainut/cipher_lines.txt`: the cipher stretches, sign by sign, with the sign names.
- `wainut/f406_decryption.md`, `wainut/f410_decryption.md`: line-by-line decryption against the copies.
- `wainut/f406_reading.md`, `wainut/f410_reading.md`: the letters as running French text (from the copies), with
  the clear and the enciphered parts marked. `wainut/f406_translation.md`, `wainut/f410_translation.md`: English.
- `wainut/decode_check.py` (standard library) and `wainut/decode_check_output.txt`: decryption and controls.

### Findings

1. **The summary of f. 406 above describes the wrong letter.** "The Spanish insolence and the Pope; Pisany and
   Cardinal Gondi should not leave Rome ...; their entry among those of the League could breed division" is the top
   of Brienne 13 fol. 171r. That text is the end of **Maisse's own letter "Au Roy du dixiesme Avril 1593"**, whose
   heading is on fol. 170v ("Sire, J'escrivay d'aujourd'huy en huict iours ..."). Fol. 170v ends "il pourroit bien
   advenir que cette" and fol. 171r goes on "insollence des Espagnolz fist resoudre Sa Saincteté ...". The King's
   letter of 8 Feb begins lower on fol. 171r, under "Coppie de lettre du Roy audict sieur de Maisse de Chartres le
   huictiesme febvrier 1593 receue le viii.e Avril", with "Monsieur de Maisse j'ay tousiours faict responce a voz
   depesches ...".
2. **Where the cipher is.** f. 406 is mostly in clear. Its cipher block starts right after "faire des bons advis
   que vous y pouvez apporter", on the same line of the leaf, with "Le surplus de voz lettres est sur le subiect des affaires de Rome du
   voiage ..." (copy fol. 172r); this was checked on f. 406 itself and on its twin f. 404. A short run of cipher
   groups also stands on an earlier line of f. 406, inside the clear part; it is not decrypted. From the start of the
   block on, the copy of 8 Feb covers the following (where the cipher ends is not fixed, so not all of it need be in
   cipher): Rome; Pisany's journey and his arrival in Italy; the war in Piedmont and the new means Maisse found to
   help it; a letter sent through Lesdiguières' men and a further charge for Lesdiguières; Gondi at Nancy
   with the King's passport; the King going down to Saumur, where his sister is. On f. 410 the cipher starts right
   after "de ma bonne grace et faveur", with "L'experience a faict cognoistre ..." (fol. 193v). It covers the affairs
   of Rome; the advice not yet to let Cardinal de Gondi and the marquis de Pisany come back, so as to keep the Pope
   from extremes; leaving their moves to the Grand Duke's advice; Gondi's promises; and probably more (see below).
   The repository's summary of f. 410 covers only the part in clear.
3. **Tomokiyo's key reads these leaves.** Applied unchanged, it gives the copy's text on every stretch: f. 410 cipher
   ll. 1-2 (ratio 0.94 and 0.93 against the copy), f. 404 l. 3 (1.00), f. 406 cipher l. 1 (0.91) and two pieces of
   l. 2 (1.00 and 0.79). With 2000 random permutations of the key values no stretch gets above 0.67, and none of the
   four longest (13 to 39 signs) above 0.53. Values confirmed include 27/e, 29/x, 14/p, to/r, 19/i, 23/c, 24/g, 26/n,
   10/s, 8/r, 7/l, 16/m, 25/d, 5/u, 6/u, 1/o, y/o, the x-like sign = p, the omega-like sign = s, the d-shaped sign = t, the
   crossed 2 = i, the T-like sign = f, the z-like sign = a, and the word signs **15 = faict, 17 = vous, 18 = est**,
   *que* (a 9 with a straight tail), *des* (p with a stroke) and *de* (looped sign). The hooked q-like sign that
   opens both blocks is Tomokiyo's l (l column, row 2), not a new homophone.
4. **Variants between cipher and copy.** The cipher spells *cougnoistre* and has *que vous en avez* and the
   abbreviation *l[ett]res*; the copy has *cognoistre*, *que vous avez*, *lettres*, and repeats *estes* ("vous ne
   vous estes estes en rien trompé").

### Corrections made on the second look

The first sign-level alignment had errors, corrected before writing: on f. 404 the sign first read "9" is the uy
sign (u) and the "+" the theta-like d; on f. 410 "9t" is c (not n), what looked like one long-s sign is two signs
(e, n), and the z-like sign is a; the middle of *cognoistre* reads with the uy sign and the crossed 2. The short
cipher run in the clear part of f. 406 was first placed near "pour le regard du pape" and on the second look near
"... & puissance ..."; its place in the copy text is open.

### Still open

- In f. 410 l. 1, the three signs where the copy has *vous ne* decode as r u e: misread, or a word sign missing from
  the key. In f. 406 l. 2 the pi-like sign in *Rome* is r by the key (*rrme*), and the `+` in *voiage* is a by the
  key but i by the copy. All marked as holes.
- The rest of both cipher blocks (about 18 lines on f. 406, and the verso, canvas 458, if it carries cipher; about
  23 lines on f. 410) is not transcribed, so the decryption covers the first lines only.
- The copies: fol. 173r (end of the 8 Feb letter) and fol. 194v after its first lines are not transcribed; on
  fol. 194v the right edge was cut off in the view used. Where each cipher block ends is not fixed. Only the
  headings and the first cipher lines of the copies were checked a second time.

### Prior art

The contemporary clear copies in Brienne 13 are in effect the decipherment of the time; they were located by Arya
Sanketbhai Patel through Berger de Xivrey's citations (PR #7). Berger de Xivrey, t. III (1846), was not re-checked
here. We know of no printed decipherment of ff. 406 and 410; Tomokiyo published the key, not readings of these leaves.
