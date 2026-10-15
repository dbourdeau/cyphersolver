# A Bavarian servant at Wardein to Duke Ludwig of Bavaria, 14 March 1537 (BayHStA KAA 4591 ff.257–259, DECODE R9414)

Split on 15 Oct 2026 from `targets/kaa4591b/` under the one-key rule (George Lasry, 14 Oct 2026). Catalogue entry 162
("… to unknown recipient, 3 ciphertexts") grouped three letters of the Bavarian key volume in three ciphers. This one
is in a homophonic alphabet ("system G") of its own. The other two are different ciphers, each with its own page:
R9403 is in Łaski's System B ([`targets/kaa4591b/`](../kaa4591b/NOTES.md), now with the other System B letters) and R9415
is in system L ([`targets/sperantio1534/`](../sperantio1534/NOTES.md), the key of the Sperantio file). Work 21–22 Sept
and 5 Oct 2026 (Claude Opus 5), as part of kaa4591b; files moved here unchanged (`r9414/`, `validation.tsv`,
`mk_validation.py`; `signstream.py` trimmed to this record).

Images: DECODE, login only. DECODE's rights line reads "Publishing it is only possible with the permission of the
Archive"; no permission has been asked for, so the images stay untracked and the site page carries no image figures.

Outcome: **key recovered based on adjacent plaintext, read in part**: 958 of 1,039 words (92.2%), under the 95% bar.
Key state: partial (homophones with alternatives; the Ψ, swash X and K word signs have no key).

## The letter

| Record | Folio | Date | Who | Language | System | Read |
|---|---|---|---|---|---|---|
| R9414 | 257–259 | Wardein (Nagyvárad), 14 March 1537 | an unnamed Bavarian servant at King John's court to Duke Ludwig of Bavaria | German | homophonic system "G" | 958/1039 words, 92.2% strict |

Homophonic system "G" (own sign set). Key from the interlinear gloss over P1 l.6–8, then annealing and a beam with
the `de-1500s` model (`r9414/beam2.py`, `beam3.txt`); key `r9414/keyb.txt` plus alternatives `cp12/alt_p12.txt`.
Three visual passes over every line (`cp12/*_progress.txt`), then `r9414/gapfill.py`, a lexicon search allowing
one edit. Reading `r9414/reading_v5.txt` (v3 + two 5 Oct passes); count `python count_v2.py reading_v5.txt` → 1039 words, 958 read, 92.2%.
Dated in clear: "Datum Wardein … den vierzehenden tag Marcii anno siben und dreissigisten"; address P6 "Herzogen
Ludwigen in Bayrn". The signs look nothing like System B; R9369 (Augurelio's 1531 key) and the System A′ key were
tried and do not fit.

Content: the writer's journey back into Hungary; Hungarian affairs; envoys of the pashas of (Greek) Belgrade and
Bosnia; the Turkish emperor ordering them to be ready and arming ("hundert tausent man"), to win Hungary and then
turn on Austria (the passage also names Constantinople); the Ferdinandists taking towns and villages; Duke Wilhelm never writes to him, so
he asks Ludwig to intercede, citing his service to their father; his debts and leave; mining and ore specimens;
Hans Schwab of Kraków as carrier. Postscript: "der herr Camermaister hat mein ziffer".

Statistical validation (`mk_validation.py` → `validation.tsv`, R9414 only, `de-1500s`): pass (11 Oct 2026; reading
−2.249 per letter against random keys −6.676 and shuffled refits −3.639).

## Remaining gaps

- code signs without a key (about 10 words: Ψ at P2.02, 08, 09, 27; swash X at P2.15, P2.25, P4.02, P4.21; K at P4.33, probably "the king") - blocker: no-key-material; single name/word signs, no key in the volume or on DECODE
- blotted or struck signs (about 15 words) - blocker: illegible; ink blots and deletions on the DECODE images
- legible but unresolved words (about 55; candidates in gapfill.py output) - blocker: open-codes; four full image passes, sibling keys and a one-edit lexicon search done, homophone ambiguity remains

## Escalation

- [x] siblings: R9404-R9407 and R9418-R9422 viewed (other letters or other systems); R9423 key register checked in kaa4591
- [x] clear-pages: the gloss over P1 l.6-8 seeded the key; the opening, date and P6 address are clear
- [x] known-keys: System A′ (R9427 gloss key), R9369 (Augurelio's 1531 cipher), System B and system L tried; none matches G
- [x] print: web search 22 Sept 2026 (Zápolya letters to the Bavarian dukes, Augurelio, Wardein 1537) found no edition
- [x] key-rebuild: de-1500s annealing and beam search, gloss-seeded
- [x] retry: three visual passes over R9414 and gapfill.py over every unread word (22 Sept 2026)
- [x] retry (2nd, 22 Sept 2026, from the ferdinand1619 session): a whole-word wildcard lexicon pass was written for
  the 56 single-gap marks (`r9414/wildfill.py`: treat the gap as any letter, match the 171,189-type de-1500s
  lexicon, score in context). It returns nothing, and for a structural reason worth recording: every `[..1]` in
  `reading_v3.txt` is a whole unread **word**, not an unread sign inside a read word, so there is no in-word pattern
  to constrain. The per-sign version of this search is what gapfill.py already does. Short of better images, the
  ~65 unresolved words are at the limit of these scans, not of the method.
- [x] retry (3rd, 5 Oct 2026, push to 95%): every unread word set beside its raw decrypt (`decrypt_v2.txt`,
  `cp12/dec_*_new.txt`). Taken only where the decrypt itself spells the word: P1.34 "kopei des anstand wider von
  **Lunden**" (the Archbishop of Lund, Charles V's negotiator with King John, 1536-38), P3.04 "im lant **feind**",
  P2.17 "**befelch**(e)", P4.34 "**handstain**" (mining term; fits the ore-specimen passage). Rejected as context
  guesses: P1.17 "wissen", P3.37 "drei jar", P4.24 "red", P4.28 "sehen". Reading `r9414/reading_v4.txt` (count_v2.py:
  951/1037, 91.7%).
- [x] retry (4th, 5 Oct 2026): full-resolution image pass (3-4x crops of the DECODE images) over every non-code
  gap, sign by sign, logged per gap in `r9414/pass4.txt` (74 entries). Accepted only where the new signs
  spell the word under keyb + alternatives and the German makes sense: P1.21 "ist", P2.03 "auch er" (the gap was
  two words around them, now [..1] auch er [..1]), P3.09 "wut", P4.02 "sag, wan", P4.22 "seiner", P4.24 "red".
  "handstain" (P4.34) withdrawn: the signs give gh?an + tstain. Spelled but rejected for sense: P1.28 "ier flieget",
  P1.36 "ain", P2.34 "fur sich", P3.01 "haiter", P3.04 "amt", P3.33 "fur kindisch". Findings: P1.18/P1.25 hold the
  large Ψ code sign; a barred ∂ not in the key stands at P2.17, P2.19, P3.39, P4.21, P4.23 (a new code or letter,
  unresolved); scribal deletions at P1.20, P2.11, P2.17, P3.24, P4.15. Result `r9414/reading_v5.txt`: 958/1039,
  92.2%. Still under the bar; the remaining ~55 words fail on the signs themselves.
- [x] joint solve of the two unkeyed signs (5 Oct 2026). Barred ∂ (∂ with a bar through the stem), five places:
  P2.17 line start before "befelche sich" (followed by a struck run), P2.19 after clear "otto" before "so wern eur
  F.G. sehen", P3.39 after clear "iij" before "n monat", P4.21 before "uon" + swash X + "kainen", P4.23 after clear
  "dann ich beger" before "urlaub". Scored with `de-1500s` over all 22 letters and 23 digraphs/short words (da, de,
  den, der, dem, das, ver, und, zu, an, ain, von, dar, des …) summed over the five places: every value scores below
  leaving the sign out (best t −41, s −45, z −48, er/ver −50, d −58 nats total); no value makes sense in all five
  (da gives "davon" at P4.21 but "beger da urlaub" at P4.23; den the reverse). Best fit is a null or abbreviation/
  deletion mark, which adds no read words; not accepted. Large Ψ code (P1.18 "von Ψ in meinem namen geschriben",
  P1.25 "dieweil sein Ψ mit eur F.G.", also P2.02, 08, 09, 27): a word sign; "Mt." (the King's Majesty) fits
  P1.18, P1.25, P2.09, P2.27 but is strained at P2.02/P2.08, and a word sign can only be had from context, so not
  counted. Neither sign appears in R9403, in R9415's code list (`sperantio1534/r9415/transcription.txt` header: its
  crossed-stem # is f, a different shape), in the System B gloss key (`kaa4591b/sysB/key_from_glosses.tsv`) or in
  sperantio1534. Measure unchanged: 958/1039 (92.2%).

## Files

- `signstream.py` writes `r9414/signs.txt` (one sign per token) for `docs/_check_profile.py --measure` (4,675 signs).
- `r9414/`: transcription*.txt, key*.txt, beam*, dec*, reading*.txt, count_v2.py, gapfill.py, `cp12/` pass logs.
  Crop scripts refer to image folders that are not in the repository.
- `mk_validation.py` → `validation.tsv`.
