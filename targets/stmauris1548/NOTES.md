# Jean de Saint-Mauris to Ferrante Gonzaga, 1547-1548: cipher letters (Biblioteca Estense, Autografoteca Campori)

Status: in progress. Not yet written up: no site page or README row. Read in part, with escalation steps still open (see Remaining gaps and Escalation). The status below is the contributor's.

Status, 3 Nov 2026: **read in part.** The table is a homophonic substitution: one sign for one letter, and a few signs
for a doubled letter. Two letters are read in part; two are not transcribed. No contemporary decipherment of these
letters was found, apart from a reader's gloss over about six rows of c. 3r, so the reading is a break.
Contributed by WAINUT. The work was done with AI language-model agents. Separate agents made the sign transcriptions,
blind to each other and to any key. No human palaeographer has checked any sign.

**Headline: 340 of 435 words (78.2%) are verbatim decryptions.** The figures "with marked repairs" include letters
filled in from context; they are not "read".

| letter | file name | cc. | status | key used for the count | words | verbatim | with marked repairs | proposed | holes |
|---|---|---|---|---|---|---|---|---|---|
| 10 Jan 1548 | `l2` | 3r-4r | **read in part** | `key.tsv` (built on this letter) | 256 | 208 (81.2%) | 238 (93.0%) | 4 | 14 |
| 2 Aug 1548 | `l4` | 9r-9v | **read in part** (held out) | `key_frozen.tsv`, unchanged | 179 | 132 (73.7%) | 173 (96.6%) | 2 | 4 |
| 1547 | | 1r-2r | not transcribed | | | | | | |
| 12 Mar 1548 | | 5r-8v (cipher blocks) | not transcribed | | | | | | |

`l2` and `l4` are the second and fourth letters of the file. Counts come from `scripts/check_marks.py`. It rebuilds each
decryption from the transcription and the key, walks the French reading letter by letter and exits 1 on any unmarked
departure. Neither letter reaches the 95% verbatim bar.

For 2 Aug the count is with the frozen table, as the held-out test requires. `key.tsv` has values set after the test by
reading this same letter; with it, 160 of 179 words (89.4%) come out verbatim. That figure is **not a test** and is
given only to show what the later values change.

Before the fixes of 3 Nov (below), the independent check counted 200 of 255 (78.4%) and 133 of 178 (74.7%). The 10 Jan
figure rose because the fixed signs now read as written. The 2 Aug held-out figure fell by one word, because the
gamma-shaped sign that had been merged into `y` no longer takes a frozen value.

## Documents and images

Biblioteca Estense Universitaria, Modena, Autografoteca Campori, Lettera S, Saint Mauris (de), Jean. Estense Digital
Library (Lodovico) IIIF, CC BY-NC-SA; scans are not in git. Manifests: cc. 1-2 b70e7528-3bf3-46cd-b78d-a956fd528f6f;
cc. 3-4 7320ae85-1d75-4b1f-81ae-662ebae08782; cc. 5-8 65514839-924d-447b-962f-547fa30c0f7f; cc. 9-11
430bc92b-78c5-49be-b3c4-37e39090847d; cc. 22-23 cb2a1bd0-5e3c-457a-88b4-088942578c2d.

**cc. 22-23 is not a decipherment.** It is a clear news sheet in the form of the enclosure c. 10r ("ung billet
contenant les dernieres nouvelles"). On 23r, checked on a full-size crop: "...de la Royne d'ung second filz, lequel les
François dient debvoir estre duc de [?]...". Henri II's second son, Louis, was born on 3 Feb 1549, so the sheet is of
early 1549, after the last cipher letter. The duchy name is not read.

## The system

Homophonic substitution, no word division, about 60 signs in use. Several signs carry a raised mark (`3o`, `4o`, `12`,
`mx2`, `x3`), but the mark belongs to the sign; it is not a vowel indicator. For example, `3o` is t, `4o` e and `12` u.
Vowels have many homophones: e has `O 4o mx` and others, a has `mx2 eee y x`, u has `12 5o & N2`.

**Doubled letters.** An earlier version of this note said that doubled letters are written out. That is wrong for ll
and nn. `Le` (looped l + small c) is ll: represaille, iournellement, Excellence, conseiller, villes, aller. `Lo`
(looped l + small o) is nn: personne, donner, bonne. In 2 Aug, `N13` gives ss (ambassadeurs, passaige) and `N18` gives
ff (affin, affection, deffensive), from context only. Other doubles are written out: mm in "commandement" and
"confidamment" (`N4` + `N6`), ff in "proffist", ss in "passer". No nomenclator signs were found in these two letters.
The table is not the Charles V to Saint-Mauris key published by Pierrot et al. (HistoCrypt 2023).

**No sign for h yet.** Plain `x` reads a (Pignatel, mains, accrue, garde, cela, prealable) and h in three places
(Rochelle 3v L10, chemin 3v L17, hors 4r L03). On the crops the three h-places look like a rounder, more looped x, but
at this resolution the difference is not settled, so `x` is not split. `N19` (2 Aug only) may be h in "prochain"; it
is not settled either.

## How the key was obtained

1. Sign names fixed in `SIGNS.md` (shape descriptions only).
2. Letter of 10 Jan 1548 (cc. 3r-4r, 63 rows): two independent blind passes (`transcription_l2_passA.txt`,
   `transcription_l2_passB.txt`). They agree on 96.0% of 1,289 aligned signs. The 25 disagreements were settled by eye on
   crops (`merge_log.tsv`). Merged file: `transcription_l2.txt` (`scripts/merge.py`).
3. Ciphertext-only solve (`scripts/solve.py`): simulated annealing over sign-to-letter maps, scored with letter 4-grams
   of 16th-century French (Montaigne, Essais I, 1595 spelling, Project Gutenberg 48529, `scripts/ngram.py`). On the
   first transcription, three of ten random restarts reached the same best table, and its text read as French at once.
4. The contemporary gloss on c. 3r: a reader wrote one letter over each sign for about six rows. Read over row 2, it
   gives 15 sign values (`gloss_seeds.tsv`). The unseeded solve agrees on 13 of them. On `vt` the gloss seems to give a,
   the solve s, and "toutesfois" needs s. On `x` the solve gave e and the gloss a; the gloss is right ("Pignatel"). A
   solve with the gloss values held fixed scored worse (-4.38 against -4.22 per 4-gram) because it forces `vt` = a. So
   the gloss is an independent check of the solve, not its seed. The independent check read the same gloss and agrees
   with all 15 pairs.
5. Hand corrections from the reading, 9 signs: `b fz` f, `D/` d, `Le` c, `eo` q, `@` i, `8` q, `N1b` q, `x` a. Then the
   table was frozen as `key_frozen.tsv` (55 signs). It is kept unchanged.
6. After the held-out test and the independent check, the current table `key.tsv` was made. It gives each value's
   source and status (frozen, changed after the test, added after the test).

## Held-out test (2 Aug 1548, cc. 9r-9v)

A separate reader transcribed the letter blind (`transcription_l4_blind.txt`; 38 rows). That reader had no table, no
clear text and no other transcription. The frozen table was applied unchanged (`scripts/heldout.py`); rerun after the
fixes of 3 Nov:

| | 4-gram score per letter | share of letters in common French words |
|---|---|---|
| frozen table | **-4.171** | **0.218** |
| 200 shuffled tables (values permuted among signs) | max -5.189, mean -5.631 | max 0.075, mean 0.015 |

795 of 830 held-out signs (95.8%) have a value in the frozen table. Before the fixes the figures were -4.176 against a
shuffled maximum of -5.181. This is a statistical test of the table, not a check of the reading. The 2 Aug word counts
are graded against the solver's own reading; the only independent clear text on 9r is the later gloss "L on" over row
1, which matches "lon".

## Fixes after the independent check (3 Nov 2026)

The independent check (`VERIFY.md`, unchanged; it predates these fixes and names the frozen table by its working name `key_frozen_l2.tsv`) asked for the following. Each was
checked on 1x and 2x crops of the row images. New sign names are logged in `merge_log.tsv` (rows "fix") and in the
header lines of the two transcriptions.

1. **`8` held two shapes.** Of its 17 places in 10 Jan, 16 were viewed again on crops (3v L08 was not). Eight have a bar
   or hook on top and are now `N15` (b): 3r L17 (bien), 3v L01 (arquebusiers), 3v L20 (delibere), 4r L06 (tres bien),
   4r L14 (publiques, with a plain `8` = q beside it in "publiques"), 4r L08 twice and 3v L03 (marked doubtful); the
   last three are in holes. The check named five places; the crops show eight. Nine stay `8` (q). `N15` is the same shape
   as the 2 Aug reader's `N15`.
2. **`N6` is m, not e** (confidamment, comme, commandement, monsieur). Changed in `key.tsv`; the frozen file keeps e.
   It is q once (4r L03) and is not read once (3r L09, in "[?Rome]").
3. **`Le` held two shapes**, as above: `Le` (l + c) = ll and `Lo` (l + o) = nn. With that, "vices" (9v L05) reads
   "villes", and the hole at 9r L10-L11 reads "aller d'austant que". 9r L08 has a sign that is neither shape clearly
   (`L1`, no value); "cependent" there now rests on context. 4r L10 last sign looks like `eo` (q) on a 2x crop, not `Le`;
   changed and marked doubtful.
4. **`R` and `x`.** `R` reads g 6 of 6 in 10 Jan. The 2 Aug reader's `R` (9v L04, L06) is a different shape on the crops,
   an 8-like loop with a raised ring, and is now `N20` (x: eulx, ceulx, Excellence; 9v L12 not viewed again, marked
   doubtful). For `x` and h, see "The system" above.
5. **`y` and the gamma.** `transcription_l4.txt` had mapped the reader's `n` to `y` and also its separate gamma-shaped
   `y` to `y`. The gamma is now kept apart as `yg` (9r L02, 9v L16). It has no frozen value; by context it is e
   ("ie ne le scais", "ligue deffensive").
6. **Second blind pass of 9r L17-L18 and 9v: not done.** The agent that made these fixes had already seen the key and
   the decryption, so it could not read blind. This needs a fresh reader. Only 9r L01-L16 has a second blind reading
   (in the independent check: 11 shape disagreements in 376 aligned signs, all settled for the solver's reader).
7. **`check_marks.py`** no longer drops round-bracketed text silently: only place notes such as `(3r, after "...")`
   are skipped; any other bracket fails the check.

For the held-out figures, `check_marks.py` and `heldout.py` give `Lo`, `L1` and `N20` the frozen value of the blind
reader's own class (`Le`, `R`), because the frozen table was tested on that reader's classes. `yg` gets none.

**Solve rerun.** The fixed 10 Jan transcription was solved again from random starts (`scripts/solve.py`, 10 restarts,
seed 1). No restart returned the table. The best restart (solver score -4.090) is a text heavy in e, s and t that does
not read, and agrees with `key.tsv` on 60.8% of signs by count. The current table scores -4.182 mean 4-gram on the fixed
text, against a maximum of -5.383 for 200 shuffled tables. So the split signs are not confirmed by a fresh unseeded
solve. Their values rest on the earlier solve, the gloss and the reading.

## What the letters say (short)

- 10 Jan 1548: Cesare (?) Pignatelli and a reprisal; Dorsey sent a courier, who arrived on 16 December, and Gonzaga's
  enterprise against Mirandola. The count of Mirandola has had his guard increased by a hundred arquebusiers. The
  French fear a castle being built. About 1,500 soldiers are being sent from La Rochelle to Scotland, and the king is
  resolving to send a powerful army there again. There is some hope of peace between "these princes", and
  Saint-Mauris advises Gonzaga to temporise. Last, a captain Sebastiano of Finale. A hole at 4r L08 contains the
  letters "borbon"; it is not read.
- 2 Aug 1548: Henri II's journey into Piedmont, with ambassadors following the court, among them the Venetian. The
  French say they will hinder the passage of "monsieur nostre prince" (taken to be Prince Philip's journey to Italy,
  autumn 1548). Saint-Mauris thinks they cannot. Gonzaga should beware of surprise attacks on towns and guard his
  person. The journey is meant to put heart into the pro-French party in Italy. A defensive league has been
  negotiated, with money to be furnished on both sides for next year; the partner is lost in a hole.

**Historical notes not verified.** Dorsey, the Pignatelli identification, the La Rochelle to Scotland sailing and the
defensive league are checked only in outline. They must be verified before anything is published.

## Open

- A second blind reading of 9r L17-L18 and all of 9v.
- Holes: 14 in 10 Jan, 4 in 2 Aug. Signs with no value: `N19` (3 places), `L1` (1). The 2 Aug values set after the test
  (`N12`-`N18`, `N20`, `yg`, `Lo`) have not been tested on a further letter.
- `x` against h, and 3v L08, on better crops or the full-size images.
- Letters of 1547 (cc. 1r-2r, glosses on 1r, 1v and 2r) and of 12 Mar 1548 (cipher blocks on 5r-8v, with a clear note
  in the margin of 5r): not transcribed. They are the natural next test of the table.
- cc. 12-21 not checked at full size.

## Prior art (3 Nov 2026)

Not in Dan Bourdeau's catalogue, leads, decode queue or open PRs. Web searches (Saint-Mauris, Gonzaga, Tomokiyo,
cryptiana; in the independent check: Saint-Mauris, Ferrante Gonzaga, 1548, cifra, Estense, Campori) find no edition or
decipherment of these Estense letters. They find Pierrot, Desenclos et al., "Deciphering Charles Quint (A diplomatic
letter from 1547)", HistoCrypt 2023, doi 10.3384/ecp195704, which covers a different table. The check also found
British Library copies of Saint-Mauris's letters to Covos (June 1547 to October 1548), which might give related clear
text; not opened.

## Files

`SIGNS.md`; `transcription_l2_passA.txt`, `transcription_l2_passB.txt`, `merge_log.tsv`, `transcription_l2.txt`;
`transcription_l4_blind.txt`, `transcription_l4.txt`; `key.tsv` (current), `key_frozen.tsv` (frozen),
`gloss_seeds.tsv`; `VERIFY.md` (the independent check, unchanged); `decryption_l2.txt` (current key), `decryption_l4.txt` (frozen key),
`decryption_l4_current_key.txt`; `reading_l2.md`, `reading_l4.md` (French with marks, English, notes); `scripts/`
(`fetch.py`, `bands.py`, `lines.py`, `ruler.py`, `compare.py`, `merge.py`, `ngram.py`, `solve.py`, `read.py`,
`show.py`, `heldout.py`, `check_marks.py`). `model/quad.npy` is rebuilt by `ngram.py` and is not in git. No images are
included.

## 14 Nov 2026 full-texts audit

The full-texts check reports the letters of 1547 (cc. 1r-2r) and of 12 Mar 1548 (cc. 5r-8v) as documents without texts. That is true and stays so after this pass: neither has a sign transcription, so there is nothing to decode with `key.tsv`. The Estense manifest of cc. 1-2 was requested once and answers (HTTP 200), so the images are reachable with `scripts/fetch.py`; the blocker is the work, not access. The cipher is graphic signs (about 50 shape classes, `SIGNS.md`); the two letters that are read each took two blind passes and a merge (`merge_log.tsv`), and a single unchecked pass over 11 more pages would not be a faithful transcription. No entry was added to `outcome.texts` for them, so that the list does not point at files that do not exist. What closes it: two passes of cc. 1r-2r and of the cipher blocks of cc. 5r-8v with the names of `SIGNS.md`, then `scripts/read.py` with the frozen table; the glosses on 1r, 1v and 2r typed as the contemporary decipherment.

## Decrypt audit, 16 Nov 2026

`research/decrypt_audit/audit.py` re-applies the key file named in the profile to each transcription and compares the
letters with the reading. It flagged this target: 26 of 232 compared words depart in 10 Jan and 35 of 169 in 2 Aug
(61 of 401). Nearly every departure was a letter n in the reading that its decrypt did not give (12 of 15 unmarked
gaps in 10 Jan, 10 of 13 in 2 Aug).

Causes, checked on the files:

- **Audit artefact, the sign `#`.** The key files hold the row `#<TAB>n` (the double-barred cross of `SIGNS.md`). The
  audit script drops every line that begins with `#` as a comment, so it had no value for that sign: 31 places in
  10 Jan and 36 in 2 Aug. Example: the signs give "tun pure represaille" (3r L04), the script's decrypt gave "tu pure".
  The scripts of this folder skip only lines that begin with `# ` (hash and a space) and do read the row; so do
  `decryption_l2.txt`, `decryption_l4.txt` and `decryption_l4_current_key.txt`, which hold the n.
- **Audit artefact, the doubt suffix.** 9 tokens of the transcriptions carry a `?` (`N15?`, `eo?`, `Le?` twice, `L1?`,
  `N4?`, `3o?`, `N20?`, `x3?`). The loader of this folder strips it; the audit script does not, and finds no value.
  Example: `N4?` (9r L09) is m in "Piedmont".
- **Audit artefact, the key of 2 Aug.** The profile named only `key.tsv`. The reading of 2 Aug is marked against
  `key_frozen.tsv`, with `Lo` and `L1` taking the frozen value of `Le` and `N20` that of `R` (a rule that is in
  `scripts/check_marks.py` and in "Fixes after the independent check" above, not in a key file).
- **No unmarked emendation was found.** An own snippet (not a script of this folder) rebuilt the three decryptions
  from the transcriptions and the key files: all three equal the files. It then walked the `## French` section of each
  reading letter by letter: 10 Jan against `key.tsv`, 1,286 letters, 0 unmarked departures (12 `{r/s}`, 7 `{+r}`,
  15 `{-s}`, 4 proposed words, 14 holes); 2 Aug against `key_frozen.tsv` with the parent classes, 830 letters,
  0 unmarked departures (47 `{r/s}`, 3 `{+r}`, 3 `{-s}`, 2 proposed, 4 holes).

Changed: `profile.json` `outcome.key_file` now lists `key.tsv` and `key_frozen.tsv` (both already in the folder; the
second is the key of the 2 Aug reading); one comment line added to `key.tsv` saying that the row `#` is a sign, not a
comment. No key value was added or changed, and no reading, decryption or transcription was touched.
`key_frozen.tsv` is unchanged.

After: the audit script still prints 26 of 232 and 35 of 169, because it still skips the `#` row; that needs a change
in the script, which is outside this folder. With the row read and nothing else changed, the same comparison gives
1 of 234 words (10 Jan: "quelque", 4r L10, token `eo?`) and 5 of 170 (2 Aug, `key.tsv`: tokens `L1?`, `N4?`, `3o?`,
`N20?`, `x3?`), all from the doubt suffix.

Not checked: the signs against the images, and whether any marked repair is right. The parent-class rule for the
frozen values of `Lo`, `L1` and `N20` is still not recorded in a key file.
