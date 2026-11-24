# Alonso Sánchez (Venice) to Charles V, May–August 1523 — RAH Salazar 9/28 (A-28)

Status: in progress (re-read 23 Oct 2026, b34: every record now reads; the site page and README row still describe
the 22 Oct audit state and are left to the write-up pass)

23 Oct 2026, re-read (REREAD_BRIEF batch b34, Claude Opus 5.5): **both uncalendared August letters read in full from
contemporary decipherments found on neighbouring leaves.** DECODE **R9768** (ff. 565-568, "Decrypted", never fetched)
is the second copy of R9767 and its **f. 567r is the court decipherment of R9767's two cipher passages**
(`R9767_decifrado_f567r.txt`); **R9770 f. 574r is the decipherment of the joint letter's cipher paragraph**
(`R9770_decifrado_f574r.txt`), which stands on R9769 f. 570v after the date (nine lines, missed in Sept: the letter is
not "all clear"). Both aligned group by group with the figures (`R9767_cipher_align.md`, `R9769_reread_log.md`): the
1522 key holds; new code **`pem` = *-mos*** (three occurrences under the decipherments); the old `yol` is `yoh` *causa*,
`xug` was spelled *mal*. Readings `R9767_reading.md` (0.684 plain, 1.000 explicit holes) and `R9769_reading.md` (the
whole joint letter transcribed; 0.575 plain on 1523 spellings, 1.000 explicit holes), with English. R9767 and R9769 read
(A), R9770 read through R9769 (B). Logs: `R9767_reread_log.md`, `R9769_reread_log.md`.

22 Oct 2026, reading audit (George Lasry's test: can sentences be built and translated?): the seven calendared
letters (R9670-R9690) read only through Bergenroth's English abstracts of the contemporary decipherings (reviewed B).
**R9767's cipher passages are decoded, not read** (code values with `…` between them; gist only), and R9769/R9770's
short cipher was never transcribed. The spelled runs are workable with the 1522 key, hence in progress.

Earlier status: done — found already calendared (Bergenroth 1866) with contemporary decipherings; the key is the 1522
key; the uncalendared August letter is read in part.

Catalogue entry 147 ("Alonso Sánchez (Venice) to unknown recipient, 10 ciphertexts", DECODE R9670–R9770).
Worked 2026-09-21. The recipient is not unknown: every letter is addressed "Sacra cesarea y catholica
magestad", i.e. Charles V. Sibling target: `../sanchez1522/` (the 1522 despatches, same cipher).

## What the records are

Metadata from `decode/metadata.tsv` (DECODE record pages, no login). All ten are flagged
`Inline Cleartext: Yes`, but that flag means passages written *in the clear* inside the letter. None of the
DECODE images carries an interlinear or facing decipherment. The contemporary decipherings Bergenroth cites
are filed separately in the volume and were not imaged with these records.

| DECODE | DECODE ff. | stamped ff. | date (from the letter) | what | CSP Spain 2 |
|---|---|---|---|---|---|
| R9670 | 18–24 | 35–38 | 8 May 1523 | Doge Grimani's death "de noventa años", Cornaro's illness; mixed clear/cipher | duplicate of no. 549 |
| R9671 | 40–43 | 40–42 | 8 May 1523 | same letter | **no. 549** (A-28 ff. 40–44) |
| R9672 | 78–79 | 78– | c. 20–23 May 1523 | "A xviij y xxiij del presente el duplicado por via de Genova escrevi"; the election of the new Doge (Gritti); facing leaf "A. Claro" | cf. no. 552 |
| R9674 | 81–82 | 81–82 | 20 May 1523 ("a xx de mayo"), "es treslado de otro" | duplicate | duplicate of no. 552 (ff. 83–85) |
| R9677 | 148–152 | 148–150 | early June 1523 ("Despues de los xx del passado no he escrito") | the Infante's powers | probably no. 554 (5 June, f. 157) |
| R9689 | 224–226 | | 13 June 1523 | | **no. 558** (ff. 224–228) |
| R9690 | 226–228 | | 13 June 1523 | | no. 558 |
| R9767 | 563–564 | 563–564 | **16 Aug 1523**, Sánchez alone | mostly clear; ~18 cipher lines on f. 563r | **not calendared** |
| R9769 | 569–571 | 569– | 16 Aug 1523, Caracciolo and Sánchez | clear: the league concluded, Pace left for Ferrara and Milan, the Infante's envoy, prisoners freed | not calendared |
| R9770 | 572–574 | 572–574 | 16 Aug 1523, Caracciolo and Sánchez, "es treslado de otro" | duplicate of R9769; short cipher at the head of the last written page; clear note f. 574 on the "mutua restitucion" instrument | not calendared |

Bergenroth's abstracts for nos. 549, 552, 554, 558 are in `csp/bergenroth_abstracts.txt`. Each says "Autograph
in cipher. Contemporary deciphering." So the content of the May–June despatches has been in print in English
since 1866, from the decipherings made at court. Nos. 566/577/587 (the joint letters of 16 July, 29 July and
18 Aug) are other letters, not these.

## The key

Unchanged from 1522. The code groups on every page examined (R9670, R9671, R9672, R9677, R9767) read
coherently with `../sanchez1522/key_codes.tsv` (Tomokiyo 2025 plus this project's additions): `xig`=de, `vog`=en,
`dom pud`=vuestra magestad, `ho`=que, `nuf`=no, `lal`=publica, `tum`=frances, `gub rac`=señor infante. It is
the same hand, the same three opening nulls and the same run of latin-looking cursive signs. Nothing new
was needed to read these letters, and nothing here contradicts the 1522 key.

## What was read here

`read_r9767.md`: the one letter not in Bergenroth, Sánchez's own despatch of 16 August 1523. The clear text is
transcribed in full. In the two cipher passages every code group is resolved except `pem` and `yol`, but the
spelled runs are only partly read. Gist: he refers the Emperor to the joint letter and answers the imperial
letter of 15 July; something in Venice leans French but "poco podra danyar"; the capitulation says nothing
about the Venetian money payment. The clear postscript says they did not bind the Infante to the defensive
league because the Venetians would not bind themselves against the Turk, and that shipping rights for the
Archduke's subjects could not be obtained.

R9769/R9770 (joint letter of the same day) are nearly all in the clear and were read at sight for the table
above; not edited.

## Why not more

A full edition of the cipher passages is transcription work at about a page per session (see the sanchez1522
notes). For eight of the ten records it would reproduce content already calendared from the contemporary
decipherings. The two records with new content are short and mostly clear. Closed as **found in print, read
in part**.

## Files

- `decode/` — `getrec.py`, `meta.py`, `fetch.py` (copied from sanchez1522; the cookie and rec*.htm are git-ignored), `metadata.tsv`.
- `csp/bergenroth_abstracts.txt` — the four CSP entries.
- `read_r9767.md` — the reading.
- Images (`img/`) are git-ignored; fetch with `python decode/fetch.py 9670 9671 …` and a DECODE cookie.

## Remaining gaps

- R9767 *[?diversas]* (one sign unmatched, the decipherment torn there) - blocker: illegible
- R9769 one numeral before *ducados de oro* (f. 569v l. 1) and *[?possessiones]* - blocker: illegible
- R9770 clear text not collated word by word with R9769 (a duplicate; nothing rests on it) - blocker: not-attempted
- `pem` = *-mos* not yet written to `../sanchez1522/key_codes.tsv` (proposed in b34)

## Escalation
- [x] siblings: R9670-R9770 tabulated; neighbours R9764-R9772 fetched 23 Oct (R9768 = R9767's copy + decipherment)
- [x] clear-pages: f. 567r (R9768) and f. 574r (R9770) contemporary decipherments transcribed and aligned
- [x] known-keys: the 1522 key (Tomokiyo 2025 + sanchez1522), unchanged
- [x] print: Bergenroth CSP Spain 2 for May-June; the August letters not calendared
- [x] key-rebuild: pem = -mos from three aligned occurrences
- [x] retry: 23 Oct 2026 (b34) every image of R9767, R9768, R9769, R9770 opened at full resolution

## 14 Nov 2026, full-texts audit: transcriptions

The audit asks for the cipher as written beside each decryption.

- **R9767, R9769**: the cipher had been transcribed on 23 Oct 2026 inside the alignment tables. Their cipher columns are now
  copied without change into `R9767_transcription.txt` (the two passages of f. 563r) and `R9769_transcription.txt` (the
  paragraph of f. 570v) and listed in `outcome.texts`. No image was opened again; both files say so in their header.
- **R9770**: the copy's cipher paragraph (ff. 573r-573v) was never transcribed; `transcription_missing`.
- **R9670, R9671, R9672, R9674, R9677, R9689, R9690**: never transcribed (viewed or identified by folio in September);
  `transcription_missing`.
- Blocker for the eight: without a login DECODE serves only 200-px thumbnails (a full-size request returns the
  placeholder image "Insufficient permissions to see the full image"); the record pages and the public API carry no
  transcription or attachment; `bibliotecadigital.rah.es` answered with a bot check. A logged-in fetch of the DECODE
  images unblocks it.
- No change to class, method, states or fraction_read.

