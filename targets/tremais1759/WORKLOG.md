# tremais1759 work log (catalogue 1392)

## 23 Nov 2026 (Claude Fable 5.2 session)

- Entry 1392: Trémais to the minister, Montréal 6 Nov 1759, ANOM COL C11A 104 ff.346-347v, LAC images e000875270-272
  (`https://data2.archives.ca/e/e036/e0008752NN.jpg`, 624 or 1125 px wide, no larger rendition: `-v8`, `.tif`, `op=img` without `app` all
  give the same file or 404). September letter ff.342-343v = e000875266-268 (left page); clear copy ff.344-345 = e000875268 (right) - 269.
- Prior work: Brice Dudout (PR 273, 5 Nov) found the Sept pair and tested a partial key; issue 810 (emgeorrk, 19 Nov, Codex-assisted)
  filed a partial decipherment of November: 1,327 groups transcribed, 188-entry working key, 49 strong passages. Saved in `prior/`.
  No reply from the author to our comment of 19 Nov as of 23 Nov; the entry was not asked to be held.
- Known keys tested and rejected: C11E 10 numerical sheets e001295272 (98 rivière, 108 tion, 115 guerre) and e001295276 (Montcalm 1758:
  98 comme, 108 quoique, 115 eau) against Trémais 98 il, 108 r, 115 M. Bigot. Sheet 274 (Vaudreuil) was rejected earlier (0.063).
  No key file in the repo matches (script over 1,294 key files, 22 Trémais pairs, none with 2 hits).
- Print: Antoine Roy, "Dossier ... Trémais", RAPQ 1959-60 (BAnQ numérique 2276324, pdf text read pp. 7-26): prints Marine C 246 pieces,
  the instruction of 3 Feb 1759 ("On lui remet ci-joint un chiffre particulier à lui pour sa correspondance dont il ne fera usage
  que pour les choses secrettes"), no letter of 6 Nov 1759, no table. Web searches for a printed reading: nothing.
- Better images: ANOM IIIF (`recherche-anom.culture.gouv.fr/iiif/MINISTERES/SEM/C14/...` works for C14) has no C11A volume under 50 path
  variants tried; the Canada inventory FRANOM_00013 flags digital objects only for the Île Royale maps. Héritage has the C11A
  transcript reels (C-2374..C-2412), not the F-reels of the originals. HD scans must be ordered (ANOM or LAC reel F-104).
- Finding: in the September letter Trémais wrote BOTH homophones of most units, stacked (497 over 119 = p) or dashed (12-437 = de).
  The pair therefore gives homophone classes as well as values.
- Clear copy read in full: `sept_clear_copy.txt`.
- Agent 1 (Sept alignment): `sept_cipher_aligned.tsv` (709 slots, 564 cipher), `sept_key_from_pair.tsv` (168 numbers; 87 high).
  Conflicts: 437 (de and ta), 89 (au / qui), 176 and 274 (tu). Estimated 15-20% of key numbers with a digit error.
- Agent 2 (Nov transcription): `nov_transcription_v2.tsv` (1,350 groups: 346r 248, 346v 457, 347r 535, 347v 37, margins 73),
  `nov_transcription_diff.tsv`. Two independent readings (agent first pass vs issue 810) agree exactly on 737 of 1,279 main-text
  numbers (58%); 279 undecidable on the image. 40 of 53 lines of f.346v lose their end in the gutter.
- `decode_nov.py` + Sept key + `key_overrides.tsv`: 1,131 of 1,350 groups get a value (0.838); with `key_nov_extension.tsv` more.
  Sense appears in long runs (e.g. f.346v: "conviendra par exemple que l'intendant ne peut être ...", "c'est sur ses ordres que
  toute sorte des ... qui y sont établis et que les vivres sont fournis aux détachements", "n'est certainement point l'intendant
  qui en donne l'idée", "où la vie est d'une cherté dont aucune province de France n'a jamais eu d'idée. Il faut donc que le
  traitement des troupes ... étoit dans le même rapport; mais la soif des gains s'étoit tellement emparée des esprits").
- Next: line-by-line reading (`reading.md`), key extension with evidence, word count against the read bar, NOTES, profile, write-up.
- Reading pass done the same day: `reading.md` (256 sure cipher words, 83 conjectural, 69 unread runs; estimate 0.58 sure of
  about 440 cipher words). Key extension in `key_nov_extension.tsv`. Finds from the sense: 437 = dé (637 is a misread), 205 = fa
  and 305 = ci, 71 = ro, 409 = pa, 408/608 = sa, 56/54 = po, 161 = fe, 206 = deux, 633 = magasins?, 118 = marchand, 168 = troupes?,
  417 = une?, 195 = er and où/dont, names M. Péan (pé-a-n) and M. Mercier (mé-r-ci-er) on f.347r.2-3.
- Paperwork: NOTES.md (Status: in progress), profile.json valid, catalogue entry 1392 status updated (catalogue valid),
  emgeorrk added to contributors.json, .gitignore rule for img/strips/work_nov. Nothing committed.
- Owed: second image pass on each conjectural word and unread run; frozen September-only key vs 200 shuffled tables;
  README word measure; write-up (/writeup tremais1759) and DECODE queue entry; reply on issue 810; HD scan request.
- Second pass the same day (after the Stop hook asked for the retry): two agents retried every unread run and conjectural word
  (`retry_346rv.tsv`, `retry_347rv.tsv`, new values in `*_newvalues.tsv`; 268 places: 181 sure, 64 conjectural, 23 open).
  `reading.md` rewritten: 357 sure, 92 conjectural, 25 unread runs (`count_reading.py`: 0.756 sure, 0.951 with conjectural).
  Control `control_frozen_key.py`: real key -2.424, best of 200 shuffled -2.617. `reading_en.md` written.
  Content corrections: "un commerce immense" (not fortune); "profité" (not probité); the favoured man is the munitionnaire
  (butcher's boy, 480 unconfirmed); "sans lui on" (260 275 156) is not a name; Montcalm portrait gains "un excellent jurisconsulte".
- Write-up first held for the owner, then made the same day on his word ("Publish now"): page docs/tremais1759.html, ledgers, catalogue entry 1392 removed; claims review by a separate agent, 15 findings, all applied.
