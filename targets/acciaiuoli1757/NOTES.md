# Acciaiuoli (nuncio in Lisbon) to the Secretariat of State, 1758–60 — read (re-read 22 Oct 2026)

Status: in progress (re-read 22 Oct 2026: all eight letters now read; the write-up pages still describe the audit state).

Catalogue: "Portuguese nuncio Acciaiuoli and the abbot Testa to The Secretariat", DECODE R25, R195–R201 (8 records).
ASV (AAV), Segreteria di Stato, Portogallo 117 ("Lettere di mons. Acciaiuoli, nunzio in Portugallo, e dell'abbate
Testa, 1757-1761", ff. 2–585). DECODE's date 18 Jan 1757 is the start of the volume; the cipher leaves date from
12 Sept 1758 to 1760.

**Result (19 Sept 2026): read.** Lasry's reconstructed key (DECODE, Oct 2020) had already turned all eight into a
letter stream, but DECODE posted no Italian text and left the 107 distinct four-digit code groups open. Here the stream is
split into words and 25 codes are fixed from the three contemporary decipherments on the leaves (R197–R199), plus
a few more from context. The full text is in `READING.md`. About 80 of the 107 distinct codes that occur once or twice stay open, and
a few passages in the long R200/R201 are broken by transcription slips.

22 Oct 2026, reading audit (George Lasry's test: can sentences be built and translated?): **read in part**.
R196, R197, R198 and R199 read (the three deciphered on the leaf, and R196 with a few open codes). **R25, R195, R200 and
R201 are decoded, not read**: the story follows, but an open code or a gap breaks almost every sentence. Read: 2,050 of
8,326 cipher tokens (24.6%). The earlier "READ" claim below is withdrawn.

22 Oct 2026, re-read (REREAD_BRIEF, batch b12, Claude Opus 5.5): **all eight read.** The DECODE records carry png
attachments (DOC_R25_D944-947, D1107-1109; DOC_R195_D1400-1407; DOC_R200_D1411-1413, D1453-1460; DOC_R201_D1414-1416)
that this file had called "key and work images". They are the Secretariat of State's own clear decipherments ("Decif.
li 11 Ottobre" etc.) and working drafts, Portogallo 117 ff. 90-113 and 161-162. The clear texts of R25 (ff. 90r-91r),
R195 (f. 94r), R200 (ff. 108r-109r, second copy ff. 110r-111r) and R201 (f. 161) are transcribed in
`texts/R*_decipherment.txt` and aligned word by word with the key decode (`research/reading_audit/b12_dec.py`,
`b12_align.py`; `texts/R*_align.tsv`); the readings are `texts/R*_reading.md`, English `texts/R*_en.md`, logs
`texts/R*_reread_log.md`. Clean sentences (reading bodies): R25 0.87, R195 0.91, R200 1.0, R201 0.95. Findings:
03 is "per", not "nel"; 2530 = Marchese (not chirurgo); 2823 = Sua Maestà; 2803 = Segretario (the draft interlines it
over "Sig.re de Carvalho"); R195's hole "poiché non . . ." (margin "non s'intende") is "poiché non ha da durare" on the
cipher image. The same attachments hold clear decipherments of R196 (f. 97) and R198 and an unrecorded cipher letter of
28 Nov 1758 ("Si continua a mantenere il segreto sulla causa del male del Re", f. 107). Fraction read 1.0.

## Key

Lasry, DECODE `DOC_R25_D3232` (reconstructed): fixed-length 2-digit homophones for letters and syllables (a 04 38 55,
e 84, i 08 53, o 81, s 88, il 43 91, che 39, non 14 …), `6` a null, 4-digit nomenclator codes beginning with `2`.
No 2-digit element begins with 2 or contains 6, so the parse is deterministic. Unassigned pairs that turn up
(82, 92, 42, 12, 32, 72, 02) are transcription slips.

## What the letters say

- **R25 (12 Sept 1758):** the nuncio's secret account of the attempt of 3 Sept 1758 on José I. The king, coming back
  from a lady "delle prime famiglie" (the young Marchioness of Távora), was fired on in his calesse; his valet
  and favourite Pedro Teixeira was badly wounded, and so were the postilion and the mule. The king was hit in the
  right arm and taken by the surgeon to the Real Barraca. The blow was thought to come from her relatives or from
  Teixeira's enemies. The Infante Don Manuel spoke of it to the nuncio "con il sospetto".
- **R195, R196 (Sept 1758):** the public version is illness. The arm is said to be broken and to stay impeded. The
  king is in bed all day. Fleets and ships are held back, to the merchants' loss.
- **R197–R199 (Oct 1758, deciphered on the leaf):** abscess and fever, not erysipelas. The arm will stay impaired.
  After the death of his sister, Queen Barbara of Spain, José says Ferdinand VI has promised to marry his daughter
  Maria Francisca, which the Spanish minister contradicts.
- **R200 (28 Nov 1758):** Carvalho (Pombal) is despotic and the king fears him. The court, the Infantes and the
  confessors. The expulsion of Jesuits and a lay brother of the Society. The nuncio is distrusted.
- **R201 (1760):** conferences of the Conde d'Oeiras (Carvalho). The Princess of Brazil's marriage to Infante Don Luis
  of Spain or to Don Pedro; London is alarmed at a Bourbon on the Portuguese throne; "il paese freme" for the
  union with the Infante Don Pedro. That marriage took place in June 1760.

## Sources and files

- `decode/` DECODE record pages, the digit transcriptions (`DOC_*_D165x-1663`), Lasry's key (`D3232`) and his
  decryption of all eight (`D3231`, one file attached to every record). The DOC_*.png files are key and work
  images. Images are in `img/` and are git-ignored (not public domain).
- `lasry_stream.txt`: Lasry's decryption flattened into one string per letter. `code_contexts.txt`: each code
  with the text around it.
- Literature: no edition of these ciphers found. The attempt of 3 Sept 1758 (the Távora affair) is well known.
  Acciaiuoli's reports are cited from the ASV but not printed in cipher or clear (web search 19 Sept 2026).

Contamination: Lasry's letter-level decryption was public on DECODE (logged-in attachments) and was used directly.
The word division, the code identifications and the historical reading are new here.

## Verification 5, 23 Oct 2026

Plain-bar check (Italian 1758, so the plain word-list share is a bar as well as the explicit-hole share). R25 and R195:
false alarms; their reading files had no `## Reading` heading, so header and notes were scored. Heading added; bodies
R25 plain 0.87 / explicit 1.0, R195 0.818 / 0.818; keep read. R196 had no reading file (the sweep scored Lasry's raw
decode, plain 0.355). Its clear decipherment (f. 97r, `DOC_R196_D1449`, recorded here on 22 Oct but never transcribed)
is now `texts/R196_decipherment.txt`; it agrees with the decode clause by clause (2754 pubblic-, 2131 ancora, 2141 come,
2349 avvis-, 2907 due, 2189 quest-). Reading `texts/R196_reading.md`, English `_en.md`, plain 1.0; keeps read, grade A.

## Read share over cipher words only (16 Nov 2026)

Recount for the rule that the read share counts cipher words only. All eight records are wholly enciphered
despatches (`ciphertext_all.txt` is figures throughout), and each reading is the Secretariat of State's clear
decipherment or Lasry's decode aligned word by word with the figures, so every word of every reading body is a cipher
word and there is no clear text to leave out ("not split" in the tool's tsv means there is no marked clear text). Recounted by hand:
R25 288 words, 1 hole (0.997); R195 139 words, 7 holes (0.952, the margin of the bar: [?solamente], [?assicurato] and
the five words of [?della gente di quei paesi]); R196 1.0; R197-R199 1.0; R200 343 words, 1 hole in the body, 0.995 ->
**0.997** (the second [?Spagna] stands in the Notes); R201 1.0. No state, class or page figure changes.

## Remaining gaps
- closed 22 Oct 2026: R25, R195, R200, R201 read from the Secretariat's clear decipherments on DECODE (texts/R*_reading.md)
- R200 code 2339 (an ambassador; the fair copies leave it blank, the draft gives 'di Spagna') - blocker: no-key-material
- R25 'Vilasso' (the figures, checked on the image, give 'suo iasso'; word not identified) and R195 'pare solamente assicurato' (figures legible, the key does not give these words) - blocker: no-key-material

## Escalation

Added by the reading audit (22 Oct 2026), which relabelled the documents that do not build sentences as decoded,
not read. Re-read 22 Oct 2026 (b12):

- [x] siblings: R196-R199 and their decipherments used for the code table
- [x] clear-pages: the png attachments on DECODE are the Secretariat's clear decipherments of R25, R195, R200, R201 (used)
- [x] known-keys: Lasry's key (DOC_R25_D3232) used; 03 corrected to per
- [x] print: none found (19 Sept web search); not needed now
- [x] key-rebuild: code values from the four decipherments (texts/R*_align.tsv)
- [x] retry: all four re-read and aligned; R195 l. 11 re-read on the image
