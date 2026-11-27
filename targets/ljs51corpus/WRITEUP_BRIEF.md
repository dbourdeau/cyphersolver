# Write-up brief: Penn LJS 51 as a whole (28 Nov 2026)

The user (Daniel) asked on 28 Nov 2026: "write up now with the keys we have", and set the goal "complete the analysis
of this manuscript and then use writeup for it to add it to the site". This overrides the earlier hold on publishing.
Follow `.claude/skills/writeup/SKILL.md` and the `/profile` skill (`.claude/skills/profile/SKILL.md`) completely, plus
CLAUDE.md. Everything below is a decision already taken; do not re-open it.

## Where to work

- The shared checkout `C:\Users\dbour\cypher` is about 820 commits behind `origin/main` and full of other sessions'
  uncommitted files. Do NOT build or commit there. Make a worktree from `origin/main`
  (`git fetch origin; git worktree add <scratchpad>\wt-ljs51 -b writeup-ljs51corpus origin/main`), copy
  `targets/ljs51corpus/` (everything except `*.orig`, `keys_fork/` may go too) and `research/ljs51_pass/` into it, add the
  line `output/ljs51/` under a dated comment at the end of `.gitignore`, and do all edits, builds, checks and the
  commit there. Push with `git push origin HEAD:main` (pull/rebase first if rejected; never force). Remove the worktree
  at the end. The master TIFFs stay in `C:\Users\dbour\cypher\output\ljs51\master\` (never committed); crops for the
  site are cut from them.
- Two key-building agents may still be writing into the main checkout's `targets/ljs51corpus/keys_eye/` while you work.
  Before the final build, copy `keys_eye/` again from the main checkout and use what is there; count keys from it.

## Target, slug, framing

- Folder and slug: `ljs51corpus`. Page `docs/ljs51corpus.html`.
- Title: "Ibn al-Durayhim's casebook of solved ciphers, Penn LJS 51 (c. 1330-1361)" (or close; the h1/title must
  share a name with the manifest title).
- What it is: a 14th-century Mamluk secretary's first-person account of about 200 cipher verses and prose pieces
  exchanged with colleagues, each followed (with a few exceptions) by his own decipherment. Text c. 1330-1361 (a cipher
  dated after the death of the patron's brother in Safar 760/1359, f. 62r); copy 15th c. per Penn.
- Compiler: strongly supported as Taj al-Din 'Ali b. Muhammad Ibn al-Durayhim (1312-1361), the cryptologist. Evidence
  checked on the masters in `identity_readings.md` and sourced in `identity_ibn_durayhim.md` and `prior_art_2.md`: f. 102v
  "my book Miftah al-kunuz fi hall al-marmuz, bab al-maqlub"; f. 50r "the laqab of the remote ancestor is al-Durayhim";
  f. 49r "I have written works on it"; the Ajwiba Shamiyya (80v) in Safadi's list of his works; his Miftah's tree script
  (Mrayati Arabic vol. 1 p. 335) is the f. 63v tree script. He never names himself: say "very probably", not "is".
- Patron: 'Ala' al-Din Ibn Fadl Allah (kātib al-sirr, Cairo), from f. 62r and Safadi (sourced). Main correspondent:
  Shihab al-Din Ahmad al-Mutarjim al-Baghdadi (Safadi, al-Wafi 7:94-95, in NOTES).
- One key, one entry: every cipher in the volume has its own alphabet. Present the page as a study of one manuscript
  (one compiler's solved-cipher casebook): the per-cipher keys are listed separately (a key table per chain in a data
  file), no two ciphers are merged into one key, and f. 106v keeps its own existing page `qaysarani1350` (link it in one
  sentence: "the last cipher in the volume has its own page"). Record this decision in NOTES.md.
- Outcome method (George Lasry's categories, docs/_methods.py): the reading of the volume is "read from existing
  decipherment" (the compiler's own solutions on the page); the project's contribution is the master transcription of
  all chains, keys recovered from that adjacent plaintext for the keyed chains (count them from keys_eye at build time),
  the tree-script decoding, the identification, the codicology and the corrections. Choose the method value the checker
  accepts for that (run `python docs/_classify_outcomes.py` and decide from NOTES); state both parts in method_basis and
  contribution.
- Extent: read in part, unless the read bar is met (it is not: 30v.7, 12v.8, 12v.11 and 1r.2 have no plaintext; 12
  chains are answered only in part). `## Remaining gaps` and `## Escalation` in NOTES.md with blockers: 1r.2 illegible
  (plaintext lost to damage; red gloss faint); 12v.8, 12v.11 too-short (40 and 32 signs, single-use alphabets, no
  plaintext); 30v.7 too-short (81 signs, single-use alphabet, no plaintext anywhere in the book, a group-length search over
  all 1,034 passages found none; a test with the neighbouring 30r.4 key may be in keys_eye/30v.7.json: report what it
  says). Escalation steps per the skill (siblings = the whole volume searched; print = Mrayati, Safadi, Penn; key-rebuild =
  the by-eye keys; retry). Set fraction_read with its method and source.

## Facts and sources (the only ones to use)

`targets/ljs51corpus/NOTES.md` (narrative; update its Status/Held lines: Status read in part, remove the "Held" line,
add the one-key decision), `chains_all.json` (211 chain records, corrected), `chains_*.jsonl`, `chains_missed.jsonl`,
`recheck_unanswered.jsonl`, `errata.md/json`, `fixes_log.jsonl`, `keys_eye/*.json` + `keys_eye/REPORT.md`, `solve_48r/REPORT.md`,
`translation_*.md` (eight files), `identity_*.md`, `prior_art_2.md`, `pilot_report.md`, `research/ljs51_pass/` (page pass,
gap checks, `vet_tashifi.md`, `prior_art.md`, `FINAL_LEADS.md`). Every figure on the page comes from these files,
recomputed where possible. Anything not in them is cut or marked "(not checked here)". Readings are model readings
checked on the master TIFFs; no human Arabist has checked them: say so.

## Required surfaces (all per SKILL.md)

- profile.json via the profile skill: documents = the chains or groups of chains (choose a structure the schema allows;
  one document per chain is best if the export accepts it), measured lengths, prior solution = the compiler's own
  decipherments (contemporary, on the page), solution steps in order with dates (page pass 27 Nov; master
  transcription 27-28 Nov; segmenter v1/v2; rekey pilot; by-eye keys; tree script; errata; identity; codicology; blind
  annealing of 48r by another session), outcome texts: full texts (Arabic plaintext per chain from chains_all.json, the
  English from translation_*.md; make per-group text files under `texts/` if the builder needs files), key_file for the
  keyed chains (a JSON or TSV built from keys_eye), validation via docs/_validate.py (validation.tsv from the keyed
  chains' alignments) or --na with the reason; replay per the skill if feasible, otherwise the reason the checker accepts.
  `python docs/_check_profile.py ljs51corpus` must print `result: valid`.
- Page: hero, glance box, numbered sections (the book; the compiler and his circle; the ciphers and their systems:
  substitution alphabets, tashifi look-alike classes, maqlub inversion, numeral and letter-shape alphabets, the tree
  script with its rule; how the keys were rebuilt and checked, red glosses as independent check (count agreement from
  keys_eye); what the texts say, with a few translated pieces; the misbound quires; what remains open; Sources). Figures:
  a cipher snip with its red gloss (e.g. f. 57v image 119 or f. 87r), the f. 63v tree figure with its decoded letters,
  each with data-credit "University of Pennsylvania, Kislak Center, LJS 51 f. NN, via OPenn". Lead image in IMAGES.
- Reveal: docs/reveal/ljs51corpus.json from a keyed chain's alignment (e.g. keys_eye/57v.4.json or 63v.trees.json),
  40-250 tokens, signs as labels, letters as p.
- Key web: docs/keys.json nodes "rebuilt here" for the keys you present (at least the tree script and a representative
  set, or a single node for the volume's keys if the format allows) with "rebuilt from" edges; source_links hub entry.
- Portraits: no trustworthy portrait of Ibn al-Durayhim or 'Ala' al-Din Ibn Fadl Allah is expected: search Commons per the
  skill, and record the skip reason in docs/_explore_skip.json if none.
- README row (section of the chosen method), SOLVED_CATALOGUE.md row, SOLVED_RANKING.md row, docs/findings.html <li>,
  manifest PAGES + IMAGES. catalogue.json: no change (no entry for the volume; 2882 was removed earlier). Do NOT
  promote the open chains to the catalogue (the user reviews leads first); mention them on the page as open.
  decode_updates/queue.json: LJS 51 has no DECODE record; follow the skill for a non-DECODE target (skip with the
  reason, or queue a proposed new record if the tool supports it).
- Build from docs with PYTHONUTF8=1 (_build_stats.py, _build_site.py), then `python docs/_check_writeup.py ljs51corpus`
  until `result: complete`; `python docs/_check_terms.py ljs51corpus`.
- Claims review: launch a separate read-only agent with `.claude/skills/writeup/claims-review.md` on the page; fix
  every error; then `python docs/_check_writeup.py --reviewed ljs51corpus --claims-reviewed`.
- Look at the page in the built-in browser at desktop and 375 px (serve docs/ locally) before committing.
- Commit by explicit paths, subject "Site: write-up for Penn LJS 51, Ibn al-Durayhim's casebook of solved ciphers,
  c. 1330-1361", body listing each surface; end the message with the Co-Authored-By line the session uses. Push to main
  and confirm the page URL after the Pages build.
- Also re-read the existing `docs/qaysarani1350.html` and add one sentence linking the new page (and that the compiler is
  very probably Ibn al-Durayhim), then `--reviewed qaysarani1350`.

Do not send anything to anyone (no emails, issues or PR comments); `outreach_yildirim_aydin_draft.md` stays unsent.
