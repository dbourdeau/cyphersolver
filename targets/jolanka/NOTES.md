# jolanka: Hungarian sign-alphabet postcards to Tóth Jolánka, 1911-1914 (Tobias Schrödel collection, DECODE)

Status: in progress. Key recovered from the ciphertext of six public cards and tested on a seventh held out; the text
is decoded, not yet read as sentences. Filed as a pull request at Malcolm McBratney's direction, 26 Nov 2026 AEST, with
the open items below stated rather than closed. Work by Claude sessions (claude-opus-5-5), 24-26 Nov 2026.
No person has checked the transcription, the key or the decode (AI-checked only). The site write-up is left to the
maintainers.

Credit: Malcolm McBratney (Brisbane), working with Claude (Anthropic).

Thanks to **Tobias Schrödel**, who owns the cards and put them on DECODE. He agreed by email on 25 Nov 2026 to this
work going on GitHub [stated, Malcolm's correspondence]. The cards are his; nothing here is a claim on them.

## Source
- [sourced] DECODE (de-crypt.org), collection of Tobias Schrödel: a series of 120 postcards named
  `cpc_..._jolanka-01` to `jolanka-120`. Search: https://de-crypt.org/decrypt-web/RecordsList?search=jolanka
  (121 rows on 24 Nov 2026: the 120 cards and one unrelated record, R3235).
- [measured] Owner Tobias Schrödel on 120 of 120 records; "Private Ciphertext" True on 120; access mode "Public" on 8,
  "Authentication required" on 112. Available Documents and Status empty on all 120 (no cleartext, plaintext, key or
  decryption filed). Counts from the 120 record pages fetched on 24 Nov 2026 (PRIOR_ART.md).
- [measured] Addressees on DECODE: Tóth Jolánka (Jász Arokszálas, now Jászárokszállás, and later Budapest) on 115
  cards; Holecz Ferenc, Rákospalota, on 4; Tóth József, Újpest, on 1. Dated 1911-1914 where a date is given
  [stated in the DECODE names; not checked card by card].
- The 8 public cards, the only ones this work could see:

| card | DECODE record | link | used as |
|---|---|---|---|
| jolanka-76 | R3524 | https://de-crypt.org/decrypt-web/RecordsView/3524 | training |
| jolanka-77 | R3525 | https://de-crypt.org/decrypt-web/RecordsView/3525 | training (lines 1-10 only) |
| jolanka-79 | R3531 | https://de-crypt.org/decrypt-web/RecordsView/3531 | training |
| jolanka-80 | R3532 | https://de-crypt.org/decrypt-web/RecordsView/3532 | training |
| jolanka-81 | R3533 | https://de-crypt.org/decrypt-web/RecordsView/3533 | training |
| jolanka-84 | R3529 | https://de-crypt.org/decrypt-web/RecordsView/3529 | training |
| jolanka-96 | R3526 | https://de-crypt.org/decrypt-web/RecordsView/3526 | **held out** (never seen by the solver) |
| jolanka-91 | R3527 | https://de-crypt.org/decrypt-web/RecordsView/3527 | not transcribed (faint pencil) |

Image ids, sizes and fetch details: IMAGE_ACCESS.md. No images are filed.

## System [derived]
A simple substitution with a drawn sign alphabet, Hungarian plaintext, no word division. Vowels are groups of bars
(two bars a, three bars e) with a dot or tick above for the long or umlaut forms (á, é, ő, ö, ü, i); consonants are
simple shapes (gamma t, reversed C s, F r, tilde l, two strokes n, three strokes m, zigzag g, S and 8 both k, figure 6
b, crossed x z, oval cs). One sign per letter; no abbreviation, so not a shorthand (Gabelsberger, Stolze-Schrey ruled
out by the result). 30 sign types occur in the transcription [measured]; the key gives 29 of them a value.

## Transcription (frozen)
- TRANSCRIPTION.tsv: 155 lines from the main text block of the 7 cards, one row per written line, signs as neutral
  shape labels (SIGNS.md, written before any solving). `?` = doubtful sign, `[.]` = one illegible sign, `[...]` = more,
  `{ }` = plain writing on the card (not cipher).
- Frozen 2026-11-24T11:19:28Z, before any key work (FREEZE_TX.txt; sha256 226dc81c... for TRANSCRIPTION.tsv,
  7c14f8bb... for SIGNS.md). First pass = figure of record. One reader (Claude), images at about 3000 px width, no
  second pass.
- Not transcribed: margin lines, upside-down lines, stamp-box lines and the crowded last lines under the address on
  every card; card 77 from line 11; card 91 entirely. Rough guess: a third of the writing on the 7 cards [unverified].
- Lengths [measured, `python docs/_check_profile.py --measure targets/jolanka/ciphertext/<file> --drop-first`;
  ciphertext/*.txt are derived by script from TRANSCRIPTION.tsv with plain writing, illegible marks and punctuation
  dropped]:

| card | signs | distinct |
|---|---|---|
| 76 | 380 | 27 |
| 77 | 204 | 24 |
| 79 | 467 | 24 |
| 80 | 430 | 26 |
| 81 | 454 | 27 |
| 84 | 241 | 25 |
| 96 (held out) | 619 | 26 |
| all | 2,795 | 30 |

  Training 380+204+467+430+454+241 = 2,176; held out 619; 2,176 + 619 = 2,795. Held-out share 619/2,795 = 22.1%.
  (The working report gave 455 for card 81 and 240 for card 84; the measured split above is the one of record. The
  totals agree.)

## Key and how it was recovered (ciphertext-only)
- key/KEY.tsv (also KEY.tsv at the folder root, the stamped copy): 29 sign types, one plain value each.
  Frozen 2026-11-24T11:28:06Z, before card 96 was decoded (FREEZE_KEY.txt; sha256 869cc149...).
- Solver (scripts/solve.py; SOLVE_LOG.md): simulated annealing over one-to-one sign-to-letter keys, scored with a
  Hungarian no-space 4-gram model, on the six training cards only. Run 1 failed (plain words leaked into the stream,
  and many-to-one keys collapsed to "tetete..."). Run 2 (seed 1), run 3 (seed 7) and run 4 (seed 20261112) all reach the
  same key, -3.9156 per sign (solve_out_seed*_fold0.json).
- Three values changed by reading the training decode, before the freeze (SOLVE_LOG.md step 5): EIGHT c to k
  ("kedves-", card 81 line 17), OVAL h to cs ("csak", "becses", card 80 line 2), V1 p to d ("edes", card 76 line 1).
  26 values from the solver, 3 from the training reading.
- Language model: none in lang/ was loadable on 24 Nov 2026 (lang/ registers `hu-modern` on the `hu-gutenberg`
  corpus, but the corpus was not cached and gutenberg.org returned 503). A model was built from 10 other Project
  Gutenberg Hungarian texts (ebooks 38494, 38673, 42071, 42286, 43029, 43653, 43746, 56460, 56591, 56592: Mikszáth,
  Ady, Bródy, Ambrus, Kóbor, Jókai, Benedek; 2.74 M letters without spaces) with scripts/build_hu_lm_ns.py. The model
  file (1.4 MB) is not filed; it can be rebuilt from those texts, or the controls re-run with `lm.load('hu-modern')`.

## Decode (DECODE.txt; scripts/decode_once.py, one pass with the frozen key on the frozen transcription)
The script checks both freeze hashes before decoding. `_` = illegible sign, `...` = illegible run, `#` = a sign with no
key value, `{ }` = plain writing. Held-out card 96, as the key gives it (no word division, nothing corrected):

```
1  szeretetédesjolankámédesegye        16 vemmikorbecsessoraitel
2  lenremenyemkivanomdogy              17 olvastemcsakeztsafnaltam
3  alegfobbegessegbentaláljaso         18 dogymiert_incsitazazan
4  raimsajnalattalveszem ...           19 gyalkaamelikesorokat
5  masuldogyutobbisoraojka             20 irjedogyszivemdezölal
6  sönvaleszoltamvolna                 21 detnemdogydagerezdetne
7  barénmikormegkadtamro               22 teljesenboldognagma
8  tönvalaszoltammart                  23 getdigyjeeledesemugyfj
9  aztdiszemédesemdogym                24 aszivemdogynemletda
10 gaisojotnedezenvarja                25 tomcsakaztszeretnemtud
11 soraimintamojennede                 26 nimedigkelmegazegyutle
12 zenvaromamagabecsesso               27 t#nkogazenarvaszivemnekó
13 rai_dogyjeeledesemszo               28 narbelenyugszikdogydaeg
14 valkisemledetfejeuniazt             29 ebölkelazt_etételeznid
15 azérzesemielfogtaszi
```

Gist [derived, unchecked; no Hungarian speaker has read it]: courtship cards from a man to Jolánka. Each opens
"Szeretett édes Jolánkám", wishes that his lines find her in the best of health ("a legjobb egészségben találja
soraim"), thanks her for her "becses sorait", asks her not to be angry, writes of his duty and work, and closes "Isten
vele édesem". Card 84 carries a plain-script address "czim Holes[?] Ferencz ... népszinház u 16 Asztalosok szakosz[...]";
four cards in the series are addressed to Holecz Ferenc at Rákospalota, which makes him the likely writer [derived, not
proven].

## Figures (per card, first pass, AI judge; never pooled across cards for the figure of record)
An AI judge (Claude; whether it ran isolated from the solving session is not recorded) scored every decoded letter of
judge/decode.txt under judge/BRIEF.txt, written before scoring: S = letter in a word that reads as Hungarian sense
(period spelling, missing accents allowed), E = the slipped letter in an otherwise readable word, N = no sense. In an
E word only the slipped letter is E; its other letters count S. No emendation. Results in judge/judge.tsv (with the
judge's word division per line), counted by judge/count.py [measured]:

| card | letters | S | E | N | S% | (S+E)% |
|---|---|---|---|---|---|---|
| 76 | 381 | 342 | 24 | 15 | 89.8 | 96.1 |
| 77 | 205 | 141 | 6 | 58 | 68.8 | 71.7 |
| 79 | 469 | 426 | 16 | 27 | 90.8 | 94.2 |
| 80 | 432 | 329 | 18 | 85 | 76.2 | 80.3 |
| 81 | 455 | 364 | 21 | 70 | 80.0 | 84.6 |
| 84 | 242 | 201 | 13 | 28 | 83.1 | 88.4 |
| **96 held out** | 623 | 520 | 30 | 73 | **83.5** | 88.3 |
| training (6 cards) | 2,184 | 1,803 | 98 | 283 | 82.6 | 87.0 |

- Figure of record: held-out card 96, S 520/623 = **83.5%**, over our own 65% line.
- Letters exceed signs because OVAL gives two letters (cs) and the judge counts letters (card 96: 623 letters from 619
  signs).
- The weakest training card is 77 (68.8%), just over the line. The lowest line is card 81 line 20 (0/17).
- The judge's word division is a working aid, not a reading: most lines still carry slips (h and p written as d; a/e
  and n/m confusions) and some runs with no sense.

## Controls (shuffle_out.txt; scripts/shuffle.py)
5,000 keys per seed, plain values permuted within the vowels and within the consonants of the real key, scored with
the same Hungarian 4-gram model as the solver (mean log10 per 4-gram) [measured]:

| part | real key | seed 20261112: best / mean / sd / shuffles >= real | seed 7: best / mean / sd / shuffles >= real |
|---|---|---|---|
| held out (619 signs) | -4.8454 | -5.8744 / -7.2380 / 0.3444 / **0** (6.9 sd) | -6.0819 / -7.2469 / 0.3477 / **0** (6.9 sd) |
| training (2,176) | -4.7586 | -6.0672 / -7.2158 / 0.3223 / 0 (7.6 sd) | -6.1757 / -7.2221 / 0.3265 / 0 (7.5 sd) |
| all (2,795) | -4.7784 | -6.0427 / -7.2208 / 0.3248 / 0 (7.5 sd) | -6.1697 / -7.2278 / 0.3288 / 0 (7.4 sd) |

- Held-out test: the key was frozen on the six training cards before card 96 was decoded; card 96 scores 83.5% S on
  the first and only pass, and its 4-gram score (-4.8454) is close to the training cards' (-4.7586).
- Not run: the same solver on a shuffled ciphertext (with its rank), which our own method asks for alongside key
  shuffles. Listed under Remaining gaps.
- Repository statistical test (docs/_validate.py): not run; it needs a Hungarian model in lang/, which was not
  cached here.

## Transcription doubts
- V1+a (all cards, 142 tokens) - read: one label; checked: decode; the decode wants h (hogy, 19 times in training), d
  (edes-, 12 times) and p (megkaptam) where this label stands, so the label merges at least three written signs. Not
  checked against the images sign by sign. The transcription is frozen, so it is not corrected: every h and p written
  with it decodes as d. A second transcription that splits the label must be a new frozen version.
- V2 for the d sign (several places, e.g. "cenveben" for kedvében) - read: V2 (n); checked: decode; not checked on the
  images.
- H2 against H3 (a against e) and V2 against V3 (n against m) - read: as transcribed; checked: decode (e.g. "mart" for
  mert, card 96 line 8); SIGNS.md lists them as known weak points; not checked on the images.
- TEE against CROSS (j against f) - read: two labels; checked: decode ("legfobb" for legjobb, card 96 line 3); may be
  one sign written two ways; not checked on the images.
- EX+aa (card 96 line 27, 1 token) - read: x with two dots; checked: decode (`#`, no key value; it does not occur in
  training); stays open.
- LC (3 tokens, read ó) - read: LC?; checked: decode; value unreliable on so few uses.

## Remaining gaps
- (a) 112 of the 120 cards cannot be seen: DECODE serves them only to accounts with the owner's permission - blocker:
  needs-physical-access (access is the owner's or DECODE's to grant). With the key, they would be routine to decode.
- (b) Card 91 (faint pencil), card 77 from line 11, and the margin, stamp-box and upside-down lines on every card are
  not transcribed - blocker: not-attempted (card 91 may be illegible at the DECODE resolution).
- (c) The V1+a label merges h, d and p; some d are read as V2 - blocker: not-attempted; needs a second, frozen
  transcription from the images.
- (d) No reading as sentences and no English translation yet; no person has read the decode - blocker: not-attempted.
  The texts are filed as "decoded, not read".
- (e) Blind second transcription by an isolated reader from the images only - blocker: not-attempted.
- (f) Solver run on shuffled ciphertext (overfitting control) and docs/_validate.py with a Hungarian model - blocker:
  not-attempted.
- (g) EX+aa on card 96 has no key value - blocker: too-short (one token; it does not occur in training).
- (h) Prior art in the owner's own books and talks, Hungarian philately forums, HathiTrust and Google Books full text
  not searched - blocker: not-attempted. Tobias Schrödel's HistoCrypt paper says 76 cards in his collection have known
  plaintext without naming them; he may hold a reading of this set (PRIOR_ART.md).

## Escalation
- [ ] siblings: the other 112 cards of the series are behind the owner's permission (gap a); the second Hungarian set
  in the collection (szomolya, 45 cards) not compared.
- [x] clear-pages: the plain-script lines on the 7 cards were read ({ } in the transcription; card 84's address names
  Holes[?] Ferencz); no key or gloss on any card seen.
- [x] known-keys: none on DECODE (Available Documents empty on all 120); none in the HistoCrypt paper.
- [ ] print: Schrödel's paper checked; his books and talks not checked (gap h).
- [ ] key-rebuild: the V1+a split (h, d, p) and TEE/CROSS need a new transcription pass (gap c); EX+aa open.
- [ ] retry: no second decode yet; the first pass stands as the figure of record.

## Files
- TRANSCRIPTION.tsv, SIGNS.md, FREEZE_TX.txt: frozen transcription and its freeze record.
- KEY.tsv, FREEZE_KEY.txt (and copies in key/): frozen key.
- DECODE.txt: the one decode. SOLVE_LOG.md: solver runs, failures included. solve_out_seed*_fold0.json: solver keys.
- shuffle_out.txt: controls. judge/: brief, decode as judged, judge.tsv, count.py.
- ciphertext/: sign labels per card, derived from TRANSCRIPTION.tsv for measuring.
- scripts/: copies of the working scripts (decode_once.py, shuffle.py, solve.py, decode_lib.py, build_tx.py,
  build_hu_lm_ns.py). They carry the working folder's absolute path in `B=`; set it to this folder (and give a model
  path) to re-run.
- stamps/: RFC 3161 (Sectigo, FreeTSA) and OpenTimestamps stamps of the working folder made 2026-11-24T11:37:44Z,
  after judging (label "jolanka-judged"; 177 files). From this folder, `sha256sum -c stamps/MANIFEST.sha256` verifies
  the 15 filed files that sit at the same path (TRANSCRIPTION.tsv, SIGNS.md, FREEZE_TX.txt, KEY.tsv, FREEZE_KEY.txt,
  DECODE.txt, SOLVE_LOG.md, shuffle_out.txt, the three solve_out files and the four judge files); the other entries
  are working files not filed (images, record pages, corpus texts, the model). PRIOR_ART.md was edited for filing
  (working paths removed), so its hash differs from the stamped copy.
- PRIOR_ART.md, IMAGE_ACCESS.md, profile.json.
