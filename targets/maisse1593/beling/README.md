# Maisse 1593: Tomokiyo's key tested, a key rebuilt and passed on 84 new lines, the full construction, and the copies finished

Contributed by Andrew Beling, with AI agents, 11-12 November 2026.
This folder adds to `targets/maisse1593/` and changes nothing in `wainut/` or Daniel Bourdeau's files.

[V] = checked on the image or in output. [I] = inference.

## 1. What is here

| File | What it is |
|---|---|
| `PREREG.md` | the test, written before any leaf was opened, with one amendment (sample) and one scoring note, both made before any transcription came back |
| `key/tomokiyo_maisse2.tsv` | Tomokiyo's key read from `../src/henryiv_Maisse2.png`, with a name and shape for each sign |
| `transcription/f406r_cipher.tsv`, `f406v_cipher.tsv`, `f410r_cipher.tsv` (+ `_legend.md`) | three blind sign-by-sign transcriptions (one reader each, none saw the copies) |
| `transcription/brienne_173r_173v.txt`, `brienne_194v_196r.txt` | the rest of the two Brienne 13 copies, to the end of each letter |
| `transcription/copy_406_from_cipher_start.txt`, `copy_410_from_cipher_start.txt` | the copy text the test compares against (WAINUT's copies plus the new pages) |
| `scripts/test_key.py` | the test; `results/test_key_result.json`, `test_key_output.txt` (with the full mechanical decryption) |
| `scripts/explore_signs.py`, `explore_rescore.py` | analysis after the run, not part of the test; `results/explore_*.txt` |
| `results/frozen_inputs.sha256` | hashes in the order they were frozen |
| `PREREG_round2.md` | round 2: the key rebuilt from round 1 by a fixed rule, tested on lines nobody had transcribed |
| `catalogue/catalogue.md`, `catalogue/README.md` | one name per sign shape (89 signs), made blind to the copies; exemplar crops are not committed |
| `transcription/round1_catalogue/` | the round-1 files with sign names fixed on the leaves (198 tokens renamed, `changes.tsv`) |
| `transcription/round2/` | three blind round-2 transcriptions: f. 406v ll. 21-33 and f. 411v ll. 1-3 (d), f. 410v (e), f. 411r (f), with legends |
| `transcription/second_reading/` | an independent second reading of both Brienne copies and the collation (66 disagreements, 63 settled on the image) |
| `transcription/copy_round2_406.txt`, `copy_round2_410.txt` | round-2 copy text (`scripts/make_copy_round2.py`) |
| `key/key_v2.tsv` | key v2, built from round 1 only (`scripts/build_key_v2.py`) and frozen before round 2 was transcribed |
| `scripts/test_key_v2.py` | the round-2 test; `results/test_key_v2_result.json`, `test_key_v2_output.txt` |
| `key/key_full.tsv`, `key/construction_overrides.tsv` | the full construction from all lines (rule values, then judged values marked [I]) |
| `scripts/full_decrypt.py` | both letters decrypted in full against the corrected copies: `results/full_decryption.txt`, `full_variants.tsv` |
| `results/frozen_inputs_round2.sha256` | round-2 hashes, in the order they were frozen |
| `CHECKS.txt` | hash checks and second runs (rounds 1 and 2) |

Images: Gallica btv1b90074656 canvases 457, 458, 461-463 and btv1b100904592 canvases 177-179, 199-201, fetched with curl
from openapi.bnf.fr IIIF at full size; not committed.

## 2. The cipher is about four times longer than NOTES says [V]

- f. 406 (8 Feb): the cipher runs from "apporter" (leaf l. 23) to the foot of the recto (l. 43), and over the whole verso
  except the clear close ("Je prie Dieu ... 1593"): 54 lines (counted in round 2), not about 18. A short run of 18 signs stands inside
  the clear text on leaf l. 13.
- f. 410 (27 Apr): from leaf l. 10 to the foot of the recto (l. 31), all of f. 410v and f. 411r, and three lines of
  f. 411v before the clear close: 93 lines (counted in round 2), not about 23.
- The copy shows what they cover: f. 406's cipher is the copy from "Le surplus de voz lettres" (fol. 172r) to "priant
  Dieu" (fol. 173v); f. 410's is the copy from "L'experience" (fol. 193v) to near "priant Dieu" (fol. 196r) [I for the
  exact end on f. 411v].
- WAINUT's line numbers on f. 406 (l. 16-17) are 7 lower than the leaf's; they are leaf ll. 23-24.

## 3. The test [V]

Sample: f. 406r ll. 25-43, f. 406v ll. 1-20, f. 410r ll. 12-31 (58 lines, 2,501 signs), all past WAINUT's lines.
Key frozen from Tomokiyo's image; three blind readers; copy text hashed before the one run.

**Result: score 0.818 (406: 0.823, 410: 0.809); 200 shuffled keys mean 0.142, best 0.230; margin 0.589.
Fail by the pre-registered rule (score below 0.85), with a very large margin over chance.**

Where the sample ends in the copy: f. 406 at "de laquelle" (fol. 173v, l. 2); f. 410 at "suivant les promesses que
led." (end of fol. 194r). So the sample covers the copy from fol. 172r to the top of 173v, and fol. 193v-194r.

## 4. Why it falls short (after the run; exploratory, no pass/fail)

- **116 signs (4.6%) decode as unknown**: names the readers gave to shapes not in the frozen key (`Rbar`, `va`, `gam`,
  `k`, raised signs `^8` ...) and 10 illegible. Left out of the count, the score is 0.852.
- **One key identification is wrong on these leaves.** The sign the readers call `pi` (read r from Tomokiyo's row 3)
  lines up with o in the copy 40 times out of 74, and with r twice. With `pi` = o the score is 0.840, and 0.875 with the
  unknowns left out. This is WAINUT's open "rrme" for *Rome* (NOTES): the sign is o.
- **`x` covers two shapes.** It lines up with p 17 times and with a 26 times: probably the key's p sign and its row-4
  a sign (a small z/x-like stroke) were given one name [I].
- Smaller: `y` lines up with y 13 times (the key's separate y sign, `yy`, was not separated); several word signs (`MC`
  fort, `ct` avec, `a~` advis) do not match where they occur [I: misidentified shapes or variants].
- The copy and the cipher also differ in wording in places (WAINUT found "que vous en avez" against "que vous avez"),
  which costs a little whatever the key.

[I] Taken together: Tomokiyo's key reads these leaves (margin 0.59 over chance, and the mechanical decryption follows
the copy word for word through long stretches), but sign naming, not the key, keeps the frozen test under 0.85. A
second pass that fixes `pi` = o, splits `x`, and names the new shapes against the key image would need a new held-out
sample (f. 406v ll. 21-37 or f. 410v), since these lines have now been compared with the copy.

## 5. Copies finished [V, two readings]

Brienne 13 fol. 173r-173v (end of the 8 Feb letter) and fol. 194v-196r (the rest of the 28 Apr letter, replacing
WAINUT's partial 194v) are transcribed, and a second reader read fol. 172r-173v and 193v-196r again, blind
(`transcription/second_reading/`). The two readings disagreed in 66 places; 63 are settled on the image, 3 stay open.
The first readings (WAINUT's and mine) had about 20 word errors. The ones that change the sense:
- fol. 195r: the 20,000 écus were sent "aux presens de Leuant" (for the Levant presents), not "aux pensions de Pisani",
  and "le secours qui vous auoit este enuoye", not "le service".
- fol. 194v: "Je croy que la resolution a esté bonne d'en faire enleuer Lancosme", not "Je voy ... retirer".
- fol. 195v: "pour Gien-/ne pour vne fois seulement", not "bien-/tost [?]"; which place is meant is open.
- fol. 194r (WAINUT): "luy veullent persuader", "le grand duc luy enuoiera", "Au moings qu'ilz n'ayent".
- fol. 172v (WAINUT): "Aiant neantm. faict entendre", not "et i'ay neantmoins"; fol. 173r: "le terme a ma noblesse",
  "Comme ont volontairement offert ceux qui sont pres de moy", "Orez que"; fol. 173v: "Apres l'ouuerture", "Et y a".
Among what the pages add: the officers taking refuge at Tours to fund the garrisons round Paris for a year; Mayenne
gone to meet the foreign army under the comte Charles; the Paris assembly and the proposed conference; Lancosme sent
away and the fear of his escape; the Chaous and Signa; 20,000 écus for the Levant presents; and whether Lesdiguières,
staying in command, might let a Catholic lord carry the title in Piedmont. The round-1 copy files are left as hashed;
round 2 and the full decryption use the corrected text.

## 6. Round 2: a key rebuilt from round 1 passes on 84 new lines [V]

Plan in `PREREG_round2.md`, written before any round-2 line was transcribed. In order:
1. A sign catalogue made blind to the copies: one name per shape, every confusable round-1 token re-examined on the
   leaves, 198 renamed. The main fix: reader b had used `x` for two shapes; most are a separate sign (`k`).
2. Key v2 built mechanically from the renamed round-1 lines and their copy, by a rule fixed in advance (a sign in
   Tomokiyo's key keeps his value unless the copy clearly says otherwise; a new sign needs 3+ places and 60% agreement).
   Frozen by sha256 before round 2.
3. Three new blind readers transcribed every remaining cipher line: f. 406v ll. 21-33, f. 410v (33 lines), f. 411r (35
   lines), f. 411v ll. 1-3; 3,543 signs. They saw the catalogue, not the copies or any key values. Hashed on arrival.
4. One run against the round-2 copy text (first readings with the second reading's settled corrections).

**Result: score 0.894 (f. 406: 0.905; f. 410-411: 0.892); 200 shuffled keys mean 0.089, best 0.149; margin 0.745. Pass.**
Per reader: d 0.891, e 0.891, f 0.898. Unknown signs: 63 of 3,543 (1.8%). Tomokiyo's key on the same tokens: 0.801.

Where the cipher ends [V on the leaf, I for the match]: f. 406v at l. 33, on "contre la convocation et autres actes du
[duc du Mayne]"; the clear close starts at l. 34. f. 411v at l. 3, on "bien disposees"; the clear "Je vous ..." follows. In all, 54 cipher lines on f. 406 (ll. 23-43 recto, 1-33 verso)
and 93 on ff. 410-411 (410r ll. 10-31, 410v 33, 411r 35, 411v 3). The cipher covers the copy from its first words to
the end of the letter in both cases.

## 7. The full construction (after the test; exploratory) [V output, I where marked]

`key/key_full.tsv` is the key rebuilt by the same rule from all 6,223 transcribed signs of both letters against the
whole corrected copies; `key/construction_overrides.tsv` adds judged values where the rule stops short. With both,
0.908 of the decrypted letters match the copies (`results/full_decryption.txt`, line by line with the copy beside it).
- 43 of Tomokiyo's signs are confirmed (5+ places, 80%+ agreement; 5,033 signs); 13 of his signs never occur.
- Corrected: `pi` is o, not r (269 places, 0.95). The ζ-shaped `yy` is "et", not y (45, 0.89).
- New signs with values from the copies: `k` a (238, 0.90; Tomokiyo's row-4 a sign, drawn like a k); `6~` ss (32);
  `La` faire (22); `va` ll (12); `Cloop` g (11); `xd` uu (8); `arch` null (8); `Sr` and `qm` bon, `curl` leur (4 each);
  `Z3` don, `c` car (3 each).
- Judged [I]: `III a~` together = rr (8 places, always rr); `III` alone = moy (Tomokiyo's "mu"); `H` bien; `tt` grand;
  `Cm` touttesfois (once neantmoins); `Dc` aiant; `6b` a; `alpha` p.
- Still weak: `y` (o in 45%; the readers do not separate the o-sign from Tomokiyo's y-sign), `1`, `4`, `a~` alone,
  `9` (ceux), `mm`, `3`.
- Cipher and copy differ in wording in places (`results/full_variants.tsv`; most short stretches are sign misreadings).
  Real variants [I]: f. 411v l. 2 cipher "il est possible que Dieu pourra amener" against the copy's "peut estre que
  Dieu amenera"; l. 1 "ne les laisser prendre" against "ne laisser prendre"; f. 406v l. 31 "que font ceulx qui"
  against "qu'ont ceux qui". The copy is not a word-for-word transcript of this cipher.
- The short run on f. 406r l. 13 decrypts "pour que e regard des presens" [V output]; with `q~` (l) for the doubtful
  `que` it is "pour le regard des presens" [I], where the copy has "pour le regard du pape".

## 8. Open

- One blind reader per round-2 part; no second reading of the cipher lines in either round.
- `y` against Tomokiyo's y-sign, `a~` alone, `1` and `4`: shapes the readers could not separate reliably.
- Three copy readings stay open (fol. 172v l. 24, 193v l. 24, 194v l. 24), and "Gien-ne" (fol. 195v) is not identified.
- The catalogue's exemplar crops `y_1.png` and `Y_1.png` collided on a case-insensitive disk; only `Y_1` survives.
