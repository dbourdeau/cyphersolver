# Beatrice d'Aragona to Eleonora d'Aragona, Pozsony, May–June 1482 (DECODE R1140, R1141)

Status: found already in print (MDE III, 1877, nos. 10 and 12). See RESULT.md for verification limits.

Split on 14 Oct 2026 under the one-key rule (George Lasry, 14 Oct 2026). Catalogue item 160 grouped five DECODE
records by sender. This entry keeps the two 1482 letters (R1140, R1141), in the 1482 alphabet. The others now have
their own folders and pages (each a different cipher, or none, with its own page):
- R1142, Buda, 8 March 1486: [`targets/beatrice1486/`](../beatrice1486/NOTES.md). Its alphabet looks different from the
  1482 one, and the letter says it uses "the old cipher" and encloses a new one;
- R1143, Buda, 2 May 1486: [`targets/beatrice1486b/`](../beatrice1486b/NOTES.md). Two months after the new cipher was
  sent; not shown to share a key with R1142;
- R1154, Naples, 29 May 1505: [`targets/beatrice1505/`](../beatrice1505/NOTES.md). Plain Italian, not a cipher.

RESULT.md (the research report on all five), metadata.json, original_catalogue_entry.json and fetch_decode.py stay
here as shared material; the OCR extracts for R1142, R1143 and R1154 moved to the new folders' `readings/`.

Research begun 20 September 2026 from the user's goal-objective attachment.
No new cryptanalytic reading claimed. The table below preserves the starting DECODE metadata; corrections and primary-source evidence are in RESULT.md.

| Record | Date | From / to | Shelfmark suffix | Pages |
|---|---|---|---|---|
| R1140 | 31 May 1482 | Pozsony / Eleonora | Carteggio Principi Esteri 1623, b. 2/2, 2, 4a | 1 |
| R1141 | 8 June 1482 | Pozsony / Eleonora | Cancelleria 1523 [name says 1623], b. 2/2, 2, 5a | 1 |
| R1142 | 8 March 1486 | Buda / Eleonora | Carteggio Principi Esteri 1623, b. 2/2, 2, 10 | 5 |
| R1143 | 2 May 1486 | Buda / Eleonora | Carteggio Principi Esteri 1623, b. 2/2, 2, 18 | 5 |
| R1154 | 29 May 1504 | Naples / Ippolito | Carteggio Principi Esteri 1623, b. 2/7, 11 | 1 |

The attachment's umbrella shelfmark b. 2/2 and origin Pozsony do not apply to all five.
Metadata recovered from repository research/catalogue_harvest/decode/views*.jsonl.
DECODE images carry an archive-permission requirement for publication; images stay local and ignored.

## Prior work checked before cryptanalysis

- Tomokiyo, Cryptiana index https://cryptiana.web.fc2.com/code/crypto.htm: retrieved; no dedicated Beatrice entry found in the index. This does not establish absence throughout his publications.
- Berzeviczy, *Aragoniai Beatrix ... okiratok* (1914), https://archive.org/details/aragoniaibeatrix00berz, OCR saved as sources/berzeviczy1914.txt. No. LVI, pp. 81 onward, prints the 8 March 1486 letter, with explicit omissions of passages printed in *Matyas korabeli diplomacziai emlekek* III p. 67 and IV p. 367. Need compare to R1142 images before treating this as its decipherment.
- Vestigia public API accessible, but simple search does not search dates and quoted full-name search gave zero results. Search Beatrice returns 418 documents, 5 per page.
- User confirms an existing DECODE cookie is available. Located targets/bordeaux/decode/cookie.txt; use only as request header to de-crypt.org, never reproduce it in notes or logs.

## Completed source identification

See RESULT.md and readings/ for the record-by-record findings and earlier Italian texts. Eighteen images downloaded successfully. R1154 is 29 May 1505 and is plain Italian. R1143 has three written pages photographed five times, including views with slips moved. Four cipher letters have readings in MDE III (1877) and IV (1878); March 1486 editorial markers remain unexplained. Research write-up prepared in `.worktrees/beatrice1482/` on `codex/beatrice1482`. No manuscript images are included in the write-up.
