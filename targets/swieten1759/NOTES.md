# Van Swieten to Cobenzl, Bonn, 14 Jan and 4 Feb 1759 (DECODE R956, R957): the 1759 table

Status: read (96% of groups, key rebuilt ciphertext-only)

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

## Remaining gaps
- code 232 (twice, R957), a name filed under G - blocker: open-codes; one name, sense of both sentences clear
- codes 147 100 126 148 (R956), the prince's name - blocker: open-codes; a name group, single occurrence
- codes 170 323 441 (R957) and 170 271 289 337 (R956) - blocker: open-codes; syllables read, words unresolved
- codes 290 313 316 313 373 (R956), the one marshal "qu'on estime" - blocker: illegible; digit division uncertain in the scan
- code 357 in R957 "supposition [pr] sans que" - blocker: open-codes; single awkward syllable

## Escalation
- [x] siblings: R955 opened (now swieten1757); its 1757 table differs; no other record in inv. 1236 on DECODE
- [x] clear-pages: no decipherment on R956/R957; the clear text round every 1759 run used as crib
- [x] known-keys: no key record for this series on DECODE; R955's table tried on 1759, does not fit
- [x] print: web search, local Tomokiyo/cryptiana copies: nothing printed
- [x] key-rebuild: monotone annealing (msolve.py) + hand correction rebuilt the 1759 table
- [x] retry: every unread group rerun against the final key and the alphabetical brackets
