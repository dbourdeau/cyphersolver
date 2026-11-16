# Lucini (nuncio in Madrid) to the Secretariat of State, 13 Oct 1767 — READ

Catalogue 246: "Abbot Vincenti and nuncio Lucini (Spain) to The Secretariat", DECODE R120
(`ASV_i1025_SdS_Spain_304-1`). ASV (AAV), Segreteria di Stato, Spagna 304 ("Cifre dell'abate Vincenti e mons.
Lucini, nunzio in Madrid, giugno-decembre 1767", Tomo II, ff. 1-492). DECODE's date 2 Jun 1767 is the start of the
volume. The four imaged pages are one letter, dated **Madrid, 13 Oct 1767**, from the nuncio Cesare Alberico Lucini
(nuncio Dec 1766 – Feb 1768) to the Cardinal Secretary of State. Page 4 carries the folio number 280.

**Result (21 Sept 2026): read.** The letter is in clear except its last sentence, which goes into figures after
"tenda ad estinguere i" and runs to the foot of p. 4. The rest of the letter is on the next leaf, which DECODE did
not image. The cipher part reads in full with Lasry's key; one nomenclator code (8107) stays open.

## Key

Lasry reconstructed the key in Oct 2020 from the sibling R121 (`ASV_i1025_SdS_Spain_304-2`, f. 485, Dec 1767) and
attached it to both records (`DOC_R120_D3314`). It has fixed-length 2-digit homophones for letters and syllables
(a 17|71, e 13|49, i 42|92, che 02, non 61 …), `5` a null, and 4-digit nomenclator codes beginning with `8`. No
2-digit element begins with 5, so the parse is deterministic (`decrypt.py`).

Nobody had deciphered R120's own cipher passage: DECODE has MEG's digit transcription (June 2020) but no decryption
of it. The only decryption attached to R120 is Lasry's text of the R121 letter.

Changes to the key made here:

- **63 = se, not di.** The first occurrence gives "si fanno se-n-ti-r-e" (sentire). The same fix improves Lasry's
  R121 text in two places: "perche 63 gli fa credere" (perché se gli fa credere) and "cades 63 in un mal cronico"
  (cadesse). di is 23, which also occurs in this passage ("in di-v-e-r-si").
- **03 = chi** (monar-03-a = monarchia; the key has no h).
- **8061 = qual** ("i qual-i", alphabetically between 8046 perche and 8063 quando).
- **8099 = zion** ("sollev-a-zion-i", last code of the alphabetical block before 8107+).
- **8700 = anno** ("si f-anno"; the 87xx block has 8706 giorni, 8720 pasante).
- **8107 open.** It falls between the end of the first alphabetical block (8099) and 8140 Camera, so it is probably a name
  or noun in A–Ca: "si fanno sentire in 8107-e". In 1767 that might be America (the Mexican risings of that year
  over the Jesuit expulsion), Andalusia or Aragon. This is a guess and is not used in the reading.

Transcription: MEG's line 1 has `3 2 3 2 6 6`; the image has `3 2 7 2 6 6` (in-te-r-n-i). The rest of her figures agree
with the image. The corrected figures are in `cipher.txt`.

## What the letter says

Right after Cardinal Pallavicini (Lucini's predecessor) left, the Marqués de Grimaldi, Secretary of State, sent
the nuncio a note (enclosed with the letter). In the king's name it asked for the faculty that Pallavicini had granted on 1 July
1766 to be renewed: the power to make churchmen submit to examination and give evidence before lay judges in cases
of crimes against His Majesty (lèse-majesté). The king wanted it without limit of time, and extended from the regular clergy to the
secular clergy. Lucini first thought the faculty had been a special one given to his predecessor "in occasione
della nota sollevazione" (the Madrid Esquilache riot of March 1766) and had lapsed. He then examined the printed cedula and found that
Pallavicini had made the faculty pass to his successors. So he offered the king a renewal (proroga) with his
predecessor's cautions, which the Pope had approved (letter of 7 Aug 1766). For the secular clergy he would
subdelegate to the bishops, as Pallavicini had done for the clergy of Cuenca (approved 4 Sept 1766). He does not
know whether the king will accept a time-limited renewal, and asks for instructions. Then the cipher:

> Io credo, che la dimanda che mi si fa tenda ad estinguere i *tumulti interni della monarchia, i quali di
> quando in quando si fanno sentire in [8107], e sollevazioni che succedono in diversi* [… continued on the
> next leaf]

That is: "I believe the request made to me aims at putting down the internal disturbances of the monarchy, which
from time to time make themselves felt in [8107], and the risings that break out in various [places] …". The
secret part is the nuncio's reading of Madrid's motive: the crown wants a permanent power to try clergy for sedition,
after the 1766 riots and the Jesuit expulsion of April 1767.

Full letter text: `READING.md`.

## Sources and files

- `decode/`: DECODE record pages and metadata for R120 and R121, MEG's transcription (`DOC_R120_D2343`), Lasry's key
  (`D3314`/`D3316`) and his R121 decryption (`D3313`/`D3315`), EHum's R121 transcriptions. The page images
  (`IMG_R120_I885-888`) are git-ignored (not public domain).
- `cipher.txt`: the corrected figures. `decrypt.py`: parser and key with the changes above. `decrypt_output.txt`: its output.
- Literature: no edition of Lucini's 1767 despatches found (web search 21 Sept 2026). Lucini: nuncio in Spain
  18 Dec 1766 – 19 Feb 1768, successor of Lazzaro Opizio Pallavicino.

Open: code 8107, and the rest of the cipher sentence on the next leaf (f. 280v/281, not imaged). R121's text could be
redone with 63 = se.

Contamination: Lasry's key was public on DECODE (logged-in attachment) and was used directly. The decryption of the
R120 passage, the code identifications and the corrections are new here.

**23 Oct 2026, verification 5 (plain bar; research/reading_audit/VERIFY5_BRIEF.md)**: the sweep had scored decrypt_output.txt, the raw group decode. READING.md is the reading; a '## Reading' heading now marks its body (clear text from MEG's transcription with the deciphered closing passage): plain 0.771, explicit 0.914. 8107 stays open; the sentence runs on to a leaf not imaged. Rescored with research/reading_audit/v2_score.py (plain word-list share and explicit-hole share); both figures are in each entry's reading_review note. Keeps read.

## Read share over cipher words only (16 Nov 2026)

README Conventions (16 Nov 2026): the read share counts the words written in cipher only. The cipher is the one
passage set in *italics* in `READING.md` (the last sentence, *tumulti interni … in diversi*); the clear Italian of
pp. 1-4 is left out.

- R120: 0.99 -> **0.952** (20 of 21 cipher words). The one hole is code 8107. The `[…]` after the passage is the rest
  of the sentence on the next leaf, which DECODE did not image: it is not on this document's pages and stays out of the
  count (reading it would need the next leaf from the archive; see Result above). Whole letter, clear included, not the measure: 0.99.
- Class unchanged: **read** (20/21 meets the 95% bar). The token figure, 81 of 82, is unchanged.

