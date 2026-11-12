# Noailles (Venice) to the Cardinal de Lorraine, 13 Nov 1558 (BnF fr. 3151 no. 33): catalogue no. 10 (part)

Status (12 Nov 2026): read in part. Michael Brackx (issue #113) transcribed the three cipher blocks and recovered the key
from the marginal decipherment of the time (key recovered based on adjacent plaintext, contributed); his decode is
reproduced here by `check_brackx.py`, his transcription was checked on the images by Andrew Beling (PR #423), and the
profile was brought into line on 12 Nov 2026 (see "Integration check"). Counts, from the files: 272 sign tokens, 12 nulls,
260 non-null, 244 with a value (93.8%), 12 of those on tentative values. Open work: the f. 60v gaps C2, C4 and C5, where
cribs from the gloss exist and do not yet meet the decode.

Split on 14 Oct 2026 from `../guiche1551/` under the one-key rule (George Lasry, 14 Oct 2026). Catalogue item 10
grouped this letter with La Guiche's Rome letter of 1551 (`../guiche1551/`, a 22-sign substitution) and Seure's
Lisbon letters of 1558 (`../seure1558/`, homophonic with numeral codes). Each is a different cipher with its own page.
Worked 2026-09-21 (Claude Opus 5) as part of the joint entry.

## The letter

Gallica btv1b9059865k, views 60–62 (ff. 59–60v). The letter is in clear (Levant galleys, Candia, Corfu) with
**three cipher blocks sharing one key**, in a symbol alphabet different from La Guiche's:

- **A and B**, three lines each on f. 60r (view 61). **The court's decipherment is written beside each block in the
  inner margin**, but the binding has swallowed the start of each gloss line. Gloss A: "… mauluaise … e pauur[eté] /
  [cond]uitte q[u'il] donne a / … affaires"; gloss B: "[gr]and seigneur / [entre]prend sur luy et le / … / de la
  Tou[ss]aint".
- **C**, seven lines on f. 60v (view 62, left page), from after "… a dommaige" to before the clear "tant en Hongrie
  qu'[en] / Italie". Its decipherment of the time stands in the **outer** margin and is nearly complete ("… pour le
  singulier / plaisir … proffit / qu'ilz ont … / … plus hardiz ny / … ravitailles qu'ilz / … osté aux aultres / …
  passées tant en / Hongrie …"). Found by Michael Brackx (issue #113, 27 Oct 2026); checked here on
  `research/gallica_sweep/hi/k62.jpg`. Our first notes counted two blocks only.

272 sign tokens in all, counted from Brackx's transcription file on 12 Nov 2026 (see "Integration check"; the "262" of
his first post and of our earlier notes was a count at another round of his work). The earlier figure, "about 150
signs", was an estimate by eye for A and B only.

**Gloss readings corrected (27 Oct 2026).** The first notes quoted "gouvernement" (gloss A, line 2), "ne luy" and "de
la fortune" (gloss B). These were misreadings: the crop `research/gallica_sweep/hi/k61_gloss.jpg` reads "…e
pauur[eté]", "[cond]uitte q[u'il] donne a", "[entre]prend sur luy et le" and "de la Tou[ss]aint", as Brackx read them.

Images: `research/gallica_sweep/btv1b9059865k/` and `research/gallica_sweep/hi/k60.jpg`, `k61*.jpg`, `k62.jpg` in the main
checkout (git-ignored). Site figure: `docs/noailles1558_f60r.jpg` (was `guiche1551_noailles.jpg`).

## Brackx 2026 (issue #113)

Michael Brackx (https://github.com/brackxm), issue #113, 27 Oct 2026. This section is his first post as he reported it,
before his files arrived (they came on 28 Oct, see "28 Oct 2026: Brackx's gist" below; the counts there replace these):

- All 262 signs of the three blocks transcribed, with positions.
- A homophonic symbol alphabet with nulls (a box sign, slashes, thin uprights) and two word signs, *qui* and *et*.
- Key recovered from the glosses (A, B inner margin; C outer margin) and a French 5-gram model (Montaigne): 246 of 262
  tokens valued, 16 of them tentative. About 0.75 of words read on firm values, 0.84 with the tentative ones; he grades
  it *read in part*. Method if reproduced: key recovered from adjacent plaintext.
- Negative checks: fr. 3151 no. 14 (Noailles to the King, 17 Oct 1558) is in clear; Ribier II has no November 1558
  Noailles letter; fr. 20974 (31 Guise alphabets, 1556) has no alphabet that fits.
- A parallel, not a source of plaintext: Charrière, *Négociations de la France dans le Levant* II, 505, "donne encore
  mauvais ordre à ses affaires". **Corrected 12 Nov 2026:** the phrase is on p. 505 but in the letter headed "Venise, 7
  et 20 octobre 1558", said of the emperor, not in the letter of 7 Nov 1558 as first cited here (Beling,
  `beling/charriere_check.md`; confirmed on the Internet Archive OCR at the independent verification). The page images
  behind the OCR were not checked.

## 11 Nov 2026: transcription checked on the images, Charrière II searched, f. 60v gaps retried (Andrew Beling, `beling/`)

Contributed with AI agents; details in `beling/README.md`.
- Brackx's 272 sign tokens checked one by one on views 61-62 against his `legend.md`: **270 agree, 2 unclear, 0 differ**;
  two pale possible extra signs (C4, A3), perhaps show-through. No decoded letter changes (`beling/transcription_check.tsv`).
- Charrière II prints Noailles's Venice letters of 7 and 15 Nov 1558, not this one, so there is no printed plaintext.
  **Correction:** the parallel "donne encore mauvais ordre à ses affaires" (p. 505) is in the letter of **7/20 Oct 1558**,
  not 7 Nov, and is said of the emperor Ferdinand I (`beling/charriere_check.md`).
- No held-out test is possible: key r5 used all three glosses.
- f. 60v gaps, all tentative: outer gloss line 4 read "ilz ont d'autruy les", line 6 "[vi]ennent p[ou]r a hazard";
  candidates `+o` = z, `Ob` = r (may be a blot), `lp` = "ost"; `ag` is cursive letters, perhaps "ay" written in clear.
  C2's trailing "u l" is in the cipher (`al 5` is clear). C4 "e r o" and C5 "t h ?" still do not meet the gloss.

## Integration check (12 Nov 2026) of PR #423

PR #423 was verified independently before it was taken in. The contributor's files in `beling/` are unchanged except one
column of the table (below).

- **Reproduced.** `beling/transcription_check.tsv` has 274 rows: 270 agree, 2 unclear, 2 possible extra signs; its sign
  sequence matches Brackx's transcription 272 of 272. About 80 signs were sampled again on Gallica views 61 and 62 with
  Brackx's positions (A1, the start of A2, B2 around `s5`, the end of C2, the start of C4, the end of C5): all match
  their labels, and the two "unclear" are fair. The Charrière OCR has the stated hash; the phrase is on p. 505 in the
  letter of 7 and 20 Oct 1558; the Venice headings then run 7 Nov, 15 Nov, 24 Nov, 3 Dec, 10 Dec, with no 13 Nov.
- **Corrected here.** (1) The old citation "II, 505 (letter of 7 Nov 1558 ...)" in the Brackx section above and in the
  Escalation line. (2) In `beling/transcription_check.tsv` the `key_r5_value` column showed `?` for the nine `#` tokens;
  `key_r5.tsv` has `#` = i, and the column now says i. No verdict in the table changes.
- **Beling's inferences, not checked:** that the emperor of the p. 505 phrase is Ferdinand I, and that Charrière's
  letter of 15 Nov is to M. de la Vigne, are his readings of the OCR; the page images were not opened by him or here.
  Vertot's *Ambassades de Messieurs de Noailles* is still unopened (he argues it covers England only).
- **The f. 60v margin gloss** is soft at Gallica's native resolution. "p[ou]r a hazard", "ravitailles qu'ilz" and "ont
  osté aux aultres" are plausible; "d'autruy" in line 4 could be neither confirmed nor rejected at the verification.
  "Tentative" is the right label for `+o` = z, `Ob` = r and `lp` = ost; none is applied to the reading.
- **Counts, recounted from the files** (replacing 262 / 260 / 272 and 244 / 246 / 256 in earlier notes and on the page):

  | Count | Number | Where the other figures came from |
  |---|---|---|
  | sign tokens in `brackx/transcription_f60r_f60v.txt`, lines A1 to C6 | 272, of 76 distinct labels | 274 with the two bracketed clear words [Comme] and [tant] |
  | nulls (`/`, `\|`, `Box`) | 12 | |
  | non-null sign tokens | 260 | 262 = 260 + the two bracketed clear words (the `check_brackx.py` printout); also the round-7 count of his first post |
  | with a value in key r5 | 244 (93.8% of 260) | 256 in `legend.md` = 244 + the 12 nulls; 246 = his round-7 count |
  | on firm values | 232 (89.2%) | |
  | on tentative values | 12 tokens, 11 labels | 16 in his first post (round 7) |
  | without a value | 16 tokens, 15 labels | |

- **Profile and NOTES made to agree.** Since 28 Oct the notes said Brackx had recovered the key from the glosses and
  graded the result read in part, while `profile.json` still said not read / not solved / key none. Decided from the
  folder by README Conventions: the key was obtained from a partial marginal decipherment in the same document, so the
  method is *key recovered based on adjacent plaintext*; an outside contributor produced it and the project checked and
  filed it, so provenance is *contributed*; the text builds one full clause (block A) and a sentence with holes
  (block C) and is under 95%, so the class is *read in part*; signs remain without a value, so the key is *partial*.
- **Read share.** `reading.md` (Brackx's three blocks, unchanged) measured with `research/reading_audit/v10_relabel.py`:
  51 words, 42 holes, **0.548**. That count takes every letter listed inside an unread stretch ("[?8 signs: d a t · u ·
  u l]") as a hole; with each unread stretch counted once it is 51 words and 21 holes, 0.708. Brackx's own figures are
  about 0.75 of words on firm values and 0.84 with the tentative ones.
- **Statistical validation** (`docs/_validate.py`, `validation.tsv` built from his transcription and key, model
  fr-1600-letters): reading -2.171 per letter; 200 random keys of the same structure, best -3.712; key refitted on
  shuffled text, mean -2.447, best -2.356. Verdict: pass. It is not a held-out test: the key was fitted to the glosses and a French model.
- **One line added to a file of Brackx's:** `brackx/translation_en.md` cites the phrase as written "on 7 Nov"; a bracketed,
  dated correction now follows that sentence. His other files are as copied.
- **Not reproduced:** Brackx's key search itself (`crib_anneal.py`, `lm_anneal.py`). `lm_anneal.py` needs a 5-gram table
  built from Montaigne that is not in the gist. What is reproduced is the decode from his key and transcription.

## Remaining gaps
- start of each marginal gloss line on f. 60r, and with it the five large signs that open block B and the four after "affaires" in block A - blocker: needs-physical-access; swallowed by the binding; needs the page opened flat
- f. 60v C2, C4, C5 unread groups: Beling's cribs from the outer gloss (11 Nov 2026, `beling/README.md` section 5) give tentative `+o` z, `Ob` r, `lp` ost, but C2 "u l", C4 "e r o" and C5 "t h ?" do not meet the gloss as read - blocker: open-codes; open work, not only an image limit: the cribs exist and the decode does not yet meet them; next is a re-reading of gloss lines 4-8 (soft at Gallica's native resolution; a sharper image from the BnF would help) together with a re-look at the signs of those three stretches
- 16 sign tokens of 15 labels without a value, and 12 tokens on tentative values (11 labels) - blocker: too-short; each open label occurs once (zb twice) and each tentative value rests on one context; 272 signs give no second occurrence to test them

## Escalation
- [x] siblings: fr. 3151 searched; the Seure letters (nos. 39-44) are a different cipher; fr. 3151 no. 14 (Noailles to the King, 17 Oct 1558) is in clear (Brackx, issue #113)
- [x] clear-pages: the marginal decipherment of the time found on f. 60r; the f. 60v outer-margin decipherment of block C (Brackx, issue #113; checked here on view 62)
- [x] known-keys: fr. 20974 Guise alphabets of 1556, 31 tried, none fits (Brackx, not checked here); the Cardinal de Lorraine's own key (pp. 41-44) is of the same sign kind with other values (Brackx)
- [x] print: Ribier II has no Nov 1558 Noailles letter (Brackx); Charrière II searched on the Internet Archive OCR (Beling, 11 Nov 2026): it prints Noailles's Venice letters of 7 and 15 Nov 1558, not this one of 13 Nov; the parallel phrase on p. 505 is in the letter of 7 and 20 Oct 1558. The Noailles ambassade edition (Vertot, 1763) not opened; it covers the embassies in England
- [x] key-rebuild: Brackx, gloss alignment + French 5-gram (Montaigne); key r5 gives 244 of 260 non-null signs a value; the search itself not rerun here, the decode from his key reproduced
- [x] retry: f. 60v gaps C2, C4, C5 retried against the outer gloss (Beling, 11 Nov 2026): three tentative values, three stretches still unmatched

## 28 Oct 2026: Brackx's gist (issue #113), checked here

Files copied unchanged into `brackx/` from https://gist.github.com/brackxm/c48586b981081bc69a5db8d672eef296 (revision
a026501dcb23, 28 Oct 2026); he allows copying under the project licence (CC BY 4.0 for text and data, MIT for code), with
credit. Tools, from his readme: Claude Code with Claude Opus 5.5, directed by him, on the BnF IIIF images (views 61-62).
His `crib_anneal.py` (alignment of the signs with the marginal gloss) and `lm_anneal.py` (French 5-gram fill of the free
values) were added to the gist later the same day (28 Oct, revision d819ac655347) and copied unchanged into `brackx/` on
5 Nov 2026, MIT, credited to him. The other twelve files of the gist at that revision have the same content as our copies
(only line endings and a trailing blank line differ). The two scripts are not run here: `lm_anneal.py` needs numpy and a
5-gram table built from Montaigne that is not in the gist, so key recovery is not reproduced.

`check_brackx.py` (our own code; it does not run his scripts) applies `key_r5.tsv` to `transcription_f60r_f60v.txt` and
compares with `decode_tvd_r5.txt`: 274 tokens, 272 agree; the 2 differences are bracketed clear words in the transcription
([Comme], [tant]). Counts: 262 non-null tokens including those two, 260 non-null sign tokens, 244 with a value (93.8%), 12
tentative: his counts, reproduced. Not done on 28 Oct: the transcription was not checked on the images (done by Beling,
11 Nov 2026, above); the positions and the tentative values are still unchecked.
