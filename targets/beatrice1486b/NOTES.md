# Beatrice d'Aragona to Eleonora d'Aragona, Buda, 2 May 1486 (DECODE R1143)

Status: found already in print, and deciphered at the time: contemporary decipherment slips are photographed with the
leaves, and MDE III (1877) no. 75, pp. 93–96, prints the reading. Matched to the images; no key applied or recovered.

Split on 14 Oct 2026 from `beatrice1482` under the one-key rule (George Lasry, 14 Oct 2026). Until then this letter was
filed with Beatrice's other letters to Ferrara (catalogue item 160). It was written two months after the March 1486
letter that enclosed a new cipher ([`targets/beatrice1486/`](../beatrice1486/NOTES.md)), so the two are not shown to
share a key; the 1482 letters are [`targets/beatrice1482/`](../beatrice1482/NOTES.md) and the plain 1505 letter
[`targets/beatrice1505/`](../beatrice1505/NOTES.md), each with its own page.

Research report on all five records of catalogue item 160, with the verification limits:
[`../beatrice1482/RESULT.md`](../beatrice1482/RESULT.md) (20 Sept 2026, GPT-6). DECODE metadata in
`../beatrice1482/metadata.json`; images (git-ignored; DECODE notice: publication needs the archive's permission) in the
main checkout's `targets/beatrice1482/img/`. Work date: 2026-09-20.

## The letter

ASMo, Carteggio Principi Esteri, 1623, b. 2/2, 2, 18; DECODE R1143. Six photographs show three written pages plus the
address side: P1 shows a handwritten decipherment slip laid over the first cipher block and P2 the same page with the
slip moved aside; P4 and P5 do the same for the last written page.

- The first cipher block: Milanese and Bari support for Ippolito, against the account of Cardinal Ascanio's envoy,
  the abbot of Forlì. The long slip begins "che don hippolyto vostro figliolo…", matching MDE III no. 75 ("che Don
  Hippolyto vostro figliolo sia tanto amato dalo Sig-re Ducha de Milano…", in italics, the editor's mark for cipher).
- A short slip: "che quello Andriolo se conferisca qua"; the print has the request in the same context.

## Open

- The date and scribe of the slips are not established. Whether the letter uses the new cipher sent in March is not
  tested (a glyph transcription exists since 14 Nov 2026, see below; no key of the March cipher is in the repository
  to compare it with).

## Files

- `readings/r1143_mde3_ocr.txt`: uncorrected OCR extract of MDE III no. 75.

## 14 Nov 2026: the cipher transcribed (audit section I, "no transcription file")

- No transcription was in the folder and DECODE R1143 has none (its public page lists six images; DECODE serves the
  full-size images only to a logged-in user).
- The letter is in the open Vestigia database as **document 1976** (https://www.vestigia.hu/documents/1976; ASMo,
  Carteggio principi esteri b. 1623, 2, fasc. 1, no. 18; MNL OL X 8921, DF 295031): six photographs, public, the same
  views as DECODE's (page 1 with the slip on and aside, page 2, page 3 with the slips on and moved, address side). No
  licence is stated on the site, so no image is copied here.
- Cipher on the letter: a block of 13 lines on page 1 (interrupted twice by clear words: "perche toccamo con mano",
  "siche scrivendose al presente tale littera comprendemo che"), one line on page 3 under the slip "che quello
  Andriolo se conferisca qua.", and a second short run on page 3 under the slip "Lo p.to Andriolo." Page 2 has none.
  The upper part of page 3 was looked at only at overview size.
- `transcr/R1143_transcription.txt`: every sign with a shape label, line by line; **445 signs, 41 distinct labels**
  (measured with `_check_profile.py --measure` on the sign labels alone). The signs are written apart and clean; 3
  are marked doubtful. A single AI transcription, not checked by a person.
- Check by decoding. The values below were read off by laying the printed reading (MDE III no. 75) and the slips
  against the signs; each sign keeps one value through all 445 signs and the whole passage comes out as Italian:
  a `+` `q` `=/` · b `o-` · c `to` · d `R` · e `r` `-o` `#` · f `ot` · g `Y` · h `Q` · i `=1` `&` · l `7` · m `9` ·
  n `6` · o `A` `F` `xo` · p `8` · r `C-` · s `h` `V` · t `d` · u/v `H` · v `2` `3` · x `-c` · ll `c` · ss `o` ·
  ct `E` · qu `PI`. `1 6`, `1 9`, `2 1` stand where the print has the Duke of Milan, the Duke of Bari and Cardinal
  Ascanio; `G 2` where it has Don Hippolyto; `G 7` where it has "et" between the two dukes and before "presertim".
  `x4` opens runs and also stands inside them, `n` closes runs and stands before the name Andriolo; neither has a
  letter value. These values are a by-product of the check and come from the existing reading; the outcome method is
  unchanged and no key file is written.
- Where the cipher and the print differ: the cipher has "esso" (print "epso") four times, "dali" + two name groups
  (print "dalo Sig-re Ducha de Milano, et Duca de Barri"), "el contrario"
  (print "il contrario"), "presertim" (print "prefertim", an OCR or print slip). Not explained: "a a a t e" where the
  print has "Abbate" (the second sign is marked doubtful), and the tall L in "su L icare" (print "supplicare") and
  "L illo" (slip "quello").
- The alphabet is neither the 1482 one (`../beatrice1482/vestigia/README.md`: a = 8, V; d = 9 ...) nor the Latin-letter
  signs of R1142 (`../beatrice1486/vestigia/README.md`). Whether it is the new cipher enclosed in March 1486 is still
  not shown.
