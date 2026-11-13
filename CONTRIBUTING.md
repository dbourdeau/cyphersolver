# Contributing

This repository is a shared ledger of historical ciphers: what has been deciphered, by whom, and how. The site is
<https://dbourdeau.github.io/cyphersolver/>; the page for contributors is
[contribute.html](https://dbourdeau.github.io/cyphersolver/contribute.html), and everyone credited so far is on
[contributors.html](https://dbourdeau.github.io/cyphersolver/contributors.html).

## Six kinds of contribution

| Kind | What to send | Issue form |
|---|---|---|
| A solution to a cipher in the ledger | target, documents covered, key, decipherment against the ciphertext, how the key was obtained, prior publication | [Solution](https://github.com/dbourdeau/cyphersolver/issues/new?template=solution.yml) |
| A fuller reading of a partial one | the write-up and the gap (from its NOTES.md `## Remaining gaps` or [contributors.html#further](https://dbourdeau.github.io/cyphersolver/contributors.html#further)), the value or reading you propose, the evidence for it | [Fuller reading](https://github.com/dbourdeau/cyphersolver/issues/new?template=further-reading.yml) |
| A new unsolved cipher | archive, shelfmark, folio, image link, date and correspondents if known, what you know of its status | [New cipher](https://github.com/dbourdeau/cyphersolver/issues/new?template=new-cipher.yml) |
| A new cipher with its solution | both of the above; say whether an unpublished result may be shown in full | [New cipher with solution](https://github.com/dbourdeau/cyphersolver/issues/new?template=new-cipher-solved.yml) |
| Leads from a search of an archive | what you searched and how, each ciphered item found (shelfmark, link, what is on the leaf), what you checked for an earlier decipherment; an empty search counts | [Leads from an archive](https://github.com/dbourdeau/cyphersolver/issues/new?template=lead-sweep.yml) |
| A verification of a reading here | the passage and images you worked from, where your reading agrees and where it does not | [Verification](https://github.com/dbourdeau/cyphersolver/issues/new?template=verification.yml) |

**Full texts.** A contribution that claims a document is read, in full or in part, has to include the complete
transcription and the complete decryption of every such document, and the key if you recovered, extended or
corrected it. They are shown on the write-up (inline, or linked when long), so that historians can use the text and
earlier contributors can judge the new reading. Please add a short summary of what each document says and its
historical context. A reading sent without its texts is recorded as a pointer until they arrive. (George Lasry,
October 2026.)

**A reading must read, in any language.** A mechanical decryption is not a reading. Before a contribution with a
reading is accepted, it must show for each document (George Lasry, 22 Oct 2026):

1. **The plaintext as coherent sentences** in the document's own language (French, Italian, Spanish, Latin, German,
   Dutch, Hungarian, English ...): word division, punctuation and resolved code groups, with every hole marked in
   place (`[...]`, `[?word]`, `[47]` for an unidentified code). A few holes are fine; holes in almost every sentence
   are not, and mean the transcription or the key needs another pass against the images.
2. **An English translation** of those sentences, with the same holes. Not needed if the plaintext is English.
3. The decryption itself, line by line against the transcription, so the reading can be checked.

A document counts as read only when 95% of its words read as sense (the README read bar); one that builds coherent
sentences under that is marked "read in part". A document that decodes but does not yet build sentences can still be
sent, marked "decoded, not read": it is shown
for others to improve, and is not counted as read. Key sheets, code lists and worksheets are marked "not prose".
`python docs/_check_reading.py <folder>` measures the share of sentences without holes and shows the weak ones; please
run it before opening the pull request. Before merging, a reviewer reads the text as sentences against its translation
and records it on each document (`reading_review` in `profile.json`); the write-up checker refuses a reading without it.

**From a key to a reading: iterate (George Lasry, 24 Oct 2026).** A key can be mostly recovered while the text is not
yet read, which is a legitimate state to submit. Recording it that way is fine: say how the key was obtained, and mark
the documents "decoded, not read". To go further, take the decryption from a good starting key and let a language model
complete the missing nomenclator entries from context and split the decryption into readable text in the document's
language. Then look at where the result stops making sense: those places often reveal an error in the transcription or
in the key. Check them against the images, correct the labels or the key, decrypt again and repeat until the
sentences hold. Mark every value the model proposed from context alone as doubtful (`[?word]`) until it holds at every
occurrence or a contemporary text confirms it. Record each round, failures included, as a solution step.

## Scanning an archive for leads

Every catalogue entry started as a lead: a ciphered document noticed in an archive that nobody seems to have read.
Finding them needs no cryptanalysis, and you do not have to solve what you find.

1. **Pick a place.** An archive you know is best. Otherwise [research/COVERAGE.md](research/COVERAGE.md) lists what
   is not searched yet: never searched, tried and blocked (often only for scripts: a browser or a reader's login gets
   through), and searched by catalogue only, where the ciphers can be found only by paging through the volumes.
   [research/README.md](research/README.md) indexes every search made so far, by area.
2. **Say what you are taking**, by opening the [Leads from an archive](https://github.com/dbourdeau/cyphersolver/issues/new?template=lead-sweep.yml)
   form with the archive or series named, so two people do not search the same one.
3. **Check each find against the ledger.** `python research/archive_sweep_2026-10/known.py "<shelfmark or name>"`
   searches the catalogue, the leads, the notes and the DECODE list. Without a checkout, search the
   [catalogue](https://dbourdeau.github.io/cyphersolver/catalogue.html) and send it anyway; duplicates are caught at merge.
4. **Send the finds and the empty searches** on the form: for each item the shelfmark and a link, date and
   correspondents, what the archive says of the cipher, whether you saw the ciphertext and what is on the leaf, what
   you checked for an earlier decipherment (DECODE, Cryptiana, the edition), and how it can be seen. What counts and
   what to leave out is in [the sweep brief](research/archive_sweep_2026-10/BRIEF.md), "What counts".

By pull request, a sweep is one folder `research/sweep_<yyyy-mm-dd>_<archive>/` with a `README.md` (what was searched,
found, blocked and left) and a `candidates.json` in the brief's row schema (`[]` is a valid result). Leave
`research/leads.json` and `catalogue.json` alone: the merge and the promotion are run after review, and a lead enters
the catalogue only when it meets the vetting bar (README Conventions). A lead keeps its finder's name, and the write-up
of a cipher that came from it credits the finder with the role `new cipher`.

Not on GitHub? Email <picture><source media="(prefers-color-scheme: dark)" srcset="docs/email-dark.png"><img src="docs/email.png" alt="email address (see image)" height="22"></picture> with the same details. The entry is made for you and credited the same way.

## Pull requests

A pull request is welcome for any of the above. The layout is in [README.md](README.md) (Repository layout,
Conventions). In short:

- One folder per target under `targets/<folder>/`, with a `NOTES.md` (what the document is, the system, the key, the
  reading, what is open and why) and the files the work used: transcription, key, decipherment, scripts. List the
  transcription and decryption file of every document, and the key file, in `profile.json` `outcome.texts` /
  `outcome.key_file` (see `docs/_texts.py`); the site shows them in a "Full texts" section.
- Large images stay out of git; link them (Gallica, DECODE, the archive's viewer) or describe where they are.
- Leave the generated files alone (`docs/*.html` built by `docs/_build_site.py`, `docs/search.json`,
  `docs/pages.json`, `docs/writeups.html`). They are rebuilt when the contribution is merged.
- Say in the description how you want to be credited (full name, initials or a handle, and a link if you like).

## How credit is recorded

Each target's `profile.json` carries `outcome.credits`: who contributed and in what role (solution, new cipher, new
cipher with solution, verification, key or decipherment used, prior solution, key corrected, transcription,
identification, pointer). The ids are in [contributors.json](contributors.json). `outcome.provenance` says whose result
it is: `project`, `contributed` or `mixed`. The write-up's credits line, the contributors page and the front page's
top contributors are all built from these fields. `docs/_check_profile.py` checks them.

Results contributed from outside are marked as such and are kept out of the figures for the study of how language
models perform against historical ciphers (`docs/_export_profiles.py` leaves out `contributed`, flags `mixed`).

## Tools

Use any tools you like, AI included. Say what you used, and check the reading against the images before sending it.
