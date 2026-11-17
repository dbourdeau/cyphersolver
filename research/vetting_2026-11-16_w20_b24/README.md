# Vetting wave 20, batch 24 (16 Nov 2026)

18 leads: 1776 2789 907 879 1802 2790 2795 2798 2927 2921 1146 1158 2546 2551 2918 1163 1292 1426.
Proposals in `proposals.json` (not applied; the lead agent applies them). No lead is proposed `open`.

Routes used: TNA Discovery API `/API/records/v1/details/<id>` and `/API/search/records` (`tna.py`, raw JSON in `raw/`);
archive.org djvu.txt for CSP Dom. 1655, CSP Dom. 1656-57, CSP Dom. W&M 1689-90 and HMC Downshire IV; British History
Online by curl (CSP Foreign vol. 16); Kalliope record pages by curl (SRU with `ead.all` is unsupported); the 11 Nov
archieven.nl harvest (`research/sweep_2026-11-11_dutch_2/anl_det.jsonl`). `prior.py` runs known.py and greps Tomokiyo's
unsolved.htm and Lasry's GL.htm (fetched 15 Nov 2026); output in `prior_out.txt`: no relevant hit for any lead.

| id | verdict | conf. | deciding fact |
|---|---|---|---|
| 1776 | none | low | TNA Discovery marks SP 36/65 f. 17 "missing." |
| 2789 | partly_read | medium | Plain letter with code names; the interceptors' list of the names (27C) is filed with it |
| 907 | duplicate | medium | Aggregate; its 1656 letters are catalogue 978-987. Three letters outside them need single leads (below) |
| 879 | none | low | TNA: "in cipher (or shorthand)"; not digitised |
| 1802 | none | low | Same volume, same wording; not digitised |
| 2790 | partly_read | medium | Plaintext "Extract (folio 99)" of the ciphered letter filed in front of it |
| 2795 | partly_read | high | "intercepted and translated", only the names still in cypher |
| 2798 | none | low | "account in code" on a 1548 merchant account: may be a price code; image needed |
| 2927 | partly_read | high | CSP preface: Pointis letters "deciphered by Dr. John Wallis"; "Part of the letter is undeciphered" |
| 2921 | partly_read | high | Plain letter on BHO with six coded name numbers |
| 1146 | none | low | Aggregate of seven items; split first; Akkerman blocker stands |
| 1158 | not_cipher | medium | Plain report signed in cipher, and a plain letter correcting a decipherment |
| 2546 | none | low | 11 Nov held block stands; only "soms enige woorden" in code; no scans |
| 2551 | read | medium | Inventory gives the letter's content (tea invitation for St Clare's day) |
| 2918 | partly_read | medium | HMC Downshire IV calendars the letters in full sense; only cover names unread |
| 1163 | none | low | Minna's cipher letter not in the Nachlass; Kinkel's replies discuss deciphering it |
| 1292 | none | low | UNC finding aid unreachable (no response / ECONNRESET) |
| 1426 | none | low | Historic Pittsburgh CAPTCHA; aggregate of 19 Frick copybook pages |

New single leads suggested by 907 (calendar notes "cyphers undecyphered", none filed yet):
- CSP Dom. 1655 vol. C no. 99, Sept 1655, Sec. Nicholas (Cologne) to Joseph Jane, pp. 325-326.
- CSP Dom. 1656-57 vol. CXXIX no. 64, 22 July 1656, Wm. Grove [Dick Pile] to [T. Ross].
- CSP Dom. 1656-57 vol. CXXIX no. 119, Aug 1656, T. Ross (Paris) to Nicholas, p. 67.

Record errors found:
- 907: the link labelled "CSP Domestic Commonwealth 1655-56" (archive.org cu31924091770440) is the 1656-57 volume; the
  Lamplugh letters to Williamson carry no cipher note, so "Lamplugh" in the title is wrong.
- 1426: dates found are 1890-1898 (19 Nov 1890, 9 Jul 1891, 6 May 1892, 25 Feb 1898, 23 Apr 1898); "Homestead 1892 among
  them" is unconfirmed; the records are Henry Clay Frick Business Records copybook pages.
- 1776: the TNA "missing." note was in the vetting note but not in the status line.
