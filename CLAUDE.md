# cyphersolver

Historical cipher targets, one folder per target with a `NOTES.md`, and a GitHub Pages site in `docs/`.
The layout, the build scripts and the reading conventions are in `README.md` (Repository layout, The website,
Conventions). Read them before touching `docs/`.

## Shared assets

Language models live in `lang/` (`lang/README.md`): a corpus registry, a model registry and one n-gram engine, e.g.
`from lang import lm; lm.load('fr-1600-letters')`. Use one of its models, or add a corpus/model there, rather than
writing a new `<target>/lm.py`. `lm.best_language(text)` is a quick language check on a decrypt.

## A target is finished only when it is written up

Finishing a cipher (read, read in part, explained, found already solved, or attempted and closed from the
evidence) is the first half of the job. The second half is the write-up, and it is done in the same session:

1. Run the `/writeup <folder>` skill (`.claude/skills/writeup/SKILL.md`). It lists every surface a result must
   reach: the `docs/<slug>.html` page, the `PAGES` and `IMAGES` manifest in `docs/_build_site.py`, the README
   results row with its write-up link, the Recent findings line on `docs/index.html`, the `unpublished/solved.html` row (optional while unpublished),
   `SOLVED_CATALOGUE.md`, `SOLVED_RANKING.md`, `TARGETS.md`, `catalogue.json`, `decode_updates/queue.json` (DECODE edits to send), and the rebuild.
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

## Outcome method and priorities

Every profile carries `outcome.method`, George Lasry's categories (`docs/_methods.py`, `docs/glossary.html`): key
recovered from ciphertext-only / from external plaintext / from adjacent plaintext; read after matching with an
external key; read with known key; read from existing decipherment; not solved; not applicable. The site badge, the
README section and the scoreboard follow it. Say what happened ("deciphered with Lasry's key", "key recovered from the
clear passages"); do not use "read" or "solved" alone as an outcome word (`python docs/_check_terms.py <slug>`).
Priorities (TARGETS.md): original ciphertext-only attempts first, external-material matches second.

## Every target keeps a profile.json

The project is being written up with George Lasry as a paper on how LLMs perform against historical ciphers.
The analysis runs on `<folder>/profile.json`, a fixed-field record of the cipher system, the ciphertexts, what
the model was given, the solution steps and the outcome (`profile.schema.json`; the `/profile` skill).

- **Except the famous targets** (the Indus script, Voynich, Beale, Kryptos, Dorabella ...; `FAMOUS` in
  `docs/_check_writeup.py`): they keep no profile.json and never go into the paper data. The checkers and the export skip them.
- On the first session with a target, create its profile with what is known. Write `"unknown"`, never a guess.
- After each move (transcription, hypothesis, solver run, crib, key found, control), append a solution step,
  including the ones that fail. This record cannot be rebuilt accurately afterwards.
- Measure lengths with `python docs/_check_profile.py --measure <file>`; do not copy counts from memory.
- Record whether a reading already existed anywhere and when it was found: that is the contamination question.
- `python docs/_check_profile.py <folder>` must print `result: valid`. `_check_writeup.py` requires it too.

## Working in the shared checkout

- Several sessions share this working tree and switch its branch. Run `git status -sb` before committing; if the
  branch is not the one you mean, commit from your own worktree and push `HEAD:main`.
- Stage by explicit path, never `git add -A`.
- Build from `docs/` with `PYTHONUTF8=1` set; `_build_stats.py` crashes on the cp1252 console without it.
- Write long HTML with the Write tool, not a Bash heredoc.
