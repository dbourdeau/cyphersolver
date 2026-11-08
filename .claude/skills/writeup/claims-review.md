# Claims review: have the page checked against its sources before it is recorded

The checkers in `docs/_check_writeup.py` are exact about markup, links, heads and what changed, but they cannot
tell whether a sentence is **true**. The 7 Nov 2026 review of all 559 pages found errors in most of them that no
script could see: a count that does not add up, "Still open" lines that a later NOTES entry had closed, a claim the
sources contradict, background the sources never carried. A second reader, run once per page, finds these.

**When:** before a new write-up is recorded (`--reviewed <slug> --claims-reviewed`, required for a page that has no
record yet), and after any large rewrite of a page's body. After a small change to a finished target's sources, a
careful re-read by you is enough (`--reviewed <slug>`).

**Who:** a separate reviewer, not the session that wrote the page (the writer repeats its own blind spots). Use the
Agent tool with `subagent_type: general-purpose`; if no agent tool is available, re-read the page yourself line by
line with the checklist below and say so in the commit message. The reviewer is **read-only**.

## The reviewer's brief (copy it, fill in `<slug>` and `<folder>`)

> You are checking one published write-up of a historical-cipher site against its source files. Work in the
> checkout at `<path>`. Do not edit anything and do not run any script from a `targets/` folder (some rewrite tracked
> files); you may run `python docs/_check_profile.py --measure <file>` to count lengths. Read `docs/<slug>.html`
> (the prose between the hero and the "Full texts" heading matters most; skip nav, scripts and the long `<pre>`
> transcriptions) and the files in `targets/<folder>/`: `NOTES.md`, `profile.json` (outcome, solution steps, documents,
> credits) and the reading, translation, VERIFICATION and key files. Check:
> 1. **Content**: the summary and every quoted word against the reading and translation; names, dates, shelfmarks,
>    folio numbers, places.
> 2. **Numbers**: every figure on the page (words or signs read, percentages, holes, counts of documents, letters,
>    groups, scores, controls) against `profile.json`, `NOTES.md` and the reading files. Recompute every sum and
>    percentage yourself before you report a mismatch. Flag two different numbers for one quantity on the same page.
> 3. **Method**: how the page says the key was found against the profile's solution steps and `outcome.method_basis`.
>    Flag overclaims ("no crib", "no outside key", "complete") that a step contradicts.
> 4. **Credits**: who is credited for key, transcription and reading against the profile credits and the
>    contributor's own notes.
> 5. **Leftovers**: text that belongs to another letter or page, or rows of a glance box left from records since split
>    off to other pages.
> 6. **Stale text**: statements a later dated entry in `NOTES.md` has superseded ("not yet", "no key", "not
>    transcribed", a Still open line that was closed), and one name spelled two ways where the sources use one.
> 7. **Unsupported claims**: history, identifications and attributions stated as certain that the sources do not
>    carry, or that they say are unchecked or from memory.
>
> Report only what you can back with a quote from the page **and** a quote or file:line from a source. Ignore pure
> style, and badge or chip wording that comes straight from `profile.json` (`outcome.method`, `outcome.class`).
> Answer with a list: for each finding the severity (error, likely, nit), the exact page text, what the source
> says and where, and the corrected wording. Name the pages and files you could not check (no images are available).

## After the review: decide and fix, do not leave a list

Apply every error and likely finding yourself, choosing the wording the sources support:

- Sources disagree with each other: say what each says, or follow the latest dated NOTES entry and name the other.
- A claim is unsupported but not contradicted: cut it, or end the sentence with "(This background is not from the
  sources and was not checked here.)".
- Text is stale: rewrite it from the latest NOTES entry.
- A count can be recomputed from a file: recompute it and use that number.
- Never invent a fact, and never credit a person from git authorship alone.
- A badge, title, cite line or Full-texts summary that is wrong is generated: fix it where it is generated
  (`docs/_build_site.py`, `profile.json` text, `docs/_portraits.json`, the target's reading files), or the next
  build undoes the fix.

Then rebuild, run `python docs/_check_writeup.py <slug>`, and record the review:

```
python docs/_check_writeup.py --reviewed <slug> --claims-reviewed
```
