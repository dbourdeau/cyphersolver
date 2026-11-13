# Vetting brief for a contributor's agent

You are an AI agent working in a checkout of this repository for a contributor. Your job is to **vet leads**: take
ciphered documents that a sweep already found and establish, for each, whether it is a real, unread cipher that
belongs in the catalogue. You do not solve anything. The person running you does not need to know the documents;
everything you need is in this repository. (To find new leads, the brief is [`SWEEP.md`](SWEEP.md).)

The contributor starts you with something like:

> Read `research/VET.md` and follow it. Leads: `<ids>`, or "pick ten that are online", or "pick ten from `<area>`".

## Why vetting exists

`catalogue.json` is the list of open ciphers the site offers to solvers. A lead reaches it only through
`python docs/_check_catalogue.py --promote <id>`, which refuses a lead until its `vetting` block shows that the
ciphertext was seen, earlier decipherments were searched for, keys were recorded and duplicates were excluded (README
Conventions, "Catalogue vetting bar"). The bar is there because unvetted entries kept turning out to be letters
already read, printed by an editor behind the words "cipher undeciphered", readable with a key already held, or
duplicates. Each `open` you write puts a cipher in front of solvers on your word.

## 1. Read first

1. The docstring of [`docs/_check_catalogue.py`](../docs/_check_catalogue.py): the `vetting` block, field by field.
2. [`vetting_2026-11/BRIEF.md`](vetting_2026-11/BRIEF.md), sections "For each lead", "Per-lead work, enforced",
   "Verdict" and "Block format". They are binding. Ignore its worktree path, its `in_NN`/`out_NN` batch files and its
   "do not use the browser" rule: those were for one pass of the project's own sessions.
3. The lead itself: `python research/vet.py --show <id>`, and the README of the sweep it came from (named in its
   `score_note` or `source`; [`README.md`](README.md) indexes them).

## 2. Choose the leads and say so

`python research/vet.py --list` prints every lead with no verdict yet; `--online` leaves out those whose ciphertext
is only in the archive, and `--area <word>` filters on region, shelfmark or title. The "last attempt" line is why
the lead is still waiting: an edition that could not be opened, a portal that blocked, a subscription database, a
leaf not seen. **Prefer the leads whose blocker you or the contributor can lift**: another network, a library
subscription (State Papers Online, Gale, a national licence), a reader's login, a book on the contributor's shelf, a
visit to the reading room. Ask the contributor what they have access to before choosing.

Take ten or fewer at a time. Before starting, tell the contributor the ids, and ask them to open a
[Leads from an archive](https://github.com/dbourdeau/cyphersolver/issues/new?template=lead-sweep.yml) issue listing
them ("Vetting leads 1243, 1255 ..."), so nobody else's agent takes the same ones. Check the open issues first.

## 3. Per lead

Do all four for each lead, with searches run for that document and no text shared between leads.

1. **Duplicates.** `python research/archive_sweep_2026-10/known.py "<shelfmark>" "<correspondent>" "R<decode id>"`.
   A hit that is only the lead's own row is not a duplicate. The DECODE dump is not in the checkout: search DECODE
   yourself (`https://de-crypt.org/decrypt-web/RecordsList`) and say what you ran.
2. **Prior art.** At least three distinct searches: the shelfmark or series with "decipher"; the correspondents with
   "cipher"; the printed edition or calendar. Cover each of DECODE, Tomokiyo's Cryptiana, Lasry (papers and GL.htm),
   the edition or calendar, and the literature (HistoCrypt, Cryptologia). If a printed edition or calendar would
   cover the item, open its text at that item; one you could not open is an unanswered question, and the lead stays
   `unvetted` naming the volume. A contemporary decipherment, printed or between the lines, is prior art.
3. **See the cipher.** Open the leaf at full size and say what is on it: signs, letters or numbers, how many lines
   or pages, and that no decipherment is written on it or filed with it. A description that only says a letter was
   "sent in cipher" does not show that ciphertext survives. For an archive-only item, quote the archive's description.
4. **Keys.** Record any key in the same volume (`key_in_volume`) or held in this repository, on DECODE or in print
   (`key_held`), and whether it was tested. A key never blocks a lead; `key_lookup` is only for a text whose reading
   with that key is already on record.

Never solve or get round a CAPTCHA, a "verify you are human" page or a login wall: ask the contributor to clear it
or to log in with their own account, and do not create accounts. One request every two or three seconds per host.
Page images stay in a scratch directory outside the repository.

## 4. Verdict

| Verdict | When |
|---|---|
| `open` | The ciphertext is real and seen, and three or more searches for this document found no decipherment. |
| `read`, `partly_read` | A decipherment is on the leaf, in print or otherwise on record. `closed` says exactly where. |
| `duplicate` | Same document as a catalogue entry, a lead or a target. `closed` names it. |
| `not_cipher` | Shorthand, a mention of cipher with no ciphertext, or a key with no ciphertext. `closed` gives the evidence. |
| `{"unvetted": "..."}` | You could not establish a verdict honestly. Name the blocker so the next attempt starts there. |

Prefer a true `unvetted` to a weak `open`. Never invent a finding, and never write `read` or `not_cipher` from a
low-resolution glance. A closed lead is as useful as an open one: it stops solvers being sent to a letter that is
already read.

## 5. Write the vetting file

Create `research/vetting_<yyyy-mm-dd>_<contributor's handle>/` with:

| File | Content |
|---|---|
| `vetting.json` | A JSON object `{"<lead id>": block}`, rewritten after every lead. A block has `date` (ISO), `by` (the contributor, then the agent and model), `seen` {`kind`, `where`, `extent`, `cipher`}, `prior_art` {`decode`, `tomokiyo`, `lasry`, `edition`, `literature`}, `key_check`, optional `key_in_volume` / `key_held`, `duplicates`, `searches` [{`query`, `result`}, ...], `verdict`, and `closed` when the verdict is not `open`. If the ciphertext is only in the archive, add `"lead_updates": {"access": "archive"}`. To overturn a verdict a lead already has, add `supersedes` saying what new evidence changes it. |
| `README.md` | First line `# Vetting, <contributor> (<date>)`. Who ran it and with which agent and model; one line per lead (verdict and why); the routes and logins that worked and those that blocked; what is left. |

Then run `python research/vet.py --check research/vetting_<...>/vetting.json` and fix what it reports until it
prints `result: pass`. Never pad a field to pass it: move the lead to `unvetted`.

Write only inside your own folder. Do **not** edit `research/leads.json` or `catalogue.json`, do not run
`_check_catalogue.py --promote` or `--close`, and do not run the site build.

## 6. Hand it over, and what happens then

Tell the contributor, in under 250 words: one line per lead (id, verdict, six words), the count by verdict, what
blocked, what is left. If they ask you to, commit the folder alone on a branch and open a pull request titled
`Vetting: leads <ids>` that mentions their issue.

After review the project applies the file to `research/leads.json`. Each `open` block that passes the gate is
promoted with `python docs/_check_catalogue.py --promote <id>`: the lead becomes a catalogue entry under the same
id and appears on the site's catalogue for anyone to solve, with the block kept on it as the record of who checked
what. Every other verdict closes the lead with its reason. A block the gate refuses is kept on the lead as a note
for the next attempt, and the contributor is told why.
