# Morosini's legation, second key "F22b": two enclosures of spring 1589 (AAV Segr. Stato Francia 22/32–33; DECODE R53, R54) — NOTES

Split on 14 Oct 2026 from `morosini1588` under the one-key rule (George Lasry, 14 Oct 2026). The old entry (catalogue
item 243) held all 36 cipher enclosures of Francia 22; 34 of them are in Meister's key no. 40 and stay there, with
R17 from Francia 18: [`targets/morosini1588/`](../morosini1588/NOTES.md), page `morosini1588.html` ("a different
key, with its own page"). These two enclosures are in a second, syllabic key that DECODE files as "ASV – F22b".

**Outcome: read with known key, in part.** George Lasry's partial reconstruction of the F22b key (DECODE R53 D3187,
R54 D3188, 24 Oct 2020, about 70 elements) was applied on 19 Sept 2026 by the decoder of `morosini1588`
(`decrypt.py --f22b`). R53 reads in most of its length, R54 in fragments (0.752 of letters in attested words, measured). Session 2026-09-19; split, measure and key-rebuild attempt 2026-10-14.

## The documents

- **R53**, Francia 22/32, image 499v. A clear covering passage (Morosini waits anxiously for letters from Rome
  granting his leave) and 785 cipher digits (DECODE transcription D1717, Midas, 31 Mar 2017). Place and date from the
  series: Tours, spring 1589.
- **R54**, Francia 22/33, image 502r. 663 cipher digits (D1825, NiLan, 6 Apr 2017); clear dating line "Di Molins à gli
  xi di Maggio 1589".
- Transcriptions and Lasry's key files: `decode/DOC_R53_D1717_1717.txt`, `decode/DOC_R54_D1825_1825.txt`,
  `decode/DOC_R53_D3187_3187.txt`, `decode/DOC_R54_D3188_3188.txt` (moved here from `morosini1588/decode/` on
  14 Oct 2026). Images on DECODE (login), not committed.

## The key (Lasry's F22b reconstruction)

Syllabic, elements of one or two digits, no nulls (his note: "variable length, not deterministic"). Nomenclator of
three digits, starting 10, 11 or 49, or a 1 with a dot on top (the dot on the first digit, where Meister no. 40 puts
it on the middle one). Examples: a 3|7, ba 86, ca 73, ce 51, di 93, e 5|8, la 60, ne 70, o 15|18, re 43, si
83|85|89|95, ta 47, u 21|54; 102 mpo, 116|216 me, 495|498 chi, 496 che; 1̇24 umena (Mayenne), 1̇85 nauarro, 1̇51
"h.s.re", 1̇86 mente. The values are in `morosini1588/decrypt.py` (`KEYB`, `NOM_B`), copied from his file.

## The reading

Decoder output: `decrypt_raw.txt`, per record with the clear headings in `plaintext_by_record.txt` (both moved out of
`morosini1588` on 14 Oct 2026; a rerun of `decrypt.py --f22b` that day gives a few different letters, the shared
model having been rebuilt since). R53: the vice-legate of Avignon has arrived at Tours and lodged near Plessis;
"si e fata una mescolanza ala corte di heretici et di catolici"; something is said of Mayenne ("Umena") near Le
Mans (the 19 Sept summary; the decoded stretch also mentions a shirt, a napkin and a dinner with "sua maiesta",
not interpreted here). R54: fragments only: the
heretics growing stronger at court beside the Catholics ("mescolati gli heretici co i catolici ala corte"), the
writer's own fears, a request to make something known. Graded M/C.

**Measured (14 Oct 2026, `measure_sense.py`):** share of decoded letters that fall in Italian word forms attested
at least twice in the it-cinquecento corpora, after the word split of `../morosini1588/make_decryptions.py`
(`decode_updates/decryptions/R53.txt`, `R54.txt`): R53 510/645 = 0.791, R54 383/542 = 0.707, both 893/1,187 =
0.752. Control: the 34 fully read Meister no. 40 records of the same legation score 0.817 by the same measure (split
errors, spelling and slips hold it below 1). The measure is an upper bound (the splitter can cut nonsense into short
real words); by eye R53 reads in most of its length, R54 in fragments. The 19 Sept estimate was "about half".

## Remaining gaps

- R53, R54: the stretches that do not read as sense (about a quarter of R53, more of R54) - blocker: no-key-material; Lasry's F22b reconstruction (about 70 elements) is the only key material; Meister 1906 prints no second Morosini key; no decipherment or clear copy on the records; a rebuild from these 1,448 figures does not fix the missing values (Escalation)
- R53, R54 nomenclator groups outside Lasry's list - blocker: open-codes; few occurrences, no context yet

## Escalation

- [x] siblings: all 36 Francia 22 enclosures opened (19 Sept 2026); only R53 and R54 use this key (R35, the Spanish copy, is in Meister no. 40)
- [x] clear-pages: the clear passages of R53 (covering text) and R54 (dating line) are not decipherments of the cipher
- [x] known-keys: Meister no. 40 is the key of the other 34 enclosures; these two were set apart as a second key (DECODE "F22b") and Lasry's F22b reconstruction applied
- [x] print: Meister 1906 searched (OCR in the main checkout's targets/vatican5/meister.txt, 14 Oct 2026): his index lists Morosini only at p. 393 (no. 40); his no. 32, "La cifra del vescovo di Brescia Nuntio in Francia" with the canon Rinolfo Rinalducci (1585-90), is a short cover-name list (Amore = the King of France, Lucerna = the Pope), not this syllabary; no edition of the legation exists (19 Sept search). The Vatican's own cipher registers were not searched (no digitised copy known here).
- [x] key-rebuild: `rebuild.py` (14 Oct 2026): Lasry's values fixed, each of the 24 empty two-figure codes given the missing syllable or letter that best raises the decoder's language-model score (coordinate ascent, margin 3 nats, restarts). Fitted on R53 alone it gives 10 values (`rebuild_R53.json`: 42 se, 27 va, 72 con ...), on R54 alone 11 (`rebuild_R54.json`: 42 fi, 59 se, 11 ve ...); the two fits agree on one code (84 c), and each breaks stretches that read before in the other record (R53 "si e fata una mescolanza" becomes "ecacauaracoscolanza" with the R54 fit). 1,448 figures are too few to fix the missing values; none adopted.
- [x] retry: R53 and R54 re-decoded with both fits; no stretch became readable that was not before, so the reading stays on Lasry's key as filed.

## Assumptions for George's review

- Credit: George is credited with the F22b key only (D3187/D3188 on R53/R54), the key these two records are read
  with. His other Francia 22 file (R18 D3175, the partial reconstruction of Meister no. 40) is credited on
  `morosini1588`, not here.
- The reading of these two records is the project's application of his partial key; no decryption of R53/R54 by
  him is on DECODE.

## Files

`decrypt_raw.txt`, `plaintext_by_record.txt`, `decode/` (transcriptions and Lasry's key files), `measure_sense.py`,
`rebuild.py` with `rebuild_R53.json`/`rebuild_R54.json` (the rejected fits), `reveal.py` (writes
`docs/reveal/morosini1589.json` from R53). The decoder is shared
with the sibling entry: `python ../morosini1588/decrypt.py --f22b`.
