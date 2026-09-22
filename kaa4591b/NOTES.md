# BayHStA Kurbayern Äußeres Archiv 4591 — three ciphertexts to the Bavarian court, 1531–1537

Catalogue entry 162 ("… to unknown recipient, 3 ciphertexts"). DECODE R9403 (f.226–228), R9414 (f.257–259),
R9415 (f.260–261). Same key volume as `kaa4591/` (catalogue 161, fourteen other records), kept apart because the
catalogue lists them apart. Work 21–22 Sept 2026, one session (Claude Opus 5).

Images: DECODE, login only. DECODE's rights line reads "Publishing it is only possible with the permission of the
Archive"; no permission has been asked for, so the images stay in the untracked `kaa4591/r94xx/` work folders
(git-ignored) and the site page carries no image figures. Only text files are in this folder.

Outcome: **read in part** (R9403 and R9415 read; R9414 91.3%, under the 95% bar). Key state: rebuilt for all three.

## The three records

| Record | Folio | Date | Who | Language | System | Read |
|---|---|---|---|---|---|---|
| R9403 | 226–228 | Łask, 17 Sept 1531 (docket "anno 32") | Hieronymus Łaski to a councillor of the Bavarian dukes (probably Leonhard von Eck: inference) | Latin | System B (Łaski's cipher) with e/r swapped | 414/416 words, 99.5% |
| R9415 | 260–261 | 18 April 1533 (clear "Datum 18 Aprilis 33") | King John Zápolya's side to "illustrissimi principes … fratres" (the dukes); address to Aurelio Augurelio, the dukes' agent | Latin | new homophonic system "L" | 386/405 words, 95.3% strict |
| R9414 | 257–259 | Wardein (Nagyvárad), 14 March 1537 | an unnamed Bavarian servant at King John's court to Duke Ludwig of Bavaria | German | new homophonic system "G" | 947/1037 words, 91.3% strict |

## R9403 — Łaski, 17 Sept 1531: read

System B is Łaski's graphic cipher, whose key was rebuilt from glosses in `kaa4591/sysB/key_from_glosses.tsv`
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

Signs look like the System A′ set of `kaa4591/sysA`, but the values differ: the A′ key does not fit. Key rebuilt
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
one edit. Reading `r9414/reading_v3.txt`; count `python count_v2.py reading_v3.txt` → 1037 words, 947 read, 91.3%.
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
- R9414 legible but unresolved words (about 65; candidates in gapfill.py output) - blocker: open-codes; three full image passes, sibling keys and a one-edit lexicon search done, homophone ambiguity remains
- R9415 19 unread or doubtful words (listed in r9415/count.txt) - blocker: open-codes; scattered, mostly one sign each
- R9403 P3 l.11 "[?]orator", P3 l.12 "[?]meus", small insertion on P1 l.4 - blocker: illegible; cramped signs on the image

## Escalation

- [x] siblings: R9404-R9407 and R9418-R9422 viewed (other letters or other systems); R9423 key register checked in kaa4591
- [x] clear-pages: glosses used on all three; R9415 P4 and R9414 P6 addresses are clear, the dates are clear
- [x] known-keys: System A′ (R9427 gloss key), R9368, R9369 (Augurelio's 1531 cipher) and sysB tried; only sysB fits (R9403); R9369 and A′ do not match L or G
- [x] print: web search 22 Sept 2026 (Łaski 1531 Lasci 17 Septembris, Zápolya letters to the Bavarian dukes, Augurelio) found no edition; Acta Tomiciana t. 8 (1530-32, Jagiellonian Digital Library) exists but is the Polish royal chancery's record and was not searched page by page; kaa4591 search for KAA 4591 also nothing
- [x] key-rebuild: la- and de-1500s annealing and beam search for L and G; gloss-seeded
- [x] retry: three visual passes over R9414, R9415 zoom pass 22 Sept, gapfill.py over every unread R9414 word

## Files

- `signstream.py` writes `r94xx/signs.txt` (one sign per token) for `docs/_check_profile.py --measure`.
- `r9403/`: build.py, transcription.tsv, decoded.txt.
- `r9415/`: transcription.txt, key*.txt, solve.py, beam.py, decrypt.txt, reading.txt, count.py/count.txt.
- `r9414/`: transcription*.txt, key*.txt, beam*, dec*, reading*.txt, count_v2.py, gapfill.py, `cp12/` pass logs.
  Crop scripts refer to image folders that are not in the repository.
