# Scipion de Fiesque, Vienna, to Catherine de' Medici and Charles IX, Oct 1567 – Nov 1569 (BnF fr. 15919)

Status: in progress (23 Oct 2026). Contributed reading (issue #52, Harumi-Matsuba), checked here; all 23 letters read into sentences
(round 2, 23 Oct), read in part: open codes and phrase holes remain inside the readings (see Remaining gaps).

14 Nov 2026, holes counted by words (owner decision: the read share counts unread words, not hole marks; a mark with a
number, `[… n]`, is n unread words). The re-reading logs record what stands under five multi-word marks; each log has
a closing section "Holes counted by words". Sizes are counts of decode fragments or groups, so estimates.

| letter | mark | size | read share by marks | by words | state |
|---|---|---|---|---|---|
| 2 Dec 1568 | "ayde a autre […]" ("bellestant du m que du ii") | 6 | 0.953 | 0.943 | read -> **read in part** |
| 11 Oct 1567 | "et que [...] bagues" (two groups) | 2 | 0.954 | 0.953 | read |
| 2 Mar 1569 | "de […] qui craignent" ("m lihngs odeccurd") | 3 | 0.958 | 0.951 | read |
| 20 Oct 1569 | "par […] le comte […]" | 2 and 4 | 0.944 | 0.926 | read in part |
| 4 Sep 1568 (Queen) | "d'Espaigne […] le mariaige" (two groups, thirty letters) | 2 | 0.943 | 0.942 | read in part |

Extent unknown (not recorded in the logs), left as one hole each: "que […] bien qu'il" (11 Oct 1567), the marks of 17 Jul 1568, 4 Sep 1568 (King)
and 6 Mar 1568 (all three letters already read in part). The readings now hold 11,615 words and 574 holes (561 before);
`fraction_read` 0.873 -> 0.872.

23 Oct 2026, r2m (Claude Opus 5.5): **the single-word holes of the 17 letters not re-checked in round 2 worked through
on native-resolution crops** (openapi.bnf.fr IIIF, views 7-8, 34-35, 49, 65, 70-71, 99-100, 103, 109-110, 125, 129-130,
140-141, 146, 155, 159, 161, 163, 168; images in the scratchpad only). Bracketed holes in the 17 readings 161 -> 90.
- **Number codes misread as letter signs.** This hand writes the codes with z for 2 and i for 1: 10 "ic", 13 "iz", 14
  "i4", 18 "i8"/"ig", 20 "zo", 21 "zi", 23 "z3". Read as codes they close many holes: "jusques a tant qu'on" (21),
  "estre", "estre esleu", "l'Emperatrice est venue", "a esté", "il est apres" (14), "vous" for the contributor's 13/II/MM
  (18), "pour" (20), "qu'il" (23), "et" (10). Label corrections in `read/r2/corrections.tsv` (r2m rows).
- **The lone codes**: ϖ for the Emperor or the King in 11 places ("des filles de [ϖ]", "de quoy [ϖ] ne m'a riens dict",
  "au prejudice du [ϖ]"), pp/ꝥ for the King of Spain ("si [pp] espouse sa fille aisnée"); Dz = con in seven more words.
- **Readings of 22 Oct corrected where the figures contradict them**: "l'Emperatrice est venue souper" (27 Mar 1568, not
  l'Empereur), "l'evesque de Retes" (4 Sep 1568, twice: le + ves + the code que; the Bishop of Rennes, Bochetel, the
  previous ambassador), "pourchassoict la seconde pour le roy de Portugal", "l'ambassadeur du Roy poussoict a
  Constantinoble le Turc", "je le prioys de me faire ce bien de ne croire les mauvais" (Oct 1567), "car il ne sçavoict
  encores en quels termes" (27 Mar 1568), "Et depuis" (20 Oct 1569: the "Il" was the null "Il ti ol"), "Chantonnay et
  Vanega" (1 Oct 1569: Luis Venegas, Philip II's ambassador). Withdrawn as not carried: "arriver" (12 Jun 1568),
  "[?princes]" (20 Oct 1569), "[?Cosme]" (4 Sep 1568), "[?estoient]" (now supplied).
- **Untranscribed cipher found**: view 7 left c20 begins with four groups the contributed line lacks ("sont [?soubz] les
  mains de luy, du Roy et du Roy d'Espaigne"); view 110 right has a whole line between the contributor's c04 and c05
  ("le seigneur Ernest ..."); cipher groups at the ends of clear lines on views 34 and 49 (no word). "Jay receu" written
  inside cipher blocks (views 110, 130, 159) behaves like the nulls "Il ti ol", "par moy".
- Scores (v2_score, plain / explicit holes) rise on 11 letters, e.g. 11 Oct 1567 0.461/0.724 -> 0.564/0.833, 20 Oct 1569
  0.333/0.667 -> 0.400/0.867, 4 Nov 1569 0.462/0.846 -> 0.615/0.923; states unchanged (all 17 were read).
- Left: 90 places, each with its figures in the r2m section of `read/<doc>_reread_log.md` (Remaining gaps).

23 Oct 2026, round 2 (REREAD_BRIEF, Claude Opus 5.5): **view 6 right and view 23 left transcribed and read; the 10 Sep
1569 letter now reads, so all 23 letters read.**
- View 6 right (f. 2r), the first cipher page of the 11 Oct 1567 letter, transcribed from native IIIF crops (23 lines,
  816 signs, `read/r2/transcription_v006r.txt`, log `read/r2/v006r_reread_log.md`) and read: Fiesque recalls his
  orders to sound the Emperor on a union of the Christian princes; the Emperor blames the disorders in Christendom on
  their disunion, "plus enclins a leur particullier qu'au bien publict". Single AI transcription, look-alike
  alternates 3.3% of its letters; letter body score 0.61 plain, 0.92 explicit holes only. v007l c01 closed.
- **Dz (ꝺʒ) = con**: the contributor's unvalued sign reads "con" in eleven words in five letters (congé, condition,
  conclusion, conditions, contanter, conservation, comme, consoler ...). Also found: this hand writes the code 20 as
  "zo" and 10 as "ic"; lone ∞ appears as a code in f. 39r; the null ".bro" reads "de" in f. 100r c24.
- View 23 left (f. 18v) transcribed (13 lines, 446 signs, `read/r2/transcription_v023l.txt`) and decoded; with a
  re-reading of the contemporary decipherment it corrects three readings of 22 Oct: "il s'en va a Prague", "ceste
  lettre" (the decipherment's "lre"), and "je n'ay eu responce de celles que vous ay envoyées par Suisse" (the
  "[?Chanton]nay" of 22 Oct was "Je n'ay"). The page ends with the closing formula in cipher.
- 25 Oct 2026 (issue #97): Harumi-Matsuba transcribed view 23 left independently (445 signs, Tomokiyo's key, shuffled
  control 0/1000; `contributed/data/transcription_v023l.txt`, `decoded_v023l.txt`). Its decode agrees with ours in
  content and settles our two open places: "par **le chemin** de Flandres, **par ce que c'est le plus** court" (the
  supposed bearer's name was *le chemin*). Taken into the reading with doubt marks, since it rests on look-alike
  alternates in both transcriptions. Not done: a sign-by-sign comparison of the two transcriptions.
- 10 Sep 1569: view 150 left c14-c23 checked on native crops; label corrections (code 18 and code 20 misread as letters)
  and Dz = con close the passage; body score 0.54 -> 0.61, look-alike 3.0% (without the y-shape class), state read (B).
- Phrase holes checked on the images: 4 Sep 1568 f. 100r c16-c27 (mostly read; [pp], the King of Spain, wished to be
  mediator), 17 Jul 1568 f. 79v c06-c08 (read), 15 Feb 1568 v038l c03-c04 (read), 6 Mar 1568 f. 39r c21-c29 (mostly
  read). Label corrections in `read/r2/corrections.tsv` (contributed/data unchanged).
- fraction_read 1.0 measured (30,969 of 30,969 signs belong to letters that read); class kept read in part.

22 Oct 2026, re-read (REREAD_BRIEF, batch b02, Claude Opus 5.5): **all 23 letters now read as French sentences and
are translated** (`read/<doc>_reading.md`, `_en.md`, `_reread_log.md`; 4 grade A, 19 B). Four follow contemporary
decipherments found in the volume: view 23 right (15 Nov 1567, now read to the end, covering the untranscribed cipher of
view 23 left) and the left margins of views 65 right (4 Jun 1568, not recorded before), 103 right (21 Aug 1568) and
125 right (6 Nov 1568); view 37 right's margin deciphers its two cipher lines. The other 19 are built word by word from
the key decode, reading through the known sign confusions, with image checks on views 6, 37, 109 and 159. Found: the
"Oct 1567?" letter is dated 11 Oct 1567 on its docket and begins with an untranscribed cipher page on view 6 right; the
4 Sep 1568 letter docketed "au Roy" addresses "Madame" in its cipher. Sign values suggested by the readings (not
entered in key.tsv): a lone ϖ is the code for l'Empereur (margins of views 65 and 103) or le Roy; 16 fits "vostre" in
the 1569 letters to the King; H# = ss in ambassadeur/commissaires/asseurer; =ii stands for a person (King of Spain;
once the Landgrave). fraction_read about 0.97 (estimated: view 6 right unread). Holes remain (Remaining gaps).

22 Oct 2026, reading audit (George Lasry's test: can sentences be built and translated?): **read**: f. 79r and f. 94r
only, in the contributed `READING.en.md` (continuous French with scattered holes; the first pages of the 17 Jul and
14 Aug 1568 letters). **Decoded, not read**: the other 21 letters and the rest of those two. The 44 `decoded_*.txt` are
unspaced mechanical output (0-17% of sentences clean, `docs/_check_reading.py`); the line readings of ff. 39r-v, 100r and
158r have "…" holes in most lines. 99.7% (signs with a value) is withdrawn as a reading figure; about 5.6% of the signs
read (estimated, 1,669 of 29,707).

**Outcome: read with known key, read in part; contributed.** Satoshi Tomokiyo's reconstructed key for this volume
(Cryptiana, "French Ciphers for German (and Eastern) Affairs", frencheastern.htm) applied by Harumi-Matsuba to an
AI-made transcription of all 44 cipher pages (822 lines, 29,707 signs). All of their transcription, decoding and
checking was done by AI models (Anthropic Claude for the first transcription and decipherment; OpenAI Codex and
Claude Sonnet for the second transcription and image checks). **No human checked the transcription.** Their "full
reading" means 85.0–93.6% value agreement between two AI transcriptions plus a shuffled-key control, not this
project's read bar (README Conventions: 95% of tokens read as sense, measured). Here: 29,627 of 29,707 signs
(99.7%) take a value; 81.0% of the decoded letters fall in French words (lexical screen, `measure.py`); one letter
calibrated against the contemporary decipherment on view 23 right: 83.8% of its letters agree (`calib.py`).

## The documents

- BnF Français 15919 (formerly Harlay 238 (8)), 174 folios: letters of Scipion de Fiesque (Scipione Fiesco), French
  envoy at the court of Emperor Maximilian II, to Charles IX and the Queen Mother, October 1567 – November 1569,
  during the negotiation of the King's marriage with Elisabeth of Austria. Gallica ark:/12148/btv1b90573568 (183
  views, each a double-page opening of microfilm MF 15717). Catalogue: https://archivesetmanuscrits.bnf.fr/ark:/12148/cc46124x
- 23 letters with cipher, 44 pages; per page view numbers, figures and summaries in `contributed/docs/PAGES.en.md`;
  grouped by letter in `profile.json` documents. Letters to the King: 15 Feb 1568, 4 Sep 1568 (ff. 100–101), 10 Sep
  1569, 20 Oct 1569, 29 Oct 1569 (f. 158); the rest to the Queen Mother. One from Speyer (2 Dec 1568).
- Clear text surrounds the cipher: openings ("Madame, j'ay receu vostre lettre…") and closings are in clear.
- No DECODE record for this volume (contributor searched DECODE fields for 15919, Fiesque, Fiesco, Harlay).

## The key

Tomokiyo's reconstructed table (one table for the whole volume; one key, so one entry). The contributor gave its
signs names (`contributed/data/key.tsv`, 95 entries: 72 `table`, 23 `inferred`): two to five homophones per letter,
doubled-letter signs (ee, ff, ll, mm, nn, rr, ss, ii), 12 word codes (=22 que, =23 qu'il/quel, =10 et, =18 vous,
=inf le Roy, Φ Saxe …) and 20 named null groups. Values inferred from context: 16 = ce, ꝭs = t, ρ = e, ꝑꝑ = ff.

## What Harumi-Matsuba did (issue #52, 20 Oct 2026)

Repository https://github.com/Harumi-Matsuba/fiesque1567-public (CC BY 4.0 data, MIT code), copied at commit
659e2e1 into `contributed/` (see `contributed/ATTRIBUTION.md`). First transcription by Claude from line crops of the
full-size BnF IIIF images; three Codex runs and Sonnet image checks used to correct it (only where both readers
agreed); independent Codex second transcriptions afterwards: 85.0–93.6% value agreement per page (lowest run);
control 0/1000 shuffled keys per page; positive control on an enciphered La Ferrière letter. Line-by-line
conjectural readings of five letters in `contributed/docs/READING.en.md` (most lines marked "inf."); mechanical
decodes of all 44 pages in `contributed/data/decoded_*.txt`. They did not calibrate on view 23 right ("AI reading of
the cursive is unreliable", their OPEN §7: 51–55% when read by Sonnet/Codex).

## What was checked here (21 Oct 2026, Claude Opus 5.5)

1. **Re-measure** (`measure.py` → `measure.txt`). The contributed key re-applied to every transcription by our own
   decoder. 29,707 signs, 29,627 with a value (99.7%). Shared model `fr-1530-despatches` (order 5, no spaces): true key
   −2.37 to −3.42 per character; best of 200 shuffled keys per page −4.38 to −5.31; 0 of 8,800 shuffled keys reach the
   true key. Clean French scores −1.64 on the same model, so the decodes are far from noise but well short of clean
   text. Lexical screen (DP segmentation into words of a lexicon from fr-henri4 + fr-1520s-diplomatic): 81.0% of
   decoded letters covered, against 27.6% for shuffled keys and 90.3% for clean French; per page 68% (view 8 left) to
   90% (view 155 right).
2. **Calibration** (`calib_v023r.txt`, `calib.py` → `calib.txt`). View 23 right ("deschiffré de la precedente", f. 19r)
   is the contemporary decipherment of the 15 Nov 1567 letter. Read here by eye from a 2,600-px IIIF crop as far as
   the end of view 22 right's cipher ("une diette"), 1,193 letters. The contributed decode of view 22 right matches
   1,000 of them (83.8%; 86.6% of the decode's letters); 98 of 182 words of three or more letters come out intact. The
   sense agrees throughout (Lignerolles's departure, levies in Germany for the Huguenots, the Emperor's mandates,
   Chantonnay, the diet). Two content differences: where the decipherment has "au pays du duc de Wirtemberg et du
   conte palatin", the decode has "du duc de SAXE et du[n]…" (the Φ code read as Saxe; palatin missing); and "lo
   sarteiment" for "le partement" (the s/p y-shape). My reading of the cursive is itself unchecked by a human.
3. **Spot check on the images** (views 22, 23, 99 from openapi.bnf.fr IIIF at 3,200 px). View 22 right line c01: 40
   signs on the image, 40 in the transcription, each consistent with the contributed sign names (e.g. Φ, ⊣, the
   lr ligature as b, △ as tri); line c03: 26 of 26 signs at its start consistent, one place near its end (between
   fu and ptil) not confirmed at this resolution. No clear disagreement found in about 80 signs.
4. **Found: view 23 left is not transcribed.** The 15 Nov 1567 letter continues in cipher on view 23 left (f. 18v,
   about 17 lines, perhaps 600 signs); the decipherment on view 23 right continues past "une diette" ("de son pays
   d'Austriche … Fiesque") with its text. The contributed page list has no v023l. Other untranscribed pages may
   exist (the contributor scanned the 183 views at reduced size).

## 14 Nov 2026: second decoder, one missing key sign, recount (Brice Dudout, with Claude)

- **Decoder.** A separate script applied `contributed/data/key.tsv` (first value of each sign; codes =NN give their
  word; the (null) signs dropped) to the 45 `contributed/data/transcription_*.txt` pages and compared the letters with
  the contributor's `decoded_*.txt`: 32,272 of 32,352 letters agree (99.75%); 18 pages are identical and no page is
  under 98.8%. Every difference is a sign with no value in the key (marked `?` or `[?]` in the contributor's decode),
  so the decode is reproduced in full.
- **Key correction (missing sign).** The transcriptions use a sign `w` 8 times (v038l c18; v049r c06, c11, c13, c17;
  v065r c06; v070r c04, c08) that is not in `key.tsv` (only `wt` = m is), so the mechanical decode prints `[?]` there.
  Tomokiyo's table (`easternScipion.png`, cryptiana.web.fc2.com/code/frencheastern.htm) has this sign: a plain W in
  its "double letters" row, under r, so **`w` = rr**, a double-letter sign like `=ll`, `=ss` and the others in the key.
  It was missed when the table was set up as key.tsv. The image confirms the shape at three places (Gallica
  btv1b90573568, full size): view 70 right c04 and c08 (a plain W, no tilde, between the cross sign and the triangle:
  "cou-rr-ier") and view 65 right c06 (W before a, in "[con]clu-rr-e"). The readings already have the r there:
  "[con]clure le mariage avec le Roy" (v065r c06), "courrier" (v070r c04, c08), "seroient" (v049r c13),
  "verriez" (v049r c06). With rr all 8 places give the reading's word in a spelling of the time (courrier, verriez;
  serroient, conclurre); m gives no word anywhere. Proposed key row: `w` -> rr (table, double letters).
- **Recount.** `research/reading_audit/v10_relabel.share` on the 23 readings of `outcome.texts`: 11,615 words and 561
  holes in all. The 22 letters that read (read or read in part) hold 10,628 of the words; the one decoded, not read
  (10 Sep 1569) holds 987. Words read in letters that read, over all words and holes: 10,628 / 12,176 = **0.873**. The
  earlier 0.91 was the letters' share of the words, estimated, with the holes inside them not taken off (measured,
  that share is 10,628 / 11,615 = 0.915, so the estimate stood). The per-letter read shares recorded agree with the
  measure to within 0.005.

Integration check (14 Nov 2026, PR #559):
- **Decoder.** An own decoder (first value of each key.tsv row, nulls dropped, unvalued signs counted as disagreement,
  letters compared by position) over the same 45 pages: 32,352 letters in the contributed decodes, every difference
  either a sign with no value in key.tsv (Dz 49, arrow 9, w 8, K 7, `?` 6, pa 1) or the apostrophe of "l'empereur"
  shifting five lines (f079, f094). The decode is reproduced.
- **The sign w is not missing from the key.** key.tsv already has the row `=rr` = rr, source table, shape note "W (double letters row)": the
  same plain W of Tomokiyo's table, under the label `=rr`, which the transcriptions use for it at 45 places (f039r
  c05, c16, c22 and others). The eight `w` are a second label for that sign, not a new key sign. Seen on Gallica at full
  size: view 70 right c04 (a plain W after the two cross signs, before the triangle, "cou-rr-ier") and, for comparison,
  view 43 right c05, where the transcription's `=rr` is the same W shape. So the value rr stands, nothing is added to the
  key, and the readings (which already read r at all eight places) are unchanged; the proposed key row above is not
  needed. The mechanical decodes keep `[?]` at the eight places because the transcription label differs from the key's.
- **Recount.** v10_relabel.share re-run on the 23 readings: 11,615 words, 561 holes, 0 doubtful; 10,628 words in the 22
  letters that read; 10,628 / 12,176 = 0.873, as stated.

## Prior work

- Tomokiyo published the key and wrote that it "will allow reading undeciphered portions"; no reading of the
  passages in Cryptiana.
- The contributor's adversarial prior-work check (`contributed/docs/PRIOR_CHECK.en.md`, 20 Oct 2026): this ledger,
  NoAutopilot/cipher-lab, pangoleen/cipher-readings, Cryptiana, DECODE, OpenAlex, Persée, BnF SRU, GitHub, La Ferrière's
  *Lettres de Catherine de Médicis* iii (prints Catherine's replies, not Fiesque's cipher): nothing found. Not
  checked: Patrouch, *Queen's Apprentice* (2010), BnF fr. 17020 ff. 227–228.
- The volume itself holds the contemporary decipherment of the 15 Nov 1567 letter (view 23 right), and the margins of
  views 103 right and 125 right may hold more (contributor's OPEN §7; not read here).

## Files

- `contributed/` — the contributor's key, transcriptions, decodes, figures and documents, unchanged (CC BY 4.0 / MIT).
- `measure.py`, `measure.txt` — project re-measure (LM, shuffled keys, lexical coverage).
- `calib_v023r.txt`, `calib.py`, `calib.txt` — calibration against the contemporary decipherment.
- `profile.json`. Images are not kept; crops for the site are `docs/fiesque1567_*.jpg`.

## Remaining gaps
- View 6 right (11 Oct 1567) c05-c06, two words, and about ten [?] words on that page - blocker: no-key-material; transcribed and checked sign by sign on native crops 23 Oct; the groups give no word under the key and no decipherment or print of this letter exists
- View 23 left (15 Nov 1567): the bearer's name (9 signs) and about 17 signs before "court" - blocker: no-key-material; decoded 23 Oct; a name not in the key, and the contemporary decipherment abridges and is cramped there
- Phrase holes left after the round-2 image checks: f. 79v c01-c03, f. 80 c01, c08 (17 Jul 1568); f. 100r c18 end, three words in c24-c26 (4 Sep 1568); v038l c17 subject (15 Feb 1568); f. 39r c08, c22-c23 end, c29 verb (6 Mar 1568); v150l [?conclurre], [?cest] (10 Sep 1569) - blocker: no-key-material; each checked on native crops (round-2 sections of read/<doc>_reread_log.md); no contemporary decipherment, clear copy or print exists for these letters
- Single-word holes left in the 17 letters after the r2m pass (90 bracketed places, from 161; each listed with its figures in the r2m section of read/<doc>_reread_log.md): groups that give no word under the key (e.g. 11 Oct 1567 view 8 left c21 "et que […] bagues", 27 Mar 1568 the seven signs at the end of the clear line, 4 Sep 1568 view 110 right line 5 after "le seigneur Ernest"), struck or unwritten words (14 Aug 1568 "devers […]"), and words that rest on a look-alike the figures do not settle ([?fort], [?bon escient], [?soubz], [?poinct], [?pouviez]) - blocker: no-key-material; checked on native crops 23 Oct 2026 (r2m); no contemporary decipherment, clear copy or print of these letters, and the look-alike and code-sign values cannot be settled without one
- Margin decipherments, cramped words: 4 Jun 1568 [?presenté], 21 Aug 1568 "[…]nt" and [?l'on tient pour seur], 6 Nov 1568 [?a assemblé] - blocker: illegible; re-read on native crops 23 Oct 2026, the margin hand is cramped or overwritten at these places and the decode is broken there too
- Lone signs standing as codes, values not settled: ϖ (l'Empereur or le Roy), ∞ alone, =ii, pp/ꝥ (the King of Spain by sense), H# alone, the group ffx-3y, the arrow, "lele"; 16 = ce or vostre - blocker: no-key-material; not in Tomokiyo's table, read from context; key.tsv unchanged (Dz = con now settled)

## Escalation
- [x] siblings: all 183 views were looked through by the contributor; here views 22, 23 and 99 opened, and view 23 left found untranscribed; 23 Oct views 5, 9, 21, 24 checked for a decipherment of views 6 and 23 left (none)
- [x] clear-pages: view 23 right is the contemporary decipherment of views 22 right and 23 left (read in full 22 Oct); the margins of views 65, 103 and 125 right decipher those letters, view 37 right's its two lines (read 22 Oct); no other cipher view has a margin decipherment (contact sheet of all 34)
- [x] known-keys: Tomokiyo's reconstructed table for this volume is the key; no other key of Fiesque's embassy is known
- [x] print: La Ferrière, Lettres de Catherine de Médicis iii (Catherine's replies only), Cryptiana, DECODE and the contributor's prior-work list; nothing printed of Fiesque's cipher
- [x] key-rebuild: contributor inferred 23 values from context; the calibration shows one code (Φ) mis-valued in one place; 23 Oct Dz valued con from eleven words in five letters
- [x] retry: the whole volume decoded again here with the contributed key and scored (measure.py); 22 Oct every letter built into sentences from the decode, with image checks on views 6, 37, 109, 159; 23 Oct (round 2) views 6 right and 23 left transcribed, and the phrase holes of ff. 39r, 79v-80, 100r and views 38 left, 150 left re-read on native-resolution crops; 23 Oct (r2m) the single-word holes of the other 17 letters re-read on native crops of 24 views (161 -> 90)

## 23 Oct 2026: round 2 review (coordinator)
- 10 Sep 1569 kept **decoded, not read**: the reading body clears the bar (0.61 plain, 0.76 explicit holes with conjectures counted), but 4.1% of its letters rest on look-alike choices (3.0% leaving out the y-shape s/p signs), over the ~3% limit, and nothing outside confirms them. The partial reading and its English stay in `read/1569-09-10_reading.md` / `_en.md`. Next step: settle the y-shape s/p signs on native crops, sign by sign, which would bring the share under the limit.
- Gap blockers "open-codes" renamed no-key-material (the lone code signs have no key entry).
- fraction_read 1.0 -> 0.91 (estimated from word counts).
