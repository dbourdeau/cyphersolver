# Lambeth Palace Library sweep (13 Nov 2026)

The first sweep run from `research/SWEEP.md`: a test of that brief by a project session (13 Nov 2026, cloud container),
with a fresh agent (Claude Code, model claude-fable-5-2) standing in for an outside contributor who was not at the keyboard,
so no login, no browser check cleared and no claim issue opened. A small sweep: one portal, nine new search terms, 14 records
opened, about 10 minutes of requests after the reading. Not merged into `research/leads.json` yet.

Reviewer's note: MS 615 p. 522 and MS 624 pp. 224, 233 are excluded below because the Carew Calendar prints their key. The
brief was clarified after this run: a printed key alone does not close a lead, a printed text does. Whether the calendar
prints the text of these three was not checked, so they are worth a second look.

Result: **1 candidate row** (catalogue level, leaf not seen, no vetting block), 0 key leads.

## Why this archive

`COVERAGE.md` lists "TCD, Lambeth" under "Tried and blocked" (security check, 403), and `_nov13/BRIEF.md` lists Lambeth as
blocked from the cloud network. Two earlier sweeps had in fact opened it: `sweep_2026-11_uk_ireland` ran "cipher" (27 records)
and `sweep_2026-11_uk_retest` ran "cypher" (10 records). This sweep continues them with the terms they did not run.

Claim check: the open issues of dbourdeau/cyphersolver were listed through the REST API on 13 Nov 2026; none is a "Leads from
an archive" claim on Lambeth. The contributor was not available, so no issue was opened. What I would have said: "I am taking
the Lambeth Palace Library catalogue (CalmView), the search terms after cipher and cypher; please open a Leads from an archive
issue naming it."

## Routes, from this network

| Route | Result |
|---|---|
| `https://archives.lambethpalacelibrary.org.uk/CalmView/advanced.aspx?src=CalmView.Catalog` | **200 to curl** with a browser User-Agent and a cookie jar. GET the form, POST it back with the hidden fields and the term in the "Any Text" box; the answer redirects to `Overview.aspx?src=CalmView.Catalog&r=((((text)='<term>')))`. A term with no hit returns the form again. `calm_search.py` |
| `.../CalmView/Record.aspx?src=CalmView.Catalog&id=<id>` | 200 to curl. `calm_record.py` |
| DECODE `https://de-crypt.org/decrypt-web/RecordsList?cmd=search&search=<term>&searchtype=` | 200 to Python urllib with a browser User-Agent (`../sweep_2026-11-11_german/decode_search.py`; "Dresden" gives 10 pages, so the 0s below are real). A first try with plain curl and only `cmd=search&search=` returned a 106 kB page from which I parsed nothing; I did not find out whether the missing `searchtype=` or my parsing was the cause |
| `archive.org` advancedsearch and `_djvu.txt` download | 200 |
| Page images | None online for Lambeth manuscripts; nothing was downloaded |

No 403, 429 or bot check was met. One request every 3 s; 33 requests to Lambeth in all.

Not tried here: the other hosts probed once while choosing (13 Nov 2026, one GET each): `archives.library.wales` 403,
`manuscripts.nls.uk` 403, `manuscripta.at` 403, `catalogue.nli.ie` 403, `opac.kbr.be` and `belgica.kbr.be` no connection,
`diglib.hab.de` 200, `www.e-manuscripta.ch` 200 (home page only).

## Search terms and hit counts (CalmView "Any Text")

| Term | Records | What they are |
|---|---|---|
| cyphers | 1 | MS 646 (letters to Charles II; already left out by `uk_retest`: Charles II's own decipherings) |
| ciphers | 4 | Carew MSS 597 pp. 109a, 199, 228 (Pelham 1579-80: letters that mention sending ciphers); MS 604 p. 161 (Carew to Cecil 1601). Calendar extracts in clear; already tracked (`uk_ireland`) |
| decipher | 9 | Noise: 1930s minutes "hard to decipher", a court roll, ECE case files, a portrait label |
| deciphered | 10 | Carew MS 597 p. 102a and MS 621 p. 143 (the word used in the clear text); MS 615 pp. 512, 520, 560/567, 561, 586 (Mountjoy and the Privy Council to Carew, 1602: cipher "deciphered by Carew", "between the lines" or "on a separate sheet"); MS 690 (Tillotson's shorthand, deciphered by Philip Gibbs, printed by Birch 1753); MS 705 f. 37 (Proby 1592, news "when deciphered", no ciphertext). Nine opened; the fonds-level record MSS 694-710 was not |
| undeciphered | 4 | MS 615 p. 522; MS 624 pp. 224, 233; MS 3597 (illegible words, not cipher). All four opened |
| decyphered | 2 | MS 930 (Blencowe, already in `uk_retest`); **MS 3473** (the row) |
| cifra | 1 | MS 646 again |
| chiffre | 0 | |
| cryptogram | 0 | |

"cipher" and "cypher" were not re-run. The result lists were short enough to need no paging; the pager code in
`calm_search.py` was therefore never exercised and is untested.

## Find

1. **Lambeth MS 3473 f. 97** (Fairhurst Papers): letters of the Sieur de Joli, minister at Montauban, to Monsieur de
   Valançay and others, December 1623, on Soubise and Rohan, and a letter to his brother in Milan; "French copies partly
   decyphered". Catalogue description only; the leaf was not seen and there is no image online. It is a weak row: the copies
   may hold no ciphertext at all. No edition was searched, so it carries no `vetting` block.

## Excluded, and why

- **MS 615 p. 522**, Mountjoy to Carew, Athlone, 10 Dec 1602 ("A few words in cipher, undeciphered", Calendar of the Carew
  MSS IV no. 351). Not a lead: the Calendar's own footnote to this letter (vol. IV, pp. 386-387, archive.org
  `calendarofcarewm04lamb`, OCR text read 13 Nov 2026) gives the key: "The cipher used in these letters is very simple. The
  letter g is used for a, h for b, and so on, i and j being treated as one letter, as also u and v." "Undeciphered" there
  means no decipherment is written on the letter. A key lookup on a few words, and the leaf is not online.
- **MS 624 p. 224** (Carew to Mountjoy, 9 Oct 1602) and **p. 233** (25 Oct 1602): "The words in italics are in cipher,
  undeciphered" and "Roger Harvy [In cipher, undeciphered]". The editors print the words, so they read them; the same
  shift cipher.
- **MS 3597**: "next six words undeciphered" is an illegible Latin line in a 15th-century devotional book, not cipher.
- **MS 615 pp. 512, 520, 560/567, 561, 586** (1602): deciphered at the time by Carew; the record for p. 520 quotes the same key
  note, and p. 561 says "The cipher is the same simple one as that used in Mountjoy's letters to Carew".
- **MS 690**: Tillotson's shorthand (shorthand is out of scope), deciphered and printed in Birch 1753.
- MS 646, MS 930: already judged by `sweep_2026-11_uk_retest` (deciphered at the time).
- The "decipher" hits: handwriting that is hard to read.

## Duplicate and prior-art checks actually run

- `python research/archive_sweep_2026-10/known.py "MS 615" "MS 3473" "Mountjoy" "Joli" "Valançay"`: no hit for MS 3473,
  Joli, Valançay; "Mountjoy" only in `sweep_2026-11_uk_ireland/README.md`. "MS 615" returned twelve false hits on
  "Add MS 6157x" (substring match), so it showed nothing about Lambeth MS 615.
- DECODE keyword search: Lambeth 0, Mountjoy 0, Carew 0, Montauban 0.
- `unsolved.htm` (Tomokiyo snapshot): no "Mountjoy", "Carew" or "Montauban".
- Calendar of the Carew Manuscripts vol. IV (1601-1603), archive.org full text: read for the three 1602 letters.
- Not run: Lasry's papers, HistoCrypt, any edition of the Rohan/Soubise correspondence for MS 3473.

## What is left

- The fonds-level record MSS 694-710 (Shrewsbury Papers, hit for "deciphered") was not opened.
- Terms not run at Lambeth: "in code", "code", "characters", "secret writing", "figures", "ziffer", "cyfer", "cypher'd",
  old spellings ("cifer", "cypherd", "sypher"), and "key" with "alphabet".
- CalmView matches whole words in description text. The big letter series (Bacon MSS 647-662, Shrewsbury and Talbot MSS
  694-710 and 3192-3206, Gibson, Fairhurst MSS 3470-3533, Carew 596-638) are catalogued letter by letter but a cipher is only
  found if the cataloguer said so. None has free images online (Bacon papers are in a subscription product, per `uk_retest`),
  so paging is not possible from outside.
- MS 3473 f. 97 needs a look at the leaf or the microfilm, and an edition search, before it is worth anything.
- `COVERAGE.md` still lists Lambeth as blocked; after three sweeps that opened it the row could go (not edited here, as the
  brief says).

## Files

- `candidates.json`: 1 row.
- `calm_search.py <outdir> term ...`: the term searches. `calm_record.py <outdir> <record id> ...`: record pages, cut to
  the cipher context. Both write their downloads to a directory outside the repository.
