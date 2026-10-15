# Cardinal of Como to Anselmo Dandini, nuncio in France, Rome, 8 August 1580 — ASV Segr. Stato Francia 283C ff. 89r–90r (DECODE R73) — NOTES

Split on 14 Oct 2026 from `dandini1580` under the one-key rule (George Lasry, 14 Oct 2026). The old entry (catalogue
244) joined this enclosure with R72 (f. 52, 16 May 1580). The two share the frame and the nomenclator but not the
letter key: Lasry's key reads R73 and gives nonsense on R72. R72, with the letter key rebuilt here, keeps the old
entry: [`targets/dandini1580/`](../dandini1580/NOTES.md), page `dandini1580.html` ("a different key, with its own page").

Status: read (Lasry 2020; 96.1% of groups have a value in his file, measured 14 Oct 2026).

**Outcome: read from existing decipherment.** George Lasry recovered the key (DECODE attachment D3190, 24 Oct 2020)
and decrypted the whole enclosure (D3191, from KaJo's 2017 transcription D1789). This project adds no reading: it
measured his decryption and, on 14 Oct 2026, found that the record's own attachments date the enclosure and hold a
contemporary clear copy of its second section (below). Session 2026-09-21; split 2026-10-14.

## The document

- ASV, Segreteria di Stato, Francia 283C ("283C-2" on DECODE), ff. 89r–90r: three pages of figures (89r, 89v blank
  or transparency only, 90r), damaged paper with bleed-through. Images `IMG_R73_I576_P1`, `I577_P2`, `I578_P3`
  (fetched 14 Oct 2026 with the shared cookie; git-ignored, in the main checkout's `targets/dandini1580/decode/`).
- **Date, from the record's attachments (14 Oct 2026).** The DOC images on R73 (D1135–D1139, same folder) are the
  covering letter and a clear sheet:
  - ff. 88 and 92: Como's clear letter, "Di Roma a 8 d'ag.to 1580", signed "Il Car.le di Como", with the note "Con
    mezzo foglio di Cifra" under the signature; f. 92v is the address to Dandini, nuncio in France.
  - f. 91: a clear text headed "Cifra … dal S.r Car.le di Como con l're di 8 agosto 80", beginning "Non lauda N.S.re
    che V.S. tenghi proposito alcuno con la regina m[ad]re nel particolare della monaca per non darle occasione di fare
    con tale coperta qualche rumore non conforme alla mente di S.S.tà …" and ending "… in questo proposito". This is
    a contemporary decipherment of the second section of R73 (f. 90r, from group 465 of Lasry's file, "non lauda M.S.
    che V.S. tenghi proposito alcuno…", to the end "in quello proposito"). The first section (f. 89r, the marriage
    negotiation) has no clear copy on the record.
  So the enclosure went with Como's letter of 8 August 1580. The old profile had "date unknown".
- DECODE status "partially decrypted"; Lasry's key and decryption are filed on R72 (DOC_R72_D3190, DOC_R72_D3191;
  D3191 = DOC_R73_D3193).

## The cipher (Lasry's key D3190)

Two-digit letter homophones, every second digit even; vowels with one or two homophones; no nulls. Nomenclator: three
digits plus a mark (`^`) for pronouns, titles and common words: 124^ S.S., 824^ N.S., 822^ V.S., 144^ M.S., 224^
S.M.tà, 266^ che, 200^ non, 366^ per, 800^ mente, 988^ essere, 966^ tanto, 744^ (r)egina. Letter values (from his
file): a 50 92, c 14, e 18 52, i 26 62, l 28, n 22, o 34 72, r 40, t 44, u/v 46 82 … (`decode/DOC_R72_D3190_3190.txt`
in `targets/dandini1580/`, kept there because R72's parse uses its frame).

## The reading

Lasry's decryption (`decode/DOC_R72_D3191_3191.txt`, moved here from dandini1580 on 14 Oct 2026), gaps as in his file.
f. 89r: a princely marriage negotiation ("il matrimonio … N.S. è certificato che il gentilhuomo … ha parlato";
"la M.S. si movere a abbracciar la pratica"; "sarebbe S.S. intieramente certa di muoversi con buon fondamento a
trattare la pratica"). f. 90r: the nun. "non lauda M.S. che V.S. tenghi proposito alcuno con la [Regina] nel
particolare della monaca per non [darle] occasione di far con tal coperta qualche rumore non conforme alla mente di
S.S."; the office "che N.S. ne fece con il confessore"; the King could do the same "con officio simile a quello, ma è
ben bisogno di procedere tanto circonspettamente che non ne nasca rumore né disordine alcuno"; "la riprensione sia
mossa e spinta da N.S. con il re".

Measured (`measure_r73.py`, 14 Oct 2026): 1,082 groups; 1,040 have a value in Lasry's file (96.1%); open: 32
illegible in the transcription, 6 occurrences of nomenclator groups he left unread (866^, 466^, 766^, 324^, 300^,
and <744^>, which his key lists as 744 "egina" without the mark), 4 groups he marked with "?" (80?, 9?, 90?).

Check against f. 91 (by eye, 14 Oct 2026, not a full collation): the clear copy and Lasry's f. 90r agree in
substance line for line. Differences seen: f. 91 "N.S.re" where Lasry has 144^ M.S.; "darle" where his values give
"parlio" (groups 36 … 26); "regina m[ad]re" where his file has <744^>.

## Remaining gaps

- 32 illegible groups - blocker: illegible; damaged paper and bleed-through, transcription marks them "?"
- nomenclator groups 866^, 466^, 766^, 324^, 300^ - blocker: open-codes; one occurrence each, no clear copy of the
  f. 89r section, not filled by Lasry

## Escalation

- [x] siblings: R72 (same frame, different letter key; own entry); the DOC attachments of R73 opened 14 Oct 2026:
  covering letter ff. 88/92 (date) and the clear copy f. 91
- [x] clear-pages: f. 91 is the decipherment of the f. 90r section; nothing for f. 89r
- [x] known-keys: Lasry's D3190 is the key; R72's letter key does not apply
- [n/a] print: not searched in print here (Nunziature di Francia for 1580 not checked); the reading is Lasry's
- [n/a] key-rebuild: Lasry's key is complete for the letters; the open nomenclator groups occur once each
- [n/a] retry: the reading is Lasry's; not re-decrypted here

## Assumptions for George's review

- Credit: George is credited with the prior solution of R73 only: key D3190 and decryption D3191, both of which his
  DECODE files show reading R73 (D3191 is the KaJo R73 transcription). He is not credited with R72's letter key,
  which his key does not read; on R72 the credit is limited to the frame and nomenclator taken from D3190.
- The date (with Como's letter of 8 Aug 1580) and the f. 91 clear copy are this project's reading of the record's
  DOC attachments, not his.
- The fraction (96.1%) counts his file as given; the "?"-marked values (80?, 9?, 90?) are counted as unread.

## Files

- `decode/DOC_R73_D1789_1789.txt` KaJo's R73 transcription (2017); `decode/DOC_R72_D3191_3191.txt` Lasry's R73
  decryption (2020); `measure_r73.py` (count; `--reveal START N` writes the reveal tokens from his file).
- Images and DOC scans are not committed (ASV); they are in the main checkout's `targets/dandini1580/decode/`.
