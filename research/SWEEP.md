# Sweep brief for a contributor's agent

You are an AI agent working in a checkout of this repository for a contributor. Your job is one **sweep**: search one
archive, portal or series for enciphered documents that nobody has read and that the project does not have yet, and
write down what you find and what you searched. You do not solve anything. The person running you does not need to
know the archive; everything you need is in this repository.

The contributor starts you with something like:

> Read `research/SWEEP.md` and follow it. Sweep: `<an archive, a portal, a series>`, or "pick one from the coverage list".

## 1. Read what has been searched

Read these before any request to an archive:

1. [`COVERAGE.md`](COVERAGE.md): what is not swept yet (never swept; tried and blocked; reachable but not looked at;
   started and not finished; swept at catalogue level only).
2. [`README.md`](README.md): the index of every sweep so far, by area. Open the `README.md` of each earlier sweep of
   your archive or area: the search terms already run, the routes that worked, the hosts that blocked, what was left.
   Do not repeat a search that is recorded there; continue it.
3. [`archive_sweep_2026-10/BRIEF.md`](archive_sweep_2026-10/BRIEF.md): what counts as a lead, what to leave out, and
   the row schema of `candidates.json`. It is binding; this file only adds to it.
4. The docstring of [`docs/_check_catalogue.py`](../docs/_check_catalogue.py) and
   [`vetting_2026-11/BRIEF.md`](vetting_2026-11/BRIEF.md): the `vetting` block, if you go that far (section 5).

## 2. Choose the sweep and say so

If the contributor named an archive, take it. If not, choose from `COVERAGE.md` and prefer, in this order:

- a row under "Tried and blocked" whose block was a network or a script block: you are on another network, so try it
  again first, and record the result either way;
- a volume or series "swept at catalogue level" whose images are online: page through it leaf by leaf. A catalogue
  that does not mention cipher hides its ciphers from every term search, so paging finds what searching cannot;
- a row under "Never swept" or "Not looked at, though reachable".

Before starting, tell the contributor in one sentence which archive or series you are taking, and ask them to open a
[Leads from an archive](https://github.com/dbourdeau/cyphersolver/issues/new?template=lead-sweep.yml) issue naming it,
so that nobody else's agent takes the same one. Check the open issues with that form for a claim on yours.

## 3. Search

- Catalogue and portal search in the archive's own language (cifra, cifrado, en chiffre, chiffré, Chiffre,
  chiffriert, Geheimschrift, in zifra, cijfer, chiffer, szyfr, шифр ...), then the finding aids, then the images.
- **Look at the leaf.** A catalogue line is not a find until you have opened the page image and seen ciphertext on
  it, unless no image is online (then quote the archive's description and mark it `needs_archive_scan: "yes"`). Say
  what you saw: signs, letters or numbers, how many lines, and whether a decipherment is written on it.
- **A glossed cipher is read, not a lead.** Plaintext between the lines, in the margin or over the groups means it
  was deciphered at the time. Only bare ciphertext with no decipherment on it or filed with it is a lead. Open the
  leaf at full size before calling it bare. A bare key or table with no ciphertext goes in `key_leads.json`.
- **Duplicates.** Run `python research/archive_sweep_2026-10/known.py "<shelfmark>" "<correspondent>"` on every
  candidate. The DECODE dump is not in the checkout, so also search DECODE yourself
  (`https://de-crypt.org/decrypt-web/RecordsList`) and give the R-number if the item is there.
- **Prior art.** For every row, search for a published decipherment: Tomokiyo's Cryptiana (`unsolved.htm` in the
  repository root is a snapshot of his list), George Lasry's papers, the HistoCrypt proceedings, and the printed
  edition or calendar of that correspondence (often on archive.org as full text). Write what you ran and what it
  showed. "Cipher undeciphered" in an old calendar usually means the editor deciphered it and printed the text.
- **Bot checks.** Never solve or get round a CAPTCHA, a "verify you are human" page or a login wall. Ask the
  contributor to clear it in their own browser, or to log in if they hold a reader's account; if they cannot, record
  the host as blocked and move on.
- **Rate.** One request every two or three seconds per host, no parallel floods; stop on a host at its first 429 or
  403 and note it. The contributor's own network and accounts are on the line.
- Never invent a shelfmark, a link or a finding. A row must be a real, citable item with a record link.

## 4. Write the sweep folder

Create `research/sweep_<yyyy-mm-dd>_<archive or area>/` (today's date, lower case, underscores) with:

| File | Content |
|---|---|
| `README.md` | First line `# <Archive> sweep (<date>)`. Then: who ran it and with which agent and model; the routes and endpoints that worked and those that blocked, from this network; every search term with its hit count; the volumes paged through, with image ranges; the finds, best first; what was excluded and why; **what is left**. A sweep that finds nothing still writes all of this. |
| `candidates.json` | A JSON list, one row per lead, with exactly the fields of the BRIEF schema. `[]` is a valid result. Rewrite it after every find so nothing is lost. |
| `key_leads.json` | Optional: bare keys and cipher tables seen on the way. |
| your scripts | Whatever you wrote to harvest, so the sweep can be re-run. |

Page images and downloads never go in the repository (copyright, size): keep them in a scratch directory outside it.

Write only inside your own folder. Do **not** edit `research/leads.json`, `catalogue.json`, `COVERAGE.md`, `README.md`
files outside your folder, `archive_sweep_2026-10/` or anything in `docs/`, and do not run the site build: the merge
into the leads, the coverage update and the index are done after review.

## 5. Vet, if you can

A lead enters the catalogue only when its `vetting` block is complete (README Conventions, "Catalogue vetting bar").
If you saw the ciphertext and ran the prior-art searches for a row, add the block to that row, with `by` naming the
contributor and the agent, and at least three searches actually run for that document listed in it. If an edition
that would cover the item could not be opened, leave the block out and name the volume in `verify`. No block is
better than a weak `open`. Vetting leads that an earlier sweep left unvetted is a job of its own: [`VET.md`](VET.md).

## 6. Hand it over

Tell the contributor, in under 250 words: the folder written, the number of rows and how many carry a complete
vetting block, the three best finds with their shelfmarks, the routes that worked and those that blocked, and what
is left. Then, if they ask you to, commit the folder alone on a branch and open a pull request titled
`Sweep: <archive> (<n> leads)`; its description repeats that summary and says how the contributor wants to be
credited. Without a pull request, the same summary and the rows can be pasted into the issue opened in section 2.
