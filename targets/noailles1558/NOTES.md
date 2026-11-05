# Noailles (Venice) to the Cardinal de Lorraine, 13 Nov 1558 (BnF fr. 3151 no. 33): catalogue no. 10 (part)

Status: in progress (28 Oct 2026: Brackx's files of issue #113 copied into `brackx/` and the decode reproduced here by
`check_brackx.py`; three cipher blocks, 260 non-null signs, 244 valued = 93.8%, 12 on tentative values). Next step: retry
the f. 60v gaps against the outer-margin gloss and check the key values on the images.

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

262 signs in all (Brackx's count; to be measured with `_check_profile.py --measure` once his transcription is in).
The earlier figure, "about 150 signs", was an estimate by eye for A and B only.

**Gloss readings corrected (27 Oct 2026).** The first notes quoted "gouvernement" (gloss A, line 2), "ne luy" and "de
la fortune" (gloss B). These were misreadings: the crop `research/gallica_sweep/hi/k61_gloss.jpg` reads "…e
pauur[eté]", "[cond]uitte q[u'il] donne a", "[entre]prend sur luy et le" and "de la Tou[ss]aint", as Brackx read them.

Images: `research/gallica_sweep/btv1b9059865k/` and `research/gallica_sweep/hi/k60.jpg`, `k61*.jpg`, `k62.jpg` in the main
checkout (git-ignored). Site figure: `docs/noailles1558_f60r.jpg` (was `guiche1551_noailles.jpg`).

## Brackx 2026 (issue #113)

Michael Brackx (https://github.com/brackxm), issue #113, 27 Oct 2026. **Not yet reproduced here: no files attached;
requested.** As he reports it:

- All 262 signs of the three blocks transcribed, with positions.
- A homophonic symbol alphabet with nulls (a box sign, slashes, thin uprights) and two word signs, *qui* and *et*.
- Key recovered from the glosses (A, B inner margin; C outer margin) and a French 5-gram model (Montaigne): 246 of 262
  tokens valued, 16 of them tentative. About 0.75 of words read on firm values, 0.84 with the tentative ones; he grades
  it *read in part*. Method if reproduced: key recovered from adjacent plaintext.
- Negative checks: fr. 3151 no. 14 (Noailles to the King, 17 Oct 1558) is in clear; Ribier II has no November 1558
  Noailles letter; fr. 20974 (31 Guise alphabets, 1556) has no alphabet that fits.
- A parallel, not a source of plaintext: Charrière, *Négociations de la France dans le Levant* II, 505 (letter of
  7 Nov 1558, "donne encore mauvais ordre à ses affaires"). Not checked here.

## Remaining gaps
- start of each marginal gloss line on f. 60r - blocker: needs-physical-access; swallowed by the binding; needs the page opened flat
- Brackx's reading of A, B and C (262 signs) - blocker: not-attempted; not yet reproduced here: files requested (issue #113): transcription with positions and legend, key with the basis of each value, raw decode aligned, readings with holes marked
- f. 60v C2, C4, C5 unread groups where the outer gloss is legible ("ilz ont dû commun…", "… pour a hazard", "… ravitaillez") - blocker: not-attempted; a crib exists, so this is work left, not an outside blocker; values fixed there may also close A3 and B1

## Escalation
- [x] siblings: fr. 3151 searched; the Seure letters (nos. 39-44) are a different cipher; fr. 3151 no. 14 (Noailles to the King, 17 Oct 1558) is in clear (Brackx, issue #113)
- [x] clear-pages: the marginal decipherment of the time found on f. 60r; the f. 60v outer-margin decipherment of block C (Brackx, issue #113; checked here on view 62)
- [x] known-keys: fr. 20974 Guise alphabets of 1556, 31 tried, none fits (Brackx, not checked here); the Cardinal de Lorraine's own key (pp. 41-44) is of the same sign kind with other values (Brackx)
- [x] print: Ribier II has no Nov 1558 Noailles letter (Brackx); Charrière II 505 a parallel phrase only. The Noailles ambassade edition (Vertot, 1763) not yet searched
- [x] key-rebuild: Brackx, gloss alignment + French 5-gram (Montaigne), 246/262 valued; not yet reproduced here
- [ ] retry: not done

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
([Comme], [tant]). Counts: 262 non-null tokens including those two, 260 sign tokens, 244 with a value (93.8%), 12 tentative:
his counts, reproduced. Not done: the transcription, positions and the 16 tentative values are not checked on the images.
