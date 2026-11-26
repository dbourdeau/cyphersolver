# No. 29, fr. 244 (view 244): three blind sign-shape sheets, 24 Nov 2026 (Brice Dudout, with Claude)

Status: decoded, not read (unchanged). This folder adds a new pass on view 244 only. It does not replace the
blind16 figure of record (77.4% on views 244-245, `../../blind16/no29_fr244-245/`), and it changes none of
McBratney's or Beling's files.

**Images: none, and nothing derived from one.** The images are LASA A 1 Nr. 530. The LASA licence forbids
publishing or passing on reproductions without written permission, so the sheets, thumbnails and crops stay
private. Box coordinates in the key files are pixels of the 2500 x 2024 view 244, so a reader who has the
image can find each place.

## Method
The starting point is McBratney's blind transcription and judge (`blind16/no29_fr244-245/judge.tsv`). Its losses are
mostly twin-form slips of the hand (JUDGE_NOTES: o/c, f/n final, q/d, t/l). The targets are words where ONE twin letter
makes the word fail.

On each sheet, Brice Dudout saw only:
- the boxed sign;
- example thumbnails of the candidate forms, cut from the same page;
- no values, no reading, no place.

The rules were written and hashed before any thumbnail was cut (in French, byte for byte as hashed):

| sheet | rule | SHA-256 |
|---|---|---|
| A | `sheet-A-rule.md` | a3df1adb... |
| B | `sheet-B-rule.md` | d4049497... |
| C | `sheet-C-rule.md` | 84b3140b... |
| C, amendment | `sheet-C-rule-amendment.md` | d4acb00c... |

The C amendment replaced a doubtful e control with u and recentred the boxes, before the answers. The keys
(`sheet-*-key.json`) were opened only after the answers (`sheet-*-answers.json`) were exported.

Each chosen letter was re-entered and the word re-decoded with the frozen key (`blind16/FREEZE/key_upstream.tsv`),
with no new value.

`sheet-*-results.tsv` has French column names: choix_brice = answer, lettre_choisie = letter of the chosen form,
retranscrit = re-entered, decode_avant/apres = decode before/after, statut = effect, remarque_brice = remark.

## Sheet A: g/q (12 targets, 3 controls)
- Controls: C1 and C3 passed. C2 was **defective**: its box sat on the p of "pgil", not the g. Brice's answer
  "other form, P" is right for the sign that was boxed, so C2 is counted as defective, not failed.
  Consequence: sheet A has no valid control on the g form.
- Results: 7 g->q and 3 q->g re-entered. 10 words read: brauchte, mochten, berichtet, special, arctior,
  sondern auch bey, hoch, es mochte, hoc, noch.
- 2 targets were seen as transcribed (L22 ggfliz, L4 xzguld): unchanged.

## Sheet B: g/q and g/y (13 targets, 3 controls)
- Controls: the g of "bgufb" (the first valid g control) and the q of "trqu" passed. The q of "zhqu" was answered
  correctly but flagged as badly boxed, so it counts as defective.
- 2 targets were flagged as badly boxed (L18 xgguld 3rd, L26 urdsdhyif 7th). They are **not used** and will be
  asked again.
- 10 words read: sonderlich, gemacht, erkundigte, nicht wol, quondam, per discursum, soceri, confesio, and two
  {probable}:
  - **cuius**: L9 "ghrhb" begins with a distinct capital form, labelled "G-maj". It is given the value c from
    sense only.
  - **erclaret**: a period spelling of erklaret.
- 1 target was seen as transcribed (L37 chye).

## Sheet C: t/l, d/e/c, final f/n (9 targets, 3 controls 3/3)
- All 8 decided targets confirm the letter as transcribed: three final n, one l, one t, two e, one d. So these
  failing letters are not misreadings of twin forms. In each case the plain text needs the very letter that is
  written: the scribe wrote the plain letter instead of its partner under the reciprocal key.
- 9 words read that way, all **{probable}** (the reading rests on sense): avisen, gelten, empfinden, vielleicht,
  ernst, einraumete, hette, undt, er.
  - "er" comes from L2 "ci": Brice could not tell c from e. e is chosen because it is the only option that gives
    a word.
- No sure letter is changed, and the key is unchanged: "zhn" still reads "auf", so a final n is not always a
  plain n.
- Sheet fault: one example thumbnail (the d of "edf", L22) was badly boxed. It will not be reused.

## Extension of the sheet C rule (applied mechanically, all {probable}, NOT checked by eye)
The rule was then applied to the rest of view 244. A word is counted only if all three conditions hold:
- every failing letter, read as itself, gives the letter of the judge's reading;
- the word has no N;
- no S letter is changed, and the key is unchanged.

This reads 29 more words (34 letters), e.g. final n in werden, sein, einen, denen, and several "undt".

## Counts (view 244, 432 rows of judge.tsv)

| stage | words read | E letters | S letters (of 2438) |
|---|---|---|---|
| blind16, as filed | 188 (43.5%) | 184 | 1961 (80.4%) |
| after sheet A | 198 (45.8%) | 174 | 1971 (80.8%) |
| after sheet B | 208 (48.1%) | 164 | 1981 (81.3%) |
| after sheet C targets | 217 (50.2%) | 155 | 1990 (81.6%) |
| after the extension | **246 (56.9%)** | 121 | 2024 (83.0%) |

Without any {probable} word: 206/432 (47.7%). `judge_fr244_after.tsv` is the 432 view-244 rows of judge.tsv after
all of this, with a `change` column. `count-after-sheet-C.json` holds the counts.

## Next
- An eye check of the extension, family by family.
- The two badly boxed targets of sheet B.
- View 245.

## Credit
- Transcription and judge: Malcolm McBratney (blind16).
- Prior work on the target: A. J. Beling.
- Blind reader of the sign forms: Brice Dudout.
- Sheets built, scored and integrated by Claude (AI agent).
