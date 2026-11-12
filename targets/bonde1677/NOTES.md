# Carl Bonde (Paris) to Charles XI, 24 Nov/4 Dec 1677: the cipher on image 489R (Riksarkivet, Diplomatica Gallica; catalogue 2317)

Status: read in part, contributed. Short text. No claim of a first reading (see Prior art).

Contributed by Malcolm McBratney (Brisbane), working with Claude (Anthropic). Issue #476 and its comment (blind second
transcription). This folder answers the request on that issue for the transcription, the frozen key, the decoder, the
decryption, the reading and translation with holes marked, and the shuffled-key control.

## What the document is

Stockholm, Riksarkivet, Diplomatica Gallica, SE/RA/2105/I/A/24/54, "Envoyén Carl Bonde, Brev till Kungl. Maj:t 1674-1678"
(image series R0003797; IIIF manifest `https://lbiiif.riksarkivet.se/arkis!R0003797/manifest`; viewer
`https://sok.riksarkivet.se/bildvisning/R0003797_00489`). A despatch of Carl Bonde, Swedish envoy in Paris, to Charles XI,
on images 488R-490L, dated "Paris d. 24 Novemb./4 Decemb. 1677" on 490L and signed. Swedish. The only cipher is on 489R:
17 short runs, 169 numbers, inside clear sentences. No gloss: the chancery's interlinear glossing in this volume appears to
stop about Nov 1677 (survey of images 379-557, b118).

| | numbers | word units | read (strict) |
|---|---|---|---|
| first transcription (b119), frozen 06:24:26 UTC, decoded once | 169 | 30 | 24 = 80.00% |
| blind second transcription (b127), frozen 09:35:28 UTC, decoded once | 169 | 30 | 23 = 76.67% |

Under the 95% bar: read in part. `counts.txt` lists every unit.

## The system and the key

The same homophonic number table as `targets/bonde1676` (Bonde and Lillieroot's French memorial of 6/16 Oct 1676 in the
same volume): numbers 19-178 for letters, up to seven for one letter, a few for ss, st, ff; word codes from about 250.

`key.tsv` is key v9, byte-identical to the file frozen on 12 Nov 2026 at 06:08:58 UTC (md5 af29e81f99e96f03663d94dea392e672,
164 rows), before 489R was transcribed. It was not changed afterwards. Its states (all in `gloss/key_history/`, all frozen
before 489R was seen):

| key | md5 | made from | tiers added |
|---|---|---|---|
| v3 | 8e1d93d1 | the 1675 chancery gloss on image 102R (A, B), 14 training lines and the test lines of image 324 of the 1676 memorial (F, P) | the key of `targets/bonde1676` |
| v4 | 8e6d8c77 | v3 + the values proposed after the memorial decode (Q) + 113 = k, 92 = i read off 327R (T) | Q, T |
| v5 | 12bcb08e | + 163 u, 146 k, 114 l, 158 s read from the decode of 327R (T) | T |
| v6 | 09e50de4 | + 127 w, 166 h, 96 w, 65 t read from the decode of 328L (T) | T |
| v7 | 63ddef1c | + 66 = y, 152 = w, 89 = l (T), declared after the 13/23 Oct 1676 decode | T |
| v8 | 9bda6437 | + only values read off chancery glosses of Nov 1676 (images 331, 334, 336, 341, 346): 176 ö, 63 k, 962 u, 335 E.K.M:t, 397 Konung | G, H |
| v9 | af29e81f | + only values read off glosses of 1677 (images 395, 429, 430): 131 r (replacing q), 434 ordinarie, 254 allierade, 478 tractat, 326 declaration, 479 tractera, 292 churfurst | G, H |

The gloss pairs behind tiers G and H: `gloss/gloss_pairs.tsv`. Those behind A and B (the 1675 gloss):
`targets/bonde1676/gloss/`.

Key lineage: one lineage with `targets/bonde1676`. v9 was made for Swedish text; the French memorial there is read with
v3 only. A later state, v10 (b122, 18 more gloss values, md5 f780c0f3), was made after this decode and is not used here.

Method class: key recovered from the decipherments of sibling despatches in the same file (glosses), with values read from
context in earlier decoded letters of the same table, then applied unchanged to a page held out from all of it.

## Corrections to our issue figures

1. **"Built only from the Swedish chancery's interlinear glosses" (the key field of #476) is wrong.** v9 also carries the
   values of tiers F, P, Q and T, read from context in the 1676 memorial and the despatches of October 1676 (table above).
   All were fixed before 489R was seen, so the test stays held out, but the key is not gloss-only. Counted by
   `scripts/build.py`: the 24 read units contain 149 cipher numbers, 90 with a value from the 1675 gloss (A 88, B 2), 1
   from a 1676-77 gloss (G), 58 from context (F 36, P 16, Q 5, T 1); 22 of the 24 read units use at least one
   context value; 2 rest on gloss values alone.
2. The figure stands: strict 24/30 = 80.00% as filed, and 23/30 = 76.67% on the blind transcription (our comment on #476).
3. The issue's "Decode as it fell out" shows `paeE` and `<418>en`; they are counted not read here as there (6 E units:
   ila, instäla, <418>en twice, paeE, <435>).
4. The issue gave one shuffle seed; both seeds are run here (0 of 5,000 each).

## What the passage says

The French court is much displeased: someone coming to Livonia and learning of Pac's opposition would delay and hold
back the [418] (march?) until the matter with Pac was settled, in the form of a vain negotiation; this has put the court
in alarm. To remove that, the French want nothing more than the designs, with a prompt diversion into [435] (Prussia?),
carried out to best advantage, and the King's Field Marshal to bring the [418] to ripeness as soon as can be, so that the
suspicions once formed are let go. The surrounding clear text was transcribed only next to the cipher runs, so the
sentences are broken by [...]. Pac is probably Michał Kazimierz Pac, grand hetman of Lithuania (our identification).

Swedish with holes: `readings/despatch_1677-11-24.md`. English: `translations/despatch_1677-11-24.md`.

## Checks

All re-run for this folder with `python3 -I` (standard library):

- `scripts/build.py`: decodes the first and the blind transcription with `key.tsv` (checks its md5), checks that each
  segmentation rebuilds the decode letter for letter, classes the units, counts the key-value sources, writes
  `decryptions/`, `units.tsv`, `counts.txt`, `holes.md`. Both decryptions are byte-identical to the session decode files
  (b119, b127). 24/30 and 23/30 reproduce.
- `scripts/compare_blind.py`: 168 of 169 numbers the same (99.41%); the one difference is 61 (first) against 67 (blind) in
  "alarme".
- `scripts/run_controls.py <Swedish corpus>`: 5,000 shuffled keys, seeds 20261112 and 7, Swedish character 4-gram model
  (w folded to v) from four Project Gutenberg texts (`controls/CORPUS.txt`), each asserted to carry "Language: Swedish";
  letter tiers A B F P Q T G scored. First transcription: true -3.1451, 0 of 5,000, best -4.0151 (seed 20261112, as filed)
  and -3.9637 (seed 7). Blind: true -3.3249, 0 of 5,000, best -4.1799 and -4.0673. Short text (165 scored numbers): the
  test is weaker than on a long one.
- The repository's checker scripts were not run by us (we treat downloaded repositories as data). The checks they make
  were verified by hand against the schema and CONTRIBUTING; see the pull request text.

## Remaining gaps

- Word codes 418 (twice, as "<418>en") and 435 (once) - blocker: open-codes; v10, made later from glosses, gives 418 =
  march and 435 = Preussen; not used, as v10 was built after this decode
- "ila" (illa), "instäla" (inställa), "paeE" (Paez, 46 a weak value) - blocker: open-codes; counted not read
- The clear text of 488R-490L is transcribed only next to the cipher runs - blocker: not-attempted
- Short text: 30 word units - blocker: too-short
- No person has compared the transcription with the image; both readers are model sessions - blocker: not-attempted
- Höjer 1875, Trolle-Bonde D.1 (1910), Grauers 1926 not seen - blocker: needs-physical-access

## Prior art (checked 12 Nov 2026): priority not established

- N. Wimarson, Sveriges krig i Tyskland 1675-1679, I-III (Lund 1897-1912): vols II and III read by the KB's OCR, vol. III
  through its register, every "Bonde, Karl" page read. He cites Bonde's despatches to the King up to 21/31 Jul 1677 and
  from 12/22 Jan 1678, in paraphrase; between those dates only letters to Bonde (Königsmarck) and Bonde's urgings to
  Christer Horn (III p. 189). On Pac, the Lithuanian passage and Horn he uses other sources (Lilliehöök, Béthune, the
  Horns). The events are known history; this text and its decipherment were not found in print.
- archive.org full-text search: nothing.
- NOT seen: Magnus Höjer, Öfversigt af Sveriges yttre politik 1676-1680 (Uppsala 1875), which Wimarson used for the Paris
  diplomacy of late 1677; Trolle-Bonde, Kongliga rådet och ambassadören grefve Carl Bonde D.1 (Lund 1910); Grauers 1926.

## Files

- `transcriptions/`: the frozen transcription (numbers as written, clear words in quotes, partly) and its doubts file,
  written before the decode; both byte-identical to stamped files.
- `segmentation/`: the reader's word division of the decode (`decoded=reading`, `!E` flags).
- `key.tsv` (v9, byte-identical to the frozen file); `gloss/gloss_pairs.tsv`; `gloss/key_history/` (v3-v8).
- `decryptions/`, `units.tsv`, `counts.txt`, `holes.md`: written by `scripts/build.py`.
- `readings/`, `translations/`.
- `second_transcription/`: b127 blind transcription (as written and in R-format), its segmentation (the b119 one with the
  single changed unit) and its freeze record.
- `controls/`: shuffle output, blind comparison, corpus list.
- `scripts/`: `build.py`, `shuffle_control.py`, `run_controls.py`, `compare_blind.py`; `original/` the session scripts.
- `timestamps/`: the stamp of 12 Nov 2026 06:25:27 GMT with a selection of the stamped files (`timestamps/README.md`).

The despatch of 17/27 Nov 1677 (images 479R-481R), decoded in the same session with v9 at 62/100 = 62.00%, is under our
threshold and is not part of this folder.
