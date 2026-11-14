# lucca (R2159): image re-read, independent check of the key and of the reading's marks (Brice Dudout, Claude Opus 5.5, 14 Nov 2026)

## Decoder
`python3 targets/lucca/verify_dudout_20261114.py` reads only `texts/key.md` and `ct.txt` (not `decode.py` or
`validation.tsv`). 231 groups, 23 figures (after the correction below), every figure has a value. 226 of 231 decoded letters are in `plaintext.txt`
as written. Key correction: none; no new key value, so no held-out measurement is needed.

The decoder lists every place where `plaintext.txt` departs from the key:

| groups | key gives | plaintext.txt | marked? |
|---|---|---|---|
| 13–23 | *sransiuania* | *Transil[u]ania* | no: the supplied *l* is unmarked, the cipher *u* is in brackets, the *s* for *T* (19) is unmarked |
| 37–39 | *ogn* | *ogn[i]* | yes |
| 72–80 | *riuolsare* | *rivoltare* | no (19 = s where *t* is wanted) |
| 117–125 | *bogodania* | *Bog[o]dania* | the bracketed *o* is a cipher letter (13), not a supplied one |
| 170–187 | *letera al imperatore* | *lettera all'Imperatore* | no (normalised spelling) |
| 194–198, 213–216 | *facia*, *habi* | *faccia*, *habbi* | no (normalised spelling) |
| 217–225 | *humiliaso* | *humiliato* | no (19 = s where *t* is wanted) |

So the brackets of `plaintext.txt` do not mark what was supplied: two of the three bracket a letter that is in the
cipher, one supplied letter and the three 19 = t emendations (NOTES §3, profile 24 Sept 2026) are silent.

## Read bar
`research/reading_audit/v2_score.py` on `plaintext.txt` turns the three in-word brackets into holes: 53 of 56 words,
the recorded 0.946. A diplomatic text with the markers of v2_score (PR #565: `{+x}` supplied, `{-x}` dropped) gives the
cipher letters exactly (231 of 231) and shows every emendation:

> Al principe di {-s}{+T}ransi{+l}uania lo impedirò con ogn{+i} modo che il Turco non li dia aiuto, e farò
> riuol{-s}{+t}are contra di lui, se sarà bisogno, il principe di Bogodania, et li darò dumilia Cosachi, et manderò
> a uoi con una sua letera al imperatore che non facia pace fin che non l'habi humilia{-s}{+t}o o uinto.

Counts on this text (56 words):
- read from the key as written: 52 (92.9%);
- read with a one-letter emendation forced by the sense: 3 (*ogni*, *riuoltare*, *humiliato*);
- read with two emendations: 1 (*Transilvania*: 19 = s for *T*, *l* supplied);
- unresolved: 0.

`v2_score` scores it 1.0 (56 of 56, no hole). Under the README's strict word rule (a word with a corrected letter is
not counted, as for mauborgne1915 and duhart1921) it is 52 of 56 = 0.929; under the in-word emendation rule of
PR #565 it is 1.0. The class is not changed in this PR; the choice of rule is left to you. *Bogodania* is left as
written (a form of *Bogdania*, Moldavia), not emended.

## Images (DECODE R2159, P1 full resolution, 14 Nov 2026)
Seen with Brice Dudout's DECODE access; not copied into the repository, nothing derived from them is published.

- **Transcription.** The nine cipher lines of f. 18r compared group by group with `ct.txt` (read with `ct.txt` in hand,
  so not a blind pass): 230 of 231 groups agree. Group 79, in *rivoltare*, is written `3·21·7`, the same 21 as
  elsewhere, not `32`: `ct.txt` corrected. Figure 32, the "r = 32 once" of NOTES §4, does not exist; the key has
  23 figures and 21 = r occurs 15 times (`texts/key.md`, `validation.tsv` line updated; the 11 Oct scores not re-run).
  The letter is unchanged, so the reading is unchanged.
- **The two forms of 19.** The nine 19s are written either with a plain 1 (seven) or with a dotted 1, *i9* (two: the
  second 19 of *Transiuania* and *Cosachi*); the writer dots other 1s too (`i·15·ii`). The three places that want *t*
  (first 19 of *Transiuania*, *riuolsare*, *humiliaso*) all have the plain form, like four of the six that are *s*.
  The shape does not follow the value: there is no second sign hidden under 19, and the three *t* stay writer's slips.
- **The emendations above.** Checked on the page: no 11 (*l*) in *Transiuania* (`19·21·9·14·19 | 15·25·3·14·15·3`
  across the line end); no *i* after *ogn* (`18·2·14·12·13`); the *o* of *Bogodania* is written (`4·18·2·13·8`); one 22
  in *letera*, one 6 in *facia*, `10·3·4·17` *habi*. Every mark in the diplomatic text above matches the page.
- **The clear text of ff. 18–19** was not transcribed: it is in clear and outside the reading, NOTES §7 already
  gives its content, and a transcription from these images could not go into the repository.
