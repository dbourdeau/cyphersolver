# Van Swieten to Cobenzl, Bonn, 14 Jan and 4 Feb 1759 (DECODE R956, R957): the 1759 table

Status: in progress (re-read 23 Oct 2026, b36: R957 now reads, class back to read; the site page and README row still describe the 22 Oct audit state and are left to the write-up pass)

**23 Oct 2026, re-read (REREAD_BRIEF batch b36, Claude Opus 5.5): R957 read from a contemporary decipherment that was on the DECODE record all along.** R957's fourth image (`IMG_R957_I4985_P4`) is a decipherment of its cipher passage on a separate leaf, in another hand; the decipherer wrote *232* above *France*. Transcribed (`R957_decipherment.txt`) and aligned group by group with the figures: they agree word for word once seven values of the rebuilt table are corrected, each at every occurrence (232 *France*, 327 *oc*, 131 *ay*, 170 *cr*, 323 *o*, 440 *y*, 316 *ni*; `key.json`, `overrides.json`); 327 and 440 close two of the table's seven order breaks. One encipherer's slip (357 *pr* for *-on* in *supposition*). "On procede toujours de la part des français dans cette Supposition, sans que nous ayons aucun ordre de la Cour"; "le Prince de Croÿ, qui y forme des pretensions". Reading `R957_reading.md`, English `R957_en.md`, log `R957_reread_log.md`; b17 0.571 -> 0.857. R956 gains *Crillon* (run 14, 170 271 289 337) and *Dumenil* (run 13). The key stays "recovered from ciphertext-only": it was rebuilt before the decipherment was seen; the decipherment now confirms it.

**22 Oct 2026, reading audit** (George Lasry's test: can sentences be built and translated?): R956 builds French sentences with scattered name groups open. R957 does not: "On promet (?) de toujours de la part des François" fails and "le prince de Con[...] [323 441] qui vous formez des prétensions" is garbled, so half its sentences have holes; R957 is *decoded, not read*. Class read -> read in part; fraction_read 0.962 -> 0.597 (estimated: tokens in R956). Both readings are excerpts: the cipher runs in full, the clear text around them in extract.

Earlier status (before the 22 Oct 2026 reading audit): read (96% of groups, key rebuilt ciphertext-only)

Split on 14 Oct 2026 from `../swieten1757/` under the one-key rule (George Lasry, 14 Oct 2026). The undated 1757–58
letter R955 uses an earlier table (202–586), read from its own decipherment: a different cipher with its own page
(`docs/swieten1757.html`). Moved here: `cipher/R956.txt`, `cipher/R957.txt`, `msolve.py`, `synth.py`, `dec.py`,
`key.json`, `key_auto.json`, `overrides.json`, `runs.txt`, `mk_validation.py`, `validation.tsv`; the readings of
R956/R957 are in `READING.md` here.

ARA Brussels, Secrétairerie d'État et de Guerre, inv.nr. 1236. Gottfried van Swieten (Bonn) to Count
Johann Karl Philipp von Cobenzl, Brussels. Letters in French with ciphered passages in numbers.

| Record | Folio | Date | Cipher |
|---|---|---|---|
| R956 | ff. 344–345 | Bonn, 4 Feb 1759 | ~20 runs of unseparated digits inside clear text, groups 100–442 |
| R957 | ff. 327–328 | Bonn, 14 Jan 1759 | 2 runs, 210 groups, 100–442 |

## Prior art

Nothing in print found (web search; local Tomokiyo/cryptiana copies have no van Swieten entry). DECODE
transcriptions by SofPe (2019) and XL (2020), marked non-decrypted.

## The 1759 key (rebuilt ciphertext-only)

A different table from R955's 1757 one (`../swieten1757/`), 100–442, but built the same way: an alphabetical list of letters and syllables with a few
word entries (nous, vous, pour, que, qui, comte, roi) and names filed alphabetically. Letter x = 438/439,
y = 441, z = 442 close the table.

Method: `msolve.py` anneals a non-decreasing map from each observed code to a sorted inventory of French
letters/syllables (at most 2 codes per unit), scored with `lang` model `fr-1750-nospace` (added for this
target) plus 1.5 per character. Validated first on a synthetic 274-token text encoded with a random
alphabetical table (recovered verbatim). On the real 491 groups, seed 5 of 8 random starts came out as
readable French ("la nouvelle convention…"); the other seeds did not. The key was then corrected by hand from
the clear text around each run (`overrides.json` over `key_auto.json` → `key.json`; `dec.py` prints the runs).
Four DECODE runs had dropped or doubled digits and were re-read from the images (runs.txt).

Counted: 553 groups in R956+R957, about 21 unread → 96%.

Correction (30 Sept 2026). R956 run 11, "le major (?) général des Liégeois de Vaut", is "le m[aréchal] général
des logis de Vaut". The groups, re-read on the image (IMG_R956_I4980_P2, seventh line of figures), are
291 300 241 315 375 289 181 294 238 281 180 428 420 399. The old reading needed 238 = ge before 239 = g (Broglio)
and 240 = ga (magazins), i.e. a ge homophone ahead of its section head, which the 1757 table never shows (its
second numbers sit beside or after the first), and "li-ge-is" is not a word. By position 238 is a second g, 294 (after 293 li, before 298 m) is lo, and with 281 is (four uses)
they give "logis"; 300 lies between 299 ma and 303 me, so mar... or a word entry "maréchal" (as comte, roi,
pour) rather than the "m" of the override. All three numbers occur once, so the new values are graded I (position and
sense). The order argument is not absolute: the rebuilt key still has seven breaks (147 bl in a name group,
283 s, 330 of after 327 om, 366 q before 367 pour, 395 ss after 392 su, 406 te after 405 ti, 440 vous after x),
but "maréchal général des logis" (the army's quartermaster-general) is a standard title and "logis" is the only
word the three groups make. key.json and overrides.json: 238 g (was ge), 294 lo (was li), 300 maréchal? (was m).
The officer is probably François-Eugène de Vault (1717-1790): a "mémoire de M. de Vault sur la situation des
armées en Allemagne en août 1758" is filed with Soubise's 1757-58 campaign papers (Service historique de la
Défense, ark 1016202); his post in 1759 is not verified. Lead, not applied: 232 lies between 231 fr and 238/239 g,
so by the same order it is filed under F, not G; "la France" fits both R957 contexts ("laisse les revenus à la
[232] en réservant la souveraineté à l'Impératrice"; "de la part de la [232]").

## Decrypt audit, 16 Nov 2026

The decrypt audit (`research/decrypt_audit/`) re-applied `key.json` to `cipher/R957.txt` and `cipher/R956.txt` and compared
the letters with `R957_reading.md` and `READING.md`: R957 3 of 76 words depart, R956 52 of 153 (34%). `key.json` gives a value
to every group of both files, and `cipher/*.txt` equals `runs.txt` group for group.

- R956, clear text in the reading file (most of the figure): `READING.md` prints the clear French between the cipher runs
  («…» marks the cipher), the two unread groups as numbers and an inline note on Crillon. Example: "Gu«eldre» avoient"
  after run 5. Nothing wrong.
- R956, letters changed or supplied inside «…» with no mark, 12 places: run 3 and run 16 "qu'il", "qu'on" (366 = q, no u);
  run 8 "pendant l'hiver" (189 = du, decrypt "pendant du hiver"); run 9 "le prince" (348 375 = p ra, decrypt "prance"; run 4
  has 348 378 = p ri); run 11 "officier" (330 267 = of ic, one f), "armée, excepté" (one e in the figures), "le duc de"
  (189 180 194 = du de e), "ignorant, et non" (375 315 400 322 = ra ne t non), "nécessaire" (315 160 210 194 = ne ch er e);
  run 15 "les maréchaux" and run 18 "les ordres" (292, 291 = le); run 17 "plaintes" (400 403 = t te). "Camille (?)" (decrypt
  camilis) and "m[aréchal] (I)" are marked.
- R957: the reading follows the contemporary decipherment, and says the figures agree with it word for word except at
  "supposition". Two more words differ: "les Revenus" (292 = le) and "beaucoups" (423 180 = up de, no s). In both the
  decipherer wrote an s the figures do not carry.
- `key.json` holds six entries that occur in neither text (53, 114, 282, 479, 505, 662; four of them outside the table's
  range 100-442), left from `key_auto.json`. Left in place: nothing in the folder says where they come from.

Nothing was changed in the key, the transcriptions or the readings: no value the readings use is missing from `key.json`,
and the wording is not edited here. The audit figures are the same after. Not checked: the groups against the DECODE
images, and whether any of the 12 places is a misread or mis-divided group rather than a slip of the encipherer.

Marked on 16 Nov 2026. `READING.md`, R956 section, 11 places inside «…», with [ ] round the letters or the word that `key.json`
does not give: q[u]'il, [l']hiver, pr[i]nce, of[f]icier, [e]xcepté, du[c], ignoran[t], [nécessaire], le[s] maréchaux, q[u]'on,
le[s] ordres. Two header lines added (what [ ] means; spelling inside «…» is modernised and the text between the runs is clear
text). No letter of the text changed. Left unmarked, 2 places where the reading drops a letter the key gives, so there is
nothing to bracket: "plaintes" (figures plainttes) and "duc de Broglio" (figures du de e broglio, the second e). Where the
key's word differs ("du hiver", "prance", "ne ch er e") the reading was kept and only marked; which of the two is right is
not settled. R957 is the decipherer's text, so nothing is marked inside it: the header of `R957_reading.md` and the R957 note
in `READING.md` now say it is not the output of the key and name the three words where the figures differ (supposition, les,
beaucoups). The same sentence on `docs/swieten1759.html` was corrected. `v2_score.py` hole rate: `READING.md` 0.076 before,
0.096 after; `R957_reading.md` 0.012 before and after.

## Remaining gaps
- codes 147 100 126 148 (R956), the prince's name - blocker: no-key-material; a name group, single occurrence, no decipherment of R956
- codes 290 313 316 313 373 (R956), the one marshal "qu'on estime" - blocker: illegible; digit division uncertain in the scan
- closed 23 Oct 2026 (b36): 232 = France, 170 323 441 = Croÿ, 170 271 289 337 = Crillon, 357 in "supposition" an encipherer's slip, and R957 runs 2 and 4, all from R957's contemporary decipherment (DECODE image 4)

## Escalation
- [x] siblings: R955 opened (now swieten1757); its 1757 table differs; no other record in inv. 1236 on DECODE
- [x] clear-pages: the clear text round every 1759 run used as crib; 23 Oct 2026 (b36) R957's fourth DECODE image found to be its contemporary decipherment (none for R956)
- [x] known-keys: no key record for this series on DECODE; R955's table tried on 1759, does not fit
- [x] print: web search, local Tomokiyo/cryptiana copies: nothing printed
- [x] key-rebuild: monotone annealing (msolve.py) + hand correction rebuilt the 1759 table
- [x] retry: every unread group rerun against the final key and the alphabetical brackets; 23 Oct 2026 (b36) R957 aligned with its decipherment, seven values corrected
