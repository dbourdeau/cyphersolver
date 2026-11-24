# cpp10a132: a cipher love charm in a medical miscellany, College of Physicians of Philadelphia Ms. 10a 132, pp. 75, 76 and verso of 76 (catalogue 2130)

Status: in progress. Contributed by pull request, not yet written up: the key was recovered from the ciphertext alone and the text deciphered in one frozen pass (strict judge 1105 of 1137 letters, 97.2%; held-out verso 408 of 428, 95.3%). By the README read bar, counted in words, the struck first start (p. 75) and p. 76 reach 95% and the verso does not (gutter losses), so the target is filed read in part. The page, ledgers and catalogue edit are left to the maintainers.

Contributed by Malcolm McBratney (Brisbane), working with Claude (Anthropic).

Provenance tags: [measured] = counted or hashed from the files in this folder; [derived] = worked out from them; [sourced] = from a named source; [stated] = given by the contributor's working session, not checked here; [unverified] = a reading of the text not checked by anyone else.

## The source

College of Physicians of Philadelphia, Historical Medical Library, Ms. 10a 132: a medical-pharmaceutical miscellany, Italy, first half of the 16th century, Latin, on OPenn (`cpp_10a_132`); Hirsch, *Catalogue of the Manuscripts and Archives of the Library of the College of Physicians of Philadelphia* (1983), no. 646 [sourced: OPenn TEI]. The book is paginated in ink ("75", "76"); OPenn's TEI calls the pages folios (75r, 76r, 76v). OPenn's only note on the cipher is "Fol.76 in cipher" [sourced].

| page (OPenn image, TEI label) | what is on it | cipher lines | cipher letters | split |
|---|---|---|---|---|
| p. 75 (6207_0112, "75r") | three struck lines of cipher, a first start of the same text; then clear Latin ear remedies | 3 | 100 | train |
| p. 76 (6207_0114, "76r") | cipher, the whole page | 21 | 609 | train |
| verso of 76 (6207_0115, "76v") | 13 lines + 2 lines in a large script, then a pen drawing of a winged head | 15 | 428 | held-out |
| total | | 39 | 1,137 | held-out 428 / 1,137 = 37.6% |

Letter counts are from `decode_once.py` (`decode_counts.txt`) [measured]: 100 + 609 + 428 = 1,137. `python docs/_check_profile.py --measure transcription_<page>.txt --letters --drop-first` gives 103, 624 and 431, because it also counts the letters of the clear numerals and the two sign labels: p. 75 103 - 3 (xij) = 100; p. 76 624 - 13 (iiij 4, iij 3, xx iiij 6) - 2 (S of S01, S02) = 609; verso 431 - 3 (iij) = 428 [measured, derived].

Images: OPenn web JPEGs and master TIFFs, URLs and md5/sha1 in `FETCH_LOG.txt`. The transcription was made from the master TIFFs of 6207_0112, 6207_0114 and 6207_0115 (sha1 matching OPenn's manifest). No image is committed.

## The system

Each letter is replaced by the next letter of the 23-letter Latin alphabet (a b c d e f g h i k l m n o p q r s t u x y z): plain a > cipher b, b > c ... h > i, i > k, l > m ... t > u, u > x, x > y (`KEY.tsv`). Word division is kept. Numerals are left in clear (12, 10, iiij, iij, xx.iiij, xij?, iij). Two ordinary scribal abbreviation signs occur inside the cipher (S01, a bar through the descender of p for "pro"; S02, the "-rum" sign) and are given no key value. Cipher letters in use: 20; a, l and z never occur in the cipher, so plain z, k and y are filled by the rule only [measured: `solve_out.txt`, `KEY.tsv`].

## Method

The pipeline is the contributor's (prior art first, frozen transcription and key, one decode, a separate strict judge, a shuffle control). Dates are 24 Nov 2026, Brisbane time.

1. **Prior art** before the transcription was frozen: `PRIOR_ART.md`. No key, decipherment, gloss or printed reading was found. See "Prior art" below.
2. **Transcription** from the OPenn master TIFFs, by a Claude session, one row per manuscript line, letters entered by shape, doubts marked with `?` (`TRANSCRIPTION.tsv`, conventions in `SIGNS.md`). Frozen with the train/held-out split at 19:27 AEST (`FREEZE_TX.txt`, sha256 of `TRANSCRIPTION.tsv` 093e18eb... and `SIGNS.md` 9251c42b..., both matching the files here) [measured].
3. **Limit on blindness.** The cipher uses ordinary letters, word-divided, and the system (each letter replaced by its successor) was recognised by eye while transcribing ("qfs" = per, "bnfo" = amen, "tboubn" = santam). The transcription is blind to a key (none exists) but not blind to the reading. The freeze records this. No letter was changed after the freeze.
4. **Held-out design.** Train = p. 75 lines 1-3 + p. 76 lines 1-21 (709 letters); held-out = the whole verso of 76 (428 letters), a different page. `solve.py` never loads the verso rows.
5. **Key from the train split only, two ways** (`SOLVE_LOG.md`, `solve.py`, `solve_out.txt`), with the Cyphersolver `la-letters` model (order 5, with spaces):
   - Statistics: 20 different letters; IC 0.0783 (Latin about 0.072): monoalphabetic.
   - A. Every shift in four alphabets (23 letters, 24 with v, 21 without k and y, 26 modern): best is a shift back by one, -2.444 per character, in the 23-, 24- and 26-letter alphabets alike; the 21-letter alphabet fails (k and y are used); next best -5.746, worst -8.813.
   - B. Free substitution with no shift assumed (hill-climb with annealing acceptance, 6 seeds x 8 restarts x 6,000 steps): 27 of 48 restarts converge on the same key at -2.444; the other 21 stall between -3.95 and -5.02 (failures, kept in `solve_out.txt`). The converged key equals the shift-by-one key in all 20 letters.
   - A first attempt with `lm.load('la')` failed (Gutenberg HTTP 503); `la-letters` was used instead.
6. **Key frozen** at 19:29 AEST (`FREEZE_KEY.txt`: `KEY.tsv` sha256 e712ee82..., matching the file here) [measured]; then **one decode** (`decode_once.py` -> `DECODE.txt`, `judge/decode.txt`). No emendations. The decode is the first pass and the figure of record.
7. **Separate strict judge** (Claude Opus 5.5): saw only `judge/BRIEF.txt` and `judge/decode.txt`; scored every decoded letter S (sense), E (one-letter slip in a readable word) or N (no sense) (`judge/judge.tsv`). `judge/count.py` re-adds it [measured, re-run 24 Nov on a copy at the path the script expects].
8. **Shuffle control** (`shuffle.py`, `shuffle_out.txt`): 5,000 shuffled keys per seed, same model, mean log-probability per character.

The scripts were run in the contributor's working folder: their paths (`/home/claude/keyless/...`, and a private copy of the repository's `lang/` at `/home/claude/keyless/_cs`) are left as they were. They do not run from this folder without changing those paths.

## Figures (first pass of record)

Strict judge, letters (`judge/judge.tsv`, re-added by `judge/count.py`) [measured]:

| page | S | E | N | letters | S share |
|---|---|---|---|---|---|
| p. 75 (train) | 96 | 4 | 0 | 100 | 96/100 = 96.0% |
| p. 76 (train) | 601 | 5 | 3 | 609 | 601/609 = 98.7% |
| verso of 76 (held-out) | 408 | 2 | 18 | 428 | 408/428 = 95.3% |
| all | 1105 | 11 | 21 | 1137 | 1105/1137 = 97.2% |

S + E + N: 96 + 4 + 0 = 100; 601 + 5 + 3 = 609; 408 + 2 + 18 = 428; 1105 + 11 + 21 = 1137. The judge's E words: cunm (x3, for coniuro), spiritui, materm, (s.)tui, digntus, resuracionem, aliqo, dicratur. N words: oue (p. 76 l.21, 3 letters), quaquoque (verso l.3, 9), _um (verso l.7, 2), quoqon_e (verso l.9, 7): 3 + 9 + 2 + 7 = 21.

Read share by words, the README read bar (`reading.md`, counted with `research/reading_audit/v2_score.holes`; clear numerals left out; `word*` slip words counted as read, as in the judge's E class) [measured]:

| page | cipher words | holes | read share |
|---|---|---|---|
| p. 75 | 21 | 1 | 20/21 = 0.952 |
| p. 76 | 130 | 3 | 127/130 = 0.977 |
| verso of 76 | 90 | 13 | 77/90 = 0.856 |
| all | 241 | 17 | 224/241 = 0.929 |

If the 10 slip words are also counted as holes: p. 75 17/21 = 0.810, p. 76 122/130 = 0.938, verso 75/90 = 0.833, all 214/241 = 0.888. The holes on the verso: 8 words cut by the gutter or a blot (person[...], rut[...] twice, biber[...], delectaci[...]one, es[...], [n]on, in [no]mine) plus [e]am, one lost word after preter, and the three N words (quaquoque, _um, quoqone) [derived from `reading.md`]. On p. 76 the holes are p[r]ofetas and angelo[rum] (scribal abbreviation signs with no key value) and oue; on p. 75 the blotted ange[...]rum.

Shuffle control (`shuffle_out.txt`) [measured]:

| split | real key | shuffles mean (sd), seed 20261112 | best shuffle | z | shuffles at or above real |
|---|---|---|---|---|---|
| full | -2.299 | -7.650 (0.517) | -5.692 | 10.3 | 0 / 5,000 |
| held-out | -2.062 | -7.625 (0.517) | -5.241 | 10.8 | 0 / 5,000 |
| train | -2.444 | -7.625 (0.538) | -5.725 | 9.6 | 0 / 5,000 |

Seed 7 gives z 10.2, 10.8 and 9.5, 0 / 5,000 each.

Repository validation (`python docs/_validate.py cpp10a132 --write`, 24 Nov, on `validation.tsv`: the 1,137 cipher letters of `TRANSCRIPTION.tsv` with their `KEY.tsv` values, the same pairs as `DECODE.txt`) [measured]: la-letters, order 4: reading -2.354 per letter; 200 random keys -6.758 (sd 0.578, best -5.290, z 7.6); a key annealed onto shuffled ciphertext best -4.381 (6 shuffles, z 131.4); the annealer on the real text from random keys reaches -2.354, the same key. Verdict: pass (recorded in `profile.json`).

**Repository sentence check** (`python docs/_check_reading.py cpp10a132`, 24 Nov) [measured]: 2 of 20 sentences clean in `reading.md` (0.10), hole rate 0.29, verdict "not a reading". Its Latin word list does not know the scribe's spellings or many common words of this text: 71 of the 176 distinct words of the file are missing from it, among them santam, santa, misa, mondi, paradixi, potenciam, uolontatem, adinplere, incarnacionem, natiuitatem, passionem, carnali, diligat, tangam, malignos and tu. With the spelling modernised in a scratch copy (sanctam, missa, mundi, voluntatem, verba ...), it still scores 8 of 20 (0.40): its list also lacks classical forms such as verba, virtutem, voluntatem, passionem and tu. The scratch copy is not filed. Counting only the file's own hole marks (`research/reading_audit/v2_score.py reading.md la`), 13 of 20 sentences are clean (0.65), hole rate 0.082. The reading is filed read in part on the word count above and on a reading review (in `profile.json`), not on the sentence check; the maintainers may judge otherwise.

## Gist [unverified: the contributor's reading of the decode, not checked against any edition or by a person]

A north Italian Latin love charm: a conjuration of the herb rue (ruta), with Italianate spelling (santam, paradixi, misa, mondi). "I conjure you, rue, in the name of the Father, the Son and the Holy Spirit, by holy Mary mother of our Lord Jesus Christ, by the 12 apostles, the 4 evangelists, the 3 patriarchs, the 24 prophets, the 10 choirs of angels and archangels, cherubim and seraphim, sun and moon, the stars, all the saints of paradise, the heavens, air and earth, the incarnation, nativity, baptism, fast, passion, cross, ascension and resurrection, by all the words said in the holy mass and all the good things of the world, by which you, rue, have the power to do all I wish." A second conjuration, "by the evil spirits", follows: the person the speaker touches with the rue is not to go, stand, drink, eat, sleep or take carnal pleasure with anyone but the speaker, and is to love the speaker alone while the rue is carried. The closing instruction: when the conjuration is made, gather the rue in the name of the person you want to be loved by, "and let it be said three times". English translation: `translation.md`.

Around it, in clear [unverified, read by the contributor's session]: on p. 75 below the struck lines, ear remedies ("Ad idem accipe amigdolas amaras ...", "Si granum vel lignum vel lapis ... in auribus cecidit"); on the verso of 75, "Item sucus rute cum sanguine anguille calidum auribus inmissus quemlibet dolorem auris statim tolit"; on p. 77 the same rue remedy again, then wounds and scrofula. The charm sits among remedies that use rue. No heading names it; the cipher pages carry no clear text but numerals.

## Catalogue corrections for the maintainers (catalogue 2130; not edited here)

- Extent: the cipher continues on the **verso of 76** (OPenn 6207_0115, TEI "76v"), 13 lines plus 2 lines in a large script. The vetting of 3 Nov 2026 recorded "f. 76v not viewed"; `folio_note` "ff. 75r, 76" should read "pp. 75 (3 struck lines), 76 and verso of 76".
- Kind: a **charm** (a conjuration of rue for love), not a recipe; `why` "A secret recipe" and the status sentence "Recipes are often simple substitutions" no longer fit.
- Status: key recovered from the ciphertext alone (each letter replaced by its successor), text deciphered: this folder.
- Count: 1,137 cipher letters on 39 lines [measured], not "about 850".

## Transcription doubts

Doubts were not settled against the image after the decode: by the freeze rule no letter was changed, and the doubts stay marked in `TRANSCRIPTION.tsv`. Each is listed with what the frozen key gives and whether that reads.

- d? (p. 75 l.2, tbod?uk) - read: d (c); checked: decode; gives "sancti". Image not rechecked.
- f? (p. 75 l.3, bohf?[...]sxn) - read: f (e); checked: decode; gives "ange[...]rum" (blot). Image not rechecked.
- p? (p. 76 l.3, bqp?tuxmpt) - read: p (o); checked: decode; gives "apostulos" (long s would give r: no sense). Image not rechecked.
- p? (p. 76 l.5, q<S01>p?gfubt) - read: p (o); checked: decode; gives "p[r]ofetas". Image not rechecked.
- p? (p. 76 l.5, dipsp?t) - read: p (o); checked: decode; gives "choros". Image not rechecked.
- b? (p. 76 l.7, tufmmb?t) - read: b (a); checked: decode; gives "stellas" (blot on the b). Image not rechecked.
- t? (p. 76 l.11, fkxt?) - read: t (s); checked: decode; gives "eius" (blot). Image not rechecked.
- e? (p. 76 l.13, e?khouxt) - read: e (d); checked: decode; gives "digntus" (c would give b: no sense). Image not rechecked.
- e? (p. 76 l.16, npoe?k) - read: e (d); checked: decode; gives "mondi". Image not rechecked.
- e? (p. 76 l.18, kuxe?kofn) - read: e (d); checked: decode; gives "(fort)itudinem". Image not rechecked.
- n? (verso l.7, [.]xn?[...]) - read: n (m); checked: decode; the word "_um" is unread either way. Open.
- x? (verso l.8, bmkrx?bn) - read: x (u); checked: decode; gives "aliquam". Image not rechecked.
- x? (verso l.9, rx?prpo[.]f) - read: x (u); checked: decode; the blotted word "quoqon_e" is unread. Open.
- s? (verso l.14, ekds?buxs) - read: s (r); checked: decode; gives "dicratur", a slip for dicatur: the doubtful letter is the extra one. Open.

## Prior art

`PRIOR_ART.md` (copied unchanged). Checked 24 Nov 2026, before the transcription was frozen: DECODE public search (Philadelphia, College of Physicians, coniuro, conjuration, charm: 0 rows each; "10a 132": 21 unrelated rows), the contributor's DECODE dump (0 matches), this repository (catalogue 2130 only, no folder, no PR), the OPenn record and TEI ("Fol.76 in cipher", Hirsch 646, no reading), web searches including "coniuro te ruta" after the system was seen (no hit on this text). Catalogue 2130's vetting of 3 Nov 2026 records Tomokiyo and Lasry/HistoCrypt as having nothing. **No earlier reading was found.** Not checked: Hirsch 1983 no. 646 (print only).

## Remaining gaps

- Line ends of the verso of 76, lines 2 to 12, hidden in the gutter of OPenn's photograph (11 line ends, about one to three letters each; 8 words of the reading cut, and one word after "preter" of unknown extent) - blocker: needs-physical-access; a flatter photograph or the book itself. Most are recoverable by sense; none was supplied as read.
- Two blotted words on the verso: l.9 "quoqon_e" and l.7 "_um" - blocker: illegible; heavy blots on the OPenn master image.
- Words that do not read in the decode: "oue" (p. 76 l.21) and "quaquoque" (verso l.3, quacumque?) - blocker: illegible; the key is complete and these are the letters as written and transcribed; only a check of the letters on the image or the book could change them (two of the 14 doubtful letters are in the blotted words).
- 14 doubtful letters (c/e and p/long s look alike in this hand), kept as transcribed, not rechecked on the image after the decode - blocker: illegible; listed under Transcription doubts; 11 give sense as transcribed.
- Scribal abbreviation signs S01 ("pro") and S02 ("-rum") inside the cipher have no key value and are counted as holes - blocker: no-key-material; they are ordinary scribal abbreviations, not cipher signs.
- Clear numerals: p. 76 l.4 "xx.iiij" has a blot in the middle (24, or a corrected 29?); p. 75 l.3 has "xij?" choirs of angels where p. 76 has "10" - blocker: illegible; clear text, not counted in any figure.
- Hirsch 1983, catalogue no. 646, not seen - blocker: needs-physical-access; print only. OPenn's note is drawn from it and says only that the leaf is in cipher.

## Escalation

- [x] siblings: the leaves next to the cipher (verso of 75, p. 77) viewed: clear ear remedies, the same rue remedy on the verso of 75 and on p. 77; no other cipher, no key, no gloss
- [x] clear-pages: the verso of 75 and p. 77 read for context; they are clear remedies, not a decipherment
- [n/a] known-keys: the key was recovered from the ciphertext (a shift by one); no earlier key exists to try
- [x] print: OPenn record and TEI; web searches for the charm's formula ("coniuro te ruta"): nothing; Hirsch 1983 not reachable (print only)
- [x] key-rebuild: the key is complete for every cipher letter in use (20 of 20); a, l, z do not occur
- [n/a] retry: the open words are gutter losses, blots and letters as written; a retry with the same key changes nothing without a better image

## Files

Copied unchanged from the contributor's working folder (sha256, first 16 hex) [measured]:

| file | what | sha256 |
|---|---|---|
| `REPORT.md` | the contributor's report (written before the judge ran; figures "pending" there are filled in above) | 737aea6bcc3a5bee |
| `PRIOR_ART.md` | prior-art searches | 4e4ec5c5f4382b3e |
| `FETCH_LOG.txt` | image and TEI URLs with md5/sha1 | 43c377d0cbf2446d |
| `TRANSCRIPTION.tsv` | the frozen transcription | 093e18eb61169dd9 |
| `SIGNS.md` | transcription conventions and letter shapes | 9251c42b991a63d1 |
| `FREEZE_TX.txt` | transcription freeze and split | 910d0e9e0781bfc1 |
| `SOLVE_LOG.md` | every solving run, failures included | 1cf58df269c91766 |
| `solve.py`, `solve_out.txt` | the two key recoveries on train | e5afb7199495caa7, 7d9f6d2e8777c4a6 |
| `KEY.tsv` | the key of record | e712ee82c4fd55e6 |
| `FREEZE_KEY.txt` | key freeze | e3cb7e3f13c2662f |
| `decode_once.py`, `DECODE.txt`, `decode_counts.txt` | the one decode (the decryption) and its counts | 0cda0de4e70d50c7, b99b25c890c39901, b01729df1c4595c9 |
| `shuffle.py`, `shuffle_out.txt` | shuffle control | 7e5915772251ba8b, 1e99ab671abce65c |
| `judge/BRIEF.txt`, `judge/decode.txt`, `judge/judge.tsv`, `judge/count.py` | the strict judge's packet, scores and adder | 46deb0311f3a9b55, 764b7e812cef8b19, 9e94ae45ca16c7b5, d21832ac97524c08 |

Made here (24 Nov 2026): `transcription_p75r.txt`, `transcription_p76r.txt`, `transcription_p76v.txt` (rows of `TRANSCRIPTION.tsv` split by page, unchanged, with a header line), `reading.md` (the decode as sentences, holes and slips marked, nothing emended), `translation.md`, `validation.tsv` (input to `docs/_validate.py`), `profile.json`, this file.

## Limits

- Model sessions did all the work: transcription, key recovery, decode, judge, reading and translation. No person read the signs or the text without AI.
- One transcription, not blind to the reading (see Method 3). The held-out page tests the key, not the transcriber's independence.
- The judge was a model session scoring sense by its own lights; its E and N calls are its own.
- The gist and the translation are unchecked.
