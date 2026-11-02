# Sigismund August, Frater Georg and Queen Isabella to Ibrahim Pasha, 1548 (catalogue 885)

Status: in progress. 7-4-4 f. 29 transcribed and decoded (the cipher spells the exemplar, 97.7% of key-derived tokens); f. 28, 7-4-5 and 7-4-9 not yet.

HHStA Wien, StAbt Türkei I 7-4-4 (AIS 7040827, f. 28-30, 5 images), 7-4-5 (AIS 7040824, f. 31-34, 6 images), 7-4-9
(AIS 7040845, f. 51-59, 11 images). Copies of letters to Ibrahim Pasha ("Hebrai Bassa") that Malvezzi sent to
Ferdinand I in the summer of 1548. Each cipher copy is filed with a clear Latin exemplar, so the plaintext is in hand.

## Access (corrects the first report)

AIS marks the records "Kein Zugang (Reservatbestand)", but the digital copy downloads to any client that keeps the
session cookie from `detail.aspx`: `fetch_images.py` (one request at a time; `width=2400` returns the full scan; the
JPEG is labelled text/html). `bildansicht.aspx` looks empty without that session. All 22 images fetched 30 Oct 2026
(not committed). PR #196 reported these as unreachable; they are not.

## What is on the images

- **7-4-4** (Sigismund August to Ibrahim Pasha, Cracow, 1 June 1548): image 1 (f. 28) and image 3 (f. 29, headed A,
  "Dupl. 1548") are cipher, image 2 is a scribbled-out verso, image 4 (f. 30) is the **Latin exemplar**
  (`texts/exemplar_7-4-4_A.txt`), image 5 a docket verso.
- **7-4-5** (Frater Georg to Ibrahim Pasha, Vinea, 2 July 1548): images 1-3 are cipher copies (B and C among them),
  image 5 carries two **Latin exemplars**, C ("Aliud exemplum", `texts/exemplar_7-4-5_C.txt`) and B (not yet
  transcribed), image 6 their continuation.
- **7-4-9** (Malvezzi to Ferdinand I, covering letter with enclosed cipher copies): images 1-5 and 10-11 landscape,
  6-9 portrait; not looked at beyond a contact sheet.

## The system (first look)

The signs on 7-4-4 f. 29 are the signs of the Ferdinand-Malvezzi key of 1548 (`../malvezzi1548/KEY_BRIEF.md`, DECODE
R367/R386): the first line begins with the Latin-letter words *Idcirco*, *b.*, *d.*, which are three of that key's
nulls, and the graphic signs (hash, pi, crossed circles, breve and bar forms) are the same. Same key family, to be
tested. The Latin exemplar of 7-4-4 is about 560 letters; the cipher on f. 29 is 13 lines of about 45 signs, the same
order of magnitude, so f. 29 may encipher exactly this text (with nulls). Not yet tested.

## 7-4-4 f. 29 transcribed and decoded (30 Oct 2026)

Thirteen lines, 572 signs (21 of them Latin-letter null words), transcribed from half-line crops by two image agents
(`TRANSCRIPTION_BRIEF.md`; `transcription/f29_lines_01-07.txt`, `f29_lines_08-13.txt`, labels in `f29_labels_*.txt`).
`align_f29.py` aligns the values on `texts/exemplar_7-4-4_A.txt`: the cipher spells the exemplar from *Sigismundus
Augustus Dei gratia Rex Poloniae ...* to *... Maiestatis*, with 462 of 473 key-derived tokens matching (97.7%;
`transcription/f29_alignment.txt`). 56 further tokens take their value from the exemplar (marked `*`) and are not counted.
The exemplar's heading (*Ad Hebrai Bassa. Exemplum literae Regis Poloniae*) is not enciphered. The cipher opens with
a short passage not in the exemplar (*replica*, after the nulls *idcirco b d*), and the last line ends *Maiestatis
propria* where the exemplar reads *... Prebria*. The date clause and the closing (*Regni vero nri primo, Et loco suo, ex
commissione ...*) fit only in part (L11-L12); 11 signs there are unexplained.

**Caveat, and the blind check.** Both transcribers had the exemplar open, so 97.7% is an upper bound. A blind
transcription of lines 8-10 (no exemplar, no crib; `transcription/blind/RESULT.md`) matches the exemplar for 61.4% of its
scored tokens (70/114), against 99.2% for the crib-assisted values of the same lines; the two transcriptions agree on 43%
of values. So the key family is confirmed without the crib (chance is about 8%), but the crib moved the ambiguous
signs: quote 61% as the independent fit, one noisy transcriber, three lines. The sign-to-value table (`transcription/f29_label_values.tsv`)
is consistent for 65 of 80 labels; 15 labels carry two values (mostly e/ae and u/e, the circle-on-stem family the key
brief already calls ambiguous).

**Corrections to the R367 brief** (from the transcribers, unchecked): r and x look reversed (the 9 with a crossed tail
reads r, the 9 with a long smooth tail reads x); a pi with a right-leg stub reads s; a cup with a taller left upright
reads g; the small round cup and the open arch read l.

## f. 28 looked at, not transcribed (30 Oct 2026, paused)

f. 28 (image 1 of AIS 7040827; also headed A, docket "1548 1/6") is not a second copy of f. 29's length: a header
line (*... cum*, *1548 1/6*) and about 19 closely set lines of cipher, roughly 1,000 signs against the exemplar's 560
letters, in a denser hand with many look-alike signs. It begins *... dicirco Dar.* (nulls) and ends *n spu atq spo*
(nulls). Lines run down to the right by about 2.5 degrees (a deskew near 2.5 degrees sharpens the line profile best),
and line spacing is about 66 px, so crops need rotation first. Whether it enciphers the same text with many more nulls
or a longer text is not known; the exemplar crib may not fit. Work paused by the user on 30 Oct 2026.

## Remaining gaps

- 7-4-4 f. 28 (second cipher copy), f. 31-33 (7-4-5) and the enclosures of 7-4-9 not transcribed - blocker: open-codes; nothing is blocked from outside, the work has not been done
- f. 29 L11-L12: 11 signs after *octauo* and before *Regni*/*commissione* unexplained; L01 first passage (*replica*) not in the exemplar; one `?` - blocker: open-codes

## Escalation

- [x] siblings: malvezzi1548 (R366, R367, R386) is the same key family; its brief is the starting key
- [ ] clear-pages: the Latin exemplars on f. 30 and f. 34 are the plaintext; 7-4-9 not yet read
- [x] known-keys: R367 applied to f. 29; it fits (97.7% of key-derived tokens), with the r/x and a few other corrections above
- [ ] print: Austro-Turcica 1541-1552 (pp. 276-278) not seen
- [ ] key-rebuild
- [ ] retry

## Next steps

1. Second blind transcriber (or the stable label table without the crib) on lines 8-10 and on L02-L05, to firm up the 61%.
2. Explain L11-L12 (the date clause) and the opening *replica* passage.
3. Repeat for f. 28, then 7-4-5 (B and C against the two exemplars), then the 7-4-9 enclosures.
4. Credit Harrison Bornstein (PR #196) for the lead to the Malvezzi key.
