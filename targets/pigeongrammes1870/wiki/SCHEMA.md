# Wiki schema: pigeongrammes 1870-71 (inspectors' code and Favre/delegation code)

This wiki follows the LLM-wiki pattern in Karpathy's gist (https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f, read 7 Nov 2026): instead of re-deriving answers from raw documents each time,
the model builds and maintains a persistent, interlinked markdown wiki, "a persistent, compounding artifact". Three layers (raw sources / the wiki / this schema), three operations (**ingest**, **query**, **lint**),
an `index.md` catalogue (every page, a link, a one-line summary, by category, read first) and an append-only `log.md` with parseable prefixes (`## [YYYY-MM-DD] kind | subject`; `grep "^## \[" log.md | tail -5`).
Added here: a fourth operation, **loop** (the hypothesis-testing engine, `tools/engine.py`), and a machine-readable lexicon, because this wiki has to drive computation as well as be read.
The wiki is the memory of the project: nothing the work learns lives only in a chat or a script output. It is a git repo of markdown (it lives in this repository).

## Layers
1. **Raw sources** (never edited): Pillon's files (`C:/Users/dbour/pigeon_dl/`, third-party, unpublished), the books' OCR (`C:/Users/dbour/enquete/`, `pigeon_src/`), the repo's plain copies (`inspecteurs_2nov_partial.txt`,
   `chaudordy_nums.json`, `chaudordy_18dec_plain.txt`). The wiki holds a **source page** for each (`sources/S..`): where it is, what it is, how reliable, how to read it.
2. **The wiki** (`wiki/`): markdown pages with front matter, linked by `[[ID]]`. Types: `source` (S), `entity` (E), `system` (Y), `claim` (C), `question` (Q), `test` (T), `synthesis` (Z: overview, filed answers and analyses). Plus machine state:
   `lexicon_inspectors.json`, `lexicon_favre.json` (group -> reading, status, claims).
3. **Schema**: this file and `PROCESS.md` (how knowledge is gained).

## Front matter (YAML-lite, one `key: value` per line; lists as `[a, b]`)
- all pages: `id`, `type`, `title`, `updated`
- claims: `status`, `confidence` (0-1), `evidence` (ids of sources/tests/claims), `depends` (claim ids), `refuted_by` (for rejected)
- questions: `status: open|answered`, `answer` when answered
- tests: `script` (path) when one exists

## Status ladder for claims
- `established`: confirmed by an independent source (a printed heading, a document, another party) AND >= 2 evidence ids. Only a human or an external document sets it; the engine never does.
- `supported`: passes the gate (see PROCESS.md): position fit, context gain, null calibration, split-half replication where possible; or a documented blind check. The engine may set it (`auto: true` in the lexicon).
- `hypothesis`: a stated idea with some evidence, not yet passing the gate.
- `open`: neither supported nor refuted.
- `rejected`: refuted (needs `refuted_by`), or withdrawn by its author.
A claim never goes up the ladder without a new test page or source page being cited. Contradictions found are logged and the lower-confidence claim is demoted.

## Rules
- Every number quoted in a page comes from a test page or a source page; cite it (`[[T05]]`).
- Say what happened ('fits within 0.02', 'rank 30 of 30k'); do not write 'solved' or 'read' alone.
- Third-party material (Pillon's files, his emails) is not published or sent anywhere without his agreement (`[[Q07]]`).
- Names and readings that came from a guess, not a test, are `hypothesis`, whatever their plausibility.
- Pages are short; one claim per page; link instead of repeating.

## Operations
- **ingest**: read a raw source -> write/update its source page -> update the entity/system/claim pages it touches -> `tools/build_index.py` -> append to `log.md`.
- **query**: read `index.md`, then the relevant pages; answer from the wiki with citations; file a good answer or analysis back as a synthesis page (Z) so explorations compound; if the answer needs a new test, add a question page.
- **lint**: `python tools/lint.py` checks front matter, link targets, evidence for supported/established claims, refuted_by on rejected ones, lexicon consistency, index freshness, **contradictions** (a supported claim depending on a rejected one),
  **stale claims** (supported claims depending on a hypothesis), orphan pages and **data gaps** (hypotheses and open questions with no test page), and prints suggested new questions. Must print `result: clean` before a loop starts and after it ends.
- **loop**: `python tools/engine.py` (PROCESS.md). Reads the lexicon and claims, proposes and tests readings, writes accepted/rejected claims, updates lexicon, index and log.
