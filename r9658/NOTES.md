# Lope Hurtado de Mendoza (Rome) to Charles V, 23 December 1522 — RAH 9/26 ff. 371–376, DECODE R9658

Status: no write-up

Catalogue entry 145 ("Jerónimo Adorno? to unknown recipient", undated). Worked 22 Sept 2026.

## Result: calendared from a contemporary decipherment (Bergenroth 1866)

The DECODE metadata is wrong on sender, recipient and date. The record is **CSP Spain vol. 2 no. 510**:

> 23 Dec. M. Re. Ac. d. Hist. Salazar. A. 26. ff. 371-377. 510. Lope Hurtado De Mendoza to the Emperor. The Pope says
> he will not enter into a league with him (the Emperor) and the King of England as long as he has any hope of
> concluding a general peace. The Bishop of Veruli is in Rome with the Swiss ambassadors. They ask 36,000 ducats. [...]
> Indorsed: "To the King. 1522. From Rome. Lope Hurtado. The 23rd of December. Answered." Spanish. Autograph in
> cipher. Contemporary deciphering. pp. 10.

Full abstract in `csp_510.txt` (from british-history.ac.uk, CSP Spain 2 pp. 510-519).

What the six DECODE images show agrees:

- f. 376v docket: "Al Rey — De Lope Hurtado de Roma a xx[.] de dezie[mbre] 152[.]". At DECODE's resolution I first took the day
  for xxvi and the year for 1523; the volume (Salazar A-26 = 1522) and CSP (23 Dec, "1522") settle both.
- ff. 371r–375v: wholly in cipher, about 11 written pages. Paragraphs open with the paragraph mark. It opens
  "De Valladolid a xvj de noviembre..." in the clear (answering the Emperor's letter of 16 Nov 1522), and a clear note
  on f. 372v reads "es duplicada de la que llevo el [correo] del arçobispo de Bari". The last page (f. 376r) is dated in the clear
  "xx[.] de deziembre" and signed with a paraph.
- A stray endorsement on the left of image 1 names the Duke of Sessa: it belongs to the neighbouring letter, CSP no. 509
  (Sessa, 17 Dec 1522, ff. 359–365, "in the cipher of Lope Hurtado"). "Jerónimo Adorno" is probably taken from CSP
  no. 513, Adorno's 26 Dec letter from Venice at A-26 ff. 401–406.
- The cipher is Lope Hurtado's 1522 system (`../lopehurtado/`, catalogue 144): the code groups `ton` (que), `zar` (de),
  `xul` (lo), `rab` (vuestra magestad), `tu` (no), `yub` (el), `top` (por), `taf` (papa) run through every page.

The contemporary decipherment Bergenroth used is not among the DECODE images (all six show the cipher and its address
leaf only).

## Why it is not re-read here

The content has been in print, in English, since 1866. A fresh reading would mean transcribing about 11 cipher pages under a
key that is itself only partly rebuilt (`../lopehurtado/key_codes.tsv`, still "in progress"; the 1523-24 letters under the same
system reach a quarter to two thirds per letter without a crib). That cannot reach the 95% read bar, and the
decipherment on file at the RAH would fix the result. A future session could add this letter as a crib source for
the 1522 key: its decipherment, somewhere in Salazar A-26, is the text to seek (RAH Biblioteca Digital), not the cipher.

## Remaining gaps

- The whole cipher text of ff. 371r-375v - blocker: needs-physical-access; the contemporary decipherment in Salazar A-26 is not imaged on DECODE; content known from CSP Spain ii 510

## Escalation

- [x] print: Bergenroth CSP Spain ii pp. 510-519 (December 1522) grepped by folio: no. 510 = these folios
- [x] siblings: identified as Lope Hurtado; sibling target lopehurtado/ (catalogue 144, same volume and cipher)
- [x] known-keys: the 1522 Lope Hurtado code groups recognised on every page; not applied line by line
- [x] clear-pages: all six DECODE images viewed; no decipherment among them
- [x] retry (access): RAH Biblioteca Digital (bibliotecadigital.rah.es) tried 22 Sept 2026 for Salazar A-26 and the contemporary deciphering: it returns nothing to automated requests (403 / bot check; see lopehurtado/NOTES.md). Daniel would have to search it by hand for 'Salazar y Castro A-26' and pull the deciphering near ff. 371-377

Catalogue entry 145 removed on 22 Sept 2026. DECODE correction queued (`decode_updates/queue.json`).
Images (`img/`) and the record page (`decode/`) are RAH/DECODE material, git-ignored.
