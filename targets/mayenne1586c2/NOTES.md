# Mayenne–Forget's Cipher-2, 1586: BnF fr. 15572 ff. 218-219 and fr. 15573 ff. 120, 385 — NOTES

Status: in progress. Read in part, contributed: 86.1% of 5,293 cipher tokens fall in runs of period French (measured
here 21 Oct 2026), but the transcriptions are AI readings with no human sign check, calibrated at 75-93% per sign on
known text, and every gap below is still workable. Page: `docs/mayenne1586c2.html`.
**22 Oct 2026, reading audit** (George Lasry's test): ff. 218-219 read. f. 120 has holes in most sentences of c01-c05, c15-c19, c28-c31 and f. 120v c03-c05, and f. 385 is a self-declared partial unspaced decode: both *decoded, not read*. fraction_read 0.861 (tokens in sense runs) -> 0.404 (tokens in ff. 218-219).


**23 Oct 2026, re-read (REREAD_BRIEF, b21)**: f. 120 and f. 385 stay *decoded, not read*. No decipherment, clear copy or
print for either (Gallica views 244-249, 750-755); f. 121v is the cover of the f. 120 letter, addressed "Pour
Monseigneur de Villeroy", docket 1586. f. 120: the contributed reading checked word by word against the decode, the
cipher's spelling restored (it had been normalised), partly carried words bracketed: `f120_harumi/f120_reading.md`,
checker 0.50, explicit holes 0.647, but r c15-c19, c24-c31 and v c03-c05 still do not hold (log
`f120_harumi/f120_reread_log.md`; one line checked on the image shows 'finances' rests on a look-alike sign). f. 385:
Burford's literal decode divided and punctuated, `f385_burford/f385_reading.md`, 0.222 (log
`f385_burford/f385_reread_log.md`). Next: a sign-by-sign image round on those lines.

Created 21 Oct 2026 under the one-key rule (George Lasry, 14 Oct 2026) from three contributions in the same cipher,
**Mayenne–Forget's Cipher-2** (S. Tomokiyo, cryptiana *Henry III's Cipher with Ambassadors*). It is a different
cipher from Cipher-1 ([`targets/matignon1586/`](../matignon1586/NOTES.md), the Mayenne–Forget despatches of
fr. 15572) and from Matignon's Cipher-3 ([`targets/matignon1586c3/`](../matignon1586c3/NOTES.md)). Code numbers do
not carry across the three. Catalogue item 12 was narrowed to ff. 218-219 on 14 Oct 2026; it is closed with this entry.

**Outcome: read with known key (Tomokiyo's Cipher-2 table, checked and extended on letters deciphered at the time),
read in part, contributed.** Nothing in the readings is the project's: the work here is the review, image spot checks,
one measure for all three documents, and the write-up.

## The three documents

| document | Gallica | lines | tokens | read (measured) | contributor | how |
|---|---|---|---|---|---|---|
| fr. 15572 ff. 218r-219r, Matignon to Henri III, camp before Monségur, May 1586 | `btv1b9061879d` views 225 right, 226 | 26+34+19 | 2,138 | 1,856 (86.8%) | Harumi-Matsuba, issue #49 | Tomokiyo's table, one Claude pass, Codex cross-check on ff. 218v-219r |
| fr. 15573 f. 120r-v, sender and recipient unknown, autumn 1586 | `btv1b90618780` views 246-247 | 31+8 | 1,103 | 1,002 (90.8%) | Harumi-Matsuba, issue #51 | Burford's key, Claude transcription, independent Codex transcription |
| fr. 15573 f. 385r-v, from Mayenne's side, autumn 1586 | `btv1b90618780` views 752-753 | 34+34 | 2,052 | 1,702 (82.9%) | Brett Burford, issue #46 | Tomokiyo's table plus values from six deciphered letters, five voted Claude passes |
| **all** | | 186 | **5,293** | **4,560 (86.1%)** | | |

Measure: `to_read.py` puts both contributors' data in one line format (Burford: his signs through his key and the
value his decoder recorded at each two-valued sign; Harumi-Matsuba: his mechanical decode, upper-case runs as code
words, `[?]` unread), then `python ../matignon1586c3/f276/scripts/measure.py read_<doc>.txt 20`, the rule of
matignon1586/matignon1586c3: a token counts read only inside a run of at least three lexicon words totalling at least
ten letters (shared `lang` model `fr-1600-letters`, words seen 20 times). Shuffled keys (20): medians 10.1% (f. 385),
11.9% (ff. 218-219), 16.0% (f. 120), max 31%. **The measure counts sense, not correctness.** On text with a known
answer, Burford's reader was right on 93% of signs (f. 104r ll. 18-24), Harumi-Matsuba's f. 120 reader on 90.5%
(same lines, letter agreement 79.4%), and the ff. 218-219 pipeline gave 74.8% letter agreement on f. 103v ll. 1-6.

The contributors' data, under their licences (CC BY 4.0 for data and text, MIT for code), are copied to
`f385_burford/` (signs, per-page keys, French and English text, unresolved list, `other-letters.md`),
`f218_219_harumi/` and `f120_harumi/` (transcriptions, decodes, key, reading, open points, method). Their repositories:
[BravoBravoIX/mayenne-forget-1586-cipher-reading](https://github.com/BravoBravoIX/mayenne-forget-1586-cipher-reading)
(Zenodo 10.5281/zenodo.23470961),
[Harumi-Matsuba/matignon1586-public](https://github.com/Harumi-Matsuba/matignon1586-public),
[Harumi-Matsuba/mayenne1586f120-public](https://github.com/Harumi-Matsuba/mayenne1586f120-public).

## The key

Tomokiyo's reconstruction of Cipher-2 (cryptiana `henryiii_MayenneForget2.png`): homophonic signs for letters,
signs for syllables and common words (*de, la, que, qui, est, et, pour, plus, monsieur*; 23 *apres*, 24 *peu*,
31 *pas*), a slash as word divider. Burford checked it by aligning his reading of ff. 103v-104r (Mayenne to the King,
camp of Libourne, Sept 1586) with their decipherment of the time, then took code values from five more letters
deciphered at the time in fr. 15573 (ff. 7v-8r, 32r-33r, 97r, 149r-150r): `Qh` *armée*, `hb` *tout*, `N` *ée*,
17 *tant*, 13 *tre* and `ub` *droit* (the last two doubtful). Harumi-Matsuba used Tomokiyo's table for ff. 218-219
(inferring 27 = d, 17 = tant, barred h = armée, yy = encore and others; ten of them agree with Burford's key) and
Burford's key for f. 120.

Two conflicts between the contributors' keys, to settle on the images: the barred h is *armée* for Harumi-Matsuba,
while Burford splits two shapes, `hb` = *tout* and `Qh` = *armée* (Harumi-Matsuba's own calibration found the barred
h where the decipherment has *tous*); and the χ° sign, *q* in the table, stands where the decipherments have *pour*.

## What the letters say (the contributors' readings)

- **ff. 218-219, Matignon to the King from the camp before Monségur, May 1586.** The battery ran from dawn to sunset,
  about twelve hundred shots, with less effect than hoped: the wall was better than expected. Three breaches were
  made; Sacramore de Birague, on guard on the side of the breach, tried for the lodgement and was badly wounded. The
  young nobles were held back; from now on, step by step. The army is in need, as the sieur de Sailly has reported;
  something (code 36) must be brought from Brittany to last until the harvest; the forces shrink daily, and the pay is
  what matters most. Mayenne has a fever, but the physicians see no danger. The closing (*Sire, je supplie le
  Createur ... Du camp devant Monsegur ce ... May 1586*) and the signature *Matignon* are in clear.
- **f. 120.** "This prince" is more vexed than ever; the treasurer Bilart wrote that thirty thousand écus in gold have
  been ready for ten days; the Cardinal of Guise writes that five thousand are coming; not five but a hundred and five
  thousand would not set the army right. Biron cannot be kept; deputies of the army have come; papers of the secretary
  La Marsilière have fallen into "our" hands.
- **f. 385.** The army in Guyenne is breaking up at the start of winter 1586: not a thousand foot left, men asking for
  leave, no powder. What to do with the regiments and the foreigners over the winter; the landsknechts from Champagne;
  a company of light horse; Monsieur d'Halincourt, Monsieur de Matignon, La Roche, probably the young Aubeterre.

## Checked here (21 Oct 2026)

- fr. 15572 view 226: f. 218v has 34 cipher lines and f. 219r 19, then the clear closing and the signature *Matignon*,
  as Harumi-Matsuba describes. The date numeral is not read here.
- fr. 15573 view 246: f. 120r is wholly in cipher, 31 lines. A few small superscript marks stand over signs (for
  example *ar*, *Hx*, *ad*); neither contributor mentions them, and they may be partial glosses. Not examined.
- fr. 15573 view 752: f. 385r has 34 lines, the same sign inventory (barred #, ∴, //, figures 23, 30, 31) as ff. 218-219
  and f. 120, which supports one entry for the three.
- Not checked: any reading sign by sign.

## Prior work

- Tomokiyo lists ff. 218-219 ("Matignon"), f. 120 ("Endorsement illegible") and f. 385 as undeciphered in Cipher-2.
- For f. 385 he prints a fragment of the opening and **credits George Lasry** with finding that the letter is in
  Cipher-2. Burford's reading of the opening agrees with the fragment and was made without it. Whether Lasry read more
  of the letter is not known: ask him.
- The contributors found no other reading (searches of 18-20 Oct 2026). Harumi-Matsuba did not check DECODE or Lasry's
  publications. No DECODE record of them is known here; DECODE was not searched for them in this session.

## Remaining gaps

- code signs without a value: f. 385 14, 15, 30, invT (probably *vostre majesté*), x?; ff. 218-219 dotted K, 15, 19, 30, 36, dotted 9, dotted E, dotted χ°, ∻; f. 120 13 kinds in 15 places - blocker: no-key-material; most occur once, and the deciphered Cipher-2 letters Burford aligned do not contain them
- ff. 218-219: stretches that do not read (f. 218r ll. 10-12, 22, 25-26; f. 218v ll. 9-10, 21-22; f. 219r ll. 1-5, 12-17) - blocker: no-key-material; one AI reading pass calibrated at 74.8%; a voted second pass with Burford's sign sheet and image checks is the next step
- f. 385: 36 short stretches not read, 41 doubtful words - blocker: no-key-material; misread signs, names and abbreviations; Burford's planned second image round not yet made
- f. 120: short stretches and three values inferred in this letter only (ooo = *escus*, struck gg = *nous*, curled stroke = *o*) - blocker: no-key-material; no person has checked the transcription
- fr. 15573 f. 120: decoded, not read (90.0% of letters by the 95% rule after the 12 Nov 2026 image round, 89.4% sure only) - blocker: illegible; r c24-c31 read in part, 13 signs still doubtful between forms the hand does not separate (dudout/README.md), and the code signs with no value are in the code-signs line above
- fr. 15573 f. 385: decoded, not read - blocker: not-attempted; normalised partial reading f385_burford/f385_reading.md (b21, 23 Oct 2026: 0.222); the v0.2 unread stretches need the signs re-read on views 752-753

## Escalation

- [x] siblings: Burford aligned six letters in Cipher-2 deciphered at the time (fr. 15573 ff. 7v-8r, 32r-33r, 97r, 103v-104r, 149r-150r) for code values; both contributors calibrated their readers on ff. 103v-104r
- [x] clear-pages: ff. 218r and 219r carry clear opening and closing (used for date and sender); no clear copy of any of the three is known; the superscript marks on f. 120r examined 23 Oct 2026 (b21): cipher signs, not glosses; f. 121v = cover of f. 120, to Villeroy
- [x] known-keys: Tomokiyo's Cipher-2 table; the Cipher-1 key (matignon1586) and Cipher-3 key (matignon1586c3) are different ciphers
- [x] print: Tomokiyo's cryptiana list and his f. 385 fragment (credited to Lasry); contributors' web, GitHub and Cryptoole searches found nothing else; Lasry to be asked about f. 385
- [x] key-rebuild: code values from the deciphered siblings (Burford); values inferred in context (Harumi-Matsuba); conflicts listed under "The key"
- [x] retry: by the contributors: f. 385 five voted passes and image rounds on every unresolved stretch (Burford v0.1-v0.2); ff. 218v-219r 197 disagreements with a Codex transcription rechecked on the images, 19 corrected (f. 218r not reviewed); f. 120 differences with Codex checked on the image, 9 corrected. A voted second pass on ff. 218-219 is still open (in the gaps)

## Assumptions for George's review

- The three documents are one entry because Tomokiyo assigns all three to Cipher-2 and Burford's key reads them; the
  sign inventory looks the same on the images. ff. 218-219 are Matignon's, the other two from Mayenne's side.
- Outcome "read with known key" for contributed AI readings without human checks. The read fraction (86.1%) measures
  sense, not correctness; the calibrations (75-93% per sign on known text) are the only measure of correctness.
- Did you read more of f. 385 than the fragment Tomokiyo prints?

## Image round on f. 120, 12 Nov 2026 (Brice Dudout)

The 16 lines of f. 120 that the b21 re-read left open (r c15-c19, c24-c31, v c03-c05) were checked sign by sign on
Gallica views 246-247 at full resolution, against Harumi-Matsuba's transcription and with his sign names; the
re-read transcription and the doubtful signs were frozen by SHA-256 before decoding with this target's key. Eight
signs change (among them w -> w2 'il m'est tombé', 9 -> q+ 'spe[ci]alement', ls -> S 'au ser[v]ice', B -> 6b);
the rest of those lines agree with his transcription. One pre-registered measure on those lines (key unchanged):
0.903 against 0.909 for the earlier transcription, all 400 controls below. The second pre-registered criterion
(re-read at least equal to the earlier transcription) **failed** (0.903 < 0.909): the corrections rest on the sign forms and
not on a score. With the 95% rule (sure + probable; restored and unresolved letters are holes) the letter stands at
89.4% with the sure letters only (1,335 of 1,493), 90.0% with the 9 probable letters; the earlier sure + probable count was 88.3%; all under 95%: r c15-c19 and v c03-c05 now read as sentences ("quelque [comme]ndement et coniuration que vous [luy]
puissies faire de s'en aler ... si [tost] qu'il saura"; "L'on ne sauroit com{p}rendre l[e] tort que la rupture de
ceste armée faict au ser[v]ice du [Roy]"), r c24-c31 in part. Values used only from context in this letter (vbar =
comme, g8 = luy, Om = tost, I = Roy, Lp = p) are not added to the key. f. 385 was not attempted. Details:
[`dudout/README.md`](dudout/README.md).
