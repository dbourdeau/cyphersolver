# castelcicala1816: key.tsv checked against the contemporary glosses; R9571 and R9589 readings corrected from the code (Brice Dudout, Claude Opus 5.5, 14 Nov 2026)

## Decoder
`verify_dudout_20261114.py targets/castelcicala1816` reads only `key.tsv` and `transcripts/R*.txt` (not `apply.py`,
`corpus.py` or `reading_partial.txt`). For every `P:` gloss line it lists the groups below, their key value and grade.
Because the gloss words are not exactly column-aligned with the groups, the test is order-based: the largest set of
key values (letters only) found in the line's gloss letters in order and without overlap.

| grade | key values found in order in the gloss of their line |
|---|---|
| G (glossed) | 180 / 215 |
| X (glossed, second context) | 30 / 41 |
| I (inferred) | 54 / 70 |

The G/X misses are: the decipherer's abbreviations (`Minro`, `Cte di Cazes`, `Fra`, `Sigr`, `confer.za`, `Inghilt`);
groups he did not gloss (R9569 has a sparse syllable gloss, e.g. `arl`, `limi`); the end of a word carried to the next
line (R9589 `2318` = *ta* of *liberta*, `2352` = *fra* of *cifra*); and the faint pencil glosses on R9563. No G/X value
contradicts the gloss once these are set aside, except `1161` (*suo*): glossed *sua* in R9571 (*per la sua elevazione*)
and *suo* in R9589 (*nel suo Disp.*), so its value is *su-o/a*.

## Reading corrections (R9571, R9589)
Both readings are the decipherer's gloss joined into running text. The code groups under it, decoded with G/X values
only, settle the four places that were marked as holes or as odd:

- R9571 `Cardinale [?Vo...] Castiglione`: the groups are `2009 2211 1725 2295 | 2012 2448 1535 2169` =
  car-di-na-le | cas-ti-gli-one. No group is left for "Vo...": it is the decipherer's own unfinished word, not cipher
  text. Dropped.
- R9571 `al Pontefica[te]`: `1609 2448 2221 1951 2450` = pon-ti-fi-ca-to, *Pontificato* (the decipherer wrote
  "Pontefica" and struck a "te"; NOTES already gives pon-ti-fi-ca-to as an example).
- R9571 `tra la Francia. L'Austria per la elezione`: `2353 332 2231 383 1418 2231 1708` = Francia **e** l' Austria per
  l' ele(zione) (332 = *e*, 2231 = *l'*, both G). The decipherer's full stop is the *e* group.
- R9589 `[…] [?avuto] la liberta`: the line has five groups, `1450 2232 2357 1758 2318` = ? la li-ber-ta. *avuto* is the
  gloss of 1450, the only group left; the `[…]` counted 1450 a second time. Dropped (*avuto* stays doubtful).

`transcripts/R9571_reading.md`, `R9589_reading.md`, `R9571_en.md`, `R9589_en.md` corrected (a dated note is added
above `## Reading`).

## Read bar (README)
`v10_relabel.share`: R9571 0.961 (49 words, 2 holes) -> **1.0** (51, 0); R9589 0.974 (74, 2) -> **0.987** (74, 1:
`[?avuto]`). Both were read and stay read; `read_share` updated in `profile.json`. Class unchanged.

## Key notes (not corrections)
- `1050` = *ciò* (I) is doubtful: in R9571 *fatto ciò vedere* is `1553 1050 2268 1568 1836`, and `2268` = *ciò* is
  glossed twice elsewhere (R9571 *che ciò nuoccia*; R9563 pencil gloss *ciò(2268)*). Two groups cannot both be the one
  *ciò*; 1050 is more likely part of *fatto* (1553 1050 = fat-to?) or a null. `2268` could be raised from I to X.
- R9563 pp. 2-3 carry faint pencil glosses (transcribed as `P:` lines, notes of `transcripts/R9563.txt`), and R9561
  has two (*Collo stesso Corriere*, *che*). The re-read log and the per-record notes say no record beyond R9566,
  R9569, R9571, R9589 has a gloss. R9563's give candidate values not in `key.tsv`: 453 *avvisi*, 1378 *a*,
  1614 *sarebbe*, 497/1502 *politici*; the transcriber marks them uncertain.

Key correction: none written into `key.tsv`.

## Not done
Images not checked (DECODE R9553-R9589, not held). No new values added to key.tsv. The 23 decoded-not-read
despatches not re-read.
