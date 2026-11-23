# Mexican embassy, Washington, to the consul at Eagle Pass, 17 April 1917: the "clave Murciélago" telegram

Status: read in part (Andrew Beling, with AI agents, 23 Nov 2026). 26 of 37 words come out of the key uncorrected (70.3%; README 95% word bar), and 11 words carry a sender's slip read from the sense. The sentences run from end to end. The first planned test (the book's Murciélago square with list word 31) missed, and the plan's 90% letter mark was missed (64.6%). Key recovered from the cipher text alone; it turns out to be the keyword alphabet TIRANO folded on itself. No person has checked the reading; an independent reviewer, an AI agent of ours (Claude Opus 5.5, 23 Nov 2026 00:20-00:45 EST), reproduced it blind (model reading, below).

## Document

- **Archive:** AHGE-SRE (Acervo Histórico Diplomático, Secretaría de Relaciones Exteriores), Archivo de la Embajada de México en Estados Unidos, leg. 507, exp. 6. The original was **not seen**.
- **Our source:** the halftone of the telegram printed as fig. 10, p. 339, in Roberto Narváez, *Criptografía diplomática, política y militar en México (1813-1926)* (Mexico: SRE, 2019). We worked from phone photographs of a loan copy. No image is committed and none of the book's tables is reproduced here.
- **Credit:** Narváez published the telegram and its context (pp. 338-342). He says the message stayed impenetrable to the consul, and he prints no reading.
- **The sheet:** typed, headed "WASHINGTON D.C. ABRIL 17 de 1917." and addressed to "SR. JOSE M. ARREDONDO, CONSUL DE MEXICO, EAGLE PASS, TEXAS." The clear preamble reads "MENSAJE AYER CIFRADO CLAVE MUERCIELAGO REPITOSELO CLAVE TREINTAIUNO". In English: the message enciphered yesterday (16 April) in the Murciélago key, repeated to you, key thirty-one.
- **Context, from the book:** in April 1917 several consuls (Douglas, San Francisco, New Orleans, Eagle Pass, Brownsville) wrote that they could not decipher embassy telegrams. On 17 April Arredondo replied that he could not read this one "con clave Murciélago ochentaidos" (word 82 of the consular key list, p. 339). Narváez explains the confusion as consuls using the wrong key list (p. 338).
- **Historical setting:** the United States had declared war on 6 April 1917. On 13 April Wilson created the Committee on Public Information by Executive Order 2594; the formal Censorship Board came only in October 1917. The "comité censura nombrado por presidente Wilson" of a 16-17 April telegram fits that committee. The identification is the independent reviewer's.

## System and key

- **Simple substitution** with a reciprocal alphabet (`key.tsv`): A-X, B-U, C-S, D-Q, E-P, F-M, G-L, I-Z, N-W, O-V, R-Y, and T stands for itself.
- **How the key was made: the keyword alphabet TIRANO, folded.** Write TIRANO and then the rest of the alphabet in order, TIRANOBCDEFGHJKLMPQSUVWXYZ (26 letters, no Ñ), round a circle, and pair each letter with the one opposite it across the line through T: I-Z, R-Y, A-X, N-W, O-V, B-U, C-S, D-Q, E-P, F-M, G-L, H-K, with T and J standing for themselves. This reproduces `key.tsv` exactly (`work/scripts/fold_check.py`).
  - **What the telegram itself fixes:** 11 pairs (B-U, C-S, D-Q, E-P, F-M, G-L, N-W, O-V, R-Y, X-A, Z-I) and T standing for itself: 12 independent facts. (The "21 observed values" of `key.tsv` count both sides of a pair, and D, M and N were set earlier by the pairing, not by the text.)
  - **Order of work, plainly:** TIRANO was noticed by eye in the recovered pairs **before** the plan for the search was written; the search under the frozen plan (SHA-256 f6372af4..., written 10:23 EST, run 10:24-10:25) is a confirmation and a check for rivals, not a discovery. The key values themselves were fixed at 00:42, ten hours earlier, and were not changed to fit TIRANO.
  - **The search** (`work/runs/fold_test.json`): about 23,000 keywords (corpus words, the 100 words of the consular list in fig. 9, the words of our OCR of Narváez ch. IX, MURCIELAGO and the number words), 26- and 27-letter alphabets, folds about every axis and two-row pairings at every offset, 3.7 million distinct keys. TIRANO folded through T is the only fit.
  - **What the controls show:** the positive control (50 of 50 planted fold keys found) only checks that the search code works. The random control (0 of 3,000 random reciprocal keys fitted) only bounds the false-fit rate at about 0.1%. The chance that a random reciprocal key matches a given candidate on these 12 facts is about 3 in 10^14, so about 1 in 10 million over the whole search. A second independent reviewer, an AI agent of ours (Claude Opus 5.5, 23 Nov 2026 10:45-11:05 EST; a model check, not a person's), ran a wider search of its own, adding columnar-transposed keyword alphabets (11.7 million keys), and also found one fit, TIRANO; its script is not in this package.
  - **Predictions, not observations:** cipher A, H, I, J and K never occur in the telegram. A = x and I = z follow from the pairs; H = k, K = h and J = j come from the construction alone, with no check in this text.
  - TIRANO is not word 31 of the printed list (fig. 9, which runs alphabetically from Cabillo; no. 31 is Escultor) and does not appear in it. How "clave treintaiuno" points to TIRANO is not known: perhaps word 31 of the second, unprinted list.
  - The same construction underlies the 1915 "Clave Garduño" printed by Narváez (p. 311): it is the 27-letter keyword alphabet GARDUÑO (the table's own name) folded the same way; all 13 pairs and the fixed J agree. This rests on one transcription of that table (by the first AI reviewer from our photograph), which the exact fit supports. As far as our OCR of pp. 311-312 shows, the book does not name the keyword, so this observation appears to be new. The book's table is not reproduced here.
- **Unseen letters:** cipher A, H, I, J and K do not occur; their values above come only from the construction.
- **Evidence:**
  - The index of coincidence is 0.071, flat over periods 1-12. That is one alphabet, not a keyword run through the Murciélago square named in the heading.
  - The book's square with key word 31 of the printed list was tested first, under a frozen plan, and missed.
- **Cipher D, M and N** have at most one clean occurrence each:
  - D, once, in "que";
  - M, twice, but one is the doubtful position 121;
  - N, twice, but one is the extra letter in "falsas".
  
  Their values rest on the reciprocal pairing, which the other 18 letters show without exception. That is an assumption about the system.
- **Not a shifted keyword alphabet:** 3,791 keywords (including MURCIELAGO) were tried as a keyword alphabet set against the plain alphabet, both directions, all 26 offsets. The best score (-3144.2) is below every shuffled control. That test did not try folding, which is how the key was in fact made (above).
- **Against the keys printed by Narváez:**
  - not the Murciélago square (p. 333 instructions, fig. 8);
  - not the 1915 "Clave Garduño" reciprocal table (p. 311), which shares one pair, though it is built the same way from another keyword;
  - not any of the nine reciprocal rows of Seguín's 1916 plana (fig. 7, p. 326), though two rows share several pairs.
  
  It is a folded keyword alphabet of the Garduño kind, with a keyword the book does not print.
- **The book's explanation stays open.** Fig. 9 is captioned as one of two key lists. "Clave treintaiuno" could be word no. 31 of the second, unprinted list, used as the keyword of a folded alphabet. That would fit Narváez's wrong-list explanation: Arredondo tried word 82 of the printed list (Rodín). Not testable without the second list.

## Method

All work was done on 23 Nov 2026 by AI agents (Claude Opus 5.5) run by Andrew Beling. Files are in `work/`.

1. **Transcription.** Three transcriptions were made from the book photographs: `transcription_pass1.txt` (agent), `transcription_pass2.txt` (a helper given only the images, blind) and `review/blind_transcription.txt` (the independent reviewer, blind). Each has 246 letters, and they differ only at the letters listed under Transcription doubts. `transcription.txt` gives the readings used.
2. **Plan.** `work/PLAN.md` was written and hashed (`PLAN.sha256`) before the runs. It sets the hypothesis, the solver, the corpus, the controls and the pass mark: Spanish sentences over at least 90% of the letters in clean words, plus a held-out check. The order rests only on local file times: plan 00:13:01 EST, first control run 00:13:44. The evidence was opened before the plan: Andrew's photographs of the book were taken and first sorted by AI agents on 21 Nov; the telegram was first cropped at 00:00 EST on 23 Nov, the Murciélago test was planned at 00:01, and passes 1 and 2 were saved at 00:04, so this plan was written after both passes and that test had been seen.
3. **Controls first** (`work/runs/controls_summary.json`, every seed and score in `work/runs/*.tsv`):
   - three shuffles of the 246 letters scored -2964.3, -2939.3 and -2923.6, with no Spanish;
   - three 246-letter passages of real Spanish (from `targets/carranza1915`, held out of the corpus) under random keys came back 99.2%, 99.2% and 99.6% right.
   
   The method works at this length.
4. **Solve.**
   - The solver is simulated annealing on Spanish letter 4-grams built from *Archivo Santander* XIV (Internet Archive OCR) and the Spanish readings of 13 Mexican 1906-1914 targets in this repository. It used 40 restarts with fixed seeds.
   - Best scores: -2490.9 on pass 1 and -2473.7 on pass 2. That is above all shuffles and inside the range of the enciphered controls.
   - The machine key was wrong on five rare cipher letters: D, L, M, N and O. L = g and O = v come from the pass 2 solve (both well attested by their pairs: cipher G = l 9 times, cipher V = o 28 times). D, M and N were set by the reciprocal pairing and the sense.
5. **Held-out check.** The key solved on letters 1-170 reads letters 171-246 unchanged apart from the sender's slips. Cipher K at position 243 (pass 1 only) does not occur in 1-170. On pass 1 as transcribed, the tail ends "...cocprobarlo caso necmswrio".
6. **Pass mark.** The plan's 90% letter mark was **missed**: 159 of 246 letters (64.6%) are in clean words. The cause is enciphering slips spread over eleven words, not unread passages.
7. **Model reading by an independent reviewer** (`review/`). Before seeing this work, a separate AI agent of ours (Claude Opus 5.5, 23 Nov 2026 00:20-00:45 EST) made its own blind transcription and solved it with its own code (`review/my_solve.py`) and its own corpus (Spanish Wikipedia extracts, not committed). It got the same paired key and the same Spanish sentence, word for word (`review/independent_solution.txt`). It also re-ran the scripts in `work/scripts/` and reproduced every run file byte for byte. This is a model reading, not a person's.

8. **Key construction** (later on 23 Nov): see "How the key was made" above. Plan hashed before the search (order on local file times only); the plan and search script stay outside the package because they also contain tables printed in the book and read our OCR of it, so the 3.7-million-key search cannot be rerun from the committed files. Its summary with controls is `work/runs/fold_test.json`; `work/scripts/fold_check.py` checks the TIRANO fit itself.
9. **Fourth blind reading of the doubtful letters** (later on 23 Nov, `review/blind_reading_doubtful_letters.md`): a helper agent (Claude Opus, medium effort, 10:21 EST) given only a crop of the photograph read every group and closed in on the doubtful ones. It adds new doubts at positions 7, 29, 83, 129, 152, 208 and 220 (listed below); at each the reading used is that of the three earlier transcriptions, which agree. It reads position 241 as F ("probable", alternative P) and 243 as X.

10. **Statistical key validation: prepared, not run.** `validation.tsv` aligns all 246 cipher letters with the reading. The 13 marked letters carry the reading, and the extra N in "falsas" counts as a null. The repository's validator (`python docs/_validate.py eaglepass1917`) needs the `es-modern` model, which builds from Project Gutenberg texts. They are not cached on our machine, Gutenberg returned HTTP 503 at the first try, and fetching from it was outside this session's permitted sites. So the test is still owed. It does apply here: a one-alphabet key over 246 letters is within its range. It has not been marked not applicable.

To re-run, from the repository root, standard library only, under `python3 -I`: `targets/eaglepass1917/decrypt.py` rewrites `decryption.txt` unchanged (for a doubtful letter, use for example `--alt 121=N`); `targets/eaglepass1917/count_words.py` prints the strict counts of the table below (26 of 37, 159 of 246, and the three alternatives); `work/scripts/fold_check.py` checks the TIRANO fold (21 of 21); `docs/_replay.py eaglepass1917` runs the key replay. Each gave the same output in two runs on 23 Nov. The solver scripts in `work/scripts/` need numpy (so they do not run under plain `python3 -I`) and read files by absolute paths on our machine, outside the repository (the corpus, the pass 1 and pass 2 files as first saved, and the repository copy of 7d9b91fb8); the corpus is not committed. They are kept as the record of the runs, which the first reviewer reran on our machine byte for byte, and which were rerun twice more on 23 Nov (afternoon) with every committed file in `work/runs/` except `fold_test.json` coming out identical; the reading does not depend on them, only on `key.tsv`, `transcription.txt` and `decrypt.py`.

## Reading

See `reading.md` (Spanish, holes marked) and `translation.md`.

> Para {presentar} los a comité censura nombrado {por} {presidente} Wilson {necesito} mándeme mayor brevedad posible nombres {periodistas} y agentes información {que} propalan {falsas} {noticias} y agitan opinión principalmente con noticias complots {alemanes}. Debemos poder {comprobarlo} caso {necesario}.

> To present them to the censorship committee appointed by President Wilson, I need you to send me as soon as possible the names of journalists and information agents who spread false news and stir up opinion, chiefly with news of German plots. We must be able to prove it if necessary.

**Counts** (`python3 -I targets/eaglepass1917/count_words.py`).

| basis | words | letters in clean words |
|---|---|---|
| readings in `transcription.txt` | 26 / 37 (70.3%) | 159 / 246 (64.6%) |
| if position 121 is N | 25 / 37 (67.6%) | 148 / 246 (60.2%) |
| if position 241 is P (against the photographs) | 27 / 37 (73.0%) | 168 / 246 (68.3%) |
| every preferred reading of the fourth blind reading (7 F, 29 X, 129 F, 220 G) | 23 / 37 (62.2%) | 136 / 246 (55.3%) |

The repository's key replay (`python docs/_replay.py eaglepass1917`, through `replay.py`) reports "reproduces (every difference marked)": 27 of 37 words exact and 233 of 246 letters exact. Ten words are marked. It scores "falsas" as exact because it charges the extra cipher letter N to the gap beside the bracket. The strict count above charges it to the word, which gives 26 of 37.

**The slips.**
- The twelve slip letters in eleven words are what the sender typed. They show clearly on the photographs, except "por", where the letter looks typed over, and position 241 (F/P).
- Five are one pattern: plain e and t exchanged. Cipher T (= t) is typed for e three times (necesito twice, alemanes), and cipher P (= e) for t twice (presidente, periodistas). Typed P and T do not look alike, so these are not misreadings.
- The pattern may come from confusing the e and t lines of a reciprocal table (T is the only letter that stands for itself), or from the Morse E/T confusion if the draft came off a telegram. Neither can be shown from one sheet.
- The other slips: presen{t}ar (F), p{o}r (Y), pre{s}idente (S, possibly seseo), q{u}e (V), an extra N in falsas, notic{i}as (C), co{m}probarlo (S), nec{e}sario (F).

**What kind of hole each one is** (from the four readings of the photograph):
- Sender's slips, clear in all four readings: presentar (11), presidente (45, 50; 45 may be a seseo spelling rather than an enciphering slip), necesito (59, 61), periodistas (108, P or F but never T), noticias (153), alemanes (205), comprobarlo (225), falsas (142, an extra letter N).
- Sender's slip beside a mark: que (131): V is clear, and a light slash follows it, which may be a correction mark.
- **Probable** slip: necesario (241). All four readings give F, but the fourth calls it only probable, with P as the alternative, and F against P is the pair this halftone confuses most. P would make the word clean.
- **Not shown to be a slip:** por (40). The letter is overtyped, so the sender may have corrected it. What lies under it can only be seen on the archive original.
- So "sender's slip" is shown for nine holes, probable for one (241) and open for one (40). Only the archive's original of leg. 507, exp. 6 can settle 40, 131 and 241; a sharper photograph of the book might help with 241 but not with the overtyping.
- **The held-out tail.** On pass 1 the held-out key read the last word as "necmswrio". Two things cause it: pass 1 read K at 243, a letter absent from letters 1-170 (the other three readings give X, which gives a); and F at 241 is a sender's slip (m for e). With X the tail reads "necmsario", one slip.

## Transcription doubts

- [P/F] (position 7, YPCPW) - read: P; checked: image, decode, transcription; the fourth blind reading prefers F (faint); P gives "presentar". A sharper photograph could settle it.
- [Y/X] (position 29, WCBYX) - read: Y; checked: image, decode, transcription; the fourth blind reading has X; Y gives "censura".
- [S/E] (position 152, VTZSC) - read: S; checked: image, decode, transcription; faint in the fourth blind reading; S gives "noticias".
- [W/V] (position 208, TFXWP) - read: W; checked: image, decode, transcription; narrow in the fourth blind reading; W gives "alemanes".
- [Q/G] (position 220, QPYSV) - read: Q; checked: image, decode, transcription; the fourth blind reading has G; Q gives "poder".
- [Q] (position 83, OPQXQ) - read: Q; checked: image, decode, transcription; the fourth blind reading sees the letter struck over (an ink mass with a Q or O shape inside); still read Q, which gives "brevedad"; no count change.
- [P/F] (position 101, PYZVQ) - read: P; checked: image, decode, transcription; bracketed in the earlier reviewer's blind transcription and "probable" in the fourth; P gives "periodistas".
- [W/F] (position 129, SZVWDV) - read: W; checked: image, decode, transcription; the fourth blind reading has F (alternatives P, W) and says it looks overtyped; W gives "información", F would make it a hole (25 of 37).
- [P/F] (position 23, ZTPSP) - read: P; checked: image, decode, transcription; F and P alike on the halftone; the three transcriptions read P, giving "comité censura".
- [Y/X] (position 40, XQVEY) - read: Y; checked: image, decode, transcription; the letter is heavily inked, apparently typed over; neither Y nor X gives the o of "por", so the word is a hole.
- [F/P] (position 73, FPFXR) - read: F; checked: image, decode, transcription; passes 1 and 2 read F, and the reviewer changed P to F on a closer look; F gives "mándeme mayor".
- [P/F] (position 82, OPQXQ) - read: P; checked: image, decode, transcription; P gives "brevedad".
- [P/F] (position 114, RXLPW) - read: P; checked: image, decode, transcription; P gives "agentes".
- [M/N] (position 121, TPCZWM) - read: M; checked: image, decode, transcription; **unresolved**: pass 1 reads M, pass 2 and the reviewer prefer N; M gives "información", N gives "inwormación" (a hole). The counts are given both ways.
- [P/F] (position 132, after the stroke in SZVWDV/PEYV) - read: P; checked: image, decode, transcription; a closed bowl on the closer zoom (reviewer); P gives "que".
- [E/B] (position 136, EXGXW) - read: E; checked: image, decode, transcription; E gives "propalan".
- [M/H] (position 141, MNX) - read: M; checked: image, decode, transcription; M gives the f of "falsas"; the N after it is an extra letter.
- [G/C] (positions 144, 232) - read: G; checked: image, decode, transcription; G gives "falsas" and "comprobarlo".
- [F/P] (position 241, SFCXY) - read: F; checked: image, decode, transcription; all three transcriptions read F, which gives "necmsario" (a hole); P would give "necesario". Kept as F because the photographs show F.
- [X/K] (position 243, SFCXY) - read: X; checked: image, decode, transcription; pass 2 and the reviewer read X and pass 1 read K; the letter looks like X over K.
- [Z/E] (position 245, ZV) - read: Z; checked: image, decode, transcription; Z gives "necesario".
- [/] (between positions 131 and 132, SZVWDV/PEYV) - read: not a letter, dropped; checked: image, decode, transcription; a thin slanted stroke, lighter than the type, in all four readings; typed or pen, and whether it marks a correction, not settled.


## Related

- **Lobo to Bonillas** (F. J. Lobo, Clifton, 25 Nov 1916 or 1917, same file, Narváez fig. 14, in our lead sweep, pull request 902) uses a different system. Its index of coincidence is 0.047-0.048, and this key applied unchanged gives no Spanish.

## Remaining gaps

One line per piece that is not read letter for letter from the key, with its blocker.

- Position 40, "por" (overtyped letter) - blocker: needs-physical-access; the letter is typed over, and whether the sender corrected it can only be seen on the archive original (AHGE-SRE, AEMEUA leg. 507, exp. 6); the book prints a halftone.
- Positions 121, 129 and 241 and the other doubtful letters listed under Transcription doubts - blocker: needs-physical-access; F/P, M/N and W/F are at the limit of the book's halftone, so a sharper photograph of the book cannot settle them; only the archive's image can.
- The nine sender's slips (presentar, presidente, necesito, periodistas, que, falsas, noticias, alemanes, comprobarlo) - blocker: needs-physical-access; they read from the sense and are clear on all four readings of the photograph; only the original can confirm that the sender typed them so, rather than the halftone misleading us.
- How "clave treintaiuno" leads to the keyword TIRANO - blocker: needs-physical-access; the second key list, which may hold TIRANO as no. 31, is in the same file and is not printed.

Not gaps in the reading, but open: cipher H, J and K never occur, so their values (k, j, h) are predictions from the TIRANO construction only.

## Escalation

- [x] siblings: the other items of the same file that the book prints were opened from our photographs. Lobo to Bonillas (fig. 14, pull request 902) is a different system (index of coincidence 0.047; this key gives no Spanish). Arredondo's reply (fig. 11) is in clear. The 16 April original, the consuls' complaints and the two key lists are in leg. 507, exp. 6 and need the archive. US intercepts of 1917 embassy-consular traffic (NARA M1194, M1085) were not searched.
- [x] clear-pages: checked the clear heading and address on the sheet, and the book's pp. 338-342 (the consuls' complaints, figs. 11-13). None holds a decipherment, and Narváez prints no reading.
- [x] known-keys: tried every key we hold for this series and decade.
  - The Murciélago square with list word 31 (Escultor), under a frozen plan: missed. Word 82 (Rodín) does not fit either, since the index of coincidence is flat.
  - The 1915 Clave Garduño (p. 311): only one pair is shared, but the table is built the same way from the keyword GARDUÑO.
  - Seguín's 1916 plana (fig. 7, nine rows): no row matches.
  - Every `key*.tsv` in the repository at 7d9b91fb8 was scanned for reciprocal letter keys: none is a Mexican key of 1913-1917.
- [x] print: searched Narváez 2019 (our OCR of pp. 311-345 and the photographs of pp. 338-345) and found no reading. The repository's catalogue, leads and `known.py` have no entry. Narváez's 2025 *Historia Mexicana* article was checked, and web searches for the telegram's phrases found nothing (first review, 23 Nov). Cryptiana and Lasry's list were not checked.
- [x] key-rebuild: the key was extended from what reads. The rare letters D, M and N were set by the reciprocal pairing. The whole alphabet was then rebuilt from the keyword construction (TIRANO folded), which predicts H, J and K (`work/scripts/fold_check.py`, `work/runs/fold_test.json`).
- [x] retry: every hole and doubtful letter was re-read in four readings of the photograph (two blind ones among them) and regraded with the full key on 23 Nov.
  - No hole closes.
  - K at 243 would give h, which makes no word, so X (= a) is kept.
  - The counts under the alternative readings are given above.
- Next step outside this session: ask AHGE-SRE for images of leg. 507, exp. 6 (this telegram, the 16 April original, the two key lists, the consuls' complaints and the Lobo telegrams).

## Files

- `transcription.txt` (readings used, doubts marked), `transcription_pass1.txt`, `transcription_pass2.txt`
- `key.tsv`, `decrypt.py`, `decryption.txt`, `count_words.py` (strict counts), `reading.md`, `translation.md`, `profile.json`
- `work/PLAN.md`, `work/PLAN.sha256`, `work/scripts/` (solver, controls, keyword test), `work/runs/` (every seed and score; `keyword_test.json`)
- `review/` (the independent reviewer's blind transcription, solution and solver; `blind_reading_doubtful_letters.md`, the fourth blind reading)
- `work/scripts/fold_check.py`, `work/runs/fold_test.json` (the key construction)
- `SHA256SUMS` (paths relative to this folder)
