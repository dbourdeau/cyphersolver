# Keresdi Bethlen cipher letters, 1645-1648 (DECODE R4936-R4940, R4942)

Status: in progress

22 Oct 2026, reading audit (George Lasry's test: can sentences be built and translated?): only **R4940's two
cipher spans read** ("votumiok", "niert dolog volna", 23 letters). **R4936, R4937 and R4942 are decoded, not read**:
the mechanical decode and the solver outputs are letter streams with garbled words, no sentences. About 1% of the
transcribed cipher letters read. (Superseded 23 Oct 2026: R4937 and R4942 read, see the b15 block below. R4936, read at
b15, went back to decoded, not read at the verify sweep of 23 Oct 2026 and is still decoded, not read; the g/q shape
check of 24 Nov 2026 is at the end of this file, and the state is left to the reviewer.)

**Split on 14 Oct 2026 (one-key rule, George Lasry).** This target first grouped the ten records R4933-R4942 by their
DECODE number range. It now keeps the Keresdi Bethlen letters in the alphabet family of R4936/R4940 (R4936, R4940, and
R4937, R4942, which give fragments under it), plus R4938 and R4939 of the same Keresdi_Bethlen_15 series, which are
not yet inspected and for which no shared key is claimed. Split off, each a different cipher with its own entry:
R4941, a different substitution (`targets/r4941/`), and the Kemény_XIX_1628 records R4933-R4935
(`targets/kemeny1628/`). Their metadata and R4941's extract and solver results moved with them; the images stay in
the main checkout's `transylvania1645/` folder for all three. The record table below is the original survey of all
ten.

## Sources

28 images downloaded from the ten DECODE records on 23 September 2026 using the existing authenticated session. Catalogue metadata saved alongside images. No document attachments listed. The catalogue dates are not confined to 1645. R4936 first page inspected: clear Hungarian introduction and long alphabetic cipher passages. No decipherment claimed.

## Prior work

User objective reports no published reading found on 22 September 2026. Independent verification remains pending.

The first R4936 annealing result preceded consultation of printed letters. Afterwards downloaded:

- Lukinich, *Keresdi Bethlen Ferencz levelezése*, first instalment (1907), https://real.mtak.hu/192384/1/MagyarTortenelmiTar_1907_55_4_08.pdf . Locally extracted to `Bethlen-correspondence-1907.txt`. Starts 1622, ends around 1647; no matching cipher reading established. Introduction points to a separate diplomatic study.
- Lukinich, *Keresdi báró Bethlen Ferencz*, first instalment (1908), https://real.mtak.hu/178743/1/717_cut_Szazadok_1908.pdf . First instalment is early biography, not yet an exact control.
- Unfollowed leads: the biography's later instalment https://real.mtak.hu/178739/1/825_cut_Szazadok_1908.pdf ; Szilágyi's 1873 *Okmánytár I. Rákóczy György svéd és franczia szövetkezéseinek történetéhez*; *Erdély és az északkeleti háború*, vol. 1, https://www.mek.oszk.hu/06500/06508/pdf/erdely1.pdf . These may contain independent editions or keys. Do not infer novelty from DECODE N/A.

## Progress, 23 September 2026

All 28 image files validated as image/jpg downloads; `image-manifest.json` gives hashes, sizes and exact download URLs. No credentials saved here. The contact sheet is for navigation only; inspect originals for reading.

| Record | Catalogue year | Work so far |
|---|---|---|
| R4933 | 1658, but name says 1628 | Two photographed spreads; requires detailed inspection and resolution of catalogue date conflict. |
| R4934 | 1628 | Two images; mostly cipher-looking text; not transcribed. |
| R4935 | 1628 | Four images; largely clear text, inspect short cipher insertions. |
| R4936 | 1645 | Both pages provisionally transcribed. Quadgram attack recovered Hungarian quickly. Many q/g, c/p, i/n transcription confusions remain. |
| R4937 | 1646 | Long single page. Partial extraction and successful Hungarian substitution fragments; no complete reading. |
| R4938 | 1647 | Four images, mainly clear text with short cipher insertion(s); not yet transcribed. |
| R4939 | 1648 | Two substantial text pages and address; not yet transcribed. |
| R4940 | 1648 | All surviving cipher read: 23 letters in two spans. See `R4940-reading.md`; both images inspected. |
| R4941 | 1648 | Different substitution, extract from pages 1–2 still not solved; pages 3–4 must also be inspected. |
| R4942 | 1648 | Partial page 2 extract yields Hungarian fragments. All other cipher spans still to inspect/transcribe. |

`attack.py` uses existing `hu-modern`, default quadgrams, no spaces, seed 4936, 50 x 12,000 trials. There was no need to add a duplicate Hungarian model. `python transylvania1645/attack.py R4941-extract 5` selects quintgrams. Early result filenames lack the order suffix; current script includes it. The raw inputs are PROVISIONAL and must not be presented as archival transcriptions.

Important transcription correction: a working shared alphabet family has c=p, p=c, g=u, q=t. The initial R4936 statistical key wrongly used c=u, g=t, q=p because the hand transcription confused these glyphs. `shared-key-hypothesis.json` fixes the proposed family mapping, with v/w representing a in different hands. This is not a verified full key for every record. First R4936 words are recognizably `persvadealni kell ...` and `... succumbalna szandekaban`; R4937 begins with `czasar dipplomaia ...`. R4940 is a useful held-out short reading using the family.

`noisy_probe.py` applies penalized alternatives to likely confused glyphs in R4936 and outputs `R4936-correction-hypotheses.json`. These are explicit UNVERIFIED hypotheses, not edits to the source transcription. They reveal coherent topics including musketeers, dragoons, payment, the king, the republic, Munkács and Rakovica. Every adopted correction needs an image check. Plaintext word spaces in explanatory notes are editorial.

**23 Oct 2026, re-read (REREAD_BRIEF, batch b15).** R4936, R4937 and R4942 are now **read** (grade B) with the family
key unchanged: R4936 re-transcribed from the images (215 label changes, `R4936_corrections.tsv`), R4937 and R4942
transcribed in full for the first time. Each has `<doc>_reading.md`, `<doc>_en.md`, a letter alignment with the figures
(`<doc>_align.tsv`, `research/reading_audit/b15_align.py`) and `<doc>_reread_log.md`. R4942's DECODE image 3 is a clear
slip of its cipher block in Zsigmond Rákóczi's name (`R4942_slip.txt`). Content: R4936 = numbered points for the 1645
Warsaw mission (3,000 musketeers and 1,000 dragoons to be hired, money at Danzig, Bregy and Croissy); R4937 = 1646, the
Emperor's diploma and the Evangelicals, hiring 4,000 foot; R4942 = Zsigmond Rákóczi 1648, the intermediaries and his
brother's plenipotentiary power. Caveat: `docs/_check_reading.py` cannot score 17th-c. Hungarian (0.07 and 0.0 on printed
1645 letters from Szilágyi 1885); explicit-hole share (b17_score.py HOLES=1) 0.94, 0.90, 1.00.
fraction_read 0.59 (estimated; R4938 and R4939 untranscribed).

## Remaining gaps

- R4937, R4942 read 23 Oct 2026 (b15). R4936 decoded, not read (verify sweep 23 Oct 2026; state unchanged by the 24 Nov 2026 shape check below): 26 letters (1.3%) still on look-alike alternates after the check (12 doubtful g=t places, 5 q=u, 3 c=y, 3 g=g, a, h, n), four u written with the hook (g=u:hook), 94 g->q relabels made by an AI pass that count as probable until a blind reader checks them, eight [?words] and three [...] runs (reading lines 9, 16, 22) - blocker: illegible; the DECODE scan (1,704 px, no larger file) leaves 17 g-shaped places undecided at 3-4x, and no contemporary or printed text confirms the choices
- R4937 l. 3 run after 'megsegni' and the end of l. 13 - blocker: illegible; decode to letter strings that are not words, checked at 2.2x
- R4938 (1647): three cipher spans (54 letters) decoded with the family key 23 Oct 2026; one word ('ailunkker') unread - blocker: too-short (occurs once). The clear letter around the spans is not transcribed (clear text, not a cipher gap).
- R4939 (1648): read 23 Oct 2026 (r2h); lines 03-09 keep about 12 unread words - blocker: illegible (figures decode to non-words with every look-alike pair tried, 3x crops of the 1,704-px scan; no printed text).
Of the records kept here: R4937, R4939, R4940, R4942 read; R4936 decoded, not read (look-alikes; after the 24 Nov 2026 shape check 234 of 341 cipher words are sure on the human-checked places, 302 if the AI-checked places are confirmed by a blind reader); R4938's spans decoded, one word too short. No gap is left not-attempted (23 Oct 2026). R4939 is a different cipher (own key and hand): under the one-key rule it should become its own target before any write-up.

## Escalation
- [x] siblings: R4936, R4937, R4940, R4942 read with one family key (23 Oct 2026)
- [x] clear-pages: R4942 image 3 is a clear slip of its cipher block; no clear copies for R4936/R4937 on the records
- [x] known-keys: the family key (shared-key-hypothesis.json) applied unchanged
- [x] print: Lukinich 1908 (both instalments), Szilágyi 1885 (Linz), Erdély és az északkeleti háború I grepped; no edition
- [x] key-rebuild: not needed; the transcription was redone instead
- [x] retry: R4936 re-transcribed and read; R4937, R4942 transcribed in full and read (23 Oct 2026); R4938 spans decoded and R4939 broken and read (23 Oct 2026, r2h); R4939 checked by an independent second reader on 6 random lines (letters 93.9%, words not carried 8.3%; 23 Oct 2026, sr)

## Next work (earlier list)

1. Resolve transcription of R4936 q/g, c/e/p, i/n and other ambiguous forms against full-resolution crops; the substitution is substantially recoverable. Do not treat noisy language-model proposals as confirmed readings.
2. Transcribe the remaining R4937 and R4942 ciphertext; test shared family mapping, correcting the input rather than forcing bad mappings.
3. Inspect ALL original folios of R4933–35, R4938–39 and R4941. Short cipher spans may be solvable with sibling alphabets; R4941 needs separate attack and better transcription (long-s/f and g/q are suspects).
4. Follow the printed diplomatic-collection leads and compare dates/openings. Keep discovery chronology for contamination assessment. Consider period Hungarian corpus only if modern scoring remains insufficient after fixing the transcription.
5. Record every step in profile.json. It currently passes `docs/_check_profile.py` with unknowns explicitly retained.
6. Do not invoke writeup yet. User requires partial readings pushed toward completion first. Once the research is exhausted, use `.claude/skills/writeup/SKILL.md`, update DECODE queue and all required publication surfaces, and run its checker. Shared checkout has extensive unrelated modifications; stage explicit paths only if committing, and isolate any broad site rebuild as necessary.

## 23 Oct 2026 — verify sweep (reading audit v2): R4936 back to decoded, not read
- `R4936_align.tsv` (b15) puts 130 of the reading's 1,932 letters on the other member of a look-alike pair of the hand:
  g=t 114, q=u 6, c=y 4, g=g 3, h, a, n 1 each; 99 of 338 words carry one. That is 6.7%, above the brief's ~3% limit,
  and no contemporary or printed text confirms them (the pencil gloss under line 1 is a later reader's start).
- Checked on IMG_R4936_I28640_P1 (main checkout `transylvania1645/`) at 3x, lines 1-2 and 4-5: the g- and q-shaped
  figures ("rdkgng" holtig, "byucayhg" fegyvert, "lyzyinxyuyq" kemeniseget) do not separate at the scan's 1,704-px
  width, so the t/u choice is made by sense. DECODE has no larger file.
- Scores of the reading body: explicit holes 0.941 (32/34) as published; **0.147 (5/34)** with the look-alike words
  counted as holes (`research/reading_audit/v2_lookalike_holes.py`, `v2_score.py`); 0.029 plain (modern hu list).
- Result: R4936 `decoded, not read`, reading kept as a partial reading; fraction_read 0.59 -> 0.22 (estimated:
  R4937 869 + R4942 252 + R4940 23 of about 5,250 letters). A sharper image of Keresdi_Bethlen_14 (archive access)
  would settle g/q and could restore it.

## 23 Oct 2026 — r2h: R4938 and R4939 worked (`R4939_reread_log.md`)
- **R4939 read** (grade B). Every image opened (P1-P2 cipher, P3 clear address "Magnificis Francisco Betthlen de Keresd
  ... ac Andreae Klobusiczki ... ad moderna comitia Reipub. Poloniae legatis"); no DECODE documents or comments; the
  Erdély és az északkeleti háború I edition prints the envoys' October 1648 reports, not this letter. The family key
  gives nothing: R4939 is **a different simple substitution in a different hand**. Transcribed (`R4939-transcription.txt`,
  1,631 letters) and broken ciphertext-only by annealing (`research/reading_audit/r2h_r4939_anneal.py`, hu-modern;
  key `R4939_key.md`); 50 look-alike labels corrected on 3x crops (`R4939_corrections.tsv`). Reading `R4939_reading.md`,
  English `R4939_en.md`: the brothers write that their father György I Rákóczi is dying ("az doctor itileti szerent is
  eletehez ... semmi ... ninc"), that he did not want the Polish crown for himself, that seeking the principality for
  Zsigmond now would endanger the country "foe nekul", and bind Bethlen and Klobusiczky to promote "oeczem uram
  promotioiat" (Zsigmond's Polish candidacy), money to be spent on it. Explicit holes 0.75 (18/24); look-alike letters
  16/1,449 = 1.1%. Lines 03-09 keep unread groups (illegible).
- **R4938**: a clear letter of 24 Apr 1647 with three cipher spans on P2 (54 letters) in the family hand, decoded with the
  family key unchanged: "az Rakoczi Sigmon", "az nekunk [...] volna", "mi [?nevunkre] forogion"; a later pencil gloss
  agrees. Fragments, not counted as a reading; one word too short to settle.
- **R4936's g/q**: not settled. R4938's spans contain no t, so they cannot test the g/q choice; R4939's hand separates g
  and q on scans of the same width, so the limit is R4936's hand. Blocker unchanged (illegible).
- fraction_read 0.22 -> 0.58 (measured letters: R4937 + R4942 + R4940 + R4939 of all six transcriptions).

## 23 Oct 2026 — independent second reader on R4939 (sr, `R4939_sr_blind.tsv`)
- Sample: 6 cipher lines drawn with `random.seed(4939)` from lines 13-46 (lines 01-12 excluded: their first-pass labels
  had been seen before the draw): **16, 17, 24, 29, 32, 45**. Transcribed blind on 2-3x crops of the DECODE scans
  (P1/P2, 1704x2272, scratchpad only), decoded with `R4939_key.md`, then compared.
- **Letters: 200 of 213 agree (93.9%)**; 5 of the 13 differences are the q/g pair, the rest a/e, c/o, ÿ/g and one
  letter the first reader dropped. **Words: 8 of 36 (22%) not carried by the blind decode; 3 (8.3%) after re-cropping**:
  "bizoeta-" (l. 24; sr sees a y-descender, and neither reading gives a word: "bizontalan" would want q), "azekatru-"
  (l. 32; sr sees ÿ, "azokat-"), "kegylme" (l. 45; the scan has x g e o g h a g, "kegyelme").
- **Key**: one cipher letter one plain letter, 23 distinct values, and ten reciprocal pairs (a-m, b-i, c-p, d-u, e-g,
  f-v, h-l, o-y, r-z, s-t): a paired alphabet, which confirms the annealer's key on its structure. The blind decode reads
  as Hungarian of 1648 by sense ("ra vetni nem akariuc, az porta alapattia miben legyen tudhattia kegyelmetek, io
  securitas"; "az hol kivantatik, oeczem uram").
- Decision: under 1 in 10: **stays read, grade B**. The three words would be better given as [?bizon]talan, azokatru-,
  kegyelme at the next pass (reading not changed here).

## 24 Nov 2026 - g/q shape check of R4936, place by place (human blind sheet, then an AI pass calibrated on it)
- **Evidence, as text, in `sign_check/`** (README.md there; no image and nothing derived from one): the rule of the
  blind sheet T, its key, answers and results; the two parts of the AI protocol and the blind calibration; and one
  table of the places, `sign_check/R4936-places.tsv` (line, rank in the line, word, position, reading, verdict hook /
  loop / doubtful, human or AI). Hashes in `sign_check/SHA256SUMS.txt`.
- **Method, in two steps, each written down before the unseen places were looked at.** (1) Blind sheet T, 14 questions
  (8 g read t and 1 q read u on p. 1 l. 1-13, 2 c read y, 3 controls), answered by Brice Dudout from the DECODE image:
  the 8 t places all show a short hook, the u place a long loop, the controls 3/3. The selection rule was hashed
  (SHA-256 7f08d4fd8ce0d43c5358f6ddd67bf533553cb1fe8c1ebfdbb2abefb35c6ad998) before the thumbnails were cut. (2) An AI
  agent (Claude) then classified the other 142 g-shaped places one by one (3x context crops, 4x zooms), calibrated on
  those answers: a blind calibration of 21 mixed crops agreed 9/9 with the human answers and 3/3 on the controls
  (limit: the agent had read the human answers, so the blinding covered which crop was which, not the expected
  proportion). The protocol was hashed in two parts, part A before any unseen place (927b4cbb...), parts A+B (human
  prototypes at 400% and the calibration result) before the remaining 133 places (bc670d63...).
- **Result.** g read t: human 8 hook; AI 94 hook, 0 loop, 12 doubtful. g read u (AI, 36): 27 loop, 4 hook, 5 doubtful.
  Relabelled g->q at the 8 human and the 94 AI hooks (102), q->g at T9, c->e at fegyvert: 104 labels, in
  R4936_align.tsv and R4936-transcription-b15.txt (rows appended to R4936_corrections.tsv); mechanical decode of the
  b15 transcription in R4936-mechanical-b15.txt (`tools/R4936_count728.py --decode`). The frozen key is unchanged, no
  value was added and the reading is unchanged.
- **Reserve.** No t is written with the loop, but four u are written with the hook (mutatnanak twice, instructioban,
  tule): tagged `g=u:hook` in class_resolved, so these words are not counted sure. The hook supports t without proving it.
- **Count** (`python3 tools/R4936_count728.py`): 341 cipher words = the 338 rows of R4936_align.tsv + the 3 `[...]` runs
  of R4936_reading.md. Sure = row carried with no tag in class_resolved. Decision of 24 Nov 2026 (Daniel Bourdeau): the 94
  AI relabels count as probable until a reader who has not seen the answers checks them; the 8 human places stand.
  Sure words: 232 before; **234 of 341 (0.686) on the human places alone**; 302 of 341 (0.886) if the AI places are
  confirmed (the 94 relabels fall in 78 words, 68 of which would become sure). R4936 stays `decoded, not read`; the
  review state is the reviewer's to record.
- **Images.** None are committed. The images are DECODE R4936 (access level 2); they are not republished and the crops
  used stay private. The use of an AI assistant on these images was not raised with the archive.
- **Record.** Sheet T is in `profile.json` as `outcome.sign_check` (moved unchanged from `sign_check_pending.json` at the
  integration of 24 Nov 2026): 11 signs, 3 controls, all passed, which meets the floor of the sign-check level (README
  Conventions). It checks sign shapes only and changes neither the state of R4936 nor any count. The reading has eight
  [?words], not five as the gap line first said (corrected the same day).
- Credit: Brice Dudout (human reviewer, 11 places on sheet T), AI-assisted shape check as stated above; DECODE for the images.
