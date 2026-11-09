# P.Oxy. I 90 (BL Pap. 761): the two non-Greek lines

Status: in progress

A Greek receipt for wheat paid into the public granary at Oxyrhynchus (Clarus, ex-agoranomus, 8 artabae 4 choenices,
179-180 AD; sitologos Diogenes signs). Below the signature are two lines in Greek letters that Grenfell and Hunt
(P.Oxy. I, 1898, p. 153) could not construe as Greek and, since they do not look like Graecized Demotic, called
"possibly a cryptogram of some kind". Kenyon (P.Lond. III, 1907) failed to read them. The current DDbDP edition leaves
them out. HGV lists N. Litinas, "A Riddle, Wrapped in a Mystery, Inside an Enigma", ZPE 227 (2023) 145-148, under the
papyrus (title from his CV; the article is not on JSTOR yet and was not seen).

## Text (Grenfell-Hunt edition image, `lines.png`)

    [.] . ιμιονοτεμειεμουησαπαραλαω
    [. .]ιμονετηεκατηεπαιδιετους.

`lines.txt` holds the 48 letters outside the lacunae. The archive.org OCR of vol. I reads line 1 as
`plovoreperepouncamapadaw`: wrong; use the image. The papyrus itself was not reached (BL viewer and
`bl.digirati.io` manifest for ark `vdc_100147463086` refuse; HGV 20749 links them).

## Findings, 9 Nov 2026

- Not a substitution cipher. With a Greek bigram model (Homer, Xenophon; Perseus) the lines as written score
  -2.46 and -2.29 per bigram, against -3.43 for shuffled letters of line 1; all 24 Caesar shifts, Atbash and
  reversal score worse (best shift -3.7 / -4.0).
- They segment as Greek. Over a Homer + Xenophon word list with itacism collapsed, line 1 beats all 150 shuffled
  controls and line 2 beats 149 of 150. Best segmentations, unchecked and not sense yet:
  line 1 ἡμείων ὅτε μὴ ἐμοὶ ἴσα παρὰ λαῷ; line 2 ἡμῶν ἔτι ἐκ ἄτη ἐπὲ διὰ τοὺς. The recurrent pieces
  (ἔτους at the end of line 2, παρα, ἐμου, ἔτη ἑκάστῃ ...) suggest Greek in phonetic spelling,
  not another language.

## Remaining gaps

- Both lines: unread. Blockers: `needs-physical-access` (a photograph of BL Pap. 761 to settle the dotted letters and
  the lacunae) and the Litinas 2023 note (not online).

## Escalation

- Litinas, ZPE 227 (2023): not accessible (JSTOR moving wall; Köln hosts only older years). Ask a library or Litinas.
- BL images: the viewer and manifest returned 403/error to curl and Chrome; try again from a UK-friendly route or ask
  the BL for the image.
- Siblings: P.Oxy. I 89 (a similar receipt) has no such lines; not checked for the hand.
- Next: segment with a papyrus word list (DDbDP, itacistic spellings) rather than literary Greek.
