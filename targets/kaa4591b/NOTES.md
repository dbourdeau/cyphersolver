# BayHStA Kurbayern Äußeres Archiv 4591 — three ciphertexts to the Bavarian court, 1531–1537

Catalogue entry 162 ("… to unknown recipient, 3 ciphertexts"). DECODE R9403 (f.226–228), R9414 (f.257–259),
R9415 (f.260–261). Same key volume as `targets/kaa4591/` (catalogue 161, fourteen other records), kept apart because the
catalogue lists them apart. Work 21–22 Sept 2026, one session (Claude Opus 5).

Images: DECODE, login only. DECODE's rights line reads "Publishing it is only possible with the permission of the
Archive"; no permission has been asked for, so the images stay in the untracked `targets/kaa4591/r94xx/` work folders
(git-ignored) and the site page carries no image figures. Only text files are in this folder.

Outcome: **read in part** (R9403 and R9415 read; R9414 92.2%, under the 95% bar; overall 1760/1860 = 94.6%). Key state: rebuilt for all three.

## The three records

| Record | Folio | Date | Who | Language | System | Read |
|---|---|---|---|---|---|---|
| R9403 | 226–228 | Łask, 17 Sept 1531 (docket "anno 32") | Hieronymus Łaski to a councillor of the Bavarian dukes (probably Leonhard von Eck: inference) | Latin | System B (Łaski's cipher) with e/r swapped | 414/416 words, 99.5% |
| R9415 | 260–261 | 18 April 1533 (clear "Datum 18 Aprilis 33") | King John Zápolya's side to "illustrissimi principes … fratres" (the dukes); address to Aurelio Augurelio, the dukes' agent | Latin | new homophonic system "L" | 388/405 words, 95.8% strict |
| R9414 | 257–259 | Wardein (Nagyvárad), 14 March 1537 | an unnamed Bavarian servant at King John's court to Duke Ludwig of Bavaria | German | new homophonic system "G" | 958/1039 words, 92.2% strict |

## R9403 — Łaski, 17 Sept 1531: read

System B is Łaski's graphic cipher, whose key was rebuilt from glosses in `targets/kaa4591/sysB/key_from_glosses.tsv`
(R9322, R9417). Here e and r are swapped (e = ⋇ starred x, r = X plain x) and some sign shapes differ. The word
sign DAG occurs three times and is King John Zápolya ("rex", "regis").

Reading: `r9403/decoded.txt` (line by line, then normalised). Ruffus brought the dukes' letters on the 15th; Łaski
thanks them. Asked what the Turk intends: this winter the Sultan told Ferdinand's envoys there is no friendship,
peace or truce unless Hungary is given up to King John; he will come looking for Ferdinand. Preparations: ships,
guns, grain carried to the Danube, a levy of soldiers. The Speyer diet will be short; Łaski is ill but will ride
post to it; the dukes and their friends should stop any decision against the king until he comes. The king trusts
no princes in the Empire more. On the marriage he cannot yet write: in ten days he will settle it with the King of
Poland; in Poland as in France the dowering of kings' daughters is fixed by law. Postscript: put the king's letters
before the imperial estates.

Caveat: `r9403/transcription.tsv` is reading-aligned. The sign codes were written from the reading with the key
(`r9403/build.py`); homophone variants (W/HH for t, EQs/T for f) were not kept, so the sign count (2,452) is a
reconstruction. Doubtful words: ergo, ruffus, sequentes, contra, postas, constituar, nam, ub[i], dotandis, meus
(97.1% if these ten count as unread). Latin LM check: `lm.best_language` → la (−1.78) against fr (−2.64).

## R9415 — King John's side, 18 April 1533: read

Signs look like the System A′ set of `targets/kaa4591/sysA`, but the values differ: the A′ key does not fit. Key rebuilt
from the P1 l.3 gloss ("… incrementum"), then annealing with the `la` model (`r9415/solve.py`, `anneal1/2.txt`) and
a beam search (`r9415/beam.py`, `beam1.txt`); final key `r9415/key.txt`. Six join nulls (ȣ/⊙) follow the clear
passages. Reading: `r9415/reading.txt`; count `r9415/count.txt` (count.py: 405 words, 19 unread or doubtful).

Content: Georgius, the dukes' servant, came back with three reasons for their urging concord at the diet of
Pressburg; thanks. The "enemy" king (Ferdinand) opened a treaty with King John while secretly suing the Sultan for
peace; the Sultan's own letters revealed it, so John recalled his orators and sent his governor to the Sultan at his
request. Ferdinand boasts of peace but does not know its terms; the dukes should not believe the rumour. The Turkish
envoy in Vienna: his speech made Ferdinand's orator in Turkey "his" orator. Address (P4, clear) to Aurelio
Augurelio, the dukes' agent.

## R9414 — Wardein, 14 March 1537: read in part

Homophonic system "G" (own sign set). Key from the interlinear gloss over P1 l.6–8, then annealing and a beam with
the `de-1500s` model (`r9414/beam2.py`, `beam3.txt`); key `r9414/keyb.txt` plus alternatives `cp12/alt_p12.txt`.
Three visual passes over every line (`cp12/*_progress.txt`), then `r9414/gapfill.py`, a lexicon search allowing
one edit. Reading `r9414/reading_v5.txt` (v3 + two 5 Oct passes); count `python count_v2.py reading_v5.txt` → 1039 words, 958 read, 92.2%.
Dated in clear: "Datum Wardein … den vierzehenden tag Marcii anno siben und dreissigisten"; address P6 "Herzogen
Ludwigen in Bayrn".

Content: the writer's journey back into Hungary; Hungarian affairs; envoys of the pashas of (Greek) Belgrade and
Bosnia; the Turkish emperor ordering them to be ready and arming ("hundert tausent man"), to win Hungary and then
turn on Austria (the passage also names Constantinople); the Ferdinandists taking towns and villages; Duke Wilhelm never writes to him, so
he asks Ludwig to intercede, citing his service to their father; his debts and leave; mining and ore specimens;
Hans Schwab of Kraków as carrier. Postscript: "der herr Camermaister hat mein ziffer".

## Remaining gaps

- R9414 code signs without a key (about 10 words: Ψ at P2.02, 08, 09, 27; swash X at P2.15, P2.25, P4.02, P4.21; K at P4.33, probably "the king") - blocker: no-key-material; single name/word signs, no key in the volume or on DECODE
- R9414 blotted or struck signs (about 15 words) - blocker: illegible; ink blots and deletions on the DECODE images
- R9414 legible but unresolved words (about 55; candidates in gapfill.py output) - blocker: open-codes; three full image passes, sibling keys and a one-edit lexicon search done, homophone ambiguity remains
- R9415 17 unread or doubtful words (listed in r9415/count.txt) - blocker: open-codes; scattered, mostly one sign each
- R9403 P3 l.11 "[?]orator", P3 l.12 "[?]meus", small insertion on P1 l.4 - blocker: illegible; cramped signs on the image

## Escalation

- [x] siblings: R9404-R9407 and R9418-R9422 viewed (other letters or other systems); R9423 key register checked in kaa4591
- [x] clear-pages: glosses used on all three; R9415 P4 and R9414 P6 addresses are clear, the dates are clear
- [x] known-keys: System A′ (R9427 gloss key), R9368, R9369 (Augurelio's 1531 cipher) and sysB tried; only sysB fits (R9403); R9369 and A′ do not match L or G
- [x] print: web search 22 Sept 2026 (Łaski 1531 Lasci 17 Septembris, Zápolya letters to the Bavarian dukes, Augurelio) found no edition; Acta Tomiciana t. 8 (1530-32, Jagiellonian Digital Library) exists but is the Polish royal chancery's record and was not searched page by page; kaa4591 search for KAA 4591 also nothing
- [x] key-rebuild: la- and de-1500s annealing and beam search for L and G; gloss-seeded
- [x] retry: three visual passes over R9414, R9415 zoom pass 22 Sept, gapfill.py over every unread R9414 word
- [x] retry (2nd, 22 Sept 2026, from the ferdinand1619 session): a whole-word wildcard lexicon pass was written for
  R9414's 56 single-gap marks (`r9414/wildfill.py`: treat the gap as any letter, match the 171,189-type de-1500s
  lexicon, score in context). It returns nothing, and for a structural reason worth recording: every `[..1]` in
  `reading_v3.txt` is a whole unread **word**, not an unread sign inside a read word, so there is no in-word pattern
  to constrain. The per-sign version of this search is what gapfill.py already does. Short of better images, the
  ~65 unresolved words are at the limit of these scans, not of the method.
- [x] retry (3rd, 5 Oct 2026, push to 95%): every unread word of R9414 and R9415 set beside its raw decrypt
  (`decrypt_v2.txt`, `cp12/dec_*_new.txt`; R9415 `decrypt.txt`). Taken only where the decrypt itself spells the
  word: R9414 P1.34 "kopei des anstand wider von **Lunden**" (the Archbishop of Lund, Charles V's negotiator with
  King John, 1536-38), P3.04 "im lant **feind**", P2.17 "**befelch**(e)", P4.34 "**handstain**" (mining term; fits the
  ore-specimen passage); R9415 "in **re**", "omnia **ea** affirmavit". Rejected as context guesses: P1.17 "wissen",
  P3.37 "drei jar", P4.24 "red", P4.28 "sehen", R9415 "iure" (decrypt iuue), "hoc". Reading `r9414/reading_v4.txt`
  (count_v2.py: 951/1037, 91.7%); R9415 `reading.txt` (count.py: 388/405, 95.8%). Overall 1753/1858 = 94.3%,
  still under the bar: the rest of R9414 needs a fresh full-resolution sign pass on the DECODE images (not in this
  checkout's target folder) or keys for the Ψ/X/K word signs.
- [x] retry (4th, 5 Oct 2026): full-resolution image pass (3-4x crops of the DECODE images) over every non-code
  gap of R9414, sign by sign, logged per gap in `r9414/pass4.txt` (74 entries). Accepted only where the new signs
  spell the word under keyb + alternatives and the German makes sense: P1.21 "ist", P2.03 "auch er" (the gap was
  two words around them, now [..1] auch er [..1]), P3.09 "wut", P4.02 "sag, wan", P4.22 "seiner", P4.24 "red".
  "handstain" (P4.34) withdrawn: the signs give gh?an + tstain. Spelled but rejected for sense: P1.28 "ier flieget",
  P1.36 "ain", P2.34 "fur sich", P3.01 "haiter", P3.04 "amt", P3.33 "fur kindisch". Findings: P1.18/P1.25 hold the
  large Ψ code sign; a barred ∂ not in the key stands at P2.17, P2.19, P3.39, P4.21, P4.23 (a new code or letter,
  unresolved); scribal deletions at P1.20, P2.11, P2.17, P3.24, P4.15. Result `r9414/reading_v5.txt`: 958/1039,
  92.2%; overall 1760/1860 = 94.6%. Still under the bar; the remaining ~55 words fail on the signs themselves.
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
  counted. Neither sign appears in R9403, in R9415's code list (`r9415/transcription.txt` header: its crossed-stem
  # is f, a different shape), in the System B gloss key (`kaa4591/sysB/key_from_glosses.tsv`) or in sperantio1534.
  Measure unchanged: R9414 958/1039 (92.2%), overall 1760/1860 = 94.6%.

## Files

- `signstream.py` writes `r94xx/signs.txt` (one sign per token) for `docs/_check_profile.py --measure`.
- `r9403/`: build.py, transcription.tsv, decoded.txt.
- `r9415/`: transcription.txt, key*.txt, solve.py, beam.py, decrypt.txt, reading.txt, count.py/count.txt.
- `r9414/`: transcription*.txt, key*.txt, beam*, dec*, reading*.txt, count_v2.py, gapfill.py, `cp12/` pass logs.
  Crop scripts refer to image folders that are not in the repository.
