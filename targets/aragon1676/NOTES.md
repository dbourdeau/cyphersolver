# aragon1676: Cardinal Pascual de Aragón to his brother Pedro de Aragón (BNE Mss/2043), system S1, p. 0496

Status: read in part (Brice Dudout, 5 Nov 2026; 82 of 95 words = 86% without restorations; key partial by our protocol, 0.742 on a single held-out page; the page carries a contemporary margin decipherment).

Contributed by Brice Dudout (Europe chiffrée), with Claude Opus 5.5 agents. Not in the catalogue; first reported in issue #254
(new lead "BNE Mss/2043"). No DECODE record found, nothing at Cryptiana (Tomokiyo), no edition found.

## Document

Madrid, Biblioteca Nacional de España, Mss/2043 (olim G. 85; BNE Digital, BDH bdh0000042925): letters of Cardinal Pascual
de Aragón (archbishop of Toledo) to his brother Pedro Antonio de Aragón ("D. Pedro mi S.r"), 1675-1677. The volume belongs
to the Aragón / Villahermosa papers. About 90-110 pieces are in one mixed syllabic cipher, called **S1** here. Several carry
a contemporary decipherment in the margin, and a separate gathering "Descifrado de las cartas…" (about f. 353) holds clear
copies of about fifty letters.

This target is **one page**: PDF view 0496, left and right pages (about f. 493). It has 20 cipher lines (273 signs) and a
contemporary decipherment in the margin. The date is not on the part transcribed; the content (suspension of arms, Sicily,
Carpio, Medina, Oropesa) points to 1676-1677. View numbers are image ranks in the PDF, not folios (folio ≈ view - 3).

Citation of images: "BNE Mss/2043, BNE Digital". **No image, crop or thumbnail is included here**: the scans were used for
research only.

## System S1 and key (`key.tsv`)

A syllabic cipher with mixed signs:

- numbers of 1-2 digits for letters and syllables (13 e, 16 a, 15 y, 18 z, 12 g, 25 que, 22 se, 21 pa, 26-30 sa…su,
  31-35 ma…mu, 36-40 ta…tu, 28 si, 23 pi, 6 p, 10 i, 20 c);
- letter-shaped signs read with a shifted consonant (te = de, ga = la, po/go = no, pa = na, ca = ua, ce = ue, to = do);
- simple signs: a = n, + = s, x = r, ø = o, a+ = l, r = u, ue = h, ) = d;
- a few 3-digit numbers, some nulls (916, 296, 316, 331), and 281 = V.E.

The key is CLE_C08c, the last of a series (see `validation.txt`). It was learned by EM alignment on 14 cipher/clear pairs
of the same volume (the margins of views 0138-0139 and 0484-0485, and ten letters of views 0318-0355 paired with the
"Descifrado" gathering), and frozen by SHA-256 before p. 0496 was opened. **It is partial by our protocol**: it clears the
shuffled-key controls by the required margin but stays under our absolute threshold of 0.85.

Sign readings settled by Brice Dudout on blind shape plates (he chose the shape seen, without values or words shown):
the three forms of the 6/10/20 family (crozier 20 = c, compact 10 = i, round 6 = p); the "U"-shaped tracing,
first transcribed as two signs 24b and 31b, is one sign and the same as the existing **21** (= pa); one occurrence on
view 0344 left, line 3, is **28** (= si). Ligature rules: "lo" = 10 (1 tied to 0), "2)" = 22; tied numbers are not one sign.

## Files

| file | content |
|---|---|
| `transcription.txt` | cipher of p. 0496, left (6 lines) and right (14 lines), 273 tokens |
| `margin_clear.txt` | the contemporary margin decipherment facing those lines (95 words) |
| `decryption.txt` | line by line, token = value, then the decoded letters, no correction |
| `reading.md` | the reading in Spanish, restored and corrected letters marked, word count |
| `translation.md` | English translation |
| `key.tsv` | the key CLE_C08c with the source of each value |
| `validation.txt` | every measurement made on S1, and the two runs on p. 0496 |

## Validation

One held-out page, opened after the key was frozen, cipher hashed before its margin was read. Character score (longest
common subsequence with the margin clear, head cut t ≤ 40) against the best of 200 shuffled keys.

- **Official result (run 2): 0.742 against 0.422 (margin +0.320): PARTIAL.** M5 0.281 against 0.186.
- Run 1 gave 0.392 against 0.344 (FAILED). It was spoilt by an input-format error: the measuring script skipped "#" note
  lines in the cipher file but not in the clear file, and the clear file began with 7 note lines, which were scored as
  clear. Run 2 was agreed before it was launched, declared as the official result with no third run, and changed only
  those 7 lines (checked by diff). Both runs are in `validation.txt`.
- An earlier key (CLE_C06) measured once on p. 0504 left gave 0.778 against 0.424: PARTIAL as well.

## Reading (`reading.md`)

95 words of the margin: 41 certain, 41 probable, 13 restored = 86% without restorations, so **read in part** by Daniel's
95% rule. The cipher corrects the margin in three places: "burgo" → **juzgo**, "mel ar" → **Melgar**, "tado" → **estado**.
At line 13 of the right page the decryption has "ualenzuela" where the margin has "valencia" (see `translation.md`: maybe
Fernando de Valenzuela; a hypothesis, not counted).

Gist: on the suspension of arms by which "lo de Sicilia" would be put in the Pope's hands; the resolution of Carpio; the
orders to Your Excellency "as they stand" at Melgar; what is clear is Medellín; the writer fears Medina, kept "in this
state" by discontent, and the conferences of Oropesa; Valencia (or Valenzuela) is "still very entrenched".

## Declared deviations

- **Two executions** of the measurement on p. 0496, as above; the first is kept.
- **A glimpse of the margin before the hash**: the first overview strip of the left page showed the right edge of the
  margin clear (a few word endings) before the cipher was hashed.
- **The interlinear clear on the right page was not read** and was not used.
- **Controls**: each measurement has two control figures, characters and M5, both from the same 200 shuffled keys;
  each control key takes its own best head cut. Because the control is computed against the clear file, the two runs
  on p. 0496 have two different control values (0.344, then 0.422).
- The margin on the right page is partly cut by the binding; the transcription of p. 0496 is less secure than the
  training pieces (pale ink, crossing interlinear writing; 7 doubtful signs given as A|B, 3 illegible).
- The left-page margin starts before the cipher block: the head cut t = 24 removes "en la suspension de armas con" from
  the score; "suspension de armas" is still counted probable in the reading because it is in the decryption.
- One reader only (an AI agent) for the transcription and the reading; Brice Dudout only answered the shape plates.

## Remaining gaps

- Other pages of S1 with a margin or with the "Descifrado" gathering are not read; no held-out page is left for a new key
  test (all the margined pages we chose have been used once).
- Pages without any clear are not attempted: the key is not validated.
- The date and the exact persons behind Carpio, Medina, Oropesa and Valencia/Valenzuela are not established.
