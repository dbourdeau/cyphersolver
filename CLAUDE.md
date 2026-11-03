# cyphersolver

Historical cipher targets, one folder per target under `targets/` with a `NOTES.md`, and a GitHub Pages site in `docs/`.
Sweeps and surveys that are not a single target (Gallica sweeps, DECODE harvests, the oldest-cipher search, Schmeh's
Top 50, MysteryTwister) live in `research/`. Skills and checkers take the bare folder name (`/writeup gramont1529`).
The layout, the build scripts and the reading conventions are in `README.md` (Repository layout, The website,
Conventions). Read them before touching `docs/`.

## Shared assets

Language models live in `lang/` (`lang/README.md`): a corpus registry, a model registry and one n-gram engine, e.g.
`from lang import lm; lm.load('fr-1600-letters')`. Use one of its models, or add a corpus/model there, rather than
writing a new `targets/<target>/lm.py`. `lm.best_language(text)` is a quick language check on a decrypt.

## A target is finished only when it is written up

Finishing a cipher (read, read in part, explained, found already solved, or attempted and closed from the
evidence) is the first half of the job. The second half is the write-up, and it is done in the same session:

1. Run the `/writeup <folder>` skill (`.claude/skills/writeup/SKILL.md`). It lists every surface a result must
   reach: the `docs/<slug>.html` page, the `PAGES` and `IMAGES` manifest in `docs/_build_site.py`, the README
   results row with its write-up link, the Recent findings line on `docs/index.html`, the `unpublished/solved.html` row (optional while unpublished),
   `SOLVED_CATALOGUE.md`, `SOLVED_RANKING.md`, `catalogue.json`, `decode_updates/queue.json` (DECODE edits to send), and the rebuild.
2. `python docs/_check_writeup.py <slug>` must print `result: complete` before the work is reported as done.
3. `python docs/_check_writeup.py --audit` lists finished targets that never got a write-up. The SessionStart hook
   shows it at the start of each session; the Stop hook blocks a stop once when a target this session worked on
   reads as finished in its NOTES but has no README row and no page.

DECODE is always updated when the work adds anything, even without a reading. A DECODE target left "attempted,
open" or closed unread still gets its `decode_updates/queue.json` entry in the same session: corrected metadata,
sibling and duplicate records, and any transcription (see the writeup skill, `decode_updates/queue.json` step).

**"Read" means the read bar in README Conventions** (95% of tokens read as sense, measured; no gap untried; every
letter read; only scattered codes or externally blocked pieces open). Record the key state separately.

**"Read in part" is a stopping point only when every unread piece has an outside blocker** (no key material,
too short, illegible, needs physical access). Otherwise keep going: work through the escalation steps in the
writeup skill (section 0a: siblings, clear pages, known keys, print, key rebuild, retry) and aim for a full
reading. The checker and the Stop hook enforce the `## Remaining gaps` and `## Escalation` sections in NOTES.md.

If a target is genuinely not finished, or deliberately not written up (found solved by others with nothing added
here), put `Status: in progress` or `Status: no write-up` in the first forty lines of its `NOTES.md`.

## The catalogue holds vetted leads only

New finds are leads, not catalogue entries. Sweeps write `research/<sweep>/candidates.json`, and
`research/archive_sweep_2026-10/merge.py --write` merges them into `research/leads.json`, never into `catalogue.json`.
`research/COVERAGE.md` lists what is still unswept: check it before choosing a sweep, and remove a row when a sweep closes it.
A lead enters the catalogue only through `python docs/_check_catalogue.py --promote <id>`, which refuses it until its
`vetting` block meets the vetting bar in README Conventions: ciphertext seen, prior art searched in DECODE, Tomokiyo,
Lasry, the edition and the literature, keys held elsewhere ruled out (a key in the same volume is allowed if no decipherment exists; record it in
`vetting.key_in_volume`), duplicates searched, verdict `open`. Never add an entry to
`catalogue.json` by hand or by script around the gate. `python docs/_check_catalogue.py` must print `result: valid`
before a commit that touches `catalogue.json`. The SessionStart audit (section L) lists any entry that fails.

## Outcome method and priorities

Every profile carries `outcome.method`, George Lasry's categories (`docs/_methods.py`, `docs/glossary.html`): key
recovered from ciphertext-only / from external plaintext / from adjacent plaintext; read after matching with an
external key; read with known key; read from existing decipherment; not solved; not applicable. The site badge, the
README section and the scoreboard follow it. Say what happened ("deciphered with Lasry's key", "key recovered from the
clear passages"); do not use "read" or "solved" alone as an outcome word (`python docs/_check_terms.py <slug>`).
Priorities (README Conventions): original ciphertext-only attempts first, external-material matches second.

## Every target keeps a profile.json

The project is being written up with George Lasry as a paper on how LLMs perform against historical ciphers.
The analysis runs on `targets/<folder>/profile.json`, a fixed-field record of the cipher system, the ciphertexts, what
the model was given, the solution steps and the outcome (`profile.schema.json`; the `/profile` skill).

- **Except the famous targets** (the Indus script, Voynich, Beale, Kryptos, Dorabella ...; `FAMOUS` in
  `docs/_check_writeup.py`): they keep no profile.json and never go into the paper data. The checkers and the export skip them.
- On the first session with a target, create its profile with what is known. Write `"unknown"`, never a guess.
- After each move (transcription, hypothesis, solver run, crib, key found, control), append a solution step,
  including the ones that fail. This record cannot be rebuilt accurately afterwards.
- Measure lengths with `python docs/_check_profile.py --measure <file>`; do not copy counts from memory.
- Record whether a reading already existed anywhere and when it was found: that is the contamination question.
- `python docs/_check_profile.py <folder>` must print `result: valid`. `_check_writeup.py` requires it too.

## Archive sweeps blocked by a bot check

When a sweep or a fetch from an archive (Gallica, DECODE, PARES, HathiTrust, a library catalogue ...) hits a bot
check (a 403 to curl/WebFetch, a Cloudflare or "verify you are human" page, a CAPTCHA, an empty JS-only shell), do
not stop the sweep and do not mark the source as unavailable. Switch to Claude in Chrome (`mcp__claude-in-chrome__*`,
the user's real Chrome) and continue the sweep there; read pages with `get_page_text` / `read_page`.

- Try a known script-friendly route first if one exists (e.g. Gallica's `openapi.bnf.fr` IIIF URLs), then Chrome.
- Never solve or click through a CAPTCHA yourself. If Chrome shows one, ask the user to clear it in that tab, then
  carry on.
- Keep the request rate polite (no parallel tab floods); the user's own session is on the line.
- Note in the sweep's notes which source needed Chrome, so the next sweep goes straight there.

## Working in the shared checkout

- Several sessions share this working tree and switch its branch. Run `git status -sb` before committing; if the
  branch is not the one you mean, commit from your own worktree and push `HEAD:main`.
- Stage by explicit path, never `git add -A`.
- Build from `docs/` with `PYTHONUTF8=1` set; `_build_stats.py` crashes on the cp1252 console without it.
- `.github/workflows/rebuild-site.yml` rebuilds `docs/` (catalogue included) on every push to main, every PR opened or
  closed, and daily, and commits the result as github-actions[bot]. Pull before pushing; on a conflict in a generated
  file (`search.json`, `_dates.json`, `*.html`) take main's copy and rebuild.
- main has two rulesets. "no force-push or delete" has no bypass: never force-push main; on a rejected push, pull and
  merge. "require pull request" lets the repo admin and deploy keys push directly; the rebuild pushes with the
  `REBUILD_DEPLOY_KEY` deploy key, because GitHub Actions cannot bypass a ruleset on a personal repo.
- Write long HTML with the Write tool, not a Bash heredoc.
