# Test plan, HStA Darmstadt D 4 Nr. 376/4 (catalogue 1637)

Written Mon 16 Nov 2026, 22:01 UTC (from `date -u`), by the lead AI agent, BEFORE any decoding and before either
helper transcription was made. Its sha256 is recorded in NOTES_darmstadt1637.md and in the hand-back.

## What the inventory has already shown (stated before the test, because it changes the test)

The whole file was fetched (102 images, 000-101) and viewed as contact sheets, and five pages were viewed
at full resolution (039, 040 both pages, 059, 068, plus Schröder's letters 022 and 023).

- The "continuous symbol script" of the vetting is, on every page I checked at full size, **ordinary German
  Kurrent handwriting**, heavily inked, with strong show-through from the other side of the leaf, and on
  several images (040 both pages, and others in the series) **photographed upside down** relative to the
  address panel. Rotated 180 degrees, image 040 reads as plain German ("...mich zu erkundigen habe bey dieser
  guten gelegenheit...", "...nach Stutgartt geschickt..."; left page opens "Durchläuchtige Fürstin,
  Hochgeehrte, Vielgeliebte ... Base und Tochter").
- The same hand signs image 059 and 068 "dienstwillige treue Base, Mutter und zu eigen ergebene Dienerin /
  Elisabetha Dorothea L[andgräfin] z[u] Hessen", i.e. Landgravine Elisabeth Dorothea (the regent, mother of
  Landgrave Ernst Ludwig) writing to her future daughter-in-law in 1687.
- The key page (image 100) is a reciprocal Latin-letter alphabet with numeral signs; the name table (image
  101) gives letters, numbers and two or three classical pseudonyms for persons of the **Württemberg court**
  (reigning duke, Duke Friedrich Karl, dowager duchess, reigning duchess, Fürst and Fürstin von Zollern ...)
  and places (Stuttgart = Tunis or Tripoli, Durlach = Roma or Athen ...).

So the test letter 040, as far as seen, contains **no cipher signs at all**. The test written in the task
("share of decoded cipher words that are real words") cannot be run on a letter without cipher words.
I therefore change the test now, before any decode, as follows. This is the one run; nothing is re-tuned.

## Test (one run)

**Material.** Image 040, both pages (the letter of Elisabeth Dorothea; both pages rotated 180 degrees), cut
into nine fixed strips (`helper_040/L_strip0-4.jpg`, `R_strip0-3.jpg`, made 21:59 UTC).

**Two blind transcriptions.** (1) A helper (Opus, medium effort) given only the strips and a neutral
instruction: transcribe word by word; mark any word that is not an ordinary German or French word, name or
abbreviation (any string of letters that makes no word, any Latin-script letter group, any isolated capital
letter or number used as a name, any classical name such as Apollo or Diana) with `{?...}`; mark illegible
words `[...]`. The helper is not told what the file is, that a key exists, or what I think the script is.
(2) My own pass over the same strips, done before reading the helper's output, flagging the same way.

**Measure 1 (is the letter in clear?).** Of all transcribed word tokens in pass 1 and pass 2, the share
that are German or French words, judged against the German and French word lists of the Eckert repository
copy (`output/eckert_local_update_2026-11-12/repository/lang/lexicons/de.json.gz`, sha256
2f4b4152...c424; `fr.json.gz`, sha256 f41eefdc...366f) after this normalisation fixed now: lower case;
ä->a, ö->o, ü->u, ß->ss; then a token also counts as a word if it matches after any of these period-spelling
rules: th->t, dt->t, ck->k, y->i, ey->ei, double consonant -> single, final -e dropped, u<->v, i<->j, c->k or
z, "ff"->"f". Abbreviations E.L., Ew., L., Hochfürstl. and the like, and proper names of places and persons
that are real places or persons, count as words. Pass mark for "the letter is in clear": at least 80% in
both passes.

**Measure 2 (is the key used in it?).** Every token flagged `{?}` by EITHER pass, and every token both
passes leave unknown, is decoded with the frozen key (file `key_frozen.json`, to be frozen from step B before
this run). The key counts as used if at least 80% of the decoded flagged tokens are German or French words
(same list and rules) AND 200 shuffled reciprocal keys (random pairings of the same 24 letters, seed 1637)
give at most 20% on the same tokens. If there are fewer than 5 flagged tokens, Measure 2 is reported as
"too few flagged tokens to test" with the tokens listed and each one's decode shown; no claim either way
beyond that.
Pseudonyms and place names from the name table (image 101) found in the letter are listed separately: one
found counts as the name table being used; none found counts as not used in this letter.

**What counts as a miss.** For Measure 1: a token that is not a word under the rules. For Measure 2: a
decoded flagged token that is not a word under the rules. Illegible tokens `[...]` are counted as misses in
Measure 1 (holes count by words).

**Reporting.** As the numbers fall. If Measure 1 passes and Measure 2 finds no use, the result is: the
letters are not in cipher; the key and name table are a separate item in the file.

## Screen of the other "cipher" letters (not a pass/fail test; recorded for the inventory)

For the remaining dense-script letters in the same hand (images 039, 041-059, 067-068, 080-081, 085-088), I
look at each at full size for: Latin-letter nonsense strings, isolated capitals or numbers used as names,
and table pseudonyms. Each is reported as "clear, no code seen" or with the item found. Schröder's
Württemberg reports (022-027), whose subject matches the name table, are screened the same way.
